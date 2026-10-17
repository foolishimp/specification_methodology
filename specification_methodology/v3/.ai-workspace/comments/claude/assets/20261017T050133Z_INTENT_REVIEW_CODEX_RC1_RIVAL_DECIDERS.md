# Reader report, verbatim, for the intent-level review of the Codex RC1 candidate `d1b3348`

One fresh-context Fable actor at maximum effort, author of neither candidate; same model family as the Claude candidate. The report follows unchanged.

---

# Rival deciders: eight shared questions in the candidate

All paths are relative to `successor/standards/` unless shown otherwise. Abbreviations: F = FOUNDATIONS.md, L = TRANSFORMATION_LIBRARY.md, S = SPEC_METHOD.md, T = TICKET_METHOD.md, B = STDO_REFERENCE_FRAME_BASELINE.md, RF = REFERENCE_FRAME_METHOD.md, R = RELEASE_METHOD.md, O = ODD_METHOD.md, D = DESIGN_MODULE_METHOD.md, I = IDENTITY_METHOD.md, AC = AXIOMATIC_CALCULUS.md.

The "Map" column means:
- **yes**: the enclosing section is listed in IDENTICAL_SECTIONS.md.
- **no**: it is not listed.
- **n/a**: the file is a frame, skill or README, which the map does not cover.

## 1. Outcome values and how domain labels map to them

| Locus | Map | Quote | Role |
|---|---|---|---|
| F:340–351, 392, 419–421 | no | "including an explicit missing-reason case … supplies a total, reason-sensitive map into this record" | Owner: five verdicts, performance, six effect values |
| RF:477–478 (RF-012) | no | "The five verdicts and their conjunction have that single owner." | Defers |
| S:1928, 1932–1939 | no | Table mapping `accept`/`local_repair`/`re_enter`/`reject` to core verdicts, citing F | Refines dispositions |
| B:563–580 | no | "finer domain outcomes, not another result algebra"; final row: "apply the core missing-reason rule" | Refines work results |
| B:1562–1563 | no | "total across the shared core verdicts as bound by RF-012" | Refines the review result |
| T:384–395; T:1487 | no | "These values select work-carrier state, not a second result algebra." | Refines close classes and status |
| R:314–322; O:1197–1198; D:2003; AC:458 | no | "domain dispositions refining the shared result algebra, not a competing verdict set" (O) | Refine |
| F:250; B:526; S:1420 | no | "Severity grades the supported consequence if a finding manifests." (F) | Severity is evidence; no locus maps it to a verdict |
| RF:124–131 ("Evaluation") | yes | "An evaluation family groups questions that require the same material relation manifold, authority basis, and result algebra." | Rival residue |
| plugins/…/stdo-review/SKILL.md:66–73 | n/a | "Keep the result projection total" | Applies |

**Classification: one owner, rival restated (weak).**
- Every domain table I found cites the F owner.
- The only uncited passage with a different answer is the unchanged RF "Evaluation" definition. It treats a result algebra as something each evaluation family has, and gives each evaluation its own "admissible result family".
- Severity is defined three times with the same answer. It is evidence, not an outcome value, so it is not a rival.
- One refinement does not conform. S's disposition table gives `accept` and `reject` no cause and has no missing-reason row, although F:419 requires one. B:580 and T:393 do include one.

## 2. When a recorded result may be reused, and what invalidates it

