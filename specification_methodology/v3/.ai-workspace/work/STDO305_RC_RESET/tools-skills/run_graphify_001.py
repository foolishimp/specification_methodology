"""Two sequential selected Graphify operations, each recorded as actually run."""
from pathlib import Path
import hashlib, json, resource, subprocess, sys, time

REPO = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).resolve().parent
RECORDS = HERE / 'current-graphify-001'
DEST = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/construction-001/graphify')
MODEL = REPO / 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1'
PYTHON = '/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'

def ref(path):
    path = Path(path).absolute(); raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def save(path, value):
    with path.open('x') as stream: stream.write(json.dumps(value, sort_keys=True, indent=2)+'\n')

phase = sys.argv[1]
assert phase in ('bootstrap', 'roundtrip')
record = RECORDS / phase
assert not record.exists()
if phase == 'bootstrap':
    assert not DEST.exists() and not DEST.is_symlink()
    producer = REPO/'a_c/scripts/bootstrap.py'
    argv = [PYTHON, '-B', str(producer), 'graphify', '--destination', str(DEST)]
    inputs = [producer] + [REPO/'a_c/build_tenants/graphify'/p for p in
        ('test_env/requirements-qualification.txt', 'code/generation/requirements.txt', 'code/code-requirements.txt')]
    outputs = [DEST/'RUNTIME.json', DEST/'bootstrap-evidence/execution.json', DEST/'bootstrap-evidence/packages.txt']
else:
    producer = REPO/'a_c/build_tenants/graphify/code/ac_upstream.py'
    selections = HERE/'model-rebind-003/formal-inputs/formal-selections.json'
    output = RECORDS/'roundtrip-output'
    assert not output.exists()
    argv = [str(DEST/'venv/bin/python'), '-B', str(producer), '--model', str(MODEL/'model.json'),
            '--carrier', str(MODEL/'carrier.json'), '--selections', str(selections), '--upstream',
            str(DEST/'graphify'), '--runtime', str(DEST/'RUNTIME.json'), '--output', str(output)]
    inputs = [MODEL/'model.json', MODEL/'carrier.json', selections, DEST/'RUNTIME.json']
    outputs = [output/name for name in ('model.json', 'carrier.json', 'selections.json', 'runtime.json', 'graph.json', 'views.json', 'result.json')]
selected = [ref(p) for p in inputs]
physical = Path(argv[0]).resolve(strict=True)
version = subprocess.check_output([argv[0], '-c', 'import sys; print(sys.version)'], text=True).strip()
environment = {'python': {'invocation': argv[0], 'executable_realpath': str(physical),
                          'sha256': ref(physical)['sha256'], 'version': version}}
record.mkdir(parents=True)
save(record/'INVOCATION.json', {'argv': argv, 'cwd': str(REPO), 'producer': ref(producer),
     'recorder': ref(__file__), 'inputs': selected, 'environment': environment,
     'bound_seconds': 900, 'scope': 'Fresh private dependency setup or exact current upstream roundtrip. No old runtime/verdict reuse.'})
before = resource.getrusage(resource.RUSAGE_CHILDREN); start = time.time_ns()
with (record/'stdout.json').open('xb') as out, (record/'stderr.log').open('xb') as err:
    proc = subprocess.run(argv, cwd=REPO, stdout=out, stderr=err, timeout=900)
end = time.time_ns(); after = resource.getrusage(resource.RUSAGE_CHILDREN)
actual = {'schema': 'stdo.execution-observation/1', 'producer': ref(producer), 'result': ref(record/'stdout.json'),
 'execution': {'argv': argv, 'cwd': str(REPO), 'returncode': proc.returncode,
 'started_ns': start, 'ended_ns': end, 'elapsed_seconds': (end-start)/1e9,
 'user_seconds': after.ru_utime-before.ru_utime, 'system_seconds': after.ru_stime-before.ru_stime,
 'child_maxrss_native_units': after.ru_maxrss, 'environment': environment, 'inputs': selected,
 'outputs': [ref(p) for p in outputs if p.is_file()], 'stdout': ref(record/'stdout.json'), 'stderr': ref(record/'stderr.log')}}
save(record/'execution.json', actual)
assert selected == [ref(p) for p in inputs], 'Selected inputs changed during operation'
print(json.dumps({'execution': ref(record/'execution.json'), 'returncode': proc.returncode,
                  'elapsed_seconds': (end-start)/1e9}))
raise SystemExit(proc.returncode)
