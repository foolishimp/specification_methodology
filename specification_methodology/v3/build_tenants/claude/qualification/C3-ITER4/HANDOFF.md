# Iteration 4 Handoff, Claude Line

This is the closing record of the Claude line's iteration 4 on the
ratified common input C3-I4-03 (`3c4c503`), under the owner's ratification
of 2026-10-15 and the pen's admission records. It is for the product owner
and for the cross-family reviewer. Every check named here is same-family
working evidence unless it says otherwise. Nothing here is accepted, and
nothing claims acceptance or eligibility.

## Candidate

| Coordinate | Value |
|---|---|
| Branch | `tenant/claude/c3-synthesis` (worktree `specification_methodology-claude`), not merged, not pushed |
| Frozen candidate | commit `c66ed4e` |
| Member text final at | `23b6556`, plus the repair of SPEC_METHOD §2 Constitutional chain after Codex's finding R1 (`4299219`) |
| Preceding candidate | `2beed8d` (iteration 3), handoff `96ccdcc` |
| Donor | the Codex candidate at `fb855df`, package `d490dd6`, read only at those commits |
| Common input | C3-I4-03 at `3c4c503`, merged inward at `7c60f32` |
| Ledger | `qualification/C3-SYNTHESIS/LEDGER.md`, section "Iteration 4" |
| Results table | [RESULTS.md](RESULTS.md) |

Digests at the freeze: SHA-256 of the sorted `shasum -a 256` lines of each tree's files.

| Tree | Files | SHA-256 |
|---|---:|---|
| members `standards/*.md` | 23 | `c2ea8dab147f30eab76f4a0c0b4525ce012df4dfa40cd8870261c6a140a1e4a3` |
| all of `standards/` | 62 | `30648e54d5cf3c3ec03354789930e1d94f9bcf75a00e7296f693258a78572733` |
| `standards/frames/` | 13 | `3af6265c8012653a828b78e37a77ebc5eab14cfbc30b28d4afcfe90ce293c5c4` |
| `a_c/i3/` | 35 | `50717a82b8fe7f491b899e74c32695b933e2c6fdf9ea8569c43d39d7a937a729` |
| `qualification/instruments/` | 10 | `3d86bfc635862c9c13bfd4b5096a3a7d80854ef47b5ee56ad4af3c74a76f3c48` |
| `plugins/` | 17 | `b82afdd4119906cd3f7d8857cfdae74025aa9150824a642d9b562017689e2979` |
| `frontier/PREDECESSOR_CLAIMS.md` | 1 | `17439e40032be4401abf227d6209e71d63f7c7f7311054322a12eb45c2182901` |
| `frontier/REVIEW.json` and `REVIEW_ASSESSMENTS.json` | 2 | `2140ddb875b04274aee21715769dda2f37747bd6122141642b905c1c48c766ea` |

## What changed in this iteration

- **Rebind** (I4-01): 24 common decisions changed since `355aa86` accounted for in [REBIND.md](REBIND.md); the ratified fit rule in ACTIVATION §2 step 3, the conservation test in RELEASE §9, contribution authorship in EVALUATION §3 and inapplicability in ACTIVATION §1, each cited to its principles and marked as law carried from the common contract.
- **Ports** (I4-03, [ports.md](ports.md)): C1 and C6 excluded with reasons; C2 realised as the trial design; C3 adapted as `frontier/REVIEW.json`; C4 as `a_c/i3/consumers.json`; C5 as the checker controls (`tools/ac_controls.py`, seven controls, all holding on the regenerated artifacts). The six I3 ports and the three adaptations had two readback rounds (R2b, R2b-2): 19 findings, 17 repaired, 2 declined with reasons.
- **Family tables** (I4-02): EXECUTIVE_BASELINE, DESIGN_MODULE and ODD read source-first (R1, 70 rows): 14 findings repaired; premises cited with their standing, F13, F15 and F18 imported, per-clause attributions in ODD.
- **Conservation** (I4-04): 140 rows read in fresh contexts in eleven activations: 137 `conserved`; 3 clauses split to proposed-replacement child rows (`#work-result` under Q1, `#define-a-project-configuration` under a new Q9, the baseline `#canonical-compression` under Q2). Repairs from the reading at ACTIVATION §7 and §8, DESIGN_MODULE §4 and §11, REFERENCE_FRAME §1. The proposed relations, by question, are posted to the pen (`main` `708dfb9`) with a supplement in `reassess/REPLACEMENTS-SUPPLEMENT.md`.
- **Frames** (I4-06): every frame carries the rows of the family tables that cite its sections (generator mode `rows: frame-anchors`, tested); capacity 150,000 bytes, the per-frame increase recorded as tradeoff TO1 in REDUCTION §4.3; the F5 `kind` residual closed.
- **Reduction** (I4-07): subjects rebound (S1 is `2beed8d`); verdict standing in the ratified values; seven sample paths traced ([paths/SUMMARY.md](paths/SUMMARY.md)).
- **Repairs read back** (I4-09): the I3-8r repairs (R2a: FR-01, -03, -05 repaired; -06, -08, -11 partly, then repaired), the I4 edits, and the three Codex findings that changed text (R1 chain, R3 trial grading, R4 README), with the chain row's readback read back as `conserved` with modal force preserved (batch 12).
- **Interpretation** (I4-05): `block-outside-claim` is a prohibition again with its condition; the artifacts regenerated from the pinned checker at the freeze; coverage unchanged at 64 clauses.

