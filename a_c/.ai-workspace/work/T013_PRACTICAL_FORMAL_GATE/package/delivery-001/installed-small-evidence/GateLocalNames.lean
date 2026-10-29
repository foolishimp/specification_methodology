module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem keys_exact : model.records.map Record.key = List.range 6 := by rfl
end AC.GateData
