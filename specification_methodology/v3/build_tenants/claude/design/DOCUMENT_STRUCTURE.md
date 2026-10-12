# Claude Tenant Design: Document Structure

Status: tenant HOW for the STDO 3 candidate on `tenant/claude/c3-v3`; not
common WHAT; not accepted. Builder basis `stdo://releases/v2.5.1-rc.2/`.
Inputs: [Intent](../../../specification/INTENT.md),
[Product](../../../specification/PRODUCT.md) (C3 contract),
[requirements](../../../specification/requirements/README.md), the common
[frontier](../../../specification/requirements/PREDECESSOR_CLAIMS.md) and
its [tenant copy](../frontier/PREDECESSOR_CLAIMS.md), and the accepted
[PRINCIPLES](PRINCIPLES.md), unchanged here.

## Purpose

The candidate is the foundational axioms first, then the whole v2.5.1-rc.2
corpus restated on them in this tenant's own text, complete and applicable
with the predecessor no longer operative. Every frontier row receives one
UP-015 disposition and, where conserved or superseded, a locus that
resolves to the tenant's text.

Two first-pass errors are retired: the corpus is as large as the law
requires; what fits an activation is a projected frame, never the corpus;
and a route to the rc.2 clause (FOUNDATIONS §1) is provenance under the
standalone successor requirement, not a disposition. The first-pass files
are starting text where they already restate; each is rewritten at its
member's activation; nothing is accepted by presence.

## Tiers and members

Files are under `standards/` unless a path says otherwise. Obligations are
PRODUCT's C3 tier table; the organisation is this tenant's. A member marked
new exists only after its activation.

### Tier 1, foundations

| Member | Owes | Why a member |
|---|---|---|
| FOUNDATIONS.md | ontology, C (proposed as P0) and P1 to P6 as commitments with standing, composition and conservation algebra, hypotheses | keeps its role; repaired at member 1 |
| REFERENCE_FRAME.md, new | the frame as a first-class object: basis, manifold, envelope, frame, frame set, configuration, lens; RF-001 to RF-017; engagement; conjunction; coverage ledger; revision; qualification | the tier owes the frame as a first-class object; the first pass had no home for it; it is the law of the activation unit |
| ACTIVATION.md, renamed from CALCULUS.md at member 1 | the bounded step: intake admitted first, activation on a projected frame under an envelope, grant, result algebra, totality, refinement, work state, restart, proportionality (UP-014), reuse | the tier owes bounded activation and work state; the rename removes the collision with the a_c calculus |
| AXIOMATIC_CALCULUS.md, new | the a_c theory in full: signature, typed records, AC-001 to AC-020, functor kinds, interpretation, exact identity, conformance obligations | the projection that produces every frame is defined here |
| IDENTITY.md, new | scoped identity, uniqueness, type and stability, hierarchy, authority split, UP-004, parsing, version boundary | the tier receives IDENTITY_METHOD; cited too widely for a subsection |
| EVALUATION.md | claims, evidence and authority law, litmus, independent assessment, review results, acceptance, conformance, qualification of the method | keeps its role; receives the generic evidence law and the reviewer-result law |

ACTIVATION section 3 is the one definition of the result algebra; RF-012
(REFERENCE_FRAME) and AC-007 (AXIOMATIC_CALCULUS) restate their laws on it
in their own words and define it nowhere else: two distinct predecessor
claims over one definition, not a merged law; their unification stays the
C2 question PRINCIPLES names.

### Tier 2, Spec Method

| Member | Owes | Why a member |
|---|---|---|
| SPEC_METHOD.md | the particular method: constitutional chain, process constitution, manifesto, ambiguity governance, requirement and design law, change classes and re-entry, migration, UP-012, UP-013 | keeps its role; carries every SPEC_METHOD clause that is not generic |
| PRODUCT_DEFINITION.md, new | the overlay and layout independence, STDO-SURFACE-001, bootstrap rule, a project's version boundary | a fifth of SPEC_METHOD; how one project binds to the method; the semantics the schemas and templates realise |
| TICKETS.md, new | work carriers: ticket and sprint model, layout, authority, triage-first intake, closure by condition, migration, ticket shape | the tier owes carriers and triage; the first pass reduced 60 KB to one section |
| ASSURANCE.md, new | evidence rules, verification layers, testing taxonomy, test authority, scenario bundles, path coverage, trace closure, the testing frame set, counterexample localisation, module-derived unit tests | the tier owes assurance and testing law; spread over three rc.2 members with no home |
| RELEASE.md, new | release identities, qualified refs, phases, candidate, immutable RC, exact-cut qualification, monotonic advancement, selector adoption, naming, cohorts, UP-015 | the tier owes release mechanics; the first pass carried lineage only |
| CONFORMANCE.md | the cases the method must pass, with independently specified expectations; the common discriminators | acceptance criterion 5 |

