# FOUNDATIONS

Tier 1. Owns the ontology, the commitments as law, the algebra of composition
and conservation, and the list of hypotheses. Every later document consumes
these definitions by reference and adds none of its own.

## 1. Vocabulary of standing

Every claim of the predecessor cut `stdo://releases/v2.5.1-rc.2/` receives
exactly one disposition in this corpus. The frontier is the tenant copy of
[PREDECESSOR_CLAIMS](../frontier/PREDECESSOR_CLAIMS.md), one row per
predecessor section; the values are those of
[UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015)
applied to the corpus itself:

- conserved: the claim is restated in this corpus's own text with every
  determination the predecessor makes, and the locus names where; a route
  to the predecessor is provenance, never the disposition;
- superseded: an accepted successor relation replaces the claim; the
  successor clause and what changed are named;
- intentionally removed: Jim's decision as Product authority, with the
  reason; no Writer records this value;
- not applicable: the claim has no successor effect; the bounded reason is
  given;
- unresolved: the only other state; it blocks qualification of the
  affected claim.

A note that a conserved claim was reframed, carried at a different scope
or by a different owner, is commentary on the carrying, never a
disposition. A clause with no predecessor row is new law and names the
purpose and material relation that require it. A commitment has one
standing relative to the others: recovered, derived (with named premises),
independent (argued by non-entailment) or hypothesis. Every clause names
the principle (P0 to P6, §3) that requires it. This corpus is complete and
applicable without the predecessor remaining operative; the predecessor
stays the builder of this construction until a release decision.

## 2. Ontology

| Term | Definition | Requires |
|---|---|---|
| Subject | the thing a claim, representation or transformation is about; exact, with inventory and bytes or semantic addresses | P3 |
| Representation | bytes, text, a model or a program standing for a subject; equal representations do not establish equal meaning | P1 |
| Interpretation | a declared contract from representation to meaning within a context; says which distinctions a consumer may rely on and which are residual | P1 |
| Context | the declared scope under which an interpretation holds: subject, definitions, basis, admissible observations | P1 |
| Outcome U | a selected, owner-defined, directly verifiable state with an acceptance interval; adequacy of a transformation is judged against it | P2 |
| Object O | a subject with scoped identity (authority, kind, value), a boundary, current state and declared material relations; identity survives admissible state and encoding change | P3 |
| Actor | whoever performs a step within a declared capability envelope (context, attention, time, capability); roles (constructor, reviewer, executive) are relations an actor occupies, not kinds of actor | P0, P6 |
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
[IDENTITY_METHOD](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#1-scoped-identity)
and
[AC-002](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-002-scoped-identity);
outcome conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013);
actor and envelope conserve
[RF-002](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-002-finite-attention);
claim, judgment and authority conserve
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001),
[AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation),
[UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004);
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
| Workspace | the bounded body of material reasoned over or acted upon: constitutional sources, domain assets, designs, implementations, tools, runtime state, evidence, historical records, external dependencies and human decisions; broader than a repository, which is one possible carrier | P3 |
| Material-relation manifold | the finite, jointly interpretable set of variables, entities, identities, states, relations, invariants, authorities, observations and exclusions an evaluation family needs; a bounded relation space whose coordinate charts may overlap; no geometric mathematics or runtime abstraction is implied | P0, P2 |
| Coordinate | the complete local position from which a value, event, decision, observation or action is interpreted: the basis, identity, lineage, input, evidence and authority information the evaluation requires; equal names, values, shapes, locations or apparent topology positions do not establish coordinate equality, which follows a declared relation | P1, P3 |
| Topology | the relation structure among the material entities, capabilities, authorities, lifecycle state spaces, adjacencies and seams visible to a frame at one basis; a frame need not hold the workspace's complete topology; a state-value change preserves the frame topology only when it preserves every such entity, relation, lifecycle, authority, capability, adjacency and seam, and a transition that changes any of them is a topology mutation that may invalidate the frame's coordinates | P3 |
| Capability envelope | the competence, context capacity, tools, access, applicable evaluation- or assurance-independence conditions and configuration required to activate a frame and perform its evaluations; the same frame may be usable by one actor and unusable by another; actor capability may justify a different frame size or activation sequence and can neither waive an invariant nor widen authority | P0, P6 |
| Reference frame | a finite specification of the attention, coordinates, authority, evidence and result relations required to perform one declared evaluation family over a stated basis; its components are the frame tuple below | P0 |
| Activated frame | one frame declaration bound to an exact evaluation, workspace subject, basis, actor and evidence-acquisition boundary; a reusable declaration is not evidence that a particular activation was correct | P3, P6 |
| Frame set | the human-declared family of frames available for a governed outcome or workspace; it may intentionally hold overlaps, alternatives, specialist frames, broad exploratory frames and separately activated assurance frames; it is not required to be a partition, tree, stack or exhaustive ontology | P6 |
| Active frame configuration | the set of frame activations and declared result relations used for one evaluation or decision; one frame, or several disjoint, overlapping or composed frames; separately activated evaluations may be disjoint or overlapping | P4a |
| Lens | a reusable family of questions applied across a frame configuration; authority, capability and reuse, temporal behaviour, transport and proof are lenses when named abstractly; a lens becomes a frame only when instantiated with a bounded evaluation, basis, material manifold, evidence, authorities, result algebra and capability envelope | P2 |
| Role, persona, abstraction, component | a role allocates responsibility or authority; a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |

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
R the closed result algebra (ACTIVATION §3); J the invalidation and rechart
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
this member now owns under the selected complete basis; the concept
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
live specification and design declare: the input and output contract; the
required context; the capability or role expectation; the admissible
evidence and evaluator regime; the provenance obligation; and the lawful
stop, hold, gap, continuation or completion states. The worker, tool, agent
or domain implementation owns the internal HOW inside that boundary unless
the product explicitly promotes part of that HOW into reusable declared
structure. The step of ACTIVATION §1 is this unit with its intake, context
and result algebra made exact.

