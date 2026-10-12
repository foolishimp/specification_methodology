# EXECUTIVE_BASELINE

Tier 3. An optional profile that maps three engagement frames (Executive,
Worker, Reviewer) and a catalogue of specialist frames onto the law of
tiers 1 and 2. It imports [FOUNDATIONS](FOUNDATIONS.md),
[REFERENCE_FRAME](REFERENCE_FRAME.md), [ACTIVATION](ACTIVATION.md),
[EVALUATION](EVALUATION.md), [SPEC_METHOD](SPEC_METHOD.md),
[PRODUCT_DEFINITION](PRODUCT_DEFINITION.md) and
[ASSURANCE](ASSURANCE.md) by reference and defines none of their objects
again: the frame, frame set, activation packet and method functions are
REFERENCE_FRAME's; intake, admission, applicability, the one result
algebra and the four dispositions are ACTIVATION §1 and §3; the
independent-assessment protocol and the review-result shape, including the
result and triage projection, are EVALUATION §3 and §4; the product
testing frames, testing value, path erasure, subject acquisition,
counterexample localisation and the interface integration frame are
ASSURANCE §7 to §13. Every clause names the principle that requires it (P0
to P6, FOUNDATIONS §3). A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md`
and is provenance only; every predecessor row received here is restated in
this text, and nothing here depends on that cut to be applied.

Role names used here bind the tier-1 roles of ACTIVATION §1: Worker is the
constructor, Reviewer the assessor, Executive the coordinating role that
acts as decision owner or its admitted proxy (P1: a label is bound to the
relation it names, not imported by spelling).

## 1. Canonical compression

REFERENCE_FRAME defines the finite engagement unit. The selected complete
method cut defines specification, design, construction, assessment,
disposition, checkpoint, continuation, identity and release law. This
profile maps three practical engagement frames onto those owners and adds
no owner of its own (P6, P0; rc.2 #canonical-compression):

```text
existing project authority
  + selected complete method basis, REFERENCE_FRAME included
  + exact governed Product or Product-chain outcome and workspace basis
  + known evaluation inventory, dependencies and residuals
  -> a sufficient direct Worker activation, or coordination where material
  -> when coordinated: Executive locks outcome and basis, holds a finite ready frontier
  -> Worker and the applicable specialist evaluations; Reviewer only where required
  -> closed results, technical triage where applicable, declared conjunction
  -> existing bounded decision authority, result recording, next lawful action
  -> updated basis, coverage, residuals and frontier
  -> repeat or stop
