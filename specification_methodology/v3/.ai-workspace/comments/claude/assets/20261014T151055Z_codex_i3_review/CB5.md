# CB5 — Cross-family review of Codex I3: actual use, evidence process, acceptance status and process

Reviewer: a Claude activation, a different model family from the Codex author, the actors, the oracle author and the grader. It has read access only and no repair grant. It did not read the Claude candidate or the sibling findings files in this directory.

Subject: `build_tenants/codex/` at `3aaa2f2`. Evidence: tenant commits `cb14a63` (trial inputs), `6627800` (frozen actor returns) and `939ce0c` (assessment and return), plus main through `2f93f78` (ticket, work list, return post, review posts). Common contract: PRODUCT.md at `355aa86` (C3 Construction Contract, Independence, Limits, Development Isolation). Expectations read first: part A (H4, M4), part B group (i), CR5.

Standing: commentary. It accepts nothing and disposes nothing.

Copy integrity:
- The scratch subject matches `git ls-tree -r 3aaa2f2` for all 1,700 entries: 1,698 blobs by hash and 2 symlinks.
- `git diff 3aaa2f2 939ce0c` touches only `build_tenants/codex/qualification/`.
- Arm C's materialised method equals `3aaa2f2:…/successor/` for all 89 members, by SHA-256 (`arms/C/ACTIVATION.json`).

## Summary

The I3 evidence process is materially better than iteration 2:
- a nonauthor oracle was frozen before any actor ran;
- the actor prompt is neutral;
- every claimed run is graded;
- reviewers acquired their own sources and recorded expectations first;
- no verdict was rewritten.

The return claims no acceptance and states its limits truthfully.

Criterion 4 is still not evidenced:
- The one trial on the frozen frames started each actor at `stdo-work/SKILL.md`, not on a frame. One context ran all six tasks.
- Arm C read 6–74% of each frame. No frame's declared scope covers the domain-binding task, and arm C answered it without DOMAIN_BINDING.
- No activation declared a context limit.
- Every one of the 30 graded assertions is decided by rules stated in the fixture text. All three arms score 30/30, rc.2 included, and there is no no-method control. The trial therefore cannot attribute success to frame content.
- Standalone freshness is not established.
- The grader, who is also the oracle author, is the author's model family. Its grading is called "independent" without the same-family exception that PRODUCT Independence requires of a Reviewer. The nonauthor oracle itself meets PRODUCT's test for independently specified expectations.

## 1. Actual use (H4; criterion 4)

### 1.1 Subject, timing and frozen bytes

| Event | UTC | Evidence |
|---|---|---|
| Frames, plugin entry and standards README unchanged from `f2cb3e5` onward | 10:35:54 | `git diff f2cb3e5 3aaa2f2` is empty for `frames/`, `plugins/`, `standards/README.md` |
| Oracle author begins; oracle and packet frozen | 10:38:43; 10:51:58 | `oracle/attempt-02/ACTIVATION.json`, `FREEZE.json` |
| Oracle committed in tenant (`fe4fcbe`) | 10:56:50 | `git log` on `ORACLE.json`; bytes unchanged through `939ce0c` |
| Package frozen (`3aaa2f2`); trial inputs recorded (`cb14a63`) | 12:52:03; 12:53:35 | commit log |
| Actors dispatched, A/B then C | 12:54:27; 12:57:58 | `harness/DISPATCH.json` |
| Returns observed; frozen (`6627800`) | 13:11–13:18; 13:18:51 | `DISPATCH.json`; `arms/` unchanged `6627800..939ce0c` |
| Grading | 13:20:19–13:38:40 | `assessment/native-use-grading-01/CLOSURE.json` |

The oracle precedes every actor by about two hours. The frame bytes and entry route the actors used were frozen before the oracle existed. While the oracle sat in the author's territory, later construction changed only the two compression summaries and `interpretation/`, and arm C read neither. Oracle exposure could not have shaped the frames. Arm C's frame bytes are `3aaa2f2`'s.

### 1.2 Trial design

Design facts:
- Three arms: installed rc.2 (71 members), preceding Codex `3ad1fca` (80) and current `3aaa2f2` (89).
- Every arm received the same packet, `d6f7bcba…`.
- Prompts are identical except for arm letter and paths (`diff arms/A/ACTOR_PROMPT.md arms/C/ACTOR_PROMPT.md`).
- One logger served all arms. Each actor entered at its arm's `plugins/spec/skills/stdo-work/SKILL.md`.
- One native context per arm ran all six tasks: "One fresh native context per arm, reused across six tasks" (`DISPATCH.json` limits).
- The model was inherited from the parent with no override. The actors are the author's family.
- There was one pass per arm.

