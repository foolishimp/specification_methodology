module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData.RangeProbe
def seeds : Finset Nat := ([182, 278] : List Nat).toFinset
def trace : List Nat := [1122, 1124, 1125, 1215, 1217, 181, 183, 1867, 276, 277, 1121, 1123, 1126, 1220, 738, 1216, 1748, 184, 281, 1127, 1128, 739, 1219, 1221, 1749, 282, 740]
def included : Finset Nat := ([181, 182, 183, 184, 276, 277, 278, 281, 282, 738, 739, 740, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1215, 1216, 1217, 1219, 1220, 1221, 1748, 1749, 1867] : List Nat).toFinset
#eval (show IO Unit from do
 let out ← IO.getStdout
 out.putStrLn "BEGIN decomposed numeric bounds"
 out.flush)
theorem seed_nonempty : seeds.Nonempty := by decide +kernel
#print axioms seed_nonempty
theorem trace_set_exact : traceSet seeds trace = included := by decide +kernel
#print axioms trace_set_exact
theorem seeds_numeric : ∀ x ∈ seeds, x < 1987 := by decide +kernel
#print axioms seeds_numeric
theorem included_numeric : ∀ x ∈ included, x < 1987 := by decide +kernel
#print axioms included_numeric
theorem seeds_in_universe : seeds ⊆ Finset.range 1987 := by
 intro x member
 exact Finset.mem_range.mpr (seeds_numeric x member)
#print axioms seeds_in_universe
theorem trace_in_universe : traceSet seeds trace ⊆ Finset.range 1987 := by
 intro x member
 apply Finset.mem_range.mpr
 apply included_numeric x
 exact trace_set_exact ▸ member
#print axioms trace_in_universe
#eval (show IO Unit from do
 let out ← IO.getStdout
 out.putStrLn "PASS exact decomposed range premises; BEGIN original trace-range subset decision"
 out.flush)
theorem original_trace_subset : traceSet seeds trace ⊆ Finset.range 1987 := by decide +kernel
#print axioms original_trace_subset
#eval (show IO Unit from do
 let out ← IO.getStdout
 out.putStrLn "PASS original trace-range subset decision"
 out.flush)
end AC.GateData.RangeProbe
