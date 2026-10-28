module
public import AC.Fixture
public import AC.Toy

/-! Fixed expected propositions. A weaker theorem of the same name cannot fill
these contracts. Independent review still assesses their source correspondence. -/
public section
namespace AC.Contract

example (d : Dependencies) (keys seeds : Finset Nat) (trace : List Nat)
    (h : checkCertificate d keys seeds trace = true) (x : Nat) :
    x ∈ traceSet seeds trace ↔
      ∃ seed ∈ seeds, Relation.ReflTransGen (fun a b => b ∈ d a) seed x :=
  certificate_exact_reachability d keys seeds trace h x

example (d : Dependencies) (keys seeds : Finset Nat) (trace : List Nat)
    (h : checkCertificate d keys seeds trace = true)
    (s : Finset Nat) (hs : seeds ⊆ s) (closed : ∀ x ∈ s, ∀ y ∈ d x, y ∈ s) :
    traceSet seeds trace ⊆ s := certificate_least d keys seeds trace h s hs closed

example (d : Dependencies) (keys seeds : Finset Nat) (trace : List Nat)
    (h : checkCertificate d keys seeds trace = true) (x : Nat) :
    x ∈ traceSet seeds trace ↔
      x ∈ seeds ∨ ∃ parent ∈ traceSet seeds trace, x ∈ d parent :=
  certificate_fixed_point d keys seeds trace h x

example (m : Model) (seeds : Finset Nat) (trace : List Nat) (budget : Nat)
    (p : Projection) (h : project m seeds trace budget = .ok p) (x : Nat) :
    x ∈ p.included ↔ Reachable m.dependencies seeds x :=
  project_ok_exact_reachability m seeds trace budget p h x

example (m : Model) (seeds selected : Finset Nat) (r : Record) :
    r ∈ (makeProjection m seeds selected).records ↔ r ∈ m.records ∧ r.key ∈ selected :=
  projection_record_conservation m seeds selected r

example (m : Model) (seeds selected : Finset Nat) (r : Record)
    (h : r ∈ (makeProjection m seeds selected).records) :
    ∃ original ∈ m.records, original = r ∧ original.owner = r.owner ∧
      original.scope = r.scope ∧ original.context = r.context ∧ original.basis = r.basis ∧
      original.payload = r.payload := projection_authority_basis_conservation m seeds selected r h

example (m : Model) (seeds selected : Finset Nat) (r : Record)
    (hr : r ∈ m.records) (family : r.family = .residuals) :
    r ∈ (makeProjection m seeds selected).unresolved ∨
      r ∈ (makeProjection m seeds selected).excludedResiduals :=
  projection_all_residuals_accounted m seeds selected r hr family

example (m : Model) (seeds : Finset Nat) (trace : List Nat) (budget : Nat)
    (hm : checkModel m = true)
    (hc : checkCertificate m.dependencies m.localKeys seeds trace = true)
    (tooSmall : budget < (traceSet seeds trace).card) :
    project m seeds trace budget = .error "insufficient record budget; required closure is not truncated" :=
  insufficient_budget_refuses m seeds trace budget hm hc tooSmall

end AC.Contract

