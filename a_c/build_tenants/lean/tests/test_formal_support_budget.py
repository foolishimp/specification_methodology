"""Support orchestration controls; compiler effects and member scan are explicit stubs."""
from contextlib import ExitStack, redirect_stdout
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import formal_support as support


class SupportBudgetTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='ac-support-budget-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / '.cache').mkdir()
        self.output = self.root / 'profiles/support.json'
        self.prefix = self.root / 'selected-compiler'
        self.environment = {'PATH': str(self.prefix / 'bin')}
        self.lock = {'lean': {'fixture': 'compiler-pin'}, 'mathlib': {'fixture': 'mathlib-pin'}}
        self.calls = []
        self.audit = '\n'.join("'" + name + "' does not depend on any axioms"
                               for name in sorted(support.GENERIC_CONTRACTS)) + '\n'

    def establish(self, fail_at=None, failure=subprocess.TimeoutExpired, audit=None):
        def effect(argv, *, cwd, env, stdout, check, timeout):
            self.assertEqual(cwd, self.root)
            self.assertEqual(env, self.environment)
            self.assertTrue(check)
            self.assertIs(type(timeout), int)
            self.assertGreater(timeout, 0)
            self.calls.append((argv, timeout))
            if len(self.calls) - 1 == fail_at:
                if failure is subprocess.TimeoutExpired:
                    raise failure(argv, timeout)
                raise failure(1, argv)
            if stdout is not None:
                stdout.write((self.audit if audit is None else audit).encode())
            return subprocess.CompletedProcess(argv, 0)

        with ExitStack() as stack:
            stack.enter_context(patch.object(support, 'ROOT', self.root))
            selected = (self.prefix, self.environment, self.lock)
            stack.enter_context(patch.object(support, 'tools', return_value=selected))
            stack.enter_context(patch.object(support, 'proof_environment', return_value=selected))
            scan = stack.enter_context(patch.object(support, 'members', return_value={'fixture': '0' * 64}))
            stack.enter_context(patch.object(support.runtime_process, 'run', side_effect=effect))
            stack.enter_context(redirect_stdout(io.StringIO()))
            try:
                return support.establish(self.output)
            except Exception:
                scan.assert_not_called()
                raise

    def test_finite_allocations_keep_exact_fresh_replay_and_audit_sequence(self):
        result = self.establish()
        self.assertEqual(self.calls, [
            ([str(self.prefix / 'bin/lake'), 'build', 'AC.GateRuntime', 'AC.GateProof'], 180),
            ([str(self.prefix / 'bin/leanchecker'), '--fresh', 'AC.GateProof'], 900),
            ([str(self.prefix / 'bin/lean'), '-j', '1', '-M', '4096', str(self.root / 'AC/GateProof.lean')], 180),
        ])
        self.assertEqual(sum(timeout for _, timeout in self.calls), 1260)
        self.assertEqual(result['kernel_replay'], 'leanchecker --fresh AC.GateProof')
        self.assertEqual(result['generic_contract_audit'], self.audit)
        self.assertEqual(json.loads(self.output.read_bytes()), result)

    def test_each_failed_stage_stops_before_inventory_and_profile_publication(self):
        for stage in range(3):
            for failure in (subprocess.TimeoutExpired, subprocess.CalledProcessError):
                with self.subTest(stage=stage, failure=failure.__name__):
                    self.calls.clear()
                    with self.assertRaises(failure):
                        self.establish(fail_at=stage, failure=failure)
                    self.assertEqual(len(self.calls), stage + 1)
                    self.assertFalse(self.output.exists())

    def test_missing_or_forbidden_axiom_audit_never_publishes_support(self):
        incomplete = self.audit.split('\n', 1)[1]
        forbidden = self.audit.replace('does not depend on any axioms',
                                        'depends on axioms: [sorryAx]', 1)
        for audit in (incomplete, forbidden):
            with self.subTest(audit=audit[:80]):
                self.calls.clear()
                with self.assertRaisesRegex(ValueError, 'theorem coverage/axiom audit failed'):
                    self.establish(audit=audit)
                self.assertEqual(len(self.calls), 3)
                self.assertFalse(self.output.exists())

    def test_existing_profile_is_preserved_before_any_compiler_effect(self):
        self.output.parent.mkdir()
        self.output.write_bytes(b'original selected profile')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.establish()
        self.assertEqual(self.calls, [])
        self.assertEqual(self.output.read_bytes(), b'original selected profile')


if __name__ == '__main__':
    unittest.main()
