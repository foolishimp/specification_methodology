module
public import Mathlib.Data.Finset.Basic
public import Mathlib.Logic.Relation

/-!
An untrusted producer supplies a finite discovery trace. The checker verifies
that each new member has a declared edge from an already reached member and
that the resulting finite set is closed. It does not trust a claimed closure.
-/
@[expose] public section

namespace AC

abbrev Dependencies := Nat → Finset Nat

def Reachable (d : Dependencies) (seeds : Finset Nat) (x : Nat) : Prop :=
  ∃ seed ∈ seeds, Relation.ReflTransGen (fun a b => b ∈ d a) seed x

def Closed (d : Dependencies) (s : Finset Nat) : Prop :=
  ∀ x ∈ s, ∀ y ∈ d x, y ∈ s

instance (d : Dependencies) (s : Finset Nat) : Decidable (Closed d s) := by
  unfold Closed
  infer_instance

def traceSet (known : Finset Nat) : List Nat → Finset Nat
  | [] => known
  | x :: rest => traceSet (insert x known) rest

def Witness (d : Dependencies) (known : Finset Nat) : List Nat → Prop
  | [] => True
  | x :: rest => (∃ parent ∈ known, x ∈ d parent) ∧ Witness d (insert x known) rest

instance witnessDecidable (d : Dependencies) (known : Finset Nat) (trace : List Nat) :
    Decidable (Witness d known trace) := by
  induction trace generalizing known with
  | nil => exact isTrue trivial
  | cons x rest ih =>
    dsimp [Witness]
    haveI := ih (insert x known)
    infer_instance

/-- All checks range over finite data. Reachability is established by `Witness`,
    not given to the verifier as a premise or an axiom. -/
def CertificateValid (d : Dependencies) (universeKeys seeds : Finset Nat) (trace : List Nat) : Prop :=
  seeds.Nonempty ∧ seeds ⊆ universeKeys ∧ traceSet seeds trace ⊆ universeKeys ∧
  Witness d seeds trace ∧ Closed d (traceSet seeds trace)

instance (d : Dependencies) (universeKeys seeds : Finset Nat) (trace : List Nat) :
    Decidable (CertificateValid d universeKeys seeds trace) := by
  unfold CertificateValid
  infer_instance

def checkCertificate (d : Dependencies) (universeKeys seeds : Finset Nat) (trace : List Nat) : Bool :=
  decide (CertificateValid d universeKeys seeds trace)

theorem checkCertificate_valid (d : Dependencies) (universeKeys seeds : Finset Nat)
    (trace : List Nat) (h : checkCertificate d universeKeys seeds trace = true) :
    CertificateValid d universeKeys seeds trace := by
  simpa [checkCertificate] using h

theorem seed_reachable (d : Dependencies) (seeds : Finset Nat) {x : Nat}
    (h : x ∈ seeds) : Reachable d seeds x := ⟨x, h, .refl⟩

theorem reachable_step (d : Dependencies) (seeds : Finset Nat) {x y : Nat}
    (h : Reachable d seeds x) (edge : y ∈ d x) : Reachable d seeds y := by
  rcases h with ⟨seed, member, path⟩
  exact ⟨seed, member, path.tail edge⟩

theorem known_subset_traceSet (known : Finset Nat) (trace : List Nat) :
    known ⊆ traceSet known trace := by
  induction trace generalizing known with
  | nil => exact Finset.Subset.refl _
  | cons x rest ih =>
    exact Finset.Subset.trans (Finset.subset_insert x known) (ih (insert x known))

theorem witness_reachable (d : Dependencies) (seeds known : Finset Nat) (trace : List Nat)
    (base : ∀ x ∈ known, Reachable d seeds x) (witness : Witness d known trace) :
    ∀ x ∈ traceSet known trace, Reachable d seeds x := by
  induction trace generalizing known with
  | nil => exact base
  | cons x rest ih =>
    rcases witness with ⟨⟨parent, hp, edge⟩, tail⟩
    apply ih (insert x known) _ tail
    intro y hy
    rcases Finset.mem_insert.mp hy with equal | old
    · subst y
      exact reachable_step d seeds (base parent hp) edge
    · exact base y old

