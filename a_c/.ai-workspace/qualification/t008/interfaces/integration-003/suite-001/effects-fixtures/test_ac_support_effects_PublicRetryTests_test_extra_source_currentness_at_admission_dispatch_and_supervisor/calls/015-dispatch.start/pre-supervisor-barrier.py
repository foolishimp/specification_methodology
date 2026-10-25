import sys,time
from pathlib import Path
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_effects as e
original=e._fault
def barrier(point):
 if point=='supervisor:before_spawn':
  Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-integrated-check-1is4hsh2/ac-public-retry-8kd6dhir/extra-source-supervisor/workspace/inputs/material.txt').write_bytes(b'incompatible deciding input two')
  Path('/private/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/a-c-integrated-check-1is4hsh2/ac-public-retry-8kd6dhir/calls/015-dispatch.start/barrier-reached.txt').write_text(str(time.time_ns()))
 original(point)
e._fault=barrier
raise SystemExit(a.main())
