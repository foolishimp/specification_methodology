module
import GateData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
 theorem names_checked : (model.records.map Record.identity).Nodup := by decide +kernel
#print axioms names_checked
end AC.GateData
