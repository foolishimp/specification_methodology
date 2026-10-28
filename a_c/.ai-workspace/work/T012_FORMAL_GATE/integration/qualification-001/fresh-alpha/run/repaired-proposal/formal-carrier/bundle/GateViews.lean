module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
def selections : List (Finset Nat × List Nat × Nat) := []
end AC.GateData
