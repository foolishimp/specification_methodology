## EXPECTATIONS (written before opening any candidate, account, conservation, evidence or prior-review material)

**Basis read so far:** INTENT.md, PRODUCT.md, requirements/README.md, conformance/README.md and requirements/ASSURANCE.md in full. PREDECESSOR_CLAIMS.md lines 1–40 (header and member table). In the predecessor, I read REFERENCE_FRAME_METHOD RF-012 and lines 589–693 (Applicability, Select, Evaluate, Closed Result, Reconfigure, Co-evaluation, Result Conjunction), AXIOMATIC_CALCULUS AC-007 to AC-011, SPEC_METHOD lines 1095–1119 (ambiguity governance and human adjudication), and TICKET_METHOD lines 637–676 (Work-Carrier-To-Execution).

**Not read:** PRINCIPLES, CAPABILITIES, A_C_DEPENDENCY, GOALS, REFERENCE_FRAME_BASIS, and most predecessor section text, which is about 600 KB across the nine members.

What I expect the candidate to show:

- **E1 Generic assessment.**
  - A foundations-owned assessment law applies to any assessed predicate and any executor: human, software or mixed.
  - Every result maps to exactly one core value from the RF-012 family (satisfied, falsified, indeterminate, out_of_frame, invalid_basis).
  - It keeps "not performed" distinct from "indeterminate", and "unknown effect" distinct from "no effect" or "completed".
  - Applicability has three values: true, false and unknown. A false premise excludes only that obligation, citing its authority. Unknown stays unresolved.
  - Conjunction is defined once. Missing, stale, wrong-subject or conflicted mandatory results withhold the conjunction. A minority counterexample survives.
  - Admitted outcomes are a relation, not a function. A human or probabilistic checker may admit both satisfied and indeterminate, and soundness is claimed over all admitted outcomes.
  - Observation sufficiency holds. Assertion provenance (necessary versus sufficient) is kept distinct from execution provenance.
  - Generic assessment must not require code, event streams or full-history replay (binding requirement item 2; conformance row 56). It must not let an automated result stand in for a required human decision (row 57). A person performing an operation does not by that fact make it human adjudication.
  - A generic assessment rule must be reachable without adopting an optional profile (ODD, Traversal Occurrence, UX, World Model).
- **E2 Carrier dependencies.** The successor of Work-Carrier-To-Execution keeps:
  - no execution without upstream authority, and a ticket is never created as substitute authority;
  - the five-row selection by surviving-state lifetime;
  - drafting kept distinct from admission;
  - an admission record giving the mechanism, authority, digest and decision.

  Consumers that depend on carriers (triage, recovery, release, assurance evidence, design) must bind to one carrier owner, without rival selection rules and without new carriers (README ASSURANCE: "no parallel ledger").
- **E3 Inverse consumer metadata.** Where an owner lists its consumers, each listed consumer must actually apply the owner at its entry point, and each consumer's own citation must match the inverse entry. A blank consumer field alone is not a defect. A positive relation asserted on only one side is a coverage gap to report, not to treat as resolved.
- **E4 Conservation.** RF-012, the conjunction rule, applicability, and the AC-007 rule against coercing results to success must keep their modal force and exceptions. Any changed meaning needs a superseded row citing an accepted owner decision. A proposed replacement must remain pending.
- **E5 Reduction.** One shared assessment and conjunction owner, with consumers (Spec testing and triage, Release acceptance, Ticket admission, Design module checks, Identity) using it instead of keeping rival result vocabularies. Every domain refinement must map back to the core.

Now the predecessor's corresponding UP-020 text, so I can compare the changed owner.

The five carrier dependencies turn out to be the plugin skills. I'm reading them now.

Assessing whether the plugin entry skills apply the changed owners consistently. I found a possible conflict over the "cheapest falsifier" proof-selection rule, which I'm checking against UP-014.

Now spot-checking the inverse consumer metadata in the interpretation account against what the source actually says. About $3.2 of the $6 budget remains.

# FINAL REVIEW: Codex STDO v3 candidate `ea27616b93c80b13ee15a9931cd9114275e5de13`

