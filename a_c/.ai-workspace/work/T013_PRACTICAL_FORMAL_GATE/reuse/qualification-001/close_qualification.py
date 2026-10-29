"""Check the retained qualification results and freeze this Worker's return."""
from pathlib import Path
import hashlib
import json
import sys
import types
from datetime import datetime, timezone

Q = Path(__file__).resolve().parent
BASE = Q.parents[1]
AC = BASE.parents[2]
ROOT = AC / 'build_tenants/lean'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def write(name, value):
    with (Q / name).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write('\n')


def inventory(directory):
    members = {}
    for path in sorted(directory.rglob('*')):
        assert not path.is_symlink(), path
        if path.is_file():
            members[path.relative_to(directory).as_posix()] = sha(path)
    return members


assert not (Q / 'CLOSED.json').exists()
prepared = read(Q / 'CONTROLS-PREPARED.json')
assert inventory(Q / 'small-cold') == prepared['original_bundle_members']
controls = []
for case in prepared['controls']:
    label = 'control-' + case['control']
    external = read(Q / (label + '.external.json'))
    result = external['returned']
    assert result['status'] == case['expected_status']
    assert external['returncode'] == case['expected_exit']
    assert result['reason'] == case['expected_reason']
    assert external['origin_before'] == external['origin_after']
    assert external['origin_after']['entry_count'] == 2
    assert external['origin_after']['pending_count'] == 0
    assert not (Q / label).exists(), label
    assert not result.get('observations', {}).get('stages', [])
    controls.append({'control': case['control'], 'status': result['status'],
                     'reason': result['reason'], 'exit': external['returncode'],
                     'external_seconds': external['external_invocation_seconds'],
                     'output_directory_created': False,
                     'entry_count_after': 2,
                     'external_receipt_sha256': sha(Q / (label + '.external.json')),
                     'proof_cost_evidence': 'Early refusal before output/deciding work; minimal results do not invent absent invocation counters.'})
write('CONTROLS.json', {'schema': 'a_c.T013.public-controls/1', 'status': 'passed',
                       'controls': controls, 'original_cold_bundle_unchanged': True,
                       'private_entries_mutated': False})

pins = read(BASE / 'reuse/integration-001/SOURCE-PINS.json')
for group in ('after', 'conserved_source_pins'):
    for name, digest in pins[group].items():
        assert sha(AC / name) == digest, name
qualifier = types.ModuleType('qualification_final')
qualifier.__file__ = str(Q / 'qualify.py')
qualifier.__package__ = ''
sys.modules[qualifier.__name__] = qualifier
exec(compile((Q / 'qualify.py').read_bytes(), qualifier.__file__, 'exec', dont_inherit=True), qualifier.__dict__)
adapter = qualifier.adapter()
current = adapter.select_checker(ROOT, qualifier.PYTHON, 600)
assert current == read(Q / 'checker.json'), 'Selected full checker configuration changed'
assert current['runtime_identity'] == read(Q / 'RUNTIME-IDENTITY.json')
origin = qualifier.origin_counts()
assert origin['entry_count'] == 2 and origin['pending_count'] == 0
write('FINAL-CURRENTNESS.json', {
    'schema': 'a_c.T013.qualification-currentness/1', 'status': 'passed',
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'integrated_pin_count': len(pins['after']),
    'conserved_pin_count': len(pins['conserved_source_pins']),
    'integration_source_pins_sha256': sha(BASE / 'reuse/integration-001/SOURCE-PINS.json'),
    'selected_configuration_equal': True,
    'checker_sha256': sha(Q / 'checker.json'),
    'full_runtime_identity': current['runtime_identity']['sha256'],
    'origin_metadata_only': origin,
    'origin_key_or_private_entry_body_recorded': False})

