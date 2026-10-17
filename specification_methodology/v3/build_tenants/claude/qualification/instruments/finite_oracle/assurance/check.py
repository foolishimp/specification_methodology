"""Finite oracle instance: three assurance relations of FOUNDATIONS §4 on finite domains (I5-04, port
D2 adapted from the Codex finite assurance witness at 28d87ee: the technique of a frozen finite
witness for the assurance formulas; none of its code or cases is copied).

Run from anywhere: python3 -I <this file> [--check]

The oracle below is written from the common assurance requirement
(specification/requirements/ASSURANCE.md: Assertions And Observation, Assurance Within A Risk Model,
Change Impact And Targeted Reassessment) and from the cited subsections of FOUNDATIONS §4, without
reading model.py: no function here calls the encoded rule, and the expected numbers are derived by
counting the domain by hand. FOUNDATIONS is also model.py's source, so for the properties taken from
it the oracle is independent of the encoding, not of its source.
"""
import importlib.util
import itertools
from fractions import Fraction
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
if not __debug__:
    raise SystemExit('Finite proof refuses disabled assertions; run without -O/PYTHONOPTIMIZE.')

INSTANCE = 'assurance_relations'
PREDICATE = ('On the declared finite domains, the encoded observation-sufficiency decision, the necessary-condition '
             'standing, the joint-miss computation and the change-impact selection meet properties P1 to P12')

# Re-declared at I5-07: Change impact and evidence reuse gained the sentence "A corrected run is not an unchanged
# independent test of the correction" (criterion 4); no modelled rule changed.
ORACLE_SOURCES = [
    {
        'path': '../../specification/requirements/ASSURANCE.md',
        'sections': {
            'assertions-and-observation': '324c3078414feb7bd8ede882e9c8db605f3501fd602728ccd72f50873b750750',
            'assurance-within-a-risk-model': '9a074a30fa71f96d86b914a682c81d726d04c6702920abed1a74935da266810a',
            'change-impact-and-targeted-reassessment': 'bc035cd3311d9309449d2ad87240d974a3e98c8ba7e400baf38f44018fd314a4',
        },
    },
    {
        'path': 'standards/FOUNDATIONS.md',
        'sections': {
            'assertions-and-observation': '4bccbc2b4c0f5915cf20e6090051b7abbae039292e114a3459511e08620ecd3e',
            'quantified-assurance': '9666dc3e83bbd769efe823a3c7657c55db8f444bc5944bc2260bd1194263229b',
            'change-impact-and-evidence-reuse': 'e989bf4b8c0dd996e5545f18db94f8ba275d14485697c0b046429746ed3bfbc6',
        },
    },
]


def partitions(items):
    """Every set partition of `items`, as tuples of tuples (15 for four items)."""
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for smaller in partitions(rest):
        for i, block in enumerate(smaller):
            yield smaller[:i] + ((first,) + block,) + smaller[i + 1:]
        yield ((first,),) + smaller


OBS = [{'scenario': 'observation', 'truth': t, 'partition': p}
       for t in itertools.product((0, 1), repeat=4) for p in partitions((0, 1, 2, 3))]
ASSERT = [{'scenario': 'assertion', 'kind': k, 'passes': b} for k in ('necessary', 'sufficient') for b in (0, 1)]
QUANT = [{'scenario': 'quantified', 'p1': p1, 'p2': p2, 'dependence': d}  # probabilities as exact strings, so the record is JSON
         for p1 in ('1/4', '1/2') for p2 in ('1/4', '1/2') for d in ('independent', 'dependent')]
DEPS = (('f1',), ('f2',), ('f1', 'f2'), 'unknown')
IMPACT = [{'scenario': 'impact', 'tests': tests, 'delta': delta}
          for delta in (('f1',), ('f2',), ('f1', 'f2'))
          for tests in itertools.product([(d, m) for d in DEPS for m in (0, 1)], repeat=2)]
