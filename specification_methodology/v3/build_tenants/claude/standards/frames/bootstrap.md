# Reference frame bootstrap

Task: Enter this method for a task not yet specified: say what the method is, bind the exact basis and the one applicable product definition, say how a reference frame is activated for a step and what the step may and may not do before its contract is admitted, give the core result values, and acquire the deciding owner sections for the task.

Purpose: The owning sections for the method's canonical statement; the product lineage objects; the product definition's required relations, recursive discovery and the one constitutional surface with its staleness binding; the authority kinds, the frame tuple and the activation packet; the step's intake and admission; context construction with the size measurement, acquisition, activation and evaluation; and the core result algebra.

Each excerpt below copies one owning section of a member of this method
byte for byte, except that each relative link destination is rebased
to resolve from this directory to the same target. Fenced code, inline
code and absolute and `stdo://` links are unchanged. The `Source:` line
before an excerpt names the member and the section's anchor, and gives
the SHA-256 of the whole owning member. The section digest recorded in
FRAME_INPUTS.json is over the owner's bytes, not over this copy. The
owning section decides; this frame owns no determination.

Routes, in order:

1. [SPEC_METHOD.md#canonical-statement](../SPEC_METHOD.md#canonical-statement)
2. [FOUNDATIONS.md#product-lineage-objects](../FOUNDATIONS.md#product-lineage-objects)
3. [PRODUCT_DEFINITION.md#2-required-definition-relations](../PRODUCT_DEFINITION.md#2-required-definition-relations)
4. [PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition](../PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition)
5. [PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary](../PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary)
6. [FOUNDATIONS.md#authority-kinds](../FOUNDATIONS.md#authority-kinds)
7. [FOUNDATIONS.md#the-frame-tuple](../FOUNDATIONS.md#the-frame-tuple)
8. [REFERENCE_FRAME.md#11-the-activation-packet](../REFERENCE_FRAME.md#11-the-activation-packet)
9. [ACTIVATION.md#intake](../ACTIVATION.md#intake)
10. [ACTIVATION.md#admission](../ACTIVATION.md#admission)
11. [ACTIVATION.md#2-context-construction-under-an-envelope](../ACTIVATION.md#2-context-construction-under-an-envelope)
12. [FOUNDATIONS.md#results](../FOUNDATIONS.md#results)

Size of this frame: 66291 bytes.

Source: SPEC_METHOD.md#canonical-statement sha256=500e420a4d9cdbf0b88c8817de26a4a6a4ed41edec529d99b7ac6f6dcfb49821

### Canonical statement

The method in one statement, each clause owned by a section of this corpus
(rc.2 #canonical-compression). Specification is constitutional source, not
commentary on code. The method defines the process constitution; intent,
product definition and requirements define the project constitution (§1).
Specification defines WHAT; design and realisation define HOW (§2). Every
product under this method publishes a layout-neutral definition that locates
its governing constitution, local constitutional decisions, collective
reference-frame bases, WHAT, independent build-tenant HOW realisations, work
surfaces and explicit product composition; the definition is a routing
overlay, not a rival truth surface
([PRODUCT_DEFINITION §1](../PRODUCT_DEFINITION.md#1-overlay-and-layout-independence)). A material term
resolves only under its bounded-context identity, owning authority, selected
basis and governed scope; equal spelling creates no cross-context meaning or
authority; explicit imports, translations, equivalences and disambiguations
govern those seams, and zero or multiple applicable meanings fail closed
([PRODUCT_DEFINITION §5](../PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)). Requirements define the full constitutional what:
capabilities, guarantees, governance and verification obligations; design
defines the structural how, and ADRs are one durable form of that record
(§2, §10). The lifecycle is a governed disambiguation pipeline: each major
boundary reduces the space of lawful interpretations and surfaces major
ambiguity explicitly; detection is mandatory; blocking or escalation is
policy under declared risk appetite, except for hard-stop prerequisite
failures (§5; ACTIVATION §4). Products, applications, modules, functions,
build tenants and runtime surfaces are implementations of the constitutional
documents, not substitutes for them. Scenarios verify operational meaning
where capability claims need end-to-end proof ([ASSURANCE §4](../ASSURANCE.md#4-scenario-bundle)). Code realises
decisions. Design is derivable from requirements, which are derivable from
goals, intent and product definition; code is derivable from requirements
and design (§2). Iteration is cumulative repricing, not waterfall. Events,
projection and delta reveal drift. Every live requirement family has design
ownership, explicit classification and downstream closure or explicit
deferment; every design record grounds itself in requirements; shipping
behaviour traces back to constitutional authority (§2). Live constitutional
surfaces are versioned history that change by supersession or withdrawal,
never by silent in-place mutation (§2). New intent emerges from real use
cases hitting the current model through explicit gap analysis, not from ad
hoc pressure (§2). Sprints are execution-control batches for pricing proof
cost and forcing close review; they are not authority layers and cannot hide
drift (§4).


Source: FOUNDATIONS.md#product-lineage-objects sha256=4fb8ff98d3e1c45344a0a989158937f71f15b06840fac86f2cfffd7d14db194b

### Product lineage objects

Software is recursive and compositional: a released product may build the
next released version of itself, a dependent product, or downstream project
artifacts. Most taxonomy drift in recursive systems comes from collapsing
the roles below into one overloaded word such as "product". Each role is an
object with its own identity (P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy`,
whose bounded context `urn:stdo:bounded-context:recursive-product-taxonomy`
this member owns under the selected complete basis; the concept
identities below are carried unchanged).

| Term | Definition | Requires |
|---|---|---|
| Substrate (`urn:stdo:concept:recursive-product-taxonomy:substrate`) | a lower product or runtime used to build other products | P3 |
| Development product (`urn:stdo:concept:recursive-product-taxonomy:development-product`) | the role of one exact install of a released product while that install acts as builder substrate for a source project; the role creates no new product identity and transfers no meaning or authority from the builder to the product being authored | P3, P6 |
| Source project (`urn:stdo:concept:recursive-product-taxonomy:source-project`) | the mutable workspace building the next release cut | P3 |
| Release cut (`urn:stdo:concept:recursive-product-taxonomy:release-cut`) | one immutable annotated release-candidate boundary over a published feature set | P3 |
| Product (`urn:stdo:concept:recursive-product-taxonomy:product`) | the released immutable thing resulting when that release cut is accepted | P3 |
| Install (`urn:stdo:concept:recursive-product-taxonomy:install`) | a stamped workspace instance of that released product | P3 |
| Artifact (`urn:stdo:concept:recursive-product-taxonomy:artifact`) | any published output built by a source project or by a configured installed product | P3 |
| Product definition (`urn:stdo:concept:recursive-product-taxonomy:product-definition`) | the present-tense source-project authority surface, conventionally carried by `PRODUCT.md`; it defines the current product WHAT for decomposition and is not the released product artifact | P3, P2 |

The governing rules: a mutable source workspace is not called a product;
when a released product acts as builder substrate, the exact install is
bound as a development product without confusing it with the product being
authored; an immutable release cut or installed product is not confused
with the mutable source project building the next cut; the product
definition is the surface of a source project, not the released product
artifact; products may depend on other products; installed products may
build the next version of themselves or other products. The compiler
analogy is the intended model: bootstrap source, release P0, install P0,
use P0 to build the source for P1, release P1. The taxonomy is load-bearing:
blurred, dependency and self-hosting errors compound quickly and are
expensive to unwind. SPEC_METHOD §6 applies these objects to lineage and
release.

Release objects. A release cut has three neighbours that release keeps
distinct from it and from each other (P3, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#release-identities`).
A candidate source is the mutable source-project state constructing a
possible successor; it is non-operative for released consumers. A release
subject is the exact declared product member set or artifact that one
release cut binds, described by that cut's release-scoped claims; a
carrier that holds it does not thereby make co-located material a
member. A version-line selector is a mutable
alias naming the highest-ordinal published release cut on one version
line of one project; it is convenient discovery, not immutable identity,
and not sufficient as an exact basis ([RELEASE §1](../RELEASE.md#1-context-and-position)
states which).
Equal version text does not collapse these objects. A selector or a
mutable carrier may move; a release cut never moves. RELEASE §2 realises
them, with the carriers that hold them, as refs of one release source.


Source: PRODUCT_DEFINITION.md#2-required-definition-relations sha256=2786351a7de4257b80df0b740ca40451ce63b74afe6e9e8f3414cf3f8bddae19

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


Source: PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition sha256=2786351a7de4257b80df0b740ca40451ce63b74afe6e9e8f3414cf3f8bddae19

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


Source: PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary sha256=2786351a7de4257b80df0b740ca40451ce63b74afe6e9e8f3414cf3f8bddae19

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

Staleness binding. What a derived surface is, when it is stale, and
what an actor uses in its place are
[ACTIVATION §2 Staleness of derived surfaces](../ACTIVATION.md#staleness-of-derived-surfaces);
which questions a derived surface decides on its own is ACTIVATION §2,
Standalone scope. This member refines that law for the derived surfaces
a released cut or an installation carries, among them compressions,
templates, bootstraps, indexes and projected frames. Each carries the
path and digest of each deciding source it was derived from, and of each
index it watches (GLOSSARY §2). A change to any of those digests is the
source change that makes it stale under that law, and it must be
regenerated or explicitly re-accepted before an installation treats it
as current. What a matching digest establishes is stated above
(EVALUATION §7). The raw owning members of the same
selected cut remain the deciding authority: a question that a stale or
insufficient carrier cannot decide is decided from them, as ACTIVATION
§2 states (P3, P5, P6; provenance rc.2
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


Source: FOUNDATIONS.md#authority-kinds sha256=4fb8ff98d3e1c45344a0a989158937f71f15b06840fac86f2cfffd7d14db194b

### Authority kinds

Authority takes these kinds (P6): frame-set authority, the human authority
that declares or accepts a project frame set; semantic authority, the
owner of meaning for a material relation; evaluation authority, the role
permitted to perform an evaluation; operation authority, the owner-issued
grant to construct, transform, admit, publish or mutate a material subject
where an evaluation performs such an operation; decision authority, the
role permitted to accept, reject or otherwise dispose a result; and actor
identity, the human, agent, tool or process performing the work, which is
an identity and not an authority. These may coincide in a lawful case and
never collapse by default. A read-only evaluation declares no operation
authority; an effectful evaluation inherits the exact operation grant from
its existing owner, and the frame does not create that grant (P6, P3).

What creates no authority. Authority of any kind exists only by an
admitted grant or an explicit authority decision of its owner, with an
identifiable basis. None of the following mints, widens, transfers or
reconstructs semantic, evaluation, operation or decision authority (P6,
P3):

- actor identity, an actor's capability, its tools or its access;
- a name, label, display label, status label, role name, capability
  string, locator, file name or path;
- declaring, naming, selecting, activating or executing a frame, or
  occupying a role;
- implementation reachability, a reachable code path or an available
  operation;
- the shape of evidence or of a payload, or the availability of evidence
  inside a frame;
- a passing check, a successful step, a completed review or a count of
  any of them;
- copying, interpreting, encoding, evaluating, transporting, projecting,
  compressing, importing or acquiring material;
- drafting, admitting or retaining a work contract, beyond what its owner
  has admitted;
- composition, delegation, adapters, wrappers and registries, which may
  restrict admitted authority or carry it faithfully, and never widen its
  scope, add a role, increase its cardinality or change its kind.

Elevation, transfer, split, merge, proxy grant, revocation and retirement
each need an explicit authority decision with an identifiable basis. A
member that names an instance of this list for its own domain cites this
paragraph and adds only the instance.

Proxy limit. Human authority may act directly, or through an explicitly
admitted bounded proxy where the governing identity and authority law
permits it; proxy identity and human-authority identity stay distinct
(P6, P3). A proxy acts only inside its existing grant. It cannot change
the governing outcome's meaning, the requirements, the governing authority
or the accepted design; such a change re-enters at its owning relation.
Proxy authority does not make a constructor's self-review independent,
confers no unrelated runtime or domain authority, and does not replace
direct human acceptance where the governing product or release law
requires it. The contents of a proxy grant are
[IDENTITY §6](../IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)'s,
and the decisions a proxy may take inside a step are
[ACTIVATION §1 Roles and delegation](../ACTIVATION.md#roles-and-delegation)'s.

Purpose and material relation of the list and the proxy limit: each
member that names what cannot create authority decides the same question,
so one list keeps the answer the same in every member, and a capability,
a label or a passing check can never be read as a permission (P6).


Source: FOUNDATIONS.md#the-frame-tuple sha256=4fb8ff98d3e1c45344a0a989158937f71f15b06840fac86f2cfffd7d14db194b

### The frame tuple

A reference frame F is the tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩
(P0): Q the evaluation family; B the workspace and topology basis; M the
material-relation manifold; C the coordinate and equality law; I the
applicable invariant set; A the authority relation; E the admissible
evidence and provenance law; X the exclusion and prohibited-assumption set;
R the closed result algebra (§4 [Results](../FOUNDATIONS.md#results), or a refinement mapped
into it); J the invalidation and rechart
condition; K the actor capability envelope; and D the optional set of
declared dependencies, overlaps, inputs and outputs involving other frames.
The tuple specifies the relation; it is not a required schema or runtime
carrier (P2). Operationally a frame is an evaluation contract that defines
the finite attention scope one evaluation family requires. A prompt, a
context packet, a symbolic program or any other representation is a
projection of an activated frame, not the frame (P1). A frame is bound
when every material coordinate above resolves to an exact source, subject,
basis, authority, evidence route, actor envelope, result relation and
invalidation condition; the binding may be expressed entirely in
source-linked prose, and representation cannot create, widen or replace it
(P3, P6).


Source: REFERENCE_FRAME.md#11-the-activation-packet sha256=1b0565ff0aeda1e44d2ee0c9ef508f560771202e3d007406b8cd308b8af4567d

## 11. The activation packet

An actor receives one activated frame or one declared active frame
configuration, never an implied demand to reconstruct the complete
workspace from ambient context (P0; rc.2 #agentic-use). The minimum
activation packet contains:

- frame identity and revision;
- the evaluation and its result algebra;
- the exact subject and basis;
- the material relations and applicable invariants;
- semantic, evaluation, operation where material, and decision authority;
- admissible evidence and tools;
- the capability and context envelope;
- exclusions and prohibited assumptions;
- declared frame dependencies or conjunction outputs; and
- invalidation, stop and reconfiguration conditions.

The actor may own its internal reasoning and search where the governing
method permits. It returns through the declared result relation. Hidden
internal reasoning is no substitute for required evidence, provenance or
authority (P6). Frame size is optimised for reliable evaluation, not for
maximum context loading: a more capable actor may activate a broader frame
and a less capable one may use a lawful refinement sequence, and both
preserve the same material invariants and authority relations (P0, P2;
RF-014).

### Minimal activation binding

The following carrier-neutral content is sufficient to bind one declared
frame for one evaluation. It may be written in Markdown, structured data, a
prompt or another consumer-selected carrier without changing the relation
(P0, RF-016; rc.2 #minimal-frame-activation-binding).

```markdown
# Reference-Frame Activation: <stable activation identity>

## Frame
- declaration identity and revision:
- exact evaluation and closed result algebra:

## Subject And Basis
- exact subject or candidate identity:
- workspace, authority, dependency, configuration, and time basis:

## Attention Surface
- material relations and applicable invariants:
- exact source and semantic references:
- explicit exclusions and prohibited assumptions:

## Actor And Authority
- actor and capability envelope:
- semantic and evaluation authority:
- operation authority, subject, and territory where material:
- decision, acceptance, and publication authority:

## Evidence And Relations
- admissible evidence and acquisition route:
- dependency, overlap, input, conjunction, or translation relations used:
- expected result consumer and return relation:

## Stop And Change
- invalidation conditions:
- stop, residual, re-entry, and reconfiguration conditions:
```

Every field resolves through stable identities and source references.
Paths, line numbers, member counts, summaries and matching labels may aid
navigation or diagnostics; they do not substitute for the declared identity
and basis (P3).


Source: ACTIVATION.md#intake sha256=a1d0788c5f4ed86004ca344c80248d647b99e0a1638991e459dca1ef786d871c

### Intake

A step is activated from an intake sufficient to reconstruct its governing
relations without conversation history, commentary or a prior actor's memory
(P0, actor-change premise). The intake names:

- the governed outcome or decision: the selected outcome, admitted
  prerequisite or experiment it serves (P2);
- the exact workspace subject and basis, and the inputs it may acquire,
  each by identity and hash or by an input commit;
- the evaluation or evaluation family the step performs and its result
  algebra: the core of [FOUNDATIONS §4 Results](../FOUNDATIONS.md#results) or
  a refinement mapped into it (§3);
- the bounded affected relation set and the applicable governing
  invariants;
- the accepted transformation-admission relations the step relies on (§4);
- the selected computational or common-library dispositions: which
  shared machinery serves the step and under what binding (FOUNDATIONS §4,
  shared machinery);
- the construction and assessment authority: the applicable frame-set,
  semantic, evaluation, operation where material, and decision authority
  (FOUNDATIONS §2, authority kinds), and the grant: the operations
  permitted, the territory that may change, and the decisions reserved to
  others (P6);
- the available actor capability envelopes;
- the conditions that make the result stale or out of scope, and the
  conditions that require re-entry at an owning relation;
- where the governed question is a cost claim, the allowance and how
  spend will be measured (§6).

Implementation folklore is not an intake source. Where a design profile
applies, its bounded-frame conservation, transformation-admission
completeness, invariant-reconstruction sufficiency and
computational-realisation projection laws supply the affected set, the
admission relations, the invariants and the computational dispositions;
this section consumes those laws and creates no second design package
([DESIGN_MODULE](../DESIGN_MODULE.md)). Conserves
[UP-020 intake](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#sufficient-execution-intake),
[UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018)
and the engagement basis (rc.2 RF #establish-the-evaluation-basis).


Source: ACTIVATION.md#admission sha256=a1d0788c5f4ed86004ca344c80248d647b99e0a1638991e459dca1ef786d871c

### Admission

Drafting a step's contract and admitting it are distinct relations, even
inside one invocation that drafts, validates, admits and executes; no
separate turn, carrier or approval ceremony is implied by the distinction.
A contract carries at minimum the states drafted, admitted, rejected and
superseded ([TICKETS §5](../TICKETS.md#execution-contract-admission)).
Execution begins only after deterministic admission or an
explicit human override of the exact contract. The drafting actor never
infers admission from its own draft, from the presence of a carrier
(ticket, sprint entry, work contract), from lane placement or from an
`active` label. The admitted result identifies the admission mechanism and
its authority, the exact contract identity or digest, the decision and the
evidence, including any human override; absent those coordinates the
contract stays drafted or rejected, and prose asserting admission is not
admission evidence (P6; the actor cannot self-certify its own execution
basis). Admission validates the contract against its cited outcome,
prerequisite or experiment basis; it does not admit that basis, and
drafting, admitting or retaining a contract creates or renews no authority
its owner has not admitted (P6, P2;
[FOUNDATIONS §2 Authority kinds](../FOUNDATIONS.md#authority-kinds), What
creates no authority). Only an admitted contract activates a step: no
result, child completion, tool output, model response, shared actor or
lateral handoff activates another step or authorises continuation by
itself, and a profile that routes results names its instances of this
rule. Purpose and material relation: a profile and a template each stated
this list for one configuration, so the generic rule had no owner (P6).
The admitted contract names one
durable result and evidence surface; every result, withheld closure and
residual obligation is recorded there before return, a conversation return
alone is not durable evidence, and if no such surface is authorised and
available, admission refuses (P4b). Absent or rejected admission returns
the missing work authority without execution, as `admission_refused` with
its cause ([§3 Admission and activation](../ACTIVATION.md#admission-and-activation)).
Provenance:
[work-carrier-to-execution rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)
and
[execution contract admission](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-contract-admission);
the selection of the carrier (ticket, sprint entry, run-scoped contract)
is tier-2 law in the [TICKETS](../TICKETS.md) member, which disposes those rows.


Source: ACTIVATION.md#2-context-construction-under-an-envelope sha256=a1d0788c5f4ed86004ca344c80248d647b99e0a1638991e459dca1ef786d871c

## 2. Context construction under an envelope

Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R (AC-010,
   [AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-010-material-closure);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-010-material-closure).
   If Z, R, the required-edge semantics, the basis or the scope is not
   exact, or the closure is not finite and unique on the exact basis,
   activation returns `closure_unresolved` (§3, Admission and activation)
   and no step proceeds; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams (AC-011,
   [AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-011-projection);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-011-projection).
   If the projection returns a gap or refusal, activation returns
   `closure_unresolved` and no step proceeds.
   Material not in the closure stays out; adjacent material does not enter
   because it exists
   ([RF-004](../REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)).
3. Test fit against B. This step owns the size measurement and the fit
   test for the context dimension. Where B declares a context capacity,
   the size of the selected context is measured before the actor reads it,
   in the unit the capacity is declared in (bytes or tokens) and over the
   boundary that the selected execution binding states for it (§6), and is
   compared with that capacity. The measurement, the capacity and the
   outcome of the comparison are recorded before the read. A fit holds
   only for the measured boundary: context outside it is recorded as not
   measured, and no fit claim covers it. The measurement applies wherever B declares a
   context capacity, whatever question the step governs, because without
   it a fit claim against that capacity is an assertion, and a context
   that exceeds it would be cut without record
   ([RF-014](../REFERENCE_FRAME.md#rf-014-capability-fit)). It applies only
   there, because a resource control applies only through a selected frame
   and its owning scope
   ([REFERENCE_FRAME §4](../REFERENCE_FRAME.md#frame-set-selection)), and a
   declared capacity is such a control: the measurement tests that
   capacity, is no budget, and is not a universal measurement gate (P0,
   P2). Where B declares no context capacity, no measurement is
   required, and the other conditions of
   [RF-002](../REFERENCE_FRAME.md#rf-002-finite-attention) still apply. The size
   shows fit and nothing else: whether the actor attends adequately to a
   context that fits is decided by actual-use evidence under
   [EVALUATION §7](../EVALUATION.md#frame-qualification). The envelope's
   other dimensions are fitted as RF-014 states; time, spend and other
   resource limits follow [§6 Resource limits](../ACTIVATION.md#resource-limits), which
   this step refines for the context dimension.
   If the context fits, activate. If it does not, one or more of these, in
   combination: refine the outer contract into steps whose contexts fit
   (§4); sequence activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](../REFERENCE_FRAME.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return `out_of_frame`
   ([§3 Admission and activation](../ACTIVATION.md#admission-and-activation)). Silent
   omission to fit is never one of them
   ([RF-014](../REFERENCE_FRAME.md#rf-014-capability-fit)).
   None of these options silently reduces the required predicate: the
   obligations the step preserves stay bound
   ([§1 Transitions](../ACTIVATION.md#transitions)), a narrowing of them is a destination
   change under its owning authority (§1, Destination change), and what
   the selected context leaves undecided stays an explicit unknown.
   Within its grant a step selects refinement, sequencing and compression
   itself; selecting another actor or enlarging the envelope re-enters the
   owner of the grant or envelope, who may delegate that choice in the grant
   (RF-014 vests the selection in human authority; a grant is that authority
   exercised in advance). Whether a compression preserved what the
   evaluation needs is a claim with the standing of any other (EVALUATION
   §1): the compressing step records the compression and its preservation
   argument, and the claim is assessed independently only where the
   promotion it serves needs independent assessment (EVALUATION §3).
4. Acquire declared inputs by their exact identity. A declared input absent
   from the actor's materialised view is neither licence to read elsewhere
   nor evidence that it is absent.

Acquisition. Acquisition is the read-only observation of the material a
step needs (its frame, its subject and its declared inputs) within the
inputs its intake permits it to acquire (§1 Intake). It is not an admission and not a further
actor stage; effectful work still needs its admitted contract (§1
Admission), and acquiring material grants no role, operation or decision
([FOUNDATIONS §2 Authority kinds](../FOUNDATIONS.md#authority-kinds), What
creates no authority). A derived surface is material derived from owning
sources by copying, projection or compression, such as a projected frame
for a task; it names its sources and owns no determination. Where a
current interpretation of the subject in `a_c` exists, the constraint
surface it yields for the task is such a derived surface, under the
conditions of
[AXIOMATIC_CALCULUS §9 Constraint surfaces](../AXIOMATIC_CALCULUS.md#constraint-surfaces).
Where a derived surface whose sources
are current serves the task, the actor acquires it. For another task, or
where the derived surface is stale ([Staleness of derived surfaces](../ACTIVATION.md#staleness-of-derived-surfaces)),
missing or insufficient for a named unresolved question, the actor acquires the deciding owner sections
directly: the owning sections that decide the task's questions, which are
declared inputs of the selected basis. Only material in the exact selected
basis is acquired: where that basis has no derived surface for the task,
its exact owner sections are used, and a candidate source, a version-line
selector or another basis is no substitute for it
([FOUNDATIONS §2 Product lineage objects](../FOUNDATIONS.md#product-lineage-objects)).
The actor reads the selected material and the actual subject, and follows
the material source and coupled-obligation references the task needs
(step 2; [RF-003](../REFERENCE_FRAME.md#rf-003-material-sufficiency));
presence of the corpus is no reason to read it (step 2;
[RF-004](../REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)). Before any dependent action, a missing binding is returned with
its outcome of [§3 Admission and activation](../ACTIVATION.md#admission-and-activation),
naming what is missing: where no available frame declares what the
evaluation needs, `out_of_frame`; where the basis the step requires is
absent, or cannot be verified as the exact basis named, the basis cannot
support the step, and the outcome is `admission_refused(basis)` at
admission or `activation_refusal(basis)` at activation. Coupled material that does not fit is handled under
step 3 (P0, P6, P3).

Activation. The actor or the assigning authority selects one frame or one
declared active frame configuration capable of the evaluation. Activation
binds each reusable frame declaration to the exact subject and basis and
loads the declared material relations and evidence sources, never an
undifferentiated workspace dump; what the actor receives is the packet of
REFERENCE_FRAME §11. When no available frame and actor pairing can lawfully
perform the evaluation, activation returns `out_of_frame` where no such
pairing declares a material relation or capability the evaluation needs,
and otherwise the `activation_refusal` whose cause holds
([REFERENCE_FRAME §5](../REFERENCE_FRAME.md#5-method-functions)); both are
outcomes of §3 Admission and activation. Work does not proceed through
implied context (P0, P5; rc.2 RF #select-and-activate).

Evaluation. The evaluator applies the activated frame's declared
invariants, evidence rules and result algebra. It distinguishes semantic
law, observed evidence, inference and decision, and records every
assumption whose failure could change the result (P6; rc.2 RF #evaluate).

Standalone scope. A derived surface or projected frame decides standalone
only the questions that its own source members own. It refuses to close a
question owned by another member, or one that joins the law of several
owners; the evaluation of that question returns `out_of_frame`
([FOUNDATIONS §4 Results](../FOUNDATIONS.md#results)) naming the owning
members, and
the question is decided from those members at their current digests or
from a derived surface whose declared sources include every owner of it
(P6, P1; provenance rc.2 authority_compressions/stdo_compressed.md,
spec_method.compressed.md and design_module_method.compressed.md, a claim
no rc.2 body states).

Prompt construction. A prompt is rendered contract over typed authority;
it is not source law. Prompt text must project the current authority
references, obligations, contracts, boundaries, proof expectations and
fallback conditions the step needs. A prompt body must not carry
historical workaround prose unless the current requirement, design,
runtime or test still needs that constraint. Construction starts from the
highest live authority surface the question needs. If the prompt needs an
upstream ambiguity resolved, it names the unresolved authority gap before
fallback context is read. The prompt projects the material that
Acquisition above selects, including the raw owning members where
Acquisition falls back to them (P6, P0, P5; provenance rc.2
authority_compressions/stdo_compressed.md and spec_method.compressed.md, a
claim no rc.2 body states). The design, ODD, UX and ticket
specialisations are
[DESIGN_MODULE §11](../DESIGN_MODULE.md#11-review),
[ODD §11.5D](../ODD.md#115d-constructive-evaluation-and-yield-loop) A5 and
[§11.7A](../ODD.md#117a-conforming-agentic-development),
[UX §7](../UX.md#7-carrier-binding) and
[TICKETS §5](../TICKETS.md#5-from-carrier-to-execution) and
[§7](../TICKETS.md#7-authority-judgment-closure-and-state) (P6).

The operation that joins AC-010, AC-011 and RF-002, RF-003, RF-004,
RF-014 and RF-017 into one procedure is new in this corpus (P0); each of
those laws is applied here from its successor section in
[AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-010-material-closure) and
[REFERENCE_FRAME §3](../REFERENCE_FRAME.md#3-laws), and a `stdo://` route in
this section is provenance only. The method does not require proving
that no undiscovered material relation exists
([RF-003](../REFERENCE_FRAME.md#rf-003-material-sufficiency)).
The size measurement of step 3, with the condition under which it
applies, and Acquisition are also new. Purpose and material relation:
finite context makes fit necessary (P0), so a fit against a declared
capacity is measured rather than asserted, while fit and attention stay
separate claims (P6); and an actor without a derived surface for its task
still reaches the sections that decide it, from the exact basis, without
reading the corpus or substituting a stale or mutable copy (P3, P6). The
material relation is whether a context larger than the declared capacity
is read as if it fit, a fit is taken as adequate attention, or a decision
rests on material other than its deciding owners at the selected basis.

### Staleness of derived surfaces

This subsection owns when a derived surface (Acquisition above) is current
and when it is stale, for any method and any carrier (P3, P5, P6):

- A derived surface names the exact identity, such as the path and
  digest, of each source it was derived from and of each source whose
  change can change its content.
- It is current for a selected basis only while every source identity it
  names equals the identity of that source in the selected basis. A change
  to any of them makes it stale.
- A stale derived surface is not used as current for any question. It
  becomes current again only by regeneration from the sources at the
  selected basis, or by an explicit re-acceptance that records the new
  source identities and the finding that its content still matches them;
  until then the actor acquires the deciding owner sections directly
  (Acquisition above).
- Matching source identities establish only that the surface was derived
  from those sources. They establish neither its fidelity to them nor its
  sufficiency for a question; a surface found insufficient for a named
  question is handled as Acquisition above states.
- The owning sections at the selected basis remain the deciding source.
  Whether a current surface is insufficient for a question, or decides
  beyond its own sources, is judged against them (Standalone scope above);
  a derived surface never decides that about itself.

A packaging or installation carrier refines this rule with its own
identities and re-acceptance procedure, and names this subsection as its
owner; [PRODUCT_DEFINITION §11](../PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary)
does so for the method's released carriers. Provenance: rc.2
authority_compressions/README.md and stdo_bootstrap.md step 5, a claim no
rc.2 body states. Purpose and material relation: an actor that relies on a
derived surface after one of its sources has changed decides from material
that no longer matches its owners, and a matching digest read as fidelity
would let a faithful-looking but wrong surface decide; the material
relation is whether a decision rests on a surface whose sources are not
those of the selected basis. This rule is new in tier 1; it was stated
only for packaging carriers before.


Source: FOUNDATIONS.md#results sha256=4fb8ff98d3e1c45344a0a989158937f71f15b06840fac86f2cfffd7d14db194b

### Results

Every performed evaluation returns one value of the core result algebra,
directly or as a refined value mapped into it (P5):

| Value | Meaning |
|---|---|
| `satisfied` | the declared predicate holds on the exact basis |
| `falsified` | a declared counterexample defeats it |
| `indeterminate` | the available admissible evidence cannot decide it |
| `out_of_frame` | the evaluation requires an undeclared material relation or capability |
| `invalid_basis` | the subject or basis cannot support the evaluation |

This core is the only one. Results of constraints, judgments, frame
evaluations, stops, work steps and effects are stated in it or in a
refinement mapped into it, so that results from any members combine under
one rule ([Conjunction of results](../FOUNDATIONS.md#conjunction-of-results)). Purpose and
material relation: no combination can report success while a failure, an
undecided question, an unperformed evaluation or an uncertain effect
remains, and none of these can be mistaken for another (P5, P6).

Recording. A result records its core value together with the predicate
evaluated and the original domain outcome, which is the refined value
where a refinement produced it. A mapping into the core never owns domain
meaning: the member, profile or adopting Product that defines the refined
value keeps it, and a consumer that needs the domain distinction reads the
domain outcome, never the core value alone (P1, P6).

Standing. The standing of a result is what it establishes about its
predicate; it is distinct from the standing of a commitment (§1). Only
`satisfied` establishes the predicate. `falsified` establishes that the
predicate fails and names the counterexample. `indeterminate`,
`out_of_frame` and `invalid_basis` establish neither, and each names what
would decide: the evidence, the missing relation or capability with its
owner where the subject gives one, or the basis repair. By support for the
predicate, `satisfied` stands above each other value, and the other four
are not ordered among themselves.

No refinement or mapping raises a result's standing (P5, P6):

- a falsified or failed result never maps to a satisfied or successful one;
- a result that admissible evidence cannot decide never maps to
  `satisfied`;
- an evaluation that was not performed stays distinct from one whose
  evidence cannot decide: it has no
  [closed result](../ACTIVATION.md#7-closed-result-and-reuse), and it is never mapped
  to `indeterminate` or to any other core value;
- an effect whose completion is unknown never maps to no effect or to
  completed.

Not performed. An evaluation that is required or planned and was not
performed has no closed result; an actor cannot report an evaluation it
did not perform (P6). Nothing is coerced to success: a failed,
indeterminate, out-of-frame, out-of-scope or invalid-basis result follows
the declared result algebra and returns its own value under it, never
`satisfied`, and a missing result, being no result, enters every
conjunction over it as a gap: a planned assessment without a closed result
where an assessment was planned, and uncovered coverage where none was.
This
conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
whose five values the table restates unchanged, and
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
whose rule that a failed, missing, indeterminate, out-of-scope or
invalid-basis result follows the declared algebra rather than being
coerced to success is the sentence before; both are restated here once.
[REFERENCE_FRAME §3](../REFERENCE_FRAME.md#rf-012-closed-results) states
RF-012 as a law over frames and
[AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
states AC-007 as a law over constraints; each uses this core and neither
defines it again.

Refinements. A member, profile or adopting Product that needs finer
outcomes defines a refinement. The refinement names the question it
answers and the predicate its mapping is for, and maps every refined value
to exactly one core value. No outcome exists outside the core; a
refinement adds no core value and keeps the pressure of `indeterminate`,
`out_of_frame` and `invalid_basis` explicit. Where a refined value would
map to one of two core values according to its cause, the cause is part of
the refined value and each resulting value maps once (P5, P1). A further
refinement, by a member, profile, project or adopting Product, may split a
refined value by cause. The parent-value rule governs every such split:
each child value names its parent value and its cause and keeps its
parent's core value; a child that needs a different core value needs a
different parent value, which only the owner of the parent declares; and
no child takes `satisfied` from a parent that is not `satisfied`. No
further refinement raises a result's standing (P5, P6, P1). Purpose and
material relation: a consumer that reads a parent value reads the same
core value from each of its children, so a split by cause adds a domain
distinction and never changes what the parent establishes (P5, P6). The
refinements for admission, activation and steps are
[ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition); each other
member, profile and adopting Product states its mapping where it defines
its values.

Availability, assessment and acceptance are separate results, each with its
own predicate: that a step produced a candidate; that the candidate meets
its declared criteria; and that the
[decision owner](../ACTIVATION.md#roles-and-delegation) accepts it at its
boundary. A step having produced a candidate never maps to the candidate's
fitness or acceptance, and acceptance is never inferred from a successful
step (P6; [ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition),
[EVALUATION §4](../EVALUATION.md#4-review-results) and
[§5](../EVALUATION.md#5-acceptance)).

Out of frame or indeterminate. The boundary between these values is drawn
on what the activated frame declares and on what the step did with it (P5,
finite capacity and graceful total handling; the material relation drawn
is the three-way out_of_frame boundary: capability not declared, capability
declared and exercised, capability declared and not exercised; rc.2 RF
#rf-012-closed-results). Three cases; the first two name core values, and
the third names none:

- `out_of_frame` when the claim requires a material relation or an
  evaluator capability that the activated frame does not declare. The
  result names the missing relation or capability, its owner where the
  subject gives one, and the reconfiguration pressure it creates
  ([ACTIVATION §4](../ACTIVATION.md#4-totality-and-refinement); rc.2 RF
  #reconfigure-when-necessary). A term the claim depends on and the frame
  leaves undefined is an undeclared material relation: its meaning can
  alter the result and it enters through no declared input (rc.2 RF
  #material-relation, RF-003; P1). Whether the step exercised anything is
  irrelevant to this value; the ground is the missing declaration.
- `indeterminate` when the available admissible evidence cannot decide the
  claim (rc.2 RF-012). The result names the evidence that would decide, as
  its residual uncertainty (rc.2 RF #return-a-closed-result). Where the
  claim also depends on an undeclared relation or capability,
  `out_of_frame` and `indeterminate` each have a lawful ground; the result
  names the value it returns and that ground, and this boundary excludes
  neither (P5).
- no value of its own when the step did not exercise a declared capability
  the evaluation requires. A result is returned wherever a sufficient
  evaluation or an applicable judgment exists without that capability,
  identifying its evidence, verdict and residual uncertainty like any
  closed result (rc.2 RF #rf-012-closed-results, #return-a-closed-result):
  a counterexample found by what was exercised, as when source inspection
  falsifies A in a claim of A and B, returns `falsified`, and common
  agreement cannot discard it (rc.2 RF #result-conjunction). Where none
  exists because the capability was not exercised, the evaluation was not
  performed and has no result: the step's stop state carries it,
  `incomplete` under
  [construction availability](../ACTIVATION.md#construction-availability), and
  its work state ([ACTIVATION §5](../ACTIVATION.md#5-work-state-and-restart))
  carries the unexercised capability as a residual (P6). In either case
  the unexercised part, B above, has no result: in every conjunction over
  it, it is a planned assessment without a closed result, and the known
  failure A survives with it ([Conjunction of results](../FOUNDATIONS.md#conjunction-of-results)).
  The evaluation's result and the step's stop state answer different
  questions, so the step's stop value never becomes the evaluation's
  result.

Foundation to law for results and their combination (family F3). The
table covers every rule of §4 and the result grounds of §2 Imports
between members, in the format of
[Foundation to law](../FOUNDATIONS.md#foundation-to-law), which states the standing of its
consequences. Purpose and material relation: a reader of §4 sees which
commitments each result rule rests on and which choices it adds, with their
owners (P6, P2). Instance premises, which the commitments do not supply:
(i) an evaluation declares its predicate, subject and basis; (ii) results
of several evaluations, steps or members are combined into one decision;
(iii) members, profiles and adopting Products need outcomes finer than the
core.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P5 (derived from P0 and P6), P6 (independent); (i), (ii) | every performed evaluation returns one closed value of one algebra shared by every member, with a value for a claim that holds, one that fails, one the evidence cannot decide, one that needs a relation or capability the frame lacks, and one whose basis cannot support it | [Results](../FOUNDATIONS.md#results), the value table | the value names, and the division of P5's outcomes other than success into `indeterminate`, `out_of_frame` and `invalid_basis`, conserved from RF-012; owner: this section | 3, 9 |
| P6 (independent), P5 (derived from P0 and P6) | a result claims no more than it establishes: only `satisfied` establishes the predicate, and no refinement or mapping raises a result's standing | [Results](../FOUNDATIONS.md#results), Standing, and the rule that nothing raises standing; for the choice, [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Reported value | the order among the four other values within one combination; owner: the member or profile that applies the conjunction, in its declared rule | 9 |
| P1 (independent), P6 (independent); (iii) | a core value alone does not carry a refined value's domain meaning, so a result records its predicate and domain outcome, and the definer of a refined value keeps its meaning | [Results](../FOUNDATIONS.md#results), Recording | each refined value and its domain meaning; owner: the member, profile or adopting Product that defines it | 6, 3 |
| P6 (independent) | an evaluation that was not performed supports no claim, so it has no closed result and is never read as undecided | [Results](../FOUNDATIONS.md#results), Not performed, and the third item of the rule that nothing raises standing | recording non-performance as the absence of a closed result, not as a core value; owner: this section | 9 |
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](../FOUNDATIONS.md#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile, project or adopting Product that defines it | 3, 6 |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](../FOUNDATIONS.md#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](../EVALUATION.md#5-acceptance) names | 9 |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](../FOUNDATIONS.md#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](../ACTIVATION.md#construction-availability), construction availability | 7, 9 |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](../FOUNDATIONS.md#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none | 6 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none | 3, 9 |
| P3 (independent), P5 (derived from P0 and P6), P6 (independent); (i), (ii) | a result supports its predicate only on the basis it binds, so a component held only on another basis has, on the basis the composite requires, no performed evaluation and is a gap, while an evaluation performed on a basis that cannot support it decides its own predicate as `invalid_basis`; one component is never answered both ways | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Stale results | none | 3, 9 |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains; with every mandatory result `satisfied`, agreeing bases and no gap, a material counterexample to a mandatory constraint falsifies it whichever contributor found it, and without one its value is the one its declared rule gives over the mandatory results; a `falsified` result that is not mandatory stays in its record | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, how results that are not mandatory count, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P4a (independent), P4b (derived from P0 and P2) | composed steps exist only under typed composition; the composite carries both steps' step-produced facts, and its result for the outer predicate is the conjunction over the outer contract's obligations | [§4](../FOUNDATIONS.md#4-algebra) Composition; [Conjunction of results](../FOUNDATIONS.md#conjunction-of-results), Composition of results; [RF-010](../REFERENCE_FRAME.md#rf-010-composition-on-demand), outside this member | whether a composition law is needed, under the conditions RF-010 states; owner: the governing evaluation | 3, 4 |
| P4b (derived from P0 and P2), P3 (independent) | every transformation records what it preserved, introduced and removed, its external witnesses and its residuals, so no fact is lost unrecorded | [§4](../FOUNDATIONS.md#4-algebra) Conservation accounting | the record's fields; owner: [AC-013](../AXIOMATIC_CALCULUS.md#ac-013-transformation) | 3 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P0 (recovered) | a reference stands for a body only where it supports the same consuming decision; otherwise the shortfall is a residual, never success, and no carrier or budget limit trims a required member | [§4](../FOUNDATIONS.md#4-algebra) Reference versus body | none | 6, 7 |
| P1 (independent), P6 (independent) | two values differ lawfully only through a declared relation; preference, probabilistic choice and human presence supply none | [§4](../FOUNDATIONS.md#4-algebra) Latitude | each latitude or transformation relation; owner: the owner of the contract that declares it | 3 |
| P3 (independent), P6 (independent) | similar computation proposes shared machinery and never decides identity or authority; each instance keeps its responsibility and binding | [§4](../FOUNDATIONS.md#4-algebra) Shared machinery | whether one implementation serves several instances; owner: the accepted design of the realisation that would share it, which [DESIGN_MODULE §5](../DESIGN_MODULE.md#capability-and-foundation-selection-up-023) refines for software design where that profile is selected | 4 |
| P6 (independent), P1 (independent) | a categorical claim is established only with its demonstration, and without it is a hypothesis | [§4](../FOUNDATIONS.md#4-algebra) Formal fragment | which categorical claims are made; owner: the member, profile or adopting Product that makes the claim | 3 |

RF-012 in [REFERENCE_FRAME §3](../REFERENCE_FRAME.md#rf-012-closed-results),
AC-007 in
[AXIOMATIC_CALCULUS §4](../AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
and [EVALUATION §4](../EVALUATION.md#4-review-results) apply the first row's
algebra to frames, constraints and reviews and add no choice of their own
beyond any refinement they map under the fifth row;
[ACTIVATION §3](../ACTIVATION.md#3-step-results-and-disposition) holds the
step's refinements of the fifth row and the stop state of the seventh.

