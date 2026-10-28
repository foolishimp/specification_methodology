# T-012 scaling probe: final bounded diagnostic return

The three-probe grant is exhausted. The large 1,987-record structural gate remains incomplete. These results do not establish a small Array-to-List correction that makes it usable within the existing budget. No candidate source, shared cache, installed toolchain or Git state was changed by this Worker.

## Results

| Probe | Checked construction | Result | Wall time | Peak child RSS |
|---|---|---|---:|---:|
| 1 | Actual 32-record model source equality, numeric permutation and adjacent String ordering | Incomplete; 60-second fence, with concurrent work | 60.139 s | Not recorded |
| 2 | Same 32 exact identity strings as literals; numeric sorted-index permutation, equality-only Nodup, adjacent String IsChain | All three declarations passed | 14.279 s | 4,248,076,288 bytes (3.956 GiB) |
| 3 | Same 32 literals reconstructed by Array lookup, then List lookup | Both declarations passed | 0.706 s | 713,261,056 bytes (0.664 GiB) |

Probes 2 and 3 ran sequentially with the private Lean 4.35.0 compiler, `-j 1 -M 4096`, a 60-second process-group fence, `debug.skipKernelTC false`, and no inherited LEAN/LAKE/loader overrides. Both processes exited 0 and were reaped. Each record includes the exact source, command, selected support identities before/after, timestamps, log digest and result. The recorded support identities were unchanged within and between both runs. Compiler commit: `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`; compiler SHA-256: `d1d9c26a539f54fe839d2aa7760bf1ac1dd76a30b26e2c9684bebf2900038fcf`. Mathlib remains the existing pinned cache at `56a005855ea17e0b0958f73ec801ae140b0a1679`.

Before execution, the owned prepared sources were changed only to disable asynchronous elaboration and flush diagnostic stderr markers. Lean still delivered all marker lines at the end of each process. Their order confirms the declarations ran; receipt timestamps do not establish individual theorem durations or memory costs. No comparison in this report attributes Probe 2's cost to a single declaration.

Probe 2's numeric and equality-only results report no axioms. Its String ordering result reports the standard `propext`, `Classical.choice` and `Quot.sound` dependencies. Probe 3's Array result reports no axioms and its List result reports `propext`. No custom axiom, `sorry`, `native_decide`, unchecked truth or hash replacement was used.

## Diagnosis and consequence

1. Literal Array lookup reconstruction is inexpensive for these 32 exact strings. Replacing Array with List alone is therefore unsupported as a remedy for the earlier actual-model timeout. This comparison does not rule out cost from reducing the complete actual Model, its imported definitions, or their composition with the proof.
2. The combined numeric/equality/ordering probe already approaches the 4-GiB fence at only 32 names. The earlier full-identity Nodup and string-sort failures reported by the primary author remain consistent with excessive concrete comparison normalization, but this probe does not isolate its exact source. The installed String order definition decodes to character lists; that remains a plausible contributor, not a measured attribution.
3. Probe 1 occurred under contention, while Probes 2 and 3 were allotted an exclusive window. Its 60-second incomplete outcome cannot be directly interpreted as a scaling curve against the successful literal cases.
4. No full large-model certificate or output-correspondence proof was obtained by this diagnostic. Preserve that status explicitly; successful small gate qualification does not discharge it.

## Smallest sound fallback for a separately bounded follow-up

Retain the unchanged exact Model and structural property. Emit small exact identity blocks, prove each block's Nodup and bounded cross-block inequalities using kernel String equality, then combine them through the existing standard `List.nodup_append` theorem. This avoids requiring String ordering or a new sorting proof. The combining lemma is:

```lean
theorem nodupJoin (xs ys : List String)
    (hx : xs.Nodup) (hy : ys.Nodup)
    (apart : ∀ a ∈ xs, ∀ b ∈ ys, a ≠ b) :
    (xs ++ ys).Nodup :=
  List.nodup_append.mpr ⟨hx, hy, apart⟩
```

This is a direct instance of the installed theorem at `Init/Data/List/Pairwise.lean:364`; the snippet was not compiled as a fourth probe. All identities must remain connected by an exact checked equality to `model.records.map Record.identity`, and the resulting Nodup proof must feed the existing `wellFormed_of_range`. Cross-block obligations should themselves be chunked, rather than reconstructing one monolithic comparison decision. Total work is still quadratic. No useful block size, full-model memory bound or full-model runtime is established here; this is a sound construction proposal, not a claim of successful scaling.

The original 60-second / 4096-MB / maximum-three-probes grant is complete. No compiler process remains, and the exclusive verification window has been returned to Root. No further experiment is authorized by this activation.
