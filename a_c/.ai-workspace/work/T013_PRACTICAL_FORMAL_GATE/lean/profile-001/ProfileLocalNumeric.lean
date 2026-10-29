module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem numeric : sortIndices 11 nameOrder = List.range 1987 := by decide +kernel
#print axioms numeric
end AC.GateData
