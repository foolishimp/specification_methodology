module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem keys : model.records.map Record.key = List.range 1987 := by rfl
theorem names : model.records.map Record.identity = (List.range 1987).map lookupName := by rfl
#print axioms keys
#print axioms names
end AC.GateData
