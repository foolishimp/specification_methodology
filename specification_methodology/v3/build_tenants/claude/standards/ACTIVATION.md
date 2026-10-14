# ACTIVATION

Tier 1. Owns how bounded work proceeds: the step (transitions from a
current state to a destination, intake, execution unit, admission,
applicability with exclusion, output, the configuration of
responsibilities over frames and its admission, roles and delegation,
recording a result without review); context construction under an
envelope, with the size measurement and fit test, acquisition, activation,
evaluation and the staleness of derived surfaces; the
refinements of the core for admission and activation and for the step's
results, and disposition; totality and refinement, with the hard stops,
licensing and approximate steps; work state and restart, with the workspace and an
actor's account; cost and proportionality, with the resource-limit law;
the closed result, its invalidators and reuse. It uses
the objects of [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology), the core result
algebra of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and the frame
object and the outcomes of `activate` of
[REFERENCE_FRAME](REFERENCE_FRAME.md) (§5). It defines the step-level
concepts it introduces, among them the current state, the destination,
the transition, the configuration, the execution unit, acquisition, the
rewrite step, the licensing law, the adequacy relation, the work state,
the actor's account, progress and churn, proportionality and the closed
result, and refines the
core for admission, activation and steps (§3); it redefines nothing those
members own. A route
written `rc.2 RF #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md` and is
provenance only.

## 1. The step

A step is the activation of one reference frame, or one declared active
frame configuration, on an exact subject (REFERENCE_FRAME §1, §11). Its
context is the projection of that activated frame to the actor; the corpus
or the workspace is never the context (P0; RF-002). Intake, admission,
applicability and activation are distinct relations inside the step even
when one invocation performs all of them.

When construction is delegated to a probabilistic or agentic worker, the
method governs the execution relation without prescribing the worker's
model, prompt, tools, internal search, process topology, repository layout
or orchestration runtime (P0; the work boundary of FOUNDATIONS §2). The
normative relation runs: accepted governing basis; bounded affected
relation set; selected computational relations; delegated execution and
decision authority; construction and self-review; independent live-surface
assessment where required; one of accept, local repair, re-enter or reject
(§3); the exact accepted checkpoint; the next already-authorised bounded
action (§5). Provenance:
[UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020).

