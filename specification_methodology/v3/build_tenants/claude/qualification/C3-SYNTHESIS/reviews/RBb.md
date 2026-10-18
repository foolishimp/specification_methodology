# RBb: Working Review Of B2 And B5 (EXECUTIVE_BASELINE, DESIGN_MODULE)

Status: same-family working check, not acceptance. Commentary, not specification or design.

| Coordinate | Value |
|---|---|
| Reviewer | RBb, a fresh Claude context activated as Reviewer by the Claude-line Executive |
| Authors of the subject | B2 and B5, fresh Claude Writer contexts; the tenant (Claude line) is the author under the design's reading, so this check is same-family and counts toward no acceptance |
| Subject commit | `4ca18ba` (previous `f7851aa`), read with `git show`; HEAD of the worktree was not used |
| Subjects | `build_tenants/claude/standards/EXECUTIVE_BASELINE.md`, `DESIGN_MODULE.md`; `qualification/C3-SYNTHESIS/returns/B2.md`, `B5.md`; `deltas/B2.md`, `deltas/B5.md` |
| Predecessor | installed `v2.5.1-rc.2` `STDO_REFERENCE_FRAME_BASELINE.md`, `DESIGN_MODULE_METHOD.md`, read-only |
| Not read | `reviews/RBa.md` (a parallel review, untracked) |

Paths are relative to `specification_methodology/v3/`. Line numbers are at `4ca18ba`. `BL:n` is a line of the installed `STDO_REFERENCE_FRAME_BASELINE.md`; `DMM:n` a line of the installed `DESIGN_MODULE_METHOD.md`.

## 1. Expectations, recorded before opening the subjects

Sources read: `specification/requirements/README.md` (all), `specification/conformance/README.md` (all), `C3-SYNTHESIS/EXPECTATIONS.md` (all), `C3-SYNTHESIS/LEDGER.md` (all), FOUNDATIONS §1, §3 and §4 Results and Conjunction, ACTIVATION §1 (opening, Transitions, Configuration, Roles and delegation) and §3 at `4ca18ba`, `PREDECESSOR_CLAIMS.md` rows for the baseline, predecessor baseline `BL:1-710`, `BL:1268-1810`, predecessor DESIGN_MODULE `DMM:1425-1510`.

### Q1. EXECUTIVE_BASELINE as an operational profile

- X1.1 [R §Single Ownership 2, 3; E-4-2, E-4-3] The member states it is an operational profile and owns only its bindings: the executive configuration's frames (Executive, Worker or Writer, Reviewer), the specialist and testing families as profile frames, their grants, limits, prohibitions, carriers and explanation. Generic rules it uses (allocation and reconfiguration, ACTIVATION §1 Configuration; results and no-raise, FOUNDATIONS §4; step refinements, ACTIVATION §3; independence, EVALUATION §3; distinct relation structures, RF-009) are referred to or refined with a named owner. Fails: the profile states a generic rule as its own, or a generic member depends on the profile for one.
- X1.2 [R §Bounded Transitions 4; C rows 20, 21; E-2-4, E-7-12, E-7-13; N-3] The executive configuration is one configuration, selected where it fits; the profile says when it fits and explains its allocation, resource limits and failure assumptions. Direct entry stays lawful; a configuration with other frames is evaluated, not rejected by label. Fails: the profile reads as the method default; its arrangement is unexplained.
- X1.3 [R §Bounded Transitions 4; E-2-6; N-8; `BL:24-30`] Naming or selecting a frame grants nothing; each frame's authority comes from the admitted grant.
- X1.4 [Ledger ruling at A4a; `BL:279-291`, `BL:361-384`, `BL:456-461`, `BL:576-583`, `BL:1340-1349`, `BL:1410-1424`, `BL:1613-1630`, `BL:1755-1766`] Every predecessor MUST or NEVER for the Executive remains in force wherever the configuration is selected, with no weakened modal:
  - no mutation of candidate, Product or worktree bytes and no implementation effect; tool access or an edit being small, test-only, reversible or obvious is no exception; mutation needs a separately activated Worker or Writer with an exact grant, subject and territory; a same-actor role change is explicit and recorded before the effect; a later record or delegation cannot authorise it;
  - no self-review counted as independent: Executive inspection is no Reviewer result; Worker self-review stays Worker evidence and a disposition does not relabel it; the Reviewer is not the author;
  - the five drift locks are revalidated before activation and before disposition, with their failure consequences, and the Executive does not repair by enlarging its frame;
  - disposition is exactly one of the four, inside the admitted grant; Executive activation adds the exact disposition grant; no `authorize` or `no_action` disposition; a hard stop or a falsified mandatory claim is not waived by lowering priority.
  Fails: any of these is dropped, made advisory, or lifted by an operation grant covering a sequence.