theorem reachable_in_closed (d : Dependencies) (seeds s : Finset Nat)
    (includeSeeds : seeds ⊆ s) (closed : Closed d s) {x : Nat}
    (h : Reachable d seeds x) : x ∈ s := by
  rcases h with ⟨seed, member, path⟩
  induction path with
  | refl => exact includeSeeds member
  | @tail b c path edge ih => exact closed b ih c edge

/-- Exact semantic connection to Mathlib's reflexive-transitive closure. -/
theorem certificate_exact_reachability (d : Dependencies) (universeKeys seeds : Finset Nat)
    (trace : List Nat) (checked : checkCertificate d universeKeys seeds trace = true) (x : Nat) :
    x ∈ traceSet seeds trace ↔ Reachable d seeds x := by
  have valid := checkCertificate_valid d universeKeys seeds trace checked
  constructor
  · exact witness_reachable d seeds seeds trace (fun _ h => seed_reachable d seeds h) valid.2.2.2.1 x
  · exact reachable_in_closed d seeds (traceSet seeds trace)
      (known_subset_traceSet seeds trace) valid.2.2.2.2

theorem certificate_seed_inclusion (d : Dependencies) (universeKeys seeds : Finset Nat)
    (trace : List Nat) (_checked : checkCertificate d universeKeys seeds trace = true) :
    seeds ⊆ traceSet seeds trace := known_subset_traceSet seeds trace

theorem certificate_closed (d : Dependencies) (universeKeys seeds : Finset Nat)
    (trace : List Nat) (checked : checkCertificate d universeKeys seeds trace = true) :
    Closed d (traceSet seeds trace) :=
  (checkCertificate_valid d universeKeys seeds trace checked).2.2.2.2

theorem certificate_least (d : Dependencies) (universeKeys seeds : Finset Nat)
    (trace : List Nat) (checked : checkCertificate d universeKeys seeds trace = true)
    (candidate : Finset Nat) (includeSeeds : seeds ⊆ candidate) (closed : Closed d candidate) :
    traceSet seeds trace ⊆ candidate := by
  intro x member
  exact reachable_in_closed d seeds candidate includeSeeds closed
    ((certificate_exact_reachability d universeKeys seeds trace checked x).mp member)

/-- The accepted finite result is a fixed point of Q ↦ seeds ∪ required(Q). -/
theorem certificate_fixed_point (d : Dependencies) (universeKeys seeds : Finset Nat)
    (trace : List Nat) (checked : checkCertificate d universeKeys seeds trace = true) (x : Nat) :
    x ∈ traceSet seeds trace ↔
      x ∈ seeds ∨ ∃ parent ∈ traceSet seeds trace, x ∈ d parent := by
  constructor
  · intro member
    rcases (certificate_exact_reachability d universeKeys seeds trace checked x).mp member with
      ⟨seed, seedMember, path⟩
    rcases path.cases_tail with same | ⟨parent, initialPath, edge⟩
    · exact Or.inl (by simpa only [same] using seedMember)
    · exact Or.inr ⟨parent,
        (certificate_exact_reachability d universeKeys seeds trace checked parent).mpr
          ⟨seed, seedMember, initialPath⟩, edge⟩
  · intro member
    rcases member with seedMember | ⟨parent, parentMember, edge⟩
    · exact known_subset_traceSet seeds trace seedMember
    · exact certificate_closed d universeKeys seeds trace checked parent parentMember x edge

/-- Two successful certificates for exact same inputs cannot choose different sets. -/
theorem certificate_unique (d : Dependencies) (universeKeys seeds : Finset Nat)
    (left right : List Nat)
    (hl : checkCertificate d universeKeys seeds left = true)
    (hr : checkCertificate d universeKeys seeds right = true) :
    traceSet seeds left = traceSet seeds right := by
  apply Finset.ext
  intro x
  rw [certificate_exact_reachability d universeKeys seeds left hl,
      certificate_exact_reachability d universeKeys seeds right hr]

end AC
