module
import GateViews
meta import GateViews
import AC.GateRuntime
meta import AC.GateRuntime
public import Lean.Data.Json.Basic
public section
def main : IO UInt32 := do
 let m := AC.GateData.model
 IO.println (Lean.Json.mkObj [("raw", Lean.Json.str m.rawSha256), ("records", Lean.toJson m.records.length), ("references", Lean.toJson m.references.length), ("externals", Lean.toJson m.externalResolutions.length), ("edges", Lean.toJson m.edges.length)]).compress
 return 0
