"""Independent readback of a sealed local native cut; no Git mutations."""
from pathlib import Path, PurePosixPath
import hashlib
import importlib.metadata
import json
import os
import stat
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from jsonschema import Draft202012Validator, FormatChecker
import stdo_toolchain
from stdo_toolchain.manifest import verify_materialization

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
WORK = ROOT / 'specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY'
RUN = WORK / 'native-release/release-run-01'
A = '44448b14ecc9c5636d0e7972c7a4f1a80a07c623'
C = '23ca9c0929d7be8570edafaf30542e3daeb8dc1f'
T = 'd03b00a7fdf8972dc236b52eb09f3eccba7f62cb'
PARENT = 'fe4941f56a52ed3697a2b516d8d68948b0ea65d9'
M = 'f7f3f824ee1ac3e048d1b1ea86ce3aae84866e2e9d5010fe5eda2e38e12f4477'
COMMON = 'specification_methodology/v3/build_tenants/common/'
NATIVE = 'specification_methodology/v3/'

def digest(raw): return hashlib.sha256(raw).hexdigest()
def sha(path): return digest(path.read_bytes())
def read(path): return json.loads(path.read_bytes())
def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, check=True, capture_output=True).stdout
def text_git(*args): return git(*args).decode().strip()
def canonical(value): return (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
def checked_rows(rows):
    for row in rows:
        data = (ROOT / row['path']).read_bytes()
        assert digest(data) == row['sha256'], row['path']
        if 'bytes' in row: assert len(data) == row['bytes'], row['path']
def tree_rows(coordinate):
    result = {}
    for row in git('ls-tree', '-r', '-z', coordinate).split(b'\0'):
        if not row: continue
        prefix, path = row.split(b'\t', 1)
        mode, kind, oid = prefix.decode().split()
        assert kind == 'blob' and mode in ('100644', '100755')
        result[path.decode()] = (mode, oid)
    return result

proof_path = RUN / 'LOCAL_PROOF.json'
assert sha(proof_path) == '45c77f72db25cf1ab4aa75c652f50e23770402135f2d67fe4dcc6afe0a97ff9b'
proof = read(proof_path); checked_rows(proof['files']); assert len(proof['files']) == 195
selection = read(RUN / 'SOURCE_SELECTION.json')
assert sha(RUN / 'SOURCE_SELECTION.json') == '0b0e94fe5e81f0c6905065e5424c182dc2b3191f51659efb96d212b55dd1261e'
assert sha(RUN / 'installed-local.json') == 'a3b51ca75aa7ca16f43dafb8a928ee58d0aa672416094964fe91fb8276a1e8f9'
assert selection['native'] == proof['native']
assert selection['source_candidate']['commit'] == A and selection['native']['commit'] == C
assert text_git('rev-parse', A + ':' + COMMON.rstrip('/')) == selection['source_candidate']['package_tree']
assert text_git('rev-parse', C + ':' + NATIVE.rstrip('/')) == selection['source_candidate']['package_tree']
commit = git('cat-file', '-p', C).decode()
assert [line[7:] for line in commit.split('\n\n', 1)[0].splitlines() if line.startswith('parent ')] == [PARENT]
assert text_git('rev-parse', C + '^{tree}') == 'c64345a9b2127df3cddc0e26f49bc9dac2a24bff'
assert text_git('rev-parse', 'refs/tags/specification_methodology/v3.0.2') == T
tag = git('cat-file', '-p', T).decode()
head, annotation = tag.split('\n\n', 1)
assert ('object ' + C) in head.splitlines()
assert 'type commit' in head.splitlines() and 'tag specification_methodology/v3.0.2' in head.splitlines()
assert [line for line in annotation.splitlines() if line.lstrip().startswith('STDO-Release-Profile:')] == ['STDO-Release-Profile: stable-v1']
assert annotation.encode() == (RUN / 'tag-message.txt').read_bytes()
refs = text_git('for-each-ref', '--format=%(refname) %(objectname)', 'refs/tags/v3.0.2*', 'refs/tags/specification_methodology/v3.0.2*').splitlines()
assert refs == ['refs/tags/specification_methodology/v3.0.2 ' + T]

# Bind the entire native payload to the union of the closed semantic/code cuts.
reviewed = {}
for path, expected in [
    (ROOT / 'specification_methodology/v3/.ai-workspace/work/PRODUCT_COMPOSITION_IMPLEMENTATION_01/common/CANDIDATE-repair1.json', '49782c5a616cb4c12ad2ef95d28d6fd7f5a60546d329cd37a8380f998f9728bd'),
    (WORK / 'method/METHOD-02.json', '7c3928c6d31d08cee9d1d0da4a2f062bd191fa04c08925a551b80a4e98a3f1b9'),
    (WORK / 'manager/CANDIDATE-repair1.json', 'e3c5302012ac9cfdc2413096976a9ba2ae49e408b0d01f47320edd21ae1fd50d')]:
    assert sha(path) == expected
    for row in read(path)['files']:
        if row['path'].startswith(COMMON): reviewed[row['path'].removeprefix(COMMON)] = row['sha256']
source_tree = tree_rows(A + ':' + COMMON.rstrip('/'))
native_tree = tree_rows(C)
assert set(source_tree) == set(reviewed) == {row['path'] for row in selection['files']}
assert len(source_tree) == 86
assert native_tree == {NATIVE + path: value for path, value in source_tree.items()}
for row in selection['files']:
    mode, oid = source_tree[row['path']]
    raw = git('cat-file', 'blob', oid)
    assert (mode, oid) == (row['git_mode'], row['git_blob'])
    assert len(raw) == row['bytes'] and digest(raw) == row['sha256'] == reviewed[row['path']]
vector = [{key: row[key] for key in ('path', 'bytes', 'sha256')} for row in selection['files']]
assert digest(json.dumps(vector, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()) == selection['inventory_sha256']

manifest_raw = (RUN / 'stdo-v3.0.2-manifest.json').read_bytes()
manifest = json.loads(manifest_raw)
assert digest(manifest_raw) == M and canonical(manifest) == manifest_raw
assert manifest['release']['profile'] == 'stable-v1'
for key in ['cut', 'commit', 'tag_object', 'tree', 'standards_tree', 'qualified_ref']:
    assert manifest['release'][key] == selection['native'][key]
assert manifest['release']['project_subtree_root'] == NATIVE.rstrip('/')
assert manifest['release']['project_subtree_tree'] == selection['native']['package_tree']
installed = RUN / 'local-store/releases/v3.0.2'
expected = {row['path']: (row['bytes'], row['sha256']) for row in selection['files']}
expected['manifest.json'] = (len(manifest_raw), M)
actual = {}
for path in installed.rglob('*'):
    mode = path.lstat().st_mode
    assert not stat.S_ISLNK(mode)
    if stat.S_ISDIR(mode): continue
    assert stat.S_ISREG(mode)
    actual[path.relative_to(installed).as_posix()] = (path.stat().st_size, sha(path))
assert actual == expected
Draft202012Validator(read(installed / 'standards/schemas/installed-release-manifest.schema.json'), format_checker=FormatChecker()).validate(manifest)
assert verify_materialization(installed, manifest) == []
assert read(RUN / 'verify-local.json')['manifest'] == manifest
assert read(RUN / 'verify-local.json')['valid'] is True
assert read(RUN / 'verify-local.json')['failures'] == []
for check in read(RUN / 'URI_CHECKS_LOCAL.json')['checks']:
    path = Path(check['installed_path'])
    relative = path.relative_to(installed).as_posix()
    assert check['uri'] == 'stdo://releases/v3.0.2/' + relative
    assert sha(path) == check['sha256'] == expected[relative][1]
    assert json.loads(check['response']) == {'path': str(path), 'uri': check['uri']}

manager = read(RUN / 'MANAGER_LOCAL.json')
assert Path(stdo_toolchain.__file__).resolve() == Path(manager['import']['module'])
assert importlib.metadata.version('stdo-toolchain') == '0.1.6'
assert 'site-packages' in Path(stdo_toolchain.__file__).parts
assert sha(Path(manager['wheel'])) == 'ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242'
with zipfile.ZipFile(manager['wheel']) as wheel:
    for name in wheel.namelist():
        if name.startswith('stdo_toolchain/') and name.endswith('.py'):
            assert (Path(stdo_toolchain.__file__).parent.parent / name).read_bytes() == wheel.read(name)
log_counts = {}
for name in ['manager-local-operations.json', 'local-install-operations.json', 'supplement-asset-operations.json']:
    operations = read(RUN / name)['operations']
    for row in operations:
        assert row['exit'] == 0
        for stream in ['stdout', 'stderr']:
            assert sha(RUN / row[stream + '_path']) == row[stream + '_sha256']
        if name != 'supplement-asset-operations.json':
            assert row['environment']['PYTHONPATH'] == row['environment']['PYTHONHOME'] == 'absent'
    log_counts[name] = len(operations)

assets_path = RUN / 'assets.json'
assert sha(assets_path) == 'bdcd9a2b64f64071cb1bd9cf480825b45cfce2c4777b66536145a801e936d758'
assets = read(assets_path); asset_rows = {row['name']: row for row in assets['files']}
assert assets['selection_sha256'] == sha(RUN / 'SOURCE_SELECTION.json')
primaries = ['stdo-v3.0.2-manifest.json', 'stdo_toolchain-0.1.6-py3-none-any.whl', 'stdo-v3.0.2-composition-release-supplement.tar.gz']
assert set(asset_rows) == set(primaries + [name + '.sha256' for name in primaries])
for row in assets['files']:
    path = Path(row['path']); assert not path.is_symlink()
    assert sha(path) == row['sha256'] and path.stat().st_size == row['bytes']
for name in primaries:
    assert Path(asset_rows[name + '.sha256']['path']).read_text() == asset_rows[name]['sha256'] + '  ' + name + '\n'

archive = Path(asset_rows[primaries[-1]]['path'])
payload = {}
with tarfile.open(archive, 'r:gz') as tar:
    for member in tar:
        path = PurePosixPath(member.name)
        assert member.isfile() and member.mode == 0o644 and not path.is_absolute() and '..' not in path.parts
        assert path.parts[0] == 'stdo-v3.0.2-supplement'
        name = '/'.join(path.parts[1:]); assert name and name not in payload
        payload[name] = tar.extractfile(member).read()
assert payload['SOURCE_SELECTION.json'] == (RUN / 'SOURCE_SELECTION.json').read_bytes()
assert payload['NATIVE_MANIFEST.json'] == manifest_raw
representation = read(WORK / 'REPRESENTATION-01.json')
for row in representation['files']:
    prefix = 'specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/representation/'
    name = row['path'].removeprefix(prefix)
    assert digest(payload[name]) == row['sha256']
for name in ['standards/PRODUCT_DEFINITION.md', 'standards/RELEASE.md']:
    assert digest(payload['source/' + name]) == reviewed[name]
assert payload['source/LICENSE'] == git('cat-file', 'blob', source_tree['LICENSE'][1])
assert digest(payload['supplement.py']) == '9c2249f9495b748680e2978380906707662eec0c089de7784615f9952c29b7b5'
assert digest(payload['tools/ac_graph.py']) == '2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667'

with tempfile.TemporaryDirectory(prefix='stdo302-independent-portable-') as temporary:
    root = Path(temporary); bundle = root / 'bundle'; cwd = root / 'empty'; cwd.mkdir(); bundle.mkdir()
    for name, raw in payload.items():
        path = bundle / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
    env = dict(os.environ); env.pop('PYTHONHOME', None); env['PYTHONPATH'] = '/nonexistent-reviewer-poison'; env['PYTHONDONTWRITEBYTECODE'] = '1'
    argv = [sys.executable, '-I', '-S', '-B', str(bundle / 'supplement.py'), 'verify', '--bundle', str(bundle)]
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stderr
    portable = json.loads(result.stdout)
    assert portable['selection_sha256'] == sha(RUN / 'SOURCE_SELECTION.json')
    assert all(json.loads(command['stdout'])['model']['sha256'] == 'b3f97a2667c277c21417230421aca02c26b3a7b19baa598197e94f67c5439151' for command in portable['commands'])
    portable_receipt = {'argv': argv, 'cwd': str(cwd), 'environment': {'PYTHONPATH':'/nonexistent-reviewer-poison','PYTHONHOME':'absent'}, 'exit': result.returncode, 'result': portable}

checked_rows(proof['files'])
result = {'local_proof_sha256': sha(proof_path), 'files_verified': len(proof['files']),
          'native_source_A': A, 'native_commit_C': C, 'native_tag_T': T, 'native_manifest_M': M,
          'closed_review_union_members': len(reviewed), 'native_payload_members': len(source_tree),
          'native_modes_blobs_and_full_root_equal': True, 'installed_files_including_manifest': len(actual),
          'schema_and_materialization': 'passed', 'URI_checks': 4, 'operation_log_counts': log_counts,
          'asset_inventory_sha256': sha(assets_path), 'assets_verified': len(asset_rows),
          'supplement_archive_sha256': sha(archive), 'supplement_members': len(payload),
          'reviewed_representation_members_equal': len(representation['files']), 'portable': portable_receipt,
          'limits': 'Local cut/install/asset readiness only; no remote publication or public reacquisition performed by this review.'}
with (HERE / 'RESULTS.json').open('x') as output:
    json.dump(result, output, indent=2); output.write('\n')
print(json.dumps({k:v for k,v in result.items() if k != 'portable'}, indent=2))
