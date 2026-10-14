"""Bounded executable interpretation, not a production result carrier or ac.py.

Evidence booleans/labels here stand for the expressly stipulated fixture facts.
They do not authenticate arbitrary real-world evidence. Temporal normalization
consumes a supplied same-part supersession proof; it does not invent one.
"""
VERDICTS = ('satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis')
PERFORMANCES = ('performed', 'not_performed', 'unconfirmed')
EFFECTS = ('not_requested', 'not_started', 'completed', 'partial', 'reverted', 'unknown')


def conjoin(values, join='S', basis=True, coverage=True):
    missing, unconfirmed, unresolved, invalid, outside, failures, citations = [], [], [], [], [], [], []
    components = dict(zip(('A', 'B'), values))
    components['join'] = join
    for name, value in components.items():
        if value in {'M', 'H'}:
            missing.append(name)
        elif value == 'N':
            missing.append(name)
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
    facts = {}
    for name, value in components.items():
        if value == 'M':
            facts[name] = {'performance': 'not_performed', 'extent': 'none', 'conclusion': 'absent'}
        elif value == 'H':
            facts[name] = {'performance': 'performed', 'extent': 'partial_aborted', 'conclusion': 'absent'}
        elif value in {'N', 'X'}:
            facts[name] = {'performance': 'unconfirmed', 'extent': 'unknown', 'conclusion': 'not_authenticated'}
        else:
            facts[name] = {'performance': 'performed', 'extent': 'observed', 'conclusion': 'returned'}
    return {'predicate': 'all required A, B and material join hold',
            'verdict': verdict, 'performance': 'performed',
            'components': components, 'failures': failures, 'citations': citations,
            'missing_evaluations': missing, 'unresolved': unresolved,
            'unconfirmed_evaluations': unconfirmed, 'coverage_performance': facts,
            'invalid_components': invalid, 'out_of_frame_components': outside,
            'coverage_known': coverage, 'composite_basis_interpretable': basis}


REFINEMENTS = {
    ('candidate_ready', 'availability', 'candidate_and_evidence_within_bounds'): 'satisfied',
    ('assessment_undecidable', 'fitness', 'insufficient_evidence'): 'indeterminate',
    ('out_of_scope', 'event_scope_compatible', 'compatibility_counterexample'): 'falsified',
    ('lost_acknowledgment', 'effect_completed', 'completion_unobserved'): 'indeterminate',
    ('yield', 'yield_contract', 'mandate_and_yield_conditions_established'): 'satisfied',
}


def performance_from_evidence(evidence):
    """undertaken is an evidenced fact or None, not an omniscient world fact."""
    fact = evidence.get('undertaken')
    if fact is True:
        return 'performed'
    if fact is False:
        return 'not_performed'
    return 'unconfirmed'


def admissible_decision(evidence):
    """The finite guard retains a claim even when it supplies no decision.

    deciding names claimed support on the exact predicate. Independent says
    it is admissible independently of this selected evaluation's undertaking.
    Predicate-specific evidence authentication remains a fixture assumption.
    """
    claim = evidence.get('deciding')
    performance = performance_from_evidence(evidence)
    if claim not in {'satisfied', 'falsified', 'out_of_frame', 'invalid_basis'}:
        return None
    if claim == 'satisfied':
        return claim if performance == 'performed' and evidence.get('completion') is True else None
    return claim if performance == 'performed' or evidence.get('independent') is True else None


def legal_coordinates(verdict, performance, evidence):
    if verdict not in VERDICTS or performance not in PERFORMANCES:
        return False
    return (performance == performance_from_evidence(evidence) and
            verdict == (admissible_decision(evidence) or 'indeterminate'))


def evaluation(observed):
    """Finite decision projection; preserve raw support and its admitted part."""
    admitted = admissible_decision(observed)
    return {'performance': performance_from_evidence(observed),
            'verdict': admitted or 'indeterminate',
            'extent': observed['extent'], 'conclusion': observed['conclusion'],
            'support': dict(observed), 'admissible_support': admitted,
            'effect': observed['effect']}