## Working results (same family, fresh contexts, Fable at max unless noted)

| Activation | Subject | Result |
|---|---|---|
| R2b (Sonnet), R2b-2 | the six I3 ports and C3, C4, C5 | 13 then 6 findings; all repaired or declined with reasons (`reviews/TRIAGE-R2.md`, `TRIAGE-R2b2.md`) |
| R2a (Opus 5.5) | the I3-8r repairs and the I4 edits | 8 findings, 7 repaired, 1 declined (`reviews/TRIAGE-R2.md`) |
| R1 | family tables of EXECUTIVE_BASELINE, DESIGN_MODULE, ODD | 14 findings, all repaired (`reviews/TRIAGE-R1.md`) |
| Batches 01 to 11 (01 on Sonnet) | 140 conservation rows | 137 `conserved`; 3 split to child rows (`reassess/`, `frontier/REVIEW_ASSESSMENTS.json`) |
| Traces DP-01, -07, -13, -19, -25, -31, -37 | seven deciding paths on rc.2, `2beed8d` and `23b6556` | DP-31 `satisfied` against rc.2; six `indeterminate` with an elimination witness each; all `indeterminate` against `2beed8d` |
| Checker | `a_c/i3` regenerated at the freeze | `valid`, 0 diagnostics; seven controls hold (identity positive and adverse, validate positive and two adverse, projections positive and adverse) |
| Codex cross-family review (`8a0ea22`) | the candidate in progress | R1 to R4, all repaired on the successor |

## Gaps the product owner should know

- **Criterion 4 (actual use).** Unevidenced. The trial (`trial/DESIGN.md`) is designed, its card, writer and grader instructions are fixed, and eight of twelve expectation sets are written and hashed by nonauthor writers; no actor has run. The runs are held because the owner's iteration 5 plan changes every frame (each must bind the construction requirement), which would make this trial's results historical on arrival. If the owner orders the trial on this candidate, TT-08's expectations are rewritten first (its frame carries the repaired chain section) and the remaining four sets are written; then 44 actor runs and 12 gradings follow. Under the ratified text criterion 4 is `unresolved`, which leaves this candidate ineligible for a qualified choice and does not qualify its peer.
- **Conservation.** 505 of the 611 `conserved` rows carry the author's disposition only (30 verified at I3); 140 are read. Every proposed relation is pending the owner.
- **Interpretation coverage.** 64 clauses over the shared-owner determinations of G1 to G4; 15 sections `encoded-in-part`, 181 `not-encoded-i3`, G5 to G13 not encoded. Consumer semantics beyond citation unread. This blocks C3 closure for interpretation coverage.
- **Reduction.** 38 of 46 paths untraced; the entry README's growth (2,330 to 28,087 bytes) is an undeclared tradeoff that leaves six traced paths `indeterminate`; no frame-entry trace; DP-19 named two residual rivals (EXECUTIVE_BASELINE §16 and §19 field lists; the "binding" homonym of PROFILES §1).
- **Discriminators.** Mapped and partly read back; no cross-family assessment of the 52 on the successor.
- **Variances recorded in the ledger:** the reviewer model changed mid-iteration on the owner's instruction (Sonnet, then Opus 5.5, then Fable at max); the packets of batches 06 and 09 gave headings without their subsections (fixed); the ledger timestamps of 2026-10-15 afternoon were written in local time and corrected from commit times.

## Open decisions for the product owner

1. The proposed replacement relations: 17 rows in 9 questions plus 10 compressions (`main` `708dfb9` and the supplement).
2. The UX compliance-test replacement; UX applies the stricter reading under the ambiguity rule.
3. Identity and packaging of the released interpretation.
4. The I5 plan: this candidate becomes the preceding candidate of an I5 admission.

## Rerunning the checks

`qualification/C3-ITER4/tools/`: `frontier_review.py`, `consumers.py`, `ac_controls.py`, `freeze_ac.sh`, `merge_batch.py`, `modal_batches.py`, `readback_packet.py`, `trial_packets.py`; the I3 tools in `qualification/C3-ITER3/tools/`; the generator and its 45 tests in `qualification/instruments/`.
