"""Execute the selected fixed-tag onboarding recipe into one fresh public workspace."""
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time
import zipfile
from pathlib import Path, PurePosixPath

R = Path.cwd()
C = Path(__file__).resolve().parent
Q = C.parent.parent
O = Q / 'public-qualification-001'
X = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/public-001')
PY = '/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/bin/python3.13'
sha = lambda raw: hashlib.sha256(raw).hexdigest()
def load(p): return json.loads(p.read_bytes())
def ref(p):
    raw = p.read_bytes()
    return {'path': str(p.relative_to(R)) if p.is_relative_to(R) else str(p), 'sha256': sha(raw), 'bytes': len(raw)}
def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: json.dump(value, f, indent=2, sort_keys=True); f.write('\n')
    return ref(p)
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1', PIP_DISABLE_PIP_VERSION_CHECK='1', GIT_TERMINAL_PROMPT='0')
for key in ('PYTHONPATH', 'PYTHONHOME', 'STDO_STORE', 'GH_TOKEN', 'GITHUB_TOKEN'):
    env.pop(key, None)
def run(name, argv, *, stdin=None):
    target = O / 'manager-operations' / name
    target.mkdir(parents=True, exist_ok=False)
    start = time.time_ns()
    save(target / 'invocation.json', {'argv': argv, 'cwd': str(R), 'started_ns': start,
        'environment_selection': {'set': {k: env[k] for k in ('PYTHONDONTWRITEBYTECODE', 'PYTHONNOUSERSITE', 'PIP_DISABLE_PIP_VERSION_CHECK', 'GIT_TERMINAL_PROMPT')}, 'unset': ['PYTHONPATH', 'PYTHONHOME', 'STDO_STORE', 'GH_TOKEN', 'GITHUB_TOKEN']}})
    if stdin is not None: (target / 'stdin.txt').write_bytes(stdin)
    print('START', name, flush=True)
    with (target / 'stdout.txt').open('xb') as out, (target / 'stderr.txt').open('xb') as err:
        result = subprocess.run(argv, cwd=R, env=env, input=stdin, stdout=out, stderr=err)
    receipt = save(target / 'execution.json', {'kind': 'stdo.public-install-execution/1', 'argv': argv, 'cwd': str(R),
        'returncode': result.returncode, 'started_ns': start, 'ended_ns': time.time_ns(),
        'elapsed_seconds': (time.time_ns() - start) / 1e9, 'stdout': ref(target / 'stdout.txt'), 'stderr': ref(target / 'stderr.txt'),
        'stdin': ref(target / 'stdin.txt') if stdin is not None else None})
    print('DONE', name, result.returncode, flush=True)
    assert result.returncode == 0, (name, (target / 'stderr.txt').read_text()[-3000:])
    return (target / 'stdout.txt').read_bytes(), receipt

published = load(C / 'publication-execution/RELEASE_PUBLISHED.json')
carrier = load(C / 'manifest-reconciliation-002/RESULT.json')['commit']
assert published['carrier'] == carrier
forms = load(C / 'publication/OPERATION_TEMPLATES.json')
prior = load(C.parent / 'native-transaction-002/HANDOFF.json')
assert prior['native_commit'] == 'b5b00b896d44804e0f5d615a9bc23a02345888b3'
assert not O.exists() and not X.exists()
for path in (X, *X.parents):
    assert not path.is_symlink() and (not path.exists() or path.is_dir())
assert os.statvfs(R).f_bavail * os.statvfs(R).f_frsize >= 2 * 1024**3
assert os.path.samefile(sys.executable, PY) and sha(Path(PY).read_bytes()) == 'a708f6e9f4803b806b29146c4e0feecfd9bf2d9eb60f3e15b850cd7cb56f200b'
O.mkdir(); X.mkdir(parents=True)
downloads = X / 'downloads'; downloads.mkdir()
guide = R / 'specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md'
guide_text = guide.read_text()
recipe = guide_text.split("```sh\nset -eu\nSTDO_CUT='v3.0.5-rc.1'", 1)[1].split('\n```', 1)[0]
recipe = "set -eu\nSTDO_CUT='v3.0.5-rc.1'" + recipe
(O / 'ONBOARDING_RECIPE.sh').write_text(recipe + '\n')
verifier = recipe.split("<<'PYVERIFY'\n", 1)[1].split('\nPYVERIFY', 1)[0]
(O / 'verify_downloads.py').write_text(verifier + '\n')
save(O / 'RECIPE_BINDING.json', {'guide': ref(guide), 'recipe': ref(O / 'ONBOARDING_RECIPE.sh'), 'verifier': ref(O / 'verify_downloads.py'),
    'selection': 'Exact guide verification code and command sequence. Only explicit external manager/store/download paths and selected physical Python are bound; curl adds disabled user config and retained response metadata. No downloaded code executes before all five API digest/size checks.',
    'manager': str(X / 'manager'), 'store': str(X / 'store'), 'downloads': str(downloads), 'python': PY})
