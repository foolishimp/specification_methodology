"""Finite oracle instance: a fragment of the conjunction of results of FOUNDATIONS §4.

Run from anywhere: python3 -I <this file> [--check]

The oracle below is written from the single result algebra requirement
(specification/requirements/README.md, items 2, 3 and 6) and from the
cited lines of FOUNDATIONS §4 Conjunction of results, without reading
model.py: no function here calls the encoded rule, and the expected numbers
are derived by counting the domain by hand. model.py is the implementation
under test. FOUNDATIONS is also model.py's source, so for the properties
taken from it the oracle is independent of the encoding, not of its source.
"""
import importlib.util
import itertools
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
if not __debug__:
    raise SystemExit('Finite proof refuses disabled assertions; run without -O/PYTHONOPTIMIZE.')

INSTANCE = 'conjunction_of_results'
PREDICATE = ('On the declared domain, the encoded conjunction rule meets properties P0 to P8 for every '
             'value it may report, on the flat conjunction and on every two-way join of its components')

# Line numbers cited below are those of standards/FOUNDATIONS.md at 8b42994;
# the run refuses if either bound FOUNDATIONS section has changed.
# Re-declared in I3-3i after review: requirement item 2 now says "No evaluation
# or decision outcome exists outside the core" and adds explicit conditions;
# P0 still follows from it, and P4 rests on item 3, unchanged. The new
# lifecycle paragraph concerns recorded states, outside this domain. In
# FOUNDATIONS the Results rule body is unchanged (its family table changed),
# and Conjunction of results adds Stale results, which concerns bases that
# disagree, outside this domain of agreeing bases.
ORACLE_SOURCES = [
    {
        'path': '../../specification/requirements/README.md',
        'sections': {
            'single-result-algebra-requirement': 'f485ce8d400b9114a5e82f948a0d5057dee64fb3f4deb004f7d79d7fbfdfe82c',
        },
    },
    {
        'path': 'standards/FOUNDATIONS.md',
        'sections': {
            'results': '2e020cbfbfa3c93ecb27a098e62cc26225a0d9bd7598e4c405c4110dd9d11e26',
            'conjunction-of-results': 'e426656616cd9c3909ea2bd54afa8c7eaf7b78159ea9300cf599c4cb94a37766',
        },
    },
]

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
    'fixed': 'every contributor is a mandatory component whose own evaluation returned its value or no closed '
             'result; declared basis relations agree; no results that are not mandatory; no counterexample other '
             'than the components\' own falsified values; no coverage admitted',
}

PROPERTIES = {
    'P0_core_value': 'the conjunction reports one value of the core and nothing outside it '
                     '(requirement items 2 and 6)',
    'P1_satisfied_only_if': 'satisfied only when every mandatory component is satisfied and there is no gap '
                            '(FOUNDATIONS §4 Conjunction of results, Reported value, 912-916, with bases agreeing '
                            'in this domain; requirement item 3, first two bullets, applied to the composite)',
    'P2_failure_survives': 'every falsified component is a known failure in the record, keeps its value, and '
                           'survives every join; no other component is a known failure (Survival, 894-900)',
    'P3a_gap_never_satisfied': 'a gap, not performed or uncovered, is never satisfied (Gaps, 887-888)',
    'P3b_gap_kind_recorded': 'the record names exactly the gap kinds present, the not-performed components by '
                             'index and the uncovered obligation (Gaps, 888-892; requirement item 3, third '
                             'bullet: non-performance stays distinct from undecidability)',
    'P4_no_mapping_raises_standing': 'each component keeps its own value: a closed result is not remapped and a '
                                     'component without a closed result carries no core value '
                                     '(requirement item 3)',
    'P5_success_reachable': 'with every component satisfied and no gap, the conjunction reports satisfied '
                            '(non-vacuity guard; this check\'s reading of Reported value, 930-935, where '
                            'FOUNDATIONS leaves the value to the declared rule; not a requirement property)',
    'P6_value_from_returned': 'where a returned mandatory component is not satisfied, the reported value is one of '
                              'the non-satisfied values returned, never a value no component returned '
                              '(Reported value, 916-921: "chosen by its declared rule from those returned")',
    'P7_gap_reports_own_indeterminate': 'where every returned mandatory component is satisfied and a gap remains, '
                                        'the reported value is indeterminate, the conjunction\'s own '
                                        '(Reported value, 925-929, with bases agreeing in this domain)',
    'P8_sole_failure_reported_falsified': 'where falsified is the only non-satisfied value returned, the reported '
                                          'value is falsified (Reported value, 914-919: a known failure is reported '
                                          'as another value only if that value was also returned)',
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
    # The non-satisfied values returned: the values the declared rule may choose among (916-921).
    returned_non_satisfied = {v for v in components if v not in (NOT_PERFORMED, 'satisfied')}
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
        'P6_value_from_returned': not returned_non_satisfied or value in returned_non_satisfied,
        'P7_gap_reports_own_indeterminate': bool(returned_non_satisfied) or not gap or value == 'indeterminate',
        'P8_sole_failure_reported_falsified': returned_non_satisfied != {'falsified'} or value == 'falsified',
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
    if {v for v in closed if v != 'satisfied'} == {'falsified'}:
        yield 'falsified_only_non_satisfied_returned'


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
# falsified_only_non_satisfied_returned: components in {satisfied, falsified,
#   not performed} with at least one falsified: 3^n - 2^n = 1, 5, 19, sum 25, x 2 = 50.
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
        'falsified_only_non_satisfied_returned': 50,
    },
}

