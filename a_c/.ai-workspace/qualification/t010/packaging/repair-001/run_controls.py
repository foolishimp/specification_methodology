"""Focused synthetic controls; never construct the final common proposal."""
from __future__ import annotations
import ast
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
from types import SimpleNamespace

sys.dont_write_bytecode = True
BASE = Path('/Users/jim/src/apps/specification_methodology/a_c')
APP = BASE / 'applications/stdo-v3-common-35fb4824'
PROOF = BASE / '.ai-workspace/qualification/t010/packaging/repair-001'
WORK = Path(tempfile.mkdtemp(prefix='ac-common-release-receipts-'))
UPSTREAM = Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
spec = importlib.util.spec_from_file_location('repaired_common_packager', APP / 'package_release.py')
pkg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pkg
spec.loader.exec_module(pkg)
checks, receipts = pkg.checks, pkg.receipts


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + '\n')


old = checks.load(BASE / '.ai-workspace/qualification/t010/package-review/first-controls.json')
fixture = Path(old['scratch']) / 'synthetic-proposal'
proposal = WORK / 'synthetic-proposal'
proposal.mkdir()
for name in receipts.ARTIFACTS:
    shutil.copyfile(fixture / name, proposal / name)
assert checks.sha((proposal / 'model.json').read_bytes()) == checks.sha((fixture / 'model.json').read_bytes())
bindings = pkg.receipt_bindings(SimpleNamespace(proposal=proposal, graph=proposal / 'graph.json'))['bindings']
accounts = WORK / 'accounts'
accounts.mkdir()
report = accounts / 'bounded-report.md'
report.write_text('# Synthetic binding control\n\nThis is a packaging fixture, not an actual common semantic review.\n')
construction = {'kind': receipts.CONSTRUCTION, 'receipt_id': 'urn:test:common:construction-receipt',
                'issuer': 'urn:test:common:construction-fixture', 'bindings': bindings,
                'scope': 'Synthetic14-record mechanical packaging fixture only; not a final common representation.',
                'details': {'fixture': 'Recorded synthetic input; no F_P construction or acceptance claimed.'},
                'construction_state': 'complete', 'private_material_included': False}
review = {'kind': receipts.REVIEW, 'receipt_id': 'urn:test:common:bounded-review-receipt',
          'issuer': 'urn:test:common:review-fixture', 'bindings': bindings,
          'scope': 'Synthetic receipt custody control only; not a common semantic assessment.',
          'details': {'fixture': 'Explicit synthetic test account; no independent semantic review claimed.'},
          'review_state': 'closed', 'outcome': 'Synthetic positive contract fixture.',
          'independence': {'relation': 'Synthetic test data; no reviewer-independence claim.'},
          'reports': [{'path': report.name, 'bytes': report.stat().st_size, 'sha256': checks.sha(report.read_bytes())}]}
public_path, review_path = accounts / 'construction.json', accounts / 'review.json'
save(public_path, construction)
save(review_path, review)


def args(directory, public=public_path, reviewed=review_path):
    return SimpleNamespace(upstream=UPSTREAM, proposal=proposal, graph=proposal / 'graph.json',
                           public_evidence=public, review=[reviewed],
                           bundle=directory / 'bundle' / pkg.ARTIFACT, dist=directory / 'dist', display_limit=7)


positive = pkg.build(args(WORK / 'positive'))
assert positive['status'] == 'local_bundle_prepared' and positive['checks']['public_evidence']['bounded_review_receipts'] == 1
bundle = Path(positive['bundle'])
second = pkg.build(args(WORK / 'another-location/deeper'))
assert positive['archive']['sha256'] == second['archive']['sha256']
extracted = WORK / 'fresh-extraction'
extracted.mkdir()
with tarfile.open(WORK / 'positive/dist' / (pkg.ARTIFACT + '.tar.gz')) as archive:
    archive.extractall(extracted, filter='data')
