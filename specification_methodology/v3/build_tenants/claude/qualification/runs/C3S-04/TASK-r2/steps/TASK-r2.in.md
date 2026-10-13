STEP TASK-r2 | cap 110000 bytes | measured 80510 bytes | fits
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
# Reference frame eb-task-d

Task: Acting as Executive in the coordinated branch, revalidate the drift locks after a configuration change, evaluate a candidate_ready work result, keep severity, priority, frame result and current-boundary effect of a review finding distinct with their owners, and apply one disposition or say why none can be applied and name the next action within the grant.

Purpose: The owning sections for the Executive and Reviewer frames, technical triage, the work-result values, Executive attention with its no-mutation rule and drift locks, the executive configuration, the complete engagement transition with its promotion constraints, actor binding and independence, construction availability and disposition, closed-result reuse and invalidation, independent assessment and review results with their triage projection, testing evidence composition, and the core result algebra with its conjunction.

Each excerpt below is a verbatim copy of one owning section of a member
of this method. The `Source:` line before it names the member and the
section's anchor, and gives the SHA-256 of the whole owning member. The
owning section decides; this frame owns no determination. Links inside
an excerpt are relative to the owning member's directory.

Routes, in order:

1. [EXECUTIVE_BASELINE.md#executive](../EXECUTIVE_BASELINE.md#executive)
2. [EXECUTIVE_BASELINE.md#reviewer](../EXECUTIVE_BASELINE.md#reviewer)
3. [EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect](../EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect)
4. [EXECUTIVE_BASELINE.md#work-result](../EXECUTIVE_BASELINE.md#work-result)
5. [EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action](../EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action)
6. [EXECUTIVE_BASELINE.md#the-executive-configuration](../EXECUTIVE_BASELINE.md#the-executive-configuration)
7. [EXECUTIVE_BASELINE.md#12-complete-engagement-transition](../EXECUTIVE_BASELINE.md#12-complete-engagement-transition)
8. [EXECUTIVE_BASELINE.md#17-actor-binding-and-independence](../EXECUTIVE_BASELINE.md#17-actor-binding-and-independence)
9. [ACTIVATION.md#construction-availability](../ACTIVATION.md#construction-availability)
10. [ACTIVATION.md#disposition](../ACTIVATION.md#disposition)
11. [ACTIVATION.md#7-closed-result-and-reuse](../ACTIVATION.md#7-closed-result-and-reuse)
12. [EVALUATION.md#3-independent-assessment](../EVALUATION.md#3-independent-assessment)
13. [EVALUATION.md#4-review-results](../EVALUATION.md#4-review-results)
14. [ASSURANCE.md#10-testing-evidence-composition](../ASSURANCE.md#10-testing-evidence-composition)
15. [FOUNDATIONS.md#results](../FOUNDATIONS.md#results)
16. [FOUNDATIONS.md#conjunction-of-results](../FOUNDATIONS.md#conjunction-of-results)

Size of this frame: 75455 bytes.

Source: EXECUTIVE_BASELINE.md#executive sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

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


Source: EXECUTIVE_BASELINE.md#reviewer sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

### Reviewer

Reviewer is this profile's label for the independent live-surface
evaluation that the assessment relation of ACTIVATION §1 consumes, governed
by EVALUATION §3 (independence and traceability) and EVALUATION §1 and §7
(assurance boundary and qualification freeze), activated as a frame. It
evaluates one exact subject and returns a closed result, with evidence-bound
technical triage when a finding exists. It does not implement the repair,
assign priority, apply disposition or activate the next frame (P6; rc.2
#reviewer).


Source: EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

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
`out_of_frame` pressure (FOUNDATIONS §4 Results); it does not invent precision and
does not send work sideways to the Worker (P5).

Severity grades the consequence if the finding manifests. Priority orders
the response relative to the complete Product outcome, likelihood and
exposure, the current MVP or release mandate, reversibility, dependencies,
cost of delay and available capacity. The Reviewer grades severity; the
Executive assigns priority (P6, P2).

The Product-owned Project Reference-Frame Basis binds the severity scale,
the priority scale, the current-boundary decision cutoff and the
non-waivable hard stops, whose owner is
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement). This profile
imposes no universal numeric scale.
Severity, priority, the frame result (FOUNDATIONS §4 Results) and the
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


Source: EXECUTIVE_BASELINE.md#work-result sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

### Work result

A work result is the Worker's closed output to its declared consumer; in
the coordinated branch that consumer is the Executive. It exists only after
a successful Worker activation. An `activation_refusal`, with the cause and
core value that
[REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions) gives it,
returns to the assigning authority or declared result carrier and creates
neither a Worker activation nor a Worker result. This applies to the
Worker the rule that
[ACTIVATION §3 Admission and activation](ACTIVATION.md#admission-and-activation)
states for every step (P5, P6; rc.2 #work-result).

The work-result values are the five values of construction availability,
the refinement that
[ACTIVATION §3](ACTIVATION.md#construction-availability) defines for the
predicate "a candidate is available". ACTIVATION §3 owns their grounds,
maps each to exactly one core value, and states that the mapping is total
and exclusive after lawful activation. In this profile they are carriers,
not new semantic dispositions, and none of them is an assessment or an
acceptance of the candidate (FOUNDATIONS §4 Results). This profile binds
only what each value means for the Worker and its consumer; the core value
shown with each is ACTIVATION §3's (P5, P6):

- `candidate_ready` (`satisfied`): the Worker's exact candidate and its
  transition evidence are available to the consumer, which decides whether
  independent review is required (§12 step 4); it is not `accept`;
- `refused` (`falsified`): the Worker was lawfully activated and its
  construction is defeated; the Executive verifies the basis and applies
  the existing authority relation (§12 step 4);
- `incomplete` (`falsified`): the Worker produced no candidate; its
  residuals and stop basis name each evaluation it did not perform, which
  has no result, and each it performed that its evidence could not decide,
  which keeps its own `indeterminate`. The work result is never read as
  `indeterminate`, and the Executive reactivates work only where current
  authority already permits it (§12 step 4);
- `re_entry_requested(authority)` (`out_of_frame`): a material decision lies
  outside the Worker's grant; the value names that decision's owner, to
  which the Executive returns the question; and
- `re_entry_requested(basis)` (`invalid_basis`): the activated basis can no
  longer support the Worker's construction; the Executive revalidates the
  basis lock (§6 Drift locks) before any further activation.

A capability, authority, stale-basis, ambiguous-basis or topology mismatch
known during activation is an `activation_refusal` with its cause, never a
synthetic Worker result (P5, P6). Consumers choose the representation;
ACTIVATION §1 and §3 stay the owners of the execution relation, its
results and its dispositions.

The result references the current computed classification, supporting
evidence, residual judgments and original rulings through their existing
carriers. It does not reconstruct unchanged C/J/O at each handoff. The
consumer checks applicability and concrete invalidators; changed evidence
revises only the affected results, preserving originals and supported
surviving claims (ACTIVATION §7; P4b).


Source: EXECUTIVE_BASELINE.md#6-executive-attention-evaluation-and-action sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

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
cannot authorise the edit retroactively (P6, P3). This prohibition is this
profile's, and it applies wherever the executive configuration is selected
([ACTIVATION §1 Configuration](ACTIVATION.md#configuration), Example; §7);
an operation grant covering a construction, status and checkpoint sequence
does not lift it
([ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)).

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
or the effect; a refused activation is `activation_refusal(authority)`
(REFERENCE_FRAME §5). An unresolved mandatory conflict prevents a satisfied
conjunction. The Executive repairs none of these by making its own frame
larger (P5, P6; FOUNDATIONS §4 Results and Conjunction of results).

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


Source: EXECUTIVE_BASELINE.md#12-complete-engagement-transition sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

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
Executive, with the cause and core value REFERENCE_FRAME §5 gives it. No
Worker frame is active, no Worker evaluation occurs, and the
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

The notation explains and mandates no schema. The material relation of
`re_entry_requested` names its cause, authority or basis, which is part of
the value. Each value maps to exactly one core value for "a candidate is
available" under
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability),
read as in §5 Work result; the mapping applies only after lawful
activation. The Worker does not send a candidate directly into an
implicitly active Reviewer. It stops after returning the result (P5,
P6).

### 4. Executive evaluates the work result

For `refused`, `incomplete` or `re_entry_requested`, the Executive verifies
the exact basis and applies the existing authority relation. It records the
applicable disposition, or reactivates work only where current authority
already permits that action. None of these variants is accepted progress
because work occurred (P6, P5; rc.2 #4-executive-evaluates-the-work-result).

Whatever the variant, an effect the work result names `completion_unknown`
([ACTIVATION §3 Effects](ACTIVATION.md#effects)) is reconciled under
[ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart), sufficiently for
the next dependent action, before work is reactivated, the effect is
repeated or any action that depends on it is taken (P5, P6).

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
- the core result (FOUNDATIONS §4 Results);
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
current MVP or release mandate, applies any declared result conjunction
(FOUNDATIONS §4 Conjunction of results), assigns priority, records the
effect on the current promotion boundary, and acts on exactly one
disposition within its grant: `accept`, `local_repair`, `re_enter` or
`reject` (ACTIVATION §3; P6, P5; rc.2
#7-executive-disposes-and-checkpoints).

ACTIVATION §3 and §5 stay the owners of each disposition, the exact accepted
checkpoint and the next already-authorised bounded action. The disposition
is the acceptance result; neither `candidate_ready` nor a satisfied review
result is acceptance (FOUNDATIONS §4 Results). A repair creates
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


Source: EXECUTIVE_BASELINE.md#17-actor-binding-and-independence sha256=920ace2bcc86375eba17d6ad3486213bdeabaa7a8cbc0f34aa9e1eca08083a9c

## 17. Actor binding and independence

Frames and actors are separate identities: activation binds an actor to
a frame ([ACTIVATION §1 Configuration](ACTIVATION.md#configuration)). In
this configuration, as
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)
permits for any configuration, one actor may occupy several frames across
different activations where authority and any claimed independence are
preserved. Humans, agents, deterministic tools or mixed configurations may
occupy them. The profile prescribes no actor count (P3, P6, RF-016; rc.2
#actor-binding-and-independence).

Where independent review is required, EVALUATION §3 controls: the
activation records the exact subject and verdict carrier, and the Reviewer
is not the author of that subject; a fresh context of the author is still
the author. For generic method qualification,
EVALUATION §7 adds its declared capability, configuration, comparison
basis, reference-exposure and freeze conditions (P6).

An Executive may inspect a subject to adjudicate a result. That inspection
does not become an additional independent Reviewer result because the actor
used reviewer-like tools (P6, P1).


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


Source: EVALUATION.md#4-review-results sha256=6383bebb0238da55ec4ea779f44d077f558f0f32ccfcfbfca38845efed9946b6

## 4. Review results

A review returns one core result
([FOUNDATIONS §4, Results](FOUNDATIONS.md#results)) for each declared
predicate it evaluated, with: the exact subject and basis, the evidence
consulted, the findings ranked by consequence, each finding's evidence and
the smallest bounded correction, the residual uncertainty, and the
invalidation conditions. A declared predicate the review planned and did
not evaluate has no result (FOUNDATIONS §4, Results). The review names it
as not performed and reports no core value for it, neither
`indeterminate` nor `falsified`, so that conjunction keeps it apart from
an undecided predicate and from required coverage that no planned
assessment addresses
([FOUNDATIONS §4, Conjunction of results](FOUNDATIONS.md#conjunction-of-results);
P5, P6). It may recommend a disposition
([ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition)), which is
evidence only and never a disposition; it does not apply one. A finding
without evidence a consumer can chase is commentary.

### Result and triage projection

Where a review returns findings with technical triage, the triage is the
assessor's evidence-bound assessment of each finding against the exact
evaluated claim and basis. Severity, the assessor's grade of consequence,
is evaluation evidence. Priority, the effect on the current promotion
boundary and the disposition are the decision owner's (ACTIVATION §1,
Roles and delegation) and stay distinct values even where a
Product-defined policy maps one to another. A recommended disposition
is evidence for the decision owner: it is not a disposition, a
priority or a boundary effect, and it is never adopted mechanically (P6,
RF-007). The fields of a triage are declared by the profile that adopts it, and
the scales it uses are bound by the adopting Product (P2, P6; provenance
[reviewer result and triage projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection)).

The projection of the finding-level triage payload is total over the core
values of [FOUNDATIONS §4, Results](FOUNDATIONS.md#results). A predicate
not performed has no result and so no triage payload; the payload class
`indeterminate` never stands for it. The payload classes `complete`,
`indeterminate` and `not_applicable` classify the triage only; they are
not new results, dispositions, priorities or lifecycle states (P5, P1).

| Core result | Finding and triage payload | Decision-owner consumption constraint |
|---|---|---|
| satisfied | an explicit no-finding state; triage `not_applicable`; evidence, residuals and invalidation stay present | priority and boundary effect are `not_applicable` to this result unless another exact consumed result supplies a finding |
| falsified | one or more exact findings; triage `complete` where supported, keeping `indeterminate` fields where evidence cannot close them | apply the Product-owned priority and boundary policy without mapping severity mechanically to a disposition |
| indeterminate | a partial finding or observation state; triage `indeterminate`; the exact evidence gaps and residual uncertainty | keep the uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or as a closed finding |
| out_of_frame | the evaluated claim needs an undeclared material relation or evaluator capability; triage `indeterminate`; the missing relation or capability and the exact reconfiguration pressure are named | refine or reconfigure a capable activation and keep the claim unresolved; do not consume the result as satisfaction or falsification |
| invalid_basis | a basis failure; triage `not_applicable`; invalidation evidence and basis-repair pressure | refuse to consume the result and return through the declared basis re-entry relation |

An adjacent observation outside the evaluated claim does not replace the
claim-relative result. The assessor returns it separately, with triage
`not_applicable` to that claim and the exact repricing or re-entry
pressure; the decision owner returns it to its declared owner without
creating a claim-relative block, or another review round, from its
severity alone (P6, P2).

The assessor returns to the decision owner, not to the constructor. It does
not edit the candidate, direct the repair or authorise continuation (P6,
§3).


Source: ASSURANCE.md#10-testing-evidence-composition sha256=c2a5e1de9fb09eb2050d0c58a0b9f78f4990147370afdfe3a17e61fafe3773cf

## 10. Testing evidence composition

One execution may provide several bound results. A supported user scenario
may supply user-acceptance evidence for the outcome, end-to-end evidence for
the runnable causal path, integration evidence for selected seams and unit
counterexamples for a module-owned algebra. Those claims stay distinct and
combine only through the declared relations of REFERENCE_FRAME §6, whose
result conjunction is
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)
(P4a, P6;
provenance #testing-evidence-composition).

The default proof responsibilities are (P6, P2):

- user acceptance proves the outcome from the user's supported frame;
- end to end proves the complete authoritative runnable Product path;
- integration proves material participant composition; and
- unit proves module-owned laws, with evidence size and strategy
  proportional to their internal combinatorial complexity.

User acceptance alone may leave internal path singularity unevaluated.
End-to-end success alone may leave unselected user populations or
combinations unevaluated. Integration and unit results cannot stand in for
either broader claim. When the Product claim requires all of them, a
conflict or a missing result stays visible to the decision owner's
disposition and cannot be hidden by aggregate green status (P5, P6;
FOUNDATIONS §4 Conjunction of results, Survival; REFERENCE_FRAME §8,
operational full coverage item 6).


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
# TASK D: dispose a Worker result and a Reviewer result as Executive

## Subject

Product `shopfront`: an online shop. You act as the Executive, Omar, in
the coordinated branch. The facts below are the whole subject; the record
is invented for this task and is evidence about no real product.

Mandate: release `1.2` (owner Jules, product owner) delivers guest checkout
with card payment. Saved-address autofill is not part of the 1.2 mandate;
it ships behind the flag `autofill_v2`, which is off in the release
configuration.

Product-owned project reference-frame basis (owner Jules):

- severity scale: critical, high, medium, low;
- priority scale: P0 (act now) to P3 (backlog);
- decision cutoff: a finding blocks the current promotion boundary only if
  its severity is critical on a path in the release mandate, or it
  violates a hard stop; findings of severity high or lower on paths outside
  the release mandate do not block and are recorded as residuals with an
  owner;
- hard stop: a card number persisted anywhere outside the payment provider.

Omar's grant: dispositions `accept`, `local_repair`, `re_enter` and
`reject` over 1.2 release candidates. The admitted work contract `EC-77`
requires independent review of any change on the payment path.

Basis at activation: build `b-77` (commit `4be19f02`), configuration
`checkout.yaml` revision r41.

Worker result `WR-31` (Worker Ada, 2026-10-11T17:00Z): `candidate_ready`;
candidate commit `4be19f02`, build `b-77`; transition evidence: user
acceptance `UA-5` (guest checkout outcome) green, end to end `E2E-3`
(checkout path from cart to confirmation) green, integration `INT-8`
(payment-provider seam) green and the unit suite green, all on `b-77` with
r41. Self-review attached. Commit `4be19f02` changes the card-payment step
(the payment-provider client and its retry handling) and the address step
(it adds the `autofill_v2` code path).

Reviewer result `RR-9` (Reviewer Hana, independent of Ada, 2026-10-12T08:00Z):
claim "guest checkout on `b-77` with r41 meets requirements R-C1 to R-C6,
including the address step"; population: the 1.2 guest checkout flows,
with `autofill_v2` both on and off; core result `falsified`; one finding:

- F-1: with `autofill_v2` on, a second guest in the same browser session
  sees the previous guest's address prefilled, against R-C4 ("a guest's
  data is never shown to another guest"); severity high; causal
  assessment: a session-storage key is not cleared on order completion,
  confidence medium; blast radius: guests sharing one browser while
  `autofill_v2` is on; workaround: keep `autofill_v2` off; repair
  complexity low, regression risk low; residual uncertainty: whether other
  session keys persist, reducible by a storage-dump test.

`RR-9` names as its invalidation conditions any change to `b-77` or to
`checkout.yaml`.

Change after the review: at 2026-10-12T09:30Z the operations lead Priya,
under her configuration authority, advanced `checkout.yaml` to r42, which
lowers the payment-provider timeout from 10 s to 4 s. Nothing else
changed. The current time is 2026-10-12T10:00Z.

## Instruction

1. Under a heading `Drift locks`, give each of the five locks as holds,
   fails or cannot be determined, with the fact that decides it, and for
   each failed lock the result it yields.
2. Under a heading `Work result`, give your evaluation of `WR-31` at step 4.
3. Under a heading `Finding F-1`, give its severity, priority, frame result
   and current-boundary effect, saying who sets each; assign the priority
   yourself with a one-sentence reason.
4. Under a heading `Disposition`, apply exactly one disposition, or say why
   none can be applied now, and name the next action you take within your
   grant.
5. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
