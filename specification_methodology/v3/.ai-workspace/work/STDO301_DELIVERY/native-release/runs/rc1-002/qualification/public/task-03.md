# Task 03: whether a handover reference is enough for the next first assessment

**Short answer.** In U, the next action is to perform the first assessment. In I, no first assessment is allowed: the closed indeterminate result stays on record, and any follow-up goes only through the policy's own re-entry contract. The handover that carries only `(d,b,false)` is not enough for this decision, because U and I give the same record but need opposite actions. The handover with a qualified reference is enough, but only under the conditions listed below. One extra field is the smallest distinction I can argue for: the first-assessment standing, which is either "none performed" or "closed: indeterminate". A digest or a typed annotation cannot carry that standing.

Paths are relative to the installed root. Clauses from the method's governing documents decide. `examples/DETERMINISTIC_CONTRACTS.md` is cited only as an illustration: it says of itself that it carries "no generic law or acceptance authority" (`standards/README.md:66`).

## 1. Next first-assessment action

| State | Decision | Installed support |
|---|---|---|
| **U** (nothing performed) | **Perform the first assessment of (d,b).** The chance to do it has not been used. | An evaluation that was not performed "has no closed result" and "is never mapped to `indeterminate` or to any other core value" (`standards/FOUNDATIONS.md:773-776`, `:780-787`). It is carried in the work state as an open residual, not as a result (`standards/ACTIVATION.md:1029-1032`). |
| **I** (closed, indeterminate) | **Do not perform a first assessment.** The fixed policy says it has been used. Keep the closed result. Follow-up is only possible under the separate re-entry contract. | `indeterminate` is a performed judgment meaning the admissible evidence cannot decide (`standards/FOUNDATIONS.md:739`, `:1188-1190`). It names what would decide (`:761-764`) and never maps to `satisfied` (`:771-772`). |

- **Same observation, different decisions.** U and I both answer "satisfied exists = false" but need incompatible decisions. That is exactly the case where an observation "cannot support a sound complete decision" (`standards/FOUNDATIONS.md:1224-1227`). The installed core keeps these states apart so that "none of these can be mistaken for another" (`standards/FOUNDATIONS.md:747-749`).
- **Proving U.** U has to be established from the workspace, the surface that records what has and has not been done (`standards/ACTIVATION.md:1460-1462`). Not finding a record does not prove U: "A missing trace … shows neither that work was not done…" (`standards/ACTIVATION.md:1487-1489`).
- **Checks before relying on I.**
  - Check the three invalidators: a material input change, a changed basis, or an observation the result itself names as revising it (`standards/ACTIVATION.md:1707-1727`).
  - An unchanged d does not rule these out (`:1709-1711`).
  - New admissible evidence that could decide the question counts as a material input change (`:1718-1723`).

## 2. Handover 1: `(d,b,false)`

**Not sufficient for this decision. The method's test fails.**
- U and I map to the same record but need different decisions, which "falsif[ies] the sufficiency claim" (`standards/FOUNDATIONS.md:1238-1240`).
- No decision rule working on the record alone can reproduce the decision on the real states (`standards/FOUNDATIONS.md:1243-1248`).
- A record that is not sufficient "is a residual, not success" (`standards/FOUNDATIONS.md:655-657`).

**What the receiver should do.** Neither assess nor refuse on the strength of this record. Fetch the assessment state for (d,b) from the workspace (`standards/ACTIVATION.md:1471-1479`; `standards/FOUNDATIONS.md:1224-1226`). If the receiver's grant does not allow that, stop and name the owner who can supply it, as `re_entry_requested(authority)` (`standards/ACTIVATION.md:1479-1482`, `:828-833`).

**Where it is enough.** For a consumer whose only question is "can I rely on a satisfied assessment?", the answer is "no" either way, so the record is enough there. Sufficiency is judged per question, never universally (`standards/ACTIVATION.md:825-828`).

## 3. Handover 2: exact accessible reference to the complete qualified record