- X1.5 [C rows 18, 24; E-7-10, E-7-16; ACTIVATION §1 Coordination across tasks] The Executive decides from closed results; a work or review result never omits a blocker or residual material to delivery; missing information is acquired or kept open, never assumed favourable; frontier items outside attention stay open. Fails: a handoff projection's minimum content allows a material blocker or residual to be left out.
- X1.6 [C rows 22, 23; E-7-14, E-7-15] The profile makes no optimality claim from familiarity or persistence; its own redistribution (role changes, reactivation) keeps obligations, effects and independence.

### Q2. Results

- X2.1 [R §Single Result Algebra 2, 4, 5; E-5-3, E-5-5, E-5-6, N-7] EXECUTIVE_BASELINE §5 work results map to exactly one core value each under ACTIVATION §3 construction availability (predicate "a candidate is available"): `candidate_ready` satisfied, `refused` falsified, `incomplete` falsified, `re_entry_requested` split by cause into `out_of_frame` and `invalid_basis`. The profile refers to that refinement rather than defining a second one. `candidate_ready` is never fitness or acceptance; a refused activation is no work result.
- X2.2 [R §Single Result Algebra 3; ledger D1] No text in EXECUTIVE_BASELINE still pairs `incomplete` with `indeterminate` or maps `indeterminate -> incomplete`. Predecessor loci to check in the successor: Work result (`BL:475-485`), step 3 (`BL:1315-1319`), Derived Worker Frame result row (`BL:637`), qualification item 5 "disjointly mapped from its Reference Frame Method result" (`BL:1666-1668`), project-basis addition "Worker result to Frame Method result mapping" (`BL:1739`). The successor mapping is not injective (two variants reach `falsified`), so "disjointly mapped from" cannot survive unchanged.
- X2.3 [E-5-2; A3] The Executive frame's result (an RF result, priority, boundary effect, disposition) and the Reviewer triage classifiers (`complete`, `indeterminate`, `not_applicable` of the triage payload, `BL:1388-1390`) are either mapped into the core or stated not to be results.
- X2.4 [R §Single Result Algebra 2, 3; ACTIVATION §1 Applicability] DESIGN_MODULE axiom verdicts (`pass`, `fail`, `not_applicable` with a reason, `DMM:1434-1438`) and the design verdict (`accepted` or not, `DMM:1471-1475`) each map to one core value with a stated predicate. For `not_applicable` mapped to `satisfied` under "the design meets the axiom, or the axiom does not apply", the mapping is truthful and non-raising only if: the predicate is declared with the value and travels with it; `not_applicable` needs an established false applicability premise and its reason; an unresolved applicability premise is not `not_applicable` (ACTIVATION Applicability: never read as false); an axiom not evaluated has no result and is a gap; a consumer asking "the design conforms to the axiom" reads the domain outcome, not the core value. Fails: `not_applicable` can be returned for a skipped or undetermined axiom, or the core `satisfied` can be counted as conformance.
- X2.5 [E-8-6, E-8-8; R §Successor Disposition] Rows 516 and 543 `superseded`: justified only if the predecessor claim of those rows pairs `incomplete` with `indeterminate` (it does at `BL:480-482` and `BL:1316-1318`), the accepted successor relation is named, the rest of each section's claim is still carried in successor text, and the row identifiers resolve to the sections holding that text. Read by line of `PREDECESSOR_CLAIMS.md`, line 516 is `Worker` and line 543 is `Complete Engagement Transition`; the pairing text sits in the rows at lines 519 (`Work result`) and 546 (`3. Worker Returns To Executive`). The return must say which sections it means.

### Q3. Family tables F16 and F17

