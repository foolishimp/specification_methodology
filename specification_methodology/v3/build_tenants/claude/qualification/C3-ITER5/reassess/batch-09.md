# I5-03 reading batch 09

Rows: 23. Members: ['REFERENCE_FRAME_METHOD.md', 'RELEASE_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `REFERENCE_FRAME_METHOD.md#select-and-activate` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#select-and-activate` at rc.2:

```text
### Select And Activate

The actor or assigning authority selects one frame or one declared active frame
configuration capable of the evaluation. Activation binds each reusable frame
declaration to the exact subject and basis. It loads the declared material
relations and evidence sources rather than an undifferentiated workspace dump.

When no available frame and actor pairing can lawfully perform the evaluation,
activation returns a refusal or `out_of_frame` pressure. Work does not proceed
through implied context.
```

Successor, `ACTIVATION.md#2-context-construction-under-an-envelope`:

```text
## 2. Context construction under an envelope

Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R (AC-010,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-010-material-closure).
   If Z, R, the required-edge semantics, the basis or the scope is not
   exact, or the closure is not finite and unique on the exact basis,
   activation returns `closure_unresolved` (§3, Admission and activation)
   and no step proceeds; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams (AC-011,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-011-projection);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-011-projection).
   If the projection returns a gap or refusal, activation returns
   `closure_unresolved` and no step proceeds.
   Material not in the closure stays out; adjacent material does not enter
   because it exists
   ([RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)).
3. Test fit against B. This step owns the size measurement and the fit
   test for the context dimension. Where B declares a context capacity,
   the size of the selected context is measured before the actor reads it,
   in the unit the capacity is declared in (bytes or tokens) and over the
   boundary that the selected execution binding states for it (§6), and is
   compared with that capacity. The measurement, the capacity and the
   outcome of the comparison are recorded before the read. A fit holds
   only for the measured boundary: context outside it is recorded as not
   measured, and no fit claim covers it. The fit claim for a measured
   boundary and the step's fit judgment are distinct: the judgment is
   established from the recorded complete active inputs, or from a
   supported upper bound that includes any host-supplied context; where
   neither exists it is `indeterminate`, unless a counterexample, such as
   a measured excess, establishes `falsified`. A correct task result keeps
   its own bounded standing and does not satisfy a missing fit judgment
   (P0, P5; new law carried at iteration 4 from the common construction
   contract's Limits). The measurement applies wherever B declares a
   context capacity, whatever question the step governs, because without
   it a fit claim against that capacity is an assertion, and a context
   that exceeds it would be cut without record
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)). It applies only
   there, because a resource control applies only through a selected frame
   and its owning scope
   ([REFERENCE_FRAME §4](REFERENCE_FRAME.md#frame-set-selection)), and a
   declared capacity is such a control: the measurement tests that
   capacity, is no budget, and is not a universal measurement gate (P0,
   P2). Where B declares no context capacity, no measurement is
   required, and the other conditions of
   [RF-002](REFERENCE_FRAME.md#rf-002-finite-attention) still apply. The size
   shows fit and nothing else: whether the actor attends adequately to a
   context that fits is decided by actual-use evidence under
   [EVALUATION §7](EVALUATION.md#frame-qualification). The envelope's
   other dimensions are fitted as RF-014 states; time, spend and other
   resource limits follow [§6 Resource limits](#resource-limits), which
   this step refines for the context dimension.
   If the context fits, activate. If it does not, one or more of these, in
   combination: refine the outer contract into steps whose contexts fit
   (§4); sequence activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](REFERENCE_FRAME.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return `out_of_frame`
   ([§3 Admission and activation](#admission-and-activation)). Silent
   omission to fit is never one of them
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)).
   None of these options silently reduces the required predicate: the
   obligations the step preserves stay bound
   ([§1 Transitions](#transitions)), a narrowing of them is a destination
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
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). A derived surface is material derived from owning
sources by copying, projection or compression, such as a projected frame
for a task; it names its sources and owns no determination. Where a
current interpretation of the subject in `a_c` exists, the constraint
surface it yields for the task is such a derived surface, under the
conditions of
[AXIOMATIC_CALCULUS §9 Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces).
Where a derived surface whose sources
are current serves the task, the actor acquires it. For another task, or
where the derived surface is stale ([Staleness of derived surfaces](#staleness-of-derived-surfaces)),
missing or insufficient for a named unresolved question, the actor acquires the deciding owner sections
directly: the owning sections that decide the task's questions, which are
declared inputs of the selected basis. Only material in the exact selected
basis is acquired: where that basis has no derived surface for the task,
its exact owner sections are used, and a candidate source, a version-line
selector or another basis is no substitute for it
([FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)).
The actor reads the selected material and the actual subject, and follows
the material source and coupled-obligation references the task needs
(step 2; [RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency));
presence of the corpus is no reason to read it (step 2;
[RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)). No frame,
derived surface or acquisition carries a universal sufficiency claim:
sufficiency is decided for the named question against the task's
material relations, never for the corpus or the frame as a whole
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)). Before any dependent action, a missing binding is returned with
its outcome of [§3 Admission and activation](#admission-and-activation),
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
([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)); both are
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
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) naming the owning
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
[DESIGN_MODULE §11](DESIGN_MODULE.md#11-review),
[ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) A5 and
[§11.7A](ODD.md#117a-conforming-agentic-development),
[UX §7](UX.md#7-carrier-binding) and
[TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and
[§7](TICKETS.md#7-authority-judgment-closure-and-state) (P6).

The operation that joins AC-010, AC-011 and RF-002, RF-003, RF-004,
RF-014 and RF-017 into one procedure is new in this corpus (P0); each of
those laws is applied here from its successor section in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure) and
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#3-laws), and a `stdo://` route in
this section is provenance only. The method does not require proving
that no undiscovered material relation exists
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)).
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
owner; [PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary)
does so for the method's released carriers. Provenance: rc.2
authority_compressions/README.md and stdo_bootstrap.md step 5, a claim no
rc.2 body states. Purpose and material relation: an actor that relies on a
derived surface after one of its sources has changed decides from material
that no longer matches its owners, and a matching digest read as fidelity
would let a faithful-looking but wrong surface decide; the material
relation is whether a decision rests on a surface whose sources are not
those of the selected basis. This rule is new in tier 1; it was stated
only for packaging carriers before.
```


### Row `REFERENCE_FRAME_METHOD.md#topology` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#topology` at rc.2:

```text
### Topology

**Topology** is the relation structure among the material entities,
capabilities, authorities, lifecycle state spaces, adjacencies, and seams
visible to a frame at one basis. The frame need not contain the workspace's
complete topology.

A state-value change preserves the frame topology only when it preserves every
material entity, relation, lifecycle, authority, capability, adjacency, and
seam. A state transition that changes any such relation is a topology mutation
and may invalidate the frame's coordinates.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
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
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `REFERENCE_FRAME_METHOD.md#using-frames-in-conjunction` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#using-frames-in-conjunction` at rc.2:

```text
## Using Frames In Conjunction

Frames participate together through four distinct relations.

### Independently Activated Co-Evaluation

Several frames may evaluate the same subject through separate activations and
return closed results. They may overlap in subject, manifold, or evidence
sources, but neither evaluation consumes or influences the other's unclosed
working result. This is useful for assurance independence, different evidence
altitudes, or distinct failure perspectives.

### Result Conjunction

A declared decision rule consumes closed frame results. The rule states:

- which results are mandatory;
- how conflict and indeterminacy are handled;
- which basis relations must agree;
- what decision authority owns the conjunction; and
- whether any result may veto or defer the decision.

Conjunction does not transfer the semantic authority of a contributing frame.

Every mandatory constraint must be satisfied with valid applicable evidence.
Common agreement cannot discard a constraint or material counterexample found
by only one contributor. Missing, wrong-subject, conflicted or indeterminate
mandatory results remain unresolved under the declared rule; aggregate green
status cannot replace them.

### Evidence Or Coordinate Translation

One frame supplies evidence or a value consumed inside another frame. The
translation declares source and target coordinates, preserved meaning,
accepted loss, provenance, equality law, and refusal conditions.

### Material Composition

Several frame-governed operations form one material execution or reasoning
relation. The owning application declares the composition, shared invariants,
effect or decision order where material, closure, failure, and semantic,
operation, and decision-authority conservation.

Composition is introduced only when the evaluation requires it. A possible
future interaction does not require a general composition law in every frame.

---
```

Successor, `REFERENCE_FRAME.md#6-frames-in-conjunction`:

```text
## 6. Frames in conjunction

Frames act together through four distinct relations, and only where the
evaluation requires one (P4a; RF-010; rc.2 #using-frames-in-conjunction).

### Independently activated co-evaluation

Several frames may evaluate the same subject through separate activations
and return closed results. They may overlap in subject, manifold or
evidence sources; neither evaluation consumes or influences the other's
unclosed working result. This serves assurance independence, different
evidence altitudes and distinct failure perspectives (P6; FOUNDATIONS §2,
evaluation independence; rc.2 #independently-activated-co-evaluation).

### Result conjunction

A declared decision rule consumes the closed results of several frames.
The rule, what it must state, and the conjunction it computes are
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
over the core values of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results);
this member defines no conjunction of its own. The outcomes of `conjoin`
map to the core as §5 states (P4a, P5, P6; rc.2 #result-conjunction).

### Evidence or coordinate translation

One frame supplies evidence or a value consumed inside another. The
translation declares source and target coordinates, preserved meaning,
accepted loss, provenance, equality law and refusal conditions (P1, P4b;
rc.2 #evidence-or-coordinate-translation). What a statement of preserved
meaning and accepted loss must show, and the law that licenses the
step, are
[ACTIVATION §4, Refinement](ACTIVATION.md#refinement), and where the
translation is represented in `a_c` it is recorded in the preservation,
introduced, removed and residual fields of
[AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation). This section adds
only the frame fields: the source and target coordinates, the
provenance, the equality law and the refusal conditions.

### Material composition

Several frame-governed operations form one material execution or reasoning
relation. The owning application declares the composition, the shared
invariants, the effect or decision order where material, closure, failure,
and the conservation of semantic, operation and decision authority.
Composition is introduced only when the evaluation requires it; a possible
future interaction does not require a general composition law in every
frame (P4a, P6, P2; rc.2 #material-composition).
```


### Row `REFERENCE_FRAME_METHOD.md#workspace` (disposition `conserved`)

Predecessor, `REFERENCE_FRAME_METHOD.md#workspace` at rc.2:

```text
### Workspace

A **workspace** is the bounded body of material being reasoned over or acted
upon. It may include constitutional sources, domain assets, designs,
implementations, tools, runtime state, evidence, historical records, external
dependencies, and human decisions.

The workspace is broader than a repository. A repository is one possible
carrier.
```

Successor, `FOUNDATIONS.md#frame-objects`:

```text
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
| Role, persona, abstraction, component | a role allocates responsibility or authority, and the authority comes only from an admitted grant: naming a role or a frame grants none (Authority kinds below, What creates no authority); a persona alters an actor's approach or salience; an abstraction hides or contracts detail; a component is a structural part of a subject; each may help construct or activate a frame and none is a reference frame by identity alone; one component may appear in several frames and one frame may cross several components | P3, P6 |
```


### Row `RELEASE_METHOD.md#acceptance-criteria` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#acceptance-criteria` at rc.2:

```text
## Acceptance Criteria

An RC may be accepted when:

- pre-RC qualification passed for the declared subject;
- independent exact-cut review passed where required;
- required operator review is complete;
- the intended release scope and successor relation are stable;
- release-scoped assets accurately describe the exact cut;
- all release-blocking gaps are closed or the claimed scope is explicitly
  narrowed; and
- the human Product authority accepted the exact immutable RC identity.

Acceptance attaches to that immutable RC identity. It neither advances nor
rolls back the version-line selector. Consumer adoption separately evaluates
the exact latest target presented by the channel and mutates only after its
digest-bound plan is accepted.
```

Successor, `RELEASE.md#acceptance-criteria`:

```text
### Acceptance criteria

An RC may be accepted when (P6, P3; rc.2 #acceptance-criteria):

- pre-RC qualification passed for the declared subject;
- independent exact-cut review passed where required;
- required operator review is complete;
- the intended release scope and successor relation are stable;
- release-scoped assets accurately describe the exact cut;
- all release-blocking gaps, including the findings that block promotion
  under [EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion),
  are closed or the claimed scope is explicitly narrowed; and
- the human Product authority accepted the exact immutable RC identity.

Each criterion is a mandatory gate in the sense of
[FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse):
it applies irrespective of any selection of checks after a change, and
retained evidence satisfies it only under the validity conditions stated
there (P6).

Acceptance attaches to that immutable RC identity. It neither advances
nor rolls back the version-line selector. Consumer adoption separately
evaluates the exact latest target presented by the channel and mutates
only after its digest-bound plan is accepted (P6, P3; EVALUATION §5 is
the generic acceptance law).
```


