"""Recheck actual freeze04 Context/admission using the successor public CLI.

No protected artifact is fabricated or rewritten. The predecessor CLI creates
the invalid retained Context/receipt in a disposable fixture. The successor
then processes those same objects with the same policy, actors and history.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import sys

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'a_c/build_tenants/graphify/test_env'))
import test_ac_support_composition as tests

os.environ['AC_SUPPORT_EFFECTS_PROOF_ROOT'] = str(HERE / 'predecessor-custody')
case = tests.CompositionPublicTests('runTest')
case._testMethodName = 'actual_predecessor_context_and_admission'
case.setUp()
try:
    packet = case._inline_provider_packet()
    current = case.code
    predecessor = case.root / 'freeze04-code'
    predecessor.mkdir()
    files = json.loads((HERE / 'source-freeze-04.json').read_text())['files']
    pins = {}
    for name, expected in files.items():
        if '/code/' not in name:
            continue
        original = HERE / 'preimages/freeze04' / name
        raw = original.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected
        (predecessor / original.name).write_bytes(raw)
        pins[original.name] = expected
    # The common graph dependency is unchanged and is pinned in provider04.
    graph = current / 'ac_graph.py'
    graph_expected = json.loads((HERE / 'provider-files-04.json').read_text())['files']['a_c/build_tenants/graphify/code/ac_graph.py']
    assert hashlib.sha256(graph.read_bytes()).hexdigest() == graph_expected
    shutil.copy2(graph, predecessor / graph.name)
    case.code = predecessor
    context = case._assemble(packet)
    receipt = case._admit(context)
    case.code = current
    admission = case._public('contract.preflight', {'context': context, 'grant_id': 'work',
        'executor_id': 'registered', 'result_key': 'public-counter', 'observations': []})
    case.assertRefused(admission, 'authority_missing')
    dispatch = case._public('dispatch.start', {'preflight': receipt})
    case.assertRefused(dispatch, 'authority_missing')
    assert not case.target.exists()
    records = [json.loads(path.read_text()) for path in (case.f.evidence / 'objects').glob('*.json')]
    assert not any(item['kind'] == 'attempt' for item in records)
    result = {'predecessor_code': pins, 'context': context, 'preflight': receipt,
              'successor_composition_sha256': hashlib.sha256((current / 'ac_support_composition.py').read_bytes()).hexdigest(),
              'admission_refusal': admission['refusal']['code'],
              'dispatch_refusal': dispatch['refusal']['code'],
              'worker_started': False, 'attempt_created': False,
              'standing': 'actual predecessor assembly/admission; successor actual public CLI refuses before effect'}
    (HERE / 'predecessor-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
finally:
    case.tearDown()
