# Claude Tenant Design: Document Structure

Status: tenant HOW for the Claude line's candidate, on branch
`tenant/claude/c3-synthesis`. Not common WHAT; not accepted. Builder:
`stdo://releases/v2.5.1-rc.2/`. Inputs: the common
[Intent](../../../specification/INTENT.md),
[Product](../../../specification/PRODUCT.md) (the C3 Construction Contract
and Cross-Synthesis),
[requirements](../../../specification/requirements/README.md),
[conformance discriminators](../../../specification/conformance/README.md),
the common [frontier](../../../specification/requirements/PREDECESSOR_CLAIMS.md)
and its [tenant copy](../frontier/PREDECESSOR_CLAIMS.md), at the snapshot
recorded in the [ledger](../qualification/C3-SYNTHESIS/LEDGER.md#basis).
Companion design files: [CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md)
(how this tenant builds) and [CROSS_SYNTHESIS](CROSS_SYNTHESIS.md) (parts
taken from the Codex candidate).

## Purpose

The candidate is the foundational axioms first, then every member of the
2.5.1-rc.2 release restated on them in this tenant's own text, usable with
the predecessor no longer in force. "Restated on the axioms" means the
three relations of the
[standalone successor requirement](../../../specification/requirements/README.md#standalone-successor-requirement):
foundation to law, ownership and use, and standalone conservation.
Unchanged predecessor wording is permitted in a clause where those
relations hold. A link to the predecessor is provenance; it never
satisfies a disposition.

The corpus is as large as its obligations require. No actor reads it
whole: each actor is started on a frame for its task (Activation unit,
below).

## Tiers and members

Files are under `standards/` unless a path says otherwise. What each tier
owes is fixed by the [C3 tier table](../../../specification/PRODUCT.md#c3-construction-contract);
the member split is this tenant's.

Identifiers carried from the previous release: `RF-nnn` are its numbered
reference-frame laws, `AC-nnn` its numbered a_c laws, and `UP-nnn`
(`STDO-UP-nnn` in full) its numbered method rules. Those named in this
file are UP-004, authority identity and conservation; UP-012, shared
method adoption and propagation; UP-013, product outcome conservation;
UP-014, proportional method and delivery; UP-015, successor baseline
conservation, which defines the disposition values; UP-020, agentic
construction execution; and UP-021, complete enclosing-relation
admission. STDO-SURFACE-001 is its rule of one constitutional surface and
version boundary.

### Tier 1, foundations

| Member | Owns |
|---|---|
| FOUNDATIONS.md | the vocabulary of standing; the ontology with the frame objects; P0 to P6 with a standing column; the foundation-to-law format, the standing of its consequences and the family index; the core result algebra and its conjunction; composition and conservation; the generic import rule; hypotheses; the authority kinds, with the one list of what creates no authority and the proxy limit (D9, R12); the pillar column of the family-table format and index |
| REFERENCE_FRAME.md | the frame as a first-class object: RF-001 to RF-017, frame sets, method functions, frames in conjunction (by reference to the core conjunction), coverage, revision, the activation packet |
| ACTIVATION.md | bounded work: transitions from current state to destination, the step, intake, admission, configuration, context construction and the size measurement, the step's result refinements and dispositions, totality and refinement, work state and resumption, proportionality and the generic resource-limit law, closed results and reuse; admission, which no result, tool output or handoff implies (R31); the generic staleness of derived surfaces (R23); recording a result without review (R12) |
| AXIOMATIC_CALCULUS.md | the a_c theory: signature, typed records, AC-001 to AC-020, functor kinds, interpretation, identity, conformance obligations, the use of an interpretation to build a task's constraint surface (§9, pillar 10) |
| IDENTITY.md | scoped identity, uniqueness, type, stability, hierarchy, authority split, UP-004, parsing, version boundary; boundaries and sufficiency claims (proposed, D9, pillar 2) |
| EVALUATION.md | claims, evidence, independent assessment, review results, acceptance, conformance and the equivalence ladder, qualification of frames and of the method, actual-use evidence of adequate attention; author identity (R11); when a finding blocks promotion (R25) |

### Tier 2, Spec Method

| Member | Owns |
|---|---|
| SPEC_METHOD.md | the particular method: constitutional chain, process constitution, requirement and design law, outcome conservation, change classes and re-entry, ambiguity governance, migration, UP-012, UP-013, the general law of build-tenant binding and its binding of the ACTIVATION §6 resource limits; the specification surface rule, including version labels (R32) |
| PRODUCT_DEFINITION.md | how one project binds to the method: overlay and layout independence, bounded-context resolution for a project's terms, STDO-SURFACE-001, bootstrap, build tenancy as a registry |
| TICKETS.md | work carriers: ticket and sprint model, layout, authority, triage-first intake, the closure condition (R14), independent-review triggers as a Spec Method policy (R11), migration, ticket shape |
| ASSURANCE.md | evidence rules, verification layers, testing taxonomy, test authority, scenario bundles, path coverage, trace closure, testing frames, counterexample localisation, module-derived unit tests |
| RELEASE.md | release identities, qualified refs, phases, immutable RC, exact-cut qualification, selector adoption, naming, cohorts, UP-015 |
| CONFORMANCE.md | the cases the method must pass, with independently specified expectations, mapped to the common discriminators |

### Tier 3, profiles

Each profile imports the tiers above and owns only its own bindings: the
terms and choices it adds, and the mapping of its result values into the
core result algebra.

| Member | Owns |
|---|---|
| PROFILES.md | the boundary: how a profile imports the tiers above, what stays out of the core, the index |
| EXECUTIVE_BASELINE.md | the operational profile restating STDO_REFERENCE_FRAME_BASELINE: profile terms, Executive attention and drift locks, the derived frames, the engagement transition, adoption and project configuration, failure classification |
| DESIGN_MODULE.md | the DESIGN_MODULE_METHOD realisation law: ontology-first design, Prime (the irreducible design relations, its Prime semantic atoms), carrier set, boundary evaluators, totality, effect edge, coupling |
| ODD.md, TRAVERSAL_OCCURRENCE.md, UX.md, WORLD_MODEL.md | each predecessor profile in full |

### Guides, route, packaging

POSTING_GUIDE.md and WRITING_GUIDE.md restate their predecessors.
POSTING_GUIDE owns the commentary layer: what a post is for, its
boundary, and when its content becomes consequential (D9, R33). Its
deciding rules are accounted under family F13 Work carriers through the
family index, since a guide has no family table of its own. TICKETS §1
refers to it for what a comment carries. WRITING_GUIDE owns writing
practice. It refers to SPEC_METHOD §2 for the specification surface rule
and its modal force, and does not restate that rule (R32). Templates and
schemas are derived authoring surfaces: each prose rule in a template
refers to its owner, and a value set used only in a template is either
adopted by an owner or replaced by the owner's values (R34).
GLOSSARY.md is the non-deciding locator index; its rows route to the
owning successor clause, never to rc.2. README.md carries the routes by
task, the document map and the layout, and owns no method determination.
Packaging mirrors the installed layout so the inventory comparison at a
release-candidate cut is mechanical.

## Ownership decisions

Each decision fixes one owning section for a question the base candidate
decides in more than one place, or adds an owner the common specification
requires. The evidence for each defect is in the
[verified gap list](../qualification/C3-SYNTHESIS/PLAN.md#verified-gap-list).
Line citations in D1 to D8 are to the members at the base,
`build_tenants/claude/` at `31f28f9`, before this rebuild's changes.
The corrections that Writer activation I3-2e added to D1, D2, D3, D4 and
D7, and D9, cite the iteration 3 preimage `5ab44d5`, as
[REDUCTION](REDUCTION.md) does.

**D1. Core result algebra and conjunction: FOUNDATIONS §4.** A new
subsection "Results" owns the core values, their meanings, the standing
relation, the rule that no refinement raises standing, and the rule that
a core value travels with the evaluated predicate and the original domain
outcome while the domain owner keeps the domain meaning (item 4 of the
[single result algebra requirement](../../../specification/requirements/README.md#single-result-algebra-requirement)).
A second new subsection, "Conjunction of results", owns conjunction and
composition of results. ACTIVATION §3 keeps the step's five refinements,
each mapped into the core:
- admission and activation;
- construction availability;
- disposition;
- ambiguity outcome;
- effects.

RF-012 in REFERENCE_FRAME §3 and REFERENCE_FRAME §6 Result conjunction
refer to the owner. AC-007 in AXIOMATIC_CALCULUS §4, EVALUATION §4 and
REFERENCE_FRAME §5 refine it, each with a map back to the owner, as
FOUNDATIONS §4 Results permits (`FOUNDATIONS.md:854`). None adds a core
value. (Corrected by I3-2e, [design discrepancy a](REDUCTION.md#design-discrepancies-found):
the earlier text listed four refinements and said these sections "define
nothing further".) Reason: the requirement
places the core in the Foundations and defines conjunction once over it.
At the base, `ACTIVATION.md:3–5` lists the result algebra among what
ACTIVATION owns, while `ACTIVATION.md:6–8` says ACTIVATION adds no
definitions and `FOUNDATIONS.md:3–5` says no later member adds any.
ACTIVATION is already tier 1, so the requirement alone does not force a
move. Placing the values and conjunction in FOUNDATIONS is this tenant's
choice: the core sits beside the commitments it rests on, and one section
ends both conflicts. The core must meet these constraints:

- the core keeps the five values of RF-012 (`satisfied`, `falsified`,
  `indeterminate`, `out_of_frame`, `invalid_basis`), so RF-012 stays
  `conserved`. An evaluation that was not performed has no closed result;
  it is never mapped to `indeterminate` or to any other core value;
- conjunction takes three inputs and keeps them apart: the core values
  returned; the planned assessments that have no closed result; and the
  required coverage that no planned assessment addresses. The second and
  third inputs are the conjunction's gaps, of two kinds: not performed and
  uncovered. A conjunction with a gap is never `satisfied`. Where every
  returned value is `satisfied` and a gap remains, the conjunction reports
  `indeterminate` as its own value for the composite predicate, because
  the results it holds cannot decide that predicate; this value is not a
  mapping of the assessment that was not performed. Where a mandatory
  returned value is not `satisfied`, the conjunction's declared rule
  chooses the reported value from the non-satisfied values returned. In
  both cases the record names each gap by kind, and every gap is carried
  with the composite through every join. The gap record keeps
  non-performance distinct from undecidability (item 3), and the core
  keeps five values;
- a work step's `incomplete` maps to `falsified` only for the predicate
  "a candidate is available", which travels with the value, and never to
  `indeterminate`. A Reviewer step that ends `incomplete` leaves each of its
  criteria not performed: no result, never `falsified`;
- the step's other work-result values and the dispositions map as
  ACTIVATION §3 states. For "a candidate is available": `candidate_ready`
  to `satisfied`, `refused` to `falsified`, `re_entry_requested(authority)`
  to `out_of_frame` and `re_entry_requested(basis)` to `invalid_basis`.
  For "the candidate is accepted at its declared boundary", the four
  dispositions of UP-020: `accept` to `satisfied`, `local_repair` and
  `reject` to `falsified`, `re_enter` to `invalid_basis`. The disposition
  is the acceptance result, separate from availability and assessment
  (item 5);
- effects are a refinement with three values (completed, not effected,
  completion unknown), mapped to `satisfied`, `falsified` and
  `indeterminate` for the predicate "the intended effect occurred"; an
  unknown completion never maps to completed or to no effect;
- each refined value maps to exactly one core value. A refined value that
  would map to one of two core values according to its cause takes the
  cause into the value, and each resulting value maps once, as
  `re_entry_requested` does;
- `candidate_ready` maps to `satisfied` only for the predicate "a candidate
  is available", which travels with the value. A conjunction keeps each
  component's predicate with its value, so an availability `satisfied`
  never counts toward fitness or acceptance.

**D2. Measurement of context size: ACTIVATION §2.** Step 3 of context
construction owns the size measurement and the fit test against the
declared capacity. RF-002 refers to it.

ACTIVATION §6 owns proportionality and the generic resource-limit law.
An activation declares its time, spend and other resource limits, with
their units and measurement boundaries, and reports them. The execution
binding supplies the units and values (D4). Tier-1 consumers apply
ACTIVATION §6, not the binding: `ACTIVATION.md:1230–1232` and
`EVALUATION.md:411–412` at `5ab44d5` cite the binding today. (Corrected by
I3-2e, [design discrepancy b](REDUCTION.md#design-discrepancies-found),
[cluster R30](REDUCTION.md#r30-resource-limits-added-by-i3-2e): the earlier
text gave ACTIVATION §6 proportionality only and sent time and spend to
the binding, which D4 places in tier 2.)

EVALUATION §7
Frame qualification owns actual-use evidence of adequate attention, kept
separate from size. At the base, unconditional measurement at
`ACTIVATION.md:211–214` conflicts with measurement only where selected at
`REFERENCE_FRAME.md:140–141`, `REFERENCE_FRAME.md:336–340`,
`ACTIVATION.md:59–60` and `ACTIVATION.md:654–657`. ACTIVATION §2 resolves
the conflict in one direction with its reason, and activation A4b of the
[PLAN](../qualification/C3-SYNTHESIS/PLAN.md) fixes that direction. The
reading this design recommends to A4b: size is measured whenever the
actor's envelope declares a size capacity; a measurement is not a budget,
and no universal budget follows.

**D3. Transitions and configuration: ACTIVATION §1.** ACTIVATION §1 gains
the account of work from a current state A to a destination Z through
bounded transitions, and the configuration law of the
[Bounded Transitions requirement](../../../specification/requirements/README.md#bounded-transitions-and-reference-frames)
item 4. ACTIVATION §5 gains item 5: the workspace and its authoritative
inputs are the continuing truth surface and an actor's context is a
disposable account of them. The fixed role list in the Actor row of
FOUNDATIONS §2 (`FOUNDATIONS.md:50`) and the three roles of ACTIVATION §1
(`ACTIVATION.md:149–153`) become examples of a derived allocation.
SPEC_METHOD §8 refers. EXECUTIVE_BASELINE keeps its catalogue and its
project configuration (§16) as its own bindings. RF-009 in REFERENCE_FRAME
§3 owns the rule that functional decomposition, communication, authority,
configuration and evaluation dependency are distinct relation structures;
ACTIVATION §1 Configuration refers to RF-009 for that rule and owns only
the derivation of an allocation from operations, dependencies, actor
capabilities and assurance. This decision stands against R16's action,
which named ACTIVATION §1 as owner of the list
([design discrepancy c](REDUCTION.md#design-discrepancies-found), I3-2e).
`ACTIVATION.md:322–324` already applies it.

**D4. Build-tenant binding: a new SPEC_METHOD section.** It owns the
general law: a tenant binds the requirements calculus to a computational
calculus and that calculus to an execution environment, under items 1 to
6 of the
[Build-Tenant Binding requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement).
PRODUCT_DEFINITION §8 refers to it from the tenant registry. This tenant's
own binding is [CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md).

SPEC_METHOD §11 binds the resource-limit law of ACTIVATION §6 (D2). A
binding names the units and measurement boundaries that law requires and
supplies their values. SPEC_METHOD §8 (`SPEC_METHOD.md:1523–1524`) refers
to ACTIVATION §6 and to the binding. It does not state the law. (Added by
I3-2e, design discrepancy b.)

**D5. Foundation to law: FOUNDATIONS §3 and the owning members.**
FOUNDATIONS §3 owns the table format and the standing of the consequences
(ported part 1), and a non-deciding index that names each material family,
its owning section and the members it accounts for. Each family's table
sits in its owning member, at the section where an actor enters that
family; it states its own instance premises and refers to FOUNDATIONS §3
for the standing of its consequences. Reason: relation 2 requires
shared contracts to be used where an actor applies them; a table at the
entry section is in the frame an actor is started on, while a central
table would be a cross-reference and would make FOUNDATIONS a second owner
of each family's choices.

**D6. Successor dispositions: RELEASE §9.** RELEASE §9 owns the UP-015
values. FOUNDATIONS §1 keeps the vocabulary of standing (recovered,
derived, independent, hypothesis) and the rule that a clause names its
requiring principle. That vocabulary is the only one for standing: the
recovered and independent commitments are the method's adopted premises,
and the derived ones are consequences of them. Its application of UP-015 to this corpus
(`FOUNDATIONS.md:9–28`, `:36–38`) concerns this construction, not any
method, so it leaves the Foundations: the record procedure is the
Disposition record section below, and the corpus's standing is stated in
the standards README, which owns no determination.

**D7. Imports between members: FOUNDATIONS §2.** A tier-1 member that uses
a concept owned by another member declares the import (source owner,
target, direction, loss, no transfer of authority). FOUNDATIONS §2 owns
that import rule, because tier-1 members need it. This tenant reads the
tier order of [PRODUCT, Method Structure](../../../specification/PRODUCT.md#method-structure),
where the Spec Method uses the foundational contracts and profiles import
the shared contracts, as requiring that a tier-1 member not depend on a
tier-2 owner. PRODUCT_DEFINITION §5 (`PRODUCT_DEFINITION.md:412–443`) owns
translation, equivalence and disambiguation between a project's bounded
contexts, and refers to FOUNDATIONS §2 for import.

At `5ab44d5`, I3-2e found these tier-1 dependencies on later tiers, each
with its resolution:
- time and spend: `ACTIVATION.md:1230`, `EVALUATION.md:411` →
  ACTIVATION §6 owns the law (D2, D4, R30);
- staleness of a derived surface: `ACTIVATION.md:527` uses
  PRODUCT_DEFINITION §11 → the generic rule moves to ACTIVATION §2, and
  PRODUCT_DEFINITION §11 refines it for packaging carriers (R23);
- a tier-1 choice owned by an optional profile: `FOUNDATIONS.md:851`
  names DESIGN_MODULE §5 → a tier-1 owner is named (R21).

The related pattern is generic law stated only in an optional profile
([conformance row 10](../../../specification/conformance/README.md#member-conformance)):
- configuration admission at `EXECUTIVE_BASELINE.md:1290` (R16);
- implicit activation and continuation at `EXECUTIVE_BASELINE.md:565–570`
  (R31);
- the boundary-evidence and Markov-limit law in WORLD_MODEL (REDUCTION
  §2, repair 6; D9).

**D8. Categorical and refinement claims.** FOUNDATIONS §4 Formal fragment
owns what a categorical claim must show: items 1, 4 and 5 of the
[categorical demonstration standard](../../../specification/requirements/README.md#categorical-demonstration-standard),
except the distinction named next. It keeps H1, the claim that the
semantic map S: 𝒜 → ℐ and the realisation map R_H: 𝒜 → 𝒞_H are functors
(symbols as in [CROSS_SYNTHESIS](CROSS_SYNTHESIS.md)), as a hypothesis.
EVALUATION §6 owns the equivalence ladder (ported part 4) and with it the
distinction, in item 4, between conformance, equivalence and functorial
preservation; FOUNDATIONS §4 refers to EVALUATION §6 for that
distinction. ACTIVATION §4 Refinement owns items 2 and 3 for refinement
and rewrite steps: the licensing law declared for the subject, exact steps
preserving meaning, and approximate steps stating an adequacy relation and
an end-to-end bound. Item 6, the worked join, has no locus while the
categorical capability is not selected
([PRODUCT, Categorical Construction](../../../specification/PRODUCT.md#categorical-construction));
it waits for the product owner's selection.

**D9. Shared owners of the reduction inventory.** Each cluster of the
[reduction inventory](REDUCTION.md#3-reduction-inventory) has one shared
owner. Every other locus refers to it, or refines it with a map back.
REDUCTION §3 holds the argument, the rivals and the action for each
cluster, and decides the owner. This table records the decisions beside
D1 to D8 without restating them. Written by I3-2e.

| Cluster | Shared owner | Related decision |
|---|---|---|
| R1 core values | FOUNDATIONS §4 Results | D1 |
| R2 conjunction | FOUNDATIONS §4 Conjunction of results, including the two stale predicates | D1 |
| R3 work-step variants | ACTIVATION §3 Construction availability, Disposition | D1 |
| R4 effects | ACTIVATION §3 Effects (values); ACTIVATION §5 (reconciliation before repetition) | D1 |
| R5 stops and refusals | by layer: ACTIVATION §3 (stop contract), §4 (hard stops); REFERENCE_FRAME §5 (activation and translation refusals); AC-007 (`hold`, `gap`, `refusal`); each mapped | D1 |
| R6 fit and remedies | ACTIVATION §2 (size, fit, remedies); EVALUATION §7 (adequate attention); FOUNDATIONS (no trimming) | D2 |
| R7 reuse and invalidation | ACTIVATION §7; EVALUATION for hash-only reuse | |
| R8 frame revision | REFERENCE_FRAME §10 (diagnostic order, coordinates); ACTIVATION §7 (result validity) | |
| R9 resumption | ACTIVATION §5 | |
| R10 applicability | ACTIVATION §1 Applicability. The lifecycle three-state rule has one owner, SPEC_METHOD or ASSURANCE, chosen by I3-2c | |
| R11 independence | EVALUATION §3 (what counts as independent; author identity); TICKETS (trigger boundaries, a Spec Method policy) | |
| R12 authority | FOUNDATIONS §2 Authority kinds (the one list of what creates no authority; the proxy limit); EVALUATION §2 (a check establishes only its claim); EVALUATION §5 (acceptance); ACTIVATION §1 (recording without review) | |
| R13 successor dispositions | RELEASE §9 | D6 |
| R14 closure labels | FOUNDATIONS §4 Results (refinement mapping); ACTIVATION §3 Disposition; TICKETS (closure condition) | D1 |
| R15 build-tenant binding | SPEC_METHOD §11 | D4 |
| R16 configuration | ACTIVATION §1 Configuration (allocation, admission of a configuration, direct entry); RF-009 (the list of distinct relation structures) | D3; discrepancy c |
| R17 change classes | SPEC_METHOD §4 | |
| R18 ambiguity | ACTIVATION §3 Ambiguity outcome; SPEC_METHOD §5 (default policy) | |
| R19 identity and basis | FOUNDATIONS §2 (basis; the spelling list); IDENTITY §2; RF-005 (evaluation basis) | |
| R20 refinement claims | FOUNDATIONS §4 Formal fragment; EVALUATION §6; ACTIVATION §4 Refinement | D8 |
| R21 imports and adoption | FOUNDATIONS §2 Imports between members (the binding field list); PRODUCT_DEFINITION (`:656`, adoption) | D7 |
| R22 evidence separation | EVALUATION §2; FOUNDATIONS (evidence class) | |
| R23 derived surfaces | ACTIVATION §2 (generic staleness, use, fallback); PRODUCT_DEFINITION §11 (packaging carriers, as a refinement); ACTIVATION §5 (an actor's account) | D7 |
| R24 hard stops | ACTIVATION §4 | |
| R25 promotion block | EVALUATION §5, heading `When a finding blocks promotion` | |
| R26 progress | ACTIVATION §5 | |
| R27 label homonyms | each sense at its owner; GLOSSARY lists the senses | |
| R29 preservation | ACTIVATION §4 Refinement; AC-013 | D8 |
| R30 resource limits | ACTIVATION §6, bound by SPEC_METHOD §11 | D2, D4, D7 |
| R31 implicit activation | ACTIVATION §1 Admission | D7 |
| R32 current surface and labels | SPEC_METHOD §2 Specification surface rule | |
| R33 commentary | POSTING_GUIDE §2, §9; FOUNDATIONS §2; PRODUCT_DEFINITION §11 | |
| R34 template-only rules | REFERENCE_FRAME §8; SPEC_METHOD §10; PRODUCT_DEFINITION §8 | |

Pillar owners from [REDUCTION §2](REDUCTION.md#2-pillar-account):
- FOUNDATIONS §3 owns the pillar column of the family-table format and
  the family index;
- pillar 10: AXIOMATIC_CALCULUS §9 `Constraint surfaces`, with its
  consumer at ACTIVATION §2;
- pillars 6 and 7: ACTIVATION §2 binds the successor's REFERENCE_FRAME
  sections;
- pillar 3: R29;
- pillar 8: SPEC_METHOD §11 rule 5 gains an evidence form.
- Pillar 2 is open. REDUCTION leaves its tier-1 owner to "IDENTITY or
  FOUNDATIONS §2", and no step 1 or step 2 activation in PLAN states that
  owner text. This design proposes IDENTITY, under a fixed heading
  `Boundaries and sufficiency claims`:
  - IDENTITY already owns scoped identity and stability;
  - I3-3j holds IDENTITY in step 2, while no step 2 activation holds
    FOUNDATIONS;
  - WORLD_MODEL refines the owner (I3-3d).

  The heading must be fixed in PLAN §3 before I3-3d runs. The Executive
  confirms or changes this proposal.

## Member map

| rc.2 member or group | Tenant members that receive it |
|---|---|
| README.md | README; PRODUCT_DEFINITION §4, §12 (installed cut, store, manifest) |
| AXIOMATIC_CALCULUS.md | AXIOMATIC_CALCULUS |
| DESIGN_MODULE_METHOD.md | DESIGN_MODULE; SPEC_METHOD (core rule, non-goals); ASSURANCE (6A to 6C, the predecessor's three rules for unit proof derived from a module) |
| GLOSSARY_GUIDE.md | GLOSSARY |
| IDENTITY_METHOD.md | IDENTITY; DESIGN_MODULE (defaults from a bound realisation) |
| ODD_METHOD.md | ODD; ACTIVATION (graph-function refinement, by note) |
| POSTING_GUIDE.md | POSTING_GUIDE; SPEC_METHOD (UP-012) |
| REFERENCE_FRAME_METHOD.md | REFERENCE_FRAME; FOUNDATIONS (frame objects); ACTIVATION (engagement as the step); EVALUATION (qualification) |
| RELEASE_METHOD.md | RELEASE; FOUNDATIONS (release objects); EVALUATION (UP-015 as acceptance evidence) |
| SPEC_METHOD.md | SPEC_METHOD; PRODUCT_DEFINITION (overlay, SURFACE-001, bootstrap); ACTIVATION (UP-014, UP-020, UP-021; consumes the work boundary); FOUNDATIONS (work boundary, product taxonomy); EVALUATION (evidence rules, litmus); ASSURANCE (testing law) |
| STDO_REFERENCE_FRAME_BASELINE.md | EXECUTIVE_BASELINE; ASSURANCE (testing frames, interface integration); EVALUATION (reviewer result, triage projection) |
| TICKET_METHOD.md | TICKETS; SPEC_METHOD (change classes as the triage target) |
| TRAVERSAL_OCCURRENCE_PROFILE.md | TRAVERSAL_OCCURRENCE |
| UX_METHOD.md | UX |
| WORLD_MODEL_METHOD.md | WORLD_MODEL |
| WRITING_GUIDE.md | WRITING_GUIDE |
| compressions (10) | unresolved until the product owner rules whether they are kept, superseded or removed (ledger default 7); the candidate's frames are verbatim excerpts, not compressions |
| schemas (2) | `standards/schemas/`, governed by PRODUCT_DEFINITION and RELEASE. They state no value set and no rule of their own (swept by I3-2e) |
| templates (24) | `standards/templates/`, governed by SPEC_METHOD, TICKETS, PRODUCT_DEFINITION, REFERENCE_FRAME. Their prose rules refer to the owners. The basis template's Executive sections are the executive profile's binding (R16, R31), and its evaluation-inventory values come under RF §8 (R34) |
| plugin (17) | `plugins/spec/`, each skill routed to its successor frames and owners |
| licence (1) | `LICENSE` at the candidate root |
| release note (1) | `release/release-note.md`, written at the release-candidate (RC) cut under RELEASE |
| manifest (1) | written at the RC cut under RELEASE; schema in the schemas row |

### Conformance rows and the members that answer them

The [common conformance questions](../../../specification/conformance/README.md)
have 52 member-conformance rows and 3 construction and integrated-closure
rows. They are numbered J1 to J55 as in
[ORACLE §2 (j)](../qualification/C3-ITER3/ORACLE.md): Jn is
member-conformance row n, and J53 to J55 are the closure rows. This
table names the members whose owned determinations each row tests first.
Applying a row to a member also covers that member's consumer bindings.
CONFORMANCE maps each row to a case or a logical-review check (PLAN
I3-3k); this table does not.

| Rows | Question | Members that answer first |
|---|---|---|
| J1, J2 | derivation and family coverage | FOUNDATIONS §3 (format, standing, index); each family's owning member |
| J3, J5, J7, J9, J46 | reduction: shared law, retained exceptions, references that keep triggers and force, one owning locus | every member, against [REDUCTION §3](REDUCTION.md#3-reduction-inventory) and D9 |
| J4 | deciding paths, not size | REDUCTION §4; README routes |
| J6 | outcome-driven transitions without the typed-graph profile | ACTIVATION §1 Transitions, §4; ODD as refinement |
| J8, J49 | exceptions and changed headings keep a valid disposition | RELEASE §9; each member's source-disposition table; the frontier |
| J10 | generic rule only in an optional profile | PROFILES; the tier-1 and tier-2 owners named in D7 and D9 |
| J11, J22 | helpers and typed joins | FOUNDATIONS §4 (algebra, shared machinery); DESIGN_MODULE |
| J12 | Markov claims | the pillar 2 owner (D9, proposed IDENTITY); FOUNDATIONS §5; WORLD_MODEL |
| J13 to J18, J40, J45 | a_c fidelity, coverage, projections, constraint surfaces, latitude, mechanical success | AXIOMATIC_CALCULUS (§9 Constraint surfaces); EVALUATION; REFERENCE_FRAME RF-017; FOUNDATIONS P1 |
| J19 | an earlier interpretation marked current | README route; `a_c/` entry ([INTERPRETATION §7](INTERPRETATION.md)) |
| J20, J21 | representation and meaning; identity and content | FOUNDATIONS P1, §2; IDENTITY; ACTIVATION §7 |
| J23, J24 | failure and uncovered scope; misbound judgements | FOUNDATIONS §4 Conjunction of results; REFERENCE_FRAME §8; EVALUATION §3 |
| J25, J26, J37 | context fit, obscured dependencies, packets without authority | ACTIVATION §2; EVALUATION §7; REFERENCE_FRAME §1 |
| J27 | a changed frame or a leaked answer | EVALUATION §7 frame qualification |
| J28 | self-review in a fresh context | EVALUATION §3 |
| J29, J30, J35 | frontier, discovery, compact results | ACTIVATION §1 Transitions and Roles, §5 |
| J31 to J34 | direct entry, peer configurations, redistribution, optimality | ACTIVATION §1 Configuration, §3 Effects, §5; RF-009 |
| J36, J38, J39 | invalidation, stale summaries, interruption | ACTIVATION §7, §2 (staleness, R23), §5 |
| J41 | process change as new law | SPEC_METHOD; TICKETS; every clause's purpose statement |
| J42 to J44 | executors, bindings, calculi, and merged assessments or automated decisions | SPEC_METHOD §11; EVALUATION §3; ACTIVATION §6 (R30) |
| J47, J48, J50 | own result values, deciding labels, a frame's result | FOUNDATIONS §4 Results; every member that defines values or declared states; the frames |
| J51, J52 | functor claims; rewrite and refinement steps | FOUNDATIONS §4 Formal fragment; EVALUATION §6; ACTIVATION §4 Refinement |
| J53 | members pass locally but disagree | the integrated assessment (PLAN I3-7x) over REDUCTION §3 and §4 |
| J54 | a clear replacement with no owner decision | the Disposition record below; the ticket record (PLAN §7 point 3) |
| J55 | five criteria satisfied, the sixth missing or adverse | the core conjunction, applied by the Executive at member acceptance |

## Disposition record

This construction's records are governed by the installed
[UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015),
the common
[Successor Disposition Requirement](../../../specification/requirements/README.md#successor-disposition-requirement)
and acceptance criteria 1 and 3, which own the disposition values and
their conditions. [RELEASE §9](../standards/RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
is the candidate's restatement of UP-015; as a candidate member it does
not govern the work that builds it
([CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md), section 2). This
section states only how this construction records the dispositions.

- The tenant frontier copy holds one disposition per row. A `conserved` or
  `superseded` row has a successor locus that resolves; other rows carry
  their bounded reason or the product owner's decision.
- `intentionally removed` is recorded only on the product owner's decision,
  never by a Writer.
- A rule moved unchanged to a new place stays `conserved` with its new
  locus; `superseded` needs an accepted replacement relation.
- A Writer returns the rows it changes as a frontier delta in its own
  territory; the integration activation applies the deltas to the frontier
  copy; a Reviewer checks them; the common pen consolidates accepted rows
  into the common file.
- A clause with no predecessor row is new law and names the purpose and the
  material relation that require it (acceptance criterion 6).

## Activation unit

A finite actor is started on a frame and its subject, never on the corpus.
A frame is a verbatim excerpt of the owning sections its task needs, each
excerpt under a `Source:` line naming its owning section and that member's
digest. The manifest `standards/frames/FRAME_INPUTS.json` lists each frame's
routes with owner and section digests. The generator regenerates every
frame from the manifest whenever an owner changes; it finds section
boundaries outside fenced code blocks, refuses where a boundary is
ambiguous and never truncates a section, so a copy never drifts from its
owner
([CROSS_SYNTHESIS](CROSS_SYNTHESIS.md), part 5). A frame whose task
returns a result includes the owner of the core result algebra, or its
profile's mapping into it (J50). For a task with no published frame, the
actor acquires the deciding owner sections directly (ACTIVATION §2). a_c
projections of the members may be published beside the frames; they are
not the activation unit and their fidelity is a separate claim.

For the iteration 3 conformance rows (added by I3-2e):
- **Contents.** A frame binds the contract, subject, evidence, capability
  and permitted effects of its task, not rules alone (J37). Each copied
  section names its owner (J46). It carries the family-table rows and
  result maps its sections need (tradeoff TO1, [REDUCTION
  §4.3](REDUCTION.md#43-declared-tradeoffs-and-expected-adverse-changes)).
- **Capacity.** A frame that would exceed its declared capacity is split
  by task, never truncated. A frame that fits is still judged for
  adequate attention, so a material dependency hidden by irrelevant
  material fails it (J26).
- **Staleness.** A frame is a derived surface. Once an owner it copies
  changes, the frame is stale until regenerated, and the actor falls back
  to the owner sections under ACTIVATION §2 (R23; J38).
- **Tasks.** Published frames cover the six task kinds, including
  "decide acceptance or release" and "build or assess a member" (PLAN
  I3-5v).
- **Trials.** A frame or task changed after a trial is a new subject; no
  earlier run is reused for it (J27).
- **Interpretation.** The interpretation route is optional, reached from
  the README entry that names the current interpretation and its limits.
  No route reaches a historical set as current (J19,
  [INTERPRETATION §7](INTERPRETATION.md)). A frame that uses an a_c
  projection is judged for fidelity and task sufficiency against the
  owning source (J15; path DP-27).

Context size and adequate attention are measured separately, as
[CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md#resources-measured) states.

## Per-member proof

A member is proved by the C3 contract's six acceptance criteria and by the
applicable rows among the 52 member-conformance rows (J1 to J52). Each
row's applicability, or its inapplicability with the reason, is recorded
under [Construction Authority](../../../specification/PRODUCT.md#construction-authority).
The table under the member map names the members each row tests first.
An absent integrated assessment does not by itself fail a member's
criterion 5.

The three construction and integrated-closure rows (J53 to J55) are not
member predicates: they "do not add candidate-text predicates to member
criterion 5". The integrated assessment (PLAN I3-7x) evaluates J53, and
the Executive applies J54 and J55 at its acceptance decisions.

Tenant checks:
- every link and anchor resolves;
- every clause names the principle that requires it;
- no profile term appears in tier 1 or 2 outside a disposition note;
- every result value the member defines maps to exactly one core value;
- every question the member decides has one owning section in the
  candidate, and every rival or duplicate that REDUCTION §3 lists in the
  member refers to that owner or refines it with a map;
- each family table the member owns names the pillar contributions bound
  to each argument. Each row's cited premises force its consequence, or a
  named policy with its owner carries the choice; no row is hollow. Every
  deciding section is in a table or excluded with a reason.

The order of work for iteration 3 is in
[C3-ITER3 PLAN](../qualification/C3-ITER3/PLAN.md). The order for revision
2 was in [PLAN](../qualification/C3-SYNTHESIS/PLAN.md).
