# Bounded recheck: candidate-03 repairs F1 and F2 from the candidate-02 review (18 Nov 2026)

**Verdict: `satisfied`.** Both findings from the candidate-02 review are closed. I found no new contradiction in the changed consumer descriptions, the Product and Goals descriptions, the regenerated frame or the new index entry. Triage is `not_applicable`.

This result covers only the bounded claim below. It is not owner acceptance, not a release qualification and not a new independent assessment of the whole architecture.

## Subject and basis

- **Subject:** `.ai-workspace/work/STDO_REVIEW_REPAIR_2026-11-18/candidate-03/`, `CANDIDATE.json` SHA-256 `c11c76174a092925ec69cd46f2af1532249c7985b6856542434792698e379c57`.
- **Prior subject:** `candidate-02/`, SHA-256 `40bf55673fc803f856b66262a10cb23244a9c55be0ae115d2d17ce344e988f50`.
- **Product:** `urn:stdo:product-definition:stdo-3` (`stdo_3.json`), unchanged.
- **Installed basis:** `stdo://releases/v3.0.4/`, manifest `102817a3…dda9f95b`, unchanged according to `BASIS.json` and the intake.
- **Owner statements and input scope:** inherited from `REVIEW_INTAKE.md`. Its candidate identity is replaced by the one above.
- **Claim:** F1 and F2 from `.ai-workspace/comments/claude/20261118_REVIEW_TRACKING_RECONCILIATION_CANDIDATE_02.md` are repaired, and the changed consumer and Product/Goals descriptions add no new contradiction.
- **Severity scale:** the prior scale, 1 highest to 5 lowest.

## Actor, independence and evidence limits

- **Reviewer:** Claude, model `claude-opus-5-5` (Opus 5.5), read from host metadata. This was a fresh session with Read, Glob and Grep only. I edited nothing and delegated nothing.
- **Author:** the Writer (Codex, according to the earlier `REVIEW_HOST.json` record, which I reused and did not re-read). I wrote no part of the repair.
- **Same-family limit:** the candidate-02 review was also by Claude. The limit it recorded on the adopted architectural direction still applies. This recheck does not widen or clear it.
- **Receipts I relied on but could not recompute:** I have no command tool, so I relied on:
  - the SHA-256 values and the changed/unchanged split in `CANDIDATE_RELATION.json`;
  - the `frame_drift` result in `CHECKS.json`, which is empty;
  - the claim that ODD and `GENERIC_REGISTER.md` are byte-identical to candidate-02.
- **Order of reading:** I read the prior finding predicates and the owning clauses before the repair diff. The owning clauses were the ODD F18 table, its consumers, and §§11.5, 11.5B and 11.5D.

## Method and evidence read

- **Control files:** `RECHECK_INTAKE.md`, `REVIEW_INTAKE.md`, the installed `stdo-review` SKILL and the candidate-02 report.
- **`REVIEW_REPAIR.patch` (1141 lines):**
  - all four source hunks;
  - the hash and size hunks in `FRAME_INPUTS.json`;
  - the regenerated `stale-summary.md` frame in full;
  - the header hunks of the other frames.
- **Candidate-03 files:**
  - ODD lines 77–151 and 650–779;
  - SPEC_METHOD lines 40–74 and 205–299;
  - standards README lines 58–87;
  - `CHECKS.json`;
  - `GENERIC_REGISTER.md`, by targeted search.
- **Searches across all of candidate-03 (patches and JSON excluded where noted):**
  - stale ODD wording: immutable ledger, replay-visible, yield loop, A0–A16, the runtime's admission authority, closure-decision values;
  - ODD near ledger, replay, register, evaluator or event log;
  - a register, ledger or event log near must, required or mandatory;
  - Product and Goals wording: current product definition, overriding concerns, present-tense terms, next body of work, current implementation, end state, future destination;
  - the frames, for any copy of the old or new SPEC_METHOD sentences.

## Closure of the prior findings

**F1 (severity 3) is closed.**
- **ACTIVATION §5 consumers, row 1, line 1448:**
  - It now says ODD's "conservation row imports F4 for records of needed step-produced facts and reconciliation with current workspace evidence."
  - That matches F18: the only row that imports F4 is the P4b row at ODD:125. That row requires recording needed step-produced facts with evidence by reference, says "no mandatory ledger or event-log design", and cites §11.5, §11.5C and §11.5D, where the reconciliation duty is stated.
  - It also matches ODD consumer 7 (ODD:141), which lists ACTIVATION §5 as consuming bounded records and current evidence.
