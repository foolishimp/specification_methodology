"""Targeted actual-byte refusals and scratch repack; never edit sealed outputs."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
BASE = Path('/Users/jim/src/apps/specification_methodology/a_c')
APP = BASE / 'applications/stdo-v3-common-35fb4824'
PROOF = BASE / '.ai-workspace/qualification/t010/packaging/final-001'
state = json.loads((PROOF / 'extracted-stdlib-result.json').read_text())
BUNDLE = Path(state['bundle'])
WORK = Path(tempfile.mkdtemp(prefix='ac-common-release-final-tamper-'))
spec = importlib.util.spec_from_file_location('sealed_actual_packager_snapshot', BUNDLE / 'package_release.py')
pkg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pkg
spec.loader.exec_module(pkg)
checks, receipts = pkg.checks, pkg.receipts
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
archive = APP / 'dist/a_c-stdo-v3-common-35fb4824.tar.gz'
expected_archive = '2b33530c20a17dd27033e8b34b1af497de7a4e0f3b8165a22d0821298516e386'
assert sha(archive) == expected_archive
repacked = pkg.archive(BUNDLE, WORK / 'repacked-frozen-bytes.tar.gz')
assert repacked['sha256'] == expected_archive and repacked['bytes'] == 10087425
print(json.dumps({'control': 'scratch_repack_frozen_bytes', 'status': 'passed', 'sha256': repacked['sha256']}), flush=True)
ac = checks.codec(BUNDLE / 'codec/ac_graph.py')
model = ac.validate(ac.read_json(BUNDLE / 'model.json'))
expected = receipts.expected_bindings(BUNDLE, model, {name: BUNDLE / name for name in receipts.ARTIFACTS})
assert receipts.bundle_evidence(BUNDLE, expected)['bounded_review_receipts'] == 1
tampered = WORK / 'own-bundle-copy'
shutil.copytree(BUNDLE, tampered)
results = []


def reindex(root):
    release_path = root / 'RELEASE.json'
    release = checks.load(release_path)
    public = root / 'evidence/authoring-public.json'
    if public.exists():
        release['public_authoring_receipt_sha256'] = sha(public)
    for row in release['review_receipts']:
        path = root / row['path']
        if path.exists():
            row['sha256'] = sha(path)
    pkg.save(release_path, release)
    inventory = checks.load(root / 'inventory.json')
    names = [name for name in checks.files(root) if name not in ('inventory.json', 'SHA256SUMS')]
    inventory['files'] = [{'path': name, 'bytes': (root / name).stat().st_size, 'sha256': sha(root / name)} for name in names]
    pkg.save(root / 'inventory.json', inventory)
    (root / 'SHA256SUMS').write_text(''.join(f'{sha(root / name)}  {name}\n' for name in sorted(names + ['inventory.json'])))


def expect_receipt_refusal(name):
    reindex(tampered)
    try:
        receipts.bundle_evidence(tampered, expected)
        raise AssertionError('portable public-evidence gate accepted ' + name)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        results.append({'case': name, 'status': 'refused', 'property': 'Actual portable receipt/report gate after outer inventory and receipt-index hashes were regenerated', 'reason': str(exc)})


def restore(names):
    for name in names + ['RELEASE.json', 'inventory.json', 'SHA256SUMS']:
        (tampered / name).write_bytes((BUNDLE / name).read_bytes())


review_path = 'evidence/reviews/review-001/receipt.json'
value = checks.load(tampered / review_path)
value['bindings']['model']['sha256'] = '0' * 64
pkg.save(tampered / review_path, value)
expect_receipt_refusal('actual_review_wrong_model_binding')
restore([review_path])
report_path = 'evidence/reviews/review-001/REVIEW.md'
(tampered / report_path).write_bytes((tampered / report_path).read_bytes() + b'Changed review body.\n')
expect_receipt_refusal('actual_bound_review_report_changed')
restore([report_path])
public_path = 'evidence/authoring-public.json'
value = checks.load(tampered / public_path)
value['bindings']['source']['section_inventory_sha256'] = '0' * 64
pkg.save(tampered / public_path, value)
expect_receipt_refusal('actual_construction_stale_section_commitment')
restore([public_path])
(tampered / review_path).unlink()
expect_receipt_refusal('actual_bounded_review_receipt_removed')
restore([review_path])

command = [str(BASE / '.venv/bin/python3'), '-B', '-S', 'release_tools/bundle_check.py', '.']
(tampered / 'README.md').write_bytes((tampered / 'README.md').read_bytes() + b'Changed bundled guide.\n')
r = subprocess.run(command, cwd=tampered, capture_output=True, text=True)
(PROOF / 'tamper-inventory.stderr.json').write_text(r.stderr)
assert r.returncode == 2 and 'bundle bytes changed: README.md' in r.stderr, r.stderr
results.append({'case': 'actual_inventory_tamper', 'status': 'refused', 'interface': 'extracted Python-S checker CLI', 'returncode': r.returncode, 'reason': json.loads(r.stderr)['reason']})

carrier = checks.load(BUNDLE / 'carrier.json')
removed = next(row for row in carrier['nodes'] if row.get('ac_role') == 'reference-occurrence')
carrier['nodes'].remove(removed)
bad_carrier = WORK / 'one-occurrence-removed.carrier.json'
pkg.save(bad_carrier, carrier)
bad_output = WORK / 'refused-recovery.json'
command = [str(BASE / '.venv/bin/python3'), '-B', '-S', str(BUNDLE / 'codec/ac_graph.py'), 'decode', str(bad_carrier), '--out', str(bad_output)]
r = subprocess.run(command, cwd=WORK, capture_output=True, text=True, timeout=900)
(PROOF / 'tamper-carrier.stderr.json').write_text(r.stderr)
assert r.returncode == 2 and not bad_output.exists(), (r.returncode, r.stderr)
results.append({'case': 'actual_reference_occurrence_removed', 'status': 'refused', 'interface': 'extracted Python-S codec decode CLI', 'returncode': r.returncode, 'reason': json.loads(r.stderr)['reason'], 'removed_node': removed['id']})
assert sha(archive) == expected_archive
result = {'status': 'passed', 'scope': 'Actual sealed bytes; own-copy structural/receipt tamper checks and scratch repack only. No semantic assessment or changes to frozen outputs.',
          'work': str(WORK), 'deterministic_scratch_repack': repacked, 'negative_cases': results,
          'actual_archive_sha256_unchanged': sha(archive), 'browser_or_server_started': False, 'new_model_calls': 0}
(PROOF / 'tamper-and-determinism.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
