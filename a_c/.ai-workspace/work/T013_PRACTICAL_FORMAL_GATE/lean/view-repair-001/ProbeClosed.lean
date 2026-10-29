module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData.ClosedProbe
def seeds : Finset Nat := ([182, 278] : List Nat).toFinset
def trace : List Nat := [1122, 1124, 1125, 1215, 1217, 181, 183, 1867, 276, 277, 1121, 1123, 1126, 1220, 738, 1216, 1748, 184, 281, 1127, 1128, 739, 1219, 1221, 1749, 282, 740]
def included : Finset Nat := ([181, 182, 183, 184, 276, 277, 278, 281, 282, 738, 739, 740, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1215, 1216, 1217, 1219, 1220, 1221, 1748, 1749, 1867] : List Nat).toFinset
#eval do
 let out ← IO.getStdout
 out.putStrLn "BEGIN original Closed decision"
 out.flush
theorem closed_checked : Closed model.dependencies (traceSet seeds trace) := by decide +kernel
#print axioms closed_checked
#eval do
 let out ← IO.getStdout
 out.putStrLn "PASS Closed"
 out.flush
end AC.GateData.ClosedProbe
