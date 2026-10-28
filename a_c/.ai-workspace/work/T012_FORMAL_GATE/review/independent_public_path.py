"""Independent, bounded T012 public-command review. Writes only review evidence.

Fixture supplies disposable policy/setup only. All operations and gate verdicts
are obtained from ordinary public CLI subprocesses, never Memory.run/execute_read.
The new subject is explicitly test-authored; it makes no F_P or authority claim.
"""
from __future__ import annotations
import argparse
import base64
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

REVIEW = Path(__file__).resolve().parent
REPO = REVIEW.parents[4]
LEAN = REPO / 'a_c/build_tenants/lean'
GRAPHIFY = REPO / 'a_c/build_tenants/graphify'
OUT = REVIEW / 'independent-public-001'
EXPECTED_RUNTIME = 'a194a9370c0f6c779f98c4cf8c3c47f9380e16315e5c8910286500fd98aa4888'
sys.path.insert(0, str(GRAPHIFY / 'test_env'))
sys.path.insert(0, str(GRAPHIFY / 'code'))
import ac_graph
import ac_support_core as core
from test_ac_support_core import Fixture


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical(value) + b'\n')


def load(path):
    return json.loads(path.read_bytes())


def call(argv, location, request=None, timeout=600):
    location.mkdir(parents=True, exist_ok=False)
    raw = None if request is None else canonical(request)
    if raw is not None:
        (location / 'stdin.json').write_bytes(raw)
    start = time.monotonic()
    done = subprocess.run(argv, input=raw, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, timeout=timeout)
    elapsed = time.monotonic() - start
    (location / 'stdout').write_bytes(done.stdout)
    (location / 'stderr').write_bytes(done.stderr)
    meta = {'argv': argv, 'returncode': done.returncode, 'elapsed_seconds': elapsed,
            'stdout_sha256': sha(done.stdout), 'stderr_sha256': sha(done.stderr)}
    save(location / 'invocation.json', meta)
    print(json.dumps({'command': str(location.relative_to(OUT)), **meta}, ensure_ascii=False), flush=True)
    return done.returncode, json.loads(done.stdout), meta


