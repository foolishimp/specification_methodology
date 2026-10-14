"""Finite executable interpretation; not the Axiom Indexer semantic engine."""


def conjoin(values, join='S', basis=True, coverage=True):
    missing, unconfirmed, unresolved, invalid, outside, failures, citations = [], [], [], [], [], [], []
    components = dict(zip(('A', 'B'), values))
    components['join'] = join
    for name, value in components.items():
        if value in {'M', 'H'}:
            missing.append(name)
        elif value == 'N':
            unconfirmed.append(name)
        elif value == 'X':
            unresolved.append(name + ':unauthenticated')
        elif value == 'U':
            unresolved.append(name + ':undecidable')
        elif value == 'I':
            invalid.append(name)
        elif value == 'O':
            outside.append(name)
        elif value == 'F':
            failures.append(name)
            citations.append('source/' + name + '#counterexample')
        elif value != 'S':
            raise ValueError('outside finite input domain')
    if not basis:
        verdict = 'invalid_basis'
    elif failures:
        verdict = 'falsified'
    elif invalid:
        verdict = 'invalid_basis'
    elif outside:
        verdict = 'out_of_frame'
    elif missing or unconfirmed or unresolved or not coverage:
        verdict = 'indeterminate'
    else:
        verdict = 'satisfied'
    return {'predicate': 'all required A, B and material join hold',
            'verdict': verdict, 'performance': 'performed',
            'components': components, 'failures': failures, 'citations': citations,
            'missing_evaluations': missing, 'unresolved': unresolved,
            'unconfirmed_evaluations': unconfirmed,
            'coverage_performance': {
                name: ({'performance': 'not_performed', 'reason': 'never_started' if value == 'M' else 'aborted'}
                       if value in {'M', 'H'} else {'performance': 'unconfirmed', 'reason': 'conclusion_not_authenticated'}
                       if value in {'N', 'X'} else {'performance': 'performed', 'reason': 'evaluation_concluded'})
                for name, value in components.items()},
            'invalid_components': invalid, 'out_of_frame_components': outside,
            'coverage_known': coverage, 'composite_basis_interpretable': basis}


def refine(domain, predicate):
    # Each case is qualified by its actual predicate, not positive wording.
    if domain == 'candidate_ready' and predicate == 'availability':
        verdict = 'satisfied'
        performance = 'performed'
        effect = 'not_requested'
    elif domain == 'assessment_undecidable' and predicate == 'fitness':
        verdict, performance, effect = 'indeterminate', 'performed', 'not_requested'
    elif domain == 'out_of_scope' and predicate == 'event_scope_compatible':
        verdict, performance, effect = 'falsified', 'performed', 'not_started'
    elif domain == 'lost_acknowledgment' and predicate == 'effect_completed':
        verdict, performance, effect = 'indeterminate', 'performed', 'unknown'
    elif domain == 'yield' and predicate == 'yield_contract':
        verdict = 'satisfied'
        performance = 'performed'
        effect = 'not_requested'
    else:
        raise ValueError('outside the selected qualified refinement domain')
    return {'predicate': predicate, 'domain_outcome': domain, 'verdict': verdict,
            'performance': performance, 'effect': effect}


def legal_coordinates(verdict, performance):
    if verdict not in {'satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis'}:
        return False
    if performance == 'performed':
        return True
    return performance in {'not_performed', 'unconfirmed'} and verdict == 'indeterminate'


def observe_effect(unit_observations):
    """Known intended effect units; None means an unobserved completion state."""
    if not unit_observations:
        return 'not_requested'
    if any(value is None for value in unit_observations):
        return 'unknown'
    if all(value is True for value in unit_observations):
        return 'completed'
    if any(value is True for value in unit_observations):
        return 'partial'
    if 'reverted' in unit_observations:
        return 'reverted'
    return 'not_started'


def join_effects(states):
    seen = set(states)
    if not seen or seen == {'not_requested'}:
        state = 'not_requested'
    elif 'unknown' in seen:
        state = 'unknown'
    elif 'partial' in seen or ('completed' in seen and seen.intersection({'not_started', 'reverted'})):
        state = 'partial'
    elif seen <= {'completed', 'not_requested'}:
        state = 'completed'
    elif 'reverted' in seen and seen <= {'reverted', 'not_started', 'not_requested'}:
        state = 'reverted'
    elif seen <= {'not_started', 'not_requested'}:
        state = 'not_started'
    else:
        raise ValueError('outside the declared effect domain')
    return {'effect': state, 'component_effects': list(states)}


def recover(effect_state, idempotent, grant):
    if effect_state == 'completed':
        return 'retain_completed_progress'
    if not grant:
        return 'withhold_effect'
    if effect_state == 'not_started':
        return 'permitted_initial_dispatch'
    if effect_state == 'unknown' and idempotent:
        return 'permitted_idempotent_retry'
    return 'observe_or_return_unresolved'
