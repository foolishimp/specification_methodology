module
import GateData
import AC.Structure
import all Init.Data.List.Sort.Basic
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
 theorem names_checked : (model.records.map Record.identity).Nodup := by
  apply names_nodup_of_sorted _ 11
  decide +kernel
#print axioms names_checked
end AC.GateData