acquired = []
def acquire(name, url):
    target = downloads / name
    headers = O / 'acquisition' / (name + '.headers'); headers.parent.mkdir(exist_ok=True)
    raw, execution = run('download-' + name, ['/usr/bin/curl', '--disable', '--fail', '--location', '--silent', '--show-error', '--dump-header', str(headers), '--write-out', '%{json}', '--output', str(target), url])
    metadata = json.loads(raw)
    assert metadata['http_code'] == 200 and metadata['ssl_verify_result'] == 0
    retained = O / 'acquisition' / name
    with retained.open('xb') as out: out.write(target.read_bytes())
    assert ref(retained)['sha256'] == ref(target)['sha256']
    row = {'url': url, 'final_url': metadata['url_effective'], 'status': metadata['http_code'], 'unauthenticated': True,
        'tls_verification': True, 'bytes': ref(target), 'retained_body': ref(retained), 'headers': ref(headers), 'execution': execution}
    acquired.append(row)
    return target

api_url = 'https://api.github.com/repos/foolishimp/specification_methodology/releases/tags/specification_methodology%2Fv3.0.5-rc.1'
api_path = acquire('release.json', api_url)
release = load(api_path)
assert release['id'] == published['release_id'] and release['tag_name'] == 'specification_methodology/v3.0.5-rc.1'
assert release['draft'] is False and release['prerelease'] is False
expected = {a['name']: (a['sha256'], a['bytes']) for a in forms['assets']}
bref = published['external_manifest']; expected[forms['external_manifest_asset']['name']] = (bref['sha256'], bref['bytes'])
assert len(release['assets']) == 5 and {a['name']: (a['digest'].removeprefix('sha256:'), a['size']) for a in release['assets']} == expected
for name in ('stdo_toolchain-3.0.5rc1-py3-none-any.whl', 'stdo-v3.0.5-rc.1-manifest.json', 'stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip', 'stdo-manager-constraints-v3.0.5-rc.1-python313.txt', 'stack-release-v3.0.5-rc.1.json'):
    path = acquire(name, 'https://github.com/foolishimp/specification_methodology/releases/download/specification_methodology%2Fv3.0.5-rc.1/' + name)
    assert (ref(path)['sha256'], path.stat().st_size) == expected[name]
run('recipe-verify-all-assets', [PY, '-', str(downloads)], stdin=(verifier + '\n').encode())
acquisition = save(O / 'ACQUISITION.json', {'kind': 'stdo.anonymous-release-acquisition/1', 'status': 'verified', 'carrier': carrier,
    'release_id': release['id'], 'release': ref(api_path), 'downloads': acquired, 'external_manifest': ref(downloads / forms['external_manifest_asset']['name']), 'recipe': ref(O / 'RECIPE_BINDING.json')})
archive = downloads / 'stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip'
with zipfile.ZipFile(archive) as z:
    assert len(z.namelist()) == len(set(z.namelist())) == 25
    for entry in z.infolist():
        p = PurePosixPath(entry.filename)
        assert str(p) == entry.filename and not p.is_absolute() and not any(part in ('', '.', '..') for part in p.parts)
        assert not entry.is_dir() and stat.S_IFMT(entry.external_attr >> 16) in (0, stat.S_IFREG)
    wheels = json.loads(z.read('WHEELS.json'))
    assert wheels['version'] == '3.0.5-rc.1' and len(wheels['members']) == 21
    for row in wheels['members']:
        raw = z.read(row['path']); assert sha(raw) == row['sha256'] and len(raw) == row['bytes']
run('recipe-runtime-extract', [PY, '-m', 'zipfile', '-e', str(archive), str(downloads / 'runtime')])
run('recipe-manager-create', [PY, '-m', 'venv', str(X / 'manager')])
run('recipe-offline-manager-install', [str(X / 'manager/bin/python'), '-m', 'pip', 'install', '--no-index', '--find-links', str(downloads / 'runtime/wheels'), '--require-hashes', '--no-deps', '-r', str(downloads / 'runtime/requirements-macos-arm64-cp313.txt')])
run('recipe-pip-check', [str(X / 'manager/bin/python'), '-m', 'pip', 'check'])
run('recipe-manager-version', [str(X / 'manager/bin/stdo'), '--store', str(X / 'store'), '--version'])
ops = load(C.parent / 'native-transaction-002/OPERATIONS.json')
identity = matched = None
for name in ('external-manager-identities', 'external-manager-source-match'):
    argv = next(c['argv'] for c in ops['commands'] if c['id'] == name)
    argv = [a.replace(prior['workspace'], str(X)).replace(str(C.parent / 'manager-001/dist/stdo_toolchain-3.0.5rc1-py3-none-any.whl'), str(downloads / 'stdo_toolchain-3.0.5rc1-py3-none-any.whl')) for a in argv]
    raw, receipt = run(name, argv)
    if name.endswith('identities'): identity = json.loads(raw)
    else: matched = json.loads(raw)
