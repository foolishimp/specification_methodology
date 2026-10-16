"""Finite construction check of the Codex conjunction, not a method executor.

The donor contributes enumeration and mutant testing. Its different reported-
value rule is not imported. Tests are authored qualification, not independent
source fidelity evidence. Inputs are already normalized disjoint effect parts;
observing real effects and authenticating real producers are outside this model.
"""
import copy
import itertools
from context import HERE, PACKAGE, INPUTS, encoded, library, sha, write

CORE = ('satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis')
EFFECTS = ('not_requested', 'not_started', 'completed', 'partial', 'reverted', 'unknown')


def effect_join(parts):
    states = set(parts)
    if 'unknown' in states:
        return 'unknown'
    if states <= {'not_requested'}:
        return 'not_requested'
    if states <= {'completed', 'not_requested'}:
        return 'completed'
    if states <= {'not_started', 'not_requested'}:
        return 'not_started'
    if states <= {'reverted', 'not_started', 'not_requested'}:
        return 'reverted'
    return 'partial'


def conjoin(leaves, parts, *, basis=True, join='true', coverage=True, effect_required=False):
    admitted = [v for v in leaves if v is not None and v['authenticated']]
    failures = [v['id'] for v in admitted if v['verdict'] == 'falsified']
    absent = [i for i, v in enumerate(leaves) if v is None]
    inadmissible = [i for i, v in enumerate(leaves) if v is not None and not v['authenticated']]
    effect = effect_join(parts)
    values = {v['verdict'] for v in admitted}
    if not basis:
        verdict = 'invalid_basis'
    elif failures or join == 'false':
        verdict = 'falsified'
    elif 'invalid_basis' in values:
        verdict = 'invalid_basis'
    elif 'out_of_frame' in values:
        verdict = 'out_of_frame'
    elif (absent or inadmissible or not coverage or join == 'unknown'
          or 'indeterminate' in values or (effect_required and effect == 'unknown')):
        verdict = 'indeterminate'
    else:
        verdict = 'satisfied'
    return {'verdict': verdict, 'performance': 'performed', 'effect': effect,
            'components': copy.deepcopy(leaves), 'absent': absent,
            'inadmissible': inadmissible, 'uncovered': not coverage,
            'known_failures': failures,
            'failure_citations': [c for v in admitted if v['verdict'] == 'falsified' for c in v['citations']],
            'join': join}


def leaf(name, verdict, performance='performed', authenticated=True):
    return {'id': name, 'verdict': verdict, 'performance': performance,
            'authenticated': authenticated, 'citations': [name + '-evidence']}


def named_cases(rule):
    """Explicit expected decisions from the owning prose and common cases."""
    S, F, U, O, I = [leaf('A', v) for v in CORE]
    cases = [
        ('all satisfied', [S, S], {}, 'satisfied'),
        ('failure plus absent assessment', [F, None], {}, 'falsified'),
        ('failure plus uncovered coverage', [F, S], {'coverage': False}, 'falsified'),
        ('failure plus invalid child', [F, I], {}, 'falsified'),
        ('uninterpretable composite retains failure', [F, S], {'basis': False}, 'invalid_basis'),
        ('invalid basis before scope', [I, O], {}, 'invalid_basis'),
        ('scope before undecidable', [O, U], {}, 'out_of_frame'),
        ('missing child', [S, None], {}, 'indeterminate'),
        ('false required join', [S, S], {'join': 'false'}, 'falsified'),
        ('unknown required join', [S, S], {'join': 'unknown'}, 'indeterminate'),
        ('uncovered coverage', [S, S], {'coverage': False}, 'indeterminate'),
        ('unauthenticated success', [S, leaf('B', 'satisfied', authenticated=False)], {}, 'indeterminate'),
        ('independent counterevidence without performance', [leaf('A', 'falsified', 'not_performed'), None], {}, 'falsified'),
    ]
    bad = []
    for name, leaves, kwargs, expected in cases:
        r = rule(leaves, ['not_requested'], **kwargs)
        if r['verdict'] != expected:
            bad.append(name + ': wrong verdict')
        if r['components'] != leaves:
            bad.append(name + ': changed component predicate/performance')
        expected_failures = [x['id'] for x in leaves if x is not None and x['authenticated'] and x['verdict'] == 'falsified']
        if r['known_failures'] != expected_failures:
            bad.append(name + ': lost failure')
        if expected_failures and not r['failure_citations']:
            bad.append(name + ': lost citations')
    for required, expected in [(True, 'indeterminate'), (False, 'satisfied')]:
        r = rule([S, S], ['completed', 'unknown'], effect_required=required)
        if r['verdict'] != expected or r['effect'] != 'unknown':
            bad.append('uncertain effect and declared dependency')
    return bad