Controls absent:
- no repetition;
- no no-method arm;
- no blinding of the grader;
- no cross-family actor;
- no control of host load.

The comparison subjects are the two that EC-CODEX-I3-02 fixed before reconstruction, so the arms were not chosen after seeing results. The emission totals recompute from the logs: 235,739 / 339,549 / 284,930 bytes. C is 16.1% below B and 20.9% above A.

### 1.3 Frames exercised (arm C, from `arms/C/ACQUISITION.jsonl`)

Arm C listed `standards/frames`, ran a heading search over all six frames, and then read line ranges and sections. Unique coverage, recomputed from the logged ranges against the `3aaa2f2` bytes:

| Frame (bytes) | Unique lines read | Bytes read |
|---|---:|---:|
| EVALUATION_CONJUNCTION (44,141) | 536/738 | 74% |
| CONSTITUTIONAL_DERIVATION (69,445) | 476/1,106 | 42% |
| TRIAGE_CARRIER (81,733) | 562/1,320 | 41% |
| RELEASE_ADOPTION (46,999) | 211/750 | 26% |
| WORK_RECOVERY (63,001) | 184/993 | 21% |
| DOMAIN_BINDING (54,985) | 55/937 | 6% |

Arm C also read owner sections directly.
- FOUNDATIONS `configuration` and TRANSFORMATION_LIBRARY `composition-law` are linked from frame text, so they are declared routes.
- FOUNDATIONS `judgment-and-authority`, `typed-composition-and-conservation` and `construction-and-use`, and SPEC_METHOD `bounded-context-semantic-resolution`, are neither excerpted nor linked by any frame (checked against `FRAME_INPUTS.json` routes and the frame text). Arm C reached them with the permitted search tool.

This is lawful tool use. It shows that the frames alone were not the material the actor used. The partial reads do not show sufficiency, and they may indicate excess.

Per-task citations (`source-citations.json` resolved through `answers.json`):
- T1 cites EVALUATION_CONJUNCTION, T2 CONSTITUTIONAL_DERIVATION, T4 RELEASE_ADOPTION, T5 WORK_RECOVERY and T6 TRIAGE_CARRIER, each with other frames or owners besides.
- T3, domain binding, cites no DOMAIN_BINDING material. Its sources are EVALUATION_CONJUNCTION, WORK_RECOVERY, and the three owner sections no frame carries (SPEC_METHOD `bounded-context-semantic-resolution`, FOUNDATIONS `typed-composition-and-conservation` and `judgment-and-authority`).
- DOMAIN_BINDING's declared scope is "the selected continuation, projection and Markov-overlay claims only" (`FRAME_INPUTS.json`). It does not cover domain-result binding.

So DOMAIN_BINDING had no in-scope task in this trial, and the domain-binding task had no frame whose scope covers it (part B I5).

Arm C's citations name only successor sources, and no predecessor identifier appears in its answers. The frames state "This selection makes no material-sufficiency claim" (`WORK_RECOVERY.md` preface). `FRAME_INPUTS.json` says "task sufficiency require[s] separate proof" and declares no byte limit. The a_c index surface `interpretation/FRAMES.md` was exercised by no actor.

Reading of "frame or acquisition view" in H4: the six `standards/frames/` views are the activation units, because DESIGN.md says "Frames are named projections of owning clauses" and they are what the ordinary entry routes to. Under that reading, each of the six views was reached through ordinary entry by one actor. None was the unit an actor started on.

### 1.4 Oracle authorship and isolation

- **Author.** A fresh native Codex context wrote the oracle. It is a nonauthor of every arm and the same family as the candidate's author.
  - Its permitted reads were common B, the three AGENTS.md files and rc.2 author/qualification routing (`attempt-02/ACTIVATION.json`, `ACQUISITION.json`).
  - Its recorded exclusions: no ticket, no candidate, no prior attempt, no review post.
