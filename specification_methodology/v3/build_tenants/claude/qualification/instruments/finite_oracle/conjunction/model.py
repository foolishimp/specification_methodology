"""Encoding of FOUNDATIONS §4 Conjunction of results over the core of §4 Results.

The implementation under test of this instance. Each clause cites the
paragraph of standards/FOUNDATIONS.md it encodes and that paragraph's lines
at commit 8b42994. The template refuses to run when the bytes of either
section differ from the digests in SOURCE, so the paragraphs cited are
exactly those encoded; the line numbers move when an earlier section of the
member changes, and the result file records the current extents. This file
encodes; it decides nothing. Whether FOUNDATIONS states the rule encoded
here is a fidelity judgement for a reviewer, not something the check
establishes.

Interface. conjoin(components, required, covered) takes one entry per
mandatory component, a core value or NO_RESULT, and the required
obligations and admitted coverage as sets. It returns (lawful, record):
lawful is the set of values the conjunction may report, because
FOUNDATIONS leaves the choice among non-satisfied values to the declared
rule of the member that applies the conjunction (Reported value, 916-921);
record keeps the three inputs apart (Conjunction of results, 875-885).
"""

SOURCE = {
    'path': 'standards/FOUNDATIONS.md',
    'sections': {
        'results': '2e020cbfbfa3c93ecb27a098e62cc26225a0d9bd7598e4c405c4110dd9d11e26',
        'conjunction-of-results': 'e426656616cd9c3909ea2bd54afa8c7eaf7b78159ea9300cf599c4cb94a37766',
    },
}

# Results, value table (676-682): the five core values; 684: the only core.
CORE = ('satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis')

# Results, Not performed (721-728): a required or planned evaluation that was
# not performed has no closed result. Results, the rule that nothing raises
# standing, third item (714-717): it is never mapped to any core value.
NO_RESULT = 'no_closed_result'


def conjoin(components, required, covered):
    # Input 1 (877-878): the closed results returned.
    returned = {i: v for i, v in enumerate(components) if v != NO_RESULT}
    # Input 2 (879-882): planned assessments with no closed result.
    not_performed = [i for i, v in enumerate(components) if v == NO_RESULT]
    # Input 3 (883-885): uncovered coverage R minus C.
    uncovered = sorted(frozenset(required) - frozenset(covered))
    # Gaps (887-889): the record names the kind of gap, not performed,
    # uncovered or both, and each item.
    gap_kinds = (['not_performed'] if not_performed else []) + (['uncovered'] if uncovered else [])
    record = {
        # Results, third item of the no-raise rule (714-717), and Gaps
        # (890-892): a component without a closed result carries no core
        # value and is never an `indeterminate` component. Predicates travel
        # (906-907): each component keeps its own value.
        'components': [returned.get(i) for i in range(len(components))],
        # Survival (894-897): every known failure is carried with the composite.
        'known_failures': [i for i, v in sorted(returned.items()) if v == 'falsified'],
        'not_performed': not_performed,
        'required': sorted(required),
        'covered': sorted(covered),
        'uncovered': uncovered,
        'gap_kinds': gap_kinds,
    }
    non_satisfied = frozenset(v for v in returned.values() if v != 'satisfied')
    if non_satisfied:
        # Reported value (916-921): where a mandatory result is not satisfied, a
        # non-satisfied value chosen by the declared rule from those returned;
        # no universal order. Every value the rule may choose is lawful.
        lawful = non_satisfied
    elif gap_kinds:
        # Reported value (925-929): every mandatory returned result satisfied, basis
        # relations agree (fixed by the domain) and a gap remains: the
        # conjunction's own `indeterminate`, gaps recorded by kind.
        lawful = frozenset({'indeterminate'})
    else:
        # Reported value (912-915 and 930-935): every mandatory result satisfied, bases
        # agree, no gap and no counterexample beyond the components: the value
        # the declared rule gives over the mandatory results. This encoding
        # reads that value as `satisfied`.
        lawful = frozenset({'satisfied'})
    return lawful, record


def join(rule, left, right):
    """Combine two conjunctions (Survival, 894-900).

    The union of the two records' components, and with them of known
    failures and of planned assessments without a closed result; uncovered
    coverage recomputed over the combined obligations. A sub-conjunction's
    reported value is never entered as a component.
    """
    components = tuple(NO_RESULT if v is None else v for v in left['components'] + right['components'])
    required = frozenset(left['required']) | frozenset(right['required'])
    covered = frozenset(left['covered']) | frozenset(right['covered'])
    return rule(components, required, covered)


RULE = conjoin
