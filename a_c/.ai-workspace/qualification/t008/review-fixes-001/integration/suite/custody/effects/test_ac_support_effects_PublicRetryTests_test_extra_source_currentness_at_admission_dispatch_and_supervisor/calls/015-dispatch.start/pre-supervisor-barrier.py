import sys,time
from pathlib import Path
sys.path.insert(0,'/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-fix-integration-z9_xtyyk/snapshot/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_effects as e
original=e._fault
def barrier(point):
 if point=='supervisor:before_spawn':
  Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-fix-integration-z9_xtyyk/suite/ac-public-retry-wnxz9l5p/extra-source-supervisor/workspace/inputs/material.txt').write_bytes(b'incompatible deciding input two')
  Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/ac-fix-integration-z9_xtyyk/suite/ac-public-retry-wnxz9l5p/calls/015-dispatch.start/barrier-reached.txt').write_text(str(time.time_ns()))
 original(point)
e._fault=barrier
raise SystemExit(a.main())
