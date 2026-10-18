# Scenario walkthroughs: candidates A and B

Conventions. Entry for every trace: `standards/README.md` (A: 28,091 bytes, 189 lines; B: 10,542 bytes, 139 lines). Hops = sections acquired beyond the entry. Bytes = `sed -n 'a,bp' | wc -c` over every range read in that trace, entry included. Line numbers are file lines. Quotes are ≤25 words. Heading maps (`grep -n '^#'`) were used to resolve section ranges and are not counted as bytes. Tenant names appear as `[tenant]`; I did not try to identify authors.

---

## S6 — Product definition says UTC; requirements silent; exports carry local time

### A

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README, Routes row "triage a report, select its change class and re-enter" | 23 | names SPEC_METHOD §4, §5, TICKETS §4 |
| 1–3 | SPEC_METHOD §4 Universal intake triage; Change classes; Computed classification and treatment | 825–1019 | named by row |
| 4 | SPEC_METHOD §5 Ambiguity governance | 1180–1247 | named by row |
| 5 | TICKETS §4 Triage metadata | 520–529 | named by row |
| 6–7 | TICKETS §4 Change class; Upward propagation check | 457–519 | Triage metadata: "Change class and Upward propagation check above" |
| 8 | SPEC_METHOD §2 Constitutional chain | 213–280 | §4 names "the lawful re-entry point into the constitutional chain" |
| 9 | SPEC_METHOD §2 Trace closure and anti-drift | 573–614 | the chain's drift/"break at any link" is this section |

Decisions
- Must: one front door; triage determines six things (SPEC 832–841); diagnosis among four causes and "routes each supported repair to the owner of its cause rather than inferring it from the intake label" (SPEC 848–851).
- Kind: an insufficient governing requirement, i.e. drift: "a gap not expressible in current requirements needs re-entry at the layer its change class names, Requirements or upstream, not a code hack" (SPEC 611–614). Upward walk: "the governing requirement is missing or insufficient | `requirement_reprice` | re-enter the requirement's owner" (TICKETS 512).
- Layer and downstream: "`requirement_reprice` | constitutional truth changes while project direction stays stable | Requirements | Design, Code, Evidence" (SPEC 886). Product definition "provides the surface that requirements decompose" (SPEC 258–259).
- Code patch alone: prohibited. `realization_refactor` only when "the current requirement and accepted design suffice, and the implementation deviates" (TICKETS 515) and it "must prove no upstream drift" (SPEC 888).
- No new goal: repricing "generates new goals or intent where the work wave, direction or scope changes" (SPEC 240–242) — not triggered here.
- Who decides: triage declares class; "A changed governing relation is accepted only at its owner" (SPEC 892–893); the ticket records `change_intent`, `change_class`, `re_entry_point`, `triaged_at` (TICKETS 522–528).
- Unresolved: "a frame planned and not applied leaves its diagnosis open, never ruled out" (SPEC 868–869); "unresolved intended meaning or necessity is J, and any reserved decision remains O" (SPEC 983–984).

Reconciliations: none. Unreachable: none. Counts: 9 hops; 54,882 bytes; 0; 0.

### B

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README, task row "Diagnose intake and select lawful re-entry" | 41 | names SPEC intake, classification/treatment, TICKET carrier rule, frame TRIAGE_CARRIER |
| 1 | SPEC_METHOD Change Management Rule / Universal Intake Triage | 1381–1479 | named |
| 2 | SPEC_METHOD Computed Classification And Treatment | 1525–1624 | named |
| 3 | TICKET_METHOD Work-Carrier-To-Execution Rule | 723–806 | named |
| 4 | frames/TRIAGE_CARRIER header and `Source:` list | 1–70 | named; its sources name Upward Propagation Check |
| 5 | TICKET_METHOD Upward Propagation Check; Triage Metadata | 690–722 | frame source line |
| 6 | SPEC_METHOD Constitutional Chain | 1090–1163 | intake names "re-entry point into the constitutional chain" |
| 7 | SPEC_METHOD Trace Closure And Anti-Drift Rule | 2984–3052 | chain: "This member chooses ... trace-closure rules" (1097–1098) |

