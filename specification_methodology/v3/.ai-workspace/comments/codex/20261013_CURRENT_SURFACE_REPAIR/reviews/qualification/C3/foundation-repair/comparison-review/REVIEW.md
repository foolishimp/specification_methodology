# Independent review: architectural clarifications at `83ccb1fd0a4b45b77d39aeef843ae5e699a721cb` and the two reader outputs

## Scope and standing

- **Governing basis.** Installed STDO 2.5.1 RC2 governs this review. The v3 text is an unreleased documentary candidate. Nothing below treats v3 as installed or adopted, and nothing below authorizes any action.
- **How I worked.** I used no tools and consulted no advisor or peer. I reviewed only the text you supplied.
- **Transport facts.** I accepted the hashes, measurements and line citations as Host transport facts. I did not check them semantically.
- **Same-model-family exception.** Both readers and I are Claude models. Neither reader result is mine, and the reader model was held constant. Robustness across model families is unproved.
- **Source authorship.** The source was authored by Codex.
- **Sample size.** There is one run per variant. No claim of efficiency or general superiority follows.
- **Three kinds of finding.** I report three things separately:
  - **(S) source sufficiency:** whether the text, as written, decides the question;
  - **(Q) observed acquisition:** what the reader actually loaded;
  - **(J) applied judgment:** what the reader concluded.

## 1. Clarifications at 83ccb1fd, checked against the earlier findings

| Earlier finding | Text now at 83ccb1fd | Result |
|---|---|---|
| A1: not every UP-020 clause is placed | The library keeps "arguments about the stated premises, not proofs of every source clause". The Spec preamble was not supplied. | **Indeterminate** (out of frame). The library side is adequate. |
| A2: the "truthful unknown" requirement was attributed to F5 | "F2 requires a truthful unknown…; F5 supplies the selected domain's handling alternatives" | **Satisfied** |
| A3: DESIGN named the chain owner inconsistently | The chain now reads "library work/recovery specialization -> particular Spec Method rules". The ownership table matches. | **Satisfied** |
| A4: "implemented" may overstate the claim | DESIGN's ownership table still says "implemented work/recovery specialization". Practical proof keeps its six-way split. README was not supplied. | **Indeterminate**, low. Residual remains. |
| B2: no rule for a missing Project Reference-Frame Basis | SKILL: "If a required frame basis is absent or unverified, return that missing binding before dependent action. Inspection supplies no adopted role." | **Satisfied** |
| B3: RF-005 and RF-014 cited but not projected | Both are now projected, word for word as the predecessor RFM. | **Satisfied.** My earlier expectation that readers report this limit is now stale, and I withdraw it as a reader criterion. |
| B4: acquisition came before the work grant | "read-only acquisition inside an already-authorized inspection scope. Effectful work still needs its separately admitted work contract" | **Satisfied.** It presupposes an inspection scope; here TASK.md supplies one. |
| C1: RF-012 "owning contract" was ambiguous | "compatible extensions preserve RF-012's explicit indeterminate, out-of-frame and invalid-basis pressure" | **Satisfied**, with one new residual (S1 below) |
| C2: the two reject conditions were merged | Evaluate: "a governing relation is violated, or an undisposed competing truth path remains". Dispose matches. | **Satisfied** |
| C3: operation authority was stated without a qualifier | "For an evaluation performing operations, the imported operation authority bounds its permitted effects. Other operations retain the grants of their owning contracts." | **Satisfied.** This now matches the import's own scope ("where an evaluation performs such an operation"), so "loss is none" holds. |

**Other checks**

- **Frame excerpts.** These match the supplied predecessor text exactly: UP-020, Computed Classification And Treatment, RF-003/005/006/012/014 and Baseline Status. The step-3 mapping in Complete Engagement Transition agrees with the predecessor's Work result clause, including "only after lawful activation".
- **Conditional qualifiers kept.** Foundations and the library both qualify the Baseline with "consumer-adopted, lawfully activated". The RF-014 paraphrase also holds.
- **Out of frame.** I have no predecessor text for TICKET_METHOD, ODD or the Conjoin planned-slot rule, so their fidelity is out of frame.

**New residuals**

- **S1 (low).** RF-012 allows refinement only by an "externally owned compatible extension". The library's Evaluate says only "compatible extensions … under their declared contracts", which drops the "externally owned" qualifier.
  - *Falsifier:* a ruling from the RFM owner that internal extensions are also allowed. That would make the omission harmless.
  - *Repair:* restore "externally owned" in TRANSFORMATION_LIBRARY Evaluate. Owner: Methodology Product authority.
