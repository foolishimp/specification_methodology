# Identity Method

## Governing Relations

The instance has subjects to distinguish, owners and kinds that may differ,
representations read by people or machines, and lifecycles across which
references must remain usable. The adopted F2 interpretation, F3 identity and
current state, F4 composition and F6 evidence and authority commitments in
[Foundations](FOUNDATIONS.md#foundational-commitments) require consumers to
preserve those distinctions through their admitted relations. Identity Method
chooses authority, kind and value as the scoped identity minimum. Governing
basis and lifecycle qualify authority or applicability where their owning
contract requires them; they are not universal object-identity fields.

Equal representation alone supplies neither identity equality nor permission;
continuing identity alone supplies no claim that content or evidence is current.
Readable or opaque names, encoding, concrete hierarchy and optional coordinates
remain choices of the adopting owner. The arguments below explain how the
identity, information, composition and authority pillars constrain the actual
readers and transitions without deriving one universal serialization.

At the identity-reading boundary, Bind and Acquire recover the identity
coordinates and their authentic owner under the
[Transformation Library](TRANSFORMATION_LIBRARY.md).
Transform and composition preserve the admitted identity and authority
relations or use an explicit owning transition. Evaluate checks uniqueness,
kind distinction, parsing, stability and applicable evidence. Dispose remains
an owning decision where elevation, transfer, supersession or retirement is
required. These descriptions use the shared relations without adding a
mandatory identity format, runtime API, actor or workflow stage.

Engine identities, domain identities and release coordinates retain separate
owners. Bound ABG defaults are a conditional realization convenience; they do
not define generic identity law. Release distinctions remain owned by release
law; carrying release coordinates does not turn release identity into object
identity.

| Deciding consumer | Premises and pillar contribution | Consequence at that consumer | Additional policy and owner |
|---|---|---|---|
| [Scoped Identity](#1-scoped-identity), [Uniqueness Law](#2-uniqueness-law) and [Type Law](#3-type-law) | F2 and F3; different authorities and kinds can use the same literal value. The identity pillar distinguishes the subjects; interpretation determines which subject a serialized value denotes. | A bare token cannot establish equality when its owner or kind differs. A family and a concrete member remain distinct even where their readable forms share a prefix. A reader needs the scope and kind required to distinguish the intended objects. | Identity Method owns the authority/kind/value minimum and uniqueness within lawful scope. The object's owning authority chooses its kinds, optional coordinates and grammar. |
| [Stability Law](#4-stability-law) and the reuse boundary in [Parsing Law](#parsing-law) | F3 and F4; references and dependent evidence persist while content, grants or coordinates may change. Identity and typed conservation preserve continuity through a declared transition rather than through string equality. | An unchanged identity cannot make a revoked grant or stale observation current. A changed coordinate alone proves neither a new object nor continuity with the old one; the owning transition supplies that relation. | Identity Method chooses stability adequate to the governed lifecycle and an explicit relation when identity changes. Foundations owns evidence currentness; the identity owner decides its actual transitions. |
| [Human-Readable vs Opaque Identity](#human-readable-vs-opaque-identity), [Identity Hierarchy](#identity-hierarchy) and [Parsing Law](#parsing-law) | F2 and F3; a reader encounters serialized forms that can look meaningful without carrying their full semantic coordinates. Information and interpretation separate recognizing a pattern from identifying its subject. | A regex match establishes only what its parsing contract says. It cannot turn a grouping label into an executable requirement, a subordinate criterion into its parent, or a readable name into authority. An opaque representation remains lawful when the required identity distinctions are preserved. | Identity Method owns the parsing and non-aliasing conditions and offers a hierarchy model. The owning domain chooses readable, opaque or hybrid forms and whether family identities exist. |
| [Authority Split](#authority-split) and [Default Formats And Overrides](#default-formats-and-overrides) | F2, F3 and F6; runtime and domain owners govern different kinds while a runtime may transport both. Specification structure and identity locate those owners; authority bounds what either may decide. | A runtime's ability to carry or normalize a domain identity does not let it invent the domain's semantic grammar. A default format cannot override a published domain decision merely because its helper is available. | Identity Method permits bound runtime defaults and domain overrides subject to its published preservation conditions. Runtime owners choose their generators; domain owners publish their kinds, grammar and overrides. ABG-specific defaults apply only to a bound ABG realization. |
| [Authority Identity And Conservation](#authority-identity-and-conservation-stdo-up-004) | F3, F4 and F6; a grant can pass through delegates, adapters and projections while the acting identity differs from the grantor. Identity names the authority relation; composition preserves its admitted extent; evidence distinguishes that relation from capability. | Carrying a grant cannot enlarge its subject, scope, role or decision rights. Recording a ruling does not widen it, and proxy actor identity cannot become human-authority identity or make the implementer's review independent. | UP-004 owns the required grant coordinates and explicit authority transitions. The grantor decides any elevation, transfer, delegation or retirement within its mandate; an adopted profile owns its projection vocabulary. |
| [Derivation Verification Material](#derivation-verification-material) | F2–F4 and F6; a later publication carries evidence for an exact historical manifest, member or fragment. Information fidelity preserves the historical byte predicate; identity keeps the historical subject distinct from the current evidence carrier. | Authentic reconstruction can establish the declared member, digest, fragment and unique-membership checks without making the predecessor operative. It cannot establish semantic derivation, historical acceptance or current successor authority. A source change invalidates the affected reconstruction binding until refreshed. | Identity Method owns exact evidence/reconstruction, membership and refusal conditions. The publication manifest binds the evidence members. Semantic derivation, acceptance and publication retain their existing decision owners. |
| [Release Version Boundary](#release-version-boundary) | F2, F3 and F6; a release coordinate identifies a published cut while domain objects and mutable selectors have their own subjects. The identity pillar separates those coordinates; authority distinguishes discovery from adoption. | Assigning a release version to a package cannot make that version the identity of each requirement or runtime object. A selector may locate a cut without becoming either its immutable identity or the consumer's operative basis. | Release Method owns exact release identities and selector/adoption mechanics. Identity Method retains the distinction at object readers; each domain owns its object identities. |

## Derivation Verification Material

Historical derivation coordinates bind their original accepted cut, manifest,
members and fragments. Resolving those coordinates is a verification operation;
it does not require that predecessor to remain installed or operative. A complete
successor can carry the exact verification evidence under its own immutable
manifest without changing the historical coordinates or basis-record preimage.

The verification material contains the exact historical manifest bytes and their
declared digest. Each required historical member is either carried as exact
evidence bytes or reconstructed by a declared ordered byte-range projection of
successor-owned members, with literal reconstruction bytes where necessary.
The source member path and digest resolve in the successor publication manifest;
reconstructed bytes have the exact historical member digest in the historical
manifest. The material records the semantic-address rule, and every required
fragment resolves under it. Missing, duplicate, altered, incomplete or unbound
material refuses the affected verification. Re-entry requires authentic complete
verification material; an installed predecessor supplies no exception to these
checks and is not an implicit fallback.

The refusal retains its cause on the affected verification predicate. A
demonstrated duplicate, alteration, incompleteness or absence in the complete
authoritative member set is falsified. Unbound material, lacking an authentic
basis binding, is invalid_basis; material not yet acquired leaves the predicate
indeterminate. Missing reasons or unsupported labels follow the core
missing-reason rule without erasing independently admissible findings.
Absence from a sparse checkout does not establish authoritative absence.

The [derivation resource](verification_material/DERIVATION_SOURCES.json) is
distribution evidence for these byte predicates, not a second constitutional
surface. It adds no field to the calculus or profile basis record; the existing
publication-manifest digest binds its declared membership. Source projections
bind the exact current member digests; changed sources require new verification
material before reuse. A successful
reconstruction establishes content and reference checks only. Acceptance of
the historical cut, semantic derivation, successor admission and publication
remain separate judgments at their existing owners.

Verification applies [Contract application](TRANSFORMATION_LIBRARY.md#contract-application)
to the exact historical-coordinate and byte-reconstruction predicates. Its
required checks are member, digest, fragment and unique membership; the
verification material above supplies their evidence and source identity. The
core result and conjunction preserve each check and its residuals. This is a
content-verification binding, not semantic derivation, acceptance or current
authority. Their predicates remain separate.


## Position

Identity must be:

- scoped
- typed
- unique
- stable enough for the governed purpose

Identity is not a flat global string convention.

Identity is made unique by hierarchy and type.

That means:

- the same literal token may be lawful in different scopes when its authority
  and kind differ
- one string format is not sufficient to define identity across all products
  and runtime surfaces
- a human-readable form may help recognition, but readability is secondary to
  uniqueness and stable governed meaning

The engine should carry identity safely.

The domain should define semantic identity law for its own constitutional
objects.

---

## Core Law

### 1. Scoped Identity

Identity is always scoped.

At minimum, identity should be interpretable through:

- authority
- kind
- value

So the minimum semantic model is:

`identity = authority + kind + value`

Optional additional coordinates may include:

- parent scope
- revision
- publication version
- temporal coordinates

### 2. Uniqueness Law

Identity must be unique within its lawful scope.

The requirement is not “every id must look globally unique as a naked string.”

The requirement is:

- no two live objects of the same kind may share the same identity within the
  same authority scope
- aliasing across scopes must remain explicit
- serialization must preserve enough hierarchy to prevent accidental collision

### 3. Type Law

Identity is typed.

Different kinds of thing should not be collapsed into one undifferentiated id
space.

Examples of distinct identity kinds include:

- goal
- intent
- requirement
- requirement_family
- acceptance_criterion
- scenario
- design_decision
- graph_function
- asset_surface
- release
- install
- run
- graph_call
- continuation
- event

The method must not treat a family id as if it were a concrete requirement id,
or a release version as if it were object identity.

### 4. Stability Law

Identity should remain stable for the governed lifecycle it serves.

This does not mean every identity is immutable forever.

It means identity must be stable enough to support:

- traceability
- comparison
- replay
- publication
- supersession

If an identity changes, the method should make the relationship explicit rather
than silently reusing the old one for a different object.

---

## Human-Readable vs Opaque Identity

Identity may be:

- opaque, such as a GUID or UUID
- human-readable, such as `REQ-F-CAPABILITY-001`
- hybrid, where one component is readable and another is opaque

The governing rule is:

- readability is a convenience for recognition
- uniqueness and scoped meaning are the actual law

Therefore:

- a GUID is lawful even when it carries no human meaning
- a readable id is lawful only if it still preserves uniqueness in scope
- no reader should infer that a readable id is safer or more authoritative than
  an opaque one merely because it looks meaningful

---

## Identity Hierarchy

Identity should be made unique by hierarchy where appropriate.

One useful general model is:

`authority / kind / value / revision`

Not every serialization needs all four visible segments, but the semantic model
should be available.

Examples:

- `(<product-authority>, requirement, REQ-F-CAPABILITY-001)`
- `(<product-authority>, requirement_family, REQ-F-CAPABILITY)`
- `(<runtime-authority>, run, 550e8400-e29b-41d4-a716-446655440000)`
- `(<release-authority>, release, 1.0.0-rc.1)`

The important point is that:

- `REQ-F-CAPABILITY` and `REQ-F-CAPABILITY-001` are not the same kind of
  identity
- a runtime `run_id` and a domain requirement id do not belong to the same
  semantic category even if both serialize as strings

---

## Authority Split

### Engine-Owned Identity

The substrate or runtime may define default identities for runtime-owned
objects, such as:

- runs
- graph calls
- jobs
- frames
- continuations
- events

For these, the engine may use opaque ids and engine-local generation rules.

Those rules should optimize for:

- uniqueness
- replay safety
- event-stream integrity

The engine should not impose domain-specific semantic grammar on domain-owned
objects.

### Domain-Owned Identity

Derived domains own the semantic identity grammar for their own constitutional
objects, such as:

- requirements
- requirement families
- acceptance criteria
- scenarios
- ADRs or design decisions
- published domain assets

The domain must define:

- which identity kinds exist
- how they are distinguished
- what makes them unique
- how they are parsed or read

The runtime may transport those identities, but it should not silently invent
their meaning.

---

## Authority Identity And Conservation (`STDO-UP-004`)

Authority is an identity-bearing semantic relation, not a display label,
capability string, actor identity, or reachable code path. Its identity
preserves owner, kind, governed subject, scope, and governing basis.

Composition, delegation, adapters, projections, wrappers, and registries may
restrict or faithfully carry admitted authority. They must not silently widen
scope, add a role, increase cardinality, change kind, or reconstruct authority
from actor identity, payload shape, or available capability. Elevation,
transfer, split, merge, proxy grant, revocation, and retirement require an
explicit authority decision and identifiable basis.

Human authority may act directly or through an explicitly admitted bounded
proxy. Proxy actor identity and human-authority identity remain distinct;
graph-native surfaces may project the relation as `F_H`. A proxy grant names
its grantor, actor, subject, scope, permitted and excluded decisions, validity,
delegation rights, revocation, and provenance.

A direct or proxied decision preserves its source, subject and basis, acting
identity and mode, scope, change class, disposition, and supersession. Recording
a ruling cannot widen it. Proxy authority does not make implementer self-review
independent or confer unrelated runtime or domain authority.

---

## Default Formats And Overrides

### Defaults From A Bound ABG Realization

A consumer-bound realization of the ABG role may publish default identity
generators, validators, and normalizers for its own runtime surfaces and for
common default ODD surface kinds used by default `F_D` helpers.

These defaults are:

- starter conventions
- convenience contracts
- not universal doctrine

They are lawful only so long as derived domains may override them.

### Derived Domain Overrides

Derived domains may override identity format and structure for their own kinds.

An override is lawful only if it preserves:

- scoped uniqueness
- explicit kind distinction
- deterministic parsing or reading
- non-aliasing between family and member identities
- stable downstream traceability

Overrides must be published in domain authority.

They must not exist only as ad hoc regex assumptions hidden in implementation
code.

### Override Publication Surface

When a domain overrides defaults published by its bound ABG realization, the
override must be published in a lawful domain authority surface rather than
inferred only from implementation code.

At minimum, the domain should publish:

- the identity kinds in scope
- the serialization or readable form used for those kinds
- the scope or hierarchy that makes them unique
- the distinction between grouping identities and concrete executable or
  traceable identities

Suitable publication surfaces include:

- `PRODUCT.md` for the active identity kinds and their governed role
- requirement surfaces for obligations around identity stability or uniqueness
- design or ADR surfaces for parsing, serialization, or normalization rules
- a dedicated identity registry surface such as `IDENTITY.md` when the domain
  has enough complexity to justify one

The important rule is that identity overrides must be visible in domain
authority, auditable, and recoverable without reverse-engineering regexes from
implementation code.

---

## Parsing Law

Regex extraction from prose is not a complete identity model.

At most, regex may be a provisional extractor over a surface whose identity law
is already defined elsewhere.

Therefore:

- a parser must distinguish between concrete identity kinds and grouping labels
- family markers, display aliases, and prose headings must not be promoted into
  executable or traceable object identities unless the governing identity law
  says they are first-class identities of their own kind
- acceptance criteria, testcases, and similar subordinate identities must not
  be collapsed into requirement identity merely because their readable form is
  derived from a requirement token

If a domain needs family ids, it should publish them explicitly as
`requirement_family` identities rather than rely on string-shape accidents.

At admission, the identity reader returns the shared
[result record](FOUNDATIONS.md#result-algebra) on the declared scoped-identity
predicate. Preserve any domain parsing/refusal outcome. A demonstrated kind,
uniqueness or coordinate violation is `falsified` on a valid basis; unavailable
decisive evidence is `indeterminate`; an unusable authoritative basis is
`invalid_basis`; a request outside the reader's declared domain is
`out_of_frame`. A check not run retains `not_performed`. Syntactic parsing alone
can satisfy only its syntax predicate, not authenticity, grant validity or
currentness.

Before reuse, observe the current owning state and the relevant invalidators
under [workspace and context](FOUNDATIONS.md#workspace-and-context). A stable
identity cannot keep stale content, a revoked grant or an old observation
current. A changed coordinate neither establishes nor ends continuity;
continuity across it requires the owning transition relation above.

---

## Release Version Boundary

Release version is not the same thing as object identity.

Under [Release Identities](RELEASE_METHOD.md#release-identities) and
[Selector And Consumer Adoption](RELEASE_METHOD.md#selector-and-consumer-adoption):

- an immutable `v<version>-rc.<n>` cut tag is the only exact operative release
  identifier
- the mutable `v<version>` tag is a version-line discovery selector naming the
  highest-ordinal published immutable RC cut for that project and version line
- release version is a release-process fact
- release version is not the live constitutional identity of every object in
  the project

So the method must distinguish:

- object identity
- release identity
- publication/revision coordinates
- mutable discovery selectors

These may relate, but they are not interchangeable.

The selector's target is determined by publication, independently of the cut's
acceptance. Moving it does not change a consumer's operative basis; consumer
adoption remains the explicit transition owned by the consumer's governing
authority under Release Method.

---

## Minimum Questions

When defining or auditing an identity surface, ask:

1. What authority owns this identity?
2. What kind of thing does this identity denote?
3. What scope makes it unique?
4. Is the identity stable enough for the governed lifecycle?
5. Is the readable form only convenience, or is it being over-trusted?
6. Can a parser distinguish families, members, aliases, and revisions without
   ambiguity?
7. Is this an engine/runtime id, a domain semantic id, or a release id?

If those questions cannot be answered, the identity surface is under-defined.

---

## Examples

### Lawful

- runtime event ids generated as UUIDs by a consumer-bound realization of the
  ABG role
- requirement ids such as `REQ-F-CAPABILITY-001` when the domain defines them as
  concrete `requirement` identities
- family ids such as `REQ-F-CAPABILITY` when the domain defines them separately as
  `requirement_family`
- acceptance-criterion ids such as `REQ-F-CAPABILITY-001-AC-01` when the domain
  defines them as a separate `acceptance_criterion` identity kind

### Unlawful

- treating `REQ-F-CAPABILITY-*` or `REQ-F-CAPABILITY` as a concrete requirement merely
  because a broad regex matched it
- using release version as the identity of every live source object
- assuming a readable string is globally unique without its authority and kind

---

## Consequence For Implementations

Implementations should prefer:

- typed identity readers
- explicit identity-kind distinctions
- source-of-authority parsing contracts

They should avoid:

- broad regex mining as the real identity model
- silent coercion between family ids and concrete ids
- leaking engine id grammar into domain semantics

If a project currently relies on those patterns, the first lawful repair is to
contain the immediate bug. The enduring repair is to publish explicit identity
law and move implementations onto it.