#print axioms AC.checkModel_sound
#print axioms AC.certificate_seed_inclusion
#print axioms AC.certificate_closed
#print axioms AC.certificate_exact_reachability
#print axioms AC.certificate_least
#print axioms AC.certificate_fixed_point
#print axioms AC.certificate_unique
#print axioms AC.project_ok_properties
#print axioms AC.project_ok_exact_reachability
#print axioms AC.insufficient_budget_refuses
#print axioms AC.projection_record_conservation
#print axioms AC.projection_authority_basis_conservation
#print axioms AC.projection_parent_conservation
#print axioms AC.projection_external_exact
#print axioms AC.projection_ordinary_exact
#print axioms AC.projection_residual_conservation
#print axioms AC.projection_excluded_residual_exact
#print axioms AC.projection_all_residuals_accounted
#print axioms AC.Fixture.model_checked
#print axioms AC.Fixture.checked0
#print axioms AC.Fixture.reachability0
#print axioms AC.Fixture.success0
#print axioms AC.Fixture.budget_refusal0
#print axioms AC.Fixture.checked1
#print axioms AC.Fixture.reachability1
#print axioms AC.Fixture.success1
#print axioms AC.Fixture.budget_refusal1
#print axioms AC.Fixture.checked2
#print axioms AC.Fixture.reachability2
#print axioms AC.Fixture.success2
#print axioms AC.Fixture.budget_refusal2
#print axioms AC.Fixture.checked3
#print axioms AC.Fixture.reachability3
#print axioms AC.Fixture.success3
#print axioms AC.Fixture.budget_refusal3
#print axioms AC.Fixture.checked4
#print axioms AC.Fixture.reachability4
#print axioms AC.Fixture.success4
#print axioms AC.Fixture.budget_refusal4
#print axioms AC.Fixture.checked5
#print axioms AC.Fixture.reachability5
#print axioms AC.Fixture.success5
#print axioms AC.Fixture.budget_refusal5
#print axioms AC.Fixture.checked6
#print axioms AC.Fixture.reachability6
#print axioms AC.Fixture.success6
#print axioms AC.Fixture.budget_refusal6
#print axioms AC.Fixture.checked7
#print axioms AC.Fixture.reachability7
#print axioms AC.Fixture.success7
#print axioms AC.Fixture.budget_refusal7
#print axioms AC.Fixture.checked8
#print axioms AC.Fixture.reachability8
#print axioms AC.Fixture.success8
#print axioms AC.Fixture.budget_refusal8
#print axioms AC.Fixture.checked9
#print axioms AC.Fixture.reachability9
#print axioms AC.Fixture.success9
#print axioms AC.Fixture.budget_refusal9
#print axioms AC.Fixture.checked10
#print axioms AC.Fixture.reachability10
#print axioms AC.Fixture.success10
#print axioms AC.Fixture.budget_refusal10
#print axioms AC.Fixture.checked11
#print axioms AC.Fixture.reachability11
#print axioms AC.Fixture.success11
#print axioms AC.Fixture.budget_refusal11
#print axioms AC.Fixture.checked12
#print axioms AC.Fixture.reachability12
#print axioms AC.Fixture.success12
#print axioms AC.Fixture.budget_refusal12
#print axioms AC.Fixture.checked13
#print axioms AC.Fixture.reachability13
#print axioms AC.Fixture.success13
#print axioms AC.Fixture.budget_refusal13
#print axioms AC.Fixture.checked14
#print axioms AC.Fixture.reachability14
#print axioms AC.Fixture.success14
#print axioms AC.Fixture.budget_refusal14
#print axioms AC.Fixture.checked15
#print axioms AC.Fixture.reachability15
#print axioms AC.Fixture.success15
#print axioms AC.Fixture.budget_refusal15
#print axioms AC.Fixture.checked16
#print axioms AC.Fixture.reachability16
#print axioms AC.Fixture.success16
#print axioms AC.Fixture.budget_refusal16
#print axioms AC.Fixture.checked17
#print axioms AC.Fixture.reachability17
#print axioms AC.Fixture.success17
#print axioms AC.Fixture.budget_refusal17
#print axioms AC.Fixture.checked18
#print axioms AC.Fixture.reachability18
#print axioms AC.Fixture.success18
#print axioms AC.Fixture.budget_refusal18
#print axioms AC.Fixture.checked19
#print axioms AC.Fixture.reachability19
#print axioms AC.Fixture.success19
#print axioms AC.Fixture.budget_refusal19
#print axioms AC.Fixture.checked20
#print axioms AC.Fixture.reachability20
#print axioms AC.Fixture.success20
#print axioms AC.Fixture.budget_refusal20
#print axioms AC.Fixture.checked21
#print axioms AC.Fixture.reachability21
#print axioms AC.Fixture.success21
#print axioms AC.Fixture.budget_refusal21
#print axioms AC.Fixture.checked22
#print axioms AC.Fixture.reachability22
#print axioms AC.Fixture.success22
#print axioms AC.Fixture.budget_refusal22
#print axioms AC.Fixture.checked23
#print axioms AC.Fixture.reachability23
#print axioms AC.Fixture.success23
#print axioms AC.Fixture.budget_refusal23
#print axioms AC.Fixture.checked24
#print axioms AC.Fixture.reachability24
#print axioms AC.Fixture.success24
#print axioms AC.Fixture.budget_refusal24
#print axioms AC.Fixture.checked25
#print axioms AC.Fixture.reachability25
#print axioms AC.Fixture.success25
#print axioms AC.Fixture.budget_refusal25
#print axioms AC.Fixture.checked26
#print axioms AC.Fixture.reachability26
#print axioms AC.Fixture.success26
#print axioms AC.Fixture.budget_refusal26
#print axioms AC.Fixture.checked27
#print axioms AC.Fixture.reachability27
#print axioms AC.Fixture.success27
#print axioms AC.Fixture.budget_refusal27
#print axioms AC.Fixture.checked28
#print axioms AC.Fixture.reachability28
#print axioms AC.Fixture.success28
#print axioms AC.Fixture.budget_refusal28
#print axioms AC.Fixture.checked29
#print axioms AC.Fixture.reachability29
#print axioms AC.Fixture.success29
#print axioms AC.Fixture.budget_refusal29
#print axioms AC.Fixture.checked30
#print axioms AC.Fixture.reachability30
#print axioms AC.Fixture.success30
#print axioms AC.Fixture.budget_refusal30
#print axioms AC.Fixture.checked31
#print axioms AC.Fixture.reachability31
#print axioms AC.Fixture.success31
#print axioms AC.Fixture.budget_refusal31