def prepare():
    OUT.mkdir(exist_ok=False)
    subject = 'repo://independent-t012-review/eight-records/'
    ns = 'urn:a-c:generation:' + sha(subject.encode())[:24] + ':'
    section = subject + 'subject.md#Review'
    source = ('# Review\nA requires B; B has unresolved evidence.\n'
              'A wording may vary; its prerequisite may not.\n'
              'C is separate and has its own unresolved evidence.\n').encode()
    (OUT / 'subject.md').write_bytes(source)
    def grounding(line, quote):
        return [{'section': section, 'path': 'subject.md', 'start_line': line,
                 'end_line': line, 'quote': quote}]
    g = grounding(2, 'A requires B; B has unresolved evidence.')
    gc = grounding(4, 'C is separate and has its own unresolved evidence.')
    gl = grounding(3, 'A wording may vary; its prerequisite may not.')
    definition = json.loads(json.dumps(load(LEAN / 'profiles/generation-signature-v1.json')['definition'],
                                      ensure_ascii=False).replace('$NS:', ns))
    kind = ns + 'relation-kind:governing:depends-on'
    endpoint = copy.deepcopy(definition['fields']['relations']['source'])
    endpoint['governing'] = True
    definition['relation_kinds'][kind] = {'source': endpoint, 'target': copy.deepcopy(endpoint),
                                        'qualifiers': copy.deepcopy(definition['fields']['relations']['qualifiers'])}
    signature = {'id': ns + 'signature:compact-source-proposal-v1', 'definition': definition}
    signature['sha256'] = sha(canonical(signature))
    ids = {key: ns + 'record:' + key for key in ('a', 'b', 'c', 'ab', 'constraint-a', 'latitude-a', 'residual-b', 'residual-c')}
    basisid = ns + 'basis'
    coordinates = {'context': ns + 'context:review', 'owner': ns + 'actor:review-author',
                   'scope': [ns + 'scope:review-subject']}
    def record(key, **values):
        return {'id': ids[key], 'basis': basisid, **copy.deepcopy(coordinates), **values}
    pops = {key: [] for key in ('objects', 'relations', 'constraints', 'latitude', 'residuals',
                               'traversals', 'transformations', 'judgments')}
    for key, text in (('a', 'A requires B.'), ('b', 'B is required by A.'), ('c', 'C is separate.')):
        pops['objects'].append(record(key, sort=ns + 'sort:authored-concept', value={
            'label': key.upper(), 'definition': text, 'conditions': [], 'exceptions': [],
            'grounding': gc if key == 'c' else g}))
    pops['relations'] = [record('ab', kind=kind, source=ids['a'], target=ids['b'], qualifiers={
        'kind': 'depends-on', 'meaning': 'A requires B.', 'conditions': [], 'exceptions': [], 'grounding': g})]
    pops['constraints'] = [record('constraint-a', kind=ns + 'constraint-kind:authored-source-statement',
        applies_to=[ids['a']], latitude_ref=[ids['latitude-a']], judgment_kind=ns + 'judgment-kind:external-semantic-review',
        refusal=ns + 'stop:no-execution-or-acceptance', predicate={'statement': 'Retain the prerequisite.',
        'conditions': [], 'exceptions': [], 'uncertainty': '', 'grounding': gl})]
    pops['latitude'] = [record('latitude-a', applies_to=[ids['a']],
        allowed_variation={'statements': ['Wording may vary.'], 'grounding': gl},
        forbidden_variation={'statements': ['Removing B is forbidden.'], 'grounding': gl},
        invalidation=ns + 'invalidation:source-or-interpretation-change')]
    for key in ('b', 'c'):
        pops['residuals'].append(record('residual-' + key, kind=ns + 'residual-kind:authored-uncertainty',
            subject=ids[key], uncertainty={'statement': key.upper() + ' evidence remains unresolved.',
            'grounding': g if key == 'b' else gc}, consequence='Do not infer resolution.', re_entry=[],
            invalidation=ns + 'invalidation:source-or-interpretation-change'))
    authority = ns + 'authority:test-authorship-only'
    dispositions = [{'source': section, 'decision': 'residual', 'records': list(ids.values()),
                     'authority': authority, 'basis': basisid,
                     'reason': 'Explicit test authorship retains both included and excluded residuals.'}]
    interpretation = {'dispositions': dispositions}
    for name, identity in [('contract', ns + 'interpretation-contract'), ('selection_ledger', ns + 'selection-ledger'),
                           ('interpreter', ns + 'interpreter:test-author'), ('authority', authority),
                           ('source_reentry', ns + 'source-reentry'),
                           ('invalidation', ns + 'invalidation:source-or-interpretation-change')]:
        value = dispositions if name == 'selection_ledger' else {'id': identity, 'claim': 'Test metadata only; no semantic or operation authority.'}
        raw = canonical(value)
        (OUT / (name + '.json')).write_bytes(raw)
        interpretation[name] = {'id': identity, 'sha256': sha(raw)}
    provenance = {'author': 'independent Reviewer', 'subject': subject, 'record_count': 8,
                  'no_model_calls': True, 'claim': 'Explicit test authorship, no original-prose fidelity claim.'}
    save(OUT / 'PROVENANCE.json', provenance)
    interpretation['provenance'] = [{'id': ns + 'provenance:review', 'sha256': sha((OUT / 'PROVENANCE.json').read_bytes())}]
    kinds = {section: 'source-section', coordinates['owner']: 'actor', authority: 'authority', basisid: 'basis',
             coordinates['context']: 'context', coordinates['scope'][0]: 'scope', ns+'sort:authored-concept': 'sort',
             kind: 'relation-kind', ns+'constraint-kind:authored-source-statement': 'constraint-kind',
             ns+'judgment-kind:external-semantic-review': 'judgment-kind',
             ns+'residual-kind:authored-uncertainty': 'residual-kind',
             ns+'stop:no-execution-or-acceptance': 'stop',
             ns+'invalidation:source-or-interpretation-change': 'invalidation'}
    externals = [{'external_identity': identity, 'reference_domain': ns+'reference-domain:declared',
                  'external_target_kind': ns+'external-kind:'+typ, 'resolved_target_identity': identity,
                  'basis_relation': ns+'basis-relation:exact', 'resolution_basis': basisid,
                  'evidence_identity': ns+'evidence:independent-test'} for identity, typ in sorted(kinds.items())]
    model = {'profile': 'a_c.graphify.model/1', 'id': ns+'model:independent-eight',
             'basis': {'id': basisid, 'calculus': {'uri': 'stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md',
              'sha256': 'cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d'},
              'subject': {'id': subject, 'sha256': sha(source), 'inventory': [{'id': section, 'sha256': sha(source)}]}},
             'coordinates': coordinates, 'signature': signature, 'interpretation': interpretation,
             'dependency_contract': {'id': ns+'dependency-contract:authored-governing-relations',
               'attachment_families': ['constraints', 'latitude', 'residuals'], 'required_relation_kinds': [kind]},
             'populations': pops, 'external_resolutions': externals,
             'identity_universe': sorted([*ids.values(), *kinds]), 'functor_bindings': {}}
    save(OUT / 'model.json', model)
    checked = ac_graph.validate(model)
    views = ac_graph.project_many(checked, [([ids['a']], 6)])
    expected = sorted(ids[k] for k in ('a', 'b', 'ab', 'constraint-a', 'latitude-a', 'residual-b'))
    assert views[0]['included'] == expected, views
    assert views[0]['excluded'] == sorted([ids['c'], ids['residual-c']])
    assert views[0]['boundary']['unresolved_residuals'] == [ids['residual-b']]
    reverse = ac_graph.project(checked, [ids['b']], 2)
    assert reverse['included'] == sorted([ids['b'], ids['residual-b']]), reverse
    save(OUT / 'views.json', views)
    save(OUT / 'reverse-direction-view.json', reverse)
    selection = [{'seeds': [ids['a']], 'budget_records': 6}]
    request = {'schema': 'a_c.formal-gate.request/1', 'input': {'format': 'model', 'path': str(OUT/'model.json'),
        'raw_sha256': sha((OUT/'model.json').read_bytes())}, 'selections': selection,
        'supplied_views': {'path': str(OUT/'views.json'), 'raw_sha256': sha((OUT/'views.json').read_bytes())},
        'context_binding': None}
    save(OUT / 'request.json', request)
    save(OUT / 'expectations.json', {'ids': ids, 'model_sha256': checked.sha256, 'included': expected,
        'excluded': sorted([ids['c'],ids['residual-c']]), 'retained_residual': ids['residual-b'],
        'excluded_residual': ids['residual-c'], 'selections': selection,
        'source_of_expected_sets': 'Direct construction above, prior to any gate call.',
        'reverse_included': sorted([ids['b'], ids['residual-b']])})
    config = core.ac_formal_gate.select_checker(LEAN, Path(sys.executable), 600)
    assert config['runtime_identity']['sha256'] == EXPECTED_RUNTIME
    save(OUT / 'checker.json', config)
    print('Prepared new eight-record model; literal directed-closure, residual and reverse-direction expectations pass.', flush=True)


