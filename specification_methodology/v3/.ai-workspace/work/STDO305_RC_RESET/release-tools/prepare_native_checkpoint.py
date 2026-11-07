"""Freeze the closed RC payload and exact local transaction path set."""
import hashlib, json, stat, subprocess
from pathlib import Path

R = Path.cwd()
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W, T = Q / 'release-tools', Q / 'tools-skills'
O = W / 'native-transaction-001'
sha = lambda raw: hashlib.sha256(raw).hexdigest()

def load(p):
    return json.loads(p.read_bytes())

def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': sha(raw), 'bytes': len(raw)}

def save(p, value):
    with p.open('x') as out:
        json.dump(value, out, indent=2, sort_keys=True)
        out.write('\n')
    return ref(p)

def git(*args):
    return subprocess.check_output(['git', '--no-optional-locks', *args], cwd=R)

assert not (O / 'PLAN.json').exists()
custody = T / 'evidence-custody-001/INDEX.json'
assert ref(custody)['sha256'] == '56150a40614666b6d32685340e51b8ba3b740be3fc5b78acf43b846979912d8f'
review_list = Path('/tmp/stdo305-rc-reset-review-K0KuCT/RC_PAYLOAD_CUSTODY_LIST.json')
assert sha(review_list.read_bytes()) == '39bf06e0ff6b60b735becffb0394f27a49ee9ea49a85328b2579ad7ad1a81660'
retained = W / 'review-custody-004'
retained.mkdir()
copies = []
for row in load(review_list):
    p = Path(row['path'])
    raw = p.read_bytes()
    assert sha(raw) == row['sha256'] and len(raw) == row['bytes']
    target = retained / p.name
    target.write_bytes(raw)
    copies.append({'original_path': str(p), 'retained': ref(target)})
(retained / review_list.name).write_bytes(review_list.read_bytes())
save(retained / 'CUSTODY.json', {'assessor': '/root/stdo305_integration_review', 'original_inventory': ref(retained / review_list.name), 'files': copies})

template = (W / 'source-checkpoint-002/execute.py').read_text()
template = template.replace('import hashlib,json,os,re,subprocess,time', 'import hashlib,json,os,re,subprocess,time,sys')
template = template.replace("assert sha(plan_raw)=='55aa4fe1953e7ef4ec8f068b015225f248ec851226d62b61abf395ff5164d46e'", 'assert sha(plan_raw)==sys.argv[1]')
template = template.replace("'/representation/stdo-v3.0.5-rc.1/source/' in name", "'/standards/documentation/' in name")
template = template.replace('One local main commit only; no refs/tags, push, publication, install or global configuration effects.', 'One local payload checkpoint; native/tag/local installation operations follow separately under OPERATIONS.json. No remote or global effects.')
template = template.replace('SOURCE_CHECKPOINT', 'PAYLOAD_CHECKPOINT')
(O / 'execute_checkpoint.py').write_text(template)

head = git('rev-parse', 'HEAD').decode().strip()
assert head == '32567ff27a6a2e86ebce7a4e949729881372a1ab'
assert git('symbolic-ref', 'HEAD').decode().strip() == 'refs/heads/main'
assert not git('diff', '--cached', '--name-only')
index = git('ls-files', '-s', '-z')
indexed = {}
for item in index.split(b'\0'):
    if item:
        metadata, name = item.split(b'\t', 1)
        mode, oid, stage = metadata.decode().split()
        assert stage == '0'
        indexed[name.decode()] = {'git_mode': mode, 'git_blob': oid}
selected = set()
excluded = [(W / 'packaging-001/archives/current.zip').relative_to(R).as_posix()]
for p in W.rglob('*'):
    if p.is_file():
        assert not p.is_symlink() and p.suffix != '.pyc', p
        name = p.relative_to(R).as_posix()
        if name not in excluded:
            selected.add(name)
source = load(W / 'materializer-review-004/FREEZE.json')['source']
for row in source:
    selected.add(row['path'])
    assert ref(R / row['path']) == {key: row[key] for key in ('path', 'sha256', 'bytes')}