def mutants():
    def altered(kind):
        def run(leaves, parts, **kwargs):
            r = conjoin(leaves, parts, **kwargs)
            if kind == 'missing_erases_failure' and any(x is None for x in leaves):
                r['verdict'] = 'indeterminate'
            elif kind == 'missing_becomes_child':
                r['components'] = [x if x is not None else leaf('invented', 'indeterminate') for x in leaves]
            elif kind == 'drop_citations':
                r['failure_citations'] = []
            elif kind == 'scope_before_basis' and any(x and x['verdict'] == 'out_of_frame' for x in leaves):
                r['verdict'] = 'out_of_frame'
            elif kind == 'unknown_effect_is_absent' and r['effect'] == 'unknown':
                r['effect'] = 'not_requested'
            elif kind == 'false_join_is_undecidable' and kwargs.get('join') == 'false':
                r['verdict'] = 'indeterminate'
            elif kind == 'unauthenticated_satisfies' and r['inadmissible']:
                r['verdict'] = 'satisfied'
            elif kind == 'invent_performance':
                for v in r['components']:
                    if v is not None:
                        v['performance'] = 'performed'
            return r
        return run
    names = ('missing_erases_failure', 'missing_becomes_child', 'drop_citations',
             'scope_before_basis', 'unknown_effect_is_absent', 'false_join_is_undecidable',
             'unauthenticated_satisfies', 'invent_performance')
    return {n: altered(n) for n in names}


def main():
    if not __debug__:
        raise RuntimeError('Assertions disabled')
    assert not named_cases(conjoin), named_cases(conjoin)
    detected = {name: named_cases(rule) for name, rule in mutants().items()}
    assert all(detected.values()), 'A mutant survived the specified cases'
    states = [None] + [leaf('A', v) for v in CORE] + [leaf('A', 'satisfied', authenticated=False)]
    enumerated = 0
    for left, right, basis, join, coverage, e1, e2, required in itertools.product(
            states, states, (False, True), ('false', 'unknown', 'true'),
            (False, True), EFFECTS, EFFECTS, (False, True)):
        leaves = [left, None if right is None else dict(right, id='B', citations=['B-evidence'])]
        r = conjoin(leaves, [e1, e2], basis=basis, join=join, coverage=coverage, effect_required=required)
        assert r['components'] == leaves
        assert r['performance'] == 'performed'
        assert r['uncovered'] == (not coverage)
        assert r['absent'] == [i for i,v in enumerate(leaves) if v is None]
        if 'unknown' in (e1, e2):
            assert r['effect'] == 'unknown'
        if r['verdict'] == 'satisfied':
            assert basis and join == 'true' and coverage
            assert all(v is not None and v['authenticated'] and v['verdict'] == 'satisfied' for v in leaves)
            assert not required or r['effect'] != 'unknown'
        if any(v and v['authenticated'] and v['verdict'] == 'falsified' for v in leaves):
            assert r['known_failures'] and r['failure_citations']
            assert r['verdict'] == ('falsified' if basis else 'invalid_basis')
        enumerated += 1
    assert enumerated == 7 * 7 * 2 * 3 * 2 * 6 * 6 * 2
    effect_triples = 0
    for a,b,c in itertools.product(EFFECTS, repeat=3):
        assert effect_join([effect_join([a,b]),c]) == effect_join([a,effect_join([b,c])])
        effect_triples += 1
    parse = library('synthesis/check_artifacts.py')
    owner = PACKAGE / 'standards/FOUNDATIONS.md'
    pins = {a: sha(parse.section(owner.read_text(), a)[1].encode()) for a in ('result-algebra', 'result-conjunction')}
    report = {'kind': 'stdo.i4.finite-conjunction-check', 'common_input': INPUTS['common_input'],
              'source': {'path': 'standards/FOUNDATIONS.md', 'sha256': sha(owner.read_bytes()), 'sections': pins},
              'script_sha256': sha(__import__('pathlib').Path(__file__).read_bytes()),
              'enumerated_cases': enumerated, 'effect_associativity_triples': effect_triples,
              'mutant_counterexamples': detected, 'valid': True,
              'standing': 'Author finite encoding and property checks; independent source fidelity review pending.',
              'limits': ['Already normalized disjoint effect parts; no real effect observation or authorization.',
                         'Exactly two declared mandatory component slots with a fixed interpretable conjunction rule.',
                         'No evidence of whole-method completeness, actual use or member acceptance.']}
    write(HERE / 'FINITE_CONJUNCTION.json', report)
    print({'cases': enumerated, 'effect_triples': effect_triples, 'mutants_detected': len(detected)})


if __name__ == '__main__':
    main()
