# Row re-assessment for I3-4a and I3-4b (working check WC-2)

Reviewer: same-family working reviewer, wrote none of the text. Subject commit S = `2a2af3a`. Predecessor P = installed `v2.5.1-rc.2/standards/`, cited P:FILE:lines. Same-family working evidence only. This file accepts nothing.

Terms. A row is a line of `frontier/PREDECESSOR_CLAIMS.md` (the frontier), keyed here by anchor because line numbers in the deltas are older than the frontier at S (for example delta row 794 is line 797 at S). `conserved` means scope, modal force (the strength of "must", "should", "may"), triggers and exceptions are all kept. `meaning change` means at least one is changed; Q10 of the oracle then requires a `superseded` row that is proposed and pending the product owner, with a replacement relation.

Verification mark. V = I read the predecessor and the candidate text myself (P: and S: lines given). D = I judged from the quotations in the activation's delta file, which I read at S; I did not re-read the locus. Rows marked D keep the delta's judgement unless I say otherwise.

## 1. Rows I judge a meaning change that the frontier does not mark proposed

| # | Row (frontier line at S) | Predecessor | Candidate at S | Why it changes meaning | Smallest repair |
|---|---|---|---|---|---|
| M1 V | Coverage Basis, `#coverage-basis` (PC:351, `conserved`) | P:REFERENCE_FRAME_METHOD:755: "Changing any material member may invalidate the coverage result." | REFERENCE_FRAME.md:645-650: "A change of any member of the tuple that could change the coverage result is a material input change or a changed basis under ACTIVATION §7, and it invalidates the coverage result." | Modal force changes from "may invalidate" (a possibility) to "invalidates" (a rule), for the class "could change the result". The delta (I3-3j) says so itself and asks a reviewer to raise it. The family table at REFERENCE_FRAME.md:179 still says "may invalidate it", so two loci of one rule differ. | Either restore "may" at :647-650 with ACTIVATION §7's materiality as a trigger, or mark PC:351 as a child row `superseded`, proposed and pending the product owner, replacement relation ACTIVATION §7; and make :179 match. |
| M2 V | Technical Triage, `#technical-triage-severity-priority-and-boundary-effect` (PC:516, `conserved`) | P:STDO_REFERENCE_FRAME_BASELINE:450-452: the Product-owned basis "binds the severity scale, priority scale, current-boundary decision cutoff, and non-waivable hard stops." | EXECUTIVE_BASELINE.md:408-416: the basis "names which conditions of the governed outcome are hard stops ... each condition the basis names is an instance of a class that section [ACTIVATION §4] states, and the basis adds no kind of stop." ACTIVATION.md:985-987 says the classes are "Typical hard-stop classes include". | Scope narrows. The predecessor lets the Product's basis bind any non-waivable hard stop. The candidate limits it to instances of ACTIVATION §4 classes, and §4 calls those classes typical, not closed, so the new limit also contradicts its own owner. The delta flagged the check and judged conserved. | Delete "and the basis adds no kind of stop", or state it as a proposed `superseded` child row pending the product owner. |
| M3 V | Condition-Based Closure And Reuse (the recording sentence; delta row 610 TICKETS UP-006/7 area, tracked under WC1-06) | P:TICKET_METHOD:879-883: "the authorized Writer **may** record the satisfied bounded result in the existing carrier without adding a ticket, Executive appointment, review or design-view recreation solely to mark completion." | ACTIVATION.md:486-491: "the constructor that holds the grant records the satisfied bounded result ... It adds no carrier, coordinating appointment, review or recreated design view solely to mark completion." Row 66 of the ACTIVATION table (line 66) says "the grant holder records the conditions it found satisfied". | "may record" (permission, no duty to record) becomes a plain present-tense rule, which reads as a duty to record. It also adds "records only conditions that were evaluated". The delta quotes the "adds no ... solely" half and not the "may". | Write "may record" at ACTIVATION.md:486 and in row 66, or propose it `superseded`. |
| M4 V, possible | `templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` (PC:820, `conserved`) | P:TPL:154: "Coverage is complete only when every mandatory material evaluation and interaction is closed, or governing authority explicitly retains its residual consistently with the claim." | Template (S): "Coverage is complete as REFERENCE_FRAME.md section 8, Coverage ledger, states; record each material row's status in its values. A `residual` row is `excluded_by_authority` where governing authority explicitly retains its residual ... otherwise `conditionally_covered` or `uncovered`." | The "only when" completeness rule and the word "interaction" are no longer in the template. REFERENCE_FRAME.md:681-720 maps each status to a core value per row but I found no sentence there that says a whole coverage claim is complete only when every row is closed. Not established as a loss; established as a missing locus. | Cite the sentence of REFERENCE_FRAME that carries "complete only when", or restore it in the template. |
| M5 V, low | Acceptance Criteria (PC:400, `conserved`) | P:RELEASE_METHOD:481-482: "all release-blocking gaps are closed or the claimed scope is explicitly narrowed" | RELEASE.md:615-617: "all release-blocking gaps, the findings that block promotion under EVALUATION §5 When a finding blocks promotion, are closed or ..." | The predecessor leaves "release-blocking gaps" undefined. The candidate equates them with findings meeting EVALUATION §5's four conditions. A gap that is not a finding (for example a missing required artifact) falls out unless it is also a finding. Scope may narrow. | Use "including" instead of the appositive, or name the extra gap kinds. |

