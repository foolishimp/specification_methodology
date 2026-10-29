module
public import GateViews
meta import GateViews
public import AC.GateRuntime
meta import AC.GateRuntime
public import Lean.Data.Json.Basic
@[expose] public section
namespace AC.GateData
def selectedExecution : Except String Projection :=
 projectWithProof model seeds0 trace0 9 model_checked checked0
theorem selectedExecution_matches_original : selectedExecution = project model seeds0 trace0 9 :=
 projectWithProof_eq_project model seeds0 trace0 9 model_checked checked0
#print axioms selectedExecution_matches_original
end AC.GateData
def main : IO UInt32 := do
 let m := AC.GateData.model
 IO.println (Lean.Json.mkObj [("model", AC.GateRuntime.modelJson m),
   ("views", Lean.Json.arr #[AC.GateRuntime.selectionResultJson m AC.GateData.selectedExecution])]).compress
 return 0