### Row `RELEASE_METHOD.md#exact-cut-qualification` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#exact-cut-qualification` at rc.2:

```text
## Exact-Cut Qualification

Qualification binds:

- the Project Release Namespace, qualified immutable RC ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree, and
  declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, owner verdicts, and unresolved gaps; and
- the complete successor relation to the declared predecessor.

Evidence matches the claim. Source success does not prove packaged or installed
behavior; packaging equivalence does not prove semantic behavior; artifact
presence does not prove usability unless presence is the exact claim.

An RC is accepted only when the required exact-cut review and operator checks
are complete and the human authority accepts that exact subject. If review
requires any qualifying-byte change, the verdict remains attached to the old
RC and a higher RC is published. The selector already advertises the highest
published RC; acceptance does not move it, rewrite it, or create another final
carrier.
```

Successor, `RELEASE.md#exact-cut-qualification`:

```text
### Exact-cut qualification

Qualification binds (P6, P3; rc.2 #exact-cut-qualification):

- the Project Release Namespace, qualified immutable RC ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree,
  and declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, owner verdicts and unresolved gaps; and
- the complete successor relation to the declared predecessor (§9).

Evidence matches the claim. Source success does not prove packaged or
installed behaviour; packaging equivalence does not prove semantic
behaviour; artifact presence does not prove usability unless presence is
the exact claim (P6, P1; EVALUATION §1 is the generic claim law).

An RC is accepted only when the required exact-cut review and operator
checks are complete and the human authority accepts that exact subject. If
review requires any qualifying-byte change, the verdict remains attached
to the old RC and a higher RC is published. The selector already
advertises the highest published RC; acceptance does not move it, rewrite
it or create another final carrier (P6, P3).
```


### Row `RELEASE_METHOD.md#external-qualification-dependencies` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#external-qualification-dependencies` at rc.2:

```text
## External Qualification Dependencies

Some claims depend on external backends, transports, or operator-facing
services outside the local carrier. Such a dependency may remain out of Product
for carrier and migration classification while still blocking the dependent
release claim.

A clean skip caused by an unhealthy external dependency may preserve correct
Product classification, but it cannot establish that the dependent capability
passed. The claim is either qualified against a healthy dependency or narrowed
before acceptance.
```

Successor, `RELEASE.md#external-qualification-dependencies`:

```text
### External qualification dependencies

Some claims depend on external backends, transports or operator-facing
services outside the local carrier. Such a dependency may remain out of
Product for carrier and migration classification while still blocking the
dependent release claim (P6, P5;
rc.2 #external-qualification-dependencies).

A clean skip caused by an unhealthy external dependency is an evaluation
not performed, which has no result
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). It may
preserve correct Product classification, but it cannot establish that the
dependent capability passed. The claim is either qualified against a
healthy dependency or narrowed before acceptance (P6, P5).
```


### Row `RELEASE_METHOD.md#historical-ref-and-public-uri-conservation` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#historical-ref-and-public-uri-conservation` at rc.2:

```text
## Historical Ref And Public-URI Conservation

Project qualification is prospective. Existing unqualified refs retain their
names, objects, peels, and public links. A historical tag object may remain
reachable through an additional archival ref, but it is not recreated,
re-annotated, moved, or replaced. An immutable historical tag remains the same
object regardless of which preserving ref reaches it.

Product-local cut names and public logical release URIs also remain unchanged.
In particular, a logical STDO release remains
`stdo://releases/v<version>-rc.<n>/`; the project-qualified Git ref is transport
identity and is not inserted into that URI. Resolution binds the public logical
cut to its exact historical or project-qualified Git ref and fails closed if
one project-local coordinate names different tag objects.

When one version line spans the transition, latest means the greatest positive
RC ordinal across that project's preserved historical cuts and its qualified
future cuts. The first qualified publication creates the qualified selector.
The historical unqualified selector is preserved at its existing object and
ceases to be the current selector for the shared source; it is not force-moved
to imitate the qualified namespace.
```

Successor, `RELEASE.md#historical-ref-and-public-uri-conservation`:

```text
### Historical ref and public-URI conservation

Project qualification is prospective. Existing unqualified refs retain
their names, objects, peels and public links. A historical tag object may
remain reachable through an additional archival ref, but it is not
recreated, re-annotated, moved or replaced. An immutable historical tag
remains the same object regardless of which preserving ref reaches it
(P3, P4b; rc.2 #historical-ref-and-public-uri-conservation).

Product-local cut names and public logical release URIs also remain
unchanged. In particular, a logical STDO release remains
`stdo://releases/v<version>-rc.<n>/`; the project-qualified Git ref is
transport identity and is not inserted into that URI. Resolution binds
the public logical cut to its exact historical or project-qualified Git
ref and fails closed if one project-local coordinate names different tag
objects (P3, P5).

When one version line spans the transition, latest means the greatest
positive RC ordinal across that project's preserved historical cuts and
its qualified future cuts. The first qualified publication creates the
qualified selector. The historical unqualified selector is preserved at
its existing object and ceases to be the current selector for the shared
source; it is not force-moved to imitate the qualified namespace (P3).
```


### Row `RELEASE_METHOD.md#immutable-rc-publication` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#immutable-rc-publication` at rc.2:

```text
## Immutable RC Publication

A published RC cut exists to provide one exact subject for review, replay, and
possible acceptance. To publish it, the project:

1. confirms the triaged scope and lawful constitutional re-entry;
2. declares the exact Product release subject and release-scoped claim set;
3. reconciles the release note and other release-facing assets to that subject;
4. runs the proportionate pre-RC qualification and operator checks;
5. commits the exact carrier;
6. resolves and records the exact Project Release Namespace, Project Subtree
   root, and Project Subtree tree;
7. creates one annotated immutable `<project>/v<version>-rc.<n>` tag and an
   annotated `<project>/v<version>` selector tag over that same commit in a
   shared release source;
8. atomically pushes the carrier, RC branch, immutable RC tag, selector, and
   optional release branch where the transport supports it;
9. verifies remotely that the immutable tag, selector, and release branch
   resolve to the highest published RC commit; and
10. records enough ref, subtree, identity, and inventory evidence to reacquire
    the cut without trusting a mutable checkout.

Each published RC tag is immutable. Further work increments `<n>` on the same
version line when the intended line remains applicable. It does not require a
minor-version increment merely because review found a bounded repair. A
published higher RC without matching selector advancement is an invalid,
fail-closed release state; it never authorizes resolution of the older cut as
the version-line latest.
```

Successor, `RELEASE.md#immutable-rc-publication`:

```text
### Immutable RC publication

A published RC cut exists to provide one exact subject for review, replay
and possible acceptance. To publish it, the project (P3, P5, P6;
rc.2 #immutable-rc-publication):

1. confirms the triaged scope and lawful constitutional re-entry;
2. declares the exact Product release subject and release-scoped claim
   set;
3. reconciles the release note and other release-facing assets to that
   subject;
4. runs the proportionate pre-RC qualification and operator checks;
5. commits the exact carrier;
6. resolves and records the exact Project Release Namespace, Project
   Subtree root and Project Subtree tree;
7. creates one annotated immutable `<project>/v<version>-rc.<n>` tag and
   an annotated `<project>/v<version>` selector tag over that same commit
   in a shared release source;
8. atomically pushes the carrier, RC branch, immutable RC tag, selector
   and optional release branch where the transport supports it;
9. verifies remotely that the immutable tag, selector and release branch
   resolve to the highest published RC commit; and
10. records enough ref, subtree, identity and inventory evidence to
    reacquire the cut without trusting a mutable checkout.

Each published RC tag is immutable. Further work increments `<n>` on the
same version line when the intended line remains applicable. It does not
require a minor-version increment merely because review found a bounded
repair. A published higher RC without matching selector advancement is an
invalid, fail-closed release state; it never authorises resolution of the
older cut as the version-line latest (P3, P5).
```


### Row `RELEASE_METHOD.md#monotonic-version-line-advancement` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#monotonic-version-line-advancement` at rc.2:

```text
## Monotonic Version-Line Advancement

Version-line advancement makes the newly published highest RC for one Project
Release Namespace discoverable:

1. identify the exact new immutable RC tag, ordinal, and peeled commit;
2. confirm that no higher RC ordinal already exists on that line;
3. confirm the project-qualified selector is absent or currently resolves to a
   lower RC ordinal on the same project line;
4. atomically create or force-update the annotated
   `<project>/v<version>` selector to the new highest RC commit;
5. create or update `release/<project>/<version>` to the same commit when that
   optional carrier is used;
6. push the carrier, RC branch, immutable RC tag, selector, and optional release
   branch atomically where the transport supports it; and
7. verify remotely that the selector peels to the highest RC commit and that
   the matching immutable annotated RC tag exists.

Advancement is refused when the target has no matching immutable annotated RC
tag, any higher ordinal already exists, the selector would move to a lower RC,
or the selector and release branch would not align to the same highest commit.

Forward movement is strictly monotonic by RC ordinal. A later defect is
repaired through a higher immutable RC, not by moving an old RC tag or rolling
the selector backward. The selector is therefore equivalent to
`v<version>-rc.latest`, while every concrete RC tag remains addressable.
```

Successor, `RELEASE.md#monotonic-version-line-advancement`:

```text
### Monotonic version-line advancement

Version-line advancement makes the newly published highest RC for one
Project Release Namespace discoverable (P3, P5;
rc.2 #monotonic-version-line-advancement):

1. identify the exact new immutable RC tag, ordinal and peeled commit;
2. confirm that no higher RC ordinal already exists on that line;
3. confirm the project-qualified selector is absent or currently resolves
   to a lower RC ordinal on the same project line;
4. atomically create or force-update the annotated `<project>/v<version>`
   selector to the new highest RC commit;
5. create or update `release/<project>/<version>` to the same commit when
   that optional carrier is used;
6. push the carrier, RC branch, immutable RC tag, selector and optional
   release branch atomically where the transport supports it; and
7. verify remotely that the selector peels to the highest RC commit and
   that the matching immutable annotated RC tag exists.

Advancement is refused when the target has no matching immutable annotated
RC tag, any higher ordinal already exists, the selector would move to a
lower RC, or the selector and release branch would not align to the same
highest commit (P5).

Forward movement is strictly monotonic by RC ordinal. A later defect is
repaired through a higher immutable RC, not by moving an old RC tag or
rolling the selector backward. The selector is therefore equivalent to
`v<version>-rc.latest`, while every concrete RC tag remains addressable
(P3).
```


### Row `RELEASE_METHOD.md#mutable-candidate-construction` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#mutable-candidate-construction` at rc.2:

```text
## Mutable Candidate Construction

During candidate construction:

- bounded fixes are allowed after intake triage;
- qualification and operator review may continue;
- release notes may remain draft until RC publication;
- the RC branch may move; and
- mutable source is explicitly non-operative for released consumers.

The intended Product boundary, release-scoped claims, excluded source-project
state, and qualification basis become explicit before RC publication. A
material scope change is repriced instead of being silently absorbed.
```

Successor, `RELEASE.md#mutable-candidate-construction`:

```text
### Mutable candidate construction

During candidate construction (P0, P6;
rc.2 #mutable-candidate-construction):

- bounded fixes are allowed after intake triage;
- qualification and operator review may continue;
- release notes may remain draft until RC publication;
- the RC branch may move; and
- mutable source is explicitly non-operative for released consumers.

The intended Product boundary, release-scoped claims, excluded
source-project state and qualification basis become explicit before RC
publication. A material scope change is repriced instead of being silently
absorbed (P2, P6).
```


### Row `RELEASE_METHOD.md#naming` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#naming` at rc.2:

```text
## Naming

The shared-source naming shape is:

- RC branch: `rc/<project>/<version>`;
- immutable RC tag: `<project>/v<version>-rc.<n>`;
- optional release branch: `release/<project>/<version>`; and
- mutable version-line selector tag: `<project>/v<version>`.

For example:

- candidate branch: `rc/stdo_representation/2.5.0`;
- first immutable cut: `stdo_representation/v2.5.0-rc.1`;
- second immutable cut: `stdo_representation/v2.5.0-rc.2`;
- latest-release branch: `release/stdo_representation/2.5.0`; and
- latest-published selector: `stdo_representation/v2.5.0`.

The unqualified profile remains lawful only under the single-project and
historical-conservation conditions above. Projects may choose another spelling
only in a release source whose ref policy proves collision freedom and preserves
the same project namespace, mutable carrier, immutable cut, and mutable selector
distinctions.
```

