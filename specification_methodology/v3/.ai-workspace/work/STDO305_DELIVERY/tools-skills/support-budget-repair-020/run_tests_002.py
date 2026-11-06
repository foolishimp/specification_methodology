"""Selected support-budget unit controls and two actual Python group-cleanup cases."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path('/Users/jim/src/apps/specification_methodology')
LEAN = REPO / 'a_c/build_tenants/lean'
sys.path.insert(0, str(LEAN / 'scripts'))
import formal_support

suite = unittest.TestSuite()
loader = unittest.TestLoader()
for name in ('test_formal_support_budget.py', 'test_runtime_process.py'):
    suite.addTests(loader.discover(str(LEAN / 'tests'), pattern=name))
sys.path.insert(0, str(LEAN / 'tests'))
import test_formal_gate
suite.addTest(test_formal_gate.FormalGateTests('test_unsettled_group_denial_is_incomplete_without_verified_claims'))
with tempfile.TemporaryDirectory(prefix='support-budget-test-') as directory:
    root = Path(directory)
    (root / '.cache').mkdir()
    with patch.object(formal_support, 'ROOT', root):
        result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
