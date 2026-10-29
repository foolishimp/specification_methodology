module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem ordering : (nameOrder.map lookupName).IsChain (· < ·) := by decide +kernel
#print axioms ordering
end AC.GateData
