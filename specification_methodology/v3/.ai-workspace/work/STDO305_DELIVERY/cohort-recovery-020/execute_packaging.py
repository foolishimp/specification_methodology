#!/usr/bin/env python3
"""Execute the assigned seven existing builders, exact auxiliary copy and one native check."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path('/Users/jim/src/apps/specification_methodology')
BASE = ROOT / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY'
OUT = BASE / 'cohort-recovery-020'
COMMON = ROOT / 'specification_methodology/v3/build_tenants/common'
TOOLS = COMMON.with_name('common-tools')
PLAN = OUT / 'PACKAGING_COMMANDS_021.json'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def ref(path):
    path = Path(path)
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(raw), 'bytes': len(raw)}


def read(reference):
    path = ROOT / reference['path']
    assert ref(path) == reference, path
    return json.loads(path.read_bytes())


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as handle:
        handle.write(encoded(value))
    return ref(path)


def inventory(directory):
    result = []
    for path in sorted(directory.rglob('*')):
        if path.is_dir():
            assert not path.is_symlink(), path
            continue
        mode = path.lstat().st_mode
        assert stat.S_ISREG(mode) and not path.is_symlink(), path
        raw = path.read_bytes()
        result.append({'path': path.relative_to(directory).as_posix(), 'bytes': len(raw),
                       'sha256': sha(raw), 'git_mode': '100755' if mode & 0o111 else '100644',
                       'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()})
    return result


plan = json.loads(PLAN.read_bytes())
plan_ref = ref(PLAN)
for selected in plan['fixed_inputs']:
    assert ref(ROOT / selected['path']) == selected
assert sha(Path(plan['python']['executable_realpath']).read_bytes()) == plan['python']['sha256']
for name in plan['absent_destinations']:
    assert not Path(name).exists(), name
execution_root = OUT / 'execution'
execution_root.mkdir(exist_ok=False)
environment = dict(os.environ)
for name in ('PYTHONPATH', 'PYTHONHOME', 'STDO_STORE'):
    environment.pop(name, None)
environment['PYTHONDONTWRITEBYTECODE'] = '1'
dynamic = {}
receipts = []

for operation in plan['commands']:
    name = operation['id']
    start = time.time_ns()
    print('START', name, flush=True)
    if 'argv' in operation:
        argv = [dynamic.get(value, value) for value in operation['argv']]
        stdout = execution_root / (name + '.stdout')
        stderr = execution_root / (name + '.stderr')
        with stdout.open('xb') as out, stderr.open('xb') as err:
            process = subprocess.run(argv, cwd=ROOT, env=environment, stdout=out, stderr=err)
        finish = time.time_ns()
        record = {'kind': 'stdo.packaging-execution/1', 'operation': name,
                  'plan': plan_ref, 'argv': argv, 'cwd': str(ROOT), 'python': plan['python'],
                  'environment': {'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONPATH': 'unset',
                                  'PYTHONHOME': 'unset', 'STDO_STORE': 'unset'},
                  'started_ns': start, 'ended_ns': finish, 'elapsed_seconds': (finish-start)/1e9,
                  'exit_code': process.returncode, 'stdout': ref(stdout), 'stderr': ref(stderr)}
        if process.returncode == 0:
            record['result'] = json.loads(stdout.read_bytes())
        receipts.append(save(execution_root / (name + '.execution.json'), record))
        assert process.returncode == 0, (name, process.returncode, ref(stderr))
    else:
        value = read(operation['predecessor'])
        if name == 'bind-proof-selection':
            value.update(copy.deepcopy(operation['fixed_fields']))
            transport = ref(Path(plan['transport']) / 'TRANSPORT.json')
            value['bundle_archive'] = {k: transport[k] for k in ('path', 'sha256')}
            selected = save(operation['destination'], value)
            dynamic['${PROOF_SELECTION_SHA256}'] = selected['sha256']
        elif name == 'bind-documentation-selection':
            catalog = ref(OUT / 'current-proofs/PROOFS.json')
            value['proof_catalog'] = {k: catalog[k] for k in ('path', 'sha256')}
            selected = save(operation['destination'], value)
            dynamic['${DOCUMENTATION_SELECTION_SHA256}'] = selected['sha256']
        else:
            raise ValueError(name)
        finish = time.time_ns()
        record = {'kind': 'stdo.packaging-binding/1', 'operation': name, 'plan': plan_ref,
                  'predecessor': operation['predecessor'], 'output': selected,
                  'started_ns': start, 'ended_ns': finish, 'elapsed_seconds': (finish-start)/1e9,
                  'notice': 'Actual metadata binding; no process execution is asserted.'}
        receipts.append(save(execution_root / (name + '.execution.json'), record))
    print('DONE', name, round(record['elapsed_seconds'], 3), flush=True)

complete = save(execution_root / 'COMPLETE.json', {'kind': 'stdo.packaging-completion/1',
    'status': 'seven_operations_succeeded', 'plan': plan_ref, 'operations': receipts,
    'construction': plan['construction'], 'tooling_selection': plan['tooling_selection']})
print('PACKAGING_COMPLETE', complete['sha256'], flush=True)

# Retain the exact generated byte/mode comparison before touching common output.
before = read(plan['native_preimage'])['files']
actual_before = inventory(COMMON)
assert actual_before == before, 'native common preimage drift'
old = {row['path']: row for row in before}
generated = {}
for directory, prefix in ((OUT / 'current-documentation', 'standards/documentation/'),
                          (OUT / 'current-tooling', 'standards/tooling/')):
    for row in inventory(directory):
        name = prefix + row['path']
        assert name not in generated
        generated[name] = (directory / row['path'], {**row, 'path': name})
old_auxiliary = {name for name in old if name.startswith(('standards/documentation/', 'standards/tooling/'))}
assert set(generated) == old_auxiliary, 'generated auxiliary membership differs'
changed = [{'before': old[name], 'after': row} for name, (_, row) in sorted(generated.items()) if old[name] != row]
assert changed
delta = save(OUT / 'PRE_COPY_DELTA.json', {'kind': 'stdo.native-auxiliary-copy-preparation/1',
    'source_native_preimage': plan['native_preimage'], 'packaging_completion': complete,
    'changed': changed, 'unchanged_native_members': len(before)-len(changed),
    'native_member_count': len(before), 'limits': 'Byte/mode delta retained before all copies; only generated documentation/tooling roots selected.'})
for row in changed:
    name = row['before']['path']
    path = COMMON / name
    prior = path.read_bytes()
    expected = row['before']
    assert sha(prior) == expected['sha256'] and len(prior) == expected['bytes']
    assert ('100755' if path.stat().st_mode & 0o111 else '100644') == expected['git_mode']
    source = generated[name][0]
    raw = source.read_bytes()
    assert sha(raw) == row['after']['sha256']
    with path.open('wb') as handle:
        handle.write(raw)
    path.chmod(0o755 if row['after']['git_mode'] == '100755' else 0o644)
after = inventory(COMMON)
expected_after = {**old, **{name: row for name, (_, row) in generated.items()}}
assert after == [expected_after[name] for name in sorted(expected_after)]
copy_result = save(OUT / 'COPY_RESULT.json', {'kind': 'stdo.native-auxiliary-copy/1', 'status': 'copied',
    'precopy_delta': delta, 'changed_paths': [row['after']['path'] for row in changed],
    'unchanged_native_members': len(before)-len(changed), 'native_member_count': len(after)})
native_inventory = save(OUT / 'NATIVE_INPUT_INVENTORY.json', {'kind': 'stdo.native-source-input-inventory/1', 'files': after})
print('COPIED', len(changed), 'native members', len(after), flush=True)

# One existing configured native validator; no separate documentation/proof reruns.
start = time.monotonic()
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location('stdo_assigned_native_release', TOOLS / 'native_release.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
configuration = plan['configuration']
module.configure(ROOT / configuration['path'], configuration['sha256'])
data = {row['path']: (COMMON / row['path']).read_bytes() for row in after}
validation_start = time.monotonic()
module.validate_payload(after, data)
validation_seconds = time.monotonic() - validation_start
semantic = read(plan['semantic_source'])
assert all(sha(data[row['path']]) == row['sha256'] for row in semantic['members']+semantic['native_contracts'])
selected = read(plan['tooling_selection'])
peer_count = sum(len(unit['members']) for unit in selected['owners'].values())
assert peer_count == 240
invariants = save(OUT / 'PAYLOAD_INVARIANTS.json', {'kind': 'stdo.current-native-payload-validation/1',
    'status': 'passed', 'registered_checker': ref(TOOLS / 'native_release.py'),
    'configuration_sha256': configuration['sha256'], 'source_semantic_identity': semantic['source_identity_sha256'],
    'semantic_members_unchanged': len(semantic['members'])+len(semantic['native_contracts']),
    'current_model_raw_sha256': read(plan['proof_predecessor'])['model']['sha256'],
    'construction_current021_result': read(plan['construction'])['result'],
    'native_files': len(after), 'native_bytes': sum(row['bytes'] for row in after),
    'native_input_inventory': native_inventory, 'copy_result': copy_result,
    'changed_native_members': len(changed), 'unchanged_native_members': len(before)-len(changed),
    'peer_source_members_current': peer_count, 'peer_source_selected_inventory': plan['tooling_selection'],
    'validate_payload_seconds': validation_seconds, 'elapsed_seconds': time.monotonic()-start,
    'limits': 'Existing full configured native payload predicate executed once. Source/model/representation/viewer unchanged; no Git/index/ref/native commit/store/publication effect.'})
print('NATIVE_VALIDATION_PASSED', round(validation_seconds, 3), invariants['sha256'], flush=True)