- **The `stale-summary` frame copy (line 660):** it carries the same corrected text.
  - The frame grew from 105693 to 105728 bytes. That 35-byte difference is consistent with the sentence change.
  - The frame's other hunks change only digests.
- **Standards README, ODD row (line 70):** "the constructive evaluation and yield loop (A0 to A16)" is replaced by "tracking, evidence and bounded decisions with an optional generic-register example", which matches §11.5D's heading and content.
- **DESIGN_MODULE row 10 (line 242):** it now says that under ODD §11.5B "consequential transformations apply ACTIVATION's admission law and runtime control retains its separately bound authority". That matches ODD:690–696, which leaves admission with ACTIVATION §4 and binds runtime control separately.
- **Searches:** no stale ODD-runtime wording remains in any candidate-03 source member or frame. The only hits are the removed (`-`) lines in `SOURCE.patch`.

**F2 (severity 5) is closed.**
- **Lines 55–59:** Goals "names the current epics or bounded work wave". `PRODUCT.md` "defines the intended Product end state, including capabilities still to be built."
- **Lines 249–250:** Goals "identifies the current epics being pursued toward the Product". "Next body of work" is gone.
- **Lines 282–283 (Manifesto):** "defines the intended Product end state, including capabilities still to be built". "Present-tense terms" is gone.
- **Consistency:** these agree with lines 215–219 and 253–258, with SPEC_METHOD:881, and with the Product and Goals templates and the templates README.
- **Frames:** no frame copies these sentences, so no frame needed regenerating for this finding.

## Counterexample search

Nothing below falsifies the claim.

- **Stale prose outside link anchors:** none. Every ODD-adjacent mention of ledger, replay, register or evaluator in a source member is one of the three repaired lines. The ACTIVATION hit concerns UX's Msg log, which is a separate profile left unchanged.
- **A register made required again:** none.
  - The new README index row calls the register optional, says it illustrates the required tracking and reconciliation, and allows equivalent LLM or other mechanisms.
  - Every other "required/must … ledger/event log" hit is in unchanged text and either denies the ledger or makes it conditional on a binding: ACTIVATION:343, `requirements/README.md`:152, TICKETS:90/755, ODD:125/728.
  - `GENERIC_REGISTER.md` still says it is "illustrative … not an additional standard or required file" and supplies no new authority.
- **Product equated with the current implementation, or Goals with a future destination:** none.
  - The remaining "current Product Definition" uses mean the definition in force: PRODUCT_DEFINITION:242, EXECUTIVE_BASELINE:794, the basis template, and the templates README:29/40, which defines "current" that way.
  - SPEC_METHOD:1111 ("bounded work wave or overriding concerns") still describes Goals as current work, not a destination.
  - TICKETS:1302 denies that the current implementation has any authority.
- **Checker label:** `GENERIC_REGISTER.md` no longer appears under `preexisting_broken_links`. Both `introduced_broken_links` and `remaining_broken_links` are empty, and `frame_drift` is empty (the last relied on, not recomputed).

## Findings

None. Triage is `not_applicable`.

## Residuals

- **Successor dispositions** for the removed ODD claims (A0–A16, the closure enum, the old §11.5B inventory table) are still unrecorded under STDO-UP-015 / RELEASE §9. This carries over from the candidate-02 review and remains open for release time.
- **The same-family independence limit** on the adopted architectural direction remains.

## Adjacent observations

Triage is `not_applicable` to the claim for all of these.

- **"Conservation row" is an informal label.** The F18 table has no row names. The reference is unambiguous because only one row imports F4.
- **`preexisting_broken_links` still lists the two Goals links** that were removed in the preimage. This is accurate as a preimage observation and does not affect the empty remaining list.
- **The ODD README row still omits §20, "Canonical compression".** This predates both candidates.

## Coverage not performed

- No recomputation of hashes, the changed/unchanged member split or frame derivation.
- I did not read every `FRAME_INPUTS.json` hunk or every frame hunk line by line. I checked the headers and the full `stale-summary` frame, and searched all frames for stale and new wording.
- No new assessment of ODD or the register example beyond the owning clauses named above.
- No whole-method or architecture assessment, and no installed or runtime behaviour.

## Invalidation and re-entry

This result is void if any of these change:
- any candidate-03 byte, or `CANDIDATE.json`;
- an owner ruling quoted in `REVIEW_INTAKE.md`;
- the selected basis or its manifest;
- the severity scale.

It does not change the candidate-02 report, which remains that candidate's closed assessment.

The result goes to the Product-owned decision authority. Acceptance, priority and the successor dispositions still need that authority's decision; this recheck does not supply them.