extracted_bundle = extracted / pkg.ARTIFACT
replay = subprocess.run([str(BASE / '.venv/bin/python3'), '-B', str(extracted_bundle / 'release_tools/bundle_check.py'), str(extracted_bundle)],
                        cwd=WORK, capture_output=True, text=True)
assert replay.returncode == 0, replay.stderr
replayed = json.loads(replay.stdout)

constructor_controls = []


def change_at(value, path, replacement):
    target = value
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = replacement


mutations = [
    ('other_source', ('bindings', 'source', 'subject_id'), 'urn:other:source'),
    ('other_commit', ('bindings', 'source', 'commit'), '0' * 40),
    ('stale_semantic_inventory', ('bindings', 'source', 'semantic_files_sha256'), '0' * 64),
    ('stale_section_inventory', ('bindings', 'source', 'section_inventory_sha256'), '0' * 64),
    ('stale_source_reentry', ('bindings', 'source', 'source_reentry_sha256'), '0' * 64),
    ('other_model', ('bindings', 'model', 'id'), 'urn:other:model'),
    ('stale_canonical_model', ('bindings', 'model', 'sha256'), '0' * 64),
    ('stale_raw_export', ('bindings', 'artifacts', 'graph.json', 'sha256'), '0' * 64),
]
for kind, base_value in [('construction', construction), ('review', review)]:
    for label, path, replacement in mutations:
        directory = WORK / 'constructor-negatives' / (kind + '-' + label)
        directory.mkdir(parents=True)
        bad = copy.deepcopy(base_value)
        change_at(bad, path, replacement)
        bad_path = directory / (kind + '.json')
        save(bad_path, bad)
        if kind == 'review':
            shutil.copyfile(report, directory / report.name)
        options = args(directory, public=bad_path if kind == 'construction' else public_path,
                       reviewed=bad_path if kind == 'review' else review_path)
        try:
            pkg.build(options)
            raise AssertionError('constructor accepted ' + kind + '-' + label)
        except ValueError as exc:
            assert not options.bundle.exists(), 'receipt refusal occurred after bundle creation'
            constructor_controls.append({'case': kind + '-' + label, 'status': 'refused_before_effects', 'reason': str(exc)})

for label, operation in [
    ('standalone_markdown', lambda d: report),
    ('missing_binding', lambda d: {key: value for key, value in review.items() if key != 'bindings'}),
    ('untyped_review', lambda d: {**review, 'kind': 'synthetic-model-review'}),
    ('incomplete_review', lambda d: {**review, 'review_state': 'partial'}),
]:
    directory = WORK / 'constructor-negatives' / label
    directory.mkdir(parents=True)
    value = operation(directory)
    target = value if isinstance(value, Path) else directory / 'review.json'
    if not isinstance(value, Path):
        save(target, value)
        shutil.copyfile(report, directory / report.name)
    options = args(directory, reviewed=target)
    try:
        pkg.build(options)
        raise AssertionError('constructor accepted ' + label)
    except ValueError as exc:
        assert not options.bundle.exists()
        constructor_controls.append({'case': label, 'status': 'refused_before_effects', 'reason': str(exc)})

changed_report_directory = WORK / 'constructor-negatives/changed-report'
changed_report_directory.mkdir(parents=True)
save(changed_report_directory / 'review.json', review)
(changed_report_directory / report.name).write_bytes(report.read_bytes() + b'Changed body.\n')
options = args(changed_report_directory, reviewed=changed_report_directory / 'review.json')
try:
    pkg.build(options)
    raise AssertionError('constructor accepted changed report')
except ValueError as exc:
    assert not options.bundle.exists()
    constructor_controls.append({'case': 'changed_report_body', 'status': 'refused_before_effects', 'reason': str(exc)})


