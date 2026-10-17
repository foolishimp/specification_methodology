# Reader report, verbatim: untouched text of the Codex RC1 repair

Fresh Fable agent at maximum effort, source only, pinned to `ad384bbe` against `d1b33480`; 201,403 tokens, 190 tool calls, 63 minutes. The working files it names were in a session scratchpad and are not retained.

**Confirmed.** Text the repair did not touch still decides one of the eight questions, Q2 Intake, differently from its owner. Two rival clauses do this, both in `SPEC_METHOD.md`.

| Scope | Questions affected |
|---|---|
| Rivals found in my sweep | 1 (Q2) |
| Rivals or ambiguous clauses found in my sweep | 2 (Q2, Q5) |
| Including the three given sites | 4 (Q1, Q2, Q5, Q6) |
| No rival or ambiguous clause found in the sections read | Q3, Q4, Q7, Q8 |

My sweep found 2 rivals, 7 ambiguous clauses, about 552 compatible restatements and about 98 deferrals. The given sites add 2 ambiguous clauses and 1 compatible one.

How the findings relate to the repair, from the text alone:
- **Standing conflicts.** Both rivals and all six Q2 ambiguous clauses conflict with Q2 owner text that is identical at `d1b3348` and `ad384bb`. That text is Universal Intake Triage, Computed Classification And Treatment, and the Proportional Disposition rows quoted under A3. The repair neither created these conflicts nor fixed them.
- **Left behind by a repair change.** A2 (BASELINE Anti-Patterns item 10) conflicts with the recheck rule in the Independent assessment section, which the repair added. Given site G3 (RF Worked Binding) restates the RF-005 rule the repair rewrote. Both are ambiguous, not rival.
- **Conflicts with owner text older than the repair.** Given site G1 (BASELINE Anti-Patterns item 11) conflicts with Change impact sentences the repair did not change.

This is a classification of text. I draw no conclusion about the repair process.

## 2. The eight owners

`P = specification_methodology/v3/build_tenants/codex/successor/standards`. Line numbers are at `ad384bb`. "Changed" means the heading block differs between `d1b3348` and `ad384bb`.

### Q1 Reuse: one owner

The owner is `FOUNDATIONS.md` "Change impact and evidence retention" (832–897). The section is marked changed, but the repair touched only 865–866 (the independence clause) and 872–877 (failure disposition). The reuse sentences quoted here did not change:
- "Excluding a check requires supported dependency coverage and a reason the change cannot invalidate the reused claim. An absent edge proves no non-influence. Unknown impact widens assessment or leaves the dependent assurance unresolved."
- "E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed."
- "The original record keeps its original subject; an applicability relation permits its use for the new claim. A changed digest proves neither invalidity nor equivalence. Changed support reopens affected reliance, not the historical observation."
- "Recovery acquires current reality and invalidates affected reliance without erasing valid work or requiring every check to run again. A role, conversation, component or resumption boundary alone is no invalidator."

Two relays point to it, and both resolve to the owner:
- `FOUNDATIONS.md` "Workspace and context" (untouched): "For reuse, apply [Change impact and evidence retention] …"; "A stored green label is no validity argument."
- `TRANSFORMATION_LIBRARY.md` "Contract application", item 5 Currentness (changed): "apply [Change impact and evidence retention] … to reliance on existing evidence."

### Q2 Intake: one owning standard, but two sections inside it decide re-entry differently (finding)

The owner sections are in `SPEC_METHOD.md`, all untouched: "Universal Intake Triage" (1378–1471), "Counterexample Localization" (1472–1516) and "Computed Classification And Treatment" (1517–1616). The deciding clauses:
- "There is one front door for substantive change."
- "The intake label does not determine the process class."
- "No bug, feature, issue, or other intake may bypass this triage by going straight to code, tests, or release handling."
- "The classification distinguishes a defective realisation, inadequate requirement or design, inaccurate prediction and insufficient observation."
- "`product_reprice`: current product realization changes while directional intent remains stable; re-enters at Product …"
- "`requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Realisation, and Evidence"
- "`realization_refactor`: … re-enters at the realized surface only and must prove no upstream drift"
- "Smaller changes may re-enter below Goals only if they explicitly assert that no upstream constitutional surface is changing."
- "The absence of a declared change class is process drift."
- From Computed Classification:
  - "Expose the smallest lawful re-entry …" (1564).
  - "If that contract remains sufficient for the authorized outcome, reject or locally repair the candidate within its grant. Re-enter the actual governing owner when the explicitly selected desired outcome requires changed meaning or an applicable assessment establishes governing insufficiency." (1593)
  - "A mistaken route is corrected at its smallest affected owner." (1605)

