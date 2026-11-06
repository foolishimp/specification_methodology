module
public import GateIdentities
public import GateBounds
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem model_checked : checkModel model = true := by decide +kernel
#print axioms model_checked
end AC.GateData
