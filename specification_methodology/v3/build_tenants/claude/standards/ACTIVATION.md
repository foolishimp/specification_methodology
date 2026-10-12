# ACTIVATION

Tier 1. Owns how bounded work proceeds: the step (intake, admission,
applicability, activation), context construction under an envelope, the
result algebra, totality, refinement, work state and restart, cost, the
closed result and reuse. Consumes [FOUNDATIONS](FOUNDATIONS.md) and the
frame object of [REFERENCE_FRAME](REFERENCE_FRAME.md); adds no
definitions. A route written `rc.2 RF #anchor` is into
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

### Intake

A step is activated from an intake sufficient to reconstruct its governing
relations without conversation history, commentary or a prior actor's memory
(P0, actor-change premise). The intake names:

- the governed outcome or decision: the selected outcome, admitted
  prerequisite or experiment it serves (P2);
- the exact workspace subject and basis, and the inputs it may acquire,
  each by identity and hash or by an input commit;
- the evaluation or evaluation family the step performs and its result
  algebra (§3);
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
- where the governed question is capability fit or a cost claim, the
  allowance and how spend will be measured (§6).

Implementation folklore is not an intake source. Where a design profile
applies, its bounded-frame conservation, transformation-admission
completeness, invariant-reconstruction sufficiency and
computational-realisation projection laws supply the affected set, the
admission relations, the invariants and the computational dispositions;
this section consumes those laws and creates no second design package
(PROFILES §3). Conserves
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
A contract is in one of the states drafted, admitted, rejected or
superseded. Execution begins only after deterministic admission or an
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
its owner has not admitted (P6, P2). The admitted contract names one
durable result and evidence surface; every result, withheld closure and
residual obligation is recorded there before return, a conversation return
alone is not durable evidence, and if no such surface is authorised and
available, admission refuses (P4b). Absent or rejected admission returns
the missing work authority without execution. Provenance:
[work-carrier-to-execution rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)
and
[execution contract admission](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-contract-admission);
the selection of the carrier (ticket, sprint entry, run-scoped contract)
is tier-2 law and lands in the TICKETS member, which disposes those rows.

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
conjunction; unresolved applicability withholds the dependent claim until
sufficient evidence or the owning decision resolves it; other applicable
constraints stay in force even if only one evaluation detects them (P4b,
P5). Qualification of an applicability rule distinguishes true, false and
unknown premises, required results that are missing or bound to the wrong
subject, and a sufficient positive result, under a finite declared fixture;
a rule that always skips or always activates cannot satisfy those distinct
expected outcomes (EVALUATION §7; rc.2 RF
#applicability-and-required-results).

### Output

The step's output is a candidate plus its step-produced facts: judgments with
their evidence, residuals, observations, authority decisions, provenance, and
one stop state from §3. The actor's internal path is not part of the output
and is not governed (FOUNDATIONS §2, work boundary; provenance
[Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)).

### Roles and delegation

Roles are relations over steps: a constructor owns the bounded
implementation and its self-review; an assessor evaluates a frozen
candidate independently; a decision owner disposes. Where independent
assessment supports promotion, the assessor evaluates the exact live
subject, its authority paths, proof and installed state, not the
constructor's summary (EVALUATION §3). This preserves the
independent-review relation and prescribes no actor count: one actor may
occupy different roles across different claims when independence for the
assessed claim is preserved; no role name confers an operation
([RF-016](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-016-implementation-neutrality);
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
intake and operation grant, it may enter directly as constructor or Writer. No
coordinating activation is required solely to appoint that Writer. The
applicable frame configuration selects coordination when material
contexts, authority, capability or required independence need it; a role
or frame name alone does not create that need. Direct entry preserves
execution-contract admission (Admission above), the smallest lawful
carrier, the required assessment and the reserved decisions; it permits
bounded work and condition-based result recording, not self-acceptance at a
boundary owned elsewhere (P0, P6).

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Actual role transitions are recorded in the existing
work carrier; a status change alone requires neither a new grant nor
rehashing an unchanged subject. A material change to the operation, the
subject, the territory, the authority or the validity conditions requires
the affected binding to be resolved before effect. The restriction that a
coordinating role mutates nothing remains applicable (P6, P3).

## 2. Context construction under an envelope

Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R (AC-010,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-010-material-closure).
   If the closure is not finite and unique on the exact basis, the step
   returns a gap or refusal; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams (AC-011,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-011-projection);
   provenance rc.2 AXIOMATIC_CALCULUS #ac-011-projection).
   Material not in the closure stays out; adjacent material does not enter
   because it exists
   ([RF-004](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-004-irrelevance-exclusion)).
3. Test fit against B. For the context dimension the test is a measurement:
   the bytes of the selected context are measured before any read and
   compared with the declared cap, and the measurement, the cap and the
   outcome are step-produced facts recorded before the read. If the context
   fits, activate. If it does not, one or more of these, in combination:
   refine the outer contract into steps whose contexts fit (§4); sequence
   activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return out_of_frame. Silent
   omission to fit is never one of them
   ([RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit)).
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

Activation. The actor or the assigning authority selects one frame or one
declared active frame configuration capable of the evaluation. Activation
binds each reusable frame declaration to the exact subject and basis and
loads the declared material relations and evidence sources, never an
undifferentiated workspace dump; what the actor receives is the packet of
REFERENCE_FRAME §11. When no available frame and actor pairing can lawfully
perform the evaluation, activation returns a refusal or out_of_frame; work
does not proceed through implied context (P0, P5; rc.2 RF
#select-and-activate).

The operation that joins AC-010, AC-011 and RF-002/003/004/014/017 into one
procedure is new in this corpus (P0). The method does not require proving
that no undiscovered material relation exists
([RF-003](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency)).

## 3. Result algebra

One core algebra for every evaluation and every step's stop state (P5):

| Result | Meaning |
|---|---|
| satisfied | the declared predicate holds on the exact basis |
| falsified | a declared counterexample defeats it |
| indeterminate | admissible evidence cannot decide it |
| out_of_frame | the evaluation needs an undeclared material relation or capability |
| invalid_basis | the subject or basis cannot support the evaluation |

Nothing is coerced to success; a missing, failed or out-of-scope result
returns its member, never satisfied. This conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
whose five members the table restates unchanged, and
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
whose rule that a failed, missing, indeterminate, out-of-scope or
invalid-basis result follows the declared algebra rather than being coerced
to success is the sentence above; both are restated here once and continue
to govern. REFERENCE_FRAME §3 states RF-012 as a law over frames and
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
states AC-007 as a law over constraints; each uses this algebra and neither
defines it again.

The boundary between out_of_frame and indeterminate is drawn on what the
activated frame declares and on what the step did with it (P5, finite
capacity and graceful total handling; the material relation drawn is the
out_of_frame boundary, three-way: capability not declared, capability
declared and exercised, capability declared and not exercised; rc.2 RF
#rf-012-closed-results). Three cases, and only the
first two are members of the algebra:

- out_of_frame when the claim requires a material relation or an evaluator
  capability that the activated frame does not declare. The result names the
  missing relation or capability, its owner where the subject gives one, and
  the reconfiguration pressure it creates (§4; rc.2 RF
  #reconfigure-when-necessary). A term the claim depends on and the frame
  leaves undefined is an undeclared material relation: its meaning can alter
  the result and it enters through no declared input (RF-003; P1). Whether
  the step exercised anything is irrelevant to this member; the ground is
  the missing declaration.
- indeterminate when every relation and capability the claim requires is
  declared and was exercised in the step, and the admissible evidence still
  cannot decide. The result names the evidence that would decide, as its
  residual uncertainty (rc.2 RF #return-a-closed-result).
- A declared capability that the step did not exercise yields no Reference
  Frame Method result for the evaluation at all: the claim is unresolved,
  not out of frame and not indeterminate, as a missing premise leaves a
  question unresolved rather than false (rc.2 RF
  #applicability-and-required-results). The step's stop state is
  `incomplete` under the construction availability refinement below, its
  work state (§5) carries the unexercised capability as a residual, and the
  actor says so rather than selecting a core member (P6; an actor cannot
  report an evaluation it did not perform). The evaluation's result and the
  step's stop state answer different questions (§1, Output), so the mapping
  of `incomplete` to the core does not make the evaluation indeterminate.

The first two cases restate RF-012's members with the boundary made
explicit, save the undefined-term clause of the first, which is a
tightening because it decides a boundary the predecessor leaves open; the
third is a tightening RF-012 does not name (P5, P6). The relation drawn is
three-way: capability not declared; declared and exercised; declared and
not exercised.

Evaluation. The evaluator applies the activated frame's declared
invariants, evidence rules and result algebra. It distinguishes semantic
law, observed evidence, inference and decision, and records every
assumption whose failure could change the result (P6; rc.2 RF #evaluate).

A composite over several results declares its conjunction (FOUNDATIONS §4).
The member it reports is chosen by that declared rule; every known failure
and uncovered obligation survives the join and is carried with the
composite. No universal order among the non-satisfied members exists; an
application declares its own.

Declared refinements answer different questions and keep their own
vocabulary, each with a total mapping to the core:

| Refinement | Question | Members | Core mapping |
|---|---|---|---|
| construction availability | did the step yield a candidate | candidate_ready, refused, incomplete, re_entry_requested | satisfied, falsified, indeterminate, out_of_frame or invalid_basis respectively ([work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result)) |
| disposition | what the decision owner does with an assessed candidate | accept, local_repair, re_enter, reject | consumes a core result; is not one ([UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)) |
| ambiguity outcome | what happened to a declared ambiguity | resolved, carried, escalated, blocked | a policy state over a core result ([Ambiguity Governance](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule)) |
| profile closure decisions | how a profile's unit closes | profile-defined | the profile declares its mapping; it may not add a core member |

### Disposition

Assessment of a candidate returns one of four semantic dispositions (P6,
P5; provenance rc.2 SPEC_METHOD #proportional-disposition):

| Disposition | Condition |
|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation |
| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent |
| `re_enter` | the governing outcome, a requirement, an identity, a lifecycle, an authority, a public contract or the accepted design must change |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path |

Global correctness means conserving every global relation affected by the
bounded action; it does not require proving the whole product inside every
local action (P4b). Repeated rejection against one unchanged boundary
requires reassessment of the frame altitude, the causal cone, the common
components, the design-versus-code placement and the authority
sufficiency. The method sets no rejection-count threshold, mandatory
review-round count or review state machine; it prohibits repeating an
unchanged failed construction relation as if iteration alone could close
it (P2).

## 4. Totality and refinement

Dispositions after any non-satisfied result are named in advance: continue
within the current contract when supported; refine; recover; yield; re-enter
the owning relation; terminate. Each admitted condition class has a declared
disposition, including an explicit unknown class. Total handling does not
claim that every external condition is recognised, that an invoked provider
terminates, or that every request can be completed. A hanging external call,
an unsatisfiable demand and a lost post-effect response are three different
cases and none is solved by adding a value to the algebra.

Ambiguity is carried or decided by lawful probabilistic processing where
policy allows, escalated to human adjudication where policy or risk appetite
requires, and recorded either way. Some conditions are hard stops regardless
of appetite: a violated invariant, an absent required authority, a missing
declared capability, an undeclared irreversible effect, an explicit human
gate (Ambiguity Governance, conserved).

Reconfiguration. An out_of_frame, invalid_basis, repeated indeterminate or
incompatible result causes one of: supply the missing admissible evidence;
select another actor inside the frame's capability envelope; activate
another existing frame; refine or extend a frame declaration; revise the
frame set (REFERENCE_FRAME §10); change the evaluation; or re-enter the
governing product or method relation. The disposition follows the cause; a
difficult evaluation alone does not prove that another frame is required
(P5, P2; rc.2 RF #reconfigure-when-necessary).

Refinement. An outer transformation T: A → X with success predicates P₀ … Pₙ
is refined by steps Tᵢ. The input of a step is its cumulative input, the
cumulative carried result of AC-016's reading: the outer input, which is
retained for every step, the last included, together with the earlier
outputs retained up to that step; the chained reading is the special case
in which no earlier output but the last is retained, and each Pᵢ ranges
over the cumulative input after i steps.
The composite's output is X, which the last step's postcondition, ranging
over its cumulative input, yields (P4a; AXIOMATIC_CALCULUS §5 AC-016
states the same reading for traversals). The refinement is faithful
when each admitted input satisfying Pᵢ yields an output with which the next
step's input satisfies Pᵢ₊₁, retains every applicable invariant, exposes
other outcomes without coercion, and each step's input satisfies that
step's domain and preconditions, the preconditions ranging over that
cumulative input (P4a). Then a successful composite carries P₀ to Pₙ by
induction. The cumulative input conserves the generic law that ODD §11.8
specialises (P4a, P4b; provenance rc.2
[ODD_METHOD §11.8](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#118-cumulative-environment-law-is-mandatory)).
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

Resumption is re-entry of the same method over current work state by a
possibly different actor. It recovers applicable progress, re-checks the
invalidators of each reused result (§7), reopens only affected support, and
reconciles uncertain external effects before any repetition. Resumption does
not imply idempotence: an action whose external effect may have occurred is
not repeated blindly; the lawful results are reconciliation, yield or stop.

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
derive its own progress and churn projections from them (P2).

The execution protocol of §1, §3 and this section is false if execution
proceeds from unreconstructable context; if a constructor's report
substitutes for required independent live evidence; if a bounded proxy
changes a governing relation outside its delegation; if unrelated
incompleteness blocks a closed causal cone; if a same-process test is used
to prove materially cross-process authority (§7); or if rejected activity
is reported as accepted progress.

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
actor can resolve; it grants no authority, weakens no invariant and waives
no acceptance (P6). The owning law may justify one coherent constraint
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
surface without materially reducing ambiguity; existing obligations absorb
new detail where they can without weakening ownership or meaning.

Apply this relation to the method's own execution: repeated source
acquisition, context assembly, hashing, activation preparation, status
recording, review and evidence generation serve an identified change,
decision or assurance need. Reuse stays subject to exact applicability and
invalidation (§7); repetition alone supplies neither validity nor
independence. Where this work materially affects the supported outcome, its
operational assumptions are qualified under UP-019 below. No universal
resource quota or separate accounting carrier follows. The delivery
priority this relation yields for a product outcome is SPEC_METHOD §8.

Cost is selected, not universal. Where capability fit or a cost claim is the
governed question, the activation declares its allowance and reports spend
with its measurement source, or records that the counter is unavailable
(new; P0 with UP-014's selection rule). Separate material startup, framework processing, external computation,
transport and assurance costs so that one cannot conceal another; declare supported input dimensions
and workloads before qualification
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019)).
Report volume is not model traffic; transferred context is counted across
every delegated actor, not only the coordinator. No universal quota, ticket
count, actor count or accounting carrier follows.

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
invalidate the affected result before reliance, preserving its
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
integration proof, the explicit non-changes and the assessor's disposition
(§3). Consumers choose the representation. Transition evidence is a read
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
| UP-020 and its six subsections | conserved in full; §1 (relation, intake, execution unit, roles and delegation), §3 (disposition), §5 (checkpoint, continuation, progress, churn, falsifiers), §7 (transition evidence and proof cadence); the generic work-state object, reconciliation of uncertain effects and non-idempotence in §5 are new; rows in the table below |
| UP-018 | conserved; §1 |
| Probabilistic Work Boundary | conserved; the object and commitment are FOUNDATIONS §2 and §3; §1 consumes them |
| RF engagement (establish basis, applicability, select and activate, evaluate, return, reconfigure) | conserved; §1 to §4 and §7; rows in the table below |
| AC-010, AC-011 | conserved; the laws themselves are restated in AXIOMATIC_CALCULUS §4, which disposes their rows; §2 applies them, joined with RF-002/003/004/014/017 into one operation (new); the step's local selection among fit options under an admitted grant is carried from RF-014; the RF laws themselves are restated in REFERENCE_FRAME §3 |
| RF-012, AC-007 | conserved; the algebra is defined once, in §3; REFERENCE_FRAME §3 states RF-012 as law and AXIOMATIC_CALCULUS §4 states AC-007 as law, and each points here; their rows are disposed in those members; the tenant text carries labelled tightenings: undefined term, unexercised capability |
| TICKET_METHOD work-carrier-to-execution rule, execution contract admission | the admission relation is restated in §1 with provenance; the rows are disposed at the TICKETS member |
| Baseline work result, UP-020 dispositions, Ambiguity Governance outcomes | conserved as declared refinements in §3 |
| ODD graph functions, ODD 11.8 | conserved; graph functions generalised in §4 to any realisation; the generic part of 11.8, a step's input as the outer input with every earlier output retained for it, conserved in §4 as the refinement input, the 11.8 row itself disposed in ODD §11.8; PROFILES §2 keeps the ODD binding |
| UP-017 | conserved; §4 |
| UP-021 and Standing Structural Qualification | conserved in full; §4; rows in the table below |
| UP-014, UP-005, UP-019 | conserved; §6 in full for UP-014's relation and method execution, its delivery priority in SPEC_METHOD §8; the allowance rule is new; rows in the table below |
| Return A Closed Result, TICKET judgment continuity | conserved; §7 |

RF rows received by this member (anchors into rc.2
REFERENCE_FRAME_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #engagement | not applicable: heading with no claim text (14 bytes); its children are disposed individually | §1 |
| #establish-the-evaluation-basis | conserved | §1 Intake |
| #applicability-and-required-results | conserved | §1 Applicability |
| #select-and-activate | conserved | §2 (Activation paragraph) |
| #evaluate | conserved | §3 (Evaluation paragraph) |
| #return-a-closed-result | conserved | §7 |
| #reconfigure-when-necessary | conserved | §4 (Reconfiguration paragraph) |

SM rows received by this member (anchors into rc.2 SPEC_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #proportional-method-and-delivery-stdo-up-014 | conserved; the relation, effective reasoning complexity, the constraint test, the symbolic-design paragraph, the disproportion test and the method's own execution are here; the delivery priority is SPEC_METHOD §8; "Ontology, IACS, Prime" generalised to "a detailed algebra or semantic design view" | §6 |
| #agentic-construction-execution-stdo-up-020 | conserved; the normative relation and the non-prescription of worker internals | §1 The step |
| #sufficient-execution-intake | conserved; all six items; the design-profile input laws are consumed by reference to PROFILES §3 | §1 Intake |
| #bounded-causal-construction | conserved | §1 Execution unit |
| #construction-assessment-and-delegation | conserved; "Executive" is written "coordinating role" in tier 1; the proxy limits are also EVALUATION §5 | §1 Roles and delegation |
| #proportional-disposition | conserved | §3 Disposition |
| #transition-evidence-and-proof-cadence | conserved | §7 Transition evidence |
| #checkpoint-continuation-progress-and-churn | conserved; "Product" is written "the selected outcome" in tier 1 | §5 |
| #complete-enclosing-relation-admission-stdo-up-021 | conserved in full | §4 Complete enclosing-relation admission |
| #standing-structural-qualification | conserved; all ten forms | §4 Standing structural qualification |