Single ownership holds at the standard level. STDO-SURFACE-001 says: "Each law has one owning standard; other standards consume it by reference." Inside SPEC it breaks down:
- The Method Families row (line 53) lists [Renewal Path] next to Computed Classification and says "Spec owns computed classification, the upward re-entry route and downstream trace closure."
- Renewal Path is the only listed section that describes an upward route, so it holds owner standing for that route.
- It decides differently from triage (R1). That is why R1 ranks first.

Separately, the SPEC preamble (17–18) points to the wrong owner: "the [workspace/context relation](FOUNDATIONS.md#workspace-and-context) governs intake and re-entry." Workspace and context holds no change-class or re-entry-point rule, so this changes no decision.

### Q3 Authority: one owner

The owner is `FOUNDATIONS.md` "Judgment and authority" (230–275, changed):
- "Actor identity, role or frame selection, a document's presence, available capability, shared machinery, implementation reachability, evidence shape and a successful judgment cannot mint, widen, transfer or reconstruct authority. Missing or ambiguous authority leaves the dependent act ungranted and returns the applicable explicit result or owner re-entry. An already-authorized act retains its grant within its current conditions."
- "A grant is carried only within its declared scope; delegation or transfer requires the governing owner's permission."

### Q4 Disposition: no single owner (finding)

Four parts divide the question's aspects without overlapping. No consumer I read sets them against each other.
1. `FOUNDATIONS.md` "Judgment and authority": "Producing a candidate, assessing it and disposing it are separate responsibilities. Evidence establishes only its supported claim; it cannot supply an operation or decision mandate."
2. `TRANSFORMATION_LIBRARY.md` "Dispose" (373–403, changed): "The actor carrying that authority consumes the closed work and evaluation results, then selects only a disposition the mandate permits. The decision is distinct from the assessment it consumes and returns its own predicate-bound core result …"
3. `FOUNDATIONS.md` "Result algebra", decision paragraph (482–485, untouched): "A decision result binds the predicate “disposition D on subject S at basis B was made under mandate M by its bound authority”. A lawful rejection can satisfy that predicate while candidate fitness remains undecided. Recording the decision is not its authority."
4. `SPEC_METHOD.md` "Proportional Disposition" (1925–1976, changed) supplies the domain conditions. The table rows quoted here are not inside a repair hunk.
   - `local_repair`: "a demonstrated defect defeats the claim while the governing relation remains coherent"
   - `re_enter`: "the intended candidate cannot satisfy an interpretable current contract without an owning-layer change", or "the governing requirements cannot supply a coherent interpretation for this assessment"
   - `reject`: "the candidate violates a governing relation or leaves an undisposed competing truth path"
   - "A proposed remedy requires supported cause and authority; the verdict alone neither selects a remedy nor forbids useful authorised repair."

### Q5 Independence: one owner

The owner is `FOUNDATIONS.md` "Independent assessment" (276–302), a section the repair added in full:
- "The governing contract selects whether independent assessment is required and which authorship, evidence, reference-exposure, actor or configuration conditions apply to the claim. Where nonauthor assessment is required, its assessor has not materially authored the subject or the repair being assessed. Self-review remains authoring evidence; a human acceptance decision cannot turn it into independent assessment."
- "Reporting a defect, supplying a counterexample or identifying behavior already required by an owning rule does not itself author the repair; that assessor may recheck the defect. Material wording, policy or design adopted in the subject is authorship."
- "Actor identity, a fresh context or a different model family alone establishes none of the required independence." … "This contract selects no extra review boundary, reviewer count or model family."

Before the repair, TICKET STDO-UP-007 at `d1b3348` read: "Where independent review is required, the reviewer is not the author of the reviewed subject …". At `d1b3348`, none of FOUNDATIONS, TICKET, BASELINE, SPEC, RF or TL had a recheck rule. UP-007 at `ad384bb` now applies [Independent assessment].

There is one stale pointer. The BASELINE "Status And Authority Boundary" table (line 111, untouched) still names UP-007 as the owner: "| author/implementer and independent-review separation | `TICKET_METHOD.md` `STDO-UP-007` | supplies Reviewer independence and exact-verdict traceability |". It still reaches the owner through UP-007, so no decision changes. The same section also says: "A profile statement that contradicts its cited owner is a defective application and requires revision".

