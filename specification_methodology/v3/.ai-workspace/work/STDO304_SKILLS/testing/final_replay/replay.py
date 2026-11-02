"""No-model replay of every retained successful native reader invocation."""
import hashlib
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
TESTING = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'stack_release.json').exists())
EXPECTED = '86afcb8a1d9e0d73297414fc935125dfb107f3cfad732be4694ec96ce8ce8c2b'


def sha(raw): return hashlib.sha256(raw).hexdigest()
def save(path, value): path.write_text(json.dumps(value, indent=2) + '\n')


raw = (TESTING.parent / 'SOURCE_FREEZE.json').read_bytes()
assert sha(raw) == EXPECTED
freeze = json.loads(raw)
for row in freeze['payload'] + freeze['support']:
    data = (REPO / row['path']).read_bytes()
    assert len(data) == row['bytes'] and sha(data) == row['sha256'], row['path']
(HERE / 'SOURCE_FREEZE.json').write_bytes(raw)
previous = json.loads((TESTING / 'successor4/SOURCE_FREEZE.json').read_text())
old = {row['path']: row for row in previous['payload'] + previous['support']}
delta = [row['path'] for row in freeze['payload'] + freeze['support'] if old.get(row['path'], {}).get('sha256') != row['sha256']]
assert set(delta) == {
    'specification_methodology/v3/build_tenants/common/plugins/spec/scripts/read_basis.py',
    'specification_methodology/v3/build_tenants/common-tools/test_skill_source_reader.py',
}
temporary = Path(tempfile.mkdtemp(prefix='stdo304-final-replay-', dir='/private/tmp'))
candidate = temporary / 'candidate'
shutil.copytree(REPO / freeze['candidate_root'], candidate)
reader = candidate / 'plugins/spec/scripts/read_basis.py'
meta = json.loads((TESTING / 'successor4/FIXTURES.json').read_text())
inputs = []
for directory in ('successor', 'successor3', 'successor4'):
    for run in sorted((TESTING / directory / 'runs').iterdir()):
        records = json.loads((run / 'TOOLS.json').read_text())
        results = {row['tool_result_id']: row for row in records if 'tool_result_id' in row}
        for row in records:
            command = row.get('command') or (row.get('input', {}).get('command') if row.get('tool') == 'Bash' else '')
            if not command or '/scripts/read_basis.py ' not in command: continue
            if 'command' in row:
                if row.get('exit_code') != 0: continue
                outer = shlex.split(command)
                if len(outer) != 3 or outer[:2] != ['/bin/zsh', '-lc']: continue
                command, output = outer[2], row['output']
            else:
                result = results.get(row.get('id'), {})
                if result.get('is_error'): continue
                output = result.get('output', '')
            try: expected = json.loads(output)
            except (ValueError, TypeError): continue
            if expected.get('status') != 'checked': continue
            argv = shlex.split(command)
            if argv[:2] != [meta['python'], '-B'] or argv[3] not in ('check', 'read'): continue
            assert argv[2].endswith('/candidate/plugins/spec/scripts/read_basis.py')
            assert all(a not in (';', '&&', '|', '>', '<') for a in argv)
            original = list(argv); argv[2] = str(reader)
            inputs.append((str(run.relative_to(TESTING)), row['line'], original, argv, expected))
repro = json.loads((TESTING / 'successor3/EF03_REPRO.json').read_text())
original = shlex.split(repro['gate_checks'][1]['command']); argv = list(original); argv[2] = str(reader)
inputs.append(('successor3/EF03_REPRO', None, original, argv, repro['reader_result']))
rows = []
for origin, line, original, argv, expected in inputs:
    result = subprocess.run(argv, capture_output=True, text=True, timeout=30)
    value = json.loads(result.stdout)
    row = {'origin': origin, 'trace_line': line, 'original_argv': original, 'successor_argv': argv,
           'exit': result.returncode, 'exact_result_object_equal': expected == value,
           'result': value, 'expected_result_sha256': sha(json.dumps(expected, sort_keys=True).encode()),
           'actual_result_sha256': sha(json.dumps(value, sort_keys=True).encode())}
    rows.append(row)
    assert result.returncode == 0 and value['status'] == 'checked' and row['exact_result_object_equal'], (origin, line)
save(HERE / 'ACTUAL_INPUT_REPLAY.json', rows)
for row in freeze['payload']:
    relative = Path(row['path']).relative_to(freeze['candidate_root'])
    assert sha((candidate / relative).read_bytes()) == row['sha256'], str(relative)
save(HERE / 'IMPACT.json', {'native_subject_freeze': sha((TESTING / 'successor4/SOURCE_FREEZE.json').read_bytes()),
     'successor_freeze': EXPECTED, 'changed_technical_inputs': delta, 'copied_candidate': str(candidate),
     'candidate_payload_pins_verified': len(freeze['payload']), 'helper_inputs_replayed': len(rows),
     'direct_inputs': sum(r['origin'] == 'successor/runs/direct' for r in rows),
     'native_final_inputs': sum(r['origin'].startswith('successor4/runs/') for r in rows),
     'all_result_objects_identical': True, 'new_actor_sessions': 0,
     'scope': 'bounded reuse for actual consumed inputs; no new native-host or general Markdown qualification'})
print(json.dumps(json.loads((HERE / 'IMPACT.json').read_text()), indent=2))
