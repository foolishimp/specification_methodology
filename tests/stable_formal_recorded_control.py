#!/usr/bin/env python3
"""Exercise the actual release evidence consumer on an actual recorded toy run.

This is a test-only manifest selecting the owner's toy model, not the STDO
semantic candidate. It never calls content/ref/public gates or manufactures
proof-execution receipts. The supplied owner receipts are consumed unchanged.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import check_stack_release as api
import stable_stack_release as stable
sys.path.insert(0, str(ROOT / 'specification_methodology/v3/build_tenants/common-tools'))
import proof_evidence as transport


def ref(path):
    path = Path(path); raw = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(raw), 'sha256': api.sha256(raw)}


def save(directory, name, value):
    path = directory / name
    if path.exists(): raise ValueError('preserve existing control output: ' + str(path))
    path.write_bytes(api.canonical_json_bytes(value))
    return ref(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipts', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(); output = args.output.absolute(); output.mkdir(exist_ok=False, parents=True)
    receipts = args.receipts.absolute(); cold = json.loads((receipts / 'cold-execution/execution.json').read_bytes())
    fresh = json.loads((receipts / 'fresh-execution/execution.json').read_bytes())
    request_path = Path(cold['execution']['argv'][cold['execution']['argv'].index('--request') + 1])
    request = json.loads(request_path.read_bytes()); model_ref = ref(request['input']['path'])
    model = json.loads((ROOT / model_ref['path']).read_bytes()); result = json.loads((ROOT / cold['result']['path']).read_bytes())
    manifest = json.loads((ROOT / 'stack_release.json').read_bytes())
    manifest['source'] = {'source_identity_sha256': hashlib.sha256(b'owner toy-model adapter control, not STDO source').hexdigest()}
    for product, value in manifest['products'].items():
        value['subject'] = {'sha256': hashlib.sha256(('test-only ' + product).encode()).hexdigest()}
    manifest['components']['representation']['facts'] = {'model': model_ref, 'model_sha256': model_ref['sha256'], 'model_canonical_sha256': api.canonical_value_sha256(model)}
    runtime_ref = save(output, 'runtime.json', result['runtime_identity'])
    transport.pack(receipts / 'cold', output / 'cold-evidence.zip')
    transport.pack(receipts / 'fresh', output / 'fresh-evidence.zip')
    transport.split(output / 'cold-evidence.zip', output / 'cold-transport')
    transport.split(output / 'fresh-evidence.zip', output / 'fresh-transport')
    auxiliary = {}
    origin = '.cache/formal-origin-v1/selection.json'
    if origin in result['runtime_identity']['pins']:
        raw = (ROOT / 'a_c/build_tenants/lean' / origin).read_bytes()
        (output / 'public-origin-selection.json').write_bytes(raw); auxiliary[origin] = ref(output / 'public-origin-selection.json')
    manifest['components']['lean']['facts'] = {'request': ref(request_path), 'selections': save(output, 'selections.json', request['selections']),
        'supplied_views': ref(request['supplied_views']['path']), 'bundle': (receipts / 'cold').relative_to(ROOT).as_posix(),
        'bundle_manifest': ref(receipts / 'cold/manifest.json'), 'runtime_identity': runtime_ref, 'runtime_auxiliary': auxiliary,
        'bundle_archive': ref(output / 'cold-transport/TRANSPORT.json'), 'replay_archive': ref(output / 'fresh-transport/TRANSPORT.json'),
        'replay_bundle': (receipts / 'fresh').relative_to(ROOT).as_posix()}
    record = {**cold, 'kind': 'stdo.cohort-evidence/1', 'claim': 'exact_candidate_lean_result', 'status': 'passed', 'category': 'execution',
        'source_identity_sha256': manifest['source']['source_identity_sha256'],
        'subjects': {p: v['subject']['sha256'] for p, v in manifest['products'].items()},
        'limits': ['Actual owner toy-model execution only; not current STDO source or whole-cohort qualification.'], 'replay': fresh}
    manifest_ref = save(output, 'test-manifest.json', manifest); evidence_ref = save(output, 'test-evidence.json', record)
    cases = []; started = time.monotonic()
    stable.evidence(api.View(ROOT), evidence_ref, record['claim'], manifest, api)
    cases.append({'case': 'real-recorded-cold-and-fresh-owner-inspection', 'status': 'passed', 'elapsed_seconds': time.monotonic() - started})
    changed = copy.deepcopy(manifest); changed['components']['representation']['facts']['model_canonical_sha256'] = '0' * 64
    try: stable.evidence(api.View(ROOT), evidence_ref, record['claim'], changed, api)
    except ValueError as exc: cases.append({'case': 'wrong-current-model-refuses', 'status': 'passed', 'reason': str(exc)})
    else: raise AssertionError('wrong current model accepted')
    changed = copy.deepcopy(record); changed['execution']['argv'] = changed['execution']['argv'][:5] + ['--help']
    bad_ref = save(output, 'help-evidence.json', changed)
    try: stable.evidence(api.View(ROOT), bad_ref, record['claim'], manifest, api)
    except ValueError as exc: cases.append({'case': 'help-instead-of-real-proof-refuses', 'status': 'passed', 'reason': str(exc)})
    else: raise AssertionError('help accepted')
    report = {'kind': 'stdo.release-gate-recorded-toy-control/1', 'scope': 'actual evidence() consumer only; no STDO candidate proof or release gate conclusion',
              'manifest': manifest_ref, 'evidence': evidence_ref, 'cold_receipt': ref(receipts / 'cold-execution/execution.json'),
              'fresh_receipt': ref(receipts / 'fresh-execution/execution.json'), 'cases': cases}
    save(output, 'RESULT.json', report); print(json.dumps(report, indent=2))


if __name__ == '__main__': main()