### Q6 Result values: one owner

The owner is `FOUNDATIONS.md` "Result algebra" (364–494, untouched). It defines five verdicts, three performance values with their legal pairings, and six effect values.
- `invalid_basis`: "The subject, governing basis or required interpretation is invalid for the claimed evaluation."
- `indeterminate`: "The available admissible evidence does not decide the predicate."
- "A domain refinement preserves that qualified original outcome and supplies a total, reason-sensitive map into this record."
- "A missing required reason maps the claimed predicate to `indeterminate`".
- "No refinement turns failure, undecidability, non-performance or unknown effect completion into greater standing."
- "A not-applicable classification needs a supported applicability judgment".

### Q7 Stops: no single owner, but the four parts agree (finding)

I found no case where the four parts decide differently.
1. "Bounded construction" (960–1063, changed):
   - "Applicable responses include continuation, repair, recovery, re-entry, refusal, yielding or termination under the actual grant."
   - "Stopping can be lawful without completion. Completion needs the required evidence and acceptance conditions on the current candidate."
   - "Repeating a failed relation needs a supported causal change; elapsed activity is no repair. Exhausting a limit proves neither completion nor impossibility."
2. "Result algebra", stop paragraph (489–493, untouched): "A stop reports the actual destination or task predicate through this record … Lawfulness of stopping is a separate decision predicate."
3. "Finite capacity and total handling" (201–229, changed): "The actor acts on an already authorized response, requests the owning decision, or stops with an explicit unresolved result".
4. "Workspace and context" (untouched): "The cycle can stop after any operation without inventing completion."

### Q8 Combination: one owner

The owner is `FOUNDATIONS.md` "Result conjunction" (495–622, untouched).
- Precedence runs falsified, then invalid_basis, then out_of_frame, then indeterminate, then satisfied.
- "The required set comes from the composite's applicability and coverage contract, not from the list of returns received."
- "An empty list proves nothing unless the declared required set is established as empty."

## 3. Rivals and ambiguous clauses, ranked by materiality

All nine sit in heading blocks that are identical at `d1b3348` and `ad384bb`.

### R1. Rival (Q2), high: SPEC "Renewal Path"

- **Location:** `SPEC_METHOD.md`, "Renewal Path", lines 2945–2946.
- **Quote:** "3. If the gap is constitutional (not just a missing implementation), new goals and/or intent are written / 4. The repriced surface then flows forward through the chain: product → requirements → design → realisation"
- **Owner clauses it contradicts:**
  - Triage `requirement_reprice`: "constitutional truth changes while project direction remains stable; re-enters at Requirements".
  - Triage `product_reprice`.
  - "Smaller changes may re-enter below Goals only if they explicitly assert that no upstream constitutional surface is changing."
  - Computed Classification: "Expose the smallest lawful re-entry".
- **Why rival and not ambiguous:**
  - Renewal Path has only two branches: "missing implementation", or "constitutional", which leads to new Goals or Intent.
  - The owner calls a requirement-level change "constitutional truth changes" and re-enters it at Requirements. So "constitutional" here cannot mean only Goals or Intent.
  - Nothing else in the section narrows step 3. "The gap must be concrete before it becomes intent" reinforces it, and "gaps … feed back into repricing" names no layer.
- **Case:** The Product definition says exports preserve UTC timestamps. The requirements omit that guarantee, and a deployment scenario finds exports shifted to local time. Direction and Product are stable.
  - Owner: `requirement_reprice` at Requirements, with the explicit assertion that nothing upstream changes, then Design, Realisation and Evidence.
  - Renewal Path: write new Goals or Intent, then re-derive the chain from Product down.
  - The two differ in change class, re-entry layer, deciding owner and what must be re-proved downstream.
- **Contrast:** TICKET "Upward Propagation Check" consumes the owner correctly: "actual requirement insufficiency re-enters its owner; … An actual upstream Goal, Intent or Product change follows its owner."

### R2. Rival (Q2), moderate to high: SPEC "Drift Signals", last bullet

