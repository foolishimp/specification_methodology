module
public import AC.Projection
public import AC.Structure

/-! The reusable gate's complete generic proof root. Serialization is a separate
tested runtime boundary and is deliberately absent from this proof import graph. -/
public section
#print axioms AC.checkModel_sound
#print axioms AC.certificate_exact_reachability
#print axioms AC.certificate_unique
#print axioms AC.project_ok_properties
#print axioms AC.projection_all_residuals_accounted
#print axioms AC.names_nodup_of_order
#print axioms AC.array_reconstruct
#print axioms AC.nodup_of_codes
#print axioms AC.separated_of_nodup
#print axioms AC.member_of_block_index
#print axioms AC.mapped_block_inside
#print axioms AC.wellFormed_of_range
#print axioms AC.checked_of_wellFormed
