import AC
set_option debug.skipKernelTC false
set_option maxRecDepth 100000

/-! Reviewer probe (Fable 5.1, 2026-11-01). Question: does the Lean side tie the
declared `edges` relation to the typed `references` it also carries? A model with a
governing local reference 0 -> 1 but an empty `edges` list is accepted as WellFormed,
and the closure of seed 0 is {0}. The kernel therefore proves "exact closure" relative
to `edges` alone; the importer (Python) is the sole guarantor that `edges` reflects the
governing references. -/
namespace ReviewProbe

def r0 : AC.Record := { key := 0, identity := "a", family := .objects, context := "c", owner := "o", scope := "s", basis := "b", payload := "{}" }
def r1 : AC.Record := { key := 1, identity := "b", family := .objects, context := "c", owner := "o", scope := "s", basis := "b", payload := "{}" }

def gap : AC.Model := {
  identity := "m", rawSha256 := "r", canonicalSha256 := "c", envelope := "{}",
  records := [r0, r1],
  references := [{ owner := 0, path := [.field "requires"], target := .localRecord 1, governing := true, domain := "d" }],
  externalResolutions := [], edges := [], invalidation := "{}" }

theorem gap_wellFormed : AC.checkModel gap = true := by decide +kernel
theorem gap_certificate : AC.checkCertificate gap.dependencies gap.localKeys {0} [] = true := by decide +kernel
theorem gap_closure_is_seed_only : AC.traceSet ({0} : Finset Nat) [] = {0} := by decide +kernel
theorem gap_success : AC.project gap {0} [] 1 = .ok (AC.makeProjection gap {0} {0}) :=
  AC.projection_success gap {0} [] 1 gap_wellFormed gap_certificate (by decide +kernel)
theorem gap_excludes_governed_target : 1 ∉ AC.traceSet ({0} : Finset Nat) [] := by decide +kernel

/-- The missing kernel-side obligation, stated as a decidable Boolean check: every
governing local reference must be a declared edge. `gap` fails it. -/
def governingCovered (m : AC.Model) : Bool :=
  m.references.all fun ref =>
    match ref.target with
    | .localRecord k => !ref.governing || decide ((ref.owner, k) ∈ m.edges)
    | .external _ => true

theorem gap_not_covered : governingCovered gap = false := by decide +kernel

#print axioms gap_success
#print axioms gap_not_covered
end ReviewProbe
