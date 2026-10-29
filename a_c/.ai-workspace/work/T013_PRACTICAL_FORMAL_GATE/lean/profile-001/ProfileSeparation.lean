module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem separate : ∀ r ∈ records0, r.identity ∉ model.externalResolutions.map External.identity := by decide +kernel
#print axioms separate
end AC.GateData