# Expected counts for each mutant, derived the same way. Notation: s, f, i, o,
# b are the five core values, N is no closed result; NS is the set of
# non-satisfied values the components returned; counts are per obligation
# flag and n = 1, 2, 3, summed, then doubled where both flags count alike.
# Every mutant's rule is a function of the components and obligations, so
# each join gives the flat output: a case fails a property on a join exactly
# when it fails it flat, and outputs differ exactly when the flat ones do.
#
# Record variants: both map N to a core value, so they lose the not-performed
# gap and give the missing component a value on every case with an N:
# 103 x 2 = 206 cases (P3b, P4), and their records differ on those 206.
# no_result_as_satisfied: NS is unchanged, so P6 and P8 hold. With no
#   obligation and every returned component s it reports satisfied where the
#   model reports indeterminate: components in {s, N} with an N, 2^n - 1 =
#   1, 3, 7, sum 11 (P1, P3a, P7); those 11 are its reported-value differences.
# no_result_as_indeterminate: never reports success, so P1, P3a and P7 hold.
#   With an N it adds i to NS. P6 fails where i was not returned and NS is not
#   empty: an N, no i, at least one of f, o, b: 5^n - 4^n - 2^n + 1 = 0, 6, 54,
#   sum 60, x 2 = 120; these are its 120 reported-value differences. P8 fails
#   where NS = {f} and an N exists: 3^n - 2 x 2^n + 1 = 0, 2, 12, sum 14, x 2 = 28.
#
# Reported-value variants: the record is the model's, so P0 to P5 hold and
# no record differs; only P6 to P8 can detect them.
# swap_falsified_out_of_frame: changes the value set exactly when NS holds one
#   of f and o but not both; then the set holds a value not returned (P6):
#   2 x (5^n - 4^n) = 2, 18, 122, sum 142, x 2 = 284. P8 fails where NS = {f}:
#   3^n - 2^n = 1, 5, 19, sum 25, x 2 = 50.
# falsified_reported_indeterminate: changes the set wherever f is returned,
#   6^n - 5^n per flag, 103 x 2 = 206. It is lawful where i was also returned,
#   since FOUNDATIONS sets no order among non-satisfied values; P6 fails where
#   f is returned and i is not: 5^n - 4^n = 1, 9, 61, sum 71, x 2 = 142. P8
#   fails where NS = {f}: 50.
# gap_reported_indeterminate: changes the set where a gap exists, NS is not
#   empty and NS is not {i}. With the obligation: 6^n - 3^n = 3, 27, 189, sum
#   219; without it, an N is also needed: 6^n - 5^n - 3^n + 2^n = 0, 6, 72,
#   sum 78; 297. P6 fails where i is not in NS: with the obligation, no i and
#   at least one of f, o, b: 5^n - 2^n = 3, 21, 117, sum 141; without, also an
#   N: 5^n - 4^n - 2^n + 1 = 0, 6, 54, sum 60; 201. P8 fails where NS = {f}:
#   with the obligation 25; without, also an N: 3^n - 2 x 2^n + 1 = 0, 2, 12,
#   sum 14; 39.
# non_satisfied_reported_out_of_frame: changes the set wherever the model does
#   not report satisfied (513 cases) and NS is not {o}; NS = {o} where the
#   components are in {s, o, N} with at least one o: 3^n - 2^n, sum 25, x 2 =
#   50; 513 - 50 = 463. P6 fails where NS is not empty and o is not in it: 5^n - 2^n = 3, 21,
#   117, sum 141, x 2 = 282. P7 fails on the 25 cases that report the
#   conjunction's own indeterminate. P8 fails where NS = {f}: 50, all within
#   the 282. Counterexample cases 282 + 25 = 307.
EXPECTED_MUTANTS = {
    'no_result_as_satisfied': {
        'counterexample_cases': 206,
        'by_property': {'P1_satisfied_only_if': 11, 'P3a_gap_never_satisfied': 11,
                        'P3b_gap_kind_recorded': 206, 'P4_no_mapping_raises_standing': 206,
                        'P7_gap_reports_own_indeterminate': 11},
        'output_differs_from_model': 206,
        'value_set_differs_from_model': 11,
        'record_differs_from_model': 206,
    },
    'no_result_as_indeterminate': {
        'counterexample_cases': 206,
        'by_property': {'P3b_gap_kind_recorded': 206, 'P4_no_mapping_raises_standing': 206,
                        'P6_value_from_returned': 120, 'P8_sole_failure_reported_falsified': 28},
        'output_differs_from_model': 206,
        'value_set_differs_from_model': 120,
        'record_differs_from_model': 206,
    },
    'swap_falsified_out_of_frame': {
        'counterexample_cases': 284,
        'by_property': {'P6_value_from_returned': 284, 'P8_sole_failure_reported_falsified': 50},
        'output_differs_from_model': 284,
        'value_set_differs_from_model': 284,
        'record_differs_from_model': 0,
    },
    'falsified_reported_indeterminate': {
        'counterexample_cases': 142,
        'by_property': {'P6_value_from_returned': 142, 'P8_sole_failure_reported_falsified': 50},
        'output_differs_from_model': 206,
        'value_set_differs_from_model': 206,
        'record_differs_from_model': 0,
    },
    'gap_reported_indeterminate': {
        'counterexample_cases': 201,
        'by_property': {'P6_value_from_returned': 201, 'P8_sole_failure_reported_falsified': 39},
        'output_differs_from_model': 297,
        'value_set_differs_from_model': 297,
        'record_differs_from_model': 0,
    },
    'non_satisfied_reported_out_of_frame': {
        'counterexample_cases': 307,
        'by_property': {'P6_value_from_returned': 282, 'P7_gap_reports_own_indeterminate': 25,
                        'P8_sole_failure_reported_falsified': 50},
        'output_differs_from_model': 463,
        'value_set_differs_from_model': 463,
        'record_differs_from_model': 0,
    },
}