DIMENSIONS = [('case', OBS + ASSERT + QUANT + IMPACT)]
DOMAIN_DESCRIPTION = {
    'observation': 'four admissible cases with every truth assignment (16) and every observation partition (15): 240',
    'assertion': 'a check that is a necessary condition or a sufficient conjunction, passing or not: 4',
    'quantified': 'two checks with miss probabilities in {1/4, 1/2}, under a declared independent or dependent joint model: 8',
    'impact': 'two tests, each with validity dependencies {f1}, {f2}, {f1,f2} or unknown and a mandatory flag, under a '
              'nonempty change {f1}, {f2} or {f1,f2}: 8 x 8 x 3 = 192',
    'cases': '240 + 4 + 8 + 192 = 444; one deterministic output each',
}

PROPERTIES = {
    'P1_satisfied_only_on_uniform_true': 'a case is judged satisfied only when every case sharing its observation is true '
                                         '(ASSURANCE Assertions And Observation: same observation, opposite truth values '
                                         'admit no sound complete decision; FOUNDATIONS Observation sufficiency)',
    'P2_falsified_only_on_uniform_false': 'a case is judged falsified only when every case sharing its observation is false '
                                          '(the same sentences: a reported failure is treated the same way)',
    'P3_mixed_observation_indeterminate': 'a case whose observation class holds opposite truth values is judged '
                                          'indeterminate (ASSURANCE: further evidence, a narrower scope or an '
                                          'indeterminate judgment is required)',
    'P4_uniform_observation_decided': 'a case whose observation class is uniform is decided, not indeterminate '
                                      '(non-vacuity guard: this check\'s reading that the sufficiency condition met '
                                      'permits the decision)',
    'P5_necessary_not_full': 'a passing check of a necessary condition does not establish the full obligation '
                             '(ASSURANCE: passing a check of a necessary condition does not establish the full obligation)',
    'P6_sufficient_establishes': 'a passing sufficient conjunction establishes the obligation (ASSURANCE: the stated '
                                 'conjunction is sufficient; non-vacuity guard)',
    'P7_joint_from_declared_model': 'the joint miss probability is the declared model\'s, and equals the product of '
                                    'marginals only under declared independence (ASSURANCE Assurance Within A Risk '
                                    'Model; FOUNDATIONS Quantified assurance: replacing the terms by the product '
                                    'requires conditional independence)',
    'P8_detection_not_correctness': 'one minus the joint miss is reported as at least one detection, never as the '
                                    'probability that the whole product is correct (FOUNDATIONS Quantified assurance)',
    'P9_affected_selected': 'every test whose known dependencies meet the change is selected (FOUNDATIONS Change '
                            'impact: S_Δ = { t : D*(t) intersects I(Δ) })',
    'P10_mandatory_selected': 'every mandatory gate is selected whatever the change (ASSURANCE: mandatory gates remain '
                              'applicable; FOUNDATIONS: a mandatory gate remains applicable)',
    'P11_unknown_selected': 'a test whose dependencies are unknown is selected (ASSURANCE: missing influence information '
                            'cannot justify exclusion; FOUNDATIONS: unknown impact widens reassessment)',
    'P12_retained_only_if_unaffected': 'a retained test is not mandatory, has known dependencies and none of them is in '
                                       'the change (FOUNDATIONS: retention establishes the validity conditions; '
                                       'excluding a check requires supported coverage of its dependencies)',
}


def outputs(model, rule, case):
    lawful, record = rule(case['case'])
    return [('one', lawful, record)]


def properties(case, value, record):
    c = case['case']
    kind = c['scenario']
    ok = {name: True for name in PROPERTIES}
    if kind == 'observation':
        for s in range(4):
            block = next(b for b in c['partition'] if s in b)
            values = {c['truth'][i] for i in block}
            v = value[s]
            if v == 'S' and values != {1}:
                ok['P1_satisfied_only_on_uniform_true'] = False
            if v == 'F' and values != {0}:
                ok['P2_falsified_only_on_uniform_false'] = False
            if len(values) > 1 and v != 'I':
                ok['P3_mixed_observation_indeterminate'] = False
            if len(values) == 1 and v == 'I':
                ok['P4_uniform_observation_decided'] = False
    elif kind == 'assertion':
        if c['kind'] == 'necessary' and value == 'established':
            ok['P5_necessary_not_full'] = False
        if c['kind'] == 'sufficient' and c['passes'] and value != 'established':
            ok['P6_sufficient_establishes'] = False
    elif kind == 'quantified':
        both_text, _, claim = value.partition('|detection=')
        both = Fraction(both_text)
        p1, p2 = Fraction(c['p1']), Fraction(c['p2'])
        expected = p1 * p2 if c['dependence'] == 'independent' else min(p1, p2)
        if both != expected:
            ok['P7_joint_from_declared_model'] = False
        if not claim.endswith('claim=at-least-one-detection'):
            ok['P8_detection_not_correctness'] = False
    elif kind == 'impact':
        for i, (deps, mandatory) in enumerate(c['tests']):
            v = value[i]
            known = deps != 'unknown'
            affected = known and bool(set(deps) & set(c['delta']))
            if affected and v != 'S':
                ok['P9_affected_selected'] = False
            if mandatory and v != 'S':
                ok['P10_mandatory_selected'] = False
            if not known and v != 'S':
                ok['P11_unknown_selected'] = False
            if v == 'R' and (mandatory or not known or affected):
                ok['P12_retained_only_if_unaffected'] = False
    return ok


