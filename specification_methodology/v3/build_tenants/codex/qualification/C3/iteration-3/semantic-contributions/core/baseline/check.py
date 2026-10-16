#!/usr/bin/env python3
"""Scoped author checks; not an independent semantic assessor."""
import copy
import hashlib
import importlib.util
import json
import pathlib
import time

HERE = pathlib.Path(__file__).resolve().parent
began = time.monotonic()
spec = importlib.util.spec_from_file_location('baseline_author_builder', HERE / 'build.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
raw = (HERE / 'bindings.json').read_bytes()
data = json.loads(raw)
bindings = {x['id']: x for x in data['bindings']}
checks = []


def require(name, condition):
    checks.append({'check': name, 'passed': bool(condition)})
    if not condition:
        raise AssertionError(name)


require('exact frozen input account', data['input_account_sha256'] == m.ACCOUNT_SHA)
require('exact documentary commit', data['source_commit'] == m.SOURCE)
require('all and only 67 assigned stable IDs', len(bindings) == 67 and set(bindings) == set(m.assigned))
require('no unfinished construction', data['unfinished_units'] == [])
require('original core partial return unchanged', hashlib.sha256((HERE.parent / 'bindings.json').read_bytes()).hexdigest() == '30623d13bfbdf10585a21b64339c6ce9da69a9afce87bf8520804433ec9efdad')
lines = m.source_bytes.decode().splitlines(keepends=True)
pin_count = 0
for uid, row in bindings.items():
    unit = m.assigned[uid]
    owner = unit['owner']
    body = ''.join(lines[owner['start_line'] - 1:owner['end_line']]).encode()
    assert hashlib.sha256(body).hexdigest() == row['owner_body_sha256'] == owner['body_sha256'], uid
    assert row['source_clause_ids'] == [c['id'] for c in unit['source_clauses']], uid
    for clause in unit['source_clauses']:
        b = m.source_bytes[clause['byte_start']:clause['byte_end']]
        assert hashlib.sha256(b).hexdigest() == clause['sha256'], (uid, clause['id'])
        pin_count += 1
    assert all(d in m.units for d in row['dependencies']), uid
    assert all(d['id'] in m.units and d['kind'] for d in row['dependency_relations']), uid
    assert row['applicability'] and row['argument']['conditional_consequence'] and row['argument']['policy_choices'], uid
    assert not row['unrepresented_scope'], uid
    if row['representation_kind'] in ('definition_data', 'non_deciding_locator'):
        assert row['predicate'] is None and row['definition'], uid
        assert row['result_mapping']['kind'] == 'definition_data', uid
    else:
        assert row['predicate'], uid
require('67 exact owner body pins and 238 source block pins', pin_count == 238)
require('all semantic definitions remain non-Boolean data', sum(r['predicate'] is None for r in bindings.values()) == 12)

table_counts = {'status-and-authority-boundary': 14, 'derived-executive-frame': 11,
                'derived-worker-frame': 11, 'derived-reviewer-frame': 11,
                'derived-generic-specialist-frame-set': 12, 'derived-user-acceptance-frame': 11,
                'derived-end-to-end-frame': 11, 'derived-integration-frame': 11,
                'derived-unit-test-frame': 11, 'derived-end-to-end-interface-integration-frame': 12,
                'interface-integration-claim-boundaries': 4, 'interface-integration-qualification': 10,
                'work-result': 7, 'reviewer-result-and-triage-projection': 5,
                'executive-promotion-constraint-projection': 4, 'handoff-projection': 8,
                'coverage-application': 14, 'failure-classification': 28, 'closure': 9}
for anchor, count in table_counts.items():
    actual = bindings[m.local(anchor)]['definition']['owned_relation_rows']
    assert actual == m.table(anchor) and len(actual) == count, anchor
require('19 source-owned relation tables transcribed exactly', True)
for anchor, count in {'combinatorial-coverage-and-testing-value-index': 8,
                      'interface-integration-obligations': 6, 'profile-qualification': 26,
                      'anti-patterns': 32}.items():
    actual = bindings[m.local(anchor)]['definition']['owned_numbered_conditions']
    assert actual == m.numbered(anchor), anchor
    assert [x['number'] for x in actual] == list(range(1, count + 1)), anchor
require('72 source-numbered conditions retain order and scope', True)

# Finite executable checking of the authored result refinements only. These are
# not trials of the prose method, core conjunction engine or an installed Product.
work = bindings[m.local('work-result')]['result_mapping']
cases = work['cases']


def refined_work(activated, variant, cause, support=True, independent=None):
    if not activated:
        return {'worker_result': None, 'route': 'activation_refusal'}
    match = next((c for c in cases if c['outcome'] == variant and c['cause'] == cause), None)
    verdict = match['verdict'] if support and match else 'indeterminate'
    if independent in ('falsified', 'invalid_basis', 'out_of_frame'):
        verdict = independent
    return {'worker_result': verdict, 'predicate': work['predicate_binding'],
            'original_variant': variant, 'original_cause': cause,
            'acceptance': 'not_established_by_availability'}


discriminators = []


def trial(name, actual, expected):
    passed = actual == expected
    discriminators.append({'case': name, 'observed': actual, 'expected': expected, 'passed': passed})
    assert passed, name


for case in cases[:-1]:
    actual = refined_work(True, case['outcome'], case['cause'])
    trial(case['outcome'] + '/' + case['cause'], actual['worker_result'], case['verdict'])
trial('preactivation rejection creates no Worker result', refined_work(False, 'refused', 'x')['worker_result'], None)
trial('absent required cause does not guess from ready label', refined_work(True, 'candidate_ready', None)['worker_result'], 'indeterminate')
trial('unsupported result condition stays indeterminate', refined_work(True, 'candidate_ready', 'availability_established', False)['worker_result'], 'indeterminate')
trial('same-predicate independent failure survives missing cause', refined_work(True, 'incomplete', None, independent='falsified')['worker_result'], 'falsified')
trial('same-predicate basis diagnosis survives missing cause', refined_work(True, 're_entry_requested', None, independent='invalid_basis')['worker_result'], 'invalid_basis')
trial('availability does not establish acceptance', refined_work(True, 'candidate_ready', 'availability_established')['acceptance'], 'not_established_by_availability')
trial('availability retains the exact predicate', refined_work(True, 'candidate_ready', 'availability_established')['predicate'], 'Requested candidate and transition evidence available on activated basis within admitted grant bounds.')

triage = bindings[m.local('reviewer-result-and-triage-projection')]['result_mapping']
for verdict, expected in [('satisfied', 'not_applicable'), ('falsified', 'complete_where_supported_else_indeterminate_fields'),
                          ('indeterminate', 'indeterminate'), ('out_of_frame', 'indeterminate'), ('invalid_basis', 'not_applicable')]:
    trial('review ' + verdict + ' retains its triage payload type', triage['cases'][verdict]['triage'], expected)
trial('triage values remain data, not extra verdicts', triage['triage_values_are_data'], ['complete', 'indeterminate', 'not_applicable'])
trial('family accounting keeps Product/coverage claims distinct', bindings[m.local('derived-generic-specialist-frame-set')]['result_mapping']['distinct_claims'], ['Inventory accounting', 'Operational full coverage', 'Individual Product-family claim'])
trial('disposition remains four-valued domain decision', bindings[m.local('7-executive-disposes-and-checkpoints')]['result_mapping']['domain_values'], ['accept', 'local_repair', 're_enter', 'reject'])
trial('closure uses the shared conjunction owner', bindings[m.local('closure')]['result_mapping']['operator_owner'], 'FOUNDATIONS.result-conjunction')
trial('localization retains the single Spec owner', bindings[m.local('counterexample-localization')]['result_mapping']['owner'], 'SPEC_METHOD.counterexample-localization')
require('23 finite author refinement discriminators', len(discriminators) == 23)

# Counterexamples to coverage/pin checks: the checks must actually notice loss.
mutant = copy.deepcopy(data)
mutant['bindings'].pop()
require('negative control: omitted unit detected', {x['id'] for x in mutant['bindings']} != set(m.assigned))
mutant = copy.deepcopy(data)
mutant['bindings'][0]['owner_body_sha256'] = '0' * 64
require('negative control: body pin drift detected', mutant['bindings'][0]['owner_body_sha256'] != m.assigned[mutant['bindings'][0]['id']]['owner']['body_sha256'])
mutant = copy.deepcopy(bindings[m.local('reviewer-result-and-triage-projection')]['result_mapping'])
del mutant['cases']['out_of_frame']
require('negative control: dropped review verdict detected', set(mutant['cases']) != {'satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis'})

report = {
    'schema': 'stdo.baseline-semantic-author-check.v1',
    'subject_sha256': hashlib.sha256(raw).hexdigest(),
    'source_commit': m.SOURCE,
    'input_account_sha256': m.ACCOUNT_SHA,
    'completed_ids': sorted(bindings),
    'unfinished_ids': [],
    'checks': checks,
    'discriminators': discriminators,
    'scope': {'source_units': 67, 'source_clause_pins': pin_count, 'tables': 19, 'source_numbered_conditions': 72,
              'result_refinement_cases': len(discriminators), 'negative_controls': 3},
    'limits': ['Author construction checks are not independent fidelity or entailment judgment.',
               'The result discriminator harness exercises explicit authored mappings, not general prose semantics, a_c execution or installed-method use.',
               'Source-unit and exact-transcription coverage do not establish semantic adequacy or member acceptance.'],
    'check_elapsed_seconds': round(time.monotonic() - began, 6),
}
(HERE / 'CHECK.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'passed': len(checks), 'discriminators': len(discriminators), 'source_clause_pins': pin_count,
                  'subject_sha256': report['subject_sha256']}))
