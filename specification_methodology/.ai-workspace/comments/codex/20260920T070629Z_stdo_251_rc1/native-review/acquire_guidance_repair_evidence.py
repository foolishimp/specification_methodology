"""Record facts from closed changed-guidance observations; no semantic grading.

Only the explicit output path in this script's report territory is written.
Native joins are replayed on stdin/stdout against their frozen executable.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys

from acquire_comparison_evidence import acquire, digest


def read_final(path):
    text = Path(path).read_text()
    try:
        return json.loads(text)
    except ValueError:
        return json.loads(re.search(r'```json\n([\s\S]+?)\n```', text)[1])


def reference_checks(value):
    rows = []
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'sha256' in value:
            path = Path(value['path'])
            if path.is_absolute():
                rows.append({'path': str(path), 'expected': value['sha256'],
                             'actual': digest(path), 'match': digest(path) == value['sha256']})
        for child in value.values():
            rows.extend(reference_checks(child))
    elif isinstance(value, list):
        for child in value:
            rows.extend(reference_checks(child))
    return rows


def compare_inventory(left_path, right_path):
    left = json.loads(Path(left_path).read_text())
    right = json.loads(Path(right_path).read_text())
    return {
        'changed_shared_paths': sorted(k for k in left.keys() & right.keys() if left[k] != right[k]),
        'left_only_paths': sorted(left.keys() - right.keys()),
        'right_only_paths': sorted(right.keys() - left.keys()),
    }


def acquire_changed(subject_path):
    subject_path = Path(subject_path).resolve()
    subject = json.loads(subject_path.read_text())
    result = acquire(subject_path)
    result['kind'] = 'independent-changed-guidance-mechanical-evidence'
    result['reference_hash_checks'] = reference_checks(subject)
    original = json.loads(Path(subject['original_pair']['path']).read_text())
    original_map = next(c for c in original['contexts'] if c['presentation'] == 'map-first')
    changed_map = next(c for c in subject['contexts'] if c['presentation'] == 'map-first')
    result['changed_map_vs_original_map'] = compare_inventory(
        original_map['frozen_inputs']['path'], changed_map['frozen_inputs']['path'])
    result['fixed_source_context_equals_original'] = (
        next(c for c in original['contexts'] if c['presentation'] == 'source') ==
        next(c for c in subject['contexts'] if c['presentation'] == 'source'))
    for context, observed in zip(subject['contexts'], result['contexts']):
        worksite = Path(context['worksite'])
        evidence = worksite.parent / 'evidence'
        events = [json.loads(line) for line in (evidence / 'stdout.jsonl').read_text().splitlines()]
        final = read_final(evidence / 'final.txt')
        observed['join_replays'] = []
        if context['host'] == 'codex':
            observed['tool_calls'] = []
            observed['tool_errors'] = []
        for line_number, event in enumerate(events, 1):
            if context['host'] == 'claude':
                blocks = event.get('message', {}).get('content', [])
                candidates = [b for b in blocks if b.get('type') == 'tool_use']
            else:
                item = event.get('item', {})
                if item.get('type') != 'command_execution':
                    continue
                if event['type'] == 'item.completed' and item.get('exit_code') not in (None, 0):
                    observed['tool_errors'].append({'line': line_number, 'id': item['id'],
                                                   'exit': item['exit_code'],
                                                   'output': item.get('aggregated_output')})
                if event['type'] != 'item.started':
                    continue
                observed['tool_calls'].append({'line': line_number, 'id': item['id'],
                                               'command': item['command']})
                candidates = [{'id': item['id'], 'input': {'command': shlex.split(item['command'])[-1]}}]
            for candidate in candidates:
                command = candidate.get('input', {}).get('command', '')
                if 'join --input /dev/stdin' not in command:
                    continue
                if command.startswith('printf '):
                    native_input = shlex.split(command)[2]
                else:
                    marker = re.search(r"<<'([^']+)'[^\n]*\n", command)
                    if not marker:
                        raise ValueError('Unrecognized actual native join input at line ' + str(line_number))
                    native_input = command[marker.end():].split('\n' + marker[1], 1)[0]
                rows = json.loads(native_input)
                replay = subprocess.run(
                    ['python3', '-B', str(worksite / 'native/axiom_indexer/build_tenants/core/code/ac.py'),
                     'join', '--input', '/dev/stdin'], input=json.dumps(rows), text=True,
                    capture_output=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, check=False)
                if context['host'] == 'codex':
                    result_event = next((n, e['item']) for n, e in enumerate(events, 1)
                                        if e.get('type') == 'item.completed' and
                                        e.get('item', {}).get('id') == candidate['id'])
                    actual = result_event[1]['aggregated_output']
                else:
                    result_event = next((n, b) for n, e in enumerate(events, 1)
                                        for b in e.get('message', {}).get('content', [])
                                        if b.get('type') == 'tool_result' and
                                        b.get('tool_use_id') == candidate['id'])
                    actual = result_event[1]['content']
                returned = final.get('joined_request')
                if isinstance(returned, dict):
                    returned = returned.get('stdout')
                if returned == 'See fenced block':
                    returned = re.search(r'```text\n([\s\S]+?)\n```',
                                         (evidence / 'final.txt').read_text())[1]
                actual_index = actual.find(replay.stdout) if replay.stdout else -1
                observed['join_replays'].append({
                    'trace_line': line_number, 'tool_id': candidate['id'],
                    'trace_result_line': result_event[0], 'exact_trace_input': native_input,
                    'trace_input_sha256': hashlib.sha256(native_input.encode()).hexdigest(),
                    'rows': rows, 'trace_rows_equal_final': rows == final.get('handoff_sections'),
                    'replay_exit': replay.returncode, 'replay_stderr': replay.stderr,
                    'replay_equals_join_law': replay.stdout == '\n\n'.join(r['label'] + '\n' + r['text'] for r in rows),
                    'returned_text_equals_replay': returned == replay.stdout,
                    'trace_tool_result_contains_exact_stdout': actual_index >= 0,
                    'trace_tool_result_prefix': actual[:actual_index] if actual_index >= 0 else None,
                    'trace_tool_result_suffix': actual[actual_index + len(replay.stdout):] if actual_index >= 0 else None,
                    'stdout_sha256': hashlib.sha256(replay.stdout.encode()).hexdigest(),
                    'stdout': replay.stdout,
                })
        execution = json.loads((evidence / 'execution-result.json').read_text())
        observed['process_exit'] = execution['exit_code']
        if 'nonsemantic_transport_before' in execution:
            observed['nonsemantic_transport_equal'] = (
                execution['nonsemantic_transport_before'] == execution['nonsemantic_transport_after'])
    return result


if __name__ == '__main__':
    result = acquire_changed(sys.argv[1])
    target = Path(sys.argv[2]).resolve()
    if target.parent != Path(__file__).resolve().parent:
        raise SystemExit('Output must remain within native-review/')
    if target.exists():
        raise SystemExit('Do not overwrite a closed evidence record')
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'output': str(target), 'sha256': digest(target),
                      'contexts': [{'name': c['name'], 'joins': len(c['join_replays']),
                                    'final_matches_last_join': c['join_replays'][-1]['returned_text_equals_replay']}
                                   for c in result['contexts']]}))