Decisions
- Must: "Intake triage must determine" six items (1403–1412); "The classification distinguishes a defective realisation, inadequate requirement or design, inaccurate prediction and insufficient observation" (1421–1423).
- Kind: constitutional gap/drift: "If a realization patch is treated as closing a real use-case gap whose required meaning is absent from current requirements, the governing gap remains unresolved" (3040–3042).
- Layer and downstream: "`requirement_reprice`: constitutional truth changes while project direction remains stable; re-enters at Requirements and flows through Design, Realisation, and Evidence" (1469); "actual requirement insufficiency re-enters its owner" (TICKET 700–701).
- No new goal: "A constitutional gap changes the meaning at that layer and its affected downstream span; it does not by itself require new Goals or Intent" (1136–1138); "missing requirement meaning does not establish a direction or scope change" (3044–3045).
- Code patch alone: `realization_refactor` "must prove no upstream drift" (1472); "Re-enter the actual governing owner when ... an applicable assessment establishes governing insufficiency" (1596–1599).
- Who decides: "Computed treatment owns the decision whether the candidate or its governing relation needs correction" (1450–1451); "F6 leaves any change to the relation's owner" (1439); ticket records the four triage fields (TICKET 718–722).
- Unresolved: "a report that cannot distinguish implementation failure from missing requirement meaning leaves that distinction unresolved" (1440–1442); J/O residuals (1600–1601).
- Corroborating, not counted: Method §"When a real use case reveals a gap": "a requirement-level gap with stable direction re-enters at Requirements" (3449–3450).

Reconciliations: none. Unreachable: none. Counts: 8 hops; 43,198 bytes; 0; 0.

### Grades
Expected: four-cause diagnosis routed to the affected owner; `requirement_reprice` re-enters at Requirements and flows through Design, Code, Evidence; code patch alone leaves the gap open; no new Goals/Intent from the gap alone. The test manager's reading applies the quoted sources correctly.
- A: **delivered** — SPEC 848–851, 886, 611–614; TICKETS 512, 515.
- B: **delivered** — SPEC 1421–1425, 1469, 1136–1138, 3040–3045; TICKET 700–701.

---

## S7 — Requirements realised entirely as a human process

### A

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README row "realise a product's WHAT as a build tenant, with a technology stack, a human process or both" | 22 | names SPEC §11, PRODUCT_DEFINITION §8 |
| 1 | SPEC_METHOD §11 Build-tenant binding | 1782–1976 | named |
| 2 | PRODUCT_DEFINITION §8 WHAT, HOW and work carriers | 740–785 | named |
| 3 | EVALUATION §6 Conformance of realisations | 386–483 | §11 rule 4: "Conformance is judged under EVALUATION §6" |
| 4 | SPEC_METHOD §2 Constitutional chain | 213–280 | §11 rule 1 cites §2; chain owns Code/Events/Projection |
| 5 | frames/binding.md header | 1–12 | README frame table: "software tenant and a human-process tenant ... conformance predicate" |

Decisions
- Examine: the tenant's "calculus binding, from the requirements calculus to its computational calculus, and its execution binding, from that computational calculus to its execution environment" (1806–1809); rule 3 content: operations "with its inputs, outputs, effects and outcome values", composition laws, resource measures, "operational assumptions on which conformance depends" (1871–1882); rule 4 evidence: "how the bound realisation satisfies the required meaning and constraints, including the applicable authority, independence, failure and recovery conditions" (1903–1906); conformance = "interpreted behaviour satisfies Σ under a declared interpretation contract (P1) and an independent judgment (P6)" (EVAL 388–390), as a conjunction "with the obligations of the requirements calculus as its required coverage" (1911–1912).
- Executor kind: "The obligations of the requirements calculus decide fitness; the kind of executor alone neither accepts nor rejects a realisation" (1900–1902).
- Code/event history: "code, an event stream or reconstruction from a complete history is required only where the governing obligations or the selected execution binding require it" (1813–1815); "an adequate human process using current records and direct observation is a permitted execution binding of a generic procedure that requires none of them" (1815–1818); chain: "no product owes a code base or an event store that its binding does not select" (251–252).
- Prohibited: a plan that "merges two required independent assessments, or substitutes an automated result for a required human decision" makes conformance `falsified` (1913–1918).
- Who decides: the independent assessor on the obligations; the tenant "owns its binding, its realisation and their evidence" (1861–1862).

