"""Assessor evidence extraction only. Does not grade or modify native subjects."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def acquire(subject_path):
    subject_path = Path(subject_path).resolve()
    subject = json.loads(subject_path.read_text())
    install = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.1')
    report = {
        'kind': 'independent-native-comparison-mechanical-evidence',
        'subject': {'path': str(subject_path), 'sha256': digest(subject_path)},
        'semantic_verdict': 'not computed by this script',
        'installed_source': {
            'path': str(install),
            'manifest_sha256': digest(install / 'manifest.json'),
            'standards': {str(p.relative_to(install / 'standards')): digest(p)
                          for p in sorted((install / 'standards').rglob('*')) if p.is_file()},
        },
        'contexts': [],
    }
    inventories = []
    for context in subject['contexts']:
        worksite = Path(context['worksite'])
        evidence = worksite.parent / 'evidence'
        inventory = json.loads(Path(context['frozen_inputs']['path']).read_text())
        inventories.append(inventory)
        mismatches = []
        for relative, expected in inventory.items():
            path = worksite / relative
            if expected['type'] == 'symlink':
                valid = path.is_symlink() and str(path.readlink()) == expected['target']
            else:
                valid = path.is_file() and digest(path) == expected['sha256']
            if not valid:
                mismatches.append(relative)
        source_root = worksite / 'native/stdo-store/releases/v2.5.1-rc.1/standards'
        source_mismatches = [str(p.relative_to(source_root)) for p in source_root.rglob('*')
                             if p.is_file() and p.read_bytes() !=
                             (install / 'standards' / p.relative_to(source_root)).read_bytes()]
        trace_path = evidence / 'stdout.jsonl'
        events = [json.loads(line) for line in trace_path.read_text().splitlines()]
        calls = []
        joins = []
        errors = []
        final = (evidence / 'final.txt').read_text()
        try:
            final_object = json.loads(final)
            final_presentation = 'bare JSON'
        except ValueError:
            fenced = re.search(r'```json\n([\s\S]+?)\n```', final)
            final_object = json.loads(fenced[1]) if fenced else None
            final_presentation = 'fenced JSON' if fenced else 'non-JSON'
        for line_number, event in enumerate(events, 1):
            message = event.get('message', {})
            for block in message.get('content', []) if isinstance(message, dict) else []:
                if block.get('type') == 'tool_result' and block.get('is_error'):
                    errors.append({'line': line_number, 'tool_id': block.get('tool_use_id'),
                                   'content': block.get('content')})
                if block.get('type') != 'tool_use':
                    continue
                calls.append({'line': line_number, 'tool': block['name'], 'id': block['id'],
                              'input': block['input']})
                command = block['input'].get('command', '')
                if ' join --input /dev/stdin ' not in command:
                    continue
                match = re.search(r"<<'EOF'[^\n]*\n([\s\S]+?)\nEOF", command)
                if not match:
                    continue
                rows = json.loads(match[1])
                law = '\n\n'.join(row['label'] + '\n' + row['text'] for row in rows)
                command_result = subprocess.run(
                    ['python3', '-B', str(worksite / 'native/axiom_indexer/build_tenants/core/code/ac.py'),
                     'join', '--input', '/dev/stdin'],
                    input=json.dumps(rows), text=True, capture_output=True,
                    env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, check=False)
                returned = final_object.get('joined_request') if final_object else None
                if isinstance(returned, dict):
                    returned = returned.get('stdout')
                if returned == 'See fenced block':
                    returned = re.search(r'```text\n([\s\S]+?)\n```', final)[1]
                joins.append({
                    'trace_line': line_number, 'tool_id': block['id'],
                    'exact_trace_input': match[1], 'rows': rows,
                    'trace_input_sha256': hashlib.sha256(match[1].encode()).hexdigest(),
                    'replay_exit': command_result.returncode,
                    'replay_stderr': command_result.stderr,
                    'replay_equals_join_law': command_result.stdout == law,
                    'returned_text_equals_replay': returned == command_result.stdout,
                    'stdout_sha256': hashlib.sha256(command_result.stdout.encode()).hexdigest(),
                    'stdout': command_result.stdout,
                })
        report['contexts'].append({
            'name': context['name'], 'worksite': str(worksite),
            'model_configuration': context['model_configuration'],
            'inventory_entries': len(inventory), 'inventory_mismatches': mismatches,
            'source_member_count': sum(p.is_file() for p in source_root.rglob('*')),
            'source_mismatches': source_mismatches,
            'evidence_hash_mismatches': [row['path'] for row in context['evidence']
                                         if digest(row['path']) != row['sha256']],
            'before_after_inventory_equal': (evidence / 'snapshot-before.json').read_bytes() ==
                                             (evidence / 'snapshot-after.json').read_bytes(),
            'final_presentation': final_presentation,
            'handoff_sections_type': type(final_object.get('handoff_sections')).__name__ if final_object else None,
            'final_sha256': digest(evidence / 'final.txt'),
            'tool_calls': calls, 'tool_errors': errors, 'join_replays': joins,
        })
    if len(inventories) == 2:
        left, right = inventories
        report['input_comparison'] = {
            'changed_shared_paths': sorted(p for p in left.keys() & right.keys() if left[p] != right[p]),
            'source_only_paths': sorted(left.keys() - right.keys()),
            'map_only_paths': sorted(right.keys() - left.keys()),
        }
    return report


if __name__ == '__main__':
    result = acquire(sys.argv[1])
    target = Path(sys.argv[2]).resolve()
    if target.parent != Path(__file__).resolve().parent:
        raise SystemExit('Report output must remain in the delegated native-review territory')
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'output': str(target), 'sha256': digest(target),
                      'contexts': [r['name'] for r in result['contexts']]}))
