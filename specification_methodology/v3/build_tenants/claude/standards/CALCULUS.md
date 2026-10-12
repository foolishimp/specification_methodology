# CALCULUS

Tier 1. Owns how bounded work proceeds: the step, context construction under
an envelope, the result algebra, totality, refinement, work state and
restart, cost, and reuse. Consumes [FOUNDATIONS](FOUNDATIONS.md); adds no
definitions.

## 1. The step

A step is activated from an intake sufficient to reconstruct its governing
relations without conversation history, commentary or a prior actor's memory
(P0, actor-change premise). The intake names:

- the selected outcome, admitted prerequisite or experiment it serves (P2);
- the affected relation set and the invariants that govern it;
- the exact basis and the inputs it may acquire, each by identity and hash
  or by an input commit;
- the grant: the operations permitted, the territory that may change, and
  the decisions reserved to others (P6);
- the conditions that require re-entry at an owning relation;
- where the governed question is capability fit or a cost claim, the
  allowance and how spend will be measured (§6).

Conserves
[UP-020 intake](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)
and
[UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018).

The step's output is a candidate plus its step-produced facts: judgments with
their evidence, residuals, observations, authority decisions, provenance, and
one stop state from §3. The actor's internal path is not part of the output
and is not governed
([Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)).

Roles are relations over steps: a constructor produces the candidate and
self-review; an assessor evaluates a frozen candidate independently; a
decision owner disposes. One actor may hold several where independence for
the assessed claim is preserved; no role name confers an operation
([RF-016](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-016-implementation-neutrality)).
When one capable context has sufficient authority and intake, it enters
directly as constructor; coordination is selected only when material
contexts, authority or required independence need it.

## 2. Context construction under an envelope

Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R
   ([AC-010](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-010-material-closure)).
   If the closure is not finite and unique on the exact basis, the step
   returns a gap or refusal; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams
   ([AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection)).
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
to govern.

Where evidence is missing because a relation or capability needed to obtain
it was not declared, the result is out_of_frame; indeterminate is reserved
for the case where the declared capability was exercised and the admissible
evidence still cannot decide.

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

Refinement. An outer transformation T: A → X with success predicates P₀ … Pₙ
is faithfully refined by steps Tᵢ when each admitted input satisfying Pᵢ
yields an output satisfying Pᵢ₊₁, retains every applicable invariant, exposes
other outcomes without coercion, and each output satisfies the next step's
domain and preconditions (P4a). Then a successful composite carries P₀ to
Pₙ by induction. Coverage of the outer obligations, correctness of the local
implications and legitimate authority are premises, not conclusions; "each
step passed" is weaker than "the outer contract was conserved". Required
coupled relations must fit together in some step; unrelated obligations stay
outside the selected context. Every seam crossing the affected set includes
its far side or states why it cannot participate
([UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017)).
Admission of a material transition is one semantic commit of the complete
transition within its enclosing relation, or none
([UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021)).
This generalises ODD
[graph functions](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#graph-functions),
which refine one outer vector into a small inner workflow, to any
realisation; PROFILES §2 keeps the ODD binding.

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
A preservation checkpoint may retain unfinished work under an existing
grant; a proposed restart, which reconstructs from less than the retained
work, states why repair of retained work is insufficient, what survives and
which causal assumptions change; reconstructability alone does not select
reconstruction. Conserves
[UP-020 checkpoint and continuation](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020);
the generic work-state object, the reconciliation of uncertain external
effects and the non-idempotence rule are new (P0, P5 with the open-world
premise).

Progress is accepted material movement toward the selected outcome;
prerequisite work names what it enables; preservation and repeated proof are
evidence, not progress; rejected or superseded construction is churn;
discovering hidden distance revises the forecast and is not negative
progress. Volume of documents, code, tests, commits or reviews is not
progress.

## 6. Cost and proportionality

Proportionality is the relation between semantic ambiguity removed and
effective reasoning complexity introduced. An obligation, distinction,
carrier or document is justified when its contraction of the admissible
interpretation space pays for the concepts, joins, exceptions and states an
actor must hold to decide. Apply this to the method's own execution: source
acquisition, context assembly, hashing, activation records, status recording
and review serve an identified decision or assurance need. Conserves
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

Cost is selected, not universal. Where capability fit or a cost claim is the
governed question, the activation declares its allowance and reports spend
with its measurement source, or records that the counter is unavailable
(new; P0 with UP-014's selection rule). Separate startup, framework, external computation, transport and assurance
costs so that one cannot conceal another; declare supported input dimensions
and workloads before qualification
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019)).
Report volume is not model traffic; transferred context is counted across
every delegated actor, not only the coordinator. No universal quota, ticket
count, actor count or accounting carrier follows.

## 7. Reuse

A closed result is reused by an unchanged consumer after an applicability
check; a role, conversation or resumption change alone invalidates nothing.
Changed material inputs or a declared revising observation invalidate the
affected result before reliance, preserving the predecessor and any
demonstrably independent surviving results; a changed basis invalidates
likewise (judgment continuity names basis; Return A Closed Result names
inputs and observation). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. Conserves
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result),
[judgment continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity).

## 8. Source dispositions

| rc.2 clause | Disposition |
|---|---|
| UP-020 intake, cone, dispositions, checkpoint and continuation | conserved; §1, §3, §5; the generic work-state object, reconciliation of uncertain effects and non-idempotence in §5 are new |
| UP-018 | conserved; §1 |
| Probabilistic Work Boundary | conserved; §1 |
| RF engagement functions (establish basis, select and activate, evaluate, return, reconfigure) | conserved; §1–§4 |
| AC-010, AC-011, RF-002, RF-003, RF-004, RF-014, RF-017 | conserved; joined into the §2 operation (new); the step's local selection among fit options under an admitted grant is reframed from RF-014 |
| RF-012, AC-007 | conserved; restated once in §3 |
| Baseline work result, UP-020 dispositions, Ambiguity Governance outcomes | conserved as declared refinements in §3 |
| ODD graph functions | conserved; generalised in §4 to any realisation; PROFILES §2 keeps the ODD binding |
| UP-017, UP-021 | conserved; §4 |
| UP-014, UP-005, UP-019 | conserved; §6; the allowance rule is new |
| Return A Closed Result, TICKET judgment continuity | conserved; §7 |
