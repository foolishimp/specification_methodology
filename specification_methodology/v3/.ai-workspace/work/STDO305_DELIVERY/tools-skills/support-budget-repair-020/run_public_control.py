"""Run only the gate control without the cleanup fixture's temporary support ROOT."""
from pathlib import Path
import sys
import unittest

REPO = Path('/Users/jim/src/apps/specification_methodology')
sys.path.insert(0, str(REPO / 'a_c/build_tenants/lean/tests'))
import test_formal_gate

suite = unittest.TestSuite([test_formal_gate.FormalGateTests(
    'test_unsettled_group_denial_is_incomplete_without_verified_claims')])
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
