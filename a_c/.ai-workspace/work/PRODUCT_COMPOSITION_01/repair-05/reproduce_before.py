"""Public CLI counterexamples run against verified, unchanged freeze04 code."""
from pathlib import Path
import hashlib
import json
import os
import sys

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'a_c/build_tenants/graphify/test_env'))
import test_ac_support_composition as tests

os.environ['AC_SUPPORT_EFFECTS_PROOF_ROOT'] = str(HERE / 'before-custody')
results = {}


def fixture(name):
    case = tests.CompositionPublicTests('runTest')
    case._testMethodName = name
    case.setUp()
    return case


case = fixture('retained_inline_missing_recipient_route')
try:
    case._route()
    case.declaration['bindings']['executive']['route'] = ['A-D']
    actor = case.f.write('inputs/hash_actor.py', b'import sys,hashlib\nfrom pathlib import Path\nraw=sys.stdin.buffer.read()\nPath(sys.argv[1]).write_text(hashlib.sha256(raw).hexdigest())\n')
    executor = case.f.policy['executors']['registered']
    executor['argv'] = [str(case.python), '-B', str(case.f.workspace / 'inputs/hash_actor.py'), str(case.target)]
    executor['dependencies'] = [actor]
    case.select()
    direct = case.read(case.f.data)
    case.assertRefused(direct, 'authority_missing')
    acquired = case._ok(case.read(case.f.data, 'executive'))
    packet = case.f.packet()
    packet['attention']['prohibited_assumptions'] = [acquired['content']]
    context = case._assemble(packet)
    admission = case._admit(context)
    started = case._ok(case._public('dispatch.start', {'preflight': admission}))
    ended = case._ok(case._finished(started['attempt']))
    retained = json.loads((case.f.evidence / 'objects' / (context['sha256'] + '.json')).read_text())['payload']
    actual = case.target.read_text()
    assert actual == retained['rendered_sha256']
    assert acquired['content'] in json.loads(retained['rendered_utf8'].split('\n', 1)[1])['packet']['attention']['prohibited_assumptions']
    results['inline'] = {'direct_refusal': direct['refusal']['code'], 'context': context,
                         'preflight': admission, 'attempt': started['attempt'],
                         'process_returncode': ended['process_end']['returncode'],
                         'actual_worker_stdin_sha256': actual,
                         'invalid_inline_delivered': True}
finally:
    case.tearDown()

case = fixture('fragment_false_positive')
try:
    case._route()
    case.declaration['bindings']['worker']['route'] = ['A-D']
    variants = {
        'list_nested_fence': '- Example:\n\n  ```markdown\n  # Support\n  <a id="support"></a>\n  ```\n',
        'list_marker_fence': '- ```markdown\n  # Support\n  <a id="support"></a>\n  ```\n',
        'unfinished_comment': '<!-- unfinished\n# Support\n<a id="support"></a>\n',
    }
    values = {}
    for name, text in variants.items():
        case.declaration['edges']['A-D']['relation'] = case.f.write('inputs/relation.md', text.encode())
        case.select()
        response = case.read(case.f.data)
        values[name] = {'text': text, 'status': response['status'], 'refusal': response['refusal']}
    results['fragments'] = values
finally:
    case.tearDown()

(HERE / 'before-results.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
