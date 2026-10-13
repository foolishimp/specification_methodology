"""Finite oracle instance: the conjunction of results of FOUNDATIONS §4.

Run from anywhere: python3 -I <this file> [--check]

The oracle below is written from the single result algebra requirement
(specification/requirements/README.md, items 2, 3 and 6) and from the
properties the C2 activation brief names, not from model.py: no function
here reads the encoded rule, and the expected numbers are derived by
counting the domain by hand. model.py is the implementation under test.
"""
import importlib.util
import itertools
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
if not __debug__:
    raise SystemExit('Finite proof refuses disabled assertions; run without -O/PYTHONOPTIMIZE.')

INSTANCE = 'conjunction_of_results'
PREDICATE = ('On the declared domain, the encoded conjunction rule meets properties P0 to P5 for every '
             'value it may report, on the flat conjunction and on every two-way join of its components')

ORACLE_SOURCE = {
    'path': '../../specification/requirements/README.md',
    'sections': {
        'single-result-algebra-requirement': 'e3fba2f2cf86b923cef6c8ef64f8362830a7e165fe618702cb4652cb0735e278',
    },
}

# The oracle's own vocabulary: the five core values of the core result
# algebra, and the mark of a planned component with no closed result.
CORE = frozenset({'satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis'})
NOT_PERFORMED = 'no_closed_result'
STATES = ('satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis', NOT_PERFORMED)
OBLIGATION = 'r'

DIMENSIONS = [
    ('components', [c for n in (1, 2, 3) for c in itertools.product(STATES, repeat=n)]),
    ('uncovered', (False, True)),
]
DOMAIN_DESCRIPTION = {
    'components': 'one to three mandatory components, each one of the five core values or no closed result '
                  '(planned, not performed): 6 + 36 + 216 = 258 assignments',
    'uncovered': 'one required obligation, uncovered or absent: 2',
    'cases': '258 x 2 = 516',
    'joins': 'for two or three components, every split into a left and a right part, with the obligation, '
             'when present, held by either part',
    'fixed': 'declared basis relations agree; no results that are not mandatory; no counterexample other than '
             'the components\' own falsified values; no coverage admitted',
}

PROPERTIES = {
    'P0_core_value': 'the conjunction reports one value of the core and nothing outside it '
                     '(requirement items 2 and 6)',
    'P1_satisfied_only_if': 'satisfied only when every mandatory component is satisfied and there is no gap '
                            '(brief; requirement item 3, first two bullets, applied to the composite)',
    'P2_failure_survives': 'every falsified component is a known failure in the record, keeps its value, and '
                           'survives every join; no other component is a known failure (brief)',
    'P3a_gap_never_satisfied': 'a gap, not performed or uncovered, is never satisfied (brief)',
    'P3b_gap_kind_recorded': 'the record names exactly the gap kinds present, the not-performed components by '
                             'index and the uncovered obligation (brief; requirement item 3, third bullet: '
                             'non-performance stays distinct from undecidability)',
    'P4_no_mapping_raises_standing': 'each component keeps its own value: a closed result is not remapped and a '
                                     'component without a closed result carries no core value '
                                     '(requirement item 3)',
    'P5_success_reachable': 'with every component satisfied and no gap, the conjunction reports satisfied '
                            '(non-vacuity guard; this check\'s reading of FOUNDATIONS §4 Conjunction of '
                            'results, Reported value, last sentence, '
                            'not a requirement property)',
}


def outputs(model, rule, case):
    """The flat conjunction, then every two-way join of it, each computed by `rule`."""
    components, uncovered = case['components'], case['uncovered']
    required = frozenset({OBLIGATION}) if uncovered else frozenset()
    results = [('flat',) + rule(components, required, frozenset())]
    for k in range(1, len(components)):
        for side in (('left', 'right') if uncovered else (None,)):
            left = rule(components[:k], required if side == 'left' else frozenset(), frozenset())
            right = rule(components[k:], required if side == 'right' else frozenset(), frozenset())
            results.append((f'join k={k} obligation={side}',) + model.join(rule, left[1], right[1]))
    return results