- **Attempt 1.** It stopped and was discarded after it saw neighbouring ticket history (`attempt-01/RETURN.md`). This is correct handling.
- **Pre-delivery revision.** One revision (r1 to r2) was made before any actor saw the packet, and the superseded files are retained.
- **Standard.** PRODUCT says "Independently specified expectations do not come from the author of the behavior being assessed." A nonauthor oracle meets this. The different-family default applies to the Reviewer.
- **Case selection.** The Executive fixed the six task families. They mirror the candidate's six frame names. The oracle author chose every case and expectation.
- **Disclosed limits:**
  - "Host system/developer instructions and an automatically supplied general workspace memory summary were already present."
  - "REQ was partially omitted" by truncation.

### 1.5 Actor instructions and fixture decidability

The author's prompt carries no outcome guidance ("Follow it without additional outcome guidance").
- Its effect boundary ("do not perform actual publication…") overlaps T4.5's witness. It only repeats the fixture's `release_actor_grant`.
- A scan of every arm result for oracle-only tokens (`expected_semantics`, `required_witness`, assertion IDs, `ORACLE.json`) found only the packet's `suite_id`.

The oracle author's fixtures state the deciding rule for each graded assertion. Several task requests also name the graded distinction:

| Task | Assertions | Deciding fixture text in the actor packet | Request text naming the distinction |
|---|---|---|---|
| T1 | 1–5 | `E.contract`: "All three checks have applicable, authenticated successful assessments of this subject on this basis. Recommendation is separate from owner approval"; required_checks includes retention. `E.evidence`: "Subject and basis must still be matched to the contract." | "identify the standing of every check" |
| T2 | 1–5 | `K.intent`: "Repeated equal amounts are separate records"; `K.spec`: "Every input occurrence contributes exactly once", "Any partition preserves all record IDs exactly once", and admitted_laws kept apart from requirements; `K.product`: "Algorithms… are choices" | "Make any partition precondition explicit"; "supply a concrete counterexample wherever a plan violates the contract" |
| T3 | 1–5 | `D.archive`: "No semantic conformance assessment or acceptance decision is performed"; `D.admission`: "A label without the required conditions does not supply them"; `D.dispatch`: "a timeout supplies no completion observation… Only an authoritative no-effect observation establishes absence of effect"; `D.consumer`: digest equality and dana's accept | "Assess the proposed adapter that changes only… type name"; "what additional owner evidence a completion claim needs" |
| T4 | 1–5 | `L.product` release rule (remy, exact candidate and manifest); `L.consumer`: "Only… arden… naming the release and manifest digest. Publication or installation alone does not change the selected basis"; `L.evidence`: "These observations are not release or adoption decisions"; "no actual publication" | "distinguish the staging install from those decisions"; "Identify any exact missing or mismatched decision" |
| T5 | 1–5 | `W.outcome` dependencies; `partial_index.complete: false`; `W.recovery`: "complete current owner answer", "Unknown completion/attempt state does not authorize another submission", "A permitted submission is not a delivery receipt", and a grant to propose only on never_submitted | "reconcile the cached account with current owner observations"; "Record performed local construction separately from proposed external effects" |
| T6 | 1–5 | `I.design`: "owns no separate maximum" and "selecting a value inside that range changes no Product or accepted design obligation"; `I.product` reserved decision (priya); work-17 and work-18 grants; carrier_policy "headings… supply no extra authority"; "No optional coordination profile is selected"; "No latency target… was supplied"; owner_routes | "Distinguish a required process step from an optional organizational choice and state why any additional carrier is necessary" |

By my reading, the fixture text decides all 30 assertions. T2.5 and T6.5 are the weakest cases, because the actor must also state the distinction in its own terms.

The defect is not that domain facts sit in the fixture. Issuers, digests, ranges and grants belong there. The defect is that generic method rules are restated as fixture text:
- a timeout is no no-effect observation;
- an unknown attempt does not license resubmission;
- a label does not supply its conditions;
- publication or installation does not adopt;
- headings supply no authority;
- subject and basis must match;
- a permitted submission is not a delivery receipt. The admission asked for tasks "decidable from a supported entry path and declared source", so this is by design rather than leakage. Its consequence is that, with all three arms at 30/30, no no-method arm and one model family, the trial supports these conclusions:
- each method's ordinary entry did not mislead a capable actor on these cases;
- C showed no regression against A or B on these cases.

It does not support frame sufficiency, attention adequacy or attribution of the answers to frame content.

### 1.6 Freshness and the predecessor

PRODUCT Audiences says:
- "predecessor rules cannot supply missing successor content during the trial";
- "The installed builder governs preparation and assessment outside that actor's task context";
- "Freshness excludes… automatically loaded repository instructions regardless of working directory."

