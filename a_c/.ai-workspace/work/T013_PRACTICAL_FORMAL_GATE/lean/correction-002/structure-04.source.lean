module
public import AC.Model

/-! Efficient certificates for the unchanged structural property. Payloads remain
in the actual Model; these lemmas avoid repeatedly deciding irrelevant fields. -/
@[expose] public section
namespace AC

/-- Exact list reconstruction without normalizing every concrete indexed lookup.
The array still contains the complete original identities. -/
theorem array_reconstruct {α : Type} (xs : Array α) (fallback : α) :
    xs.toList = (List.range xs.size).map (fun i => xs[i]?.getD fallback) := by
  apply List.ext_getElem
  · simp
  · intro i hi hj
    simp only [List.getElem_map, List.getElem_range, Array.getElem_toList]
    simp [Array.getElem?_eq_getElem (by simpa using hi)]

def mergeIndices : Nat → List Nat → List Nat → List Nat
  | 0, xs, ys => xs ++ ys
  | _ + 1, [], ys => ys
  | _ + 1, xs, [] => xs
  | fuel + 1, x :: xs, y :: ys =>
    if x ≤ y then x :: mergeIndices fuel xs (y :: ys)
    else y :: mergeIndices fuel (x :: xs) ys

theorem mergeIndices_perm (fuel : Nat) (xs ys : List Nat) :
    (mergeIndices fuel xs ys).Perm (xs ++ ys) := by
  induction fuel generalizing xs ys with
  | zero => exact List.Perm.refl _
  | succ fuel ih =>
    cases xs with
    | nil => simp only [mergeIndices, List.nil_append]; exact List.Perm.refl _
    | cons x xs =>
      cases ys with
      | nil => simp only [mergeIndices, List.append_nil]; exact List.Perm.refl _
      | cons y ys =>
        simp only [mergeIndices]
        split
        · exact (ih xs (y :: ys)).cons x
        · exact ((ih (x :: xs) ys).cons y).trans List.perm_middle.symm

def sortIndices : Nat → List Nat → List Nat
  | 0, xs => xs
  | fuel + 1, xs =>
    let left := xs.take (xs.length / 2)
    let right := xs.drop (xs.length / 2)
    mergeIndices xs.length (sortIndices fuel left) (sortIndices fuel right)

theorem sortIndices_perm (fuel : Nat) (names : List Nat) :
    (sortIndices fuel names).Perm names := by
  induction fuel generalizing names with
  | zero => exact List.Perm.refl _
  | succ fuel ih =>
    unfold sortIndices
    exact (mergeIndices_perm _ _ _).trans
      (((ih _).append (ih _)).trans (by rw [List.take_append_drop]))

/-- A complete byte-derived numerical witness. No injectivity or collision
assumption is used: distinct values of any function imply distinct inputs. -/
def identityCode (name : String) : Nat :=
  name.toByteArray.data.toList.foldl (fun n b => n * 257 + b.toNat + 1) 1

theorem nodup_of_codes {α : Type} (encode : α → Nat) (names : List α)
    (codes sorted : List Nat) (fuel : Nat)
    (source : names.map encode = codes)
    (permutation : sortIndices fuel codes = sorted)
    (ordered : sorted.IsChain (· < ·)) : names.Nodup := by
  apply List.Nodup.of_map encode
  rw [source]
  have nd : sorted.Nodup := ordered.pairwise.imp (fun h => Nat.ne_of_lt h)
  have perm : sorted.Perm codes := by
    rw [← permutation]
    exact sortIndices_perm fuel codes
  exact perm.nodup_iff.mp nd

theorem separated_of_nodup (records : List Record) (external : List String)
    (unique : (records.map Record.identity ++ external).Nodup) :
    ∀ r ∈ records, r.identity ∉ external := by
  intro r hr he
  exact (List.nodup_append.mp unique).2.2 _ (List.mem_map.mpr ⟨r, hr, rfl⟩) _ he rfl

