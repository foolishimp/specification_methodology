import hashlib, importlib.util, json, os, stat, subprocess, sys, time
from pathlib import Path

R = Path.cwd()
O = Path(__file__).resolve().parent
COMMON = R / 'specification_methodology/v3/build_tenants/common'
TOOLS = COMMON.parent / 'common-tools'
sha = lambda raw: hashlib.sha256(raw).hexdigest()

def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': sha(raw), 'bytes': len(raw)}

def load(p):
    return json.loads(p.read_bytes())

def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as out:
        json.dump(value, out, indent=2, sort_keys=True)
        out.write('\n')
    return ref(p)

def inventory(root):
    result = []
    for p in sorted(root.rglob('*')):
        assert not p.is_symlink(), p
        if p.is_dir():
            continue
        assert stat.S_ISREG(p.lstat().st_mode), p
        raw = p.read_bytes()
        result.append({'path': p.relative_to(root).as_posix(), 'sha256': sha(raw),
                       'bytes': len(raw), 'git_mode': '100755' if p.stat().st_mode & 0o111 else '100644'})
    return result

assert ref(O / 'PLAN.json')['sha256'] == '9573f8c6c6934f4c889e05f6976fe8d0cd391872130bee692f4df0a3112a331d'
plan = load(O / 'PLAN.json')
assert subprocess.check_output(['git', '--no-optional-locks', 'rev-parse', 'HEAD']).decode().strip() == plan['source_checkpoint']
repair = O.parent / 'materializer-review-004/FREEZE.json'
assert ref(repair)['sha256'] == '4a10d33e606e7109b49e747158bbafabc90bf54d18de92789aa3660fff9cc7f6'
new_sources = load(repair)['source']
for row in new_sources:
    assert ref(R / row['path']) == {k: row[k] for k in ('path', 'sha256', 'bytes')}
for row in plan['fixed_inputs']:
    if row['path'].endswith('/tooling_materialize.py'):
        assert row['sha256'] == '601fdb839266528db8999b1f04cf64bce0c41faf107f0f9311549c085d4f897e'
    else:
        assert ref(R / row['path']) == row, row['path']
assert sha(Path(plan['python']['invocation']).read_bytes()) == plan['python']['sha256']
for name in ('tooling-002', 'execution/tooling-002.json', 'execution/COMPLETE.json', 'PRE_COPY_DELTA.json', 'COPY_RESULT.json', 'NATIVE_INPUT_INVENTORY.json', 'PAYLOAD_VALIDATION.json', 'OPERATION_SUCCESSOR_002.json'):
    assert not (O / name).exists(), name

custody = O.parent / 'review-custody-003'
custody.mkdir()
origin = Path('/tmp/stdo305-rc-reset-review-K0KuCT')
copies = []
for name in ('MATERIALIZER_REVIEW_004.json', 'materializer004-controls.txt'):
    raw = (origin / name).read_bytes()
    if name.endswith('.json'):
        assert sha(raw) == '7a02736aacbafd5dd75f4b5dbba87c3a9b923ed5bfe2be47330489bc6b4782e2'
    target = custody / name
    with target.open('xb') as out:
        out.write(raw)
    copies.append({'original_path': str(origin / name), 'retained': ref(target)})
review = save(custody / 'CUSTODY.json', {'kind': 'stdo.independent-review-custody/1', 'assessor': '/root/stdo305_integration_review', 'files': copies})
prior_receipts = [ref(O / 'execution' / (name + '.json')) for name in ('pack', 'split', 'bind-proof', 'reader', 'bind-docs', 'docs')]
for row in prior_receipts:
    observed = load(R / row['path'])
    if 'returncode' in observed:
        assert observed['returncode'] == 0
failed = ref(O / 'execution/tooling.json')
assert failed['sha256'] == 'd40f6b3a942ed3b874e8cb7215e99cf4034644295e7e8e08b0948a94082be533'
assert load(O / 'execution/tooling.json')['returncode'] == 2
argv = list(plan['commands'][-1]['argv'])
assert argv[-1] == str(O / 'tooling')
argv[-1] = str(O / 'tooling-002')
successor = save(O / 'OPERATION_SUCCESSOR_002.json', {
    'kind': 'stdo.packaging-operator-successor/1',
    'authority': 'Root accepted MATERIALIZER_REVIEW_004 and assigned tooling onward only; first six operations remain retained successful observations.',
    'predecessor_plan': ref(O / 'PLAN.json'), 'prior_successful_operations': prior_receipts,
    'preserved_refusal': failed, 'repair_freeze': ref(repair), 'review_custody': review,
    'current_sources': [{k: row[k] for k in ('path', 'sha256', 'bytes')} for row in new_sources],
    'command': argv, 'python': plan['python'], 'source_checkpoint': plan['source_checkpoint'],
    'postconditions': plan['postconditions'], 'limits': plan['limits']})