Judged conserved but worth the owner's eye (not counted as meaning changes):
- PC:204 UP-004 (V). P:IDENTITY_METHOD:220: carriers "must not silently widen scope, add a role, increase cardinality, change kind". FOUNDATIONS.md:152-155: "never widen its scope, add a role, increase its cardinality or change its kind". "Silently" is gone. The explicit route is kept, because the next sentence of FOUNDATIONS (:157-158) says elevation, transfer and the rest each need an explicit authority decision, so I judge the outcome the same. IDENTITY.md:67 still says "never silently widen". DESIGN_MODULE `#authority-model` (PC:121, D) keeps rc.2's "implicitly" verbatim while the owner says "never"; the delta flags this. Two wordings of one rule coexist.
- Plugin text, not frontier rows. `plugins/spec/skills/stdo-work/SKILL.md:113-116`: the old "an unknown condition needs a bounded resolution or explicit residual" is now "is unresolved, not false, and the claim that depends on it is withheld until evidence or the owning decision resolves it". The "explicit residual" route is gone. `plugins/spec/references/GETTING_STARTED.md:605`: the freeze of the review subject "where generic-method qualification requires it" is replaced by freeze for every required independent review (see WC2-01 in WC-2).

## 2. Frontier cells that contain "superseded"

Checked at S with a script over `frontier/PREDECESSOR_CLAIMS.md`. 27 table lines contain the word.
- Each of rows 162, 210, 512, 518, 525, 528, 548, 559, 567, 573, 660, 671, 686 and 797 says "superseded, proposed and pending the product owner's acceptance". Pass.
- Row 610 uses "superseded" for a repricing state of an obligation (retained, superseded, deferred, withdrawn), which is not a supersession of a predecessor claim. Pass, but the cell could say so.
- Rows 805 to 814 (the ten authority compressions) say "unresolved; proposed superseded by projection from the a_c set program ... pending the product owner's ruling". They do not use the required phrase "proposed and pending the product owner's acceptance"; they say "ruling". Disposition `unresolved` is tolerated for packaging rows at [R]. Finding WC2-07.
- No cell says accepted. Header line 5 says no disposition is accepted.

## 3. Row-by-row

Notation: P:BASE = STDO_REFERENCE_FRAME_BASELINE.md; P:SPEC = SPEC_METHOD.md; P:TICKET = TICKET_METHOD.md; P:TOP = TRAVERSAL_OCCURRENCE_PROFILE.md.

### 3.1 I3-2r (WC1 repairs)

