"""Focused captured-workspace documentation and conserved-binding controls."""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tarfile
import tempfile
from types import SimpleNamespace

sys.dont_write_bytecode = True
BASE = Path('/Users/jim/src/apps/specification_methodology/a_c')
APP = BASE / 'applications/stdo-v3-common-35fb4824'
PROOF = BASE / '.ai-workspace/qualification/t010/packaging/documentation-repair-001'
WORK = Path(tempfile.mkdtemp(prefix='ac-common-release-documentation-'))
UPSTREAM = Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-graphify-t008-upstream-w0b_fyxv/checkout')
spec = importlib.util.spec_from_file_location('portable_document_packager', APP / 'package_release.py')
pkg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pkg
spec.loader.exec_module(pkg)
checks = pkg.checks
prior = checks.load(BASE / '.ai-workspace/qualification/t010/packaging/repair-001/controls.json')
old_work = Path(prior['work'])
proposal, accounts = WORK / 'synthetic-proposal', WORK / 'accounts'
shutil.copytree(old_work / 'synthetic-proposal', proposal)
shutil.copytree(old_work / 'accounts', accounts)
public, review = accounts / 'construction.json', accounts / 'review.json'
expected = checks.load(public)['bindings']
bound = subprocess.run([sys.executable, '-B', str(APP / 'package_release.py'), 'receipt-bindings',
                        '--proposal', str(proposal), '--graph', str(proposal / 'graph.json')],
                       cwd=WORK, capture_output=True, text=True)
assert bound.returncode == 0, bound.stderr
assert json.loads(bound.stdout)['bindings'] == expected


def args(directory, review_path=review):
    return SimpleNamespace(upstream=UPSTREAM, proposal=proposal, graph=proposal / 'graph.json',
                           public_evidence=public, review=[review_path], bundle=directory / 'bundle' / pkg.ARTIFACT,
                           dist=directory / 'dist', display_limit=7)


first, second = pkg.build(args(WORK / 'first')), pkg.build(args(WORK / 'different/depth'))
assert first['archive']['sha256'] == second['archive']['sha256']
extracted = WORK / 'extracted'
extracted.mkdir()
with tarfile.open(WORK / 'first/dist' / (pkg.ARTIFACT + '.tar.gz')) as archive:
    archive.extractall(extracted, filter='data')
bundle = extracted / pkg.ARTIFACT
original = (APP / 'SOURCE-READINESS.md').read_bytes()
assert checks.sha(original) == pkg.SOURCE_READINESS_SHA
document = (bundle / 'SOURCE-READINESS.md').read_text()
assert document == pkg.source_readiness_projection(original)
assert pkg.SOURCE_READINESS_SHA in document and 'captured-workspace projection' in document
assert 'Originating-workspace custody checks (unavailable in this archive)' in document
assert '```text\npython3 -B freeze_sources.py --check\n' in document
assert '```sh\npython3 -B freeze_sources.py' not in document
assert document.count('external originating-workspace') == 2
assert not (bundle / 'freeze_sources.py').exists()
assert not any('.ai-workspace' in p.parts for p in bundle.rglob('*'))
valid_original_links = ['source/', 'package-custody.json', 'source-classification.json', 'source-manifest.json']
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', document)
for name in valid_original_links:
    assert links.count(name) == 1 and (bundle / name).exists()
for name in links:
    assert not name.startswith('../') and (bundle / name).exists(), name
gate_start = original.decode().index('## Current method-release standing')
gate_end = original.decode().index('The Writer activation, basis/source preimages')
assert original.decode()[gate_start:gate_end] in document
commands = re.findall(r'```sh\n(.*?)\n```', document, re.S)
assert commands == ['python3 -B release_tools/bundle_check.py .']
replay = subprocess.run(shlex.split(commands[0]), cwd=bundle, capture_output=True, text=True)
assert replay.returncode == 0, replay.stderr
for row in checks.load(APP / 'package-custody.json')['members']:
    assert (bundle / 'source' / row['path']).read_bytes() == (APP / 'source' / row['path']).read_bytes()
for name in checks.SOURCE_PINS:
    assert (bundle / name).read_bytes() == (APP / name).read_bytes()

wrong_dir = WORK / 'wrong-bound-review'
wrong_dir.mkdir()
wrong = copy.deepcopy(checks.load(review))
wrong['bindings']['model']['sha256'] = '0' * 64
pkg.save(wrong_dir / 'review.json', wrong)
shutil.copyfile(accounts / 'bounded-report.md', wrong_dir / 'bounded-report.md')
options = args(wrong_dir, wrong_dir / 'review.json')
try:
    pkg.build(options)
    raise AssertionError('wrong model-bound review accepted')
except ValueError as exc:
    wrong_reason = str(exc)
    assert not options.bundle.exists()

tampered = WORK / 'tampered-report'
shutil.copytree(bundle, tampered)
report = tampered / 'evidence/reviews/review-001/bounded-report.md'
report.write_bytes(report.read_bytes() + b'Changed body.\n')
inventory = checks.load(tampered / 'inventory.json')
for row in inventory['files']:
    if row['path'] == report.relative_to(tampered).as_posix():
        row.update(bytes=report.stat().st_size, sha256=checks.sha(report.read_bytes()))
pkg.save(tampered / 'inventory.json', inventory)
names = sorted([row['path'] for row in inventory['files']] + ['inventory.json'])
(tampered / 'SHA256SUMS').write_text(''.join(f'{checks.sha((tampered / name).read_bytes())}  {name}\n' for name in names))
try:
    checks.check(tampered)
    raise AssertionError('changed bound report accepted after inventory reindex')
except ValueError as exc:
    report_reason = str(exc)

activation = checks.load(PROOF / 'activation.json')
for row in activation['guarded']:
    assert checks.sha((APP / row['path']).read_bytes()) == row['sha256'], row['path']
assert not (APP / 'bundle').exists() and not (APP / 'dist').exists()
result = {'status': 'passed', 'scope': 'Documentation delta and conserved binding controls on synthetic14-record fixtures; no actual final common artifact',
          'work': str(WORK), 'source_readiness_original_sha256': checks.sha(original),
          'portable_projection_sha256': checks.sha((bundle / 'SOURCE-READINESS.md').read_bytes()),
          'portable_markdown_links': links, 'workspace_only_commands': 2, 'textual_external_custody_routes': 2,
          'advertised_portable_command': commands[0], 'advertised_command_returncode': replay.returncode,
          'source_files_preserved': 81, 'manifests_preserved': 3, 'receipt_bindings_unchanged': True,
          'wrong_bound_review_refusal': wrong_reason, 'changed_report_refusal_after_inventory_reindex': report_reason,
          'deterministic_archive_sha256': first['archive']['sha256'],
          'guarded_untouched_checker_receipt_contract_and_source_files': len(activation['guarded']),
          'private_proof_or_ticket_copied': False, 'native_model_calls': 0, 'browser_or_server_started': False}
pkg.save(PROOF / 'controls.json', result)
print(json.dumps(result, indent=2))