def refine(domain, predicate, cause, evidence, separate_support=None):
    """Bounded map plus separately admitted negative/diagnostic support.

    The fixed subject/basis and evidence authentication are fixture premises.
    A flat deciding claim in the original contribution is retained, never
    substituted for its reason-sensitive map. Separate positive combination
    is outside this model: its own evaluation/result would be required.
    """
    mapping = REFINEMENTS.get((domain, predicate, cause))
    supported_reason = mapping is not None and evidence.get('reason_supported') is True
    mapped_evidence = dict(evidence, deciding=mapping if supported_reason else None,
                           independent=False)
    mapped_result = evaluation(mapped_evidence)
    separate = dict(separate_support) if separate_support is not None else None
    admitted = None
    separate_status = 'not_supplied' if separate is None else 'not_admitted'
    if (separate is not None and separate.get('predicate') == predicate and
            separate.get('independent') is True and separate.get('admissible') is True and
            isinstance(separate.get('provenance'), str) and bool(separate['provenance'].strip())):
        if separate.get('deciding') in {'falsified', 'invalid_basis', 'out_of_frame'}:
            admitted = separate['deciding']
            separate_status = 'admitted_negative_or_diagnostic'
        elif separate.get('deciding') == 'satisfied':
            separate_status = 'positive_combination_not_modeled'
        elif separate.get('deciding') == 'indeterminate':
            separate_status = 'undecided_combination_not_modeled'
    mapped_verdict = mapped_result['verdict']
    # This conflict precedence is an explicit finite-model policy, not a
    # derived source law for resolving contradictory single-predicate evidence.
    # Retain both claims and expose conflict for an actual owner to decide.
    if 'falsified' in (mapped_verdict, admitted):
        verdict = 'falsified'
    elif admitted in {'invalid_basis', 'out_of_frame'}:
        verdict = admitted
    else:
        verdict = mapped_verdict
    support = dict(mapped_evidence, deciding=None if verdict == 'indeterminate' else verdict,
                   independent=admitted is not None)
    result = evaluation(support)
    result.update(domain_outcome=domain, predicate=predicate, cause=cause,
                  raw_evidence=dict(evidence), reason_supported=supported_reason,
                  unresolved_authentication=not supported_reason,
                  mapped_verdict=mapped_verdict, mapped_result=mapped_result,
                  separate_support=separate, admitted_separate_support=admitted,
                  separate_support_status=separate_status,
                  conflict=(admitted is not None and mapped_verdict != 'indeterminate'
                            and admitted != mapped_verdict))
    return result


def observe_effect(unit_observations, effect_free_scope=False):
    if not unit_observations:
        return 'not_requested' if effect_free_scope else 'unknown'
    if any(v is None or not (v is True or v is False or v == 'reverted')
           for v in unit_observations):
        return 'unknown'
    if all(v is True for v in unit_observations):
        return 'completed'
    if any(v is True for v in unit_observations):
        return 'partial'
    if 'reverted' in unit_observations:
        return 'reverted'
    return 'not_started'


def _fold_states(states):
    observed = set(states)
    if not observed <= set(EFFECTS):
        raise ValueError('Outside declared effect domain')
    if 'unknown' in observed:
        return 'unknown'
    if 'partial' in observed or ('completed' in observed and observed.intersection({'not_started', 'reverted'})):
        return 'partial'
    if 'completed' in observed:
        return 'completed'
    if 'reverted' in observed:
        return 'reverted'
    if 'not_started' in observed:
        return 'not_started'
    return 'not_requested'


def join_effects(parts, effect_free_scope=False):
    """Only disjoint normalized current parts may reach the summary operation."""
    ids = [p['part'] for p in parts]
    if len(ids) != len(set(ids)) or any(p.get('normalized') is not True for p in parts):
        raise ValueError('Normalize temporal overlap and establish disjoint parts first')
    return {'effect': (_fold_states(p['state'] for p in parts) if parts else
                       'not_requested' if effect_free_scope else 'unknown'), 'parts': list(parts)}


