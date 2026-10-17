# I5 comparative review: Codex and Claude standards realizations, architecture and decision consistency

**Subjects.** Common `4c340f7`, Codex `99f932c` (`codex/successor/standards/`), Claude `5da6bde` (`claude/standards/`).

**Reviewer.** Claude CLI, model `claude-opus-5-5`. This is the same model family as the Claude candidate. I have no knowledge of who authored either candidate, and I saw no author explanation or earlier review. Tools were read and search only; I made no edits and ran no commands.

## Comparative verdict

**Codex is the somewhat stronger current methodological basis on the matched architecture cases. Neither candidate is a qualified selection.**

- Codex settles more recurring decisions once, in a shared owner. The clearest example is how combined results report a failure next to a missing assessment.
- Codex also keeps generic and domain-specific definitions layered correctly, for example progress versus Product progress.
- Claude's strengths are real: better traceability from owners to consumers, a cleaner treatment of "not performed", and a stronger build-tenant owner. But Claude leaves one load-bearing decision, the reported value of a combined result, to every consumer and adopting project.
- The difference is moderate, not decisive. Several weaknesses are shared.

I did not use the difference in maturity as evidence. Claude says it is under construction (Claude `README.md`, preamble, lines 3–7) and openly lists an open obligation (Claude `FOUNDATIONS.md` §4 Assurance relations, Row 8, line 1174). I count neither against its design.

## Criteria and strengths

| | Codex | Claude |
|---|---|---|
| **C1 claim accounting** | Unresolved. Disposition records not read (outside sampled scope). | Unresolved. Per-member Source dispositions seen in a sample only (Claude `README.md` §Source dispositions, lines 170–189). |
| **C2 semantic conservation** | Unresolved (not available in this review). | Unresolved. |
| **C3 accepted replacements** | Unresolved. | Unresolved. |
| **C4 actual task use / context fit** | Unresolved. I make no claim from byte counts. | Unresolved. |
| **C5 discrimination and interpretation fidelity** | Unresolved. Owners reproduce the common discriminators on the sampled cases; the a_c interpretation was not read. | Unresolved, on the same basis. |
| **C6 governing reduction** | Indeterminate. Supporting witnesses only; no predecessor deciding-path comparison was done. | Indeterminate. Supporting witnesses only. |
| **Strength 1** | One fixed precedence for combining results: an authenticated falsification decides the combined result and missing coverage stays explicit. `FOUNDATIONS.md` §Result conjunction, lines 506–518. | Every owner row lists its consumers and says each consumer "decides nothing the owning section does not". `FOUNDATIONS.md` §4 Results, lines 985–1008; §Assurance relations, lines 1164–1177. |
| **Strength 2** | Performance (`performed` / `not_performed` / `unconfirmed`) and effect state are separate from the verdict, and consumers actually use them. Owner: `FOUNDATIONS.md` §Result algebra, lines 350–416. Consumers: `REFERENCE_FRAME_METHOD.md` lines 501–505, `ODD_METHOD.md` lines 1215–1221, `DESIGN_MODULE_METHOD.md` lines 1503–1505. | A required evaluation that was not performed simply has no result. That is the cleanest way to keep it apart from `indeterminate`. `FOUNDATIONS.md` §4 Results, lines 835–849 and 922–941. |
| **Strength 3** | One shared admissibility law ("Contract application", six conditions) reused at intake, evidence rules, design admission and frame activation. `TRANSFORMATION_LIBRARY.md` §Contract application, lines 115–185; consumed at `SPEC_METHOD.md` lines 1442–1450 and 2466–2477. | A dedicated build-tenant owner that permits human processes and direct observation. `SPEC_METHOD.md` §11 Build-tenant binding, lines 1801–1808 and 1928–1937. A strong recovery owner: the work state is an explicit object, resumption reconciles uncertain effects first, and three named invalidators replace the predecessor's differing lists. `ACTIVATION.md` §5, lines 1372–1388 and 1460–1507; §7, lines 1705–1748. |
| **Most consequential weakness** | Finding 4: one owner allows two representations of a check that was never run. Finding 3, shared, also applies. | Finding 1: the reported value of a combined result is left to each consumer and adopting project. |

