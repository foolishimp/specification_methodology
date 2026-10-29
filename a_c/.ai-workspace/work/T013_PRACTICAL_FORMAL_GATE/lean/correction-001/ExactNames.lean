module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem names_array : model.records.map Record.identity = nameTable.toList := by rfl
theorem nameTable_size : nameTable.size = 1987 := by rfl
theorem names_exact : model.records.map Record.identity = (List.range 1987).map lookupName := by
 rw [names_array]
 simpa only [nameTable_size, lookupName] using array_reconstruct nameTable ""
#print axioms AC.array_reconstruct
#print axioms names_array
#print axioms names_exact
end AC.GateData
