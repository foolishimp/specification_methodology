module
import GateViews
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
example : AC.checkCertificate AC.GateData.model.dependencies AC.GateData.model.localKeys AC.GateData.seeds0 [] = true := by decide +kernel
