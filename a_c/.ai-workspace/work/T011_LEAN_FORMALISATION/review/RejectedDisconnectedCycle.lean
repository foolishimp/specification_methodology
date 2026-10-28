import AC.Closure
set_option debug.skipKernelTC false
def disconnected (key : Nat) : Finset Nat :=
  if key = 0 then {1} else if key = 1 then {0} else if key = 2 then {2} else ∅
-- Deliberately false. Closedness alone does not justify this extra cycle.
example : AC.checkCertificate disconnected {0, 1, 2} {0} [1, 2] = true := by decide +kernel