### Tier 3, profiles

| Member | Owes | Why a member |
|---|---|---|
| PROFILES.md | the boundary: how a profile imports the tiers above, what stays out of the core, the index | keeps its role as index and boundary only |
| EXECUTIVE_BASELINE.md, new | STDO_REFERENCE_FRAME_BASELINE in full: profile terms, Executive attention and drift locks, derived frames, engagement transition, adoption, failure classification | the tier receives the frame catalogues and Executive law; this construction runs under it |
| DESIGN_MODULE.md, new | DESIGN_MODULE_METHOD realisation law: ontology-first design, prime law, carrier set, boundary evaluators, totality, effect edge, coupling | 121 KB of realisation law; PROFILES §3 was a stub |
| ODD.md, TRAVERSAL_OCCURRENCE.md, UX.md, WORLD_MODEL.md, new | each predecessor profile in full, importing the tiers above | the tier owes a full restatement per profile; a stub cannot carry 15 to 85 sections |

### Guides, route, packaging

POSTING_GUIDE.md and WRITING_GUIDE.md restate their predecessors.
GLOSSARY.md, new, is the non-deciding locator index whose rows route to the
owning successor clause, never to rc.2; generated from anchors where
possible. README.md carries the routes by task, the document map and the
layout. Packaging members and paths are in the member map; the candidate
mirrors the installed layout so the inventory comparison at the RC cut is
mechanical.

## Member map

| rc.2 member or group | Tenant members that receive it |
|---|---|
| README.md | README; RELEASE (installed cut, store, manifest) |
| AXIOMATIC_CALCULUS.md | AXIOMATIC_CALCULUS |
| DESIGN_MODULE_METHOD.md | DESIGN_MODULE; SPEC_METHOD (core rule, non-goals); ASSURANCE (6A to 6C) |
| GLOSSARY_GUIDE.md | GLOSSARY |
| IDENTITY_METHOD.md | IDENTITY; DESIGN_MODULE (defaults from a bound realisation) |
| ODD_METHOD.md | ODD; ACTIVATION (graph-function refinement, by note) |
| POSTING_GUIDE.md | POSTING_GUIDE; SPEC_METHOD (UP-012) |
| REFERENCE_FRAME_METHOD.md | REFERENCE_FRAME; FOUNDATIONS (ontology objects); ACTIVATION (engagement as the step); EVALUATION (qualification) |
| RELEASE_METHOD.md | RELEASE; FOUNDATIONS (recursive product objects); EVALUATION (UP-015 as acceptance evidence) |
| SPEC_METHOD.md | SPEC_METHOD; PRODUCT_DEFINITION (overlay, SURFACE-001, bootstrap); ACTIVATION (work boundary, UP-014, UP-020, UP-021); FOUNDATIONS (product taxonomy); EVALUATION (evidence rules, litmus); ASSURANCE (testing law) |
| STDO_REFERENCE_FRAME_BASELINE.md | EXECUTIVE_BASELINE; ASSURANCE (testing frames, interface integration); EVALUATION (reviewer result, triage projection) |
| TICKET_METHOD.md | TICKETS; SPEC_METHOD (change classes as the triage target) |
| TRAVERSAL_OCCURRENCE_PROFILE.md | TRAVERSAL_OCCURRENCE |
| UX_METHOD.md | UX |
| WORLD_MODEL_METHOD.md | WORLD_MODEL |
| WRITING_GUIDE.md | WRITING_GUIDE |
| compressions (10) | `a_c/` program, map and frames, proposed `superseded` by the relation "projection from the set program"; `stdo_bootstrap.md` to PRODUCT_DEFINITION and bootstrap templates |
| schemas (2) | `standards/schemas/`, governed by PRODUCT_DEFINITION and RELEASE |
| templates (24) | `standards/templates/`, governed by SPEC_METHOD, TICKETS, PRODUCT_DEFINITION, REFERENCE_FRAME |
| plugin (17) | `plugins/spec/`, each skill re-routed to its successor frames |
| licence (1) | `LICENSE` at the candidate root |
| release note (1) | `release/release-note.md`, written at the RC cut under RELEASE |
| manifest (1) | written at the RC cut under RELEASE; schema in the schemas row |

