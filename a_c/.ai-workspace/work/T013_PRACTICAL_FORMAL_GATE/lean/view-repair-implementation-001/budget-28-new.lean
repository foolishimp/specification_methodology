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
theorem witness_edge0_0 : 1122 ∈ model.dependencies 182 := by decide +kernel
theorem witness_edge0_1 : 1124 ∈ model.dependencies 182 := by decide +kernel
theorem witness_edge0_2 : 1125 ∈ model.dependencies 182 := by decide +kernel
theorem witness_edge0_3 : 1215 ∈ model.dependencies 278 := by decide +kernel
theorem witness_edge0_4 : 1217 ∈ model.dependencies 278 := by decide +kernel
theorem witness_edge0_5 : 181 ∈ model.dependencies 1122 := by decide +kernel
theorem witness_edge0_6 : 183 ∈ model.dependencies 1125 := by decide +kernel
theorem witness_edge0_7 : 1867 ∈ model.dependencies 1125 := by decide +kernel
theorem witness_edge0_8 : 276 ∈ model.dependencies 1215 := by decide +kernel
theorem witness_edge0_9 : 277 ∈ model.dependencies 1215 := by decide +kernel
theorem witness_edge0_10 : 1121 ∈ model.dependencies 181 := by decide +kernel
theorem witness_edge0_11 : 1123 ∈ model.dependencies 181 := by decide +kernel
theorem witness_edge0_12 : 1126 ∈ model.dependencies 181 := by decide +kernel
theorem witness_edge0_13 : 1220 ∈ model.dependencies 276 := by decide +kernel
theorem witness_edge0_14 : 738 ∈ model.dependencies 277 := by decide +kernel
theorem witness_edge0_15 : 1216 ∈ model.dependencies 277 := by decide +kernel
theorem witness_edge0_16 : 1748 ∈ model.dependencies 277 := by decide +kernel
theorem witness_edge0_17 : 184 ∈ model.dependencies 1126 := by decide +kernel
theorem witness_edge0_18 : 281 ∈ model.dependencies 1220 := by decide +kernel
theorem witness_edge0_19 : 1127 ∈ model.dependencies 184 := by decide +kernel
theorem witness_edge0_20 : 1128 ∈ model.dependencies 184 := by decide +kernel
theorem witness_edge0_21 : 739 ∈ model.dependencies 281 := by decide +kernel
theorem witness_edge0_22 : 1219 ∈ model.dependencies 281 := by decide +kernel
theorem witness_edge0_23 : 1221 ∈ model.dependencies 281 := by decide +kernel
theorem witness_edge0_24 : 1749 ∈ model.dependencies 281 := by decide +kernel
theorem witness_edge0_25 : 282 ∈ model.dependencies 1221 := by decide +kernel
theorem witness_edge0_26 : 740 ∈ model.dependencies 282 := by decide +kernel
theorem witness0 : Witness model.dependencies seeds0 trace0 := by
 exact
  ⟨⟨182, by decide +kernel, witness_edge0_0⟩,
   ⟨⟨182, by decide +kernel, witness_edge0_1⟩,
    ⟨⟨182, by decide +kernel, witness_edge0_2⟩,
     ⟨⟨278, by decide +kernel, witness_edge0_3⟩,
      ⟨⟨278, by decide +kernel, witness_edge0_4⟩,
       ⟨⟨1122, by decide +kernel, witness_edge0_5⟩,
        ⟨⟨1125, by decide +kernel, witness_edge0_6⟩,
         ⟨⟨1125, by decide +kernel, witness_edge0_7⟩,
          ⟨⟨1215, by decide +kernel, witness_edge0_8⟩,
           ⟨⟨1215, by decide +kernel, witness_edge0_9⟩,
            ⟨⟨181, by decide +kernel, witness_edge0_10⟩,
             ⟨⟨181, by decide +kernel, witness_edge0_11⟩,
              ⟨⟨181, by decide +kernel, witness_edge0_12⟩,
               ⟨⟨276, by decide +kernel, witness_edge0_13⟩,
                ⟨⟨277, by decide +kernel, witness_edge0_14⟩,
                 ⟨⟨277, by decide +kernel, witness_edge0_15⟩,
                  ⟨⟨277, by decide +kernel, witness_edge0_16⟩,
                   ⟨⟨1126, by decide +kernel, witness_edge0_17⟩,
                    ⟨⟨1220, by decide +kernel, witness_edge0_18⟩,
                     ⟨⟨184, by decide +kernel, witness_edge0_19⟩,
                      ⟨⟨184, by decide +kernel, witness_edge0_20⟩,
                       ⟨⟨281, by decide +kernel, witness_edge0_21⟩,
                        ⟨⟨281, by decide +kernel, witness_edge0_22⟩,
                         ⟨⟨281, by decide +kernel, witness_edge0_23⟩,
                          ⟨⟨281, by decide +kernel, witness_edge0_24⟩,
                           ⟨⟨1221, by decide +kernel, witness_edge0_25⟩,
                            ⟨⟨282, by decide +kernel, witness_edge0_26⟩,
                             True.intro⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩
theorem seed_nonempty0 : seeds0.Nonempty := by decide +kernel
theorem seed_universe0 : seeds0 ⊆ Finset.range 1987 := by decide +kernel
theorem trace_universe0 : traceSet seeds0 trace0 ⊆ Finset.range 1987 := by decide +kernel
theorem closed0 : Closed model.dependencies (traceSet seeds0 trace0) := by decide +kernel
theorem checked0 : checkCertificate model.dependencies model.localKeys seeds0 trace0 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty0, seed_universe0, trace_universe0, witness0, closed0⟩
theorem set0 : traceSet seeds0 trace0 = included0 := by decide +kernel
theorem reachability0 (x : Nat) : x ∈ included0 ↔ Reachable model.dependencies seeds0 x := by
 rw [← set0]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds0 trace0 checked0 x
theorem result0 : project model seeds0 trace0 28 = .error "insufficient record budget; required closure is not truncated" :=
 insufficient_budget_refuses model seeds0 trace0 28 model_checked checked0 (by decide +kernel)
def execution0 : Except String Projection := projectWithProof model seeds0 trace0 28 model_checked checked0
theorem execution_matches_project0 : execution0 = project model seeds0 trace0 28 :=
 projectWithProof_eq_project model seeds0 trace0 28 model_checked checked0
#print axioms checked0
#print axioms set0
#print axioms reachability0
#print axioms result0
#print axioms execution_matches_project0
def selections : List (Finset Nat × List Nat × Nat) := [(seeds0,trace0,28)]
def executions : List (Except String Projection) := [execution0]
end AC.GateData