def normalize_effects(material_parts, observations, effect_free_scope=False, unrequested_parts=()):
    """Bounded fixture interpreter for externally established supersession.

    The fixture supplies exact same-part identities, order and evidence for
    supersedes. A timestamp alone never supersedes. Unaccounted material possible-effect
    parts, invalid reversal support or conflicting terminal observations remain
    unknown. This is not a general temporal/conflict-resolution theorem.
    """
    if not set(unrequested_parts) <= set(material_parts):
        raise ValueError('Unrequested part outside declared boundary')
    if len(material_parts) != len(set(material_parts)):
        raise ValueError('Duplicate declared part')
    if any(o['part'] not in material_parts for o in observations):
        raise ValueError('Observation outside declared effect boundary')
    parts = []
    for part in material_parts:
        rows = [dict(o) for o in observations if o['part'] == part]
        seen, superseded, invalid = {}, set(), False
        for row in rows:
            if row['id'] in seen or row['state'] not in EFFECTS or row['state'] == 'not_requested':
                raise ValueError('Invalid requested-part observation')
            targets = row.get('supersedes', [])
            supported = row.get('supersession_proved') is True and all(x in seen for x in targets)
            if targets and supported:
                superseded.update(targets)
            elif targets:
                invalid = True
            if row['state'] == 'reverted' and row.get('begun_and_reversal_proved') is not True:
                invalid = True
            seen[row['id']] = row
        heads = [r for r in rows if r['id'] not in superseded]
        states = {r['state'] for r in heads}
        state = next(iter(states)) if len(states) == 1 and not invalid else 'unknown'
        if state == 'not_started' and part in unrequested_parts:
            state = 'not_requested'
        parts.append({'part': part, 'state': state, 'normalized': True,
                      'observations': rows, 'current_observation_ids': [r['id'] for r in heads]})
    return join_effects(parts, effect_free_scope)


def operator_wellformed(table):
    """Complete, disjoint 2-leaf truth/falsity table, plus required join."""
    import itertools
    domain = {''.join('1' if b else '0' for b in row) for row in itertools.product((False, True), repeat=3)}
    if set(table) != domain:
        return False
    for key, outcomes in table.items():
        if len(outcomes) != 2 or any(type(b) is not bool for b in outcomes) or sum(outcomes) != 1:
            return False
        if key[-1] == '0' and outcomes != [False, True]:
            return False
    return True


def apply_operator(table, a, b, join, wellformedness_established=True):
    if not wellformedness_established:
        return 'indeterminate'
    if not operator_wellformed(table):
        return 'invalid_basis'
    key = ''.join('1' if bit else '0' for bit in (a, b, join))
    return 'satisfied' if table[key][0] else 'falsified'


def operator_view(table, a, b, join, wellformedness_established=True, predicate='Q(A,B) under required J'):
    return {'predicate': predicate,
            'verdict': apply_operator(table, a, b, join, wellformedness_established),
            'leaves': {'A': a, 'B': b}, 'join': join}


def negate_view(table, a, b, join, wellformedness_established=True):
    """A new bound predicate, NOT Q under the same required J, not a flip.

    The original result, leaf facts and required join remain. Negating Q never
    negates the required join or turns unknown operator validity into truth.
    """
    original = operator_view(table, a, b, join, wellformedness_established)
    if not wellformedness_established:
        verdict = 'indeterminate'
        negated_table = None
    elif not operator_wellformed(table):
        verdict = 'invalid_basis'
        negated_table = None
    else:
        negated_table = {}
        for key, outcomes in table.items():
            truth = (not outcomes[0]) and key[-1] == '1'
            negated_table[key] = [truth, not truth]
        verdict = apply_operator(negated_table, a, b, join)
    return {'predicate': 'NOT Q(A,B) under required J', 'verdict': verdict,
            'original_result': original, 'leaves': original['leaves'],
            'join': join, 'declared_table': negated_table}


def recover(effect, idempotent, grant):
    # Decision table only: effect/current authority/idempotence facts have
    # already been acquired and are fresh for this bound operation.
    if effect == 'completed':
        return 'retain_completed_progress'
    if not grant:
        return 'withhold_effect'
    if effect == 'not_started':
        return 'permitted_initial_dispatch'
    if effect == 'unknown' and idempotent:
        return 'permitted_idempotent_retry'
    return 'observe_or_return_unresolved'