- X3.1 [FOUNDATIONS §3 Foundation to law; R §Standalone Successor 1; E-1-2] Each table sits where the actor enters the family (F16 at EXECUTIVE_BASELINE §3, F17 at DESIGN_MODULE §1, per the FOUNDATIONS index), states labelled instance premises, has exactly the four columns, and refers to FOUNDATIONS §3 for the standing of consequences.
- X3.2 Premise standings match FOUNDATIONS §3: P0 recovered; P1, P2, P3, P4a, P6 independent; P4b derived from P0 and P2; P5 derived from P0 and P6. A profile table names the families it imports under PROFILES §1.
- X3.3 Each consequence names a linked rule that states it; the consequence column states nothing the rule does not; each added choice names its owner or "none".
- X3.4 Every deciding rule of each member is accounted for by a row or by a stated reason. A few rows are not presented as deriving the whole member.

### Q4. Conservation of changed text

- X4.1 [R §Standalone Successor 3; E-1-5, E-8-7] Each changed determination keeps the predecessor's meaning in the successor's own text, or its change is a recorded disposition (`superseded` with relation, or owner removal). Sampling weighted to EXECUTIVE_BASELINE §5 to §7 and §16 to §19 and DESIGN_MODULE §7.

### Q5. Links and writing

- X5.1 Every relative link and anchor resolves at `4ca18ba`; no `build_tenants/codex/` link (PT-7).
- X5.2 [WRITING_GUIDE; memory rule on tone] No undefined new term, floral language, history narration in normative text, person's name, or silent modal change.

Citation corrections found after opening the predecessor in full (the expectations themselves are unchanged): the step 3 mapping sentence is `BL:1321-1322`, the Worker result row `BL:638`, qualification item 5 `BL:1659-1660`, the basis-addition field `BL:1738`. On X2.5: `deltas/B2.md:4-6` states that its line numbers are those of the tenant copy `frontier/PREDECESSOR_CLAIMS.md`, where line 516 is `#work-result` and line 543 is `#3-worker-returns-to-executive`. The identifiers resolve; the numbering concern in X2.5 is closed.

## 2. Results

`EB:n` is a line of EXECUTIVE_BASELINE, `DM:n` of DESIGN_MODULE, `ACT:n` of ACTIVATION, `FND:n` of FOUNDATIONS, all at `4ca18ba`.

| Q | Result | Evidence | Findings (severity; smallest repair below) |
|---|---|---|---|
| 1 | falsified | Owns only its bindings: `EB:3-14`, `EB:120-124`, `EB:138-142`; every generic rule it uses is referred to its owner (`EB:16-32`, `EB:722-731`, `EB:1353-1358`). One configuration selected where it fits: `EB:102-104`, `EB:677-720` with fit, resource limits and failure assumptions; other configurations judged by task, not label or distance (`EB:685-687`, `EB:1318-1326`). Naming grants nothing: `EB:45-47`, `EB:78-80`. Predecessor Executive MUST/NEVER in force where selected: no mutation `EB:500-513` (= `BL:284-291`, plus `ACT:422-425`); no self-review as independence `EB:1078-1079`, `EB:1353-1362` (= `BL:1350`, `BL:1615-1630`); drift locks `EB:590-607` (= `BL:363-384`); disposition grant `EB:758`, `EB:762-765`, `EB:1133-1135`, `EB:1500` (= `BL:576-583`, `BL:1415`, `BL:1761`). No optimality claim (grep). | F-1 material; m1, m2, m3 minor |
| 2 | satisfied, with minor findings | Work results: `EB:408-436` read ACTIVATION §3 construction availability (`ACT:667-688`), each value with one core value for "a candidate is available"; `incomplete` is `falsified` (`EB:425-430`); no text pairs `incomplete` with `indeterminate` (grep: `EB:425-429` and `EB:1723`, `EB:1750` only). DESIGN_MODULE: reconstruction decisions `DM:1275-1310`, axiom verdicts `DM:1407-1439`, design verdicts bound to ACTIVATION §3 Disposition `DM:1450-1477`. `not_applicable` to `satisfied` is truthful and non-raising (reasoning below). Rows 516 and 543 `superseded` is justified against `BL:480` and `BL:1322` (reasoning below). | m4, m5, m6, m7 minor |
| 3 | F16 falsified; F17 satisfied, with minor findings | F16 `EB:188-240`: four columns, labelled instance premises I1-I3, standings consistent with `FND:315-324`, links resolve, every choice has an owner or "none". It leaves deciding rules untraced (F-2). F17 `DM:145-209`: four columns, standing stated in full (`DM:159-163`), I1-I3, 24 rows, whole-member accounting sentence `DM:203-204`. | F-2 material; m8, m9 minor |
| 4 | satisfied, with minor findings | 37 changed or dependent determinations sampled (table below; 30 in EXECUTIVE_BASELINE, weighted to §5 to §7 and §16 to §19, and 7 in DESIGN_MODULE §7 and §10). None lost. One opening that can weaken a determination (m6); one disposition-consistency question (m5). F-1 is a gap against the new common requirement, not a loss: the predecessor had no such field either. | m5, m6 (as above) |
| 5 | satisfied | Relative links: 80 in EB, 130 in DM, and every link in the four returns and deltas resolve with their anchors (checked by slug script at `4ca18ba`; 0 broken). `rc.2 #anchor` provenance routes: 70 in EB and 63 in DM resolve against the installed predecessor headings. No `build_tenants/codex/` link. No person's name. "New in this corpus" sentences state standing, as AC6 requires, not history. Present tense carries obligation (WRITING_GUIDE §9); DM keeps its explicit modal convention (`DM:67-71`). No undefined new term found: "executive configuration" (`EB:677`, `ACT:349-360`), "construction availability" (`ACT:663`), I1-I3 defined in place. | none |