| Row | Predecessor | Candidate | Verdict |
|---|---|---|---|
| 364 Revision Actions D | P:RF:636-637 "Changed material inputs or a declared revising observation invalidates ..." | REFERENCE_FRAME.md:911-914 (hunk): "admissible evidence that is material to a closed result, a material input change under ACTIVATION §7, reopens that result" | conserved. Trigger is the predecessor's material input change again. |
| 553 Promotion Constraint Projection D | P:BASE:1428-1441 "determines blocking from the exact affected claim, current mandate, applicable hard stops, and Product-owned cutoff policy" | EXECUTIVE_BASELINE.md:1274-1278 (diff): "For the Executive, the governed outcome or decision that section names is read under the current Product mandate, so the Executive determines blocking from the exact affected claim, the current mandate, the applicable hard stops and the Product-owned cutoff policy." EVALUATION §5 generalises to "the decision owner" and says it is new tier-1 law. | conserved at EB. The general table is new law with purpose stated; it removes nothing. |
| 481 Fundamental Migration Rule V | P:SPEC:2570-2576 "nothing carries forward by default"; "absence ... means 'not yet adopted' and carries no automatic authority" | SPEC_METHOD.md:1483, :1526 keep both, and :1520-1531 separate the adoption decision from the live-surface class. SPEC_METHOD.md:1478-1480 reads "every retained statement ... is explicitly re-adopted" where P says "must be". | conserved. The "must" became an indicative inside a list whose other items are also indicative; low risk. |
| 593 Sprint Close Review D | P:TICKET:284 "the close review must classify and pay down the debt" | TICKETS.md (diff hunk @@ -284): "the close review classifies, under that authority"; `remove` takes `falsified` with no matching disposition | conserved. "must" became "classifies", the same drift as M3 but inside a normative sentence of a section whose own rule says the review decides; low. |
| 439 Product Outcome Conservation UP-013 V | P:SPEC:1360-1363, 1420-1421 "Only material advance projects Product progress ... A regression or unresolved gap blocks further promotion on the affected path until repaired, repriced, or accepted by the owning authority." | SPEC_METHOD.md:648-657: "regression maps to evidence that is not new progress, and this member adds one need to it: the promotion block". F10 row (SPEC_METHOD.md:171-175 area) says "falsifies the claim of the path it affects, so it blocks further promotion only on that path". | conserved. The unblocking routes (repair, reprice, accept) are in the unchanged last paragraph of §3. |
| 606 UP-007 four conditions V | P:TICKET:748-755 "A finding blocks current promotion only when it falsifies that claim, ..." | TICKETS.md (hunk @@ -1045): "stated once at EVALUATION §5 ... adds no trigger". EVALUATION.md:281-298: "A finding can block current promotion only when it: 1. falsifies that claim; 2. ... 4. ...". | conserved. "only when" kept. Note UP-007 now has three owners (EVALUATION §3 what counts as independent, TICKETS §7 when required, EVALUATION §5 blocking); each sub-rule is stated once. |
| 610 Condition-Based Closure And Reuse V | P:TICKET:879-883 (quoted at M3) | ACTIVATION.md:486-491 | **meaning change, see M3.** The delta judged it conserved. |
| 517 Work result: `incomplete` pairing D | P:BASE:480 "`incomplete` accompanies `indeterminate`" | frontier PC:518 `superseded`, proposed and pending the product owner's acceptance, by ACTIVATION §3 Construction availability; ACTIVATION §3 maps `incomplete` to `falsified` for "a candidate is available" | meaning change, already marked proposed. Pass. Note ORACLE Q3 says the common requirement accepts no particular replacement; the cell now cites ACTIVATION §3 as replacement and the common requirement only as the reason. Pass. |
| Unchanged rows with an owner citation (ACT §2 constraint surface; EVALUATION §7 `conjoin`; 473 Reconstruction Litmus; PD §5 term identity; AC Latitude and ACT §6 capability) D, 473 V | P:SPEC (Reconstruction Litmus ends "Reconstruction sufficiency also depends on ambiguity governance") | SPEC_METHOD.md:336-342 now refers to EVALUATION §6 Layered sufficiency; EVALUATION.md:372-387 and table row at :431 hold "reuse ... grants no restart authority and does not excuse stale success ... new material counterexamples still challenge the relation" | conserved. The relocated sentences are present at the owner. |

### 3.2 I3-3a (EXECUTIVE_BASELINE)

