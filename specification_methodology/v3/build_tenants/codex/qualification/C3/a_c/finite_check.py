"""Exhaust the SOURCE.md token interpretation; not an a_c semantic engine.

The other selected qualitative clauses receive independent source comparison.
This hand-authored executable/model relation also requires that assessment.
"""
import hashlib
import itertools
import json
from pathlib import Path

root = Path(__file__).resolve().parent

def operation(owners, token, destination, grant, observed, infer_permission=False):
    if not observed:
        return 'unresolved', owners
    admitted = isinstance(grant, dict) and (
        grant['issuer'] == owners[token] and grant['token'] == token and
        grant['destination'] == destination and grant['operation'] == 'assign')
    if not admitted and not infer_permission:
        return 'refused', owners
    output = list(owners)
    output[token] = destination
    return 'completed', tuple(output)

grants = [None, 'label:A', 'label:B'] + [
    {'issuer': issuer, 'token': token, 'destination': destination, 'operation': kind}
    for issuer, token, destination, kind in itertools.product(['A', 'B'], range(2), ['A', 'B'], ['assign', 'inspect'])]
counts = {'completed': 0, 'refused': 0, 'unresolved': 0}
violations = []
cases = 0
for owners in itertools.product(['A', 'B'], repeat=2):
    for token, destination, grant, observed in itertools.product(range(2), ['A', 'B'], grants, [False, True]):
        result, output = operation(owners, token, destination, grant, observed)
        assert len(output) == 2 and all(value in {'A', 'B'} for value in output)
        assert output[1-token] == owners[1-token]
        if result == 'completed':
            # Inverse postcondition: every effect has its exact source-owned
            # grant, independently of the implementation's Boolean guard.
            assert grant == {'issuer': owners[token], 'token': token,
                             'destination': destination, 'operation': 'assign'}
            assert observed and output[token] == destination
        else:
            assert output == owners
        if not observed:
            assert result == 'unresolved'
        counts[result] += 1
        bad_result, bad_output = operation(owners, token, destination, grant, observed, True)
        if bad_result != result or bad_output != output:
            violations.append({'owners': list(owners), 'token': token, 'destination': destination,
                               'grant': grant, 'observed': observed,
                               'correct_result': result, 'mutant_result': bad_result,
                               'state_changed_by_mutant': bad_output != output})
        cases += 1
# Independently derived domain cardinalities: 16 exact grants complete; each
# known operation has 18 nonmatching grant values; half the domain is unknown.
assert cases == 608
assert counts == {'completed': 16, 'refused': 288, 'unresolved': 304}
assert len(violations) == 288
harm = next(v for v in violations if v['state_changed_by_mutant'])

first_grant = {'issuer': 'A', 'token': 0, 'destination': 'B', 'operation': 'assign'}
first_result, changed = operation(('A', 'A'), 0, 'B', first_grant, True)
assert first_result == 'completed' and changed == ('B', 'A')
unknown_result, unknown_state = operation(changed, 0, 'B', first_grant, False)
assert unknown_result == 'unresolved' and unknown_state == changed
stale_result, stale_state = operation(changed, 0, 'B', first_grant, True)
assert stale_result == 'refused' and stale_state == changed
current_grant = {'issuer': 'B', 'token': 0, 'destination': 'A', 'operation': 'assign'}
resumed_result, resumed_state = operation(changed, 0, 'A', current_grant, True)
assert resumed_result == 'completed' and resumed_state == ('A', 'A')

report = {'kind': 'finite_token_interpretation_check',
          'source_sha256': hashlib.sha256((root/'SOURCE.md').read_bytes()).hexdigest(),
          'executable_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'cases': cases, 'grant_variants': len(grants), 'outcomes': counts,
          'invariants_valid': True, 'unauthorized_mutant_counterexamples': len(violations),
          'state_changing_counterexample': harm,
          'resumption': {'original_effect': first_result, 'unknown_observation': unknown_result,
                         'old_issuer_after_state_change': stale_result, 'current_owner_grant': resumed_result},
          'limits': ['Hand-authored token interpretation requires separate fidelity review',
                     'Qualitative join/finding/authority clauses are not executed by this script',
                     'ac.py validates structure and source resolution, not these predicates',
                     'No distributed transport, whole-corpus or universal category proof']}
(root/'FINITE_RESULT.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report))