Successor, `RELEASE.md#5-naming`:

```text
## 5. Naming

The shared-source naming shape is (P3; rc.2 #naming):

- RC branch: `rc/<project>/<version>`;
- immutable RC tag: `<project>/v<version>-rc.<n>`;
- optional release branch: `release/<project>/<version>`; and
- mutable version-line selector tag: `<project>/v<version>`.

For example:

- candidate branch: `rc/stdo_representation/2.5.0`;
- first immutable cut: `stdo_representation/v2.5.0-rc.1`;
- second immutable cut: `stdo_representation/v2.5.0-rc.2`;
- latest-release branch: `release/stdo_representation/2.5.0`; and
- latest-published selector: `stdo_representation/v2.5.0`.

The unqualified profile remains lawful only under the single-project and
historical-conservation conditions of §2. Projects may choose another
spelling only in a release source whose ref policy proves collision
freedom and preserves the same project namespace, mutable carrier,
immutable cut and mutable selector distinctions (P3).
```


### Row `RELEASE_METHOD.md#open-questions` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#open-questions` at rc.2:

```text
## Open Questions

- What exact qualification bundle is mandatory for each Product class?
- What version-line compatibility rule requires a new `<version>` rather than a
  higher RC ordinal?
```

Successor, `RELEASE.md#10-open-questions`:

```text
## 10. Open questions

These questions remain open (P2; rc.2 #open-questions):

- What exact qualification bundle is mandatory for each Product class?
- What version-line compatibility rule requires a new `<version>` rather
  than a higher RC ordinal?
```


### Row `RELEASE_METHOD.md#phases` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#phases` at rc.2:

```text
## Phases

The release process has three phases:

1. mutable candidate construction;
2. immutable RC publication and monotonic version-line advancement; and
3. exact-cut qualification, acceptance, and explicit consumer adoption.

There is no second final cut after an accepted RC. Publication immediately
makes the new highest ordinal discoverable through the version-line selector;
acceptance remains a verdict over the exact immutable RC rather than a second
carrier. If any byte capable of affecting the Product or a release-scoped claim
changes, the project publishes and reviews a higher immutable RC cut instead.
```

Successor, `RELEASE.md#3-phases`:

```text
## 3. Phases

The release process has three phases (P0, P3, P6; rc.2 #phases):

1. mutable candidate construction;
2. immutable RC publication and monotonic version-line advancement; and
3. exact-cut qualification, acceptance and explicit consumer adoption.

There is no second final cut after an accepted RC. Publication immediately
makes the new highest ordinal discoverable through the version-line
selector; acceptance remains a verdict over the exact immutable RC rather
than a second carrier. If any byte capable of affecting the Product or a
release-scoped claim changes, the project publishes and reviews a higher
immutable RC cut instead (P3, P6).

### Mutable candidate construction

During candidate construction (P0, P6;
rc.2 #mutable-candidate-construction):

- bounded fixes are allowed after intake triage;
- qualification and operator review may continue;
- release notes may remain draft until RC publication;
- the RC branch may move; and
- mutable source is explicitly non-operative for released consumers.

The intended Product boundary, release-scoped claims, excluded
source-project state and qualification basis become explicit before RC
publication. A material scope change is repriced instead of being silently
absorbed (P2, P6).

### Immutable RC publication

A published RC cut exists to provide one exact subject for review, replay
and possible acceptance. To publish it, the project (P3, P5, P6;
rc.2 #immutable-rc-publication):

1. confirms the triaged scope and lawful constitutional re-entry;
2. declares the exact Product release subject and release-scoped claim
   set;
3. reconciles the release note and other release-facing assets to that
   subject;
4. runs the proportionate pre-RC qualification and operator checks;
5. commits the exact carrier;
6. resolves and records the exact Project Release Namespace, Project
   Subtree root and Project Subtree tree;
7. creates one annotated immutable `<project>/v<version>-rc.<n>` tag and
   an annotated `<project>/v<version>` selector tag over that same commit
   in a shared release source;
8. atomically pushes the carrier, RC branch, immutable RC tag, selector
   and optional release branch where the transport supports it;
9. verifies remotely that the immutable tag, selector and release branch
   resolve to the highest published RC commit; and
10. records enough ref, subtree, identity and inventory evidence to
    reacquire the cut without trusting a mutable checkout.

Each published RC tag is immutable. Further work increments `<n>` on the
same version line when the intended line remains applicable. It does not
require a minor-version increment merely because review found a bounded
repair. A published higher RC without matching selector advancement is an
invalid, fail-closed release state; it never authorises resolution of the
older cut as the version-line latest (P3, P5).

### Exact-cut qualification

Qualification binds (P6, P3; rc.2 #exact-cut-qualification):

- the Project Release Namespace, qualified immutable RC ref, annotated tag
  object, peeled commit, repository tree, Project Subtree root and tree,
  and declared Product member set;
- the exact release-scoped claim bytes;
- the governing Product and release basis;
- each claimed property and its observation boundary;
- evidence subjects, owner verdicts and unresolved gaps; and
- the complete successor relation to the declared predecessor (§9).

Evidence matches the claim. Source success does not prove packaged or
installed behaviour; packaging equivalence does not prove semantic
behaviour; artifact presence does not prove usability unless presence is
the exact claim (P6, P1; EVALUATION §1 is the generic claim law).

An RC is accepted only when the required exact-cut review and operator
checks are complete and the human authority accepts that exact subject. If
review requires any qualifying-byte change, the verdict remains attached
to the old RC and a higher RC is published. The selector already
advertises the highest published RC; acceptance does not move it, rewrite
it or create another final carrier (P6, P3).

### Monotonic version-line advancement

Version-line advancement makes the newly published highest RC for one
Project Release Namespace discoverable (P3, P5;
rc.2 #monotonic-version-line-advancement):

1. identify the exact new immutable RC tag, ordinal and peeled commit;
2. confirm that no higher RC ordinal already exists on that line;
3. confirm the project-qualified selector is absent or currently resolves
   to a lower RC ordinal on the same project line;
4. atomically create or force-update the annotated `<project>/v<version>`
   selector to the new highest RC commit;
5. create or update `release/<project>/<version>` to the same commit when
   that optional carrier is used;
6. push the carrier, RC branch, immutable RC tag, selector and optional
   release branch atomically where the transport supports it; and
7. verify remotely that the selector peels to the highest RC commit and
   that the matching immutable annotated RC tag exists.

Advancement is refused when the target has no matching immutable annotated
RC tag, any higher ordinal already exists, the selector would move to a
lower RC, or the selector and release branch would not align to the same
highest commit (P5).

Forward movement is strictly monotonic by RC ordinal. A later defect is
repaired through a higher immutable RC, not by moving an old RC tag or
rolling the selector backward. The selector is therefore equivalent to
`v<version>-rc.latest`, while every concrete RC tag remains addressable
(P3).
```


### Row `RELEASE_METHOD.md#position` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#position` at rc.2:

```text
## Position

Release process is distinct from live project specification.

Live specification defines the current constitutional truth of the project.
Release process defines how one published point-in-time cut is evaluated,
bounded, named, published, and made discoverable.

The product-local cut name is always:

```text
v<version>-rc.<n>
```

In a release source carrying one independently released project, that name may
also be the Git tag name. In a shared release source it is the suffix of the
project-qualified Git ref defined below. Equal product-local cut names do not
collapse releases owned by different projects.

The product-local version-line selector name is:

```text
v<version>
```

It denotes a mutable **Version-Line Selector**. The selector points to the
latest published immutable RC cut on that line, where latest means the greatest
positive RC ordinal published for that project and version line. It is
convenient discovery, not immutable identity and not sufficient as an exact
constitutional, dependency, evidence, or replay basis.

Release handling is downstream of intake triage. A bug, feature, regression,
or release blocker first receives its change class, lawful re-entry point,
affected scope, downstream proof obligations, and version-line disposition.
The existence of an RC window does not authorize untriaged mutation.
```

Successor, `RELEASE.md#1-context-and-position`:

```text
## 1. Context and position

This member owns the release-publication bounded context
`urn:stdo:bounded-context:release-publication` under the selected complete
STDO basis. It owns the identities and transitions used to qualify,
publish and select released cuts. It does not own Product meaning or
consumer adoption; the consumer side of adoption is PRODUCT_DEFINITION §4
(P6, P3; rc.2 #release-publication-context).

Release process is distinct from live project specification. Live
specification defines the current constitutional truth of the project.
Release process defines how one published point-in-time cut is evaluated,
bounded, named, published and made discoverable (P3; rc.2 #position).

The product-local cut name is always:

```text
v<version>-rc.<n>
```

In a release source carrying one independently released project, that
name may also be the Git tag name. In a shared release source it is the
suffix of the project-qualified Git ref of §2. Equal product-local cut
names do not collapse releases owned by different projects (P3).

The product-local version-line selector name is:

```text
v<version>
```

It denotes a mutable version-line selector (FOUNDATIONS §2). The selector
points to the latest published immutable RC cut on that line, where latest
means the greatest positive RC ordinal published for that project and
version line. It is convenient discovery, not immutable identity and not
sufficient as an exact constitutional, dependency, evidence or replay
basis (P3, P6).

Release handling is downstream of intake triage. A bug, feature,
regression or release blocker first receives its change class, lawful
re-entry point, affected scope, downstream proof obligations and
version-line disposition
([SPEC_METHOD §4](SPEC_METHOD.md#universal-intake-triage)). The existence
of an RC window does not authorise untriaged mutation (P0, P6).

Results. This member defines no result values of its own. Where it says
that an operation is refused, stops or fails closed, the operation does
not complete; its intended effect, with any part of it that began, is
reported under [ACTIVATION §3 Effects](ACTIVATION.md#effects), never as
`completed`.
Where it calls a release state invalid or a cohort incomplete, or says
that a verification fails, the condition named is a counterexample to the
predicate that check evaluates, and the check returns its value under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). What the disposition
values of §9 are, §9 states. Purpose and material relation: release
outcomes combine with every other result in the one core, so a refused
publication or a failed verification is never read as a published or
qualified cut (P5, P6).

### Foundation to law: release and successor conservation

This family (F15 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law))
decides how a product's releases are identified, published, qualified,
accepted and selected, and how a successor conserves its predecessor's
claims. Its instance premises, which the commitments do not supply, are
named in the rows as follows: recursive products, a released product may
build other products and the next version of itself; published cuts, a
project publishes point-in-time cuts of its product for review, replay and
adoption by consumers it does not control; mutable carriers, the carrier
that holds a release has movable names and may hold several independently
released projects; derived assets, some products are released with
derived or distributed assets that must match their source; external
services, some claims depend on services outside the carrier; successor
lines, a product evolves from a predecessor release whose claims may
affect it. The index also assigns to this family
[FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects);
the table traces that section in its first two rows, whose rule column
names it, and owns none of it. Each commitment's standing is written as
the table of commitments in FOUNDATIONS §3 states it.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent); P6 (independent); instance: recursive products | By P3 each object binds its own identity and basis, so substrate, development product, source project, release cut, product, install, artifact and product definition are distinct objects. A mutable source workspace binds no fixed identity and so is not called a product; by P6 binding grants nothing, so an install acting as builder substrate is bound as a development product and transfers no meaning or authority to the product being authored, and a product definition is a source-project surface, not the released artifact. | [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects), the taxonomy and its governing rules | the eight roles, their concept identities and the compiler analogy as the intended model: choices of FOUNDATIONS §2; their application to lineage: [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release) (family F10) | 1, 2 |
| P3 (independent); P6 (independent); instance: published cuts, mutable carriers | By P3 an identity binds exact content, so a candidate source, a release cut, a release subject and a version-line selector are distinct, and equal version text collapses none. A selector or mutable carrier may move and a release cut never moves, so a selector is discovery, not identity and not an exact basis; by P6 sharing a carrier grants nothing, so material does not become a member by sharing one. | [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects), Release objects; [§1](#1-context-and-position), the selector paragraph; [§2](#2-release-identities) | the four generic objects: choices of FOUNDATIONS §2; their realisation as Git branches, tags and aliases in the seven identities: domain choices of this member | 1, 2 |
| P3 (independent); P6 (independent); P0 (recovered); instance: published cuts | By P6 an authority owns only what it is admitted to decide, so release process is separate from live specification and owns neither Product meaning nor consumer adoption. By P3 and P0 a release changes what consumers bind, so release handling follows intake triage, and an open release window authorises no untriaged change. | [§1](#1-context-and-position) | the bounded-context identity and the cut and selector name forms: domain choices of this member; triage: [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) (family F11) | 1, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent) | By P5 a value decides only what its evidence establishes, and by P6 an operation's outcome is not its acceptance, so a refused, stopped or fail-closed release operation, an invalid state and a failed check report in the one core, and none is read as success. | [§1](#1-context-and-position), Results | none | 3, 9 |
| P3 (independent); P6 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance: mutable carriers | By P3 a cut must be re-acquirable from what it binds, so a cut binds the namespace, exact ref and commit, subtree root and tree, member inventory, claims and dispositions, and an inventory without these is not a reacquirable identity. By P6 and P1 a name or path grants no membership, so each project's refs carry the namespace Product release authority assigns, and a tag over a shared commit makes no sibling a member. By P4b published identities are not erased, so existing refs and public URIs are conserved, never recreated or moved. | [§2](#2-release-identities), Project-qualified Git refs, Project-subtree release identity, Historical ref and public-URI conservation; [§5](#5-naming); [§6 Product subject and repository carrier](#product-subject-and-repository-carrier) | the ref shapes, the namespace pattern, the canonical root spelling, the naming examples and the unqualified single-project profile: domain choices of this member; each namespace, the three allocated ones included: the Product release authority | 1, 2, 8 |
| P3 (independent); P6 (independent); P0 (recovered); P5 (derived from P0 and P6, with P0's open-world premise); instance: published cuts | By P3 review and replay need one fixed subject, so publication fixes one exact immutable subject, and a change to any qualifying byte, a release-scoped asset included, needs a higher immutable cut. By P6 and P0 consumers rely only on what was released, so mutable candidate source is non-operative for released consumers. | [§3](#3-phases), Mutable candidate construction and Immutable RC publication; [§6 Release-scoped assets](#release-scoped-assets) | the division into three phases (mutable candidate construction; immutable publication; exact-cut qualification, acceptance and explicit adoption), the rule that there is no second final cut, the ten publication steps, the six release-scoped surfaces and the RC ordinal: domain choices of this member | 1, 9 |
| P6 (independent); P1 (independent); P3 (independent); instance: published cuts | By P3 and P6 a verdict holds for the exact subject and claim it binds, so qualification binds the exact cut, claims, basis, each claimed property with its observation boundary, evidence, verdicts, gaps and successor relation, and acceptance is the acceptance authority's verdict over the exact immutable cut. By P1 a weaker kind of evidence does not stand for a stronger claim. A verdict moves no selector, and a change to a qualifying byte leaves the verdict on the old cut. | [§3 Exact-cut qualification](#exact-cut-qualification); [§8 Acceptance criteria](#acceptance-criteria) | the seven acceptance criteria: domain choices of this member; the generic claim and acceptance law: [EVALUATION §1](EVALUATION.md#1-claims) and [§5](EVALUATION.md#5-acceptance) (family F6); acceptance of each cut: the human Product authority | 7, 9 |
| P3 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent); instance: published cuts, mutable carriers | By P3 a selector names an existing cut and never governs, so it advances strictly by ordinal, only to an existing immutable cut, and is refused otherwise; it answers which highest cut exists, never which cut governs a consumer. By P6 a consumer's basis changes only by its own authority, so it changes only by an explicit adoption whose presented plan is accepted; by P5 drift invalidates that acceptance, and resolution fails closed. | [§3 Monotonic version-line advancement](#monotonic-version-line-advancement); [§4](#4-selector-and-consumer-adoption) | the seven advancement steps, the four refusal conditions and the channel URI as discovery selector: domain choices of this member; the adoption plan, its hashing and the manager commands: [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) (family F12) | 1, 9 |
| P3 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent); instance: derived assets, mutable carriers | By P3 matching is a relation between exact versions, so a declared cohort carries one exact version suffix, and equal versions establish matching only. By P4b and P5 a derived member depends on its source, so a missing, stale or differently versioned member makes the cohort incomplete, and a source change invalidates the derived members, which are regenerated and released under the new cut. By P6 a partial cohort is not the declared one, so publication is atomic or refused, each ref guarded against an unexpected remote state, and verification refuses a partial cohort. | [§7](#7-coordinated-release-matched-asset-cohorts), Two-commit construction and one publication transaction, Qualification and recovery | declaring each cohort: the declaring Product authority; the five members of the STDO stack cohort, the two-commit construction and the per-ref lease: domain choices of this member; any same-version recovery: separately authorised recovery law | 1, 6, 9 |
| P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: external services | By P5 a skipped evaluation has no result, and by P6 a claim is qualified only on its evidence, so a claim that depends on an external service is qualified against a healthy dependency or narrowed before acceptance, and a skipped evaluation establishes nothing about the dependent capability. | [§8 External qualification dependencies](#external-qualification-dependencies) | none | 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P6 (independent); P1 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: successor lines | By P4b and P3 a successor evolves one exact, immutable predecessor whose established claims persist, so it names that predecessor, and every predecessor claim that can affect it receives one disposition. By P6 and P1 a disposition is a claim evaluated on evidence, so naming or code similarity does not prove conservation, and a missing patch does not prove loss when a successor-native realisation preserves behaviour; by P5 an unresolved disposition leaves a gap, so the affected claim cannot be qualified. | [§9](#9-successor-baseline-conservation-stdo-up-015) | the four disposition values: this member, restating UP-015; each removal: the current Product authority; the record of a successor's dispositions: that successor's construction | 1, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P6 (independent); instance: successor lines | By P4b a change on a support line persists into what the successor retains, and by P6 its effect needs a disposition by evidence, so where a maintenance or support line may affect retained claims, the release basis names its watched source, observation boundary, inclusion policy and successor candidate, and relevant changes receive a disposition at integration and at qualification. | [§9](#9-successor-baseline-conservation-stdo-up-015), the support-line paragraph | the record, branch strategy, comparison and proof mechanism: the consumer; a policy of this member: the four items the release basis names (watched source, observation boundary, inclusion policy, successor candidate) | 1, 9 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).
The table accounts for §1 to §9 and for FOUNDATIONS §2 Product lineage
objects. §10 records open questions and decides nothing; §11 records
dispositions and decides nothing.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the lineage objects: [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the roles are applied to lineage and the product definition is the source project's present-tense surface; [EXECUTIVE_BASELINE §6 Product-chain basis](EXECUTIVE_BASELINE.md#product-chain-basis), whose basis records the distinct role of every lineage object in a chain, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the Product chain imports F15; [WORLD_MODEL §2](WORLD_MODEL.md#2-role-and-imports) and [Builder Project specialisation](WORLD_MODEL.md#builder-project-specialisation), which import the lineage concepts and narrow Source Project without aliasing it; the [ODD family table](ODD.md#foundation-to-law), whose row for builder, release and source distinctions imports F15.
- Row 2, release objects and release identities: [IDENTITY §9](IDENTITY.md#9-release-version-boundary), where the immutable cut is the only exact operative release identifier and the selector only names the highest-ordinal published cut; [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the mutable tag is a discovery selector and not a dependency, evidence or constitutional basis; [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager), where the definition's channel selector takes its alias semantics from the release law and is not operative authority; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), Acquisition, where a candidate source or a version-line selector is no substitute for the exact selected basis; the [ODD family table](ODD.md#foundation-to-law), whose row for builder, release and source distinctions imports F15 for the selected release and mutable source.
- Row 3, position and triage: [ODD §15](ODD.md#15-release-boundary), where publication, selector advancement and acceptance stay a process surface apart from graph truth; [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the cut is release metadata and not part of the live project specification; [§3 Mutable candidate construction](#mutable-candidate-construction), where bounded fixes follow intake triage, and [Immutable RC publication](#immutable-rc-publication), step 1, which confirms the triaged scope.
- Row 4, results of release operations: the clauses of this member that refuse, stop, fail closed or find a state invalid report under it: [§2 Historical ref and public-URI conservation](#historical-ref-and-public-uri-conservation), [§3 Immutable RC publication](#immutable-rc-publication) and [Monotonic version-line advancement](#monotonic-version-line-advancement), [§4](#4-selector-and-consumer-adoption), and [§7](#7-coordinated-release-matched-asset-cohorts) with [Two-commit construction and one publication transaction](#two-commit-construction-and-one-publication-transaction) and [Qualification and recovery](#qualification-and-recovery); no section of another member applies it, and PRODUCT_DEFINITION §4 maps its manager's outcomes into the core through ACTIVATION §3 without this paragraph.
- Row 5, refs, subtree, conservation, naming and the Product subject: [§3 Immutable RC publication](#immutable-rc-publication), steps 6 and 7, which record the namespace, subtree root and tree and create the project-qualified tags; [§3 Exact-cut qualification](#exact-cut-qualification), which binds the namespace, qualified ref, tag object, commit, trees and declared member set; [§4](#4-selector-and-consumer-adoption), whose channel resolution enumerates a namespace's published tags, preserved historical cuts included; [§7](#7-coordinated-release-matched-asset-cohorts), whose cut names and refs render the cohort suffix and whose cut tags are create-only; otherwise no separate consumer applies: the ref shapes, namespaces and the Product subject are this member's domain choices, and the installed-manifest binding of PRODUCT_DEFINITION §4 names the cut's tag object, commit, tree and inventory without naming this section.
- Row 6, candidate construction, immutable publication and release-scoped assets: [AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity), whose edition identity record is issued at the release of its bytes and nowhere earlier; [§7](#7-coordinated-release-matched-asset-cohorts) and [Two-commit construction and one publication transaction](#two-commit-construction-and-one-publication-transaction), where derived members are regenerated and released under the new cut and the cut tags are published atomically or refused; [§8 Acceptance criteria](#acceptance-criteria), where release-scoped assets describe the exact cut; [§3 Exact-cut qualification](#exact-cut-qualification), where a qualifying-byte change leaves the verdict on the old cut and a higher cut is published.
- Row 7, exact-cut qualification and acceptance criteria: [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where the acceptance criteria are the mandatory gates that stay applicable irrespective of the selection of checks; [§7 Qualification and recovery](#qualification-and-recovery), whose content, local-ref-graph and post-publication qualification bind the exact cut; [§8 External qualification dependencies](#external-qualification-dependencies), where a dependent claim is qualified or narrowed before acceptance; [§9](#9-successor-baseline-conservation-stdo-up-015), where an unresolved disposition blocks qualification of the affected claim.
- Row 8, selector advancement and consumer adoption: [ODD §4](ODD.md#4-method-library-classes), where the selected immutable cut is consumer authority and mutable source and the moving selector cannot repair, replace or outrank it; [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager), whose `adopt` resolves the selector only to present an exact digest-bound plan and whose `sync` never consults it; [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the selector cannot silently change a consumer selection.
- Row 9, release-matched cohorts: [PRODUCT_DEFINITION §4 Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update), which binds the complete companion population of one exact upstream cohort and verifies its dependency closure before relying on it; otherwise no separate consumer applies: declaring a cohort is the declaring Product authority's act under this section, and SPEC_METHOD §6 refers the process for cutting a release to §2 to §8 and applies none of it.
- Row 10, external qualification dependencies: no separate consumer applies. The rule acts inside this member's qualification and acceptance (§3 Exact-cut qualification, §8 Acceptance criteria), where a claim that depends on an external service is qualified against a healthy dependency or narrowed; the result of a clean skip is FOUNDATIONS §4 Results', Not performed, which this section applies, and no section of another member names this section.
- Row 11, successor baseline conservation: [EVALUATION §5](EVALUATION.md#5-acceptance), where a successor's acceptance evidence includes the disposition record and an unresolved disposition blocks acceptance; [SPEC_METHOD §2 Requirement categories and classification](SPEC_METHOD.md#requirement-categories-and-classification), where each predecessor claim takes its disposition by this section's predicates and no lifecycle status supplies it, and [§7 Fundamental migration](SPEC_METHOD.md#fundamental-migration), where no migration class is or supplies a disposition; [FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing), which keeps the standing of a commitment apart from a disposition, and [§4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction), where a change to the governing meaning follows the successor rules; [TICKETS §7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) and [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), which keep repricing dispositions and closure decisions apart from the disposition of a predecessor claim; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 7, 8 and 49; [§2 Project-subtree release identity](#project-subtree-release-identity) and [§3 Exact-cut qualification](#exact-cut-qualification), which bind the dispositions and the successor relation this section requires; the Source dispositions sections of the members record the values and decide nothing.
- Row 12, support lines: no separate consumer applies. The record, branch strategy, comparison and proof mechanism are the consumer's, as the choice column states; a release basis that names a watched source does so under this paragraph, and no section of another member names it.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `RELEASE_METHOD.md#product-subject-and-repository-carrier` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#product-subject-and-repository-carrier` at rc.2:

```text
## Product Subject And Repository Carrier

Before qualification, the project declares:

- its Project Release Namespace and exact Project Subtree root;
- the exact Product member set or artifact constituting the release subject;
- the release-scoped claim surfaces describing that subject; and
- co-located mutable source-project fields excluded from both.

A repository commit carries those declared sets but does not make every
co-located file or sibling Project Subtree a Product member. The exact
Project Subtree tree and Product member inventory distinguish the subject from
the wider carrier. Once the immutable RC is published, no post-review carrier
delta is admitted into that cut. Publication-caused ticket or source-work
bookkeeping is recorded afterward on the continuing source branch and cannot
move the immutable RC tag.
```

Successor, `RELEASE.md#product-subject-and-repository-carrier`:

```text
### Product subject and repository carrier

Before qualification, the project declares (P3, P6;
rc.2 #product-subject-and-repository-carrier):

- its Project Release Namespace and exact Project Subtree root;
- the exact Product member set or artifact constituting the release
  subject;
- the release-scoped claim surfaces describing that subject; and
- co-located mutable source-project fields excluded from both.

A repository commit carries those declared sets but does not make every
co-located file or sibling Project Subtree a Product member. The exact
Project Subtree tree and Product member inventory distinguish the subject
from the wider carrier. Once the immutable RC is published, no post-review
carrier delta is admitted into that cut. Publication-caused ticket or
source-work bookkeeping is recorded afterward on the continuing source
branch and cannot move the immutable RC tag (P3, P6).
```


### Row `RELEASE_METHOD.md#qualification-and-recovery` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#qualification-and-recovery` at rc.2:

```text
### Qualification And Recovery

Prepublication content qualification binds the exact commit-A STDO tag and
manifest, commit-B source tree, all Product-local target refs, version markers,
Product member inventories, semantic-index bytes, and complete source-corpus
digest closure. It proves that the frozen candidate can be tagged without
changing a qualifying byte. After tag and mutable ref creation, local-ref-graph
qualification binds their annotated objects, peels, target commits, exact push
set, and every fetched remote expected object ID or required absence to that
unchanged content result. Post-publication qualification
verifies the same relation from remote refs and refuses a partial cohort.

A historically published source cut may be the basis of a later same-version
backfill only when separately authorized recovery law names that exception.
Every recovered asset still binds the exact historical cut and same cut name,
and remote completeness remains mandatory. Recovery cannot move the historical
tag, add bytes to its Product subject, or be represented as an atomic cohort
that existed at the original publication. Normal successor publication uses
the atomic cohort process above.

Adding or changing this cohort law changes qualifying Release Method bytes. It
governs only a higher immutable RC that contains those bytes and cannot
retroactively make an earlier cut a coordinated cohort.
```

Successor, `RELEASE.md#qualification-and-recovery`:

```text
### Qualification and recovery

Prepublication content qualification binds the exact commit-A STDO tag
and manifest, commit-B source tree, all Product-local target refs, version
markers, Product member inventories, semantic-index bytes and complete
source-corpus digest closure. It proves that the frozen candidate can be
tagged without changing a qualifying byte. After tag and mutable ref
creation, local-ref-graph qualification binds their annotated objects,
peels, target commits, exact push set, and every fetched remote expected
object ID or required absence to that unchanged content result.
Post-publication qualification verifies the same relation from remote refs
and refuses a partial cohort (P6, P3, P5;
rc.2 #qualification-and-recovery).

A historically published source cut may be the basis of a later
same-version backfill only when separately authorised recovery law names
that exception. Every recovered asset still binds the exact historical cut
and same cut name, and remote completeness remains mandatory. Recovery
cannot move the historical tag, add bytes to its Product subject, or be
represented as an atomic cohort that existed at the original publication.
Normal successor publication uses the atomic cohort process above (P3,
P6).

Adding or changing this cohort law changes qualifying bytes of this
member. It governs only a higher immutable RC that contains those bytes
and cannot retroactively make an earlier cut a coordinated cohort (P3).
```


### Row `RELEASE_METHOD.md#release-identities` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#release-identities` at rc.2:

```text
## Release Identities

The release-publication context distinguishes:

- **Project Release Namespace** — a stable repository-local key assigned by the
  Product release authority to one independently released source project;
- **Project Subtree** — the exact repository-relative source-project root and
  Git tree object selected for one cut;
- **Candidate Source** — mutable source-project state constructing a possible
  successor;
- **RC Branch** — a mutable project-qualified carrier for the current candidate
  window;
- **Immutable RC Cut** — an annotated project-qualified Git tag plus its exact
  Product release subject, naming one published candidate and, once accepted,
  one released Product;
- **Version-Line Selector** — the mutable project-qualified tag alias naming
  the highest-ordinal published immutable RC cut for that project and version
  line; and
- **Release Branch** — an optional mutable project-qualified convenience
  carrier aligned to the same latest-published commit as the selector.

Equal version text does not collapse these identities. Branches and the
version-line selector may move. An immutable RC tag never moves.
```

Successor, `RELEASE.md#2-release-identities`:

```text
## 2. Release identities

The release-publication context distinguishes (P3;
rc.2 #release-identities):

- Project Release Namespace: a stable repository-local key assigned by
  the Product release authority to one independently released source
  project;
- Project Subtree: the exact repository-relative source-project root and
  Git tree object selected for one cut;
- Candidate Source: the candidate source of FOUNDATIONS §2, the mutable
  source-project state constructing a possible successor;
- RC Branch: a mutable project-qualified carrier for the current
  candidate window;
- Immutable RC Cut: an annotated project-qualified Git tag plus its exact
  Product release subject (FOUNDATIONS §2), naming one published candidate
  and, once accepted, one released Product; it realises the release cut;
- Version-Line Selector: the mutable project-qualified tag alias naming
  the highest-ordinal published immutable RC cut for that project and
  version line; it realises the version-line selector of FOUNDATIONS §2;
  and
- Release Branch: an optional mutable project-qualified convenience
  carrier aligned to the same latest-published commit as the selector.

Equal version text does not collapse these identities. Branches and the
version-line selector may move. An immutable RC tag never moves (P3).

### Project-qualified Git refs

`<project>` is one explicit Project Release Namespace. It matches
`[a-z0-9]+(?:[-_][a-z0-9]+)*`, contains no slash, is unique within the
release source, and remains stable for the continuing release line. It is
assigned by the Product release authority. A directory name, display name,
definition label, package name or matching version cannot infer or
reassign it (P3, P6; rc.2 #project-qualified-git-refs).

A shared release source uses these exact ref shapes for every future
publication (P3):

```text
RC branch:              refs/heads/rc/<project>/<version>
immutable RC cut tag:   refs/tags/<project>/v<version>-rc.<n>
version-line selector:  refs/tags/<project>/v<version>
release branch:         refs/heads/release/<project>/<version>
```

The short Git tag names are therefore `<project>/v<version>-rc.<n>` and
`<project>/v<version>`. A shared release source does not publish a future
cut or selector under the unqualified `v<version>-rc.<n>` or `v<version>`
refs (P3).

A single-project release source may retain the unqualified ref profile
only while it has exactly one independently released project and its
release record declares that profile. Adding a second independently
released project requires project-qualified refs before either project
publishes another cut (P3).

For the Specification Stack shared source, the allocated namespaces are
`specification_methodology`, `axiom_indexer` and `stdo_representation`.
These keys distinguish release refs; they do not merge the three Products
or imply a dependency or composition relation (P3, P6).

### Project-subtree release identity

In a shared release source, an immutable cut binds all of (P3;
rc.2 #project-subtree-release-identity):

- the Project Release Namespace and owning Product authority;
- the exact qualified Git ref and annotated tag object;
- the peeled commit and repository-root tree;
- the normalised repository-relative Project Subtree root at that commit;
- the Git tree object at that exact Project Subtree root;
- the declared Product member inventory and release-scoped claim bytes;
  and
- the predecessor and successor dispositions required by §9.

The Project Subtree root is a locator inside the exact peeled commit, not
Product identity. Its canonical spelling is the slash-separated Git path
from the repository root, with no leading or trailing slash and no empty,
`.` or `..` component; `.` alone denotes the repository root. Each
non-root component names the exact tree entry bytes traversed at that
commit. Moving a source project changes this locator and its cut identity
without reassigning the Project Release Namespace. If the source project
occupies the repository root, its project-subtree tree equals the
repository-root tree (P3).

A tag over a monorepo commit does not make sibling subtrees Product
members. Unrelated sibling bytes remain carrier state outside the declared
Product subject. Conversely, a member inventory or payload digest without
the qualified ref, commit, Project Subtree root and Project Subtree tree is
not a complete reacquirable release identity (P3, P6).

### Historical ref and public-URI conservation

Project qualification is prospective. Existing unqualified refs retain
their names, objects, peels and public links. A historical tag object may
remain reachable through an additional archival ref, but it is not
recreated, re-annotated, moved or replaced. An immutable historical tag
remains the same object regardless of which preserving ref reaches it
(P3, P4b; rc.2 #historical-ref-and-public-uri-conservation).

Product-local cut names and public logical release URIs also remain
unchanged. In particular, a logical STDO release remains
`stdo://releases/v<version>-rc.<n>/`; the project-qualified Git ref is
transport identity and is not inserted into that URI. Resolution binds
the public logical cut to its exact historical or project-qualified Git
ref and fails closed if one project-local coordinate names different tag
objects (P3, P5).

When one version line spans the transition, latest means the greatest
positive RC ordinal across that project's preserved historical cuts and
its qualified future cuts. The first qualified publication creates the
qualified selector. The historical unqualified selector is preserved at
its existing object and ceases to be the current selector for the shared
source; it is not force-moved to imitate the qualified namespace (P3).
```

Successor, `FOUNDATIONS.md#product-lineage-objects`:

```text
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
```


### Row `RELEASE_METHOD.md#release-publication-context` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#release-publication-context` at rc.2:

```text
## Release-Publication Context

`RELEASE_METHOD.md` owns the release-publication bounded context
`urn:stdo:bounded-context:release-publication` under the selected complete STDO
basis. It owns the identities and transitions used to qualify, publish, and
select released cuts. It does not own Product meaning or consumer adoption.
```

Successor, `RELEASE.md#1-context-and-position`:

```text
## 1. Context and position

This member owns the release-publication bounded context
`urn:stdo:bounded-context:release-publication` under the selected complete
STDO basis. It owns the identities and transitions used to qualify,
publish and select released cuts. It does not own Product meaning or
consumer adoption; the consumer side of adoption is PRODUCT_DEFINITION §4
(P6, P3; rc.2 #release-publication-context).

Release process is distinct from live project specification. Live
specification defines the current constitutional truth of the project.
Release process defines how one published point-in-time cut is evaluated,
bounded, named, published and made discoverable (P3; rc.2 #position).

The product-local cut name is always:

```text
v<version>-rc.<n>
```

In a release source carrying one independently released project, that
name may also be the Git tag name. In a shared release source it is the
suffix of the project-qualified Git ref of §2. Equal product-local cut
names do not collapse releases owned by different projects (P3).

The product-local version-line selector name is:

```text
v<version>
```

It denotes a mutable version-line selector (FOUNDATIONS §2). The selector
points to the latest published immutable RC cut on that line, where latest
means the greatest positive RC ordinal published for that project and
version line. It is convenient discovery, not immutable identity and not
sufficient as an exact constitutional, dependency, evidence or replay
basis (P3, P6).

Release handling is downstream of intake triage. A bug, feature,
regression or release blocker first receives its change class, lawful
re-entry point, affected scope, downstream proof obligations and
version-line disposition
([SPEC_METHOD §4](SPEC_METHOD.md#universal-intake-triage)). The existence
of an RC window does not authorise untriaged mutation (P0, P6).

Results. This member defines no result values of its own. Where it says
that an operation is refused, stops or fails closed, the operation does
not complete; its intended effect, with any part of it that began, is
reported under [ACTIVATION §3 Effects](ACTIVATION.md#effects), never as
`completed`.
Where it calls a release state invalid or a cohort incomplete, or says
that a verification fails, the condition named is a counterexample to the
predicate that check evaluates, and the check returns its value under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). What the disposition
values of §9 are, §9 states. Purpose and material relation: release
outcomes combine with every other result in the one core, so a refused
publication or a failed verification is never read as a published or
qualified cut (P5, P6).

### Foundation to law: release and successor conservation

This family (F15 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law))
decides how a product's releases are identified, published, qualified,
accepted and selected, and how a successor conserves its predecessor's
claims. Its instance premises, which the commitments do not supply, are
named in the rows as follows: recursive products, a released product may
build other products and the next version of itself; published cuts, a
project publishes point-in-time cuts of its product for review, replay and
adoption by consumers it does not control; mutable carriers, the carrier
that holds a release has movable names and may hold several independently
released projects; derived assets, some products are released with
derived or distributed assets that must match their source; external
services, some claims depend on services outside the carrier; successor
lines, a product evolves from a predecessor release whose claims may
affect it. The index also assigns to this family
[FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects);
the table traces that section in its first two rows, whose rule column
names it, and owns none of it. Each commitment's standing is written as
the table of commitments in FOUNDATIONS §3 states it.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent); P6 (independent); instance: recursive products | By P3 each object binds its own identity and basis, so substrate, development product, source project, release cut, product, install, artifact and product definition are distinct objects. A mutable source workspace binds no fixed identity and so is not called a product; by P6 binding grants nothing, so an install acting as builder substrate is bound as a development product and transfers no meaning or authority to the product being authored, and a product definition is a source-project surface, not the released artifact. | [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects), the taxonomy and its governing rules | the eight roles, their concept identities and the compiler analogy as the intended model: choices of FOUNDATIONS §2; their application to lineage: [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release) (family F10) | 1, 2 |
| P3 (independent); P6 (independent); instance: published cuts, mutable carriers | By P3 an identity binds exact content, so a candidate source, a release cut, a release subject and a version-line selector are distinct, and equal version text collapses none. A selector or mutable carrier may move and a release cut never moves, so a selector is discovery, not identity and not an exact basis; by P6 sharing a carrier grants nothing, so material does not become a member by sharing one. | [FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects), Release objects; [§1](#1-context-and-position), the selector paragraph; [§2](#2-release-identities) | the four generic objects: choices of FOUNDATIONS §2; their realisation as Git branches, tags and aliases in the seven identities: domain choices of this member | 1, 2 |
| P3 (independent); P6 (independent); P0 (recovered); instance: published cuts | By P6 an authority owns only what it is admitted to decide, so release process is separate from live specification and owns neither Product meaning nor consumer adoption. By P3 and P0 a release changes what consumers bind, so release handling follows intake triage, and an open release window authorises no untriaged change. | [§1](#1-context-and-position) | the bounded-context identity and the cut and selector name forms: domain choices of this member; triage: [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) (family F11) | 1, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent) | By P5 a value decides only what its evidence establishes, and by P6 an operation's outcome is not its acceptance, so a refused, stopped or fail-closed release operation, an invalid state and a failed check report in the one core, and none is read as success. | [§1](#1-context-and-position), Results | none | 3, 9 |
| P3 (independent); P6 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); instance: mutable carriers | By P3 a cut must be re-acquirable from what it binds, so a cut binds the namespace, exact ref and commit, subtree root and tree, member inventory, claims and dispositions, and an inventory without these is not a reacquirable identity. By P6 and P1 a name or path grants no membership, so each project's refs carry the namespace Product release authority assigns, and a tag over a shared commit makes no sibling a member. By P4b published identities are not erased, so existing refs and public URIs are conserved, never recreated or moved. | [§2](#2-release-identities), Project-qualified Git refs, Project-subtree release identity, Historical ref and public-URI conservation; [§5](#5-naming); [§6 Product subject and repository carrier](#product-subject-and-repository-carrier) | the ref shapes, the namespace pattern, the canonical root spelling, the naming examples and the unqualified single-project profile: domain choices of this member; each namespace, the three allocated ones included: the Product release authority | 1, 2, 8 |
| P3 (independent); P6 (independent); P0 (recovered); P5 (derived from P0 and P6, with P0's open-world premise); instance: published cuts | By P3 review and replay need one fixed subject, so publication fixes one exact immutable subject, and a change to any qualifying byte, a release-scoped asset included, needs a higher immutable cut. By P6 and P0 consumers rely only on what was released, so mutable candidate source is non-operative for released consumers. | [§3](#3-phases), Mutable candidate construction and Immutable RC publication; [§6 Release-scoped assets](#release-scoped-assets) | the division into three phases (mutable candidate construction; immutable publication; exact-cut qualification, acceptance and explicit adoption), the rule that there is no second final cut, the ten publication steps, the six release-scoped surfaces and the RC ordinal: domain choices of this member | 1, 9 |
| P6 (independent); P1 (independent); P3 (independent); instance: published cuts | By P3 and P6 a verdict holds for the exact subject and claim it binds, so qualification binds the exact cut, claims, basis, each claimed property with its observation boundary, evidence, verdicts, gaps and successor relation, and acceptance is the acceptance authority's verdict over the exact immutable cut. By P1 a weaker kind of evidence does not stand for a stronger claim. A verdict moves no selector, and a change to a qualifying byte leaves the verdict on the old cut. | [§3 Exact-cut qualification](#exact-cut-qualification); [§8 Acceptance criteria](#acceptance-criteria) | the seven acceptance criteria: domain choices of this member; the generic claim and acceptance law: [EVALUATION §1](EVALUATION.md#1-claims) and [§5](EVALUATION.md#5-acceptance) (family F6); acceptance of each cut: the human Product authority | 7, 9 |
| P3 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent); instance: published cuts, mutable carriers | By P3 a selector names an existing cut and never governs, so it advances strictly by ordinal, only to an existing immutable cut, and is refused otherwise; it answers which highest cut exists, never which cut governs a consumer. By P6 a consumer's basis changes only by its own authority, so it changes only by an explicit adoption whose presented plan is accepted; by P5 drift invalidates that acceptance, and resolution fails closed. | [§3 Monotonic version-line advancement](#monotonic-version-line-advancement); [§4](#4-selector-and-consumer-adoption) | the seven advancement steps, the four refusal conditions and the channel URI as discovery selector: domain choices of this member; the adoption plan, its hashing and the manager commands: [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager) (family F12) | 1, 9 |
| P3 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P5 (derived from P0 and P6, with P0's open-world premise); P6 (independent); instance: derived assets, mutable carriers | By P3 matching is a relation between exact versions, so a declared cohort carries one exact version suffix, and equal versions establish matching only. By P4b and P5 a derived member depends on its source, so a missing, stale or differently versioned member makes the cohort incomplete, and a source change invalidates the derived members, which are regenerated and released under the new cut. By P6 a partial cohort is not the declared one, so publication is atomic or refused, each ref guarded against an unexpected remote state, and verification refuses a partial cohort. | [§7](#7-coordinated-release-matched-asset-cohorts), Two-commit construction and one publication transaction, Qualification and recovery | declaring each cohort: the declaring Product authority; the five members of the STDO stack cohort, the two-commit construction and the per-ref lease: domain choices of this member; any same-version recovery: separately authorised recovery law | 1, 6, 9 |
| P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: external services | By P5 a skipped evaluation has no result, and by P6 a claim is qualified only on its evidence, so a claim that depends on an external service is qualified against a healthy dependency or narrowed before acceptance, and a skipped evaluation establishes nothing about the dependent capability. | [§8 External qualification dependencies](#external-qualification-dependencies) | none | 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P6 (independent); P1 (independent); P5 (derived from P0 and P6, with P0's open-world premise); instance: successor lines | By P4b and P3 a successor evolves one exact, immutable predecessor whose established claims persist, so it names that predecessor, and every predecessor claim that can affect it receives one disposition. By P6 and P1 a disposition is a claim evaluated on evidence, so naming or code similarity does not prove conservation, and a missing patch does not prove loss when a successor-native realisation preserves behaviour; by P5 an unresolved disposition leaves a gap, so the affected claim cannot be qualified. | [§9](#9-successor-baseline-conservation-stdo-up-015) | the four disposition values: this member, restating UP-015; each removal: the current Product authority; the record of a successor's dispositions: that successor's construction | 1, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P6 (independent); instance: successor lines | By P4b a change on a support line persists into what the successor retains, and by P6 its effect needs a disposition by evidence, so where a maintenance or support line may affect retained claims, the release basis names its watched source, observation boundary, inclusion policy and successor candidate, and relevant changes receive a disposition at integration and at qualification. | [§9](#9-successor-baseline-conservation-stdo-up-015), the support-line paragraph | the record, branch strategy, comparison and proof mechanism: the consumer; a policy of this member: the four items the release basis names (watched source, observation boundary, inclusion policy, successor candidate) | 1, 9 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).
The table accounts for §1 to §9 and for FOUNDATIONS §2 Product lineage
objects. §10 records open questions and decides nothing; §11 records
dispositions and decides nothing.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the lineage objects: [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the roles are applied to lineage and the product definition is the source project's present-tense surface; [EXECUTIVE_BASELINE §6 Product-chain basis](EXECUTIVE_BASELINE.md#product-chain-basis), whose basis records the distinct role of every lineage object in a chain, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the Product chain imports F15; [WORLD_MODEL §2](WORLD_MODEL.md#2-role-and-imports) and [Builder Project specialisation](WORLD_MODEL.md#builder-project-specialisation), which import the lineage concepts and narrow Source Project without aliasing it; the [ODD family table](ODD.md#foundation-to-law), whose row for builder, release and source distinctions imports F15.
- Row 2, release objects and release identities: [IDENTITY §9](IDENTITY.md#9-release-version-boundary), where the immutable cut is the only exact operative release identifier and the selector only names the highest-ordinal published cut; [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the mutable tag is a discovery selector and not a dependency, evidence or constitutional basis; [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager), where the definition's channel selector takes its alias semantics from the release law and is not operative authority; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), Acquisition, where a candidate source or a version-line selector is no substitute for the exact selected basis; the [ODD family table](ODD.md#foundation-to-law), whose row for builder, release and source distinctions imports F15 for the selected release and mutable source.
- Row 3, position and triage: [ODD §15](ODD.md#15-release-boundary), where publication, selector advancement and acceptance stay a process surface apart from graph truth; [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the cut is release metadata and not part of the live project specification; [§3 Mutable candidate construction](#mutable-candidate-construction), where bounded fixes follow intake triage, and [Immutable RC publication](#immutable-rc-publication), step 1, which confirms the triaged scope.
- Row 4, results of release operations: the clauses of this member that refuse, stop, fail closed or find a state invalid report under it: [§2 Historical ref and public-URI conservation](#historical-ref-and-public-uri-conservation), [§3 Immutable RC publication](#immutable-rc-publication) and [Monotonic version-line advancement](#monotonic-version-line-advancement), [§4](#4-selector-and-consumer-adoption), and [§7](#7-coordinated-release-matched-asset-cohorts) with [Two-commit construction and one publication transaction](#two-commit-construction-and-one-publication-transaction) and [Qualification and recovery](#qualification-and-recovery); no section of another member applies it, and PRODUCT_DEFINITION §4 maps its manager's outcomes into the core through ACTIVATION §3 without this paragraph.
- Row 5, refs, subtree, conservation, naming and the Product subject: [§3 Immutable RC publication](#immutable-rc-publication), steps 6 and 7, which record the namespace, subtree root and tree and create the project-qualified tags; [§3 Exact-cut qualification](#exact-cut-qualification), which binds the namespace, qualified ref, tag object, commit, trees and declared member set; [§4](#4-selector-and-consumer-adoption), whose channel resolution enumerates a namespace's published tags, preserved historical cuts included; [§7](#7-coordinated-release-matched-asset-cohorts), whose cut names and refs render the cohort suffix and whose cut tags are create-only; otherwise no separate consumer applies: the ref shapes, namespaces and the Product subject are this member's domain choices, and the installed-manifest binding of PRODUCT_DEFINITION §4 names the cut's tag object, commit, tree and inventory without naming this section.
- Row 6, candidate construction, immutable publication and release-scoped assets: [AXIOMATIC_CALCULUS §8](AXIOMATIC_CALCULUS.md#8-calculus-identity), whose edition identity record is issued at the release of its bytes and nowhere earlier; [§7](#7-coordinated-release-matched-asset-cohorts) and [Two-commit construction and one publication transaction](#two-commit-construction-and-one-publication-transaction), where derived members are regenerated and released under the new cut and the cut tags are published atomically or refused; [§8 Acceptance criteria](#acceptance-criteria), where release-scoped assets describe the exact cut; [§3 Exact-cut qualification](#exact-cut-qualification), where a qualifying-byte change leaves the verdict on the old cut and a higher cut is published.
- Row 7, exact-cut qualification and acceptance criteria: [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where the acceptance criteria are the mandatory gates that stay applicable irrespective of the selection of checks; [§7 Qualification and recovery](#qualification-and-recovery), whose content, local-ref-graph and post-publication qualification bind the exact cut; [§8 External qualification dependencies](#external-qualification-dependencies), where a dependent claim is qualified or narrowed before acceptance; [§9](#9-successor-baseline-conservation-stdo-up-015), where an unresolved disposition blocks qualification of the affected claim.
- Row 8, selector advancement and consumer adoption: [ODD §4](ODD.md#4-method-library-classes), where the selected immutable cut is consumer authority and mutable source and the moving selector cannot repair, replace or outrank it; [PRODUCT_DEFINITION §4](PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager), whose `adopt` resolves the selector only to present an exact digest-bound plan and whose `sync` never consults it; [SPEC_METHOD §6](SPEC_METHOD.md#6-lineage-and-release), where the selector cannot silently change a consumer selection.
- Row 9, release-matched cohorts: [PRODUCT_DEFINITION §4 Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update), which binds the complete companion population of one exact upstream cohort and verifies its dependency closure before relying on it; otherwise no separate consumer applies: declaring a cohort is the declaring Product authority's act under this section, and SPEC_METHOD §6 refers the process for cutting a release to §2 to §8 and applies none of it.
- Row 10, external qualification dependencies: no separate consumer applies. The rule acts inside this member's qualification and acceptance (§3 Exact-cut qualification, §8 Acceptance criteria), where a claim that depends on an external service is qualified against a healthy dependency or narrowed; the result of a clean skip is FOUNDATIONS §4 Results', Not performed, which this section applies, and no section of another member names this section.
- Row 11, successor baseline conservation: [EVALUATION §5](EVALUATION.md#5-acceptance), where a successor's acceptance evidence includes the disposition record and an unresolved disposition blocks acceptance; [SPEC_METHOD §2 Requirement categories and classification](SPEC_METHOD.md#requirement-categories-and-classification), where each predecessor claim takes its disposition by this section's predicates and no lifecycle status supplies it, and [§7 Fundamental migration](SPEC_METHOD.md#fundamental-migration), where no migration class is or supplies a disposition; [FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing), which keeps the standing of a commitment apart from a disposition, and [§4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction), where a change to the governing meaning follows the successor rules; [TICKETS §7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) and [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), which keep repricing dispositions and closure decisions apart from the disposition of a predecessor claim; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 7, 8 and 49; [§2 Project-subtree release identity](#project-subtree-release-identity) and [§3 Exact-cut qualification](#exact-cut-qualification), which bind the dispositions and the successor relation this section requires; the Source dispositions sections of the members record the values and decide nothing.
- Row 12, support lines: no separate consumer applies. The record, branch strategy, comparison and proof mechanism are the consumer's, as the choice column states; a release basis that names a watched source does so under this paragraph, and no section of another member names it.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `RELEASE_METHOD.md#release-scoped-assets` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#release-scoped-assets` at rc.2:

```text
## Release-Scoped Assets

An immutable RC cut may carry release-scoped surfaces such as:

- release notes;
- release and installed-distribution manifests;
- dependency declarations;
- package or installed-carrier metadata;
- qualification receipts; and
- branch and tag identity declarations.

Before RC publication, each used surface is reconciled to the exact RC subject.
After publication, changing one of those bytes creates a different candidate
and therefore requires a higher RC tag. The version-line selector has no
content-reconciliation phase because it adds no new Product bytes.

Version-line branding does not belong in live present-tense Product or
requirements surfaces merely to signal recency. Exact version and RC identity
belong in release-scoped carriers and consumer basis bindings.
```

Successor, `RELEASE.md#release-scoped-assets`:

```text
### Release-scoped assets

An immutable RC cut may carry release-scoped surfaces such as (P3, P6;
rc.2 #release-scoped-assets):

- release notes;
- release and installed-distribution manifests;
- dependency declarations;
- package or installed-carrier metadata;
- qualification receipts; and
- branch and tag identity declarations.

Before RC publication, each used surface is reconciled to the exact RC
subject. After publication, changing one of those bytes creates a
different candidate and therefore requires a higher RC tag. The
version-line selector has no content-reconciliation phase because it adds
no new Product bytes (P3).

Exact version and RC identity belong in release-scoped carriers and
consumer basis bindings (P3). How a live constitutional surface, Product
and requirements surfaces included, uses version labels is the
[SPEC_METHOD §2 Specification surface rule](SPEC_METHOD.md#specification-surface-rule).
```


### Row `RELEASE_METHOD.md#selector-and-consumer-adoption` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#selector-and-consumer-adoption` at rc.2:

```text
## Selector And Consumer Adoption

The version-line selector answers only:

> Which highest-ordinal published immutable RC cut currently exists on this
> version line?

It never answers:

> Which exact STDO cut governs this consumer?

A Product Definition may retain `stdo://channels/<version>` as its discovery
selector, but its operative basis is the exact
`stdo://releases/v<version>-rc.<n>/` URI and installed-manifest digest. Moving
the Git version-line selector does not update any consumer. Adoption is a
separate explicit Product-Definition transition that resolves, presents,
installs, verifies, and pins the selected immutable RC. Resolution requires an
annotated selector with a distinct peeled commit; absence of a peeled selector
ref fails closed and cannot be interpreted as a lightweight selector whose tag
object is its commit.

Channel resolution enumerates the published RC tags for the selected Project
Release Namespace, including preserved unqualified historical cuts during a
namespace transition, selects the greatest positive ordinal, requires that cut
and the current selector to be annotated tags peeling to the same commit, and
fails closed when the selector lags or points elsewhere. Channel adoption also
refuses a same-line target whose ordinal is below the Product Definition's
current exact basis. A consumer that intentionally retains an older cut names
that immutable RC URI and digest explicitly and uses exact-basis operations
such as `sync`; it does not express that choice through the latest-version
channel.

Presentation and mutation are separate invocations. The read-only plan binds
the current Product Definition bytes and basis to the target immutable cut,
annotated tag object, peeled commit, tree, and installed-manifest digest, then
emits a deterministic plan digest. Mutation requires that exact digest as the
operator's acceptance and re-derives it before changing any Product Definition.
Selector, target, manifest, or definition drift invalidates the acceptance. A
fleet uses the same law with one aggregate digest over all exact per-definition
plans; planning inside a mutating invocation is not external presentation and
cannot authorize itself.

This split lets operators refer to `v<version>` for the latest published RC
without repeatedly incrementing the version line, while every governed project
retains reproducible exact-cut authority and changes only through explicit
adoption.
```

Successor, `RELEASE.md#4-selector-and-consumer-adoption`:

```text
## 4. Selector and consumer adoption

The version-line selector answers only (P6, P3;
rc.2 #selector-and-consumer-adoption):

> Which highest-ordinal published immutable RC cut currently exists on
> this version line?

It never answers:

> Which exact STDO cut governs this consumer?

A Product Definition may retain `stdo://channels/<version>` as its
discovery selector, but its operative basis is the exact
`stdo://releases/v<version>-rc.<n>/` URI and installed-manifest digest,
the installed release basis of PRODUCT_DEFINITION §4. Moving the Git
version-line selector does not update any consumer. Adoption is a separate
explicit Product-Definition transition that resolves, presents, installs,
verifies and pins the selected immutable RC. Resolution requires an
annotated selector with a distinct peeled commit; absence of a peeled
selector ref fails closed and cannot be interpreted as a lightweight
selector whose tag object is its commit (P6, P3, P5).

Channel resolution enumerates the published RC tags for the selected
Project Release Namespace, including preserved unqualified historical cuts
during a namespace transition, selects the greatest positive ordinal,
requires that cut and the current selector to be annotated tags peeling to
the same commit, and fails closed when the selector lags or points
elsewhere. Channel adoption also refuses a same-line target whose ordinal
is below the Product Definition's current exact basis. A consumer that
intentionally retains an older cut names that immutable RC URI and digest
explicitly and uses exact-basis operations such as `sync`; it does not
express that choice through the latest-version channel (P5, P6).

Presentation and mutation are separate invocations. The read-only plan,
the Adoption Plan of PRODUCT_DEFINITION §4, binds the current Product
Definition bytes and basis to the target immutable cut, annotated tag
object, peeled commit, tree and installed-manifest digest, then emits a
deterministic plan digest. Mutation requires that exact digest as the
operator's acceptance and re-derives it before changing any Product
Definition. Selector, target, manifest or definition drift invalidates the
acceptance. A fleet uses the same law with one aggregate digest over all
exact per-definition plans. Planning inside a mutating invocation is not
external presentation and cannot authorise itself. The plan's hashing rule
and the manager's command boundaries are PRODUCT_DEFINITION §4 (P6, P3).

This split lets operators refer to `v<version>` for the latest published
RC without repeatedly incrementing the version line, while every governed
project retains reproducible exact-cut authority and changes only through
explicit adoption (P2, P3, P6).
```

Successor, `PRODUCT_DEFINITION.md#4-shared-installed-release-basis-and-toolchain-manager`:

```text
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

Outcomes as results. The outcomes of the manager's operations in §4,
its refusals, its reported completion and the recovery that
loss requires, are stated in the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) through the refinements
of [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), each
for its own predicate; the cause of an outcome selects its value, and the
mapping adds no core value (P5, P6):

- Effect. An operation that writes, such as `install`, `sync`, a mutating
  `adopt`, fleet adoption or the complete consumer update, has an
  intended external effect, recorded under
  [ACTIVATION §3 Effects](ACTIVATION.md#effects) for the predicate "the
  intended effect occurred". Reported completion is `completed`
  (`satisfied`) only where evidence about the subject establishes the
  effect in full, as the complete update's verification of every
  selected resulting binding and companion does. The cause selects the
  other values. A refusal before any effect, with the retained prior
  state as the evidence about the subject, is `not_effected`
  (`falsified`), and the effect has ended. A caught application failure
  is also `not_effected` (`falsified`): the failure observed on the
  subject establishes that the complete update is not attained, and the
  operation applies no later part of it, so no later completion of this
  effect can attain it. Whether its restored preimages are verified
  decides only whether the effect's end is established, never the value:
  verified, the effect has ended; a restoration not verified, or rollback
  storage unavailable after the failure, leaves the end not established,
  recorded beside the value as a residual naming the verification that
  would establish it. Newly staged immutable installs left unused are
  named with the value as the part that did occur. Abrupt process or
  host loss, where no caught failure establishes that the update fell
  short, is `completion_unknown` (`indeterminate`), never `completed` or
  `not_effected`. `completion_unknown`, and `not_effected` with its end
  not established, are effects of uncertain completion under
  [ACTIVATION §3 Effects](ACTIVATION.md#effects): recovery from the
  presented preimages reconciles them, as
  [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) states, before
  any repetition or claim of the complete relation.
- Refusal. A refusal also answers whether the operation may apply its
  effect on the exact subject and basis it binds. Found before the
  operation begins, it is an outcome of
  [ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation),
  for "the step is lawfully admitted and activated on the exact subject
  and basis"; found after it has begun, as by the recheck after immutable
  staging, it is a value of
  [construction availability](ACTIVATION.md#construction-availability),
  for "a candidate is available". A missing explicit acceptance of the
  exact plan, or missing whole-selection authorisation of a fleet write,
  is missing operation authority: `admission_refused(authority)`
  (`out_of_frame`), naming the acceptance or authorisation needed and
  its owner. Every other refusal has a basis cause: drift of the Product
  Definition bytes or of a consumer preimage; a stale plan; each other
  condition of the fail-closed list above, ambiguous discovery included
  because it leaves no exact subject; a path, locator or marker span that
  escapes or breaks its boundary; and missing, ambiguous, changed or
  unavailable derived-context evidence, which holds the complete update.
  It is `admission_refused(basis)` before the operation begins and
  `re_entry_requested(basis)` after, `invalid_basis` in both, and names
  the basis coordinate that fails and, for derived-context evidence, the
  source owner whose re-entry repairs it.
- Command without an intended effect. A command without an intended
  external effect, such as `verify` or `adopt --dry-run`, has no value
  under Effects, and its refusal maps by cause as above. A condition it
  reports about the subject it evaluates, such as a member that `verify`
  finds missing, extra or changed, is a counterexample to that command's
  own predicate, `falsified`, not a refusal.

Purpose and material relation: a consumer that combines the manager's
outcomes with other results cannot read a refused or failed operation as
completed, an operation whose value is `completion_unknown` as either
completed or not effected, a caught failure whose restoration is not
verified as undecided when the update is known to have fallen short, or
a refusal for missing acceptance as one for a defective basis (P5, P6).
This mapping is new in this corpus.
```