```

The three frames are overlapping evaluation contexts. They are neither a
hierarchy nor an actor topology (P6; RF-009). The Worker supplies the
candidate and never activates the Reviewer. The Reviewer evaluates and does
not implement. The Executive applies only decision authority already
granted by Product, Goals, requirements, accepted design, a ticket, identity
law or release law. The Worker carries only the construction or
transformation authority of its admitted intake. No frame acquires
admission, publication, mutation or any other operation authority from its
label (P6).

The profile derives twelve generic specialist-frame families (§11):
Product, Product Composition, Design, Design Component, Public Boundary,
Entity, Operator, Owner, Effect, Reuse/Foundation, Install and Proof. They
keep apart recurring evaluation questions that otherwise collapse across
constitutional WHAT, structural HOW, identity, authority, effects,
foundations, installed subjects and evidence. They are available families,
not mandatory actors, stages, components, services, files or runtime types.
An activation selects only the families material to its exact evaluation
and keeps an explicit residual for any material family it cannot cover (P2,
P1).

The four product testing frames (user acceptance, end to end, integration,
unit) are tier-2 law in ASSURANCE §7. Under this profile they are activated
inside the same conditionally selected engagement relation; they add no
role, stage, authority or testing hierarchy. Their evidence topology, the
assignment of claims to congruent evidence frames, is ASSURANCE §7; a
broader frame cannot make a module-owned law true, and any number of
narrower green frames cannot establish an unevaluated Product composition
or user outcome (P6, P4a).

A project may adopt this profile or define another frame configuration
(§16). The choice is admitted by the existing project authority that owns
the affected decision. A local axioms file may carry the decision; carrying
it does not make the file a new constitutional owner (P6).

## 2. Status and authority boundary

This member is an optional derived role and evaluation profile. It owns no
part of the execution protocol and no Product binding (P6; rc.2
#status-and-authority-boundary). Three ownership layers stay distinct:
REFERENCE_FRAME owns the pure frame principles; this member owns the
optional Executive, Worker, Reviewer and specialist mappings; PRODUCT_DEFINITION
§7 owns the Product-binding relation, and each adopting Product's authority
owns its concrete Project Reference-Frame Basis. The testing-frame
mappings this profile uses are ASSURANCE's.

| Relation | Owner in this method | Use in this profile |
|---|---|---|
| frame declaration, activation, result algebra, conjunction, translation, coverage and revision | REFERENCE_FRAME; ACTIVATION §1 and §3 | defines each engagement frame and the active configuration |
| bounded-frame conservation and execution intake | ACTIVATION §1 Intake, consuming the design profile's bounded-frame conservation laws ([DESIGN_MODULE](DESIGN_MODULE.md)) | supplies the Worker activation basis |
| construction, self-review, assessment, disposition, checkpoint and continuation | ACTIVATION §1, §3 and §5 | supplies the complete execution transition |
| constructor and independent-assessor separation | EVALUATION §3 | supplies Reviewer independence and traceability of the exact verdict |
| exact assurance subject, evidence population and freeze for generic method qualification | EVALUATION §1, §3 and §7 | supplies review-boundary and qualification constraints |
| module-derived unit proof | the design profile's design-to-module evidence route and module-derived unit-test law ([ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route) and [§15](ASSURANCE.md#15-module-derived-unit-tests)) | supplies the unit frame's module-ownership basis, while ASSURANCE §7 limits its claim and evidence altitude |
| capability and foundation selection before material generic construction | the design profile's capability-and-foundation selection law ([DESIGN_MODULE](DESIGN_MODULE.md)) | supplies the Worker's proportional reuse comparison; reuse is no authority transfer, and an assigned foundation role keeps its declared relation and owner |
| Product testing taxonomy, claim, ordinary user path and acceptance meaning | ASSURANCE §1 to §3 and §7; the current Product, requirements, accepted design and release authority where applicable | selects user outcomes, supported interfaces, material compositions, runnable Product subjects, harnessed or live mode and required testing populations |
| the twelve generic families | current Product and requirements; SPEC_METHOD composition law; accepted design; the design profile; identity and release law ([IDENTITY](IDENTITY.md), [RELEASE](RELEASE.md)); applicable domain, effect, interface, dependency and assurance owners | supplies recurring specialist evaluation families without moving their owners or requiring one architecture |
| work selection and growth authority | current Goals, Product, requirements and an admitted ticket or equivalent work authority | selects the governed outcome and admits the local frame configuration |
| design structure and local realisation frame decisions | accepted design under its governing Product and requirements | supplies specialist frames and material relations |
| human and proxy identity | identity law ([IDENTITY](IDENTITY.md)) with project authority; EVALUATION §5 for the proxy grant | binds the Executive actor and its decision envelope |
| Product and release acceptance | the current Product and release law ([RELEASE](RELEASE.md)); EVALUATION §5 | keeps direct acceptance where those owners require it |

Every requirement of this profile is one of two kinds: an exact
application of a cited owning relation, or a condition for claiming
adoption of this optional profile. Neither kind opens a second amendment
path for the owning law. Where this profile conflicts with an owning
clause, the owning clause controls and this profile requires revision (P6).

Inclusion in an exact released cut or another admitted method basis makes
the profile available; it does not adopt it. Adoption requires a separately
accepted Product-owned Project Reference-Frame Basis (PRODUCT_DEFINITION
§7). Mutable authoring source, the presence of an installed file, prompts,
summaries and commentary neither select nor adopt it (P6, P3).

## 3. Engagement applicability

Direct entry, and the coordination that activates when it cannot cover
the material contexts, authority, capability or required independence, are
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation);
here the directly entering role is Worker (Writer) and the coordinating
role Executive. A role or frame name alone creates no review obligation
either (P0, P6; rc.2 #engagement-applicability).

This profile adds to direct entry (P2, P6):

- the direct route binds the same exact intake, operation territory,
  applicable obligations, evidence, stop conditions and declared result
  consumer as the coordinated route;
- it uses the smallest existing carrier (carrier selection is tier-2 law,
  ACTIVATION §1 Admission), and admission stays distinct from drafting;
- a sufficient local outcome with no required independent assessment and
  no reserved acceptance may finish as Writer and record its satisfied
  conditions in that carrier; it gains no review, ticket, diagram
  recreation or owner ceremony from using this profile;
- any required assessment or owner decision stays required; an
  insufficiency discovered during the work withholds the dependent effect
  and returns the affected question to its existing owner.

The transition of §12 and the handoffs of §13 apply when the coordinated
branch is selected. Direct work returns its closed result to the declared
work authority or existing result carrier, with the same result algebra
(ACTIVATION §3) and the same separation of operation from decision. In
either branch, applicability is ACTIVATION §1 (Applicability), and valid
computed facts, judgments and owner rulings (C/J/O) are reused under
ACTIVATION §7. No route alters a Product's exact adopted basis or supplies
missing authority (P6, P4b).

## 4. Empirical revision boundary

Accumulated delivery practice and observed failure may inform frame
selection, qualification and revision. That evidence does not become method
authority, and it imports none of the originating consumer's architecture,
names, actors, topology, runtime, artifacts or work stages into this
generic profile (P6, P2; rc.2 #empirical-revision-boundary).

The engagement relation of this profile requires (P0, P6):

- one bounded authority selects the active work and the finite frames
  needed to evaluate it;
- a Worker constructs one exact candidate, self-reviews, reports and stops;
- where independent assessment is required, a separately activated
  Reviewer acquires sufficient exact live authority, subject and evidence,
  reusing valid computed facts while supplying its own judgment;
- an activated Reviewer returns evidence-bound severity and technical
  implications without becoming a second implementation loop;
- where coordination is required, the Executive assigns priority and
  adjudicates the current Product mandate under an existing bounded grant;
  and
- inability to perceive a known violation is evidence of a missing,
  misactivated, oversized or capability-incompatible frame (RF-014).

Repeated resets, long repair loops, moving review subjects, proof masking
and duplicated authority are generic signals that a frame declaration,
activation, capability match, basis or authority relation may be defective
(REFERENCE_FRAME §10, missing-frame signals). They justify re-evaluation;
they neither identify one universal architecture nor give a precedent
semantic authority (P6, P5).

Repeated Product drift is read the same way: a useful implementation,
specialisation, scenario, dependency, installed builder or downstream
Product does not become the Product being authored because it is visible to
the same actor or takes part in one delivery chain (P3, P2).

## 5. Profile terms

### Engagement frame

An engagement frame is a frame (REFERENCE_FRAME §1) whose evaluation family
concerns selecting, constructing, assessing or disposing governed work.
Executive, Worker and Reviewer are this profile's engagement frames (P1;
rc.2 #engagement-frame).

### Specialist frame

A specialist frame is an activated Product, requirement, design, identity,
release, domain, implementation, test, operational, historical or
capability frame that one engagement evaluation needs. A method member,
file, component or lens becomes a frame only when its evaluation, basis,
material manifold, authority, evidence, result algebra and capability
envelope are declared (REFERENCE_FRAME §13, minimal frame declaration; P1,
P6; rc.2 #specialist-frame).

### Generic specialist-frame family

A generic specialist-frame family is a reusable evaluation-family archetype
of this profile (§11). It names a recurring distinction that a project
either instantiates where material, has capable authority establish as
non-material for the governed outcome, or keeps as an explicit coverage
residual (P2, P6; rc.2 #generic-specialist-frame-family).

A family selects no concrete carrier, component, actor, architecture, owner
or implementation. One project may instantiate several frames in one
family. One declared frame may cover several families only when its
evaluation and result relations preserve every material distinction instead
of flattening them behind one broad label (P1, RF-008).

### Terms owned by ASSURANCE

Testing frame, authoritative Product path and material combinatorial
complexity are tier-2 terms defined in ASSURANCE §7. This profile uses them
as defined there and adds nothing to them (P1; rc.2 #testing-frame,
#authoritative-product-path, #material-combinatorial-complexity).

### Executive

Executive is this profile's label for the frame that selects or confirms
the bounded activation configuration and consumes closed Worker and
Reviewer results under existing project decision authority. It holds the
complete Product view and the current MVP or release mandate needed to
assign priority, apply disposition and select the next authorised action
(P6, P2; rc.2 #executive).

The frame may be occupied by direct human authority or by a bounded proxy
admitted under the proxy grant of EVALUATION §5, ACTIVATION §1 (Roles and
delegation), identity law and current project authority. It is not a
universal semantic owner, controller, manager service or runtime executive
observer (P6, RF-016).

### Worker

Worker is this profile's label for the constructor role of ACTIVATION §1
activated as a frame. It owns construction and self-review inside its exact
intake, through the operation authority inherited from the governing work
relation. It acquires no admission, publication, acceptance or continuation
authority (P6; rc.2 #worker).

### Reviewer

Reviewer is this profile's label for the independent live-surface
evaluation that the assessment relation of ACTIVATION §1 consumes, governed
by EVALUATION §3 (independence and traceability) and EVALUATION §1 and §7
(assurance boundary and qualification freeze), activated as a frame. It
evaluates one exact subject and returns a closed result, with evidence-bound
technical triage when a finding exists. It does not implement the repair,
assign priority, apply disposition or activate the next frame (P6; rc.2
#reviewer).

### Technical triage, severity, priority and boundary effect

Technical triage is the Reviewer's assessment of one finding against the
exact evaluated claim and basis. Where admissible evidence and the actor's
capability envelope support it, the triage records (P6, P5; rc.2
#technical-triage-severity-priority-and-boundary-effect):

- the affected claim and the observed failure;
- severity on the Product-selected severity scale;
- causal assessment and confidence;
- blast radius and the affected users, paths or relations;
- an available workaround or containment;
- repair complexity, regression risk and material dependencies; and
- residual uncertainty and the evidence that would reduce it.

Missing causal or repair evidence stays explicit. Where the missing
relation can change the evaluation, the Reviewer returns `indeterminate` or
`out_of_frame` pressure (ACTIVATION §3); it does not invent precision and
does not send work sideways to the Worker (P5).

Severity grades the consequence if the finding manifests. Priority orders
the response relative to the complete Product outcome, likelihood and
exposure, the current MVP or release mandate, reversibility, dependencies,
cost of delay and available capacity. The Reviewer grades severity; the
Executive assigns priority (P6, P2).

The Product-owned Project Reference-Frame Basis binds the severity scale,
the priority scale, the current-boundary decision cutoff and the
non-waivable hard stops. This profile imposes no universal numeric scale.
Severity, priority, the frame result (ACTIVATION §3) and the
current-boundary effect are four distinct values; none of them alone makes
a finding release-blocking (P6, P1).

Current-boundary effect is the Executive's determination that a finding
blocks the current promotion boundary, requires narrowing, or may remain an
explicit residual. The Executive then applies exactly one existing
disposition (ACTIVATION §3, Disposition). A hard stop or a falsified
mandatory claim cannot be waived by lowering priority. An observation
outside the exact claim boundary cannot open another review round because
it carries a severe label (P6, P2). How each result member projects the
triage payload and constrains its consumption is EVALUATION §4 (Result and
triage projection).

### Work result

A work result is the Worker's closed output to its declared consumer; in
the coordinated branch that consumer is the Executive. It exists only after
a successful Worker activation. An `activation_refusal` (REFERENCE_FRAME
§5) returns to the assigning authority or declared result carrier and
creates neither a Worker activation nor a Worker result (P5, P6; rc.2
#work-result).

The variants `candidate_ready`, `refused`, `incomplete` and
`re_entry_requested` are the construction availability refinement of
ACTIVATION §3, which defines their total mapping to the core algebra. In
this profile they are carriers, not new semantic dispositions, and each
variant has this reading (P5):

- `candidate_ready` (with `satisfied`): an exact candidate and its
  transition evidence are available;
- `refused` (with `falsified`): lawful activation occurred, and a governing
  prohibition or an owner-valid construction refusal defeats the requested
  construction;
- `incomplete` (with `indeterminate`): the valid activation produced no
  candidate because admissible evidence or bounded execution cannot yet
  decide or complete the relation; and
- `re_entry_requested` (with `out_of_frame` or `invalid_basis`): a material
  decision lies outside Worker authority, or the activated basis can no
  longer support the work.

The mapping is total and exclusive after lawful activation. Payload
wording, stop timing or actor preference cannot select another variant. A
capability, authority, stale-basis, ambiguous-basis or topology mismatch
known during activation is an `activation_refusal`, never a synthetic
Worker result (P5, P6). Consumers choose the representation; ACTIVATION §1
and §3 stay the owners of the execution relation and its dispositions.

The result references the current computed classification, supporting
evidence, residual judgments and original rulings through their existing
carriers. It does not reconstruct unchanged C/J/O at each handoff. The
consumer checks applicability and concrete invalidators; changed evidence
revises only the affected results, preserving originals and supported
surviving claims (ACTIVATION §7; P4b).

### Exact candidate

An exact candidate is the subject identity that the transition evidence of
ACTIVATION §7 and the traceability of EVALUATION §3 require. Where generic
method qualification applies (EVALUATION §7), its construction result is
frozen before material reference exposure as that clause requires.
Elsewhere this profile stabilises the review subject through an immutable
identity or an equivalent exact-subject relation sufficient for the claimed
assessment. The profile creates no new lifecycle state named `frozen` (P3,
P6; rc.2 #exact-candidate).

### Baseline-adoption projection

A baseline-adoption projection consumes the Product-owned Project
Reference-Frame Basis of PRODUCT_DEFINITION §7. Where that basis adopts
this profile, the projection records the selected profile mapping, exact
outcome, actor envelopes, evidence coordinates and revision conditions
needed in addition to the Product binding (§16). It is not a second
frame-basis definition and mints none of the authority it projects (P6;
rc.2 #baseline-adoption-projection).

## 6. Executive attention, evaluation and action

### The three duties

The Executive is the frame for three inseparable duties over one governed
outcome (P0, P6, P2; rc.2 #executive-attention-evaluation-and-action):

1. attention management: it keeps the exact outcome and basis, the
   Product-role map, the evaluation inventory, the dependency relation, the
   unresolved frontier, the actor envelopes, the current MVP or release
   mandate, the applicable triage policy and the residual boundary, and it
   selects the smallest dependency-ready activation set sufficient for the
   next decision within the finite actor envelopes;
2. evaluation orchestration: it activates capable Workers, Reviewers or
   specialists, keeps their exact subjects and bases, and consumes only
   closed results or declared translations; and
3. authorised action selection: it assigns priority, determines the effect
   on the current promotion boundary, applies an existing disposition, and
   issues only the next already-authorised activation or action.

The Executive does not contain the complete workspace and does not perform
every evaluation. It acquires no Product meaning, implementation, mutation,
acceptance, publication or other operation authority from the role. A
material effect stays owned by the actor that carries its exact operation
grant (P6, RF-002).

### No mutation while Executive

An actor occupying the Executive frame modifies no candidate, Product or
worktree bytes and performs no implementation effect. Filesystem or tool
access is no exception, and neither is an edit that is small, test-only,
reversible or apparently obvious. Mutation requires a separately activated
Worker or Writer relation carrying the exact operation grant, subject and
write territory. A same-actor role transition is explicit and is recorded in
the existing work carrier before the effect; for that effect the actor is no
longer acting as Executive. Recording or delegating after an Executive edit
cannot authorise the edit retroactively (P6, P3; ACTIVATION §1, the
coordinating role mutates nothing).

### Attention cycle

```text
U0 = every known material evaluation not closed on the current basis

while U is non-empty:
  select a finite dependency-ready subset M that fits the assigned actors
  activate each member of M against the exact outcome and basis
  keep assurance-independent evaluations free of unclosed peer results
  when no other authorised decision is ready:
    await decision-relevant input (event-driven attention, below)
  record every closed result, technical triage, residual and invalidation condition
  apply only declared conjunctions or translations
  assign priority and boundary effect only under the current Product mandate
  invalidate affected results when the subject or basis changes
  update U from coverage, dependencies, conflicts and discovered materiality

