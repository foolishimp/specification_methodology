**Q6 does not meet H6’s distribution condition. The combined result is `falsified`, and the proposed disposition is to withhold distributable status pending repair and sufficient evidence.** This is an assessment and proposal; no distribution decision or action is authorized.

**Frame evaluation result — T1**

- **Frame:** `run://T1/frame`, selecting `TRANSFORMATION_LIBRARY.evaluate` and `TRANSFORMATION_LIBRARY.conjoin`; frame SHA-256 `844cca7fb85b18218a3e60d9b35305b29e8e3e857f6237ca825bbb1b41eec02f`.
- **Activation:** T1, bounded source-candidate assessment.
- **Subject and basis:** Workshop Reporting Method r6, clauses H6 and D6, and report Q6.
- **Authority:** H6 supplies the specimen’s distribution conditions. This actor may assess the supplied clauses and records and propose a disposition. It has no distribution authority.
- **Composite predicate:** All three checks required by H6 have succeeded for Q6’s report revision.
- **Core result:** `falsified`.
- **Performance:** `performed` for this review and conjunction; component performance remains separately recorded.

H6 requires the conjunction of checksum integrity, reader access, and empty-section handling, each successfully checked for the same report revision. D6 makes checksum success sufficient to mark the report distributable. **D6 therefore weakens its owner’s requirement:** it allows marking despite failed or unassessed access and empty-section handling. The predicate “D6 preserves H6’s distribution conditions” is `falsified`, established by comparing the two supplied clauses. This clause defect exists independently of the defects in Q6’s returned records. [Task: H6, D6; M2, M4]

| Item | Assessment and preserved evidence | Standing for Q6/H6 |
|---|---|---|
| **R-access** | Producer P1, subject Q6, and basis H6 match A-access. Preserve original outcome **“failed”** and E-access: an unauthenticated public reader retrieved Q6’s staff-only annex. | The required reader-access predicate is **`falsified`**. Performance is **`performed`** to the observed extent of the access check. Authentication here means the supplied packet’s producer/subject/basis/plan match; no independent verification of external records was performed. |
| **R-checksum** | Producer P2 matches A-checksum, but the returned subject and basis are **Q5/H5**, whereas the plan requires **Q6/H6**. Preserve original outcome **“passed”** and E-checksum: all checksums matched for Q5. | The offered binding to Q6/H6 is **`invalid_basis`**. This diagnosis was performed in the current review; it does not establish that Q6’s checksum evaluation ran. The Q5 claim cannot discharge Q6’s obligation. |
| **A-checksum’s intended Q6/H6 judgment** | No authentic Q6/H6 checksum judgment is supplied after rejecting the mismatched contribution. | A **missing planned judgment**, with intended evaluation performance **`unconfirmed`**. It is retained as an absent slot, without inventing a producer return or claiming that the check never ran. |
| **Empty-section handling** | Required by H6, expressly outside the two planned assessments, with no supplied observation or assessment. | **Required coverage outside the plan remains uncovered.** No child result is invented. Execution is unconfirmed; this is neither established non-applicability nor a successful check. |

These distinctions follow the exact-subject result contract and the conjunction owner’s separate treatment of invalid contributions, missing planned judgments, and required coverage outside the plan. [Task: assessment plan, R-access/E-access, R-checksum/E-checksum, empty-section statement; M1, M2, M3, M4, M5]

The composite subject Q6 and governing condition H6 are interpretable. R-checksum’s mismatch does not make the whole composite uninterpretable. Under the declared conjunction rule, an authenticated applicable failure of one required predicate establishes **`falsified`**, while the other gaps remain visible. Thus the access failure decides the current conjunction; the checksum mismatch and empty-section gap neither erase that failure nor become successes. [M2]

