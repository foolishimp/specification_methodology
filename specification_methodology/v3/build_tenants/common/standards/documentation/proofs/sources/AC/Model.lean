module
public import Mathlib.Data.Finset.Basic
public import Mathlib.Data.Finset.Card

/-!
A source-bound finite representation. `payload` and `envelope` contain complete
canonical JSON, not interpretations of prose predicates. Importing JSON and
extracting the declared dependency relation is an explicit boundary outside Lean.
-/
@[expose] public section

namespace AC

inductive Family where
  | objects | relations | constraints | latitude | residuals
  | traversals | transformations | judgments
  deriving DecidableEq, Repr

structure Record where
  key : Nat
  identity : String
  family : Family
  context : String
  owner : String
  scope : String
  basis : String
  payload : String
  deriving DecidableEq, Repr

inductive Target where
  | localRecord (key : Nat)
  | external (identity : String)
  deriving DecidableEq, Repr

inductive PathStep where
  | field (name : String)
  | index (position : Nat)
  deriving DecidableEq, Repr

structure Reference where
  owner : Nat
  path : List PathStep
  target : Target
  governing : Bool
  domain : String
  deriving DecidableEq, Repr

structure External where
  identity : String
  payload : String
  deriving DecidableEq, Repr

structure Model where
  identity : String
  rawSha256 : String
  canonicalSha256 : String
  envelope : String
  records : List Record
  references : List Reference
  externalResolutions : List External
  edges : List (Nat × Nat)
  invalidation : String
  deriving DecidableEq, Repr

def Model.localKeys (m : Model) : Finset Nat := (m.records.map Record.key).toFinset

def Model.dependencies (m : Model) (key : Nat) : Finset Nat :=
  (m.edges.filterMap fun e => if e.1 == key then some e.2 else none).toFinset

def Target.Resolves (keys : Finset Nat) (external : List String) : Target → Prop
  | .localRecord key => key ∈ keys
  | .external name => name ∈ external

instance (keys : Finset Nat) (external : List String) (target : Target) :
    Decidable (target.Resolves keys external) := by
  cases target <;> dsimp [Target.Resolves] <;> infer_instance

/-- This checks only the imported finite structural fragment, not schema meaning. -/
def Model.WellFormed (m : Model) : Prop :=
  (m.records.map Record.key).Nodup ∧
  (m.records.map Record.identity).Nodup ∧
  (m.externalResolutions.map External.identity).Nodup ∧
  (∀ r ∈ m.records, r.identity ∉ m.externalResolutions.map External.identity) ∧
  (∀ e ∈ m.edges, e.1 ∈ m.localKeys ∧ e.2 ∈ m.localKeys) ∧
  (∀ ref ∈ m.references, ref.owner ∈ m.localKeys ∧
    ref.target.Resolves m.localKeys (m.externalResolutions.map External.identity))

instance (m : Model) : Decidable m.WellFormed := by
  unfold Model.WellFormed
  infer_instance

def checkModel (m : Model) : Bool := decide m.WellFormed

theorem checkModel_sound (m : Model) (h : checkModel m = true) : m.WellFormed := by
  simpa [checkModel] using h

end AC