- **Location:** `SPEC_METHOD.md`, "Trace Closure And Anti-Drift Rule", subsection "Drift Signals", lines 3016–3017.
- **Quote:** "If a real use case reveals a gap not expressible in current requirements, a new intent is needed, not a code hack."
- **Owner clauses it contradicts:** triage `requirement_reprice` and `product_reprice` (direction stable, so re-entry at Requirements or Product), and the smallest-lawful-re-entry rule.
- **Case:** Customers need bulk export of 10,000 records, which falls within the Product's stated export capability. The requirements carry no performance bound.
  - Owner: `requirement_reprice` at Requirements.
  - Drift Signals: new Intent.
- **Fairness:** the bullet's main point is "not a code hack", which agrees with the owner's ban on bypassing triage. It still decides, because it names Intent as the destination layer without any condition.

### A1. Ambiguous (Q2), moderate: SPEC "Constitutional Chain", Repricing bullet

- **Location:** `SPEC_METHOD.md`, line 1123.
- **Quote:** "**Repricing** updates goals, intent, product, requirements, design, or realisation when the system no longer harmonizes. When gap analysis reveals constitutional insufficiency, it generates new **Goals** and/or **Intent**."
- **Owner clauses:** as for R1.
- **Case:** the UTC case from R1. The second sentence sends it to new Goals or Intent; the owner sends it to Requirements.
- **Why ambiguous and not rival:** the first sentence allows repricing at any layer. That supports a reading where only top-level insufficiency produces new Goals or Intent, which is compatible. Read next to R1, the second sentence restates R1's rule in the method's core definition.

### A2. Ambiguous (Q5), moderate: BASELINE "Anti-Patterns" item 10

- **Location:** `STDO_REFERENCE_FRAME_BASELINE.md`, line 2023.
- **Quote:** "Reviewer edits or directs repair while retaining independent-review status;"
- **Owner clause:** "Reporting a defect, supplying a counterexample or identifying behavior already required by an owning rule does not itself author the repair; that assessor may recheck the defect. Material wording, policy or design adopted in the subject is authorship."
- **Case:** A Reviewer returns `falsified` with "R-3 requires empty input to be refused; the candidate accepts it; repair per R-3". It contributes no design or wording. The Worker repairs, and the same Reviewer rechecks.
  - This is exactly the owner's exception for "identifying behavior already required by an owning rule". The recheck counts as independent.
  - If naming the required repair counts as "directs repair", AP10 strips the Reviewer's independent status, so a fresh Reviewer is needed. That conflicts with the owner's statement that it "selects no extra review boundary, reviewer count".
- **Why ambiguous:**
  - "Edits", and "directs" meaning prescribing design adopted in the subject, are both authorship under the owner. Those readings are compatible.
  - "Directs" in the Executive sense is a decision-authority matter, not an independence matter. The member's own Failure Classification keeps the two apart: "Reviewer implements the fix while retaining its verdict | violation of `STDO-UP-007` independence and frame authority" is a separate row from "Reviewer assigns priority, blocks promotion, directs repair, or activates another frame | Reviewer-to-Executive decision-authority bleed".
  - Only AP10 ties directing repair to independence.
- **Context from changed sections (not swept):**
  - Derived Reviewer Frame: "Reviewer may assess likely repair complexity and regression risk without becoming the repair owner."
  - Actor Binding And Independence: "Where independent review is required, apply [Independent assessment] …"
- **Relation to the repair:** the recheck rule is new. Before the repair, AP10 had no rule to conflict with.

### A3. Ambiguous (Q2, also touches Q4), moderate to low: BASELINE "Failure Classification" row

- **Location:** `STDO_REFERENCE_FRAME_BASELINE.md`, line 1971.
- **Quote:** "| implementation produces a coherent capability that is not the selected Product | Product-frame falsification and Product re-entry |"
- **Owner clauses:**
  - Computed Classification: "If that contract remains sufficient for the authorized outcome, reject or locally repair the candidate within its grant. Re-enter the actual governing owner when the explicitly selected desired outcome requires changed meaning or an applicable assessment establishes governing insufficiency."
  - Proportional Disposition `re_enter`: "the intended candidate cannot satisfy an interpretable current contract without an owning-layer change". This row is outside the repair hunks.
- **Case:** The selected Product is a CSV-to-JSON command-line converter, and its definition is clear. The Worker delivers a coherent CSV-viewer GUI.
  - Owner: reject the candidate or repair it locally within the grant. No Product re-entry.
  - Row: Product re-entry.