def standalone():
    entry = [sys.executable, '-I', '-S', '-B', str(LEAN/'scripts/formal_gate.py')]
    code, verified, fresh = call(entry + ['verify', '--request', str(OUT/'request.json'),
        '--output', str(OUT/'verified')], OUT/'commands/verify')
    assert code == 0 and verified['status'] == 'verified', verified
    assert verified['runtime_identity']['sha256'] == EXPECTED_RUNTIME
    code, replayed, replay = call(entry + ['check-evidence', '--bundle', str(OUT/'verified'),
        '--output', str(OUT/'replayed')], OUT/'commands/replay')
    assert code == 0 and replayed['status'] == 'verified', replayed
    views = load(OUT/'views.json')
    views[0]['populations']['residuals'][0]['uncertainty']['statement'] = 'Forged resolution of retained uncertainty.'
    save(OUT/'tampered-views.json', views)
    request = load(OUT/'request.json')
    request['supplied_views'] = {'path': str(OUT/'tampered-views.json'),
        'raw_sha256': sha((OUT/'tampered-views.json').read_bytes())}
    save(OUT/'tampered-request.json', request)
    code, refused, tamper = call(entry + ['verify', '--request', str(OUT/'tampered-request.json'),
        '--output', str(OUT/'tamper-refusal')], OUT/'commands/tamper')
    assert code == 2 and refused['status'] == 'refused', refused
    save(OUT/'STANDALONE.json', {'verify': verified, 'replay': replayed, 'tamper': refused,
        'costs_seconds': {'verify': fresh['elapsed_seconds'], 'replay': replay['elapsed_seconds'], 'tamper': tamper['elapsed_seconds']}})