Against that:
- The actor prompt says "The installed STDO v2.5.1-rc.2 process governs this activation", which places the predecessor inside the task context.
- The actors were native sub-agents of a parent working in `/Users/jim/src/apps/specification_methodology-codex`. AGENTS.md files exist at `/Users/jim/src/apps/`, at the worktree root and in `v3/`. The workspace file embeds a method compression, and the `v3/` file holds an STDO bootstrap that routes to the installed basis.
- `ACTIVATION.json` says "inherited platform instructions and host context are not measured". The assessment says "persisted records cannot prove complete host-context isolation."

Freshness is therefore not established, and it is also not shown to be violated. Arm C's citations are successor-only (§1.3). Part B I4 says a trial in which predecessor rules supply content is not standalone criterion-4 evidence. Here that cannot be excluded.

### 1.7 Context measurement, limits and spend

What was measured:
- prompt bytes (3,235 per arm) and the packet (35,410), from `MEASUREMENTS.json`;
- logger emissions, repeated reads and source I/O, kept separately;
- actor wall times.

What was not:
- Inherited host context is unmeasured.
- No actor, oracle or grading activation declared a context, wall-time or spend limit:
  - oracle: "No numeric limits were supplied in this activation";
  - arms: "retained_context_or_platform_budget": "uninstrumented; do not infer fit";
  - MATCHED-USE-01: "Context is bounded by material task acquisition."
- Spend is reported for no I3 activation. Native inference is "uninstrumented". There were no external paid calls.

Criterion 4's "fits the declared limits" therefore has nothing to evaluate against. Arm C's cumulative emission of 284,930 bytes says nothing about active-context fit, and the return correctly makes no fit claim.

### 1.8 Grading coverage and independence

Coverage is complete:
- `GRADES.json` holds 90 judgments, 30 "met" per arm, recounted.
- Each judgment carries the actor evidence pointer, fixture sources and the cited package clause, with hash and range checked.
- The copied-code probes reproduce K1–K3 (5/1/5, 0/0/0, 5/5/5).
- Digests recompute: `ASSESSMENT.md` `d5ec5a7…` and `FREEZE.json` `278fb38f…`. All 24 frozen files match.

Independence is limited:
- The grader is the oracle author, in the same retained context: "Existing oracle-author context retained", with context compaction during grading.
- It can see arm identities and is the author's family.
- It is the only grader.
- The grader checks that cited clauses exist. It does not judge whether the cited clause, rather than the fixture, decided the case.

### 1.9 What the trial supports

Supported:
- The frozen `3aaa2f2` ordinary entry routes a fresh native actor to all six task views.
- That actor answered 21 fixture-decidable cases with no forbidden outcome, citing only successor sources.
- The predecessor and the preceding candidate did the same.
- One-run emission and wall-time observations.

Not supported:
- per-frame criterion 4;
- frame sufficiency;
- standalone use;
- reduction;
- any ranking.

The return and MATCHED_RETURN disclaim each of these, except that I3-10 is headed "Actual use of final frames" (CB5-09).

## 2. Evidence process (M4)

| Question | Result | Evidence |
|---|---|---|
| Review packets assembled by the author with stated expectations? | No, for all I3 working reviews. | VIEW, SEMANTIC and COMPILED reviews acquired frozen objects with `git show` themselves. SEMANTIC preserves a 19,412-byte source-first expectation prefix (`971a497e…`) recorded before account acquisition. COMPILED fixed expectations at 12:21:19Z, before artifact acquisition. The activation texts in T-002-CODEX state scope, not conclusions. |
| Verdicts changed without new evidence? | None found. | Each original `falsified` result is preserved: VIEW on `f2cb3e5`, SEMANTIC on `a6d5f00`, COMPILED on `b6ae345`. Each `satisfied` readback is on a new frozen subject (`6bcc412`, `3a98206`, `3aaa2f2`) and is scoped to the original findings. |
| Grading covers every claimed run? | Yes, 3 of 3. | §1.8. In iteration 2 it was 15 of 31. |
| Same-family reviews counted as independent? | Not as acceptance. Grading and one review are labelled "independent" without a declared exception and reason. | A nonauthor oracle meets PRODUCT's test for expectations, so "independent expectations" is conformant. SEMANTIC, COMPILED and their readbacks declare "same-family defect review". EC-CODEX-I3-02's Actors line says "Same-family defect reviews disclose their limits". That provision is contract-level and gives no reason. The VIEW-REVIEW-01 activation does not mention family; its report discloses it. The grading activation, which judges the work, declares no same-family exception or reason. Grading labels: MATCHED_RETURN "Independent grading is closed"; RETURN.md I3-10 "under independent grading"; return post "The independent oracle author graded". Review labels: ticket "the independent documentary review"; work list I3-08 "independently read back". Each is qualified elsewhere, for example "not… a cross-family assessment". |
| Exposure handling | Inconsistent. | Oracle attempt 1 was restarted after over-broad ticket exposure. The COMPILED reviewer saw ticket lines 189–199 (prior semantic findings), and the Executive "explicitly directed this bounded conversion review to continue" (`I3_R2_COMPILED_RELATION_REVIEW.md:28`). |
| Withholding of the oracle | By instruction only. | `ORACLE.json` was in the actors' worktree at `cb14a63`, a sibling of the reader path given in the prompt. The actors had a shell. The logger records only reader calls. No oracle-only token appears in any answer. |

