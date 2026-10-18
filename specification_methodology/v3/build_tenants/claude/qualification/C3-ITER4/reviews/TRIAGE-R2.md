# Triage of the readbacks R2b (ports) and R2a (repairs and I4 edits)

One repair round, by the Executive. R2b ran on Sonnet and R2a on Opus 5.5
(high) before the product owner selected Fable at max for later readings;
both are same-family nonauthor working evidence in fresh contexts. Every
finding is repaired at its owning locus or declined with its reason. The
changed ports and the changed loci receive one successor readback (I4-09).

## R2b, ports (13 findings)

| Id | Disposition | Where |
|---|---|---|
| R2b-01 | repaired: the record names the Pillar column, the pillar definition, the trace paragraph and the placement rule as this line's own additions, with reasons | CROSS_SYNTHESIS part 1 |
| R2b-02 | repaired: the unrecorded differences and the uncarried owner sentence are recorded with reasons | CROSS_SYNTHESIS part 2 |
| R2b-03 | repaired: the import rule has one owner. REFERENCE_FRAME §1 no longer repeats the rule's sentences; the record says which Codex sentences FOUNDATIONS §2 carries, as a port in its cone | REFERENCE_FRAME §1; CROSS_SYNTHESIS part 3 |
| R2b-04 | repaired: the two added rules and the omissions are recorded with reasons | CROSS_SYNTHESIS part 3 |
| R2b-05 | repaired: FOUNDATIONS §3 names PROFILES §1's rule the family-import rule, under the import rule of §2 | FOUNDATIONS §3 |
| R2b-06 | repaired: "the pair" replaced by the functor and its quasi-inverse; the Formal fragment's items referred to, not restated; the differences recorded with reasons | EVALUATION §6; CROSS_SYNTHESIS part 4 |
| R2b-07 | repaired: the row filter is recorded (requirement 6), documented in the generator, tested (`RowSelection`, three tests), and the preface says a `rows=k/n` excerpt is not a byte copy | CROSS_SYNTHESIS part 5; generate_frames.py; test_generate_frames.py |
| R2b-08 | repaired: `id` and `task`, the acquisition additions and the restored no-universal-sufficiency sentence are recorded; the sentence is restored in ACTIVATION §2 | CROSS_SYNTHESIS part 5; ACTIVATION §2 |
| R2b-09 | repaired: the verbatim list corrected to lines 6–9, 12–13 and 94–95, line 11 adapted | CROSS_SYNTHESIS part 6 |
| R2b-10 | declined in part: the `conserved`-only condition is kept, because a `superseded` row is decided by its proposed relation and not by the conservation reading; the condition, its reason and the extra fields are now recorded | frontier_review.py docstring; ports.md C3 |
| R2b-11 | declined: the locus hash follows the frontier's own granularity (a row covers its heading's text up to the next heading of any level), which differs on purpose from the frame generator's whole-section rule; recorded | frontier_review.py docstring; ports.md C3 |
| R2b-12 | explained and scheduled: the positive reproductions fail because the frozen `a_c/i3` artifacts are stale against the member edits of this iteration, which is the checker reporting correctly; the artifacts are regenerated at the freeze and the controls rerun then. The dropped-clause control now has a passing baseline, the fresh positive projection of the same index, and the projections run from the fresh map | ac_controls.py; ports.md C5 |
| R2b-13 | repaired: the identity check reads the executable, schema and output-contract digests from the common `A_C_DEPENDENCY.md` and the adverse control appends one byte to a copy of the schema and expects the same check to refuse; it does | ac_controls.py |

## R2a, repairs and I4 edits (8 findings, 4 unexplained changes)

| Id | Disposition | Where |
|---|---|---|
| R2a-01 | repaired: `block-outside-claim` is again a prohibition (`forbids`, `must-not`) with the condition "by itself" and the repricing or re-entry consequence as its qualification; program rebuilt, 64 clauses, `assemble --check` 0 | a_c/i3/tools/spec.py; a_c/i3 |
| R2a-02 | declined: the purpose and material relation of the §5 table is stated at the end of EVALUATION §5 `When a finding blocks promotion` ("Purpose and material relation: the method stated these conditions in a work carrier, a design profile and the Executive profile…"); it predates `416bdb5`, so it is not in the diff the reviewer saw | EVALUATION §5 |
| R2a-03 | repaired: the disposition row conserved at EXECUTIVE_BASELINE names it in its Locus column | ACTIVATION §8 |
| R2a-04 | recorded as intended: the J55 case text follows the ratified common discriminator, which dropped "applicable" and added that inapplicability waives no criterion; REBIND item 12 | REBIND.md; this record |
| R2a-05 | repaired: the preface no longer claims the omitted rows are not needed; the frame's qualification decides sufficiency | generate_frames.py header |
| R2a-06 | repaired: both additions cite their principles and say they are new law carried from the common contract at iteration 4; the fit claim for a boundary and the step's fit judgment are stated as distinct | ACTIVATION §1, §2 |
| R2a-07 | repaired: the sentence is scoped to a received contribution | EVALUATION §3 |
| R2a-08 | repaired: a `conserved` disposition recorded before the test applied is re-evaluated under it before the claim qualifies, `unresolved` until then; this is what `frontier/REVIEW.json` records | RELEASE §9 |
| unexplained 1 | the same as R2a-01 | |
| unexplained 2 | explained: the EVALUATION §4 paragraph states the purpose of the generalisation FR-01's rows introduced, as criterion 6 requires of new law | |
| unexplained 3, 4 | explained: frame regeneration after the repaired member text | |
| FR-06 partly | the only remaining "core conjunction" in the design (DOCUMENT_STRUCTURE line 56) describes REFERENCE_FRAME's reference to FOUNDATIONS §4 for frames in conjunction, not the reader of J53 to J55; no change | |
| FR-11 partly | the body of ACTIVATION §1 generalises the restriction; the predecessor claim is conserved at EXECUTIVE_BASELINE, whose row now names it (R2a-03) | |
