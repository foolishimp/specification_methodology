"""Bind the existing local native transaction to the reviewed RC1 package."""
import hashlib, json, os, stat, subprocess
from pathlib import Path

R = Path.cwd()
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W = Q / 'release-tools'
O = W / 'native-transaction-001'
P = W / 'packaging-001'
D = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_DELIVERY'
X = Path('/Users/jim/.local/share/stdo-qualification/v3.0.5-rc.1/local-001')
N = Q / 'native-release/cut-001'
sha = lambda raw: hashlib.sha256(raw).hexdigest()

def load(p):
    return json.loads(p.read_bytes())

def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': sha(raw), 'bytes': len(raw)}

def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as out:
        json.dump(value, out, indent=2, sort_keys=True)
        out.write('\n')
    return ref(p)

old = load(D / 'cohort-recovery-020/DRAFT_OPERATIONS.json')
old_external = '/Users/jim/.local/share/stdo-qualification/v3.0.5/local-004'
replacements = [
    (str(D / 'cohort-recovery-020'), str(O)),
    (str(D / 'native-release/local-qualification-003/native-index'), str(O / 'native-index')),
    (str(D / 'native-release/cut-004'), str(N)),
    (str(D / 'native-preparation-config.json'), str(P / 'native-configuration.json')),
    ('18885c62f93e9c384c9ade39fe00e4786342e82683859adb966ca5506ef71353', ref(P / 'native-configuration.json')['sha256']),
    (str(D / 'manager/runtime-preparation-001/wheels'), str(X / 'manager-runtime/wheels')),
    (str(D / 'manager/runtime-preparation-001/requirements-macos-arm64-cp313.txt'), str(X / 'manager-runtime/requirements-macos-arm64-cp313.txt')),
    (str(D / 'manager/dist/stdo_toolchain-3.0.5-py3-none-any.whl'), str(W / 'manager-001/dist/stdo_toolchain-3.0.5rc1-py3-none-any.whl')),
    (old_external, str(X)),
    ('stdo_toolchain.__version__=="3.0.5"', 'stdo_toolchain.__version__=="3.0.5rc1"'),
    ('refs/tags/specification_methodology/v3.0.5', 'refs/tags/specification_methodology/v3.0.5-rc.1'),
]

def translate(value):
    if isinstance(value, str):
        for before, after in replacements:
            value = value.replace(before, after)
        return 'v3.0.5-rc.1' if value == 'v3.0.5' else value
    if isinstance(value, list):
        return [translate(item) for item in value]
    if isinstance(value, dict):
        return {key: translate(item) for key, item in value.items()}
    return value

commands = []
for previous in old['commands']:
    if previous['id'] in ('stage', 'whitespace', 'checkpoint-C', 'qualification-handoff'):
        continue
    command = translate(previous)
    command = {key: value for key, value in command.items() if key in ('id', 'argv', 'environment', 'stdin_path', 'stdout_path', 'transport_mode')}
    if command['id'] == 'native-candidate-tag-CAS':
        command['id'] = 'native-RC-tag-create-only'
        command['argv'][-1] = '0' * 40
        command['precondition'] = 'Selected RC1 ref absent locally and remotely; all former 3.0.5 tag objects remain exact. No selector or archive ref moves in this local transaction.'
    if command['id'] == 'native-annotated-tag-object':
        command['stdin_template'] = 'object ${A}\ntype commit\ntag specification_methodology/v3.0.5-rc.1\ntagger ${committer_ident}\n\n${exact newly prepared cut-001/tag-message.txt bytes}'
        command['precondition'] = 'New annotation must bind actual C2, current package tree and native parent 16bc30d215915a4b7b3ed2f13e52e14510ae1c9d; no predecessor cut annotation.'
    commands.append(command)

manager = load(W / 'manager-001/BUILD.json')
extract = {
    'id': 'manager-runtime-extract',
    'operation': 'Read the exact 25-member selected ZIP; reject traversal, duplicate or nonregular members; write the absent external manager-runtime directory; require each of 21 WHEELS members digest/size and version 3.0.5-rc.1 / Python distribution 3.0.5rc1. No ambient dependency selection.',
    'archive': manager['runtime_archive'], 'destination': str(X / 'manager-runtime')}
commands.insert(0, extract)
native_inventory = load(P / 'NATIVE_INPUT_INVENTORY.json')['files']

def tree_hash(rows):
    tree = {}
    for path, mode, blob in rows:
        parts = path.split('/')
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = (mode, blob)
    def encode(node):
        entries = []
        for name, value in node.items():
            if isinstance(value, dict):
                mode, blob = '40000', encode(value)
                sort_name = name + '/'
            else:
                mode, blob = value
                sort_name = name
            entries.append((sort_name.encode(), mode.encode() + b' ' + name.encode() + b'\0' + bytes.fromhex(blob)))
        raw = b''.join(item[1] for item in sorted(entries))
        return hashlib.sha1(b'tree ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    return encode(tree)

native_rows = []
for row in native_inventory:
    p = R / 'specification_methodology/v3/build_tenants/common' / row['path']
    raw = p.read_bytes()
    assert sha(raw) == row['sha256'] and len(raw) == row['bytes']
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    native_rows.append((row['path'], row['git_mode'], blob))
package_tree = tree_hash(native_rows)
root_tree = tree_hash([('specification_methodology/v3/' + path, mode, blob) for path, mode, blob in native_rows])
value = {'kind': 'stdo.rc-native-local-transaction-operations/1', 'version': '3.0.5-rc.1',
    'source_checkpoint_preimage': '32567ff27a6a2e86ebce7a4e949729881372a1ab',
    'expected_package_tree': package_tree, 'expected_native_tree': root_tree,
    'native_parent': '16bc30d215915a4b7b3ed2f13e52e14510ae1c9d',
    'configuration': ref(P / 'native-configuration.json'), 'payload_freeze': ref(P / 'FREEZE.json'),
    'payload_validation': ref(P / 'PAYLOAD_VALIDATION.json'), 'manager_build': ref(W / 'manager-001/BUILD.json'),
    'external_root': str(X), 'native_run': str(N), 'commands': commands,
    'dynamic_bindings': 'C2/A/native tree/tag object/manifest and selection digests derive only from successful actual prior outputs.',
    'preconditions': ['Exact reviewed source/package pins and selected staged set', 'Main/index preimages match; external local-001 and native cut-001 absent ordinary paths', 'At least 2 GiB free for this bounded checkpoint/install; no compiler or broad maintenance concurrently', 'Native RC1 ref absent; preserve old selectors and every unrelated ref'],
    'effects': 'One exact main checkpoint then local RC native cut/tag and fresh external manager/store install. No remote push, selector/archive replacement, four peer tags or GitHub effects in this transaction.',
    'qualification_handoff': 'After exact installed bytes and manager verification, reactivate Tools with actual native/manifest/manager/store under the existing fixed-interface qualification grant.'}
print(json.dumps(save(O / 'OPERATIONS.json', value)))
