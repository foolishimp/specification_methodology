module
public import AC.Projection
public import AC.Structure

/-! The reusable gate's complete generic proof root. Serialization is a separate
tested runtime boundary and is deliberately absent from this proof import graph. -/
public section

namespace AC

/-- Execute the original budget/projection computation on a domain whose model
and closure checks have already been proved. Proofs remain exact dependent inputs;
this is not an unchecked projection constructor or a cached status flag. -/
@[expose] def projectWithProof (m : Model) (seeds : Finset Nat) (trace : List Nat)
    (budget : Nat) (_modelChecked : checkModel m = true)
    (_closureChecked : checkCertificate m.dependencies m.localKeys seeds trace = true) :
    Except String Projection :=
  if (traceSet seeds trace).card ≤ budget then
    .ok (makeProjection m seeds (traceSet seeds trace))
  else .error "insufficient record budget; required closure is not truncated"

theorem projectWithProof_eq_project (m : Model) (seeds : Finset Nat)
    (trace : List Nat) (budget : Nat)
    (modelChecked : checkModel m = true)
    (closureChecked : checkCertificate m.dependencies m.localKeys seeds trace = true) :
    projectWithProof m seeds trace budget modelChecked closureChecked =
      project m seeds trace budget := by
  simp [projectWithProof, project, modelChecked, closureChecked]

end AC

#print axioms AC.checkModel_sound
#print axioms AC.certificate_exact_reachability
#print axioms AC.certificate_unique
#print axioms AC.project_ok_properties
#print axioms AC.projection_all_residuals_accounted
#print axioms AC.names_nodup_of_order
#print axioms AC.array_reconstruct
#print axioms AC.sortLabeled_perm
#print axioms AC.nodup_of_labeled_characters
#print axioms AC.rendered_labeled_source
#print axioms AC.isChain_of_pairs
#print axioms AC.separated_of_nodup
#print axioms AC.member_of_block_index
#print axioms AC.mapped_block_inside
#print axioms AC.wellFormed_of_range
#print axioms AC.checked_of_wellFormed
#print axioms AC.projectWithProof_eq_project