## Disposition vocabulary

Every frontier row takes exactly one of `conserved` (restated in the
tenant's own text; the locus resolves; an author-independent source
comparison finds the determination present), `superseded` (an accepted
successor relation, named), `intentionally removed` (Jim's decision and
reason) or `not applicable` (bounded reason); `unresolved` is the only
other state and blocks qualification. Every clause carries the principle
that requires it, C (proposed as P0) and P1 to P6 of
[PRINCIPLES](PRINCIPLES.md), and may carry a provenance route into
`stdo://releases/v2.5.1-rc.2/`. A clause with
no predecessor row is new law, admitted only with the purpose and material
relation that require it (criterion 6). `reframed` is a note on how a
conserved claim was carried, never a disposition. A member's Writer fills the
Disposition and Successor locus columns of its cone in the tenant frontier
copy; the Reviewer checks them; the Executive consolidates accepted rows
into the common file through the pen.

## Activation unit

A finite actor is activated on a projected reference frame, never on the
corpus. The set program under `a_c/` (a_c.text, validated per the common
dependency contract) encodes the corpus; each member's activation extends
it and publishes one projected frame per selected task of the contract. A frame is the subject plus the
clauses the task needs and nothing else, materialised or reference-only.
Its bytes are measured with `wc -c` before any actor reads it and recorded
with the activation under `qualification/`. A frame that exceeds its
envelope is refined or returns `out_of_frame`, never padded with the
corpus. A member's Writer reads the rc.2 member it restates and the frames
of its dependencies; a member larger than one activation is declared as a
cone of sections.

## Construction order

One Writer activation per member or declared cone, in this sequence:

1. REFERENCE_FRAME, with the foundation repairs it forces: FOUNDATIONS
   gains frame, frame set, lens and coverage ledger as ontology objects and
   takes the UP-015 vocabulary; CALCULUS becomes ACTIVATION and admits the
   intake before the step, whose context is an activated frame. The member
   map is reviewed with this member.
2. AXIOMATIC_CALCULUS.
3. SPEC_METHOD, with PRODUCT_DEFINITION split off, its generic law in tier
   1 and its testing law in ASSURANCE.
4. TICKET_METHOD into TICKETS.
5. STDO_REFERENCE_FRAME_BASELINE into EXECUTIVE_BASELINE, its testing
   frames into ASSURANCE, its reviewer law into EVALUATION.
6. RELEASE_METHOD and IDENTITY_METHOD into RELEASE and IDENTITY.
7. DESIGN_MODULE_METHOD into DESIGN_MODULE, SPEC_METHOD and ASSURANCE.
8. ODD, TRAVERSAL_OCCURRENCE, UX, WORLD_MODEL; PROFILES reduced to index
   and boundary.
9. Guides, GLOSSARY and README.
10. Packaging: the compressions' successor, schemas, templates, plugin,
    licence, release note, manifest (RELEASE); closes before any RC cut.

Each step: the Writer returns one closed result and disposes its cone's
rows in the tenant frontier copy; a Reviewer who is not the author, by
default of another model family (same family is a declared exception,
reason in the activation, marked on the result), is activated on every
`candidate_ready`; the Executive disposes; the pen ledgers. Per-member
proof is the contract's six criteria plus: links and anchors resolve; every
clause has its principle; no profile term in tier 1 or 2 outside a
disposition note.

## Cost

Envelopes are declared per activation by the Executive (context bytes,
wall, spend) and reported in each return in `qualification/RETURNS.md`:
bytes measured before the read, wall by `date -u`, spend as the host
reports it or as unavailable.