Reconciliations: none — the chain's "Every link is load-bearing" is resolved in place by "Load-bearing means owned, not software" (248–249). Unreachable: none. Counts: 5 hops; 54,668 bytes; 0; 0.

### B

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README owners row "Constitutional WHAT and lawful construction → Spec Method"; task row "Assess whether lawful work meets the required outcome" | 71, 44 | no task row names build-tenant realisation |
| 1 | SPEC_METHOD head: Method Families, Canonical Compression, Position | 1–120 | member entry; row 2 names WHAT/HOW, Design Rule, Reconstruction Litmus; row 4 names Method |
| 2 | SPEC_METHOD WHAT, HOW, And Work Carriers | 902–965 | Method Families row 2 |
| 3–4 | SPEC_METHOD Reconstruction Litmus; Design Rule | 2889–2947 | row 2 |
| 5 | SPEC_METHOD Constitutional Chain | 1090–1163 | row 1 |
| 6 | SPEC_METHOD Method | 3376–3459 | row 4 (I located it by grep first; route confirmed) |
| 7 | SPEC_METHOD Verification Layers | 2622–2646 | member TOC only |
| 8 | SPEC_METHOD Operational Lifecycle Sufficiency | 1332–1380 | member TOC only |
| 9–10 | SPEC_METHOD Test Authority; Scenario Bundle | 2786–2823 | member TOC only |
| 11 | FOUNDATIONS Bounded construction | 961–1064 | README task row |
| 12 | FOUNDATIONS Assertions and observations; Parallel assurance | 679–782 | README task row |

Decisions
- Examine: the tenant's design supplies "which operations realise those requirements, how they compose, which actors or mechanisms perform them, what effects they permit, the operational assumptions" (913–916); "each affected requirement identifies its realising operation or invariant, the preservation obligation at its interfaces, and the evidence capable of defeating the claimed realisation" (929–931); "The binding preserves applicable authority, required human decisions, independence, failure and recovery conditions; a convenient execution environment cannot weaken them" (932–934); "Every live requirement must have written testcase authority" (2788).
- Executor kind: "The binding may use software, hardware, people, organisations or a mixture" (917–918); "Changing the executor or notation alone neither defeats nor establishes that relation" (52); "a folder, software stack or graph runtime is not required by these premises" (52); "A requirement-to-operation route alone does not discharge preservation or demonstrate fitness" (941–942).
- Code/event history: "a performed human procedure is another case" (1119); "Events are a durable carrier where selected" (1121); projection "does not require every consumer to replay a complete event stream" (1123–1124); "Code is the software case of this step" (3407); "Events, projection and delta are used where that binding selects them; adequate direct observation remains available" (3410–3411).
- Who decides: assessor under Independent assessment where required (FOUNDATIONS 276–303); "Spec owns the requirement-to-realization binding ... The tenant owns its calculus, environment and material resource measures" (52).

Reconciliations: none that decide differently; but the Method Families table disclaims force ("Each linked consumer owns its detailed conditions, exceptions and modal force", 45–46), so the actor must confirm the owner sections carry the rule — they do (917–918, 1119–1124, 3407–3411). Unreachable: none. Counts: 12 hops; 61,693 bytes; 0; 0.

### Grades
Expected: tenant supplies calculus, execution binding and conformance evidence; common requirements decide fitness; executor kind alone neither rejects nor accepts; generic procedures permit an adequate human process using current records and direct observation without code or complete event-history replay.
- A: **delivered** — SPEC 1806–1818, 1900–1906 state all three parts in one section.
- B: **delivered**, with a cost caveat — all three parts are decided on-route (913–934, 52, 1119–1124, 3407–3411), but spread over the member head table, WHAT/HOW, Constitutional Chain and the "Method" procedure list, which the family table files under the classification/renewal/ADR row; the README has no task row for this situation.

---

## S8 — Parity bit as the only observation

