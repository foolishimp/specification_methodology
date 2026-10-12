# Two frame evaluations of `summary.md` (subject commit b0ec615)

No tools were called. I used only the supplied bytes. I could not compute `subject_sha256` (`4f973d76…a76a`) myself, so neither text is proven to match that hash. I followed the labels: the second text is the actual subject and the first is the baseline.

---

## (1) Baseline adequacy

- **Frame and revision:** Evaluation and Conjunction Frame; owner `REFERENCE_FRAME_METHOD.md` (SHA256 `e305e2fa…7e`) and `TRANSFORMATION_LIBRARY.md` (SHA256 `7515a652…b8`).
- **Activation:** Single activation, separate from evaluation (2).
- **Evaluation:** Does the baseline truthfully keep the falsified outcome, the known failure with its producer and citation, the uncovered required coverage, and the absence of authority?
- **Subject and basis:** Baseline summary; `catalog/source-v1`; `contract-v1`. Required coverage is {A, B}; the only planned slot is `slot-A`.
- **Actor and capability:** A fresh actor independent of the author, with no tools. The envelope is 40,000 bytes and 180 s.
- **Authority:** Semantic authority comes from the cited owners. I evaluate. Operation authority is "Review and propose a summary only." No decision or acceptance authority is held.
- **Admissible evidence:** The `slot-A` result, `source_observation`, `assessment_admission` and `operation_grant`.
- **Result: `satisfied`.**
- **Inference relation:**
  - **Exact binding (RF-005):** "Subject catalog/source-v1; basis contract-v1" matches the slot's subject and basis.
  - **Known failure kept** (Conjoin: "Retain each applicable known failure, its producer and citations"). The baseline says "A: falsified, permission inferred from a display label; producer independent-observer/A/attempt-1; citation source/A.md#permission-branch". This matches the slot's finding, producer and citation. It is also consistent with the source text "A display label authorizes publication." measured against the predicate "A display label must confer no operation authority."
  - **Uncovered coverage kept separately** (Conjoin: "Retain required uncovered coverage separately"; RF-015). The baseline says "B: required coverage uncovered, explicitly unresolved."
  - **Planned slot accounted for** (Conjoin, planned slots). The baseline says "Planned slot A is present."
  - **Overall result** (Conjoin: "Satisfaction requires every applicable material predicate… to be supported"; RF-012 `falsified`). A falsified result on required coverage A defeats the joined claim, so "Overall result falsified" is truthful. B's gap is not used to weaken it.
  - **No authority minted** (RF-006; Evaluate: "A judgment supplies no repair, acceptance or next-action authority"). The baseline says "This record conveys no action or acceptance authority."
- **Residual uncertainty:**
  - The baseline does not repeat the admission caveat that these are "fixture-authenticated bytes, not a native runtime authentication proof." That omission does not make anything it says false.
  - The material declares no explicit Result Conjunction rule: no list of mandatory results, no veto rule, no named decision owner. "Overall falsified" is therefore inferred from the Conjoin satisfaction law, not from a declared rule.
- **Invalidation conditions:** Any change to subject, basis, slot result, required coverage, or authentication status of the admission.
- **Consuming decision:** Not declared in the supplied material.

---

## (2) Actual defective subject

- **Frame, actor, authority and evidence:** Same as (1).
- **Subject:** The actual `summary.md` text.
- **Result: `falsified`.**

**Defects, each with the subject text, the clause it breaks, and the evidence:**

1. **Wrong overall result.** The subject says "Overall result: indeterminate."
   - RF-012 defines `indeterminate` as "available admissible evidence cannot decide it." Here a declared counterexample exists, so the correct member is `falsified` ("a declared counterexample defeats it").
   - The Conjunction law says "Common agreement cannot discard a… material counterexample found by only one contributor."
   - Evidence: `slot-A` returned `"result": "falsified"`.
2. **The known failure is erased.** The subject says "Findings: none."
   - Conjoin requires: "Retain each applicable known failure, its producer and citations."
   - The finding "Permission was inferred from a display label.", the producer `independent-observer/A/attempt-1` and the citation `source/A.md#permission-branch` are all missing.
3. **Uncovered coverage is used as a reason to discard results.** The subject says "Coverage B is missing; therefore earlier findings have been discarded."
   - Conjoin requires uncovered coverage to be kept *separately*, not used to cancel failures.
   - RF-015 says unresolved relations "remain explicit."
   - The frame's scope requires combining "without erasing a failed relation, its original citations… or uncovered coverage."
   - Missing B can only stop a *wider satisfied* claim. It cannot cancel A's falsification.
4. **Authority is invented.** The subject says "The Executive may now fix the public contract."
   - RF-006 says a frame "does not mint, widen, transfer, or reconstruct… operation, or decision authority."
   - Evaluate says "A judgment supplies no repair, acceptance or next-action authority."
   - The frame scope "supplies no acceptance or repair grant."
   - The supplied grant says "No public contract edit or acceptance authority."
   - Nothing supplied gives any "Executive" a grant.
5. **The planned slot and the B gap are misreported.** The subject never says that planned `slot-A` is present and accounted for. It labels B "missing" but never marks it as required coverage that stays unresolved.
   - Conjoin's planned-slot clause and RF-015 apply.
   - This is the lesser defect. It fails to record facts rather than stating something false, but the joined record still needs them.

**Smallest lawful repair (proposed only, not performed):** replace the body with:

```markdown
# Joined assessment

Subject: catalog/source-v1. Basis: contract-v1.
Overall result: falsified.
A: falsified — permission inferred from a display label; producer independent-observer/A/attempt-1; citation source/A.md#permission-branch.
B: required coverage uncovered; explicitly unresolved.
Planned slot slot-A is present (fixture-authenticated, not native runtime authentication proof).
This record conveys no repair, action or acceptance authority.
```

**Owner of the repair:** The producer of the joined summary, acting under the supplied grant "Review and propose a summary only." Whoever disposes of the result (accepts it or orders a contract fix) must be a decision owner the material actually names. It names none. The fix to `source/A.md` is a separate operation, and no supplied grant covers it.

- **Residual uncertainty:**
  - The subject hash is unverified.
  - No conjunction rule or decision owner is declared.
  - "Executive" is not identified anywhere in the supplied material.
- **Invalidation conditions:** Same as (1).
- **Consuming decision:** Not declared.

---

## Did the view alone suffice?

**Yes, for these two evaluations.** RF-005, RF-006, RF-012, RF-015, the Conjunction section, Evaluate and Conjoin covered every defect. I used no remembered law.

**Missing material relations (unresolved, not imported):**
- A declared Result Conjunction rule: which results are mandatory, the veto or defer rule, and who owns the decision.
- Any way to authenticate beyond the fixture, and to check `subject_sha256`.

**Limits:**
- These results cover only this fixture and these two texts.
- They make no claim about whether the method works as a whole.
- They decide no acceptance and perform no repair.
