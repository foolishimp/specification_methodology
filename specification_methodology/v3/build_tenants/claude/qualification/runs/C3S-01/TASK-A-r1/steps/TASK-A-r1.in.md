STEP TASK-A-r1 | cap 110000 bytes | measured 85001 bytes | fits
BLOCKS: METHOD, TASK
# C3S Card

After this card you receive two blocks. The block labelled METHOD is one
reference frame. The block labelled TASK is the work to do.

The METHOD block is your only method source. Apply it to the TASK and use
no knowledge of any methodology from outside it. Where the TASK needs
something the METHOD block does not supply, say so in the place the TASK
names for that. Where the TASK does not state a fact you need, say it is
missing; do not invent it.

Do what the TASK block instructs and return only what it asks for, in the
order and shape it names. For each result you give, state the predicate it
is for and its core value, in the METHOD block's own terms. Keep explicit
what the stated facts leave uncertain and where your authority ends.

There is no one to ask; do not ask questions.

===== METHOD =====
# Reference frame rf-task-a

Task: Declare one reference frame for one evaluation, activate it on an exact subject and basis, return a minimal evaluation result, and say what that result does and does not settle about an owner's claim and who disposes the claim.

Purpose: The owning sections for the frame declaration, its activation on an exact subject and basis, the minimal evaluation result with one core result value, and the disposition of a claim that consumes the result.

Each excerpt below is a verbatim copy of one owning section of a member
of this method. The `Source:` line before it names the member and the
section's anchor, and gives the SHA-256 of the whole owning member. The
owning section decides; this frame owns no determination. Links inside
an excerpt are relative to the owning member's directory.

Routes, in order:

1. [FOUNDATIONS.md#2-ontology](../FOUNDATIONS.md#2-ontology)
2. [REFERENCE_FRAME.md#rf-001-evaluation-relativity](../REFERENCE_FRAME.md#rf-001-evaluation-relativity)
3. [REFERENCE_FRAME.md#rf-002-finite-attention](../REFERENCE_FRAME.md#rf-002-finite-attention)
4. [REFERENCE_FRAME.md#rf-003-material-sufficiency](../REFERENCE_FRAME.md#rf-003-material-sufficiency)
5. [REFERENCE_FRAME.md#rf-004-irrelevance-exclusion](../REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)
6. [REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates](../REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)
7. [REFERENCE_FRAME.md#rf-006-authority-conservation](../REFERENCE_FRAME.md#rf-006-authority-conservation)
8. [REFERENCE_FRAME.md#rf-007-semantic-evidence-and-verdict-separation](../REFERENCE_FRAME.md#rf-007-semantic-evidence-and-verdict-separation)
9. [REFERENCE_FRAME.md#rf-011-topology-mutation-and-recharting](../REFERENCE_FRAME.md#rf-011-topology-mutation-and-recharting)
10. [REFERENCE_FRAME.md#rf-012-closed-results](../REFERENCE_FRAME.md#rf-012-closed-results)
11. [REFERENCE_FRAME.md#rf-013-reconstructable-activation](../REFERENCE_FRAME.md#rf-013-reconstructable-activation)
12. [REFERENCE_FRAME.md#rf-014-capability-fit](../REFERENCE_FRAME.md#rf-014-capability-fit)
13. [REFERENCE_FRAME.md#rf-015-residual-uncertainty](../REFERENCE_FRAME.md#rf-015-residual-uncertainty)
14. [REFERENCE_FRAME.md#5-method-functions](../REFERENCE_FRAME.md#5-method-functions)
15. [REFERENCE_FRAME.md#7-frame-relations](../REFERENCE_FRAME.md#7-frame-relations)
16. [REFERENCE_FRAME.md#11-the-activation-packet](../REFERENCE_FRAME.md#11-the-activation-packet)
17. [REFERENCE_FRAME.md#minimal-frame-declaration](../REFERENCE_FRAME.md#minimal-frame-declaration)
18. [REFERENCE_FRAME.md#minimal-evaluation-result](../REFERENCE_FRAME.md#minimal-evaluation-result)
19. [EVALUATION.md#frame-qualification](../EVALUATION.md#frame-qualification)
20. [ACTIVATION.md#admission-and-activation](../ACTIVATION.md#admission-and-activation)
21. [ACTIVATION.md#disposition](../ACTIVATION.md#disposition)
22. [ACTIVATION.md#7-closed-result-and-reuse](../ACTIVATION.md#7-closed-result-and-reuse)
23. [FOUNDATIONS.md#results](../FOUNDATIONS.md#results)
24. [FOUNDATIONS.md#conjunction-of-results](../FOUNDATIONS.md#conjunction-of-results)

Size of this frame: 80757 bytes.

Source: FOUNDATIONS.md#2-ontology sha256=259ef2fe5f1d6056d237c5ff0cdc0c051f89606f53e85c2137c9398cf6fafc71

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

### Accounts of a construction

A construction is the realisation of a selected outer contract through
steps, as P0 states it (§3). Three accounts of a construction stay
distinct (P1, P0):

- the algorithmic description: the steps;
- the informational interpretation: what the data means, given under an
  Interpretation (the ontology table above);
- the computational realisation: how people, machines or combinations of
  them carry it out in a declared execution environment; for a build
  tenant that environment is the one
  [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.

The distinction is kept for any construction and is independent of the
tiers of this corpus: a construction may need all three accounts, and no
account is a tier (P1). The distinction is an added choice in the sense
of §3 Foundation to law, not a commitment, and has none of the standings
of §1; its owner is the Intent of the Product that owns this corpus, in
its Direction. Purpose and material relation: the steps, the meaning of
the data and the means of execution can each change while the others
hold, so a claim about one account is never taken for a claim about
another (P1, P6).

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


Source: REFERENCE_FRAME.md#rf-001-evaluation-relativity sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-001 Evaluation relativity

Every frame declares the evaluation family it supports. A frame with no
declared evaluation family has no testable sufficiency boundary (P2; rc.2
#rf-001-evaluation-relativity).


Source: REFERENCE_FRAME.md#rf-002-finite-attention sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-002 Finite attention

An activated frame contains a finite attention surface that fits the
selected actor's declared capability envelope. A frame that needs
undeclared ambient memory, conversation history or an effectively global
workspace context is not reconstructable for that actor (P0; rc.2
#rf-002-finite-attention). The fit is tested in
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
which owns the measurement of the context's size and when it applies.
Whether the actor attends adequately to a frame that fits is a separate
question, answered by actual-use evidence under
[EVALUATION §7](EVALUATION.md#frame-qualification); a size measurement
does not answer it (P0, P6).


Source: REFERENCE_FRAME.md#rf-003-material-sufficiency sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-003 Material sufficiency

Every known relation whose lawful change can alter the evaluation result,
the validity of the basis, the sufficiency of evidence, operation authority
or decision authority appears in the frame or enters through a declared
authoritative input. Omitting a material relation makes the frame
insufficient. The law does not require proving that no undiscovered
material relation exists (P2; P0 with the open-world premise; rc.2
#rf-003-material-sufficiency).


Source: REFERENCE_FRAME.md#rf-004-irrelevance-exclusion sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-004 Irrelevance exclusion

Relations that cannot affect the declared evaluation stay outside active
attention unless they are needed to establish that irrelevance. A frame
does not expand because adjacent workspace material exists (P2; rc.2
#rf-004-irrelevance-exclusion).


Source: REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-005 Exact basis and coordinates

Every result binds its exact subject, basis, coordinates and evidence
scope. A stale, advanced, ambiguous or mismatched basis returns
`invalid_basis` or requires reactivation. Apparent equality never
substitutes for declared coordinate equality (P3, P1; rc.2
#rf-005-exact-basis-and-coordinates).


Source: REFERENCE_FRAME.md#rf-006-authority-conservation sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-006 Authority conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer or reconstruct semantic, evaluation, operation or decision
authority from actor identity, available capability, evidence shape,
implementation reachability or frame selection (P6; rc.2
#rf-006-authority-conservation).


Source: REFERENCE_FRAME.md#rf-007-semantic-evidence-and-verdict-separation sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-007 Semantic, evidence and verdict separation

Semantic law defines what the evaluation means. Evidence supplies
observations. The evaluator applies the declared relation. Where the
evaluation performs a material operation, the existing operation owner
supplies the exact grant. Decision authority disposes the result. A frame
declaration keeps these roles distinguishable even when one actor lawfully
performs several of them (P6; rc.2
#rf-007-semantic-evidence-and-verdict-separation). EVALUATION §2 applies
this law to review.


Source: REFERENCE_FRAME.md#rf-011-topology-mutation-and-recharting sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-011 Topology mutation and recharting

An activated frame declares the topology changes capable of invalidating
its coordinates or its materiality judgment. A detected material topology
mutation causes reevaluation, frame revision or recharting before the
previous result is reused. Material revision of the frame itself
invalidates for reuse every result bound to the prior revision coordinate;
§10 Revision actions states that rule (P3, P4b; rc.2
#rf-011-topology-mutation-and-recharting).


Source: REFERENCE_FRAME.md#rf-012-closed-results sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-012 Closed results

Every performed evaluation of a frame returns one closed result in the
frame's declared result algebra: the core algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), or a refinement mapped
into it under that section. That section owns the five core values
(`satisfied`, `falsified`, `indeterminate`, `out_of_frame` and
`invalid_basis`), their meanings and the rules over them: that nothing is
coerced to success; that a refinement adds no core value, keeps
indeterminate, out-of-frame and invalid-basis pressure explicit and raises
no result's standing; and that an evaluation not performed has no result,
its stop state being
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition). This law
applies them to every frame and defines none of them (P5; rc.2
#rf-012-closed-results).


Source: REFERENCE_FRAME.md#rf-013-reconstructable-activation sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-013 Reconstructable activation

A fresh competent actor inside the declared capability envelope can
reconstruct the activated evaluation from the frame declaration, the exact
subject, the basis and the admissible inputs, without undocumented
conversational or historical context (P0 with the actor-change premise;
rc.2 #rf-013-reconstructable-activation).


Source: REFERENCE_FRAME.md#rf-014-capability-fit sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-014 Capability fit

Frame adequacy includes actor usability. When the material manifold
exceeds an actor's capability envelope, human authority may select
another actor, refine the frame, sequence activations or provide a lawful
compression (RF-017); the selection is human authority's, exercised
directly or in advance through the grant, and ACTIVATION §2 says which of
these a step selects itself and which re-enter the grant's owner. The
actor may not silently omit material relations to fit its context (P0, P5;
rc.2 #rf-014-capability-fit).


Source: REFERENCE_FRAME.md#rf-015-residual-uncertainty sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-015 Residual uncertainty

Coverage and evaluation results retain known uncertainty. Unresolved
relations, uncovered evaluations, contested evidence and unknown capability
stay explicit. Absence of a recorded counterexample is not evidence of
universal completeness (P4b, P6; open-world premise; rc.2
#rf-015-residual-uncertainty).


Source: REFERENCE_FRAME.md#5-method-functions sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

## 5. Method functions

The frame and the functions over it remain distinct. An application may
realise the following relations in any conforming form; the signatures
describe relations, not callable software interfaces (P2; RF-016; rc.2
#method-functions):

```text
declare(human_authority, workspace, outcome, practices, capabilities)
  -> frame_set

activate(frame, evaluation, subject, basis, actor)
  -> activated_frame | activation_refusal

evaluate(activated_frame, admissible_evidence)
  -> result + evidence + residuals

conjoin(decision_rule, frame_results)
  -> decision | conflict | indeterminate

translate(source_frame, target_frame, value_or_evidence, mapping)
  -> translated_value | declared_loss | refusal

audit_coverage(workspace, outcome, evaluation_inventory, frame_set)
  -> coverage_ledger

revise(frame_set, new_evidence, failures, capability_change, topology_change)
  -> proposed_frame_set_delta
```

`declare` is §4; `activate` and `evaluate` are ACTIVATION §1 and §2;
`evaluate` returns its result under RF-012, and the closed result is
returned and reused under ACTIVATION §7; `conjoin` and `translate` are §6;
`audit_coverage` is §8, which maps the statuses of its ledger to the core;
`revise` is §10. EVALUATION §7 qualifies each.

The outcomes of `activate`, `conjoin` and `translate` form a refinement of
the core algebra, stated under the refinement rule of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results): each outcome below maps
to exactly one core value for the predicate its function names, the value
travels with that predicate and with the outcome, whose meaning stays here,
and an outcome named in the signatures above that would map to more than
one core value according to its cause carries the cause in its name, as in
`activation_refusal(basis)` (P5, P6). The refinement is new in this
corpus. Purpose and material relation: a consumer that combines these
outcomes with other results reads them in the one core, so a refusal, a
conflict or a loss outside the accepted loss is neither mistaken for
success nor merged with an evaluation that was not performed.

| Function and predicate | Outcome | Cause | Core value |
|---|---|---|---|
| `activate`: the frame is activated for this evaluation, subject, basis and actor | `activated_frame` | the frame declaration is bound to the exact evaluation, subject, basis and actor | `satisfied` |
| | `activation_refusal(capability)` | the frame declares a capability the evaluation needs, and the selected actor's declared envelope lacks it; the refusal names that capability and its owner where the subject gives one | `out_of_frame` |
| | `activation_refusal(authority)` | the activation needs semantic, evaluation, operation or decision authority that is not admitted to it; the refusal names that authority's owner | `out_of_frame` |
| | `activation_refusal(basis)` | the subject or basis is stale, advanced, ambiguous or mismatched (RF-005), a topology mismatch included: the subject's topology is not the topology basis the frame declares (RF-011) | `invalid_basis` |
| `conjoin`: the composite predicate holds under the declared decision rule | `decision(holds)` | the conjunction of FOUNDATIONS §4 reports `satisfied` | `satisfied` |
| | `decision(fails)` | the conjunction reports `falsified`, and no mandatory result for the same claim is `satisfied` | `falsified` |
| | `conflict` | the conjunction reports `falsified` while mandatory results for the same claim disagree, one `satisfied` and another `falsified`; the counterexample survives the join, and the disagreement stays unresolved for the decision authority | `falsified` |
| | `indeterminate` | the conjunction reports `indeterminate` | `indeterminate` |
| `translate`: the value or evidence enters the target frame as the declared translation states | `translated_value` | the value or evidence is carried into the target coordinates with its declared meaning | `satisfied` |
| | `declared_loss` | the value or evidence is carried with a loss inside the declared accepted loss; the loss travels with it as a residual (P4b) | `satisfied` |
| | `refusal(condition)` | a refusal condition the translation declares holds, a loss outside the accepted loss included; or the value or evidence fails identity or equality under the translation's declared equality law | `falsified` |
| | `refusal(authority)` | an authority mismatch the translation does not declare: the value or evidence carries semantic, evaluation, operation or decision authority whose relation to the target frame's authority the translation states neither as preserved nor as a refusal condition; the refusal names that authority's owner | `out_of_frame` |
| | `refusal(basis)` | the source value or evidence binds a stale, advanced, ambiguous or mismatched basis or coordinate (RF-005) | `invalid_basis` |

Where no frame the actor can use declares a material relation or
capability the evaluation needs, `activate` returns `out_of_frame` itself
([ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope),
Activation). Where the conjunction reports `out_of_frame` or
`invalid_basis`, `conjoin` returns that value; the signatures name no
outcome for either case, and the `refusal` that EVALUATION §7 names for
`conjoin` on a basis mismatch is this returned `invalid_basis`. Under a
declared veto or deferral, `conjoin` returns the outcome above whose cause
holds for the value the conjunction reports
([FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results)), or that value
itself where it is `out_of_frame` or `invalid_basis`. A planned
assessment without a closed result, and required coverage that no planned
assessment addresses, are no outcome of `conjoin`:
[FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results) records them
beside the reported value, and they map to no core value. The outcomes of
`activate` answer whether a frame was activated, never the
evaluation's claim: a refused activation performs no evaluation.
`decision(holds)` assesses the composite predicate and is not its
acceptance, which is a separate result
([FOUNDATIONS §4](FOUNDATIONS.md#results)).


Source: REFERENCE_FRAME.md#7-frame-relations sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

## 7. Frame relations

Frames may relate as (rc.2 #frame-relations):

- disjoint: no material variable, coordinate, evidence or result dependency
  is shared for the declared evaluations;
- overlapping: some material variables, evidence or entities are shared;
- complementary: distinct evaluations jointly inform one decision;
- alternative: different frames can evaluate the same claim under declared
  capability or evidence conditions;
- refinement: one frame resolves a material distinction left aggregated in
  another;
- restriction: one frame evaluates a lawful subset of another frame's
  domain;
- translated: values or evidence move through a declared coordinate map;
- temporally successive: a later frame evaluates a changed basis;
- composed: several frame relations form one governed evaluation or
  action; or
- governing and subordinate: one frame inherits declared constraints from
  another where a real authority or decomposition relation exists.

No relation is the default universal frame topology. A project declares
only the relations its evaluations and coverage claims need (P3, P2;
RF-009).


Source: REFERENCE_FRAME.md#11-the-activation-packet sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

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


Source: REFERENCE_FRAME.md#minimal-frame-declaration sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### Minimal frame declaration

(rc.2 #minimal-frame-declaration)

```markdown
# Frame: <stable local identity>

## Evaluation Family
<questions, predicates, and closed result algebra>

## Subject And Basis
<workspace boundary, exact identity, version/time/topology coordinates>

## Material Manifold
<entities, variables, relations, states, and interactions>

## Coordinates And Equality
<how positions are distinguished and related>

## Invariants
<applicable governing laws>

## Authorities
<frame-set, semantic, evaluation, operation where material, and decision authority>

## Evidence
<admissible sources, provenance, and exclusions>

## Capability Envelope
<competence, context, access, tools, evaluation/assurance independence, configuration>

## Boundary And Exclusions
<irrelevant material, prohibited assumptions, and out-of-frame conditions>

## Optional Frame Relations
<inputs, outputs, overlaps, conjunctions, or translations actually used>

## Invalidation And Recharting
<changes that stale this frame or its results>

## Qualification
<representative cases, counterexamples, and known residuals>
```


Source: REFERENCE_FRAME.md#minimal-evaluation-result sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### Minimal evaluation result

(rc.2 #minimal-evaluation-result)

```markdown
# Frame Evaluation Result

- frame identity and revision:
- activation identity:
- evaluation:
- subject and basis:
- actor and capability envelope:
- semantic, evaluation, operation where material, and decision authority:
- admissible evidence:
- result:
- inference relation:
- residual uncertainty:
- out_of_frame residual (missing relation or capability, owner, reconfiguration pressure):
- invalidation conditions:
- consuming decision or conjunction:
```

The out_of_frame residual field is new in this corpus; it carries what
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) requires an out_of_frame
result to name, and reads `none` for any other result (P5).


Source: EVALUATION.md#frame-qualification sha256=6383bebb0238da55ec4ea779f44d077f558f0f32ccfcfbfca38845efed9946b6

### Frame qualification

A candidate frame ([REFERENCE_FRAME](REFERENCE_FRAME.md)) is qualified in
proportion to its claims (P6, P2; provenance
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#frame-qualification`).
The minimum evaluation asks:

1. Decision test: can a competent actor produce a result in the declared
   algebra for representative in-domain evaluations?
2. Reconstruction test: can a fresh competent actor activate the frame
   from the declared packet without hidden history (RF-013)?
3. Sensitivity test: do changes to declared material relations affect the
   result where expected?
4. Irrelevance test: do excluded unrelated changes leave the result stable
   where expected?
5. Basis test: does stale, mismatched or ambiguous basis information
   invalidate or refuse the evaluation?
6. Authority test: does frame selection preserve semantic and decision
   authority and the exact inherited operation authority for every
   material construction, transformation, admission, publication or
   mutation?
7. Counterexample test: does the frame detect the representative
   historical or constructed violations it claims to cover?
8. Capability test: can the declared actor class hold and operate the
   frame within its envelope?
9. Result-consumption test: can a declared consumer use the closed result
   without importing hidden frame context?

Qualification binds the exact frame revision, actor envelope, evaluation
family, basis class and evidence conditions evaluated. It does not
generalise to an unevaluated population by naming the frame generically
(§1, the quantifier rule).

Adequate attention. The capability test asks two questions, and they are
evaluated separately. Whether the declared actor class can hold the frame
is fit: for the context dimension, the size of the selected
representation, measured as ACTIVATION §2 step 3 measures it, against the
declared capacity; the envelope's other dimensions are fitted as RF-014
states. Whether the actor class
operates the frame adequately is adequate attention, and only actual-use
evidence establishes it: actors of the declared class apply the frame to
its declared tasks under its declared conditions, and the results are
judged against expectations recorded from the governing sources before the
results are opened, by an assessor under §3 where the claim needs
independent assessment. A size measurement, or any byte or token
threshold, establishes fit and nothing about attention; a frame that fits
is not thereby adequately attended. Actual-use evidence binds the frame
revision, actor class, tasks and conditions evaluated, like the
qualification above, and establishes no universal attention score (§1,
the quantifier rule). Time, spend and other resource limits are those of
the selected execution binding
([SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding)), not of this
test. The separation is new law: finite attention makes fit necessary
(RF-002), and only use shows that a frame that fits is applied, so a frame
is never qualified for attention because it fits (P0, P6).


Source: ACTIVATION.md#admission-and-activation sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Admission and activation

A step exists only after its contract is admitted (§1, Admission) and its
frame is activated on the exact subject and basis (§2). The outcomes of
admission and of context construction are owned here; each maps for the
predicate "the step is lawfully admitted and activated on the exact
subject and basis", and its cause selects its value (P5, P6; RF-005 for
the basis causes). The outcomes of frame activation are the `activate`
refinement of [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions),
which owns their causes, their predicate and their core values. Because
this predicate requires activation, a refused activation decides it with
the value REFERENCE_FRAME §5 gives; the table names those outcomes and
maps none of them again:

| Outcome | Cause | Core value |
|---|---|---|
| `activated` | the contract is admitted with its admission evidence (§1), Z, R, the required-edge semantics, the basis and the scope are exact and the material closure is finite and unique (§2, step 1), its projection returns a selected context (§2, step 2), and activation returns `activated_frame` | satisfied |
| `admission_refused(authority)` | the work authority the step needs is not admitted: no admission mechanism or explicit human override admits the exact contract, or no durable result and evidence surface is authorised and available; the outcome names the missing authority or surface and its owner | out_of_frame |
| `admission_refused(basis)` | the contract's cited outcome, prerequisite or experiment basis, or the exact subject and basis it names, cannot support it; the outcome names that basis | invalid_basis |
| `closure_unresolved` | the seed set Z, the relation family R, the required-edge semantics, the basis or the scope is not exact, or the material closure is not finite and unique on the exact basis (§2, step 1; AC-010), or the projection of the closure returns a gap or refusal (§2, step 2; AC-011); the outcome names the condition that fails and the basis coordinates that leave it open | invalid_basis |
| `out_of_frame` | no available frame and actor pairing declares a material relation or capability the evaluation needs (§2, Activation), or no fit option of §2 step 3 fits the selected context to an actor's envelope | out_of_frame |
| `activation_refusal` with its cause | a cause REFERENCE_FRAME §5 states | the core value REFERENCE_FRAME §5 maps that cause to |

These outcomes are not values of construction availability and are not
results of a step. A refused admission or activation creates no step, no
activation of the step's frame and no work result, the closed output of a
constructing actor to its consumer; the outcome returns to the assigning
authority or the declared result carrier, and no consumer records it as a
step's stop state. [EXECUTIVE_BASELINE §5](EXECUTIVE_BASELINE.md#work-result)
applies this rule to the Worker (provenance
[work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result)).
Purpose and material relation: a mismatch known before the step begins is
reported with its cause in the one core, so it is neither mistaken for a
step that stopped nor for one that ran.


Source: ACTIVATION.md#disposition sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Disposition

The decision owner disposes an assessed candidate with one of four
semantic dispositions (§1, Roles and delegation; P6, P5; provenance rc.2
SPEC_METHOD #proportional-disposition). An assessor may recommend one; the
recommendation is evidence for the decision owner, never a disposition
([EVALUATION §4](EVALUATION.md#4-review-results)). The disposition is the
acceptance result: it consumes the candidate's availability and assessment
results and stays separate from both (FOUNDATIONS §4 Results). Each maps
to the core for the predicate "the candidate is accepted at its declared
boundary":

| Disposition | Condition | Core value |
|---|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation | satisfied |
| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent | falsified |
| `re_enter` | the governing outcome, a requirement, an identity, a lifecycle, an authority, a public contract or the accepted design must change | invalid_basis |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path | falsified |

For `local_repair` the local defect, and for `reject` the violated relation
or the competing truth path, is the counterexample to accepting this
candidate; a repaired candidate is a new candidate with its own results.
For `re_enter` the governing basis the candidate was built and assessed on
must change, so that basis cannot support acceptance; the change re-enters
at its owning relation (§4). The core values are new; they place
acceptance in the one core, as FOUNDATIONS §4 Results requires, so that a
consumer combining results cannot take availability or assessment as
acceptance (P6).

Global correctness means conserving every global relation affected by the
bounded action; it does not require proving the whole product inside every
local action (P4b). Repeated rejection against one unchanged boundary
requires reassessment of the frame altitude, the causal cone, the common
components, the design-versus-code placement and the authority
sufficiency. The method sets no rejection-count threshold, mandatory
review-round count or review state machine; it prohibits repeating an
unchanged failed construction relation as if iteration alone could close
it (P2).


Source: ACTIVATION.md#7-closed-result-and-reuse sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

## 7. Closed result and reuse

A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context is not
transferred when the closed result and its provenance are sufficient for
the consuming decision (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. Changed material inputs or a declared revising observation
invalidate the affected result before reliance, even where the subject's
own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results; a changed basis invalidates
likewise (judgment continuity names basis; Return A Closed Result names
inputs and observation). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity).

### Transition evidence

A reviewable transition identifies the exact candidate, the affected
relations, the changed realisation paths, the authority paths added or
removed, the retained and open seams, the focused proof, any required
integration proof, the explicit non-changes, and the decision owner's
disposition or the assessor's recommended disposition (§3). Consumers
choose the representation. Transition evidence is a read
model; it does not become specification, design or admission authority
(P6, P4b; provenance rc.2 SPEC_METHOD
#transition-evidence-and-proof-cadence).

Construction uses the cheapest focused proof capable of falsifying the
active relation. Expensive whole-candidate qualification occurs at a
declared candidate boundary rather than after every local edit, unless the
affected risk makes whole-candidate proof necessary (§6). A durable or
reconstructable authority claim is not established solely by a same-process
proof when loss of incidental process state is a material counterexample:
the proof destroys or excludes the incidental authority and compares the
reconstructed semantic outcomes (P5, P6).


Source: FOUNDATIONS.md#results sha256=259ef2fe5f1d6056d237c5ff0cdc0c051f89606f53e85c2137c9398cf6fafc71

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
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile, project or adopting Product that defines it |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](EVALUATION.md#5-acceptance) names |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](ACTIVATION.md#construction-availability), construction availability |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains; with every mandatory result `satisfied`, agreeing bases and no gap, a material counterexample to a mandatory constraint falsifies it whichever contributor found it, and without one its value is the one its declared rule gives over the mandatory results; a `falsified` result that is not mandatory stays in its record | [Conjunction of results](#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, how results that are not mandatory count, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule |
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


Source: FOUNDATIONS.md#conjunction-of-results sha256=259ef2fe5f1d6056d237c5ff0cdc0c051f89606f53e85c2137c9398cf6fafc71

### Conjunction of results

Conjunction combines results into one result for a composite predicate: a
claim made of component claims, a decision over several evaluations, or
the outer contract of composed steps. It is defined here once, over the
core. A member or profile that combines results applies this rule and
declares only the choices it leaves open (P4a, P4b, P5, P6). Purpose and
material relation: failure, undecidability, non-performance and uncertain
effects stay distinct after combination, so a composite can neither report
success nor hide which kind of gap it has while one of them remains in
what it requires.

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
with a material counterexample to a mandatory constraint or an uncovered
required obligation cannot project success. Where a mandatory result is
not `satisfied`, the conjunction
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
recorded by kind. A `falsified` result that is not mandatory stays in the
conjunction's record with its predicate and is never discarded. Where
every mandatory result is `satisfied`, the declared basis relations agree
and no gap remains, a material counterexample to a mandatory constraint
falsifies the conjunction whichever contributor found it, and without one
the conjunction's value is the one its declared rule gives over the
mandatory results.

The declared rule. A conjunction declares which results are mandatory; how
conflict and indeterminacy are handled; which basis relations must agree,
results on different bases combining only under a declared coherent
composite basis (§2, Basis); which decision authority owns the
conjunction; how results that are not mandatory count; and whether any
result may veto or defer the decision.
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


===== TASK =====
# TASK A: declare a frame and return an evaluation result

## Subject

Workspace `W-ledger-export`: a small service that exports one database
table to a CSV file. The facts below are the whole subject; the record is
invented for this task and is evidence about no real product.

Basis coordinates:

- source commit `c0ffee12` (service `ledger-export`, file `exporter.py`,
  SHA-256 `5f1a…9c2e`)
- builds: `b-118` (commit `b7a1d3e0`), `b-120` (commit `c0ffee12`)
- configuration: `export.yaml` revision 14
- database: production table `ledger_rows`; on 2026-10-09 reads were moved
  from the primary to a read replica whose documented lag is up to 30 s
- time of the claim: 2026-10-11T16:00Z

Requirement R-3: every export file carries, in its trailer line, the row
count of the source table at export time.

Design note D-3: the exporter opens a read transaction, streams the rows to
the file, then issues `SELECT COUNT(*)` and writes the count as the trailer.

Evidence on file:

| Id | Observation | Provenance |
|---|---|---|
| V1 | three tests green: `test_trailer_present`, `test_trailer_is_integer`, `test_count_matches_fixture_table` (fixture table of 25 rows) | CI run 4471 on build `b-118`, 2026-10-08 |
| V2 | an export of the production table on 2026-10-10 produced a file whose trailer reads 1,204,311; the operator did not record the primary's row count at that time | operations log entry OPS-391 |
| V3 | the read-replica move, lag up to 30 s | infrastructure change CHG-2026-1009 |

Authorities: the product owner (Mara) owns the meaning of R-3 and the
release decision; the service team lead (Deon) owns changes to
`exporter.py` and `export.yaml`; the operations lead (Priya) owns the
database configuration.

Evaluation inventory (three evaluations):

- E1: on build `b-120`, does the trailer count equal the source table's row
  count at export time?
- E2: is the test evidence V1 evidence about build `b-120`?
- E3: does the move to the read replica change which table state the count
  in D-3 is taken from?

Owner's claim K (Mara, 2026-10-11): "R-3 is satisfied on `b-120`; the
export is ready to ship."

## Instruction

1. Declare one reference frame for evaluation E1, using the minimal frame
   declaration shape the METHOD block gives, with every one of its sections
   filled from the subject above. Where a section needs something the
   subject does not state, write what is missing rather than inventing it.
2. Activate that frame on the exact subject and basis for E1 and return a
   minimal evaluation result in the shape the METHOD block gives, with the
   `result` field holding exactly one member of the result algebra and the
   `inference relation` field saying how the admissible evidence led to it.
3. Under a heading `Claim K`, state in at most three sentences what your
   result does and does not say about claim K, and who disposes it.
4. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those four parts, in that order. Do not restate the subject.
Do not add recommendations about the product.
