"""Deliberately wrong variants of the conjunction rule in model.py.

Each variant maps a component that has no closed result to a core value
before conjoining, which FOUNDATIONS §4 Results forbids (the third item of
the rule that nothing raises standing, lines 714-717 at 8b42994). The check
must find their counterexamples; a variant it does not falsify fails the
run.

- no_result_as_satisfied: the missing result counts as `satisfied`, so a
  conjunction with an unperformed component can report success and records
  no not-performed gap.
- no_result_as_indeterminate: the missing result counts as an
  `indeterminate` component; the conjunction never reports success
  wrongly, but the not-performed gap kind is lost (Conjunction of results,
  Gaps, lines 890-892 at 8b42994).
"""


def variants(model):
    def substitute(value):
        def rule(components, required, covered):
            mapped = tuple(value if v == model.NO_RESULT else v for v in components)
            return model.conjoin(mapped, required, covered)
        return rule

    return {
        'no_result_as_satisfied': substitute('satisfied'),
        'no_result_as_indeterminate': substitute('indeterminate'),
    }
