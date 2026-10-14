# WC-2: Working Check Of Iteration 3 Step 2

Same-family working reviewer for the Claude build line. I wrote none of the assessed text. This is working evidence only. It accepts nothing and is not a member review.

## 1. Subject, basis and limits

- Subject S = commit `2a2af3a` (worktree `/Users/jim/src/apps/specification_methodology-claude`). All subject files read with `git -C T show 2a2af3a:./<path>`; T is `specification_methodology/v3/build_tenants/claude`. Baseline `007727a`. Predecessor P = installed `v2.5.1-rc.2/standards/`, cited P:FILE:lines.
- Terms. A family table is a table with the five-column header named in the task. A "row" of a family table is one body line. A frontier row is a line of `frontier/PREDECESSOR_CLAIMS.md`. `conserved`, `meaning change` and the row labels M1 to M5 are defined in `reassess/rows.md`.
- Files read at S: the 17 family tables in the 13 named members (sampled rows, plus the instance-premise paragraph above each table); FOUNDATIONS.md lines 146-160 and 556-570; the word-level diff `007727a..2a2af3a` of standards/ and plugins/ and design/ with table-row hunks skipped (read in full for SPEC_METHOD, ACTIVATION, TICKETS, TRAVERSAL_OCCURRENCE, UX, WORLD_MODEL, IDENTITY, WRITING_GUIDE, REFERENCE_FRAME, EVALUATION, AXIOMATIC_CALCULUS, PRODUCT_DEFINITION, RELEASE, ASSURANCE, EXECUTIVE_BASELINE, FOUNDATIONS, README, PROFILES, GLOSSARY, templates, design, plugins; CONFORMANCE diff not read); the deltas I3-2r, 3a, 3b, 3c, 3d, 3f, 3g, 3h, 3j, 3k; F1-F5.md lines 244-end; PREDECESSOR_CLAIMS.md at S (rows and every "superseded" cell, by script); excerpts of EXECUTIVE_BASELINE, ACTIVATION, EVALUATION, SPEC_METHOD, REFERENCE_FRAME, IDENTITY, RELEASE at S; P excerpts from STDO_REFERENCE_FRAME_BASELINE, REFERENCE_FRAME_METHOD, IDENTITY_METHOD, SPEC_METHOD, RELEASE_METHOD, TRAVERSAL_OCCURRENCE_PROFILE.
- Bytes acquired (displayed to me, counting repeats): about 365 KB, about 15 KB over the 350 KB guide. Step 0 28 KB; table check about 105 KB; deltas and F1-F5 about 93 KB; frontier and verification excerpts about 50 KB; diffs about 90 KB. Some files were copied whole to scratch and filtered by script (family tables, frontier); only the filtered output was displayed. These figures are estimates from my output sizes, not a metered count.
- Start `date -u`: Wed 14 Oct 2026 18:26:12 UTC. End `date -u`: Wed 14 Oct 2026 18:36 UTC (system clock; see R2 for file time).
- Not done: CONFORMANCE diff and its 52-row mapping; the unsampled rows of each family table (about 70 percent); family tables F17, F18 (DESIGN_MODULE, ODD) which the task did not list; the I3-2a, 2b, 2c deltas; all rows marked D in `reassess/rows.md`.

## 2. Expectations, recorded before opening the subject

Terms. "Family table" is a Markdown table with columns premises, consequence, rule, added choice and owner, pillar. "Core value" is a value of the Foundations' single result algebra. "Predecessor" is the installed rc.2 text, cited P:FILE:lines. "Frontier" is frontier/PREDECESSOR_CLAIMS.md.