stop only when every mandatory evaluation is closed, or governing authority
has explicitly retained every remaining residual consistently with the claim
```

The cycle needs no scheduler and no frame engine (RF-016). `M` may hold
parallel activations. Recursion follows declared evaluation dependencies and
bounded refinements; it does not nest or join undifferentiated copies of
every frame. The Executive holds the frontier and the closed-result ledger
in attention, not the undocumented working context of every evaluator (P0,
P4b, P2).

Severity supplied by the Reviewer is evaluation evidence. Priority,
current-boundary effect, disposition and the next action are Executive
decisions. They stay distinct ledger entries even where a Product-defined
policy maps one to another (P6, RF-007).

Every result returns to the Executive, to a declared conjunction or to
another frame through an explicit declared relation. No lateral handoff,
child completion, model response, tool output or shared actor implicitly
activates another frame or authorises continuation. A consumer receives the
closed result and its source routes, not the child's hidden reasoning
context (P6, P4a; ACTIVATION §7).

### Event-driven attention

Executive attention is event-driven by default. The Executive re-enters the
attention cycle for a decision-relevant closed result, a material exception
or changed basis, an owner request, or a declared deadline or checkpoint.
While Workers carry out their bounded grants and no other authorised
decision is ready, it waits. It does not repeatedly inspect unfinished work,
replay unchanged judgments or request status without a decision need (P0,
P2; rc.2 #event-driven-executive-attention).

It keeps the frontier, the return conditions and the valid evidence and
judgments. It refreshes affected support when a material observation
changes its basis, and revalidates the drift locks (below) before activation
and before disposition. Waiting waives no current-workspace verification,
evidence validity, required independent assessment, closed-result
consumption, or authority or closure duty (P6, P4b).

Where notification is unavailable or unreliable, or an actual supervision
obligation requires observation, the Executive uses bounded fallback
observation with a declared purpose, cadence or checkpoint, evidence target,
and stop or escalation condition. Silence proves neither progress nor
failure. A genuine blocker or material risk is investigated, with
intervention where required, within existing grants; unknown status alone
does not establish a stalled Worker (P5, P6).

Repeated no-progress observations, or returns with no new decision-relevant
evidence, require a bounded reassessment of the frame, grant, dependency or
evidence gap and a decision under existing authority. The Executive does not
keep polling or repeat the same repair on an unchanged basis (ACTIVATION §3,
Disposition). Reduced reasoning churn is not a lower-assurance path and is
no permission to reduce required actor capability; it introduces no
universal cost, budget or accounting gate (P2, P0; ACTIVATION §6).

### Drift locks

Before activation and before disposition, the Executive revalidates five
locks (P3, P6, P2; rc.2 #executive-drift-locks):

| Lock | Holds when |
|---|---|
| outcome lock | the selected Goal, Product outcome, boundary and lawful re-entry class, the current MVP or release mandate, and the triage policy are unchanged |
| basis lock | the subject, authority, dependency, configuration, topology, evidence, time and candidate coordinates are exact and current |
| Product-role lock | the mutable Source Project, Product Definition, Release Cut, Product, Install, Artifact and dependent Product identities stay distinct, and every Development Product role stays bound to its exact underlying Install |
| authority lock | the semantic, evaluation, operation, decision, acceptance and publication owners and grants are unchanged |
| coverage-and-return lock | every material evaluation and interaction is closed or an explicit residual, and every consumed result followed its declared return relation |

On a failed lock: changed Product meaning requires
re-entry. A stale or substituted basis is `invalid_basis`. Missing material
scope is `out_of_frame`. Missing operation authority refuses the activation
or the effect. An unresolved mandatory conflict prevents a satisfied
conjunction. The Executive repairs none of these by making its own frame
larger (P5, P6; ACTIVATION §3).

### Product-chain basis

A governed outcome may concern one Product or an explicit directed chain of
Products. Its basis records the distinct role of every mutable Source
Project, current Product Definition, exact candidate checkpoint, Release
Cut, Product, Install, Artifact, Development Product, dependent Product and
composition edge. Each Development Product role binds one exact underlying
Install identity. Each edge names its source and target roles, its governing
authority and contracts, its lifecycle, its evidence boundary, its refusal
and its invalidation (P3, P6; rc.2 #product-chain-basis; the Product-role
map in the basis is PRODUCT_DEFINITION §7, the lineage objects FOUNDATIONS
§2).

An installed Product may lawfully build its own successor or another
Product. That Development Product stays distinct from the mutable Source
Project and from the Product being authored. Directory nesting, shared code,
shared actors, source imports, tool reachability, matching labels or equal
outputs create no Product identity, composition edge or authority transfer
(P3, P1).

Exact basis does not make a Source Project immutable. A Worker may
cumulatively mutate the exact Source Project and write territory named by
its operation grant. A Reviewer evaluates an exact candidate checkpoint
produced from that workspace. A repair advances the workspace, creates a new
candidate and invalidates the affected results. A released Product, Release
Cut or exact Install stays immutable under its own lifecycle law and imposes
no immutability on the Source Project constructing a successor (P3, P4b).

## 7. Non-hierarchical frame configuration

The active configuration uses three distinct relation structures (P6,
RF-009; rc.2 #non-hierarchical-frame-configuration):

1. authority precedence decides which existing surface may select work,
   admit a frame configuration, dispose a result or require re-entry;
2. temporal and evidence flow carries activation packets and closed
   results; and
3. frame topology records disjointness, overlap, conjunction, translation
   or composition among the evaluations actually used (REFERENCE_FRAME §7),
   while evaluation independence and Reviewer assurance independence stay
   separate activation relations.

The three may coincide in one case. They are not one hierarchy (P6,
RF-009).

Executive, Worker and Reviewer commonly overlap on the selected method
basis, the governed outcome, the workspace checkpoint, the affected relation
set, the candidate, the evidence and the residuals. The overlap collapses
neither evaluation nor authority (P1, P6, RF-008): the Executive evaluates
activation, priority, boundary effect and disposition; the Worker evaluates
and performs bounded construction; the Reviewer evaluates the exact
candidate claim and supplies technical triage where assessment is activated.

The active evaluation may be represented as (P0, P4a):

```text
engagement frame
  + material specialist frame set
  + exact subject and basis
  + capable actor
  -> one activated evaluation