| Locus | Map | Quote | Role |
|---|---|---|---|
| F:819–822 | no | "an applicability relation permits its use for the new claim. A changed digest proves neither invalidity nor equivalence." | Owner |
| F:893 | no | "A stored green label is no validity argument." | Owner (reuse) |
| L:156–158 | no | "A previously satisfied check can be reused on supported unchanged premises" | Applies F |
| T:1059–1060; T:940–945 | no | "Reuse binds Contract application's Currentness condition to [Change impact and evidence retention]" | Defers |
| S:1981–1990 | no | "Retain applicable evidence on its original subject with the required new applicability relation." | Defers |
| B:1273–1274 | no | "establish the applicability relation needed to use its evidence on the new claim" | Defers |
| RF:736–737; I:422–423 | no | "Result reuse applies the shared currentness rule" | Defer |
| RF:409–410 (RF-005) | yes | "A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or requires reactivation." | **Rival** |
| frames: DOMAIN_BINDING:720, CONSTITUTIONAL_DERIVATION:901, EVALUATION_CONJUNCTION:349, RELEASE_ADOPTION:622, WORK_RECOVERY:996, TRIAGE_CARRIER:1263 | n/a (verbatim excerpt of in-map RF-005) | Same sentence | **Rival**, present in every task frame |
| B:731–732 (Steel-Thread Delivery) | yes | "Reuse qualified results while their exact subject and basis remain valid; rerun affected assurance when a material change invalidates it." | **Rival** |
| B:357; B:1850 | no | "invalidate affected results when the subject or basis changes"; "changed candidate or basis invalidates the affected review result" | Restated in own terms, uncited |
| B:691, 752, 785 | yes | e.g. "material intake, basis, checkpoint, dependency, configuration, capability, or topology change" | Invalidator lists local to each frame, uncited |
| plugins/…/stdo-review/SKILL.md:29–30 | n/a | "Reuse exact applicable computed facts and traceable prior judgments after checking their support and invalidation." | Applies |

**Classification: one owner, rival restated.**
- F lets a retained record serve a new subject through an applicability relation. It also denies that a changed digest invalidates a result.
- RF-005 makes a stale or advanced basis yield `invalid_basis`. RF's own derivation table (RF:363) lists RF-005 as "used by result reuse".
- Steel-Thread Delivery limits reuse to an unchanged exact subject.
- WORK_RECOVERY carries RF-005 (line 996) next to F's Change impact (line 1149), so the recovery frame holds both answers.

## 3. Who disposes of an assessed candidate

| Locus | Map | Quote | Role |
|---|---|---|---|
| S:1928–1930 | no | "It returns evidence and a proposed semantic disposition. Only the existing decision authority applies that disposition" | Owner (construction) |
| F:252–254; F:442–443 | no | "whose domain conditions belong to [Spec's proportional disposition]"; "Recording the decision is not its authority." | Defers to S |
| L:347–348; L:389–391 | no | "The actor with bound decision authority separately returns the authorised disposition; the library supplies no second table." | Defers |
| RF:425 (RF-007) | yes | "Decision authority disposes the result." | Same answer, uncited |
| B:780; B:794–795 | yes | "Executive as the authorized assessor or proxy that applies the one existing disposition" | Defers to UP-020, but merges assessor and disposer |
| B:1537–1538 (5A); B:1590–1603 | yes; no | "It applies `STDO-UP-020` disposition within its decision envelope." | Applies |
| T:404–406; T:1049–1050 | no | "The applied treatment has a separate decision predicate" | Applies (sprint and closure) |
| O:943; O:1201–1202 | no | "It decides close, yield, retry, repair, re-enter, reprice, or block"; "an unadmitted evaluator proposal supplies no admission fact" | ODD's own domain control, reconciled within ODD |
| S:1199–1202 (Sprint Execution Boundary) | yes | "Close review … classifies each gap, accepts compliant work, opens paydown work for local debt" | **Rival** |
| S:1977, also WORK_RECOVERY:654 and TRIAGE_CARRIER:1116 | no / n/a | "explicit non-changes, and the assessor disposition" | Ambiguous wording |
| plugins/…/stdo-review/SKILL.md:8–9 | n/a | "It does not repair, assign Product priority, apply disposition, or activate the next work." | Applies |

**Classification: one owner, rival restated.**
- S's UP-020 disposition rule owns construction disposition, and F defers to it.
- The unchanged Sprint Execution Boundary gives acceptance to the close review itself.
- T's rewritten Sprint Close Review separates that into an assessment and a decision "under the sprint's bound mandate".
- RF-007 states the shared law independently.
- ODD's `evaluate_action` returning a disposition is a declared domain function. F:239 permits it: "Other domain judgment and control functions retain their own declared contracts".

## 4. What confers authority