def classes(case, lawful, record):
    c = case['case']
    kind = c['scenario']
    yield f'scenario={kind}'
    if kind == 'observation':
        mixed = sum(1 for b in c['partition'] if len({c['truth'][i] for i in b}) > 1)
        yield 'observation:all_decided' if mixed == 0 else 'observation:some_indeterminate'
    elif kind == 'impact':
        value = next(iter(lawful))
        yield 'impact:all_selected' if 'R' not in value else 'impact:some_retained'
    elif kind == 'quantified':
        yield f'quantified:{c["dependence"]}'
    elif kind == 'assertion':
        yield 'assertion:established' if (c['kind'] == 'sufficient' and c['passes']) else 'assertion:condition-only'


# Cardinalities derived by hand.
# Observation: partitions of four items by block count: 1 (one block), 7 (two), 6 (three), 1 (four).
#   all_decided = truth constant on every block = sum of 2^blocks = 2 + 28 + 48 + 16 = 94; some_indeterminate = 240 - 94 = 146.
# Impact, per test: 8 (dependency, mandatory) combos; retained iff not mandatory, dependencies known and disjoint from
#   the change: change {f1}: deps {f2} -> 1 combo; {f2}: 1; {f1,f2}: 0. all_selected = 7^2 + 7^2 + 8^2 = 162; some_retained = 30.
EXPECTED = {
    'cases': 444,
    'outputs': 444,
    'value_checks': 444,
    'classes': {
        'scenario=observation': 240, 'scenario=assertion': 4, 'scenario=quantified': 8, 'scenario=impact': 192,
        'observation:all_decided': 94, 'observation:some_indeterminate': 146,
        'assertion:established': 1, 'assertion:condition-only': 3,
        'quantified:independent': 4, 'quantified:dependent': 4,
        'impact:all_selected': 162, 'impact:some_retained': 30,
    },
}