**Reviewer:** a fresh, cross-family reviewer (Claude, Opus 5.5) who is not an author of this candidate. I contributed no wording, policy or repair. Access was Read, Glob and Grep inside the scratch directory only. There were no changes, no shell, no Git and no subagents.

**Ordering:** the EXPECTATIONS message above was written before any candidate, account, conservation, evidence or prior-review file was opened. Before writing it I only listed file paths.

## 1. Scoped judgment

**Overall: `indeterminate` for candidate readiness within the reviewed scope.** Within the changed scope I confirmed four source/account defects: two Medium and two Low. None of them makes the shared result and conjunction law or the carrier-selection law invalid. Separately, large parts of the nine primary members were not read (section 6), so I make no whole-member or whole-candidate claim.

Nothing here supports acceptance, a winner, a release, or a claim that the whole candidate is correct. The shared actual-use trial has still not been performed.

## 2. Confirmed defects

### D1 — Medium. Conservation: a changed determination is still labelled `conserved`
- **Where:** `conservation-by-source/standards__SPEC_METHOD.md.json:2165-2201` for the row `SPEC_METHOD.md#construction-assessment-and-delegation`. Source: `candidate/standards/SPEC_METHOD.md:1888-1894` against `predecessor/standards/SPEC_METHOD.md:1557-1563`.
- **What changed:** the predecessor said the assessor "evaluates the exact live **code**". The candidate says "the exact live **realisation** under the selected computational binding".
- **Trigger:** a promotion that requires independent assessment, where the realisation is a human procedure or a mixed procedure that is not only code.
  - Under the predecessor's text, the required subject (live code) does not exist, so the assessment cannot be satisfied.
  - Under the candidate, it can be satisfied. The author's own discriminator says so: `evidence/rc1/integration/CHANGED_SCOPE.json:76-81`, "subject condition can be satisfied without software code".
  - For software bindings the two texts decide the same way.
- **Consequence:**
  - The required and permitted decision changes on a material case. Under `basis/requirements/README.md:32` that change needs a replacement relation; at minimum, conservation stays unresolved.
  - The frozen row still says `conserved`, with the pre-repair digest `a58a251b…`, `changed_carrying_loci: []`, and no same-case argument.
  - `CONSERVATION_APPLICABILITY.json:14691-14709` marks the row as needing reassessment but keeps the `conserved` disposition.
  - Under `PRODUCT.md:224`, the common binding requirement, as accepted general direction, "does not by itself accept particular changed meanings".
- **Smallest owner repair:** in the Codex conservation account, change this row to `superseded`. Add a proposed relation, "exact live code → exact live realisation under the selected binding (software case unchanged)", with standing pending the owner's decision. Alternatively, record a same-case argument that the predecessor's "code" was scoped to code realisations only.
- **Disputed part:** whether the predecessor's "code" was merely scope-limited to agentic software construction. I could not settle that from the predecessor text. Either way, the current `conserved` label is not supported.

### D2 — Medium. Single ownership: the ordinary work entry restates a rule the owner proposes to replace, and cites the wrong owner
- **Where:** `candidate/plugins/spec/skills/stdo-work/SKILL.md:120`. It says "Use the cheapest adequate falsifier under `SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014`."
- **Problem with the cited owner:** UP-014 (`SPEC_METHOD.md:1735-1813`, read in full) contains no proof-selection rule.
- **Where the rule actually lives:** at UP-020 Transition Evidence (`SPEC_METHOD.md:1981-1992`), which delegates to Foundations change-impact and risk selection. That owner is the subject of the proposed replacement `I5-ACCOUNT-R004`, which specifically removes "cheapest focused falsification" as the selection rule (`conservation-by-source/…SPEC_METHOD.md.json:2353-2366`).
- **Same old rule elsewhere:** `plugins/spec/references/GETTING_STARTED.md:516` also restates it.
- **Trigger:** a worker enters through `stdo-work` after a change whose impact is unknown, for example a changed fixture dependency. The skill tells them to pick the cheapest adequate falsifier. The cited owner gives them nothing to apply. The real owner requires unknown impact to widen reassessment, and requires covering new obligations and mandatory gates.
- **Consequence:**
  - The deciding entry carries a rival determination: the predecessor rule, attributed to a section that does not hold it. This violates `requirements/README.md:146` (packaging derives from the method-law owners) and the reduction requirement in README §2.
  - It also matches assurance discriminator `conformance/README.md:101` ("selection is cheap but omits a material obligation").
  - The prior core review (`prior-closed-reviews/20261016T154154Z_I5_CORE_REVIEW.md:50`) covered only the Spec paragraph, not the plugin entries.
