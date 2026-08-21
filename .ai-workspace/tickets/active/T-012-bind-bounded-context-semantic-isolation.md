# T-012 - Bind Bounded-Context Semantic Isolation

- id: T-012
- title: Bind bounded-context semantic isolation and explicit term resolution
- type: proposal
- ticket_category: constitutional
- status: active
- review_status: pending
- goal: >-
    Prepare one STDO 2.4.3 successor over immutable v2.4.2 that prevents equal
    term spelling from collapsing meaning or authority across bounded contexts.
- change_intent: >-
    Make term resolution depend on explicit bounded context, owning authority,
    selected basis, and governed scope; require explicit import, translation,
    or disambiguation relations at cross-context seams; and fail closed when a
    material occurrence remains unresolved or ambiguous.
- change_class: product_reprice
- re_entry_point: specification/PRODUCT.md
- triaged_at: 2026-08-21
- created_at: 2026-08-21
- updated_at: 2026-08-21
- owner: specification_methodology
- pen_holder: codex
- predecessor_release: v2.4.2 at e50ee39a4e446dd781e6dc4e490076588c71982d
- predecessor_standards_aggregate:
  5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be
- target_release: 2.4.3
- release_class: patch_release_default_rc_path
- current_goal_binding: this ticket
- work_authorization: direct_human_authorization_2026-08-21

## Intake Triage

**Substantive?** Yes. The released glossary's context-free shared-default rule
can silently import meaning and misroute semantic or decision authority when
several bounded contexts reuse the same term.

**Boundary crossed?** The live Intent and Product, normative specification,
ODD, World Model, Reference Frame, baseline-profile, ticket, and glossary-index
surfaces, the Product Definition Overlay interoperability schema, starter
templates, source-maintained compressions, and agent bootstrap projections. No
immutable release or downstream consumer is mutable under this ticket.

**Smallest lawful re-entry.** Product repricing. The defect affects the
constitutional meaning-resolution relation used by every downstream method,
product definition, multi-product workspace, and composed bounded context.

## Current Goal

Author one reviewable successor candidate that:

1. treats a term as a lexical label rather than a context-free concept identity;
2. resolves meaning through bounded-context identity, owning authority,
   selected basis, and governed scope;
3. permits unqualified prose only where those coordinates resolve exactly one
   applicable meaning;
4. requires explicit, owner-authorized imports, translations, equivalences, or
   disambiguations at cross-context seams without transferring authority;
5. makes zero or multiple applicable meanings a fail-closed result;
6. turns the glossary into a context-qualified index of source-owned meanings;
7. strengthens Product Definition Overlay disambiguation bindings without
   turning the overlay into a second semantic authority;
8. projects the same rule into compressed and agent bootstrap surfaces; and
9. qualifies both positive resolution and material collision cases.

## Required Collision Cases

- `Frame`: Reference Frame Method evaluation context versus an ABG or other
  Product-owned runtime carrier;
- `Owner`: generic specialist evaluation family versus the authority that owns
  a semantic or decision relation;
- `Product`: immutable released Product versus mutable Product Definition;
- `Tenant`: STDO build realization versus hosted, customer, account, runtime,
  or data tenancy; and
- `User`: a downstream Product role versus person, principal, account, actor,
  operator, or data-subject meanings owned by other contexts.

Equal spelling alone must resolve none of these seams. A positive case must
show exact resolution under one declared context, and a cross-context case must
show the explicit relation and its authority, basis, scope, direction where
material, and invalidation law.

## Schema Migration Boundary

The Product Definition Overlay schema identity advances from
`urn:stdo:schema:product-definition:1` to
`urn:stdo:schema:product-definition:2`. Definitions with an explicitly empty
`local_constitution.disambiguations` array retain their shape. Every retained
non-empty revision-1 disambiguation adds `term`, `context`, `resolves_to`, and
`basis`; its existing `uri`, `disambiguates`, `authority`, and `applies_to`
bindings remain. No other overlay field changes under this ticket.

## Successor Delta And Practical Provenance

Immutable `v2.4.2` remains the exact predecessor. The mutable successor work
changes semantic isolation, context declaration, glossary routing, World Model
specialization, schema disambiguation, and their projections. Exact changed and
conserved member counts, digests, review state, and release identity belong in
this ticket and any authorized release note rather than the live Intent or
Product definition.

The Version 2 line historically began as incremental evolution from accepted
`v1.8.0`, preserving or explicitly superseding accepted predecessor semantics
while excluding rejected executable or overcorrected candidate scope. That
historical direction is retained here; live `INTENT.md` now states the stable
evolution law without carrying a version ledger.