X1 (ORACLE B1, B3; PLAN step 2). Each sampled table row has cited premises that force the consequence, or a named policy choice with an owner that carries what the premises leave open. A rule filed wholly as a choice is hollow. File boundaries are not a justification for a grouping.
X2 (B2, B12). Unchanged inherited deciding rules appear in the tables, not only edited ones. A reference keeps the trigger, force and exceptions of the rule it refers to.
X3 (A0-A10). Each Pillar cell names a contribution that FOUNDATIONS section 3 lists, and is plausible for the rule. A pillar is not asserted as an independent axiom.
X4 (B4, B5). Consumers decide through the shared contract in their own deciding text. A bare cross-reference is not the only connection. Text at the candidate supplies the determination; `stdo://` links are provenance only.
X5 (D1, D5). One owning locus per rule. A rival either refers or refines with a mapping. No two loci decide; no precedence replaces an owner; no circular referral.
X6 (D2, D3). Placement follows the responsibility table: profiles own bindings only, packaging derives meaning, generic law is not only in the ODD or Traversal profile.
X7 (D6, D7, N3). Every value set that decides maps each value to exactly one core value, with predicate and meaning conditions. No value maps to zero or two core values. No bare "see core" where a map is owed. Conjunction is defined once.
X8 (D8). Standing never rises: failure and undecidable never become satisfied; "not performed" stays distinct from "cannot decide"; unknown-completion effects never become "no effect" or "completed".
X9 (D9, D10, N2). Availability, assessment and acceptance stay separate. `candidate_ready` is not read as fitness. A status field does not decide closure. Nothing in the diff claims member, checkpoint, supersession or removal acceptance.
X10 (B12, H6, Q10, N9). A change of scope, force, trigger or exception is a supersession. A `conserved` row carries no new obligation. A conditional policy does not become unconditional.
X11 (N11). No new obligation or process step appears without its stated purpose.
X12 (H4, H5). Each `superseded` row names the claim, the replacement and its loci, and is marked proposed, pending the product owner. No supersession is shown as accepted, and no hash or review is cited as acceptance.
X13 (H3, B5, C4). Each conserved or superseded row names an owner locus that resolves to candidate text, not to predecessor text.
X14 (E2, E3, E7). No rule lets capacity pressure license omission; byte fit and attention adequacy remain separate.
X15 (N5, N12). Changes stay in the member territories: standards, plugins, design, frontier. No change to the 2.* line, stack_release.json, or the common specification.
X16 (N7, N8). No role inventory, hierarchy, universal budget or fixed actor count becomes law; example specifics (Hello World and the like) do not become method rules.
X17 (D4, D11). A frame copy names and matches its owner; a result-returning frame carries the core algebra or its map.
X18 (H2, G6). Each frontier row has one disposition value; the unselected categorical capability is not presented as law or accepted.

## 3. Results

### 3.1 Table check (PLAN step 2)

Method. For each table I took the first row and rows spread across it, at least 30 percent (rounded up). `real`: the cited premises, with the instance premises the member declares, force the consequence, or a named policy with an owner carries what they leave open. `weak`: a cited premise does not do the work claimed. `hollow`: the whole rule filed as a choice or a consequence with no derivation. Pillar cells were compared to the FOUNDATIONS paragraph at FOUNDATIONS.md:560-569 (ten pillars, a Pillar cell is a trace and not a premise). I also computed, for every table, the union of its Pillar cells and compared it with the FOUNDATIONS index cell (FOUNDATIONS.md:601-621).

| Table (rows) | Sampled | real | weak | hollow | Weak rows (line at S) |
|---|---|---|---|---|---|
| REFERENCE_FRAME F1 (36) | 11 | 10 | 1 | 0 | :181 |
| ACTIVATION F2 (9) | 3 | 3 | 0 | 0 | |
| ACTIVATION F4 (6) | 2 | 2 | 0 | 0 | |
| ACTIVATION F5 (6) | 2 | 2 | 0 | 0 | |
| EVALUATION F6 (17) | 6 | 5 | 1 | 0 | :76 |
| EVALUATION F7 (12) | 4 | 3 | 1 | 0 | :440 |
| IDENTITY F8 (12) | 4 | 3 | 1 | 0 | :72 |
| AXIOMATIC_CALCULUS F9 (19) | 6 | 5 | 1 | 0 | :183 |
| SPEC_METHOD F10 (13) | 4 | 4 | 0 | 0 | |
| SPEC_METHOD F11 (10) | 3 | 3 | 0 | 0 | |
| TICKETS F13 (11) | 4 | 2 | 2 | 0 | :593, :600 |
| PRODUCT_DEFINITION F12 (10) | 3 | 2 | 1 | 0 | :123 |
| RELEASE F15 (12) | 4 | 3 | 1 | 0 | :129 |
| ASSURANCE F14 (14) | 5 | 5 | 0 | 0 | |
| TRAVERSAL_OCCURRENCE F19 (9) | 3 | 3 | 0 | 0 | |
| UX F20 (10) | 3 | 3 | 0 | 0 | |
| WORLD_MODEL F21 (11) | 4 | 4 | 0 | 0 | |
| **Total (204)** | **71 (35%)** | **62** | **9** | **0** | |