```

The notation needs no Cartesian-product schema and no universal frame
runtime (P2, RF-016).

## 8. Derived Executive frame

The Executive frame, in the shape of a frame declaration (REFERENCE_FRAME
§13; P6, P0; rc.2 #derived-executive-frame):

| Frame element | Executive |
|---|---|
| evaluation family | Is the bounded outcome and execution basis authorised? Which frames and actors are capable? Is a returned result exact and current? Which priority, current-boundary effect, disposition and next action follow from the current Product mandate? |
| subject and basis | the complete selected method cut; the exact Goals, Product, requirements, design and work authority; the current MVP or release mandate; the current workspace and checkpoint; open findings and their technical triage; the Product-selected triage policy; the proxy grant where one is used |
| material manifold | outcome, mandate, affected causal cone, evaluation inventory, frame configuration, actor envelopes, evidence obligations, returned results and technical triage, priority, boundary effect, re-entry owners and the boundary of already-authorised continuation |
| coordinates | exact method, project, outcome, mandate, authority, checkpoint, candidate, evidence, finding, triage-policy and actor identities |
| governing invariants | RF-001 to RF-017 (REFERENCE_FRAME §3); the execution relation and intake of ACTIVATION §1 with the design profile's bounded-frame conservation laws; applicable identity, carrier, assurance and release law |
| authority | the existing Product or work frame-set and decision authority, or its admitted bounded proxy; no operation or other authority arises from the label |
| evidence | live authority surfaces, frame results, Reviewer technical triage, exact candidate identity, transition evidence, coverage residuals and specialist results |
| capability envelope | enough method, Product, release or MVP, authority, workspace, triage and actor-selection competence to configure, prioritise and dispose the bounded evaluation; implementation expertise may be delegated to specialist frames |
| exclusions | candidate, Product or worktree byte mutation and implementation effects while occupying the frame; implementation ownership; silently rewriting Reviewer evidence or severity; claiming independent review without a qualifying activation; semantic reconstruction owned elsewhere; disposition outside the admitted grant |
| result | one core result (ACTIVATION §3), the assigned priority and current-boundary effect, and one existing disposition where the basis is decidable |
| invalidation | a material change of method, authority, outcome, mandate, triage policy, checkpoint, candidate, evidence, finding, capability or topology |

The frame adds no `authorize` or `no_action` disposition. Activation is the
`activate` function of REFERENCE_FRAME §5; candidate disposition stays
exactly `accept`, `local_repair`, `re_enter` or `reject` (ACTIVATION §3,
Disposition). Priority and current-boundary effect are decision
projections, neither core results nor dispositions. If the Executive cannot
rely on a supplied severity or technical assessment, it reactivates a
capable evaluation or keeps the uncertainty; it never silently rewrites the
Reviewer result (P5, P6).

### Steel-thread delivery

The Executive sequences delivery around a steel thread: the smallest real,
runnable path from a supported Product entry to a material outcome through
the selected composition. The path is established early and widened in
bounded increments; where it already exists, the affected thread is extended
or revalidated. Increments are chosen for consequential uncertainty,
dependency and interface reach, and failure impact (P2; rc.2
#steel-thread-delivery; the generic sequencing heuristic is SPEC_METHOD §8).

Early end-to-end and integration evidence prunes incompatible construction
choices before they spread; it settles the exercised interfaces, keeps
working composition, and concentrates construction on unresolved
obligations. Each passing thread establishes only the relations and
conditions actually exercised; untested branches, interaction combinations,
and refusal and recovery paths keep their material proof obligations.
Settled construction decisions are revisited when material counterevidence
invalidates their basis (P6, P4b).

During construction, focused deterministic regression and targeted
judgment probes resolve material uncertainty, and unit evidence covers
module-owned laws under the testing frames (ASSURANCE §7). Substantial,
resource-intensive user-acceptance cycles are scheduled near release or
when a bounded capability is complete enough to qualify; an early focused
user probe stays appropriate where it decides a material outcome
uncertainty (P2, ACTIVATION §7 proof cadence).

The product testing frames keep their distinct claims and govern the
necessary scenarios, independent assessments and repetitions. Qualified
results are reused while their exact subject and basis stay valid; affected
assurance is rerun when a material change invalidates it. The Executive
selects this sequence under the existing mandate and activates construction
only through the existing operation grants (P6, P4b).

## 9. Derived Worker frame

(P6, P0; rc.2 #derived-worker-frame)

| Frame element | Worker |
|---|---|
| evaluation family | Can the exact authorised outcome be constructed through the smallest coherent causal cone while preserving every affected governing relation and disposing of competing paths? |
| subject and basis | the sufficient execution intake of ACTIVATION §1, with the accepted design-to-execution basis of the design profile where it applies |
| material manifold | affected entities, lifecycles, transformations, authorities, capabilities, algorithms, inputs, outputs, dependencies, interaction seams, failure boundaries and proof obligations |
| coordinates | exact activation, source checkpoint, workspace, inputs, dependencies, configuration, actor envelope, outputs, candidate and evidence identities |
| governing invariants | the complete selected method and project relations material to the affected cone; ACTIVATION §1 owns construction and self-review |
| authority | inherited bounded construction or transformation authority and self-review only; mutation only where the exact inherited owner grant names the subject and write territory; no admission, publication, independent acceptance, frame-set revision or inferred next action |
| evidence | live implementation, tests and test source, analysis, generated artifacts, installed or operational behaviour where claimed, reconstruction, mutations and exact transition evidence |
| capability envelope | the declared method, domain, implementation, tool, access and finite-context competence the causal cone requires |
| exclusions | upstream semantic change, unauthorised cone expansion, self-acceptance, hidden competing paths, and advancing after returning the work result |
| result | one core result (ACTIVATION §3) and exactly one work-result variant (§5) |
| invalidation | a material change of intake, basis, checkpoint, dependency, configuration, capability or topology |

`candidate_ready` binds the exact candidate and the transition evidence of
ACTIVATION §7. It is not `accept`. Green tests are evidence only for the
relations their production and test semantics actually exercise (P6;
EVALUATION §1).

The Worker label grants no mutation authority. An effectful Worker may
mutate only the exact subject and write territory named by its inherited
construction or transformation grant; missing, ambiguous or out-of-territory
mutation authority refuses the effect (P6).

Read scope follows the complete causal cone and may exceed write territory
within the declared access grant. A narrow mutation grant does not justify
omitting a material producer, consumer or governing owner from inspection.
A repair needed outside the territory is returned to its owner;
understanding a relation grants no cross-boundary effect (P0, P6;
ACTIVATION §1, Execution unit).

## 10. Derived Reviewer frame

(P6, P5; rc.2 #derived-reviewer-frame)

| Frame element | Reviewer |
|---|---|
| evaluation family | Is this the exact claimed subject and basis? Does it satisfy the applicable method and project relations without competing authority, proof masking or an unevaluated composition boundary? For each finding, which evidence-bound severity and technical implications follow? |
| subject and basis | exact candidate, claim, governing method and project authority, scope, exclusions, evidence population, Product-selected severity scale, review carrier and declared independence conditions |
| material manifold | claimed relations; causal producers and consumers; authority seams; competing paths; failure, recovery, installed and reconstruction surfaces where claimed; test and fixture semantics; historical counterexamples; a finding's cause, blast radius, workaround, repair complexity, regression risk and uncertainty where supportable |
| coordinates | exact candidate, source basis, authority revision, configuration, dependency, evidence population, severity scale, installed subject, review time and Reviewer identity |
| governing invariants | RF-001 to RF-017; the execution relation (ACTIVATION §1 and §3); independence and traceability (EVALUATION §3); assurance boundary and qualification freeze (EVALUATION §1, §3 and §7); applicable Product, design, identity and release law |
| authority | bounded evaluation only; review access yields no construction, transformation, admission, publication, mutation, decision, disposition or next-activation authority |
| evidence | independently acquired live authority, candidate implementation, tests, artifacts, history, operational evidence, mutations, replay or reconstruction, and reproduced observations material to the claim and the technical triage |
| capability envelope | declared method, domain, implementation, assurance, technical-triage, tool, access, context, counterexample-search and independence competence |
| exclusions | editing the candidate, implementing a repair, assigning priority, disposing the release or MVP boundary, selecting the next action, substituting the Worker's summary, assurance-owned semantic reconstruction, flattening unbound evidence, silent scope expansion |
| result | one core result with findings, counterexamples, evidence-bound technical triage and residuals sufficient for the Executive to assign priority and apply the existing disposition where the basis is decidable |
| invalidation | a material change of candidate, authority, basis, evidence population, severity scale, dependency, configuration, scope or independence |

EVALUATION §3 decides when independent review is required and what makes
it traceable; EVALUATION §1, §3 and §7 decide the exact assurance boundary
and the qualification freeze. This profile adds no universal review round
and no new independence test (P6).

ACTIVATION §1 and §3 stay the owners of assessment and disposition. This
profile uses an activated Reviewer result as independent live-surface
evaluation input and, in the coordinated branch, the Executive as the
authorised assessor or proxy that applies the one existing disposition. It
creates no second verdict or disposition family (P6, P5).

The Reviewer may assess likely repair complexity and regression risk
without becoming the repair owner. Where cause, blast radius, workaround or
repair risk cannot be supported inside the activation, the result records
that uncertainty instead of manufacturing a complete triage (P5).

Tests are inside the Reviewer's manifold when their code, fixtures,
mutations, environment or interpretation can change the proof claim; a
passing result is not relied on in place of reviewing those semantics (P6,
EVALUATION §1).

Each finding binds a violated property, a supported entry or state, the
governing operating or threat model and a credible causal path. The same
conditions apply to retained guards and acceptance predicates as to new
findings. An excluded threat alone gives no retention claim; a proposed
wider threat model re-enters its owner. Internal location alone does not
establish trust, and hypothetical hostility alone does not establish
applicability. The actual untrusted-input, mutable-state, authority and
effect checks the supported model requires are retained. A suggested repair
becomes an obligation only through its proper owner (P6, P2, P5).

## 11. Derived generic specialist frame set

The profile declares the following generic families for Product work. Each
row is an evaluation archetype, not a complete frame declaration
(REFERENCE_FRAME §13). An adopting project binds, for every activated
instance, the exact subject, basis, material manifold, coordinates,
invariants, authority, evidence, exclusions, result algebra, capability
envelope, dependencies and invalidation conditions (P2, P6; rc.2
#derived-generic-specialist-frame-set).

The family labels resolve inside
`urn:stdo:bounded-context:reference-frame-evaluation`, owned by
REFERENCE_FRAME, under the selected basis. Under bounded-context semantic
resolution (PRODUCT_DEFINITION §5), `Product`, `Owner`, `Entity`,
`Operator`, `Install` and the other labels do not become equal to
same-spelled Product, authority, domain or runtime concepts; every material
cross-context seam needs an explicit relation (P1, P3).

| Family | Evaluation family and exact subject | Governing authority and permitted output | Immediate falsifier |
|---|---|---|---|
| Product | Does one exact current Product claim, outcome, boundary and lifecycle govern the claimed Product subject without downstream reinterpretation? The basis is the current Intent, Product, requirements, acceptance meaning and exact Product coordinates. | Product and requirement authority keep meaning and acceptance. The frame returns only a bounded evaluation result and evidence. | Design, code, tests, a predecessor's behaviour or a local convention changes Product meaning or substitutes another Product subject. |
| Product Composition | Does one exact directed relation between Products preserve the source and target roles, the Product Definition, Release Cut, Product and Install identities, each Development Product role binding, the governing contracts, authority, lifecycle, evidence boundary and invalidation law? A chain is evaluated through bounded edge activations and a declared conjunction. | Each Product keeps its own meaning. The authority and contracts the composition relation cites own the edge. The frame returns evaluation evidence only. | Directory nesting, shared implementation, a common actor, a source import, tool reachability, matching output or builder convenience creates or changes a composition relation; a Development Product is confused with the Product being authored; or one node silently redefines another. |
| Design | Does the accepted structural HOW satisfy the material constitutional WHAT, close the required design relations and keep their owners across the affected topology? | Accepted design under its governing Product and requirements owns structural decisions. The frame may identify satisfaction, contradiction or a design re-entry gap; it cannot invent Product truth. | Implementation precedent resolves an open material design decision, design creates Product meaning, or a material relation or competing structure stays undeclared. |
| Design Component | Does one bounded design component, with its direct causal dependency cone, preserve its parent contract, internal relations, sibling seams and required outputs? | The accepted design boundary owns only its bounded composition decision. Parent, sibling, Product, requirement and runtime owners keep their relations. | The component omits a material far-side seam, absorbs a sibling or parent decision, or reports local closure while its direct composition is unresolved. |
| Public Boundary | Does one supported public entry or exit perform exactly its assigned validation, selection, transport, refusal and projection relations while preserving the selected interior owners? | Product, interface, identity, security and accepted-design authority define the boundary. The frame evaluates the boundary result or refusal and returns only its closed evaluation; it does not recreate interior semantics. | The public surface interprets owner meaning, sequences hidden domain decisions, exposes an interior carrier as Product truth, or admits an unsupported path. |
| Entity | Is one semantic, artifact or runtime entity bound to its exact identity, kind, lifecycle, owner, representation and applicable effect regime? | Product, domain, identity, requirement and accepted-design authority define the entity. The frame returns an identity- and lifecycle-bound evaluation. | A filename, wrapper, ticket, object shape, cache or process instance stands in for stable entity identity, or distinct lifecycle coordinates are collapsed. |
| Operator | Is one material operation an irreducible declared relation over its admitted domain, inputs, outputs, refusals, algebra, effects and lawful compositions? | Product, requirements, the accepted ontology and design, and the named operation owner define the relation. The frame evaluates it without creating another executable plan. | An endpoint, function, class, command or file label is asserted to be the semantic atom; orchestration hides the real operator; or generic mechanics are rebuilt as domain law. |
| Owner | Does one semantic or authority-bearing relation preserve its owner, role kind, subject, scope, basis, lifecycle, refusal invariants and permitted delegation? | The existing Product, requirement, identity, accepted-design, release or other named authority owns the relation. The frame may evaluate authority congruence only. | Another surface recreates the judgment, source authorship is treated as authority transfer, or a proxy, foundation, frame or actor widens the grant. |
| Effect | Does one action obey its declared pure, observational, artifact or runtime effect regime, including commit, failure, retry, recovery, compensation, admission and projection law where material? | The applicable Product, requirement, design, artifact, runtime and admission owners keep their decisions. The frame returns an effect-bound result and evidence. | Distinct effect regimes are collapsed, a mutation bypasses its admitted owner, compensation is treated as semantic rollback, or a read becomes rival writable truth. |
| Reuse/Foundation | Has one material generic capability or dependency been normalised and compared against credible lawful foundations, with any irreducible local remainder and authority-bearing role preserved? | The design profile's capability-and-foundation selection law and the existing trade-off owner govern selection. The frame cannot move semantic authority to a foundation. | Incumbent or local code wins without a bounded comparison, a richer lawful foundation is reproduced, unknowns are scored favourably, or reuse acquires owner authority. |
| Install | Is the exact selected Product, release, artifact, dependency set, configuration and callable entry resolved and exercised through its admitted installed coordinate, independently of mutable source convenience? | Product, identity, release, dependency, packaging and accepted-design authority define the installed subject. The frame returns installed identity, reachability and refusal evidence. | Source-tree imports, ambient resolution, process registries, fixture bindings, rebuilt artifacts or a moving workspace stand in for the claimed installed subject. |
| Proof | Does one exact claim have a congruent subject, basis, path, population, oracle, evidence, falsifier, residual boundary and invalidation law? | The claim owner defines meaning; the applicable testing, assurance, review, Product and release owners define evaluation and acceptance. The frame returns evidence and a closed evaluation result, not Product meaning or disposition. | A harness recreates owner meaning, evidence targets another subject or path, a count or aggregate green stands in for the claim, or proof tooling mutates the subject undetectably. |

The families are non-hierarchical and may overlap (RF-008, RF-009).
Product does not outrank Design by frame topology; Product authority
already governs constitutional meaning. Owner gains no authority over
Entity or Operator by being a broader frame. Proof does not become Reviewer,
acceptance or disposition authority. The existing authority graph stays in
control (P6).

### Family dispositions

For each governed outcome the known evaluation inventory (REFERENCE_FRAME
§8) disposes every family as one of (P2, P6, P5):

- instantiated by one or more exact frame declarations or authoritative
  acquisition paths, because the family is material;
- evidenced as non-material to the exact outcome by the authority capable
  of that determination; or
- kept as an explicit uncovered, conditional, conflicted or `out_of_frame`
  residual.

The absence of a named file, component, runtime object or actor is no
evidence that a family is non-material. Conversely, adopting this profile
does not require a project to create twelve components or to activate
twelve frames for every task (P2, P1).

### Refinement and conjunction

When a generic frame is recursively refined, each child declaration records
its parent contract, purpose, material entities, identity and lifecycle
relations, semantic owners, direct sibling seams, applicable invariants and
prohibited competing paths. Refinement opens only for a material
distinction needed to close the parent evaluation. It is a frame dependency
relation, not an organisational or runtime hierarchy (P2, P4a; ACTIVATION
§4).

Coverage records the union of admissible observations the activated frames
contribute. A composite claim is `satisfied` only through a declared
conjunction in which every applicable constraint is satisfied and every
material cross-frame seam preserves, or lawfully translates, exact
identity, coordinate and basis, carried value or evidence, lifecycle scope,
authority and provenance (REFERENCE_FRAME §6). A missing or non-commuting
seam returns the applicable `falsified`, `indeterminate`, `out_of_frame` or
`invalid_basis`; no frame is selected as dominant (P4a, P5).

The set imports no consumer-specific frame, runtime role, architectural
topology or renamed local substitute. A consumer may declare such frames
under its own Product or accepted-design authority when they are material;
they are not part of this baseline (P2, P6).

### Relation to the testing and interface frames

Where this set is adopted, the product testing frames of ASSURANCE §7 supply
claim-congruent evidence to one or more Proof evaluations. Proof is not a
testing hierarchy or an aggregate-green frame: user-acceptance, end-to-end,
integration and unit results keep their distinct claims and coordinates (P6,
P4a; rc.2 #derived-product-testing-frame-set).

The end-to-end interface integration frame (ASSURANCE §13) relates the
Public Boundary, Design, Operator, Owner and Proof families to the
integration, end-to-end and user-acceptance frames. Its computational
whole-path evaluation composes the selected interface claims with Operator,
Owner, Reuse/Foundation and Proof. Neither adds a thirteenth family, a fifth
testing type, a role or a universal activation gate (P2; rc.2
#derived-end-to-end-interface-integration-frame,
#computational-whole-path-evaluation).

## 12. Complete engagement transition

The steps below describe the coordinated branch selected under §3. Direct
Worker engagement keeps the same sufficient intake, work-result algebra,
closure conditions and owner boundaries without inserting an Executive
appointment, or a review that no applicable condition requires (P0, P6;
rc.2 #complete-engagement-transition).

### 1. Existing authority selects the basis

Goals, Product, requirements, accepted design, a ticket, release law or an
admitted bounded proxy selects the outcome and the work authority under its
existing owner. The Product-owned Project Reference-Frame Basis
(PRODUCT_DEFINITION §7) projects that decision (P6; rc.2
#1-existing-authority-selects-the-basis).

### 2. Executive activates Worker

In the coordinated branch the Executive applies `activate` (REFERENCE_FRAME
§5) to the sufficient execution intake of ACTIVATION §1. The packet is
REFERENCE_FRAME §11; for this step it identifies (P0, P6; rc.2
#2-executive-activates-worker):

- the selected complete method and project authority;
- the exact governed outcome and checkpoint;
- the affected causal relation set and the governing invariants;
- the selected computational relations and specialist frames;
- where testing evidence is required: the testing claims, exact subjects,
  frame topology, material combination populations, ordinary paths,
  oracles and forbidden-path exclusions (ASSURANCE §7 to §9);
- the Worker's authority and capability envelope, and, where mutation is
  authorised, the exact inherited operation grant, subject and write
  territory;
- the evidence and qualification obligations;
- exclusions, prohibited competing paths, stop conditions and re-entry
  conditions; and
- the exact bounded action already authorised.

If activation detects a known capability, authority, subject, basis or
topology mismatch, it returns `activation_refusal` directly to the
Executive. No Worker frame is active, no Worker evaluation occurs, and the
Executive does not manufacture a Worker result to represent the failed
activation (P5, P6).

### 3. Worker returns to Executive

Every coordinated Worker activation ends in one closed work result sent to
the Executive; direct work uses its declared result consumer (P5, P6; rc.2
#3-worker-returns-to-executive):

```text
WorkerResult
  = candidate_ready(exact_subject, transition_evidence, residuals)
  | refused(reason, authority, evidence)
  | incomplete(residuals, evidence, stop_basis)
  | re_entry_requested(owner, material_relation, evidence)
