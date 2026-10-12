# PRODUCT_DEFINITION

Tier 2. Owns how one project binds to this method: the product definition
overlay and its independence from layout, the relations a definition
carries, what a constitutional set must make recoverable, the installed
release basis and the toolchain manager that realises it, bounded-context
semantic resolution, local constitutional binding, the project's collective
reference-frame basis, the WHAT, HOW and work-carrier bindings, recursive
discovery with explicit composition, the semantic-resolution conformance
cases, the one constitutional surface and version boundary
(STDO-SURFACE-001), and the bootstrap of a project. Consumes
[FOUNDATIONS](FOUNDATIONS.md) (object, authority and its kinds, basis,
residual), [REFERENCE_FRAME](REFERENCE_FRAME.md) (frame set, frame-set
declaration, activation packet), [ACTIVATION](ACTIVATION.md) (the step and
the result algebra) and [EVALUATION](EVALUATION.md) (claims, separation,
conformance); adds no definition to tier 1. The generic WHAT and HOW law
and the recursive product taxonomy are [SPEC_METHOD §2 and
§6](SPEC_METHOD.md); release identities, cohorts and selectors are the
release law (the [RELEASE](RELEASE.md) member); assurance and testing law is
[ASSURANCE](ASSURANCE.md). The schemas, templates, filenames, manifest
fields and commands named here are this Product's own realisation shapes,
accepted as interoperability boundaries under §11; they are not profile
terms. Three bounded contexts the predecessor placed in its SPEC_METHOD are
owned here: product-definition-routing (§1 to §4, §9, §12),
semantic-resolution (§5, §6, §10) and build-tenancy (§8). Every clause
names the principle that requires it (P0 to P6, FOUNDATIONS §3). A route
written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md` and is provenance
only; under the standalone successor requirement every predecessor row
received here is restated in full in this text, and nothing here depends
on that cut to be applied.

## 1. Overlay and layout independence

This member owns the product-definition-routing bounded context,
`urn:stdo:bounded-context:product-definition-routing`, under the selected
complete STDO basis, and defines that context's overlay, definition,
discovery, locator and composition concepts. The JSON schema named below
realises the accepted interoperability shape of the overlay and is not a
second semantic owner (P6; rc.2
#stdo-product-definition-overlay-and-layout-independence).

Every product defined under this method publishes one JSON definition for
each distinct current product WHAT. Its conventional filename is
`stdo_<label>.json`; `stdo_default.json` is the default for a source
project with one product definition. A directory may hold more than one
definition when it hosts more than one distinct product WHAT, and only
then. Several build tenants realising the same WHAT are entries in one definition and
never add definition files (P3).

The suffix `<label>` is the Definition Label: a stable lowercase local
discovery label of ASCII letters, digits, hyphens or underscores, unique
only among the definitions in the same directory. It is not Product
identity. The `product.definition_id` URI inside the definition is the
Product-Definition Identity: the stable identity of the mutable
product-definition line, unique within the discovered workspace definition
set. It identifies one continuing WHAT definition, not one immutable
released Product (P3).

The definition identity may stay stable while that source line authors
successive Product releases. Every immutable Product or release produced
from the line keeps its own Product and release identity. A fork, a
replacement or an independently governed WHAT definition receives another
`product.definition_id`; changing a released Product does not repurpose
the definition identity as release identity (P3; SPEC_METHOD §6).

Product-definition, immutable Product, bounded-context and build-tenant
identity URIs are identity carriers, not self-authorising strings. They
stay subject to the identity law (the [IDENTITY](IDENTITY.md) member) and to the owning
Product, release or domain authority. A URI locator, filename, path or
display label cannot mint or widen identity authority (P6, P3).

The directory containing a definition is its definition root. Relative URI
references resolve against the definition file's retrieval URI. The
`product.source_project` reference identifies the source-project root and
may resolve to the definition root or elsewhere. File proximity creates no
authority (P6).

The normative schema is `schemas/product-definition.schema.json`; the
single fill-in form is `templates/PRODUCT_DEFINITION_TEMPLATE.json`. This
concrete JSON shape is an accepted interoperability boundary under
STDO-SURFACE-001 (§11). It standardises only identity, location, relation
and discovery fields and absorbs no meaning owned by a referenced
constitutional, Product, requirement, design, ticket or commentary surface
(P6, P2).

## 2. Required definition relations

Each definition contains (P3, P6; rc.2 #required-definition-relations):

- `product`: the stable product-definition identity, display name,
  source-project locator and an explicit bounded-context declaration or
  `null`;
- `constitution.stdo`: the STDO source repository, the mutable
  version-line discovery selector, and the exact installed release basis
  with its deterministic manifest digest;
- `constitution.additional_authorities`: every non-STDO constitutional
  set;
- `constitution.entrypoints`: basis-qualified useful reading routes;
- `constitution.agent_bootstrap`: the constitutional entrypoint and the
  marker-managed agent-instruction targets;
- `local_constitution`: local axioms, overrides and disambiguations with
  their owning authority, target, basis and scope, including
  context-qualified term resolution where applicable;
- `reference_frame_bases`: one or more accepted collective
  reference-frame basis declarations with their admitting authorities and
  governed scopes;
- `what`: the current Intent, Product and specification bindings;
- `how`: any shared realisation surfaces and one or more independent
  build tenants;
- `ticketing`: the Goals, ticket, comment and optional sprint carrier
  bindings;
- `composition`: explicit relations to other product definitions; and
- `$schema` and `kind`: the schema locator and the
  `stdo.product-definition` discriminator.

The overlay owns this locator and relation map; the referenced documents
own their content. Repeating source truth inside the JSON creates a rival
authority and is non-conformant (P6).

`product.bounded_context` identifies the enclosing bounded context of the
definition's own product WHAT, or is `null` when no separate enclosing
context is claimed. It is not an exhaustive registry and does not flatten
subordinate, peer, composed, tenant, user or runtime contexts into one
namespace. Those contexts stay defined by their owning authorities, and
every local disambiguation names the exact context in which its resolution
applies (P1, P3).

## 3. Constitutional-set sufficiency

A Constitutional Set is the complete set of governing documents selected
for a product, not a prescribed number of files. Collectively the selected
set makes five things recoverable for the governed scope (P2, P1; rc.2
#constitutional-set-sufficiency):

- axioms: irreducible starting truths, invariants and refusal conditions;
- ontology: the kinds of things treated as real and their material
  identities, relations, boundaries and lifecycle;
- epistemology: how claims become knowable or acceptable, including
  admissible evidence, observation, uncertainty, falsification and
  decision authority;
- taxonomy: the classifications and kind distinctions that prevent
  category collapse; and
- semantics: the governed meaning of terms, relations, states, operations
  and outcomes.

These are sufficiency dimensions of the complete set, not filename classes,
required folders or a one-document-per-dimension partition. One document
may cover several dimensions and one dimension may be distributed across
several owning documents (P2).

`constitution.stdo.basis` locates the complete selected STDO constitutional
set; `constitution.additional_authorities` locates every additional
constitutional set or source. The STDO basis identifies one complete
immutable RC cut and its exact installed-release manifest, never a
hand-selected subset. Each `constitution.entrypoints[]` member names the
basis against which its URI resolves. Entry points are derived navigation
and can neither narrow nor replace a complete selected constitution (P3,
P6).

This rule promotes no concrete design ontology into constitutional WHAT.
Product-level ontology that fixes Product meaning belongs in, or is cited
by, the bound WHAT. An accepted design ontology of a realisation boundary
(the design profile's) stays semantic-design authority for that boundary,
derives from constitutional WHAT and the applicable domain methods, and
cannot invent missing Product meaning (P6, P2).

## 4. Shared installed release basis and toolchain manager

Within the product-definition-routing context an Installed Release Basis
is the pair (P3; rc.2
#shared-installed-release-basis-and-toolchain-manager):

```text
(immutable stdo://releases/<cut>/ URI, installed-manifest SHA-256)
```

The URI identifies one immutable annotated RC cut. The digest identifies
the deterministic installed-release manifest, which binds the cut's tag
object, commit, repository tree, standards subtree, exact standards
inventory, member bytes and admitted auxiliary payloads. The manifest shape
is owned by `schemas/installed-release-manifest.schema.json`. The manifest
is transport and integrity evidence, not a replacement constitution (P6).

An Adoption Plan is the read-only, deterministic acceptance object that
binds one current Product Definition's identity and bytes to its current
basis and to one resolved immutable target's cut, annotated tag object,
commit, tree and installed-manifest digest. Its SHA-256 is the
operator-presentable acceptance token. Possession of the token alone grants
no authority; a mismatch proves that the presented subject is no longer the
subject being mutated (P6, P3). A Fleet Adoption Plan binds an authorised
fleet root and the complete ordered set of per-definition plan digests
under the same law.

Plan hashing covers the acceptance object only: local installation status
and machine-local install paths are excluded. The canonical bytes are UTF-8
JSON with recursively sorted object keys, two-space indentation, LF line
endings and one final LF. Fleet order is deterministic discovery-path
order. These rules make a presented digest independently reproducible
rather than an opaque session token (P3, P6).

The STDO Toolchain Manager is the bounded executable realisation that (P2,
P3):

- installs each immutable cut once in a shared, versioned release store;
- resolves logical `stdo://releases/...` URIs to verified installed bytes;
- inventories and verifies complete installed distributions;
- synchronises the exact basis already selected by a Product Definition;
- emits an exact digest-bound adoption plan from a mutable version-line
  selector and performs adoption only when that plan is explicitly
  accepted;
- manages the stable marker-bounded bootstrap in declared agent files; and
- applies those operations to an explicitly discovered fleet of Product
  Definitions.

The store may live at any machine-local path. Its registry maps logical
release URIs to installed paths and manifest digests and owns neither
Product selection nor method meaning. A consumer repository therefore needs
no project-local standards copy and no prescribed folder structure, and
several Product Definitions on one machine may select different installed
cuts concurrently (P3, P6). Every manager-owned component from the
configured store root downward is a physical directory or regular file of
its declared type; a symlink, junction, reparse point, device, socket or
other redirection or special entry fails closed. Verification inventories
every filesystem entry type, directories included, rejects any entry not
derived from the manifest's exact file paths, and never follows an
unmanifested alias (P5, P3).

`constitution.stdo.source.repository` identifies the transport source.
`constitution.stdo.selector` is a mutable `stdo://channels/<version>`
discovery selector whose alias semantics are owned by the release law (the
[RELEASE](RELEASE.md) member). Neither is operative authority.
`constitution.stdo.basis.uri` and `constitution.stdo.basis.manifest_sha256`
are the sole authored STDO selection for that Product Definition (P6, P3).

The manager observes these command boundaries (P6, P5):

- `install` admits one explicitly named immutable RC cut without changing
  any Product Definition;
- `sync` installs and verifies only the exact basis already selected by
  the Product Definition and never consults its mutable selector;
- `adopt --dry-run` resolves the annotated selector and immutable RC, and
  presents the target cut, tag object, commit, tree, manifest digest,
  current Product-Definition byte digest and a deterministic
  adoption-plan digest, without mutation;
- mutating `adopt` requires that exact prior plan digest as explicit
  acceptance, re-derives it before installation, installs only the bound
  target, rechecks the Product Definition bytes, and atomically changes
  only its basis and its basis-relative schema locator; any drift refuses
  mutation;
- `status`, `verify`, `list`, `manifest` and `resolve` are read-only with
  respect to Product Definitions; and
- fleet adoption emits, and requires explicit acceptance of, one aggregate
  plan digest over every per-definition plan; all fleet writes require
  explicit whole-selection authorisation and infer no composition or
  inheritance from directory nesting.

Missing cuts, moved immutable tags, tag-to-commit mismatch, manifest-digest
mismatch, missing, extra or changed installed members, ambiguous Product
Definition discovery, unaccepted or stale adoption plans, URI escape,
physical store redirection, undeclared filesystem entry types and malformed
bootstrap markers fail closed (P5). Every `stdo:` schema locator is parsed
before schema loading under URI scheme case-insensitivity and names the
same immutable cut as `constitution.stdo.basis`; spelling variation cannot
cross that basis. No cache, registry entry, source checkout, version alias,
schema or agent file may silently replace the basis selected in the
Product Definition (P6, P3).

`constitution.agent_bootstrap` embeds no other constitution. It names one
basis-qualified bootstrap entrypoint and the local instruction files (such
as `AGENTS.md` or `CLAUDE.md` targets) whose small discovery block the
manager owns between explicit markers. Each target is a portable relative
path resolved against `product.source_project`; absolute paths, parent
traversal, redirected path components and escape from that boundary fail
closed. A fleet additionally confines every resolved source project to its
explicitly authorised fleet root and preflights every target before the
first write. Exactly one correctly ordered marker span may be replaced;
the bytes before and after it, trailing whitespace included, stay
project-owned and byte-identical, and appending a new span preserves all
existing bytes as an exact prefix. The bootstrap routes agents to the
applicable Product Definition, the exact installed basis and the owning
sources; it can neither restate nor override them (P6, P3, P5).

Recursive fleet discovery prunes these exact directory names as
version-control, dependency, generated, cache or managed-store internals:
`.git`, `.hg`, `.svn`, `.bzr`, `.venv`, `venv`, `node_modules`, `vendor`,
`site-packages`, `build`, `dist`, `out`, `target`, `.gradle`, `.tox`,
`.nox`, `.cache`, `.ruff_cache`, `.mypy_cache`, `.pytest_cache`,
`__pycache__`, `.genesis` and `.stdo`. A discovered Product Definition may
not itself be a symlink. These exclusions are discovery law, not evidence
that an excluded tree lacks another independently governed Product (P5,
P6).

### Explicit complete consumer update

A Complete Consumer Update Plan binds one explicitly selected Product
Definition and the complete companion population of one exact upstream
release-matched cohort to the consumer bindings selected by the
invocation's owner. The Product Definition continues to own composition;
the upstream cohort and each Product's release record own release and
member identity. An invocation selection and its derived plan and result
are operation evidence, not another persistent dependency declaration,
registry or lock. The caller selects every native route and derived context
for the claimed update scope; directory proximity or an empty discovery
result cannot supply that selection, and an empty derived-context
population means the owner selected none, not that the manager established
the absence of semantic context (P6, P3; rc.2
#explicit-complete-consumer-update).

The separate `cohort-update` operation presents the whole plan without
consumer effects. Unlike the basis-only Adoption Plan above, its acceptance
object also binds the physical effect destinations and binding preimages,
the exact selected cohort bytes, the companion annotated tags, commits,
subtrees and inventories, the replacement dependency locators, the native
routes and the declared derived-source observations. It uses the same
canonical JSON hashing rule. Already-installed status supplies no
additional authority and does not change the digest. Mutation requires
explicit acceptance of this exact plan and re-derives it; possession of its
digest alone grants no operation authority. The `adopt`, `sync` and fleet
contracts above keep their narrower boundaries (P6, P3).

The complete operation verifies the selected cohort's dependency closure
and each exact companion's definition, release record and admitted members
before relying on them. It stages absent immutable installs, verifies
existing installs without repairing them in place, and preflights every
consumer target. Only the selected basis and schema, the existing
composition locators and contracts, and the selected native and install
links may change; historical installs and unrelated consumer content stay
available and unchanged. It creates no consumer-local checker and changes
no Product meaning or local semantic map (P3, P6, P2).

For each selected derived context, missing, ambiguous, changed or
unavailable program, map or source evidence holds the complete update
before any consumer effect. The source owner performs any semantic re-entry
that is needed; the manager cannot mechanically relabel an older map as
current. Exact source freshness is integrity evidence, not semantic
conformance and not an independent semantic verdict (P1, P6). After
immutable staging the manager rechecks the consumer preimages and the
source evidence. It reports completion only after verifying every selected
resulting binding and companion. Refusal before consumer effects retains
the prior state; a caught application failure restores the affected
consumer preimages and does not report completion; newly staged immutable
installs may stay unused. The operation requires an exclusive consumer
write scope during application. It claims no crash-atomic transaction
across independent filesystem paths: abrupt process or host loss, or
unavailable rollback storage, requires recovery from the presented
preimages before the complete relation can be claimed (P5, P4b).

## 5. Bounded-context semantic resolution

This member owns this law in the semantic-resolution bounded context,
`urn:stdo:bounded-context:semantic-resolution`, under the selected complete
STDO basis. A glossary may index this identity and does not participate in
its declaration (P1, P6; rc.2 #bounded-context-semantic-resolution).

A term is a lexical label used in an occurrence, not a context-free concept
identity. A bounded context is an explicitly identified semantic scope in
which a governed vocabulary, concept set and relation set are jointly
interpretable under named authority. A concept reference is an exact,
resolvable reference to a meaning owned by an authority under a selected
basis; the reference locates that meaning and mints neither the meaning nor
its authority (P1, P3, P6).

A bounded context exists only when an owning authority declares its stable
identity, owner, selected basis and governed semantic scope. A consuming
member may define a concept inside that context only through an explicit
owner relation. A filename, heading, index row, glossary section, schema
value or bare URI cannot constitute the context (P6).

Every material term occurrence resolves under this semantic address (P1):

```text
(term, bounded-context identity, owning authority, selected basis, governed scope)
```

Equal spelling, capitalisation, shape, file location, directory nesting,
actor or implementation does not establish equal meaning, concept identity,
equivalence, inheritance or authority; different spelling does not prove
different meaning. Those relations follow only from the applicable semantic
address or from an explicit authorised relation (P1, P3).

Resolution proceeds in this order (P1, P5):

1. identify the occurrence's governed scope and nearest explicit
   bounded-context declaration;
2. identify the exact selected basis and the authorities applicable to
   that context and scope;
3. collect the context-local definitions and the explicitly imported
   concept references admitted by those authorities and that basis;
4. apply every applicable owner-authorised override or disambiguation; and
5. admit the occurrence only when exactly one concept remains.

A document, section, schema field, operation or other owning surface may
declare a context for all subordinate occurrences, so uniquely resolved
prose need not repeat a qualifier on every term. A repository, directory,
filename, heading, glossary match, prompt, actor or nearby definition does
not declare a bounded context by accident (P1, P6).

Zero applicable concepts is unresolved meaning; more than one is ambiguous
meaning. Both fail closed at a material boundary: an agent, design, schema,
implementation, test, translation or reviewer must not select one by
familiarity, frequency, recency, nominal match or a context-free glossary
fallback (P5, P1).

The glossary (the [GLOSSARY](GLOSSARY.md) member) is a non-deciding locator index. Each
record points to an exact source clause that declares the bounded context
and owns the indexed concept. The glossary defines neither and cannot
repair a missing declaration. An indexed concept applies only when the
semantic address selects its owning clause or the target context explicitly
imports it; appearance in the glossary creates no shared default (P6, P1).

A cross-context relation is explicit and owner-authorised. Its carrier
states (P1, P6, P4b):

- the exact source and target concept references and bounded-context
  identities;
- whether the relation imports unchanged meaning, disambiguates a use,
  translates directionally (a specialisation included) or establishes the
  stronger equivalence claim;
- its direction and any lawful inverse where material;
- the preserved meaning, changed meaning, loss and refusal conditions;
- the source and target semantic owners, without transferring either
  authority;
- the selected source and target bases, the governed scope and
  provenance; and
- its lifecycle and invalidation conditions.

A Semantic Import adopts the cited meaning unchanged for its declared
target scope. A Semantic Translation declares how meaning changes in one
direction. Semantic Equivalence requires the governing authorities to
establish the claimed equality; neither identical spelling nor two opposing
translations proves it automatically. A Semantic Disambiguation selects one
meaning for one scope and does not make competing concepts equal. No
relation widens its source or target authority (P1, P6; these four kinds
are related to the typed relations that AC-012, AXIOMATIC_CALCULUS §4,
names, with Semantic Import defined here).

A specialisation is a directional translation whose target preserves the
declared source meaning while narrowing its admissible instances or adding
target-context constraints. It identifies the exact target concept, the
preserved and narrowed meaning, the excluded source instances, and the
absence or law of any inverse. Calling a term a specialisation without
those coordinates establishes nothing (P1, P3).

## 6. Local constitutional binding

A local axiom, override or disambiguation gains no authority from its file
category or from being listed in the overlay. Every local entry names (P6;
rc.2 #local-constitutional-binding):

- the URI carrying the local decision;
- the existing Product, requirement, accepted-design or other lawful
  authority that owns it;
- the clause or ambiguity it overrides or resolves, where applicable; and
- the exact scope to which it applies.

Each `local_constitution.disambiguations` binding additionally names (P1,
P3):

- `term`: the exact lexical label being resolved;
- `context`: the bounded-context identity in which the resolution applies;
- `disambiguates`: the complete material candidate concept or clause
  references;
- `resolves_to`: the exact selected concept reference, which is one member
  of `disambiguates`;
- `basis`: every selected semantic basis needed to interpret the
  candidates and the resolution; and
- `uri`, `authority` and `applies_to`: the owning resolution carrier, the
  lawful authority and the exact governed scope.

The referenced `uri` owns the resolution. When the candidates cross bounded
contexts, that carrier also declares the complete import, translation or
equivalence relation §5 requires. The overlay metadata makes the relation
discoverable and checkable; it neither restates the source-owned meanings
nor mints the decision (P6).

An empty local array explicitly declares that no local entry of that kind
is bound for the product. Omission is not an equivalent declaration (P6,
P4b).

## 7. Collective reference-frame basis

A Project Reference-Frame Basis is the Product-owned accepted declaration
of the shared frame set through which finite actors collectively engage one
governed Product scope or outcome (P0, P6; rc.2
#collective-reference-frame-basis). It binds:

```text
Project Reference-Frame Basis
  = exact reference-frame law and optional profile basis
  + admitting authorities and governed scopes
  + frame declarations and evaluation inventory
  + actor-binding rules and capability envelopes
  + semantic, evaluation, operation and decision grants
  + result, conjunction, translation and coverage relations
  + lifecycle activation triggers and invalidation law
```

[REFERENCE_FRAME](REFERENCE_FRAME.md) supplies frame principles only, and
its §4 the shape of a frame-set declaration; a profile member (the
Executive baseline, tier 3) supplies one optional profile only. Neither
selects, adopts or owns a Product binding. The adopting Product's existing
authority owns the concrete declaration and every grant it contains (P6).

`reference_frame_bases` is the non-empty locator set for the accepted
frame bases through which finite actors collectively engage the governed
Product and its work. Each entry names (P6, P3):

- the URI carrying one accepted frame-basis declaration;
- every existing Goals, Product, requirement, accepted-design or other
  lawful authority that admits the declaration; and
- the exact Product, bounded context, build tenant, outcome or other
  governed scope to which it applies.

The referenced declaration owns the selected frame set, the method or
profile basis, the governed outcome, the actor-binding rules, the
capability envelopes, the grant requirements, the triggers, the coverage,
the result relations and the invalidation law. It may adopt an available
profile or define a project configuration. The JSON entry locates that
declaration and its authority relation; it does not contain the binding,
adopt the profile, restate the frames or create frame-set authority (P6).

Profile availability, Product adoption and execution-scoped activation are
three distinct relations. Inclusion in a selected method cut makes a
profile available; only Product authority may adopt it; only an exact
authorised work instruction may activate one bound frame for an actor and
subject (P6, P3).

The collective basis and an actor activation are distinct. An Agent Frame
Activation is the execution-scoped binding of one agent to an applicable
frame declaration or active configuration, an exact evaluation, subject,
basis, evidence boundary and capability envelope; what the agent receives
is the activation packet of REFERENCE_FRAME §11, and the step it performs
is ACTIVATION §1. The Product Definition records the durable shared basis;
a ticket or other authorised work instruction carries the activation
packet. That execution binding does not mutate the overlay, and the overlay
registers no agents, assigns no permanent frames and persists no temporary
active frame configuration (P3, P0).

Frames and actors keep separate identities. Several agents may activate
overlapping subsets of one frame set; one agent may activate different
frames over time. Neither an actor name nor a broad frame grants semantic,
operation, review, acceptance or disposition authority beyond the cited
owners and the exact activation (P6, P3).

The Project Reference-Frame Basis also records the Product-role map when
the governed outcome crosses a chain of Products. The map keeps mutable
source projects, Product Definitions, candidate checkpoints, release cuts,
released Products, installs, artifacts and dependent Products as distinct
identities (SPEC_METHOD §6), and records each development product as a
role binding over its exact underlying install identity. Every directed
Product-composition edge names its source and target roles, governing
authority and contracts, lifecycle, evidence boundary, refusal and
invalidation conditions. Common actors, repositories, files,
implementations, outputs or tool access create no composition or identity
relation (P3, P6).

An accepted Project Reference-Frame Basis may be expressed entirely as
source-linked prose. The starter at
`templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md` projects this binding
law into one copyable shape. The template is not authority, and no schema,
axiomatic representation, prompt framework or runtime frame engine is
needed to use the method. An adopting Product replaces every placeholder
with its own exact identities, owners, scopes, sources, grants, results and
invalidation conditions, then admits that completed declaration under
existing authority (P2, P6).

A Product, domain or runtime carrier also named `Frame` is not included by
nominal match. It stays governed by its bound WHAT and HOW and may be the
subject or a coordinate of an evaluation frame. It enters the collective
frame set only through an explicit frame declaration with the required
evaluation and authority relations (P1, P3).

## 8. WHAT, HOW and work carriers

This member owns the build-tenancy bounded context,
`urn:stdo:bounded-context:build-tenancy`, under the selected complete STDO
basis. The multi-build-tenant work-item relation of
[TICKETS §4](TICKETS.md#multi-build-tenant-independence) is a
concept of this context owned there (statement of ownership, P1, P3). It governs the realisation relation that SPEC_METHOD §2 states
generically: one constitutional product WHAT is realised by one or more
independent project-owned HOW tenants. A build tenant is one such
realisation. Build tenancy is the one-or-more relation; one tenant is its
singleton case, and multi-build-tenancy begins when the same WHAT has more
than one independent realisation (P3, P2; rc.2
#what-how-and-work-carriers).

`what.intent`, `what.product` and `what.specification` locate the current
constitutional WHAT. Intent and Product each have one canonical entrypoint;
specification may cite more than one requirement or specification surface
(P3).

The Tenant Registry is the canonical `how.build_tenants` collection for the
product's independent HOW realisations. Each entry has stable identity and
locates its root, design and implementation surfaces. The Common
Build-Tenant Surface is the realisation law bound by `how.common` and
explicitly adopted across more than one tenant. A separate
`TENANT_REGISTRY.md` may remain as a human-readable companion or generated
projection and cannot become a second tenant-identity or location
authority (P3, P6).

`ticketing.goals` locates the current work-wave carrier.
`ticketing.tickets` locates the durable ticket root and the minimum
backlog, active and completed lanes. `ticketing.comments` locates the
commentary root. `ticketing.sprints` optionally locates bounded
execution-batch manifests. These bindings may resolve to directories,
repository resources, tracker collections, API endpoints or product-scoped
queries. Goals own the bounded work wave, ticket state stays ticket
authority, and comments stay non-authoritative commentary (P6, P3). Which
carrier a given work item takes is SPEC_METHOD §4 and the [TICKETS](TICKETS.md) member;
this section binds where each carrier kind lives.

## 9. Recursive discovery and explicit composition

Tools discover `stdo_*.json` recursively within the selected workspace
boundary: definitions at the workspace root and definitions at arbitrarily
deep nested project roots (P3; rc.2
#recursive-discovery-and-explicit-composition).

For a requested Product scope exactly one applicable definition is
selected; zero or several unresolved definitions fail closed, and a
symlinked definition is refused (P6, P5; provenance: several unresolved
definitions and the symlink refusal are rc.2
#shared-installed-release-basis-and-toolchain-manager, restated in §4
here; zero definitions is rc.2 templates/CLAUDE_TEMPLATE.md and
templates/AGENTS_TEMPLATE.md item 7, a missing Product Definition fails
closed; rc.2 authority_compressions/stdo_bootstrap.md discovery claims 1
and 2 state the whole rule).

Directory nesting creates no implicit inheritance, ownership, composition
or constitutional override. Parent and child definitions stay independent
until `composition` explicitly relates them. Each composition entry records
(P6, P3):

- `product_definition`: the current locator for the target definition;
- `target_definition_id`: the stable identity expected from the target's
  `product.definition_id`;
- `relation`: the authority defining the directed composition kind, the
  source and target roles, owner, scope, lifecycle and invalidation
  conditions; and
- `contracts`: one or more exact interface, capability, identity,
  lifecycle, data, evidence or other governing contract references
  consumed by that relation.

Resolution verifies both the locator and the expected identity. Moving a
definition requires a locator update and does not change its identity.
Replacing the content at the same locator with another definition identity
fails closed. When an edge binds exact immutable Product or release
versions, the cited relation and contracts also carry and verify those
identities; the mutable definition identity cannot substitute for them
(P3, P5).

A conforming discovered set satisfies all of the following (P3, P6, P1):

- every definition validates against its selected released schema;
- every required URI and fragment resolves under the declared workspace
  and resolver boundary;
- every `product.definition_id` is unique;
- every build-tenant identity is unique within its overlay;
- every governed scope has a resolvable applicable reference-frame basis,
  and overlapping basis bindings are reconciled by their cited authority;
- every local disambiguation binds one exact term, target context,
  complete material candidate set, selected concept, authority, basis and
  scope; `resolves_to` is a member of `disambiguates`; and its referenced
  resolution carrier is congruent with those bindings;
- every material cross-context term seam resolves through an explicit
  import, disambiguation, translation or equivalence relation rather than
  nominal match;
- every composition target resolves to another product definition whose
  `product.definition_id` equals `target_definition_id`, and every
  relation and non-empty contract set resolves; and
- no two carriers claim authority for the same Product, tenant, ticket
  state or constitutional relation.

Portable Draft 2020-12 JSON Schema validation establishes structural shape.
The schema's `uri` and `uri-reference` formats are annotations unless the
declared validator implements format assertion. Conformance therefore
performs an explicit RFC 3986 URI and URI-reference syntax check with an
assertion-capable validator, followed separately by resolution, fragment
existence, selected-release identity, uniqueness across files,
constitutional sufficiency, semantic-resolution and cross-context-relation
completeness, and authority-congruence checks. The structural subset and
the semantic subset of these checks are distinct claims (EVALUATION §2;
P1, P6).

## 10. Semantic-resolution conformance cases

Conformance covers both uniquely resolved use and material collision. At
minimum it establishes these cases under an exact selected basis (P1, P6;
rc.2 #semantic-resolution-conformance-cases):

| Term | Candidate contexts | Required result without an explicit cross-context relation |
|---|---|---|
| `Frame` | the reference-frame-evaluation context (REFERENCE_FRAME §1) and a consumer-owned runtime carrier | remain distinct; nominal match cannot enrol the runtime carrier as an evaluation frame |
| `Owner` | a generic specialist evaluation family and a semantic or decision authority owner | remain distinct; the evaluation family acquires no owner authority |
| `Product` | an immutable released Product and a mutable Product Definition | remain distinct and select only through the occurrence's declared context |
| `Tenant` | an STDO build realisation and hosted, customer, account, runtime or data tenancy | remain distinct; build tenancy supplies no default for the other contexts |
| `User` | a Product role, human person, identity principal, account, actor, operator or data subject | unresolved until downstream authority defines or explicitly relates the applicable meanings |

A positive local case declares one context and resolves exactly one
concept. A positive cross-context case supplies the complete authorised
relation. Negative cases cover zero candidates, multiple candidates after
disambiguation, a selected concept outside the candidate set, a
context-free glossary fallback, incomplete relation coordinates, authority
or basis mismatch, undeclared loss and invalidated relations. Correct
downstream behaviour produced through a guessed meaning does not pass
semantic conformance (P6, P1). [CONFORMANCE](CONFORMANCE.md) may index
these cases; it does not redefine them.

## 11. One constitutional surface and version boundary

STDO-SURFACE-001. The shared methodology is modular in authorship and
singular in authority. Each law has one owning member; other members
consume it by reference. The members become operative only as one complete
released version of the method (P6, P3; rc.2
#one-constitutional-surface-and-version-boundary-stdo-surface-001).

A released cut identifies its exact member set, member digests, review
basis, human acceptance and immutable identity. Compressions, templates,
comments, candidate work, installed copies and mutable source are derived,
evidential or authoring surfaces. They cannot become a selectable partial
constitution and cannot reinterpret the owning members (P3, P6).

Within their declared scope, derived instructions preserve the owning
clauses' applicability, obligations, permissions, exclusions, decision
owners and invalidators. A projected prohibition cannot lose its condition
or its lawful alternative, even when every source digest is correct. A
summary, bootstrap or index cannot require a stricter or weaker relation by
compression. Its references are resolvable within the declared actor's
access; otherwise the required meaning is supplied directly (P4b, P1;
FOUNDATIONS §4, reference versus body).

Staleness binding. A derived surface or projected frame carries the path
and digest of each deciding source it was derived from, and of each index
it watches (GLOSSARY §2). A change to any of those digests makes it stale,
and it must be regenerated or explicitly re-accepted before an
installation treats it as current. A matching digest establishes
identity, not fidelity or sufficiency (above; EVALUATION §7). The raw
owning members of the same selected cut remain
the deciding authority and decide when a derived surface or frame is
stale or insufficient for a question (P3, P5, P6; provenance rc.2
authority_compressions/README.md and stdo_bootstrap.md step 5, a claim no
rc.2 body states).

The method owns normative construction algebra, authority relations,
abstract state and transition laws, admissibility conditions, necessary
causal order and evidence invariants. Consumers own concrete Product
realisation: instantiated types and schemas, files, tools, runtime and
orchestration machinery, tests and executable conformance implementation.
A concrete form is method law only when the method explicitly accepts it
as an interoperability boundary, as §1 does for the definition schema and
template (P2, P6).

A shared-method amendment cannot create an executable tool, workflow
engine, runtime, assurance system or consumer realisation as STDO Product
scope without separate explicit human authorisation. An agent recording a
ruling cannot widen its subject, implication, authority or change class
(P6).

Only a released method version is publication authority. Mutable method
source may author a future cut; it must not silently govern a consumer
(P6, P3).

## 12. Bootstrap

Every product defined under this method begins from
`templates/PRODUCT_DEFINITION_TEMPLATE.json`, copied to the product's
definition root as `stdo_default.json` for a singleton default project or
as `stdo_<label>.json` for a named product definition. An existing project
fills the URI bindings over its current layout; adoption requires no
moving, renaming or duplicating of existing authority or realisation
surfaces (P2, P3; rc.2 #bootstrap-rule).

The default scaffold binds:

- a shared versioned STDO store, addressed through the exact
  `constitution.stdo.basis`, as the installed distribution of the selected
  process constitution;
- `specification/GOALS.md` as current work-wave orientation;
- `specification/INTENT.md` as domain direction;
- `specification/PRODUCT.md` as the current product-definition surface;
- `specification/requirements/` as the live requirement surface;
- `build_tenants/` as the root for shared and tenant-local realisation
  surfaces; and
- `.ai-workspace/` as the sprint, ticket and comment carrier root.

These are template defaults, not universal path law; the definition's URI
bindings select the actual project carriers (P2).

The authority split is (P6, P3):

- mutable methodology authoring lives in the method's own source workspace
  (the standards of its source project) and governs only a future
  candidate cut;
- released methodology authority is the exact immutable STDO version
  selected by the consumer;
- installed methodology distribution lives in the toolchain manager's
  shared versioned store by default and matches the basis URI and manifest
  digest;
- project-owned constitutional surfaces live at the definition's `what`
  bindings; and
- project-owned realisation and work surfaces live at its `how` and
  `ticketing` bindings.

A project creates no competing local methodology root, such as a default
`specification/standards/`, and binds no mutable or partial method source
as if it were the selected immutable release (P6).

Method authority is singular: the selected immutable STDO release
authority, projected into the installed distribution located by the
overlay; and the project constitutional authority at the definition's
bound WHAT surfaces (P6). When editing or repricing methodology, the
mutable source path is authoring authority for the candidate being
constructed; it is not operative consumer law before release and explicit
selection (P3, P6). When operating inside a governed workspace, the
resolved installed basis is the operative distribution of the selected
immutable release until the consumer explicitly adopts another cut. A
project-local exact copy stays lawful when explicitly bound and verified;
it is not the default, and file proximity cannot select it (P6, P3).

The corresponding default folder shape is:

```text
stdo_default.json

specification/
├── GOALS.md
├── INTENT.md
├── PRODUCT.md
└── requirements/
    └── *.md

build_tenants/
├── common/
└── default/

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
```

This is a starter topology, not a conformance requirement. A monorepo may
place several `stdo_<label>.json` definitions at one root and bind each to
a different WHAT. A hierarchical repository may place one or more
definitions at any nested project root. Recursive discovery (§9) finds both
shapes; explicit composition, never directory nesting, relates their
products (P3, P2).

A project need not start with a complete `requirements/` tree on day zero.
Requirements may be sourced from any legitimate constitutional input
regardless of its path, including `GOALS.md`, `INTENT.md`, `PRODUCT.md`,
existing requirement documents, imported standards or policy material,
prior project versions, and migration or repricing source material. Most
projects begin by deriving `INTENT.md` from `GOALS.md`, then `PRODUCT.md`
from `INTENT.md`, then the first requirement surface from the product
definition; that is the usual starting point, not the only lawful source
(P2).

The bootstrap sequence is (P3, P6, P2):

1. Install the STDO toolchain manager once, resolve one version-line
   selector, and explicitly select one immutable RC cut.
2. Install that complete cut in the shared release store and retain its
   deterministic installed-manifest digest.
3. Copy `PRODUCT_DEFINITION_TEMPLATE.json` from that exact cut to the
   product definition root as `stdo_default.json` or `stdo_<label>.json`.
4. Assign the stable `product.definition_id` for the mutable WHAT
   definition line, its source-project locator and its bounded-context
   declaration; keep it distinct from every immutable Product and release
   identity.
5. Bind `constitution.stdo.source`, its non-operative selector, the exact
   basis URI and manifest digest, every additional constitutional
   authority and the relevant basis-qualified entrypoints; confirm that
   the set collectively defines axioms, ontology, epistemology, taxonomy
   and semantics for the governed scope (§3).
6. Bind the agent bootstrap entrypoint and portable targets relative to
   the resolved `product.source_project`, then let the manager preflight
   every target and install or refresh only their marker-bounded
   discovery blocks.
7. Bind, or explicitly empty, the local axiom, override and
   disambiguation collections (§6).
8. Bind at least one accepted collective reference-frame basis, its
   admitting authorities and its exact governed scope (§7).
9. Write or confirm the current Goals carrier, run the goals to intent to
   product steps, and bind the resulting Intent and Product entrypoints.
10. Gather, derive, classify and bind the live specification or
    requirement surfaces without creating a co-equal rival.
11. Bind at least one build tenant, including its root, design and
    implementation surfaces, and bind any shared realisation law (§8).
12. Bind the Goals carrier, the ticket lanes, the comments root and the
    optional sprint root.
13. Bind every known product-composition edge explicitly, including its
    target definition identity, relation authority and non-empty contract
    set (§9).
14. Validate the JSON shape, assert URI and URI-reference syntax,
    synchronise and verify the exact installed basis, then resolve every
    URI and perform the cross-definition identity, composition,
    constitutional-sufficiency and authority-congruence checks.

Once a bound requirement set is the live constitutional surface, no rival
monolithic requirements document should remain co-equal authority with it. This
keeps requirement truth structurally clear, derivable and non-monolithic
without prescribing its folder (P6, P2).

## 13. Source dispositions

Rows received by this member. Anchors are into rc.2 SPEC_METHOD.md; a
locus is a section of this file unless another member is named. Every row
is restated in this member's own text; a route is provenance only. Where
the predecessor named one of its own members, the tenant member that
receives the same law is named instead; this is carrying, not a
disposition, and is recorded in the row.

| Anchor | Disposition | Locus |
|---|---|---|
| #stdo-product-definition-overlay-and-layout-independence | conserved; the owner of the product-definition-routing bounded context is this member rather than SPEC_METHOD; `IDENTITY_METHOD.md` is carried as the [IDENTITY](IDENTITY.md) member | §1 |
| #required-definition-relations | conserved | §2 |
| #constitutional-set-sufficiency | conserved; "the accepted Design Module Method Ontology" is carried as the design profile's accepted design ontology of a realisation boundary, losing no determination | §3 |
| #shared-installed-release-basis-and-toolchain-manager | conserved in full: the basis pair, the manifest binding, the Adoption and Fleet Adoption Plans, the hashing rule, the seven manager functions, the store and registry law, the physical-entry rule, the selector and basis fields, the six command boundaries, the fail-closed list, the schema-locator rule, the agent bootstrap marker law and the exact prune list; `RELEASE_METHOD.md` as owner of the selector's alias semantics is carried as the [RELEASE](RELEASE.md) member | §4 |
| #explicit-complete-consumer-update | conserved in full | §4 Explicit complete consumer update |
| #bounded-context-semantic-resolution | conserved; the owner of the semantic-resolution bounded context is this member; `GLOSSARY_GUIDE.md` is carried as the [GLOSSARY](GLOSSARY.md) member; the relation kinds are related to AC-012 (AXIOMATIC_CALCULUS §4) without being redefined | §5 |
| #local-constitutional-binding | conserved | §6 |
| #collective-reference-frame-basis | conserved; `REFERENCE_FRAME_METHOD.md` is carried as REFERENCE_FRAME and `STDO_REFERENCE_FRAME_BASELINE.md` as the Executive baseline profile member; the activation packet and the step are pointed to REFERENCE_FRAME §11 and ACTIVATION §1, which define them | §7 |
| #what-how-and-work-carriers | conserved; the owner of the build-tenancy bounded context is this member; the generic WHAT/HOW law is SPEC_METHOD §2 and carrier selection is SPEC_METHOD §4 and [TICKETS](TICKETS.md), neither restated here | §8 |
| #recursive-discovery-and-explicit-composition | conserved | §9 |
| #semantic-resolution-conformance-cases | conserved; "Reference Frame Method evaluation context" is carried as the reference-frame-evaluation bounded context owned by REFERENCE_FRAME §1 | §10 |
| #one-constitutional-surface-and-version-boundary-stdo-surface-001 | conserved; "standard" is carried as "member" | §11 |
| #bootstrap-rule | conserved in full: the scaffold bindings, the authority split, the singular-authority rule, the folder shape, the requirement sources and the fourteen-step sequence; the predecessor's own mutable source path `specification_methodology/specification/standards/` is generalised to the method's source workspace, since this line's source path differs and the law does not depend on it | §12 |
