module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
def seeds0 : Finset Nat := ([182, 278] : List Nat).toFinset
def trace0 : List Nat := [1122, 1124, 1125, 1215, 1217, 181, 183, 1867, 276, 277, 1121, 1123, 1126, 1220, 738, 1216, 1748, 184, 281, 1127, 1128, 739, 1219, 1221, 1749, 282, 740]
def included0 : Finset Nat := ([181, 182, 183, 184, 276, 277, 278, 281, 282, 738, 739, 740, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1215, 1216, 1217, 1219, 1220, 1221, 1748, 1749, 1867] : List Nat).toFinset
theorem checked0 : checkCertificate model.dependencies model.localKeys seeds0 trace0 = true := by
 rw [localKeys_range model _ keys_exact]
 decide +kernel
theorem set0 : traceSet seeds0 trace0 = included0 := by decide +kernel
theorem reachability0 (x : Nat) : x ∈ included0 ↔ Reachable model.dependencies seeds0 x := by
 rw [← set0]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds0 trace0 checked0 x
theorem result0 : project model seeds0 trace0 29 = .ok (makeProjection model seeds0 included0) := by
 rw [← set0]
 exact projection_success model seeds0 trace0 29 model_checked checked0 (by decide +kernel)
def execution0 : Except String Projection := projectWithProof model seeds0 trace0 29 model_checked checked0
theorem execution_matches_project0 : execution0 = project model seeds0 trace0 29 :=
 projectWithProof_eq_project model seeds0 trace0 29 model_checked checked0
#print axioms checked0
#print axioms set0
#print axioms reachability0
#print axioms result0
#print axioms execution_matches_project0
def selections : List (Finset Nat × List Nat × Nat) := [(seeds0,trace0,29)]
def executions : List (Except String Projection) := [execution0]
end AC.GateData