## Ranked findings

### 1. Claude: combined-result reporting is left to consumers (moderate; affects reduction)

- **Where.** Claude `FOUNDATIONS.md` §4 Conjunction of results, "Reported value", lines 1088–1111: "no universal order among the non-satisfied values exists, and the member or profile that applies the conjunction declares its own". The Executive consumer passes the choice on again to the adopting project: Claude `EXECUTIVE_BASELINE.md` §Refinement and conjunction, lines 1087–1092.
- **Case.** Mandatory check A is authenticated `falsified`; mandatory check B has no result. Claude's owner fixes only that the combined result is not `satisfied`. Whether it reports `falsified` or `indeterminate` depends on a rule each consumer or project must declare.
- **Common obligation.** "Conjunction and composition of results are defined once, over the core" (`common/specification/requirements/README.md` §Single Result Algebra Requirement, item 6, lines 171). Also Foundational Reduction item 2: replace the independent decision at each consumer (line 63).
- **What is preserved.** A's failure does survive in the record (Claude `FOUNDATIONS.md` lines 1070–1080), so failure survival holds.
- **Consequence.** The deciding value is decided again at every combining consumer. Two projects can report different values for the same evidence.
- **Codex contrast.** Codex decides this once (finding cited in Strength 1, Codex `FOUNDATIONS.md` lines 506–518).

### 2. Claude: progress is defined two ways in tier-1 ACTIVATION (moderate)

- **Where.** Claude `ACTIVATION.md` §5 Work state and restart, lines 1406–1418, defines generic progress as "accepted material movement toward the selected outcome". The same member's §1 Construction relation, lines 295–305, defines progress as "the work moves towards Z on evidence".
- **Case.** An evidenced candidate that has not yet been accepted, or a bounded uncertainty-reducing step. Under §1 it counts as progress. Under §5 it fits none of the five categories (progress, prerequisite work, evidence that is not new progress, churn, forecast revision).
- **Common obligation.** Preservation, progress, termination and outcome satisfaction are distinct, and acceptance is separate from progress (`common/.../README.md` §Universal Construction Requirement, items 6–7, lines 112–113). Also single ownership (lines 139–147).
- **Codex contrast.** Codex layers this correctly. Generic progress is "supported movement" (Codex `FOUNDATIONS.md` §Bounded construction, line 979). "Accepted" applies only to Product progress (Codex `SPEC_METHOD.md` §Checkpoint, Continuation, Progress, And Churn, lines 2018–2024).

### 3. Shared: the four-cause diagnosis is not carried through to re-entry (moderate)

- **Codex.** `SPEC_METHOD.md` §Universal intake triage, lines 1414–1423, says to "bind the supported cause to the change classes below". The class list at lines 1458–1470 is purely layer-based. The procedure "When a real use case reveals a gap" (lines 3394–3403) still asks a two-way question: "missing implementation or a constitutional insufficiency?"
- **Claude.** The same pattern appears at `SPEC_METHOD.md` lines 836–844 (four causes), 866–888 (class table) and 1157–1168 (two-way gap analysis).
- **Case.** A test fails because its oracle is wrong (insufficient observation), or because a predictive model is wrong. The procedure forces an "implementation" or "constitutional" branch. No class names correction of an assertion or observation.
- **Common obligation.** Diagnosis distinguishes four causes, keeps unresolved alternatives open, and routes each supported repair to the affected owner (`common/.../README.md` §Universal Construction Requirement, item 4, line 110).
- **Workaround.** Both intake owners allow acquiring further observation first. Codex keeps more surrounding text (lines 1425–1450), which makes this route harder to read.

### 4. Codex: one owner allows two representations of a never-run check (low to moderate)