### A

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README row "prove a realisation" | 25 | names EVALUATION §1–2, §6, ASSURANCE |
| 1–2 | EVALUATION §1 Claims (with family table); §2 Separation | 11–177 | named |
| 3 | FOUNDATIONS §4 Assertions and observation | 1230–1301 | EVALUATION §1 names it (118–121) |
| 4 | FOUNDATIONS §4 Assurance relations (family table) | 1131–1176 | heading over Assertions; row 4 "observation sufficiency" |
| 5 | FOUNDATIONS §4 Results | 790–1007 | README row "do a bounded piece of work"; `indeterminate` definition |
| 6 | ASSURANCE §11 Assurance subject acquisition | 680–714 | documents table names "11 ..."; restates the rule |

Decisions
- Condition for a sound complete decision: "A checker that always decides `q_t` correctly from π alone requires: ... π(s) = π(s') implies q_t(s) = q_t(s')" (1283–1288).
- Otherwise "further evidence, a justified narrower scope or an indeterminate judgment is required" (1292–1293).
- Soundness: "(π(s), sat) in T implies q_t(s). (π(s), fal) in T implies not q_t(s)" (1262–1264).
- Binding support: "an idealised π does not establish that the instrument, actor or execution acquired the required facts correctly" (1273–1275) — the authenticated bit supplies this.
- `indeterminate` = "the available admissible evidence cannot decide it" (795).
- ASSURANCE §11: where observation "cannot separate two admissible subjects on which the assessed predicate takes opposite truth values, the frame returns further evidence, a justified narrower scope or `indeterminate`" (690–694).
- Application: parity bit — equal observations never carry opposite evenness, so sound `satisfied`/`falsified` is permitted; constant observation — condition fails, so acquire, narrow or return `indeterminate`.

Reconciliations: none. Unreachable: none. Counts: 6 hops; 125,941 bytes; 0; 0.

### B

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README rows "Assess whether lawful work meets the required outcome"; "Determine result values or combine required assessments" | 44–45 | name FOUNDATIONS assertions/observations, bounded construction, provenance, result algebra, conjunction |
| 1 | FOUNDATIONS Assertions and observations; Parallel assurance | 679–782 | named |
| 2 | FOUNDATIONS Result algebra | 365–495 | named |
| 3 | FOUNDATIONS Result conjunction | 496–623 | named |
| 4 | FOUNDATIONS Bounded construction | 961–1064 | named |
| 5 | REFERENCE_FRAME_METHOD RF-003, RF-004 | 390–405 | README "Distribution and entry" |
| 6 | TRANSFORMATION_LIBRARY Contract application | 115–247 | named by RF-003 and intake |

Decisions
- "A checker claiming always to decide q_t correctly from pi alone requires: ... pi(s) = pi(s') implies q_t(s) = q_t(s')" (730–734).
- "If equally observed admissible cases disagree on q_t, acquire distinguishing evidence, justify a narrower scope, or return indeterminate on that attempted decision" (736–738).
- Soundness (705–709); "An idealised pi does not prove that an instrument or actor acquired the material facts correctly" (720–721).
- `indeterminate`: "The available admissible evidence does not decide the predicate" (389).
- "the limited observation is not permission to erase" independently admissible evidence (740–741).

Reconciliations: none. Unreachable: none. Counts: 7 hops; 49,742 bytes; 0; 0.

### Grades
Expected: the observation-sufficiency condition; parity bit sufficient for "even" given a supported binding; constant observation insufficient. The test manager's reading is a correct application.
- A: **delivered** — FOUNDATIONS 1283–1296, 1273–1275.
- B: **delivered** — FOUNDATIONS 730–741, 720–721.

---

## S9 — Broken decoder records 1; scenario reports failure

### A

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README row "prove a realisation" → ASSURANCE; documents table "12 counterexample localisation" | 25, 59 | |
| 1 | ASSURANCE §1 Verification layers | 38–78 | row: "ASSURANCE for verification layers" |
| 2 | ASSURANCE §11 | 680–714 | documents table |
| 3 | ASSURANCE §12 Counterexample localisation | 715–756 | §1 names it |
| 4–5 | FOUNDATIONS Assertions and observation; Parallel derivation | 1230–1356 | §1 names it |
| 6–7 | EVALUATION §1–2 | 11–177 | route row |
| 8 | ACTIVATION §1 Construction relation (Feedback and diagnosis) | 198–353 | §1 names it |
| 9 | SPEC_METHOD §4 Universal intake triage | 825–1019 | ACTIVATION names it |

