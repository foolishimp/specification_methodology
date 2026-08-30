# Worker Return — Constraints Governing Reference-Frame Use in a Pre-RC Release Review

**Role and bounded outcome.** Acting as Worker under a bounded, read-only evidence task. Outcome: identification of governing constraints only. No readiness judgment, no acceptance, no verdict. Work-result variant: `candidate_ready` in the profile's sense of "result returned to the Executive" — the result is this constraint enumeration, not any release disposition.

## Map-first evidence

Started from `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` (kind `axiom-indexer.logical-constraint-map`, `map_sha256: 2df34c…21b78`, calculus_ref `stdo://releases/v2.5.0-rc.1/standards/AXIOMATIC_CALCULUS.md`). The broad Source STDO corpus was not opened first.

## Selected frames

| Frame URI | Purpose for this task | Source route |
|---|---|---|
| `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws` | Owns pure frame law: what a bounded frame is, its result algebra, and authority limits | Map `frame_refs`, resolved to installed cut `~/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md` |
| `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame` | Defines the Worker frame's authority, evidence, exclusions, and result family for candidate construction/review work | Same installed cut, `STDO_REFERENCE_FRAME_BASELINE.md` |
| `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame` and `#derived-executive-frame` | Bound what review-shaped evaluation may claim and who disposes | Same file (single source re-entry covers all baseline anchors) |

Material map clauses linked to these frames: `reference-frame-is-bounded`, `engagement-return-topology`, `release-rc-is-immutable`, `standards-cut-is-complete-basis`, `compression-assets-are-read-models`, `aggregate-compression-reenters-source`, `bootstrap-resolves-exact-basis`.

## Governing constraints for reference-frame use in a pre-RC release review

1. **Bounded frame binding.** Each frame used in the review must bind an exact subject and basis, finite material relations, capability, authority, admissible evidence, exclusions, closed results, invalidation, and re-entry (`reference-frame-is-bounded`; RF laws). A review frame cannot be open-ended over the corpus.
2. **Exact complete basis.** The frame basis is the complete immutable selected STDO release inventory — individual standards are not independently selectable method versions (`standards-cut-is-complete-basis`), and the basis is resolved through exactly one applicable Product Definition's `constitution.stdo.basis`, failing closed on ambiguity (`bootstrap-resolves-exact-basis`).
3. **No authority from breadth or labels.** A frame selection or result acquires no semantic, operation, or decision authority from usefulness, breadth, actor, or technology (RF Core Claim 8). The Worker label grants no mutation authority; the Reviewer role has bounded evaluation only — no repair, disposition, or next-activation authority; disposition (`accept`, `local_repair`, `re_enter`, `reject` under `STDO-UP-020`) belongs only to the Executive with existing authority (`engagement-return-topology`).
4. **Closed result algebra with lawful residuals.** Every frame evaluation returns exactly one of `satisfied | falsified | indeterminate | out_of_frame | invalid_basis`; unknown/out-of-frame results are pressure for reconfiguration, not implied acceptance or failure (RF Core Claims 9–10; Missing-Frame And Re-Entry Application).
5. **Source re-entry over derived views.** Compressions, maps, and indexes are read models; unresolved or stale meaning requires re-entry into exact raw selected-cut owners through declared routes (`compression-assets-are-read-models`, `aggregate-compression-reenters-source`). An upstream authority gap is repaired by `re_enter` to the owner, not by enlarging the frame.
6. **Adoption is explicit.** Inclusion of the frame baseline in a released cut makes it available but does not adopt it; adoption requires a separately accepted Product-owned Project Reference-Frame Basis. Prompts, installed presence, and commentary neither select nor adopt (Status And Authority Boundary).
7. **Pre-RC vs. post-publication distinction.** A pre-RC candidate review evaluates a mutable source-project candidate through Worker/Reviewer frames, returning results to the Executive; only publication of an immutable annotated RC creates exact-cut authority, and the moving version-line selector remains discovery, not authority (`release-rc-is-immutable`). Pre-RC review therefore may not treat frame results as exact-cut qualification, and post-publication qualification may not be back-projected onto the candidate.

## Source STDO re-entries (2 of 2 permitted)

1. `REFERENCE_FRAME_METHOD.md` (installed v2.5.0-rc.1 cut) — Canonical Compression, Position, Core Claims. Needed because the map states frames "are bounded" but not the result algebra or authority-limit laws themselves.
2. `STDO_REFERENCE_FRAME_BASELINE.md` (same cut) — anchors `#status-and-authority-boundary`, `#derived-executive-frame`, `#derived-worker-frame`, `#derived-reviewer-frame`, `#missing-frame-and-re-entry-application`. Needed to resolve exact role-frame authority, exclusions, work-result variants, and the review/disposition boundary.

## Residuals and limits

- The map's frame ref anchor `#reference-frame-laws` does not appear verbatim as a heading in the installed `REFERENCE_FRAME_METHOD.md`; the laws content resolves to Canonical Compression / Core Claims. Unresolved anchor drift is retained as a residual.
- `STDO-UP-007/017–023` (ticket, design, spec method owners) were cited but not opened — within the two-file limit their exact wording remains unverified.
- Whether this repository's Product Definition has actually adopted the frame baseline was not evaluated; adoption status is out of frame for this task.
- No inference is made of semantic acceptance, frame adoption, release authorization, Product disposition, or an RC verdict.

**No-edit statement.** Read-only analysis only. No repository file was modified, and no mutation, publication, acceptance, or continuation action was invoked. Prior dogfood outputs were not inspected.
