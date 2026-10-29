"""Tests; all inline and temporary inputs are authored test data."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from gate_report import report, encode

BASE = Path(__file__).parent


def sample(**fields):
    return dict(schema='a_c.formal-gate.result/1', status='refused', **fields)


def run_report(data):
    return report(json.dumps(data).encode())


class ReportTests(unittest.TestCase):
    def test_retained_examples(self):
        cases = {
            'verified': ('verified', 'verified_claims_reported'),
            'model-only': ('verified', 'verified_claims_reported'),
            'budget-refusal': ('refused', 'record_budget_refusal'),
            'view-mismatch': ('refused', 'supplied_view_mismatch'),
            'malformed-model': ('refused', 'malformed_model'),
            'historical-incomplete': ('incomplete', 'check_incomplete'),
            'authored-unsupported': ('unsupported', 'unsupported_contract'),
        }
        for name, (status, category) in cases.items():
            with self.subTest(name=name):
                raw = (BASE / 'inputs/examples' / (name + '.json')).read_bytes()
                result = report(raw)
                rendered = json.loads(encode(result))
                self.assertEqual(rendered['reported'], json.loads(raw))
                self.assertEqual(result['summary']['status'], status)
                self.assertEqual(result['summary']['category'], category)
                self.assertEqual(result['source'], {'bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest()})
                self.assertEqual(set(result), {'schema', 'source', 'reported', 'summary', 'cost', 'standing'})
                self.assertTrue(all(v is False for v in result['standing'].values()))

    def test_minimal_and_exact_reasons(self):
        for reason in (None, 'new refusal', 'signature: expected object ', 'SIGNATURE: EXPECTED OBJECT'):
            data = sample(reason=reason)
            result = run_report(data)
            self.assertEqual(result['summary']['category'], 'other_refusal')
            self.assertEqual(result['reported'], data)
            self.assertIsNone(result['summary']['checked_claim_count'])
        self.assertEqual(run_report(sample())['reported'], sample())

    def test_cost(self):
        for obs, expected in [
            (None, 'unknown'), ({}, 'unknown'), ({'elapsed_seconds': None}, 'unknown'),
            ({'elapsed_seconds': 0}, 'reported'), ({'elapsed_seconds': 2.5}, 'reported'),
            *[({'elapsed_seconds': v}, 'invalid') for v in (-1, True, False, '3', [], {})],
            ({'stages': [{'seconds': 5}]}, 'unknown'),
        ]:
            with self.subTest(obs=obs):
                data = sample(observations=obs, tokens=100, money_usd=20)
                result = run_report(data)
                self.assertEqual(result['reported'], data)
                self.assertEqual(result['cost']['elapsed_seconds']['state'], expected)
                for key in ('tokens', 'money_usd'):
                    self.assertEqual(result['cost'][key], {'state': 'unknown', 'value': None})
        self.assertEqual(run_report(sample(observations={'elapsed_seconds': 0}))['cost']['elapsed_seconds']['value'], 0)
        self.assertEqual(run_report(sample())['cost']['elapsed_seconds']['state'], 'unknown')

    def test_preservation_and_unchecked(self):
        data = sample(checked_claims=['z', 'a'], requested_claims=['z', 'a', 'unchecked'],
                      model={'id': 'urn:Exact/α', 'sha256': '000ABC'},
                      limits=['retained'], extension={'null': None, 'array': [3, 1]})
        result = run_report(data)
        self.assertEqual(result['reported'], data)
        self.assertEqual(result['summary']['checked_claim_count'], 2)
        self.assertEqual(result['summary']['requested_claim_count'], 3)
        self.assertNotIn('reason', result['reported'])
        self.assertEqual(run_report(sample(checked_claims=[]))['summary']['checked_claim_count'], 0)

    def test_invalid_grammar(self):
        bad = [b'\xff', b'{', b'[]', b'null', b'{"x":1,"x":2}',
               b'{"x":{"y":1,"y":2}}', b'{"x":NaN}', b'{"x":Infinity}']
        for data in ({}, {'schema': 'bad', 'status': 'refused'},
                     {'schema': 'a_c.formal-gate.result/1', 'status': []}):
            bad.append(json.dumps(data).encode())
        for key, value in [('reason', 1), ('request_sha256', []),
                           ('selections', {}), ('checked_claims', None),
                           ('requested_claims', [1]), ('limits', 'bad')]:
            bad.append(json.dumps(sample(**{key: value})).encode())
        for key in ('inputs', 'model', 'runtime_identity', 'evidence', 'observations', 'context_binding'):
            bad.append(json.dumps(sample(**{key: []})).encode())
        for raw in bad:
            with self.subTest(raw=raw), self.assertRaises((ValueError, UnicodeError)):
                report(raw)

    def test_decimal_preservation(self):
        raw = b'{"schema":"a_c.formal-gate.result/1","status":"verified","x":1e9999,"observations":{"elapsed_seconds":0.123456789012345678901}}'
        output = encode(report(raw))
        self.assertIn('1E+9999', output)
        self.assertIn('0.123456789012345678901', output)

    def test_cli(self):
        def cli(*args):
            return subprocess.run([sys.executable, '-B', str(BASE / 'gate_report.py'), *args],
                                  capture_output=True)
        for path in sorted((BASE / 'inputs/examples').glob('*.json')):
            result = cli(str(path))
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stderr, b'')
            self.assertTrue(result.stdout.endswith(b'\n'))
            self.assertEqual(json.loads(result.stdout)['reported'], json.loads(path.read_bytes()))
        with tempfile.TemporaryDirectory(dir=BASE / 'scratch') as directory:
            path = Path(directory) / 'test-data.json'
            for raw in (b'{', b'\xff', b'{"x":1,"x":2}'):
                path.write_bytes(raw)
                result = cli(str(path))
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, b'')
                self.assertTrue(result.stderr)
            result = cli(str(Path(directory) / 'absent'))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, b'')
            self.assertTrue(result.stderr)
        result = cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, b'')
        self.assertTrue(result.stderr)


if __name__ == '__main__':
    unittest.main()
