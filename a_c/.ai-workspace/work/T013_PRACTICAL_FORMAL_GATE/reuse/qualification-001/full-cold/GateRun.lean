module
import GateViews
meta import GateViews
import AC.GateRuntime
meta import AC.GateRuntime
public import Lean.Data.Json.Basic
public section
def main : IO UInt32 := do
 let m := AC.GateData.model
 let result := Lean.Json.mkObj [("model", AC.GateRuntime.modelJson m),
   ("views", Lean.Json.arr (AC.GateData.executions.map (AC.GateRuntime.selectionResultJson m)).toArray)]
 IO.println result.compress
 return 0
