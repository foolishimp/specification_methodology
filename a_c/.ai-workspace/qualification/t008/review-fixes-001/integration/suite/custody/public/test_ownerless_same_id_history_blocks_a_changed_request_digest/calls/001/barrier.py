import sys,time
from pathlib import Path
from contextlib import contextmanager
sys.path.insert(0,'/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-fix-integration-z9_xtyyk/snapshot/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_core as c,ac_support_effects as e
def fault(point):
 if point=='writer_intent:before_publish': raise SystemExit(77)
e._fault=fault
raise SystemExit(a.main())