Breadth: the semantic review covered 71 of 697 IDs, and no broad source-first review ran on the complete package `3aaa2f2`. The documentary bytes at `3aaa2f2` equal D2 `6bcc412`, so the view review and readback apply to them. The interpretation has only the conversion review and readback.

## 3. Acceptance status (criteria 1–6 and the whole-candidate check)

| Item | Assessed by | Status at `3aaa2f2` |
|---|---|---|
| Crit 1, one disposition and resolving loci | Author: `CONSERVATION.json`, mechanical checks | 691 rows, recounted 639/51/1. All 691 rows read `disposition_standing: author_proposal` and `acceptance: current_independent_review_pending`. 631 rows carry a `semantic_review` scope beginning "Inherited author disposition" (my count). The map's limits say "Other row dispositions are inherited proposals… not a new 691-row semantic audit". No nonauthor assessment. |
| Crit 2, nonauthor semantic conservation | None | Not assessed. The view and semantic reviews compare successor views and account to successor source, not predecessor to successor. The per-row field `semantic_review` (all "indeterminate") is author-written, despite the name. |
| Crit 3, supersessions accepted by the owner | None | 51 proposals pending, with no owner decision. The return says so. |
| Crit 4, frame use | §1 | Not evidenced per frame (CB5-01). |
| Crit 5, conformance discriminators | None | "full common conformance remains open" (`RETURN.md`, I3-12). |
| Crit 6, reduction | Author measurements | Open. Adverse evidence is disclosed: a 23,865,207-byte package (recomputed), with the interpretation 22,062,742; selected closures of 1.2–2.6 MB; C emits more than rc.2. |
| Interpretation fidelity (Outcome bullet 3) | Same-family nonauthor: 71 IDs semantic; conversion mechanical | Partial. |
| Whole-candidate check, integrated reduction and coverage | None | Not started. |

Nothing is presented as accepted. "Closed" is used for grading completion and for the common round-2 repair. "satisfied" is the returning Writer's own evaluation of a bounded construction predicate and is labelled "not an independent member-acceptance verdict" (`RETURN.md`). Part B N2 and N10 hold: no acceptance is drawn from a frontier, return or review, and no iteration-2 trial is reused. All six frames changed since `3ad1fca`.

Part B group (i):
- I12 holds. `qualification/C3/iteration-3/RETURN.md` covers all four Outcome bullets, with variant `candidate_ready` and exact coordinates.
- I11 is falsified: limits were not declared and spend was not reported.
- I4 and I5 are not met: no frame starts, freshness unestablished, no declared limits.
- I9 is partly met: every reviewer and the grader are nonauthors, but the same-family exception, with its reason, is undeclared in the grading activation and in VIEW-REVIEW-01's.
- I1–I3, I6, I7, I8 and I10 are open, as the return states.

## 4. Process