class PublicCase:
    def __init__(self, name, missing_authority=False):
        self.root = OUT/name
        self.root.mkdir(exist_ok=False)
        self.f = Fixture(self.root)
        self.f.model_source = self.f.write('inputs/model.json', (OUT/'model.json').read_bytes())
        model = ac_graph.validate(load(OUT/'model.json'))
        self.f.model = {'source': self.f.model_source, 'format': 'model', 'model_id': model.identity, 'model_sha256': model.sha256}
        actor = self.f.write('inputs/review_worker.py', b'import hashlib,json,sys\nfrom pathlib import Path\ndata=sys.stdin.buffer.read()\nPath(sys.argv[1]).write_bytes(data)\nprint(json.dumps({"stdin_sha256":hashlib.sha256(data).hexdigest(),"stdin_bytes":len(data)}))\n')
        executor = self.f.policy['executors']['registered']
        executor['argv'] = [str(Path(sys.executable).resolve()), '-B', str(self.f.workspace/'inputs/review_worker.py'),
                            str(self.f.workspace/'outputs/received.bin')]
        executor['dependencies'] = [actor]
        executor['settings'] = {'timeout_ms': 5000, 'max_output_bytes': 100000}
        self.f.policy['formal_gate'] = {'checker': load(OUT/'checker.json'), 'required_targets': ['worker']}
        if missing_authority:
            self.f.policy['grants']['work']['targets'] = []
        self.policy_sha256 = self.f.runtime().policy_sha256
        self.counter = 0

    def invoke(self, operation, args):
        self.counter += 1
        request = {'schema': core.REQUEST, 'id': 'independent-review-'+str(self.counter), 'operation': operation, 'arguments': args}
        _, response, _ = call([sys.executable, '-B', str(GRAPHIFY/'code/ac_support.py'), '--policy', str(self.root/'policy.json'),
            '--policy-sha256', self.policy_sha256, '--principal', 'executive', 'call', '--request', '-'],
            self.root/'calls'/str(self.counter), request)
        return response

    def artifact(self, ref):
        raw = (self.f.evidence/'objects'/(ref['sha256']+'.json')).read_bytes()
        assert sha(raw) == ref['sha256']
        return json.loads(raw)

    def context(self):
        response = self.invoke('context.assemble', {'packet': self.f.packet(),
            'models': [{'model': self.f.model, 'selections': load(OUT/'expectations.json')['selections']}],
            'sources': [], 'late_acquisition': [], 'envelope': {'capacity_bytes': None, 'boundary': 'executor-stdin-utf8',
            'host_context': {'state': 'unknown', 'bytes': None, 'evidence': None}}})
        assert response['status'] == 'ok', response
        ref = response['result']['artifact']
        return ref, self.artifact(ref)['payload']

    def preflight(self, context):
        response = self.invoke('contract.preflight', {'context': context, 'grant_id': 'work', 'executor_id': 'registered',
            'result_key': 'independent-review', 'observations': []})
        assert response['status'] == 'ok', response
        gate = self.artifact(response['result']['value']['formal_evidence'])['payload']
        assert gate['status'] == 'verified', gate
        return response


