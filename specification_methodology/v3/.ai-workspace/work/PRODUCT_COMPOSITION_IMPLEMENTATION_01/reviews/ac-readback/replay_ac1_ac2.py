"""Independent bounded freeze04 repair replay; generated temporary fixtures only."""
from __future__ import annotations

import base64
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import time
from unittest.mock import patch

ROOT = Path('/Users/jim/src/apps/specification_methodology')
CODE = ROOT / 'a_c/build_tenants/graphify/code'
sys.path[:0] = [str(CODE), str(ROOT / 'a_c/build_tenants/graphify/test_env')]
import ac_support
import ac_support_core as c
from test_ac_support_composition import CompositionPublicTests

OUT = Path(__file__).with_name('independent-replay.json')
INDEX = ROOT / 'a_c/.ai-workspace/work/PRODUCT_COMPOSITION_01/source-freeze-04.json'
EXPECTED = '53db95d31d32dd00fc8f0c8b13bc184dc45c422bc52dbb7239fd1370212160b8'
assert hashlib.sha256(INDEX.read_bytes()).hexdigest() == EXPECTED
inventory = json.loads(INDEX.read_text())
assert all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest for name, digest in inventory['files'].items())
os.environ.pop('AC_SUPPORT_EFFECTS_PROOF_ROOT', None)
record = {'source_freeze_sha256': EXPECTED, 'scope': 'Independent exact original CLI negatives plus bounded allowed and error-projection controls; no paid actor', 'cases': []}


@contextlib.contextmanager
def fixture():
    case = CompositionPublicTests('runTest')
    case.setUp()
    try:
        yield case
    finally:
        case.tearDown()


def envelope(case, ref):
    return json.loads((case.f.evidence / 'objects' / (ref['sha256'] + '.json')).read_text())


def forbidden_absent(response, marker):
    serialized = json.dumps(response)
    assert marker not in serialized, serialized
    assert base64.b64encode((marker + '\n').encode()).decode() not in serialized, serialized


def refused(response, code):
    assert response['status'] != 'ok', response
    assert response['refusal']['code'] == code, response


def review_args(case):
    return {'phase': 'expectation', 'claim': case.f.law, 'sources': [], 'candidate': None,
            'proof': [], 'comparison': None, 'expectations': None, 'expectation_body': None}


def install_policy(case, marker, authority=None):
    source = case.f.write('inputs/private-independence.json', {
        'id': 'private-independence', 'authority_source': case.f.owner if authority is None else authority,
        'claim_scope': marker, 'require_non_author': True, 'allowed_family_pairs': [['A', 'B']],
        'source_first': True, 'mechanical_sharing': [], 'predicates': []})
    case.f.policy['independence_policy'] = source
    case.declaration['resources']['private-policy'] = {'source': source, 'owner': 'urn:test:product', 'complete': True, 'parents': []}
    case.declaration['bindings']['reviewer']['allow'].append('private-policy')
    return source


with fixture() as case:
    marker = 'REVIEW-DENIED-POLICY-CONTENT-7e37'
    source = install_policy(case, marker)
    binding = case.declaration['bindings']['reviewer']
    binding['exclude'] = ['private-policy']; case.select()
    direct = case.read(source, 'reviewer')
    denied = case._public('review.prepare', review_args(case), principal='reviewer')
    refused(direct, 'acquisition_denied'); refused(denied, 'acquisition_denied'); forbidden_absent(denied, marker)
    binding['exclude'] = []; case.select()
    permitted = case._public('review.prepare', review_args(case), principal='reviewer')
    assert permitted['status'] == 'ok', permitted
    assert permitted['result']['value']['independence']['governing_conditions']['claim_scope'] == marker
    artifacts = [json.loads(p.read_text()) for p in (case.f.evidence / 'objects').glob('*.json')]
    acquisitions = [item for item in artifacts if item['kind'] == 'acquisition' and item['payload'].get('source') == source]
    assert len(acquisitions) == 1, acquisitions
    acquired = acquisitions[0]
    assert acquired['payload']['recipient'] == 'reviewer'
    assert acquired['payload']['channel'] == 'public-response'
    assert acquired['payload']['composition']['resources'][0]['id'] == 'private-policy'
    binding['exclude'] = ['private-policy']; binding['clean_room'] = True; case.select()
    reentry = case.read(case.f.law, 'reviewer'); refused(reentry, 'basis_stale')
    record['cases'].append({'name': 'AC1 exact denied policy; allowed disclosure and retained exposure', 'result': 'pass',
        'source': source, 'direct_denial': direct, 'automatic_denial': denied, 'allowed': permitted,
        'policy_acquisition': acquired, 'strict_reentry': reentry})

