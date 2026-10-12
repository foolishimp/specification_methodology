# IDENTITY

Tier 1. Owns identity law: scoped identity with its uniqueness, type and
stability laws; readable and opaque identity; the identity hierarchy; the
split between engine-owned and domain-owned identity; authority identity
and its conservation (STDO-UP-004); domain overrides of default identity
formats and their publication; parsing; the boundary between object
identity and release version; the minimum questions for an identity
surface; lawful and unlawful examples; and the consequence for
implementations. It consumes [FOUNDATIONS](FOUNDATIONS.md) §2, where
Object (a subject with scoped identity of authority, kind and value),
Authority with its kinds, and Basis are defined once, and adds no
definition to tier 1. The same scoped identity is
[AC-002](AXIOMATIC_CALCULUS.md#ac-002-scoped-identity) within the
calculus, and the identity of one calculus edition is
[AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity);
neither is restated here. Release identity, its names and its forms are
the release law of [RELEASE](RELEASE.md); this member states only the
boundary between it and object identity. Every clause names the principle
that requires it (P0 to P6, FOUNDATIONS §3): identity is P3's commitment
and authority P6's. A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md` and is
provenance only; nothing here depends on that cut to be applied.

## 1. Position

Identity is scoped, typed, unique, and stable enough for the governed
purpose. Identity is not a flat global string convention; it is made
unique by hierarchy and type (P3; rc.2 #position). That means:

- the same literal token may be lawful in different scopes when its
  authority and kind differ;
- one string format is not sufficient to define identity across all
  products and runtime surfaces; and
- a human-readable form may help recognition, but readability is
  secondary to uniqueness and stable governed meaning.

The engine should carry identity safely. The domain should define
semantic identity law for its own constitutional objects (P3, P6).

## 2. Core law

### Scoped identity

Identity is always scoped. At minimum, identity should be interpretable
through authority, kind and value. So the minimum semantic model is:

```text
identity = authority + kind + value
```

This is the scoped identity of an Object (FOUNDATIONS §2). Optional
additional coordinates may include parent scope, revision, publication
version and temporal coordinates (P3; rc.2 #1-scoped-identity).

### Uniqueness

Identity is unique within its lawful scope. The requirement is not that
every identity looks globally unique as a naked string. The requirement is
(P3; rc.2 #2-uniqueness-law):

- no two live objects of the same kind may share the same identity within
  the same authority scope;
- aliasing across scopes remains explicit; and
- serialisation preserves enough hierarchy to prevent accidental
  collision.

### Type

Identity is typed. Different kinds of thing should not be collapsed into
one undifferentiated identity space. Examples of distinct identity kinds
include goal, intent, requirement, requirement_family,
acceptance_criterion, scenario, design_decision, published_function,
carrier_surface, release, install, run, function_call, continuation and
event. The method does not treat a family identity as if it were a
concrete requirement identity, or a release version as if it were object
identity (P3; rc.2 #3-type-law).

### Stability

Identity should remain stable for the governed lifecycle it serves. This
does not mean every identity is immutable forever. It means identity is
stable enough to support traceability, comparison, replay, publication
and supersession. If an identity changes, the method should make the
relationship explicit rather than silently reusing the old identity for a
different object (P3, P4b; rc.2 #4-stability-law).

## 3. Readable and opaque identity

Identity may be opaque, such as a GUID or UUID; human-readable, such as
`REQ-F-CAPABILITY-001`; or hybrid, where one component is readable and
another is opaque. The governing rule is that readability is a
convenience for recognition, and uniqueness and scoped meaning are the
actual law (P3, P1; rc.2 #human-readable-vs-opaque-identity). Therefore:

- a GUID is lawful even when it carries no human meaning;
- a readable identity is lawful only if it still preserves uniqueness in
  scope; and
- no reader should infer that a readable identity is safer or more
  authoritative than an opaque one merely because it looks meaningful.

## 4. Identity hierarchy

Identity should be made unique by hierarchy where appropriate. One useful
general model is:

```text
authority / kind / value / revision
```

Not every serialisation needs all four visible segments, but the semantic
model should be available (P3; rc.2 #identity-hierarchy). Examples:

- `(<product-authority>, requirement, REQ-F-CAPABILITY-001)`
- `(<product-authority>, requirement_family, REQ-F-CAPABILITY)`
- `(<runtime-authority>, run, 550e8400-e29b-41d4-a716-446655440000)`
- `(<release-authority>, release, 1.0.0-rc.1)`

The important point is that `REQ-F-CAPABILITY` and `REQ-F-CAPABILITY-001`
are not the same kind of identity, and that a runtime `run_id` and a
domain requirement identity do not belong to the same semantic category
even if both serialise as strings (P3).

## 5. Authority split

### Engine-owned identity

The substrate or runtime may define default identities for runtime-owned
objects, such as runs, function calls, jobs, execution frames,
continuations and events. For these, the engine may use opaque identities and engine-local
generation rules. Those rules should optimise for uniqueness, replay
safety and event-stream integrity. The engine should not impose
domain-specific semantic grammar on domain-owned objects (P3, P6;
rc.2 #engine-owned-identity).

### Domain-owned identity

Derived domains own the semantic identity grammar for their own
constitutional objects, such as requirements, requirement families,
acceptance criteria, scenarios, ADRs or design decisions, and published
domain assets. The domain defines which identity kinds exist, how they
are distinguished, what makes them unique, and how they are parsed or
read. The runtime may transport those identities, but it should not
silently invent their meaning (P3, P6; rc.2 #domain-owned-identity).

## 6. Authority identity and conservation (STDO-UP-004)

Authority is an identity-bearing semantic relation, not a display label,
capability string, actor identity or reachable code path. Its identity
preserves owner, kind, governed subject, scope and governing basis (P6,
P3; rc.2 #authority-identity-and-conservation-stdo-up-004; the Authority
object and its kinds are FOUNDATIONS §2).

Composition, delegation, adapters, projections, wrappers and registries
may restrict or faithfully carry admitted authority. They do not silently
widen scope, add a role, increase cardinality, change kind, or
reconstruct authority from actor identity, payload shape or available
capability. Elevation, transfer, split, merge, proxy grant, revocation and
retirement require an explicit authority decision and identifiable basis
(P6, P4b).

Human authority may act directly or through an explicitly admitted
bounded proxy. Proxy actor identity and human-authority identity remain
distinct; a profile's own surfaces may project the human-authority
relation under that profile's term (PROFILES). A proxy grant names its
grantor, actor, subject, scope, permitted and excluded decisions,
validity, delegation rights, revocation and provenance (P6, P3).

A direct or proxied decision preserves its source, subject and basis,
acting identity and mode, scope, change class, disposition and
supersession. Recording a ruling cannot widen it. Proxy authority does
not make implementer self-review independent or confer unrelated runtime
or domain authority (P6, P4b). EVALUATION §5 applies this law to
acceptance.

## 7. Default formats and overrides

### Derived domain overrides

Default identity formats that a bound runtime realisation publishes are
starter conventions and convenience contracts, not universal doctrine;
they are lawful only so long as derived domains may override them (P3,
P6). What such a realisation publishes, and for which surfaces, is
realisation law outside this member
([DESIGN_MODULE §12](DESIGN_MODULE.md#identity-defaults-from-a-bound-runtime-realisation)).

Derived domains may override identity format and structure for their own
kinds. An override is lawful only if it preserves (P3;
rc.2 #derived-domain-overrides):

- scoped uniqueness;
- explicit kind distinction;
- deterministic parsing or reading;
- non-aliasing between family and member identities; and
- stable downstream traceability.

Overrides are published in domain authority. They do not exist only as
ad hoc regex assumptions hidden in implementation code (P6, P3).

### Override publication surface

When a domain overrides defaults published by its bound runtime
realisation, the override is published in a lawful domain authority
surface rather than inferred only from implementation code (P6, P3;
rc.2 #override-publication-surface).

At minimum, the domain should publish (P3, P6):

- the identity kinds in scope;
- the serialisation or readable form used for those kinds;
- the scope or hierarchy that makes them unique; and
- the distinction between grouping identities and concrete executable or
  traceable identities.

Suitable publication surfaces include (P6, P3):

- the product definition (conventionally `PRODUCT.md`) for the active
  identity kinds and their governed role;
- requirement surfaces for obligations around identity stability or
  uniqueness;
- design or ADR surfaces for parsing, serialisation or normalisation
  rules; and
- a dedicated identity registry surface, such as a project's own
  `IDENTITY.md`, when the domain has enough complexity to justify one.

The important rule is that identity overrides are visible in domain
authority, auditable, and recoverable without reverse-engineering regexes
from implementation code (P6, P3).

## 8. Parsing

Regex extraction from prose is not a complete identity model. At most,
regex may be a provisional extractor over a surface whose identity law is
already defined elsewhere (P3, P1; rc.2 #parsing-law). Therefore:

- a parser distinguishes concrete identity kinds from grouping labels;
- family markers, display aliases and prose headings are not promoted
  into executable or traceable object identities unless the governing
  identity law says they are first-class identities of their own kind;
  and
- acceptance criteria, test cases and similar subordinate identities are
  not collapsed into requirement identity merely because their readable
  form is derived from a requirement token.

If a domain needs family identities, it should publish them explicitly as
`requirement_family` identities rather than rely on string-shape
accidents (P3).

## 9. Release version boundary

Release version is not the same thing as object identity (P3;
rc.2 #release-version-boundary). Under the release law
([RELEASE §1 and §2](RELEASE.md#2-release-identities), with
[SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release)):

- an immutable release cut is the only exact operative release
  identifier;
- the mutable version-line selector only names the highest-ordinal
  published immutable cut on its line (FOUNDATIONS §2);
- release version is a release-process fact; and
- release version is not the live constitutional identity of every
  object in the project.

So the method distinguishes object identity, release identity,
publication or revision coordinates, and mutable discovery selectors.
These may relate, but they are not interchangeable (P3, P6).

## 10. Minimum questions

When defining or auditing an identity surface, ask (P3, P6;
rc.2 #minimum-questions):

1. What authority owns this identity?
2. What kind of thing does this identity denote?
3. What scope makes it unique?
4. Is the identity stable enough for the governed lifecycle?
5. Is the readable form only convenience, or is it being over-trusted?
6. Can a parser distinguish families, members, aliases and revisions
   without ambiguity?
7. Is this an engine or runtime identity, a domain semantic identity, or
   a release identity?

If those questions cannot be answered, the identity surface is
under-defined (P3).

## 11. Examples

### Lawful

Lawful (P3; rc.2 #lawful):

- runtime event identities generated as UUIDs by a consumer-bound runtime
  realisation;
- requirement identities such as `REQ-F-CAPABILITY-001` when the domain
  defines them as concrete `requirement` identities;
- family identities such as `REQ-F-CAPABILITY` when the domain defines
  them separately as `requirement_family`; and
- acceptance-criterion identities such as `REQ-F-CAPABILITY-001-AC-01`
  when the domain defines them as a separate `acceptance_criterion`
  identity kind.

### Unlawful

Unlawful (P3; rc.2 #unlawful):

- treating `REQ-F-CAPABILITY-*` or `REQ-F-CAPABILITY` as a concrete
  requirement merely because a broad regex matched it;
- using release version as the identity of every live source object; and
- assuming a readable string is globally unique without its authority
  and kind.

## 12. Consequence for implementations

Implementations should prefer typed identity readers, explicit
identity-kind distinctions, and source-of-authority parsing contracts.
They should avoid broad regex mining as the real identity model, silent
coercion between family identities and concrete identities, and leaking
engine identity grammar into domain semantics (P3, P1;
rc.2 #consequence-for-implementations).

If a project currently relies on those patterns, the first lawful repair
is to contain the immediate bug. The enduring repair is to publish
explicit identity law and move implementations onto it (P3, P0).

## 13. Source dispositions

Rows of rc.2 IDENTITY_METHOD.md received by this member. Anchors are into
rc.2 IDENTITY_METHOD.md; a locus is a section of this file unless another
member is named. Every conserved row is restated in this member's own
text; a route is provenance only. Generalisations recorded here, each
removing a profile term from tier 1: in the type law, `graph_function` is
written `published_function`, `asset_surface` `carrier_surface` and
`graph_call` `function_call`; in engine-owned identity, "graph calls" is
written "function calls" and "frames" is written "execution frames", the
runtime's frames, distinct from the frame of FOUNDATIONS §2; in UP-004, "graph-native surfaces may project
the relation as `F_H`" is written "a profile's own surfaces may project
the human-authority relation under that profile's term (PROFILES)", the
permission kept as "may"; in the override publication surface and the
first lawful example, "bound ABG realization" and "consumer-bound
realization of the ABG role" are written "bound runtime realisation" and
"consumer-bound runtime realisation". "Id" is written "identity"; the
predecessor's "must" is written in the indicative and its "should",
"may", "at minimum", "at most", "optional", "useful" and "suitable" keep
their force. Release version boundary: superseded. The predecessor
clause, which cites RELEASE_METHOD for its content, calls the mutable
selector "latest-accepted"; that determination is replaced by the release
law it cites, under which the selector names the highest-ordinal
published cut and acceptance never moves it (RELEASE §1, the selector
paragraph; §3 Exact-cut qualification; §8 Acceptance criteria). The
row's other determinations are restated unchanged in §9. The `v<version>-rc.<n>` and `v<version>` forms are written in
RELEASE §1, not in this tier-1 member.

| Anchor | Disposition | Locus |
|---|---|---|
| #position | conserved; the four properties, not a flat string convention, hierarchy and type, the three consequences, the engine and domain "should" clauses | §1 |
| #core-law | not applicable: heading with no claim text (12 bytes, the heading line); its four children are disposed individually | §2 |
| #1-scoped-identity | conserved; always scoped, "at minimum ... should be interpretable", the model `authority + kind + value`, the four optional coordinates | §2 Scoped identity; FOUNDATIONS §2 Object |
| #2-uniqueness-law | conserved; uniqueness in lawful scope, not a naked global string, the three requirements | §2 Uniqueness |
| #3-type-law | conserved; typed, "should not be collapsed", the fifteen example kinds (three generalised, see above), the family and release-version prohibitions | §2 Type |
| #4-stability-law | conserved; "should remain stable", not immutable forever, the five supports, "should make the relationship explicit" | §2 Stability |
| #human-readable-vs-opaque-identity | conserved; the three forms, the governing rule, the three consequences with "no reader should infer" | §3 |
| #identity-hierarchy | conserved; "should be made unique by hierarchy where appropriate", the useful general model, the four examples, the two points | §4 |
| #authority-split | not applicable: heading with no claim text (19 bytes, the heading line); its two children are disposed individually | §5 |
| #engine-owned-identity | conserved; the six runtime-owned kinds (graph calls and frames generalised), opaque identities and local generation, the three "should optimise" aims, the "should not impose" rule | §5 Engine-owned identity |
| #domain-owned-identity | conserved; the six domain-owned examples, the four things the domain defines, transport without invented meaning | §5 Domain-owned identity |
| #authority-identity-and-conservation-stdo-up-004 | conserved in full; authority as an identity-bearing relation and its five preserved coordinates, restriction or faithful carriage only, the six prohibitions, the seven explicit-decision transitions, direct or proxied human authority, distinct proxy identity (the profile projection generalised), the nine grant fields, the eight preserved decision coordinates, no widening by recording, the two proxy limits | §6; EVALUATION §5 applies it; FOUNDATIONS §2 Authority kinds |
| #default-formats-and-overrides | not applicable: heading with no claim text (33 bytes, the heading line); its three children are disposed individually | §7 |
| #defaults-from-a-bound-abg-realization | conserved; the "may publish" permission for a consumer-bound runtime realisation's own runtime surfaces and default surface kinds is restated in DESIGN_MODULE §12 Identity defaults from a bound runtime realisation; its identity-law determinations (starter conventions and convenience contracts, not universal doctrine, lawful only while overridable) are in §7 Derived domain overrides | DESIGN_MODULE §12 Identity defaults from a bound runtime realisation; §7 Derived domain overrides |
| #derived-domain-overrides | conserved; override permission, the five preservation conditions, publication in domain authority, no hidden regex assumptions | §7 Derived domain overrides |
| #override-publication-surface | conserved; publication in domain authority, the four "at minimum ... should publish" items, the four suitable surfaces, the visibility rule | §7 Override publication surface |
| #parsing-law | conserved; regex not a complete model, "at most ... may be a provisional extractor", the three parser rules, "should publish them explicitly as `requirement_family`" | §8 |
| #release-version-boundary | superseded; "latest-accepted" selector replaced by the release law it cites (RELEASE §1 selector paragraph, §3 Exact-cut qualification, §8 Acceptance criteria: highest-ordinal published, never moved by acceptance); object identity versus release version, the other release-version facts and the four-way distinction restated unchanged | §9; RELEASE §1, §3, §8 |
| #minimum-questions | conserved; the seven questions and the under-definition rule | §10 |
| #examples | not applicable: heading with no claim text (12 bytes, the heading line); its two children are disposed individually | §11 |
| #lawful | conserved; the four lawful examples (the runtime realisation generalised) | §11 Lawful |
| #unlawful | conserved; the three unlawful examples | §11 Unlawful |
| #consequence-for-implementations | conserved; the three "should prefer" and three "should avoid" items, contain then publish and move | §12 |
