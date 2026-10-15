# Review of C3-I5-02: the consolidated iteration 5 common input at c0f16ee

**Reviewer**: Claude, cross-family, nonauthor of the common source and of the Codex candidate.
**Subject**: source `c0f16ee` ("Consolidate I5 construction requirements and both candidate reviews"), recorded as C3-I5-02 at `03972c8`. Preimage `455ce5d` (C3-I5-01).
**Expectations**: `claude/20261015T225927Z_EXPECTATIONS_REVIEW_C3_I5_02_C0F16EE.md`, committed at `87c4e34` before this reviewer opened the pen's readback.
**Standing**: commentary. It claims no ratification, admission or acceptance. The product owner is the human who ratifies an exact commit. "The pen" is Codex, holder of the common Writer grant. "The map" is the table "Iteration 5 consolidated work" in T-002.

**Result: `candidate_ready` for exact-commit ratification at `c0f16ee`. No blocking defect. Three Low findings, one of which drops a sentence the preimage carried.** The product owner may ratify `c0f16ee` as it stands, or have the pen fix the three Low findings in one successor commit and ratify that commit exactly.

## Expectations against the source

| # | Result | Evidence |
|---|---|---|
| E1 fourteen findings dispositioned and mapped | Met | Disposition tables list F1 to F4, R1 to R4 and CY-01 to CY-06. Map rows: F1 to F4 in I5-00; R1 and CY-05 in I5-02; CY-01 in I5-03; CY-06 in I5-04; R2 in I5-05; R3 in I5-06; CY-02 in I5-07; R4, CY-03 and CY-04 in I5-08 |
| E2 F1 admitted discriminator basis | Met | Candidate Comparison: "Each is assessed against the requirements, criteria and discriminators in its admitted input; a later draft does not rebind it"; the conformance preamble repeats it and keeps unmatched scope explicit |
| E3 F2 categorical sequence is this project's strategy | Met | Categorical Construction: "The following sequence is this source project's strategy ... Consumers select their own strategy" |
| E4 F3 homeostasis and bugs | Met | Homeostasis is defined with its limits ("guarantees neither convergence nor the adequacy of those conditions"). The bug sentence is bounded to work management and defined by its colon clause. The "feature" reading is the product owner's model; this reviewer's preference for "change work" was a wording preference and its non-adoption is lawful |
| E5 F4 exact pins | Met | All 27 pins reproduce from `c0f16ee` (bytes and SHA-256). GOALS moved again at `03972c8` (status line and goal table), so the pinned GOALS member differs from HEAD's; the owner ratifies `c0f16ee`, not "main" |
| E6 no determination dropped by a replaced line | Not met for one row | See L1 |
| E7 no new obligation without purpose; no tenant design in the WHAT | Met | Each added sentence answers a named finding. No role, ledger, result algebra, architecture or control arm is prescribed; the new integrated row is a check, placed in the integrated table |
| E8 P1 to P6, pillars, member set unchanged; amended criterion named | Met in part | PRINCIPLES, INTENT, REFERENCE_FRAME_BASIS, CAPABILITIES, A_C_DEPENDENCY and PREDECESSOR_CLAIMS hash-identical to `455ce5d`. Member discriminators 52 + 9 unchanged; integrated checks 4 to 5. Criterion 4 gains three sentences, but the GOALS revision record says "the six criteria ... remain" without naming criterion 4 as amended; see L3 |
| E9 links resolve | Met | 361 relative links in the 27 pinned members, 0 broken (scheme links such as `stdo://` excluded). The pen's counts of 385, 406 and 299 cover different file sets; every count reports zero broken |
| E10 the two residuals at `c66ed4e` are real | Met | `qualification/C3-ITER4/trial/DESIGN.md` line 52 still says a control pass means "decided by the fixture, not the method"; `standards/SPEC_METHOD.md` lines 231 to 232 carry "corrected at iteration 4 after a cross-family finding". Both are this line's to repair under I5-06 and I5-08 |
| E11 the pen's corrections of this reviewer's claims | All three hold | See "Corrections of my earlier claims" |
| E12 every open I4 duty carried; protocol with the pen; replacements reserved | Met | Mapping sentence I4-01 to 09 → I5-01 to 09 checked against the common I4 staging rows; the shared-protocol paragraph keeps recording with the pen; Q2 and Q9 and "per-tenant predecessor replacements/removals" are listed as owner decisions |
| E13 the map pre-accepts nothing | Met | "The map selects no donor and gives no whole-candidate verdict"; "retain" rows are work instructions rechecked "on the chosen preceding candidate" |
| E14 readback labelled same-family | Met | The readback names itself "a declared same-family nonauthor working review, not a cross-family review or an acceptance-owner decision"; T-001 records the exception |

