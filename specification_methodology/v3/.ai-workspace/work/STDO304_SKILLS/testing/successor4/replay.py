"""Replay real successful source-helper inputs under the selected successor."""
import json
from pathlib import Path
import shlex
import subprocess

HERE = Path(__file__).resolve().parent
meta = json.loads((HERE / 'FIXTURES.json').read_text())
reader = str(Path(meta['candidate']) / 'plugins/spec/scripts/read_basis.py')
inputs = []
for directory in ('successor', 'successor3'):
    for run in sorted((HERE.parent / directory / 'runs').iterdir()):
        tools = json.loads((run / 'TOOLS.json').read_text())
        results = {row['tool_result_id']: row for row in tools if 'tool_result_id' in row}
        for row in tools:
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
            try: previous = json.loads(output)
            except (ValueError, TypeError): continue
            if previous.get('status') != 'checked': continue
            argv = shlex.split(command)
            if argv[:2] != [meta['python'], '-B'] or argv[3] not in ('check', 'read'): continue
            assert argv[2].endswith('/candidate/plugins/spec/scripts/read_basis.py')
            assert all(a not in (';', '&&', '|', '>', '<') for a in argv)
            argv[2] = reader
            inputs.append((str(run.relative_to(HERE.parent)), row['line'], argv, previous))

# Include the denied-spelling reproduction's actual successful Effects read.
repro = json.loads((HERE.parent / 'successor3/EF03_REPRO.json').read_text())
argv = shlex.split(repro['gate_checks'][1]['command']); argv[2] = reader
inputs.append(('successor3/EF03_REPRO', None, argv, repro['reader_result']))
rows = []
for origin, line, argv, previous in inputs:
    result = subprocess.run(argv, capture_output=True, text=True, timeout=30)
    value = json.loads(result.stdout)
    row = {'origin': origin, 'trace_line': line, 'argv': argv, 'exit': result.returncode, 'result': value,
           'identity_unchanged': all(previous.get(k) == value.get(k) for k in ('basis_uri', 'manifest_sha256', 'member_sha256', 'definition_sha256')),
           'sections_unchanged': previous.get('sections') == value.get('sections'),
           'catalog_unchanged': previous.get('headings') == value.get('headings')}
    rows.append(row)
    assert result.returncode == 0 and value['status'] == 'checked' and row['identity_unchanged'] and row['sections_unchanged'] and row['catalog_unchanged'], origin

# Rebind every source operation to the new installed fixture as well.
current = []
seen = set()
for _, _, argv, _ in inputs:
    suffix = tuple(argv[argv.index('--member'):]) if '--member' in argv else ()
    if suffix in seen: continue
    seen.add(suffix)
    command = [meta['python'], '-B', reader, 'read' if suffix else 'check', '--stdo', meta['manager'], '--store', meta['store'], '--definition', str(Path(meta['projects']['coordinated']) / 'stdo_fixture.json')] + list(suffix)
    result = subprocess.run(command, capture_output=True, text=True, timeout=30)
    value = json.loads(result.stdout)
    current.append({'argv': command, 'exit': result.returncode, 'result': value})
    assert result.returncode == 0 and value['status'] == 'checked'
(HERE / 'READER_REPLAY.json').write_text(json.dumps({'retained_inputs': rows, 'current_binding': current}, indent=2) + '\n')
print(json.dumps({'retained_successful_inputs': len(rows), 'direct_retained': sum(r['origin'] == 'successor/runs/direct' for r in rows), 'all_replays_unchanged': True, 'current_binding_operations_checked': len(current)}, indent=2))