**Sufficient for I's next step, under conditions.** This matches the installed guidance on qualified references (`standards/ACTIVATION.md:695-706`): "a reference can supply sufficient context when its accessible target and qualifications preserve the consuming contract".

The conditions:
1. **The reference resolves.** It must resolve exactly once (AC-003, `standards/AXIOMATIC_CALCULUS.md:502-507`). Its target must be present and on the current basis. Otherwise it is a residual (`standards/FOUNDATIONS.md:657`).
2. **The policy version is pinned.** The installed check list includes "active obligation and version" (`standards/ACTIVATION.md:699-701`), which the task's list does not name. It is covered only if b is an exact basis in the method's sense, which includes version and configuration coordinates (`standards/FOUNDATIONS.md:70`). Otherwise this is an open check.
3. **Authority is covered.** I assume "material provenance" includes the producer and the assessor's authority. I did not read the authority-conservation law (AC-005), so this is an assumption.
4. **Invalidators have not fired.** This is checked at the time of reliance (`standards/ACTIVATION.md:1707-1716`).
5. **Hash assumptions are stated.** If exactness rests on hash matching, the collision and access assumptions must be written down (`standards/ACTIVATION.md:708-709`).

**What it does not need.** It does not need the assessor's internal working context (`standards/ACTIVATION.md:1686-1689`). It does not need a full-history scan (`:1697-1698`).

**For U** (my interpretation). There is no assessment record to point to. Handover 2 works for U only if its target is a current work-state entry that positively states that no closed assessment exists for (d,b). A reference that resolves to nothing does not establish U. The example agrees that missing or stale targets give "no usable record" (`examples/DETERMINISTIC_CONTRACTS.md:139-141`).

## 4. Smallest record distinction for these two cases

```
U:  subject: d | basis: b | first assessment: none performed (no closed result)
I:  subject: d | basis: b | first assessment: closed — result: indeterminate | record: <exact reference>
```

**Why one field is enough.**
- It is necessary: `(d,b,false)` gives U and I the same record, so at least one more distinction is required.
- It is enough: with this field, the first-assessment decision follows from the record alone (U → assess; I → no first assessment, use the re-entry contract).
- "Satisfied exists: false" can be derived from it, so it does not need to be carried.
- The `record:` reference is not needed for the first-assessment decision itself. It becomes necessary once I's follow-up or reliance is the question, because that needs what would decide and the invalidators.
- "None performed" describes the state of the work; it is not a result value (`standards/FOUNDATIONS.md:887`).

**Limits of this claim.**
- **Scope.** It holds only for the fixed policy, unchanged d and b, these two cases, and the first-assessment decision. It is not a general sufficiency claim (`standards/FOUNDATIONS.md:1240-1241`).
- **"Smallest".** It means only the fewest added distinctions in the sense argued above. It says nothing about minimal bytes, context or cost; that would need its own objective and evidence (`standards/FOUNDATIONS.md:1264-1267`; `standards/AXIOMATIC_CALCULUS.md:665-666`).
- **Larger domain.** If F, `out_of_frame` or `invalid_basis` are possible, the field needs "none performed" plus all five core values (`standards/FOUNDATIONS.md:735-741`), along with any refined domain outcome (`:751-756`).
- **Correctness.** It does not establish that the indeterminate judgment, or the observations behind it, were correct (`standards/FOUNDATIONS.md:1203-1212`).
- **Freshness.** A U record is a snapshot and goes stale as soon as an assessment closes. Exactness over several steps follows only in a closed domain; approximations need a stated horizon (`standards/FOUNDATIONS.md:1257-1258`).
- **Follow-up.** It does not settle the re-entry follow-up, because that contract was not supplied.

## 5. Human handover

The same fields work as plain sentences. No software, registry or event log is needed:
- the work-state law requires no particular carrier (`standards/ACTIVATION.md:1375-1379`, `:703`);
- there is no obligation to replay history (`standards/ACTIVATION.md:1499-1500`);
- Markdown is a sufficient carrier for a result (`standards/REFERENCE_FRAME.md:1041-1044`).

