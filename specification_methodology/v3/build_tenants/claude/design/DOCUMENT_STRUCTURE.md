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

### Tier 1, foundations

| Member | Owns |
|---|---|
| FOUNDATIONS.md | the vocabulary of standing; the ontology with the frame objects; P0 to P6 with a standing column; the foundation-to-law format and family index; the core result algebra and its conjunction; composition and conservation; the generic import rule; hypotheses |
| REFERENCE_FRAME.md | the frame as a first-class object: RF-001 to RF-017, frame sets, method functions, frames in conjunction (by reference to the core conjunction), coverage, revision, the activation packet |
| ACTIVATION.md | bounded work: transitions from current state to destination, the step, intake, admission, configuration, context construction and the size measurement, the step's result refinements and dispositions, totality and refinement, work state and resumption, proportionality, closed results and reuse |
| AXIOMATIC_CALCULUS.md | the a_c theory: signature, typed records, AC-001 to AC-020, functor kinds, interpretation, identity, conformance obligations |
| IDENTITY.md | scoped identity, uniqueness, type, stability, hierarchy, authority split, UP-004, parsing, version boundary |
| EVALUATION.md | claims, evidence, independent assessment, review results, acceptance, conformance and the equivalence ladder, qualification of frames and of the method, actual-use evidence of adequate attention |

### Tier 2, Spec Method

| Member | Owns |
|---|---|
| SPEC_METHOD.md | the particular method: constitutional chain, process constitution, requirement and design law, outcome conservation, change classes and re-entry, ambiguity governance, migration, UP-012, UP-013, the general law of build-tenant binding |
| PRODUCT_DEFINITION.md | how one project binds to the method: overlay and layout independence, bounded-context resolution for a project's terms, STDO-SURFACE-001, bootstrap, build tenancy as a registry |
| TICKETS.md | work carriers: ticket and sprint model, layout, authority, triage-first intake, closure by condition, migration, ticket shape |
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
| DESIGN_MODULE.md | the DESIGN_MODULE_METHOD realisation law: ontology-first design, Prime, carrier set, boundary evaluators, totality, effect edge, coupling |
| ODD.md, TRAVERSAL_OCCURRENCE.md, UX.md, WORLD_MODEL.md | each predecessor profile in full |

### Guides, route, packaging

POSTING_GUIDE.md and WRITING_GUIDE.md restate their predecessors.
GLOSSARY.md is the non-deciding locator index; its rows route to the
owning successor clause, never to rc.2. README.md carries the routes by
task, the document map and the layout, and owns no method determination.
Packaging mirrors the installed layout so the inventory comparison at a
release-candidate cut is mechanical.

## Ownership decisions

