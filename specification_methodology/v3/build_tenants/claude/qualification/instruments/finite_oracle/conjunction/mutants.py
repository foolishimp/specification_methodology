"""Deliberately wrong variants of the conjunction rule in model.py.

The check must find the counterexamples of every variant; a variant it
does not falsify fails the run. Line numbers are those of
standards/FOUNDATIONS.md at 8b42994.

Record variants. Each maps a component that has no closed result to a core
value before conjoining, which FOUNDATIONS §4 Results forbids (the third
item of the rule that nothing raises standing, lines 714-717). Record and
reported value both change.

- no_result_as_satisfied: the missing result counts as `satisfied`, so a
  conjunction with an unperformed component can report success and records
  no not-performed gap.
- no_result_as_indeterminate: the missing result counts as an
  `indeterminate` component; the conjunction never reports success
  wrongly, but the not-performed gap kind is lost (Conjunction of results,
  Gaps, lines 890-892), and `indeterminate` enters the reported values
  although no component returned it.

Reported-value variants. Each calls the model unchanged and rewrites only
the set of values it may report; the record is returned intact, so only a
property of the reported value can detect it (Conjunction of results,
Reported value, lines 912-935).

- swap_falsified_out_of_frame: `falsified` and `out_of_frame` exchanged in
  the reported values (the Codex review's variant, F4).
- falsified_reported_indeterminate: `falsified` reported as
  `indeterminate` (RC12 M3).
- gap_reported_indeterminate: `indeterminate` whenever a gap exists, even
  with a non-satisfied component returned (RC12 M1).
- non_satisfied_reported_out_of_frame: `out_of_frame` whenever the model
  does not report `satisfied` (RC12 M2).
"""


def variants(model):
    def substitute(value):
        def rule(components, required, covered):
            mapped = tuple(value if v == model.NO_RESULT else v for v in components)
            return model.conjoin(mapped, required, covered)
        return rule

    def rewrite_value(change):
        def rule(components, required, covered):
            lawful, record = model.conjoin(components, required, covered)
            return frozenset(change(lawful, record)), record
        return rule

    swap = {'falsified': 'out_of_frame', 'out_of_frame': 'falsified'}
    return {
        'no_result_as_satisfied': substitute('satisfied'),
        'no_result_as_indeterminate': substitute('indeterminate'),
        'swap_falsified_out_of_frame': rewrite_value(
            lambda lawful, record: {swap.get(v, v) for v in lawful}),
        'falsified_reported_indeterminate': rewrite_value(
            lambda lawful, record: {'indeterminate' if v == 'falsified' else v for v in lawful}),
        'gap_reported_indeterminate': rewrite_value(
            lambda lawful, record: {'indeterminate'} if record['gap_kinds'] else lawful),
        'non_satisfied_reported_out_of_frame': rewrite_value(
            lambda lawful, record: lawful if lawful == {'satisfied'} else {'out_of_frame'}),
    }