Example wording:
- **U:** "d on basis b: the first assessment has NOT been performed; no closed result exists (checked in <where>, <when>). Perform it."
- **I:** "d on basis b: the first assessment WAS performed and closed, and the result was INDETERMINATE (not failed, not pending). Record: <location>. What would decide: <…>. It is void if <…>. Do not repeat the first assessment; any follow-up goes only under <re-entry contract>."

Avoid labels such as "not approved". They collapse U and I, which `examples/DETERMINISTIC_CONTRACTS.md:100-102` illustrates; the governing ground is `standards/FOUNDATIONS.md:1238-1240`. A human reader may draw different conclusions from the same observation (`standards/FOUNDATIONS.md:1186-1188`), so the standing must be stated outright, not left to inference. If a human decides on re-entry, they need an exact identity, grant and decision contract; being present gives no authority (`standards/AXIOMATIC_CALCULUS.md:1015-1017`).

## 6. What a digest or typed annotation alone can establish

**A stable digest d can establish:**
- the identity of the candidate bytes, under stated collision, authenticity and access assumptions (`standards/ACTIVATION.md:708-709`);
- that the selected text is authentic (`standards/FOUNDATIONS.md:1166-1167`);
- whether a derived copy is stale relative to its sources (`standards/ACTIVATION.md:907-912`).

**A digest cannot establish:**
- whether an assessment happened, or its standing: a candidate-only pointer loses the satisfied/indeterminate distinction (`standards/ACTIVATION.md:705-708`);
- faithfulness or sufficiency (`standards/ACTIVATION.md:919-922`);
- that nothing has been invalidated (`standards/ACTIVATION.md:1709-1711`);
- equality of basis (`standards/REFERENCE_FRAME.md:316-317`).

**A typed annotation:**
- It can declare which kind of value a field holds, as a claim that helps route and parse.
- It "supplies no evidence of sufficiency by itself" (`standards/ACTIVATION.md:701-702`). Storage, schema or name establish no boundary or sufficiency (`standards/IDENTITY.md:146-151`).
- It cannot supply missing standing (`examples/DETERMINISTIC_CONTRACTS.md:130-131`).

## 7. Gaps and uncertainty

- **Re-entry contract.** Its terms were not supplied, and the installed method does not own them. So whether follow-up from I is available, and on what conditions, is undetermined.
- **Invalidated I.** Whether invalidating I gives back a first-assessment opportunity is not settled by the installed method. Invalidation withdraws a result from reliance and keeps its predecessor/successor relation (`standards/ACTIVATION.md:1709-1712`). My reading is that the opportunity stays used, but that is an interpretation.
- **Policy version and authority** in handover 2 are open (points 2 and 3 in section 3).
- **What I did not do.** I ran no structural check, did not verify any digest, manifest or installed bytes, and did not run `deterministic_contracts.py`. The transport proofs in the task say nothing about meaning. This is a logical-review assessment; no actual handover was used.

## 8. Routes actually used

- **Entry:** `standards/README.md:21,23,38`.
- **FOUNDATIONS:** `:70-71`, `:640-787`, `:887`, `:1161-1267`.
- **ACTIVATION:** `:693-714`, `:808-833`, `:902-926`, `:1002-1039`, `:1170-1181`, `:1370-1517`, `:1681-1748`.
- **AXIOMATIC_CALCULUS:** `:500-507`, `:651-695`, `:995-1017`, `:1081-1084`, `:1095-1115`.
- **REFERENCE_FRAME** (reached through owner links): `:296-320`, `:389-402`, `:1039-1143`.
- **IDENTITY:** `:144-165`.
- **Example:** `examples/DETERMINISTIC_CONTRACTS.md:1-16, 85-153`, read as illustration only.
- **Locating:** Grep and Glob within the installed root.
- **Not read:** TICKETS, EVALUATION, GLOSSARY, the frames, the plugins, `manifest.json`, and the Python program.
- **Tools and resources:** about 22 Read/Glob/Grep calls and no shell. Spend was under about USD 1 by the running counter. Elapsed time was not measured by me.