print('SUCCESSOR', successor['sha256'], flush=True)
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
for name in ('PYTHONPATH', 'PYTHONHOME', 'STDO_STORE'):
    env.pop(name, None)
stdout, stderr = O / 'execution/tooling-002.stdout', O / 'execution/tooling-002.stderr'
start = time.monotonic()
print('START tooling-002', flush=True)
with stdout.open('xb') as out, stderr.open('xb') as err:
    process = subprocess.run(argv, cwd=R, env=env, stdout=out, stderr=err)
record = {'kind': 'stdo.packaging-execution/1', 'operation': 'tooling-002', 'argv': argv, 'cwd': str(R),
          'returncode': process.returncode, 'python': plan['python'], 'stdout': ref(stdout), 'stderr': ref(stderr),
          'elapsed_seconds': time.monotonic() - start}
if process.returncode == 0:
    record['result'] = load(stdout)
receipt = save(O / 'execution/tooling-002.json', record)
assert process.returncode == 0, (process.returncode, stderr.read_text())
print('DONE tooling-002', record['elapsed_seconds'], flush=True)
complete = save(O / 'execution/COMPLETE.json', {'kind': 'stdo.packaging-completion/1', 'status': 'seven_selected_operations_succeeded',
    'plan': ref(O / 'PLAN.json'), 'operator_successor': successor, 'operations': prior_receipts + [receipt], 'preserved_failed_attempt': failed})
before = load(R / plan['native_preimage']['path'])['files']
assert inventory(COMMON) == before, 'common preimage drift'
old = {row['path']: row for row in before}
generated = {}
for directory, prefix in ((O / 'documentation', 'standards/documentation/'), (O / 'tooling-002', 'standards/tooling/')):
    for row in inventory(directory):
        name = prefix + row['path']
        assert name not in generated
        generated[name] = (directory / row['path'], {**row, 'path': name})
assert set(generated) == {name for name in old if name.startswith(('standards/documentation/', 'standards/tooling/'))}, 'auxiliary member closure differs'
changed = [{'before': old[name], 'after': row} for name, (_, row) in sorted(generated.items()) if old[name] != row]
delta = save(O / 'PRE_COPY_DELTA.json', {'kind': 'stdo.rc-native-auxiliary-delta/1', 'source_preimage': plan['native_preimage'],
    'packaging': complete, 'changed': changed, 'native_files': len(before), 'unchanged_files': len(before) - len(changed)})
for row in changed:
    name = row['before']['path']
    p = COMMON / name
    assert sha(p.read_bytes()) == row['before']['sha256']
    assert ('100755' if p.stat().st_mode & 0o111 else '100644') == row['before']['git_mode']
    raw = generated[name][0].read_bytes()
    assert sha(raw) == row['after']['sha256']
    p.write_bytes(raw)
    p.chmod(0o755 if row['after']['git_mode'] == '100755' else 0o644)
after = inventory(COMMON)
expected = {**old, **{name: row for name, (_, row) in generated.items()}}
assert after == [expected[name] for name in sorted(expected)]
copy = save(O / 'COPY_RESULT.json', {'status': 'copied', 'delta': delta, 'changed_paths': [row['after']['path'] for row in changed]})
native_inventory = save(O / 'NATIVE_INPUT_INVENTORY.json', {'files': after})
print('COPIED', len(changed), 'of', len(after), 'members', flush=True)
sys.dont_write_bytecode = True
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location('selected_native', TOOLS / 'native_release.py')
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
native.configure(R / plan['configuration']['path'], plan['configuration']['sha256'])
data = {row['path']: (COMMON / row['path']).read_bytes() for row in after}
start = time.monotonic()
native.validate_payload(after, data)
duration = time.monotonic() - start
freeze = load(R / load(R / plan['configuration']['path'])['source']['path'])
assert all(sha(data[row['path']]) == row['sha256'] for row in freeze['members'] + freeze['native_contracts'])
result = save(O / 'PAYLOAD_VALIDATION.json', {'kind': 'stdo.rc-native-payload-validation/1', 'status': 'passed',
    'source_checkpoint': plan['source_checkpoint'], 'configuration': plan['configuration'], 'native_inventory': native_inventory,
    'copy_result': copy, 'native_files': len(after), 'native_bytes': sum(row['bytes'] for row in after), 'changed_files': len(changed),
    'semantic_members_unchanged': 68, 'tooling_members': 243, 'validation_seconds': duration, 'construction': plan['construction'],
    'limitations': 'Actual construction package validation only; native commit/install/public qualification pending.'})
print('NATIVE_PAYLOAD_VALID', duration, result['sha256'], flush=True)
