# T-012 scaling probe: partial diagnostic return

Root paused compiler work to protect the main gate milestone and then requested this closed partial return. No candidate source, shared cache, Git or installed-method bytes were changed.

## Performed probe

`Probe1.lean` separates the 32-record source-name equality, numeric sorted-index permutation and adjacent-name ordering into named kernel theorems. The invocation used the exact private Lean 4.35.0 binary, one thread, `-M 4096`, and a 60-second process-group fence. It timed out at 60.139 seconds and was killed with SIGKILL; retained status is incomplete. Its log contains only the parsing profile (115 ms). Command messages/profiler output were insufficient to identify which declaration was active. This run occurred while other Lean work was active, so it does not establish an isolated cost.

One of the maximum three probes has executed. No complete new theorem result or soundness defect is claimed from that timeout.

## Static findings and possible corrections

The certificate currently combines three distinct costs: concrete range/Array lookup reconstruction, Nat sorting/permutation and String ordering. Installed Lean's `Init/Data/String/Basic.lean:421` defines String `<` through decoded character lists; its extern comparator does not replace the definition used by kernel reduction. Thus UTF-8/character-list normalization is a plausible independent cost, not an established root cause.

The exact source linkage can potentially use generic reconstruction rather than repeated concrete Array normalization: standard `List.ofFn_getElem` (`Init/Data/List/OfFn.lean:109`) and Mathlib `List.ofFn_getElem_eq_map` (`Mathlib/Data/List/OfFn.lean:96`) reconstruct lists without weakening their contents. A range/getD equivalent can use the already checked record-key range to establish the length. A same-string List or Nat-pattern lookup is another discriminator. These changes have not been compiled or measured here.

If String ordering is the expensive step, an equality-only fallback already has standard proof support. `List.nodup_append` (`Init/Data/List/Pairwise.lean:364`) combines exact sublist uniqueness and cross-sublist inequalities; Mathlib `List.nodup_flatten` (`Mathlib/Data/List/Nodup.lean:296`) combines block uniqueness and pairwise disjointness. Bounded blocks may control peak kernel memory while retaining quadratic total work. This remains a proposal, not a measured performance or correctness result for the large model.

## Prepared, unexecuted probes

- `Probe2.lean`: exact 32 published-fixture identity strings; numeric permutation, literal equality-only Nodup and literal sorted String.IsChain as separate declarations, with immediate IO markers before and after each. Markers are diagnostic only; all mathematical facts use `decide +kernel`.
- `Probe3.lean`: the same exact 32 strings; compare Array lookup and List lookup source equalities using `rfl`, again with immediate markers.

Both must retain the same 60-second/4096-MB Lean fence. They import AC.Structure and can run through the selected tenant's `lake env lean -j 1 -M 4096` in a bounded process group. Neither has run, and a current support identity should be recorded when they do. No further compiler activity is authorized in this paused probe activation; Root will give a follow-up if those two probes remain useful.