Decisions
- "That report is an observation, so it shows that actual behaviour disagrees only where its observation binding is supported" (ASSURANCE 63–65).
- "The failure alone does not show whether the realisation, the governing claim, the scenario's expected outcome or its observation is wrong" (67–69).
- "An observed test pass remains an observation while the oracle's fidelity is unestablished ... a reported failure is treated the same way" (FOUNDATIONS 1266–1271).
- "disagreement requires diagnosis ... and does not identify the faulty party by itself. Assurance accounts for shared specifications, interpretations, tools, fixtures, observations" (1333–1338).
- A harness or "expected-value builder, proof script ... does not reconstruct a parallel owner state from raw payloads" (ASSURANCE 685–689).
- Cause location: "returned to its earliest supported causal frontier on the declared path" (717–718); forms include "unresolved alternative frontiers, when the evidence supports several possible causal explanations but cannot establish which occurred" (730–732) and `indeterminate` (733–734).
- Four causes incl. "insufficient observation" (ACTIVATION 288–291); "a frame planned and not applied leaves its diagnosis open, never ruled out" (SPEC 868–869).
- Prohibited: a frontier "does not itself authorise ... compatibility repair" (751–753).
- Unresolved: realisation vs expected outcome (assertion provenance) vs observation (execution provenance) until the decoder is checked.

Reconciliations: none. Unreachable: none. Counts: 9 hops; 100,071 bytes; 0; 0.

### B

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README row "Assess whether lawful work meets the required outcome" | 44 | |
| 1 | FOUNDATIONS Assertions and observations; Parallel assurance and provenance | 679–782 | named |
| 2 | FOUNDATIONS Bounded construction | 961–1064 | named |
| 3 | SPEC_METHOD Universal Intake Triage | 1381–1479 | bounded construction names Spec intake |
| 4 | SPEC_METHOD Counterexample Localization | 1480–1524 | intake names "causal localization" |
| 5 | SPEC_METHOD head | 1–120 | owners table → member |
| 6 | SPEC_METHOD Verification Layers | 2622–2646 | member TOC only |

Decisions
- "A reported pass or failure is an observation until the applicable oracle and observation justification support the claimed conclusion" (723–724); "Insufficient evidence is not a failure of the predicate" (726).
- "An idealised pi does not prove that an instrument or actor acquired the material facts correctly" (720–721).
- "the failure alone does not distinguish a realization defect, inadequate governing meaning, inaccurate prediction or an inadequate scenario, oracle or observation" (2637–2639).
- "disagreement requires diagnosis and does not identify the faulty party by itself. Account for material shared specifications, interpretations, tools, fixtures, observations" (765–768).
- "Preserve unresolved alternatives; the next useful action may acquire evidence rather than repair" (1019–1020).
- Localization to the "earliest supported causal frontier on the declared path" (1490–1491), forms 1495–1503; "Satisfaction of localization never overwrites the original counterexample's result or establishes repair success" (1517–1518).
- Execution provenance: "the actual checker, exact subject, applicable environment, inputs, acquired observations and result" (753–754).

Reconciliations: none. Unreachable: none. Counts: 7 hops; 47,305 bytes; 0; 0.

### Grades
Expected: a reported failure is an observation while oracle fidelity is unestablished; the binding needs support; diagnosis locates the cause among realisation, expected outcome and observation. The test manager's reading is correct.
- A: **delivered** — ASSURANCE 63–71; FOUNDATIONS 1266–1275; ASSURANCE §12.
- B: **delivered** — FOUNDATIONS 720–727, 765–768; SPEC 2637–2639, 1489–1518.

---

## S10 — Superseded claim with no owner decision on the replacement

