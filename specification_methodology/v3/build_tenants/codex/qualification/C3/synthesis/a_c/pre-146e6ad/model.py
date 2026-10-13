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


def refine(domain, predicate):
    # These fixed fixtures stipulate a supported effect-free operating scope
    # except where the case explicitly observes a requested external effect.
    cases = {
        ('candidate_ready', 'availability'): ('satisfied', 'not_requested'),
        ('assessment_undecidable', 'fitness'): ('indeterminate', 'not_requested'),
        ('out_of_scope', 'event_scope_compatible'): ('falsified', 'not_started'),
        ('lost_acknowledgment', 'effect_completed'): ('indeterminate', 'unknown'),
        ('yield', 'yield_contract'): ('satisfied', 'not_requested'),
    }
    if (domain, predicate) not in cases:
        raise ValueError('No admitted predicate substitution in this finite fixture')
    verdict, effect = cases[domain, predicate]
    return {'domain_outcome': domain, 'predicate': predicate, 'verdict': verdict,
            'performance': 'performed', 'effect': effect}


def legal_coordinates(verdict, performance, evidence):
    """Check pairs AND the stipulated evidence guard, not just enum membership.

    deciding is an admissible conclusion on this exact predicate. Independent
    means the support does not pretend the selected evaluation was undertaken.
    completion is the declared satisfaction completion/evidence condition.
    """
    if verdict not in VERDICTS or performance not in PERFORMANCES:
        return False
    expected = {'performed': True, 'not_performed': False, 'unconfirmed': None}[performance]
    if evidence['undertaken'] is not expected:
        return False
    deciding = evidence.get('deciding')
    if verdict == 'indeterminate':
        return deciding is None
    if deciding != verdict:
        return False
    if verdict == 'satisfied':
        return performance == 'performed' and evidence.get('completion') is True
    return performance == 'performed' or evidence.get('independent') is True


def evaluation(observed):
    """Finite observation-to-result view retaining extent, conclusion and support."""
    undertaken = observed['undertaken']
    performance = 'unconfirmed' if undertaken is None else 'performed' if undertaken else 'not_performed'
    support = observed.get('deciding')
    admissible = support is not None and (performance == 'performed' or observed.get('independent') is True)
    verdict = support if admissible else 'indeterminate'
    if verdict == 'satisfied' and (performance != 'performed' or not observed.get('completion')):
        verdict = 'indeterminate'
    return {'performance': performance, 'verdict': verdict,
            'extent': observed['extent'], 'conclusion': observed['conclusion'],
            'support': dict(observed), 'effect': observed['effect']}


def observe_effect(unit_observations, effect_free_scope=False):
    if not unit_observations:
        return 'not_requested' if effect_free_scope else 'unknown'
    if any(v is None for v in unit_observations):
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


def normalize_effects(material_parts, observations, effect_free_scope=False):
    """Bounded fixture interpreter for externally established supersession.

    The fixture supplies exact same-part identities, order and evidence for
    supersedes. A timestamp alone never supersedes. Unaccounted material possible-effect
    parts, invalid reversal support or conflicting terminal observations remain
    unknown. This is not a general temporal/conflict-resolution theorem.
    """
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


def operator_view(table, a, b, join, wellformedness_established=True):
    return {'verdict': apply_operator(table, a, b, join, wellformedness_established),
            'leaves': {'A': a, 'B': b}, 'join': join}


def negate_result(verdict):
    return {'satisfied': 'falsified', 'falsified': 'satisfied'}.get(verdict, verdict)


def recover(effect, idempotent, grant):
    if effect == 'completed':
        return 'retain_completed_progress'
    if not grant:
        return 'withhold_effect'
    if effect == 'not_started':
        return 'permitted_initial_dispatch'
    if effect == 'unknown' and idempotent:
        return 'permitted_idempotent_retry'
    return 'observe_or_return_unresolved'