- **Smallest repair:**
  - In stdo-work line 120, route to `SPEC_METHOD.md#transition-evidence-and-proof-cadence` and do not restate the selection rule.
  - Align GETTING_STARTED line 516 the same way.
  - Update the `CARRIER.plugins.spec.skills.stdo-work.SKILL.md` account obligation, which currently says "Use adequate focused proof".

### D3 — Low. The replacement record does not disclose all of the changed meaning
- **Where:** `candidate/standards/TICKET_METHOD.md:819-824` against `predecessor/standards/TICKET_METHOD.md:710-714`.
- **What changed:** "logged in runtime/event truth" became "recorded in the selected work carrier, including an event log when that is its declared realisation". "Prompt assembly" also became "frame or prompt assembly".
- **The record:** the superseding relation `I3-R2-R025` (`conservation-by-source/…TICKET_METHOD.md.json:1298-1310`) describes only the result-algebra binding. It does not mention that the event-log requirement was relaxed.
- **Consequence:** the change itself is consistent with the common binding requirement (`README.md:125`) and Foundations `:903-905`. But an owner accepting R025 as written would accept a change that was not described. That conflicts with "each supersession names … the replacement determination" (`README.md:36`).
- **Repair:** add the event-log-to-selected-carrier change to the `changed_meaning` of R025.

### D4 — Low. The refresh registry leaves out two declared frames
- **Where:** `candidate/plugins/spec/references/REFRESH.md:40-46`. It lists "the five views". The package has seven frames: `MEMBER_CONSTRUCTION_ASSESSMENT` and `TRIAGE_CARRIER` are missing. Both are named entry routes in `standards/README.md:36-43`, and both carry the changed UP-020 paragraph.
- **Trigger:** `/spec:refresh --doc` for triage or member assessment.
- **Consequence:** the procedure refuses it as an unknown name (`REFRESH.md:61`). The manual route cannot load the current changed frames. The direct-owner fallback still exists, so there is no loss of meaning, but the entry route is inconsistent.
- **Repair:** add both frames to the registry and fix the count.

## 3. Disputed claims (not counted as defects)

- **stdo-review entry and mixed bindings.** `stdo-review/SKILL.md:26-28,41-42` lists "implementation, tests, fixtures, installed or runtime evidence". It does not mention the selected computational binding or performed human operations. In the mixed-binding case where only code was reviewed, a reviewer following only the skill might return a result the generic owner would not allow. The skill's wording is generic enough ("implementation"), and it says to "determine required evaluations from the owning applicability conditions". I record this as a fidelity risk, not a confirmed defect. Suggested fix: add "under the selected computational binding, including material performed operations".
- **Sufficient Execution Intake.** The predecessor (`SPEC_METHOD.md:1526-1528`) explicitly excluded conversation history, commentary, prior-worker memory and folklore. The candidate (`:1856-1869`) replaces this with Contract application plus the constraint surface. The meaning is recoverable through Foundations `:859-866`, RF-013, Spec `:959` (commentary is non-authoritative) and the falsifier at `:2029`. I judge this conserved, but the named exclusions are now spread across several places. Leaning toward conserved.
- **Proportional Disposition `re_enter`.** The predecessor listed the layers that may change (Product, requirement, identity, lifecycle, authority, public contract, design). The candidate says "owning-layer change". The relation `I3-R2-R021` is already proposed as superseded and pending. I found no lost layer.

## 4. Supported within scope (source first)