- **Mitigation:** the column is headed "First diagnosis", and the section ends "The table routes evaluation. It does not predetermine a verdict." But a re-entry route is not a verdict, so that sentence does not cancel the row. "Product re-entry" might also mean evaluating in the Product frame rather than repricing Product.

### A4. Ambiguous (Q2), low: DESIGN "Proportional Design Sequencing"

- **Location:** `DESIGN_MODULE_METHOD.md`, lines 482–485.
- **Quote:** "Repeated or cross-cutting material surprises are evidence that the affected design cut is underconstrained and require one bounded `design_reframe`; retained code remains provisional evidence until that reframe is accepted."
- **Owner clause:** triage diagnoses the cause ("defective realisation, inadequate requirement or design, inaccurate prediction and insufficient observation") and "Bind[s] the supported cause to the change classes".
- **Case:** Repeated surprises in a refund flow come from an ambiguous requirement: does a refund restore promotional credit?
  - Owner: `requirement_reprice`, or more observation while the cause is unresolved.
  - Clause: `design_reframe`.
- **Mitigation:** the paragraph opens with "previously hidden architectural ambiguity". The section also bars implementation from choosing to "select the missing semantic answer, rewrite upstream truth to legalize itself", so a reframe would have to escalate. The clause still picks the class from the symptom, not the cause.

### A5. Ambiguous (Q2), low: SPEC "Spec-Drivenness Litmus" item 11

- **Location:** `SPEC_METHOD.md`, line 302.
- **Quote:** "Drift is discovered, but the constitutional source is not repriced."
- **Owner clause:** `realization_refactor` "re-enters at the realized surface only and must prove no upstream drift".
- **Case:** A regression makes code violate a sound current requirement. Drift Signals counts this as drift ("either code is wrong …").
  - Owner: fix the code and reprice nothing.
  - Litmus 11 read literally: the work "is not genuinely spec-driven".
- **Why low:** "drift" may mean drift on the specification side only, and the item is a test rather than a routing rule.

### A6. Ambiguous (Q2), low: SPEC "Verification Layers"

- **Location:** `SPEC_METHOD.md`, line 2626.
- **Quote:** "When a scenario fails, the gap is between the system's actual behavior and its claimed capability — not between the spec's words and the spec's other words."
- **Owner clause:** triage lists "scenario failure" as an intake and diagnoses its cause among the four classes.
- **Case:** A scenario written against superseded requirement wording fails, while the system meets the current requirement.
  - Owner: the defect is in the scenario, which is part of the specification.
  - Clause: rules out exactly that location.
- **Why low:** the sentence mainly describes what scenarios are for.

### A7. Ambiguous (Q2), low: SPEC "Drift Signals", events and projection bullet

- **Location:** `SPEC_METHOD.md`, lines 3007–3008.
- **Quote:** "If events and projection reveal persistent delta, either code is wrong or the requirement/design stack is stale."
- **Owner clauses:** triage's "insufficient observation"; TL "Faithful projection" (untouched): "Failure re-enters the first owning defect: source ambiguity, interpretation, projection, producer or consumer."
- **Case:** A read model shows persistent delta because the observation boundary misses one event source. The producer code and the requirements are both correct.
  - Owner: insufficient observation.
  - Clause: offers only two locations, neither of which applies.
- **Why low:** "code" can be read to include projector code.

### Near misses judged compatible (not counted above)

- SPEC UP-021 requires validation when a trust boundary is crossed. This is an authentication gate, and the owner keeps mandatory gates.
- SPEC UP-008: "a broad digest may conservatively invalidate review". This matches the owner's rule that unknown impact widens assessment.
- SPEC Sprint Execution Boundary: "accepts compliant work". TICKET Sprint Close Review binds the decision predicate.
- RELEASE Phases, Release-Scoped Assets and Coordinated Cohorts require a higher RC whenever bytes change. Each is either a new subject or a declared release rule ("a release rule … can justify wider testing").
- ODD, WORLD_MODEL and TL: a changed basis "invalidates the import until reevaluated".
- TRAVERSAL: "A readiness judgment can authorize dispatch". The member's Effect Relation binds the owner-issued grant: "Profile construction and occurrence admission supply none of that grant."
- IDENTITY: "changed sources require new verification material before reuse". This is a domain byte-predicate rule.

## 4. Counts

