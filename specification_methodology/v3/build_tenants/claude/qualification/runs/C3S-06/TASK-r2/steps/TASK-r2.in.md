STEP TASK-r2 | cap 110000 bytes | measured 86288 bytes | fits
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
# Reference frame configuration

Task: Propose and justify a configuration for remaining multi-part work across actors with stated capabilities and context capacities, with each activation, its inputs and bytes, its result and where it goes, the dependency order, what each exchange carries and who holds each effect authority; judge a familiar proposal and its optimality claim; and evaluate one stated check with its result value and what was not performed.

Purpose: The owning sections for transitions, intake, configuration with its optimality rule, roles and delegation, context construction with the size measurement, fit test and acquisition, the activation packet, closed results and reuse, construction availability and effects as the step result mappings, finite attention, capability fit and no assumed hierarchy, authority kinds and the kinds of independence, independent assessment and adequate attention, the executive configuration as one example, and the core result algebra with its conjunction.

Each excerpt below is a verbatim copy of one owning section of a member
of this method. The `Source:` line before it names the member and the
section's anchor, and gives the SHA-256 of the whole owning member. The
owning section decides; this frame owns no determination. Links inside
an excerpt are relative to the owning member's directory.

Routes, in order:

1. [ACTIVATION.md#transitions](../ACTIVATION.md#transitions)
2. [ACTIVATION.md#intake](../ACTIVATION.md#intake)
3. [ACTIVATION.md#configuration](../ACTIVATION.md#configuration)
4. [ACTIVATION.md#roles-and-delegation](../ACTIVATION.md#roles-and-delegation)
5. [ACTIVATION.md#2-context-construction-under-an-envelope](../ACTIVATION.md#2-context-construction-under-an-envelope)
6. [ACTIVATION.md#7-closed-result-and-reuse](../ACTIVATION.md#7-closed-result-and-reuse)
7. [ACTIVATION.md#construction-availability](../ACTIVATION.md#construction-availability)
8. [ACTIVATION.md#effects](../ACTIVATION.md#effects)
9. [REFERENCE_FRAME.md#rf-002-finite-attention](../REFERENCE_FRAME.md#rf-002-finite-attention)
10. [REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy](../REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy)
11. [REFERENCE_FRAME.md#rf-012-closed-results](../REFERENCE_FRAME.md#rf-012-closed-results)
12. [REFERENCE_FRAME.md#rf-014-capability-fit](../REFERENCE_FRAME.md#rf-014-capability-fit)
13. [REFERENCE_FRAME.md#11-the-activation-packet](../REFERENCE_FRAME.md#11-the-activation-packet)
14. [EVALUATION.md#3-independent-assessment](../EVALUATION.md#3-independent-assessment)
15. [EVALUATION.md#frame-qualification](../EVALUATION.md#frame-qualification)
16. [EXECUTIVE_BASELINE.md#the-executive-configuration](../EXECUTIVE_BASELINE.md#the-executive-configuration)
17. [FOUNDATIONS.md#authority-kinds](../FOUNDATIONS.md#authority-kinds)
18. [FOUNDATIONS.md#disjointness-and-independence](../FOUNDATIONS.md#disjointness-and-independence)
19. [FOUNDATIONS.md#results](../FOUNDATIONS.md#results)
20. [FOUNDATIONS.md#conjunction-of-results](../FOUNDATIONS.md#conjunction-of-results)

Size of this frame: 80897 bytes.

Source: ACTIVATION.md#transitions sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Transitions

Construction moves work from a current state towards a destination
(P0, P2). The current state is the material state of the workspace and
its authoritative inputs, together with what is justifiably known about
that state, with the unknowns explicit. The work state of §5 records it:
the workspace, the governing basis, and the closed results and judgments
that still apply, with the residuals and the uncertainty over external
effects as the explicit unknowns. An actor's context is an account of the
current state, not the state itself
([§5](#the-workspace-and-an-actors-account)) (P3, P5).

The destination is defined by constraints: the selected outcome with its
acceptance conditions (Outcome U, [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology))
and the governing obligations the work must keep. It names no single
state: its acceptance conditions admit several realised states. Its
owning authority defines it (P2, P6).

A transition is a bounded change from the current state to a next state,
carried out by one step. Where the work exceeds one activation's capacity,
the outer transformation towards the destination is refined into a series
of bounded transitions under §4 Refinement, each carried out by its own
step; work that fits one activation is a single transition. Each
transition binds the obligations it must preserve: the outer obligations
of the destination and of the governing relations it affects, as far as
they apply to it. A step's intake binds the current state, the
destination and the obligations: the governed outcome names the
destination, or the prerequisite towards it, that the step serves; the
exact subject and basis identify the current state it starts from; and
the affected relation set with its governing invariants holds the
obligations it preserves (Intake below; P0, P4a).
Transitions compose only as §4 Refinement permits.

Discovery. Construction, observation and evaluation change the current
state and what is known about it. A new observation may add obligations,
which join the known work, or invalidate a claim, which is re-established
or withdrawn before anything relies on it (§7). Discovery can enlarge the
known work while knowledge improves (P5, P4b).

Open work outside attention. An obligation outside a frame's current
attention stays open. A bounded view disposes of none of the work it
excludes, and the next decision keeps its material dependencies on that
work (P4b, P6).

Destination change. An authorised change may revise the destination. The
change follows its owning authority and re-enters at the owning relation
(§4). A revised destination does not establish that the previous
destination was reached, and a candidate that satisfies the revised
destination is no evidence that it satisfies the previous one (P2, P6).

Completion. Work is complete only when sufficient evidence shows that the
current state satisfies the applicable destination and its acceptance
conditions; accepting that claim is the decision owner's disposition
(§3 Disposition). An empty list of known work, a count of closed or
remaining items, or the absence of a recorded counterexample does not
establish completion (P6;
[RF-015](REFERENCE_FRAME.md#rf-015-residual-uncertainty)).

Stops. Work that cannot continue ends in an explicit stop that names its
cause: a step that cannot deliver its output stops with a value of
construction availability other than `candidate_ready`, and a declared
ambiguity that halts the work or exceeds the step's authority stops it
with `blocked` or `escalated` (§3). A refused admission or activation
stops the work without creating a step (§3 Admission and activation).
The work state (§5) retains the unresolved outcome, the residuals and the
obligations still owed. A stop reaches no destination and discards none
of these (P4b, P5).

Progress. Progress is judged against the selected outcome and the
evidence for it, as §5 defines progress, not by the number of remaining
items alone: discovery
can raise that number while the work moves towards the destination (P2).

Purpose and material relation: finite context and attention (P0) mean
that an outcome beyond one activation is reached through bounded steps.
Binding the destination and the preserved obligations at each transition
keeps the outer contract through that decomposition. Keeping completion,
destination change and stops apart prevents a count, an exhausted list or
a revised destination from standing in for evidence that the applicable
destination is satisfied (P2, P6). The state, the destination and the
obligations are those that the intake and the work state already bind; no
further carrier is required. This account is new in this corpus.


Source: ACTIVATION.md#intake sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Intake

A step is activated from an intake sufficient to reconstruct its governing
relations without conversation history, commentary or a prior actor's memory
(P0, actor-change premise). The intake names:

- the governed outcome or decision: the selected outcome, admitted
  prerequisite or experiment it serves (P2);
- the exact workspace subject and basis, and the inputs it may acquire,
  each by identity and hash or by an input commit;
- the evaluation or evaluation family the step performs and its result
  algebra: the core of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) or
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
([DESIGN_MODULE](DESIGN_MODULE.md)). Conserves
[UP-020 intake](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#sufficient-execution-intake),
[UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018)
and the engagement basis (rc.2 RF #establish-the-evaluation-basis).


Source: ACTIVATION.md#configuration sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Configuration

A configuration allocates a task's responsibilities and information
exchanges to frames; activation binds an actor to each frame (§2). It
spans the task's work. The active frame configuration of
[FOUNDATIONS §2](FOUNDATIONS.md#frame-objects) is the part of it used for
one evaluation or decision (P0, P6).

Allocation. The allocation is derived from the task's operations, the
dependencies among them, the capabilities of the available actors and the
required assurance. These conditions constrain a configuration without
determining it. One frame or several, fixed or adaptive allocation, a
hierarchy, peer coordination, or an arrangement that changes as actors
allocate work within their contracts may each be adequate. The method
prescribes no role inventory, hierarchy, coordinator or actor sequence
(P0, P2; [RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality)).

Explanation. The design that selects a configuration explains its
allocation, including the material resource limits it assumes, such as
context, attention, time and spend, and its assumptions about failure. The
explanation is recorded in the existing design, frame declarations and
work records; no separate configuration carrier is required. It is
proportional (§6): for a direct entry, the intake states it, its
capability envelopes carrying the resource limits and its stale,
out-of-scope and re-entry conditions the failure assumptions (P2, P6).

Direct entry. A one-frame configuration is lawful. One directly
authorised task that fits a sufficient frame may be entered directly, as
Roles and delegation below states, subject to any separately required
assessment (P0, P2).

Evaluation of a configuration. A configuration is evaluated against the
task, its dependencies, the actors' limits, the authority it applies and
the required assurance. Its labels, its topology, and the presence or
absence of a coordinator or of familiar roles neither accept nor reject
it (P1, P6).

Distinct relations. Within a configuration, functional decomposition,
communication, authority and evaluation dependency stay distinct relation
structures under [RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy),
which owns that rule. Naming or selecting a frame grants no authority
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds);
[RF-006](REFERENCE_FRAME.md#rf-006-authority-conservation)): each
activation binds its subject, result algebra, actor capability and
admitted authority through its intake (Intake above) and its activation
(§2).

Reconfiguration. The allocation, and every reconfiguration, preserves the
material dependencies, the outstanding obligations, the effects,
including those of unknown completion, the admitted authority and the
required independence. A reconfiguration is any change of allocation
during the work, including actors redistributing work among themselves
and the changes §4 Reconfiguration selects after a result. An outstanding
obligation and the results that depend on it move with the work. An
effect of unknown completion is resolved sufficiently for the next
dependent action before that action (§3 Effects, §5). Required
independence keeps its authorship and evidence conditions
([EVALUATION §3](EVALUATION.md#3-independent-assessment)), which a fresh
context alone does not meet. An adaptive or self-organised arrangement is
exempt from none of these conditions (P4b, P5, P6).

Coordination across tasks. Where a configuration separates carrying out a
bounded change from managing delivery across successive tasks, the frame
that manages delivery, a coordinator, keeps the longer-term outcome. It
decides from a sufficient bounded view of the closed results of the task
frames (§7), not from their working context. When a decision needs
information that view lacks, the coordinator acquires it through its
permitted frame inputs or requests a further bounded evaluation. Missing
information is never assumed favourable. A task result never omits a
blocker material to delivery: a compact result keeps every residual and
stop material to delivery, and its size is no evidence that none exists
(P0, P4b, P6).

Optimality. Adequacy and optimality are separate claims. A claim that a
configuration is optimal is relative to stated objectives, constraints and
comparison scope, and rests on evidence for that comparison. Familiarity,
persistence or self-organisation is no such evidence. Different
objectives or actor models can favour different configurations (P2, P6).

Example. The executive configuration, which the
[executive baseline profile](EXECUTIVE_BASELINE.md) defines, is one
configuration, for task-based work in which a bounded change and delivery
across tasks need separate attention. It allocates construction,
assessment and disposition (Roles and delegation below) to three frames: a
Worker frame, specialised as Writer for documents and records, constructs;
a Reviewer frame assesses; an Executive frame keeps the longer-term
outcome, selects the next work and disposes within its decision grant, and
mutates nothing. That profile owns its frames, their grants, limits and
prohibitions, and its explanation; they apply where it is selected. It is
not the method's default. A configuration with other frames, names or
topology is evaluated as Evaluation of a configuration above states.

Purpose and material relation: finite context and attention bound each
responsibility (P0); dependencies between tasks require exchanges and
compatible results (P4a); and fallible actors with incomplete knowledge
require checking and recovery (P5, P6). These conditions constrain a
configuration without determining it, so the method states what every
allocation preserves and leaves the arrangement to the design. A
coordinator that decides from a bounded view relies on what the view
holds, so a blocker missing from a task result would be read as absent
(P4b). The material relation is whether an allocation or a reallocation
can drop an obligation, an effect or a required independence, move
authority with position in a decomposition, or hide a blocker from the
decision that needs it. This law is new in this corpus.


Source: ACTIVATION.md#roles-and-delegation sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Roles and delegation

Roles are relations over steps that a configuration allocates
(Configuration above), not kinds of actor and not a fixed inventory.
Where a configuration's operations include construction, assessment or
disposition, this member names the responsibility for each: a
constructor owns the bounded implementation and its self-review; an
assessor evaluates a frozen candidate independently; a decision owner
disposes. A configuration may allocate other responsibilities. Where
independent assessment supports promotion, the assessor evaluates the
exact live subject, its authority paths, proof and installed state, not
the constructor's summary (EVALUATION §3). This preserves the
independent-review relation and prescribes no actor count: one actor may
occupy different roles across different claims when independence for the
assessed claim is preserved; no role name confers an operation
([RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality);
P6; provenance rc.2 SPEC_METHOD #construction-assessment-and-delegation).

The governing authority relation declares whether a bounded proxy may
accept and advance routine actions. A proxy may accept preservation,
require local repair, reject a violating candidate and advance to the next
already-authorised action. It cannot change the governing outcome's
meaning, the requirements, the governing authority or the accepted design;
such a change re-enters at its owning relation (EVALUATION §5). Human
ceremony is not required at every transition when the governing basis, the
affected cone, the decision envelope and the re-entry conditions are
already accepted; this delegation does not weaken direct human acceptance
where the governing product or release law requires it (P6).

When one capable context has sufficient existing work authority, exact
intake and operation grant, it may enter directly as constructor. No
coordinating activation is required solely to appoint that constructor.
The applicable configuration (Configuration above) selects
coordination when material contexts, authority, capability or required
independence need it; a role or frame name alone does not create that
need. Direct entry preserves
execution-contract admission (Admission above), the smallest lawful
carrier, the required assessment and the reserved decisions; it permits
bounded work and condition-based result recording, not self-acceptance at a
boundary owned elsewhere (P0, P6).

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Actual role transitions are recorded in the existing
work carrier; a status change alone requires neither a new grant nor
rehashing an unchanged subject. A material change to the operation, the
subject, the territory, the authority or the validity conditions requires
the affected binding to be resolved before effect. Where the selected
configuration restricts its coordinating role from mutation, as the
executive configuration (Configuration above) restricts its Executive,
the restriction that the coordinating role mutates nothing remains
applicable; an operation grant covering the sequence does not lift it
(P6, P3).


Source: ACTIVATION.md#2-context-construction-under-an-envelope sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

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
   ([RF-004](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-004-irrelevance-exclusion)).
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
   that exceeds it would be cut without record (RF-014). It applies only
   there, because a resource control applies only through a selected frame
   and its owning scope
   ([REFERENCE_FRAME §4](REFERENCE_FRAME.md#frame-set-selection)), and a
   declared capacity is such a control: the measurement tests that
   capacity, is no budget, and is not a universal measurement gate (P0,
   P2). Where B declares no context capacity, no measurement is
   required, and the other conditions of RF-002 still apply. The size
   shows fit and nothing else: whether the actor attends adequately to a
   context that fits is decided by actual-use evidence under
   [EVALUATION §7](EVALUATION.md#frame-qualification). The envelope's
   other dimensions are fitted as RF-014 states; time, spend and other
   resource limits are those of the selected execution binding (§6).
   If the context fits, activate. If it does not, one or more of these, in
   combination: refine the outer contract into steps whose contexts fit
   (§4); sequence activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return `out_of_frame`
   ([§3 Admission and activation](#admission-and-activation)). Silent
   omission to fit is never one of them
   ([RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit)).
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
(§1 Configuration). A derived surface is material derived from owning
sources by copying, projection or compression, such as a projected frame
for a task; it names its sources and owns no determination. Where a derived surface whose sources
are current serves the task, the actor acquires it. For another task, or
where the derived surface is stale, missing or insufficient for a named
unresolved question, the actor acquires the deciding owner sections
directly: the owning sections that decide the task's questions, which are
declared inputs of the selected basis. Only material in the exact selected
basis is acquired: where that basis has no derived surface for the task,
its exact owner sections are used, and a candidate source, a version-line
selector or another basis is no substitute for it
([FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)).
The actor reads the selected material and the actual subject, and follows
the material source and coupled-obligation references the task needs
(step 2; RF-003); presence of the corpus is no reason to read it (step 2;
RF-004). Before any dependent action, a missing binding is returned with
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

The operation that joins AC-010, AC-011 and RF-002/003/004/014/017 into one
procedure is new in this corpus (P0). The method does not require proving
that no undiscovered material relation exists
([RF-003](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency)).
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


Source: ACTIVATION.md#construction-availability sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Construction availability

A step's output is a candidate until evaluated (FOUNDATIONS §3, P0): the
constructed subject of a constructing step, or the closed results of an
assessing step. Construction availability records whether that output
exists (P5, P6; provenance
[work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result)):

| Value | Core value | Ground |
|---|---|---|
| `candidate_ready` | satisfied | an exact candidate and its transition evidence are available |
| `refused` | falsified | lawful activation occurred, and a governing prohibition or an owner-valid construction refusal defeats the requested construction; the prohibition or refusal is the counterexample |
| `incomplete` | falsified | the lawfully activated step stopped without its output, because an evaluation the output needs was not performed or could not be decided on the admissible evidence, or bounded execution ended first; the stop basis is the counterexample, and it and the residuals name which |
| `re_entry_requested(authority)` | out_of_frame | a material decision the step needs lies outside its grant; the value names the owner of that decision |
| `re_entry_requested(basis)` | invalid_basis | the activated basis can no longer support the work |

The mapping is total and exclusive after lawful activation: the cause of
the stop selects the value, and payload wording, stop timing or actor
preference cannot select another. A mismatch known during admission or
activation is no value of this refinement, because no step exists; it
takes its outcome under Admission and activation above.

`satisfied` here establishes availability only and never counts toward the
candidate's fitness or acceptance (FOUNDATIONS §4 Results).

`incomplete` maps to `falsified` only for "a candidate is available", never
to `indeterminate`. The step's evaluations keep their own results: each
evaluation it performed returns its core value, `indeterminate` where the
admissible evidence could not decide; each evaluation it planned and did
not perform has no result, and its work state (§5) carries it as a
residual with the capability or the execution left unfinished
(FOUNDATIONS §4 Results, the third case of the boundary). An evaluation
not performed thus stays distinct from one whose evidence cannot decide
(P5, P6).

An assessing step that ends `incomplete` leaves each criterion it did not
evaluate not performed: no result, never `falsified`. The `falsified` of its
availability concerns its own output, never the subject under assessment
(P6).

The cause of a re-entry request is part of its value, because a re-entry
request without its cause would map to `out_of_frame` or to
`invalid_basis` according to that cause, and a refined value maps to
exactly one core value (FOUNDATIONS §4 Results, Refinements). A stop
with both causes records both and takes `re_entry_requested(basis)`,
because a decision cannot be taken on a basis that cannot support it (P5,
P3).


Source: ACTIVATION.md#effects sha256=179a3368a8daee4eae477ace858bc77c42c1a2bc86a76293dc54c25ee759eaed

### Effects

An effectful step's intended external effect has one of three values,
mapped for the predicate "the intended effect occurred" (P5 with the
open-world premise, P6):

| Value | Core value | Ground |
|---|---|---|
| `completed` | satisfied | evidence about the subject establishes that the intended effect occurred in full |
| `not_effected` | falsified | evidence about the subject establishes that the intended effect did not occur in full; any part that did occur is named with the value |
| `completion_unknown` | indeterminate | the evidence cannot establish whether the intended effect occurred, as for an effect that began and whose end is not observed, or a request whose response was lost |

`not_effected` requires evidence about the subject. A lost response, an
absent record, or an actor's context that holds no trace of the effect is
not that evidence, and the value stays `completion_unknown`; §5 reconciles
it before any repetition or dependent action. `completion_unknown` never
maps to `completed` or to `not_effected`. The refinement is new. Its
material relation is whether an action whose external effect may have
occurred is repeated or relied on; §4 names a lost post-effect response as
a case that no added core value solves, and this refinement records it in
the existing core.


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


Source: REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy sha256=92464e86126e807e8e225a08c8d42ce929f11b823dfb07e204b34ff1b3ae57bc

### RF-009 No assumed hierarchy

Frames may relate through disjointness, overlap, refinement, restriction,
translation, temporal succession, composition or governance (§7). Parent
and child relations apply only where explicitly declared. Functional
decomposition, communication, authority precedence, frame configuration,
subject topology and evaluation dependency are distinct relation
structures; a consumer may align them where the governed subject warrants
it and may not silently treat them as one hierarchy (P3, P1; rc.2
#rf-009-no-assumed-hierarchy). Communication is the exchange of
information between frames, or between the actors activated on them. An
exchange by itself grants no authority and establishes neither a
decomposition nor an evaluation dependency (P6, P1). Communication is new
in this list. Purpose and material relation: a configuration assigns
information exchanges as well as responsibilities
([ACTIVATION §1](ACTIVATION.md#configuration)), and an exchange read as a
grant or as a dependency would move authority or change a result without a
declared relation.


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


Source: EVALUATION.md#3-independent-assessment sha256=6383bebb0238da55ec4ea779f44d077f558f0f32ccfcfbfca38845efed9946b6

## 3. Independent assessment

A constructor's self-review is construction output, not assessment. Where
promotion needs independent assessment, the assessor evaluates the exact
live subject, authority paths, proof and installed state, not the
constructor's summary (P6, and P0 with its premise that a step's output is
a candidate until evaluated; instance premise (c) of §1 Foundation to law;
conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)).

Protocol: the subject is frozen by identity before material reference
exposure; the assessor records its expectations from the governing source
before opening the candidate; it reads the subject at a named immutable
identity, never a working tree; it makes no repair; it does not assess its
own authorship. Reusing the constructor's judgment does not satisfy
independence; shared mechanical evidence may be reused, judgment may not
(ACTIVATION §7). Any post-exposure revision is a declared intervention: it
is either a method constituent with its own qualification boundary or a new
qualification subject, and it cannot retroactively make the original
frozen construction pass. This law prescribes no actor type or count,
review-round count, engine, prompt or orchestration (UP-022).

Independence rests on authorship and on the evidence conditions above, not
on a new context. The assessor may read the same governing sources as the
constructor. A fresh context alone establishes no independence, and it
supplies no review authority the author lacks: an author that opens a
fresh context to review its own candidate is still its author, and its
review is self-review, which stays construction output and cannot be
relabelled as independent assessment (P6; UP-007 applied to a fresh
context).

Independence across actor families is declared, not assumed. Whether two
activations of one model family are independent for a semantic judgment is a
policy the governing basis states for the claim; the default where it is not
stated is that they are not independent.


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


Source: EXECUTIVE_BASELINE.md#the-executive-configuration sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

### The executive configuration

The executive configuration is the configuration this profile describes,
in the sense of [ACTIVATION §1 Configuration](ACTIVATION.md#configuration).
It allocates construction to the Worker frame, specialised as Writer for
documents and records; assessment, where it is required, to the Reviewer
frame; and coordination across tasks to the Executive frame, which disposes
within the decision grant existing authority admits (§5, §8 to §10). It is
one configuration, selected where it fits the task, not an inventory of
roles that all work needs. Existing authority selects it or another
configuration under §16, and a configuration with other frames, names or
topology is evaluated against its own task as ACTIVATION §1 Configuration
states, not by its distance from this one (P0, P2, P6).

Where it is selected, every grant, duty, limit and prohibition this
profile places on its frames is in force without exception: the
Executive's prohibition on mutation (§6 No mutation while Executive), its
duties under §6 The three duties, Attention cycle, Event-driven attention
and Drift locks, and the exclusions of the Worker and Reviewer frames (§9,
§10) among them.
Selecting the configuration makes none of them optional, and no operation
grant lifts them (P6).

Explanation of the allocation. ACTIVATION §1 Configuration requires the
design that selects a configuration to explain its allocation; for this
configuration the explanation is (P0, P5, P6):

- fit: task-based work in which carrying out a bounded change and managing
  delivery across successive tasks need separate attention; where one
  sufficient frame covers the task, direct entry applies instead (§3);
- resource limits assumed: every actor has a finite context and attention
  envelope, so no frame holds the whole workspace. The Worker's context
  holds one causal cone (§9), the Reviewer's one exact claim with its
  evidence (§10), and the Executive's the outcome, the frontier and the
  closed-result ledger (§6), never the working context of an evaluator.
  The adopting Product's basis records the concrete capability envelopes
  (§16 Adopt this baseline); time, spend and other resource limits are
  those of the selected execution binding (ACTIVATION §6);
- failure assumptions: a constructor can be wrong about its own candidate,
  so its self-review is construction output and required assessment is
  independent (EVALUATION §3); a coordinator that also changed the subject
  would decide on its own effects, so the Executive makes none (§6); a
  result can become stale or bound to another subject, so the Executive
  revalidates the drift locks before activation and disposition (§6); an
  activation can fail, so a refused activation returns with its cause and
  no Worker result (§5 Work result); an effectful activation can stop
  with an effect whose completion is unknown, as where a response was
  lost, so the work result names each intended effect with its
  [ACTIVATION §3 Effects](ACTIVATION.md#effects) value, and an effect of
  unknown completion is reconciled under
  [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart), sufficiently
  for the next dependent action, before work is reactivated or that
  action is taken (§12 step 4, §13); and a
  bounded view can lack what a task frame knows, so results carry every
  blocker material to delivery (next paragraph).

Coordination. The Executive is this configuration's coordinator, and
[ACTIVATION §1 Configuration](ACTIVATION.md#configuration), Coordination
across tasks, owns the rule for a coordinator's bounded view. Here that
view is the closed-result ledger (§6 Attention cycle) with the
work-result, review-result and specialist-result projections of §13. The
Executive acquires what a decision needs beyond that view through its
frame inputs (§8) or by activating a further bounded evaluation (§6). A
compact result carries every blocker material to delivery, as that rule
requires, in the residuals, stop basis and effect values of a work
result, the findings, counterexamples and residuals of a review result,
and the residuals of a specialist result (P0, P4b, P6).

This subsection is new; it has no rc.2 row. Purpose and material relation:
ACTIVATION §1 makes the executive configuration one example among lawful
configurations and leaves its frames, prohibitions and explanation to this
profile. Without the explanation the allocation could be applied where it
does not fit or read as the method's default; without the statement that
its prohibitions hold wherever it is selected, selection could be read as
relaxing them. The material relation is whether a task receives this
allocation only where it fits, and whether its prohibitions and its
reporting of blockers hold wherever it is used.


Source: FOUNDATIONS.md#authority-kinds sha256=259ef2fe5f1d6056d237c5ff0cdc0c051f89606f53e85c2137c9398cf6fafc71

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


Source: FOUNDATIONS.md#disjointness-and-independence sha256=259ef2fe5f1d6056d237c5ff0cdc0c051f89606f53e85c2137c9398cf6fafc71

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
# TASK: configure the remaining tide-table work

## Subject

Product `tide-tables` publishes a harbour authority's tide predictions for
three ports: North, East and South. The facts below are the whole subject.
The record is invented for this task and is evidence about no real product.

The product owner, Marta, admitted work item `W-12`: publish the 2027 tables
for all three ports. It states four requirements:

- R1: each port's harmonic constants are fitted from that port's 2026 gauge
  record, following the method notes.
- R2: each port's constants are assessed against that port's 2026 gauge
  record, following the method notes, by an assessor that is not the author
  of those constants. This happens before any table made from them is
  published.
- R3: every table gives heights relative to chart datum CD-2026.
- R4: the three ports are published together, by the holder of the
  publication grant.

Material, in bytes:

| Item | Bytes |
|---|---|
| 2026 gauge record: North, East, South | 70,000; 60,000; 50,000 |
| method notes (fitting and assessment) | 40,000 |
| constants, per port | 10,000 |
| port configuration `ports/<port>.yaml`, per port | 20,000 |
| table template | 15,000 |
| datum offsets `datum/cd2026.csv` (admitted by Marta) | 8,000 |
| task contract and result, per activation | 10,000 |

Dependencies:

- One port's constants depend only on that port's gauge record and the
  method notes.
- One port's tables depend only on its constants, its port configuration
  and the template.
- `north.yaml` and `south.yaml` declare CD-2026.

Actors:

- A1: an agent with a context capacity of 200,000 bytes. Its tools fit
  harmonic constants and compare them numerically with a gauge record.
- A2: an agent with a context capacity of 200,000 bytes. It has the same
  tools as A1, plus the table generator.
- A3: an agent with a context capacity of 64,000 bytes. It has the table
  generator and can edit configuration files. It cannot fit or assess
  constants.
- Ravi: an operations officer, a person. He holds the only grant to publish
  to the public portal and is available for one hour on Thursday.
- You: an agent with a context capacity of 120,000 bytes, and no fitting or
  table tools.

W-12 grants edits to `constants/`, `tables/` and `ports/*.yaml` to whichever
agent activation the configuration assigns to that work. Marta must accept
the configuration before it starts.

Last week Tomas ran a pilot for East only:

- A1 fitted East's constants and committed them as `east-c1`.
- A new A1 session, started with an empty context, compared `east-c1` with
  the 2026 East record. It returned `satisfied`, within 3 cm.
- A3 generated East's tables from `east-c1` and returned to Tomas the
  result `East tables: done, 0 errors`.
- The workspace log `tables/east/run.log` holds the line
  `WARN datum: east.yaml declares CD-2019; heights written relative to CD-2019`.
- Nothing has been done for North or South.

Tomas proposes this for the remaining work: "Use the setup we have used for
three years. A1 is Executive and holds the whole W-12 record. A2 is Writer
for all fitting and all tables. A3 is Reviewer. It is the optimal
configuration; the team knows it."

Marta asks you to propose a configuration for the remaining W-12 work.

## Instruction

1. Under a heading `Configuration`, list each activation, with:
   - its operation;
   - its actor;
   - its inputs, with their total bytes;
   - its result, and where that result goes.

   Then give the dependency order, what each exchange must carry, and who
   holds the authority for each effect, including publication.
2. Under a heading `Justification`:
   - say why this allocation fits the dependencies, the actors' capabilities
     and capacities, and R2;
   - say what you keep from the pilot;
   - judge Tomas's proposal, and his claim that it is optimal.
3. Under a heading `Check`, evaluate the predicate "the East tables from the
   pilot meet R2 and R3 and may be published". Give its result value, the
   facts that decide it, and anything you record as not performed.
4. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply. Write `none` if nothing.

Return only those four parts, in that order. Do not restate the subject.
