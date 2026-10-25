import sys,time
from pathlib import Path
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_effects as e
original=e._fault
def barrier(point):
 if point=='supervisor:before_spawn':
  Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-retry-o04sdovw/extra-source-supervisor/workspace/inputs/material.txt').write_bytes(b'incompatible deciding input two')
  Path('/Users/jim/src/apps/specification_methodology/a_c/.ai-workspace/qualification/t008/code-review-repair-001/implementation-001/tmp/ac-public-retry-o04sdovw/calls/015-dispatch.start/barrier-reached.txt').write_text(str(time.time_ns()))
 original(point)
e._fault=barrier
raise SystemExit(a.main())
