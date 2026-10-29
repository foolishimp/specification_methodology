module
import GateViews
meta import GateViews
import AC.GateRuntime
meta import AC.GateRuntime
public import Lean.Data.Json.Basic
public section
def main : IO UInt32 := do
 IO.println (AC.checkModel AC.GateData.model)
 return 0