/-- Membership witnesses may point into one exact block. Neither the index nor
the producer's table is trusted without the equality and block inclusion. -/
theorem member_of_block_index {α : Type} (all : List α) (block : Array α)
    (index : Nat) (value : α)
    (inside : ∀ x ∈ block.toList, x ∈ all)
    (atIndex : block[index]? = some value) : value ∈ all := by
  apply inside
  exact Array.mem_toList_iff.mpr (Array.mem_of_getElem? atIndex)

theorem mapped_block_inside {α β : Type} (project : α → β)
    (blocks : List (List α)) (block : List α) (member : block ∈ blocks) :
    ∀ x ∈ block.map project, x ∈ blocks.flatten.map project := by
  intro x hx
  rw [List.map_flatten]
  exact List.mem_flatten.mpr
    ⟨block.map project, List.mem_map.mpr ⟨block, member, rfl⟩, hx⟩

theorem names_nodup_of_order (names : List String) (lookup : Nat → String)
    (order : List Nat) (n fuel : Nat)
    (source : names = (List.range n).map lookup)
    (permutation : sortIndices fuel order = List.range n)
    (sorted : (order.map lookup).IsChain (· < ·)) : names.Nodup := by
  have perm : order.Perm (List.range n) := by
    rw [← permutation]
    exact (sortIndices_perm fuel order).symm
  have nd : (order.map lookup).Nodup :=
    sorted.pairwise.imp (fun {a b} h eq => by
      subst b
      exact String.lt_irrefl a h)
  rw [source]
  exact (perm.map lookup).nodup_iff.mp nd

def targetBound (n : Nat) (external : List String) : Target → Prop
  | .localRecord key => key < n
  | .external name => name ∈ external

instance (n : Nat) (external : List String) (target : Target) :
    Decidable (targetBound n external target) := by
  cases target <;> dsimp [targetBound] <;> infer_instance

theorem all_flatten {α : Type} (p : α → Prop) (chunks : List (List α))
    (h : ∀ block ∈ chunks, ∀ a ∈ block, p a) :
    ∀ a ∈ chunks.flatten, p a := by
  intro a member
  obtain ⟨block, hb, ha⟩ := List.mem_flatten.mp member
  exact h block hb a ha

theorem localKeys_range (m : Model) (n : Nat)
    (keys : m.records.map Record.key = List.range n) : m.localKeys = Finset.range n := by
  ext x
  simp only [Model.localKeys, keys, List.mem_toFinset, List.mem_range, Finset.mem_range]

theorem wellFormed_of_range (m : Model) (n : Nat)
    (keys : m.records.map Record.key = List.range n)
    (names : (m.records.map Record.identity).Nodup)
    (external : (m.externalResolutions.map External.identity).Nodup)
    (separate : ∀ r ∈ m.records, r.identity ∉ m.externalResolutions.map External.identity)
    (edges : ∀ e ∈ m.edges, e.1 < n ∧ e.2 < n)
    (refs : ∀ r ∈ m.references, r.owner < n ∧
      targetBound n (m.externalResolutions.map External.identity) r.target) :
    m.WellFormed := by
  refine ⟨?_, names, external, separate, ?_, ?_⟩
  · rw [keys]
    exact List.nodup_range
  · intro e he
    simpa only [localKeys_range m n keys, Finset.mem_range] using edges e he
  · intro r hr
    have bounds := refs r hr
    refine ⟨?_, ?_⟩
    · simpa only [localKeys_range m n keys, Finset.mem_range] using bounds.1
    · cases h : r.target <;>
        simpa only [h, targetBound, Target.Resolves, localKeys_range m n keys,
          Finset.mem_range] using bounds.2

theorem checked_of_wellFormed (m : Model) (h : m.WellFormed) : checkModel m = true := by
  simpa only [checkModel, decide_eq_true_eq] using h

end AC