Why each weak row is weak (one line each):
- REFERENCE_FRAME.md:181 (failure coverage): P4b and P5 force that a known failure persists as input, but the list "success, refusal, boundary, integration, recovery, reconstruction and competing-path cases" is a choice, and the choice cell says "none".
- EVALUATION.md:76 (independent assessment protocol): P3 and P6 force a frozen, identified subject. "The assessor makes no repair" and "a revision after exposure is a declared intervention" are not forced by the cited premises and are not named as choices. The unconditional freeze is also the subject of WC2-01.
- EVALUATION.md:440 (bounded-construction trial): P0 forces bounded context. Declaring a cap and a work budget "before each run" and counting context "across every delegated actor" is a policy; the choice cell says "each cap and budget: the trial's declaration", which names an owner for the value, not for the obligation to declare.
- IDENTITY.md:72 (consequence for implementations): P3 and P1 force reading identity through published law; "the enduring repair publishes identity law and moves implementations onto it" is not forced by P0 (bounded repair) and the choice cell is "none".
- AXIOMATIC_CALCULUS.md:183 (conformance obligations): P6 alone forces evidence per law; "positive and refusal cases" is a policy not named as one.
- TICKETS.md:593 (sprints): P2 does not force the existence of a sprint; the choice cell lists fields and statuses but not the decision to batch closure at all.
- TICKETS.md:600 (recommended shapes): the second sentence ("it reads this member only for the question a derived surface leaves open") is guidance, not a consequence of P0, and no policy owner is named for it.
- PRODUCT_DEFINITION.md:123 (one authority surface): P6 and P3 force one owner per law. "The members govern only together, as one released version" is a release-unit choice not named in the choice cell.
- RELEASE.md:129 (support lines): P4b and P6 force a disposition; the four named items (watched source, observation boundary, inclusion policy, successor candidate) are a choice with no owner (the cell names only the mechanism owner, "the consumer").