| Row | Verdict | Note |
|---|---|---|
| 497 Canonical Compression D | conserved | Adopter now "Product authority" (PRODUCT_DEFINITION §7); P:BASE:114-116 already requires a Product-owned basis. |
| 498 Status And Authority Boundary D | conserved | UP-007 split between EVALUATION §3 and TICKETS UP-007, the second owner stated in the cell. |
| 499 Engagement Applicability D | conserved | "may finish as Writer" keeps "may"; this is the permission that M3 shows ACTIVATION §1 lost. The 499 row and the ACTIVATION §1 sentence therefore state the same permission with different force. |
| 511 Executive Drift Locks V (frontier PC:511-512) | parent conserved; child meaning change | Child PC:512 `superseded`, proposed and pending the product owner's acceptance, replacement FOUNDATIONS §4 Stale results. Pass. |
| 515 Technical Triage V | **meaning change, see M2**, not marked. |
| 516 Work Result D | conserved | Grounds moved to ACTIVATION §3; the two child rows PC:518, PC:525 cover the pairing. |
| 517 | see 3.1 | marked. |
| 520 Non-hierarchical configuration D | conserved | "not one hierarchy" kept; owner now RF-009. |
| 525 Derived Reviewer Frame D | conserved | Triggers and traceability to TICKETS UP-007. Matches P:BASE:674-676. |
| 526 Derived Generic Specialist Frame Set D | parent conserved; child `superseded` (PC:528), proposed and pending, replacement item 3 of the common requirement applied by FOUNDATIONS §4 Gaps | Pass. |
| 547 Executive Evaluates D | conserved | All seven sources kept. |
| 552 Executive Disposes D | conserved | First three sentences now by reference to EVALUATION §5 with the Executive as decision owner. |
| 553 | see 3.1 | conserved |
| 556 Missing-Frame And Re-Entry D | parent conserved; child `superseded` (PC:559), proposed and pending | Adds RF question 5 (new diagnostic obligation). Pass. |
| 558 Existing Authority Selects The Configuration D | conserved | Six bullets unchanged; ACTIVATION §1 holds the rule. |
| 562 Actor Binding And Independence V | conserved on trigger | P:BASE:1620-1622 "Where independent review is required, UP-007 controls". Candidate refers to TICKETS UP-007 and EVALUATION §3. But the candidate's freeze rule at EVALUATION.md:154 is unconditional while EB:504-507 and EB:1206-1208 keep P:BASE:507-509 "where ... qualification applies", so two loci decide the freeze differently (WC2-01). |
| 569 Closure D | conserved | Condition is TICKETS §7; "must" kept through TICKETS §7. |

### 3.3 I3-3b (DESIGN_MODULE), all D unless marked

| Row | Verdict | Note |
|---|---|---|
| 114, 116, 119, 122, 141, 143 | conserved | Added text names instances of ACTIVATION §7 or FOUNDATIONS §2. The 119 trigger "could materially alter the lawful frontier" is inside ACTIVATION §7's "could change the result's value". |
| 121 Authority model | conserved, with the wording difference stated in the delta | See the UP-004 note in section 1. |
| 157 Post-Ticket Design Review | conserved | (a) "adopts" becomes "applies this profile", which depends on row 162; if the product owner rejects 162, "adopts" returns. (b) and (c) keep the exceptions and the unconditional closure-claim block. |
| 162 Adoption Guidance | meaning change | PC:162 `superseded`, proposed and pending the product owner's acceptance, replacement PRODUCT_DEFINITION §7, rest of #15 unchanged. Pass. |
| 103, 104, 105, 117, 142, 145, 804 | conserved or unchanged | F17 trace only. |

### 3.4 I3-3c (ODD), all D

| Row | Verdict | Note |
|---|---|---|
| 253 11.5D | conserved | The new paragraph says a closure decision is "never recorded as" a disposition of ACTIVATION §3. The predecessor itself uses "disposition" for closure decisions (P ODD A8), and the candidate keeps that sense ("In §11.5D, §16 and §19 'disposition' names a closure decision"). Wording "never recorded as one" could read as a new prohibition; low. |
| 256 11.7A, 270 §20 | conserved | "Compression is prompt input, never the deciding authority" kept. |
| 223 §1 Position and the 12 re-read rows | conserved | Table and trace only. 805, 806, 804 stay unresolved. |

### 3.5 I3-3d (UX, WORLD_MODEL, PROFILES, plugins, templates)