small, full = read(Q / 'SMALL.json'), read(Q / 'FULL.json')
assert small['status'] == full['status'] == 'passed'
labels = ['small-cold', 'small-reuse-1', 'small-reuse-2', 'full-cold', 'full-reuse']
runs = []
for label in labels:
    result = read(Q / label / 'result.json')
    external = read(Q / (label + '.external.json'))
    assert result == external['returned']
    assert result['status'] == 'verified'
    assert result['runtime_identity'] == current['runtime_identity']
    assert external['external_invocation_seconds'] < 600
    stages = result['observations']['stages']
    assert all(stage['seconds'] < 90 for stage in stages if 'exit_code' in stage)
    runs.append({'label': label, 'external_seconds': external['external_invocation_seconds'],
                 'internal_checking_seconds': result['observations']['elapsed_seconds'],
                 'external_child_high_water_rss_bytes': external['child_high_water_rss_bytes'],
                 'launcher_high_water_rss_bytes': external['parent_high_water_rss_bytes'],
                 'current_compiler_invocations': result['observations']['current_dynamic_proof_invocations'],
                 'current_kernel_replay_invocations': result['observations']['current_kernel_replay_invocations'],
                 'current_runtime_invocations': result['observations']['current_runtime_invocations'],
                 'stages': stages})
large = [{'path': path.relative_to(Q).as_posix(), 'bytes': path.stat().st_size,
          'sha256': sha(path)} for path in sorted(Q.rglob('*'))
         if path.is_file() and path.stat().st_size > 100 * 1024 * 1024]
write('OVERSIZED-EVIDENCE.json', {'schema': 'a_c.T013.qualification-oversized-evidence/1',
      'files': large, 'bytes_preserved': True,
      'transport_or_ignore_changes_by_this_worker': False,
      'handoff': 'Checkpoint Writer must cover these exact additional public proof artifact paths before remote publication.'})
write('MEASUREMENTS.json', {
    'schema': 'a_c.T013.reuse-measurements/1', 'runs': runs,
    'compiler_limits': {'seconds_per_checking_process': 90, 'lean_memory_mb': 4096,
                        'public_seconds': 600, 'physical_rss_ceiling': False},
    'scope': 'Each launcher is a fresh isolated process. External interval includes adapter validation, actual CLI execution and final publication; excludes writing its external receipt. Internal intervals exclude final bundle/origin publication. Darwin child ru_maxrss is aggregate high-water for that invocation, not stage attribution. leanchecker has no memory flag.',
    'full_measured_cold_over_reuse_ratio': runs[3]['external_seconds'] / runs[4]['external_seconds'],
    'general_performance_claim': False,
    'quiet_sequential_proof_window': True})

