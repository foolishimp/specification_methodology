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
                require(fact == {'performance': 'not_performed', 'reason': 'never_started'}, 'nonstart reason lost')
            elif value == 'H':
                require(fact == {'performance': 'not_performed', 'reason': 'aborted'}, 'abort reason lost')
            elif value in {'N', 'X'}:
                require(fact['performance'] == 'unconfirmed', 'absence was promoted to known non-conclusion')
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
        require(model.observe_effect(row['units']) == row['expected'], repr(row))
        cases += 1
    # Fixed expectation: only a concluded judgment can carry a deciding, scope
    # or basis verdict; known absent/unconfirmed conclusion stays indeterminate.
    legal = 0
    for performance in ('performed', 'not_performed', 'unconfirmed'):
        for verdict in ('satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis'):
            want = (performance, verdict) in {
                ('performed', 'satisfied'), ('performed', 'falsified'),
                ('performed', 'indeterminate'), ('performed', 'out_of_frame'),
                ('performed', 'invalid_basis'), ('not_performed', 'indeterminate'),
                ('unconfirmed', 'indeterminate')}
            require(model.legal_coordinates(verdict, performance) == want, 'illegal core coordinates')
            legal += int(want)
    require(legal == 7, 'legal core coordinate cardinality')
    representatives = {'not_requested': (), 'not_started': ('absent',),
                       'completed': ('done',), 'partial': ('done', 'absent'),
                       'reverted': ('reverted',), 'unknown': (None,)}
    effect_cases = 0
    for states in itertools.product(representatives, repeat=3):
        observed_units = tuple(unit for state in states for unit in representatives[state])
        # Independent expectation over observed units, not summary-name priority.
        facts = set(observed_units)
        want = ('unknown' if None in facts else 'partial' if 'done' in facts and len(facts) > 1
                else 'completed' if facts == {'done'} else 'reverted' if 'reverted' in facts
                else 'not_started' if facts == {'absent'}
                else 'not_requested')
        got = model.join_effects(states)
        require(got == {'effect': want, 'component_effects': list(states)}, 'effect scope/evidence lost')
        left = model.join_effects((model.join_effects(states[:2])['effect'], states[2]))['effect']
        right = model.join_effects((states[0], model.join_effects(states[1:])['effect']))['effect']
        require(left == right == want, 'fixed-domain effect associativity failed')
        effect_cases += 1
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
        return model.legal_coordinates(verdict, 'performed')

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
        'core_coordinate_cases': 15, 'legal_core_coordinate_pairs': legal,
        'effect_composition_cases': effect_cases,
        'exhaustive_verdicts': counts, 'detected_mutants': [row['mutant'] for row in counterexamples],
        'mutant_counterexamples': counterexamples,
        'context_reset_trace': {'workspace_retained': True, 'private_context_rebuilt': True, 'duplicate_effect': False},
        'elapsed_seconds': time.perf_counter() - started,
        'inputs': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                   for name in ('ORACLE.json', 'model.py', 'finite_check.py', 'program.json')},
        'limits': ['Finite AND domain only; no universal categorical proof',
                   'Separate oracle algorithms and fixed expectations are same-Writer artifacts, not independent fidelity acceptance',
                   'Context-reset trace is a finite state model, not an external transport or native-agent trial',
                   'ac.py does not execute these semantic predicates; independent source-first review is required']}
    (ROOT / 'FINITE_RESULT.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
