module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
set_option profiler true
set_option profiler.threshold 1
namespace Probe
open AC AC.GateData
theorem sourceEq : model.records.map Record.identity = (List.range 32).map lookupName := by rfl
#print axioms sourceEq
theorem numericPermutation : sortIndices 6 nameOrder = List.range 32 := by decide +kernel
#print axioms numericPermutation
theorem orderedNames : (nameOrder.map lookupName).IsChain (· < ·) := by decide +kernel
#print axioms orderedNames
end Probe
