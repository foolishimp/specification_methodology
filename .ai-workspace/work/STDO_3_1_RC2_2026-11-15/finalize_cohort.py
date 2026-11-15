"""Bind finite identity follow-up and exact final assets without changing the reviewed graph."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

p = argparse.ArgumentParser()
p.add_argument('--mechanical-readback', type=Path, required=True)
args = p.parse_args()
w = Path(__file__).resolve().parent
r = w.parents[2]
b = '4a7f7cdfcd724d6b2e47b3d790fa88030b70d84a'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_text())


plan = w / 'REF_PLAN.json'
assert sha(plan.read_bytes()) == '882bb34fda8770fc4ebebe5863a25688402de23f9d913341968eac82c15bbeee'
assert read(w / 'assessment/identity-01/VERDICT.json')['status'] == 'supported'
draft = read(w / 'COHORT_DRAFT.json')
final = read(w / 'COHORT_POST_REVIEW.json')
assert all(draft[k] == final[k] for k in draft if k != 'qualification')
for name in ['assessed-packaged/RESULT.json', 'PRODUCT_EXTRACTION.json']:
    path = w / name
    relative = path.relative_to(r).as_posix()
    committed = subprocess.check_output(['git', '-C', str(r), 'show', b + ':' + relative])
    assert committed == path.read_bytes()
    final['qualification']['evidence'].append({'commit': b, 'path': relative, 'sha256': sha(committed)})
mechanical_bytes = args.mechanical_readback.read_bytes()
final['qualification']['post_assessment_mechanical_readback'] = {
    'sha256': sha(mechanical_bytes),
    'standing': 'Finite independent-operator comparisons following the actual identity assessment; not a new independent semantic verdict.',
    'record': json.loads(mechanical_bytes)}
disposition = (w / 'IDENTITY_FINDINGS_DISPOSITION.md').read_bytes()
final['qualification']['release_actor_dispositions'] = {
    'sha256': sha(disposition), 'report': disposition.decode()}
assert all(draft[k] == final[k] for k in draft if k != 'qualification')
asset = w / 'assets/cohort-release-v3.1.0-rc.2.json'
assert not asset.exists()
asset.write_text(json.dumps(final, indent=2) + '\n')
selection = read(r / 'releases/3.1.0-rc.2/COHORT_INPUTS.json')
assets = []
for name in selection['assets']:
    path = w / 'assets' / name
    data = path.read_bytes()
    assets.append({'name': name, 'bytes': len(data), 'sha256': sha(data)})
for row in draft['assets']:
    assert row == next(item for item in assets if item['name'] == row['name'])
expected = w / 'EXPECTED_ASSETS.json'
expected.write_text(json.dumps({'kind': 'stdo.expected-public-assets/1', 'version': '3.1.0-rc.2', 'assets': assets}, indent=2) + '\n')
paths = [plan, expected, w/'PREPUBLICATION_QUALIFICATION.json',
         w/'assessment/identity-01/ASSESSMENT.md', w/'assessment/identity-01/EXECUTION.json',
         w/'assessment/identity-01/VERDICT.json', args.mechanical_readback.resolve(),
         w/'IDENTITY_FINDINGS_DISPOSITION.md', w/'TAG_INTERNAL_READBACK.json',
         w/'GITHUB_RELEASE_NOTES.md', w/'run_public_install.py', w/'close_public_readback.py']
paths += [w/'assets'/row['name'] for row in assets]
gate = {'kind': 'stdo.final-prepush-gate/1',
        'status': 'qualified-for-declared-prepublication-claims',
        'native': final['native']['commit'], 'carrier': b,
        'reviewed_ref_plan_sha256': sha(plan.read_bytes()),
        'ref_graph_sha256': final['ref_graph_sha256'],
        'draft_to_final_changes': ['qualification.post_tag_review',
                                   'qualification.evidence: two existing committed evidence bindings',
                                   'qualification.post_assessment_mechanical_readback',
                                   'qualification.release_actor_dispositions'],
        'product_and_ref_identity_fields_equal_reviewed_draft': True,
        'qualified_files': [{'path': str(path), 'sha256': sha(path.read_bytes())} for path in paths],
        'unperformed': ['Atomic remote publication', 'Normal GitHub release',
                        'Anonymous public acquisition and fresh install',
                        'Human exact-cut acceptance and consumer adoption remain separate']}
(w/'FINAL_PREPUSH_GATE.json').write_text(json.dumps(gate, indent=2) + '\n')
print(json.dumps({'assets': assets, 'graph': final['ref_graph_sha256'],
                  'plan_unchanged': True, 'gate_sha256': sha((w/'FINAL_PREPUSH_GATE.json').read_bytes())}))