**What a count is:**
- The unit is one noted classification entry. One entry may cover several quotes from the same section under one tag.
- An entry that bears on several questions counts once under each.
- Given sites are excluded.
- The figures come from a script over my notes, with three hand corrections, so they are approximate.
- "Owner sections" counts sections, not clauses.

**By question:**

| Question | Owner sections | Defers | Compatible | Rival | Ambiguous |
|---|---|---|---|---|---|
| Q1 Reuse | 1, plus 2 relays | 24 | 83 | 0 | 0 |
| Q2 Intake | 3 (SPEC) | 8 | 47 | 2 | 6 |
| Q3 Authority | 1 | 4 | 147 | 0 | 0 |
| Q4 Disposition | 4 parts | 4 | 70 | 0 | 0 |
| Q5 Independence | 1 | 9 | 25 | 0 | 1 |
| Q6 Result values | 1 | 22 | 76 | 0 | 0 |
| Q7 Stops | 4 parts | 13 | 49 | 0 | 0 |
| Q8 Combination | 1 | 14 | 55 | 0 | 0 |
| **Total** | | **98** | **552** | **2** | **7** |

**By member** (FOUNDATIONS and TL counts cover only their untouched text outside the owner sections):

| Member | Owns | Defers | Compatible | Rival | Ambiguous | Given |
|---|---|---|---|---|---|---|
| FOUNDATIONS | Q1, Q3, Q4 parts 1 and 3, Q5, Q6, Q7, Q8 | 3 | 10 | 0 | 0 | |
| TRANSFORMATION_LIBRARY | Q4 part 2; Q1 relay | 9 | 22 | 0 | 0 | |
| SPEC | Q2; Q4 part 4 | 25 | 87 | 2 | 4 | |
| BASELINE | | 16 | 89 | 0 | 2 | G1 ambiguous, G2 compatible |
| TICKET | | 7 | 33 | 0 | 0 | |
| REFERENCE_FRAME | | 10 | 44 | 0 | 0 | G3 ambiguous |
| DESIGN | | 12 | 67 | 0 | 1 | |
| RELEASE | | 5 | 40 | 0 | 0 | |
| ODD | | 0 | 59 | 0 | 0 | |
| WORLD_MODEL | | 4 | 21 | 0 | 0 | |
| TRAVERSAL | | 3 | 29 | 0 | 0 | |
| AXIOMATIC_CALCULUS | | 4 | 39 | 0 | 0 | |
| IDENTITY | | 0 | 12 | 0 | 0 | |

**Compatible examples:**
- DESIGN 11D (Q1): "A new role, conversation or review occurrence does not itself require re-authoring … Missing, stale or ambiguous coverage is not a no-delta proof."
- AC-017 (Q1): "Changing observations reopens affected reliance under the shared currentness rule; unchanged independent support remains reusable."
- RELEASE Position (Q2): "Release handling is downstream of intake triage. … The existence of an RC window does not authorize untriaged mutation."
- TRAVERSAL Authority And Adoption (Q3): "Profile adoption and record construction supply no semantic, operation, evaluation, admission, decision, correction, continuation or closure grant."
- ODD A8 (Q4): "A lawful decision can be `satisfied` while the edge's fitness remains falsified or unresolved."
- TICKET Recorded Judgment And Owner-Ruling Continuity (Q5): "Reusing the author's J cannot satisfy that condition."
- RELEASE Exact-Cut Qualification (Q6): "`skipped`, `cached green` or any other raw label without deciding support is `indeterminate`"
- AC-007 (Q7): "A bare stop word cannot satisfy a consumer."
- ODD 11.9 (Q8): "Unknown applicability cannot remove required coverage."

**Deferral examples:**
- RELEASE Qualification And Recovery (Q1): "Apply [Change impact and evidence retention] … to any reused qualification on those exact subjects."
- TICKET Change Class (Q2): "Tickets must record the `change_class` declared by intake triage".
- SPEC Collective Reference-Frame Basis (Q3): "Only Product authority may adopt it."
- BASELINE step 7 (Q4): "acts on exactly one `STDO-UP-020` disposition within its grant".
- RELEASE Acceptance Criteria (Q5): "independent exact-cut review passed where required".
- RF-010 (Q8): "Use [Result conjunction] … for the result relation."

Owner examples are in section 2.

## 5. The three given sites

Another reader supplied these three sites; I did not find them myself. I judged them only after my own sweep was complete.

### G1. Ambiguous (Q1), moderate: BASELINE "Anti-Patterns" item 11

