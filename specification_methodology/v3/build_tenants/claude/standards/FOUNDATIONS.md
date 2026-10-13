# FOUNDATIONS

Tier 1. Owns the vocabulary of standing (§1); the ontology, with the frame,
authority, lineage and work-boundary objects, and the rule for imports
between members (§2); the commitments P0 to P6 with their standing, the
foundation-to-law format with the standing of its consequences, and the
index of material families (§3); the algebra of composition and
conservation, the core result algebra, the conjunction of results and the
demonstration a categorical claim requires (§4); and the hypotheses (§5).
Other members import these definitions
([Imports between members](#imports-between-members)) or refine them. A
refinement names its owner here and never redefines it; a refinement of
results maps each of its values into the core ([Results](#results)).

## 1. Vocabulary of standing

The standing of a foundational claim is what grounds it relative to the
other foundational claims: whether the method adopts it as a premise,
taking it without derivation, derives it from them or holds it for test
(P6). A foundational claim is a commitment (P0 to P6, §3) or a hypothesis
(§4 Formal fragment, §5). Each has exactly one of four standings:

- recovered: an adopted premise that states as one commitment what
  several rules of the method state in parts; those rules are named as its
  sources, not as its proof;
- independent: an adopted premise argued by non-entailment, that is, by a
  case in which the other commitments hold and this one fails;
- derived: a consequence of other commitments, with the premises it
  follows from named;
- hypothesis: a claim that no clause and no argument of this method
  establishes; it is not law and is carried for falsification (§5).

The recovered and independent commitments are the method's adopted
premises, and the derived ones are consequences of them. A premise is
never presented as derived, and a hypothesis never as law (P6). This
standing is distinct from the standing of a result, which is what the
result establishes about its predicate (§4 Results), and from the
disposition a successor gives a predecessor claim
([RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015))
(P1, P6). Every clause names the principle (P0 to P6, §3) that requires it.

## 2. Ontology

| Term | Definition | Requires |
|---|---|---|
| Subject | the thing a claim, representation or transformation is about; exact, with inventory and bytes or semantic addresses | P3 |
| Representation | bytes, text, a model or a program standing for a subject; equal representations do not establish equal meaning | P1 |
| Interpretation | a declared contract from representation to meaning within a context; says which distinctions a consumer may rely on and which are residual | P1 |
| Context | the declared scope under which an interpretation holds: subject, definitions, basis, admissible observations | P1 |
| Outcome U | a selected, owner-defined, directly verifiable state with an acceptance interval; adequacy of a transformation is judged against it | P2 |
| Object O | a subject with scoped identity (authority, kind, value), a boundary, current state and declared material relations; identity survives admissible state and encoding change | P3 |
| Actor | whoever performs a step within a declared capability envelope (context, attention, time, capability); a role is a relation an actor occupies, not a kind of actor, and which roles exist is set by a configuration ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration)), not by this definition | P0, P6 |
| Step | one bounded unit of work: intake, selected context, grant, execution, output | P0 |
| Step-produced fact | a judgment, residual, observation or authority decision produced by a step that cannot be re-acquired from declared sources; an observation reproducible from declared sources is re-acquirable and is not one | P0, P4b |
| Claim | an assertion with subject, property, basis, witness relation and falsifier | P6 |
| Evidence | the exact observations or artifacts admitted to evaluate a claim on a basis; each carries provenance, subject identity, basis and scope; evidence becomes neither semantic truth nor decision authority by being available inside a frame | P6 |
| Judgment | a recorded evaluation over an unchanged subject, with evaluator, decision, evidence, scope and revising observation | P6 |
| Authority | an identity-bearing permission to operate or to dispose acceptance within a scope; never minted from capability, label or reachability; its kinds are defined under Authority kinds below | P6 |
| Residual | a material uncertainty, omission, loss or unproven relation that remains until an authorised disposition | P4b |
| Basis | the exact state a step, claim, result or evaluation binds: every version, identity, time, topology, authority, configuration or evidence coordinate whose change can alter it; immutable, or moving with a declared way of detecting advancement and a declared condition for reevaluation; mixed bases need an explicit composite relation | P6, P3 |
| Material | of a relation: its lawful change can change an evaluation's result, invalidate its basis, change the admissible evidence, change who may perform a material operation, or change who may decide the evaluation or a material operation; of an uncertainty or closure: likewise; materiality is evaluation-relative, so a relation material in one frame may be irrelevant in another; the relation family of ACTIVATION §2 is the material relations of a step | P2, P6 |

Dispositions: subject, representation and interpretation conserve
[AC Interpretation And Models](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#interpretation-and-models)
and
[bounded-context semantic resolution](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution);
identity conserves
[IDENTITY_METHOD](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#1-scoped-identity),
restated in [IDENTITY §2](IDENTITY.md#scoped-identity),
and
[AC-002](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-002-scoped-identity);
outcome conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013);
actor and envelope conserve
[RF-002](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-002-finite-attention);
claim, judgment and authority conserve
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001),
[AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation),
[UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004),
restated in [IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004);
residual and basis conserve
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation)
and
[AC-006](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-006-basis-coherence).
Step and step-produced fact are reframed from the
[Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)
and
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result)
to the generic unit.

### Frame objects

The reference frame and the objects it binds are first-class in this
corpus. Each is defined here once; [REFERENCE_FRAME](REFERENCE_FRAME.md)
states the laws over them and [ACTIVATION](ACTIVATION.md) the step that
activates one. Provenance for this subsection and the three that follow is
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#definitions`
and its child sections.

| Term | Definition | Requires |
|---|---|---|
| Evaluation | a declared question whose admissible result family, evidence basis, decision authority and, where it performs a material action, operation authority are known; it may ask for a judgment, prediction, construction, comparison, proof, refusal, classification or action recommendation | P6, P2 |
| Evaluation family | evaluations that need the same material-relation manifold, authority basis and result algebra; similar wording does not prove that two evaluations share a family | P1, P2 |
| Workspace | the bounded body of material reasoned over or acted upon, which may include constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority above; Authority kinds below); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |

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
never collapse by default. Declaring, selecting, activating or executing a
frame grants no semantic, operation or decision authority. A read-only
evaluation declares no operation authority; an effectful evaluation
inherits the exact operation grant from its existing owner, and the frame
does not create that grant. Human authority may act directly or through an
explicitly admitted bounded proxy where the governing identity and
authority law permits it; proxy identity and human-authority identity stay
distinct (P6, P3).

