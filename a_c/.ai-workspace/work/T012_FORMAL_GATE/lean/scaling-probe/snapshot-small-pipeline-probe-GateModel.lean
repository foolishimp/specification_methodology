module
public import GateData
public import AC.Structure
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
theorem keys_exact : model.records.map Record.key = List.range 32 := by rfl
theorem names_checked : (model.records.map Record.identity).Nodup := by
 apply names_nodup_of_order _ lookupName nameOrder 32 6
 · rfl
 · decide +kernel
 · decide +kernel
theorem external_checked : (model.externalResolutions.map External.identity).Nodup := by decide +kernel
theorem separate0 : ∀ x ∈ records0, (fun r : Record => r.identity ∉ model.externalResolutions.map External.identity) x := by decide +kernel
theorem separate : ∀ x ∈ model.records, (fun r : Record => r.identity ∉ model.externalResolutions.map External.identity) x := by
 change ∀ x ∈ [records0].flatten, (fun r : Record => r.identity ∉ model.externalResolutions.map External.identity) x
 apply all_flatten
 intro block member
 simp only [List.mem_cons, List.not_mem_nil, or_false] at member
 rcases member with rfl
 · exact separate0
theorem edgeBounds0 : ∀ x ∈ edges0, (fun e : Nat × Nat => e.1 < 32 ∧ e.2 < 32) x := by decide +kernel
theorem edgeBounds : ∀ x ∈ model.edges, (fun e : Nat × Nat => e.1 < 32 ∧ e.2 < 32) x := by
 change ∀ x ∈ [edges0].flatten, (fun e : Nat × Nat => e.1 < 32 ∧ e.2 < 32) x
 apply all_flatten
 intro block member
 simp only [List.mem_cons, List.not_mem_nil, or_false] at member
 rcases member with rfl
 · exact edgeBounds0
theorem refBounds0 : ∀ x ∈ references0, (fun r : Reference => r.owner < 32 ∧ targetBound 32 (model.externalResolutions.map External.identity) r.target) x := by decide +kernel
theorem refBounds1 : ∀ x ∈ references1, (fun r : Reference => r.owner < 32 ∧ targetBound 32 (model.externalResolutions.map External.identity) r.target) x := by decide +kernel
theorem refBounds : ∀ x ∈ model.references, (fun r : Reference => r.owner < 32 ∧ targetBound 32 (model.externalResolutions.map External.identity) r.target) x := by
 change ∀ x ∈ [references0, references1].flatten, (fun r : Reference => r.owner < 32 ∧ targetBound 32 (model.externalResolutions.map External.identity) r.target) x
 apply all_flatten
 intro block member
 simp only [List.mem_cons, List.not_mem_nil, or_false] at member
 rcases member with rfl | rfl
 · exact refBounds0
 · exact refBounds1
theorem model_checked : checkModel model = true :=
 checked_of_wellFormed model (wellFormed_of_range model 32 keys_exact names_checked external_checked separate edgeBounds refBounds)
#print axioms model_checked
end AC.GateData