Nothing found is blocking.

### Findings

**F-1 (material; Q1, Q4).** Effects of unknown completion have no carrier in the executive configuration.
- Evidence: the work-result projection's minimum content is "result variant, exact subject if any, transition evidence, non-changes, residuals, stop basis" (`EB:1175`). §12 step 4 lets the Executive "reactivate work" after `refused`, `incomplete` or `re_entry_requested` with no condition on effect state (`EB:1059-1063`). The failure assumptions of §7 (`EB:711-720`) omit an effect of uncertain completion.
- ACTIVATION keeps effect uncertainty apart from residuals: the work state is "the residuals; and the known uncertainty over external effects" (`ACT:999-1001`). It requires that "an effect of unknown completion is resolved sufficiently for the next dependent action before that action" (`ACT:323-325`) and gives effects their own refinement (`ACT:777-797`).
- Neither carrier the work result cites holds effect state. A closed result names "the verdict, the residual uncertainty and the invalidation conditions" (`ACT:1221-1225`). Transition evidence names candidate, relations, paths, seams, proof, non-changes and disposition, but no external effect (`ACT:1244-1249`). Reading "residuals" or "residual uncertainty" as carrying effect state goes against ACT:999-1001, which lists effect uncertainty separately.
- An effectful Worker that stops `incomplete` after a write whose response was lost reaches the Executive with no field naming that effect. The Executive's bounded view then lacks a blocker material to delivery, and reactivating another Worker is the redistribution case of C row 22 (E-2-5, E-7-14) at the profile's own point of use (R §Standalone Successor 2).
- Repair:
  - §13 work-result row: add "each intended effect with its ACTIVATION §3 Effects value";
  - §12 step 4: add "an effect of unknown completion is reconciled under ACTIVATION §5 before reactivation or any dependent action";
  - §7 failure assumptions: add one clause for it.

**F-2 (material; Q3).** F16 leaves deciding rules of its member untraced, and gives no reason.
- The FOUNDATIONS index makes F16 account for the whole of EXECUTIVE_BASELINE (`FND:530`). No row's rule column reaches these sections:
  - §5 Specialist frame (`EB:287-295`);
  - Exact candidate (`EB:451-460`): freeze and stabilisation of the review subject;
  - Baseline-adoption projection (`EB:462-470`);
  - §6 Product-chain basis (`EB:609-635`): the Development Product to Install binding, the mutability of a Source Project under a Worker grant, a repair creating a new candidate;
  - the §7 opening (`EB:637-673`): the three relation structures and the rule that overlap collapses neither evaluation nor authority;
  - §12 step 1 (`EB:996-1002`).