- **Territory.** All 23 non-merge tenant-only commits of iteration 3 (`21c5191` through `939ce0c`), including `cb14a63`, `6627800` and `939ce0c`, change only `build_tenants/codex/`. The tenant tree is unchanged across both inward merges: `d832a51` and `1ea382a` are both `dd222838…`, and `939ce0c` and `0517eb2` are both `a877e261…`.
- **No merge, push or tag.** `3aaa2f2` and `939ce0c` are not ancestors of `main`. No remote branch or tag contains `3aaa2f2`. Main's tenant tree equals `3ad1fca`'s (`b9520a01…`).
- **Contract.** EC-CODEX-I3-02 recomputes to 5,089 bytes, `b1a8ab97…`, at `651581c` (the admission, 07:38:23Z), `3aaa2f2`, `939ce0c` and `main`. Admission precedes the inward merge (10:06:03Z) and all construction. EC-CODEX-I3-01 recomputes to `fc6ed417…`. "Both admitted contract digests remain unchanged" is supported.
- **Input binding.**
  - R `651581c` descends from B `355aa86`.
  - All 24 snapshot members recompute at B by bytes and SHA-256.
  - The specification tree at `3aaa2f2` equals R's (`70862464…`). R differs from B only in GOALS.md work standing (3 lines).
  - The comparison subjects match the contract.
- **Activations.** Six activations were recorded on main before their first effect, with scope and exclusions:
  - ORACLE-01: `f0783a9` 10:35:28, before 10:38:43;
  - VIEW-REVIEW-01: `ab11cbc` 10:47:49, before 10:48:17;
  - MATCHED-USE-01: `f0676fa` 11:11:11, before 12:54;
  - SEMANTIC-REVIEW-01: `b6c04ab` 11:43:46, before 11:45:37;
  - COMPILED-RELATION-01: `1aaad75` 12:15:39, before 12:21:19;
  - grading: `5bcb110` 13:19:26, before 13:20:19.

## 5. Claims in the return post (`20261014T134223Z_RETURN_CODEX_V3_I3_R2.md`)

| # | Claim | Assessment | Evidence |
|---|---|---|---|
| 1 | Checkpoint `939ce0c`, `candidate_ready` under EC-CODEX-I3-02, package frozen at `3aaa2f2`, not merged | Supported | §4 ancestry; diff `3aaa2f2..939ce0c` is qualification only |
| 2 | Builder rc.2 `3d860ff…`; input B recorded by R; common source unchanged since R | Supported | §4 |
| 3 | 697 source units, 37 contracts, no declared unfinished omission | Not tested | Authored; outside this review's scope; labelled authored |
| 4 | 691 rows: 639/51/1; authored proposals; acceptance open | Supported | Recounted; all `author_proposal` and pending |
| 5 | Six views, 98 exact excerpts | Supported | 23+18+11+12+19+15 = 98; view review 98/98 on bytes equal to `3aaa2f2` documentary |
| 6 | 89 members; 1,590 links, 32 pins, two schemas | Partly | 89 members and byte totals recomputed; links, pins and schemas not rerun |
| 7 | Ten conservation controls; 19 identity controls in a fixture | Not tested | As recorded |
| 8 | Working reviews caused bounded corrections and retained failed subjects | Supported | §2 |
| 9 | 734 clauses and 720 indexes; conversion checks all records; source review bounded | Supported as recorded | COMPILED review and readback; 71 IDs |
| 10 | Arms share "precommitted tasks and independent expectations, ordinary entry, acquisition logger and inherited model family" | Supported | Same packet, entry and logger verified; the expectations were frozen before the actors by a nonauthor, which meets PRODUCT's expectation rule |
| 11 | One fresh context per arm completed six tasks and 21 cases | Partly | New agent per arm, verified. PRODUCT freshness not established (§1.6). |
| 12 | Actor outputs frozen at `6627800` | Supported | Arms unchanged to `939ce0c`; dispatch hashes |
| 13 | 30/30 per arm; times; emissions | Supported | 90 "met" recounted; emission sums and percentages recompute |
| 14 | "independent oracle author graded… exercised copied code" | Partly | Graded 90/90 with probes. Same context as the oracle author, same family, unblinded, single grader. The return discloses this. |
| 15 | Assessment `d5ec5a7…`; 90 judgments; 1,101.4 s | Supported | Digests and freeze recomputed; `CLOSURE.json` |
| 16 | "no correctness advantage or efficiency gain over rc.2"; listed limits | Supported | §1.9 |
| 17 | No semantic repair or actor retry selected | Supported | Arms and oracle unchanged after freeze |
| 18 | Nine interpretation members take 22,062,742 of 23,865,207 bytes; practical compression a material weakness | Supported | Recomputed from `arms/C/ACTIVATION.json` |
| 19 | Fidelity, reduction, conjunction, policy proposals, ports, identity and release remain open | Supported | §3 |
| 20 | Both contract digests unchanged | Supported | §4 |
| 21 | Final recording verified 89 members, 24 assessor files, 41 return links and unchanged inputs | Partly | 89, 24 and unchanged inputs verified; 41 links not tested |
| 22 | No external paid call, merge, push, tag or publication | Supported, with one limit | No merge, push or tag found. Native inference spend is unreported, so the absence of cost is not shown (the return says so). |

