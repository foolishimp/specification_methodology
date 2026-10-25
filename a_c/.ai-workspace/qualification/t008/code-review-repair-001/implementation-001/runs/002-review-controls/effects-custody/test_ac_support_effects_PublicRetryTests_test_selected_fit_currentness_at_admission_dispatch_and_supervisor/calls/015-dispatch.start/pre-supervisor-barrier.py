import sys,time
from pathlib import Path
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_effects as e
original=e._fault
def barrier(point):
 if point=='supervisor:before_spawn':
  Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-retry-4z7j75_z/fit-supervisor/workspace/inputs/host-bound.json').write_bytes(b'{"claimed_bytes":2000000}')
  Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-retry-4z7j75_z/calls/015-dispatch.start/barrier-reached.txt').write_text(str(time.time_ns()))
 original(point)
e._fault=barrier
raise SystemExit(a.main())
