"""Tests of the tenant pre-check. Run: python3 -I a_c/i3/tools/test_assemble.py"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble as A  # noqa: E402

S = A.STANDING
R = A.V + 'role:'
SRC = A.SOURCE + 'FOUNDATIONS.md#results'


def clause(uri, standing, extra, operator='operator:requires', statement='A statement.'):
    return {'uri': uri, 'clause_type': 'constraint', 'operator': A.V + operator,
            'arguments': [{'role': R + 'standing', 'ref': S + standing}] + extra,
            'statement': statement, 'source_refs': [SRC]}


PREMISE = clause('urn:t:c:premise', 'premise', [{'role': R + 'force', 'literal': 'must'}])


def run(*clauses, residuals=()):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / 'f.json'
        p.write_text(json.dumps({'clauses': [PREMISE, *clauses], 'residuals': list(residuals)}))
        return A.assemble([p], None)


class PreCheck(unittest.TestCase):
    def test_lawful_fragment_passes(self):
        ok = clause('urn:t:c:cons', 'consequence', [{'role': R + 'support', 'ref': 'urn:t:c:premise'}])
        policy = clause('urn:t:c:pol', 'policy-choice', [
            {'role': R + 'owner', 'literal': 'TICKETS §3'}, {'role': R + 'choice', 'literal': 'six names'},
            {'role': R + 'among', 'literal': 'any naming of the close outcomes'}], statement='The six classifications are named so.')
        mapping = clause('urn:t:c:map', 'policy-choice', [
            {'role': R + 'owner', 'literal': 'TICKETS §3'}, {'role': R + 'choice', 'literal': 'remove to falsified'},
            {'role': R + 'among', 'literal': 'the five core values'},
            {'role': R + 'refined-value', 'literal': 'remove'}, {'role': R + 'predicate', 'literal': 'the item is accepted'},
            {'role': R + 'core-value', 'ref': A.CORE + 'falsified'}], operator='operator:maps-to')
        mapping['clause_type'] = 'relation'
        run(ok, policy, mapping)

    def test_hollow_policy_rejected(self):
        hollow = clause('urn:t:c:hollow', 'policy-choice', [
            {'role': R + 'owner', 'literal': 'X'}, {'role': R + 'choice', 'literal': 'A statement.'},
            {'role': R + 'among', 'literal': 'anything'}])
        with self.assertRaisesRegex(A.Refusal, 'hollow policy choice'):
            run(hollow)

    def test_refinement_to_two_core_values_rejected(self):
        two = clause('urn:t:c:two', 'policy-choice', [
            {'role': R + 'owner', 'literal': 'X'}, {'role': R + 'choice', 'literal': 'c'}, {'role': R + 'among', 'literal': 'a, b'},
            {'role': R + 'refined-value', 'literal': 'v'}, {'role': R + 'predicate', 'literal': 'p'},
            {'role': R + 'core-value', 'ref': A.CORE + 'falsified'}, {'role': R + 'core-value', 'ref': A.CORE + 'indeterminate'}],
            operator='operator:maps-to')
        with self.assertRaisesRegex(A.Refusal, 'exactly one core value'):
            run(two)

    def test_support_kind_literal_checked(self):
        good = clause('urn:t:c:sk', 'premise', [{'role': R + 'support-kind', 'literal': 'stated-formula'}])
        run(good)
        bad = clause('urn:t:c:sk2', 'premise', [{'role': R + 'support-kind', 'literal': 'proved'}])
        with self.assertRaisesRegex(A.Refusal, 'support-kind'):
            run(bad)
        two = clause('urn:t:c:sk3', 'premise', [{'role': R + 'support-kind', 'literal': 'stated-formula'},
                                                 {'role': R + 'support-kind', 'literal': 'execution-evidence'}])
        with self.assertRaisesRegex(A.Refusal, 'support-kind'):
            run(two)

    def test_residual_dependent_clause_without_blocked_by_rejected(self):
        open_clause = clause('urn:t:c:open', 'unresolved', [])
        with self.assertRaisesRegex(A.Refusal, 'without blocked-by'):
            run(open_clause)


if __name__ == '__main__':
    unittest.main()
