from pathlib import Path
import hashlib
import importlib.util
import json
import os
import subprocess
import time

R = Path('/Users/jim/src/apps/specification_methodology')
O = Path(__file__).resolve().parent
W = O.parent
COMMON = R / 'specification_methodology/v3/build_tenants/common'
TOOLS = COMMON.parent / 'common-tools'
PY = '/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'


def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(name, value):
    p = O / name
    assert not p.exists(), p
    p.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')
    return ref(p)


def main():
    freeze = json.loads((O / 'FREEZE.json').read_bytes())
    for row in freeze['sources']:
        assert ref(R / row['path']) == row
    old_selection = W / 'packaging-001/tooling-selection.json'
    selection = json.loads(old_selection.read_bytes())
    corpus = next(x for x in freeze['sources'] if x['path'].endswith('/source-corpus.json'))
    changed = []
    for row in selection['owners']['stdo_representation']['members']:
        if row['path'] == corpus['path']:
            changed.append({'before': dict(row), 'after': {**row, **corpus}})
            row.update(corpus)
    assert len(changed) == 1
    selection['owner_inventories']['representation']['metadata_successor'] = ref(O / 'FREEZE.json')
    selected = save('tooling-selection.json', selection)
    argv = [PY, '-B', str(TOOLS / 'tooling.py'), 'build', '--repository', str(R), '--selection', str(R / selected['path']),
            '--selection-sha256', selected['sha256'], '--destination', str(O / 'tooling')]
    old_inventory = json.loads((W / 'packaging-001/NATIVE_INPUT_INVENTORY.json').read_bytes())['files']
    old = {x['path']: x for x in old_inventory}
    plan = save('REBUILD_PLAN.json', {'kind': 'stdo.affected-tooling-rebuild/1', 'source_freeze': ref(O / 'FREEZE.json'),
                                     'predecessor_selection': ref(old_selection), 'selection': selected,
                                     'selected_source_delta': changed, 'argv': argv,
                                     'unchanged': 'All model/map/proof/reader/documentation/manager/S inputs remain selected byte-exact; only one transported source and setup.py change.'})
    started = time.time_ns()
    with (O / 'tooling.stdout').open('xb') as out, (O / 'tooling.stderr').open('xb') as err:
        process = subprocess.run(argv, cwd=R, stdout=out, stderr=err, timeout=180)
    save('REBUILD_EXECUTION.json', {'plan': plan, 'argv': argv, 'returncode': process.returncode, 'elapsed_seconds': (time.time_ns()-started)/1e9,
                                   'stdout': ref(O / 'tooling.stdout'), 'stderr': ref(O / 'tooling.stderr')})
    assert process.returncode == 0, (O / 'tooling.stderr').read_text()
    delta = []
    generated = {}
    for p in sorted((O / 'tooling').iterdir()):
        assert p.is_file() and not p.is_symlink()
        name = 'standards/tooling/' + p.name
        new = {**ref(p), 'path': name, 'git_mode': '100755' if p.stat().st_mode & 0o111 else '100644'}
        generated[name] = (p, new)
        if new != old[name]:
            delta.append({'before': old[name], 'after': new})
    assert {x['after']['path'] for x in delta} == {'standards/tooling/' + n for n in ('setup.py', 'sources.zip', 'SELECTION.json', 'TOOLING.json')}
    before_ref = save('PRE_COPY_DELTA.json', {'kind': 'stdo.native-tooling-successor-delta/1', 'changed': delta, 'unchanged_native_members': 169})
    for row in delta:
        name = row['before']['path']
        path = COMMON / name
        assert ref(path)['sha256'] == row['before']['sha256'] and path.stat().st_size == row['before']['bytes']
        assert ('100755' if path.stat().st_mode & 0o111 else '100644') == row['before']['git_mode']
        raw = generated[name][0].read_bytes()
        path.write_bytes(raw)
        path.chmod(0o755 if row['after']['git_mode'] == '100755' else 0o644)
    current = {**old, **{n: x for n, (_, x) in generated.items()}}
    save('NATIVE_INPUT_INVENTORY.json', {'files': [current[k] for k in sorted(current)]})
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    import sys
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(TOOLS))
    import native_release
    config = W / 'packaging-001/native-configuration.json'
    native_release.configure(config, ref(config)['sha256'])
    started = time.time_ns()
    checked = native_release.validate_payload(COMMON)
    save('PAYLOAD_VALIDATION.json', {'status': 'passed', 'elapsed_seconds': (time.time_ns()-started)/1e9,
                                    'result': checked, 'delta': before_ref, 'configuration': ref(config)})
    print(json.dumps({'status': 'passed', 'changed': [x['after']['path'] for x in delta], 'selection': selected,
                      'inventory': ref(O / 'NATIVE_INPUT_INVENTORY.json'), 'validation': ref(O / 'PAYLOAD_VALIDATION.json')}, sort_keys=True))


if __name__ == '__main__':
    main()
