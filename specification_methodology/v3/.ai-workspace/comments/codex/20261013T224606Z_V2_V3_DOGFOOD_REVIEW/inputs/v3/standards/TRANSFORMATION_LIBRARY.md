# Transformation Library

This member owns the shared transformation contract vocabulary for the
purposeful, specification-governed construction domain declared by
[Foundations](FOUNDATIONS.md#foundational-commitments). Bind, Acquire, Transform,
Evaluate, Conjoin and Dispose are responsibilities that can be composed or
co-located, not compulsory stages, actors or runtime APIs.

The contracts below are conditional on selected foundational premises and
instance choices. Particular methods retain ownership of their concrete types,
result refinements, applicability, adoption, admission and operation grants.
A contract definition does not supersede an owner determination or authorize
its use.

Its shared contract vocabulary resolves in bounded context
`urn:stdo:bounded-context:transformation-library`, owned by the STDO Specification
Methodology Product authority. The basis is this exact member digest and its
cited source-owned contracts under the activation's governing cut; its scope
is the generic contract vocabulary, conditional specialization arguments and
the explicitly imported authority vocabulary.
Named domain examples retain their source context; their role labels, types and
outcome enums are not local definitions or a shared library contract. A linked family correspondence
uses that context, while each named source function keeps its own context and
contract. Equal spelling is no equivalence or import. One function may have
several correspondences: this account is neither a partition nor a hierarchy.

## Reference-only semantic imports

The target context is urn:stdo:bounded-context:transformation-library and its
semantic owner is the STDO Specification Methodology Product authority.
Direction is source to this contract account; meanings are unchanged owner-qualified
references, with no translation, loss, inverse or ownership transfer. The source
context and owner are declared in [Frame Method's Position](REFERENCE_FRAME_METHOD.md#position).
Its exact source member digest is supplied by the selected complete cut or
frozen source inventory.
The target has its own exact member digest supplied by the frozen activation
or selected installed manifest. A review carrier is not an installed dependency
and supplies no authority. An activation binds
each member's distinct coordinates in its selected complete governing basis.
Changed member, basis,
source declaration or adoption premise invalidates reliance until applicability
is re-established. Source lifecycle and adoption conditions remain unchanged.

| Referenced concept | Source context | Exact source concept and owner |
|---|---|---|
| frame-set authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the human authority that declares or accepts the project frame set |
| semantic authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the owner of meaning for a material relation |
| evaluation authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the role permitted to perform an evaluation |
| operation authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the owner-issued grant to construct, transform, admit, publish, or mutate a material subject where an evaluation performs such an operation |
| decision authority | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the role permitted to accept, reject, or otherwise dispose its result |
| actor identity | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): the human, agent, tool, or process performing work. |

These imports provide no semantic, evaluation, operation or decision authority.
Missing meaning or authority bindings remain unresolved before dependent use.
The named Baseline Reviewer and WorkerResult cases below are owner-qualified
domain examples, not imported local role labels, aliases or outcome types.
Their source contracts retain applicability, adoption and activation conditions.

## Foundational contract

Premise owner: FOUNDATIONS.md, context urn:stdo:bounded-context:foundations,
under the selected complete STDO basis. F1–F6 retain their exact definitions
at that source. Direction is source premises to the library's conditional
contracts; no meaning is translated or lost and no authority is transferred.
The target is this member's context and its Product owner declared above. The
activation or installed manifest binds both exact member digests. A changed
premise, basis or adoption condition reopens the affected argument before use.

For one selected operation, let X and Y be its declared input and output
domains, K its interpretation, P its required outcome predicate, I its material
identity/state relations and G its actual effect or decision grant. These are
parameters, not serialized fields or a universal schema. The instance owns its original domain outcomes and their total refinement into
[the core result algebra](FOUNDATIONS.md#result-algebra). Unknown judgment,
non-performance and uncertain effects retain their separate coordinates.

- F1 and F2 require P to be about the intended subject under K; satisfying a
  different predicate cannot establish that outcome.
- F3 and F4 require I and the outer contract's material support to survive a
  handoff. Permitted variation or loss is an explicit instance choice.
- F2 requires a truthful unknown when material support is insufficient; F5
  supplies the selected domain's handling alternatives. Neither requires
  stopping unrelated authorized work.
- F6 requires an actual G before a dependent effect or disposition. Sufficient
  evidence for P cannot supply G.

An instance of Acquire returns support adequate for its selected predicate, or
the applicable core result on that exact acquisition predicate, retaining its
scope, basis or insufficient-support cause; Transform preserves the material
relations of the selected X-to-Y contract; Evaluate judges P rather than granting
effects; Conjoin uses the selected composite rule; Dispose chooses only from
already permitted actions. Bind supplies their current instance coordinates.
A single function can discharge several responsibilities. Every result uses the [core algebra](FOUNDATIONS.md#result-algebra); domain
refinements and independent assessment conditions stay with their owners.

## Work/recovery specialization

This chain specializes the generic contract for interrupted, purposeful work.
It assumes an admitted work identity, persistent workspace, selected outcome,
actual grants and a material uncertain effect. These are explicit instance
premises; they do not follow from finite capacity alone.

| Premises | Conditional consequence | Particular contract and independent choice |
|---|---|---|
| F1, F2; selected outcome and current subject | A current claim needs its actual predicate and support, not a remembered green status. | Spec Method UP-020 binds target truth and checkpoint; RF-005 fixes basis/coordinates. The owner chooses the outcome. |
| F2, F5; coupled material obligations and finite actor | Acquire sufficient material or return the admitted uncertainty; omitted support cannot become satisfaction. | RF-003/RF-014 bind sufficiency/capability; the work entry locates a responsibility view. Frame selection and configuration authority remain independent grants. |
| F3, F4; persistent work and affected dependencies | Re-enter on observed current state, retaining applicable progress and reconsidering changed support. | [Computed Classification And Treatment](SPEC_METHOD.md#computed-classification-and-treatment) and [Ticket reuse](TICKET_METHOD.md#work-carrier-to-execution-rule) bind applicability, invalidation and the wider frontier when dependency independence is unproved. Their concrete freshness rules are domain policy. |
| F2, F3, F6; an effect is uncertain and repetition could duplicate it | Neither historical intent nor a timeout proves completion or grants a safe repeat. Observe/reconcile, select another permitted action, or return unresolved. | [Workspace and context](FOUNDATIONS.md#workspace-and-context) owns the generic unknown-effect rule; [Computed Classification And Treatment](SPEC_METHOD.md#computed-classification-and-treatment) binds its Product context. The operation grant supplies allowed observation and repair. Idempotence must be established for the actual operation. |
| F1, F4, F6; required results and current mandate | Preserve failures, uncovered obligations and uncertainty; choose only an already-authorized continuation or truthful stop. | UP-020, declared conjunction and any adopted Baseline engagement specialize evaluation/disposition. Independence, decision rule and role adoption are additional owner choices. |

The consequences are arguments about the stated premises, not proofs of every
source clause. Concrete work-carrier layout, number of actors, numeric budgets,
optional Baseline adoption, release procedure and all domain result enums are
independent choices. They are not inferred from the foundational commitments.
This chain leaves those choices at their owners and adds no mandatory ledger.

A recovery activation uses the sufficient projected clauses and actual subject.
It need not load this entire argument, every method or historical event bodies.
The [ordinary work entry](../plugins/spec/skills/stdo-work/SKILL.md#acquire-the-responsibility-frame)
locates that material after basis selection. Its projection does not become a
rival authority or guarantee sufficiency for a different task.

## Transformation-admission specialization

This instance assumes a consequential entity transition, an identified current
predecessor, a declared candidate family, a durable commit boundary and actual
admission authority. These domain choices supplement F1–F6; the foundational
commitments do not choose an admission predicate, quorum or supported topology.

| Premises | Conditional consequence | Particular deciding owner and policy |
|---|---|---|
| F2, F3; current entity and predecessor are material | A candidate or judgment about another identity or superseded basis cannot establish this transition. | UP-016 declares exact basis continuity and enclosing joins; the domain chooses its identity and currentness law. |
| F4; a transition crosses material governing seams | Local validity cannot establish conservation of an unexamined affected relation; omitted support remains unresolved. | UP-017 determines the affected network and inherited invariants. Domain seam declarations supply design evidence; each UP-021 admission owner still derives and validates its complete enclosing relation and any claimed far-side independence. |
| F6; proposal, judgment and durable admission are distinct | A projection or satisfied judgment supplies evidence, not the missing admission grant. | UP-016 declares admitters, cardinality and competing-path disposition; UP-021 alone owns admission and standing-test semantics. |
| F2, F5; supported forms or commit effects are unresolved | Missing support cannot establish admission or non-applicability. Unknown effects remain explicit before dependent use. | UP-016 declares supported boundaries, partial-failure coverage and reconstruction; the owning admission relation retains its concrete outcomes. |

The [design admission consumer](DESIGN_MODULE_METHOD.md#admission-contract-use)
binds this contract to its transition relation and uses the consequences to
distinguish valid support from a shape-correct candidate lacking material basis
or authority. Its predicate, result refinement, commit-unit decomposition and
permitted direct/composite/nested forms remain domain policy. This argument
neither derives those choices nor creates an additional validation pass.

## Bind

Recover the current purpose, subject identity, governing specification, role,
authority, state and required relations. Conflicting, missing or stale bindings
are explicit results. A name, path, cached result or available tool is no grant.

## Acquire

Apply [Workspace and context](FOUNDATIONS.md#workspace-and-context) to the
selected task. Bind the current subject, requirements, grant and destination;
resolve sufficient authentic material and material dependencies; reconcile stale
summaries with observations. Measure context where the execution binding selects
it, and assess actual adequacy separately. For capacity misfit, apply [the admitted response rule](FOUNDATIONS.md#finite-capacity-and-total-handling);
the selected grant determines available refinement, reassignment or escalation.
Capacity does not license omission.

## Transform

Construct output or perform effects within the bound contract. Preserve the
original producer, material inputs and observed effects. Return the instance-owned outcome. A consumer-adopted, lawfully activated
[Baseline WorkerResult](STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame)
retains its declared outcomes; an [AC-013 instance](AXIOMATIC_CALCULUS.md#ac-013-transformation)
retains that owner's outcomes. These are original domain outcomes mapped under the core result contract. Apply the unknown-effect rule at [Workspace and context](FOUNDATIONS.md#workspace-and-context). The worker's internal search is its HOW; it cannot widen
the outer outcome or effect grant.

## Evaluate

Apply the [core result algebra](FOUNDATIONS.md#result-algebra) to the exact
predicate, subject and basis. Preserve the original domain outcome, performance,
effect observations, citations and residual coverage. A domain's evaluation
rule determines what evidence decides its predicate; it does not introduce a
parallel result algebra. Required independent authorship remains part of that
rule. Evaluation supplies no new operation or decision grant. A function may
exercise decision authority already admitted by its own contract, while the [Baseline Reviewer](STDO_REFERENCE_FRAME_BASELINE.md) retains the
grant defined by that profile.

For an UP-020 assessment, the original assessor classification is a
reason-qualified outcome on the exact cone-preservation predicate. The
[Spec disposition consumer](SPEC_METHOD.md#proportional-disposition) owns its
mapping and conditions. The actor with bound decision authority separately
returns the authorised disposition; the library supplies no second table.

## Conjoin

Apply [Result conjunction](FOUNDATIONS.md#result-conjunction) to the selected
composite predicate, required coverage and material joins. Authenticate each
contribution and retain its predicate, original outcome and supporting evidence.
Known failure and required uncovered coverage both survive the aggregate. A
planned but absent judgment is not confused with uncovered coverage outside an
authenticated plan. Another declared logical operator uses the same core result
record on its own predicate; it cannot silently weaken conjunction.

## Dispose

The actor carrying bound decision authority consumes exact closed work and evaluation results with the
current mandate. For an agentic construction instance it selects accept, local_repair, re_enter
or reject for the declared cone under [UP-020](SPEC_METHOD.md#agentic-construction-execution-stdo-up-020). It may select a next already-authorized action or stop under the instance's
permitted outcomes. Domain-specific yield remains with its declared owner. It cannot change upstream meaning or take a reserved owner decision.
Accept binds an exact checkpoint; it does not imply release. A Product-outcome
acceptance interval is separately governed by
[UP-013](SPEC_METHOD.md#product-outcome-conservation-stdo-up-013).

Other instances retain their original domain classifications as core refinements. [Ticket Method](TICKET_METHOD.md)
owns sprint/paydown and work-carrier closure classifications; [Release Method](RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015)
owns conserved/superseded/intentionally removed/not applicable. An actor carrying
that contract's bound operation authority may record condition-based closure
when that owning contract permits it.
Sharing Dispose machinery changes none of those grants or classifications.

The [UP-020 disposition conditions](SPEC_METHOD.md#proportional-disposition)
determine accept, local repair, re-entry and rejection for that contract. They
are applied once at that owner; this library does not redefine them.

## Composition law

[Transformation admission](DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)
and [bounded-frame conservation](DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017)
own design composition; [Foundations](FOUNDATIONS.md#result-conjunction) owns result conjunction;
[Frame Method](REFERENCE_FRAME_METHOD.md#using-frames-in-conjunction) binds its
application to declared frames, and [the calculus](AXIOMATIC_CALCULUS.md#ac-016-typed-composition)
owns its typed traversal composition. The account below preserves each owning
contract's restrictions; an explicit translation is lawful only where that
contract admits it.

For a selected construction handoff T: X -> Y and S: Y -> Z, the applicable
owner determines admission and the conserved meaning, identity, basis,
lifecycle, effects and authorities. A coherent composite basis can join distinct
bases under its declared topology; distinct authorities remain distinct and
conserved. Neither matching every field nor translating every difference is a
universal precondition. The outer contract determines required invariants. A
shared helper may serve several contracts without changing their owners.
Where independent judgment is required, author self-assessment does not replace it.

Identity and associative-composition claims follow their declared owner and
domain laws. For an algorithmic/categorical model, those laws and their proof
are separately required; this explanatory family establishes neither a new
composition obligation nor a universal category theorem for arbitrary software.

## Recovery law

Apply [Workspace and context](FOUNDATIONS.md#workspace-and-context) before
selecting the next dependent action. Bind current work identity, observe changed
material state, retain applicable work and reconsider affected support. Unknown
effects stay unknown until sufficiently observed or reconciled. Private context
is replaceable; the workspace survives the actor.

[Bounded construction](FOUNDATIONS.md#bounded-construction) supplies progress,
stop and total-handling distinctions. Spec Method binds Product progress and
owning-layer re-entry; [Ticket Method](TICKET_METHOD.md#work-carrier-to-execution-rule) binds carrier use; adopted profiles bind
their additional recovery duties. Retry applies the causal-change condition in
[Bounded construction](FOUNDATIONS.md#bounded-construction). A process restart by itself is an acquisition event, not proof that a
construction restart or workspace deletion is required.

Select a proof adequate to falsify the affected relation and satisfying its
required independence. Its cost selection follows [UP-014](SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014).
For a claim of continuity independent of private actor state, exclude that state
and compare the reconstructed decision with current material reality. A
same-context exercise cannot establish that claim.

## Cost and contraction

[Method proportionality](SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014)
owns the justification of method burden; apply its deciding definition rather
than treating raw counts as proof of improvement. For a computational or handoff cost claim, select those
measures material to that claim. Possible measures include transferred/acquired
bytes, attention, I/O, CPU, addressable memory, critical-path elapsed time,
aggregate work or displaced human assurance. This is an illustrative choice,
not an all-fields obligation, universal quota or separate accounting carrier.

A reference reduces storage only when its resolution preserves adequacy. A
smaller document or faster local preparation does not prove whole-path
improvement. Contract duplicated meaning and authority only while preserving
required distinctions and independent evaluations.