report = f'''# T013 actual reuse qualification — Worker return

The integrated candidate passed two fresh cold proofs, three authenticated reuse
checks and five targeted public refusal controls. Source and selected full runtime
identity remained exact. No production source or private entry was edited.

| Actual subject | Cold | Reuse | Further reuse |
|---|---:|---:|---:|
| Six-record carrier and supplied view | {runs[0]['external_seconds']:.3f}s | {runs[1]['external_seconds']:.3f}s | {runs[2]['external_seconds']:.3f}s |
| Complete 1,987-record model and supplied nine-record view | {runs[3]['external_seconds']:.3f}s | {runs[4]['external_seconds']:.3f}s | Not selected |

Times cover the complete public invocation, including final evidence/origin
publication. Each cold run performed seven generated compiler checks, one fresh
kernel replay and one actual specialized runtime. Every checking stage finished
within 90 seconds and every public invocation within 600 seconds. All reuse hits
performed zero current compiler, replay or runtime invocations, while rechecking
current source/import/certificates, support, authenticated artifacts and full
model/view correspondence. Reuse-of-reuse points directly to the original cold
entry; it does not create an evidence chain or another private establishment.

Full input correspondence covers all 1,987 records, 1,021 external resolutions,
16,498 references and 3,995 edges. The supplied view retains indices
`[0,9,10,664,666,866,867,869,1825]`, one unresolved residual and 18 external boundaries.
Actual output uses `projectWithProof` with freshly checked premises and a
kernel-replayed equality to unchanged `project`. The original raw `checkModel`
timeout remains a recorded limitation; this run does not claim it became fast.

Fresh public `init-origin` was invoked exactly once, before these cold runs. Only
their successful cold completion established the two current entries. No prior
proof was retrospectively signed. Public identity is
`{current['runtime_identity']['sha256']}`; selection is frozen in `checker.json`.
No key bytes or private entry bodies are retained here. The original public cold
bundle remains unchanged; adversarial copies have ordinary copied bytes.

All five controls refused before output-directory creation: omitted unresolved
residual, altered runtime payload and integer-to-boolean context change (with
public hashes refreshed) failed exact local establishment binding; a recomputed
non-origin stale source pin failed compatibility; a boolean budget failed typed
request validation. These are actual public CLI results. Early minimal results
do not expose invocation counters, so the evidence records their early path and
absence of generated output rather than fabricating counters. Private entry count
remained two, with no pending entry.

Memory remains material. Full cold child high-water RSS was
{runs[3]['external_child_high_water_rss_bytes']:,} bytes
({runs[3]['external_child_high_water_rss_bytes'] / 1024**3:.2f} GiB); full reuse was
{runs[4]['external_child_high_water_rss_bytes']:,} bytes
({runs[4]['external_child_high_water_rss_bytes'] / 1024**3:.2f} GiB). These are
Darwin aggregate child high-water observations for separate public invocations,
not per-stage measurements. Compiler `-M4096` is not an OS physical RSS ceiling;
the kernel checker has no memory flag. The measured full pair is
{runs[3]['external_seconds'] / runs[4]['external_seconds']:.2f} times faster on reuse.
This single pair establishes a useful local result, not a general benchmark.

The exact original mathematical omitted-view/budget refusal evidence is conserved;
no redundant full adverse proof was run here. Existing established support was
checked, not rebuilt or re-established. The Worker ran no actor/model call,
Context, preflight or dispatch. Qualification-only context metadata is not actual
delivery evidence.

Independent assessment of this cut, actual task delivery, an origin-free extracted
package check, final packaging/transport, and acceptance remain for their owners.
`OVERSIZED-EVIDENCE.json` identifies four new public proof files needing remote
transport coverage. Their bytes have been preserved. No Git action, ignore edit,
source-package archive or release was performed. All selected runs completed
without an unexpected production failure or repeat.

The Worker closes this increment and returns live runtime ownership to Executive.
'''
with (Q / 'FINAL_RETURN.md').open('x', encoding='utf-8') as stream:
    stream.write(report)
members = inventory(Q)
assert 'PINS.json' not in members and 'CLOSED.json' not in members
write('PINS.json', {'schema': 'a_c.T013.qualification-pins/1', 'members': members})
write('CLOSED.json', {
    'schema': 'a_c.T013.reuse-qualification-closure/1', 'status': 'worker-complete',
    'closed_utc': datetime.now(timezone.utc).isoformat(),
    'pins_sha256': sha(Q / 'PINS.json'),
    'return_sha256': sha(Q / 'FINAL_RETURN.md'),
    'activation_sha256': sha(Q / 'ACTIVATION.json'),
    'runtime_identity': current['runtime_identity']['sha256'],
    'checker_sha256': sha(Q / 'checker.json'),
    'small_sha256': sha(Q / 'SMALL.json'), 'full_sha256': sha(Q / 'FULL.json'),
    'controls_sha256': sha(Q / 'CONTROLS.json'),
    'currentness_sha256': sha(Q / 'FINAL-CURRENTNESS.json'),
    'measurements_sha256': sha(Q / 'MEASUREMENTS.json'),
    'oversized_evidence_sha256': sha(Q / 'OVERSIZED-EVIDENCE.json'),
    'live_runtime_ownership': 'returned to /root',
    'independent_review_or_acceptance': 'not established by Worker closure'})
print(json.dumps({'closure_sha256': sha(Q / 'CLOSED.json'),
                  'pins_sha256': sha(Q / 'PINS.json'),
                  'return_sha256': sha(Q / 'FINAL_RETURN.md'),
                  'currentness_sha256': sha(Q / 'FINAL-CURRENTNESS.json'),
                  'oversized_files': large}, sort_keys=True))
