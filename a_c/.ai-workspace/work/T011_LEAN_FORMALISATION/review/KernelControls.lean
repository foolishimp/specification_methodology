import AC

set_option debug.skipKernelTC false
set_option maxRecDepth 100000

namespace IndependentReview

def deps (key : Nat) : Finset Nat :=
  if key = 0 then {1} else if key = 1 then {0} else if key = 2 then {2} else ∅

def keys : Finset Nat := {0, 1, 2}
def seeds : Finset Nat := {0}

-- A disconnected self-cycle can be added to a closed fixed point, but is not
-- reachable and cannot enter a successful least-closure certificate.
example : AC.Closed deps keys := by decide +kernel
example : AC.checkCertificate deps keys seeds [1] = true := by decide +kernel
example : AC.checkCertificate deps keys seeds [1, 2] = false := by decide +kernel
example : AC.checkCertificate deps keys seeds [] = false := by decide +kernel
example : AC.checkCertificate deps keys (∅ : Finset Nat) [] = false := by decide +kernel

theorem exactSelected (x : Nat) :
    x ∈ AC.traceSet seeds [1] ↔ AC.Reachable deps seeds x :=
  AC.certificate_exact_reachability deps keys seeds [1] (by decide +kernel) x

theorem disconnectedNotReachable : ¬ AC.Reachable deps seeds 2 := by
  intro reachable
  have included := (exactSelected 2).mpr reachable
  have excluded : 2 ∉ AC.traceSet seeds [1] := by decide +kernel
  exact excluded included

def dangling : AC.Model := { AC.Fixture.model with edges := [(0, 1000)] }
theorem dangling_checked : AC.checkModel dangling = false := by decide +kernel
example : AC.project dangling AC.Fixture.seeds0 AC.Fixture.trace0 32 =
    .error "invalid imported model or closure certificate" := by
  simp [AC.project, dangling_checked]

#print axioms exactSelected
#print axioms disconnectedNotReachable

end IndependentReview