| Row | Predecessor | Candidate | Verdict |
|---|---|---|---|
| 668 1A and 683 13 (S: PC:671, PC:686) V | P:UX_METHOD:22 "When a product, ticket, design module, or review adopts"; :339 "A project adopts `UX_METHOD.md` by:" | UX.md:74-78 "When Product authority adopts this profile ... recording the adoption in a product definition, ticket, design module or review"; UX.md:540 "Product authority adopts this profile for a project" | meaning change (narrows who may adopt); marked `superseded`, proposed and pending the product owner's acceptance. Pass. |
| 678 8A Msg-Replay D, V for text | P:UXM:493 | UX.md:440-446 adds a purpose paragraph | conserved, no obligation added. |
| 1A exits D, V | P:UXM:34 three exits, before implementation proceeds | UX.md:87-93 maps them to `resolved`, `escalated`, `carried`, with `blocked` until one is taken | conserved. |
| UX prompt carriage D, V | compression claim only | UX.md:401-406 "must carry the governing UX law the task needs, acquired as ACTIVATION §2 ... otherwise the deciding sections of this member" | no rc.2 body row; compression rows stay `unresolved`. The old sentence "rather than require the worker to rediscover it from the raw member" is dropped, and the fallback to the deciding sections is now allowed. That loosens a prohibition in a compression-only claim. Not a frontier meaning change; reported to the owner. |
| 715 Mappings Are Semantic Treatments V | P:WMM "Every treatment declares preserved structure, changed meaning, loss, surplus, and ambiguity." | WORLD_MODEL.md:539-546 keeps the sentence and adds the refinement relation | conserved. |
| WM translation lifecycle D | list unchanged, named as ACTIVATION §7 instances | conserved. |
| PROFILES §7 D, V | no frontier row | PROFILES.md:134-139 states the dispositions; TRAVERSAL cell says "25 conserved and 1 proposed superseded" | conserved. |
| 820 template V | P:TPL:154 | see M4 | possible loss. The "Executive appointment" to "coordinating appointment" rename is a neutral rename. Template hunk also adds "Under the executive profile" before "Executive assigns priority", which makes the Executive text conditional on adopting that profile. That is a scope narrowing of template text to the executive configuration; the template is a slot and the delta says so. |
| 821 templates/README D | conserved | Pointer corrected from section 6 to 5. |
| Plugins D, V (GETTING_STARTED, stdo-work) | see section 1 | | Plugin text has no frontier row; two changes in permitted work noted above. |

### 3.6 I3-3f (SPEC_METHOD, TICKETS, WRITING_GUIDE, ADR templates)