## 3. Commitments

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope. The
actor's internal path within a step is its own. Recovered as a composite;
the generic statement is reframed from the ODD profile's graph functions.
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
Independent: with purpose, identity, evidence and authority fixed, two
contracts give one representation two meanings. "Algorithmic" means explicit
and structurally checkable; a semantic decision is lawful only under an exact
decision contract; structural success never establishes fidelity. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit material
obligations from the transformation they serve; an obligation with no route
to the outcome is unjustified. Independent: identical capacity serves
opposite purposes. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; current state, historical observation and
representation identity stay separate; a boundary is a claim with a proof
obligation. Independent: equal capacity admits identity by persistence or by
digest. Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's domain and preconditions; composition
retains both identities, intermediate results, judgments, evidence,
authority, provenance and stop states. Independent. Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them; sources a later step can re-acquire are governed by
sufficiency, not conservation. Derived from P0 with P2 and the
step-produced-facts premise. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each continues to govern its own scope.

P5 Totality. A step can meet a condition outside its context; it cannot
report success on one; so its result algebra carries indeterminate,
out_of_frame and invalid_basis as first-class outcomes and its control model
names the next move. Derived from P0 with the open-world premise and P6.
Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in ACTIVATION §3 and continue to govern.

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope;
neither is minted by the other. Independent: a bounded actor satisfying all
else can still take a green label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004,
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

## 4. Algebra

Composition. For steps s₁: X → Y and s₂: Y → Z, s₂ ∘ s₁ exists only under P4a.
The composite's output carries both steps' step-produced facts. Composition
law is required only where the governing evaluation combines internal
variables or transports values across steps; independent closed results may
instead go to one declared conjunction (RF-010).

Conservation accounting. Every transformation records what it preserved,
introduced and removed, its external resolution witnesses and its residuals
(AC-013). For a required obligation set R and admitted coverage C, uncovered
coverage is R minus C; combining results takes the union of known failures
and recomputes uncovered coverage; a composite with a known failure or an
uncovered required obligation cannot project success. A known failure A and
an uncovered obligation B survive every join.

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

Formal fragment (new in this corpus; P1). Where 𝒜 is the free category on
typed primitives, ℐ the selected carrier sets with total functions and 𝒞_H
pairs of functions with additive costs, S: 𝒜 → ℐ and R_H: 𝒜 → 𝒞_H are
functors and S is not faithful; that S is not an equivalence. Any further
categorical claim defines its objects, arrows, identities and composition and
proves preservation (conserves
[functor kinds](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds),
which states that obligation and asserts no categorical functor itself).
H names an architecture, never a runtime.

## 5. Hypotheses

Not law; carried for falsification: categorical equivalence of 𝒜 and ℐ under
some reformulation; universal algorithmic capture of meaning; the statistical
Markov boundary (candidate status under
[WORLD_MODEL_METHOD](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct));
traversal composition laws of any runtime.

## 6. Source dispositions