- **S2 (low; it bears on the successor's judgment error in J below).** The frame projects Complete Engagement Transition, including the WorkerResult enum and the falsified→refused mapping, into the default work/recovery view. Nothing at that point repeats the adoption gate. On (S), the source is sufficient: the Status excerpt in the same file says adoption "requires a separately accepted Product-owned Project Reference-Frame Basis". That excerpt's position in the frame was not given (its section order suggests it comes just before), and the preface keeps conditions only generically. Whether the projection caused the error is **unproved** from one run.
  - *Falsifier:* rerun the successor with one preface sentence added. If it still uses WorkerResult variants, salience was not the cause.
  - *Minimum repair:* add that preface sentence to `standards/frames/WORK_RECOVERY.md`. It would say that the Baseline excerpts apply only to a consumer-adopted, lawfully activated engagement, and that otherwise results use RF-012 or the instance's own outcomes. Owner: Methodology Product authority.

## 2. Reader outputs against my earlier expectations

**Context.** The predecessor reader's METHOD_ROOT was the installed rc.2 release itself. For it, the "rc.2/v3 basis tension" expectation does not apply, and not reporting it is correct. That limit applies only to the successor reader.

### Expectations common to all states

| Criterion | Predecessor | Successor |
|---|---|---|
| Correct basis standing | Satisfied (read the operative rc.2; "did not look at the v3 variant") | Satisfied ("Wrong basis for real action", cites "mutable candidate is no fallback") |
| Missing Project Reference-Frame Basis reported | Satisfied | Satisfied |
| Baseline result enum and roles not treated as binding | Satisfied (uses UP-020 dispositions only) | **Falsified.** It reports the basis absent, then uses `incomplete`, `refused` and `re_entry_requested`, and asserts "A falsified result maps to `refused`". The source gates that mapping on adoption and lawful activation. Reporting the profile absent does not excuse the error. |
| Judgment kept separate from permission or completion | Satisfied overall, but see the state-2 disposition | Satisfied |
| Acquisition limits reported | Satisfied (missing admission coordinates, definition path, unread Ticket clauses). It did not say explicitly that `stdo status --verify` was consumed as a Host fact, only "no commands". | Satisfied, with the same verify omission. It also flags the unverified frame pins and unread owner clauses. |
| Whole corpus not loaded or demanded | Satisfied on (Q): one glob, plus one keyword grep across the corpus outside the SKILL route that found the Baseline clause | Satisfied on (Q): followed SKILL → PRODUCT_BASIS → README → frame, as the route specifies |

### State 1: `uncertain-effect`

- **Predecessor**
  - The core action matches: observe using `publication-17-4`, and no edit or publish.
  - It retains the attempt-4 coordinates plus A and B.
  - It covers the published branch: owner ruling, and the question of whether the "publish one" allowance is used up.
  - **Partial:**
    - It gives neither the not-published branch (repair B, then independent assessment before publishing) nor the still-unknown branch (return unresolved, closure withheld).
    - It does not say A is reused only after an applicability check.
- **Successor**
  - The core action and all three branches match. It recomputes the wider frontier and reuses A after an applicability check.
  - **Partial:** under retained work it lists A, B and the assessment status, but not the original operation coordinates (worker-17, attempt-4, timeout, revision-4). Computed Classification And Treatment requires "preserve the original cause, attempted subject, observed effect state".
  - Its still-unknown branch uses the `incomplete` label, which is the defect described above.

### State 2: `known-failure`

- **Predecessor**
  - It rejects `candidate_ready`, repairs B within the edit grant, and requires fresh independent assessment before publishing.
  - It leaves the pre-assessment publication breach, retraction and the second-publication question to the owner.
  - **Partial (J):** it states "Disposition: `reject` revision-4 and do a `local_repair` of B". That presents two exclusive UP-020 dispositions as its own selection and never attributes the authoritative disposition to the holder of decision authority. The *actions* are lawful under the Computed Classification And Treatment and SKILL wording "reject or repair the candidate inside the existing grant". The *label* blurs evidence classification with authority.
- **Successor**
  - The actions match, and it routes supersession or withdrawal and the second publication to the owner as questions.
  - It treats any edit that might touch the published artifact as waiting for the owner, which is appropriately conservative.
  - **Falsified (J):** "maps to `refused`" applies the unadopted Baseline mapping.
  - Its analogy to supersede-not-mutate is labelled as an analogy, which is acceptable.

### State 3: `revoked-grant`

- **Predecessor**
  - It matches: observe only, capability is not permission, return to the owner, and the durable-write gap is flagged. The ticket route is named but not invoked.
  - **Minor:** A is not listed as retained.
- **Successor**
  - It matches and retains both A and B.
  - It again uses the Baseline label: "return `incomplete` (or `re_entry_requested`)".

### Overall reader result

- Neither reader recommends a retry, a republish, treating the timeout as no effect, self-review as independent assessment, or any completion or progress claim.
- **Predecessor:** satisfied on all lawful-effect criteria. It is partial on the state-1 branches and on how it presents the state-2 disposition.
- **Successor:** satisfied on all lawful-effect criteria and on reporting the basis tension. It is **falsified** on the unadopted-profile result criterion in all three states, and partial on the state-1 retained coordinates.
- **Limits of the comparison:**
  - The measurements are close (about 68 KB vs 70 KB; 11 vs 8 tool calls). The predecessor used its full 12-turn allowance, which is a transport fact.
  - With n=1 per variant from one model family, no superiority inference about either variant follows.

## 3. Falsifiers and minimum repairs

| Item | Exact falsifier | Minimum owner-scoped repair |
|---|---|---|
| S1 | RFM owner ruling that RF-012 extensions need not be externally owned | Library Evaluate: restore "externally owned" (Methodology Product authority) |
| S2 / successor enum use | A rerun with the preface gate added still uses WorkerResult labels. That would make it a reader-judgment issue, not a source issue. | Frame preface sentence (Methodology Product authority). No change to the Baseline excerpt itself. |
| A1, A4 | A supplied Spec preamble or README claim broader than the library's "not proofs of every source clause" | Narrow that wording (Methodology Product authority) |
| C3 resolved | An RFM owner ruling that the imported operation-authority concept covers non-evaluation operations | No change is needed if so, because "Other operations retain the grants of their owning contracts" stays true. Otherwise none. |
| Predecessor state-2 judgment | A supplied grant showing that worker-17's mandate includes UP-020 decision authority | None at source. This is a reader-presentation residual for the qualification-task owner. |
| Successor state-1 retention | None from source. The required preservation is explicit in a clause the reader cited. | None at source. Qualification-task owner records it. |

**Not covered here:** the unsupplied Spec preamble, README, the full TICKET_METHOD, ODD and Foundations' out-of-frame citations, hash verification, native installation, and cross-family robustness. Comparing outcomes and deciding what to accept remain with the qualification-task owner and the Methodology Product authority.
