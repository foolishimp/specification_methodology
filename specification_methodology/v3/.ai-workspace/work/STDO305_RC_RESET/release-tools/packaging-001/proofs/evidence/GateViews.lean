module
public import GateModel
@[expose] public section
set_option maxRecDepth 100000
set_option maxHeartbeats 0
set_option debug.skipKernelTC false
namespace AC.GateData
def seeds0 : Finset Nat := ([671] : List Nat).toFinset
def trace0 : List Nat := [872, 1681, 1682, 1683, 1688, 1689, 1690, 661, 866, 1658, 662, 867, 1659, 1660, 1668, 663, 1664, 1665, 1666, 1882]
def included0 : Finset Nat := ([661, 662, 663, 671, 866, 867, 872, 1658, 1659, 1660, 1664, 1665, 1666, 1668, 1681, 1682, 1683, 1688, 1689, 1690, 1882] : List Nat).toFinset
theorem witness_edge0_0 : 872 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_1 : 1681 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_2 : 1682 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_3 : 1683 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_4 : 1688 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_5 : 1689 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_6 : 1690 ∈ model.dependencies 671 := by decide +kernel
theorem witness_edge0_7 : 661 ∈ model.dependencies 872 := by decide +kernel
theorem witness_edge0_8 : 866 ∈ model.dependencies 661 := by decide +kernel
theorem witness_edge0_9 : 1658 ∈ model.dependencies 661 := by decide +kernel
theorem witness_edge0_10 : 662 ∈ model.dependencies 866 := by decide +kernel
theorem witness_edge0_11 : 867 ∈ model.dependencies 662 := by decide +kernel
theorem witness_edge0_12 : 1659 ∈ model.dependencies 662 := by decide +kernel
theorem witness_edge0_13 : 1660 ∈ model.dependencies 662 := by decide +kernel
theorem witness_edge0_14 : 1668 ∈ model.dependencies 662 := by decide +kernel
theorem witness_edge0_15 : 663 ∈ model.dependencies 867 := by decide +kernel
theorem witness_edge0_16 : 1664 ∈ model.dependencies 663 := by decide +kernel
theorem witness_edge0_17 : 1665 ∈ model.dependencies 663 := by decide +kernel
theorem witness_edge0_18 : 1666 ∈ model.dependencies 663 := by decide +kernel
theorem witness_edge0_19 : 1882 ∈ model.dependencies 663 := by decide +kernel
theorem witness0 : Witness model.dependencies seeds0 trace0 := by
 exact
  ⟨⟨671, by decide +kernel, witness_edge0_0⟩,
   ⟨⟨671, by decide +kernel, witness_edge0_1⟩,
    ⟨⟨671, by decide +kernel, witness_edge0_2⟩,
     ⟨⟨671, by decide +kernel, witness_edge0_3⟩,
      ⟨⟨671, by decide +kernel, witness_edge0_4⟩,
       ⟨⟨671, by decide +kernel, witness_edge0_5⟩,
        ⟨⟨671, by decide +kernel, witness_edge0_6⟩,
         ⟨⟨872, by decide +kernel, witness_edge0_7⟩,
          ⟨⟨661, by decide +kernel, witness_edge0_8⟩,
           ⟨⟨661, by decide +kernel, witness_edge0_9⟩,
            ⟨⟨866, by decide +kernel, witness_edge0_10⟩,
             ⟨⟨662, by decide +kernel, witness_edge0_11⟩,
              ⟨⟨662, by decide +kernel, witness_edge0_12⟩,
               ⟨⟨662, by decide +kernel, witness_edge0_13⟩,
                ⟨⟨662, by decide +kernel, witness_edge0_14⟩,
                 ⟨⟨867, by decide +kernel, witness_edge0_15⟩,
                  ⟨⟨663, by decide +kernel, witness_edge0_16⟩,
                   ⟨⟨663, by decide +kernel, witness_edge0_17⟩,
                    ⟨⟨663, by decide +kernel, witness_edge0_18⟩,
                     ⟨⟨663, by decide +kernel, witness_edge0_19⟩,
                      True.intro⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩
