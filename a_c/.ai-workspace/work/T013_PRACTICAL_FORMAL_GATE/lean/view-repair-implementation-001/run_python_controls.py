"""Run live Lean Python tests with temporary writes confined to this activation."""
from contextlib import ExitStack
import importlib
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]/'build_tenants/lean'
temporary=OUT/'python-tmp';temporary.mkdir()
tempfile.tempdir=str(temporary)
os.environ['TMPDIR']=str(temporary)
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ.pop('AC_FORMAL_CONTROL_EVIDENCE',None)
original_temporary=tempfile.TemporaryDirectory
original_mkdir=Path.mkdir
redirected={ROOT/'.cache',ROOT/'.cache/reuse-unit'}
def scoped_temporary(*args,**kwargs):
 if kwargs.get('dir') is not None and Path(kwargs['dir']) in redirected:kwargs['dir']=temporary
 return original_temporary(*args,**kwargs)
def scoped_mkdir(path,*args,**kwargs):
 if path in redirected:return None
 return original_mkdir(path,*args,**kwargs)
modules=('test_adapter','test_formal_gate','test_runtime_process','test_formal_reuse','test_gate_codegen')
with ExitStack() as stack:
 stack.enter_context(patch.object(tempfile,'TemporaryDirectory',scoped_temporary))
 stack.enter_context(patch.object(Path,'mkdir',scoped_mkdir))
 sys.path.insert(0,str(ROOT/'tests'))
 suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(importlib.import_module(name)) for name in modules)
 assert suite.countTestCases()==77,suite.countTestCases()
 started=time.monotonic()
 result=unittest.TextTestRunner(verbosity=2).run(suite)
 record={'schema':'a_c.T013.view-repair-python-controls/1','status':'PASS' if result.wasSuccessful() else 'FAIL','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'seconds':time.monotonic()-started,'modules':list(modules),'live_deciding_sources_loaded':True,'temporary_substitution':'tempfile defaults and only the two explicit live test-cache TemporaryDirectory arguments redirect here; mkdir of exactly those cache paths is a no-op; all other filesystem/code behavior unchanged.','evidence_kind':'Python controls; reuse support/proof stubs and temporary synthetic origins are unit evidence only.'}
 (OUT/'PYTHON-RESULTS.json').write_text(json.dumps(record,indent=2)+'\n')
 print(json.dumps(record),flush=True)
 raise SystemExit(0 if result.wasSuccessful() else 1)
