"""Deliberately wrong variants of the assurance encoding in model.py; each changes one decision."""
from fractions import Fraction


def variants(model):
    def with_observe(obs):
        def rule(case):
            if case['scenario'] != 'observation':
                return model.rule(case)
            lawful, record = model.rule(case)
            return {obs(case)}, record
        return rule

    def majority(case):
        out = []
        for s in range(len(case['truth'])):
            block = next(b for b in case['partition'] if s in b)
            ones = sum(case['truth'][i] for i in block)
            out.append('S' if ones * 2 > len(block) else 'F' if ones * 2 < len(block) else 'I')
        return ''.join(out)

    def optimistic(case):
        out = []
        for s in range(len(case['truth'])):
            block = next(b for b in case['partition'] if s in b)
            out.append('S' if any(case['truth'][i] for i in block) else 'F')
        return ''.join(out)

    def pessimistic(case):
        out = []
        for s in range(len(case['truth'])):
            block = next(b for b in case['partition'] if s in b)
            out.append('F' if not all(case['truth'][i] for i in block) else 'S')
        return ''.join(out)

    def necessary_as_established(case):
        if case['scenario'] != 'assertion':
            return model.rule(case)
        lawful, record = model.rule(case)
        return {'established' if case['passes'] else 'condition-only'}, record

    def with_select(sel):
        def rule(case):
            if case['scenario'] != 'impact':
                return model.rule(case)
            lawful, record = model.rule(case)
            return {sel(case)}, record
        return rule

    def link_only(case):  # impact seen only through the requirement-to-test link f1
        return ''.join('S' if (m or d == 'unknown' or ('f1' in (d if d != 'unknown' else ()) and 'f1' in case['delta'])) else 'R'
                       for d, m in case['tests'])

    def drop_mandatory(case):
        return ''.join('S' if (d == 'unknown' or bool(set(d) & set(case['delta']))) else 'R' for d, m in case['tests'])

    def unknown_as_unaffected(case):
        return ''.join('S' if (m or (d != 'unknown' and bool(set(d) & set(case['delta'])))) else 'R' for d, m in case['tests'])

    def independent_product(case):
        if case['scenario'] != 'quantified':
            return model.rule(case)
        lawful, record = model.rule(case)
        both = Fraction(case['p1']) * Fraction(case['p2'])
        return {f'{both}|detection={1 - both}|claim=at-least-one-detection'}, record

    def detection_as_correctness(case):
        if case['scenario'] != 'quantified':
            return model.rule(case)
        lawful, record = model.rule(case)
        value = next(iter(lawful)).replace('claim=at-least-one-detection', 'claim=product-correct')
        return {value}, record

    return {
        'majority_in_class': with_observe(majority),
        'optimistic_on_mixed': with_observe(optimistic),
        'pessimistic_on_mixed': with_observe(pessimistic),
        'necessary_as_established': necessary_as_established,
        'link_only_selection': with_select(link_only),
        'drop_mandatory_when_unaffected': with_select(drop_mandatory),
        'unknown_as_unaffected': with_select(unknown_as_unaffected),
        'independent_product': independent_product,
        'detection_as_correctness': detection_as_correctness,
    }