theorem seed_nonempty0 : seeds0.Nonempty := by decide +kernel
theorem seed_universe0 : seeds0 ⊆ Finset.range 1885 := by decide +kernel
theorem trace_universe0 : traceSet seeds0 trace0 ⊆ Finset.range 1885 := by decide +kernel
theorem closed0 : Closed model.dependencies (traceSet seeds0 trace0) := by decide +kernel
theorem checked0 : checkCertificate model.dependencies model.localKeys seeds0 trace0 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty0, seed_universe0, trace_universe0, witness0, closed0⟩
theorem set0 : traceSet seeds0 trace0 = included0 := by decide +kernel
theorem reachability0 (x : Nat) : x ∈ included0 ↔ Reachable model.dependencies seeds0 x := by
 rw [← set0]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds0 trace0 checked0 x
theorem result0 : project model seeds0 trace0 21 = .ok (makeProjection model seeds0 included0) := by
 rw [← set0]
 exact projection_success model seeds0 trace0 21 model_checked checked0 (by decide +kernel)
def execution0 : Except String Projection := projectWithProof model seeds0 trace0 21 model_checked checked0
theorem execution_matches_project0 : execution0 = project model seeds0 trace0 21 :=
 projectWithProof_eq_project model seeds0 trace0 21 model_checked checked0
#print axioms checked0
#print axioms set0
#print axioms reachability0
#print axioms result0
#print axioms execution_matches_project0
def seeds1 : Finset Nat := ([635] : List Nat).toFinset
def trace1 : List Nat := [860, 1628, 1629, 1706, 1718, 637, 638, 639, 681, 1631, 1879, 1632, 1633, 1634, 1717, 1884]
def included1 : Finset Nat := ([635, 637, 638, 639, 681, 860, 1628, 1629, 1631, 1632, 1633, 1634, 1706, 1717, 1718, 1879, 1884] : List Nat).toFinset
theorem witness_edge1_0 : 860 ∈ model.dependencies 635 := by decide +kernel
theorem witness_edge1_1 : 1628 ∈ model.dependencies 635 := by decide +kernel
theorem witness_edge1_2 : 1629 ∈ model.dependencies 635 := by decide +kernel
theorem witness_edge1_3 : 1706 ∈ model.dependencies 635 := by decide +kernel
theorem witness_edge1_4 : 1718 ∈ model.dependencies 635 := by decide +kernel
theorem witness_edge1_5 : 637 ∈ model.dependencies 860 := by decide +kernel
theorem witness_edge1_6 : 638 ∈ model.dependencies 1706 := by decide +kernel
theorem witness_edge1_7 : 639 ∈ model.dependencies 1706 := by decide +kernel
theorem witness_edge1_8 : 681 ∈ model.dependencies 1718 := by decide +kernel
theorem witness_edge1_9 : 1631 ∈ model.dependencies 637 := by decide +kernel
theorem witness_edge1_10 : 1879 ∈ model.dependencies 637 := by decide +kernel
theorem witness_edge1_11 : 1632 ∈ model.dependencies 638 := by decide +kernel
theorem witness_edge1_12 : 1633 ∈ model.dependencies 639 := by decide +kernel
theorem witness_edge1_13 : 1634 ∈ model.dependencies 639 := by decide +kernel
theorem witness_edge1_14 : 1717 ∈ model.dependencies 681 := by decide +kernel
theorem witness_edge1_15 : 1884 ∈ model.dependencies 681 := by decide +kernel
theorem witness1 : Witness model.dependencies seeds1 trace1 := by
 exact
  ⟨⟨635, by decide +kernel, witness_edge1_0⟩,
   ⟨⟨635, by decide +kernel, witness_edge1_1⟩,
    ⟨⟨635, by decide +kernel, witness_edge1_2⟩,
     ⟨⟨635, by decide +kernel, witness_edge1_3⟩,
      ⟨⟨635, by decide +kernel, witness_edge1_4⟩,
       ⟨⟨860, by decide +kernel, witness_edge1_5⟩,
        ⟨⟨1706, by decide +kernel, witness_edge1_6⟩,
         ⟨⟨1706, by decide +kernel, witness_edge1_7⟩,
          ⟨⟨1718, by decide +kernel, witness_edge1_8⟩,
           ⟨⟨637, by decide +kernel, witness_edge1_9⟩,
            ⟨⟨637, by decide +kernel, witness_edge1_10⟩,
             ⟨⟨638, by decide +kernel, witness_edge1_11⟩,
              ⟨⟨639, by decide +kernel, witness_edge1_12⟩,
               ⟨⟨639, by decide +kernel, witness_edge1_13⟩,
                ⟨⟨681, by decide +kernel, witness_edge1_14⟩,
                 ⟨⟨681, by decide +kernel, witness_edge1_15⟩,
                  True.intro⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩
theorem seed_nonempty1 : seeds1.Nonempty := by decide +kernel
theorem seed_universe1 : seeds1 ⊆ Finset.range 1885 := by decide +kernel
theorem trace_universe1 : traceSet seeds1 trace1 ⊆ Finset.range 1885 := by decide +kernel
theorem closed1 : Closed model.dependencies (traceSet seeds1 trace1) := by decide +kernel
theorem checked1 : checkCertificate model.dependencies model.localKeys seeds1 trace1 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty1, seed_universe1, trace_universe1, witness1, closed1⟩
theorem set1 : traceSet seeds1 trace1 = included1 := by decide +kernel
theorem reachability1 (x : Nat) : x ∈ included1 ↔ Reachable model.dependencies seeds1 x := by
 rw [← set1]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds1 trace1 checked1 x
theorem result1 : project model seeds1 trace1 17 = .ok (makeProjection model seeds1 included1) := by
 rw [← set1]
 exact projection_success model seeds1 trace1 17 model_checked checked1 (by decide +kernel)
def execution1 : Except String Projection := projectWithProof model seeds1 trace1 17 model_checked checked1
theorem execution_matches_project1 : execution1 = project model seeds1 trace1 17 :=
 projectWithProof_eq_project model seeds1 trace1 17 model_checked checked1
#print axioms checked1
#print axioms set1
#print axioms reachability1
#print axioms result1
#print axioms execution_matches_project1
def seeds2 : Finset Nat := ([641] : List Nat).toFinset
def trace2 : List Nat := [861, 1641, 1707, 1880, 644, 862, 1637, 1638, 645, 1639]
def included2 : Finset Nat := ([641, 644, 645, 861, 862, 1637, 1638, 1639, 1641, 1707, 1880] : List Nat).toFinset
theorem witness_edge2_0 : 861 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge2_1 : 1641 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge2_2 : 1707 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge2_3 : 1880 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge2_4 : 644 ∈ model.dependencies 861 := by decide +kernel
theorem witness_edge2_5 : 862 ∈ model.dependencies 644 := by decide +kernel
theorem witness_edge2_6 : 1637 ∈ model.dependencies 644 := by decide +kernel
theorem witness_edge2_7 : 1638 ∈ model.dependencies 644 := by decide +kernel
theorem witness_edge2_8 : 645 ∈ model.dependencies 862 := by decide +kernel
theorem witness_edge2_9 : 1639 ∈ model.dependencies 645 := by decide +kernel
theorem witness2 : Witness model.dependencies seeds2 trace2 := by
 exact
  ⟨⟨641, by decide +kernel, witness_edge2_0⟩,
   ⟨⟨641, by decide +kernel, witness_edge2_1⟩,
    ⟨⟨641, by decide +kernel, witness_edge2_2⟩,
     ⟨⟨641, by decide +kernel, witness_edge2_3⟩,
      ⟨⟨861, by decide +kernel, witness_edge2_4⟩,
       ⟨⟨644, by decide +kernel, witness_edge2_5⟩,
        ⟨⟨644, by decide +kernel, witness_edge2_6⟩,
         ⟨⟨644, by decide +kernel, witness_edge2_7⟩,
          ⟨⟨862, by decide +kernel, witness_edge2_8⟩,
           ⟨⟨645, by decide +kernel, witness_edge2_9⟩,
            True.intro⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩
theorem seed_nonempty2 : seeds2.Nonempty := by decide +kernel
theorem seed_universe2 : seeds2 ⊆ Finset.range 1885 := by decide +kernel
theorem trace_universe2 : traceSet seeds2 trace2 ⊆ Finset.range 1885 := by decide +kernel
theorem closed2 : Closed model.dependencies (traceSet seeds2 trace2) := by decide +kernel
theorem checked2 : checkCertificate model.dependencies model.localKeys seeds2 trace2 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty2, seed_universe2, trace_universe2, witness2, closed2⟩
theorem set2 : traceSet seeds2 trace2 = included2 := by decide +kernel
theorem reachability2 (x : Nat) : x ∈ included2 ↔ Reachable model.dependencies seeds2 x := by
 rw [← set2]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds2 trace2 checked2 x
theorem result2 : project model seeds2 trace2 11 = .ok (makeProjection model seeds2 included2) := by
 rw [← set2]
 exact projection_success model seeds2 trace2 11 model_checked checked2 (by decide +kernel)
def execution2 : Except String Projection := projectWithProof model seeds2 trace2 11 model_checked checked2
theorem execution_matches_project2 : execution2 = project model seeds2 trace2 11 :=
 projectWithProof_eq_project model seeds2 trace2 11 model_checked checked2
#print axioms checked2
#print axioms set2
#print axioms reachability2
#print axioms result2
#print axioms execution_matches_project2
def seeds3 : Finset Nat := ([651] : List Nat).toFinset
def trace3 : List Nat := [863, 1646, 649, 1644]
def included3 : Finset Nat := ([649, 651, 863, 1644, 1646] : List Nat).toFinset
theorem witness_edge3_0 : 863 ∈ model.dependencies 651 := by decide +kernel
theorem witness_edge3_1 : 1646 ∈ model.dependencies 651 := by decide +kernel
theorem witness_edge3_2 : 649 ∈ model.dependencies 863 := by decide +kernel
theorem witness_edge3_3 : 1644 ∈ model.dependencies 649 := by decide +kernel
theorem witness3 : Witness model.dependencies seeds3 trace3 := by
 exact
  ⟨⟨651, by decide +kernel, witness_edge3_0⟩,
   ⟨⟨651, by decide +kernel, witness_edge3_1⟩,
    ⟨⟨863, by decide +kernel, witness_edge3_2⟩,
     ⟨⟨649, by decide +kernel, witness_edge3_3⟩,
      True.intro⟩⟩⟩⟩
theorem seed_nonempty3 : seeds3.Nonempty := by decide +kernel
theorem seed_universe3 : seeds3 ⊆ Finset.range 1885 := by decide +kernel
theorem trace_universe3 : traceSet seeds3 trace3 ⊆ Finset.range 1885 := by decide +kernel
theorem closed3 : Closed model.dependencies (traceSet seeds3 trace3) := by decide +kernel
theorem checked3 : checkCertificate model.dependencies model.localKeys seeds3 trace3 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty3, seed_universe3, trace_universe3, witness3, closed3⟩
theorem set3 : traceSet seeds3 trace3 = included3 := by decide +kernel
theorem reachability3 (x : Nat) : x ∈ included3 ↔ Reachable model.dependencies seeds3 x := by
 rw [← set3]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds3 trace3 checked3 x
theorem result3 : project model seeds3 trace3 5 = .ok (makeProjection model seeds3 included3) := by
 rw [← set3]
 exact projection_success model seeds3 trace3 5 model_checked checked3 (by decide +kernel)
def execution3 : Except String Projection := projectWithProof model seeds3 trace3 5 model_checked checked3
theorem execution_matches_project3 : execution3 = project model seeds3 trace3 5 :=
 projectWithProof_eq_project model seeds3 trace3 5 model_checked checked3