### Row `RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015` at rc.2:

```text
## Successor Baseline Conservation (`STDO-UP-015`)

A successor identifies the exact predecessor immutable RC whose semantic claims
it evolves. That origin remains immutable for the candidate. Every predecessor
claim capable of affecting the successor receives one semantic disposition:

- **conserved** — the successor retains the claim;
- **superseded** — an accepted successor relation replaces it;
- **intentionally removed** — current Product authority removes it; or
- **not applicable** — it has no successor effect, with a bounded reason.

An unresolved disposition blocks qualification of the affected claim.
Conservation is semantic: patch absence does not prove loss when a
successor-native realization preserves behavior, and naming or code similarity
does not prove conservation without relevant evidence.

Where a maintenance or support line may affect retained claims, the release
basis identifies the watched source, observation boundary, inclusion policy,
and successor candidate. Relevant changes receive semantic disposition at
material integration and exact-cut qualification. The consumer owns its record,
branch strategy, comparison, and proof mechanism.
```

Successor, `RELEASE.md#9-successor-baseline-conservation-stdo-up-015`:

```text
## 9. Successor baseline conservation (STDO-UP-015)

A successor identifies the exact predecessor immutable RC whose semantic
claims it evolves. That origin remains immutable for the candidate. Every
predecessor claim capable of affecting the successor receives one semantic
disposition (P4b, P3, P6;
rc.2 #successor-baseline-conservation-stdo-up-015):

- conserved: the successor retains the claim;
- superseded: an accepted successor relation replaces it;
- intentionally removed: current Product authority removes it; or
- not applicable: it has no successor effect, with a bounded reason.

Evidence for a disposition is retained or reassessed under
[FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse):
a `conserved` reading made on an earlier successor text applies to a later
one only where the owning text and the consumer bindings that carry it
are unchanged, or the change is shown not to affect the claim (P3, P6).

An unresolved disposition blocks qualification of the affected claim.
Conservation is semantic: patch absence does not prove loss when a
successor-native realisation preserves behaviour, and naming or code
similarity does not prove conservation without relevant evidence (P6,
P1). The comparison that decides `conserved` is made on the same material
case, scope and authority: what must happen, what may happen, what is
prohibited, and what follows when a trigger, exception or required
premise is absent, in the owning text and in the consumer bindings that
apply it, with the counterexamples that would expose a changed decision.
Modal wording is judged by that meaning: indicative wording can state a
binding law, and rewriting "must" or "shall" is neither conservation nor
supersession by itself; an obligation stays obligatory, a preference
stays a preference, and every permitted exception and scope condition
survives, or the claim is not conserved. A statement that a whole
package's wording is equivalent establishes none of this for any claim
(P6, P1; the common successor disposition requirement, carried here as
the test this section applies). A `conserved` disposition recorded
before this test applied is re-evaluated under it before the affected
claim qualifies; until then its standing is `unresolved`.

Each disposition is a claim the successor makes about one predecessor
claim ([EVALUATION §1](EVALUATION.md#1-claims)), not a result value; its
predicate is its value's wording above. It is distinct from the decision
owner's disposition of an assessed candidate
([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)), which is an
acceptance result. Qualification evaluates each
disposition on evidence and records a value of the core result algebra
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) with that predicate.
An unresolved disposition states no claim and so has no result: in the
qualification of the affected claim it is a planned assessment without a
closed result, which is why it blocks that qualification
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps). Purpose and material relation: a recorded disposition establishes
nothing until it is evaluated, so no disposition stands as a result (P6,
P5).

Where a maintenance or support line may affect retained claims, the
release basis identifies the watched source, observation boundary,
inclusion policy and successor candidate. Relevant changes receive
semantic disposition at material integration and exact-cut qualification.
The consumer owns its record, branch strategy, comparison and proof
mechanism (P4b, P6).

[EVALUATION §5](EVALUATION.md#5-acceptance) states what acceptance
requires of the disposition record; it applies this section and is not
part of it (P4b, P6).
```

Successor, `EVALUATION.md#5-acceptance`:

```text
## 5. Acceptance

Acceptance is the decision owner's disposition over an unchanged subject;
recording it cannot widen it, and it exhausts only the instance and interval
it names (P6, P2; conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013),
[AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation)).
A work item closes by the condition it stated, not by a reviewer's approval;
a reviewer result is an input to closure, never the closure. Green labels,
document counts, review counts and historical outcomes are not acceptance.
A human decision may be exercised directly or through an explicitly admitted
bounded proxy. What a proxy grant names is
[IDENTITY §6](IDENTITY.md#6-authority-identity-and-conservation-stdo-up-004)'s,
and what a proxy can never decide is
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds)';
for acceptance, a change a proxy cannot make re-enters at its owning
relation (provenance rc.2 IDENTITY_METHOD
#authority-identity-and-conservation-stdo-up-004 and
[UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)).

Where the subject is a successor, its acceptance evidence includes the
successor disposition record of [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)
(STDO-UP-015), which states the law: the exact predecessor immutable cut
the successor evolves, and one semantic disposition for every predecessor
claim capable of affecting the successor. A claim whose disposition is
unresolved cannot be qualified and so cannot be accepted; how the record
is evaluated is [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015).
An intentionally removed disposition is a decision of the current Product
authority, and its record is that decision (P6, P3, P4b).

### When a finding blocks promotion

A finding is a defect a review reports against the exact claim it
evaluated (§4). Blocking current promotion is the decision owner's act
over that finding (§4, Result and triage projection). This section is the
one statement of when a finding can block; profiles and work carriers
refer to it and add only their domain triggers.

A review verdict is bounded by the exact reviewed claim and its applicable
hard stops ([ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement)). A
finding can block current promotion only when it:

1. falsifies that claim;
2. exposes competing or ambiguous authority on the claim's acceptance
   path;
3. violates applicable active authority, safety or retained accepted
   behaviour; or
4. establishes a material architectural decision with durable
   consequences that forecloses an admitted Product outcome.

These conditions are necessary. Which of them suffice is decided as
follows:

| Consumed condition | Effect on the current promotion boundary |
|---|---|
| a valid falsification of a mandatory claim governed by a non-waivable hard stop | the boundary blocks, whatever the assigned priority or the decision cutoff |
| any other finding meeting one of the four conditions | the decision owner decides blocking from the exact affected claim, the governed outcome or decision the work serves ([ACTIVATION §1, Intake](ACTIVATION.md#intake)), the applicable hard stops and the Product-owned cutoff policy; below that cutoff no block follows mechanically, and an accepted residual is retained explicitly |
| a finding meeting none of the four conditions | it does not block |
| an observation outside the exact reviewed claim | repricing or re-entry input, returned as §4 states: by itself it does not widen the reviewed subject, block its bounded claim, or require a new ticket, artifact, review round or implementation increment |

Severity selects neither priority nor a block mechanically, and priority
neither erases severity nor waives a hard stop. The decision cutoff is the
adopting Product's policy; this member sets no cutoff (P6, P2; conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)'s
blocking conditions). The table is new tier-1 law: it states for the
decision owner of any promotion boundary the rule that the predecessor's
[Executive promotion constraint projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-promotion-constraint-projection)
states for the Executive only, which
[EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md#promotion-constraint-projection)
keeps as its instance. Purpose and material
relation: the method stated these conditions in a work carrier, a design
profile and the Executive profile, so an actor reconciled three texts; one
statement gives every review consumer the same answer, and the conditions
keep a bounded review from blocking on observations outside its claim
while a non-waivable hard stop still blocks.
```


### Row `RELEASE_METHOD.md#two-commit-construction-and-one-publication-transaction` (disposition `conserved`)

Predecessor, `RELEASE_METHOD.md#two-commit-construction-and-one-publication-transaction` at rc.2:

```text
### Two-Commit Construction And One Publication Transaction

Exact installed-manifest identity includes the annotated STDO tag object, so a
same-commit carrier containing both that identity and derived child bytes would
be self-referential. A coordinated STDO cohort therefore uses this bounded
two-commit construction:

1. commit A freezes the exact STDO corpus, plugin, release record, and their
   qualification bytes;
2. the annotated STDO cut tag is created locally over commit A but is not
   pushed;
3. that exact local cut is installed and verified, producing the manifest
   identity used by every derived Product and index;
4. the Axiom Indexer, STDO Representation, semantic-index bytes, and cohort
   record are derived and frozen in commit B;
5. prepublication qualification evaluates commit B against the exact local
   STDO tag before child immutable tags are created;
6. annotated child cut tags and every Product-local RC branch, version-line
   selector, and optional release branch are prepared locally; and
7. a mandatory post-tag, pre-push gate re-runs qualification over every local
   annotated tag object and peel, selector, RC and release branch, normalized
   version mapping, target commit, and the exact closed ref set; it also fetches
   and binds the expected remote object ID or required absence for every
   destination ref; and
8. one transport transaction atomically publishes only that qualified carrier
   branch and
   complete Product ref set.

If the remote does not support atomic ref publication, publication refuses.
The process has no sequential-push fallback. Every immutable cut tag is
create-only and therefore requires bound remote absence. Every mutable carrier,
RC branch, selector, and release branch uses an explicit per-ref
compare-and-swap lease, such as `--force-with-lease=<ref>:<expected-oid>`, in
that same atomic transaction. A missing expected ref, unexpected existing tag,
or changed remote object ID stops publication; the operator refetches and
repeats complete content and local-ref-graph qualification before constructing
another push. A lease mismatch never falls back to an unguarded force, a
partial push, or an in-place expectation update.

Remote verification fails closed when any required cohort ref is absent,
lightweight, differently versioned, points to the wrong Product commit, or has
a selector or release branch that does not match its immutable cut.
Post-publication bookkeeping may use a later commit, but it cannot move any
immutable cohort tag.
```

Successor, `RELEASE.md#two-commit-construction-and-one-publication-transaction`:

```text
### Two-commit construction and one publication transaction

Exact installed-manifest identity includes the annotated STDO tag object,
so a same-commit carrier containing both that identity and derived child
bytes would be self-referential. A coordinated STDO cohort therefore uses
this bounded two-commit construction (P3, P5;
rc.2 #two-commit-construction-and-one-publication-transaction):

1. commit A freezes the exact STDO corpus, plugin, release record and
   their qualification bytes;
2. the annotated STDO cut tag is created locally over commit A but is not
   pushed;
3. that exact local cut is installed and verified, producing the manifest
   identity used by every derived Product and index;
4. the Axiom Indexer, STDO Representation, semantic-index bytes and cohort
   record are derived and frozen in commit B;
5. prepublication qualification evaluates commit B against the exact
   local STDO tag before child immutable tags are created;
6. annotated child cut tags and every Product-local RC branch,
   version-line selector and optional release branch are prepared
   locally;
7. a mandatory post-tag, pre-push gate re-runs qualification over every
   local annotated tag object and peel, selector, RC and release branch,
   normalised version mapping, target commit and the exact closed ref
   set; it also fetches and binds the expected remote object ID or
   required absence for every destination ref; and
8. one transport transaction atomically publishes only that qualified
   carrier branch and complete Product ref set.

If the remote does not support atomic ref publication, publication
refuses. The process has no sequential-push fallback. Every immutable cut
tag is create-only and therefore requires bound remote absence. Every
mutable carrier, RC branch, selector and release branch uses an explicit
per-ref compare-and-swap lease, such as
`--force-with-lease=<ref>:<expected-oid>`, in that same atomic
transaction. A missing expected ref, unexpected existing tag or changed
remote object ID stops publication; the operator refetches and repeats
complete content and local-ref-graph qualification before constructing
another push. A lease mismatch never falls back to an unguarded force, a
partial push or an in-place expectation update (P5, P3).

Remote verification fails closed when any required cohort ref is absent,
lightweight, differently versioned, points to the wrong Product commit, or
has a selector or release branch that does not match its immutable cut.
Post-publication bookkeeping may use a later commit, but it cannot move
any immutable cohort tag (P5, P3).
```