### Disjointness and independence

Three relations stay distinct (P6, P1). Frame disjointness is structural:
two frames share no material variable, coordinate, evidence or result
dependency for the declared evaluations. Evaluation independence is
procedural: separately activated evaluations neither consume nor influence
one another's unclosed working results, although they may inspect the same
subject, overlap in their manifolds and later supply closed results to one
conjunction. Assurance independence is claim-relative: the governing
assurance law states the non-authorship, evidence-acquisition,
reference-exposure, actor and configuration separation a verdict needs to
count as independent assurance (EVALUATION §3). Disjoint frames need not
be independently evaluated; independently activated evaluations need not
be disjoint; and the unqualified word "independent" establishes none of
the three.

### The frame tuple

A reference frame F is the tuple ⟨Q, B, M, C, I, A, E, X, R, J, K, D⟩
(P0): Q the evaluation family; B the workspace and topology basis; M the
material-relation manifold; C the coordinate and equality law; I the
applicable invariant set; A the authority relation; E the admissible
evidence and provenance law; X the exclusion and prohibited-assumption set;
R the closed result algebra (§4 [Results](#results), or a refinement mapped
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
and not sufficient as an exact basis ([RELEASE §1](RELEASE.md#1-context-and-position)
states which).
Equal version text does not collapse these objects. A selector or a
mutable carrier may move; a release cut never moves. RELEASE §2 realises
them, with the carriers that hold them, as refs of one release source.

### Work boundary

The method governs the boundary around a probabilistic, agentic or
delegated work unit; it does not absorb the worker's internal solution
strategy into the framework (P0, P6; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary`).
The declared boundary of such a unit is an object with six parts, which the
live specification and design should declare: the input and output contract; the
required context; the capability or role expectation; the admissible
evidence and evaluator regime; the provenance obligation; and the lawful
stop, hold, gap, continuation or completion states. The worker, tool, agent
or domain implementation owns the internal HOW inside that boundary unless
the product explicitly promotes part of that HOW into reusable declared
structure. The step of ACTIVATION §1 is this unit with its intake, context
and result algebra made exact.

### Imports between members

A member that uses a concept another member defines imports it and does
not define it again (P1, P3; provenance
`stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution`,
whose semantic import adopts the cited meaning unchanged). An import is
reference-only. Source and target meanings are identical owner-qualified
references, not new local definitions. Direction is from the named source
to the importing context; loss is none and no translation or ownership
transfer is asserted. An import provides no semantic, evaluation,
operation or decision authority (P6). A use that changes, narrows or loses
the source meaning is not an import and is never declared as one.

An import declaration states, for each imported concept (P1, P3, P6):

- what is imported: the concept, under the name its owner gives it;
- its owner: the owning section of the member that defines it, which is a
  place in the text, not a semantic authority (Authority kinds above);
- the source context: the bounded context the owning member declares, or
  that member itself where it declares none;
- the target context and the member that owns it;
- the direction and the loss, which one sentence may state for all the
  concepts of one declaration.

An import takes one of two forms. A declaration states these contents
for each imported concept in one place; between members of this corpus it
rests on the authority of the Product that owns the corpus, so the
relation is owner-authorised (P6). A reference at the point of use
that names the owning section is also an import: it states what is
imported and its owner; its source context is the one the list above
names, its target is the using member's context, and its direction, loss
and lack of authority are those stated above. A concept another member
defines enters a bounded context only by one of these forms, never by
proximity or equal spelling (P1, P3).

An activation binds each member's distinct coordinates in its selected
complete governing basis; equal cut selection does not mean equal member
coordinates. Adoption is a target's taking an imported concept into use
under the conditions its source states, which are its adoption premises.
Lifecycle and adoption remain source-owned. A changed member,
selected basis, source declaration or adoption premise requires fresh
applicability before use. An activation lacking the source meaning,
adoption or authority binding reports that unresolved relation before
dependent reliance rather than interpreting it from equal spelling (P3,
P5). For an evaluation that depends on the imported concept, a missing
source meaning, adoption or authority binding is an undeclared material
relation, the ground of `out_of_frame` ([Results](#results), Out of frame
or indeterminate); a changed member or basis whose applicability is not
yet re-established is the ground of `invalid_basis` (§4 Results).

Purpose and material relation of the declaration's contents, its two
forms, a member as source context and the two grounds above: a concept
used outside its owning section keeps one meaning and one owner, so two
members cannot answer one question two ways, and using a concept grants
no authority over it (P1, P6).

## 3. Commitments

Each commitment has exactly one standing, in the terms §1 defines; the
table states it, with a distinction the commitment retains. The adopted
premises, which §1 identifies as the recovered and independent
commitments, are commitments adopted for the domain this method governs,
not theorems derived from finite capacity alone, that is, from the bound
on an actor's envelope (P0). Particular method rules need these premises
plus their stated domain and policy choices, each with its owner
([Foundation to law](#foundation-to-law)). An argument from the premises
preserves that distinction; it does not create authority (P6). Purpose
and material relation of this paragraph and the standing column: each
commitment shows what grounds it, so no premise is presented as derived
and no consequence is taken for a premise (P6).

| Commitment | Standing | Distinction retained |
|---|---|---|
| P0 Bounded construction | recovered | the actor's internal path within a step is its own |
| P1 Interpretation | independent | structural success never establishes fidelity |
| P2 Purpose | independent | an obligation with no route to the outcome is unjustified |
| P3 Identity | independent | current state, historical observation and representation identity stay separate |
| P4a Typed composition | independent | composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states |
| P4b Conservation of step-produced facts | derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable | sources a later step can re-acquire are governed by sufficiency, not conservation |
| P5 Totality | derived from P0 and P6, with P0's open-world premise | a step cannot report success on a condition outside its context |
| P6 Justification and authority | independent | neither evidence nor authority is minted by the other |

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope.
Sources, named as sources and not as proof (§1): finite attention within a
declared envelope ([RF-002](REFERENCE_FRAME.md#rf-002-finite-attention)),
material sufficiency ([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)),
material closure ([AC-010](AXIOMATIC_CALCULUS.md#ac-010-material-closure)),
the [work boundary](#work-boundary), and the refinement of one outer
contract into inner steps
([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement).
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

P0's boundary commitment (the work boundary of §2): deterministic checks
and validation are evidence surfaces; they may optimise or prove a
domain-local path where the domain can make part of the work precise, and
they do not authorise the method, a runtime or a framework to absorb domain
solution strategy as constitutional law. Any unconstrained part of a
probabilistic worker's reasoning remains hidden worker-internal activity
and is forced back through the declared contracts, evidence, provenance and
control truth of the boundary. A framework layer that prescribes domain
solution strategy beyond the declared work contract and control truth has
crossed its authority boundary (P6). A profile may bind the unit to its own
traversal unit, in which that traversal is the admissible external space;
PROFILES §2 keeps that binding.

P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Non-entailment: let two steps fit their envelopes under one selected
outcome, keep declared identities, compose because the first's declared
result type, a length, meets the second's declared domain, record their
step-produced facts, return closed results and keep evidence apart from
authority, while the second reads the value under a contract no one
declares, in metres where the first wrote feet; P0 and P2 to P6 hold, yet
one representation has two meanings and no declared contract, which P1
forbids. "Algorithmic" means
explicit and structurally checkable; a semantic decision is lawful only
under an exact decision contract. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit
material obligations from the transformation they serve. Non-entailment:
let a finite actor realise a selected outer contract that names an
outcome, through steps that fit its envelope, read under declared
contracts, keep declared identities, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each interface's obligations are set by the capacity
available and not inherited from the transformation it serves; P0, P1 and
P3 to P6 hold, yet the same obligations count as adequate for opposite
outcomes and an obligation with no route to the outcome stands, which P2
forbids. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; a boundary is a claim with a proof obligation.
Non-entailment: let steps fit their envelopes under one selected outcome,
read under declared contracts, compose by type, record their
step-produced facts, return closed results and keep evidence apart from
authority, while each object's identity is taken from the place that
stores it and no authority, kind or value is declared, so an admissible
move makes one object two; P0 to P2 and P4a to P6 hold, yet identity is
neither declared nor kept across admissible change, which P3 forbids.
Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law),
restated in [WORLD_MODEL §9](WORLD_MODEL.md#9-entity-cut-construction).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's exact declared domain and preconditions.
Non-entailment: let a second step run on every output of the first, read it
under its own declared contract and return `invalid_basis` where the output
lies outside its declared domain, and let the composite keep only the
step-produced facts the outer contract needs. Each step fits its envelope and serves the selected
outcome, identities are declared and kept, the needed facts are recorded,
every result is closed and authority stays with its owners, so P0 to P3,
P4b, P5 and P6 hold. Yet the steps compose although the first's result type
need not meet the second's declared domain, and the first step's other
intermediate results and stop state are lost; P4a forbids both. The
retention has its own route to the outcome: when the composite is later
falsified or must be resumed, the kept intermediate results and stop state
locate the step to repair or restart, which a record of what the outer
contract needs does not supply (P2). Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them. The outer contract needs these facts (P2); the next
actor may re-acquire declared sources but not the producing step's private
result, because step-produced facts are not re-acquirable (P0); so only the
producing step can record them. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each is restated for its own scope by the
member §6 names.

P5 Totality. A step can meet a condition outside its context (P0's
open-world premise), and it cannot report success on one (P6). Its result
algebra therefore carries first-class outcomes other than success for such
a condition, and its control model names the next move. That these
outcomes are three, indeterminate, out_of_frame and invalid_basis, is a
declared choice conserved from RF-012, whose owner is §4
[Results](#results) (family F3, first row). Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in §4 [Results](#results), and are
stated as laws in
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal).

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope.
Non-entailment: a bounded actor satisfying all else can still take a green
label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004 ([IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)),
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

### Foundation to law

A family of deciding rules is a group of related rules that decide
outcomes; it is a material family when the outcomes it decides matter to
the method's selected outcome (P2). Each material family is traced in one
family table. The table sits in the member that owns the family, at the
section where an actor enters the family, so the actor meets the trace
where it applies the rules (P2, P6). A family table first states its
instance premises: the conditions of the situations the family governs,
which the commitments do not supply. They are labelled as instance
premises, never as commitments. The table then has one row per
consequence, in four columns:

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner |
|---|---|---|---|

- Premises, with standing: the commitments the row rests on, each with its
  standing from the table of commitments above, and the instance premises
  it uses. A profile's table also names the families it imports, under
  [PROFILES §1](PROFILES.md#1-the-boundary).
- Consequence that follows: what those premises together require of the
  family.
- Rule in this member that states it: the owning section or clause,
  linked. Where a table accounts for a section of another member, this
  column names that section, linked and marked as outside this member, or
  a paragraph after the table names the sections of other members that
  apply its rows; the section keeps its owner.
- Added domain or policy choice, and its owner: what the rule decides that
  the premises leave open, with the member, profile, adopting Product (a
  Product that applies this method) or authority that owns it, or "none".

A family table is a trace. Its consequence and choice columns state no
determination that the rule it names does not state, and the table owns
none of the rules or choices it lists (P1, P6).

Standing of the consequences. The consequences are arguments from the
stated premises, not proofs of every clause of the rules they name.
Concrete carrier layouts, the number of actors, numeric limits, adoption
of an optional profile, release procedures and the values of each
refinement are added choices. They are not inferred from the foundational
commitments. Each table leaves those choices at their owners and adds no
record that its rules do not require. Tables over some members are not a
derivation of every member: the index below accounts for every member, by
the table that traces it, by a row marked table pending, or by the reason
it has none. Each family table refers here for the standing of its
consequences and does not restate it (P6, P2).

Index of families. Each row names a family, the section that holds its
table and the members or sections the table accounts for. A row marked
table pending names the section that is to hold its table; until that
table is written, the row names its members and traces none of their
rules. The index decides nothing: each rule is in its owning section, and
each trace is in its table (P1, P6).

| ID | Family | Table | Accounts for |
|---|---|---|---|
| F1 | Frames and context | [REFERENCE_FRAME §1](REFERENCE_FRAME.md#1-the-frame-as-the-engagement-unit) | REFERENCE_FRAME; ACTIVATION §2; FOUNDATIONS §2 Frame objects, Authority kinds, Disjointness and independence, The frame tuple |
| F2 | Transitions, steps and configuration | [ACTIVATION §1](ACTIVATION.md#1-the-step) | ACTIVATION §1, §4; SPEC_METHOD §8 except delivery priority |
| F3 | Results and their combination | [FOUNDATIONS §4 Results](#results) | FOUNDATIONS §4, and the result grounds of §2 Imports between members; ACTIVATION §3; RF-012; AC-007; EVALUATION §4 |
| F4 | Work state, resumption and reuse | [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) | ACTIVATION §5, §7 |
| F5 | Proportionality and cost | [ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality) | ACTIVATION §6; SPEC_METHOD §8 delivery priority |
| F6 | Claims, evidence, assessment and acceptance | [EVALUATION §1](EVALUATION.md#1-claims) | EVALUATION §1 to §5 |
| F7 | Conformance, equivalence and qualification | [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations) | EVALUATION §6, §7; CONFORMANCE |
| F8 | Identity | [IDENTITY §1](IDENTITY.md#1-position), table pending | IDENTITY |
| F9 | The a_c calculus | [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position), table pending | AXIOMATIC_CALCULUS |
| F10 | Constitutional chain, outcome and build-tenant binding | [SPEC_METHOD §2](SPEC_METHOD.md#2-the-chain) | SPEC_METHOD §1 to §3, §6, §9 to §11 |
| F11 | Change management and ambiguity | [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | SPEC_METHOD §4, §5, §7 |
| F12 | Binding a project to the method | [PRODUCT_DEFINITION §1](PRODUCT_DEFINITION.md#1-overlay-and-layout-independence) | PRODUCT_DEFINITION; FOUNDATIONS §2 Imports between members except its result grounds (F3) |
| F13 | Work carriers | [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) | TICKETS |
| F14 | Assurance and testing | [ASSURANCE §1](ASSURANCE.md#1-verification-layers), table pending | ASSURANCE |
| F15 | Release and successor conservation | [RELEASE §1](RELEASE.md#1-context-and-position), table pending | RELEASE; FOUNDATIONS §2 Product lineage objects |
| F16 | Engagement baseline (operational profile) | [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability) | EXECUTIVE_BASELINE |
| F17 | Software design | [DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position) | DESIGN_MODULE |
| F18 | Outcome-driven development | [ODD §1](ODD.md#1-position) | ODD |
| F19 | Traversal occurrence | [TRAVERSAL_OCCURRENCE, Position](TRAVERSAL_OCCURRENCE.md#position) | TRAVERSAL_OCCURRENCE |
| F20 | UX | [UX §1](UX.md#1-position), table pending | UX |
| F21 | World model | [WORLD_MODEL §1](WORLD_MODEL.md#1-position), table pending | WORLD_MODEL |

Members and sections with no family table, each with its reason:

- FOUNDATIONS §1, the ontology table of §2, and §3: they state the
  vocabulary of standing, the objects the commitments are about, and the
  commitments themselves with this format, which every family table cites
  as its premises. §2 Work boundary is the object that P0's boundary
  commitment states. FOUNDATIONS §5: its hypotheses are not law and decide
  no outcome.
- PROFILES: §1 owns the import rule that every profile table cites in its
  premise column; §2 to §6 index the profiles, whose own tables trace
  their bindings.
- POSTING_GUIDE and WRITING_GUIDE: their conventions are policy choices
  whose owner is the guide.
- GLOSSARY: a locator index; it decides nothing.
- The standards README and the other packaging (templates, schemas and
  plugin files): they own no determination.
- The source-dispositions section of every member: it records where each
  predecessor claim is carried and decides no outcome of the method.

Purpose and material relation of the family table and its format,
instance premises, the standing of the consequences and this index: for
every member, a reader can see which commitments its rules
rest on and which choices they add, with their owners, so no added choice
is presented as following from the foundations and no partial trace as a
derivation of the whole method (P6, P2).

## 4. Algebra

Composition. For steps s₁: X → Y and s₂: Y → Z, s₂ ∘ s₁ exists only under P4a.
The composite's output carries both steps' step-produced facts; its result
is composed as [Conjunction of results](#conjunction-of-results) states.
[RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand) states once
when a composition law is required and when independently activated
evaluations may instead return closed results to one declared conjunction
or decision rule (P4a).

Conservation accounting. Every transformation records what it preserved,
introduced and removed, its external resolution witnesses and its residuals
(AC-013). How results, known failures and uncovered coverage combine is
[Conjunction of results](#conjunction-of-results).

Reference versus body. A reference conserves a relation when its owner,
exact selector, authenticity, availability and completeness support the same
consuming decision. An inaccessible or insufficient reference is a residual,
not success. A projection cannot trim a required member to fit a carrier or
budget
([AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection)).

Latitude. Two values differ lawfully only through a declared latitude or
transformation relation; preference, probabilistic choice and human presence
are not implicit latitude
([AC-008](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude)).

Shared machinery. Computational similarity yields a commonisation candidate,
never an adjudication of identity or authority; one implementation may serve
many instances while each instance keeps its responsibility and binding
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019),
[UP-023](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#capability-and-foundation-selection-stdo-up-023)).

Formal fragment (P6, P1). A categorical claim, about this method or about a
construction made with it, is established only with the demonstration it
requires, as far as each part applies to it:

- each category it claims states its objects, its arrows, when two arrows
  are equal, an identity arrow on each object, and a composition of arrows
  that is associative and has those identities as units;
- each map between categories is defined on objects and on arrows, and is
  called a functor only after its preservation of identities and
  composition is proved;
- its laws, records and maps are represented in a_c
  ([AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md)), keeping apart which
  statements are premises, which are consequences and which are declared
  choices; the separate identities of a_c, its interpretations and their
  carriers are
  [AC-020](AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation)'s,
  and what a structural check of the representation establishes is
  [EVALUATION §2](EVALUATION.md#2-separation)'s;
- it names its evidence class, the kind of support it rests on: mechanically
  checked, established by mathematical argument, tested against an
  independently specified oracle, or unresolved.

Whether a claim asserts conformance, an equivalence or a map's preservation
of structure, and how those claims differ, is the equivalence ladder of
[EVALUATION §6](EVALUATION.md#6-conformance-of-realisations). What a
refinement or rewrite step preserves, and the law that licenses it, are
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement. A
categorical statement without the demonstration it requires is a
hypothesis: it is not law and is carried for falsification with §5. This
conserves
[functor kinds](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds),
which requires a model claiming functor laws to define its source and
target categories and prove identity and composition preservation, and
asserts no categorical functor itself. Purpose and material relation of
arrow equality, associativity, the representation in a_c and the evidence
class: a categorical statement is useful only where its constructions
preserve meaning, and these are what preservation must show (P1, P6).

Formal fragment, hypothesis H1, categorical structure: with 𝒜 the free category on typed primitives, ℐ the selected
carrier sets with total functions and 𝒞_H pairs of functions with additive
costs, S: 𝒜 → ℐ and R_H: 𝒜 → 𝒞_H would be
functors, S neither faithful nor an equivalence. Its evidence class is
unresolved: no rc.2 clause and no argument in this corpus establishes it,
S and R_H are not defined on arrows, and no preservation of identities or
composition is proved. Until its objects, arrows, arrow equality,
identities and composition are written and preservation is proved, the
diagram is notation; it is not law and is carried for falsification with
§5. H names an architecture, never a runtime.

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
one rule ([Conjunction of results](#conjunction-of-results)). Purpose and
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
  [closed result](ACTIVATION.md#7-closed-result-and-reuse), and it is never mapped
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
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results) states
RF-012 as a law over frames and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
states AC-007 as a law over constraints; each uses this core and neither
defines it again.

Refinements. A member, profile or adopting Product that needs finer
outcomes defines a refinement. The refinement names the question it
answers and the predicate its mapping is for, and maps every refined value
to exactly one core value. No outcome exists outside the core; a
refinement adds no core value and keeps the pressure of `indeterminate`,
`out_of_frame` and `invalid_basis` explicit. Where a refined value would
map to one of two core values according to its cause, the cause is part of
the refined value and each resulting value maps once (P5, P1). The
refinements for admission, activation and steps are
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition); each other
member, profile and adopting Product states its mapping where it defines
its values.

Availability, assessment and acceptance are separate results, each with its
own predicate: that a step produced a candidate; that the candidate meets
its declared criteria; and that the
[decision owner](ACTIVATION.md#roles-and-delegation) accepts it at its
boundary. A step having produced a candidate never maps to the candidate's
fitness or acceptance, and acceptance is never inferred from a successful
step (P6; [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition),
[EVALUATION §4](EVALUATION.md#4-review-results) and
[§5](EVALUATION.md#5-acceptance)).

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
  ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement); rc.2 RF
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
  [construction availability](ACTIVATION.md#construction-availability), and
  its work state ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart))
  carries the unexercised capability as a residual (P6). In either case
  the unexercised part, B above, has no result: in every conjunction over
  it, it is a planned assessment without a closed result, and the known
  failure A survives with it ([Conjunction of results](#conjunction-of-results)).
  The evaluation's result and the step's stop state answer different
  questions, so the step's stop value never becomes the evaluation's
  result.

Foundation to law for results and their combination (family F3). The
table covers every rule of §4 and the result grounds of §2 Imports
between members, in the format of
[Foundation to law](#foundation-to-law), which states the standing of its
consequences. Purpose and material relation: a reader of §4 sees which
commitments each result rule rests on and which choices it adds, with their
owners (P6, P2). Instance premises, which the commitments do not supply:
(i) an evaluation declares its predicate, subject and basis; (ii) results
of several evaluations, steps or members are combined into one decision;
(iii) members, profiles and adopting Products need outcomes finer than the
core.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner |
|---|---|---|---|
| P5 (derived from P0 and P6), P6 (independent); (i), (ii) | every performed evaluation returns one closed value of one algebra shared by every member, with a value for a claim that holds, one that fails, one the evidence cannot decide, one that needs a relation or capability the frame lacks, and one whose basis cannot support it | [Results](#results), the value table | the value names, and the division of P5's outcomes other than success into `indeterminate`, `out_of_frame` and `invalid_basis`, conserved from RF-012; owner: this section |
| P6 (independent), P5 (derived from P0 and P6) | a result claims no more than it establishes: only `satisfied` establishes the predicate, and no refinement or mapping raises a result's standing | [Results](#results), Standing, and the rule that nothing raises standing; for the choice, [Conjunction of results](#conjunction-of-results), Reported value | the order among the four other values within one combination; owner: the member or profile that applies the conjunction, in its declared rule |
| P1 (independent), P6 (independent); (iii) | a core value alone does not carry a refined value's domain meaning, so a result records its predicate and domain outcome, and the definer of a refined value keeps its meaning | [Results](#results), Recording | each refined value and its domain meaning; owner: the member, profile or adopting Product that defines it |
| P6 (independent) | an evaluation that was not performed supports no claim, so it has no closed result and is never read as undecided | [Results](#results), Not performed, and the third item of the rule that nothing raises standing | recording non-performance as the absence of a closed result, not as a core value; owner: this section |
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile or adopting Product that defines it |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](EVALUATION.md#5-acceptance) names |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](ACTIVATION.md#construction-availability), construction availability |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains | [Conjunction of results](#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule |
| P4a (independent), P4b (derived from P0 and P2) | composed steps exist only under typed composition; the composite carries both steps' step-produced facts, and its result for the outer predicate is the conjunction over the outer contract's obligations | [§4](#4-algebra) Composition; [Conjunction of results](#conjunction-of-results), Composition of results; [RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand), outside this member | whether a composition law is needed, under the conditions RF-010 states; owner: the governing evaluation |
| P4b (derived from P0 and P2), P3 (independent) | every transformation records what it preserved, introduced and removed, its external witnesses and its residuals, so no fact is lost unrecorded | [§4](#4-algebra) Conservation accounting | the record's fields; owner: [AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation) |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P0 (recovered) | a reference stands for a body only where it supports the same consuming decision; otherwise the shortfall is a residual, never success, and no carrier or budget limit trims a required member | [§4](#4-algebra) Reference versus body | none |
| P1 (independent), P6 (independent) | two values differ lawfully only through a declared relation; preference, probabilistic choice and human presence supply none | [§4](#4-algebra) Latitude | each latitude or transformation relation; owner: the owner of the contract that declares it |
| P3 (independent), P6 (independent) | similar computation proposes shared machinery and never decides identity or authority; each instance keeps its responsibility and binding | [§4](#4-algebra) Shared machinery | whether one implementation serves several instances; owner: the design decision of [DESIGN_MODULE §5](DESIGN_MODULE.md#capability-and-foundation-selection-up-023) |
| P6 (independent), P1 (independent) | a categorical claim is established only with its demonstration, and without it is a hypothesis | [§4](#4-algebra) Formal fragment | which categorical claims are made; owner: the member, profile or adopting Product that makes the claim |

RF-012 in [REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results),
AC-007 in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
and [EVALUATION §4](EVALUATION.md#4-review-results) apply the first row's
algebra to frames, constraints and reviews and add no choice of their own
beyond any refinement they map under the fifth row;
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) holds the
step's refinements of the fifth row and the stop state of the seventh.

### Conjunction of results

Conjunction combines results into one result for a composite predicate: a
claim made of component claims, a decision over several evaluations, or
the outer contract of composed steps. It is defined here once, over the
core. A member or profile that combines results applies this rule and
declares only the choices it leaves open (P4a, P4b, P5, P6). Purpose and
material relation: failure, undecidability, non-performance and uncertain
effects stay distinct after combination, so a composite can neither report
success nor hide which kind of gap it has while one of them remains.

A conjunction takes three inputs and keeps them apart:

1. the closed results returned, each a core value with its predicate and
   domain outcome;
2. the planned assessments that have no closed result applicable to the
   composite: evaluations the composite requires that were not performed,
   or whose result is absent, stale, bound to another subject or basis, or
   incapable of establishing its claim;
3. the required coverage that no planned assessment addresses: for a
   required obligation set R and the coverage C that the planned
   assessments admit, the uncovered coverage R minus C.

Gaps. A conjunction with any item in the second or third input is never
`satisfied`. Its record names which kind of gap it has, not performed,
uncovered or both, and each item. An uncovered obligation is never
reported as satisfied or as an omitted planned assessment; a planned
assessment without a closed result is never reported as uncovered or as an
`indeterminate` component.

Survival. Every known failure (a `falsified` result with its
counterexample), every planned assessment without a closed result and
every uncovered obligation is carried with the composite and survives every
join: combining conjunctions takes the union of known failures and of
planned assessments without a closed result, and recomputes uncovered
coverage over the combined obligations. A known failure and a gap of
either kind survive every join. Common agreement among contributors
cannot discard a constraint or a material counterexample that only one
contributor found. A missing, wrong-subject, conflicted or indeterminate
mandatory result stays unresolved under the declared rule, and aggregate
satisfied status cannot replace it (P4b, P5).

Predicates travel. Each component keeps its predicate and domain outcome
through every join, so an uncertain effect stays distinct from a failure
and from an undecided claim, and a `satisfied` for one predicate never
counts toward another: a step's `satisfied` for "a candidate is available"
never counts toward the candidate's fitness or acceptance.

Reported value. The conjunction is `satisfied` only when every mandatory
result is `satisfied` with valid applicable evidence, the declared basis
relations agree, and the second and third inputs are empty. A composite
with a known failure or an uncovered required obligation cannot project
success. Where a mandatory result is not `satisfied`, the conjunction
reports a non-satisfied value chosen by its declared rule from those
returned; no universal order among the non-satisfied values exists, and
the member or profile that applies the conjunction declares its own in
its declared rule. Where every mandatory returned result is `satisfied`
and the declared basis relations disagree, the conjunction reports
`invalid_basis`, because no coherent composite basis supports the
composite predicate (§2, Basis); any gaps stay recorded by kind. Where
every mandatory returned result is `satisfied`, the declared basis
relations agree and a gap remains, the conjunction reports
`indeterminate`, because the results it holds cannot decide the composite
predicate; that value is the conjunction's own, and the gaps stay
recorded by kind.

The declared rule. A conjunction declares which results are mandatory; how
conflict and indeterminacy are handled; which basis relations must agree,
results on different bases combining only under a declared coherent
composite basis (§2, Basis); which decision authority owns the
conjunction; and whether any result may veto or defer the decision.
Conjunction does not transfer the semantic authority of a contributing
evaluation (P6, P4a).

Composition of results. The result of composed steps for the outer
predicate is the conjunction of the steps' results, with the outer
contract's obligations as the required coverage. That each step returned
`satisfied` supports the outer predicate only where the refinement's
premises hold ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement),
Refinement).

Provenance: rc.2 RF #result-conjunction and
#applicability-and-required-results, and the combination rule of
conservation accounting.

## 5. Hypotheses

Not law; carried for falsification: categorical equivalence of 𝒜 and ℐ under
some reformulation; universal algorithmic capture of meaning; the statistical
Markov boundary (candidate status under
[WORLD_MODEL §4](WORLD_MODEL.md#epistemic-status); provenance
[WORLD_MODEL_METHOD](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct));
traversal composition laws of any runtime.

## 6. Source dispositions

| rc.2 clause family | Disposition in this corpus |
|---|---|
| AC Position, Derivation Provenance, Scope | conserved; restated in AXIOMATIC_CALCULUS §1 |
| AC Core Signature, Typed Records and its five records | conserved; restated in AXIOMATIC_CALCULUS §2 and §3; Semantic Object and Residual are related to the §2 objects Object and Residual, the definitions stay here |
| AC-001, AC-003, AC-004, AC-012 | conserved; restated in AXIOMATIC_CALCULUS §4 |
| AC-002, AC-005, AC-006, AC-009, AC-014 | conserved; restated in AXIOMATIC_CALCULUS §4 as laws over the §2 objects Object, Authority, Basis, Residual and Judgment, which are defined once here; P3, P4b and P6 consume them |
| AC-007 | conserved; restated in AXIOMATIC_CALCULUS §4 as a law over constraints using the core result algebra of §4 Results, where its no-coercion rule is restated |
| AC-008, AC-011 | conserved; restated in AXIOMATIC_CALCULUS §4; their generic forms over any two values and any reference are the Latitude and Reference-versus-body paragraphs of §4 above |
| AC-010 | conserved; restated in AXIOMATIC_CALCULUS §4; applied by ACTIVATION §2 |
| AC-013 transformation | conserved; restated in full in AXIOMATIC_CALCULUS §4; its delta fields are the conservation accounting of §4 above |
| AC Fundamental Laws heading | not applicable: heading with no claim text (20 bytes); listed in AXIOMATIC_CALCULUS §11 |
| AC Traversals And Functor Kinds, AC-015, AC-016 | conserved; restated in AXIOMATIC_CALCULUS §5; P4a consumes AC-016; the functor-kind proof obligation is carried for every categorical claim by the demonstration of §4 Formal fragment, which adds arrow equality, associativity, the representation in a_c and the evidence class, and under which H1 stays a hypothesis |
| AC Interpretation And Models, AC-017, AC-018, AC-019 | conserved; restated in AXIOMATIC_CALCULUS §6; P1 consumes them; the generic structural-and-semantic separation is EVALUATION §2 |
| AC Subject And Carrier Boundaries, AC-020 | conserved; restated in AXIOMATIC_CALCULUS §7; applied to release lineage in SPEC_METHOD §6 |
| AC Exact Calculus Identity | conserved; the identity law is restated in AXIOMATIC_CALCULUS §8; the record instance is a release artefact issued under RELEASE and AC-020 at this corpus's own release |
| AC Application Boundary, External Imports And Specializations, Exclusions, Conformance Obligations | conserved; restated in AXIOMATIC_CALCULUS §9 and §10 |
| RF definitions (#definitions and its 17 children) | conserved; restated in §2 (amended rows, frame objects, authority kinds, disjointness and independence, the frame tuple); rows in the table below |
| RF-001 to RF-017, engagement atom, frame set, functions, conjunction, relations, coverage, completeness, revision, activation packet, violations, declarations, closure | conserved; restated in REFERENCE_FRAME, whose §15 lists the rows; the algebra RF-012 names is defined once in §4 Results, and the rule of result conjunction once in §4 Conjunction of results |
| RF-012, AC-007 core values | conserved; the five values with their meanings, the no-coercion rule and the boundary between out_of_frame and indeterminate are restated in §4 Results, whose first two boundary cases restate RF-012's values; two clauses there are tightenings that rc.2 implies and does not state: the undefined-term clause, because a relation is material when its lawful change can change the evaluation result, which a term's meaning can, and an undefined term neither appears in the frame nor enters through a declared input (rc.2 #material-relation, RF-003; P1); and the unexercised-capability case, because RF-012, Return A Closed Result, Applicability And Required Results and Result Conjunction together return what a sufficient evaluation supports and leave the unexercised part open (P5, P6); REFERENCE_FRAME §3 and AXIOMATIC_CALCULUS §4 state them as laws and dispose their rows; ACTIVATION §3 refines the core for steps. New in §4 Results, each required by the single result algebra and its purpose stated there: the standing relation and the no-raise rule, the separation of a not-performed evaluation from an indeterminate one, the recording of predicate and domain outcome with the core value, the separation of availability, assessment and acceptance, and the rule for refinements. RF-012's externally owned compatible extension is a refinement that a member, profile or adopting Product defines under §4 Refinements, which names that owner. Family F3 at the end of §4 Results traces these rules to the commitments |
| RF Result Conjunction; the conjunction sentences of Applicability And Required Results | conserved; the conjunction rule is restated in §4 Conjunction of results, which also carries the combination rule formerly stated under conservation accounting; REFERENCE_FRAME §6 and ACTIVATION §1 Applicability refer to it, and REFERENCE_FRAME §15 and ACTIVATION §8 dispose the rows. New there, with the purpose stated there: the three inputs kept apart, the gap record, the travelling predicate, and the reported value where only gaps remain or the declared basis relations disagree |
| RF engagement, frame qualification, method self-qualification | conserved; restated in ACTIVATION §1 to §4 and §7 and in EVALUATION §7, whose tables list the rows |
| UP-001, UP-004, UP-008, UP-022 | conserved; UP-004 restated in IDENTITY §6, whose §13 lists the IDENTITY_METHOD rows; all four consumed by EVALUATION |
| UP-013, UP-014, UP-005 | conserved; UP-013 restated in SPEC_METHOD §3 and UP-014 in ACTIVATION §6 with its delivery priority in SPEC_METHOD §8; UP-005 restated in DESIGN_MODULE §6 Boundary and governance cost, its proportionality relation ACTIVATION §6; P2 consumes them |
| UP-015 | conserved; restated in full in RELEASE §9, which owns the disposition values, and applied to acceptance evidence in EVALUATION §5; the standing of §1 is not a disposition |
| RM Release Identities | conserved; candidate source, release subject and version-line selector restated in §2 Release objects beside the release cut; their realisation as refs, with the namespace, subtree and branch carriers, in RELEASE §2, whose §11 lists the RELEASE_METHOD rows |
| IDENTITY_METHOD scoped identity | conserved; the Object of §2 carries scoped identity, whose laws are IDENTITY §2 |
| UP-016, UP-018, UP-019, UP-023 | conserved; all four restated in DESIGN_MODULE §5 and §7, which disposes their rows; UP-016's admission semantics are ACTIVATION §4, UP-018's general reconstruction rule ACTIVATION §1 Intake, and UP-019's and UP-023's shared machinery §4 above, each pointed to |
| UP-017, UP-021 | conserved; UP-017 restated in DESIGN_MODULE §5 Bounded frame conservation, which disposes its row, its frame instance being P4b's one obligation (reframed with AC-005, AC-009 and AC-013) and its seam rule ACTIVATION §1 and §4; UP-021 and its standing structural qualification are restated in full in ACTIVATION §4 |
| UP-020 | conserved; restated in ACTIVATION §1, §3, §5 and §7 |
| SM Probabilistic Work Boundary | conserved; restated in §2 Work boundary and §3 under P0; ACTIVATION §1 consumes it; row in the table below |
| SM Recursive Product Taxonomy | conserved; restated in §2 Product lineage objects; SPEC_METHOD §6 consumes it; row in the table below |
| SM Bounded-Context Semantic Resolution, its semantic import | conserved; the unchanged-meaning import is restated in §2 Imports between members, which owns the rule for imports; PRODUCT_DEFINITION §5 refines that rule between a project's bounded contexts for a declared target scope, keeps the bounded context, the semantic address, the carrier and the relation kinds other than import, and disposes the row; new in §2, with its purpose stated there: the declaration's contents and two forms, a member as source context, and the grounds of `out_of_frame` and `invalid_basis` |
| SM Ambiguity Governance | conserved; restated in SPEC_METHOD §5; its outcome refinement, mapped into the core, is ACTIVATION §3 Ambiguity outcome and its hard stops ACTIVATION §4 |
| ODD, DESIGN_MODULE, UX, WORLD_MODEL profile law | conserved; restated in full in the ODD, DESIGN_MODULE, UX and WORLD_MODEL members, which dispose their rows and are indexed in PROFILES §2 to §5; nothing imported into tier 1. P0 names among its sources the refinement of ACTIVATION §4, which generalises ODD's graph functions |

New law with no predecessor row, each part stating its purpose and
material relation where it stands: the opening paragraph of §3 and the
standing column of its table; §3 Foundation to law, with the family table
format, instance premises, the standing of the consequences and the index
of families; the family F3 table at the end of §4 Results; and, in §4
Formal fragment, arrow equality, associativity, the representation in a_c
and the evidence class, which the AC Traversals And Functor Kinds row
above names.

RF rows received by this member (anchors into rc.2
REFERENCE_FRAME_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #definitions | not applicable: heading with no claim text (15 bytes); its children are disposed individually | §2 |
| #evaluation | conserved | §2 Frame objects (Evaluation, Evaluation family) |
| #workspace | conserved | §2 Frame objects |
| #basis | conserved | §2 ontology table, Basis |
| #material-relation | conserved | §2 ontology table, Material |
| #material-relation-manifold | conserved | §2 Frame objects |
| #coordinate | conserved | §2 Frame objects |
| #topology | conserved | §2 Frame objects |
| #evidence | conserved | §2 ontology table, Evidence |
| #authority | conserved | §2 Authority kinds |
| #disjointness-and-independence | conserved | §2 Disjointness and independence |
| #capability-envelope | conserved | §2 Frame objects |
| #reference-frame | conserved | §2 Frame objects; §2 The frame tuple |
| #activated-frame | conserved | §2 Frame objects |
| #frame-set | conserved | §2 Frame objects |
| #active-frame-configuration | conserved | §2 Frame objects |
| #lens | conserved | §2 Frame objects |
| #role-persona-abstraction-and-component | conserved | §2 Frame objects |

SM rows received by this member (anchors into rc.2 SPEC_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #probabilistic-work-boundary | conserved; the six declared parts, the worker's ownership of the internal HOW, the evidence-surface rule and the authority-boundary rule; the profile binding to one traversal is generalised and kept by PROFILES §2 | §2 Work boundary; §3 P0 |
| #recursive-product-taxonomy | conserved; the eight objects with their concept identities, the six governing rules, the compiler analogy and the load-bearing claim | §2 Product lineage objects |
