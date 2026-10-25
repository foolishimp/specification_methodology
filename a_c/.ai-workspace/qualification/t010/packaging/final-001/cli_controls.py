"""Actual extracted CLI controls, using only Python standard library."""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess

BASE = Path('/Users/jim/src/apps/specification_methodology/a_c')
PROOF = BASE / '.ai-workspace/qualification/t010/packaging/final-001'
state = json.loads((PROOF / 'extracted-stdlib-result.json').read_text())
BUNDLE, WORK = Path(state['bundle']), Path(state['work'])
OUT = WORK / 'cli-outputs'
OUT.mkdir(exist_ok=True)
COMMANDS = PROOF / 'commands'
COMMANDS.mkdir(exist_ok=True)
PYTHON = str(BASE / '.venv/bin/python3')
env = dict(os.environ)
env['PYTHONDONTWRITEBYTECODE'] = '1'
env['XDG_CACHE_HOME'] = str(WORK / 'cache')
env['TMPDIR'] = str(WORK / 'tmp')


def run(name, arguments, expected=0):
    command = [PYTHON, '-B', '-S', *arguments]
    conserved = json.loads((PROOF / 'cli-conserved-completions.json').read_text())
    if name in conserved:
        row = conserved[name]
        assert row['returncode'] == expected
        for item in row['files'].values():
            assert hashlib.sha256((COMMANDS / item['path']).read_bytes()).hexdigest() == item['sha256']
        recorded = json.loads((COMMANDS / (name + '.invocation.json')).read_text())
        assert recorded == {'command': command, 'cwd': str(BUNDLE)}
        print(json.dumps({'operation': name, 'returncode': expected, 'status': 'conserved_successful_completion'}), flush=True)
        return json.loads((COMMANDS / (name + '.stdout.json')).read_text())
    (COMMANDS / (name + '.invocation.json')).write_text(json.dumps({'command': command, 'cwd': str(BUNDLE)}, indent=2) + '\n')
    result = subprocess.run(command, cwd=BUNDLE, env=env, capture_output=True, text=True, timeout=900)
    (COMMANDS / (name + '.stdout.json')).write_text(result.stdout)
    (COMMANDS / (name + '.stderr.txt')).write_text(result.stderr)
    assert result.returncode == expected, (name, result.returncode, result.stderr)
    response = json.loads(result.stdout if expected == 0 else result.stderr)
    print(json.dumps({'operation': name, 'returncode': result.returncode, 'status': response.get('status', 'returned')}), flush=True)
    return response


jobs = {
    'validate-model': ['codec/ac_graph.py', 'validate', 'model.json'],
    'recover-carrier': ['codec/ac_graph.py', 'decode', 'carrier.json', '--out', str(OUT / 'carrier-model.json')],
    'recover-upstream': ['codec/ac_graph.py', 'decode', 'graph.json', '--out', str(OUT / 'upstream-model.json')],
    'find-admission': ['codec/ac_graph.py', 'find', 'carrier.json', 'admission'],
}
results = {}
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = {executor.submit(run, name, args): name for name, args in jobs.items()}
    for future in as_completed(futures):
        results[futures[future]] = future.result()
model = json.loads((BUNDLE / 'model.json').read_text())
for name in ('carrier-model.json', 'upstream-model.json'):
    assert json.loads((OUT / name).read_text()) == model
expected_model = {'id': model['id'], 'profile': 'a_c.graphify.model/1', 'sha256': '691c4ab0d0993312a31e7e2371070ea4758fdf74b32862ff4d5a32d05af79fbf'}
assert all(results[name]['model'] == expected_model for name in ('validate-model', 'recover-carrier', 'recover-upstream'))
assert results['find-admission']['matches'] and results['find-admission']['parent'] == expected_model
seed = results['find-admission']['matches'][0]['id']
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = {
        executor.submit(run, 'inspect-found-record', ['codec/ac_graph.py', 'inspect', 'carrier.json', seed]): 'inspect',
        executor.submit(run, 'project-found-record', ['codec/ac_graph.py', 'project', 'carrier.json', '--seed', seed,
                                                     '--budget', '1987', '--out', str(OUT / 'selected-projection.json')]): 'project',
    }
    for future in as_completed(futures):
        results[futures[future]] = future.result()
assert results['inspect']['parent'] == expected_model and results['inspect']['record']['id'] == seed
assert results['project']['parent'] == expected_model and seed in results['project']['included']
assert set(results['project']['included']).isdisjoint(results['project']['excluded'])
assert len(results['project']['included']) + len(results['project']['excluded']) == 1987
source = run('source-reentry', ['release_tools/source_reentry.py', 'standards/ACTIVATION.md', '--start', '1', '--end', '30'])
assert source['text'] == ''.join((BUNDLE / 'source/standards/ACTIVATION.md').read_text().splitlines(keepends=True)[:30])
result = {'status': 'passed', 'scope': 'Representative actual extracted CLI mechanics; no F_P actual-use/invariant-reconstruction or semantic acceptance judgment',
          'site_packages_disabled': True, 'model': expected_model, 'model_validation_records': results['validate-model']['records'],
          'both_full_carriers_recovered_exactly': True,
          'recovered_raw_hashes': {name: hashlib.sha256((OUT / name).read_bytes()).hexdigest()
                                  for name in ('carrier-model.json', 'upstream-model.json')},
          'literal_admission_matches': len(results['find-admission']['matches']), 'selected_seed': seed,
          'inspect_family': results['inspect']['family'], 'projection_records': len(results['project']['included']),
          'projection_excluded_records': len(results['project']['excluded']), 'source_reentry_exact_lines': 30,
          'outputs': str(OUT), 'commands': 7, 'browser_or_server_started': False}
(PROOF / 'cli-controls.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