Tally: 16 supported or supported as recorded, 4 partly supported, 0 unsupported, 2 not tested. The weaker statements sit in labels: "independent" grading (CB5-04) and the I3-10 heading (CB5-09).

## 6. Findings

Each finding is rated by its effect on C3 acceptance. None falsifies the `candidate_ready` return, which claims no acceptance.

| ID | Severity | Claim | Evidence | Smallest repair |
|---|---|---|---|---|
| CB5-01 | High (blocks crit 4) | Criterion 4 is not evidenced for any frame at `3aaa2f2`. | No actor started on a frame: all entered at `SKILL.md` (§1.2). One context ran six tasks, so per-frame attribution is impossible. Arm C read 6–74% of each frame and also used four owner sections that no frame carries (§1.3). The domain-binding task cites no DOMAIN_BINDING material, and that frame's declared scope does not cover it (§1.3). The frames disclaim sufficiency. No activation declared a context limit (§1.7). The task design does not discriminate (CB5-02). | For each selected task, start a fresh actor on the frame whose declared scope covers that task, with its subject alone, under declared byte, wall-time and spend limits and a new nonauthor oracle. Otherwise keep criterion 4 open and stop heading the trial as frame use. |
| CB5-02 | Medium | The matched-use oracle cannot attribute success to method or frame content. | By my reading, the fixture text decides all 30 assertions, and several requests name the graded distinction (§1.5 table). The generic method rules being tested are restated in the fixture (§1.5 list). All arms score 30/30, rc.2 included, with no no-method arm, one model family and one pass each. The admission required fixture decidability ("decidable from a supported entry path and declared source"). | Amend the oracle admission so that the fixtures carry only domain facts, and generic method rules come from the selected method. Add a fixture-only arm as a control. Grade only against the common requirements; do not grade against pending supersessions as if accepted. |
| CB5-03 | Medium | Standalone freshness is not established for the actors. | The prompt says rc.2 "governs this activation" inside the task context. AGENTS.md files with a method compression and the rc.2 bootstrap sit on the parent's path. Inherited host context is unmeasured; the records "cannot prove complete host-context isolation" (§1.6). Part B I4. | Run actors in a directory with no auto-loaded instruction files. Remove builder-governance text from the actor prompt. Record the actor's full supplied instructions. |
| CB5-04 | Low | Grading and one working review are labelled "independent" without the same-family exception and reason that PRODUCT Independence requires of a Reviewer. | The grading activation (the oracle author judging the work) declares no exception or reason. VIEW-REVIEW-01's activation does not mention family, although its report discloses it. EC-CODEX-I3-02's "Same-family defect reviews disclose their limits" covers defect reviews at contract level, with no reason, and does not cover grading. The labels are listed in §2. This is a narrower recurrence of the CR5-06 pattern. Nothing is counted as acceptance, and the nonauthor oracle is conformant. | Record the same-family exception, its reason (no cross-family allowance) and its limits in the grading and review activations. Call such grading "nonauthor" rather than "independent". |
| CB5-05 | Medium | The Limits rule is not met: no limits declared, spend unreported. | Oracle: "No numeric limits were supplied". Arms: "uninstrumented; do not infer fit". Grader: spend unknown. No I3 activation reports spend (§1.7). Part B I11 falsifier. This widens CR5-11: iteration 2 at least reported USD for its CLI calls. | The Executive declares byte, wall-time and spend limits at each activation and reports them after, naming the uninstrumented parts. |
| CB5-06 | Low | Task coverage is author-scoped, toy-sized and misaligned with one frame. | The Executive fixed the six families to the candidate's frame names. The domain-binding family falls outside DOMAIN_BINDING's declared scope (§1.3). The PRODUCT tasks "review work" and "build or assess a member" are exercised only through synthetic fixtures; T2 is a total-of-integers. Under reading Q4, coverage of the selected tasks stays open. | Have the oracle author select the cases against the PRODUCT task list and each frame's declared scope, including a member-scale build or review task. |
| CB5-07 | Low | Oracle withholding relied on instruction. | `ORACLE.json` sat in the actors' worktree beside the reader path. The actors had a shell, and the logger sees only reader calls. Zero oracle-only tokens appear in any answer. | Keep the oracle outside the actors' filesystem until the returns freeze. |
| CB5-08 | Low | Acquisition over-exposure was handled inconsistently. | The oracle author was restarted. The COMPILED reviewer continued after seeing prior semantic findings, by Executive direction (§2). | Apply one rule: restart, or record a declared exception with its limits. |
| CB5-09 | Low | The I3-10 heading overstates. | "Actual use of final frames — three selected-task returns graded 30/30": two of the three returns are non-candidate arms, and none started on a frame. The following sentence about fresh actors covering "each selected task on the exact final frame" is the work assignment carried from B, not a status claim. | Retitle the row as a matched ordinary-entry comparison. Keep criterion-4 frame use OPEN. |