**Effects and limits of the finding.** E-access reports a completed public retrieval of the staff-only annex at that observation boundary. The wider extent of disclosure or report distribution is **unknown**. The record does not establish that the whole report was formally distributed, that exposure has been contained, or that any repair occurred. This actor undertook a response-only assessment and no report mutation or distribution operation. Evidence of retrieval supplies no distribution authority. [Task: E-access and authority; M1, M6]

**Proposed disposition and repair**

1. Withhold Q6’s distributable status under H6.
2. Replace D6’s checksum-only gate with an owner-preserving reference, for example:
   **“Mark a report revision distributable only when every check required by H6 has succeeded for that same revision, supported by admissible evidence for each required check.”**
3. Address the demonstrated staff-only annex access failure and obtain a successful access assessment for the exact resulting report revision.
4. Obtain the intended checksum assessment on that same revision under its applicable basis; retain the Q5/H5 record in its original scope.
5. Add the missing empty-section obligation to the assessment coverage and obtain its result.
6. Reapply the full H6 conjunction and submit the result to the authority that owns any subsequent distribution decision.

These are proposed actions. A changed report revision, governing clause, access configuration, or evidence basis requires reconsidering the affected judgments. Any claim that new evidence supersedes the demonstrated access failure must identify the supported repair and reassessment; a later timestamp alone is insufficient. [M2, M3, M6]

**Actual source locators**

- **Task:** `task` — H6, D6, assessment plan, both returned records and evidence descriptions, empty-section exclusion, and authority.
- **Selected frame:** `run://T1/frame` — `TRANSFORMATION_LIBRARY.evaluate`, `TRANSFORMATION_LIBRARY.conjoin`, and their declared owner dependencies.
- **M1:** `run://T1/method/standards/FOUNDATIONS.md#result-algebra`
- **M2:** `run://T1/method/standards/FOUNDATIONS.md#result-conjunction`
- **M3:** `run://T1/method/standards/TRANSFORMATION_LIBRARY.md#evaluate`
- **M4:** `run://T1/method/standards/TRANSFORMATION_LIBRARY.md#conjoin`
- **M5:** `run://T1/method/standards/REFERENCE_FRAME_METHOD.md`, acquired lines 344–485, particularly RF-005 and RF-012.
- **M6:** `run://T1/method/standards/FOUNDATIONS.md#judgment-and-authority` and the acquired RF-006/RF-007 clauses.
- **Result form:** `run://T1/method/standards/REFERENCE_FRAME_METHOD.md#minimal-evaluation-result`

**Acquisition and observed limits**

| Declared route | Supplied full-resource bytes | Acquisition |
|---|---:|---|
| `task` | 2,236 | Full, once |
| `run://T1/frame` | 252,846 | Full, twice; second read parsed and filtered in memory |
| `run://T1/method/standards/FOUNDATIONS.md` | 46,866 | Sections `result-algebra`, `result-conjunction`, `judgment-and-authority` |
| `run://T1/method/standards/TRANSFORMATION_LIBRARY.md` | 28,064 | Sections `conjoin`, `evaluate` |
| `run://T1/method/standards/REFERENCE_FRAME_METHOD.md` | 67,377 | Full read filtered to headings; subsequent lines 344–485 and section `minimal-evaluation-result` |

The catalogued task/frame/method resources total **397,389 supplied bytes**. Control routes `catalog` and `measurements` were also read once each. No case routes were listed.

The single near-completion measurement reported **606,243 cumulative acquired bytes before that measurement report**, including repeated acquisitions, against **1,044,152 bytes** allowed; **129.114 seconds** elapsed against **600 seconds** allowed. The final response’s subsequent generation time is not included in that observation.

The supported active/retained-context bound and native spend are **unknown**; the reader reported **zero additional paid calls**. Host retention, inference context, and native spend are uninstrumented. Large frame outputs were truncated in the host display, so the decisive rules above were acquired directly through their owner sections. The acquisition-byte count is not a measurement of retained model context.

The requested review and proposed disposition are complete. Actual repair, reassessment, and distribution remain outside this activation’s authority.
