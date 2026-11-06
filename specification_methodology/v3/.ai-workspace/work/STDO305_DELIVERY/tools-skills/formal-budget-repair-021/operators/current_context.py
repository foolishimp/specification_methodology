"""Run the selected current Context qualification through actual public calls.

Two explicit phases keep the heavy proof separate from subsequent controls and
recipient delivery. Adversarial control artifacts are visibly operator-created;
none is represented as an actual successful preflight/proof producer result.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import os
import subprocess
import sys
import time

RESIDUAL = 'urn:a-c:generation:ba37e2825e4e3c758a5cfaec:record:3aefacf2fe0b450b760b5bca67a02c82'


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def pin(path):
    path = Path(path).absolute()
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(path, value):
    raw = value if isinstance(value, bytes) else canonical(value)
    with path.open('xb') as stream:
        stream.write(raw)
    return pin(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', type=Path, required=True)
    parser.add_argument('--phase', choices=('preflight', 'controls-dispatch'), required=True)
    args = parser.parse_args()
    case_path = args.case.absolute()
    selected = json.loads(case_path.read_bytes())
    assert selected['label'] == 'current-context'
    for value in (selected['configuration'], selected['policy'], selected['provider']):
        assert pin(value['path']) == value
    config = json.loads(Path(selected['configuration']['path']).read_bytes())
    ac_root = Path(config['ac_root'])
    for name, expected in config['provider_pins'].items():
        assert pin(ac_root / name)['sha256'] == expected
    policy = json.loads(Path(selected['policy']['path']).read_bytes())
    evidence_root = Path(policy['evidence_root'])
    assert evidence_root == case_path.parent / 'evidence'
    output = case_path.parent / ('operator-' + args.phase)
    output.mkdir(exist_ok=False)
    recorder = Path(__file__).with_name('record_public_call.py')
    index = 0

    def invoke(operation, arguments=None, existing=None, expected='ok', timeout=120):
        nonlocal index
        index += 1
        label = f'{index:03d}-' + operation
        request_path = existing or output / (label + '.request.json')
        if existing is None:
            save(request_path, {'schema': 'a_c.fd-support.request/1',
                               'id': 'installed017-context-' + args.phase + '-' + str(index),
                               'operation': operation, 'arguments': arguments})
        argv = [config['python'], '-B', str(recorder), '--case', str(case_path),
                '--request', str(request_path), '--output', str(output / label),
                '--timeout-seconds', str(timeout)]
        save(output / (label + '.recorder-invocation.json'), {'argv': argv, 'cwd': selected['cwd']})
        print(json.dumps({'operation': operation, 'status': 'starting', 'phase': args.phase}), flush=True)
        result = subprocess.run(argv, cwd=selected['cwd'], capture_output=True)
        save(output / (label + '.recorder-stdout'), result.stdout)
        save(output / (label + '.recorder-stderr'), result.stderr)
        response = json.loads((output / label / 'stdout.json').read_bytes())
        if expected == 'ok':
            assert result.returncode == 0 and response['status'] == 'ok', response
        else:
            assert result.returncode == 2 and response['status'] != 'ok', response
        return response

    def acquire(reference):
        observed = invoke('evidence.read', {'artifact': reference})['result']['value']
        assert observed['artifact'] == reference and observed['parent_sha256'] == reference['sha256']
        assert hashlib.sha256(canonical(observed['envelope'])).hexdigest() == reference['sha256']
        return observed['envelope']

    count = Path(selected['cwd']) / 'outputs/count'
    assert not count.exists(), 'Original activation already has a recipient effect; do not repeat'
    if args.phase == 'preflight':
        response = invoke('context.assemble', existing=case_path.parent / 'context-request.json')
        context_ref = response['result']['artifact']
        context = acquire(context_ref)['payload']
        expected_views = json.loads((case_path.parent / 'expected-views.json').read_bytes())
        assert context['projections'][0]['views'] == expected_views
        assert len(expected_views[0]['included']) == 21 and RESIDUAL in expected_views[0]['included']
        assert hashlib.sha256(context['rendered_utf8'].encode()).hexdigest() == context['rendered_sha256']
        preflight = invoke('contract.preflight', {'context': context_ref, 'grant_id': 'work',
            'executor_id': 'registered', 'result_key': 'current-native-work21', 'observations': []}, timeout=7500)
        receipt = preflight['result']['value']
        assert receipt['decision'] == receipt['contract_state'] == 'admitted', receipt
        preflight_ref = preflight['result']['artifact']
        formal_ref = receipt['formal_evidence']
        formal = acquire(formal_ref)['payload']
        assert formal['status'] == 'verified' and len(formal['runs']) == 1
        run = formal['runs'][0]
        assert run['result']['selections'] == context['projections'][0]['selections']
        assert run['result']['context_binding']['rendered_sha256'] == context['rendered_sha256']
        bundle = Path(run['bundle'])
        save(output / 'PREFLIGHT.json', {'schema': 'stdo305.current-installed-context-preflight/1',
            'case': pin(case_path), 'context': context_ref, 'preflight': preflight_ref,
            'formal_evidence': formal_ref, 'request': pin(bundle.parent / 'request.json'),
            'formal_result': pin(bundle / 'result.json'), 'bundle': str(bundle),
            'rendered_sha256': context['rendered_sha256'], 'views': pin(case_path.parent / 'expected-views.json'),
            'standing': 'Actual public context and admitted preflight with selected current proof. No recipient dispatch performed.'})
        print(json.dumps({'status': 'actual_preflight_complete', 'record': str(output / 'PREFLIGHT.json')}))
        return

    prior = json.loads((case_path.parent / 'operator-preflight/PREFLIGHT.json').read_bytes())
    assert prior['case'] == pin(case_path)
    context_envelope = acquire(prior['context'])
    receipt_envelope = acquire(prior['preflight'])
    formal_envelope = acquire(prior['formal_evidence'])
    for item in (prior['request'], prior['formal_result'], prior['views']):
        assert pin(item['path']) == item
    # Read-only actual owner inspection; no fresh kernel invocation.
    argv = [config['python'], '-I', '-S', '-B', str(ac_root / 'build_tenants/lean/scripts/formal_gate.py'),
            'inspect-evidence', '--bundle', prior['bundle'], '--request', prior['request']['path']]
    save(output / 'inspection-invocation.json', {'argv': argv, 'cwd': selected['cwd']})
    started = time.time_ns()
    inspected = subprocess.run(argv, cwd=selected['cwd'], capture_output=True, timeout=180)
    save(output / 'inspection-stdout.json', inspected.stdout)
    save(output / 'inspection-stderr.log', inspected.stderr)
    save(output / 'inspection-execution.json', {'argv': argv, 'cwd': selected['cwd'], 'returncode': inspected.returncode,
         'started_ns': started, 'ended_ns': time.time_ns(), 'stdout': pin(output / 'inspection-stdout.json'),
         'stderr': pin(output / 'inspection-stderr.log')})
    inspection = json.loads(inspected.stdout)
    assert inspected.returncode == 0 and inspection['status'] == 'consistent', inspection

    sys.path.insert(0, str(ac_root / 'build_tenants/graphify/code'))
    import ac_support_core as core
    import ac_support_effects as effects
    runtime = core.Runtime.from_policy(Path(selected['policy']['path']), selected['policy']['sha256'], 'executive')
    store = effects.EvidenceStore(runtime)
    runtime = runtime.with_callbacks(store.resolve, store.query_artifacts)

    # Controlled adversarial artifact retention only; no original envelope changes.
    def adversarial(envelope, label):
        save(output / (label + '.adversarial-envelope.json'), envelope)
        result = store.retain(envelope)
        save(output / (label + '.adversarial-reference.json'), result)
        return result

    omitted = copy.deepcopy(context_envelope)
    payload = omitted['payload']; view = payload['projections'][0]['views'][0]
    assert view['included'].count(RESIDUAL) == 1
    view['included'].remove(RESIDUAL)
    view['populations']['residuals'] = [row for row in view['populations']['residuals'] if row['id'] != RESIDUAL]
    body = {key: payload[key] for key in ('packet', 'projections', 'sources', 'late_acquisition', 'boundaries', 'formal_gate')}
    body['schema'] = 'a_c.fd-support.actor-context/1'
    payload['rendered_utf8'] = core.PREFIX + canonical(body).decode()
    payload['rendered_sha256'] = hashlib.sha256(payload['rendered_utf8'].encode()).hexdigest()
    omitted_ref = adversarial(omitted, 'omitted-context')
    rebound = copy.deepcopy(receipt_envelope); rebound['payload']['context'] = omitted_ref
    omission_ref = adversarial(rebound, 'omitted-preflight')
    omission = invoke('dispatch.start', {'preflight': omission_ref}, expected='refusal')
    assert omission['refusal']['code'] == 'basis_stale'
    assert omission['refusal']['reason'] == 'Formal evidence has another origin, policy or exact Context'
    assert not count.exists()

    # Only a copied report is needed to exercise the first stale-report check.
    # No incomplete copied bundle is called a successful proof or replay.
    stale = copy.deepcopy(formal_envelope)
    run = stale['payload']['runs'][0]
    original_bundle = Path(run['bundle'])
    changed = evidence_root / 'formal/operator-stale-report-017'
    changed.mkdir(exist_ok=False)
    original_result = (original_bundle / 'result.json').read_bytes()
    save(changed / 'result.json', original_result + b'\n')
    assert hashlib.sha256(original_result).hexdigest() == run['result_sha256']
    run['bundle'] = str(changed)
    stale_ref = adversarial(stale, 'stale-formal-evidence')
    rebound = copy.deepcopy(receipt_envelope); rebound['payload']['formal_evidence'] = stale_ref
    stale_preflight = adversarial(rebound, 'stale-preflight')
    refusal = invoke('dispatch.start', {'preflight': stale_preflight}, expected='refusal')
    assert refusal['refusal']['code'] == 'contract_violation'
    assert refusal['refusal']['reason'] == 'Retained checker result changed'
    assert not count.exists()
    assert (original_bundle / 'result.json').read_bytes() == original_result
    save(output / 'CONTROLS.json', {'schema': 'stdo305.current-context-delivery-controls/1',
        'standing': 'Explicit operator-authored adversarial copies; public dispatch responses are actual. No copied success field is presented as an actual producer result.',
        'omitted_required_record': RESIDUAL, 'omission_response': omission, 'stale_response': refusal,
        'stale_copy': pin(changed / 'result.json'), 'original_result': prior['formal_result'],
        'recipient_effects_after_controls': 0})
    actual = invoke('dispatch.start', {'preflight': prior['preflight']}, timeout=7500)
    attempt = actual['result']['artifact']
    deadline = time.monotonic() + 120
    while True:
        observed = invoke('dispatch.observe', {'attempt': attempt, 'after_event': 0})['result']['value']
        if observed['process_end'] is not None and any(row['kind'] == 'effect_observation' for row in observed['events']):
            break
        assert time.monotonic() < deadline, 'Retain unresolved current attempt; do not dispatch again'
        time.sleep(0.5)
    context = context_envelope['payload']
    received = Path(selected['cwd']) / 'outputs/received-stdin.bin'
    received_views = Path(selected['cwd']) / 'outputs/received-views.json'
    assert count.read_text() == '1'
    assert received.read_bytes() == context['rendered_utf8'].encode()
    expected = [p['views'] for p in context['projections']]
    assert received_views.read_bytes() == canonical(expected)
    assert expected[0] == json.loads(Path(prior['views']['path']).read_bytes())
    save(output / 'DELIVERY.json', {'schema': 'stdo305.current-context-delivery/1', 'context': prior['context'],
        'preflight': prior['preflight'], 'attempt': attempt, 'observation': observed,
        'received_stdin': pin(received), 'received_views': pin(received_views), 'count': 1,
        'exact_context_bytes_delivered': True, 'exact_ordered_native_work21_view_delivered': True,
        'limits': 'One cooperative local recipient; process-end and exact stdin receipt do not prove external effect completion, actor attention or host permission enforcement.'})
    print(json.dumps({'status': 'actual_controls_and_delivery_complete', 'record': str(output / 'DELIVERY.json')}))


if __name__ == '__main__':
    main()
