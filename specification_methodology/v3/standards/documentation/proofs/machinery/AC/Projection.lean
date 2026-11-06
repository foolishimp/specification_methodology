module
public import AC.Model
public import AC.Closure

@[expose] public section

namespace AC

def retained (m : Model) (selected : Finset Nat) : List Record :=
  m.records.filter fun r => decide (r.key ∈ selected)

/-- No record fields are rewritten. This also conserves opaque predicates,
    ordered arrays, repeated values, owner, basis, scope, and residual payloads. -/
theorem retained_iff (m : Model) (selected : Finset Nat) (r : Record) :
    r ∈ retained m selected ↔ r ∈ m.records ∧ r.key ∈ selected := by
  simp [retained]

def externalBoundary (m : Model) (selected : Finset Nat) : List External :=
  m.externalResolutions.filter fun e =>
    m.references.any fun ref => ref.owner ∈ selected && ref.target == .external e.identity

def ordinaryBoundary (m : Model) (selected : Finset Nat) : List Reference :=
  m.references.filter fun ref => ref.owner ∈ selected &&
    match ref.target with
    | .localRecord key => !(key ∈ selected)
    | .external _ => false

def residualBoundary (m : Model) (selected : Finset Nat) : List Record :=
  (retained m selected).filter fun r => r.family == .residuals

def excludedResidualBoundary (m : Model) (selected : Finset Nat) : List Record :=
  m.records.filter fun r => !(r.key ∈ selected) && r.family == .residuals

structure Projection where
  parentIdentity : String
  parentRawSha256 : String
  parentCanonicalSha256 : String
  parentEnvelope : String
  seeds : Finset Nat
  included : Finset Nat
  excluded : Finset Nat
  records : List Record
  external : List External
  ordinary : List Reference
  unresolved : List Record
  excludedResiduals : List Record
  invalidation : String

def makeProjection (m : Model) (seeds selected : Finset Nat) : Projection where
  parentIdentity := m.identity
  parentRawSha256 := m.rawSha256
  parentCanonicalSha256 := m.canonicalSha256
  parentEnvelope := m.envelope
  seeds := seeds
  included := selected
  excluded := m.localKeys \ selected
  records := retained m selected
  external := externalBoundary m selected
  ordinary := ordinaryBoundary m selected
  unresolved := residualBoundary m selected
  excludedResiduals := excludedResidualBoundary m selected
  invalidation := m.invalidation

/-- Finite record budget. No initialPath/truncation branch can return success. -/
def project (m : Model) (seeds : Finset Nat) (trace : List Nat) (budget : Nat) :
    Except String Projection :=
  if checkModel m && checkCertificate m.dependencies m.localKeys seeds trace then
    if (traceSet seeds trace).card ≤ budget then
      .ok (makeProjection m seeds (traceSet seeds trace))
    else .error "insufficient record budget; required closure is not truncated"
  else .error "invalid imported model or closure certificate"

theorem projection_success (m : Model) (seeds : Finset Nat) (trace : List Nat) (budget : Nat)
    (modelChecked : checkModel m = true)
    (closureChecked : checkCertificate m.dependencies m.localKeys seeds trace = true)
    (fits : (traceSet seeds trace).card ≤ budget) :
    project m seeds trace budget = .ok (makeProjection m seeds (traceSet seeds trace)) := by
  simp [project, modelChecked, closureChecked, fits]

/-- Eliminate a real executable success result; callers cannot substitute an
    arbitrary projection while appealing only to the generic theorem. -/
theorem project_ok_properties (m : Model) (seeds : Finset Nat) (trace : List Nat)
    (budget : Nat) (p : Projection) (result : project m seeds trace budget = .ok p) :
    checkModel m = true ∧
    checkCertificate m.dependencies m.localKeys seeds trace = true ∧
    (traceSet seeds trace).card ≤ budget ∧
    p = makeProjection m seeds (traceSet seeds trace) := by
  unfold project at result
  split at result
  · rename_i checks
    have checked : checkModel m = true ∧
        checkCertificate m.dependencies m.localKeys seeds trace = true := by
      simpa using checks
    split at result
    · rename_i fits
      exact ⟨checked.1, checked.2, fits, (Except.ok.inj result).symm⟩
    · cases result
  · cases result