| Row | Predecessor | Candidate | Verdict |
|---|---|---|---|
| 602 Upward Propagation Check V | P:TICKET:614 "If the governing requirement is actually missing or insufficient, re-enter its owner" | TICKETS.md:506-508 "checks each layer and stops at the highest layer found missing or insufficient" | conserved (delta explains the previous prose picked the lowest). |
| 437 Computed Classification D | conserved | SPEC_METHOD.md:847-851 "grant no authority, an instance of FOUNDATIONS §2". |
| SPEC_METHOD §9 closure evidence V | no rc.2 body row | SPEC_METHOD.md:1641-1645 "this section adds no second closure condition" | conserved. |
| UP-006 milestones D | "Ticket completion requires every closure-bearing milestone to be accepted" | TICKETS.md:116-119 adds that each milestone is a work claim under §7 | conserved; the added sentence restates the owner. |
| 582 Comments V | "not task status authority" | TICKETS.md:73-79 | conserved. |
| 488 ADR Conventions V | rules stated only in `templates/.../adrs/README_TEMPLATE.md` | SPEC_METHOD.md:1666-1677 "ADRs are append-only history ... a superseded ADR is deleted only when it is explicitly retired ... the ADR moves to that tenant's design surface" with its purpose | conserved; relocation from a template to the method owner. This raises the force from template text to method law for all tenants. The purpose is stated, so N11 is met; note scope widening is by relocation. |
| SPEC_METHOD §6 version labels V | P:SPEC §6 | SPEC_METHOD.md:1196-1200 "likewise describe current truth by role, boundary and status" | conserved, "should" kept. |
| 794 Current-Surface Writing (S: PC:797) V | P:WRITING_GUIDE:112 "Active specification should describe the current constitutional surface in present tense." | WRITING_GUIDE.md:114-122 "constitutional specification is written in the present tense, material that is no longer live is deleted, superseded or moved to commentary, and an explicit version label is reserved for ..." | meaning change ("should" to the owner's mandatory force; adds "superseded material"); marked `superseded`, proposed and pending the product owner's acceptance. Pass. |
| 792 D | "remove stale law, as §9 states" | conserved. |

### 3.7 I3-3g (TRAVERSAL_OCCURRENCE), I3-3h (PRODUCT_DEFINITION, RELEASE, ASSURANCE), I3-3j, I3-3k

| Row | Verdict | Note |
|---|---|---|
| 641 Closed kinds V | conserved | TRAVERSAL_OCCURRENCE.md:761-770 adds that the value set "refines AC-007 by excluding `out_of_frame`" with the reason; the value set is unchanged. `partial_effect(not_attained)` and `(undecided)` are not in P:TOP (it only has `partial_effect`, P:TOP:143, :725); they are candidate-new refinements, so the "every other" clause is not a predecessor-claim change. |
| 654 Authority And Adoption V | conserved | TRAVERSAL_OCCURRENCE.md:1428-1432 "Only Product authority adopts the profile, as PRODUCT_DEFINITION §7 states for every available profile". P:TOP:1044 "A Product adoption declares at least" already names Product; P:SPEC:748 states the general rule. |
| 400 Acceptance Criteria V | see M5 |
| 394 Naming V | conserved | RELEASE.md:465-469; the "merely to signal recency" prohibition is carried by SPEC_METHOD §2 (diff shows "never recency"). |
| 527 Testing Frame Set D | conserved | ASSURANCE.md:320-324 names instances. |
| PRODUCT_DEFINITION §11 digest V | conserved | PRODUCT_DEFINITION.md:899-901 refers to EVALUATION §7 where "digest integrity ... establish identity and structure, not semantic fidelity" is stated (EVALUATION table row at :437). |
| 204 UP-004 V | conserved | see note in section 1. |
| 617 proxy rows V | conserved | EVALUATION.md:265-268 refers to FOUNDATIONS §2's proxy limit. |
| 351 Coverage Basis V | **meaning change, see M1**. |
| RF Communication D | conserved | "grants no authority" cites FOUNDATIONS §2. |
| IDENTITY §2 (new tier-1 law) V | no predecessor row | IDENTITY.md:128-150 with purpose stated; WORLD_MODEL §4 refines. Pass. |
| I3-3k CONFORMANCE D | no predecessor member | R1: an unrunnable case "is a planned evaluation that was not performed". Consistent with FOUNDATIONS "not performed". Not assessed further. |

### 3.8 F1-F5 "Frontier rows touched by revision 2b"

| Row | Verdict |
|---|---|
| 175 Traversal Index D | conserved, locus text only. |
| 364 Revision Actions V | conserved (3.1). |
| 423 Explicit Complete Consumer Update D | conserved; effect values `completed` and `not_effected` per I3-2c; I did not re-read. |
| 427 WHAT/HOW/Work carriers, 431 Constitutional Chain D | conserved; not re-read. |
| 437 V | conserved. |
| 547 D | conserved (3.2). |
| 641 V | conserved (3.7). |
| 649 OP-003 Correction Without Erasure D | conserved; not re-read at S. |
| Possibly affected: 441, 447, 49, 294, 295, 393, 422, 435, 499, 520, 542, 634, 818, 382, 554 | Not assessed (no text read). Rows 499 and 520 are covered in 3.2. |

## 4. Not assessed, or only judged from the delta

- Rows marked D above were not re-read at S.
- Not assessed: the 13 possibly-affected rows of F1-F5 listed in 3.8 other than 499 and 520; ODD §4 / RELEASE §4 (reported by I3-3c as unlisted); the I3-3k mapping of the 52 discriminators (no predecessor rows, not compared with the common table at `355aa86`); the I3-2a, I3-2b and I3-2c deltas (outside the list).
- Number of rows: about 75 distinct rows or groups appear in the deltas and F1-F5. About 30 were verified against both texts (V). The rest are D.