| Locus | Map | Quote |
|---|---|---|
| F:243–244 | no | "Neither evidence shape nor actor capability mints a grant." |
| F:1013 | no | "Roles acquire authority from their grants, never from their names." |
| F:232–233 | no | "The [frame authority law] owns authority conservation for frame evaluation." (points outward to RF-006) |
| RF:415–418 (RF-006) | yes | "does not mint, widen, transfer, or reconstruct … authority from actor identity, available capability, evidence shape, implementation reachability, or frame selection" |
| I:312–314 (UP-004) | yes | "must not silently widen scope, add a role, … or reconstruct authority from actor identity, payload shape, or available capability" |
| AC:445–446 (AC-005) | yes | "Copying, interpreting, encoding, evaluating, or transporting a record does not transfer authority." |
| L:148–149 | no | "Shared code, a source reference or a satisfied judgment supplies no missing grant." |
| B:686; B:758 | yes | "no operation authority or other authority arises from the Executive label"; "The Worker label grants no mutation authority." |
| T:861–863 | no | "Drafting, admitting, or retaining an active execution contract cannot create or renew authority" |
| README.md:19–20; standards/README.md:50 | n/a | "Views and skills … confer no operation or decision grant"; "a prepared frame grants no work or admission" |
| plugins/…/stdo-review/SKILL.md:47; plugins/…/stdo-work/SKILL.md:16 | n/a | "test presence creates no authority"; "that selection grants no work or mutation authority" |

**Classification: no single owner.**
- Every locus gives the same answer: none of a check, a label, a frame, a tool or a capability grants or widens authority.
- At least five loci decide this independently, each over a different list of things that cannot confer authority.
- F hands frame evaluation to RF-006 and a_c to AC-014, then states its own general rule. RF-006, UP-004 and AC-005 are unchanged and cite nothing in F.
- No locus covers all five sources the question names. A passing check is covered only by L ("satisfied judgment") and T (contract admission).

## 5. When a review is independent

| Locus | Map | Quote | Role |
|---|---|---|---|
| T:874–876 (UP-007) | no | "Where independent review is required, the reviewer is not the author of the reviewed subject" | Owner |
| T:872 | no | "Fresh context alone changes no authorship relation." | Owner |
| F:1011–1012 | no | "retains its authorship and evidence conditions; a new context alone does not supply it" | Restates, defers through "its" |
| F:1047 | no | "Domain contracts select acceptable derivations and required authorship independence." | Points outward |
| B:787–788; B:1798–1802 | yes | "`STDO-UP-007` controls"; "`STDO-UP-022` adds its declared … reference-exposure, and freeze conditions" | Defers |
| B:172–173 | no | "a fresh context does not remove an actor's authorship" | Applies |
| RF:247–250 | yes | "the governing assurance law states the required non-authorship, evidence-acquisition, reference-exposure, actor, and configuration separation" | Defers |
| RF:738–740; T:949–950 | no | "may share valid mechanical evidence while supplying their own sufficiently acquired evidence and judgments"; "Reusing the author's J cannot satisfy that condition." | Shared-evidence rule |
| S:1890–1892 | no | "rather than treating the constructor's summary as sufficient evidence" | Applies |
| S:2541–2545 (UP-022) | no | "An independently authorized evaluator has a declared governing basis and comparison predicate"; "withheld from the constructor until its construction result is frozen" | Uncited refinement |
| plugins/…/stdo-review/SKILL.md:27–31 | n/a | "Do not use the Worker summary as evidence." | Applies |

**Classification: one owner, rival restated (mild).**
- UP-007, located in Ticket Method, owns authorship independence, and its consumers cite it.
- UP-022 sets its own independence conditions for method qualification. It never names UP-007, Ticket Method or Foundations; I checked all of S:2516–2603.
- Only the Baseline (B:1800–1802) links the two. The answers are compatible, but the ownership link is missing.

## 6. What follows when work cannot finish