### A

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README row "decide acceptance or release"; also 77–88, 118–120 | 32 | names EVALUATION §5, SPEC §6, RELEASE §8, §9 |
| 1 | EVALUATION §5 Acceptance; When a finding blocks promotion | 310–385 | named |
| 2 | SPEC_METHOD §6 Lineage and release | 1248–1317 | named |
| 3 | RELEASE §8 Acceptance | 624–666 | named |
| 4 | RELEASE §9 Successor baseline conservation | 667–732 | named |

Decisions
- "superseded: an accepted successor relation replaces it" (RELEASE 676); "An unresolved disposition blocks qualification of the affected claim" (690).
- "A claim whose disposition is unresolved cannot be qualified and so cannot be accepted" (EVAL 332–334).
- "a reviewer result is an input to closure, never the closure" (316–317); "Acceptance is the decision owner's disposition over an unchanged subject" (312).
- RC: "the intended release scope and successor relation are stable" (632); "the human Product authority accepted the exact immutable RC identity" (636–637).
- Owner: "An intentionally removed disposition is a decision of the current Product authority" (335–336); README: "pending the product owner's acceptance of their proposed supersession" (119–120); "a route is not a disposition" (80–81).
- "a recorded disposition establishes nothing until it is evaluated, so no disposition stands as a result" (RELEASE 713–715); "a change a proxy cannot make re-enters at its owning relation" (325–326).
- Decision: member not acceptable, RC not publishable as accepted, Product authority decides; the reviewer's support is evidence.

Reconciliations: none. Unreachable: none — but `frames/acceptance-release.md` and `frames/member-build-assess.md` exist for exactly this task and are absent from the README frame table (100–111), so they are not reachable from the entry. Counts: 4 hops; 42,543 bytes; 0; 0.

### B

Route

| Hop | File §Section | Lines | Why |
|---|---|---|---|
| 0 | README row "Assess a candidate and apply its authorised disposition"; owners row "Exact cuts, successor conservation ... → Release Method" | 46, 79 | |
| 1–2 | SPEC_METHOD Construction, Assessment, And Delegation; Proportional Disposition | 1894–1984 | named |
| 3–4 | FOUNDATIONS Judgment and authority; Independent assessment | 230–303 | named |
| 5 | TRANSFORMATION_LIBRARY Dispose | 373–403 | Proportional Disposition names it |
| 6–8 | RELEASE_METHOD Acceptance Criteria; External deps; Successor Baseline Conservation | 607–702 | Dispose names UP-015; owners table |
| 9 | FOUNDATIONS Change impact and evidence retention | 833–898 | frame source lines (MEMBER_CONSTRUCTION_ASSESSMENT, RELEASE_ADOPTION) |
| 10 | TRANSFORMATION_LIBRARY Contract application | 115–247 | Proportional Disposition names it |

Decisions
- "superseded — an accepted successor relation replaces it" (661); required decision relation: "actual acceptance of that successor relation by its governing authority, plus the bound disposition" (669).
- "unconfirmed authority, reason or decision is `indeterminate`" (686–687); "an actual additional obligation where named, not a decision manufactured by recording a row" (689–690); "An unresolved disposition blocks qualification of the affected claim" (692).
- RC: "the intended release scope and successor relation are stable" (612); "the human Product authority accepted the exact immutable RC identity" (616).
- Member: `accept` only if "the candidate closes its declared cone and preserves every affected governing relation" (1947); `reject` where it "leaves an undisposed competing truth path" (1952); a proxy "cannot change Product meaning, requirements, governing authority, or accepted design" (1907–1908); "This delegation does not weaken direct-human acceptance where Product or release law requires it" (1913–1915).
- "a successful judgment cannot mint, widen, transfer or reconstruct authority. Missing or ambiguous authority leaves the dependent act ungranted" (241–244).
- Reviewer: assessment "returns evidence and a proposed semantic disposition. Apply Dispose to the separate decision on that proposal" (1936–1939).

Reconciliations: none. Unreachable: none. Counts: 10 hops; 40,936 bytes; 0; 0.

### Grades
Expected: a reviewer's support does not accept a changed meaning; dependent acceptance waits for the owner's decision; a construction grant does not supply it.
- A: **delivered** — EVAL 316–317, 332–334; RELEASE 676, 690, 636–637.
- B: **delivered** — RELEASE_METHOD 669, 686–692, 616; SPEC 1907–1915; FOUNDATIONS 241–244.

