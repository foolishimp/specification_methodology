"""Encoding of three assurance relations of FOUNDATIONS §4 on a finite model.

The implementation under test of this instance. It encodes, on finite
domains: (a) Assertions and observation: a checker that decides a predicate
from an observation partition returns a decided value only where the
observation class is uniform in truth, and `indeterminate` where two
admissible cases with the same observation have opposite truth values; a
pass of a necessary condition establishes only that condition; (b)
Quantified assurance: a joint miss probability comes from the declared
joint model, not from the product of marginals, and one minus it is the
chance of at least one detection, not the probability that the product is
correct; (c) Change impact and evidence reuse: the selection S_Δ is every
test whose validity dependencies meet the impact cover, every mandatory
gate and every test whose dependencies are unknown; the rest is retained.
The template refuses to run when a bound section's bytes differ from the
digests in SOURCE. This file encodes; it decides nothing.
"""
from fractions import Fraction

SOURCE = {
    'path': 'standards/FOUNDATIONS.md',
    'sections': {
        'assertions-and-observation': '4bccbc2b4c0f5915cf20e6090051b7abbae039292e114a3459511e08620ecd3e',
        'quantified-assurance': '9666dc3e83bbd769efe823a3c7657c55db8f444bc5944bc2260bd1194263229b',
        'change-impact-and-evidence-reuse': 'e989bf4b8c0dd996e5545f18db94f8ba275d14485697c0b046429746ed3bfbc6',
    },
}


def observe(case):
    """Assertions and observation, Observation sufficiency: π(s) = π(s') implies q(s) = q(s') is
    required for a sound complete decision; where two admissible cases share an observation and
    differ in truth, the judgment is `indeterminate`."""
    truth, partition = case['truth'], case['partition']
    out = []
    for s in range(len(truth)):
        block = next(b for b in partition if s in b)
        values = {truth[i] for i in block}
        out.append('S' if values == {1} else 'F' if values == {0} else 'I')
    return ''.join(out)


def assert_kind(case):
    """Assertions and observation: a pass of a check of a necessary condition does not establish the
    full obligation; a sufficient conjunction establishes it when every conjunct passes."""
    return 'established' if (case['kind'] == 'sufficient' and case['passes']) else 'condition-only'


def joint_miss(case):
    """Quantified assurance: the joint miss probability is the declared joint model's; replacing it by
    the product of marginals requires conditional independence; one minus it is at least one
    detection, not whole-product correctness."""
    p1, p2, dependence = Fraction(case['p1']), Fraction(case['p2']), case['dependence']
    both = p1 * p2 if dependence == 'independent' else min(p1, p2)
    return f'{both}|detection={1 - both}|claim=at-least-one-detection'


def select(case):
    """Change impact and evidence reuse: S_Δ = { t : D*(t) intersects I(Δ) }; a mandatory gate remains
    applicable; unknown impact widens reassessment; retention needs known, unaffected dependencies."""
    chosen = []
    for deps, mandatory in case['tests']:
        affected = deps == 'unknown' or bool(set(deps) & set(case['delta']))
        chosen.append('S' if (mandatory or affected) else 'R')
    return ''.join(chosen)


def rule(case):
    """One lawful value per case (the encoding is deterministic) and a record of the inputs read."""
    kind = case['scenario']
    if kind == 'observation':
        value = observe(case)
        mixed = [sorted(b) for b in case['partition'] if len({case['truth'][i] for i in b}) > 1]
        return {value}, {'scenario': kind, 'blocks': len(case['partition']), 'mixed_blocks': mixed}
    if kind == 'assertion':
        return {assert_kind(case)}, {'scenario': kind, 'kind': case['kind'], 'passes': case['passes']}
    if kind == 'quantified':
        return {joint_miss(case)}, {'scenario': kind, 'dependence': case['dependence']}
    if kind == 'impact':
        return {select(case)}, {'scenario': kind, 'delta': sorted(case['delta']),
                                'unknown': [i for i, (d, _) in enumerate(case['tests']) if d == 'unknown']}
    raise ValueError(kind)


RULE = rule
