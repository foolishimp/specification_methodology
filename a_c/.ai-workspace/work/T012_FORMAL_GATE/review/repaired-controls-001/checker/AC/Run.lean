module
public import AC.Fixture
public import AC.Toy
meta import AC.Fixture
meta import AC.Toy
public import Lean.Data.Json.Basic

@[expose] public section
namespace AC
open Lean

def familyName : Family → String
  | .objects => "objects"
  | .relations => "relations"
  | .constraints => "constraints"
  | .latitude => "latitude"
  | .residuals => "residuals"
  | .traversals => "traversals"
  | .transformations => "transformations"
  | .judgments => "judgments"

def recordJson (r : Record) : Json := Json.mkObj [
  ("key", toJson r.key), ("identity", toJson r.identity), ("family", toJson (familyName r.family)),
  ("context", toJson r.context), ("owner", toJson r.owner), ("scope", toJson r.scope),
  ("basis", toJson r.basis), ("payload", toJson r.payload)]

def pathStepJson : PathStep → Json
  | .field name => Json.mkObj [("field", toJson name)]
  | .index position => Json.mkObj [("index", toJson position)]

def referenceJson (r : Reference) : Json := Json.mkObj [
  ("owner", toJson r.owner), ("path", Json.arr (r.path.map pathStepJson).toArray),
  ("target", match r.target with
    | .localRecord key => Json.mkObj [("local", toJson key)]
    | .external identity => Json.mkObj [("external", toJson identity)]),
  ("governing", toJson r.governing), ("domain", toJson r.domain)]

def externalJson (e : External) : Json := Json.mkObj [
  ("identity", toJson e.identity), ("payload", toJson e.payload)]

/-- Output ordering follows the source record indices; canonical payload bytes
    are emitted directly rather than being reparsed and normalized in Lean. -/
def keysJson (m : Model) (keys : Finset Nat) : Json :=
  toJson ((m.records.map Record.key).filter fun key => decide (key ∈ keys))

def projectionJson (m : Model) (p : Projection) : Json := Json.mkObj [
  ("parentIdentity", toJson p.parentIdentity), ("parentRawSha256", toJson p.parentRawSha256),
  ("parentCanonicalSha256", toJson p.parentCanonicalSha256), ("parentEnvelope", toJson p.parentEnvelope),
  ("seeds", keysJson m p.seeds), ("included", keysJson m p.included), ("excluded", keysJson m p.excluded),
  ("records", Json.arr (p.records.map recordJson).toArray),
  ("external", Json.arr (p.external.map externalJson).toArray),
  ("ordinary", Json.arr (p.ordinary.map referenceJson).toArray),
  ("unresolved", Json.arr (p.unresolved.map recordJson).toArray),
  ("excludedResiduals", Json.arr (p.excludedResiduals.map recordJson).toArray),
  ("invalidation", toJson p.invalidation)]

def runSelection (m : Model) (selection : Finset Nat × List Nat × Nat) : Except String Json := do
  let (seeds, trace, budget) := selection
  let projection ← project m seeds trace budget
  match project m seeds trace (budget - 1) with
  | .ok _ => .error "underbudget operation unexpectedly succeeded"
  | .error reason =>
    if reason != "insufficient record budget; required closure is not truncated" then
      .error reason
    else .ok (Json.mkObj [("budget", toJson budget),
      ("underbudgetRefusal", toJson reason), ("projection", projectionJson m projection)])

end AC

def main : IO UInt32 := do
  let computed : Except String Lean.Json := do
    let mainFixture ← AC.Fixture.selections.mapM (AC.runSelection AC.Fixture.model)
    let toyFixture ← AC.Toy.selections.mapM (AC.runSelection AC.Toy.model)
    pure (Lean.Json.mkObj [("stdo302", Lean.Json.arr mainFixture.toArray),
      ("toy", Lean.Json.arr toyFixture.toArray)])
  match computed with
  | .error reason =>
    IO.eprintln reason
    return 2
  | .ok results =>
    IO.println (Lean.Json.compress results)
    return 0
