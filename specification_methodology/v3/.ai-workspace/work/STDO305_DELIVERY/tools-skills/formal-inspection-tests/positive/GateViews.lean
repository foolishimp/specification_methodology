module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
def seeds0 : Finset Nat := ([1] : List Nat).toFinset
def trace0 : List Nat := [2, 3, 4, 6, 8, 9, 10, 5]
def included0 : Finset Nat := ([1, 2, 3, 4, 5, 6, 8, 9, 10] : List Nat).toFinset
theorem witness_edge0_0 : 2 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_1 : 3 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_2 : 4 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_3 : 6 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_4 : 8 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_5 : 9 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_6 : 10 ∈ model.dependencies 1 := by decide +kernel
theorem witness_edge0_7 : 5 ∈ model.dependencies 2 := by decide +kernel
theorem witness0 : Witness model.dependencies seeds0 trace0 := by
 exact
  ⟨⟨1, by decide +kernel, witness_edge0_0⟩,
   ⟨⟨1, by decide +kernel, witness_edge0_1⟩,
    ⟨⟨1, by decide +kernel, witness_edge0_2⟩,
     ⟨⟨1, by decide +kernel, witness_edge0_3⟩,
      ⟨⟨1, by decide +kernel, witness_edge0_4⟩,
       ⟨⟨1, by decide +kernel, witness_edge0_5⟩,
        ⟨⟨1, by decide +kernel, witness_edge0_6⟩,
         ⟨⟨2, by decide +kernel, witness_edge0_7⟩,
          True.intro⟩⟩⟩⟩⟩⟩⟩⟩
theorem seed_nonempty0 : seeds0.Nonempty := by decide +kernel
theorem seed_universe0 : seeds0 ⊆ Finset.range 14 := by decide +kernel
theorem trace_universe0 : traceSet seeds0 trace0 ⊆ Finset.range 14 := by decide +kernel
theorem closed0 : Closed model.dependencies (traceSet seeds0 trace0) := by decide +kernel
theorem checked0 : checkCertificate model.dependencies model.localKeys seeds0 trace0 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty0, seed_universe0, trace_universe0, witness0, closed0⟩
theorem set0 : traceSet seeds0 trace0 = included0 := by decide +kernel
theorem reachability0 (x : Nat) : x ∈ included0 ↔ Reachable model.dependencies seeds0 x := by
 rw [← set0]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds0 trace0 checked0 x
theorem result0 : project model seeds0 trace0 9 = .ok (makeProjection model seeds0 included0) := by
 rw [← set0]
 exact projection_success model seeds0 trace0 9 model_checked checked0 (by decide +kernel)
def execution0 : Except String Projection := projectWithProof model seeds0 trace0 9 model_checked checked0
theorem execution_matches_project0 : execution0 = project model seeds0 trace0 9 :=
 projectWithProof_eq_project model seeds0 trace0 9 model_checked checked0
#print axioms checked0
#print axioms set0
#print axioms reachability0
#print axioms result0
#print axioms execution_matches_project0
def selections : List (Finset Nat × List Nat × Nat) := [(seeds0,trace0,9)]
def executions : List (Except String Projection) := [execution0]
end AC.GateData