def path():
    case = PublicCase('required-worker')
    context_ref, context = case.context()
    receipt = case.preflight(context_ref)
    assert receipt['result']['value']['decision'] == 'admitted', receipt
    response = case.invoke('dispatch.start', {'preflight': receipt['result']['artifact']})
    assert response['status'] == 'ok', response
    attempt = response['result']['value']['attempt']
    deadline = time.monotonic()+180
    while time.monotonic() < deadline:
        observed = case.invoke('dispatch.observe', {'attempt': attempt, 'after_event': 0})
        assert observed['status'] == 'ok', observed
        value = observed['result']['value']
        if value['process_end'] is not None:
            break
        time.sleep(2)
    else:
        raise AssertionError('No observed Worker process end within independent bound')
    assert value['process_end']['returncode'] == 0, value
    raw = (case.f.workspace/'outputs/received.bin').read_bytes()
    assert raw == context['rendered_utf8'].encode(), 'Actual Worker bytes differ from the selected Context'
    stdout = case.artifact(value['output']['stdout'])['payload']
    worker = json.loads(base64.b64decode(stdout['bytes_base64']))
    assert worker == {'stdin_sha256': sha(raw), 'stdin_bytes': len(raw)}, worker
    assert context['rendered_sha256'] == sha(raw)
    dispatch_use = case.artifact(value['anchor']['formal_use'])['payload']
    assert dispatch_use['stage'] == 'dispatch' and dispatch_use['binding']['rendered_sha256'] == sha(raw)
    checked = [e for e in value['events'] if e['kind']=='formal_gate_verified']
    assert len(checked)==1, checked
    supervisor_ref = checked[0]['data']['formal_use']
    use = case.artifact(supervisor_ref)
    assert use['payload']['stage']=='supervisor' and use['provenance']['attempt']==attempt
    assert use['payload']['binding']['rendered_sha256'] == sha(raw)
    save(OUT/'DELIVERY.json', {'context': context_ref, 'preflight': receipt['result']['artifact'], 'attempt': attempt,
        'dispatch_formal_use': value['anchor']['formal_use'], 'supervisor_formal_use': supervisor_ref,
        'worker_stdout': value['output']['stdout'], 'stdin_bytes': len(raw), 'stdin_sha256': sha(raw),
        'observed_process_end': value['process_end'], 'events': value['events'],
        'claim': 'Exact checked Context bytes observed in controlled actual Worker stdin; no semantic, external-effect or descendant-end claim.'})
    denied = PublicCase('proof-without-authority', missing_authority=True)
    cref, _ = denied.context()
    rejected = denied.preflight(cref)
    assert rejected['result']['value']['decision']=='rejected', rejected
    refused = denied.invoke('dispatch.start', {'preflight': rejected['result']['artifact']})
    assert refused['status']=='refused', refused
    assert not (denied.f.workspace/'outputs/received.bin').exists()
    save(OUT/'AUTHORITY.json', {'formal_status': 'verified', 'preflight': rejected,
        'dispatch': refused, 'worker_output_absent': True,
        'claim': 'Successful formal checking does not supply a missing operation grant.'})
    print('Independent public required Worker delivery and good-proof/missing-authority control passed.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('stage', choices=['prepare', 'standalone', 'path'])
    args = parser.parse_args()
    globals()[args.stage]()
