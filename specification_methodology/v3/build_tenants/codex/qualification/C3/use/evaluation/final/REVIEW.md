# Evaluation of summary.md under the Evaluation and Conjunction Frame

I used only the selected view and the supplied task material. I called no tools.

## Binding
- **Subject and basis:** `catalog/source-v1`, `contract-v1`. Both summaries name these correctly, so neither result is `invalid_basis`.
- **Required coverage:** A and B.
- **Planned slots:** only `slot-A`. It is admitted, and its producer, subject, basis and coverage A are bound to this fixture.
- **Conjunction rule:** A required `falsified` result blocks a `satisfied` outcome. Every known finding, its producer and its citations must be kept. B stays separately unresolved. No judgment for B may be invented.
- **Authority:** I may review and propose a summary only. I have no authority to accept anything or to edit the public contract.

## 1. Baseline adequacy: `satisfied`
The baseline meets every predicate this view sets for this task:
- **Overall result:** it keeps "Overall result falsified", as the conjunction rule requires (Conjoin; RF "Result Conjunction").
- **Finding A:** it keeps the finding ("permission inferred from a display label"), the producer `independent-observer/A/attempt-1` and the citation `source/A.md#permission-branch`. Conjoin requires each known failure to be kept with "its producer and citations".
- **Coverage B:** it states B as "uncovered, explicitly unresolved", kept separately and with no invented judgment (Conjoin; RF-015).
- **Planned slot:** it records that planned slot A is present (Conjoin, planned-slot authentication).
- **Authority:** it states that it "conveys no action or acceptance authority" (RF-006; Evaluate).

The source observation is consistent with the slot-A finding. "A display label authorizes publication" contradicts "A display label must confer no operation authority". I only checked consistency here; I did not re-judge A.

## 2. Defective subject adequacy: `falsified`
Each line below is quoted from the defective subject and is a counterexample:

1. **"Overall result: indeterminate."** A required `falsified` result was supplied, so the conjunction rule makes the overall result `falsified`. Indeterminacy cannot replace a known counterexample. Violates the conjunction_rule, Conjoin and RF "Result Conjunction": "Common agreement cannot discard a constraint or material counterexample found by only one contributor."
2. **"Findings: none."** This erases the slot-A finding, its producer and its citation. Violates Conjoin ("Retain each applicable known failure, its producer and citations") and the conjunction_rule ("all applicable known findings/lineage/citations survive").
3. **"Coverage B is missing; therefore earlier findings have been discarded."** This inference is unlawful. Uncovered coverage must be kept *separately* and cannot cancel an existing finding. Violates Conjoin ("Retain required uncovered coverage separately") and RF-015. It also never states that B is unresolved, and it drops the record that planned slot A is present.
4. **"The Executive may now fix the public contract."** This creates repair authority from an assessment result. Violates:
   - RF-006 (Authority Conservation);
   - Evaluate ("A judgment supplies no repair, acceptance or next-action authority");
   - the frame scope ("supplies no acceptance or repair grant");
   - the operation_grant ("No public contract edit");
   - the consuming_decision: the Executive may act on "this bounded fixture proof only", and upstream changes are reserved.

## Smallest lawful repair
Replace the subject's text with the following summary. It adds no assessment or grant beyond what was supplied:

```markdown
# Joined assessment

Subject catalog/source-v1; basis contract-v1. Overall result falsified.
A: falsified, permission inferred from a display label; producer independent-observer/A/attempt-1; citation source/A.md#permission-branch.
B: required coverage uncovered, explicitly unresolved. Planned slot A is present.
This record conveys no action or acceptance authority.
```

- **Who makes the change:** the Codex C3 fixture Writer, under its tenant-only grant.
- **Who decides:** the Codex C3 Executive decides whether to accept or repair this bounded fixture proof.
- This is a proposal only. I made no edits and decided nothing about acceptance.

## Scope sufficiency
The view was enough to decide both results:
- It supplies the conjunction rule and the rules for keeping findings, uncovered coverage and authority.
- No material relation fell outside the frame, so I did not need `out_of_frame`.
- B was not judged and remains unresolved, not satisfied. Neither result supports a wider "satisfied" claim for the Product.
- The UP-020 assessor-disposition field was not invoked by the task, so I made no disposition classification.

## Unresolved evidence and limits
- **Digests not checked:** I could not reacquire or compute `subject_sha256` (`4f973d76…`), the subject commit `427a0de…` or the owner digests. I relied on the host Writer's check before dispatch, as the measurement_limit states.
- **Authentication:** slot A is authenticated only by the fixture bytes, not by a native runtime proof.
- **Coverage B:** it has no planned slot and no result, so it remains open.
- **Fit:** the inputs fit within the 40,000-byte / 180-second envelope.
