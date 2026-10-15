# Expectations for the review of C3-I5-02 at c0f16ee

Recorded 2026-10-15T22:59Z, after reading the source delta `455ce5d..03972c8` and the pen's disposition post (`codex/20261015T165424Z_DISPOSITION_I5_REVIEW_CONSOLIDATION.md`), and before reading the pen's nonauthor readback (`codex/20261015T165424Z_REVIEW_I5_CONSOLIDATED_COMMON_C0F16EE.md`) or the expectations that readback fixed.

Subject: source `c0f16ee`, the consolidated iteration 5 common input recorded as C3-I5-02 at `03972c8`. Preimage: `455ce5d`, C3-I5-01, which this reviewer reviewed at `27ee76c`.

Standing: a cross-family review of common source. It claims no ratification, admission or acceptance. The product owner is the human who ratifies an exact commit. "The pen" is Codex, the holder of the common Writer grant. "The map" is the table "Iteration 5 consolidated work" in T-002.

| # | Expectation | How it is checked |
|---|---|---|
| E1 | Each of the fourteen findings (F1 to F4 on C3-I5-01; R1 to R4, Codex on the Claude I4 candidate; CY-01 to CY-06, Claude on the Codex I4 candidate) has one disposition that names the owning clause or the reason for non-adoption, and one primary row in the map | Count fourteen in the disposition tables and the map |
| E2 | F1: Candidate Comparison or the conformance preamble says a candidate is assessed under the discriminator set of its admitted input and a later draft does not rebind it | Read the clauses |
| E3 | F2: Categorical Construction labels its sequence as this source project's strategy, not a consumer obligation | Read the clause |
| E4 | F3: "homeostatic" is defined or removed; the bug sentence names bugs as change work or bounds the "feature" reading | Read PRODUCT and requirement item 4 |
| E5 | F4: the snapshot pins reproduce from the exact source commit, and any member that moved after that commit is visible so that the owner ratifies an exact commit | Recompute the 27 pins at `c0f16ee`; diff the members `c0f16ee..03972c8` |
| E6 | A replaced row or sentence loses no determination the preimage carried, unless the disposition names the removal | Diff every replaced line; search the successor for the removed meaning |
| E7 | The clarifications add no obligation without purpose and material relation and copy no tenant design into the WHAT: no new role, ledger, result algebra, prescribed architecture or mandatory control arm | Read each added sentence against criterion 6 |
| E8 | P1 to P6, the pillars and the member discriminator set are byte-unchanged from `455ce5d`; an amended acceptance criterion is named as amended in the revision record | Hash PRINCIPLES; count rows; read the GOALS revision record |
| E9 | Every relative link in the 27 pinned members resolves | Link check |
| E10 | The two residuals the pen names against the Claude candidate at `c66ed4e` (the control arm's description in the trial design; the chain-repair provenance in SPEC_METHOD §2) are present at that commit | Read the two locations |
| E11 | The pen's corrections of this reviewer's earlier claims hold or are refuted: the return-file part of CY-03 at `9a93c5a`, the count of 55 in CY-05, and the comparison's "reached only through tooling" | Read the named files at the named commits |
| E12 | The map carries every open I4 duty into an I5 row, keeps the shared comparison protocol with the pen, and leaves the proposed replacement relations as owner decisions | Read the map and its I4-to-I5 mapping sentence |
| E13 | The map pre-accepts nothing: a row that says "retain" a tenant repair is a work instruction, and the map says it gives no whole-candidate verdict | Read the map's standing sentences |
| E14 | The nonauthor readback is same-family (Codex reading Codex), labelled as such, and claims no ratification or cross-family standing | Read the readback and T-001 |

Expected result if every row holds: `candidate_ready` for exact-commit ratification at `c0f16ee`, with findings at most Low.
