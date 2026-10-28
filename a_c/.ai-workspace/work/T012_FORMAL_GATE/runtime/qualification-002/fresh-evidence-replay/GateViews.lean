module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
def seeds0 : Finset Nat := ([0] : List Nat).toFinset
def trace0 : List Nat := [2, 3, 4, 5, 1]
def included0 : Finset Nat := ([0, 1, 2, 3, 4, 5] : List Nat).toFinset
theorem checked0 : checkCertificate model.dependencies model.localKeys seeds0 trace0 = true := by
 rw [localKeys_range model _ keys_exact]
 decide +kernel
theorem set0 : traceSet seeds0 trace0 = included0 := by decide +kernel
theorem reachability0 (x : Nat) : x ∈ included0 ↔ Reachable model.dependencies seeds0 x := by
 rw [← set0]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds0 trace0 checked0 x
theorem result0 : project model seeds0 trace0 6 = .ok (makeProjection model seeds0 included0) := by
 rw [← set0]
 exact projection_success model seeds0 trace0 6 model_checked checked0 (by decide +kernel)
#print axioms checked0
#print axioms set0
#print axioms reachability0
#print axioms result0
def selections : List (Finset Nat × List Nat × Nat) := [(seeds0,trace0,6)]
end AC.GateData
