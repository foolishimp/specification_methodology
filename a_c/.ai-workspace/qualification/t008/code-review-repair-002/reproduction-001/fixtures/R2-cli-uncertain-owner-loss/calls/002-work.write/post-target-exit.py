import sys
sys.path.insert(0,'/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
import ac_support as a,ac_support_effects as e
def fault(point):
 if point=='writer:after_target_publication': raise SystemExit(77)
e._fault=fault
raise SystemExit(a.main())
