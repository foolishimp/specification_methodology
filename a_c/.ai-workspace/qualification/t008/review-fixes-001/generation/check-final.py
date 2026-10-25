"""Owned closure proof; reads frozen studies and writes only this proof subtree."""
from pathlib import Path
import datetime
import difflib
import hashlib
import importlib.util
import json
import subprocess
import sys

ROOT = Path('/Users/jim/src/apps/specification_methodology/a_c')
PROOF = ROOT / '.ai-workspace/qualification/t008/review-fixes-001/generation'
TEMP = Path((PROOF / 'temp-root.txt').read_text().strip())
UPSTREAM = Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    (PROOF / name).write_text(json.dumps(value, indent=2) + '\n')

before = json.loads((PROOF / 'preimages.json').read_text())
after = []
diff = []
for entry in before:
    rel = entry['path']
    path = ROOT / rel
    saved = PROOF / 'preimages' / rel
    assert sha(saved) == entry['sha256']
    target = PROOF / 'source-after' / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(path.read_bytes())
    after.append({'path': rel, 'sha256': sha(path), 'bytes': path.stat().st_size})
    diff.extend(difflib.unified_diff(saved.read_text().splitlines(keepends=True), path.read_text().splitlines(keepends=True),
                                   fromfile='preimage/' + rel, tofile='after/' + rel))
save('source-after.json', after)
(PROOF / 'source.diff').write_text(''.join(diff))
source_pins = {entry['path']: entry['sha256'] for entry in after}
run = json.loads((PROOF / 'focused-002.json').read_text())
assert run['exit_code'] == 0
assert 'Ran 67 tests' in (PROOF / run['stderr']).read_text()
assert 'skipped=' not in (PROOF / run['stderr']).read_text()
run['source_pins'] = source_pins
save('focused-002.json', run)

frozen_before = json.loads((PROOF / 'frozen-studies-before.json').read_text())
frozen_after = [{'path': str(path.relative_to(ROOT)), 'sha256': sha(path), 'bytes': path.stat().st_size}
                for path in sorted((ROOT / 'dogfood').rglob('*')) if path.is_file()]
save('frozen-studies-after.json', frozen_after)
assert frozen_before == frozen_after
save('frozen-study-guard.json', {'status': 'satisfied', 'existing_files': len(frozen_before), 'after_files': len(frozen_after),
                              'changed': [], 'added': [], 'removed': [], 'all_dogfood_bytes_unchanged': True})