def properties(case, value, record):
    components, uncovered = case['components'], case['uncovered']
    not_performed = [i for i, v in enumerate(components) if v == NOT_PERFORMED]
    failures = [i for i, v in enumerate(components) if v == 'falsified']
    all_satisfied = all(v == 'satisfied' for v in components)
    gap = bool(not_performed) or uncovered
    kinds = (['not_performed'] if not_performed else []) + (['uncovered'] if uncovered else [])
    kept = [None if v == NOT_PERFORMED else v for v in components]
    return {
        'P0_core_value': value in CORE,
        'P1_satisfied_only_if': value != 'satisfied' or (all_satisfied and not uncovered),
        'P2_failure_survives': record['known_failures'] == failures
                               and all(record['components'][i] == 'falsified' for i in failures),
        'P3a_gap_never_satisfied': not gap or value != 'satisfied',
        'P3b_gap_kind_recorded': record['gap_kinds'] == kinds and record['not_performed'] == not_performed
                                 and record['uncovered'] == ([OBLIGATION] if uncovered else []),
        'P4_no_mapping_raises_standing': record['components'] == kept,
        'P5_success_reachable': not (all_satisfied and not uncovered) or value == 'satisfied',
    }


def classes(case, lawful, record):
    """Classes of the model's flat output, counted against the derivations in EXPECTED."""
    closed = [v for v in record['components'] if v is not None]
    if lawful == {'satisfied'}:
        yield 'reports_satisfied'
    elif lawful == {'indeterminate'} and all(v == 'satisfied' for v in closed):
        yield 'reports_own_indeterminate'
    else:
        yield 'reports_from_returned_non_satisfied'
    yield 'gap_kinds=' + ('+'.join(record['gap_kinds']) or 'none')
    if record['known_failures']:
        yield 'known_failure_present'


# Expected cardinalities, derived by counting the domain, not by running the
# model. Per component count n (1, 2, 3) and per obligation flag:
#   assignments 6^n: 6, 36, 216, sum 258; cases 258 x 2 = 516.
#   with no not-performed component 5^n: 5, 25, 125, sum 155.
#   with at least one 6^n - 5^n: 1, 11, 91, sum 103.
# Gap kinds: none = no not-performed, no obligation = 155; uncovered only =
#   no not-performed, obligation = 155; not_performed only = 103; both = 103.
# known_failure_present: at least one falsified, 6^n - 5^n per flag, 103 x 2 = 206.
# reports_satisfied: every component satisfied, no obligation: one per n = 3.
# reports_own_indeterminate: every component satisfied or not performed, and a
#   gap: 2^n with the obligation plus 2^n - 1 without = 3, 7, 15, sum 25.
# reports_from_returned_non_satisfied: the rest, 516 - 3 - 25 = 488.
# Joins: n = 2 has 1 split, n = 3 has 2; one placement without the obligation,
#   two with it: 36 x 1 x 3 + 216 x 2 x 3 = 108 + 1296 = 1404; outputs 516 + 1404 = 1920.
# Value checks, flat: a non-satisfied core value w is a lawful report exactly
#   when w occurs, so each of the 4 contributes 6^n - 5^n per flag; plus 25
#   own indeterminate and 3 satisfied. Per flag and n: n=1 6, n=2 48, n=3 372
#   (4 x 91 + 8, or 4 x 91 + 7 + 1). Flat 2 x (6 + 48 + 372) = 852.
#   A join's lawful set equals the flat one, so joins add 48 x 3 + 372 x 6 =
#   144 + 2232 = 2376; total 3228.
EXPECTED = {
    'cases': 516,
    'outputs': 1920,
    'value_checks': 3228,
    'classes': {
        'reports_satisfied': 3,
        'reports_own_indeterminate': 25,
        'reports_from_returned_non_satisfied': 488,
        'gap_kinds=none': 155,
        'gap_kinds=uncovered': 155,
        'gap_kinds=not_performed': 103,
        'gap_kinds=not_performed+uncovered': 103,
        'known_failure_present': 206,
    },
}

