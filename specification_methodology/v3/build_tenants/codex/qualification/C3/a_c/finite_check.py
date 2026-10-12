"""Exhaust a declared finite SOURCE.md interpretation, separately from ac.py.

This checks a hand-authored executable model of the selected source. It does
not execute a_c clauses, or prove that this encoding/model is faithful. That
relation receives independent source-first assessment.
"""
import hashlib
import itertools
import json
from pathlib import Path

root = Path(__file__).resolve().parent

def operation(owners, token, destination, permission, observed, infer_permission=False):
    if not observed:
        return 'unresolved', owners
    if not permission and not infer_permission:
        return 'refused', owners
    changed = list(owners)
    changed[token] = destination
    return 'completed', tuple(changed)

counts = {'completed': 0, 'refused': 0, 'unresolved': 0}
counterexamples = []
cases = 0
for owners in itertools.product(['A', 'B'], repeat=2):
    for token, destination, grant_mask, observed in itertools.product(range(2), ['A', 'B'], range(16), [False, True]):
        # Four exact token/destination operations. Permission must match the
        # current owner in this immutable case; no permission is carried across
        # a later state. All sixteen permission subsets are considered.
        bit = token * 2 + (destination == 'B')
        permission = bool(grant_mask & (1 << bit))
        result, actual = operation(owners, token, destination, permission, observed)
        expected = 'unresolved' if not observed else ('completed' if permission else 'refused')
        assert result == expected
        assert len(actual) == 2 and all(value in {'A', 'B'} for value in actual)
        assert actual[1-token] == owners[1-token]
        if result != 'completed':
            assert actual == owners
        else:
            assert actual[token] == destination
        counts[result] += 1
        mutant_result, mutant_actual = operation(owners, token, destination, permission, observed, True)
        if mutant_result != expected or mutant_actual != actual:
            counterexamples.append({'owners': list(owners), 'token': token,
                                    'destination': destination, 'grant_mask': grant_mask,
                                    'observed': observed, 'expected': expected,
                                    'mutant_result': mutant_result})
        cases += 1
assert cases == 512 and len(counterexamples) == 128

report = {'kind': 'finite_source_interpretation_check', 'source_sha256': hashlib.sha256((root/'SOURCE.md').read_bytes()).hexdigest(),
          'executable_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'cases': cases, 'outcomes': counts, 'invariants_valid': True,
          'unauthorized_mutant_counterexamples': len(counterexamples),
          'first_counterexample': counterexamples[0],
          'limits': ['Hand-authored interpretation requires separate fidelity review',
                     'ac.py validates structure and source resolution, not these predicates',
                     'No distributed transport, whole-corpus or universal category proof']}
(root/'FINITE_RESULT.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report))