- F17 closes with an accounting sentence (`DM:203-204`). F16 has none.
- Fails E-1-2 and E-1-3 ("a member is silently missing", at section level) and Q3's "every deciding rule accounted for".
- Repair:
  - add a row for Product-chain basis: P3, P6, P4b; choice owner PRODUCT_DEFINITION §7 for the role map;
  - add a row for Exact candidate: P3, P6; F6 imported; freeze owner EVALUATION §7;
  - add a row for the three relation structures: P6, P1; F1, F2 imported; owner of the rule RF-009;
  - add §5 Specialist frame, the baseline-adoption projection and §12 step 1 to the rule columns of rows 11 and 13;
  - close with an accounting sentence as at `DM:203-204`.

**m1 (minor; Q1).** `EB:689-694` puts "every grant, limit and prohibition" in force wherever the configuration is selected.
- Duties are not named: the drift-lock revalidation (`EB:590`), consuming only closed results (`EB:485-487`) and event-driven waiting (`EB:557-563`). They remain in force through §6's present-tense law, so nothing is lost.
- The sentence that guards against selection being read as relaxing the profile is narrower than the predecessor's MUST set.
- Repair: "every grant, duty, limit and prohibition".

**m2 (minor; Q1).** The lead's list of owned bindings (`EB:8-14`) omits §3's additions to direct entry and §4's empirical revision boundary. F16 rows 2 and 3 attribute both to this profile (`EB:221-222`). Repair: add "the additions to direct entry (§3) and the empirical revision boundary (§4)" to the list.

**m3 (minor; Q1).** `EB:730-731` says a compact result carries its blockers in "the residuals and the stop basis of those two projections".
- A review result has no stop basis: its blockers are findings, counterexamples and residuals (`EB:1177`).
- Specialist results also return to the Executive (`EB:1179`) and are not named.
- Repair: "the residuals and stop basis of a work result, the findings, counterexamples and residuals of a review result, and the residuals of a specialist result".

**m4 (minor; Q2).** Rows 516 and 543 read "superseded in its mapping … the rest … conserved" (`EB:1723`, `EB:1750`; `deltas/B2.md:21-22`).
- Reading applied: one disposition value, `superseded`, with a note on what the replacing relation leaves standing. Under that reading E-8-6 holds. The single value still hides that most of each section is conserved in successor text.
- Repair: split each row into child rows, a `superseded` child for the mapping sentence and a `conserved` child for the remainder. The common granularity rule provides child rows.

**m5 (minor; Q2, Q4).** Rows 522, 560 and 565 keep `conserved` (`EB:1729`, `EB:1767`, `EB:1772`; `deltas/B2.md:41`, `:47`, `:50`).
- The predecessor claims are:
  - "one Reference Frame Method result plus exactly one … variant" (`BL:638`);
  - "every Worker work-result variant is disjointly mapped from its Reference Frame Method result" (`BL:1659-1660`);
  - "every Worker result maps exclusively from one closed Reference Frame Method result" (`BL:1890`).
- The successor text (`EB:820`, `EB:1394-1396`, `EB:1627-1630`) drops the accompanying result and its disjointness: `refused` and `incomplete` now share `falsified`. The meaning changes because of the same replacement that supersedes 516 and 543.
- Under E-8-7 a lossy paraphrase does not conserve. Consistency with 516 and 543 gives `superseded` in that item, with the same relation.
- The Executive confirmed `conserved` (`LEDGER.md:182`); this check records the inconsistency and leaves the decision there.
- Repair: a `superseded` child row for obligation 5 and for condition 4, or a stated argument that the predecessor's purpose (a closed, total, exclusive classification after lawful activation) is the conserved meaning.

**m6 (minor; Q2, Q4).** The §19 mapping field (`EB:1477-1479`) admits "any project refinement of a work-result value mapped under FOUNDATIONS §4 Results".
- FOUNDATIONS §4 Refinements (`FND:717-729`) states no parent-value rule. The ledger's B8 ruling (a child maps to its parent's core value; `LEDGER.md:217`) is stated only in AXIOMATIC_CALCULUS (`:915-919`) and TRAVERSAL_OCCURRENCE (`:955-956`).
- So a project child of `incomplete` mapped to `indeterminate` is barred only by reading `ACT:688` ("never to `indeterminate`") as binding children too.
- Repair in this territory: the field reads "each refined value mapped to its parent value's core value (ACTIVATION §3)". The generic rule belongs in FOUNDATIONS §4 Refinements, which is outside this subject.