---

## Summary table

| Scenario | A grade | A hops | A bytes | A rec. | A unreach. | B grade | B hops | B bytes | B rec. | B unreach. |
|---|---|---|---|---|---|---|---|---|---|---|
| S6 | delivered | 9 | 54,882 | 0 | 0 | delivered | 8 | 43,198 | 0 | 0 |
| S7 | delivered | 5 | 54,668 | 0 | 0 | delivered (dispersed) | 12 | 61,693 | 0 | 0 |
| S8 | delivered | 6 | 125,941 | 0 | 0 | delivered | 7 | 49,742 | 0 | 0 |
| S9 | delivered | 9 | 100,071 | 0 | 0 | delivered | 7 | 47,305 | 0 | 0 |
| S10 | delivered | 4 | 42,543 | 0 | 0 | delivered | 10 | 40,936 | 0 | 0 |
| Total | 5/5 | 33 | 378,105 | 0 | 0 | 5/5 | 44 | 242,874 | 0 | 0 |

---

## Overall answer

On these five situations both corpora decide the same way and in line with the expected distinctions; neither misled on substance, and I found no intra-candidate passages deciding a point differently. The difference is in how an uninformed actor reaches the deciding clause and what it pays.

Candidate A's README routes are task-shaped: S6, S7 and S10 each have a row that names the exact deciding sections, so the first hop lands on the rule, and the rules are stated once, in tables an actor can apply mechanically (change-class table, upward-walk table, blocking table, §11's rules). A is more reliable for S7, where B has no task row and the decision is assembled from four places. A's cost is the tier-1 members: EVALUATION §1–2 (36KB) and FOUNDATIONS Results (41KB) are mostly foundation-to-law tables and consumer lists, and the route names them wholesale, so S8 and S9 cost 2–2.5× B's. A would most likely mislead by its frame table, which omits two existing frames (`acceptance-release`, `member-build-assess`) and so hides the compact surface for S10; and by tempting the actor to read whole family tables where a paragraph decides.

Candidate B's README rows for evidence and result questions point straight at FOUNDATIONS, whose sections are short prose; S6, S8, S9 and S10 cost 41–50KB each. B would most likely mislead on realisation/binding questions (S7): the actor enters a 200KB SPEC_METHOD through the owners table, finds the human-process permission only in the "Method" procedure list filed under an unrelated family row, and must trust a family table that disclaims its own modal force. Verification Layers (S9) is reachable only through the member's heading list.

Net: B lets the actor act correctly at lower acquisition cost on four of five; A is the more reliable guide where the question concerns the build-tenant binding, and its routes are more precise everywhere, at roughly 1.5× the bytes.

---

## Limits

- Tool calls used: 42 of 140 (two were reads of my own persisted command output; two were a failed and repeated grep).
- Read only under the packet directory; no git; no writes. Two command outputs exceeded the display limit and were read from the harness's saved tool-result files (my own output, not corpus content).
- Heading maps (`grep -n '^#'`) were used to resolve section line ranges in both candidates; this is equivalent to reading a member's table of contents and is not counted in bytes. For B, three sections (Verification Layers, Lifecycle Sufficiency, Test Authority/Scenario Bundle) were reached only this way after entering SPEC_METHOD through the owners table; I treated that as on-route and applied the same standard to A's ASSURANCE §1.
- Departure: for S7/B, I located the "Method" section by grep before confirming that Method Families row 4 names it; I then counted it as on-route. For S6/B, the Method section was not counted though it corroborates.
- Not read: `A/a_c/i3/README.md`, `B/interpretation/FRAMES.md`, B's frame bodies beyond headers and `Source:` lines, A's frame bodies beyond headers; no route in S6–S10 required them. B's root `README.md` and `interpretation/README.md` were read for context only.
- Bytes for EVALUATION §1–2 and FOUNDATIONS Results (A) are full-section reads as the README route names them; an actor stopping at the prose would pay less, but the route does not say where to stop.
- S1–S5 were not traced.