## 7. Closure of H4 and M4

**H4: partly closed.**
- Holds:
  - actor runs on frozen `3aaa2f2` bytes (89/89);
  - a nonauthor oracle, frozen about two hours before the actors, with isolated acquisition;
  - no author paraphrase in the prompt;
  - all runs graded;
  - claims bounded to the cases and arms tried.
- Does not hold:
  - each frame "tried by fresh actors starting from the frozen bytes": entry was at `SKILL.md`, in one context, with partial reads, and the domain-binding task had no in-scope frame (CB5-01);
  - freshness (CB5-03);
  - grading with a declared same-family exception and reason (CB5-04);
  - attribution of the results to the frames (CB5-02).

**M4: largely closed.**
- Holds:
  - oracle authorship by a nonauthor;
  - grading of 3 of 3 runs;
  - no author-assembled review packets;
  - reviewer expectations recorded before the subject was read;
  - no verdict changed without new evidence.
- Residual: the "independent" label on grading and one review without a declared same-family exception and reason (CB5-04), and the inconsistent exposure handling (CB5-08).

## 8. What holds

- **Territory and integrity.** Every I3 tenant commit stays in `build_tenants/codex/`, and the tree is unchanged across both inward merges. There was no merge, push or tag.
- **Contract and input.** EC-CODEX-I3-02 was admitted with a recomputable digest before construction. All 24 shared-input members verify. The specification at `3aaa2f2` equals R.
- **Ordering.** The frames and entry were frozen before the oracle, the oracle before the actors, and the actors' returns before grading. No arm, oracle or task changed after use.
- **Oracle conduct.** The contaminated oracle attempt was discarded rather than repaired. The pre-delivery revision is retained.
- **Prompt and grading.** The actor prompt is neutral and identical across arms. All 90 assertions are graded with evidence pointers, and copied-code probes reproduce the arithmetic.
- **Measurements.** Emission, read and source-I/O measurements are kept separately and recompute.
- **Reviews.** All three working reviews acquired their own frozen sources. Two recorded expectations before reading the subject. Every failed result is preserved, and readbacks bind new subjects.
- **Honest reporting.** The return reports adverse evidence plainly: C emits more than rc.2, a 22 MB interpretation, 1.2–2.6 MB closures. It makes no superiority, reduction, fit or acceptance claim.
- **Improvements over CR5.**
  - No outcome guidance in the prompt (CR5-02).
  - Grading of 3 of 3 runs, against 15 of 31 (CR5-03).
  - Reviewers acquired sources themselves (CR5-04).
  - No verdict rewritten (CR5-06).
  - Trials run on the frozen frames, against 1 of 31 runs (CR5-01).

## 9. Limits of this review

- **Conflicts.** Claude builds the competing candidate. Claude wrote CR5 and the part B oracle that this review applies. Unlike CR5, this review is cross-family to the actors, oracle author and grader as well as to the author.
- **Not done.** I re-ran no actor, harness, probe, artifact check, conservation check, identity check or native validation. I recomputed selected digests, counts and coverage.
- **Fixture-decidability (§1.5)** is my reading of the packet. I ran no fixture-only control.
- **Freshness (§1.6)** rests on the files present and the records' own disclosures. I cannot observe the Codex host's actual injected context.
- **Section coverage (§1.3)** uses my slug rule for section anchors. All anchors resolved.
- **Out of scope.** I did not assess per-row conservation, conformance discriminators, reduction, interpretation fidelity, or the five ported parts. Port authorship would make any finding on ported text non-independent.
- **Timestamps** come from the records and Git, not from host logs.
