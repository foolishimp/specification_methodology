"""Factual handoff/link and immutable-byte guards only; no qualification replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess

BASE = Path('/Users/jim/src/apps/specification_methodology/a_c')
APP = BASE / 'applications/stdo-v3-common-35fb4824'
HERE = BASE / '.ai-workspace/qualification/t010/handoff'
FINAL = BASE / '.ai-workspace/qualification/t010/packaging/final-001'
BUNDLE = APP / 'bundle/a_c-stdo-v3-common-35fb4824'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require_file(path, expected):
    raw = path.read_bytes()
    assert sha(raw) == expected['sha256'], str(path)
    if 'bytes' in expected:
        assert len(raw) == expected['bytes'], str(path)


activation = json.loads((HERE / 'activation-and-root-decision.json').read_text())
verified = json.loads((FINAL / 'verified-inputs-and-guards.json').read_text())
closed = json.loads((FINAL / 'CLOSED.json').read_text())
for entry in activation['preimages']:
    require_file(HERE / entry['preserved_as'], entry)
for entry in activation['consumed_results']:
    require_file(BASE / entry['path'], entry)
for rel, expected_sha in verified['application_pins'].items():
    require_file(APP / rel, {'sha256': expected_sha})
require_file(APP / 'SOURCE-READINESS.md', {'sha256': '114a4580a344daa1cf32bcbc19246ab189c26b3f50b58d47c105ae7a2b54bd1d'})
for rel, expected in verified['sealed_artifacts']['artifacts'].items():
    require_file(APP / 'run/repaired-proposal' / rel, expected)
    require_file(BUNDLE / rel, expected)
review_dir = BASE / '.ai-workspace/qualification/t010/semantic-review/assessment-001'
require_file(review_dir / 'bounded-review.json', {'sha256': verified['review_receipt_sha256']})
for entry in verified['review_reports']:
    require_file(review_dir / entry['path'], entry)

custody = json.loads((APP / 'package-custody.json').read_text())
for entry in custody['members']:
    require_file(APP / 'source' / entry['path'], entry)
assert len(custody['members']) == 81

vector = json.loads((FINAL / 'sealed-bundle-files.json').read_text())
actual_files = sorted(p.relative_to(BUNDLE).as_posix() for p in BUNDLE.rglob('*') if p.is_file())
assert actual_files == sorted(x['path'] for x in vector)
for entry in vector:
    require_file(BUNDLE / entry['path'], entry)
assert len(vector) == 213
assert sum(x['bytes'] for x in vector) == 110470239
assert sha(json.dumps(vector, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()) == closed['bundle']['complete_file_vector_sha256']
for key in ['archive', 'external_checksum']:
    require_file(Path(closed[key]['path']), closed[key])

unrelated = verified['unrelated_guard']
require_file(BASE / unrelated['path'], unrelated)
guard = json.loads((BASE / unrelated['path']).read_text())
for rel, entry in guard['files'].items():
    require_file(BASE / rel, entry)
assert len(guard['files']) == 3913
for entry in verified['preexisting_tracked_modifications']:
    require_file(BASE.parent / entry['path'], entry)
assert len(verified['preexisting_tracked_modifications']) == 23
head = subprocess.run(['git', '--no-optional-locks', 'rev-parse', 'HEAD'], cwd=BASE.parent, check=True, capture_output=True).stdout.decode().strip()
assert head == verified['head']
tracked = subprocess.run(['git', '--no-optional-locks', 'status', '--porcelain=v1', '-z', '--untracked-files=no'], cwd=BASE.parent, check=True, capture_output=True).stdout
assert sha(tracked) == verified['tracked_status_sha256']

docs = [APP / 'README.md', APP / 'RELEASE-PREPARATION.md', BASE / '.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md']
links = []
doc_pins = []
for doc in docs:
    raw = doc.read_bytes()
    text = raw.decode()
    doc_pins.append({'path': str(doc), 'bytes': len(raw), 'sha256': sha(raw)})
    for label, target in re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', text):
        target = target.strip().split(' "', 1)[0].strip('<>')
        if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
            continue
        resolved = (doc.parent / target.split('#', 1)[0]).resolve()
        assert resolved.exists(), f'{doc}: {target}'
        links.append({'document': str(doc.relative_to(BASE)), 'label': label, 'target': target, 'exists': True})
    assert 'waiting for' not in text
    assert 'not_ready' in text
    assert 'unverified' in text.lower()
    assert '2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386' in text

result = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'passed',
    'scope': 'Three factual handoff documents, local links and immutable/unrelated guards only; no new qualification or artifact construction',
    'documents': doc_pins,
    'local_links': links,
    'local_links_resolved': len(links),
    'guards': {
        'application_frozen_inputs_and_code_pins': len(verified['application_pins']),
        'source_readiness_unchanged': True,
        'source_members_unchanged': 81,
        'source_manifests_unchanged': 3,
        'sealed_proposal_artifacts_unchanged': 5,
        'model_canonical_identity_conserved_by_unchanged_raw_artifact': verified['sealed_artifacts']['model'],
        'public_construction_receipt_and_review_receipt_unchanged': True,
        'bound_review_reports_unchanged': 4,
        'bundle_files_unchanged': len(vector),
        'bundle_bytes': sum(x['bytes'] for x in vector),
        'bundle_complete_file_vector_sha256': closed['bundle']['complete_file_vector_sha256'],
        'archive': closed['archive'],
        'external_checksum': closed['external_checksum'],
        'consumed_closures_and_review_unchanged': len(activation['consumed_results']),
        'guarded_existing_files_unchanged': len(guard['files']),
        'preexisting_tracked_modifications_unchanged': len(verified['preexisting_tracked_modifications']),
        'tracked_status_sha256_unchanged': sha(tracked),
        'head_unchanged': head,
        'no_whole_worktree_cleanliness_claim': True
    },
    'prohibited_effects_performed': [],
}
(HERE / 'checks.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'status': result['status'], 'documents': doc_pins, 'local_links_resolved': len(links), 'guarded_existing_files_unchanged': 3913, 'bundle_files_unchanged': 213, 'tracked_modifications_unchanged': 23, 'head': head}, indent=2))