## Findings

| # | Severity | Finding | Fix |
|---|---|---|---|
| L1 | Low | The replaced member-conformance row "The same requirements are realised by software, a human team or a mixed process" drops the preimage sentence "Common requirements decide fitness; the kind of executor alone neither rejects nor accepts the realisation." No other clause at `c0f16ee` states that the executor kind alone decides nothing (the binding requirement's items 2, 4 and 6 carry the two halves separately). The disposition does not name the removal | Keep the dropped sentence beside the new one; the new sentence is an instance of it |
| L2 | Low | "Generic procedures" is used without definition at its first use in the binding requirement item 2 and in the same conformance row | Define it once: a procedure the method states for every realisation, such as the constitutional chain |
| L3 | Low | The GOALS revision record for this consolidation says "the six criteria ... remain" while criterion 4 is amended by three sentences. An I5 admission binds the amended criterion; an I4 candidate keeps the I4 text under the new comparison clause. The record should say so | Name criterion 4 as amended in the revision record |

## Corrections of my earlier claims

The pen's disposition corrects three statements this reviewer made on 2026-10-15. All three corrections hold at the named commits.

| Claim | Correction | Checked |
|---|---|---|
| CY-03: `qualification/C3/RETURN.md` "says the current construction is the I3 native-fidelity repair" | At the named return `9a93c5a` that file already says "The current construction is iteration 4". My reading came from the package commit `903f119`, where it still named the I3 repair | Both commits read. The root records `C3/CONSERVATION.json`, `FRONTIER.json` and `FRAME_INPUTS.json` remain at `9a93c5a` without a historical label; that residual is what I5-08 keeps |
| CY-05: "55 per-unit determinations carry the generic consequence" | 38 rows of the 701 determinations at `903f119` carry it. The other part stands: 389 bind no consumer, 312 do | `qualification/C3/iteration-4/DETERMINATIONS.json` at `903f119` recounted |
| Comparison: Codex's arguments are "reached only through tooling" | Too broad. Codex's members carry prose argument tables: "Fundamental Laws" in AXIOMATIC_CALCULUS and "Core contract derivations" in FOUNDATIONS at `62318d3` | Both tables read. The remaining point stands: the per-determination account is a 43.6 MB machine record |

CY-03 therefore reduces to the root-record labelling, and CY-05's count is 38. The severities (Medium, Low) do not change: CY-03's routing defect at the package commit was real and the residual is still open; CY-05 was Low already.

## Consequence for the Claude line

On ratification of `c0f16ee` (or its successor), the Claude line's I5 admission binds that input, its preceding candidate `c66ed4e`, and I5-01 to I5-09 as the map states. The line's own residuals from the map: the trial design's control-arm description (I5-06), the chain-repair provenance in SPEC_METHOD §2 (I5-08), and the open I4 duties already recorded in its ledger (interpretation coverage, 38 untraced paths, 505 unread conserved rows, criterion 4). Nothing in this review changes `c66ed4e`.

## Limits

This review read the source delta `455ce5d..03972c8` in full, the pen's disposition, the readback and its expectations, the two named residual locations at `c66ed4e`, and the Codex files named in the corrections at `903f119`, `9a93c5a` and `62318d3`. It reran the 27 pins and a link check. It did not reread the whole of PRODUCT or the requirements, did not assess either candidate, and ran no actor.