#print axioms checked3
#print axioms set3
#print axioms reachability3
#print axioms result3
#print axioms execution_matches_project3
def seeds4 : Finset Nat := ([656] : List Nat).toFinset
def trace4 : List Nat := [864, 1653, 1654, 641, 861, 1641, 1707, 1880, 644, 862, 1637, 1638, 645, 1639]
def included4 : Finset Nat := ([641, 644, 645, 656, 861, 862, 864, 1637, 1638, 1639, 1641, 1653, 1654, 1707, 1880] : List Nat).toFinset
theorem witness_edge4_0 : 864 ∈ model.dependencies 656 := by decide +kernel
theorem witness_edge4_1 : 1653 ∈ model.dependencies 656 := by decide +kernel
theorem witness_edge4_2 : 1654 ∈ model.dependencies 656 := by decide +kernel
theorem witness_edge4_3 : 641 ∈ model.dependencies 864 := by decide +kernel
theorem witness_edge4_4 : 861 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge4_5 : 1641 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge4_6 : 1707 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge4_7 : 1880 ∈ model.dependencies 641 := by decide +kernel
theorem witness_edge4_8 : 644 ∈ model.dependencies 861 := by decide +kernel
theorem witness_edge4_9 : 862 ∈ model.dependencies 644 := by decide +kernel
theorem witness_edge4_10 : 1637 ∈ model.dependencies 644 := by decide +kernel
theorem witness_edge4_11 : 1638 ∈ model.dependencies 644 := by decide +kernel
theorem witness_edge4_12 : 645 ∈ model.dependencies 862 := by decide +kernel
theorem witness_edge4_13 : 1639 ∈ model.dependencies 645 := by decide +kernel
theorem witness4 : Witness model.dependencies seeds4 trace4 := by
 exact
  ⟨⟨656, by decide +kernel, witness_edge4_0⟩,
   ⟨⟨656, by decide +kernel, witness_edge4_1⟩,
    ⟨⟨656, by decide +kernel, witness_edge4_2⟩,
     ⟨⟨864, by decide +kernel, witness_edge4_3⟩,
      ⟨⟨641, by decide +kernel, witness_edge4_4⟩,
       ⟨⟨641, by decide +kernel, witness_edge4_5⟩,
        ⟨⟨641, by decide +kernel, witness_edge4_6⟩,
         ⟨⟨641, by decide +kernel, witness_edge4_7⟩,
          ⟨⟨861, by decide +kernel, witness_edge4_8⟩,
           ⟨⟨644, by decide +kernel, witness_edge4_9⟩,
            ⟨⟨644, by decide +kernel, witness_edge4_10⟩,
             ⟨⟨644, by decide +kernel, witness_edge4_11⟩,
              ⟨⟨862, by decide +kernel, witness_edge4_12⟩,
               ⟨⟨645, by decide +kernel, witness_edge4_13⟩,
                True.intro⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩⟩
theorem seed_nonempty4 : seeds4.Nonempty := by decide +kernel
theorem seed_universe4 : seeds4 ⊆ Finset.range 1885 := by decide +kernel
theorem trace_universe4 : traceSet seeds4 trace4 ⊆ Finset.range 1885 := by decide +kernel
theorem closed4 : Closed model.dependencies (traceSet seeds4 trace4) := by decide +kernel
theorem checked4 : checkCertificate model.dependencies model.localKeys seeds4 trace4 = true := by
 rw [localKeys_range model _ keys_exact]
 exact decide_eq_true ⟨seed_nonempty4, seed_universe4, trace_universe4, witness4, closed4⟩
theorem set4 : traceSet seeds4 trace4 = included4 := by decide +kernel
theorem reachability4 (x : Nat) : x ∈ included4 ↔ Reachable model.dependencies seeds4 x := by
 rw [← set4]
 exact certificate_exact_reachability model.dependencies model.localKeys seeds4 trace4 checked4 x
theorem result4 : project model seeds4 trace4 15 = .ok (makeProjection model seeds4 included4) := by
 rw [← set4]
 exact projection_success model seeds4 trace4 15 model_checked checked4 (by decide +kernel)
def execution4 : Except String Projection := projectWithProof model seeds4 trace4 15 model_checked checked4
theorem execution_matches_project4 : execution4 = project model seeds4 trace4 15 :=
 projectWithProof_eq_project model seeds4 trace4 15 model_checked checked4
#print axioms checked4
#print axioms set4
#print axioms reachability4
#print axioms result4
#print axioms execution_matches_project4
def selections : List (Finset Nat × List Nat × Nat) := [(seeds0,trace0,21), (seeds1,trace1,17), (seeds2,trace2,11), (seeds3,trace3,5), (seeds4,trace4,15)]
def executions : List (Except String Projection) := [execution0, execution1, execution2, execution3, execution4]
end AC.GateData