- **Single result algebra:** `FOUNDATIONS.md:322-451` meets E1:
  - five verdicts, which conserve RF-012;
  - a separate performance coordinate (`not_performed` and `unconfirmed` never pair with `satisfied`);
  - effect values that never let `unknown` become `not_requested` or `completed`;
  - total, reason-sensitive refinement maps, under which a missing reason yields `indeterminate`;
  - availability, fitness and acceptance kept as separate predicates.
- **Result conjunction:** `FOUNDATIONS.md:453-579` conserves the predecessor's Result Conjunction and Applicability rules (RF `:589-608`, `:674-690`):
  - the required set comes from the coverage contract, not from the returns received;
  - a falsification is kept when other results are missing;
  - precedence is falsified, then invalid_basis, then out_of_frame, then indeterminate;
  - an empty list proves nothing;
  - the regrouping and associativity argument is stated mathematically.
- **AC-007 (no coercion to success):** carried by the refinement rule at `:433-435`.
- **Work-Carrier-To-Execution:** `TICKET_METHOD.md:741-798` matches predecessor `:639-696` text for text on all five rows, the no-substitute-ticket rule, drafting versus admission, the admission coordinates, the durable result surface (refuse if absent) and handling of surviving obligations. New material at `:723-739` and `:800-805` adds derivation and core-result binding without changing the decisions. The admission reason domain (`:826-845`) maps every value to exactly one core value, and an override leaves the original verdict in place.
- **Generic human/software/mixed assessment:**
  - `SPEC_METHOD.md:908-938` (binding, reuse of a calculus, a person performing a procedure is not human adjudication, human decisions preserved);
  - `:1831-1833` (optional profile adds duties only when adopted);
  - Foundations `:903-905` (event log not required) and `:976-977`.

  These meet conformance rows 56-59. Ambiguity governance (`:1264-1296`) keeps the predecessor's human-adjudication and probabilistic policy and maps it to the core results.
- **Bounded Causal Construction:** the predecessor's default that a seam is inside the cone (`:1550-1551`) survives through Contract application Support (`TRANSFORMATION_LIBRARY.md:132-137`).
- **Changed paragraph copies:** the text is the same in `frames/WORK_RECOVERY.md:566`, `MEMBER_CONSTRUCTION_ASSESSMENT.md:621`, `TRIAGE_CARRIER.md:1028` and `authority_compressions/spec_method.compressed.md:379-380`. No remaining "live code" wording was found in candidate Markdown.
- **The five carrier dependencies** (help, review, status and ticket depend on PRODUCT_BASIS; the refresh adapter depends on REFRESH):
  - each skill's source calls the procedure before any effect;
  - PRODUCT_BASIS is read-only and grants no authority;
  - the forward `dependencies` edges are present in `interpretation/source-account.json` (lines 5935, 6477, 6615, 6749, 6884, 7023).

  I did not check the generated inverse `consumers` in `program.json` (long lines).

### Eleven unmatched positive consumer pairs (`evidence/rc1/integration/CONSUMER_RELATIONS.json`) — source-based contributions only, no resolution claimed

| Pair | What the source shows |
|---|---|
| risk-and-assurance-selection → UP-014 | UP-014 cites no such rule. The positive looks stale. The real consumers are Spec `:1983` and Transformation Library `:363` and `:458`. This connects to D2. |
| construction-assurance → TL.evaluate, TL.conjoin, TICKET condition-based-closure | The consumers cite child sections instead: TL `:333`, `:339`, `:361`, `:363`; Ticket `:1060`. Use is supported; the mismatch is parent-versus-child granularity. |
| assertions-and-observations → judgment-and-authority | Foundations `:256-259` actually uses the relation but links the parent section. Supported; the reciprocal declaration is missing. |
| change-impact → universal-intake-triage | Searching Spec found no direct citation in `:1378-1471`, and I did not read that section. Unresolved. |
| parallel-assurance → configuration | Foundations `:1010-1012` applies the independence condition without a citation. Plausible but not established. |

Pairs not examined: construction-assurance → Baseline assurance-subject, and the three Baseline testing-reassessment pairs.

## 5. Contributions to the six criteria