No hollow row found in the sample. The three rows that PLAN lists as formerly hollow or weak and that I read (EVALUATION.md:70, :78, IDENTITY.md:70; the PLAN's older line numbers map to these) now carry derivations and I rate them real. TICKETS.md first-row (:590) now derives the smallest-carrier order and rates real.

Pillar cells. Every row carries a Pillar cell. None is implausible in the sample. Each table's union of Pillar cells equals the FOUNDATIONS index cell (checked by script for all 17 tables; EVALUATION and SPEC_METHOD per table). I found no row where the Pillar cell is used as a premise.

Coverage question (do all deciding sections appear in the table or get excluded with a reason): I did not check this for the unsampled sections. The deltas claim it; not verified.

### 3.2 Diff check against the expectations (X1 to X18)

- X5, X10, X12, X13 (single owner, conserved versus changed meaning, supersession marking, owner resolves). Fourteen frontier rows (162, 210, 512, 518, 525, 528, 548, 559, 567, 573, 660, 671, 686, 797) carry "superseded, proposed and pending the product owner's acceptance". I found three firm and two possible further meaning changes that the frontier marks only `conserved` (M1 to M5 in `reassess/rows.md`): WC2-02, WC2-03, WC2-04 (firm) and WC2-05, WC2-06 (possible). No rival wording is shown as owning a rule. Referrals are acyclic in the pairs I traced: EVALUATION §3 refers to TICKETS §7 for when independence is required, TICKETS §7 refers to EVALUATION §3 for what counts as independent; the split is by sub-question, each stated once. UP-007 is now spread across three owners (EVALUATION §3, TICKETS §7, EVALUATION §5); acceptable, noted for the integrated assessment.
- X2 (no lost predecessor trigger, force or exception). Two conditional policies lose their condition: the freeze rule (WC2-01) and, in the plugin text, the residual route for unknown conditions (WC2-08). Moves of text to owners kept "only when" (EVALUATION.md:281-298), the four blocking conditions, the closure condition and the reconstruction-litmus sentences (EVALUATION.md:372-387).
- X7, X8 (result values map to exactly one core value; standing never rises). TICKETS close classifications (`remove` takes `falsified` with no matching disposition), UX §15 and WORLD_MODEL §14 refinements ("mapped to exactly one core value for a named predicate"), REFERENCE_FRAME coverage statuses (:700-720 each status one core value), TRAVERSAL `out_of_frame` exclusion with reason. No value maps to two core values in what I read. "A verification that was not run has no result" (WORLD_MODEL row 186) keeps "not performed" distinct. CONFORMANCE R1 text ("planned evaluation that was not performed") consistent. I did not read ACTIVATION §3's full map; the `incomplete` to `falsified` map is the marked supersession.
- X9, X11 (no acceptance, no new obligation without purpose). Nothing in the added lines claims member, supersession or checkpoint acceptance (grep of added lines for ratified, accepted by, product owner accepted: no hit). New law I read states its purpose: ADR rules (SPEC_METHOD.md:1666-1677), IDENTITY §2 (IDENTITY.md:128-150), GLOSSARY §17, ACTIVATION.md:243-249, UX Msg-replay purpose (UX.md:440-446), EVALUATION §5 table. ODD §11.5D "never recorded as a disposition" could read as a prohibition without a stated reason beyond the homonym fix (low).
- X14, X15, X16 (capacity, territory, no role inventory). No rule in the diff lets capacity license omission. Changes are confined to standards/, plugins/, design/ and templates. "Executive" is rewritten to "coordinating" in plugins and the basis template, with a configuration-neutral slot; the basis template now says its Executive sections apply "only when the Product adopts that profile" (a scope narrowing of template text, noted in R2 row 820).
- X17 (frames). Not checked; no frame files in the diff range I read.
- X18 (one disposition, categorical capability). Frontier cells have one value each in the rows I read. 805 to 814 are `unresolved` with a proposal (WC2-07). The categorical capability is not presented as law in anything I read.


## 4. Findings

| ID | Severity | Finding, with file:line at S | Smallest repair | Territory |
|---|---|---|---|---|
| WC2-01 | High | A conditional policy became unconditional in shared law. P:STDO_REFERENCE_FRAME_BASELINE:505-509 and :1367-1368 freeze the candidate before material reference exposure only "where STDO-UP-022 generic method qualification applies", and "elsewhere" stabilise the subject by an immutable identity "or an equivalent exact-subject relation sufficient for the claimed assessment". EXECUTIVE_BASELINE.md:504-507 and :1206-1208 keep that condition. EVALUATION.md:154-156 and the F6 row at :76 say assessment "binds a subject frozen by identity before material reference exposure ... never a working tree" for every independent assessment. Step 2 extends the unconditional reading to `plugins/spec/references/GETTING_STARTED.md:605` ("freeze one exact review subject by identity before material reference exposure (EVALUATION §3 Protocol)"), and the I3-3d delta says the narrower plugin condition "was not a member rule". Two loci decide the freeze differently (D1, B10, B12). | Restore the condition in EVALUATION §3 Protocol and in GETTING_STARTED (freeze where qualification requires it, otherwise an immutable identity or an equivalent exact-subject relation sufficient for the claim), or mark the widening as a proposed `superseded` row pending the product owner and make EB cite it. | `standards/EVALUATION.md` (also `plugins/spec/references/GETTING_STARTED.md`, `standards/EXECUTIVE_BASELINE.md`) |
| WC2-02 | Medium | Modal force change presented as `conserved`: P:REFERENCE_FRAME_METHOD:755 "may invalidate the coverage result" became "invalidates the coverage result" for a change "that could change the coverage result" (REFERENCE_FRAME.md:645-650). The F1 row at REFERENCE_FRAME.md:179 still says "may invalidate it", so the member states the rule twice with different force. PC:351 says only `conserved`. | Keep "may" at :645-650 and cite ACTIVATION §7's materiality as the trigger, or add a child `superseded` row, proposed and pending the product owner, and align :179. | `standards/REFERENCE_FRAME.md` (and `frontier/PREDECESSOR_CLAIMS.md` if a child row is added) |
| WC2-03 | Medium | Scope narrowing presented as `conserved`: P:STDO_REFERENCE_FRAME_BASELINE:450-452 lets the Product-owned basis bind "non-waivable hard stops". EXECUTIVE_BASELINE.md:408-416 says the basis "adds no kind of stop" beyond the classes of ACTIVATION §4, and ACTIVATION.md:985-987 calls those classes "Typical hard-stop classes include", so the limit conflicts with its own owner. PC:516 says `conserved`. | Remove "and the basis adds no kind of stop", or propose it `superseded` pending the product owner. | `standards/EXECUTIVE_BASELINE.md` |
| WC2-04 | Medium | Modal force "may" lost: P:TICKET_METHOD:879-883 "the authorized Writer may record the satisfied bounded result in the existing carrier without adding ..." became "the constructor that holds the grant records the satisfied bounded result" (ACTIVATION.md:486-491) and "the grant holder records the conditions it found satisfied" (ACTIVATION.md:66). A permission reads as a duty, and "records only conditions that were evaluated" is new. EXECUTIVE_BASELINE keeps "may finish as Writer", so the two loci differ. The I3-2r delta judged it conserved. | Write "may record" at both ACTIVATION.md loci. | `standards/ACTIVATION.md` |
| WC2-05 | Low | The basis template drops the predecessor's completeness rule: P:templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md:154 "Coverage is complete only when every mandatory material evaluation and interaction is closed, or governing authority explicitly retains its residual" is replaced by "Coverage is complete as REFERENCE_FRAME.md section 8, Coverage ledger, states". REFERENCE_FRAME.md:681-720 maps each row status to a core value but I found no sentence that a coverage claim is complete only when every row is closed, and "interaction" is gone. | Cite the REFERENCE_FRAME sentence that carries "complete only when", or restore it. | `standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` |
| WC2-06 | Low | RELEASE.md:615-617 defines "release-blocking gaps" as "the findings that block promotion under EVALUATION §5". P:RELEASE_METHOD:481-482 leaves the term undefined. A gap that is not a finding falls out of the criterion. | Use "including" in place of the appositive, or name the other gap kinds. | `standards/RELEASE.md` |
| WC2-07 | Low | Frontier rows 805 to 814 (ten authority compressions) say "unresolved; proposed superseded by projection ... pending the product owner's ruling". The required wording is "proposed and pending the product owner's acceptance". | Use the standard phrase in the ten cells (disposition `unresolved` stays tolerated for packaging rows). | `frontier/PREDECESSOR_CLAIMS.md` |
| WC2-08 | Low | `plugins/spec/skills/stdo-work/SKILL.md:113-116`: the installed text "an unknown condition needs a bounded resolution or explicit residual" now allows only resolution ("is unresolved, not false, and the claim that depends on it is withheld until evidence or the owning decision resolves it"). The "explicit residual" route is removed from permitted work. The delta justifies it by ACTIVATION §1 Applicability, but it is a change of permitted work (Q10) in shipped text. | State it as a proposed change pending the product owner, or restore the residual route if ACTIVATION §1 allows it. | `plugins/spec/skills/stdo-work/SKILL.md` |
| WC2-09 | Low | Nine weak family-table rows (section 3.1): REFERENCE_FRAME.md:181, EVALUATION.md:76, :440, IDENTITY.md:72, AXIOMATIC_CALCULUS.md:183, PRODUCT_DEFINITION.md:123, RELEASE.md:129, TICKETS.md:593, :600. Each states a choice that its cited premises do not force and that the choice cell does not name. | In each, add the missing choice and its owner to the fourth column ("a policy of this member: ..."), or narrow the consequence to what the premises force. | the nine member files |
| WC2-10 | Low | Two wordings of one authority rule coexist. P:IDENTITY_METHOD:220 "must not silently widen scope, add a role ..." became FOUNDATIONS.md:152-155 "never widen its scope, add a role ...", while IDENTITY.md:67 still says "never silently widen" and DESIGN_MODULE `#authority-model` keeps rc.2's "implicitly" (per the I3-3b delta; not re-read). I judge the outcome unchanged because FOUNDATIONS.md:157-158 keeps the explicit-decision route, but the owner and its instances differ in force wording. | Make instances quote the owner's words, or add "silently" to the owner. | `standards/FOUNDATIONS.md` |
| WC2-11 | Low | Modal drift from "must" to an indicative in normative lists: P:SPEC_METHOD:2570 "must be explicitly re-adopted" became "is explicitly re-adopted" (SPEC_METHOD.md:1478-1480); P:TICKET_METHOD:284 "the close review must classify" became "the close review classifies" (TICKETS.md hunk at :291-296). Probably harmless but exact modal force was asked for. | Keep "must". | `standards/SPEC_METHOD.md`, `standards/TICKETS.md` |
| WC2-12 | Low | UX prompt carriage (UX.md:401-406) drops "rather than require the worker to rediscover it from the raw member" and allows "otherwise the deciding sections of this member". No rc.2 body row (compression claim), so no frontier meaning change, but a prohibition is loosened. | Record it as part of the pending compression ruling. | `standards/UX.md` |

Row counts for the re-assessment (R2): about 75 rows or groups in the named deltas and F1-F5; about 30 verified against P and S text; the rest judged from the delta. Meaning changes not yet marked proposed: 3 firm (M1 PC:351, M2 PC:516, M3 the recording-without-review sentence) and 2 possible (M4 PC:820, M5 PC:400).

## 5. Support

Step 2 as a whole: `local_repair`. The deficiencies are in named member files (WC2-01 to WC2-06) and can be repaired by the Writers without a change upstream, except that choosing to keep WC2-01, WC2-02 or WC2-03 as written would need a proposed `superseded` row and the product owner's acceptance. I do not give `accept`: the sample covers 35 percent of the tables, 30 of about 75 re-assessed rows were read at both texts, and the check is same-family.

