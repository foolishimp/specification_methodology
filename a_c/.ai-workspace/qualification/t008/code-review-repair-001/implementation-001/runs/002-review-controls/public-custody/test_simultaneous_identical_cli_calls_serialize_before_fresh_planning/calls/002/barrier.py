import sys,time
from pathlib import Path
from contextlib import contextmanager
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_core as c,ac_support_effects as e
original_plan=c.prepare_write
def plan(runtime,request):
 Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-writer-dljb0p_v/contender-planning').write_text(str(time.time_ns()))
 return original_plan(runtime,request)
c.prepare_write=plan
original_lock=e.EvidenceStore._lock
@contextmanager
def lock(store,identity,*,nonblocking=False):
 if identity.startswith('request:'): Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-writer-dljb0p_v/contender-attempted').write_text(str(time.time_ns()))
 with original_lock(store,identity,nonblocking=nonblocking):
  if identity.startswith('request:'): Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-writer-dljb0p_v/contender-acquired').write_text(str(time.time_ns()))
  yield
e.EvidenceStore._lock=lock
raise SystemExit(a.main())
