"""Genuine retained examples plus explicitly authored test data."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from gate_report import make_report

ROOT = Path(__file__).resolve().parent


def authored(**fields):
    """Small authored test data, not gate execution evidence."""
    return json.dumps(dict(schema='a_c.formal-gate.result/1', status='refused', **fields)).encode()


class ReportTests(unittest.TestCase):
    def test_genuine_examples(self):
        expected = {'verified': ('verified', 'verified_claims_reported'),
                    'model-only': ('verified', 'verified_claims_reported'),
                    'budget-refusal': ('refused', 'record_budget_refusal'),
                    'view-mismatch': ('refused', 'supplied_view_mismatch'),
                    'malformed-model': ('refused', 'malformed_model'),
                    'historical-incomplete': ('incomplete', 'check_incomplete'),
                    'authored-unsupported': ('unsupported', 'unsupported_contract')}
        for name, (status, category) in expected.items():
            with self.subTest(name=name):
                raw = (ROOT / 'inputs/examples' / (name + '.json')).read_bytes()
                r = make_report(raw)
                self.assertEqual(r['reported'], json.loads(raw))
                self.assertEqual(set(r), {'schema', 'source', 'reported', 'summary', 'cost', 'standing'})
                self.assertEqual(r['source'], {'raw_sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
                self.assertEqual(r['summary']['status'], status)
                self.assertEqual(r['summary']['category'], category)
                self.assertFalse(any(r['standing'].values()))

    def test_exact_reason_and_minimal(self):
        for reason in (None, 'new reason', 'signature: expected object ',
                       'insufficient record budget; verified refusal, no truncated projection'):
            r = make_report(authored(reason=reason))
            self.assertEqual(r['summary']['category'], 'other_refusal')
            self.assertIsNone(r['summary']['checked_claim_count'])
        self.assertNotIn('reason', make_report(authored())['reported'])

    def test_costs(self):
        for obs in (None, {}, {'stages': [{'seconds': 10}]}, {'elapsed_seconds': None}):
            self.assertEqual(make_report(authored(observations=obs))['cost']['elapsed_seconds'],
                             {'state': 'unknown', 'value': None})
        for value in (0, 0.0, 1.25, 100):
            self.assertEqual(make_report(authored(observations={'elapsed_seconds': value}))['cost']['elapsed_seconds'],
                             {'state': 'reported', 'value': value})
        for value in (-1, True, False, '2', [], {}):
            r = make_report(authored(observations={'elapsed_seconds': value}, tokens=42, money_usd=10))
            self.assertEqual(r['reported']['observations']['elapsed_seconds'], value)
            self.assertEqual(r['cost']['elapsed_seconds'], {'state': 'invalid', 'value': None})
            for key in ('tokens', 'money_usd'):
                self.assertEqual(r['cost'][key], {'state': 'unknown', 'value': None})

    def test_preservation_and_unchecked(self):
        raw = authored(checked_claims=['urn:exact:β'], requested_claims=['urn:exact:β', 'unchecked'],
                       model={'id': ' exact identity ', 'sha256': None}, limits=['limit'],
                       extension={'array': [None, False, 0, 'é'], 'nested': {'x': 1}})
        r = make_report(raw)
        self.assertEqual(r['reported'], json.loads(raw))
        self.assertEqual(r['summary']['checked_claim_count'], 1)
        self.assertEqual(r['summary']['requested_claim_count'], 2)
        self.assertEqual(make_report(authored(checked_claims=[]))['summary']['checked_claim_count'], 0)

    def test_invalid_inputs(self):
        invalid = [b'\xff', b'{', b'[]', b'null', b'{}', b'{"schema":"wrong","status":"refused"}',
                   b'{"schema":"a_c.formal-gate.result/1","status":[]}',
                   authored().replace(b'"refused"', b'"new"'),
                   b'{"x":1,"x":2}', authored(extension={'x': 1}).replace(b'"x": 1', b'"x": 1, "x": 2')]
        for number in (b'NaN', b'Infinity', b'-Infinity', b'1e999'):
            invalid.append(authored(extension=0).replace(b'"extension": 0', b'"extension": ' + number))
        for key in ('reason', 'request_sha256', 'checked_claims', 'requested_claims', 'limits',
                    'inputs', 'model', 'runtime_identity', 'evidence', 'observations', 'context_binding', 'selections'):
            invalid.append(authored(**{key: 42}))
        invalid.extend([authored(checked_claims=[1]), authored(limits=None)])
        for raw in invalid:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                make_report(raw)

    def test_cli(self):
        command = [sys.executable, '-B', str(ROOT / 'gate_report.py')]
        for path in sorted((ROOT / 'inputs/examples').glob('*.json')):
            p = subprocess.run(command + [str(path)], capture_output=True)
            self.assertEqual(p.returncode, 0)
            self.assertEqual(p.stderr, b'')
            self.assertTrue(p.stdout.endswith(b'\n'))
            self.assertEqual(json.loads(p.stdout), make_report(path.read_bytes()))
        with tempfile.TemporaryDirectory(dir=ROOT / 'scratch') as tmp:
            path = Path(tmp) / 'bad.json'
            path.write_bytes(b'{')
            for args in ([], [str(path)], [str(Path(tmp) / 'absent')], [str(path), 'extra']):
                p = subprocess.run(command + args, capture_output=True)
                self.assertEqual(p.returncode, 2)
                self.assertEqual(p.stdout, b'')
                self.assertTrue(p.stderr)
                self.assertNotIn(b'Traceback', p.stderr)
            self.assertEqual(list(Path(tmp).iterdir()), [path])


if __name__ == '__main__':
    unittest.main()