```

The notation explains and mandates no schema. Each variant accompanies
exactly one core result under the mapping of ACTIVATION §3 (construction
availability), read as in §5 (Work result); the mapping applies only after
lawful activation. The Worker does not send a candidate directly into an
implicitly active Reviewer. It stops after returning the result (P5,
P6).

### 4. Executive evaluates the work result

For `refused`, `incomplete` or `re_entry_requested`, the Executive verifies
the exact basis and applies the existing authority relation. It records the
applicable disposition, or reactivates work only where current authority
already permits that action. None of these variants is accepted progress
because work occurred (P6, P5; rc.2 #4-executive-evaluates-the-work-result).

For `candidate_ready`, the Executive verifies the exact subject and decides
whether independent assessment is required by EVALUATION §3, ACTIVATION §1,
EVALUATION §7 (method qualification), Product, release, risk or the admitted
work contract. Green aggregate status cannot satisfy this step when a
required user-acceptance, end-to-end, integration, unit or negative-path
result is missing, bound to another subject, or contradicted by a material
frame result (P6; ASSURANCE §10).

### 5A. Candidate does not require independent review

In the coordinated branch, when independent review is not required, the
Executive consumes the exact candidate, the Worker's self-review, the
transition evidence and any mandatory specialist results, and applies the
disposition within its decision envelope. Self-review stays Worker
evidence; the disposition does not relabel it as independent (P6; rc.2
#5a-candidate-does-not-require-independent-review).

### 5B. Candidate requires independent review

When independent review is required, the Executive activates the Reviewer
with (P6, P3; rc.2 #5b-candidate-requires-independent-review):

- the exact candidate and governing basis;
- the exact claim, composition boundary, population, scope and exclusions;
- the applicable method and project authority;
- the required evidence and the ordinary assurance path;
- the required user-acceptance, end-to-end, integration, unit,
  combinatorial and negative-path frame results, with their exact claims and
  populations;
- the Product-selected severity scale and the exact affected Product claims;
- the Reviewer's capability and independence envelope; and
- invalidation and stop conditions.

Where EVALUATION §7 requires it, the candidate is frozen before material
reference exposure. Otherwise the subject is stabilised to the exactness
that EVALUATION §3, ACTIVATION §7 and the claim require (P3, P6).

### 6. Reviewer returns to Executive

The Reviewer returns one closed evaluation in the shape of EVALUATION §4,
which here contains (P6, P5; rc.2 #6-reviewer-returns-to-executive):

- frame and activation identity;
- the exact subject, basis, claim, scope, exclusions and evaluated
  population;
- the Reviewer actor and the independence conditions;
- the evidence and the ordinary assurance path acquired;
- the core result;
- findings, counterexamples and adjacent observations;
- for each finding, where supportable: the affected claim, severity, causal
  assessment and confidence, blast radius, workaround, repair complexity,
  regression risk and residual uncertainty; and
- invalidation conditions and, where applicable, the re-entry owner.

The finding-level triage payload projects over the result algebra as
EVALUATION §4 (Result and triage projection) states; in this profile the
assessor there is the Reviewer and the decision owner is the Executive. The
Reviewer returns to the Executive, not to the Worker, and returns no
disposition; a recommendation is evidence only (EVALUATION §4). It does not
edit the candidate, direct the repair or authorise continuation (P6; rc.2
#reviewer-result-and-triage-projection).

### 7. Executive disposes and checkpoints

The Executive verifies that every consumed result is still bound to the
current subject and basis, revalidates the complete Product view and the
current MVP or release mandate, applies any declared result conjunction,
assigns priority, records the effect on the current promotion boundary, and
acts on exactly one disposition within its grant: `accept`, `local_repair`,
`re_enter` or `reject` (ACTIVATION §3; P6, P5; rc.2
#7-executive-disposes-and-checkpoints).

ACTIVATION §3 and §5 stay the owners of each disposition, the exact accepted
checkpoint and the next already-authorised bounded action. A repair creates
a new candidate, and an affected review is reactivated against it.
Acceptance does not widen the Product outcome or authorise an unselected
successor (P4b, EVALUATION §5).

Severity neither selects priority mechanically nor blocks promotion.
Priority neither erases severity nor waives a hard stop. The Executive
decides blocking from the exact affected claim, the current mandate, the
applicable hard stops and the Product-owned cutoff policy. An unsupported
technical assessment returns through a new or refined activation rather
than being silently rewritten (P6, P1).

### Promotion constraint projection

(P6, P5; rc.2 #executive-promotion-constraint-projection)

| Consumed condition | Required Executive constraint |
|---|---|
| a valid falsification of a mandatory claim governed by a non-waivable hard stop | the current promotion boundary blocks, whatever the assigned priority or decision cutoff |
| a valid finding below the Product-owned decision cutoff, with no hard stop | no block follows mechanically; the Product-owned policy is applied and any accepted residual is kept explicitly |
| an observation outside the exact evaluated claim | bounded repricing or re-entry input; it creates no claim-relative block and no further review round by its severity label |
| an unsupported or materially incomplete technical assessment | a capable evaluation is reactivated, or `indeterminate` is kept; Reviewer evidence is not rewritten |

## 13. Handoff projection

The coordinated branch uses the following bounded projections. They may be
fields in existing Goals, tickets, design assets, commentary, qualification
or release evidence, or other admitted carriers; the profile requires no new
artifact type (P2, P6; rc.2 #handoff-projection).

| Projection | Producer to consumer | Minimum material content | Owning law |
|---|---|---|---|
| Worker activation | Executive to Worker | exact intake, basis, affected cone, inherited operation grant, mutation subject and write territory where applicable, frames, evidence, exclusions, stop and re-entry conditions | REFERENCE_FRAME §11; ACTIVATION §1 |
| activation refusal | the activation relation to Executive | attempted frame, subject and basis, actor, the failed capability or authority predicate, evidence and reconfiguration pressure; no Worker result | REFERENCE_FRAME §5; ACTIVATION §1 |
| work result | Worker to Executive | result variant, exact subject if any, transition evidence, non-changes, residuals, stop basis | ACTIVATION §3 and §7 |
| Reviewer activation | Executive to Reviewer | exact subject, claim, composition boundary, evidence population, Product-selected severity scale, authority, independence, invalidation | REFERENCE_FRAME §11; EVALUATION §3 and §7 |
| review result | Reviewer to Executive | exact verdict basis, evidence, findings, counterexamples, technical triage, residuals, invalidation; no priority and no disposition, a recommendation being evidence only | EVALUATION §3 and §4; ACTIVATION §3 |
| specialist activation | Executive or a declared parent relation to a capable evaluator | exact evaluation, subject and basis, bounded map of material relations, actor envelope, evidence, authority, dependencies, exclusions, result consumer, invalidation | REFERENCE_FRAME §11; the exact specialist owner |
| specialist result | evaluator to Executive, a declared conjunction or the exact parent relation | closed result, exact activation and basis, evidence and source routes, residuals, invalidation, no implicit continuation | ACTIVATION §7; the exact specialist owner |
| disposition and checkpoint | Executive to the existing work authority and any next activation | the exact consumed results and technical triage, current Product and MVP or release mandate, priority, promotion-boundary effect, decision grant, disposition, checkpoint, residuals, next already-authorised action | ACTIVATION §3 and §5; the Product-owned triage policy |

Flattening these projections across candidates, processes, episodes,
configurations, evidence populations or bases establishes no relation among
them; equality or translation is declared under REFERENCE_FRAME §6 where
needed (P3, P4a).

Direct engagement carries the same material intake and result coordinates
in its existing work carrier. Where that branch has no Executive
activation, it substitutes the actual granting or result authority for the
Executive; it does not silently activate a Reviewer or acquire new decision
authority (P6).

## 14. Coverage application

The three engagement frames do not claim to contain the complete Product or
project workspace. They organise finite evaluations over specialist frames
(P0, P2; rc.2 #coverage-application).

| Known evaluation | Primary engagement frame | Authority or specialist input |
|---|---|---|
| exact method, project and work basis | Executive | the complete method cut; current Goals, Product, requirements, design and work authority |
| affected causal cone and frame configuration | Executive, challenged by Worker and Reviewer | ACTIVATION §1 intake and execution unit with the design profile's bounded-frame conservation laws; domain, identity, dependency, implementation and history frames |
| generic family coverage and cross-frame seam conservation | Executive for configuration; Worker and Reviewer for their exact evaluations | material declarations or authoritative acquisition paths for the twelve families of §11; explicit non-material and residual dispositions |
| bounded realisation and self-review | Worker | accepted design; the design profile's capability-and-foundation selection where material; capability and reuse, implementation, environment and proof frames |
| candidate and transition evidence | Worker | ACTIVATION §7 and the exact identity and evidence relations |
| a user can obtain the Product-defined outcome through supported surfaces | Worker for execution and self-review; Reviewer where independent assurance is required | the user-acceptance frame (ASSURANCE §7); Product, requirement, UX, identity, installed-subject and acceptance inputs |
| the complete authoritative installed path realises the outcome | Worker for execution and self-review; Reviewer where independently assessed | the end-to-end frame (ASSURANCE §7); composition, authority, lifecycle, persistence, recovery, replay and negative-reachability inputs |
| material interfaces compose across their interaction population | Worker and Reviewer according to the claim | integration frames (ASSURANCE §7); actual participant, carrier, state, configuration, failure and recovery inputs |
| module-owned laws hold | Worker and Reviewer according to the claim | unit frames (ASSURANCE §7); the design's ontology and carrier inventory, public module contract, algebra, calculation, state-machine, invariant and module-bounded combination inputs |
| obsolete and rival Product paths are absent, unreachable or refused | Worker for deletion evidence; Reviewer for exact-subject challenge where required | the distinct production-closure and assurance/source-closure graphs (ASSURANCE §9); package, consumer, mutation, sabotage, reconstruction and history frames |
| independent exact-subject assessment and technical triage where required | Reviewer | EVALUATION §3 and §7; ACTIVATION §1; the Product-selected severity scale; live implementation and assurance frames |
| result conjunction, priority, promotion-boundary effect and disposition | Executive | the exact closed Worker, Reviewer and mandatory specialist results; current Product and MVP or release mandate; the Product-owned triage policy |
| checkpoint and continuation | Executive under existing authority | ACTIVATION §5; the current Goals, Product and release boundary |
| missing-frame and topology-change response | Executive, with pressure from any frame | REFERENCE_FRAME §8 and §10 |

The Executive derives the complete known evaluation inventory from the
selected method members, the project domain, the outcome, history,
dependencies and the workspace. Operational full coverage keeps every
unknown, uncovered, conditional, conflicted or authority-excluded residual
REFERENCE_FRAME §8 requires (P4b, P5).

Executive visibility is not coverage. Every material evaluation still needs
a capable frame, admissible evidence and identified semantic and decision
owners; every material construction, transformation, admission, publication
or mutation also needs its existing operation owner and exact grant (P6;
REFERENCE_FRAME §8, authority coverage).

## 15. Missing-frame and re-entry application

Any active frame may return `out_of_frame`, `indeterminate` or
`invalid_basis` (ACTIVATION §3). The closed result names the missing
relation, coordinate, evidence, authority, capability or interaction that
can change the evaluation (P5; rc.2
#missing-frame-and-re-entry-application).

The Executive applies the diagnostic order of REFERENCE_FRAME §10, read for
this profile with two specific steps (P2, P6): the actor check covers
independence as well as capability (step 3), and before a missing
material variable is suspected the Executive verifies the required
specialist-frame inputs (step 5). The applied order is: the declared frame
activation; the exact subject and basis; actor capability and independence;
admissible evidence acquisition; the required specialist-frame inputs; the
conjunction or translation; the evaluation family; and only when none of
these closes the gap, a frame added or revised.

If the discovery changes Product, a requirement, identity, lifecycle,
authority, a public contract or the accepted design, the disposition is
`re_enter` to that existing owner (ACTIVATION §3). The Executive does not
repair an upstream authority gap by making its frame larger (P6).

## 16. Adoption or project-defined configuration

### Existing authority selects the configuration

The frame configuration is admitted by the smallest existing project
authority that owns the material decision (P6, P2; rc.2
#existing-authority-selects-the-configuration):

- Goals or admitted work authority own bounded work selection;
- Product owns Product-wide capability or acceptance meaning;
- requirements own constitutional behaviour;
- accepted design owns realisation structure and specialist design frames;
- identity and release owners keep their declared decisions; and
- an explicitly bounded proxy acts only inside its existing grant.

One configuration may derive from several governing owners. The
Product-owned Project Reference-Frame Basis (PRODUCT_DEFINITION §7) cites
all material sources and does not collapse them into a new local-axiom
authority (P6).

### Adopt this baseline

A baseline-adoption projection records inside that Product-owned basis
(P6, P3; rc.2 #adopt-this-baseline):

- the exact selected complete method, REFERENCE_FRAME and profile
  identities;
- the existing authority admitting adoption;
- the governed workspace, Product scope, outcome, basis and time;
- local Executive, Worker and Reviewer capability envelopes and
  actor-binding rules;
- generic family declarations or authoritative acquisition paths, with an
  authority-bound non-material or explicit residual disposition for each of
  the twelve families of §11;
- specialist-frame declarations or authoritative acquisition paths;
- where testing evidence is material: testing-frame declarations, exact
  Product and module claims, ordinary-path identities, combinatorial
  populations, the scenario matrix, oracles and the forbidden-path
  inventory (ASSURANCE §7 to §9);
- local subject, evidence, checkpoint and review-result coordinates;
- the coverage ledger and the accepted residual boundary; and
- invalidation and frame-set revision conditions.

### Define a project configuration

A project may define different frames, names, overlaps, sequences and actor
bindings. The defining Product, requirement, Goals or accepted-design
authority records (P6, P2; rc.2 #define-a-project-configuration;
REFERENCE_FRAME §4):

- the exact method and project basis;
- the known evaluation inventory;
- each frame declaration and capability envelope;
- semantic, evaluation, operation where material, and decision authority;
- intentional overlap, separately activated evaluations and required
  assurance independence;
- the conjunction, translation and composition actually used;
- the mapping to the applicable construction, assessment, disposition,
  identity and release obligations;
- coverage and residual uncertainty; and
- re-entry, invalidation and revision conditions.

A project configuration need not keep the labels Executive, Worker and
Reviewer or map one local frame to each. It keeps every applicable method
relation and identifies how its evaluations cover the claims it makes. A
local axioms document may carry the accepted configuration; its authority is
the cited Goals, Product, requirement or accepted-design decision, not the
document's category (P6, P1).

### Extension versus replacement

Adding domain or specialist frames, additional separately activated or
assurance-independent coverage, or local evidence coordinates extends this
profile. Changing the material Executive, Worker, Reviewer, handoff,
independence or disposition configuration creates a project-defined
profile (P6; rc.2 #extension-versus-replacement).

Neither choice amends the method's execution law. A project that
intentionally departs from that law records a separate method basis or a
non-conformance; it does not describe the departure as local frame
selection (P6, EVALUATION §6).

## 17. Actor binding and independence

Frames and actors are separate identities. One actor may occupy several
frames across different activations where authority and any claimed
independence are preserved. Humans, agents, deterministic tools or mixed
configurations may occupy them. The profile prescribes no actor count (P3,
P6, RF-016; rc.2 #actor-binding-and-independence).

Where independent review is required, EVALUATION §3 controls: the
activation records the exact subject and verdict carrier, and the Reviewer
is not the author of that subject. For generic method qualification,
EVALUATION §7 adds its declared capability, configuration, comparison
basis, reference-exposure and freeze conditions (P6).

An Executive may inspect a subject to adjudicate a result. That inspection
does not become an additional independent Reviewer result because the actor
used reviewer-like tools (P6, P1).

## 18. Profile qualification

Qualification of this profile applies frame qualification and method
self-qualification (EVALUATION §7); it creates no other qualification
protocol (P6; rc.2 #profile-qualification).

A profile trial evaluates this profile and its declared composition with
the exact REFERENCE_FRAME basis without reproducing either as a peer
authority. A valid pure-method trial does not prove this profile, and a
valid profile trial does not prove the method's complete function
population (P6, P4a).

Mechanical document checks may protect exact table shape, result
cardinality, source-digest congruence and named refusal boundaries. They do
not establish semantic truth and do not replace a capable source-linked
Reviewer evaluation. Profile qualification binds both kinds of evidence
without claiming one as the other (P6, P1; EVALUATION §2).

A representative profile trial establishes at least that (P6, P5):

1. existing project authority selects and projects the frame
   configuration;
2. a known incapable or unauthorised actor produces an activation refusal
   and no Worker result;
3. a fresh capable Worker reconstructs its intake without hidden
   conversation history;
4. every effectful Worker activation carries its exact inherited operation
   grant, subject and write territory; an in-territory mutation succeeds
   only under that grant and an out-of-territory mutation refuses, without
   granting operation authority to another frame;
5. every work-result variant is mapped disjointly from its core result and
   returns to its declared consumer, the Executive in the coordinated
   branch;
6. a sufficient direct local case starts and finishes as Writer in its
   existing carrier without Executive appointment or independent review,
   and a coordinated `candidate_ready` also reaches disposition without a
   Reviewer activation when independent review is not required;
7. a review-required `candidate_ready` causes the Executive, not the Worker,
   to activate the Reviewer;
8. the Reviewer reacquires the exact subject and the live production and
   assurance surfaces material to its claim;
9. a changed candidate or basis invalidates the affected review result;
10. Worker self-review, Reviewer evaluation, Executive decision authority
    and the disposition stay distinguishable;
11. missing-frame pressure triggers bounded diagnosis or lawful re-entry;
12. a supported-surface user scenario binds one exact user, one deployed,
    installed or otherwise runnable Product form, its configuration, the
    ordinary path and the Product outcome, without hidden capability or a
    test-only entry;
13. the corresponding end-to-end frame observes the authoritative runnable
    causal path and falsifies an equal output obtained through a forbidden
    path;
14. integration trials vary the material participant interaction
    dimensions and keep omitted higher-order combinations as residuals;
15. every coded module has a module-derived unit lane, and unit trials use
    evidence size and strategy proportional to the internal combinatorial
    complexity of the module-owned law while staying unable to establish an
    integration, runnable-Product, user or Product claim;
16. disabling the selected path or forcing a rival path produces the
    declared failure or refusal without undetectably mutating the assurance
    subject;
17. aggregate green status cannot hide a missing, conflicted, stale-subject
    or wrong-path testing-frame result;
18. owner-issued runtime truth is acquired through the exact owner surface
    and evaluated with a separately derived oracle, while generic assurance
    mechanics stay authority-neutral;
19. a counterexample returns a causally minimal supported frontier
    represented as one unique locus, a jointly established incomparable
    set, unresolved alternative frontiers, or `indeterminate`;
20. a project-defined configuration can replace the profile without
    changing the selected method law or inventing another authority layer;
21. every generic family is instantiated where material, evidenced as
    non-material by capable authority, or kept as an explicit residual,
    never omitted because an artifact or component is absent;
22. a representative multi-frame claim refuses, or returns
    non-satisfaction, when an identity, coordinate, value or evidence,
    lifecycle, authority or provenance seam is missing, stale, foreign or
    non-commuting;
23. the generic set can be instantiated without importing a
    consumer-specific architecture, runtime object or renamed local
    topology into the baseline;
24. the Reviewer returns evidence-bound severity and technical implications
    while staying unable to assign priority, block promotion, direct repair
    or activate another frame;
25. the Executive consumes the exact technical triage with the complete
    Product view and the current MVP or release mandate, keeps severity,
    priority, frame result and promotion-boundary effect distinct, and
    selects only an authorised disposition and action; and
26. a finding outside the exact claim boundary stays repricing input rather
    than creating a release block or another review round by its severity
    label.

The claim is limited to the frame revisions, actor envelopes, result
branches and evidence populations actually evaluated (P6; EVALUATION §1).

## 19. Baseline-specific basis and activation additions

### Project-basis additions

An adopting Product starts from the Project Reference-Frame Basis of
PRODUCT_DEFINITION §7 and its starter template. This profile adds only the
following profile-specific content; it is not a competing basis definition
or adoption authority (P6, P2; rc.2
#baseline-specific-project-basis-additions):

```markdown
# Executive Baseline Adoption Additions