1. **Disposition completeness:** D1 (disposition value not supported) and D3 (replacement incompletely described). Row coverage outside these rows was not assessed.
2. **Conservation:** supported for RF-012, Applicability and Conjunction, AC-007, Work-Carrier rows 1-5, ambiguity governance and the cone default. D1 is not conserved as recorded. Intake is leaning conserved (disputed).
3. **Accepted replacements:** none. Every relation I saw has `owner_decision: null` (R021, R025, I5-ACCOUNT-R004). They are proposals, not accepted replacements, so no dependent member acceptance follows.
4. **Actual use and context fit:** not assessed. The shared actual-use trial has not been performed. D2 and D4 are entry-route defects that such a trial should exercise.
5. **Fidelity and conformance:** supported for the core result algebra discriminators (conformance rows 37, 38, 56-62, 64) and the changed frame and compression copies. D2 is a fidelity defect at a packaging entry. The a_c program and map fidelity was not assessed.
6. **Governing reduction:** a positive witness that one owner governs conjunction and contract application, and Ticket and Spec consume it rather than keeping rival enums. A counterexample is D2: a rival proof-selection rule at the plugin entry. No path measurements were assessed.

## 6. Coverage and unassessed scope (none of it marked satisfied)

**Read in full:**
- Basis files: INTENT, PRODUCT, requirements/README, ASSURANCE, conformance/README.
- Candidate:
  - FOUNDATIONS `:230-584` and `:845-1022`;
  - TRANSFORMATION_LIBRARY `:60-299`;
  - SPEC_METHOD `:898-962`, `:1215-1324` and `:1735-2037`;
  - TICKET_METHOD `:1-46` and `:723-864`;
  - standards/README;
  - plugin files: PRODUCT_BASIS, REFRESH, refresh adapter, stdo-review, stdo-ticket, stdo-work, GETTING_STARTED `:505-529`;
  - TRIAGE_CARRIER `:1024-1033`.
- Predecessor sections listed in EXPECTATIONS, plus SPEC_METHOD `:1503-1632` and TICKET_METHOD `:676-750`.
- Account and evidence: the conservation rows for the three SPEC rows and the TICKET admission row; the rc1 CHANGED_SCOPE, RETURN.json, source-repair RETURN.md, consumer-account RETURN.md and CONSUMER_RELATIONS; part of CONSERVATION_APPLICABILITY; the I5 core review `:1-70`.

**Not read:**
- AXIOMATIC_CALCULUS, REFERENCE_FRAME_METHOD, DESIGN_MODULE_METHOD, IDENTITY_METHOD and RELEASE_METHOD, in candidate and predecessor bodies.
- Most of SPEC_METHOD and TICKET_METHOD.
- FOUNDATIONS `:1-229` and `:585-844`.
- stdo-help and stdo-status bodies.
- program.json and map.json; account-by-owner; the other two prior reviews.
- PRINCIPLES, CAPABILITIES, A_C_DEPENDENCY, GOALS, REFERENCE_FRAME_BASIS.
- About 680 of the 691 conservation rows.

**Primary members whose own content I did not assess:** AXIOMATIC_CALCULUS, REFERENCE_FRAME_METHOD (successor), DESIGN_MODULE_METHOD, IDENTITY_METHOD and RELEASE_METHOD, beyond their appearance as conjunction and dependency targets.

## 7. Justified reuse

From the I5 core review I reuse only its unchanged-predicate conclusions for Foundations `:324-579` and `:845-996`. The Foundations hash it binds (`a3e19f8a…`) is the member hash listed in CONSERVATION_APPLICABILITY, and the rc1 change touched SPEC_METHOD only. I also read those sections myself and agree with them. I did not reuse its Spec conclusions, because SPEC_METHOD changed.

## 8. Resources

- **Spend:** about $3.8 of the $6 allowance at the time of writing; the parent's measurement governs.
- **Elapsed time and token counts:** not available to me.
- **Acquisition:** about 25 Read and Grep calls inside the scratch directory, with no external calls.
- **Context fit:** not measured, so no fit claim.
- **Stopping point:** I stopped at the scope above to stay within budget. The remaining work is the unread list in section 6, without a restart.