**m7 (minor; Q2).** The gate lists "an applicable axiom with no result" as keeping the verdict non-accepted (`DM:1469-1472`).
- An axiom whose applicability is unresolved and which the pack did not evaluate is not named. `ACT:242-246` withholds the dependent claim, so acceptance is still barred by the owner rule, but the gate's own list is narrower.
- Repair: "or an axiom with no result whose applicability is not established false".

**m8 (minor; Q3).** F16's premise column writes "P5 (derived)" and "P4b (derived)" (`EB:223`, `225`, `227`, `229`, `230`, `232`) without the premises the commitments table gives (`FND:322-323`), and its lead does not state them, unlike `DM:159-163`. Imported families appear in rows by ID only. PROFILES §1 asks for the ID and the section in the premise column (`PROFILES.md:35`); the sections are in the lead (`EB:196-205`), as in F17. Repair: add a standing sentence to F16's lead in the form of `DM:159-163`.

**m9 (minor; Q3).** F17 row 2 says "every evaluation under the profile returns a core value" (`DM:179`). The rule it cites says "a performed evaluation" (`DM:44`), and an unperformed evaluation has no result (FOUNDATIONS §4 Not performed). The consequence column states more than the rule. Repair: "every performed evaluation".

### Q2 reasoning

`not_applicable` to `satisfied` (`DM:1418`) is truthful and non-raising:
- The predicate is the disjunction "meets the axiom, or the axiom does not apply". It is declared with the value and travels with it (`DM:1410-1413`), so a `satisfied` never counts toward "the design meets the axiom" (FOUNDATIONS §4 Predicates travel). `DM:1421-1423` says so outright.
- `not_applicable` is a performed evaluation of applicability. It needs a false premise on basis-bound facts and names the excluding authority (`DM:1418`), as `ACT:242-243` requires of any exclusion.
- An unresolved premise supports no `not_applicable` (`DM:1424-1426`). An unresolved premise with a design that fails the axiom is `indeterminate` (`DM:1429-1430`). An unevaluated applicable axiom has no result (`DM:1433-1434`).
- A non-evaluation therefore cannot reach `satisfied`.
- This matches the predecessor gate, where among axiom verdicts only a failed applicable axiom blocked acceptance (`DMM:1471-1475`; the other three blockers there are not verdicts).
- The same pattern stands at REFERENCE_FRAME §8 for authorised exclusions (`LEDGER.md:145`).
- The head keeps the predecessor's discovery-record `not_applicable`, which `DMM:612-615` allows for "a category not searched", out of the core (`DM:55-57`). This prevents a non-performed search from being read as `satisfied`.

Rows 516 and 543 `superseded`:
- The rc.2 claim pairs the values at `BL:480` ("`incomplete` accompanies `indeterminate`") and `BL:1322` ("`indeterminate -> incomplete`").
- `incomplete` covers both not-performed and undecided causes (`ACT:675`). Mapping it to `indeterminate` merges non-performance into undecidability, which R §Single Result Algebra 3 forbids.
- The named relation is that item, applied by ACTIVATION §3 (`ACT:688-696`).
- The replacement value `falsified` for "a candidate is available" is an ACTIVATION §3 choice confirmed by the Executive's D1 ruling (`LEDGER.md:97`); it is not entailed by item 3. The row names both.

### Q4 conservation sample