theorem project_ok_exact_reachability (m : Model) (seeds : Finset Nat) (trace : List Nat)
    (budget : Nat) (p : Projection) (result : project m seeds trace budget = .ok p)
    (x : Nat) : x ∈ p.included ↔ Reachable m.dependencies seeds x := by
  have facts := project_ok_properties m seeds trace budget p result
  rw [facts.2.2.2]
  exact certificate_exact_reachability m.dependencies m.localKeys seeds trace facts.2.1 x

theorem insufficient_budget_refuses (m : Model) (seeds : Finset Nat) (trace : List Nat) (budget : Nat)
    (modelChecked : checkModel m = true)
    (closureChecked : checkCertificate m.dependencies m.localKeys seeds trace = true)
    (insufficient : budget < (traceSet seeds trace).card) :
    project m seeds trace budget =
      .error "insufficient record budget; required closure is not truncated" := by
  simp [project, modelChecked, closureChecked, Nat.not_le.mpr insufficient]

theorem projection_record_conservation (m : Model) (seeds selected : Finset Nat) (r : Record) :
    r ∈ (makeProjection m seeds selected).records ↔ r ∈ m.records ∧ r.key ∈ selected :=
  retained_iff m selected r

theorem projection_authority_basis_conservation (m : Model) (seeds selected : Finset Nat)
    (r : Record) (h : r ∈ (makeProjection m seeds selected).records) :
    ∃ original ∈ m.records, original = r ∧ original.owner = r.owner ∧
      original.scope = r.scope ∧ original.context = r.context ∧ original.basis = r.basis ∧
      original.payload = r.payload := by
  exact ⟨r, (projection_record_conservation m seeds selected r).mp h |>.1,
    rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem projection_residual_conservation (m : Model) (seeds selected : Finset Nat) (r : Record) :
    r ∈ (makeProjection m seeds selected).unresolved ↔
      r ∈ m.records ∧ r.key ∈ selected ∧ r.family = .residuals := by
  simp [makeProjection, residualBoundary, retained, and_assoc, and_comm]

theorem projection_excluded_exact (m : Model) (seeds selected : Finset Nat) (x : Nat) :
    x ∈ (makeProjection m seeds selected).excluded ↔ x ∈ m.localKeys ∧ x ∉ selected := by
  simp [makeProjection]

theorem projection_external_exact (m : Model) (seeds selected : Finset Nat) (e : External) :
    e ∈ (makeProjection m seeds selected).external ↔
      e ∈ m.externalResolutions ∧ ∃ ref ∈ m.references,
        ref.owner ∈ selected ∧ ref.target = .external e.identity := by
  simp [makeProjection, externalBoundary]

theorem projection_ordinary_exact (m : Model) (seeds selected : Finset Nat) (ref : Reference) :
    ref ∈ (makeProjection m seeds selected).ordinary ↔
      ref ∈ m.references ∧ ref.owner ∈ selected ∧
        ∃ key, ref.target = .localRecord key ∧ key ∉ selected := by
  cases h : ref.target <;> simp [makeProjection, ordinaryBoundary, h]

theorem projection_excluded_residual_exact (m : Model) (seeds selected : Finset Nat)
    (r : Record) :
    r ∈ (makeProjection m seeds selected).excludedResiduals ↔
      r ∈ m.records ∧ r.key ∉ selected ∧ r.family = .residuals := by
  simp [makeProjection, excludedResidualBoundary]

/-- Every original residual is either retained unresolved or explicitly named as
    an excluded residual; exclusion is never interpreted as disposition. -/
theorem projection_all_residuals_accounted (m : Model) (seeds selected : Finset Nat)
    (r : Record) (original : r ∈ m.records) (residual : r.family = .residuals) :
    r ∈ (makeProjection m seeds selected).unresolved ∨
      r ∈ (makeProjection m seeds selected).excludedResiduals := by
  by_cases h : r.key ∈ selected
  · exact Or.inl ((projection_residual_conservation m seeds selected r).mpr
      ⟨original, h, residual⟩)
  · exact Or.inr ((projection_excluded_residual_exact m seeds selected r).mpr
      ⟨original, h, residual⟩)

theorem projection_parent_conservation (m : Model) (seeds selected : Finset Nat) :
    (makeProjection m seeds selected).parentIdentity = m.identity ∧
    (makeProjection m seeds selected).parentRawSha256 = m.rawSha256 ∧
    (makeProjection m seeds selected).parentCanonicalSha256 = m.canonicalSha256 ∧
    (makeProjection m seeds selected).parentEnvelope = m.envelope ∧
    (makeProjection m seeds selected).invalidation = m.invalidation := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩

end AC