for row in load(W / 'packaging-001/PRE_COPY_DELTA.json')['changed']:
    selected.add('specification_methodology/v3/build_tenants/common/' + row['after']['path'])
for row in load(custody)['eligible_files']:
    p = R / row['path']
    assert ref(p) == {key: row[key] for key in ('path', 'sha256', 'bytes')}
    assert ('100755' if p.stat().st_mode & 0o111 else '100644') == row['git_mode']
    selected.add(row['path'])
selected.add(custody.relative_to(R).as_posix())
rows = []
for name in sorted(selected):
    p = R / name
    mode = p.lstat().st_mode
    assert stat.S_ISREG(mode) and not p.is_symlink()
    raw = p.read_bytes()
    assert len(raw) < 100 * 1024**2, name
    row = {'path': name, 'bytes': len(raw), 'sha256': sha(raw), 'git_mode': '100755' if mode & 0o111 else '100644',
        'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(), 'preimage': indexed.get(name)}
    if row['preimage'] != {key: row[key] for key in ('git_mode', 'git_blob')}:
        rows.append(row)
outside = [row['path'] for row in rows if not row['path'].startswith(Q.relative_to(R).as_posix() + '/')]
assert len(outside) == 38, outside
source_ref = save(O / 'SOURCE_SELECTION.json', {'payload': ref(W / 'packaging-001/FREEZE.json'),
    'payload_review': ref(retained / 'RC_PAYLOAD_REVIEW_001.json'), 'materializer_review': ref(W / 'review-custody-003/MATERIALIZER_REVIEW_004.json'),
    'tools_custody': ref(custody), 'outside_work_paths': outside, 'excluded_exact': excluded,
    'excluded_by_custody': load(custody)['excluded_files'],
    'preserved_unselected': 'All inherited unrelated untracked work, external environments/private origins/dependency caches and old release assets/evidence remain untouched.',
    'ordinary_generated_duplicates': 'Selected generated copies are exact builder evidence; Git blob identity deduplicates equal payload bytes.'})
paths_ref = save(O / 'PATHS.json', {'files': rows, 'bytes': sum(row['bytes'] for row in rows), 'largest': max(rows, key=lambda row: row['bytes']), 'head': head, 'index_logical_sha256': sha(index)})
controls = [O / name for name in ('SOURCE_SELECTION.json', 'PATHS.json', 'stage-paths.z', 'PLAN.json')]
names = sorted([row['path'] for row in rows] + [p.relative_to(R).as_posix() for p in controls])
assert len(names) == len(set(names))
nul = b'\0'.join(name.encode() for name in names) + b'\0'
(O / 'stage-paths.z').write_bytes(nul)
plan = {'kind': 'stdo.reviewed-native-checkpoint-and-local-transaction/1',
    'authority': 'Owner authorized complete RC reset publication; Root standing grant explicitly covers OPERATIONS0270020d after matched reviewed source/payload identities. Independent payload review is satisfied.',
    'head': head, 'branch': 'refs/heads/main', 'index_logical_sha256': sha(index), 'source': source_ref, 'paths': paths_ref,
    'nul': ref(O / 'stage-paths.z'), 'stage_paths': len(names), 'commit_message': 'Package reviewed STDO 3.0.5-rc.1 native distribution',
    'operations': ref(O / 'OPERATIONS.json'), 'minimum_free_bytes': 2 * 1024**3,
    'effects': ['One exact main C2 checkpoint with sole parent C1', 'Execute fixed native operations with actual C2/tree/A/tag/manifest bindings; create-only local RC1 tag; fresh explicit external manager/store install', 'Notify Tools and independent reviewer with verified actual handoff'],
    'whitespace': 'Authored live errors stop; sealed historical/generated evidence whitespace is retained and classified.',
    'limits': 'No push, selector/archive replacement, peer tags or GitHub effect in this transaction. Current native/runtime qualification and publication remain separate.'}
result = save(O / 'PLAN.json', plan)
print(json.dumps({'plan': result, 'paths': paths_ref, 'nul': plan['nul'], 'stage_paths': len(names), 'bytes': sum(row['bytes'] for row in rows), 'outside_work_paths': len(outside)}, indent=2))