- **Location:** `STDO_REFERENCE_FRAME_BASELINE.md`, line 2024.
- **Quote:** "changed candidate or basis reuses the predecessor verdict;"
- **Owner clauses:**
  - "The original record keeps its original subject; an applicability relation permits its use for the new claim. A changed digest proves neither invalidity nor equivalence."
  - From Independent assessment: "Changed subjects, tests or assessment conditions apply [Change impact and evidence retention] before the former evidence supports a new claim."
- **The question that decides it:** the owner forbids carrying the old result over as the new candidate's verdict, because the record "keeps its original subject". It permits using the old record for the new claim through an applicability relation. AP11's word "verdict" does not say which of the two it condemns.
  - If it condemns relabeling, it is compatible.
  - If it condemns any reliance on the old result, it is a rival.
- **Case:** The Reviewer satisfied "parser rejects empty input" on candidate C1. The Worker then repairs an unrelated log line, producing C2.
  - Owner: keep the parser result for C2 through an applicability relation, backed by dependency coverage, and re-review only the affected claims.
  - AP11 read literally: relying on the old result is a misapplication, so the parser claim must be re-reviewed.
- **Mitigation in the same member:**
  - Testing Reassessment And Evidence Reuse: "Retain each old execution's subject and establish the applicability relation needed to use its evidence on the new claim." and "Supported unaffected evidence need not be re-executed solely because another dependency changed".
  - Work result: "changed evidence revises only affected results, preserving originals and supported surviving claims".
  - Step 7: "An affected review is reactivated against that candidate."

  These favour the compatible reading, but AP11 itself carries no qualifier.
- **Relation to the repair:** the Change impact sentences it conflicts with (867–870) are outside the repair hunks.

### G2. Compatible (Q1): BASELINE "Product-Chain Basis"

- **Location:** `STDO_REFERENCE_FRAME_BASELINE.md`, line 482.
- **Quote:** "Repair advances the workspace, creates a new candidate, and invalidates affected results."
- **Reasons:**
  - The owner has the same structure: "Recovery acquires current reality and invalidates affected reliance"; "Changed support reopens affected reliance, not the historical observation."
  - "Affected" limits the scope.
  - The member's integration-frame row has the same shape and states reuse explicitly: "invalidates affected conclusions; unchanged valid evidence and owner rulings remain reusable".
  - Unknown impact is covered elsewhere in the member: "Unknown influence cannot justify dropping a test".
- **Remaining risk:** if "results" meant the historical record rather than reliance on it, the clause would contradict "not the historical observation". The clause gives no instruction about historical records, so I do not adopt that reading.

### G3. Ambiguous (Q6, also touches Q1), low to moderate: RF "Worked Binding: Product-Chain Drift Evaluation", Stop And Change

- **Location:** `REFERENCE_FRAME_METHOD.md`, line 1284, inside the fenced example.
- **Quote:** "invalid_basis on stale or substituted basis;"
- **Owner clauses:**
  - Result algebra: `invalid_basis` means "The subject, governing basis or required interpretation is invalid for the claimed evaluation."
  - Change impact: "A changed digest proves neither invalidity nor equivalence."
- **The rewritten consumer rule:** RF-005 at `ad384bb`, read only to judge this site, says:
  - "An attempted evaluation whose stale, ambiguous or mismatched governing basis cannot support interpretation of its bound predicate returns `invalid_basis` or requires reactivation on a resolved basis."
  - "Stale supporting evidence under an interpretable governing basis instead follows [RF-012]: insufficient support leaves the predicate `indeterminate` …"
  - "A basis advance … does not by itself invalidate a historical result."

  At `d1b3348`, RF-005 said: "A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or requires reactivation." The example still states that older rule.
- **Case:** An activation is pinned to checkpoint K1, and the workspace advances to K2 mid-evaluation. K1 is still interpretable.
  - Example: stop with `invalid_basis`.
  - Owner and repaired RF-005: the K1 result stands for K1; relying on it at K2 needs an applicability relation; stale supporting evidence gives `indeterminate`.
  - "Substituted basis" giving `invalid_basis` is compatible.
- **Materiality:**
  - It is lowered because the example declares itself non-normative: "This non-normative example demonstrates a complete prose binding."
  - It is raised because the example is written to be copied: "A consumer replaces them with its own exact identities and source routes."
  - The Frame Qualification basis test ("Does stale, mismatched, or ambiguous basis information invalidate or refuse the evaluation?") is posed as a question and does not decide the case.