| Locus | Map | Quote | Role |
|---|---|---|---|
| F:447–449 | no | "A stop reports the actual destination or task predicate through this record, with its reason, observed effects and outstanding obligations." | Owner |
| F:216–217; F:985–986 | no | "requests the owning decision, or stops with an explicit unresolved result"; "Stopping can be lawful without completion." | Owner |
| S:158–160 | no | "binds each returned state and reason to its actual task predicate under the [core stop rule]" | Defers |
| T:749; T:800–802 | no | "stop or re-enter"; "retain the exact failed or undecided admission predicate" | Defers |
| B:592–593; B:366–367 | no | "incomplete work names its stop basis; re-entry identifies the owning authority and material relation" | Defers |
| O:884–885 | no | "through the [core stop contract]" | Defers |
| D:1999–2002; L:439–440 | no | "[Bounded construction] supplies progress, stop and total-handling distinctions." | Defer |
| RF:519–521 (RF-014) | yes | "human authority may select another actor, refine the frame, sequence activations, or provide a lawful compression" | Cited by F:213–215 |
| S:1206–1207 | yes | "split, escalated, repriced, or carried as explicit paydown according to the governing method" | Defers |
| O:760–763 (11.5A) | yes | "ABG owns: continuation authority; re-entry after publish boundaries" | Runtime allocation within ODD |
| plugins/…/stdo-work/SKILL.md:94 | n/a | "An unavailable result surface or unresolved authority returns its actual cause" | Applies |

**Classification: one owner, consumers defer.** Where work re-enters is delegated to S (F:1042: "Spec Method owns Product progress and re-entry").

## 7. Combining one failed, one not-performed and one stale result

| Locus | Map | Quote |
|---|---|---|
| F:499–501 | no | "An unauthenticated claim cannot discharge an obligation. A missing planned judgment remains an absent slot with its known performance fact" |
| F:508–510 | no | "Any authenticated, applicable falsification … makes the conjunction `falsified`. Missing or undecidable other coverage remains explicit alongside it." |
| L:355 | no | "Known failure and required uncovered coverage both survive the aggregate." |
| RF:477–478; RF:780–781 | no | "A declared decision rule consumes closed frame results through [core conjunction]" |
| B:1526; B:1868–1869 | no | "aggregate green status cannot hide a missing, conflicted, stale-subject, or wrong-path testing-frame result" |
| R:321–322; T:401 | no | "the release labels supply no alternative rule for them" |
| O:1210–1211 | no | "indeterminate only when core conjunction has no deciding falsification" |
| plugins/…/stdo-review/SKILL.md:33–34 | n/a | "unknown applicability or a missing required exact result prevents a satisfied conjunction" |

**Outcome.** The aggregate is `falsified` by rule 1:
- The failed result decides it.
- The not-performed result stays an absent slot that keeps `not_performed`.
- The stale result cannot discharge its slot.

RF-005 would label the stale member `invalid_basis`. That conflict belongs to question 2 and does not change this aggregate.

**Classification: one owner, consumers defer.**

## 8. How a reported defect enters work

| Locus | Map | Quote | Role |
|---|---|---|---|
| S:1380–1382 | no | "There is one front door for substantive change. The intake label does not determine the process class." | Owner |
| S:1463, 1465 | no | "`requirement_reprice` … re-enters at Requirements"; "`realization_refactor` … re-enters at the realized surface only" | Owner (classes) |
| S:1593–1594 | no | "If that contract remains sufficient for the authorized outcome, reject or locally repair the candidate within its grant." | Owner (treatment) |
| F:962–964 | no | "Its intake label supplies neither cause, repair class nor grant." | Defers to S |
| T:663–664; T:712–714 | yes | "using the change classes from `SPEC_METHOD.md`" | Defers |
| T:700 | no | "Apply the Spec owner's rule to the affected layer" | Defers |
| R:79–80 | yes | "Release handling is downstream of intake triage." | Defers |
| B:1302–1303 | no | "a test label supplies no repair class, cause or authority" | Defers |
| plugins/spec/references/GETTING_STARTED.md:377–378, 390–397 | n/a | "The owning rule is `SPEC_METHOD.md`, **Computed Classification And Treatment**" | Defers |
| plugins/…/stdo-ticket/SKILL.md:29, 37 | n/a | "Select the smallest lawful change class" | Applies |
| T:670–671 (Change Class) | yes | "`bug` with `requirement_reprice`, `design_reframe`, or `realization_refactor`" | Label-to-class pairing |
| S:3400–3401 (`## Method`) | no | "If constitutional: reprice **Goals** when the current work wave changes, write a new **Intent**, then flow forward" | **Rival** |

**Classification: one owner, rival restated.**
- S's `## Method` section is not in the map and cites nothing. It splits a defect into "implementation" or "constitutional".
- Its constitutional branch rewrites Intent, where intake would re-enter at Requirements under `requirement_reprice`.
- Its implementation branch says "write requirements/design as needed", where `realization_refactor` re-enters at the realized surface.
- T's pairing ties the `bug` label to classes below Product, which contradicts F:962.
- Neither passage appears in the frames.