- **Where.** Codex `FOUNDATIONS.md` §Result algebra, lines 356–360 and 370–379.
- **Case.** A required check is known never to have run. The legal pairs allow a record with verdict `indeterminate` and performance `not_performed`. The same owner also says a missing required judgment "stays an absent coverage slot … not a fabricated child result".
- **Consequence.** The combined verdict is the same either way (`indeterminate`, rule 3 at line 514). However, any projection that carries only the verdict merges "not run" with "cannot decide". Codex forbids verdict-only handoff (line 389) but cannot enforce that on views.
- **Common obligation.** `common/.../README.md` §Single Result Algebra Requirement, item 3, line 167; `common/.../ASSURANCE.md` §Assertions And Observation, line 39.

### 5. Claude: software residue in generic consumers (low)

- **Where.** Claude `SPEC_METHOD.md` §Change classes, line 878: `realization_refactor` is a "local code, configuration or attribute change". The chain at lines 216–217 reads `Design → Code → Events`, and lines 248–251 say every realisation carries an "Events" responsibility.
- **What mitigates it.** Lines 228–251 and §11 (lines 1801–1808) scope Code, Events and Projection to the selected binding.
- **Case.** A human-process tenant revises one checklist step. The class text does not name that case. The chain also assumes a retained record where direct observation would suffice.
- **Common obligation.** `common/.../README.md` §Build-Tenant Binding Requirement, item 2, line 125.
- **Codex contrast.** Codex uses "implementation, procedure" (line 1465), `Realisation → Observations` (lines 1113–1116), and "adequate direct observation remains available" (line 3372).

### 6. Allowed differences, not defects

- Codex models effects with six values; Claude uses three, as a refinement in `ACTIVATION.md` §3 Effects (lines 1117–1155). Both keep unknown completion from mapping to "no effect" or "completed".
- Claude says resumption may "reconcile, yield or stop" (line 1388). Codex also allows an operation proven idempotent to be retried (Codex `FOUNDATIONS.md` lines 898–905). Both meet the common requirement.

## Matched cases with no material difference

Both owners satisfy the common source on these sampled cases:

- **Assertion necessity vs. sufficiency and observation sufficiency.** Codex `FOUNDATIONS.md` lines 634–696; Claude `FOUNDATIONS.md` lines 1232–1302.
- **Assertion vs. execution provenance and correlated error.** Codex lines 698–733; Claude lines 1304–1357. Claude adds that authenticating a returned assessment is a third thing, separate from both.
- **Quantified assurance.** Codex lines 735–783; Claude lines 1359–1409.
- **Change-based reassessment** (`S_Δ` selection and `E_new` evidence retention). Codex lines 785–843; Claude lines 1411–1492.
- **A-to-Z recovery from current workspace.** Codex lines 845–905; Claude `ACTIVATION.md` §5.

Claude's assurance owner restates the common text almost verbatim. Codex paraphrases it compactly. I count neither as a reduction witness.

## Recommendation, conditions and limits

**Recommendation.** Use Codex as the current comparison basis, on the condition that finding 3 is repaired. Use Claude's per-row consumer lists, its "not performed has no result" treatment and its §11 build-tenant owner as counterexamples Codex must match. This is not qualified selection: criteria 1–4 are unresolved and 5–6 are indeterminate.

**What would reverse it:**
- Claude fixes one precedence for combined results in FOUNDATIONS (or shows every deciding consumer declares the same one) and reconciles its two progress definitions.
- Or a fresh-use trial shows Codex's denser, layered intake text produces more misroutings than Claude's on the same cases.
- Or Codex consumers are found to pass only the verdict where `not_performed` matters.

**Limits:**
- I read selected sections only. I estimate roughly 330–370 KiB of presented text, counting search output. This is not instrumented.
- Elapsed time is unknown to me, since I had no clock.
- Not read: either a_c interpretation, any frame body, CONFORMANCE, Codex disposition and derivation records, Claude's frontier, the predecessor, and most profile members.
- Host and active-context conditions are unknown. Nothing here is evidence for criterion 4.