## 6. Coverage

**Method.**
- I read only through `git show` and `git diff`, pinned to `ad384bb` and `d1b3348`.
- A heading block counts as changed when any `git diff -U0 d1b3348 ad384bb` hunk touches it.
- I read every untouched block whole and skipped changed blocks.
- I read changed blocks only for a stated purpose:
  - marked * below: read as an owner, not swept;
  - marked † below: read as context for one judgment.

| Member | Untouched blocks read whole | Changed blocks skipped | Not reached |
|---|---|---|---|
| FOUNDATIONS | 15 | 11 | 0 |
| TRANSFORMATION_LIBRARY | 13 | 4 | 0 |
| SPEC | 77 | 5 | 0 |
| BASELINE | 63 | 8 | 0 |
| TICKET | 49 | 2 | 0 |
| REFERENCE_FRAME | 75 | 7 | 0 |
| DESIGN | 64 | 1 | 0 |
| RELEASE | 23 | 0 | 0 |
| ODD | 50 | 0 | 0 |
| WORLD_MODEL | 83 | 0 | 0 |
| TRAVERSAL | 27 | 0 | 0 |
| AXIOMATIC_CALCULUS | 39 | 1 | 0 |
| IDENTITY | 25 | 1 | 0 |

**Changed blocks skipped:**
- **FOUNDATIONS:** preamble; Finite capacity and total handling*; Judgment and authority*; Independent assessment*; Preservation obligations; Assertions and observations; Parallel assurance and provenance; Change impact and evidence retention*; Bounded construction*; Configuration; Core contract derivations.
- **TL:** Contract application (item 5 read to resolve the Q1 relay); Bind; Evaluate; Dispose*.
- **SPEC:** Construction, Assessment, And Delegation; Proportional Disposition*; Transition Evidence And Proof Cadence; STDO-UP-022; Method.
- **BASELINE:** Engagement Applicability; Executive Attention, Evaluation, And Action; Derived Executive Frame; Steel-Thread Delivery; Derived Worker Frame; Derived Reviewer Frame†; Actor Binding And Independence†; Profile Qualification.
- **TICKET:** Execution Contract Admission; STDO-UP-007 (only its pointer line at `ad384bb` and its independence sentence at `d1b3348`).
- **RF:** Core Claims; Evaluation; Authority; RF-005†; RF-006; RF-007; Return A Closed Result.
- **DESIGN:** Authority Model.
- **AC:** AC-005.
- **IDENTITY:** STDO-UP-004.

**Not read:**
- The cut files: GLOSSARY_GUIDE, WRITING_GUIDE, POSTING_GUIDE, UX_METHOD, README.md, templates/, schemas/, frames/, authority_compressions/.
- verification_material/. I read IDENTITY's "Derivation Verification Material" section as member text only.
- The common requirements at `4c340f7`. Owners were taken from package text.
- Nothing under `.ai-workspace/`, the Codex tenant's qualification/, release/ or interpretation/, the Claude tenant, or any JSON check or account record. I ran none of the author's tools.
- The scratchpad also holds files I did not write, including one named like another reader's report. I opened none of them.

**Limits:**
- These are one reader's classifications, and the counts are approximate tallies of noted entries.
- Changed sections were outside the sweep. A rival in them is "not examined", not absent.
- For Q3, Q4, Q7 and Q8, and for Q1 and Q6 apart from the given sites, the result is "none found in the sections read". It is not a finding that none exists.
- A block was judged changed or untouched on its own text up to its first subheading. A parent can be untouched while its subsections changed. FOUNDATIONS "Construction assurance", for example, is untouched while four of its five subsections changed.
- I confirmed where the cited deferrals lead (Workspace and context and TL Currentness lead to Change impact; UP-007 leads to Independent assessment). I did not re-sweep the changed sections they cite.
- G3's materiality depends on whether anyone copies the template.
- I draw no inference about the author's intent, process or tests.

**Working files** (my per-section classifications, tally script and section map):
- `/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/f2219060-0bfd-4baf-9b1d-3f863c3f9bd2/scratchpad/notes.md`
- `/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/f2219060-0bfd-4baf-9b1d-3f863c3f9bd2/scratchpad/bin/tally.py`
- `/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/f2219060-0bfd-4baf-9b1d-3f863c3f9bd2/scratchpad/sectmap.txt`