with fixture() as case:
    marker = 'REVIEW-DENIED-POLICY-CONTENT-7e37'
    install_policy(case, marker, case.hidden)
    case.declaration['bindings']['reviewer']['exclude'] = ['hidden']; case.select()
    denied = case._public('review.prepare', review_args(case), principal='reviewer')
    refused(denied, 'acquisition_denied'); forbidden_absent(denied, marker)
    record['cases'].append({'name': 'AC1 automatically read authority independently denied', 'result': 'pass', 'response': denied})

with fixture() as case:
    marker = 'CONTROL-DENIED-OUTPUT-9492'
    actor = case.f.write('inputs/control_actor.py', b'import sys\nsys.stdin.buffer.read()\nprint("CONTROL-DENIED-OUTPUT-9492",flush=True)\n')
    executor = case.f.policy['executors']['registered']
    executor['argv'] = [str(case.python), '-B', str(case.f.workspace / 'inputs/control_actor.py')]
    executor['dependencies'] = [actor]
    case.f.policy['grants']['work']['operations'].append('dispatch.cancel')
    case.declaration['bindings']['worker']['exclude'] = []
    case.declaration['bindings']['worker']['output']['sources'] = ['hidden']; case.select()
    context = case._assemble(); attempt = case._ok(case._public('dispatch.start', {'preflight': case._admit(context)}))['attempt']
    ended_response = case._finished(attempt); ended = case._ok(ended_response)
    assert ended['process_end']['returncode'] == 0
    # Separate eligible recipient is the positive control; the original Executive never acquires these bytes.
    allowed = case._public('evidence.read', {'artifact': ended['output']['stdout']}, principal='reviewer')
    assert marker in base64.b64decode(case._ok(allowed)['envelope']['payload']['bytes_base64']).decode()
    case.declaration['bindings']['executive']['exclude'] = ['hidden']; case.select()
    denied = case._public('evidence.read', {'artifact': ended['output']['stdout']}); refused(denied, 'acquisition_denied')
    events = []
    for path in (case.f.evidence / 'objects').glob('*.json'):
        item = json.loads(path.read_text()); payload = item['payload']
        if isinstance(payload, dict) and payload.get('schema') == 'a_c.fd-support.attempt-event/1' and payload.get('attempt') == attempt:
            events.append((payload['cursor'], path, item))
    events.sort(key=lambda item: item[0]); assert events[0][0] == 1
    removed = events[0][2]; events[0][1].unlink()
    cancelled = case._public('dispatch.cancel', {'attempt': attempt, 'reason': 'targeted history-gap reconciliation probe'})
    refused(cancelled, 'history_incomplete'); forbidden_absent(cancelled, marker)
    assert cancelled['refusal']['gaps'][0]['effect_state'] == 'completion_unknown'
    assert cancelled['refusal']['gaps'][0]['end_established'] is False
    operation = envelope(case, cancelled['evidence'])['payload']
    diagnostic_pairs = [(ref, envelope(case, ref)) for ref in operation['artifacts']
        if envelope(case, ref)['payload'].get('schema') == 'a_c.fd-support.composition-diagnostic/1']
    assert len(diagnostic_pairs) == 1
    diagnostic_ref, diagnostic = diagnostic_pairs[0]
    assert base64.b64encode((marker + '\n').encode()).decode() in json.dumps(diagnostic)
    private_read = case._public('evidence.read', {'artifact': diagnostic_ref})
    assert private_read['status'] != 'ok'; forbidden_absent(private_read, marker)
    observed = case._public('dispatch.observe', {'attempt': attempt, 'after_event': 0}); forbidden_absent(observed, marker)
    if observed['status'] == 'ok':
        assert observed['result']['value']['history_complete'] is False
        assert observed['result']['value']['effect']['end_established'] is False
    else:
        assert observed['refusal']['gaps'][0]['effect_state'] == 'completion_unknown'
    record['cases'].append({'name': 'AC2 exact interrupted history and denied output; private original retained', 'result': 'pass',
        'attempt': attempt, 'normal_observation': ended_response, 'allowed_other_recipient_read': allowed,
        'denied_executive_read': denied, 'removed_first_event': removed, 'cancel_response': cancelled,
        'private_diagnostic': diagnostic, 'private_read_response': private_read, 'subsequent_observation': observed})