def reindex(root):
    release_path = root / 'RELEASE.json'
    release = checks.load(release_path)
    public = root / 'evidence/authoring-public.json'
    if public.exists():
        release['public_authoring_receipt_sha256'] = checks.sha(public.read_bytes())
    for row in release['review_receipts']:
        path = root / row['path']
        if path.exists():
            row['sha256'] = checks.sha(path.read_bytes())
    save(release_path, release)
    inventory = checks.load(root / 'inventory.json')
    names = [name for name in checks.files(root) if name not in ('inventory.json', 'SHA256SUMS')]
    inventory['files'] = [{'path': name, 'bytes': (root / name).stat().st_size,
                           'sha256': checks.sha((root / name).read_bytes())} for name in names]
    save(root / 'inventory.json', inventory)
    (root / 'SHA256SUMS').write_text(''.join(f'{checks.sha((root / name).read_bytes())}  {name}\n'
                                          for name in sorted(names + ['inventory.json'])))


portable_controls = []
for label, path, replacement in mutations:
    for kind, name in [('construction', 'evidence/authoring-public.json'),
                       ('review', 'evidence/reviews/review-001/receipt.json')]:
        root = WORK / 'portable-negatives' / (kind + '-' + label)
        shutil.copytree(bundle, root)
        receipt_path = root / name
        value = checks.load(receipt_path)
        change_at(value, path, replacement)
        save(receipt_path, value)
        reindex(root)
        try:
            checks.check(root)
            raise AssertionError('portable checker accepted ' + kind + '-' + label)
        except (ValueError, KeyError, TypeError, OSError) as exc:
            portable_controls.append({'case': kind + '-' + label, 'status': 'refused_after_inventory_reindex', 'reason': str(exc)})

for label in ['removed_construction', 'removed_review', 'removed_report', 'changed_report_body', 'stale_raw_result', 'removed_all_review_index', 'missing_review_binding', 'missing_receipt_contract']:
    root = WORK / 'portable-negatives' / label
    shutil.copytree(bundle, root)
    if label == 'removed_construction':
        (root / 'evidence/authoring-public.json').unlink()
    elif label == 'removed_review':
        (root / 'evidence/reviews/review-001/receipt.json').unlink()
    elif label == 'removed_report':
        (root / 'evidence/reviews/review-001/bounded-report.md').unlink()
    elif label == 'changed_report_body':
        target = root / 'evidence/reviews/review-001/bounded-report.md'
        target.write_bytes(target.read_bytes() + b'Changed body.\n')
    elif label == 'stale_raw_result':
        target = root / 'result.json'
        value = checks.load(target)
        value['claim'] = 'Changed raw result after receipts were frozen.'
        save(target, value)
    elif label == 'removed_all_review_index':
        target = root / 'RELEASE.json'
        value = checks.load(target)
        value['review_receipts'] = []
        save(target, value)
    elif label == 'missing_review_binding':
        target = root / 'evidence/reviews/review-001/receipt.json'
        value = checks.load(target)
        del value['bindings']
        save(target, value)
    elif label == 'missing_receipt_contract':
        target = root / 'RELEASE.json'
        value = checks.load(target)
        del value['public_receipt_contract']
        save(target, value)
    reindex(root)
    try:
        checks.check(root)
        raise AssertionError('portable checker accepted ' + label)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        portable_controls.append({'case': label, 'status': 'refused_after_inventory_reindex', 'reason': str(exc)})

for path in [APP / 'package_release.py', APP / 'release_tools/bundle_check.py', APP / 'release_tools/public_receipts.py']:
    ast.parse(path.read_text())
result = {'status': 'passed', 'fixture': 'Synthetic14-record source-coordinate packaging control only; no final common model/bundle/archive',
          'work': str(WORK), 'positive': positive, 'fresh_extracted_cli': replayed,
          'deterministic_archive_second_build_sha256': second['archive']['sha256'],
          'constructor_controls': constructor_controls, 'portable_controls': portable_controls,
          'browser_or_server_started': False, 'native_model_calls': 0}
save(PROOF / 'controls.json', result)
print(json.dumps({'status': 'passed', 'work': str(WORK), 'constructor_negative_cases': len(constructor_controls),
                  'portable_negative_cases': len(portable_controls), 'clean_extracted_cli': replayed['status'],
                  'deterministic_archive_sha256': second['archive']['sha256']}, indent=2))
