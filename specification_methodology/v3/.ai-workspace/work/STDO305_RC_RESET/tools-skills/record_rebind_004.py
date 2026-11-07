"""Execute the unchanged deterministic rebind with full contemporaneous custody."""
from pathlib import Path
import hashlib, json, resource, subprocess, sys, time

REPO = Path('/Users/jim/src/apps/specification_methodology')
HERE = Path(__file__).resolve().parent

def ref(path):
    path = Path(path).absolute(); raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def save(path, value):
    with path.open('x') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')

record = HERE / 'model-rebind-004'
record.mkdir()
invocation = json.loads((HERE / 'model-rebind-003/invocation.json').read_text())
argv = invocation['argv']
argv[argv.index('--model-output') + 1] = str(record / 'emitted-model.json')
argv[argv.index('--report') + 1] = str(record / 'REBIND.json')
inputs = [Path(argv[argv.index(flag) + 1]) for flag in
          ('--predecessor', '--predecessor-source-freeze', '--source-freeze', '--current-source-inventory')]
source_root = Path(argv[argv.index('--source-root') + 1])
freeze = json.loads(inputs[2].read_bytes())
inputs += [source_root / row['path'] for row in freeze['members'] + freeze['native_contracts']]
producer = Path(argv[2]); selected_inputs = [ref(p) for p in inputs]
python = {'invocation': argv[0], 'executable_realpath': str(Path(argv[0]).resolve()),
          'sha256': ref(Path(argv[0]).resolve())['sha256'], 'version': sys.version}
assert Path(sys.executable).resolve() == Path(argv[0]).resolve()
save(record / 'invocation.json', {'argv': argv, 'cwd': str(REPO), 'producer': ref(producer),
     'recorder': ref(__file__), 'environment': {'python': python}, 'inputs': selected_inputs,
     'standing': 'New actual deterministic execution; original 003 observations are unchanged.'})
start = time.time_ns(); before = resource.getrusage(resource.RUSAGE_CHILDREN)
with (record / 'stdout.json').open('xb') as out, (record / 'stderr.txt').open('xb') as err:
    result = subprocess.run(argv, cwd=REPO, stdout=out, stderr=err, timeout=180)
end = time.time_ns(); after = resource.getrusage(resource.RUSAGE_CHILDREN)
assert selected_inputs == [ref(p) for p in inputs], 'inputs changed during execution'
outputs = [record / name for name in ('emitted-model.json', 'REBIND.json', 'stdout.json', 'stderr.txt')]
save(record / 'execution.json', {'schema': 'stdo.execution-observation/1', 'producer': ref(producer),
     'result': ref(record / 'stdout.json'), 'execution': {'argv': argv, 'cwd': str(REPO),
     'returncode': result.returncode, 'started_ns': start, 'ended_ns': end,
     'elapsed_seconds': (end-start)/1e9, 'user_seconds': after.ru_utime-before.ru_utime,
     'system_seconds': after.ru_stime-before.ru_stime, 'child_maxrss_native_units': after.ru_maxrss,
     'environment': {'python': python}, 'inputs': selected_inputs,
     'outputs': [ref(p) for p in outputs if p.is_file()],
     'stdout': ref(record/'stdout.json'), 'stderr': ref(record/'stderr.txt')}})
assert result.returncode == 0, result.returncode
canonical = REPO / 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/model.json'
assert (record/'emitted-model.json').read_bytes() == canonical.read_bytes()
save(record/'CORRESPONDENCE.json', {'kind': 'stdo.coordinate-rebind.emitted-correspondence/1',
     'emitted_model': ref(record/'emitted-model.json'), 'canonical_model': ref(canonical),
     'exact_raw_bytes_equal': True, 'prior_execution': ref(HERE/'model-rebind-003/execution.json'),
     'claim': '004 observed current invocation; no retrospective environment assertion for 003.'})
binding = canonical.parent/'current-binding.json'
(record/'current-binding-preimage.json').write_bytes(binding.read_bytes())
value = json.loads(binding.read_bytes())
for key, path in (('execution', record/'execution.json'), ('rebind', record/'REBIND.json'),
                  ('emitted_model', record/'emitted-model.json')):
    value[key] = ref(path); value[key]['path'] = path.relative_to(REPO).as_posix()
binding.write_text(json.dumps(value, sort_keys=True, indent=2)+'\n')
print(json.dumps({'execution': ref(record/'execution.json'), 'report': ref(record/'REBIND.json'),
                  'correspondence': ref(record/'CORRESPONDENCE.json'), 'binding': ref(binding)}))
