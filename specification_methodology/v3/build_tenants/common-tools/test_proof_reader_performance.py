"""Conservation controls for the bounded lexical reader cost repair.

The old function comes from the exact released historical fixture; it is only
run on small inputs. Select STDO_CURRENT_READER_ORACLE for the frozen current010
reader byte oracle. That test executes the optimized public check, never the
slow full predecessor or any Lean process.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest

import proof_reader as reader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LIBRARY = ('Closure', 'GateProof', 'GateRuntime', 'Model', 'Projection', 'Structure')
ORACLE_HASHES = {
    'PROOFS.json': '05b155370d642a078f9504ea960d5069445a7e607910c9361a96c5d9c168c17a',
    'index.html': '10bf2932f9a5f02e0a8f1ed44e86cd9fe3cae7dc78320c1bbb6a87577aa43109',
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class CatalogCostConservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = HERE / 'fixtures/proof_reader-v3.0.4.py'
        if digest(path.read_bytes()) != '37a74b721347635ddfdf1032cbed124c97c46aabbfd5f4fd919aca19f9cdf457':
            raise AssertionError('Exact predecessor source fixture changed')
        spec = importlib.util.spec_from_file_location('pre_cost_repair_reader', path)
        cls.previous = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.previous)

    def assert_equivalent(self, sources):
        def result(function):
            try:
                return {'value': function(sources)}
            except ValueError as error:
                return {'error': type(error).__name__, 'message': str(error)}
        self.assertEqual(result(reader.source_catalog), result(self.previous.source_catalog))

    def test_actual_six_library_sources_keep_every_declaration_reference_and_line(self):
        sources = {'library/AC/' + name + '.lean': (ROOT / 'a_c/build_tenants/lean/AC' / (name + '.lean')).read_text()
                   for name in LIBRARY}
        self.assert_equivalent(sources)

    def test_line_boundaries_scope_masking_and_refusals_match_previous_function(self):
        cases = {
            'scope_and_suffix': {'a.lean': 'namespace A\ndef x := 1\nnamespace N\ndef y := x + A.x\nend N\nend A\nnamespace B\ndef x := 2\ndef y := x + A.x\nend B\ndef unresolved := x\n'},
            'comment_string_anonymous': {'a.lean': 'def x := 1\n/- hidden\n /- nested -/ -/\ninstance : Inhabited Nat := ⟨x⟩\ndef text := "x\\\" x\nx"\nexample : x = 1 := rfl\n-- hidden x\ndef y := x\n'},
            'same_and_next_line': {'a.lean': 'def x := 1\ndef y := x + x +\n x\n\n'},
            'crlf': {'a.lean': 'def x := 1\r\ndef y := x +\r\n x\r\n'},
            'cr_and_unicode': {'a.lean': 'def x := 1\rdef y := x\u2028def z := y\n'},
            'empty_final_line': {'empty.lean': '', 'a.lean': 'def x := 1\ndef y := x'},
            'duplicate_refusal': {'a.lean': 'def x := 0\n', 'b.lean': 'def x := 1\n'},
            'comment_refusal': {'a.lean': 'def x := 1\n/- unterminated\n'},
            'string_refusal': {'a.lean': 'def x := "unterminated\n'},
        }
        for name, sources in cases.items():
            with self.subTest(boundary=name):
                self.assert_equivalent(sources)

    def test_full_current_catalog_and_html_match_exact_retained_oracle(self):
        selected = os.environ.get('STDO_CURRENT_READER_ORACLE')
        if not selected:
            self.skipTest('Select the exact retained current010 reader with STDO_CURRENT_READER_ORACLE')
        root = Path(selected).resolve()
        before = {name: (root / name).read_bytes() for name in ORACLE_HASHES}
        self.assertEqual({name: digest(raw) for name, raw in before.items()}, ORACLE_HASHES)
        argv = [sys.executable, '-B', str(HERE / 'proof_reader.py'), 'check', str(root)]
        started = time.perf_counter()
        process = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=60)
        elapsed = time.perf_counter() - started
        retained = os.environ.get('STDO_READER_TEST_EVIDENCE')
        if retained:
            output = Path(retained).absolute()
            output.mkdir(parents=True, exist_ok=False)
            (output / 'stdout.json').write_bytes(process.stdout)
            (output / 'stderr.log').write_bytes(process.stderr)
            (output / 'execution.json').write_text(json.dumps({'argv': argv, 'cwd': str(ROOT),
                'returncode': process.returncode, 'elapsed_seconds': elapsed,
                'producer_sha256': digest((HERE / 'proof_reader.py').read_bytes()),
                'oracle': {'path': str(root), 'members': ORACLE_HASHES},
                'stdout_sha256': digest(process.stdout), 'stderr_sha256': digest(process.stderr)}, indent=2, sort_keys=True) + '\n')
        self.assertEqual(process.returncode, 0, process.stdout.decode(errors='replace') + process.stderr.decode(errors='replace'))
        self.assertEqual(json.loads(process.stdout)['status'], 'checked')
        self.assertEqual({name: (root / name).read_bytes() for name in ORACLE_HASHES}, before)


if __name__ == '__main__':
    unittest.main()
