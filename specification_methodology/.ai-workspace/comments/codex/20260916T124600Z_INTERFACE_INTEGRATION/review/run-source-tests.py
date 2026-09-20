"""Run frozen source guards read-only; no semantic/runtime/UAT classifier."""
import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest

REVIEW = Path(__file__).resolve().parent
ROOT = REVIEW.parents[4]
CANDIDATE = REVIEW.parent / "source-worker/candidate"

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

boundary = load("test_reference_frame_boundaries", CANDIDATE / "tests/test_reference_frame_boundaries.py")
for name in ("METHOD", "SPEC_METHOD", "PRODUCT", "BASIS", "DEFINITION", "DECISION", "BASIS_TEMPLATE"):
    original = getattr(boundary, name)
    setattr(boundary, name, ROOT / original.relative_to(CANDIDATE))
boundary.ROOT = ROOT
# PROFILE, COMPRESSION and BOOTSTRAP remain the exact frozen candidate paths.
interface = load("test_interface_integration_frame", CANDIDATE / "tests/test_interface_integration_frame.py")
compression = load("test_compressions", ROOT / "tests/test_compressions.py")
# Unchanged complete source-dependency digests are checked against the byte-bound
# source tree. The two changed compression files are independently byte-equal
# to their frozen copies before and after this run.
suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(m) for m in (boundary, interface, compression))
stream = io.StringIO()
result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
print(json.dumps({"testsRun": result.testsRun, "failures": len(result.failures), "errors": len(result.errors), "successful": result.wasSuccessful(), "output": stream.getvalue()}))
sys.exit(0 if result.wasSuccessful() else 1)
