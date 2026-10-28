module
public import AC.Projection
public import AC.Structure
public import Lean.Data.Json.Basic
@[expose] public section
namespace AC.GateRuntime
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


def modelJson (m : Model) : Json := Json.mkObj [
  ("identity", toJson m.identity), ("rawSha256", toJson m.rawSha256),
  ("canonicalSha256", toJson m.canonicalSha256), ("envelope", toJson m.envelope),
  ("records", Json.arr (m.records.map recordJson).toArray),
  ("references", Json.arr (m.references.map referenceJson).toArray),
  ("externalResolutions", Json.arr (m.externalResolutions.map externalJson).toArray),
  ("edges", toJson (m.edges.map fun e => [e.1, e.2])), ("invalidation", toJson m.invalidation)]

def gateSelectionJson (m : Model) (s : Finset Nat × List Nat × Nat) : Json :=
  let (seeds, trace, budget) := s
  match project m seeds trace budget with
  | .ok p => Json.mkObj [("status", toJson "verified"), ("projection", projectionJson m p)]
  | .error reason => Json.mkObj [("status", toJson "refused"), ("reason", toJson reason)]

end AC.GateRuntime