# Expected counterexamples of each mutant, derived the same way.
# Both lose the not-performed gap and give the missing component a core value
# on every case with a not-performed component: 103 x 2 = 206 cases (P3b, P4).
# no_result_as_satisfied also reports success where every other component is
#   satisfied and there is no obligation: 2^n - 1 = 1, 3, 7, sum 11 (P1, P3a);
#   those 11 are the cases where its reported values differ from the model's.
# no_result_as_indeterminate never reports success, so P1 and P3a hold; its
#   reported values differ where the model chooses only among falsified,
#   out_of_frame and invalid_basis and a not-performed component adds
#   indeterminate: at least one not-performed, at least one of those three, no
#   indeterminate: 5^n - 4^n - 2^n + 1 = 0, 6, 54, sum 60, x 2 = 120.
EXPECTED_MUTANTS = {
    'no_result_as_satisfied': {
        'counterexample_cases': 206,
        'by_property': {'P1_satisfied_only_if': 11, 'P3a_gap_never_satisfied': 11,
                        'P3b_gap_kind_recorded': 206, 'P4_no_mapping_raises_standing': 206},
        'output_differs_from_model': 206,
        'value_set_differs_from_model': 11,
    },
    'no_result_as_indeterminate': {
        'counterexample_cases': 206,
        'by_property': {'P3b_gap_kind_recorded': 206, 'P4_no_mapping_raises_standing': 206},
        'output_differs_from_model': 206,
        'value_set_differs_from_model': 120,
    },
}

LIMITS = [
    'Fidelity is not established: the check does not show that FOUNDATIONS §4 states the rule model.py '
    'encodes; that is a reviewer\'s judgement against the bound section digests',
    'The oracle properties are this check\'s reading of the single result algebra requirement and the C2 '
    'brief; their fidelity to the requirement is likewise a reviewer\'s judgement',
    'The encoding and the oracle share an author, the C2 Writer, who wrote model.py first: the oracle is '
    'independent of the encoding in its source (the requirement, not FOUNDATIONS), not in its author',
    'P5 checks this encoding\'s reading that, with every mandatory result satisfied, agreeing bases and no '
    'gap, the declared rule gives satisfied (FOUNDATIONS §4 Conjunction of results, Reported value, last '
    'sentence); FOUNDATIONS leaves that value to the '
    'declared rule',
    'The choice among non-satisfied values is modelled as the set of values a declared rule may report; '
    'every value in the set is checked, so every choice is covered, but no particular declared rule is',
    'Domain: one to three mandatory components; the empty conjunction is not in the domain',
    'Basis relations are fixed at agreeing: the invalid_basis rule for disagreeing bases (Reported value, '
    'fourth sentence) is not exercised',
    'No results that are not mandatory (Reported value, sixth sentence) and no counterexample found outside '
    'the components (Reported value, last sentence) are in the domain',
    'Coverage is one obligation, uncovered or absent; no part of a join covers another part\'s obligation, so '
    'the recomputation of uncovered coverage is exercised only where it changes nothing',
    'Joins are two-way splits of one flat conjunction into contiguous parts, combined as a union of component '
    'records; nested conjunctions whose parts carry their own composite predicates are not modelled',
    'Predicates and domain outcomes are represented only by component position; refinements and their '
    'mappings, effects whose completion is unknown, and the separation of availability, assessment and '
    'acceptance (requirement items 2 to 5 beyond this domain) are not exercised',
    'A failed or refused run writes no result; an older result file stays bound to its own digests',
    'A finite check on the declared domain only: no claim beyond it, and no categorical or universal claim',
]


def _load_template():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('finite_oracle_template', root.parent / 'template.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == '__main__':
    sys.exit(_load_template().run(sys.modules[__name__], sys.argv))