| rc.2 clause family | Disposition in this corpus |
|---|---|
| AC Position, Derivation Provenance, Scope | conserved; restated in AXIOMATIC_CALCULUS §1 |
| AC Core Signature, Typed Records and its five records | conserved; restated in AXIOMATIC_CALCULUS §2 and §3; Semantic Object and Residual are related to the §2 objects Object and Residual, the definitions stay here |
| AC-001, AC-003, AC-004, AC-012 | conserved; restated in AXIOMATIC_CALCULUS §4 |
| AC-002, AC-005, AC-006, AC-009, AC-014 | conserved; restated in AXIOMATIC_CALCULUS §4 as laws over the §2 objects Object, Authority, Basis, Residual and Judgment, which are defined once here; P3, P4b and P6 consume them |
| AC-007 | conserved; restated in AXIOMATIC_CALCULUS §4 as a law over constraints using the one result algebra of ACTIVATION §3 |
| AC-008, AC-011 | conserved; restated in AXIOMATIC_CALCULUS §4; their generic forms over any two values and any reference are the Latitude and Reference-versus-body paragraphs of §4 above |
| AC-010 | conserved; restated in AXIOMATIC_CALCULUS §4; applied by ACTIVATION §2 |
| AC-013 transformation | conserved; restated in full in AXIOMATIC_CALCULUS §4; its delta fields are the conservation accounting of §4 above |
| AC Fundamental Laws heading | not applicable: heading with no claim text (20 bytes); listed in AXIOMATIC_CALCULUS §11 |
| AC Traversals And Functor Kinds, AC-015, AC-016 | conserved; restated in AXIOMATIC_CALCULUS §5; P4a and the formal fragment of §4 above consume them |
| AC Interpretation And Models, AC-017, AC-018, AC-019 | conserved; restated in AXIOMATIC_CALCULUS §6; P1 consumes them; the generic structural-and-semantic separation is EVALUATION §2 |
| AC Subject And Carrier Boundaries, AC-020 | conserved; restated in AXIOMATIC_CALCULUS §7; applied to release lineage in SPEC_METHOD §6 |
| AC Exact Calculus Identity | conserved; the identity law is restated in AXIOMATIC_CALCULUS §8; the record instance is a release artefact issued under RELEASE and AC-020 at this corpus's own release |
| AC Application Boundary, External Imports And Specializations, Exclusions, Conformance Obligations | conserved; restated in AXIOMATIC_CALCULUS §9 and §10 |
| RF definitions (#definitions and its 17 children) | conserved; restated in §2 (amended rows, frame objects, authority kinds, disjointness and independence, the frame tuple); rows in the table below |
| RF-001 to RF-017, engagement atom, frame set, functions, conjunction, relations, coverage, completeness, revision, activation packet, violations, declarations, closure | conserved; restated in REFERENCE_FRAME, whose §15 lists the rows; the algebra RF-012 names is defined once in ACTIVATION §3 |
| RF engagement, frame qualification, method self-qualification | conserved; restated in ACTIVATION §1 to §4 and §7 and in EVALUATION §7, whose tables list the rows |
| UP-001, UP-004, UP-008, UP-022 | conserved; UP-004 restated in IDENTITY §6, whose §13 lists the IDENTITY_METHOD rows; all four consumed by EVALUATION |
| UP-013, UP-014, UP-005 | conserved; UP-013 restated in SPEC_METHOD §3 and UP-014 in ACTIVATION §6 with its delivery priority in SPEC_METHOD §8; P2 consumes them; UP-005 is disposed at the design profile |
| UP-015 | conserved; restated in full in RELEASE §9, applied to this corpus in §1 and to acceptance evidence in EVALUATION §5 |
| RM Release Identities | conserved; candidate source, release subject and version-line selector restated in §2 Release objects beside the release cut; their realisation as refs, with the namespace, subtree and branch carriers, in RELEASE §2, whose §11 lists the RELEASE_METHOD rows |
| IDENTITY_METHOD scoped identity | conserved; the Object of §2 carries scoped identity, whose laws are IDENTITY §2 |
| UP-016, UP-018, UP-019, UP-023 | conserved; UP-018 consumed by ACTIVATION §1, UP-019/023 by §4 above; UP-016 stays in the software-design profile |
| UP-017, UP-021 | conserved; reframed with AC-005, AC-009 and AC-013 into P4b's one obligation; UP-021 and its standing structural qualification are restated in full in ACTIVATION §4 |
| UP-020 | conserved; restated in ACTIVATION §1, §3, §5 and §7 |
| SM Probabilistic Work Boundary | conserved; restated in §2 Work boundary and §3 under P0; ACTIVATION §1 consumes it; row in the table below |
| SM Recursive Product Taxonomy | conserved; restated in §2 Product lineage objects; SPEC_METHOD §6 consumes it; row in the table below |
| SM Ambiguity Governance | conserved; restated in SPEC_METHOD §5; its outcome refinement is ACTIVATION §3 and its hard stops ACTIVATION §4 |
| ODD, DESIGN_MODULE, UX, WORLD_MODEL profile law | conserved by reference in PROFILES; nothing imported into tier 1 |

Rows of other members above still read "conserved by reference" from the
first pass; each is rewritten to the §1 vocabulary at its member's
activation.

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