## A. Does the Foundations tier govern these questions?

Partly. Foundations owns questions 1, 2, 6 and 7 itself, and every rewritten consumer of those cites it. For the other four it points ownership outward instead of governing:
- Q3 to Spec: "whose domain conditions belong to Spec's proportional disposition" (F:252–254).
- Q4 to RF-006, an unchanged section: "The frame authority law owns authority conservation for frame evaluation" (F:232–233).
- Q5 to domain contracts: "Domain contracts select … required authorship independence" (F:1047).
- Q8 to Spec intake (F:962–964).

Unchanged predecessor sections still decide next to the new owners:
- Q2: RF-005, copied into all six task frames, and Steel-Thread reuse.
- Q1: RF "Evaluation".
- Q3: "accepts compliant work" in Spec's Sprint Execution Boundary.
- Q8: Ticket's bug pairing.

Spec's `## Method`, which is not in the map, gives a different re-entry rule for Q8.

| Classification | Count | Questions |
|---|---|---|
| One owner, consumers defer | 2 | Q6, Q7 |
| One owner, rival restated | 5 | Q1, Q2, Q3, Q5, Q8 |
| No single owner | 1 | Q4 |
| Cannot tell | 0 | — |

Q1 and Q5 rest on uncited restatements whose answers are compatible. Counting only different answers moves them to "defer", giving 4 / 3 / 1 / 0.

## B. Loci an actor entering at README.md must read for questions 1 and 3

**Question 1: 8 loci.**
1. README.md:11–15
2. standards/README.md:14–19
3. F Result algebra, 322–451
4. F Judgment and authority, 249–254 (severity)
5. RF-012, 474–509
6. S Proportional Disposition, 1924–1959
7. T Sprint Close Review, 362–429
8. T Allowed Status, 1475–1493

`candidate_ready`, `refused`, `incomplete` and `re_entry_requested` are mapped only in the Baseline, which applies only when a Product adopts that profile. WORK_RECOVERY.md:16–17 says: "no WorkerResult enum or falsified-to-refused mapping follows from this view". If the profile is adopted, add B Work result (555–603), Technical triage (502–540) and Reviewer projection (1560–1588), for 11. RF "Evaluation" would be a twelfth to reconcile.

**Question 3: 9 loci.**
1. README.md:5–6, 19–20
2. standards/README.md:24–27, 112–114
3. F 249–254
4. F 437–443
5. L Evaluate, 344–348
6. L Dispose, 368–391
7. S Proportional Disposition, 1924–1959
8. S Construction, Assessment, And Delegation, 1886–1922
9. RF-007, 420–426

If the profile is adopted, add B Derived Executive Frame (677–700), Derived Reviewer Frame (771–796), 5A (1533–1541) and step 7 (1590–1612), for 13. A sprint item also needs T 404–413 and the rival S 1199–1202.

Without double-counting, the two questions together need 12 distinct loci, or 19 with the profile adopted.

## Limits

- **Tool calls:** 46 of 50, including one advisor consultation.
- **Not searched:**
  - `interpretation/` (FRAMES.md, program.json, MAPPING.json, source-account.json).
  - `authority_compressions/`, excluded on purpose even though spec_method.compressed.md and stdo_compressed.md contain `accept`, `local_repair`, `re_enter` and `reject`.
  - `templates/` and `schemas/`.
- **Only partly read:**
  - UX_METHOD and WORLD_MODEL_METHOD were reached only by greps. POSTING_GUIDE and WRITING_GUIDE were not read.
  - The frames were searched for specific sentences, not read whole, and I did not check their excerpts against the source sections.
  - GETTING_STARTED was read only at lines 364–400. The stdo-help and stdo-status skills were only grepped.
- **How I read the map:** I took each listed section to run to the next heading of any level, and gave each line the status of its nearest preceding heading. This fits the evidence that RF:760 is listed while its subsection RF:778 cites Foundations. "no" means changed or new, not necessarily new wording. I did not diff against the predecessor directly.
- **Search method:** loci were found by keyword. A rival rule written in other words could have been missed.