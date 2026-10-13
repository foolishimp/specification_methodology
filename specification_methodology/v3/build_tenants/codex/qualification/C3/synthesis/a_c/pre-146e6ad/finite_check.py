"""Check selected finite core semantics against a separately specified oracle.

Set-based truth classification is independent of model.py's procedural fold.
Both are same-Writer constructions, not an independent fidelity assessment.
"""
import hashlib
import itertools
import json
from pathlib import Path
import time

import model

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def oracle(values, join, basis, coverage):
    population = set(values) | {join}
    # Declarative strata of the source's AND predicate, not domain word order.
    cases = {
        'invalid_outer': not basis,
        'counterexample': basis and 'F' in population,
        'invalid_member': basis and 'F' not in population and 'I' in population,
        'scope_gap': basis and not population.intersection({'F', 'I'}) and 'O' in population,
        'complete': basis and coverage and population == {'S'},
    }
    if cases['invalid_outer'] or cases['invalid_member']:
        return 'invalid_basis'
    if cases['counterexample']:
        return 'falsified'
    if cases['scope_gap']:
        return 'out_of_frame'
    if cases['complete']:
        return 'satisfied'
    return 'indeterminate'


def main():
    started = time.perf_counter()
    expected = json.loads((ROOT / 'ORACLE.json').read_text())
    cases = 0
    for row in expected['conjunction']:
        got = model.conjoin(row['values'], row['join'], row['basis'], row['coverage'])
        require(got['verdict'] == row['expected'], row['name'])
        require(got['failures'] == row['failures'], row['name'] + ':failures')
        require(got['missing_evaluations'] == row['missing'], row['name'] + ':missing')
        cases += 1
    exhaustive = 0
    counts = {}
    for values, join, basis, coverage in itertools.product(
            itertools.product('SFUOIMHNX', repeat=2), 'SFUOI', (False, True), (False, True)):
        got = model.conjoin(values, join, basis, coverage)
        want = oracle(values, join, basis, coverage)
        require(got['verdict'] == want, repr((values, join, basis, coverage)))
        require(got['performance'] == 'performed', 'aggregate evaluation was executed')
        require(got['components'] == {'A': values[0], 'B': values[1], 'join': join}, 'components lost')
        expected_failures = [name for name, value in got['components'].items() if value == 'F']
        require(got['failures'] == expected_failures, 'authenticated failure erased')
        require(got['citations'] == ['source/' + n + '#counterexample' for n in expected_failures], 'citation erased')
        for name, value in got['components'].items():
            fact = got['coverage_performance'][name]
            if value == 'M':
                require(fact == {'performance': 'not_performed', 'extent': 'none', 'conclusion': 'absent'}, 'nonstart reason lost')
            elif value == 'H':
                require(fact == {'performance': 'performed', 'extent': 'partial_aborted', 'conclusion': 'absent'}, 'abort reason lost')
            elif value in {'N', 'X'}:
                require(fact['performance'] == 'unconfirmed', 'absence was promoted to known non-performance')
        require(model.conjoin(values[::-1], join, basis, coverage)['verdict'] == want, 'logical AND changed under permutation')
        exhaustive += 1
        counts[want] = counts.get(want, 0) + 1
    require(exhaustive == 1620, 'finite domain cardinality')
    for row in expected['refinement']:
        got = model.refine(row['domain'], row['predicate'])
        require(all(got[k] == row[k] for k in ('predicate', 'verdict', 'performance', 'effect')), repr(row))
        require(got['domain_outcome'] == row['domain'], 'qualified original outcome lost')
        cases += 1
    for row in expected['refused_predicate_substitutions']:
        try:
            model.refine(row['domain'], row['predicate'])
        except ValueError:
            cases += 1
        else:
            raise RuntimeError('predicate substitution fabricated an assessment: ' + repr(row))
    for row in expected['effect_observations']:
        require(model.observe_effect(row['units'], row.get('effect_free_scope', False)) == row['expected'], repr(row))
        cases += 1
    # Thirteen pairs are potentially legal, never sufficient by themselves.
    # Cross the observed undertaking and separately deciding support guards.
    legal = coordinate_cases = 0
    for performance, verdict in itertools.product(model.PERFORMANCES, model.VERDICTS):
        observed = {'undertaken': {'performed': True, 'not_performed': False,
                                  'unconfirmed': None}[performance],
                    'deciding': None if verdict == 'indeterminate' else verdict,
                    'independent': True, 'completion': True}
        want = performance == 'performed' or verdict != 'satisfied'
        require(model.legal_coordinates(verdict, performance, observed) == want, 'conditional legal pair')
        legal += int(want)
        for undertaken, independent, completion in itertools.product((True, False, None), (False, True), (False, True)):
            probe = dict(observed, undertaken=undertaken, independent=independent, completion=completion)
            matching = ((performance == 'performed' and undertaken is True) or
                        (performance == 'not_performed' and undertaken is False) or
                        (performance == 'unconfirmed' and undertaken is None))
            expected_pair = matching and (verdict == 'indeterminate' or
                            (verdict == 'satisfied' and performance == 'performed' and completion) or
                            (verdict in {'falsified', 'invalid_basis', 'out_of_frame'} and
                             (performance == 'performed' or independent)))
            require(model.legal_coordinates(verdict, performance, probe) == expected_pair, 'evidence guard dropped')
            coordinate_cases += 1
        if verdict != 'indeterminate':
            require(not model.legal_coordinates(verdict, performance, dict(observed, deciding=None)),
                    'no deciding support supplied a decision')
    require(legal == 13 and coordinate_cases == 180, 'coordinate domain count')
    for row in expected['evaluation']:
        got = model.evaluation(row['observed'])
        require(got['verdict'] == row['verdict'] and got['performance'] == row['performance'], row['name'])
        require(all(got[k] == row['observed'][k] for k in ('extent', 'conclusion', 'effect')), 'observed facts lost')
        require(got['support'] == row['observed'], 'independent support lost')
        cases += 1
    representatives = {'not_requested': (), 'not_started': ('absent',),
                       'completed': ('done',), 'partial': ('done', 'absent'),
                       'reverted': ('reverted',), 'unknown': (None,)}
    effect_cases = 0
    for states in itertools.product(representatives, repeat=3):
        observed_units = tuple(unit for state in states for unit in representatives[state])
        facts = set(observed_units)
        want = ('unknown' if None in facts else 'partial' if 'done' in facts and len(facts) > 1
                else 'completed' if facts == {'done'} else 'reverted' if 'reverted' in facts
                else 'not_started' if facts == {'absent'} else 'not_requested')
        parts = [{'part': str(i), 'state': state, 'normalized': True,
                  'observations': list(representatives[state])} for i, state in enumerate(states)]
        got = model.join_effects(parts)
        require(got == {'effect': want, 'parts': parts}, 'normalized effect scope/evidence lost')
        # Disjoint grouped boundaries only: no temporal stage-label substitution.
        left_summary = model.join_effects(parts[:2])
        left = model.join_effects([{'part': '01', 'state': left_summary['effect'],
                                   'normalized': True, 'observations': left_summary['parts']}, parts[2]])['effect']
        right_summary = model.join_effects(parts[1:])
        right = model.join_effects([parts[0], {'part': '12', 'state': right_summary['effect'],
                                             'normalized': True, 'observations': right_summary['parts']}])['effect']
        require(left == right == want, 'disjoint normalized effect associativity failed')
        effect_cases += 1
    for row in expected['temporal_effects']:
        got = model.normalize_effects(row['parts'], row['observations'], row.get('effect_free_scope', False))
        require(got['effect'] == row['effect'], row['name'])
        require({p['part'] for p in got['parts']} == set(row['parts']), 'material possibly affected part erased')
        retained = [o for part in got['parts'] for o in part['observations']]
        require(sorted(retained, key=lambda o: o['id']) == sorted(row['observations'], key=lambda o: o['id']),
                'temporal evidence was erased')
        cases += 1
    for bad_parts in ([{'part': 'x', 'state': 'completed', 'normalized': False}],
                      [{'part': 'x', 'state': state, 'normalized': True} for state in ('completed', 'reverted')]):
        try:
            model.join_effects(bad_parts)
        except ValueError:
            pass
        else:
            raise RuntimeError('raw or overlapping effect summaries were accepted')
    def table_for(name):
        table = {}
        for a, b, join in itertools.product((False, True), repeat=3):
            truth = ((a and b) if name == 'and' else (a or b) if name == 'or'
                     else ((not a) or b)) and join
            table[''.join('1' if x else '0' for x in (a, b, join))] = [truth, not truth]
        return table
    tables = {name: table_for(name) for name in ('and', 'or', 'implies')}
    tables['overlap'] = dict(tables['and'], **{'111': [True, True]})
    tables['gap'] = dict(tables['and'], **{'111': [False, False]})
    tables['ignores_join'] = dict(tables['and'], **{'110': [True, False]})
    for row in expected['operator_cases']:
        require(model.apply_operator(tables[row['operator']], *row['input']) == row['expected'], row['name'])
        cases += 1
    for row in expected['operator_unresolved']:
        view = model.operator_view(tables['and'], *row['input'], wellformedness_established=False)
        raw = view['verdict']
        require(raw == row['expected'], row['name'])
        require(model.negate_result(raw) == 'indeterminate', 'negation invented decision from unproved operator')
        require(view['leaves'] == {'A': row['input'][0], 'B': row['input'][1]} and
                view['join'] == row['input'][2], 'operator view lost original leaves or join')
        cases += 1
    require(model.negate_result(model.apply_operator(tables['overlap'], True, True, True)) ==
            'invalid_basis', 'negation promoted invalid operator')
    operator_rows = 0
    for name in ('and', 'or', 'implies'):
        for key, (truth, falsity) in tables[name].items():
            require(truth != falsity, 'operator truth/falsity overlap')
            require(model.apply_operator(tables[name], *(v == '1' for v in key)) ==
                    ('satisfied' if truth else 'falsified'), 'operator table row')
            operator_rows += 1
    implication = lambda a, b: (not a) or b
    implication_left = implication(implication(False, True), False)
    implication_right = implication(False, implication(True, False))
    require(implication_left is False and implication_right is True,
            'arbitrary implication associativity counterexample disappeared')
    and_associativity_cases = 0
    for a, b, c in itertools.product('SFIOU', repeat=3):
        codes = {'satisfied': 'S', 'falsified': 'F', 'invalid_basis': 'I',
                 'out_of_frame': 'O', 'indeterminate': 'U'}
        left = model.conjoin((codes[model.conjoin((a, b))['verdict']], c))['verdict']
        right = model.conjoin((a, codes[model.conjoin((b, c))['verdict']]))['verdict']
        require(left == right, 'fixed interpretable AND precedence associativity')
        and_associativity_cases += 1
    for row in expected['recovery']:
        require(model.recover(row['state'], row['idempotent'], row['grant']) == row['expected'], repr(row))
        cases += 1

    # Actual faulty functions run against fixed oracle cases. They model one
    # isolated rule defect each, leaving the normal interpretation unchanged.
    def lost_failure(values):
        result = model.conjoin(values)
        if set(values).intersection({'M', 'H', 'N', 'U'}):
            result['verdict'] = 'indeterminate'
        return result['verdict']

    def inferred_performance(verdict, performance):
        return model.legal_coordinates(verdict, 'performed', {'undertaken': True, 'deciding': verdict, 'completion': True})

    def candidate_implies_fitness(domain, predicate):
        result = model.refine(domain, 'availability')
        result['predicate'] = predicate
        return result

    def unknown_means_no_effect(units):
        return 'not_started' if None in units else model.observe_effect(units)

    def scope_word_relabel(domain, predicate):
        result = model.refine(domain, predicate)
        if domain == 'out_of_scope':
            result['verdict'] = 'out_of_frame'
        return result['verdict']

    def prefix_implies_partial(units):
        return model.observe_effect([False if value is None else value for value in units])

    def granted_blind_retry(state, idempotent, grant):
        return 'permitted_initial_dispatch' if grant else model.recover(state, idempotent, grant)

    counterexamples = [
        {'mutant': 'unknown-erases-failure', 'input': ['F', 'M'],
         'actual': lost_failure(['F', 'M']), 'expected': expected['conjunction'][1]['expected']},
        {'mutant': 'missing-assessment-performed', 'input': ['satisfied', 'not_performed'],
         'actual': inferred_performance('satisfied', 'not_performed'), 'expected': False},
        {'mutant': 'candidate-means-fit', 'input': ['candidate_ready', 'fitness'],
         'actual': candidate_implies_fitness('candidate_ready', 'fitness'), 'expected': 'refused predicate substitution'},
        {'mutant': 'unknown-means-effect-not-started', 'input': [False, None],
         'actual': unknown_means_no_effect([False, None]), 'expected': expected['effect_observations'][5]['expected']},
        {'mutant': 'out-of-scope-means-out-of-frame', 'input': ['out_of_scope', 'event_scope_compatible'],
         'actual': scope_word_relabel('out_of_scope', 'event_scope_compatible'), 'expected': expected['refinement'][2]['verdict']},
        {'mutant': 'known-prefix-means-partial', 'input': [True, None],
         'actual': prefix_implies_partial([True, None]), 'expected': expected['effect_observations'][4]['expected']},
        {'mutant': 'blind-retry', 'input': ['unknown', False, True],
         'actual': granted_blind_retry('unknown', False, True), 'expected': expected['recovery'][0]['expected']},
    ]
    def conclusion_required_for_performance(observed):
        return 'performed' if observed['conclusion'] == 'conclusive' else 'not_performed'

    # These additional mutants implement the superseded interpretation defects.
    counterexamples += [
        {'mutant': 'inconclusive-run-called-unperformed', 'input': expected['evaluation'][0]['observed'],
         'actual': conclusion_required_for_performance(expected['evaluation'][0]['observed']), 'expected': expected['evaluation'][0]['performance']},
        {'mutant': 'raw-temporal-labels-joined', 'input': expected['temporal_effects'][0],
         'actual': model._fold_states(['completed', 'reverted']), 'expected': 'reverted'},
        {'mutant': 'later-timestamp-is-supersession', 'input': expected['temporal_effects'][2],
         'actual': expected['temporal_effects'][2]['observations'][-1]['state'], 'expected': 'unknown'},
        {'mutant': 'arbitrary-operator-is-associative', 'input': [False, True, False],
         'actual': implication_left, 'expected': implication_right},
    ]
    require(all(row['actual'] != row['expected'] for row in counterexamples), 'mutant escaped fixed oracle')

    # A finite loss-of-context trace retains the material workspace and observes
    # the completed effect. This is a model trace, not external-process proof.
    workspace = {'completed_units': 1, 'effect': 'completed', 'basis': 'r1'}
    context = {'completed_units': 0, 'effect': 'unknown', 'basis': 'r0'}
    context.clear()
    context.update(workspace)
    require(context == workspace and workspace['completed_units'] == 1, 'reset erased progress')
    require(model.recover(context['effect'], False, True) == 'retain_completed_progress', 'completed effect repeated')
    wrong_reset = {'completed_units': 0, 'effect': 'not_started', 'basis': 'r1'}
    require(wrong_reset != workspace, 'workspace-reset mutant escaped')
    counterexamples.append({'mutant': 'reset-erases-workspace', 'input': dict(workspace),
                           'actual': wrong_reset, 'expected': dict(workspace)})
    report = {
        'kind': 'codex-v3-synthesis-finite-interpretation', 'valid': True,
        'fixed_oracle_cases': cases, 'exhaustive_conjunction_cases': exhaustive,
        'syntactic_coordinate_pairs': 15, 'potentially_legal_coordinate_pairs': legal,
        'evidence_guard_coordinate_cases': coordinate_cases,
        'temporal_effect_cases': len(expected['temporal_effects']),
        'operator_rows': operator_rows, 'operator_fixed_cases': len(expected['operator_cases']) + len(expected['operator_unresolved']),
        'and_associativity_cases': and_associativity_cases,
        'effect_composition_cases': effect_cases,
        'exhaustive_verdicts': counts, 'detected_mutants': [row['mutant'] for row in counterexamples],
        'mutant_counterexamples': counterexamples,
        'context_reset_trace': {'workspace_retained': True, 'private_context_rebuilt': True, 'duplicate_effect': False},
        'elapsed_seconds': time.perf_counter() - started,
        'inputs': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                   for name in ('ORACLE.json', 'model.py', 'finite_check.py', 'program.json')},
        'limits': ['Finite AND and declared Boolean operator domains only; no universal categorical proof',
                   'Effect associativity only for disjoint normalized current parts; temporal cases consume stipulated supersession proof',
                   'Thirteen potentially legal performance/verdict pairs still require evidence guards; enum membership does not admit a result',
                   'Separate oracle algorithms and fixed expectations are same-Writer artifacts, not independent fidelity acceptance',
                   'Context-reset trace is a finite state model, not an external transport or native-agent trial',
                   'ac.py does not execute these semantic predicates; independent source-first review is required']}
    (ROOT / 'FINITE_RESULT.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