#print axioms AC.Toy.model_checked
#print axioms AC.Toy.checked0
#print axioms AC.Toy.reachability0
#print axioms AC.Toy.success0
#print axioms AC.Toy.budget_refusal0
#print axioms AC.Toy.checked1
#print axioms AC.Toy.reachability1
#print axioms AC.Toy.success1
#print axioms AC.Toy.budget_refusal1
#print axioms AC.Toy.checked2
#print axioms AC.Toy.reachability2
#print axioms AC.Toy.success2
#print axioms AC.Toy.budget_refusal2
#print axioms AC.Toy.checked3
#print axioms AC.Toy.reachability3
#print axioms AC.Toy.success3
#print axioms AC.Toy.budget_refusal3
#print axioms AC.Toy.checked4
#print axioms AC.Toy.reachability4
#print axioms AC.Toy.success4
#print axioms AC.Toy.budget_refusal4
#print axioms AC.Toy.checked5
#print axioms AC.Toy.reachability5
#print axioms AC.Toy.success5
#print axioms AC.Toy.budget_refusal5
#print axioms AC.Toy.checked6
#print axioms AC.Toy.reachability6
#print axioms AC.Toy.success6
#print axioms AC.Toy.budget_refusal6
#print axioms AC.Toy.checked7
#print axioms AC.Toy.reachability7
#print axioms AC.Toy.success7
#print axioms AC.Toy.budget_refusal7
#print axioms AC.Toy.checked8
#print axioms AC.Toy.reachability8
#print axioms AC.Toy.success8
#print axioms AC.Toy.budget_refusal8
#print axioms AC.Toy.checked9
#print axioms AC.Toy.reachability9
#print axioms AC.Toy.success9
#print axioms AC.Toy.budget_refusal9
#print axioms AC.Toy.checked10
#print axioms AC.Toy.reachability10
#print axioms AC.Toy.success10
#print axioms AC.Toy.budget_refusal10
#print axioms AC.Toy.checked11
#print axioms AC.Toy.reachability11
#print axioms AC.Toy.success11
#print axioms AC.Toy.budget_refusal11
#print axioms AC.Toy.checked12
#print axioms AC.Toy.reachability12
#print axioms AC.Toy.success12
#print axioms AC.Toy.budget_refusal12
#print axioms AC.Toy.checked13
#print axioms AC.Toy.reachability13
#print axioms AC.Toy.success13
#print axioms AC.Toy.budget_refusal13
