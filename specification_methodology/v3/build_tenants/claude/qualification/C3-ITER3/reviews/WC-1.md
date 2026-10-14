# WC-1: Working Check Of Iteration 3 Step 1

**Same-family working check, not acceptance.** This is a Reviewer
activation, WC-1, run in a Claude-family context that wrote none of the
subject. It supports `local_repair`, `re_enter` or `reject` and never
`accept` ([PLAN §3](../PLAN.md#3-conventions-for-every-activation)). It
repairs nothing and changes no git state.

## 1. Subject, basis and limits

| Coordinate | Value |
|---|---|
| Subject | commit `13676de`, read with `git show`. The working tree's HEAD had moved to `2d3838f`, and step 2 edits were in progress; neither was read |
| Previous | `1214524` |
| Subject files | returns I3-2a, I3-2b, I3-2c, I3-2e; deltas I3-2a, I3-2b, I3-2c; FOUNDATIONS, ACTIVATION, EVALUATION, REFERENCE_FRAME, AXIOMATIC_CALCULUS, IDENTITY, SPEC_METHOD, TICKETS, ASSURANCE, PRODUCT_DEFINITION; `design/REDUCTION.md`, `design/DOCUMENT_STRUCTURE.md` |
| Sources read first | ORACLE (all of it; groups a, b, d, e and f, plus N, used); PLAN §3 and the step 1 rows; REDUCTION §2–§3 at `1214524` (before I3-2e changed it); the common requirements README at `13676de`, SHA-256 `b04dad3b…c79fc8`, equal to the oracle basis; F1-F5 Summary, F1 and F2 (unchanged by the subject) |
| Predecessor | installed `v2.5.1-rc.2` standards, read by targeted line ranges: BASE 1420–1441; TICKET 284 and 310–336, 596–626, 736–738; UX grep hits for "close review" and "classif" (426–537); SPEC 1169, 1319, 2565–2600, 2650–2685; RF 428–436, 637; AC 452–460; IDENTITY 218–226 |
| Time | start not recorded. In order: the sources were read, the expectations file was written (§2), and only then were the subject returns and deltas opened. The first `date -u` (17:29:28Z) came after the returns and deltas had been read. The file was first written by 17:40:31Z and corrected after a review of the draft, 2026-10-14 |
| Bytes | supplied: about 4 KB of intake. Cumulative acquired with repeats: about 380 KB ±20%, an estimate from file sizes and the excerpts read. That is over the 300,000-byte default of PLAN §3, and the activation did not stop. Active retained: not measured. Spend: `unavailable` |
| Mechanical checks | the scripts are in session scratch, not committed. 726 relative links and anchors across the ten members and two design files resolve, with one false positive inside a code block (`AXIOMATIC_CALCULUS.md:931`). Family-table column counts are uniform per table. The index Pillar cells of F2–F5 equal the union of their rows' cells |

Coverage limits: the sampling is stated per question. Predecessor
meaning was compared directly where the table in Q3 says "read";
elsewhere the delta's predecessor quote was used, and those quotes
matched in the five places they were checked (rows 78, 204/306, 437,
342, 434).

## 2. Expectations, recorded before opening the subject

This is the pre-opening record, copied verbatim from the scratch file
written before any subject file was read. Its line numbers are those of
the text at `1214524`.

```text
Expectations recorded before opening the subject (13676de member text, returns, deltas). Sources: ORACLE a,b,d,e,f + N; PLAN §3, step 1 rows; REDUCTION §2-§3 at 1214524; RQ at 13676de (sha b04dad3b..., equals oracle basis); F1-F5 §F1-F2 (unchanged by subject).

X1 (Q1; D1, D5, RQ-SO 3,7; B4) Each touched cluster: owner locus states the determination once; every rival in these members either refers (names the owner, decides nothing of its own) or refines (names owner, maps each value/case to owner's, adds only domain instances). F: rival keeps its own list; precedence instead of owner; bare "see X" where a map is owed (D7).
X2 (Q1; B12, J9, RQ-FR 3) A rival turned into a reference keeps its trigger, force, exceptions; no circular referral (A->B->A, e.g. SPEC_METHOD/TICKETS closure condition). F: lost trigger; responsibility sent back to consumer.
X3 (Q1) Per-cluster REDUCTION §3 actions expected in these members:
  R2 FOUNDATIONS §4 states both stale predicates; RF:277 refers; EVALUATION:454 maps veto outcomes.
  R6 RF remedy list and budget refer to ACTIVATION §2; AC:646 refers for trimming; ACTIVATION §2 binds successor RF sections, rc.2 links provenance only.
  R7 SPEC_METHOD:902-905, :932, TICKETS:1065-1070, :1142 refer to ACTIVATION §7; domain triggers as instances of material-input change; EVALUATION:101 mandatory.
  R8 RF §10 and ACTIVATION §7 one trigger term.
  R9 EVALUATION:297, SPEC_METHOD:340 references.
  R10 ACTIVATION §1 states an exclusion is no result; disjunctive-predicate rule; consumers (SPEC_METHOD:609, RF:699) consistent; lifecycle three-state rule has one owner.
  R11 TICKETS keeps triggers as Spec Method policy (UP-007), names EVALUATION §3; author identity at EVALUATION §3; SPEC_METHOD §11 refers.
  R12 one list at FOUNDATIONS Authority kinds; RF-006, AC:481, IDENTITY:194, PD:77 cite it adding domain instances; proxy limit owned there; EVALUATION/IDENTITY/ACTIVATION refer; recording-without-review owner ACTIVATION §1, TICKETS refers.
  R13 SPEC_METHOD:1466 states predicate and relation to RELEASE §9; ACTIVATION:1322, ASSURANCE:1096 use the four values (split rows).
  R14 TICKETS states how close classifications return through dispositions; TICKETS owns closure condition; SPEC_METHOD:924 refers (no cycle).
  R16 one relation-structure list at ACTIVATION §1; RF-009, RF:980 cite it and name profile additions; configuration admission at ACTIVATION §1.
  R17 TICKETS:481 applies or refines SPEC_METHOD §4.
  R18 ACTIVATION:849 refers to SPEC_METHOD §5.
  R19 FOUNDATIONS:51 spelling list; AC:459, PD:484 cite; AC-002 -> IDENTITY §2; AC-006 -> RF-005.
  R20 EVALUATION:278 maps to formal-fragment items.
  R21 FOUNDATIONS:268 binding field list; AC:1243, PD:571 refine; FOUNDATIONS:851 names a tier-1 owner.
  R22 EVALUATION §2 owner; RF-007, AC-018 refer keeping domain binding.
  R23 ACTIVATION §2 "### Staleness of derived surfaces" owns generic rule; PD §11 refines for packaging.
  R25 EVALUATION §5 "### When a finding blocks promotion" owns; TICKETS:1019 refers keeping domain triggers.
  R26 SPEC_METHOD:627 refinement of ACTIVATION §5.
  R29 RF translation, SPEC_METHOD:1757-1764 refer to ACTIVATION §4/AC-013 with domain fields only.
  R1 EVALUATION:352 unrunnable case = planned evaluation with no result.
  disc. b: ACTIVATION §6 owns resource-limit law; SPEC_METHOD §11 binds it.
  Pillar 10: AC §9 "### Constraint surfaces"; ACTIVATION §2 acquisition consumes it.
X4 (Q2; A0, B1, Q11) Family-table format and index gain Pillar column citing PD-FR rows 1-10; Pillar column binds contributions, does not claim derivation from pillars or pillar-as-axiom; no column filled indiscriminately. Touched family rows: premises with standing force the consequence, or a named policy with an owner. F: hollow row (choice filed as consequence); policy with no owner; S/T/D/O still called "pillar".
X5 (Q3; H3, H6, Q10, B12, N9, PLAN §3) Every changed conserved/superseded row re-assessed in the delta against the predecessor (scope, modal force, triggers, exceptions). Meaning-preserving relocation stays conserved. Any changed scope/force/trigger/exception -> proposed superseded with replacement relation, marked proposed (H4). F: conserved row whose locus now has a new obligation, lost trigger, changed modal force, or narrowed/widened scope. F: proposed shown as accepted (N2).
X6 (Q4; D8, E5, F2 record) PD restoration rule: unverified restoration must not become not_effected; but if non-attainment of the intended outcome is established, the result must not be masked as merely uncertain (F2 pattern); ACTIVATION §3 owner's values and end-as-residual applied. R25: EVALUATION §5 states the blocking rule once, distinguishes assessment from authority to act (D10), maps to core or states purpose; rivals keep domain triggers; no predecessor meaning change without proposed supersession.
X7 (Q5; B10, D1, J53) Links between step 1 members resolve to existing anchors; fixed-interface headings (PLAN §3) exist with exact names; no two members decide one question differently; design (REDUCTION/DOCUMENT_STRUCTURE) and members agree on owners (R16).
X8 (Q6; WRITING_GUIDE; N7, N11) Terms introduced at first use or defined at an owner; role names not personal names; no new obligation without purpose (CF r41); modal force changes deliberate and recorded; no Executive/Writer/Reviewer role inventory as law.
X9 (scope; N5, PLAN step 1) Each activation writes only its territory; R4/PD:416-418 was assigned to I3-3h, so a step 1 edit there is out-of-plan though in I3-2c territory.
```

Readings made after opening, kept apart from the record above:

- **X6.** Its two clauses conflict for a caught failure whose restoration is not verified. The first clause forbids `not_effected`. The second requires an established non-attainment to show as `not_effected`. The owner resolves this (ACTIVATION §3 Effects: "The end never decides a `not_effected` value"), and Q4 applies the owner's rule. The first clause is read as forbidding `not_effected` where non-attainment is not established, and that is how the repair reads.
- **Decider.** WC1-11 rests on ORACLE Q10, which was read before opening: "any change of scope, force, trigger, exception or permitted work is a supersession". Who may classify is permitted work. X5 does not cover it.

## 3. Results

### Q1. One owner per cluster; rivals refer or refine

**Result: partly met.** 21 clusters were sampled across the four
activations.

- Six keep a live second decider or a cross-member contradiction: R2 veto, R8, R9, R12 recording, R25 and R26 (WC1-08, -01, -09, -06, -05, -04).
- Three are partly done: R13, R19 and pillar 10.
- One refines with an internal ordering defect: R17 (WC1-12).
- Eleven are clean: R6, R7, R10, R11, R14, R16, R18, R22, R23, R29 and R30.

| Cluster | Owner (quote, `13676de`) | Rival (quote) | Verdict |
|---|---|---|---|
| R2 stale | FOUNDATIONS:960 "Stale results … an evaluation performed on a … stale … basis … returns `invalid_basis` … a component whose only held result is stale … is … a gap" | RF-005 "A stale … basis returns `invalid_basis` or requires reactivation" | refers, consistent; the owner cites RF-005 as the frame instance |
| R2 veto | RF §5 `conjoin` outcomes `decision(holds|fails)`, `conflict`, `indeterminate` | EVALUATION:538 "a declared veto return conflict, indeterminate or refusal" | **still deciding** (WC1-08) |
| R6 | ACTIVATION §2 step 3 owns the remedies | RF-014:377 "the remedies are those of ACTIVATION §2 step 3, which owns the list" | refers; the four predecessor remedies are named |
| R7 | ACTIVATION §7 "The invalidators are three" | SPEC_METHOD:935 "material inputs of C … by name"; TICKETS:1089, :1173; EVALUATION:109 "where it does, the invalidation is mandatory" | refine as instances; no trigger lost |
| R8 | ACTIVATION §7 "a declared revising observation: an observation that the result … itself names"; evidence sits under "a material input change … when it could change the result's value" | RF §10:907 "newly acquired admissible evidence that bears on a closed result, an instance of the revising observation of ACTIVATION §7" | **contradiction** (WC1-01) |
| R9 | ACTIVATION §5 | EVALUATION:381 and SPEC_METHOD:342, near-identical "grants no restart authority" paragraphs | **duplicate remains** (WC1-09) |
| R10 | ACTIVATION §1 "An exclusion … is no result … A predicate that its owner declares as a disjunction … `satisfied` … for the declared disjunction only" | RF coverage `excluded_by_authority` → `satisfied`, for a predicate ending "or a governing authority the row cites excludes it"; SPEC_METHOD:619 owns the three lifecycle answers; ASSURANCE:1040 applies them | consistent; RF uses the disjunctive form without citing the owner (minor) |
| R11 | EVALUATION §3 owns author identity (:165) and what counts as independent | TICKETS:1016 "What counts as independent … are EVALUATION §3"; SPEC_METHOD:1708 refers | refers; see WC1-10 on where the trigger owner is named |
| R12 list | FOUNDATIONS §2 "What creates no authority" (nine bullets) | RF-006, AC-005, IDENTITY §6 "That list is FOUNDATIONS §2 Authority kinds'; its instances … include …" | refers with domain instances; the wording differs from IDENTITY (WC1-13) |
| R12 recording | ACTIVATION §1:480 "Carriers and profiles refer to this paragraph" | TICKETS:1165 "the authorised constructor may record the satisfied bounded result … without adding a ticket, a coordinating appointment, a review or a recreated design view" | **duplicate remains** (WC1-06) |
| R13 | RELEASE §9 | SPEC_METHOD:523 states the predicate and denies substitution; ASSURANCE:1099 uses a four-value cell; ACTIVATION:1523 "superseded in its mapping" | partly done (WC1-16) |
| R14 | TICKETS §7:1159 "This section owns the closure condition" | SPEC_METHOD §4:962 "closes only under the closure condition that TICKETS §7 … owns" | refers, with no cycle |
| R16 | RF-009 "Functional decomposition, communication, authority precedence, frame configuration, subject topology and evaluation dependency are distinct" | ACTIVATION §1 "RF-009 owns that list … this section adds no structure to it and drops none"; RF §12 item 3 cites RF-009 | consistent; I3-2e's discrepancy c settles it (Q5) |
| R17 | SPEC_METHOD §4 | TICKETS:491 "The re-entry rule is SPEC_METHOD §4's … this check refines that rule into an upward walk" | refines with a map; one ordering defect (WC1-12) |
| R18 | SPEC_METHOD §5 | ACTIVATION §4 "for this method the owner of the default policy is SPEC_METHOD §5 … and this section states none" | refers |
| R19 | IDENTITY §2; FOUNDATIONS §2 Representation | AC-002:459 maps its coordinates to IDENTITY §2 and keeps its spelling list as an "`a_c` binding"; PRODUCT_DEFINITION:497 keeps a different list | partly done (WC1-15) |
| R22 | EVALUATION §2 "owns the separations" | RF-007 "is EVALUATION §2's. This law binds it to a frame"; AC-018 "are EVALUATION §2's … This law binds them to `a_c`" | refers with a domain binding |
| R23 | ACTIVATION §2 "Staleness of derived surfaces … owns when a derived surface … is stale, for any method and any carrier" | PRODUCT_DEFINITION §11 "This member refines that law for the derived surfaces a released cut or an installation carries" | refines; the restated digest sentence is minor (WC1-14) |
| R25 | EVALUATION §5 "This section is the one statement of when a finding can block" | TICKETS:1046 "A finding blocks current promotion only when it falsifies that claim; exposes …" (all four conditions) | **two deciders** (WC1-05) |
| R26 | ACTIVATION §5 "a category it cannot map is a change to this owner, not a parallel category" | SPEC_METHOD §3 "Regression is this member's added category, which ACTIVATION §5 does not name" | **contradiction** (WC1-04) |
| R29 | ACTIVATION §4 Refinement; AC-013 | RF translation "This section adds only the frame fields"; SPEC_METHOD §11 rule 7 "The binding adds only which accounts the mapping joins" | refers |
| R30 / disc. b | ACTIVATION §6 Resource limits "owns the law for every such limit. It sets no value" | SPEC_METHOD:1768 "this rule binds it"; EVALUATION:496 "under the resource-limit law of ACTIVATION §6" | refers; the tier-1 dependency on tier 2 is removed |
| Pillar 10 | AXIOMATIC_CALCULUS §9 Constraint surfaces | ACTIVATION §2 holds no consumer | owner without consumer (WC1-07) |

The fixed-interface headings exist with their exact text: ACTIVATION:689,
EVALUATION:281, AXIOMATIC_CALCULUS:1271, FOUNDATIONS:116, and the Pillar
column at FOUNDATIONS:541. ACTIVATION §2 cites no rc.2 link for a
successor rule. The links that remain are labelled provenance, at :519,
:528 and :674.

### Q2. Family arguments and the Pillar column

**Result: met for the rows step 1 touched. B1 stays open for F1 and F6
to F21, which is planned for step 2.**

- **Format** (FOUNDATIONS:541–581). The Pillar column is "a trace … not a premise, adds no standing … does not claim that a pillar is an axiom or follows from finite capacity". That respects ORACLE Q11 and A0. The ten contributions are named in PD-FR order, and the Product is named as their owner.
- **Index.** F2–F5 are filled, and each cell equals the union of its table's rows. F1 and F6–F21 read `pending` under a declared rule ("A Pillar cell marked pending names no pillar"). Tables F6–F15 in these members still have four columns. That is consistent with the pending rule, but they do not yet meet the five-column format. I3-2a reports that no activation is assigned to fill the index cells after step 2.
- **Rows sampled** (11): ACTIVATION F2 (Applicability; Recording a result without review; Configuration), F5 (Resource limits; Cost is selected), FOUNDATIONS F3 Stale results (:910), EVALUATION F6 :73, :78, :84, F7 :436, AXIOMATIC_CALCULUS F9 :182, SPEC_METHOD F10 :179. Each states premises with their standing, gives a consequence those premises force, and leaves choices with named owners. None is hollow. The Pillar cells are selective and plausible, for example Resource limits "8, 7" and Refinement "3, 4".
- **One placement tension** in F6 :84 and §3 (WC1-10). UP-007's four blocking conditions are filed as a choice of a tier-1 section ("this section, conserving UP-007"), while UP-007's trigger boundaries are filed as Spec Method policy at TICKETS.
- **Rename.** S/T/D/O is now "four named areas", defined where it is written (SPEC_METHOD:93–101, TICKETS:15). `GLOSSARY.md:82` is left for I3-3e.

### Q3. Changed `conserved` or `superseded` rows

**Result: three meaning changes are recorded as `conserved` (rows 553,
481 and 593), and one row's prose conflicts with its table (602).**

| Row | Predecessor | Judgement | Basis |
|---|---|---|---|
| 553 BASE Executive promotion projection | read | **meaning change** (scope) | WC1-02 |
| 423 PD complete consumer update | delta quote; owner read | conserved; the repair is correct | Q4 |
| 481 SPEC fundamental migration | read | **meaning change for requirements** | WC1-03 |
| 593 TICKET sprint close review | read (TICKET 284, 310–336; UX 493, 537) | **meaning change** (classifier) | WC1-11 |
| 602 TICKET upward propagation | read | conserved by the table; the prose conflicts | WC1-12 |
| 606 TICKET UP-007 | read (:736–738) | conserved. "A governing basis may add boundaries" falls within "explicitly risk-bearing boundaries that claim it". I3-2c deferred this sentence to I3-2b's delta, which never assesses it: a coverage gap in the deltas, not a meaning change | — |
| 364 RF revision actions | delta quote | the dependency I3-2b states is unmet: the owner files evidence under the material-input invalidator with a materiality test, not under the revising observation | WC1-01 |
| 204 UP-004, 321 RF-006 | read (IDENTITY 218–226) | conserved; their dependencies are met. FOUNDATIONS lists payload shape, evidence shape, reachability and frame selection, and both proxy limits | — |
| 306 RF #authority | read (UP-004) | conserved. The bullet now reads "never widen" where the predecessor read "must not silently widen". With "Elevation … require an explicit authority decision", the net meaning is equal, but IDENTITY keeps "silently" | WC1-13 |
| 78 AC-011 | read (:456) | conserved. The material closure holds every required member, so dropping "silently" changes nothing | — |
| 329 RF-014 | read (:428–436) | conserved; the four remedies, human selection and the prohibition are kept | — |
| 463 UP-008 | delta quote | conserved. The "can" of possibility is kept; mandatory force comes from the owner | — |
| 558 BASE configuration admission | delta quote | conserved; "project" is dropped for tier 1, and the per-layer list stays in EB | — |
| 437 SPEC computed classification | read (:1319) | conserved. Every trigger is named, and the added revising observation was already predecessor law (RF :637) | — |
| 610 TICKET closure | delta quote; text read | conserved. The condition is verbatim, and the added J-observation trigger is the member's own (TICKET 788) | — |
| 339 RF applicability | delta quote; text read | conserved. "Unresolved, not false" and "excludes only that obligation" are kept. Exclusion as no result is new law, with its purpose stated | — |
| 434 SPEC lifecycle | read (:1169) | conserved; "answered" is named | — |
| 342 RF return a closed result | read (:637) | conserved. "Material" scopes the evidence case | — |

### Q4. The F2 repair and the R25 owner

**F2 repair (PRODUCT_DEFINITION:411–432): correct.**

- The owner (ACTIVATION §3 Effects) decides `not_effected` from evidence that the outcome is not attained and cannot be. The end "never decides a `not_effected` value", and an effect of uncertain completion is "`completion_unknown`, or … `not_effected` with its end not established".
- The repair applies exactly that. A caught failure is `not_effected`. Restoration verification decides only the end. Host loss without a caught failure is `completion_unknown`. Both kinds are reconciled before repetition.
- The phrase "uncertain completion" is the owner's own term, not a redefinition.
- The premise "the operation applies no later part of it" comes from the operation's contract: the predecessor's "restores the affected consumer preimages and does not report completion". It is not a new assumption.
- No predecessor obligation is lost: completion is not reported, and recovery from the preimages precedes the claim.
- Process note: PLAN assigned R4 to I3-3h. I3-2c's edit sits inside its own territory but outside its row (WC1-18).

**R25 owner (EVALUATION §5): placed, but with defects.**

- The section exists. It states the four conditions as necessary, and its table covers every case. It keeps severity, priority and blocking apart, and it states its purpose.
- Defects:
  - TICKETS still decides the same question (WC1-05).
  - Writing the Executive projection for every decision owner changes the bound party, and it brings in "current mandate", which no tier-1 or tier-2 member defines (WC1-02).
  - The tier-1 filing of UP-007's conditions conflicts with the Spec-Method filing of UP-007's triggers (WC1-10).

### Q5. Cross-member consistency

- **Links.** All resolve (§1).
- **R16.** Consistent at `13676de`. I3-2a followed D3, with RF-009 as owner. I3-2e then corrected REDUCTION's R16 action (discrepancy c) and recorded D9 as "ACTIVATION §1 Configuration (allocation, admission of a configuration, direct entry); RF-009 (the list of distinct relation structures)". RF-009's six structures include the four of RQ-BT 4. RF §12 item 3 is a violation instance that cites RF-009, not a rival list. Residue: REDUCTION's summary row (`design/REDUCTION.md:1340`) still names only "ACTIVATION §1" as the R16 owner. Low; I3-2e's territory.
- **Contradictions found between step 1 members:** WC1-01 (RF §10 against ACTIVATION §7) and WC1-04 (SPEC_METHOD §3 against ACTIVATION §5).
- **Second deciders inside step 1 members:** WC1-05, -06, -08 and -09.
- **One-sided reference:** WC1-07. AXIOMATIC_CALCULUS §9 condition 3 names ACTIVATION §2 as "where a step uses a surface", and ACTIVATION is silent.
- **I3-2e exit proof: holds.**
  - `git diff -U0 1214524 13676de -- design/REDUCTION.md` removes lines only at old :6, :57–58, :82, :91 (§1), :707 (the R16 action), :907 (the R25 action) and :1265 (§6). Nothing in §4.1–§4.6 (old :996–1240) is removed or changed; §4.7 is inserted after :1240.
  - R30 to R34 each have an owner, an action with an activation, and a path (DP-41 to DP-46, REDUCTION :1632–1637).
- **Oracle F2 on the R11 move: holds.** Author identity moved to EVALUATION §3 (:165), which keeps author apart from actor. Operation kind and the three-way distinction stay at SPEC_METHOD §11: "Author identity, actor identity and operation kind stay distinct, and none determines another" (:1715, :1737–1738). So does the rule on human adjudication (:1743–1744, citing §5).
- **Consistent pairs checked:** R2 stale; R10 against RF coverage; R14; R18; R22; R23; R29; R30 against SPEC_METHOD §11 and EVALUATION §7; D1's five ACTIVATION §3 refinements against ACTIVATION's own table.

### Q6. Writing

- **Undefined term:** "current mandate" at EVALUATION:307, the only use in tiers 1 and 2. It is an Executive-profile term, which DOCUMENT_STRUCTURE forbids in tier 1 or 2 ("no profile term appears in tier 1 or 2 outside a disposition note").
- **Body text that defers its owner to a trace:** EVALUATION §3 "a policy choice, whose owner the family table of §1 names". FOUNDATIONS §3 says a family table "state[s] no determination that the rule it names does not state" (WC1-10).
- **Modal wording:** FOUNDATIONS "never widen" against IDENTITY "do not silently widen" (WC1-13). The other modal changes are deliberate and recorded: EVALUATION:109 "can" plus the owner's mandatory force; EVALUATION §5's "These conditions are necessary".
- **Naming:** none. No tenant, model, iteration or activation names appear in the added member text. Roles are stated as roles. Every new law carries a purpose and material relation.

## 4. Findings

Class R is a return defect: the activation caused or overclaimed it. Class
C is a composed-state gap: an item outside the activation's PLAN row,
usually a REDUCTION §3 action the PLAN row omitted. Class P is a process
note.

| ID | Sev. | Class | Finding | Smallest repair | Territory |
|---|---|---|---|---|---|
| WC1-01 | Medium | R (I3-2b) | RF §10:907–909 calls admissible evidence "an instance of the revising observation of ACTIVATION §7". The owner defines the revising observation as one "the result … itself names", and files evidence under "a material input change … when it could change the result's value". The kind is wrong, and RF keeps a broader test ("bears on"). Row 364's dependency is unmet, so the F1 seam is open again | Rewrite RF §10 as "newly acquired admissible evidence that is material to a closed result, a material input change under ACTIVATION §7, reopens …". If the owner reads "bears on" as intended (MT-2, MT-9), raise it as an ACTIVATION §7 change instead. Update delta row 364 | REFERENCE_FRAME |
| WC1-02 | Medium | R (I3-2b) | Row 553 is recorded `conserved`. EVALUATION §5's table now binds every decision owner in tier 1 to decide blocking "from the exact affected claim, the current mandate, the applicable hard stops and the Product-owned cutoff policy"; the predecessor bound the Executive only. That is a changed bound party (Q10, H6), and "current mandate" is undefined there | Either keep row 553 at EB, state the tier-1 table as new law with its purpose (drop "conserves … the Executive projection with the Executive written as the decision owner"), and replace "current mandate" with a tier-1 term; or propose `superseded` for row 553 with I3-2b's own replacement relation, pending the product owner | EVALUATION; delta I3-2b |
| WC1-03 | Medium | R (I3-2c) | Row 481 is recorded `conserved`. "For a requirement the two are one classification: … deferred … [is] Deferred, with that table's meanings" makes a migration-deferred requirement "retained in the live surface as an explicit not-yet-operative … obligation". The predecessor's migration rule says "absence from the new constitutional surface means 'not yet adopted' and carries no automatic authority", and "nothing carries forward by default". A requirement whose adoption is deferred now becomes a live obligation, which changes its standing. "Adopted is Active" also narrows adoption to operative requirements, although the lifecycle axis lets a live requirement be "explicitly deferred". This is the Writer's own check point, and it resolves to a change | State the relation, not an identity: the migration class records the adoption decision, and the legacy class records live-surface standing; adopted pairs with Active or Deferred; migration-deferred is not live. Or propose `superseded` for row 481, requirements only | SPEC_METHOD §7 |
| WC1-04 | Medium | R (I3-2c) | R26 contradiction. SPEC_METHOD §3 makes "Regression … this member's added category, which ACTIVATION §5 does not name". ACTIVATION §5, at the same commit, maps each finer category to one of five, and "a category it cannot map is a change to this owner, not a parallel category". I3-2a's delta had asked for the map | Map regression to "evidence that is not new progress" (the text already says it "projects no progress") and keep its promotion-block need. Or raise an ACTIVATION §5 owner change | SPEC_METHOD §3 |
| WC1-05 | Medium | C | R25. TICKETS:1045–1052 still states UP-007's four conditions and the outside-observation rule in full, beside EVALUATION §5's "one statement". Two deciders (D1, J46). REDUCTION named I3-2c; its PLAN row did not | TICKETS refers to EVALUATION §5 and keeps only its carrier binding (no new ticket or review round) | TICKETS (I3-3f) |
| WC1-06 | Low–Med | C | R12. TICKETS:1165–1170 restates ACTIVATION §1 "Recording a result without review" almost word for word, although the owner says "Carriers and profiles refer to this paragraph" | Refer; keep "including sprint-close law (§3) and the design profile's law" as the carrier binding | TICKETS (I3-3f) |
| WC1-07 | Low–Med | C | Pillar 10. AXIOMATIC_CALCULUS §9 condition 3 names the acquisition step of ACTIVATION §2 as where a surface is used, and ACTIVATION is silent, so A10 stays partial. REDUCTION §2 repair 3 named I3-2a; the PLAN row did not | One sentence in ACTIVATION §2 Acquisition naming AXIOMATIC_CALCULUS §9 Constraint surfaces as the route where a current interpretation exists | ACTIVATION (body; needs an assignment) |
| WC1-08 | Low | C | R2. EVALUATION:538 (`conjoin` qualification row) uses "conflict, indeterminate or refusal" and "declared veto". RF §5's `conjoin` has no `refusal`, a basis mismatch is held as `invalid_basis` (FOUNDATIONS Stale results), and "veto" is undefined. REDUCTION cites it as :454 | Name the RF §5 outcomes and the stale-results case | EVALUATION (I3-3j) |
| WC1-09 | Low | C | R9. EVALUATION:377–384 and SPEC_METHOD:338–345 restate the same reconstructability paragraph, including "grants no restart authority" | Choose one owner; the other refers | EVALUATION or SPEC_METHOD |
| WC1-10 | Low | R (I3-2b) | EVALUATION §3 leaves the owner of the trigger policy to the family table, which FOUNDATIONS §3 makes a trace that states no determination. Separately, F6 :84 files UP-007's four blocking conditions as a tier-1 choice, while R11 files UP-007's triggers as Spec Method policy (D2) | Name the owner in the §3 body, and decide in DOCUMENT_STRUCTURE D9 whether the four conditions are tier-1 consequences or Spec Method policy | EVALUATION; design |
| WC1-11 | Medium | R (I3-2c) | Row 593 is recorded `conserved`. The predecessor gives classification to the close review: "the close review must classify and pay down the debt" (TICKET 284), and "close review must classify" (UX 493, 537). The candidate makes each classification a disposition under "the law of that section … unchanged", so ACTIVATION §3's decision owner classifies, and "an assessor's proposed classification is a recommendation, not the classification". That moves the act from the review to the decision owner unless the close review is the decision owner's own act, which neither text states. The delta's premise, "the predecessor names no decider for the classification", is wrong. Separately, `remove` → `reject`, "wider than `reject`'s", creates a homonym (R27) | Keep classification with the close review under the sprint authority, and use ACTIVATION §3 only for the core-value map. Or propose `superseded` for the classifier change. Map `remove` to its core value without calling it `reject` | TICKETS §3 |
| WC1-12 | Low | R (I3-2c) | Row 602. The prose's "an upward walk from the realised surface that stops at the first layer that is missing or insufficient" picks design when both requirement and design are insufficient. The table and the predecessor ("If the governing requirement is … insufficient, re-enter its owner; if that requirement is sufficient but …") pick the requirement | "stops at the highest layer found missing or insufficient", or "the table gives the stopping point" | TICKETS |
| WC1-13 | Low | R (I3-2a/2b) | One rule, two modal forms: FOUNDATIONS "never widen its scope …" against IDENTITY §6 "do not silently widen scope …" | IDENTITY cites the bullet and states only identity instances | IDENTITY |
| WC1-14 | Low | R | Restatements that add no domain binding: EVALUATION §5 "Applied to acceptance: a proxy cannot change Product meaning …" (the owner's proxy limit); PRODUCT_DEFINITION §11 "A matching digest establishes identity, not fidelity or sufficiency" | Refer only | EVALUATION; PRODUCT_DEFINITION |
| WC1-15 | Low | C | R19. FOUNDATIONS §2 holds no spelling list. AC-002 treats §2 Representation as its owner and keeps its own list. PRODUCT_DEFINITION:497 keeps a different list. This differs from the REDUCTION action, and the difference is not recorded | Record the chosen resolution in REDUCTION R19, or carry out the action; PRODUCT_DEFINITION:497 cites the owner | design; PRODUCT_DEFINITION (I3-3h) |
| WC1-16 | Low | C | R13. ACTIVATION:1523 "superseded in its mapping" is not a UP-015 value, and it cites the common requirement as its replacement relation, which ORACLE Q3 says accepts no particular replacement. I3-2a reported it not done | Split the row into UP-015 values, and mark any supersession as proposed | ACTIVATION |
| WC1-17 | Medium | P | PLAN step 1 rows omit REDUCTION §3 actions that name step 1 activations: R2 and R9 (I3-2b); R9, R12 and R25 (I3-2c); R13, R19 and the pillar 10 consumer (I3-2a); and I3-2e's new R12 locus AC:407. WC1-05 to -09, -15 and -16 follow from this. No later PLAN row holds the ACTIVATION or FOUNDATIONS bodies (I3-3j has "tables only"), so WC1-07 and WC1-16 have no territory at all. This blocks I3-4d's source settlement, after which member files change only through step 7 | The Executive assigns each item to a territory before I3-4d | Executive |
| WC1-18 | Info | P | I3-2c repaired R4 at PRODUCT_DEFINITION:411–432, which PLAN gave to I3-3h. The content is correct (Q4) | I3-3h's intake drops R4 or re-checks it | Executive |
| WC1-19 | Low | P | Every Writer reports cumulative acquisition over the 300,000-byte default without refining or stopping: I3-2a about 420 KB, I3-2b about 330 KB, I3-2c about 400 KB, I3-2e about 307 KB. This check did the same (§1). ORACLE E2 and I11; PLAN §3 | Record it in the ledger as a variance. Set limits per activation kind, or split the work | Executive |

## 5. Support per activation

| Activation | Supports | Blocking findings |
|---|---|---|
| I3-2a | `local_repair` | none of its own; WC1-13 is shared. Its owner texts are sound; its reported "not done" items are composed-state gaps (WC1-07, -15, -16) |
| I3-2b | `local_repair` | WC1-01 and WC1-02, both Medium |
| I3-2c | `local_repair` | WC1-03, WC1-04 and WC1-11 (Medium); WC1-12 |
| I3-2e | `local_repair` | none blocking. Its exit proof holds (Q5); only the REDUCTION summary row for R16 needs updating |

Separately, WC1-17 (Medium) asks the Executive to assign the omitted
REDUCTION actions before I3-4d.

No finding calls for `re_enter` or `reject`. Each repair is local to an
owning member or to a delta row. Rows 553, 481 and 593 need the product
owner's reading only if the Writers choose the `superseded` route instead
of the narrower text.
