# C3 Cross-Synthesis Plan, Claude Line

This plan covers steps 2 to 6 of the
[cross-synthesis proposal](../../../../.ai-workspace/comments/claude/20261013T174341Z_STRATEGY_cross_synthesis_rebuild.md).
Activation W1 (step 1, design re-entry) wrote it. It is a working plan for
the Executive, not acceptance. The design it applies is in
[design/](../../design/README.md): ownership decisions D1 to D8 in
[DOCUMENT_STRUCTURE](../../design/DOCUMENT_STRUCTURE.md#ownership-decisions),
the tenant's binding in [CONSTRUCTION_BINDING](../../design/CONSTRUCTION_BINDING.md),
and the ports in [CROSS_SYNTHESIS](../../design/CROSS_SYNTHESIS.md).

Basis: the snapshot in the [ledger](LEDGER.md#basis), including the inward
merge of `a7eba66` at `923c755`. The conformance table now has 31
discriminators. The independent expectations in [EXPECTATIONS](EXPECTATIONS.md)
are the oracle cited below by ID (E-…, N-…, PT-…).

Line numbers are those of the candidate at `31f28f9` (the tenant tree is
unchanged on this branch except `design/` and `qualification/C3-SYNTHESIS/`).

## Verified gap list

"Proposal" names the item in the proposal's section "Where the Claude
candidate stands". Each row was checked by reading or by grep on
2026-10-14.

| # | Obligation | Finding | Evidence | Against the proposal | Closed by |
|---|---|---|---|---|---|
| G1 | Build-tenant binding | No member states a computational calculus, an execution environment, or the distinction between author, actor and operation kind. SPEC_METHOD treats a stack only as a design choice; PRODUCT_DEFINITION §8 defines build tenancy as a registry of realisations. | grep of all 23 members: no hit for "computational calculus", "execution environment", "execution binding" or "human process"; "actor identity" occurs only in authority law (`IDENTITY.md:149–163`, `REFERENCE_FRAME.md:172`) and "operation kind" only in the traversal effect relation (`TRAVERSAL_OCCURRENCE.md:501`); `SPEC_METHOD.md:378–392`; `PRODUCT_DEFINITION.md:576–600` | confirmed; the tenant's own binding is now [CONSTRUCTION_BINDING](../../design/CONSTRUCTION_BINDING.md) | B1, B4 |
| G2 | Measurement, one owner (Bounded Transitions item 3) | Six loci, two of them in conflict: unconditional measurement before every read against measurement only where selected. No section separates context fit from adequate attention. | unconditional: `ACTIVATION.md:211–214`; selected: `REFERENCE_FRAME.md:140–141`, `:336–340`, `ACTIVATION.md:59–60`, `:654–663`; reconstruction cost: `EVALUATION.md:351–360`; grep "actual use", "adequate attention": no hit | corrected: more than two owners | A4b, A2, A3 |
| G3 | Results and their combination, one owner (single result algebra items 1 and 6) | Two loci claim the algebra and three decide combination; conjunction is not defined once over the core, since each composite declares its own rule. | `FOUNDATIONS.md:3–5` claims the algebra; `ACTIVATION.md:6–8` says ACTIVATION adds no definitions, yet `:282–305` defines the values; combination at `FOUNDATIONS.md:343–349`, `ACTIVATION.md:367–371`, `REFERENCE_FRAME.md:391–404`, and the `conjoin` signature at `REFERENCE_FRAME.md:360–361` | answered: two owners for values, three for combination | A1 |
| G4 | Core content (items 2 to 5) | Non-performance merges with undecidability; the owner's own mapping is one-to-many and lives in a profile; availability maps to `satisfied`; effects have no refinement; ambiguity outcomes have no mapping. | `ACTIVATION.md:339–342`, `:349–350` and `EXECUTIVE_BASELINE.md:330–332` route `incomplete` to `indeterminate`; `ACTIVATION.md:378` maps four values "respectively" onto five, the actual mapping being `EXECUTIVE_BASELINE.md:325–335`; `re_entry_requested` maps to two values (`:333`); `ACTIVATION.md:380` "a policy state over a core result"; effect completion only at `TRAVERSAL_OCCURRENCE.md:800–801` | new | A1 |
| G5 | Every refined value maps to exactly one core value (item 2) | Unmapped or two-valued result vocabularies in seven members. | unmapped: `REFERENCE_FRAME.md:355` (`activation_refusal`), `:361` (`decision`, `conflict`, `indeterminate`), `:364` (`translated_value`, `declared_loss`, `refusal`); `ACTIVATION.md:242`; `EXECUTIVE_BASELINE.md:314`, `:340`, `:853`; `DESIGN_MODULE.md:1269` (`pass`, `fail`, `not_applicable`) and `:1300` (verdict `accepted`, an acceptance value); deferred: `AXIOMATIC_CALCULUS.md:782–788` (each traversal record declares its stop mapping); two-valued: `ODD.md:957–961` (`retry`, `repair`, `re-enter`, `block`), `TRAVERSAL_OCCURRENCE.md:797`, `:800`, `:801`; non-performance to `indeterminate`: `WORLD_MODEL.md:1082`. Checked and not defects: `EVALUATION.md:131–134` (triage payload classes declared non-results), `TICKETS.md:283–288` (close classifications consume results; reading A3 of the expectations), `TICKETS.md:477–479` (lifecycle states) | new | A3, B2, B3, B5, B6, B8 |
| G6 | Bounded transitions, configuration and the workspace (items 1, 4, 5) | No account of a current state A, a destination Z and transitions between them; a fixed three-role vocabulary in tiers 1 and 2; no generic configuration law; RF-009 omits communication; no rule that the workspace is the truth surface and an actor's context a disposable account. | grep "destination" in tier 1: no hit; refinement only at `ACTIVATION.md:433–459`; roles at `FOUNDATIONS.md:50`, `ACTIVATION.md:149–159`, `SPEC_METHOD.md:1390–1397`; project configuration only in the profile, `EXECUTIVE_BASELINE.md:1113–1137`; `REFERENCE_FRAME.md:197–203`; work state at `ACTIVATION.md:549–560` lacks item 5's first three sentences; the stale-summary rule exists only in the profile's failure table, `EXECUTIVE_BASELINE.md:1319` | new | A4a, A4b, A5a, B1, B2 |
| G7 | Relation 1, foundation to law | No family is laid out as premises, consequences and choices. Standing is already stated inline for each commitment, so the gap is the family tables and the explicit "adopted, not derived from finite capacity" discipline, not standing as such. | standing inline at `FOUNDATIONS.md:245`, `:267`, `:278`, `:286`, `:295`, `:302`, `:316`, `:327`; no family table in any member | confirmed, refined | A5b, wave B |
| G8 | Single ownership, other questions decided twice | (a) UP-015 dispositions restated with added rules in tier 1, which applies a tier-2 owner and names a person; (b) roles decided in three loci; (c) work-result readings decided in the profile, not the owner; (d) tier-1 import statements depend on the tier-2 cross-context law; (e) the "every clause names its principle" rule repeated. Checked and distinct: equivalence of concepts (`PRODUCT_DEFINITION.md:428–433`) against equivalence of realisations (`EVALUATION.md:184–188`). | (a) `FOUNDATIONS.md:9–28` against `RELEASE.md:579–609`, name at `FOUNDATIONS.md:23`; (b) G6; (c) `ACTIVATION.md:376–378` against `EXECUTIVE_BASELINE.md:319–342`; (d) `REFERENCE_FRAME.md:77–87` relying on `PRODUCT_DEFINITION.md:412–443`; (e) `FOUNDATIONS.md:35–36`, `REFERENCE_FRAME.md:12–13`, `standards/README.md:74–77` | new | A5a, A3, B2, B4, D1 |
| G9 | Categorical demonstration standard | H1 is kept as a hypothesis with the functor obligation (items 1 and 4 in part). Missing: the categorical equivalence rung; licensing laws and approximate steps with an adequacy relation and an end-to-end bound for refinement and rewrite steps; an evidence class per claim. | `FOUNDATIONS.md:369–383`; `EVALUATION.md:184–188`; `ACTIVATION.md:433–459` (exact refinement only); grep: no hit for "evidence class" or "end-to-end bound", and "licens" occurs only in unrelated senses (`DESIGN_MODULE.md:575`, `TRAVERSAL_OCCURRENCE.md:856`) | new | A2, A4b, A5b |
| G10 | 31 discriminators (criterion 5) | CONFORMANCE says every common discriminator is covered by a case. Its 22 cases were built against the earlier 10; the 21 later rows (single ownership, result values, functor claims, binding, peer configuration, stale summary and others) have none. | `CONFORMANCE.md:63–65`; cases C-01 to C-12, T-01 to T-08, R-01, R-02 | new | B9, C3, C5 |
| G11 | Public entry | The "load it into a model's context" route points to set-4 while set-6 is current; the "resume" route ships a qualification case's expectations to the actor; the a_c README lists only up to set-3. | `standards/README.md:42`; `:28`; `a_c/README.md` | confirmed, extended | D1 |
| G12 | Stale frame projection | set-6 binds TRAVERSAL_OCCURRENCE at `79f75845…`; the current member is `2e97d78a…`. The other 22 members match their bound digests (script check). Materialised frames run from 38 to 95 KB. | `a_c/set-6/README.md:51`, `:120–135` | confirmed | C1, C4 (verbatim frames replace them) |
| G13 | Eleven unresolved rows | Ten compression-group rows (the compressions README, eight compressed summaries and `stdo_bootstrap.md`) and `templates/PRODUCT_DEFINITION_TEMPLATE.json`, whose entrypoint is the placeholder `a_c/REPLACE_WITH_SET/frames/bootstrap-PENDING-RULING`. | `frontier/PREDECESSOR_CLAIMS.md:797–806`, `:813` | corrected: the eleventh row is the template, not the bootstrap file | D1, D3 after the ruling |
| G14 | Standalone use (relation 3) | Three members link into this source project's common specification, which a released corpus does not carry; SPEC_METHOD §11 imports this source project's local development law into the method. | `SPEC_METHOD.md:1465–1478`, `CONFORMANCE.md:63`, `AXIOMATIC_CALCULUS.md:1056` | new | B1, B8, B9 |
| G15 | Naming | A person is named where the writing standard requires "the product owner". | `FOUNDATIONS.md:23`, `standards/README.md:144`, frontier header lines 5 and 13 and rows 797–806, 813 | new | A5a, A7, D1 |
| G16 | On record, not re-verified here | carrier-retention case lacks a write grant (Codex cross-assessment, lines 216, 242–246, 301); unsupported approval gate in both resume runs; criterion 4 not established for REFERENCE_FRAME, AXIOMATIC_CALCULUS, EXECUTIVE_BASELINE, DESIGN_MODULE and TRAVERSAL_OCCURRENCE ([T-002-CLAUDE](../../../../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md) entries 2026-10-12T11:21:23Z and T15:43:36Z); all first-pass acceptances same-family and reopened (entry T14:24:16Z) | as cited | confirmed from the record | C3 to C7 |

Two of Codex's findings on the common specification are resolved by
`a7eba66`: the C3 Outcome now requires a locus only for `conserved` and
`superseded` rows, and `stdo_3.json` routes to the Codex candidate's
`successor/` directory.

## Material families for relation 1

A material family is a group of related rules that decide outcomes that
matter to the product. Relation 1 requires each to show its premises, the
consequences that follow, and its added choices with their owners, and
requires every member to be accounted for. The candidate has 21 families,
not the proposal's "about fourteen": each of the six profiles rests on
its own added choices and needs its own table.

**Where the tables live.** Each table sits in its owning member, at the
section where an actor enters the family (decision D5). Reason: relation 2
requires shared contracts to be used where actors apply them, and a table
at the entry section is inside the frame that actor is started on. A
central table in FOUNDATIONS would be a cross-reference only, and would
make FOUNDATIONS a second owner of each family's choices. FOUNDATIONS §3
"Foundation to law" holds the table format and a non-deciding index of the
families below.

| ID | Family | Main premises | Table location (entry section) | Accounts for |
|---|---|---|---|---|
| F1 | Frames and context | P0, P5, P1, P6 | REFERENCE_FRAME §1 | REFERENCE_FRAME; ACTIVATION §2 |
| F2 | Transitions, steps and configuration | P0, P2, P4a, P6 | ACTIVATION §1 | ACTIVATION §1, §4 |
| F3 | Results and their combination | P5, P6, P4b | FOUNDATIONS §4 Results | FOUNDATIONS §4; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 |
| F4 | Work state, resumption and reuse | P0, P3, P4b, P5 | ACTIVATION §5 | ACTIVATION §5, §7 |
| F5 | Proportionality and cost | P0, P2 | ACTIVATION §6 | ACTIVATION §6; SPEC_METHOD §8 delivery priority |
| F6 | Claims, evidence, assessment and acceptance | P6, P1 | EVALUATION §1 | EVALUATION §1 to §5 |
| F7 | Conformance, equivalence and qualification | P1, P6, P0 | EVALUATION §6 | EVALUATION §6, §7; CONFORMANCE |
| F8 | Identity | P3, P6 | IDENTITY §1 | IDENTITY |
| F9 | The a_c calculus | P1, P3, P4a, P6 | AXIOMATIC_CALCULUS §1 | AXIOMATIC_CALCULUS |
| F10 | Constitutional chain, outcome and build-tenant binding | P2, P1, P6 | SPEC_METHOD §2 | SPEC_METHOD §1 to §3, §6, §9 to §11 |
| F11 | Change management and ambiguity | P4b, P2, P5, P6 | SPEC_METHOD §4 | SPEC_METHOD §4, §5, §7 |
| F12 | Binding a project to the method | P3, P1, P6 | PRODUCT_DEFINITION §1 | PRODUCT_DEFINITION |
| F13 | Work carriers | P6, P4b, P2 | TICKETS §5 | TICKETS |
| F14 | Assurance and testing | P6, P1, P5 | ASSURANCE §1 | ASSURANCE |
| F15 | Release and successor conservation | P3, P6, P4b | RELEASE §1 | RELEASE |
| F16 | Executive engagement (operational profile) | imports F1 to F4, F6 | EXECUTIVE_BASELINE §3 | EXECUTIVE_BASELINE |
| F17 | Software design | imports F2, F3, F6, F10 | DESIGN_MODULE §1 | DESIGN_MODULE |
| F18 | Outcome-driven development | imports F2 to F4, F9 | ODD §1 | ODD |
| F19 | Traversal occurrence | imports F3, F9 | TRAVERSAL_OCCURRENCE, Position | TRAVERSAL_OCCURRENCE |
| F20 | UX | imports F2, F3, F4 | UX §1 | UX |
| F21 | World model | imports F3, F8, F9 | WORLD_MODEL §1 | WORLD_MODEL |

Members with no family table, each with its reason, are listed in the same
index: FOUNDATIONS §1 to §3 state the premises themselves; PROFILES §1
owns the import rule that every profile table cites in its premise column;
POSTING_GUIDE and WRITING_GUIDE own conventions, which are policy choices
whose owner is the guide; GLOSSARY decides nothing; the standards README
and the other packaging own no determination.

## Re-proof span

**Rule.** The span is every frontier row whose text a later step changes,
plus every row that depends on a section whose content or ownership
changes, even when the row's own text does not change. Criterion 2 (the
claim-by-claim source comparison) is redone for every row in the span.

**What the span does not do.** It bounds re-work. It does not narrow
acceptance: under [ledger default 2](LEDGER.md#defaults-taken-for-the-open-decisions)
no first-pass judgment counts toward acceptance, so every row still needs
cross-family criterion 2. Outside the span, a first-pass judgment is kept
as evidence once its applicability is checked.

**Sections whose text changes.**

- Step 2: FOUNDATIONS, every section; ACTIVATION, every section;
  REFERENCE_FRAME §1, RF-002, RF-009, RF-012, §4 Frame-set selection, §5,
  §6 Result conjunction, §13 Minimal evaluation result, §15; EVALUATION §3,
  §4, §6, §7, §8.
- Steps 3 and 4: SPEC_METHOD §5, §8, §11, §12; PRODUCT_DEFINITION §5, §8;
  TICKETS §3; RELEASE §9; AXIOMATIC_CALCULUS §4 (AC-007), §5; ASSURANCE
  sections citing core results (§7, §13); EXECUTIVE_BASELINE §5 Work
  result, §7, §12 steps 3 to 7, §16, §17, §19; DESIGN_MODULE §7 Cross-view
  axiom evaluation and Gate and retrospective work, §10; ODD §11.5D;
  TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds;
  UX §15; WORLD_MODEL §14; PROFILES §1; CONFORMANCE. Family tables are new
  subsections and put no row in the span unless a table exposes a defect.
- Step 6: the standards README, the templates and plugin files on the
  bootstrap route, and the eleven unresolved rows.

**Sections whose ownership or content others depend on.** The owners of
results (today ACTIVATION §3), of conjunction (FOUNDATIONS §4,
REFERENCE_FRAME §6) and of measurement (ACTIVATION §2 and §6, RF-002).
Every row whose locus section refers to one of them is in the span.

**Estimate.** About 114 rows by text change, located in the sections
listed above, and about 40 more by dependency only: about 154 of 691 rows.
Method: each row's successor locus was matched against the section list,
and each locus section was scanned for references to the changed owners
(two scans, by leaf section and by section with its subsections, gave 124
to 135 rows that depend on those owners). The scan ran from an uncommitted
scratch script, and it is a lower bound, because implicit dependencies are
not matched. By predecessor member: REFERENCE_FRAME_METHOD 39,
STDO_REFERENCE_FRAME_BASELINE 37, SPEC_METHOD 19, DESIGN_MODULE_METHOD 14,
non-body standards members 11, UX 9, WORLD_MODEL 8, AXIOMATIC_CALCULUS 7,
TICKET_METHOD 4, others 6. Activation A6 makes the exact list durable with
a committed script.

## Activations for steps 2 to 6

### Conventions for every activation

- **Shared files.** Every Writer writes its return to
  `qualification/C3-SYNTHESIS/returns/<ID>.md` and the frontier rows it
  changes to `qualification/C3-SYNTHESIS/deltas/<ID>.md` (anchor,
  disposition, locus, reason). Neither file is shared. Only the integration
  activations (A7, B10, D3) change `frontier/PREDECESSOR_CLAIMS.md` and
  `standards/GLOSSARY.md`; only B10 and D1 change `standards/README.md`.
- **Fixed interfaces.** So that concurrent activations can link to sections
  that another activation creates, these headings are fixed in advance:
  FOUNDATIONS §2 `### Imports between members`; FOUNDATIONS §3
  `### Foundation to law`; FOUNDATIONS §4 `### Results` and
  `### Conjunction of results`; ACTIVATION §1 `### Transitions` and
  `### Configuration` (the heading "Roles and delegation" stays);
  ACTIVATION §3 renamed `## 3. Step results and disposition`; ACTIVATION §5
  `### The workspace and an actor's account`; SPEC_METHOD
  `## 11. Build-tenant binding` replacing "Governance of tenants in this
  source project"; no sixth core value: non-performance is the absence
  of a closed result, kept apart by conjunction (D1);
  frames in `standards/frames/` with `standards/frames/FRAME_INPUTS.json`.
  Each activation re-points, in its own files, every link to
  `ACTIVATION.md#3-result-algebra`: to `FOUNDATIONS.md#results` where it
  means core values, otherwise to the renamed ACTIVATION §3.
- **Reviews.** Every Writer result is followed by a same-family Reviewer
  working check that records expectations from EXPECTATIONS before opening
  the subject. EXPECTATIONS is the oracle for these working checks only;
  cross-family acceptance reviews bring their own expectations. Writers may
  read it as an input. Reviewers count toward the limit of three concurrent
  activations. Every Reviewer also applies E-8-6, E-8-7 (criterion 2 for
  the activation's rows in the span), E-8-11 and E-8-13.
- **Size.** Each activation is sized for one fresh agent in about 45
  minutes or less; an activation that cannot finish returns `incomplete`
  with its committed progress, and the Executive splits it.

### Wave A: Foundations (step 2)

A1 runs first; it is at the 45-minute limit and is split if it returns
`incomplete`. A2 and A3 may run with it, because their links target the
fixed interfaces; their Reviewers run after A1 is committed. After A1, A4a
and A5a may run together, then A4b and A5b. A6 may run at any time after
A1.

| ID | Territory | Work | Inputs | Outputs | Reviewer checks |
|---|---|---|---|---|---|
| A1 | `standards/FOUNDATIONS.md`, `standards/ACTIVATION.md` | D1: move the core values (the five of RF-012) and conjunction into FOUNDATIONS §4 Results and Conjunction of results, with conjunction's three inputs, the standing relation and the no-raise rule; reduce ACTIVATION §3 to the step's refinements, each mapped once (construction availability with its grounds, disposition, ambiguity outcome, effects); fix the ownership statements at `FOUNDATIONS.md:3–5` and `ACTIVATION.md:3–8`; update source-disposition rows | single result algebra requirement; D1; G3, G4; `EXECUTIVE_BASELINE.md:319–342` read only; EXPECTATIONS §5 | the two members; return; delta | E-5-1 to E-5-9, E-4-1, E-4-3, E-4-6, N-2, N-7; RF-012's five values still govern every performed evaluation |
| A2 | `standards/EVALUATION.md` | port 4 into §6 (equivalence ladder); §7 owns actual-use evidence of adequate attention (D2); §3 states that a fresh context of the author is not independent; §4 points to FOUNDATIONS Results, and a planned evaluation that was not performed has no result (D1); §8 rows | CROSS_SYNTHESIS part 4; D2, D8; G2, G9 | member; return; delta | E-6-4, E-2-3, E-2-7, E-5-3, PT-1 to PT-10 |
| A3 | `standards/REFERENCE_FRAME.md` | RF-002 refers to ACTIVATION §2 (D2); RF-009 names communication; RF-012 and §6 Result conjunction refer to FOUNDATIONS §4; §1 statement of ownership becomes an import declaration (port 3, D7); §4 Frame-set selection refers for measurement; §5 maps `activation_refusal`, the `conjoin` and the `translate` outcomes, each to one core value; §15 rows | CROSS_SYNTHESIS part 3; D1, D2, D7; G2, G5, G6, G8(d) | member; return; delta | E-4-1, E-4-3, E-2-3, E-2-5, E-5-3, PT-1 to PT-10 |
| A4a | `standards/ACTIVATION.md` | D3: §1 Transitions (A to Z, discovery, destination change, completion and stops) and Configuration (allocation from operations, dependencies, capabilities and assurance; the three roles become examples); §8 rows for §1 | Bounded Transitions requirement items 1 and 4; D3; G6 | member; return; delta | E-2-1, E-2-4 to E-2-7, E-2-9, discriminator rows 10 to 16 (E-7-10 to E-7-16), N-3, N-8 |
| A4b | `standards/ACTIVATION.md` | D2: §2 step 3 owns the size measurement, and the conflicting sentences at `:59–60` and `:654–663` refer to it or to the binding; port 5's acquisition rule in §2; item 5 in §5 (workspace as truth surface, disposable context, reconciliation); D8 in §4 Refinement (licensing law, approximate steps with adequacy relation and end-to-end bound); §8 rows for §2, §4, §5, §6 | Bounded Transitions requirement items 2, 3 and 5; D2, D8; G2, G6, G9; CROSS_SYNTHESIS part 5 | member; return; delta | E-2-2, E-2-3, E-2-8, E-2-10 to E-2-12, E-6-2, E-6-3, discriminator rows 7, 8, 17 to 20 and 31 (E-7-7, E-7-8, E-7-17, E-7-18, E-7-31, E-7-19, E-7-30), N-4, N-13, N-14 |
| A5a | `standards/FOUNDATIONS.md` | D6: trim §1 to the vocabulary of standing, remove the corpus-specific application and the person's name; D7: §2 Imports between members; D3: the Actor row; §6 rows for §1 and §2 | D6, D7; G8(a), G8(d), G15 | member; return; delta | E-4-2, E-4-3, E-1-1, PT-1 to PT-10 for port 3's rule |
| A5b | `standards/FOUNDATIONS.md` | port 2: standing column in §3, using the four standing terms of §1; D5: §3 Foundation to law with the format (port 1) and the family index above; D8: §4 Formal fragment carries items 1, 4 and 5 and refers to EVALUATION §6; §6 rows for §3 and §4 | CROSS_SYNTHESIS parts 1 and 2; D5, D8; G7, G9 | member; return; delta | E-1-1, E-1-3, E-6-1, E-6-4, E-6-5, N-1, N-6, PT-1 to PT-10 |
| A6 | `qualification/C3-SYNTHESIS/span/` | commit a script that lists the span rows under the rule above, from the frontier copy and the section list; write `SPAN.md` | this plan; frontier copy; members after A1 | script; SPAN.md; return | re-run reproduces SPAN.md; ten rows spot-checked against their sections |
| A7 | `frontier/PREDECESSOR_CLAIMS.md`, `standards/GLOSSARY.md` | integration 1: apply the deltas of A1 to A5b; GLOSSARY rows for moved and new concepts; replace the person's name in the frontier header | deltas; members at their accepted commits | frontier; GLOSSARY; return | every delta applied exactly and nothing else changed (diff); every locus resolves (script) |

### Wave B: Foundation to law, Spec Method and profiles (steps 3 and 4)

Wave B starts after A7. Order: B1, B2 and B3 together; then B4, B5 and
B6; then B7, B8 and B9; then B10. Each activation also inserts its
families' tables (format from FOUNDATIONS §3) and re-points its own links.

| ID | Territory | Work | Reviewer checks |
|---|---|---|---|
| B1 | `standards/SPEC_METHOD.md` | D4: §11 Build-tenant binding (items 1 to 6), replacing the imported local development law; §8 refers to ACTIVATION §1 Configuration; §5 refers to ACTIVATION §3 for ambiguity outcomes; tables F10 (§2) and F11 (§4); §12 rows | E-3-1 to E-3-6, E-1-2, E-1-4, E-4-2, discriminator rows 23 to 26 (E-7-22 to E-7-25) |
| B2 | `standards/EXECUTIVE_BASELINE.md` | §5 Work result refers to ACTIVATION §3's mapping and keeps its readings as profile bindings mapped once; `activation_refusal` refers to REFERENCE_FRAME §5; §7 and §16 refer to ACTIVATION §1 Configuration; §17; §19 line 1283; table F16 (§3); §23 rows | E-5-3, E-5-4, E-5-6, E-2-4, E-2-6, discriminator rows 12 to 16 (E-7-12 to E-7-16), N-3, N-7 |
| B3 | `standards/ODD.md`, `standards/TRAVERSAL_OCCURRENCE.md` | each two-valued decision or stop kind split by its cause into refined values, each mapped once; tables F18 and F19 | E-5-3, E-5-4, E-5-5, E-1-2, E-8-4 |
| B4 | `standards/PRODUCT_DEFINITION.md`, `standards/TICKETS.md` | PRODUCT_DEFINITION §5 refines FOUNDATIONS §2 imports and maps its four relation kinds back; §8 refers to SPEC_METHOD §11; table F12 (§1); TICKETS table F13 (§5); TICKETS §3 close classifications refer to FOUNDATIONS Results | E-4-3, E-1-2, E-1-4, discriminator row 22 (E-7-21) |
| B5 | `standards/DESIGN_MODULE.md` | map `pass`, `fail` and `not_applicable` to the core; state the design verdict `accepted` as a decision that consumes results; §10 reference; table F17 (§1) | E-5-3, E-5-6, N-2, N-7 |
| B6 | `standards/UX.md`, `standards/WORLD_MODEL.md`, `standards/PROFILES.md` | UX §15 and WORLD_MODEL §14 mapped once, with `WORLD_MODEL.md:1082` restated under D1 (the unrun verification has no evaluation result; the step's `incomplete` maps as ACTIVATION §3 states, never to `indeterminate`); PROFILES §1 import rule; tables F20 and F21 | E-5-3, E-5-4, E-8-4 |
| B7 | `standards/ASSURANCE.md`, `standards/RELEASE.md` | core-result references re-pointed; RELEASE §9 lines 605–609 follow D6; tables F14 and F15 | E-1-2, E-8-8, E-4-1 |
| B8 | `standards/IDENTITY.md`, `standards/AXIOMATIC_CALCULUS.md` | AC-007 and §5 refer to FOUNDATIONS Results, with each traversal's stop mapping required to be exactly one; the link out at `:1056` restated; tables F8 and F9 | E-5-9, E-6-5, E-1-2, E-1-7 |
| B9 | `standards/CONFORMANCE.md` | map all 31 discriminators to a case or a logical-review check; correct `:63–65`; add case rows where actual use is needed (configuration, binding, stale summary); remove the link out of the corpus | E-8-10 (31 rows), E-7-1 to E-7-31 coverage complete |
| B10 | `frontier/PREDECESSOR_CLAIMS.md`, `standards/GLOSSARY.md`, `standards/README.md` | integration 2: apply the deltas of B1 to B9; GLOSSARY rows; README document map and links (routes wait for D1) | as A7 |

Inputs for each B activation: its members, the design decisions it
applies, the gaps it closes (gap list above), FOUNDATIONS §3 at its
accepted commit, and EXPECTATIONS. Outputs: its members, return and delta.

### Wave C: Frames and actual use (step 5)

Wave C starts after B10. C1, C2 and C3 run together; then C4 and C5; then
C6. Oracles are written before any run, by Writers that wrote none of the
members or frames under test.

| ID | Territory | Work | Reviewer checks |
|---|---|---|---|
| C1 | `qualification/instruments/generate_frames.py`, `standards/frames/` | port 5: the generator, the manifest and the frames for the F-01 and F-02 tasks, each with the result-algebra owner among its routes where its task returns a result | regeneration is byte-identical; each `Source:` line names its owner; E-4-4, E-5-8, E-8-12, PT-1 to PT-10 |
| C2 | `qualification/instruments/finite_oracle/` | port 6: the oracle template | the template's mutant is detected; PT-1 to PT-10 |
| C3 | `qualification/cases/C3S-01/` to `C3S-03/` | oracles for REFERENCE_FRAME, AXIOMATIC_CALCULUS and TRAVERSAL_OCCURRENCE tasks | expectations derive from sources only; no candidate wording in the oracle |
| C4 | `qualification/instruments/generate_frames.py`, `standards/frames/` | frames for the F-03 tasks, the bootstrap task and the new configuration, binding and stale-summary tasks | as C1 |
| C5 | `qualification/cases/C3S-04/` to `C3S-08/` | oracles for EXECUTIVE_BASELINE, DESIGN_MODULE, configuration, binding and the stale-summary discriminator (E-7-31) | as C3 |
| C6 | `qualification/runs/C3S-*/` | fresh-actor runs with `bounded_step.py` under declared limits; spend estimated USD 5 to 15 in total | context measured before start; no tools; run outside any repository; no oracle text in any input |

Assessment of the runs against the oracles is a Reviewer activation per
case, by an actor that wrote neither the frame nor the oracle.

### Wave D: Packaging (step 6)

Wave D starts after the product owner's ruling on the compressions
(ledger default 7). D1 and D2 run together; D3 follows.

| ID | Territory | Work | Reviewer checks |
|---|---|---|---|
| D1 | `standards/README.md`, `a_c/README.md`, `standards/templates/PRODUCT_DEFINITION_TEMPLATE.json`, `standards/templates/AGENTS_TEMPLATE.md`, `standards/templates/CLAUDE_TEMPLATE.md` | route the public entry to the verbatim frames; remove the case route (`README.md:28`) and the set-4 route (`:42`); set the bootstrap entrypoint under the ruling; state the corpus's standing (D6); replace the person's name (`:144`) | E-1-7, E-8-5, routes resolve; no qualification material on a public route |
| D2 | `plugins/spec/` | route each skill to its frames and owners; the `stdo-work` skill carries port 5's acquisition route | links resolve; each skill's owner citations match the members |
| D3 | `frontier/PREDECESSOR_CLAIMS.md`, `standards/GLOSSARY.md` | integration 3: dispose the eleven unresolved rows under the ruling; final link check; re-run A6's script | as A7; E-8-1, E-8-6 |

Step 7 (acceptance) follows and is outside this plan: criteria 1 to 6 per
member against all 31 discriminators, by cross-family Reviewers.

## Points for the product owner or the common pen

These are not changed by this plan.

1. Single result algebra item 3 keeps non-performance distinct from
   undecidability, while RF-012's five values have no member for
   non-performance. EXPECTATIONS ambiguity A2 reads either a separate core
   value or a carried domain outcome as lawful. Decision D1 takes a
   separate core value, because conjunction is defined over the core. The
   requirement could say which reading it intends.
2. The C3 Activation unit and Limits paragraphs require context measured in
   bytes before the actor reads. Subagent actors receive host-added context
   that a tenant cannot measure; only headless fresh actors measure their
   whole context ([CONSTRUCTION_BINDING](../../design/CONSTRUCTION_BINDING.md#resources-measured)).
   The contract could state which boundary it means.
3. "The Foundations own exactly one core result algebra" can be read as the
   tier or as a member. Decision D1 places the core in the FOUNDATIONS
   member, which satisfies both readings.