# Mutant counts, derived by hand on the same domains.
# majority_in_class: differs only on mixed blocks with a strict majority: partition {3,1}: the three-block mixed (6
#   assignments) x singleton (2) x 4 partitions = 48; partition {4}: 3:1 or 1:3 = 8; ties stay indeterminate. 56 cases;
#   majority true (S on mixed) 24 + 4 = 28 (P1), majority false 28 (P2); every one fails P3.
# optimistic_on_mixed: S on every mixed block (146 cases): P1 and P3. pessimistic_on_mixed: F on every mixed block: P2 and P3.
# necessary_as_established: the one case (necessary, passing): P5.
# link_only_selection: a test affected through f2 alone is retained: per test, change {f2}: deps {f2} or {f1,f2}, not
#   mandatory: 2 of 8; change {f1,f2}: deps {f2}, not mandatory: 1 of 8; change {f1}: none. Cases with at least one such
#   test: 64 - 36 = 28, 64 - 49 = 15, 0: 43 (P9 and P12).
# drop_mandatory_when_unaffected: a mandatory test with known dependencies disjoint from the change is retained: per
#   test 1 of 8 for changes {f1} and {f2}, 0 for {f1,f2}: 15 + 15 = 30 (P10 and P12).
# unknown_as_unaffected: an unknown, non-mandatory test is retained: per test 1 of 8 under every change: 15 x 3 = 45
#   (P11 and P12).
# independent_product: differs where dependence is declared: 4 (P7). detection_as_correctness: every quantified case: 8 (P8).
EXPECTED_MUTANTS = {
    'majority_in_class': {'counterexample_cases': 56, 'by_property': {'P1_satisfied_only_on_uniform_true': 28, 'P2_falsified_only_on_uniform_false': 28, 'P3_mixed_observation_indeterminate': 56},
                          'output_differs_from_model': 56, 'value_set_differs_from_model': 56, 'record_differs_from_model': 0},
    'optimistic_on_mixed': {'counterexample_cases': 146, 'by_property': {'P1_satisfied_only_on_uniform_true': 146, 'P3_mixed_observation_indeterminate': 146},
                            'output_differs_from_model': 146, 'value_set_differs_from_model': 146, 'record_differs_from_model': 0},
    'pessimistic_on_mixed': {'counterexample_cases': 146, 'by_property': {'P2_falsified_only_on_uniform_false': 146, 'P3_mixed_observation_indeterminate': 146},
                             'output_differs_from_model': 146, 'value_set_differs_from_model': 146, 'record_differs_from_model': 0},
    'necessary_as_established': {'counterexample_cases': 1, 'by_property': {'P5_necessary_not_full': 1},
                                 'output_differs_from_model': 1, 'value_set_differs_from_model': 1, 'record_differs_from_model': 0},
    'link_only_selection': {'counterexample_cases': 43, 'by_property': {'P9_affected_selected': 43, 'P12_retained_only_if_unaffected': 43},
                            'output_differs_from_model': 43, 'value_set_differs_from_model': 43, 'record_differs_from_model': 0},
    'drop_mandatory_when_unaffected': {'counterexample_cases': 30, 'by_property': {'P10_mandatory_selected': 30, 'P12_retained_only_if_unaffected': 30},
                                       'output_differs_from_model': 30, 'value_set_differs_from_model': 30, 'record_differs_from_model': 0},
    'unknown_as_unaffected': {'counterexample_cases': 45, 'by_property': {'P11_unknown_selected': 45, 'P12_retained_only_if_unaffected': 45},
                              'output_differs_from_model': 45, 'value_set_differs_from_model': 45, 'record_differs_from_model': 0},
    'independent_product': {'counterexample_cases': 4, 'by_property': {'P7_joint_from_declared_model': 4},
                            'output_differs_from_model': 4, 'value_set_differs_from_model': 4, 'record_differs_from_model': 0},
    'detection_as_correctness': {'counterexample_cases': 8, 'by_property': {'P8_detection_not_correctness': 8},
                                 'output_differs_from_model': 8, 'value_set_differs_from_model': 8, 'record_differs_from_model': 0},
}

LIMITS = [
    'Fidelity is not established: the check does not show that FOUNDATIONS §4 states the rules model.py encodes; '
    'that is a reviewer\'s judgement against the bound section digests',
    'The properties are this check\'s reading of the common assurance requirement and of the cited FOUNDATIONS '
    'subsections; their fidelity to those sources is likewise a reviewer\'s judgement',
    'The encoding and the oracle share an author, the I5-04 Writer, who wrote model.py first; the oracle is independent '
    'of the encoding only in being written without reading or calling it',
    'Observation: four admissible cases and deterministic truth; the checker is modelled as a function of the '
    'observation class, so a probabilistic or human checker admitting several conclusions (Assertions and '
    'observation) is not modelled; the narrower-scope response is not modelled, only the indeterminate one',
    'Assertion: one necessary condition or one sufficient conjunction, passing or not; conjunctions with several '
    'conjuncts and their coverage and compatibility argument are not modelled',
    'Quantified: the dependent joint model is fixed at the maximal positive dependence P(both) = min(p1, p2); no '
    'calibration, prior or population is modelled, and no Bayes update is exercised',
    'Impact: two tests, two facts and nonempty changes; the mandatory gate, the unknown dependency and the '
    'requirement-to-test link are the only selection relations; serialisation and cost are not modelled',
    'A failed or refused run writes no result; an older result file stays bound to its own digests',
    'A finite check on the declared domains only: no claim beyond them, and no categorical or universal claim',
]


def _load_template():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('finite_oracle_template', root.parent / 'template.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == '__main__':
    sys.exit(_load_template().run(sys.modules[__name__], sys.argv))
