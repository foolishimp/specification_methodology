"""Hash only selected new public evidence; no origin/library/compiled-object reads."""
from pathlib import Path
import hashlib
import json

R = Path(__file__).resolve().parent
W = R.parents[1]
BASE = W / 'real-use/runtime-preparation-003'
hashes = {}
def load(path):
    return json.loads(path.read_bytes())
def check(path, expected=None, size=None):
    assert 'formal-origin-v1' not in path.parts
    with path.open('rb') as f:
        actual = hashlib.file_digest(f, 'sha256').hexdigest()
    if expected is not None: assert actual == expected, str(path)
    if size is not None: assert path.stat().st_size == size, str(path)
    hashes[str(path.relative_to(W))] = {'sha256': actual, 'bytes': path.stat().st_size}
    return actual
selected = [('execution-001', 'e4c7455ed963c88115158a0919d960e6866b65b4d2148ecab6c610c67b57c6e2',
             'd5a1202279f441bfb8f0ab1f8f459008822230371bc4ca68ee33364e30234820'),
            ('execution-002', '87c01ee10aa3f7b4cdd13bc579fdad16663efb12a8a66243a1b9ac802aa6810d',
             '53c183ae956496f5c7096946e71f246a8e051a7a284ff01a113ea9e58b6bed33')]
skipped = {}
for phase, closure, pins_hash in selected:
    d = BASE / phase
    check(d / 'CLOSED.json', closure); check(d / 'PINS.json', pins_hash)
    pins = load(d / 'PINS.json')
    for name, record in pins['members'].items():
        check(d / name, record['sha256'], record['bytes'])
    custody = load(d / ('PUBLIC-EVIDENCE-CUSTODY.json' if phase == 'execution-001' else 'operational/CUSTODY.json'))
    root = Path(custody['root'])
    members = custody.get('members', custody.get('public_members'))
    names = custody.get('new_members', custody.get('new_public_members'))
    for name in names:
        rec = members[name]
        if any(s in Path(name).name for s in ('.olean', '.ir')):
            skipped[str((root / name).relative_to(W))] = rec
            continue
        check(root / name, rec['sha256'], rec['bytes'])
    for name, rec in custody.get('transport_members', {}).items():
        check(root / name, rec['sha256'], rec['bytes'])
check(W / 'review/matched-quality-001/CLOSED.json', 'fa50735cf15fd1aa7f01a49b90b6b6ab905ee171b506b112ca7a3e262ce487c1')
report = {'schema': 'a_c.T013.independent-operation-selected-hashes/1', 'status': 'PASS',
          'members': hashes, 'members_hashed': len(hashes), 'bytes_hashed': sum(v['bytes'] for v in hashes.values()),
          'compiled_members_not_rehashed': skipped,
          'limits': 'Prior source/component/generic/reuse assessments conserved; no compiled artifact or external support recensus; no private origin reads'}
with (R / 'SELECTED-HASHES.json').open('x', encoding='utf-8') as f:
    f.write(json.dumps(report, sort_keys=True, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('status', 'members_hashed', 'bytes_hashed')}))
