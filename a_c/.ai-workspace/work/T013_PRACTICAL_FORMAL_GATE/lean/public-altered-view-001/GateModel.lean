module
public import GateIdentities
public import GateBounds
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem model_checked : checkModel model = true :=
 checked_of_wellFormed model (wellFormed_of_range model 1987 keys_exact names_checked external_checked separate edgeBounds refBounds)
#print axioms model_checked
end AC.GateData