normal = lambda value: re.sub(r'[-_.]+', '-', value).lower()
population = {normal(r['name']): r['version'] for r in identity['dependencies']}
assert population == {normal(r['name']): r['version'] for r in wheels['members']}
assert identity['manager_version'] == '3.0.5rc1' and len(matched['members']) == 13
manager = {'kind': 'stdo.external-manager-qualification/1', 'version': '3.0.5rc1', 'release_version': '3.0.5-rc.1', 'workspace': str(X),
    'manager': ref(X / 'manager/bin/stdo'), 'source_member_count': 13, 'dependencies_exact': True, 'selected_distribution_population': population,
    'dependency_selection': ref(downloads / 'runtime/WHEELS.json'), 'identities': ref(O / 'manager-operations/external-manager-identities/stdout.txt'),
    'source_match': ref(O / 'manager-operations/external-manager-source-match/stdout.txt'),
    'python': {'invocation': str(X / 'manager/bin/python'), 'executable_realpath': str((X / 'manager/bin/python').resolve()), 'sha256': sha(Path(PY).read_bytes()), 'version': '3.13.7'}}
save(O / 'MANAGER.json', manager)
pin = expected['stdo-v3.0.5-rc.1-manifest.json'][0]
install_raw, install_receipt = run('native-public-install', [str(X / 'manager/bin/stdo'), '--store', str(X / 'store'), 'install', 'v3.0.5-rc.1', '--repository', 'https://github.com/foolishimp/specification_methodology.git', '--manifest-sha256', pin])
verify_raw, verify_receipt = run('native-public-verify', [str(X / 'manager/bin/stdo'), '--store', str(X / 'store'), 'verify', 'v3.0.5-rc.1', '--manifest-sha256', pin])
install, verify = json.loads(install_raw), json.loads(verify_raw)
native = X / 'store/releases/v3.0.5-rc.1'
assert install['status'] == 'installed' and install['manifest_sha256'] == pin and install['path'] == str(native)
assert verify['valid'] is True and verify['failures'] == [] and verify['manifest_sha256'] == pin and verify['cut'] == 'v3.0.5-rc.1'
assert install['release']['commit'] == prior['native_commit'] and install['release']['tag_object'] == prior['native_tag_object']
selection = load(R / prior['source_selection']['path'])
# Native identity is checked against the sealed exact Git tree, including modes.
published_native = load(downloads / 'stdo-v3.0.5-rc.1-manifest.json')
tree = subprocess.check_output(['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', 'ls-tree', '-r', '-z', prior['native_commit'] + ':' + published_native['release']['project_subtree_root']], cwd=R)
expected_members = {}
for item in tree.split(b'\0'):
    if not item: continue
    meta, name = item.split(b'\t', 1); mode, kind, oid = meta.decode().split()
    assert kind == 'blob' and mode in ('100644', '100755')
    expected_members[name.decode()] = (mode, oid)
actual = {str(p.relative_to(native)): p for p in native.rglob('*') if p.is_file()}
assert len(actual) == 174 and set(actual) == set(expected_members) | {'manifest.json'}
members = []
for name, path in sorted(actual.items()):
    assert not path.is_symlink()
    raw = path.read_bytes(); mode = '100755' if path.stat().st_mode & 0o111 else '100644'
    if name == 'manifest.json': assert sha(raw) == pin
    else:
        assert mode == expected_members[name][0]
        assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == expected_members[name][1]
    members.append({'path': name, 'sha256': sha(raw), 'bytes': len(raw), 'mode': mode})
attestation = save(O / 'NATIVE_ATTESTATION.json', {'kind': 'stdo.public-native-byte-attestation/1', 'status': 'verified', 'native_root': str(native), 'native_commit': prior['native_commit'], 'manifest_sha256': pin, 'files': len(members), 'members': members})
handoff = dict(prior)
handoff.update({'kind': 'stdo.public-native-qualification-handoff/1', 'workspace': str(X), 'store': str(X / 'store'), 'native_root': str(native), 'manager': manager,
    'native_manifest': ref(downloads / 'stdo-v3.0.5-rc.1-manifest.json'), 'transport_mode': 'public_readback',
    'acquisition': {'mode': 'public_readback', 'repository': 'https://github.com/foolishimp/specification_methodology.git'},
    'install': install_receipt, 'verify': verify_receipt, 'installed_byte_attestation': attestation,
    'public_readback': {'carrier': carrier, 'release_id': release['id'], 'acquisition': acquisition, 'external_manifest': ref(downloads / forms['external_manifest_asset']['name'])},
    'routes': {k: v.replace(prior['workspace'], str(X)) for k, v in prior['routes'].items()},
    'limits': 'Actual anonymous five-asset acquisition, exact published recipe, fresh manager/native installation and 174-member attestation. Runtime, fixed interfaces, proof and public gate remain pending; no adoption or new LLM/Context trial.'})
result = save(O / 'HANDOFF.json', handoff)
print('HANDOFF', result['sha256'], flush=True)
