module
import GateData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
#check List.IsChain
#check List.isChain_iff_pairwise
#check List.IsChain.pairwise
#check List.nodup_mergeSort
#check List.Nodup.of_map
#check List.mem_range
#check List.Perm.nodup_iff
#check String.lt_trans
#check List.pairwise_cons
#check List.isChain_cons_cons
#check List.Nodup.range
 theorem keys_exact : model.records.map Record.key = List.range 1987 := by rfl
end AC.GateData