| # | Predecessor | Successor | Result |
|---|---|---|---|
| 1 | `BL:74-75` optional profile, no independent ownership | `EB:111-113` | conserved |
| 2 | `BL:65-68` adopt or define; existing authority admits; axioms file is no owner | `EB:102-107` | conserved; "selected where it fits, not default" added |
| 3 | `BL:88` REFERENCE_FRAME owns frames, result algebra, conjunction | `EB:122-123` | conserved, owners split (REFERENCE_FRAME; FOUNDATIONS §4) |
| 4 | `BL:121-127` direct entry as Worker (Writer); coordination when direct cannot cover; a name creates no obligation | `EB:152-161`; `ACT:404-411` | conserved at owner and here |
| 5 | `BL:463-469` work result exists only after activation; refusal returns to the assigner | `EB:397-406` | conserved |
| 6 | `BL:471-473` variants are carriers, disjoint by RF result | `EB:413-415` | carriers conserved; disjointness superseded (row 516) |
| 7 | `BL:475-476` `candidate_ready` grounds | `EB:419-421`; `ACT:673` | conserved |
| 8 | `BL:477-479` `refused`: governing prohibition or owner-valid refusal | `EB:422-424`; `ACT:674` | conserved at owner; the profile reading refers to it |
| 9 | `BL:480-482` `incomplete` with `indeterminate` | `EB:425-430`; `ACT:675`, `ACT:688` | superseded, relation named |
| 10 | `BL:483-485` `re_entry_requested` with `out_of_frame` or `invalid_basis` | `EB:431-436`; `ACT:676-677` | conserved, split by cause |
| 11 | `BL:487-488` total and exclusive; payload wording, timing or preference cannot select | removed from EB; `ACT:678-680`; EB names the owner at `EB:411-413` | conserved at owner, not lost |
| 12 | `BL:489-490` activation mismatch is a refusal, not a Worker result | `EB:438-440` | conserved |
| 13 | `BL:492-493` consumers choose the representation | `EB:440-442` | conserved |
| 14 | `BL:284-291` Executive must not mutate; no exception; record before the effect; no retroactive authorisation | `EB:500-513`; `ACT:422-425` | conserved; scope and sequence-grant rule added |
| 15 | `BL:363-384` five locks before activation and disposition; failure consequences | `EB:590-607` | conserved; refusal cause named |
| 16 | `BL:528-538` three relation structures, not one hierarchy | `EB:639-652` | conserved |
| 17 | `BL:577` Executive result | `EB:759` | conserved |
| 18 | `BL:638` Worker result: one RF result plus exactly one variant | `EB:820` | meaning changed, recorded `conserved` (delta row 522; m5) |
| 19 | `BL:1300-1303` refusal to Executive; no manufactured Worker result | `EB:1026-1031` | conserved |
| 20 | `BL:1321-1322` step 3 mapping | `EB:1047-1053` | superseded mapping sentence; notation, after-activation condition and stop rule conserved |
| 21 | `BL:1350` self-review stays Worker evidence | `EB:1078-1079` | conserved |
| 22 | `BL:1410-1424` step 7, exactly one disposition within grant | `EB:1129-1144` | conserved; acceptance-result sentence added |
| 23 | `BL:1454` refusal projection: failed capability or authority predicate | `EB:1174` | conserved, widened to basis |
| 24 | `BL:1538-1550` smallest existing authority admits the configuration | `EB:1253-1271` | conserved |
| 25 | `BL:1574-1597` project configuration record; labels need not be kept; method relations kept | `EB:1296-1326` | conserved; explanation item added |
| 26 | `BL:1615-1630` frames and actors separate; Reviewer not the author; Executive inspection is no review | `EB:1343-1362` | conserved; fresh-context sentence added |
| 27 | `BL:1659-1660` item 5 disjoint mapping | `EB:1394-1396` | meaning changed, recorded `conserved` (m5) |
| 28 | `BL:1738` mapping field | `EB:1477-1479` | conserved by reference; project-refinement opening (m6) |
| 29 | `BL:1890` closure condition 4 | `EB:1627-1630` | meaning changed, recorded `conserved` (m5) |
| 30 | `BL:1778` compression or summary replaces source authority | `EB:1515` | conserved; ACTIVATION §5 rule cited |
| 31 | `DMM:1307-1356` UP-018: reasoning state, two inputs, four decisions, two boundaries, falsifier, withheld-history test | `DM:1252-1324` | conserved, the table word for word; core column added |
| 32 | `DMM:1434-1438` `pass`, `fail`, `not_applicable` with a reason | `DM:1378-1380`, `DM:1415-1419` | conserved; grounds and mapping added |
| 33 | `DMM:1471-1475` both verdicts `accepted`; four blockers | `DM:1443-1448`, `DM:1468-1472` | conserved; tightened to non-satisfied or no-result axioms |
| 34 | `DMM:1477-1481` unchanged `realization_refactor` reuses the verdict | `DM:1479-1484` | conserved |
| 35 | `DMM:1483-1488` co-evolution: provisional evidence; spike | `DM:1486-1492` | conserved |
| 36 | `DMM:1504-1508` absence of an Ontology, view, evaluation or verdict means not complete | `DM:1507-1511` | conserved |
| 37 | `DMM:1882-1904` totality rule | `DM:1699-1716` | conserved; stale owner sentence restated |