LIMITS = [
    'Fidelity is not established: the check does not show that FOUNDATIONS §4 states the rule model.py '
    'encodes; that is a reviewer\'s judgement against the bound section digests',
    'The oracle properties are this check\'s reading of the single result algebra requirement and of the cited '
    'lines of FOUNDATIONS §4 Conjunction of results; their fidelity to those sources is likewise a reviewer\'s '
    'judgement',
    'The encoding and the oracle share an author, the C2 Writer, who wrote model.py first. P0 and P4 rest on the '
    'requirement alone; the other properties cite FOUNDATIONS §4, which is also model.py\'s source, so for them '
    'the oracle is independent of the encoding only in being written without reading or calling it',
    'P5 checks this encoding\'s reading that, with every mandatory result satisfied, agreeing bases and no '
    'gap, the declared rule gives satisfied (Reported value, 930-935); FOUNDATIONS leaves that value to the '
    'declared rule',
    'The choice among non-satisfied values is modelled as the set of values a declared rule may report; '
    'every value in the set is checked, so every declared order is covered, but no particular declared rule is. '
    'A variant whose reported set is a non-empty subset of that set is itself a lawful declared rule, so it is '
    'no counterexample: falsified_reported_indeterminate differs from the model on 206 cases and is falsified on '
    '142',
    'No property forces falsified where falsified is returned together with another non-satisfied value: '
    'FOUNDATIONS sets no order among them (Reported value, 919-921; Results, Standing, 706-707), so such a '
    'property would add an order that FOUNDATIONS leaves to the declared rule',
    'Domain: one to three mandatory components, each contributed by its own evaluation; the empty conjunction '
    'is not in the domain',
    'Basis relations are fixed at agreeing: the invalid_basis rule for disagreeing bases (Reported value, '
    '921-924) is not exercised',
    'Excluded, outside the interface of model.py as well as the domain: a falsified result that is not '
    'mandatory stays in the record (Reported value, 929-930); and a material counterexample to a mandatory '
    'constraint, found by any contributor, falsifies the conjunction where every mandatory result is satisfied, '
    'bases agree and no gap remains (930-933). A component\'s own falsified value never meets that condition, '
    'so in this domain FOUNDATIONS forces falsified for a known failure only through 916-919 (P8). Encoding '
    'either clause needs the declared rule\'s choices of how results that are not mandatory count and whether '
    'any may veto or defer (The declared rule, 937-942), and an explicitly selected further claim',
    'The declared rule\'s other choices (handling of conflict and indeterminacy, the decision authority; '
    '937-942), Survival\'s conflicted mandatory result (902-904) and Composition of results (946-951) are not '
    'modelled',
    'Coverage is one obligation, uncovered or absent; no part of a join covers another part\'s obligation, so '
    'the recomputation of uncovered coverage is exercised only where it changes nothing',
    'Joins are two-way splits of one flat conjunction into contiguous parts, combined as a union of component '
    'records; nested conjunctions whose parts carry their own composite predicates are not modelled',
    'Predicates and domain outcomes are represented only by component position (Predicates travel, 906-910); '
    'refinements and their mappings, effects whose completion is unknown, and the separation of availability, '
    'assessment and acceptance (requirement items 2 to 5 beyond this domain) are not exercised',
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