sys.path.insert(0, str(ROOT / 'build_tenants/graphify/code'))
import ac_generate as current
spec = importlib.util.spec_from_file_location('ac_generation_saved_preimage', TEMP / 'preimage-regressions/code/ac_generate.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
compatibility = []
for path in sorted((ROOT / 'dogfood/stdo-v3-generation-rc9/runs-v2').glob('*/*/plan.json')):
    plan, chunks = old.checkpoint(path.parent)
    assert plan['runner_sha256'] == '7002a7942f612f5a11e2a69dc865849ffef51c29c7b0cab9feb5170fb32d0479'
    try:
        current.checkpoint(path.parent)
    except current.GenerationError as exc:
        assert str(exc) == 'runner changed since preparation; create a new plan'
        new_refusal = str(exc)
    else:
        raise AssertionError('changed generator accepted old frozen plan')
    model = path.parent / 'repaired-proposal/model.json'
    compatibility.append({'plan': str(path.relative_to(ROOT)), 'old_engine_checkpoint': 'passed', 'chunks': len(chunks),
                          'new_engine_checkpoint': 'refused', 'refusal': new_refusal, 'model': str(model.relative_to(ROOT)),
                          'model_file_sha256': sha(model)})
assert len(compatibility) == 4
save('frozen-engine-boundary.json', compatibility)

commands = {}
for name, command in {
    'diff_check': ['git', 'diff', '--check', '--', *source_pins],
    'head': ['git', 'rev-parse', 'HEAD'],
    'upstream_head': ['git', '-C', str(UPSTREAM), 'rev-parse', 'HEAD'],
    'upstream_status': ['git', '-C', str(UPSTREAM), 'status', '--porcelain=v1', '--untracked-files=all'],
    'worktree_status': ['git', 'status', '--short', '--branch', '--untracked-files=normal'],
}.items():
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    commands[name] = {'command': command, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    assert result.returncode == 0
assert commands['head']['stdout'].strip() == 'bfe228511415d346459523cec44e7e8157e2991a'
assert commands['upstream_head']['stdout'].strip() == 'fe085cedddde3a18554f8749b230bfe47f3dcce7'
assert commands['upstream_status']['stdout'] == ''
save('final-read-checks.json', commands)
(PROOF / 'status-after.txt').write_text(commands['worktree_status']['stdout'])

baseline = json.loads((PROOF / 'preimage-regressions-001.json').read_text())
assert baseline['exit_code'] == 1
closure = {
    'status': 'CLOSED', 'actor': '/root/fix_ac_generation', 'role': 'Worker',
    'closed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reentry': 'realization_refactor', 'head': commands['head']['stdout'].strip(), 'source_pins': source_pins,
    'claims': {
        'ordinary_custody': 'Shared gate authenticates exact stage-specific frozen prompt, source/schema/assets/code, retained raw evidence, settings/argv/isolation/events/usage, and recomputed source validation before reuse.',
        'latest_attempt': 'Newer unfinished/failed attempts prevent older success reuse; explicit retry remains required. F_D source-validation-failed recovery does not relabel original success.',
        'fence_partition': 'Same marker, closing width >= opening width, at most three leading spaces, and trailing horizontal whitespace only; preserves source characters and lawful heading identities.',
        'unicode_coordinates': 'Recover-anchor offset mapping uses the same splitlines convention as preparation and strict validation, including U+2028/U+2029, with invariant non-grounding payload and SectionId.',
    },
    'performed_checks': {
        'initial_focused': {'tests': 66, 'skipped': 4, 'exit_code': 0, 'evidence': 'focused-001.json'},
        'preimage_sensitivity': {'tests': 3, 'expected_failures': 12, 'expected_errors': 2, 'exit_code': 1, 'evidence': 'preimage-regressions-001.json'},
        'final_focused': {'tests': 67, 'skipped': 0, 'exit_code': 0, 'actual_upstream_cases': 4, 'evidence': 'focused-002.json'},
        'frozen_studies': {'files': len(frozen_before), 'changed': 0, 'added': 0, 'removed': 0, 'evidence': 'frozen-study-guard.json'},
        'frozen_engine_boundary': {'old_preimage_checkpoint_passes': 4, 'new_generator_correctly_refuses_old_frozen_plans': 4, 'evidence': 'frozen-engine-boundary.json'},
        'diff_check': {'exit_code': 0, 'evidence': 'final-read-checks.json'},
    },
    'limits': [
        'Focused affected-source qualification only; no full suite was run by this Worker.',
        'All actor artifacts are synthetic; no native, model, provider, vendor, network, installation or global configuration effects.',
        'Actual upstream emitted retained cache-root-switch RuntimeWarnings while crossing temporary test roots in one process; all four boundary assertions passed.',
        'No frozen source/model/carrier/receipt/plan/hash or historical study regeneration; new engine qualification is separate from old frozen engine evidence.',
        'No F_P semantic corrections, semantic-fidelity/acceptance/full-calculus/release claim; owner disposition remains separate.',
        'Whole worktree is pre-existing dirty and concurrently modified by other granted Workers; only the six granted source files and this proof/temp territory were written here.',
    ],
    'exploratory_read_errors': [
        {'command': 'cat build_tenants/graphify/test_env/pyproject.toml', 'exit_code': 1, 'reason': 'No such optional configuration file; no effect.'},
        {'command': 'git -C /private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv rev-parse HEAD', 'exit_code': 128, 'reason': 'Container directory was not checkout root; verified child checkout afterward.'},
    ],
    'next_owner': 'Executive /root for integration and independent assessment; Worker stops after this closed return.',
}
save('CLOSED.json', closure)
lines = ['Generation repair Worker CLOSED.\n\n',
         'The three assigned realization defects are repaired in the six granted files. `ac_generate.actor_evidence` is shared with grounding and handles author versus extraction schema/prompt/source contracts without circular imports. Latest-attempt selection preserves retries and prevents an older success from hiding a failed or active newer attempt. Ordinary reuse cannot consume source-failed drafts; F_D recovery retains its original narrow allowance and immutable failures/usage.\n\n',
         'The fence partitioner retains opening marker/width and accepts only lawful same-marker closing lines. Grounding recovery maps exact offsets through the same splitlines convention used by preparation and strict validation. Tests preserve source characters, heading identities, same SectionId, and all non-grounding F_P content.\n\n',
         'Validation: 67 focused generation/grounding/repair tests passed with zero skips, including four actual pinned-upstream trials. The three primary regressions fail against saved preimage engines in scratch (expected exit 1; 12 assertions and 2 Unicode errors). Raw logs, commands, exits, source preimages, final source copies, and the complete diff are retained here.\n\n',
         f'Frozen guard: all {len(frozen_before):,} existing dogfood files remain byte-identical, with no additions or removals. Each of the four RC9 plans still passes checkpoint under the saved old generator; the new generator correctly refuses all four unchanged old plans because its runner digest differs. No plan/hash was refreshed to fit the repaired engine.\n\n',
         'No full suite, real actor/model/native/provider call, semantic correction, Git mutation, install, release or acceptance action was performed. The pinned upstream checkout remains clean. Its cache-root-switch RuntimeWarnings are retained in the passing focused-run log. Whole-worktree cleanliness is not claimed.\n\n',
         'Final SHA-256 values:\n\n']
lines.extend(f"- `{rel}`: `{value}`\n" for rel, value in source_pins.items())
lines.append('\nAuthority, exact grant, triage and installed basis were recorded in `activation.json` before source effects. Executive integration and independent assessment remain outside this closed Worker result.\n')
(PROOF / 'REPORT.md').write_text(''.join(lines))
print(json.dumps({'status': 'CLOSED', 'source_pins': source_pins, 'focused_tests': 67, 'skips': 0,
                  'frozen_studies_unchanged': len(frozen_before), 'frozen_rc9_engine_boundary': compatibility,
                  'proof': str(PROOF)}, indent=2))
