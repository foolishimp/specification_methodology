"""Record exact already-authored subjects for the proposed internal RC7 frames."""
from pathlib import Path
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
DEST = OUT / 'frame-proposals'
DEST.mkdir(exist_ok=True)

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

cohort = json.loads((ROOT / 'stack_release.json').read_text())
rows = []
for child in ('axiom_indexer', 'stdo_representation'):
    paths = [ROOT / child / 'specification/PRODUCT.md', ROOT / child / 'specification/INTENT.md']
    paths += sorted((ROOT / child / 'specification/requirements').glob('*.md'))
    paths += [ROOT / child / 'specification/REFERENCE_FRAME_BASIS.md', ROOT / child / ( 'stdo_default.json' if child == 'axiom_indexer' else 'stdo_representation.json')]
    for path in paths:
        rows.append({'path': str(path.relative_to(ROOT)), 'sha256': sha(path)})
    current = ROOT / child / '.ai-workspace/decisions/20260906_rc6_frame_basis_acceptance.json'
    decision = json.loads(current.read_text())
    assert decision['subject_sha256'] == 'sha256:' + sha(ROOT / child / 'specification/REFERENCE_FRAME_BASIS.md')
    rows.append({'path': str(current.relative_to(ROOT)), 'sha256': sha(current)})
program_root = ROOT / 'stdo_representation/build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7'
for path in sorted(program_root.iterdir()):
    if path.is_file(): rows.append({'path': str(path.relative_to(ROOT)), 'sha256': sha(path)})
value = {'kind': 'stdo.rc7-frame-selection-subject', 'status': 'unaccepted-construction-subject',
    'stage_a_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
    'source_stdo': cohort['products']['specification_methodology'],
    'axiom_candidate': cohort['products']['axiom_indexer'],
    'representation_candidate': cohort['products']['stdo_representation'],
    'native_task_sha256': sha(OUT / 'native-task.md'),
    'source_and_dependency_repair': 'Three source members change; three Executive clauses and one index are authored, steel support expands; one Axiom executable restores existing symlink-loop/output preservation. No new mechanics contract.',
    'owning_source_and_inputs': rows,
    'live_binding': 'Both peer Definitions and accepted frame decisions remain RC6. STDO source project stays RC4. This record does not activate proposed RC7 configuration.',
    'exclusions': ['independent semantic acceptance', 'Product acceptance', 'publication', 'external adoption', 'unobserved Python/runtime/native reliability']}
target = DEST / 'selection-subject.json'
assert not target.exists(), 'Preserve a prior subject'
target.write_text(json.dumps(value, indent=2) + '\n')
print(json.dumps({'path': str(target.relative_to(ROOT)), 'sha256': sha(target)}))
