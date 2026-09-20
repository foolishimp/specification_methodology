"""Extract the closed Codex records without interpreting or repairing them."""
from pathlib import Path
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys

from acquire_comparison_evidence import acquire, digest


subject_path = Path(sys.argv[1]).resolve()
subject = json.loads(subject_path.read_text())
result = acquire(subject_path)
for context, observed in zip(subject['contexts'], result['contexts']):
    worksite = Path(context['worksite'])
    evidence = worksite.parent / 'evidence'
    events = [json.loads(line) for line in (evidence / 'stdout.jsonl').read_text().splitlines()]
    final = json.loads((evidence / 'final.txt').read_text())
    for number, event in enumerate(events, 1):
        item = event.get('item', {})
        if item.get('type') != 'command_execution':
            continue
        if event['type'] == 'item.completed' and item.get('exit_code') not in (None, 0):
            observed['tool_errors'].append({'line': number, 'id': item['id'],
                                           'exit': item['exit_code'],
                                           'output': item.get('aggregated_output')})
        if event['type'] != 'item.started':
            continue
        command = shlex.split(item['command'])[-1]
        observed['tool_calls'].append({'line': number, 'id': item['id'],
                                       'command': item['command']})
        if 'join --input /dev/stdin' not in command:
            continue
        if command.startswith('printf '):
            native_input = shlex.split(command)[2]
        else:
            marker = re.search(r"<<'([^']+)'\n", command)
            native_input = command[marker.end():].rsplit('\n' + marker[1], 1)[0]
        rows = json.loads(native_input)
        replay = subprocess.run(
            ['python3', '-B', str(worksite / 'native/axiom_indexer/build_tenants/core/code/ac.py'),
             'join', '--input', '/dev/stdin'],
            input=json.dumps(rows), text=True, capture_output=True,
            env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, check=False)
        actual = next(record['item']['aggregated_output'] for record in events
                      if record.get('type') == 'item.completed'
                      and record.get('item', {}).get('id') == item['id'])
        observed['join_replays'].append({
            'trace_line': number, 'tool_id': item['id'],
            'exact_trace_input': native_input, 'rows': rows,
            'trace_rows_equal_final': rows == final['handoff_sections'],
            'replay_exit': replay.returncode, 'replay_stderr': replay.stderr,
            'replay_equals_join_law': replay.stdout == '\n\n'.join(row['label'] + '\n' + row['text'] for row in rows),
            'returned_text_equals_replay': final['joined_request'] == replay.stdout,
            'trace_stdout_equals_final': actual == final['joined_request'],
            'stdout_sha256': hashlib.sha256(replay.stdout.encode()).hexdigest(),
            'stdout': replay.stdout,
        })
    execution = json.loads((evidence / 'execution-result.json').read_text())
    observed['nonsemantic_transport_equal'] = execution['nonsemantic_transport_before'] == execution['nonsemantic_transport_after']
result['prior_transport'] = subject['prior_transport']
target = Path(sys.argv[2]).resolve()
if target.parent != Path(__file__).resolve().parent:
    raise SystemExit('Report output must remain in the delegated native-review territory')
target.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'output': str(target), 'sha256': digest(target),
                  'join_matches': [r['join_replays'][0]['returned_text_equals_replay'] for r in result['contexts']]}))