Each decision fixes one owning section for a question the current
candidate decides in more than one place, or adds an owner the common
specification now requires. The evidence for each defect is in the
[verified gap list](../qualification/C3-SYNTHESIS/PLAN.md#verified-gap-list).

**D1. Core result algebra and conjunction: FOUNDATIONS §4.** A new
subsection "Results" owns the core values, their meanings, the standing
relation, the rule that no refinement raises standing, and conjunction
and composition of results. ACTIVATION §3 keeps the step's refinements
(construction availability, disposition, ambiguity outcome), each mapped
into the core. RF-012 in REFERENCE_FRAME §3, REFERENCE_FRAME §6 Result
conjunction, AC-007 in AXIOMATIC_CALCULUS §4 and EVALUATION §4 refer to
the owner and define nothing further. Reason: the
[single result algebra requirement](../../../specification/requirements/README.md#single-result-algebra-requirement)
places the core in the Foundations and defines conjunction once over it.
`FOUNDATIONS.md:3–5` already claims the algebra while `ACTIVATION.md:6–8`
says ACTIVATION adds no definitions; values and conjunction in one section
end both conflicts. The core must meet these constraints:

- a required evaluation or step that was not performed has a core value
  distinct from `indeterminate` (proposed name `not_performed`). A separate
  value is chosen over carrying the distinction only in the domain outcome,
  because conjunction is defined over the core and can preserve only
  distinctions the core holds. `not_performed` is the result of a planned
  assessment or step that was not carried out; required coverage that no
  planned assessment addresses is an uncovered obligation, not a result,
  and conjunction keeps the two apart;
- effects are a refinement with three values (completed, not effected,
  completion unknown), mapped to `satisfied`, `falsified` and
  `indeterminate` for the predicate "the intended effect occurred"; an
  unknown completion never maps to completed or to no effect;
- each refined value maps to exactly one core value. Where a refined value
  maps today to one of two core values by its cause, the cause becomes part
  of the refined value, and each resulting value maps once;
- `candidate_ready` maps to `satisfied` only for the predicate "a candidate
  is available", which travels with the value. A conjunction keeps each
  component's predicate with its value, so an availability `satisfied`
  never counts toward fitness or acceptance.

**D2. Measurement of context size: ACTIVATION §2.** Step 3 of context
construction owns the size measurement and the fit test against the
declared capacity. RF-002 refers to it. ACTIVATION §6 owns proportionality
only and refers to the execution binding for time and spend. EVALUATION §7
Frame qualification owns actual-use evidence of adequate attention, kept
separate from size. The present conflict, unconditional measurement at
`ACTIVATION.md:211–214` against measurement only where selected at
`REFERENCE_FRAME.md:140–141`, `REFERENCE_FRAME.md:336–340`,
`ACTIVATION.md:59–60` and `ACTIVATION.md:654–657`, is resolved in ACTIVATION
§2 in one direction with its reason. Recommended reading: size is measured
whenever the actor's envelope declares a size capacity; a measurement is
not a budget, and no universal budget follows.

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
project configuration (§16) as its own bindings.

**D4. Build-tenant binding: a new SPEC_METHOD section.** It owns the
general law: a tenant binds the requirements calculus to a computational
calculus and that calculus to an execution environment, under items 1 to
6 of the
[Build-Tenant Binding requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement).
PRODUCT_DEFINITION §8 refers to it from the tenant registry. This tenant's
own binding is [CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md).

**D5. Foundation to law: FOUNDATIONS §3 and the owning members.**
FOUNDATIONS §3 owns the table format (ported part 1) and a non-deciding
index that names each material family, its owning section and the members
it accounts for. Each family's table sits in its owning member, at the
section where an actor enters that family. Reason: relation 2 requires
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
target, direction, loss, no transfer of authority). The generic rule moves
to FOUNDATIONS §2, because tier-1 members need it and a tier-1 member must
not depend on a tier-2 owner. PRODUCT_DEFINITION §5 (`:412–443`) refines it
for a project's bounded contexts and maps its four relation kinds back to
the owner.

**D8. Categorical and refinement claims.** FOUNDATIONS §4 Formal fragment
owns what a categorical claim must show: items 1, 4 and 5 of the
[categorical demonstration standard](../../../specification/requirements/README.md#categorical-demonstration-standard);
it keeps H1 as a hypothesis. EVALUATION §6 owns the equivalence ladder
(ported part 4). ACTIVATION §4 Refinement owns items 2 and 3 for
refinement and rewrite steps: the licensing law declared for the subject,
exact steps preserving meaning, and approximate steps stating an adequacy
relation and an end-to-end bound.

## Member map

| rc.2 member or group | Tenant members that receive it |
|---|---|
| README.md | README; PRODUCT_DEFINITION §4, §12 (installed cut, store, manifest) |
| AXIOMATIC_CALCULUS.md | AXIOMATIC_CALCULUS |
| DESIGN_MODULE_METHOD.md | DESIGN_MODULE; SPEC_METHOD (core rule, non-goals); ASSURANCE (6A to 6C) |
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
| schemas (2) | `standards/schemas/`, governed by PRODUCT_DEFINITION and RELEASE |
| templates (24) | `standards/templates/`, governed by SPEC_METHOD, TICKETS, PRODUCT_DEFINITION, REFERENCE_FRAME |
| plugin (17) | `plugins/spec/`, each skill routed to its successor frames and owners |
| licence (1) | `LICENSE` at the candidate root |
| release note (1) | `release/release-note.md`, written at the RC cut under RELEASE |
| manifest (1) | written at the RC cut under RELEASE; schema in the schemas row |

## Disposition record

The disposition values and their conditions are owned by
[RELEASE §9](../standards/RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
and, for this product, by the common
[successor requirements](../../../specification/requirements/README.md#successor-disposition-requirement)
and acceptance criteria 1 and 3. This section states only how this
construction records them.

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
routes with owner and section digests; a generator regenerates every frame
from the manifest whenever an owner changes, so a copy never drifts from its
owner ([CROSS_SYNTHESIS](CROSS_SYNTHESIS.md), part 5). A frame whose task
returns a result includes the owner of the core result algebra, or its
profile's mapping into it. For a task with no published frame, the actor
acquires the deciding owner sections directly (ACTIVATION §2). a_c
projections of the members may be published beside the frames; they are
not the activation unit and their fidelity is a separate claim.

Context size and adequate attention are measured separately, as
[CONSTRUCTION_BINDING](CONSTRUCTION_BINDING.md#resources-measured) states.

## Per-member proof

A member is proved by the C3 contract's six acceptance criteria and all 31
conformance discriminators, plus these tenant checks: every link and
anchor resolves; every clause names the principle that requires it; no
profile term appears in tier 1 or 2 outside a disposition note; every
result value the member defines maps to exactly one core value; and every
question the member decides has one owning section in the candidate. The
order of work for the current rebuild is in
[PLAN](../qualification/C3-SYNTHESIS/PLAN.md).
