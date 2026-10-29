module
public import AC.Structure
public section
example : AC.identityCode "a" = 355 := by decide +kernel
example : AC.identityCode "a" = 355 := by rfl
#print axioms AC.nodup_of_codes