Foundation to law. This family, transitions, steps and configuration,
covers this section and §4. Its instance premises are: (a) a selected
outcome with its acceptance conditions; (b) work that may exceed one
activation's capacity; (c) actors with declared capability envelopes; (d)
an admitted grant. They are conditions of the work this family governs,
not commitments, and do not follow from finite capacity alone. The
standing of the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P0 (recovered), P2 (independent); instance premises a, b | By P0 an actor's context is bounded, and by P2 work serves a selected destination, so work that exceeds one activation reaches its destination through bounded transitions, each binding the current state, the destination and the obligations it preserves | [Transitions](#transitions); [Intake](#intake); [Execution unit](#execution-unit) | the destination and its acceptance conditions: the owning authority of the selected outcome | 1, 5 |
| P0 (recovered), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); instance premise d | By P0 and P4b an actor cannot recover a governing relation from memory, and by P6 admission is a separate authority, so a step starts only from an intake that reconstructs its governing relations without history, and only after an admission its drafting actor does not certify; its output is a candidate with its step-produced facts | [Intake](#intake); [Admission](#admission); [Output](#output) | the carrier (ticket, sprint entry, run-scoped contract): [TICKETS](TICKETS.md) | 5, 9 |
| P1 (independent), P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premise a | By P1 a premise's form is not its truth, by P6 applicability is decided on evidence, and by P5 an unresolved premise is undecided, so applicability is decided from basis-bound facts and is itself a result in the core; an unresolved premise withholds the dependent claim and is never read as false; an excluded obligation, after a `falsified` applicability result, has no result and maps to no core value, and a `satisfied` for a disjunction that includes non-application counts toward that disjunction only | [Applicability](#applicability), with Exclusion and the core | which obligations apply to a subject: the owning evaluation and its scope declarations; a predicate declared as a disjunction that includes non-application: the owner of that predicate | 9, 6 |
| P0 (recovered), P2 (independent), P4a (independent), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premises b, c, d | By P4a responsibilities compose through declared operations and dependencies, by P6 a decision belongs to its owner, and by P0 and P5 each frame must fit a finite actor, so responsibilities are allocated to frames from operations, dependencies, capabilities and assurance; no role inventory, hierarchy or actor sequence follows; reconfiguration keeps dependencies, obligations, effects, authority and independence; a configuration is admitted only by the authority that owns the decision it makes, and its admission creates no authority | [Configuration](#configuration), with Admission of a configuration; [Roles and delegation](#roles-and-delegation) | the configuration (frames, topology, coordinator, role names) and its explanation: the design that selects it; which authority owns which decision: the method or profile that applies the rule, [EXECUTIVE_BASELINE §16](EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration) for the executive configuration; the executive configuration: [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md) | 7, 9 |
| P6 (independent), P2 (independent), P0 (recovered); instance premise d | By P6 a record is no assessment or acceptance unless the law requires one, by P2 a step with no route to the outcome is unjustified, and by P0 the record must outlive the actor, so where the applicable law requires no assessment and reserves no acceptance, the grant holder may record the conditions it found satisfied in the existing result surface without adding ceremony, because a step with no route to the outcome is unjustified; the record is no disposition and waives no condition that applies | [Roles and delegation](#roles-and-delegation), Recording a result without review | which conditions require assessment or reserve acceptance: the applicable law and the governing grant; the carrier: [TICKETS](TICKETS.md) | 9, 1 |
| P2 (independent), P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P5 (derived from P0 and P6, with P0's open-world premise); instance premise a | By P2 completion is measured against the destination, by P6 and P5 only evidence can establish it, and by P4b a stop's cause persists, so completion needs evidence against the applicable destination; a count, an empty list or a revised destination is no such evidence; a stop names its cause and keeps what is owed | [Transitions](#transitions): Completion, Destination change, Stops | accepting a completion claim: the decision owner ([§3 Disposition](#disposition)) | 1, 5, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P2 (independent), P6 (independent); instance premise d | By P5 a non-satisfied result leaves the outcome undecided or failed, by P2 work continues only toward the outcome, and by P6 a hard stop is no policy decision, so every non-satisfied result has a named next move, an explicit unknown class included, and reconfiguration follows the cause; a hard stop holds whatever the risk appetite | [§4](#4-totality-and-refinement), Hard stops and the paragraphs before Refinement | the ambiguity policy and its risk appetite: the project's declared policy ([SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)) | 5 |
| P4a (independent), P1 (independent), P6 (independent); instance premise b | By P4a a step composes only under declared laws, by P1 structural success does not establish meaning, and by P6 preservation needs evidence, so a refinement or rewrite step is admissible only under a law declared for its subject, and each layer discharges what it preserves; a refinement is faithful only when its steps are exact and each output meets the next step's declared domain; a composite with an approximate step is adequate only within its stated adequacy relation and end-to-end bound | [Refinement](#refinement) | the laws declared for a subject: the subject's owner | 3, 4 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P3 (independent), P6 (independent); instance premise d | By P4b a partial commit would leave facts that later steps cannot reconcile, by P3 the relation binds one basis identity, and by P6 admission is the owner's act, so admission of a material transition derives and validates the complete enclosing relation on one basis identity and commits all of it or none; qualification covers every admission owner and supported boundary | [Complete enclosing-relation admission](#complete-enclosing-relation-admission); [Standing structural qualification](#standing-structural-qualification) | the supported boundaries and the operating or threat model: the accepted design | 4, 9 |

[SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method),
outside this member, binds the step to that member's terms and applies
these rows, except its delivery priority, which family F5 traces at §6.
Its execution relation applies the second and fourth rows; its binding of
the selected outcome to the product outcome, and of the owning relations
and re-entry conditions to the chain's layers and change classes, applies
the first and sixth rows; and its rule that the configuration sets the
frames for construction, assessment and disposition, the consumer of a
step's return and any coordinator applies the fourth row. Two of its
statements apply other sections: the step's results in the core apply
§3, which family F3 traces, and the computational relations, actors and
resource limits of the tenant's binding apply SPEC_METHOD §11, which
family F10 traces. SPEC_METHOD §8 keeps its owner.

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

### Execution unit

The execution unit is the smallest coherent causal dependency cone capable
of delivering working behaviour while preserving every affected governing
relation. It need not coincide with one function, file, module, ticket
field or design document (P0, P4b; provenance rc.2 SPEC_METHOD
#bounded-causal-construction). A seam whose far side can causally affect,
or be affected by, the action is inside the cone unless the basis
establishes that it cannot participate. Unrelated incompleteness outside
the cone is recorded as repricing input and does not block the bounded
claim. The cone is the seed set Z of §2; the context is its projection.

### Admission

Drafting a step's contract and admitting it are distinct relations, even
inside one invocation that drafts, validates, admits and executes; no
separate turn, carrier or approval ceremony is implied by the distinction.
A contract carries at minimum the states drafted, admitted, rejected and
superseded ([TICKETS §5](TICKETS.md#execution-contract-admission)).
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
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
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
its cause ([§3 Admission and activation](#admission-and-activation)).
Provenance:
[work-carrier-to-execution rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)
and
[execution contract admission](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-contract-admission);
the selection of the carrier (ticket, sprint entry, run-scoped contract)
is tier-2 law in the [TICKETS](TICKETS.md) member, which disposes those rows.

### Applicability

The owning evaluation and scope declarations determine which frame
obligations apply to the exact subject. Their declared predicates are
evaluated from sufficient basis-bound facts: a true predicate requires the
applicable evaluation and its result; a false predicate excludes only that
obligation, under its cited authority; a missing or ambiguous premise
leaves applicability unresolved, not false. A frame name, an available
tool or a listed family triggers no activation by itself. Where
applicability needs residual semantic judgment, that judgment and its
evidence are retained as a judgment, never represented as a computed fact
(P6, P1). A required result that is absent, stale, bound to another subject
or basis, or incapable of establishing its claim cannot satisfy a dependent
conjunction ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results));
unresolved applicability withholds the dependent claim until
sufficient evidence or the owning decision resolves it; other applicable
constraints stay in force even if only one evaluation detects them (P4b,
P5). Qualification of an applicability rule distinguishes true, false and
unknown premises, required results that are missing or bound to the wrong
subject, and a sufficient positive result, under a finite declared fixture;
a rule that always skips or always activates cannot satisfy those distinct
expected outcomes (EVALUATION §7; rc.2 RF
#applicability-and-required-results).

Exclusion and the core. Deciding applicability is an evaluation of the
predicate "the obligation applies to the exact subject", and its result is
a core value of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results): a true
predicate is `satisfied`; a false predicate is `falsified`, the
basis-bound fact that makes it false being the counterexample; a missing
or ambiguous premise is `indeterminate`, or `out_of_frame` where the
premise needs a relation the frame does not declare, and never
`falsified`. An exclusion is the state of the excluded obligation after a
`falsified` applicability result: it is no result, the obligation's own
evaluation is not performed and maps to no core value, and the obligation
leaves the required coverage of a dependent conjunction under the cited
authority of that applicability result. An obligation whose applicability is
unresolved stays in that required coverage. A predicate that its owner
declares as a disjunction that includes non-application, such as "meets
the axiom or does not apply", may be `satisfied` because the obligation
does not apply; that `satisfied` is for the declared disjunction only and
never counts toward the predicate that the obligation holds
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Predicates travel). Members, profiles and projects refer to this
paragraph for exclusions and do not decide them again (P5, P6, P1).
Purpose and material relation: an exclusion read as a result of the
excluded obligation, or a "does not apply" counted toward that obligation,
would report a skipped obligation as met; an unresolved premise read as an
exclusion would drop an obligation that may apply.

### Output

The step's output is a candidate plus its step-produced facts: judgments with
their evidence, residuals, observations, authority decisions, provenance, and
one stop state, a value of construction availability (§3). The actor's
internal path is not part of the output
and is not governed (FOUNDATIONS §2, work boundary; provenance
[Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)).

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
context, attention, time and spend, each declared as §6 Resource limits
states, and its assumptions about failure. The
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

Distinct relations. Within a configuration, the relation structures that
[RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy) lists as
distinct stay distinct; RF-009 owns that list and the rule, and this
section adds no structure to it and drops none. Naming or selecting a
frame grants no authority
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority): each activation binds its subject, result algebra,
actor capability and admitted authority through its intake (Intake above)
and its activation (§2).

Admission of a configuration. A configuration is admitted by the smallest
existing authority that owns the material decision the configuration
makes. One configuration may derive from several governing owners; each
keeps its own decision, and admitting the configuration creates no new
authority over them. An explicitly bounded proxy admits a configuration
only inside its existing grant (FOUNDATIONS §2 Authority kinds, Proxy
limit). Which authority owns which decision is a binding of the method or
profile that applies this rule; the executive configuration's binding is
[EXECUTIVE_BASELINE §16](EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration),
which refers here for the rule (P6, P2; provenance
[Existing Authority Selects The Configuration](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#existing-authority-selects-the-configuration)).
Purpose and material relation: a configuration allocates authority-bearing
responsibilities, so admitting one by an authority that does not own the
decision would move authority with position in the decomposition; the
rule holds for every configuration, so it is stated here and not only in
an optional profile.

Reconfiguration. The allocation, and every reconfiguration, preserves the
material dependencies, the outstanding obligations, the effects,
including those of uncertain completion, the admitted authority and the
required independence. A reconfiguration is any change of allocation
during the work, including actors redistributing work among themselves
and the changes §4 Reconfiguration selects after a result. An outstanding
obligation and the results that depend on it move with the work. An
effect of uncertain completion is resolved sufficiently for the next
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
accept and advance routine actions. Inside a step, a proxy so declared may
accept preservation, require local repair, reject a violating candidate
and advance to the next already-authorised action; what it cannot change,
and the re-entry such a change requires, is the proxy limit of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), which
this paragraph applies and does not restate. Human ceremony is not
required at every transition when the governing basis, the affected cone,
the decision envelope and the re-entry conditions are already accepted;
this delegation does not weaken direct human acceptance where the
governing product or release law requires it (P6).

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

Recording a result without review. Where the applicable law requires no
independent assessment and reserves no acceptance, the constructor that
holds the grant may record the satisfied bounded result, with the conditions
it found satisfied and their evidence, in the existing durable result
surface (Admission above), without adding a carrier, coordinating
appointment, review or recreated design view solely to mark completion. The
recording waives no condition that actually applies, states only
conditions that were evaluated, as an actor cannot report an evaluation it
did not perform
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed), and is
no disposition at a boundary owned elsewhere
(§3 Disposition). Where an assessment or a reserved acceptance does apply,
it stays required, and an insufficiency found during the work withholds
the dependent effect and returns the question to its owner. Carriers and
profiles refer to this paragraph and add only their own carrier binding
(P0, P2, P6; provenance rc.2 SPEC_METHOD
#construction-assessment-and-delegation). Purpose and material relation:
requiring a review or a ceremony that no law requires adds reasoning cost
without removing ambiguity (§6), while recording a satisfied result where
a review or acceptance is required would read construction as acceptance.

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
   measured, and no fit claim covers it. The measurement applies wherever B declares a
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
[RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)). Before any dependent action, a missing binding is returned with
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

## 3. Step results and disposition

A step returns its results in the core algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results): each evaluation it
performed returns one core value with its predicate and domain outcome,
and an evaluation it did not perform has no result. The outcomes of
admitting and activating a step, and the step's own outcomes, answer other
questions than its evaluations do. This section owns them as five
refinements of the core. Each names the question it answers and the
predicate its mapping is for, and maps each of its values to exactly one
core value; the predicate travels with the value, so no refinement's
`satisfied` counts toward another predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
Purpose and material relation: admission, work, decisions and effects
stand in the one core (P5, P6), so a consumer that combines them cannot
read a refused activation as a step's stop, availability as fitness or
acceptance, a carried ambiguity as resolved, or an unknown effect as none.

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| admission and activation | may the step begin | the step is lawfully admitted and activated on the exact subject and basis |
| construction availability | did the step yield its output | a candidate is available |
| disposition | what the decision owner does with an assessed candidate | the candidate is accepted at its declared boundary |
| ambiguity outcome | what happened to a declared ambiguity | the declared ambiguity is resolved on the exact basis |
| effects | did an intended external effect occur | the intended effect occurred |

A profile that refines these values for its own units maps each of its
values to exactly one core value under FOUNDATIONS §4 Results and adds no
core value.

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

### Ambiguity outcome

A declared ambiguity is resolved, carried, escalated or blocked, and the
outcome is recorded either way (§4, which also names the hard stops;
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
applies this to the method's chain of authority surfaces). Each outcome
maps to the core for the predicate "the declared ambiguity is resolved on
the exact basis" (P5, P6):

| Outcome | Core value | Ground |
|---|---|---|
| `resolved` | satisfied | a decision was taken under the policy that permits lawful probabilistic processing, or by human adjudication, and recorded |
| `carried` | falsified | policy permits work to continue with the ambiguity open; the open ambiguity is the counterexample, and it stays a recorded residual that names the evidence or decision that would resolve it |
| `escalated` | out_of_frame | policy or risk appetite reserves the decision to human adjudication, an authority the step does not hold; the value names that authority |
| `blocked` | falsified | the ambiguity stays unresolved, and policy or a hard stop (§4) halts work at it; the open ambiguity is the counterexample, and the value names the halting condition and what would lift it |

An open ambiguity is a known state of the exact basis, so `carried` and
`blocked` decide the predicate false; neither is `indeterminate`, whose
evidence cannot decide the predicate. Each keeps its domain outcome with
the value: `carried` with what would resolve the ambiguity, `blocked` with
the halting condition and what would lift it (FOUNDATIONS §4 Results,
Recording). No outcome other than `resolved` maps to `satisfied`, so a
dependent claim cannot rest on a carried, escalated or blocked ambiguity
as if it were resolved. The mapping is new; it places ambiguity outcomes
in the one core, which FOUNDATIONS §4 Results requires of every outcome
(P5, P6).

### Effects

An effectful step's intended external effect has one of three values,
mapped for the predicate "the intended effect occurred", that is, the
declared outcome of the effect is attained. The value turns on what the
admitted evidence establishes about that outcome (P5 with the open-world
premise, P6):

| Value | Core value | Ground |
|---|---|---|
| `completed` | satisfied | evidence about the subject establishes that the intended effect occurred in full and that the effect has ended |
| `not_effected` | falsified | evidence about the subject establishes that the declared outcome is not attained and that no later completion of the effect can attain it, for example where no effect began, the effect ended short, an interval that the declared outcome bounds has closed with part of it not done, or the part already done has itself made the declared outcome unattainable, as when it destroyed what the outcome needed; any part that did occur is named with the value |
| `completion_unknown` | indeterminate | neither of the other values is established: the evidence cannot decide whether the intended effect has occurred or will occur, as for a request whose response was lost with no counterexample observed; or the evidence shows the intended effect in full while the effect may still be acting, and the outcome stays undecided until what the effect leaves on the subject is settled; its residual names the observation that would decide |

`not_effected` requires evidence about the subject. A lost response, an
absent record, or an actor's context that holds no trace of the effect is
not that evidence, and the value stays `completion_unknown`.
`completion_unknown` never maps to `completed` or to `not_effected`.

Whether the effect has ended is a second question beside the predicate
above, and it enters the value only as a conjunct of `completed`. An
effect has ended where evidence about the subject establishes
that it no longer acts on the subject or that it never began. Where an
effect began and the evidence does not establish its end, the end is not
established, and that is recorded beside the value as a residual naming
the observation that would establish it. The end never decides a
`not_effected` value and is never folded into one: when an interval that
the declared outcome bounds has closed with part not done, the value is
`not_effected` while the effect may still be acting. The residual does
not weaken the counterexample, and the counterexample does not resolve
the residual. `completed` alone requires the end established, so a
counterexample stands without proof that the effect has ended, while
success is never claimed for an effect that may still be acting
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Standing).

An effect of uncertain completion is one whose value is
`completion_unknown`, or whose value is `not_effected` with its end not
established. §5 reconciles it, sufficiently for the next dependent
action, before any repetition or dependent action. A `not_effected`
value licenses neither treating the effect as absent nor repeating it
while its end is not established.

The refinement is new. Its material relation is whether an action whose
external effect may have occurred is repeated or relied on; §4 names a
lost post-effect response as a case that no added core value solves, and
this refinement records it in the existing core. Keeping the end of the
effect beside the value keeps two facts that one value would merge: a
counterexample already established for the declared outcome, and an
effect that may still be acting.

## 4. Totality and refinement

Next moves after any non-satisfied result are named in advance: continue
within the current contract when supported; refine; recover; yield; re-enter
the owning relation; terminate. Each admitted condition class has a declared
next move, including an explicit unknown class. Total handling does not
claim that every external condition is recognised, that an invoked provider
terminates, or that every request can be completed. A hanging external call,
an unsatisfiable demand and a lost post-effect response are three different
cases and none is solved by adding a value to the algebra.

Which outcome of [§3 Ambiguity outcome](#ambiguity-outcome) a declared
ambiguity takes is decided by the applicable ambiguity policy and its risk
appetite, an added choice; for this method the owner of the default
policy is [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle),
and this section states none. The outcome is recorded either way.

Hard stops. Some conditions are not optional ambiguity decisions and
remain hard stops regardless of risk appetite. Typical hard-stop classes
include: a violated invariant or guarantee; an absent required authority
surface; a missing declared capability for an executional or operational
stage; an undeclared irreversible side effect; and an explicit policy gate
requiring human approval. A hard stop halts the work at its condition whatever the policy:
for a declared ambiguity, with the §3 Ambiguity outcome `blocked`;
otherwise, as a stop of [§1 Transitions](#transitions), Stops. This
section owns the hard stops;
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
applies them to the method's chain of authority surfaces (P6, P5;
provenance rc.2
[Ambiguity Governance Rule](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule)).

Reconfiguration. An out_of_frame, invalid_basis, repeated indeterminate or
incompatible result causes one of: supply the missing admissible evidence;
select another actor inside the frame's capability envelope; activate
another existing frame; refine or extend a frame declaration; revise the
frame set (REFERENCE_FRAME §10); change the evaluation; or re-enter the
governing product or method relation. The next move follows the cause; a
difficult evaluation alone does not prove that another frame is required
(P5, P2; rc.2 RF #reconfigure-when-necessary).

### Refinement

An outer transformation T: A → X with success predicates P₀ … Pₙ
is faithfully refined by steps Tᵢ when each admitted input satisfying Pᵢ
yields an output satisfying Pᵢ₊₁, retains every applicable invariant, exposes
other outcomes without coercion, and each output satisfies the next step's
declared domain and preconditions, as typed composition requires (P4a;
[AXIOMATIC_CALCULUS §5 AC-016](AXIOMATIC_CALCULUS.md#ac-016-typed-composition)).
Then a successful composite of exact steps carries P₀ to Pₙ by induction;
a composite that contains an approximate step carries only what its
end-to-end bound states (Exact and approximate steps below). A refinement
carries an earlier output to a later step other than the next only through
a declared adapter, itself a step composed under AC-016, or a declared
specialised contract, in either case one whose declared domain names what
is carried; a specialised contract is declared under its owner's exact
authority, context, basis, scope, preservation, loss, refusal and
invalidation law (P4a, P4b; provenance rc.2
[AC External Imports And Specializations](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#external-imports-and-specializations)).
Coverage of the outer obligations, correctness of the local
implications and legitimate authority are premises, not conclusions; "each
step passed" is weaker than "the outer contract was conserved". Required
coupled relations must fit together in some step; unrelated obligations stay
outside the selected context. Every seam crossing the affected set includes
its far side or states why it cannot participate
([UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017)).
Admission of a material transition is one semantic commit of the complete
transition within its enclosing relation, or none (the law below). This
generalises ODD
[graph functions](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#graph-functions),
which refine one outer vector into a small inner workflow, to any
realisation; PROFILES §2 keeps the ODD binding.

Preservation and licensing. A refinement step decomposes a transformation
into steps, as above. A rewrite step replaces a representation, a step or
a composite by another that is claimed to keep its meaning, for example
by partitioning, regrouping, reordering, merging or substituting parts.
Each refinement layer, the steps that refine one transformation, states
what it preserves of the layer above, the transformation it refines, and
discharges that obligation (P4a, P6). A refinement or rewrite step is
admissible only under the laws declared for its subject. Its licensing law is the declared
law that permits it, such as an associativity, commutativity or
equivalence law that the subject's owner declares for the subject. Where
no law is declared for the subject, only universally valid steps are
admissible: steps that hold whatever laws the subject has. A step that
is neither licensed nor universally valid, such as a partition or
regrouping that no declared law permits, is inadmissible, and so is a
refinement or rewrite that relies on it (P4a, P1).

Exact and approximate steps. An exact step preserves meaning: under the
subject's declared interpretation, its output means what the material it
replaces means, and an exact refinement step carries Pᵢ to Pᵢ₊₁ without
approximation (P1). Faithful refinement, defined above, is refinement by
exact steps. An approximate step does not preserve meaning exactly. It
states its adequacy relation, which says how close its output must be to
the exact result to be close enough for the outer contract, and the
composite that contains it states an end-to-end bound, which limits how
far the whole composite may depart from the outer obligation and is
argued for that composite. Such a composite is not faithful; it is
adequate within its end-to-end bound and establishes nothing beyond that
bound. A fixed tolerance at each step does not compose into an
end-to-end bound, because deviations that each stay within the tolerance
can accumulate across steps, so the induction above applies to exact
steps only. A step that is neither exact nor approximate with its
adequacy relation and an end-to-end bound for its composite is
inadmissible: a composite that relies on it is neither faithful nor
adequate within a bound (P4a, P6).

Purpose and material relation: a decomposition or rewrite that changes
meaning, or approximations whose deviations accumulate, would let a
composite whose every step passed violate the outer contract (P4a, P1,
P6). The material relation is whether the composite still meets the outer
obligations. Preservation per layer, licensing laws and approximate steps
are new in this corpus.

### Complete enclosing-relation admission

For a material transition, each admission owner is independently
responsible for deriving and validating the complete enclosing relation
from authoritative inputs (P4b, P6; provenance
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021)).
The relation contains every participant and equality join whose identity,
validity, authority, currentness or transition can affect or be affected by
admission; each crossing seam includes its relevant far side or
authoritatively establishes that the far side cannot participate. Caller or
owner assertions of completeness, validity, prior admission or authority do
not establish truth.

An owner may consume established facts when their exact subject, basis,
scope, provenance and validity remain applicable to its relation. Their
production and invalidation are recoverable; an unsupported assertion of
prior success is not such a fact. A function, component, role,
conversation or status boundary alone invalidates none of those coordinates
and requires no repeated derivation. Material mutation, rollback, changed
authority or basis, expired validity and an actual trust boundary trigger
the applicable validation before reliance or effect. Reuse does not
transfer the owner's admission responsibility, omit a participant or
satisfy a separately required independent judgment (§7).

Derivation and validation bind one exact admission-valid authoritative
basis identity through admission. If validity or currentness can advance
after preflight, admission remains conditional on the declared predecessor
and currentness law for that basis, or re-enters derivation and validation
without effect. Participating owners bind an equal basis or a
design-declared coherent composite basis; independently valid mixed-basis
judgments cannot combine (FOUNDATIONS §2, Basis).

Every participant and join is validated before any transition effect.
Internal evaluation order and lawful reuse are implementation-owned, and no
participant subset or nested constituent becomes admitted truth. Admission
is one semantic commit of the complete transition, bound to its exact basis
identity; failure or interruption admits the complete transition or none,
never a subset. No realisation mechanism or participant count is
prescribed. Direct and every supported composite or nested boundary
preserve this law: a partial result cannot substitute for an owner's
derivation and validation, and a competing same-scope path cannot establish
the transition outside the governing admission relation. Fresh
reconstruction and replay over the same basis reproduce the enclosing
relation, the basis identity and the complete outcome or refusal exactly at
semantic altitude (P3, P5).

The law is false if completeness is asserted rather than derived; a
relevant participant, join or seam is omitted; validation and admission use
an unidentified, stale or incoherently mixed basis; currentness can
advance without a commit condition or effect-free re-entry; any effect
precedes complete validation; failure or interruption exposes a subset;
fresh reconstruction differs; or competing same-scope authority remains.

### Standing structural qualification

Qualification of the admission law is instantiated for every admission
owner and supported boundary declared by accepted design (P6; provenance
rc.2 SPEC_METHOD #standing-structural-qualification). Case applicability
follows the supported input, state and operating or threat model. An
excluded threat alone cannot create an acceptance predicate or require
defensive work; a proposed scope expansion returns to its owning authority.
Supported malformed inputs, stale state and effect boundaries retain their
required checks:

| Form | Required observation |
|---|---|
| direct | the complete direct relation is derived, validated and admitted once |
| supported composite or nested | every supported constituent and owning boundary satisfies the same law; unsupported forms have a design-grounded `not_applicable` disposition and no weaker or competing path |
| forged | forged identity, membership, equality or authority reachable within the supported operating or threat model is refused without effect; exclusion requires its owning authority, not a helper's inability to construct the case |
| ambiguous enclosing relation | unresolved participant, join, seam or relation identity ambiguity is refused without effect |
| stale or advanced basis | stale input is refused, and basis advancement between preflight and admission causes effect-free re-entry rather than mixed-basis admission |
| incoherent multi-owner basis | owner judgments on bases that are neither equal nor joined by a design-declared coherent composite basis cannot combine and are refused without effect |
| competing same-scope admission authority | an undisposed competing same-scope path cannot establish the transition |
| reconstructed or fresh-process | the same basis reconstructs the same relation, basis identity and outcome or refusal |
| exact replay equality | replay over the same basis reproduces exactly the enclosing relation, basis identity and complete outcome or refusal |
| atomic publication failure | after validation succeeds, failure or interruption is observed at every materially distinct commit or publication boundary capable of exposing a subset, followed by fresh reconstruction showing the complete transition or none; named representative observations suffice only under a design-declared dominance or equivalence proof covering the complete partial-failure surface |

For an indivisible commit unit the atomic test establishes that boundary
and observes failure immediately on both sides. Final-participant
validation failure does not substitute for post-validation atomic-failure
evidence. A standing claim is false if an owner or supported boundary is
omitted, a materially distinct partial-failure boundary lacks an
observation or a declared coverage proof, a case uses a weaker helper or a
manufactured refusal, or fresh reconstruction does not compare the complete
semantic result (EVALUATION §1).

## 5. Work state and restart

Work state is the tuple of: the current persistent workspace; the governing
basis; the applicable closed results and judgments with their invalidators;
the residuals; and the known uncertainty over external effects. It is an
object (P3); its carrier (files, an event stream, another admitted owner) is
a profile or realisation choice.

Resumption is re-entry of the same method over the current work state,
starting from the current material state, by a possibly different actor.
It recovers applicable progress, re-checks the invalidators of each reused
result (§7), reopens only affected support, and reconciles uncertain
external effects, sufficiently for the next dependent action, before any
repetition or dependent action. Resumption does not imply idempotence: an
action whose external effect may have occurred is not repeated blindly;
the lawful next moves are reconciliation, yield or stop.

Checkpoint. Acceptance binds one exact checkpoint. The next
already-authorised bounded action may begin without renewed human approval;
acceptance does not widen the selected outcome or the affected relation set
(P6, P2). A preservation checkpoint may retain unfinished or unaccepted
work under an existing exact operation grant; it identifies its parent or
predecessor, the included territory, the concurrent-writer disposition and
the durable evidence location, and it is neither acceptance, promotion nor
publication. A proposed restart, which reconstructs from less than the
retained work, identifies why repair of retained work is insufficient,
which obligations and evidence survive, and which causal assumptions
change; reconstructability alone does not select reconstruction. Conserves
[UP-020 checkpoint and continuation](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#checkpoint-continuation-progress-and-churn);
the generic work-state object, the reconciliation of uncertain external
effects and the non-idempotence rule are new (P0, P5 with the open-world
premise).

Progress is accepted material movement toward the selected outcome;
prerequisite work names the obligation it enables; preservation and
repeated proof are evidence, not new progress; rejected or superseded
construction is churn; discovering previously hidden distance revises the
forecast and is not negative progress. Paperwork, code volume, test count,
commit count and review count are not progress by themselves. These are
semantic categories, not a numeric progress algorithm; a consumer may
derive its own progress and churn projections from them (P2). A member,
profile or project that distinguishes finer categories for its own
outcome states them as a refinement of these, naming this paragraph and
mapping each of its categories to one of progress, prerequisite work,
evidence that is not new progress, churn or forecast revision; a category
it cannot map is a change to this owner, not a parallel category (P2, P6).

The execution protocol of §1, §3 and this section is false if execution
proceeds from unreconstructable context; if a constructor's report
substitutes for required independent live evidence; if a bounded proxy
changes a governing relation outside its delegation; if unrelated
incompleteness blocks a closed causal cone; if a same-process test is used
to prove materially cross-process authority (§7); or if rejected activity
is reported as accepted progress.

Foundation to law. This family, work state, resumption and reuse, covers
this section and §7. Its instance premises are: (a) a workspace that
persists across activations; (b) work that spans activations; (c) actors
that may change between activations; (d) external effects in an open
world. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent), P0 (recovered); instance premises a, b | By P3 work state binds an exact basis, and by P0 an actor holds only part of it at a time, so work state is an object: the workspace, the governing basis, the applicable closed results and judgments, the residuals and the uncertainty over external effects | [§5](#5-work-state-and-restart), first paragraph | its carrier (files, an event stream, another admitted owner): the profile or realisation | 2, 5 |
| P0 (recovered), P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); instance premises a, c | By P0 an actor's context is bounded and disposable, by P3 the workspace binds the exact state, and by P4b recorded facts persist where the context does not, so the workspace is the truth surface and an actor's context a disposable account of it; current evidence corrects the account; discarding the account resets nothing | [The workspace and an actor's account](#the-workspace-and-an-actors-account) | the observations and reconciliations a resumption needs: the recovery contract, which is the resuming step's intake with the work state | 6, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise d | By P5 an effect of uncertain completion is undecided, and by P6 repeating an effect needs evidence that it is safe, so an effect of uncertain completion is reconciled before any repetition or dependent action; resumption does not imply idempotence | [§5](#5-work-state-and-restart) Resumption; [§3 Effects](#effects) | none | 4, 5 |
| P2 (independent), P6 (independent); instance premise b | By P2 progress is movement toward the selected outcome, and by P6 acceptance binds what was evaluated, so acceptance binds one exact checkpoint; a restart states why repair of retained work is insufficient; progress is accepted movement towards the selected outcome, not a count; finer progress categories refine these with a map | [§5](#5-work-state-and-restart) Checkpoint and Progress | progress and churn projections: their consumer | 5 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P0 (recovered), P6 (independent); instance premise c | By P4b and P0 private working context does not survive the actor, and by P6 a reused judgment is not a new independent one, so handoff is by closed results without private working context; reuse checks exact applicability and three invalidators, a material input change (newly acquired material evidence included), a changed basis and a declared revising observation, and a domain trigger is an instance of one of them; a reused judgment does not satisfy a required independent judgment | [§7](#7-closed-result-and-reuse) | the revising observation a result declares, and its other invalidation conditions: the producer of that result | 7, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise c | By P5 a transition's outcome is undecided without its evidence, and by P6 a proof establishes only the authority it was produced under, so a reviewable transition names its exact candidate, changes, proof and disposition; a same-process proof does not establish a reconstructable authority claim where the loss of process state is a counterexample | [Transition evidence](#transition-evidence) | the representation of transition evidence: its consumer | 9 |

### The workspace and an actor's account

The workspace and its authoritative inputs persist across activations and
are the continuing truth surface of the work: the surface whose current
material state decides what the work has and has not done. An actor's
context is an account of that state. It is bounded, because it is a
projection of the state (§2); revisable, because an observation can
correct it; and disposable, because a step records its closed results and
step-produced facts before it returns (§1 Admission; P4b). An account is
never a second truth surface, and no later activation needs a prior
actor's context: its intake reconstructs the governing relations without
it (§1 Intake) (P0, P3, P6).

Acquisition ([§2](#2-context-construction-under-an-envelope)) observes the
current subject and its authoritative inputs. Where they materially
disagree with a cached belief, a retained summary or a prior result, the
actor reconciles the disagreement: current evidence corrects the account,
and what the evidence cannot decide stays an explicit unknown. A stored
belief, a summary or a successful prior result never overrules contrary
current evidence. A prior result is relied on only after its
applicability and invalidators are checked against the current subject
and inputs (§7). The actor corrects its account within its grant; where
resolving the disagreement needs an operation, a territory or a decision
outside the grant, the step stops with `re_entry_requested(authority)`,
naming the owner of what it needs (§3 Construction availability) (P5,
P6).

Discarding an actor's private context resets nothing: the workspace, the
applicable valid work and the outstanding obligations remain as the work
state records them. A missing trace in a context, a memory or a summary is
no evidence about the subject. It shows neither that work was not done
nor that an external effect did not occur, nor that it ended; an effect
of uncertain completion keeps the value `completion_unknown`, or its end
stays not established beside its `not_effected` value, until evidence
about the subject decides it (§3 Effects) (P5).

Work that an interruption left partly written is part of the current
material state from which resumption (above) starts, and is assessed as
it stands; an assessment that was not performed has no result and is
never recorded as performed
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results); §3 Construction
availability). The method imposes no universal reset and no obligation to
replay the complete history. The recovery contract that applies, which is
the resuming step's intake with the work state, determines which
observations and which effect reconciliations the next dependent action
needs. Handoff between actors is by closed results, which carry no private
working context and keep their validity and independence conditions (§7)
(P0, P4b).

Purpose and material relation: finite context (P0) means an actor's
context ends or is replaced while the work continues, and discarding it is
safe only because the step-produced facts the outer contract needs are
recorded (P4b). Treating the account as the truth surface would let a
stale account overrule the workspace; treating a discarded account as a
reset would erase progress or repeat an effect that occurred (P5, P6). The
material relation is whether a decision relies on an account that current
evidence contradicts, or reads a missing record as undone work or an
absent effect. This subsection is new in this corpus. The workspace, the
work state and the closed results carry it, and no further carrier is
required.

## 6. Cost and proportionality

Proportionality is the relation between semantic ambiguity removed and
effective reasoning complexity introduced. A method obligation is
proportional when its contraction of the admissible interpretation space
justifies the additional concepts, relations, projections and evidence an
actor must hold together to reach a correct decision (P2, P0; conserves
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005)).

Effective reasoning complexity includes independent concepts and authority
surfaces, cross-document joins, exceptions and branching, states and
transitions, duplicated representations requiring reconciliation, and the
detail required to decide the governed question. It is not raw line count,
artifact count or context-window size. A detailed algebra or semantic
design view may be highly proportional when it eliminates rival
interpretations; a short additional ticket, receipt or summary may be
disproportionate when it creates another truth surface without reducing
uncertainty.

A proportional method deliberately constrains the admissible reasoning and
realisation space. Each constraint identifies the semantic ambiguity it
removes and contracts enough of the admissible interpretation space to
justify the reasoning complexity it introduces. Rival authority,
uncertainty over failure classification and evidence uncertainty count only
where they leave materially distinct admissible semantic, authority,
outcome or acceptance interpretations; they measure or evidence the same
interpretation space removed and are not independent proportional
benefits. The method does not prescribe an internal decomposition, search,
collaboration, tool or synthesis procedure when variation in that procedure
cannot affect a governed semantic, authority, evidence, safety or release
property. Increased actor capability may enlarge the bounded relation an
actor can resolve; it grants no authority, an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and it weakens no invariant and waives no
acceptance (P6). The owning law may justify one coherent constraint
family once; no rationale field, receipt or repeated audit is required for
every clause or consumer application.

For symbolic design, materially divergent implementation paths, runtime
states, tests, reviews and reconciliation joins are counterfactual evidence
of the semantic alternatives the design contracts; they are not an
independent numerator. When one bounded symbolic model can resolve those
material alternatives within effective reasoning capacity, resolving it at
design altitude is proportional even when the model is detailed. A prior
design surface that removes no material semantic alternative is
disproportionate. A method addition is disproportionate when it duplicates
truth, increases reconciliation paths or expands the bounded reasoning
surface without materially reducing ambiguity; existing obligations should
absorb new detail where they can without weakening ownership or meaning.

Apply this relation to the method's own execution: repeated source
acquisition, context assembly, hashing, activation preparation, status
recording, review and evidence generation serve an identified change,
decision or assurance need. Reuse stays subject to exact applicability and
invalidation (§7); repetition alone supplies neither validity nor
independence. Where this work materially affects the supported outcome, its
operational assumptions are qualified under UP-019 below. No universal
resource quota or separate accounting carrier follows. The delivery
priority this relation yields for a product outcome is SPEC_METHOD §8.

Cost is selected, not universal. Where a cost claim is the governed
question, the activation declares its allowance and reports its spend,
measured under the selected execution binding or recorded as unmeasured
(new; P0 with UP-014's selection rule). The size of an activation's
context is measured and fitted under §2 step 3, which refines the
resource-limit law below for the context dimension. Separate material startup, framework
processing, external computation, transport and assurance costs so that
one cannot conceal another; declare supported input dimensions and
workloads before qualification
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019)).
Report volume is not model traffic; a cost claim over transferred context
counts the context transferred to every delegated actor, not only to the
coordinator. No universal quota, ticket count, actor count or accounting
carrier follows.

Foundation to law. This family, proportionality and cost, covers this
section, with Resource limits below, and the delivery priority of
SPEC_METHOD §8. Its instance premises
are: (a) a selected outcome; (b) method obligations that each add
reasoning complexity; (c) where one is the governed question, a cost
claim; (d) an activation that consumes bounded resources, such as
context, attention, time or spend. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P2 (independent), P0 (recovered); instance premise b | By P2 an obligation is justified only by its route to the outcome, and by P0 reasoning capacity is finite, so a method obligation is proportional only when the ambiguity it removes justifies the reasoning complexity it adds, and that complexity is not raw size | [§6](#6-cost-and-proportionality), first three paragraphs | the justification of a constraint family: its owning law, once for the family | 6, 7 |
| P2 (independent), P0 (recovered), P1 (independent); instance premise b | By P2 and P0 detail is justified where it resolves alternatives the actor can hold, and by P1 a duplicate of truth is a second representation, not more truth, so a detailed symbolic design that resolves material alternatives within reasoning capacity is proportional; an addition that duplicates truth or adds reconciliation paths without reducing ambiguity is not | [§6](#6-cost-and-proportionality), symbolic-design paragraph | none | 4, 6 |
| P2 (independent), P0 (recovered), P6 (independent); instance premise b | By P2 the method's own steps need an identified purpose, and by P6 and P0 repetition adds neither validity nor independence, so the method's own acquisition, hashing, review and evidence serve an identified need; repetition supplies neither validity nor independence | [§6](#6-cost-and-proportionality), method's own execution | none | 7, 9 |
| P0 (recovered), P2 (independent); instance premise c | By P0 and P2 spend is part of what a finite actor's work costs the outcome, so a cost claim declares its allowance and reports spend measured under the selected execution binding, or recorded as unmeasured; costs that could conceal one another are kept apart; no universal quota follows | [§6](#6-cost-and-proportionality), Cost is selected | the allowance: the activation that makes the claim; the measurement units and boundaries of the cost components: the selected execution binding, under [Resource limits](#resource-limits) | 8 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent), P2 (independent); instance premise d | By P0 limits bind only as declared and measured, by P5 an unmeasured consumption supports no claim of fit, and by P6 and P2 staying within a limit establishes no adequacy, so a resource limit binds only where it is declared, with its unit and measurement boundary, and no universal quota follows; consumption outside the measured boundary supports no fit; pressure on a limit never licenses omission, so the activation refines, sequences, reassigns or stops with a named value; staying within limits shows no adequacy and grants no authority | [Resource limits](#resource-limits) | the value of each limit and the units and boundaries the environment can measure: the selected execution binding, for a build tenant [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) | 8, 7 |
| P2 (independent), P0 (recovered); instance premise a | By P2 delivery serves the outcome, and by P0 an actor can pursue only part of it at a time, so delivery for a product outcome is prioritised by this relation over likelihood, impact, reversibility, dependency and delayed feedback; probability waives no hard stop | [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), outside this member | the default priority, the smallest supported product path first: SPEC_METHOD §8 | 1, 5 |

### Resource limits

A resource limit bounds a resource that an activation consumes: context,
attention, wall time, spend, human effort, communication or a machine
resource (P0). This subsection owns the law for every such limit. It sets
no value (P0, P2, P5, P6):

- Declaration. A limit applies to an activation only where its intake,
  its actor's capability envelope or the selected execution binding
  declares it, because a resource control applies only through a selected
  frame and its owning scope
  ([REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection)).
  A declared limit states its unit and the boundary over which it is
  measured: which inputs, actors, processes and repeated reads it counts.
  No universal quota, budget or measurement gate follows.
- Measurement. A declared limit is measured in its unit over its boundary
  where the obligation it serves needs the measurement; consumption
  outside the boundary is recorded as not measured, and no claim against
  the limit covers it. A context limit bounds the material held in active
  context at once, including material acquired during the activation, so
  the bytes supplied at its start, the cumulative bytes it acquires,
  counting repeated reads, and the bound on what it holds at once are
  reported separately; §2 step 3 refines this for the measurement of the
  selected context before it is read. Measures that answer different
  questions, such as the cost components of Cost is selected above, are
  reported separately.
- Exhaustion. Pressure on a declared limit never licenses omitting or
  truncating a material obligation or input. Before a limit would be
  exceeded, the activation refines the task, sequences activations,
  reassigns the work to an actor whose limits fit, or stops with the
  applicable value of §3, naming the limit, such as `incomplete` where
  bounded execution ends first; a stop keeps the unresolved outcome
  ([§1 Transitions](#transitions), Stops). Enlarging a limit re-enters the
  owner of the grant or binding that set it.
- Values. The value of each limit, and the units and boundaries the
  selected environment can measure, are set by the selected execution
  binding, which binds this law; for a build tenant that binding is the
  one [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.
  A value is stated before the activation it limits.
- Standing. An activation that stays within its limits is not thereby
  adequate, and an actor's larger limits grant no authority and waive no
  invariant (P2, P6).

Purpose and material relation: the configuration (§1), context
construction (§2) and frame qualification
([EVALUATION §7](EVALUATION.md#frame-qualification)) rely on resource
limits, so the law for declaring, measuring and honouring them is stated
once in tier 1, and only their values are left to the execution binding.
The material relation is whether an undeclared, unmeasured or exceeded
limit is read as fitting, or forces a silent omission. This subsection is
new in this corpus; its parts carry RF-014's prohibition of silent
omission, REFERENCE_FRAME §4's rule that a resource control applies only
through a selected frame, and UP-014's selection rule.

## 7. Closed result and reuse

A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context is not
transferred when the closed result and its provenance are sufficient for
the consuming decision (P4b, P0; rc.2 RF #return-a-closed-result).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity),
whose "changed material evidence" is the evidence case of the first
invalidator. Purpose and material relation of naming the three kinds once
and of the instance rule: the predecessor stated its invalidators in
several differing lists, so a consumer had to take their union; one list
with named instances gives every consumer the same triggers, and the
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.

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

## 8. Source dispositions

| rc.2 clause | Disposition |
|---|---|
| UP-020 and its six subsections | conserved in full; §1 (relation, intake, execution unit, roles and delegation), §3 (disposition), §5 (checkpoint, continuation, progress, churn, falsifiers), §7 (transition evidence and proof cadence); the generic work-state object, reconciliation of uncertain effects and non-idempotence in §5 are new: the work-state object is the object UP-020's restart rule operates on (P3), and reconciliation and non-idempotence follow from P5 with the open-world premise and P6, the material relation being whether an external effect whose response was lost has occurred; rows in the table below |
| The workspace and an actor's account | no rc.2 row; §5 The workspace and an actor's account is new, with its purpose and material relation stated there; it states for tier 1 the rule of the rc.2 baseline failure classification that a compression, summary, generated map or prior result does not replace current source authority, which EXECUTIVE_BASELINE §20 keeps as profile law |
| Foundation to law | no rc.2 row; §1, §5 and §6 each hold the table of one family in the format of FOUNDATIONS §3 Foundation to law; a table decides nothing and names the rule that states each consequence. Purpose: a reader sees which rules follow from the commitments and which are added choices with their owners, so no added choice is presented as derived (P6) |
| Transitions | no rc.2 row; §1 Transitions is new: the current state, the destination defined by constraints, bounded transitions preserving the outer obligations, discovery, destination change, completion on evidence and explicit stops, with its purpose and material relation stated there; progress and churn stay §5, refinement §4 |
| Configuration | no rc.2 row; §1 Configuration is new: allocation of responsibilities and information exchanges to frames, its explanation, direct entry by reference to Roles and delegation, evaluation of a configuration, reconfiguration, coordination across tasks and optimality claims, with its purpose and material relation stated there; the distinct relation structures stay RF-009 in REFERENCE_FRAME §3, to which §1 refers without a list of its own; the executive configuration is an example, owned by EXECUTIVE_BASELINE. Admission of a configuration states for tier 1 the rule of rc.2 BASE Existing Authority Selects The Configuration, that the smallest existing authority owning the material decision admits a configuration, with the proxy bound; the per-layer owners of that rule stay EXECUTIVE_BASELINE §16, which disposes the row |
| UP-018 | conserved; restated in DESIGN_MODULE §7 Invariant reconstruction sufficiency, which disposes its row; its general reconstruction-without-history rule is §1 Intake |
| Probabilistic Work Boundary | conserved; the object and commitment are FOUNDATIONS §2 and §3; §1 consumes them |
| RF engagement (establish basis, applicability, select and activate, evaluate, return, reconfigure) | conserved; §1 to §4 and §7; rows in the table below |
| AC-010, AC-011 | conserved; the laws themselves are restated in AXIOMATIC_CALCULUS §4, which disposes their rows; §2 applies them, joined with RF-002/003/004/014/017 into one operation (new), each RF law applied from its successor section in REFERENCE_FRAME §3, the rc.2 routes kept as provenance only; the step's local selection among fit options under an admitted grant is carried from RF-014; the RF laws themselves are restated in REFERENCE_FRAME §3; the size measurement of step 3 with the condition under which it applies, its separation from adequate attention, and Acquisition are new, with their purpose and material relation stated in §2 |
| RF-012, AC-007 | conserved; the core algebra, its meanings and its two labelled tightenings are FOUNDATIONS §4 Results, whose §6 lists them; REFERENCE_FRAME §3 and AXIOMATIC_CALCULUS §4 dispose their rows; §3 here refines the core for steps |
| RF Result Conjunction, the conjunction sentences of Applicability And Required Results | conserved; the conjunction rule, including the rule for a composite over several results formerly stated in §3, is FOUNDATIONS §4 Conjunction of results; §1 Applicability refers to it |
| TICKET_METHOD work-carrier-to-execution rule, execution contract admission | the admission relation is restated in §1 with provenance; the mapping of admission outcomes into the core is new, in §3 Admission and activation, with its purpose stated there; the rows are disposed at the TICKETS member |
| Baseline work result | conserved in §3, except the pairing of `incomplete` with `indeterminate`, which is proposed `superseded`, pending the product owner. Proposed replacement relation: §3 Construction availability maps `incomplete` to falsified for "a candidate is available", so an evaluation that was not performed stays distinct from one whose evidence cannot decide. The common single result algebra requirement, item 3, requires that distinction and accepts no particular replacement; FOUNDATIONS §4 Results restates it in its no-raise rule. `re_entry_requested` is split by its cause into two values, each mapped once; the rest of the mapping, its totality and exclusivity are conserved in §3. The activation-refusal exclusion is stated for tier 1 in §3 Admission and activation; the variant readings and the exclusion's reading for the Worker stay in EXECUTIVE_BASELINE §5, which disposes the row |
| UP-020 dispositions | conserved in §3 Disposition; their core values for acceptance are new, with the purpose stated there |
| Ambiguity Governance outcomes and hard stops | outcomes conserved in §3 Ambiguity outcome, their core values new, with the purpose stated there; the hard-stop classes conserved in full in §4 Hard stops, which owns them; SPEC_METHOD §5 disposes the row |
| Effects | no rc.2 row; §3 Effects is new, with its purpose and material relation stated there |
| Staleness of derived surfaces | no rc.2 body row; §2 Staleness of derived surfaces is new in tier 1, with its purpose and material relation stated there; provenance rc.2 authority_compressions/README.md and stdo_bootstrap.md step 5; PRODUCT_DEFINITION §11 refines it for the method's released carriers. The disposition of the compression carrier awaits the product owner's ruling and is not decided here |
| Refinement and rewrite steps | no rc.2 row; in §4 Refinement, preservation per layer, licensing laws and approximate steps with their adequacy relation and end-to-end bound are new, with their purpose and material relation stated there; the induction over exact steps is the conserved refinement law of the row below |
| ODD graph functions, ODD 11.8 | conserved; graph functions generalised in §4 to any realisation as typed refinement; 11.8 is not generalised: it stays profile law, its row disposed in ODD §11.8, and ODD §5 Graph functions declares its cumulative carried environment as the specialised contract through which §4 lets a refinement carry earlier outputs; PROFILES §2 keeps the ODD binding |
| UP-017 | conserved; restated in DESIGN_MODULE §5 Bounded frame conservation, which disposes its row; its seam rule is §1 Execution unit and §4 |
| UP-021 and Standing Structural Qualification | conserved in full; §4; rows in the table below |
| UP-014, UP-005, UP-019 | conserved; §6 in full for UP-014's relation and method execution, its delivery priority in SPEC_METHOD §8; UP-005 and UP-019 restated in DESIGN_MODULE §6 and §7, which dispose their rows, §6 carrying their proportionality and cost relation; the allowance rule is new; §6 Resource limits is new, owning the generic law for declaring, measuring and honouring a resource limit, with the values, units and boundaries referred to the selected execution binding, which SPEC_METHOD §11 defines for a build tenant; rows in the table below |
| Return A Closed Result | conserved; §7, which names the invalidators once as three kinds (material input change, with newly acquired or changed material evidence, from TICKET judgment continuity; changed basis; declared revising observation) and requires a domain trigger to be stated as an instance of one of them (new, with its purpose stated there) |
| TICKET judgment continuity | conserved; restated in [TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity), which disposes its row; the generic reuse law is §7 |

RF rows received by this member (anchors into rc.2
REFERENCE_FRAME_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #engagement | not applicable: heading with no claim text (14 bytes); its children are disposed individually | §1 |
| #establish-the-evaluation-basis | conserved | §1 Intake |
| #applicability-and-required-results | conserved; its conjunction sentence applies FOUNDATIONS §4 Conjunction of results, which owns the rule; new in §1 Applicability, with its purpose stated there: the applicability decision as a result in the core, an exclusion as no result of the excluded obligation, and the disjunctive predicate | §1 Applicability |
| #select-and-activate | conserved | §2 (Activation paragraph) |
| #evaluate | conserved | §2 (Evaluation paragraph) |
| #return-a-closed-result | conserved | §7 |
| #reconfigure-when-necessary | conserved | §4 (Reconfiguration paragraph) |

SM rows received by this member (anchors into rc.2 SPEC_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #proportional-method-and-delivery-stdo-up-014 | conserved; the relation, effective reasoning complexity, the constraint test, the symbolic-design paragraph, the disproportion test and the method's own execution are here; the delivery priority is SPEC_METHOD §8; "Ontology, IACS, Prime" generalised to "a detailed algebra or semantic design view" | §6 |
| #agentic-construction-execution-stdo-up-020 | conserved; the normative relation and the non-prescription of worker internals | §1 The step |
| #sufficient-execution-intake | conserved; all six items; the design-profile input laws are consumed by reference to DESIGN_MODULE | §1 Intake |
| #bounded-causal-construction | conserved | §1 Execution unit |
| #construction-assessment-and-delegation | conserved; constructor, assessor and decision owner are named as the responsibilities a configuration allocates where its operations include construction, assessment or disposition, not as an inventory of roles (§1 Configuration); "No Executive activation is required" is written "No coordinating activation is required"; "Executive mutation restrictions remain applicable" is read as the restriction a selected configuration places on its coordinating role, as the executive configuration places it on its Executive; the proxy's permitted decisions inside a step are here, and what a proxy cannot change is the proxy limit of FOUNDATIONS §2 Authority kinds, which this section applies; "condition-based result recording" is stated in full in Recording a result without review | §1 Roles and delegation |
| #proportional-disposition | conserved; "Assessment returns one of these semantic dispositions" is read as the decision owner's disposition after assessment, an assessor's recommendation being evidence for it, as EVALUATION §8 reads #reviewer-result-and-triage-projection | §3 Disposition |
| #transition-evidence-and-proof-cadence | conserved; "the assessor disposition" is read as the decision owner's disposition or the assessor's recommended disposition, which §3 Disposition separates | §7 Transition evidence |
| #checkpoint-continuation-progress-and-churn | conserved; "Product" is written "the selected outcome" in tier 1; new: the rule that finer progress categories refine these with a map | §5 |
| #complete-enclosing-relation-admission-stdo-up-021 | conserved in full | §4 Complete enclosing-relation admission |
| #standing-structural-qualification | conserved; all ten forms | §4 Standing structural qualification |
