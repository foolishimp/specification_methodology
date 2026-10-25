import sys,time
from pathlib import Path
from contextlib import contextmanager
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_core as c,ac_support_effects as e
original_plan=c.prepare_write
def plan(runtime,request):
 Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-integrated-check-3vlvt6ql/ac-public-writer-6i4ii8vb/plan-planning').write_text(str(time.time_ns()))
 deadline=time.monotonic()+8
 while not Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-integrated-check-3vlvt6ql/ac-public-writer-6i4ii8vb/release-planning').exists():
  if time.monotonic()>deadline: raise RuntimeError('Test barrier expired')
  time.sleep(0.005)
 return original_plan(runtime,request)
c.prepare_write=plan
raise SystemExit(a.main())
