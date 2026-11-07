"""Join only closed current public observations; no new qualification execution."""
import hashlib
import json
from pathlib import Path
R = Path.cwd()
C = Path(__file__).resolve().parent
O = C.parent.parent / 'public-qualification-001'
def load(p): return json.loads(p.read_bytes())
def ref(p):
    b = p.read_bytes()
    return {'path': str(p.relative_to(R)), 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}
manifest = load(R / 'stack_release.json')
handoff = load(O / 'HANDOFF.json')
aggregate_path = O / 'cohort/evidence/complete_installed_cohort.json'
aggregate = load(aggregate_path)
assert aggregate['status'] == 'passed' and len(aggregate['component_evidence']) == 14
proof = load(O / 'executions/installed-full-current-verify/execution.json')
inspection = load(O / 'executions/installed-full-owner-inspection/execution.json')
assert proof['execution']['returncode'] == inspection['execution']['returncode'] == 0
assert load(R / proof['result']['path'])['status'] == 'verified'
assert load(R / inspection['result']['path'])['status'] == 'consistent'
assert load(O / 'proof-retention/COMPLETION.json')['status'] == 'passed'
assert load(O / 'installed-owner-checks/COMPLETION.json')['status'] == 'passed'
assert load(O / 'ACQUISITION.json')['status'] == 'verified'
external = manifest['publication']['external_manifest_asset']
download = Path(handoff['public_readback']['external_manifest']['path'])
if not download.is_absolute(): download = R / download
assert download.read_bytes() == (R / 'stack_release.json').read_bytes()
record = {'kind': 'stdo.public-cohort-readback/1', 'status': 'verified', 'unauthenticated': True,
    'source_identity_sha256': manifest['source']['source_identity_sha256'], 'carrier': handoff['public_readback']['carrier'],
    'release_id': handoff['public_readback']['release_id'], 'assets': manifest['publication']['assets'],
    'external_manifest': {**external, 'sha256': ref(R / 'stack_release.json')['sha256']},
    'fresh_store': handoff['store'], 'installed_manifest_sha256': handoff['native_manifest']['sha256'],
    'installed_qualification': ref(aggregate_path), 'handoff': ref(O / 'HANDOFF.json'), 'acquisition': ref(O / 'ACQUISITION.json'),
    'proof_transport': ref(O / 'proof-retention/COMPLETION.json'),
    'limits': 'Anonymous acquired exact fixed RC1 release and all five assets; fresh manager/native/source installation, current fixed host interfaces/MCP/Graphify, fresh support and actual full structural proof, owner inspection, documentation checks and independent file-browser observation. Third-party dependencies were acquired through verified independent APFS cache clones, not asserted network-fresh. Source operations retain their original execution and preservation-based semantic scope. No new LLM/Context trial, universal behavior, semantic completeness or Product adoption is asserted. Public gate and Latest are later operations.'}
path = O / 'PUBLIC_READBACK.json'
with path.open('x') as f: json.dump(record, f, indent=2, sort_keys=True); f.write('\n')
print(json.dumps(ref(path)))