The STDO reference-frame profile was practically discovered through
ABIogenesis delivery and review work. The names ABIogenesis, GTL, HoG, and ABG,
their local roles, and their topology are provenance or consumer-local
architecture, not members of the generic baseline. The reusable observations
are the bounded authority, exact candidate, independent reacquisition,
non-implementing review, bounded disposition, and missing-frame failure signals
now stated generically in the baseline's Empirical Revision Boundary. This
historical provenance is retained here instead of in the live profile.

## Independent Review Disposition

The first mutable candidate was held on four high-severity findings:

1. six bounded-context identities existed only in the glossary rather than in
   their cited owning standards;
2. the glossary still carried definitions and the compression README promoted
   it among deciding sources;
3. World Model claimed an unchanged `Source Project` import while narrowing it
   and deriving `Builder Project` without a complete directional relation; and
4. live Product, Intent, and baseline text retained successor and provenance
   history.

The required repair is owner-declared contexts, a locator-only glossary, an
exact World Model specialization relation, and present-tense live
constitutional surfaces. The prior mechanical green state and aggregate do not
qualify the repaired bytes.

## Release Authorization

On 2026-08-21, Jim directly instructed `ok release 2.4.3`. This authorizes the
normal governed release path: prepare exact release assets, qualify the mutable
candidate, publish one immutable RC, obtain author-independent exact-carrier
review, present that exact carrier and its final-delta relation for human
acceptance, and tap only after that acceptance.

The instruction does not turn mutable-source checks into independent review and
does not pre-accept an exact carrier that did not yet exist when the instruction
was given.

## Closure Law

This ticket closes only when:

- the mutable Product and deciding standards express one consistent semantic-
  isolation law;
- every glossary row points to an exact context-declaring owning clause and the
  glossary contains no semantic definition;
- Product Definition Overlay schema revision and template guidance agree;
- source-specific and aggregate compressions are semantically current and all
  recorded digest edges reproduce;
- Codex and Claude bootstrap templates carry equal minimum semantics;
- structural schema cases and the required collision cases pass;
- immutable `v2.4.2`, its release branch, and its annotated tag remain
  unchanged; and
- any release preparation, review, acceptance, or publication is separately
  authorized and performed under `RELEASE_METHOD.md`.

## Non-Closure Conditions

- the glossary remains an implicit global namespace;
- nominal equality selects meaning, identity, equivalence, or authority;
- every bare term is rejected even where one declared context resolves it
  uniquely;
- a translation hides changed meaning, loss, direction, or invalidation;
- a disambiguation URI is listed without exact concept, context, authority,
  basis, and scope binding;
- the overlay restates source-owned semantic truth;
- an agent is permitted to guess among unresolved meanings; or
- mutable authoring work is represented as a released or accepted Product.

## Current State

- first mutable-candidate qualification: superseded by the independent HOLD;
- owner-context, glossary-authority, World Model relation, and live-surface
  repairs: complete in mutable source;
- schema and template projection: retained as Product Definition Overlay schema
  revision 2 and requalified with 13 positive, structural-negative, URI, and
  selected-candidate membership cases;
- prior candidate subject: 45 members, 15 changed from `v2.4.2`, aggregate
  `34bd9a195e75a216bb2c11481cec6380e4565c915339fe1c2fc36b8bc3496976`;
- repaired candidate subject: 45 members, 21 changed from `v2.4.2`, aggregate
  `3617ba1b13f134284564621b6e61dbce361d2f6341b768e4d90b5a47554c67cd`;
- semantic/index qualification: all ten context identities occur in their
  owning standards, all 27 distinct glossary clause locators resolve, the
  glossary has no term-definition headings, and the World Model specialization
  carries every required relation field;
- compression qualification: all 17 deciding-source digest edges and the one
  separately classified non-deciding index edge reproduce;
- predecessor regression: local and remote annotated `v2.4.2` still peel to
  `e50ee39a4e446dd781e6dc4e490076588c71982d`, with predecessor aggregate
  `5b5957d1a43be52a03b1316d442f2d797ba86a084550a1346dfc2dc6254123be`;
- release preparation and immutable RC publication: authorized by the direct
  2026-08-21 instruction and in progress under `RELEASE_METHOD.md`;
- independent exact-carrier review: pending;
- exact-carrier human acceptance: pending; and
- final release branch, tag, and publication: not established.