with fixture() as case:
    marker = 'LIVE-CONTROL-DENIED-OUTPUT'
    actor = case.f.write('inputs/live_control_actor.py', b'import sys,time\nfrom pathlib import Path\nsys.stdin.buffer.read()\nPath(sys.argv[1]).write_text("started")\nprint("LIVE-CONTROL-DENIED-OUTPUT",flush=True)\ntime.sleep(10)\n')
    executor = case.f.policy['executors']['registered']
    executor['argv'] = [str(case.python), '-B', str(case.f.workspace / 'inputs/live_control_actor.py'), str(case.target)]
    executor['dependencies'] = [actor]
    case.f.policy['grants']['work']['operations'].append('dispatch.cancel')
    case.declaration['bindings']['worker']['exclude'] = []
    case.declaration['bindings']['worker']['output']['sources'] = ['hidden']; case.select()
    attempt = case._ok(case._public('dispatch.start', {'preflight': case._admit(case._assemble())}))['attempt']
    deadline = time.monotonic() + 3
    while not case.target.exists() and time.monotonic() < deadline:
        time.sleep(0.02)
    assert case.target.exists()
    case.declaration['bindings']['executive']['exclude'] = ['hidden']
    case.declaration['bindings']['executive']['operations'] = []; case.select()
    observed = case._public('dispatch.observe', {'attempt': attempt, 'after_event': 0})
    assert observed['status'] == 'ok'; forbidden_absent(observed, marker)
    cancelled = case._public('dispatch.cancel', {'attempt': attempt, 'reason': 'authorized bounded live cancellation'})
    assert cancelled['status'] == 'ok', cancelled
    ended = case._finished(attempt); forbidden_absent(ended, marker)
    assert ended['result']['value']['process_end'] is not None
    record['cases'].append({'name': 'AC2 authorized live control remains usable after composition revocation', 'result': 'pass',
        'observation': observed, 'cancel_response': cancelled, 'ended': ended})

with fixture() as case:
    marker = 'PRIVATE-REVIEW-HISTORY-DETAIL-READBACK'
    (case.f.evidence / 'objects').mkdir(exist_ok=True)
    (case.f.evidence / 'objects' / ('.stage-' + marker)).write_text('isolated history fault')
    response = case._public('review.prepare', review_args(case), principal='reviewer')
    assert response['status'] == 'ok'; forbidden_absent(response, marker)
    assert response['result']['value']['gaps']
    operation = envelope(case, response['evidence'])['payload']
    diagnostics = [envelope(case, ref) for ref in operation['artifacts'] if envelope(case, ref)['payload'].get('schema') == 'a_c.fd-support.composition-diagnostic/1']
    assert any(marker in json.dumps(item) for item in diagnostics)
    record['cases'].append({'name': 'Successful review retains private incomplete-history detail without disclosure', 'result': 'pass', 'response': response, 'private_diagnostics': diagnostics})

with fixture() as case:
    marker = 'PRIVATE-FAILURE-DETAIL-READBACK'
    encoded = base64.b64encode(marker.encode()).decode()
    runtime = ac_support._load_runtime(case.policy_path, case.policy_sha, 'executive')
    request = {'schema': c.REQUEST, 'id': 'independent-projection-probe', 'operation': 'source.read', 'arguments': {'source': case.f.law, 'encoding': 'utf8'}}
    error = c.SupportError('evidence_publication_failed', marker, [{'nested': {'bytes_base64': encoded}}], [case.hidden])
    with patch.object(ac_support.effects, 'persist_outcome', side_effect=error):
        response = ac_support.execute(runtime, request)
    assert response['evidence'] is None
    assert marker not in json.dumps(response) and encoded not in json.dumps(response)
    assert response['refusal']['gaps'][0]['private_retention'] == 'not established'
    success = ac_support.execute(runtime, request); assert success['status'] == 'ok'
    target = io.BytesIO(); stderr = io.StringIO()
    with patch.object(ac_support.effects.EvidenceStore, 'retain', side_effect=RuntimeError(encoded)), contextlib.redirect_stderr(stderr):
        ac_support._deliver(runtime, request, success, target)
    assert encoded not in stderr.getvalue() and marker not in stderr.getvalue()
    assert 'unknown' in stderr.getvalue()
    record['cases'].append({'name': 'Selected-mode publication and transport failure projections', 'result': 'pass',
        'method': 'in-process boundary fault injection, not CLI environmental reproduction', 'publication_response': response, 'transport_stderr': stderr.getvalue()})

record['result'] = 'all six bounded readbacks passed'
OUT.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'result': record['result'], 'evidence': str(OUT), 'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest()}))