- exact Executive baseline profile identity:
- Executive, Worker and Reviewer declaration or acquisition references:
- role-specific actor capability, authority and independence bindings:
- Product-selected severity and priority scales, current-boundary cutoff,
  non-waivable hard stops, and the Reviewer-to-Executive triage relation:
- work-result to core-result mapping (ACTIVATION §3):
- the twelve generic family declarations, non-material evidence or
  explicit residuals:
- Product-testing claims, frame topology, material combination
  populations, scenario matrix, oracles, and required and forbidden
  authoritative paths:
- profile-specific activation refusal, closed-result, conjunction and
  return relations:
- profile-specific qualification evidence and residuals:
```

### Activation additions

Every activation first carries the generic binding of REFERENCE_FRAME §11
(minimal activation binding). This profile adds, by frame (P0, P6; rc.2
#baseline-specific-activation-additions):

| Frame | Added to the generic binding |
|---|---|
| Worker | the binding is also the sufficient execution intake of ACTIVATION §1, and adds the exact inherited operation grant, mutation subject and write territory where applicable |
| Reviewer | the exact claim, composition boundary, evaluated population, oracle, ordinary or module path, falsification condition, the independence and assurance basis (EVALUATION §3 and §7), the Product-selected severity scale and the required technical-triage capability |
| Executive | the current Product-role map, the MVP or release mandate, the evaluation frontier, the closed-result and technical-triage ledger, the priority and boundary policy, the conjunction rule and the exact disposition grant |

## 20. Failure classification

The table routes evaluation; it does not predetermine a verdict (P5, P2;
rc.2 #failure-classification; REFERENCE_FRAME §10).

| Observation | First diagnosis |
|---|---|
| implementation produces a coherent capability that is not the selected Product | Product-frame falsification and Product re-entry |
| a Development Product's structure becomes the authored Product's meaning | Product-role or composition-basis drift |
| an authorised mutable Source Project is treated as one immutable review subject throughout construction | collapse of the Source Project and candidate-checkpoint lifecycles |
| one actor receives every specialist concern as one global context and repeatedly misses known violations | attention-surface or capability mismatch; refine and independently activate frames |
| every local frame is green but an affected Product edge is unevaluated | missing Product Composition activation |
| a child result directly starts repair, review, publication or continuation | return-topology and decision-authority violation |
| a compression, summary, generated map or prior result replaces current source authority | invalid basis or evidence substitution |
| the Worker cannot see a material violation visible from another evaluation | missing or misactivated specialist frame, capability mismatch, or oversized frame |
| the Reviewer asks assurance code to recreate Product or implementation meaning | Reviewer authority bleed, or a missing capability or reuse frame |
| a harness derives current owner state from raw events or payloads although an installed owner projection exists | rival semantic interpreter and invalid assurance subject |
| a downstream symptom is assigned to one upstream owner without causal-frontier evidence | unsupported counterexample localisation; determine whether the evidence supports one locus, a joint incomparable set, alternative frontiers or `indeterminate` (ASSURANCE §12) |
| passing tests mask malformed fixtures or a false proof relation | test semantics omitted from the Reviewer's manifold |
| hundreds of green unit tests coexist with a failed Product outcome | unit evidence flattened into an unevaluated user-acceptance, end-to-end or composition claim |
| the expected output is reached through an obsolete or bypass path | end-to-end path-conformance falsification despite equal output |
| a UAT scenario uses private APIs, injected state, hidden administrator capability or a test-only endpoint | invalid user-frame subject or unsupported ordinary path |
| one sunny end-to-end path is reported as combinatorial coverage | undeclared interaction population and residual higher-order combinations |
| pairwise coverage is used for authority, persistence, recovery, migration or historical multi-boundary failures without justification | insufficient interaction strength or invalid coverage basis |
| successor tests pass while obsolete exports, consumers, fallbacks or proof scripts remain | technical-debt deletion and forbidden-path exclusion unproved |
| a negative-path test overwrites the frozen install it is meant to qualify | assurance-subject invalidation and missing mutation isolation |
| review evaluates a moving tree or a rebuilt artifact | invalid exact-subject basis (EVALUATION §3 and §7) |
| several episodes or stores are flattened into one apparent path | missing coordinate translation or interaction binding |
| the Worker starts the next stage after self-review | violation of decision and continuation authority (ACTIVATION §1 and §5) |
| the Reviewer implements the fix while keeping its verdict | violation of independence and frame authority (EVALUATION §3) |
| the Reviewer assigns priority, blocks promotion, directs repair or activates another frame | Reviewer-to-Executive decision-authority bleed |
| the Executive treats severity, priority, frame verdict and release blocking as one value | triage-relation collapse; reapply the Product-owned policy to the exact claim and mandate |
| the Executive rewrites semantics to close a local problem | decision outside the proxy grant; re-entry required (ACTIVATION §3, EVALUATION §5) |
| repeated local repair creates another authority path | incomplete affected cone, or a missing owner or capability frame |
| long effort resets after local success | coverage, frame altitude, topology, evidence or capability diagnosis required |

## 21. Anti-patterns

The profile is misapplied when (P6, P2; rc.2 #anti-patterns):

1. Executive, Worker or Reviewer is treated as a persona without a declared
   evaluation and authority relation;
2. the frames are treated as an organisational hierarchy;
3. the Executive is made a universal context, semantic interpreter or
   implementation controller;
4. the Worker sends a candidate directly into an implied Reviewer
   activation;
5. an activation refusal is relabelled as a Worker result, or a work-result
   variant is selected without its required core result;
6. refused, incomplete or re-entry work results have no route to the
   Executive;
7. the Worker accepts its own result, infers continuation, or treats its
   role label or broad workspace access as mutation authority;
8. the Reviewer relies on the Worker's narrative instead of acquiring the
   material live subject;
9. the Reviewer trusts tests without reviewing their semantics where they
   can change the proof;
10. the Reviewer edits or directs repair while keeping independent-review
    status;
11. a changed candidate or basis reuses the predecessor verdict;
12. results from different coordinates are flattened into one relation;
13. a local axioms file is treated as authority without an owning Goals,
    Product, requirement or design decision;
14. this profile restates the execution relation (ACTIVATION §1 and §3),
    independent assessment (EVALUATION §3) or the assurance-boundary law
    (EVALUATION §1 and §7) as peer constitutional law;
15. a project-defined configuration silently changes selected method law;
16. consumer-specific realisation machinery, or a renamed architectural
    equivalent, is presented as a universal requirement;
17. test labels or runner choice stand in for declaring the exact testing
    frame, subject, claim, population, oracle, path and falsification
    condition;
18. unit-test, assertion, snapshot, line, branch or function count is used
    as a Product-confidence or closure measure;
19. implementation-shaped unit tests are treated as independent design,
    architecture, integration, installed or user-outcome assurance;
20. interface, persistence, orchestration, authority, configuration or user
    complexity is mocked away and then counted as unit coverage;
21. helper-level tests become the canonical proof surface for a
    module-owned algebra or for a broader Product composition;
22. an expected output is accepted without proving the required
    authoritative path, or while a material rival path stays reachable;
23. one sunny end-to-end path stands in for a declared combinatorial
    population, an interaction-strength justification, failure coverage and
    a residual set;
24. UAT gains capabilities, information, setup paths or interfaces
    unavailable to the declared user;
25. a harness, fixture, proof script or expected-value builder
    reconstructs owner-issued runtime meaning and treats the reconstruction
    as the assurance subject;
26. a downstream symptom is assigned to one owner when the evidence
    establishes a joint causal frontier, unresolved alternatives or no
    bounded frontier, or localisation is used to authorise a wider repair;
27. a mutation, sabotage, fixture or proof capture changes the exact
    assurance subject without isolation, restoration and revalidation;
28. aggregate green status hides a missing or conflicting user-acceptance,
    end-to-end, integration, unit or negative-path result;
29. a generic family is treated as a required component, actor, service,
    file, runtime type, stage or new semantic owner;
30. a material generic family is omitted because no artifact shares its
    name, or several families are flattened into one broad frame without
    preserving their distinct evaluation and result relations;
31. the Reviewer assigns priority, decides promotion blocking, directs
    repair or starts another activation; or
32. the Executive collapses severity, priority, frame result,
    promotion-boundary effect and disposition into one status value.

## 22. Closure

Only the obligations applicable to the exact selected outcome and
engagement branch are evaluated. A listed frame or an available testing
family does not make its claim applicable (ACTIVATION §1, Applicability).
Every applicable obligation is satisfied with valid evidence and the
required judgments and owner rulings, with no active non-closure condition;
a work item closes by its stated condition (EVALUATION §5). A closed
`indeterminate` result or a review event does not satisfy an unresolved
obligation (P5, P6; rc.2 #closure).

A project has applied this baseline to one outcome when (P6, P2):

1. existing project authority admits and projects the exact frame basis;
2. the complete selected method, REFERENCE_FRAME included, stays the
   governing source;
3. Executive, Worker and Reviewer are available finite evaluation frames,
   activated only where applicable, not a hierarchy or actor identities;
4. activation refusal stays distinct from Worker results, and every Worker
   result maps exclusively from one closed core result and returns to its
   declared consumer, first to the Executive in the coordinated branch;
5. existing work authority decides whether an exact candidate requires
   independent review; the coordinated Executive activates the Reviewer
   where required, and the sufficient direct branch adds no such
   activation;
6. required Reviewer assessment binds the exact subject, evidence
   population, verdict, evidence-bound technical triage and independence
   conditions;
7. an activated Executive consumes closed results and technical triage
   against the complete Product view and the current MVP or release
   mandate, keeps severity, priority, frame result and boundary effect
   distinct, and applies only the existing disposition and continuation
   relation;
8. specialist frames and result relations cover every known material
   evaluation and interaction or keep an explicit residual;
9. frame, basis, capability, evidence and topology change can invalidate
   and rechart the configuration;
10. every material operation carries its existing owner's exact grant;
11. no new execution authority, local constitutional layer, actor topology,
    runtime or universal completeness claim is inferred from the profile;
12. every material Product testing claim is assigned to an exact
    user-acceptance, end-to-end, integration, unit or explicitly declared
    alternative frame rather than inferred from a suite label;
13. a user-outcome claim binds the declared user capability, the exact
    Product subject, the supported ordinary surface, the environment and
    the observable outcome;
14. an end-to-end claim binds the exact deployed, installed or otherwise
    runnable Product form and records the required authoritative causal
    path, rather than accepting equal output through an unknown or
    forbidden path;
15. material interface and Product factors have a declared combinatorial
    population, adequate interaction strength, an exercised scenario matrix
    and explicit residual combinations;
16. unit evidence proves module-owned laws, public module contracts
    included, with volume and strategy proportional to useful
    discrimination of the module-bounded population rather than to
    implementation size;
17. required paths have positive runnable-Product witnesses; the
    production closure excludes obsolete, rival, fallback and bypass paths;
    the assurance/source closure cannot falsely supply evidence or
    reintroduce a removed production path; and declared isolated test-only
    seams stay outside ordinary-path claims;
18. source or code coverage, test count and aggregate green status do not
    stand in for Product, installed, path, composition or user-frame proof;
19. test fixtures, mutations, sabotage, proof capture and assurance tooling
    preserve or revalidate the exact subject they claim to evaluate;
20. owner-issued Product and runtime truth is acquired through the exact
    owner surface and evaluated by a separately derived oracle, without a
    rival assurance-owned semantic interpreter;
21. counterexamples return a causally minimal supported frontier
    represented as one unique locus, a jointly established incomparable
    set, unresolved alternative frontiers, or `indeterminate`;
22. every one of the twelve families material to the outcome has an exact
    declaration or acquisition path, and every non-material or uncovered
    family has an authority-bound disposition;
23. every material cross-frame seam preserves or lawfully translates
    identity, coordinate and basis, carried value or evidence, lifecycle
    scope, authority and provenance; and
24. no consumer-specific architecture, renamed local topology, runtime
    object or component roster is inferred from the generic set.

A project-defined frame configuration closes against REFERENCE_FRAME, the
selected complete method cut and its cited existing project authorities. It
need not claim conformance to this optional profile (P6).

## 23. Source dispositions

Rows of rc.2 `STDO_REFERENCE_FRAME_BASELINE.md` (anchors into that member).
Every conserved row is restated in tenant text at its locus; a route is
provenance only. Rows that land in ASSURANCE or EVALUATION are listed here
and in those members' tables.

| Anchor | Disposition | Locus |
|---|---|---|
| #canonical-compression | conserved; the testing-frame evidence topology moves to ASSURANCE §7 with the frames | §1; ASSURANCE §7 |
| #status-and-authority-boundary | conserved; the ownership table is rewritten onto tenant members, and the owners DESIGN_MODULE, IDENTITY and RELEASE are linked | §2 |
| #engagement-applicability | conserved; direct entry itself is ACTIVATION §1, and the profile's additions are restated here | §3 |
| #empirical-revision-boundary | conserved | §4 |
| #profile-terms | not applicable: heading with no claim text (17 bytes); its children are disposed individually | §5 |
| #engagement-frame | conserved | §5 Engagement frame |
| #specialist-frame | conserved | §5 Specialist frame |
| #generic-specialist-frame-family | conserved | §5 Generic specialist-frame family |
| #testing-frame | conserved; defined in tier 2 because the testing frames use it | ASSURANCE §7 |
| #authoritative-product-path | conserved; defined in tier 2 because the testing frames use it | ASSURANCE §7 |
| #material-combinatorial-complexity | conserved; defined in tier 2 because the testing frames use it | ASSURANCE §7 |
| #executive | conserved; the proxy is admitted under EVALUATION §5 and ACTIVATION §1 | §5 Executive |
| #executive-attention-evaluation-and-action | conserved; the three duties, the no-mutation rule, the attention cycle and the severity-versus-decision ledger rule | §6 |
| #event-driven-executive-attention | conserved | §6 Event-driven attention |
| #executive-drift-locks | conserved; the five locks as a table, with their failure consequences | §6 Drift locks |
| #product-chain-basis | conserved; the role map lives in the basis (PRODUCT_DEFINITION §7) | §6 Product-chain basis |
| #worker | conserved | §5 Worker |
| #reviewer | conserved | §5 Reviewer |
| #technical-triage-severity-priority-and-boundary-effect | conserved; the per-result projection is EVALUATION §4 | §5 Technical triage, severity, priority and boundary effect |
| #work-result | conserved; the total mapping is ACTIVATION §3's construction availability refinement, and the variant readings, refusal exclusion and C/J/O reuse are restated here | §5 Work result |
| #exact-candidate | conserved | §5 Exact candidate |
| #baseline-adoption-projection | conserved | §5 Baseline-adoption projection |
| #non-hierarchical-frame-configuration | conserved | §7 |
| #derived-executive-frame | conserved; table of eleven elements | §8 |
| #steel-thread-delivery | conserved | §8 Steel-thread delivery |
| #derived-worker-frame | conserved; table of eleven elements | §9 |
| #derived-reviewer-frame | conserved; table of eleven elements | §10 |
| #derived-generic-specialist-frame-set | conserved; all twelve families as a table | §11 |
| #derived-product-testing-frame-set | conserved; the frame set in tier 2, available and activated only where the governing configuration or work authority selects it, as the predecessor's "when this profile supports" required; its relation to the Proof family here | ASSURANCE §7; §11 Relation to the testing and interface frames |
| #derived-user-acceptance-frame | conserved | ASSURANCE §7 User-acceptance frame |
| #derived-end-to-end-frame | conserved | ASSURANCE §7 End-to-end frame |
| #derived-integration-frame | conserved | ASSURANCE §7 Integration frame |
| #derived-unit-test-frame | conserved | ASSURANCE §7 Unit frame |
| #combinatorial-coverage-and-testing-value-index | conserved | ASSURANCE §8 |
| #legitimate-path-and-technical-debt-erasure | conserved | ASSURANCE §9 |
| #testing-evidence-composition | conserved | ASSURANCE §10 |
| #assurance-subject-acquisition-and-evaluation | conserved | ASSURANCE §11 |
| #counterexample-localization | conserved | ASSURANCE §12 |
| #derived-end-to-end-interface-integration-frame | conserved; the frame identity is unchanged and still resolves in the reference-frame-evaluation context; its relation to the generic families is here | ASSURANCE §13; §11 Relation to the testing and interface frames |
| #interface-integration-claim-boundaries | conserved | ASSURANCE §13 Claim boundaries |
| #interface-integration-obligations | conserved | ASSURANCE §13 Obligations |
| #computational-whole-path-evaluation | conserved; the family names of the composition are here | ASSURANCE §13 Computational whole-path evaluation; §11 |
| #interface-integration-qualification | conserved; all ten cases | ASSURANCE §13 Qualification |
| #complete-engagement-transition | conserved | §12 |
| #1-existing-authority-selects-the-basis | conserved | §12 step 1 |
| #2-executive-activates-worker | conserved | §12 step 2 |
| #3-worker-returns-to-executive | conserved | §12 step 3 |
| #4-executive-evaluates-the-work-result | conserved | §12 step 4 |
| #5a-candidate-does-not-require-independent-review | conserved | §12 step 5A |
| #5b-candidate-requires-independent-review | conserved | §12 step 5B |
| #6-reviewer-returns-to-executive | conserved | §12 step 6 |
| #reviewer-result-and-triage-projection | conserved; the projection table is tier-1 law with assessor and decision owner in place of Reviewer and Executive | EVALUATION §4 Result and triage projection; §12 step 6 |
| #7-executive-disposes-and-checkpoints | conserved | §12 step 7 |
| #executive-promotion-constraint-projection | conserved; all four rows | §12 Promotion constraint projection |
| #handoff-projection | conserved; all eight projections | §13 |
| #coverage-application | conserved; all fourteen rows | §14 |
| #missing-frame-and-re-entry-application | conserved; the order is REFERENCE_FRAME §10 with the profile's two specific steps stated | §15 |
| #product-owned-adoption-or-project-defined-configuration | not applicable: heading with no claim text (59 bytes); its children are disposed individually | §16 |
| #existing-authority-selects-the-configuration | conserved | §16 Existing authority selects the configuration |
| #adopt-this-baseline | conserved | §16 Adopt this baseline |
| #define-a-project-configuration | conserved | §16 Define a project configuration |
| #extension-versus-replacement | conserved | §16 Extension versus replacement |
| #actor-binding-and-independence | conserved | §17 |
| #profile-qualification | conserved; all twenty-six trial obligations | §18 |
| #baseline-specific-project-basis-additions | conserved; the block heading reads "Executive Baseline Adoption Additions" | §19 Project-basis additions |
| #baseline-specific-activation-additions | conserved; the three frame additions as a table | §19 Activation additions |
| #failure-classification | conserved; all twenty-eight rows | §20 |
| #anti-patterns | conserved; all thirty-two | §21 |
| #closure | conserved; all twenty-four conditions | §22 |
