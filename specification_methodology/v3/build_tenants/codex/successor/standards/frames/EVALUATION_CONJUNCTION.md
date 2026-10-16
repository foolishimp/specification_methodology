# Evaluation and Conjunction Frame

Scope: Judge and combine declared material predicates without erasing a failed relation, its original citations, incompatible basis or uncovered coverage. This frame supplies no acceptance or repair grant.

Bind this scope to the exact subject, selected governing basis, actor, capability
envelope, required coverage and existing grant before use. Any missing material
relation remains unresolved. The excerpts below are derived acquisition views of
the named owners; those owners retain authority. Section text is retained, with
relative links relocated to the same targets. A source digest binds the entire
owner, not proof that this selection suffices for another task.

## Governing argument routes

These source families state the premises, shared consequences and
additional choices behind the selected clauses. Acquire the relevant
argument when its derivation or applicability is material to this task;
a route alone does not discharge that judgment.

- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).
- [REFERENCE_FRAME_METHOD.md — Reference Frame Laws](../REFERENCE_FRAME_METHOD.md#reference-frame-laws).
- [TRANSFORMATION_LIBRARY.md — Foundational contract](../TRANSFORMATION_LIBRARY.md#foundational-contract).
- [FOUNDATIONS.md — Core contract derivations](../FOUNDATIONS.md#core-contract-derivations).

Source: [FOUNDATIONS.md — Result algebra](../FOUNDATIONS.md#result-algebra); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Result algebra

A result makes a claim about one predicate on one subject and basis. Its core
record contains the predicate, exact subject and basis, verdict, performance,
original qualified domain outcome, supporting evidence and citations, unresolved
obligations and material effect observations. A reference can carry these when
its resolution preserves their meaning and availability. This is a semantic
contract, not a mandatory serialization format or additional work carrier.

F1 selects the question and F2/F6 restrict its answer to supported evidence.
Because an execution can be interrupted and its effects can outlive its actor
(F3/F5), evaluation performance, the predicate's truth and effect completion
are separate questions. The informational contribution is the recoverable
meaning of each answer; the computational contribution is what was performed
and observed. The following value choices implement those distinctions.
RF-012 and every domain refinement bind all three questions before consuming a
label such as `ready` or `refused`; no label decides the other predicates.

The verdict has exactly these values:

| Value | Meaning for the bound predicate |
|---|---|
| `satisfied` | Admissible evidence establishes the predicate under its declared evaluation rule. |
| `falsified` | Admissible evidence establishes a counterexample or failure of that predicate. |
| `indeterminate` | The available admissible evidence does not decide the predicate. |
| `out_of_frame` | The predicate is outside the evaluation's bound scope or capability; it is not silently omitted from the wider obligation. |
| `invalid_basis` | The subject, governing basis or required interpretation is invalid for the claimed evaluation. |

Performance records whether the named predicate's declared evaluation was
actually undertaken; it is `performed`, `not_performed` or `unconfirmed`.
The activation identifies that evaluation separately from dispatch, admission
or the work being assessed. Retain the observed extent, interruption and
conclusion in its outcome and evidence. The legal pairs are:

| Performance | Permitted verdicts | Meaning |
|---|---|---|
| `performed` | Any of the five verdicts | Evidence establishes that the evaluation was undertaken, including a scoped basis or capability diagnosis. Its extent and conclusion remain separate facts. |
| `not_performed` | Any except `satisfied`, with the evidence condition below | Evidence establishes that the evaluation was not undertaken. Dispatch or admission alone does not establish performance. |
| `unconfirmed` | Any except `satisfied`, with the evidence condition below | Whether the evaluation was undertaken is not established. |

An interruption does not erase evaluation already undertaken or admissible
evidence obtained. A suite aborted after a witnessed failure is performed with
that partial extent and falsifies “all tests pass”. A completed load test that
cannot generate its required load is performed but indeterminate on the
requested service-performance predicate. Neither case is a never-run test.
Satisfaction still requires all evidence and completion conditions selected by
the predicate's evaluation rule; performed alone proves none of them.

When the selected evaluation was not undertaken or its performance is
unconfirmed, separately admissible counterevidence to its bound predicate can
still establish falsified; an established basis or scope diagnosis can likewise
establish invalid_basis or out_of_frame. The result identifies that independent
support without inventing execution. Without deciding support it is
indeterminate. An absent return establishes neither non-performance nor an
undecidable evaluation: retain the missing slot and what is actually known.

A missing required judgment stays an absent coverage slot, with the known
performance fact or its uncertainty; it is not a fabricated child result. A
performed but undecidable evaluation differs from a known unperformed one and
from unconfirmed execution. A failed admission check can conclude while
downstream work does not. The plan fixes which predicates are required; a
precondition is evidence for its dependent evaluation unless the plan separately
requires that precondition as a predicate. A concluding basis/scope diagnosis
on P reports invalid_basis/out_of_frame on P with its supporting evidence; a
different admission predicate is not silently substituted for P. An aborted
procedure does not erase separately authenticated counterexamples observed
during the attempt. Every result projection preserves these
coordinates and the original predicate; a verdict alone is an insufficient
handoff where performance is material.

An effect observation is `not_requested`, `not_started`, `completed`, `partial`,
`reverted` or `unknown`, on its declared observation boundary. These values describe the selected effect and observation
boundary, not the predicate verdict. `not_started` needs evidence that the selected effect did not begin, including
an authenticated rejection before mutation. Transport dispatch alone proves
neither effect completion nor absence; `unknown` includes a lost acknowledgment
after possible execution.
`reverted` means that at least one part began and every begun part is observed to have been reversed within
the declared boundary, with the reversal and any unstarted remainder retained
as evidence. For every effect value, the boundary includes each material part
the operation may have affected under its supported operating model and any
observed departure, whether requested or unintended. Irreversible messages or
other material external effects cannot be omitted to improve a result.
`partial` means an observed
completed part and an observed requested but unexecuted, or reverted, remainder.
If any material remainder has unknown completion, the state is `unknown`,
retaining the completed parts as evidence. An effect can be completed while
the intended product outcome is falsified.
An empty local log or discarded context does not establish no effect.
`not_requested` states an established effect-free scope under that operating
model; lack of a request alone is insufficient. A material possible unintended
effect without sufficient observation is `unknown`. If observation establishes
that an unrequested possible part did not begin, it contributes `not_requested`
at this boundary, retaining that observation and any earlier uncertainty.
It is not an uncompleted requested remainder. A requested part observed not to
begin remains `not_started`.

A refined value is the pair of original domain outcome and cause in its
declared reason domain, including an explicit missing-reason case. A domain
refinement preserves that qualified original outcome and supplies a
total, reason-sensitive map into this record. If the original outcome is too
coarse to determine a verdict, its required reason distinguishes the cases; a
consumer cannot guess from a word such as `refused`, `ready` or `accepted`.
A missing required reason maps the claimed predicate to indeterminate and
leaves that contribution inadmissible as deciding support for its slot;
retain its raw outcome and unresolved authentication. Its claimed predicate
remains indeterminate until admissible evidence decides it. Independently
established counterevidence or a basis/scope diagnosis uses the legal pairs above
on that same bound predicate; it does not invent execution or completion.
Requested or material possible unintended effects without sufficient observation
are unknown, never defaulted to not_requested. Unconfirmed evaluation performance
stays unconfirmed. Domain meaning stays with its domain owner.
No refinement turns failure, undecidability, non-performance or unknown effect
completion into greater standing. A new result over a different predicate does
not overwrite the earlier result.

Candidate availability, candidate fitness and authorised acceptance are three
predicates. `candidate_ready` can satisfy availability while fitness remains
falsified or unassessed. A lawful yield can satisfy the selected yielding
contract while product completion remains unresolved. A decision result binds
the predicate “disposition D on subject S at basis B was made under mandate M
by its bound authority”. A lawful rejection can satisfy that predicate while
candidate fitness remains undecided. Recording the decision is not its authority.
A not-applicable classification needs a supported applicability judgment; it is
never a synonym for a missing evaluation.

A stop reports the actual destination or task predicate through this record,
with its reason, observed effects and outstanding obligations. Its verdict
is indeterminate when the outcome remains undecided, falsified when admissible
evidence defeats that predicate, or the established scope/basis diagnosis.
Lawfulness of stopping is a separate decision predicate.


Source: [FOUNDATIONS.md — Result conjunction](../FOUNDATIONS.md#result-conjunction); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

## Result conjunction

Conjunction evaluates whether all required predicates and their material joins
hold on the declared composite subject and basis. It retains the contributing
results, their authentication and predicate mapping, known failures and their
citations, uncovered required coverage, uncertain effects and invalidators.
The aggregate is another result in the same algebra, with those components
available through sufficient references. Its summary never replaces them.

The required set comes from the composite's applicability and coverage
contract, not from the list of returns received. F4's preservation obligation
therefore makes a missing required return visible even when every available
return is satisfied. F2/F6 also retain an authenticated counterexample when
another slot is missing. Frame conjunction and the library's Conjoin operation
apply this same distinction; their owners supply which predicates and joins
are required, not another rule for erasing failures or filling gaps.

The aggregate evaluation has performance performed when its combining rule is
applied; this does not change component performance. The composite declares its
effect boundary and the selected effect parts within it. First resolve a current
observation for each part, retaining the contributing observations, identities,
ordering and any supported supersession. A later timestamp alone is no
supersession argument. Conflicting or insufficient observations leave the part
unknown. Normalize every material possibly affected part, including one owned
by an absent evaluation slot, through the effect-observation rule in
[Result algebra](../FOUNDATIONS.md#result-algebra). That rule distinguishes a requested part
that did not start from an unrequested possible part observed not to begin.
The composite supplies no different classification for either case.

Sequential stages can affect the same part. Their local completion labels are
not inputs to the composite join until mapped onto that part's observed state
at the composite boundary. A completed deployment followed by its completed
rollback is reverted for the deployment effect; a subsequent completed
reapplication is completed there. The historical rollback remains evidence.
The declarations retain every material external part, including irreversible
ones; a local reversal cannot silently remove them from the scope.

Over the resulting disjoint part observations: any unknown gives unknown;
all not_requested gives not_requested; completed with only completed or
not_requested gives completed; not_started with only not_started or
not_requested gives not_started; reverted with only reverted, not_started or
not_requested gives reverted; every remaining fully observed mixture gives
partial. Retain each observation's part and contributing components. The combining
operation's own lack of mutation cannot label an effectful composite not_requested.

First authenticate each contribution against its producer, subject, basis and
required plan membership. An unauthenticated claim cannot discharge an
obligation. A missing planned judgment remains an absent slot with its known performance
fact or uncertainty; required coverage outside an authenticated plan remains
uncovered. These are separate
conditions. An invalid contribution does not erase an independently
authenticated finding.

For an interpretable composite predicate and governing basis:

1. Any authenticated, applicable falsification of a required predicate or material join makes
   the conjunction `falsified`. Missing or undecidable other coverage remains
   explicit alongside it.
2. With no such falsification, an invalid required basis prevents satisfaction
   and yields `invalid_basis`; a required out-of-frame judgment yields
   `out_of_frame` when no invalid basis applies.
3. Otherwise any unresolved applicability, missing evaluation, undecidable
   predicate or undecided material join yields `indeterminate`.
4. `satisfied` requires every applicable obligation and material join to be
   authentically satisfied, with coverage itself established. An empty list
   proves nothing unless the declared required set is established as empty.

The composite declaration distinguishes its admission conditions from the
material joins of the predicate being evaluated. Each relation has one of
those roles in that evaluation. A failed admission condition prevents an
interpretation; a false required join is counterevidence within an admitted
interpretation. The result names that declared role instead of reclassifying a
known failed join as a missing basis. If the composite subject or governing basis itself cannot be interpreted, the
aggregate is `invalid_basis`; independently valid component failures and their
scope remain exposed. This does not pronounce them false or forgotten.
Effect uncertainty prevents satisfaction where the predicate requires a known
effect state. An unrelated effect does not automatically invalidate a different
predicate; the dependency relation must justify its relevance.

A declared operator states its truth and falsity conditions over exact leaf
predicates and joins. On its fully decided admitted domain, those conditions
are disjoint and exhaustive, including failure of a required join. An
overlapping, incomplete or uninterpretable operator declaration is invalid_basis.
Unresolved well-formedness makes the operator result indeterminate and supplies
neither satisfaction nor falsification; independently valid leaf results remain
visible. Once well-formedness is established, its result can be satisfied only when authenticated
evidence establishes its truth condition and the material joins and coverage
needed for that condition. It can be falsified only on an established falsity
condition. Otherwise a material invalid_basis yields invalid_basis, a material
out_of_frame yields out_of_frame when no invalid basis applies, and every
remaining undecided case is indeterminate. Only dependencies needed to decide
the bound predicate enter that ordering. Authentication, original failure
retention, performance and effect composition remain the rules above. Negation
or disjunction evaluates a different predicate; it cannot erase a failed leaf
or pass that result off as conjunction of all leaves. A first-nonfailure rule
cannot turn an undecided fallback into success.

Sequential composition records an unreturned dependent evaluation as an absent
slot, retaining its observed performance, extent and missing conclusion. A lawful regrouping requires the same interpretable composite basis, required
leaf predicates, joins, normalized effect parts and authentication, with no intermediate basis failure
hidden by the grouping. On that fixed domain, retained component sets combine
by union, the conjunction precedence is associative, and the effect join over
normalized disjoint parts is associative. The argument is mathematical: union
retains the same authenticated leaves under either grouping; selecting the
highest applicable diagnostic in the declared precedence over those leaves
has the same result. Normalized disjoint effect observations likewise retain
the same parts, so the stated unknown and completion conditions decide the same
aggregate. An intermediate result must retain those leaves and parts; a bare
verdict cannot establish this equivalence. This grants no associativity to an
arbitrary declared operator; regrouping it requires preservation of the same
outer predicate and its own demonstrated associativity law. An invalid
intermediate join is a failed premise of that rewrite, not evidence that every
arbitrary grouping is equivalent. Reordering
operations additionally needs an effect-independence law; associativity alone
supplies no such permission.

Sequential operations compose under their applicable owning contracts:
[UP-016/017](../DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016)
for design composition and [AC-016](../AXIOMATIC_CALCULUS.md#ac-016-typed-composition)
within a_c. Their returned result applies the operator rule above to the
declared outer predicate using
its preservation argument and the retained component results. For a pipeline
whose contract requires every stage postcondition, this is the conjunction
above; a recovery path need not require a failed earlier test to become true.
Unexecuted stages remain coverage facts, with no invented evaluations. A
sequence without an established outer interpretation or join returns the
applicable unresolved or invalid-basis result rather than a guessed success.


Source: [REFERENCE_FRAME_METHOD.md — Reference Frame Laws](../REFERENCE_FRAME_METHOD.md#reference-frame-laws); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

## Reference Frame Laws

The [F1–F6 commitments](../FOUNDATIONS.md#foundational-commitments) have their
standing at their owner. Each row assumes a declared evaluation and the
material relations named in it; neither the evaluation nor its authority is
derived from a resource limit. The linked rules decide the questions. Their
arguments distinguish the pillar contribution from the additional frame policy.

| Deciding family and consumer | Premises and pillar contribution | Conditional consequence | Additional choice and owner |
|---|---|---|---|
| [RF-001](../REFERENCE_FRAME_METHOD.md#rf-001-evaluation-relativity), used by Select And Activate and Diagnostic Order | F1 selects a question; F2 requires its interpreted subject. Specification supplies the intended decision and reference frames its bounded evaluation family. | A frame's presence in a set cannot establish that it can decide this question. Activation binds the actual evaluation to the declared family before relying on its sufficiency. | The frame owner declares the family and its tuple; the task owner selects the actual question. Similar names do not establish inclusion. |
| [RF-002–004](../REFERENCE_FRAME_METHOD.md#rf-002-finite-attention) and [RF-013–014](../REFERENCE_FRAME_METHOD.md#rf-013-reconstructable-activation), used by Select And Activate | F2/F3 distinguish current material state from its view; F5 bounds the actor. Reference frames contribute sufficient acquisition; world models and identity supply the bound subject. | A missing material relation cannot be replaced by ambient memory or an irrelevant easier question. If sufficient acquisition does not fit, the dependent evaluation needs a granted response or an explicit unresolved result. | This member selects family-relative sufficiency and reconstructability; frame-set authority selects the actor and partition. The execution binding selects its resource envelope, not a universal byte cap. |
| [RF-005](../REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates) and [RF-011](../REFERENCE_FRAME_METHOD.md#rf-011-topology-mutation-and-recharting), used by result reuse and Reconfigure When Necessary | F3 supplies scoped identity and changing topology; F2 restricts reliance to supported interpretation. Identity and evidence/correction contribute exact basis and invalidation. | Equal coordinates on a changed basis cannot preserve a judgment without its equality and applicability relation. A material topology change reopens the dependent claim before reuse. | Subject owners supply coordinate equality; the frame declares its invalidators. Foundations owns shared currentness; the domain selects recharting and observation mechanisms. |
| [RF-006–008](../REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation), used by Evaluate and Evidence Or Coordinate Translation | F2/F4 preserve interpreted distinctions across a relation; F6 separates evidence and grants. Information and interpretation preserve meaning; evidence and authority preserve the permitted evaluator, effect and disposition. | Shared evidence or overlapping coordinates neither equate two meanings nor grant a new effect. An evaluation needs the actual relation and mandate it uses. | This member names frame authority kinds. Their existing owners supply the grants; a translation owner supplies its declared mapping and loss. |
| [RF-009](../REFERENCE_FRAME_METHOD.md#rf-009-no-assumed-hierarchy) and [RF-016](../REFERENCE_FRAME_METHOD.md#rf-016-implementation-neutrality), used by Human Frame-Set Declaration, Frame-Set Optimization and Agentic Use | F4 supplies dependencies; F5 bounds capability; F6 bounds allocation authority. Reference frames distribute attention; computational execution supplies actor capability and communication conditions. | Functional decomposition, communication and authority do not become one hierarchy. One adequate frame or several may satisfy the same task while preserving required independence. | The frame-set owner selects its topology, representation and actor allocation under Foundations Configuration. No runtime, fixed role inventory or unique optimum follows. |
| [RF-010](../REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand), used by Using Frames In Conjunction | F4 requires preservation of the relation actually combined. Algebraic calculus contributes compatible joins; functional design separates internal execution from result consumption. | Closed results can be conjoined without merging internal manifolds. Transporting coordinates or combining execution requires the corresponding material composition contract. | This member selects composition on demand; the declared join owner supplies translation or execution law. Foundations owns result conjunction. |
| [RF-012](../REFERENCE_FRAME_METHOD.md#rf-012-closed-results) and [RF-015](../REFERENCE_FRAME_METHOD.md#rf-015-residual-uncertainty), used by Return A Closed Result and Result Conjunction | F2/F6 bind evidence to its predicate; F5 admits incomplete work. Information preserves the claim; computational execution distinguishes performance and effects; evidence/correction retains failures and gaps. | Admission refusal cannot fabricate a downstream evaluation or erase independently supported counterevidence. A lost return leaves performance and effects at their supported standing. | Foundations owns verdicts, performance, effects and combination. This member binds activation and downstream predicates separately; a frame owns finer outcomes and the decision owner owns disposition. |
| [RF-017](../REFERENCE_FRAME_METHOD.md#rf-017-proportional-compression), used by acquired frame views | F2 preserves meaning; F4 preserves failure detection; F5 bounds usable context. Information/interpretation and axiomatic calculus supply faithful task views; reference frames supply the actual consumer. | A smaller view fails when it drops a material permission, failure or uncertainty. Useful overlap remains when it supports independent assessment or a different capability envelope. | Faithful projection owns the shared fidelity decision; this member adds family-wide failure detection and fit. The frame owner selects compression and justified overlap. |
| [Applicability And Required Results](../REFERENCE_FRAME_METHOD.md#applicability-and-required-results) and [Workspace Coverage](../REFERENCE_FRAME_METHOD.md#workspace-coverage), used by engagement and coverage claims | F1 selects the governed outcome; F4 retains required predicates and joins; F2/F6 require support for exclusion. Specification supplies applicable obligations; algebraic calculus combines their results; evidence preserves uncovered scope. | An available family is not automatically required, while unknown applicability cannot exclude it. Received returns cannot determine the required set or prove complete coverage. | Owning predicates select obligations. This member chooses the coverage tuple, ledger and operational-full-coverage criteria; frame-set authority selects the declared inventory and justified exclusions. |
| [Discovery And Revision](../REFERENCE_FRAME_METHOD.md#discovery-and-revision), Completeness Boundary, Frame Qualification and Method Self-Qualification, used by diagnosis and closure | F2/F3 bind evidence to the actual subject; F4 preserves dependent claims; F5 limits the inspected population. Evidence/correction supplies counterexamples; reference frames supply bounded qualification and reconstruction. | A historical failure remains a diagnostic input, and one successful activation cannot qualify every family, actor or changed frame. Diagnose the failed relation before adding a frame. | This member selects diagnostic order and claim-scoped qualification tests. The adopting owner selects configuration and acceptance; unknown coverage remains open. |

### RF-001 Evaluation Relativity

Every frame declares the evaluation family it supports. A frame with no
declared evaluation family has no testable sufficiency boundary.

An activation uses that declaration to establish that its actual question is
in the family. Membership of the frame in an available frame set, or a similar
task name, does not establish that relation. A question outside the declared
family needs a suitable frame or the applicable scoped result; renaming the
question does not preserve the original obligation.

### RF-002 Finite Attention

An activated frame contains a finite attention surface that fits the selected
actor's declared capability envelope. A frame that requires undeclared ambient
memory, conversation history, or an effectively global workspace context is
not reconstructable for that actor.

### RF-003 Material Sufficiency

Apply [Contract application: Support](../TRANSFORMATION_LIBRARY.md#contract-application)
to the evaluation family `Q`: its known material relations, as defined by
[Material relation](../REFERENCE_FRAME_METHOD.md#material-relation), enter `M` or a declared authoritative
input. An omitted material relation makes the activation insufficient. This
known-relation boundary does not require proving that no undiscovered relation
exists.

### RF-004 Irrelevance Exclusion

Apply [Workspace and context](../FOUNDATIONS.md#workspace-and-context) to `Q`'s
attention surface: exclude relations established irrelevant to that evaluation,
retaining any material needed to establish irrelevance. A frame does not expand
merely because adjacent workspace material exists.

### RF-005 Exact Basis And Coordinates

Every result binds its exact subject, basis, coordinates, and evidence scope.
A stale, advanced, ambiguous, or mismatched basis returns `invalid_basis` or
requires reactivation. Apparent equality does not substitute for declared
coordinate equality.

### RF-006 Authority Conservation

A frame carries and applies admitted authority. It does not mint, widen,
transfer, or reconstruct semantic, evaluation, operation, or decision authority
from actor identity, available capability, evidence shape, implementation
reachability, or frame selection.

### RF-007 Semantic, Evidence, And Verdict Separation

Semantic law defines what the evaluation means. Evidence supplies observations.
The evaluator applies the declared relation. Where the evaluation performs a
material operation, the existing operation owner supplies the exact grant.
Decision authority disposes the result. A frame declaration keeps these roles
distinguishable even when one actor lawfully performs several of them.

### RF-008 Overlap Without Identity Collapse

Frames may share entities, variables, evidence, or coordinates. Shared material
does not establish identical meaning, basis, authority, or result. Every
cross-frame equality or translation used by an evaluation is declared where it
is needed.

### RF-009 No Assumed Hierarchy

The [configuration relation](../FOUNDATIONS.md#configuration) governs allocation
of tasks to bounded frames. Roles label selected responsibilities; they are not
an exhaustive primitive inventory or a prerequisite for every task.

Frames may relate through disjointness, overlap, refinement, restriction,
translation, temporal succession, composition, or governance. Parent and child
relations apply only where explicitly declared.

Functional decomposition, authority precedence, frame configuration, subject
topology, and evaluation dependency are distinct relation structures. A
consumer may align them where the governed subject warrants it. It may not
silently treat them as one hierarchy.

### RF-010 Composition On Demand

Using several frames does not require composing their internal manifolds.
Composition law is required only when the governing evaluation combines their
internal variables, transports evidence or values across them, or treats their
operations as one material execution relation.

Independently activated evaluations may instead return closed results to one
declared conjunction or decision rule.

Use [Result conjunction](../FOUNDATIONS.md#result-conjunction) for the result
relation. When the evaluation transports evidence or coordinates, or combines
operations into one execution, apply
[Composition law](../TRANSFORMATION_LIBRARY.md#composition-law) to that material
join as well. The latter obligation comes from the relation the consumer
actually uses, not from the mere count of contributing frames.

### RF-011 Topology Mutation And Recharting

An activated frame declares the topology changes capable of invalidating its
coordinates or materiality judgment. A detected material topology mutation
causes reevaluation, frame revision, or recharting before the previous result
is reused.

### RF-012 Closed Results

Every evaluation returns the [core result](../FOUNDATIONS.md#result-algebra)
bound to its exact frame, activation, subject, basis and predicate. The five
verdicts and their conjunction have that single owner. A frame-specific outcome
retains its original domain meaning and has one explicit mapping to the core
verdict for the declared predicate. An outcome lacking its required reason,
outside the declared mapping, or without its mapping's required support follows
the core missing-reason rule; its label supplies no deciding evidence.

An activation attempt and the work it would authorize are different subjects.
A refused activation records its own result on “this frame may be activated
for this actor, subject and basis”, with its cause and evidence. Established
failure of an admission condition maps to `falsified`; unresolved admissibility
maps to `indeterminate`. Capability, authority, basis and topology are the
conditions being checked, not the admission check's own capability or basis.
A declared ambiguity that prevents admission therefore falsifies admission;
uncertainty about whether that ambiguity exists remains indeterminate. If the
admission check itself lacks scope or a usable basis, its result follows the
core diagnosis rule instead. Missing causes follow the core missing-reason rule.

Where the plan requires the downstream work predicate, a separately established
capability or basis diagnosis can report `out_of_frame` or `invalid_basis` on
that predicate with its actual performance. Otherwise its slot stays absent
with the observed performance fact. Neither case fabricates a Worker return,
and an admission prohibition alone is no counterexample to downstream fitness.
Successful
activation satisfies admission only. The work remains `not_performed` until
actually undertaken. Each result retains performance and known effect state.

Where execution cannot be confirmed, retain the core `unconfirmed` performance
state. An absent return is not evidence that an invoked operation did not run.

A domain may refine these cases but cannot erase a failure, unknown, refusal,
non-performance or uncertain effect, or promote candidate availability into
fitness, acceptance or authority.

### RF-013 Reconstructable Activation

A fresh competent actor inside the declared capability envelope can reconstruct
the activated evaluation from the frame declaration, exact subject, basis, and
admissible inputs without undocumented conversational or historical context.

### RF-014 Capability Fit

Frame adequacy includes actor usability. When the material manifold exceeds an
actor's capability envelope, human authority may select another actor, refine
the frame, sequence activations, or provide a lawful compression. The actor may
not silently omit material relations to fit context.

### RF-015 Residual Uncertainty

Coverage and evaluation results retain known uncertainty. Unresolved relations,
uncovered evaluations, contested evidence, and unknown capability remain
explicit. Absence of a recorded counterexample is not evidence of universal
completeness.

### RF-016 Implementation Neutrality

This method requires the declared relations and observable outcomes. It does
not require a frame runtime, universal carrier, registry, controller, prompt
format, repository layout, collaboration topology, worker count, or software
framework.

### RF-017 Proportional Compression

A frame declaration compresses accumulated practice lawfully only when it
preserves the material distinctions and failure detections required by its
whole declared evaluation family, with adequate capability fit under RF-014.
A frame view applies [Faithful projection](../TRANSFORMATION_LIBRARY.md#faithful-projection)
from the owning declaration and material subject to the actor's evaluation
`Q`. Its required distinctions include `Q`'s failure detections; its adequacy
includes the capability fit in RF-014.

Compression does not require a unique smallest frame. Intentional overlap is
retained where it supplies independently activated evaluation, different
capability fit, different evidence altitude, or useful fault detection. Frames
are merged only when the merged frame preserves evaluation meaning, authority,
capability fit, and proportional reasoning cost.

### Engagement Atom And Semantic Prime

A reference frame is atomic at engagement altitude: it is activated and
evaluated as one bounded attention unit. Semantic irreducibility is a separate
question. One frame may contain several semantic atoms, and one semantic atom
may participate in several frames.

Where an adopting method supplies a Prime or equivalent semantic-contraction
law, that law governs the domain atom family. Frame-set contraction then asks a
different question: whether two frame declarations support the same evaluation
relation without material difference in evidence, authority, capability fit,
evaluation or assurance independence, or failure detection. A frame set is not
contracted into a disjoint minimum merely because its material variables
overlap.

---


Source: [REFERENCE_FRAME_METHOD.md — Applicability And Required Results](../REFERENCE_FRAME_METHOD.md#applicability-and-required-results); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

### Applicability And Required Results

The owning evaluation and scope declarations determine which frame obligations
apply to the exact subject. Evaluate their declared predicates from sufficient
basis-bound facts. A true predicate requires the applicable evaluation and
result; a false predicate excludes only that obligation under its cited
authority. Missing or ambiguous premises leave applicability unresolved, not
false. A frame name, available tool or listed family is no activation trigger
by itself. Where applicability needs residual semantic judgment, retain that
judgment and its evidence rather than representing it as a computed fact.

Use that applicability determination to bind the required set in
[Result conjunction](../REFERENCE_FRAME_METHOD.md#result-conjunction), including unresolved applicability.
Other applicable constraints remain in force even if only one evaluation detects
them. Qualification distinguishes true, false and unknown premises, missing or
wrong-subject required results, and a sufficient positive result within a finite
declared fixture; always skipping or always activating cannot meet that contract.


Source: [REFERENCE_FRAME_METHOD.md — Using Frames In Conjunction](../REFERENCE_FRAME_METHOD.md#using-frames-in-conjunction); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

## Using Frames In Conjunction

Frames participate together through four distinct relations.

### Independently Activated Co-Evaluation

Several frames may evaluate the same subject through separate activations and
return closed results. They may overlap in subject, manifold, or evidence
sources, but neither evaluation consumes or influences the other's unclosed
working result. This is useful for assurance independence, different evidence
altitudes, or distinct failure perspectives.

For a mutual-assurance claim, apply
[Parallel assurance and provenance](../FOUNDATIONS.md#parallel-assurance-and-provenance)
to the selected paths and their material shared causes. Separate activations
satisfying the declared authorship conditions do not by themselves establish
statistical independence or validate a shared governing expectation.

### Result Conjunction

A declared decision rule consumes closed frame results through
[core conjunction](../FOUNDATIONS.md#result-conjunction). Its frame-specific
binding states:

- which results are mandatory;
- how conflicting or indeterminate contributions are routed for re-evaluation;
- which basis relations must agree;
- what decision authority owns the conjunction; and
- whether any result may veto or defer the decision.

These parameters bind the mandatory claims and material joins before the core
rule is applied. Its result carries coverage, conflicts and residuals; the
decision rule cannot replace a required constraint with a count of agreeing
frames or acquire a contributing frame's semantic authority.

### Evidence Or Coordinate Translation

Apply [Faithful projection](../TRANSFORMATION_LIBRARY.md#faithful-projection)
with the producing frame's value or evidence as source and the receiving
frame's evaluation as consumer. Bind both `C` coordinate/equality laws and the
translation's refusal conditions alongside the shared preservation, loss and
provenance requirements.

The returned `translated_value`, `declared_loss` or `refusal` is retained with
its cause. Evaluate “this translation meets the bound target-use contract on
these source/target coordinates”: supported preservation, including expressly
admitted loss, maps to `satisfied`; an established forbidden loss, equality,
identity, basis-compatibility or authority violation maps to `falsified`;
undecided preservation or loss permission maps to `indeterminate`. If that
evaluation itself lacks material scope/capability or a usable basis, the map is
`out_of_frame` or `invalid_basis`, respectively. Missing causes use RF-012's
missing-reason rule. A coordinate mismatch established by a valid check is a
failed translation condition, not necessarily an invalid basis for the check.
All cases preserve actual performance and effects; refusal does not establish
the target predicate the untranslated evidence was intended to support.

### Material Composition

Apply [Composition law](../TRANSFORMATION_LIBRARY.md#composition-law) to the
frame-governed operations and the declared outer execution or reasoning
predicate. The application binds shared invariants, material effect or decision
order, closure and failure conditions, using each frame's `A`, `C` and `D`
relations for authority, coordinates and joins.

Composition is introduced only when the evaluation requires it. A possible
future interaction does not require a general composition law in every frame.

---


Source: [REFERENCE_FRAME_METHOD.md — Minimal Evaluation Result](../REFERENCE_FRAME_METHOD.md#minimal-evaluation-result); SHA256 `ddfab516705f945f2bf5e08b89ea32834273b7dd09f6c5bf9f583f9ea241645d`.

## Minimal Evaluation Result

```markdown
# Frame Evaluation Result

- frame identity and revision:
- activation identity:
- evaluation:
- exact predicate and domain refinement:
- subject and basis:
- actor and capability envelope:
- semantic, evaluation, operation where material, and decision authority:
- admissible evidence:
- core verdict and original domain outcome:
- performance and known effect state:
- inference relation:
- residual uncertainty:
- invalidation conditions:
- consuming decision or conjunction:
```

---


Source: [TRANSFORMATION_LIBRARY.md — Bind](../TRANSFORMATION_LIBRARY.md#bind); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Bind

Recover the current purpose, subject identity, governing specification, role,
authority, state and required relations. Conflicting, missing or stale bindings
are explicit results. A name, path, cached result or available tool is no grant.


Source: [TRANSFORMATION_LIBRARY.md — Acquire](../TRANSFORMATION_LIBRARY.md#acquire); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Acquire

Apply [Workspace and context](../FOUNDATIONS.md#workspace-and-context) to the
selected task. Bind the current subject, requirements, grant and destination;
resolve sufficient authentic material and material dependencies; reconcile stale
summaries with observations. That owner distinguishes context fit from attention
adequacy and states their evidence boundaries. For capacity misfit, apply [the admitted response rule](../FOUNDATIONS.md#finite-capacity-and-total-handling);
the selected grant determines available refinement, reassignment or escalation.
Capacity does not license omission.


Source: [TRANSFORMATION_LIBRARY.md — Evaluate](../TRANSFORMATION_LIBRARY.md#evaluate); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Evaluate

Apply the [core result algebra](../FOUNDATIONS.md#result-algebra) to the exact
predicate, subject and basis. Preserve the original domain outcome, performance,
effect observations, citations and residual coverage. A domain's evaluation
rule determines what evidence decides its predicate; it does not introduce a
parallel result algebra. Required independent authorship remains part of that
rule. Evaluation supplies no new operation or decision grant. A function may
exercise decision authority already admitted by its own contract, while the [Baseline Reviewer](../STDO_REFERENCE_FRAME_BASELINE.md) retains the
grant defined by that profile.

Bind [Assertions and observations](../FOUNDATIONS.md#assertions-and-observations)
to the source obligation, its interpreted required predicate, the assertion's
actual target and the observation/checker basis. Establish the implication
needed by this consumer before using a local pass or failure for the broader
claim. Bind actual observation acquisition as well as the ideal checker model;
an authenticated source or execution record supplies neither missing relation.
Use [Parallel assurance and provenance](../FOUNDATIONS.md#parallel-assurance-and-provenance)
to retain the assertion's derivation and the actual execution's provenance in
the existing evidence. The result remains on its original predicate, with
unresolved fidelity, unavailable observation and non-performance distinguished.

For an UP-020 assessment, the original assessor classification is a
reason-qualified outcome on the exact cone-preservation predicate. The
[Spec disposition consumer](../SPEC_METHOD.md#proportional-disposition) owns its
mapping and conditions. The actor with bound decision authority separately
returns the authorised disposition; the library supplies no second table.


Source: [TRANSFORMATION_LIBRARY.md — Conjoin](../TRANSFORMATION_LIBRARY.md#conjoin); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Conjoin

Apply [Result conjunction](../FOUNDATIONS.md#result-conjunction) to the selected
composite predicate, required coverage and material joins. Authenticate each
contribution and retain its predicate, original outcome and supporting evidence.
Known failure and required uncovered coverage both survive the aggregate. A
planned but absent judgment is not confused with uncovered coverage outside an
authenticated plan. Another declared logical operator uses the same core result
record on its own predicate; it cannot silently weaken conjunction.

When comparison or repeated evidence is used for mutual assurance, apply
[Parallel assurance and provenance](../FOUNDATIONS.md#parallel-assurance-and-provenance)
to the material shared causes and dependencies, and
[Risk and assurance selection](../FOUNDATIONS.md#risk-and-assurance-selection)
to any quantitative confidence claim. This evidence binding supplies no new
logical conjunction rule. One execution supporting several predicates is not
several independent observations.


Source: [TRANSFORMATION_LIBRARY.md — Contract application](../TRANSFORMATION_LIBRARY.md#contract-application); SHA256 `5e6103a666f0ceb866bda43c6a133a6f9815cf28148bc00b070a3c1f14daef10`.

## Contract application

A contract bounds an operation by its input and output domains, intended
predicate, governing constraints, material relations, evidence rule and actual
grants. Its binding names their owners and current basis. These are semantic
coordinates, not a required record format. An existing design, frame, function
or work carrier can supply them; this law requires no additional carrier or
validation stage.

The application predicate is: **this proposed operation or reliance is
admissible under this bound contract**. It differs from the predicate that the
operation achieves its intended outcome. Application uses the following
conditions once at the responsible consumer:

1. **Binding.** Identify the actual subject, intended predicate, governing
   interpretation, applicable policy and source/current-state coordinates.
   Names or equal bytes alone do not supply identity, standing or applicability.
2. **Support.** Account for the conditions and material dependencies capable
   of changing this determination. Inspect through an affected seam until its
   governing obligations are covered or evidence establishes independence of
   the far side. A task boundary, partial listing or absence of observed failure
   does not establish that independence. The domain selects its completeness
   and sufficiency criteria; the actor does not silently narrow them.
3. **Preservation.** Show that required input, output and cross-boundary
   relations hold under the declared compatibility or translation, applying
   [Preservation obligations](../FOUNDATIONS.md#preservation-obligations) to the
   claimed step or composition. Retain
   identity, meaning, lifecycle, producer/evidence coordinates, constraints,
   authority and effect distinctions where material. A difference may be
   lawful; it needs the instance's admitted relation. Neither universal field
   equality nor an invented translation decides compatibility.
4. **Authority.** Establish the actual operation or decision grant for the
   selected effect. Keep the owners of meaning, evidence, operation and
   disposition distinct. Shared code, a source reference or a satisfied
   judgment supplies no missing grant. Required independent assessment retains
   its owning conditions.
5. **Currentness.** Acquire observations, concurrency conditions and uncertain
   effects under [Workspace and context](../FOUNDATIONS.md#workspace-and-context),
   and apply [Change impact and evidence retention](../FOUNDATIONS.md#change-impact-and-evidence-retention)
   to reliance on existing evidence. A
   supported changed dependency reopens the affected determination; an
   unsupported currentness claim stays unresolved. A previously satisfied
   check can be reused on supported unchanged premises; this law does not
   require rechecking fixed graphs or every unchanged relation on every event.
6. **Result.** Apply the [core result and conjunction law](../FOUNDATIONS.md#result-algebra)
   on the actual predicates. Retain known failures, absent required coverage,
   scope/basis diagnoses, original domain outcomes, performance and effects.
   Unknown applicability is not non-applicability. A supported failure does
   not disappear because another required condition is undecided.

A consumer binds these conditions to its decision and domain exceptions rather
than copying the generic conditions into a second rule. Its dependency and
authority arguments are part of the existing decision evidence. Conditional
exceptions must be named at their owning policy; a generic application cannot
invent one. A library helper can implement several consumers, but their
subjects, required evidence and powers remain separate.

These conditions constrain what counts as admissible; they do not give a
universal algorithm for deciding arbitrary predicates. Insufficient support
returns the applicable core uncertainty or scope/basis result. A known violated
condition is retained with its evidence. A supported admissibility result
permits only the already-granted operation; it predicts neither success nor
termination. The control contract handles its observed outcome separately.

At design admission the bound instance is the proposed transition and its
complete enclosing relation. At frame activation it is the declared evaluation,
subject, basis and actor. Both use these same conditions; the design commit
predicate and frame capability predicate remain different domain decisions.
A consumer uses the supported condition once and retains its validity route;
a boundary crossing alone neither requires a second proof nor permits omission
of a changed material dependency.

### Constraint surface

For a current subject and basis, the bound contract describes the work allowed
by its constraints and grants. It also exposes obligations still unresolved.
This is the task's constraint surface. It distinguishes the permitted choices
inside the contract from the choices reserved to an owner. A missing condition
is not freedom; a condition proved irrelevant to this task need not be loaded
again while that proof remains applicable.

The surface can be represented as prose, typed relations, predicates, a_c or a
faithful task view. Dependencies can form a graph; they need not form a tree or
prescribe one execution order. A model must retain the distinction between
established facts, assumed premises, discretionary choices and unknowns. Its
constraint satisfaction result does not authenticate its observations or
appoint an actor. [a_c interpretation](../AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity)
binds the source-to-model relation and its independent evidence.

Two different implementations may both lie within this surface. Selection
between them follows the declared outcome, cost and owner criteria, not a
hidden requirement for the author's preferred implementation. A worker acquires
the sufficient constraints **and the actual material subject**; the abstract
surface alone is not a complete activation.

### Faithful projection

A projection or interpretation applies Contract application to a declared
source-to-consumer relation. Its binding states the authoritative source and
selector, target interpretation, consumer task, required distinctions, admitted
loss or approximation, and invalidation conditions. Source and target retain
their own identities. The domain owns additional publication and adoption
conditions.

For an exact projection, a consumer must recover the same material
determinations from the view and the owning source. Approximation requires a
declared adequacy relation and evidence of its end-to-end bound; local
tolerances alone do not compose. Lost authority, a weakened condition or an
unknown promoted to permission is a fidelity defect, not compression.

The binding determines whether a full reproduction, a narrower sufficient view
or an available authentic reference is required. Omitted task-irrelevant
material can remain at its owner. Material omissions, stale sources or
unavailable references prevent the corresponding reliance; they do not require
copying every source body into every event. A view has no independent power to
change its source meaning. Its currentness is established from the selected
source and dependency state, not from its label or generation timestamp alone.

Check fidelity against independently specified source decisions: at least the
material permissible, prohibited and unresolved distinctions for the selected
claim. A self-consistent model, matching schema, checksum or generated diff
checks a different relation. Failure re-enters the first owning defect: source
ambiguity, interpretation, projection, producer or consumer. It does not license
changing the source to agree with its view.

The consuming task determines which distinctions the check must preserve.
For an RF-017 frame view these include the evaluation's failure detections and
capability conditions; for an AC-017 interpretation they include the represented
predicates, dependencies and permitted latitude. A representation adequate for
one of those claims is not evidence for the other without the corresponding
source-to-consumer binding. This is the informational consequence of F2/F4;
neither predicate decidability nor a particular serialization follows from it.


Source: [FOUNDATIONS.md — Assertions and observations](../FOUNDATIONS.md#assertions-and-observations); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

### Assertions and observations

For an owning obligation r, let Q_r = interpret(r, Gamma, Omega) be its required
predicate over a declared case domain Omega. A case includes material inputs,
behaviour and environment. Justify this interpretation with its conditions,
exceptions and permitted alternatives. A source identifier or digest establishes
which text was selected, not that Q_r expresses it faithfully.

An assertion targets q_t. State whether it checks Q_r or a narrower condition,
and support the implication used by the consuming decision:

```text
Q_r implies q_t                     q_t is necessary for Q_r.
q_t implies Q_r                     q_t is sufficient for Q_r.
(q_1 and ... and q_n) implies Q_r    The stated conjunction is sufficient.
```

These are conditional on Gamma and Omega. A pass on a necessary condition
cannot establish Q_r. A collection of assertions needs its own coverage and
compatibility argument before its conjunction establishes Q_r. Valid different
realisations may satisfy Q_r with different outputs; equality is an oracle only
where the obligation requires it.

Let pi: Omega → O model the observations available to a checker,
and T contained in O × R be the checker's admitted evaluation relation, with R
the [core result records](../FOUNDATIONS.md#result-algebra). The following sat and fal abbreviate
their satisfied and falsified verdicts about q_t; they add no execution states:

```text
For every s in Omega:
  (pi(s), sat) in T implies q_t(s).
  (pi(s), fal) in T implies not q_t(s).
```

Identify the support and unresolved premises for each claimed direction.
Deterministic checking is a functional special case. Human or probabilistic
checking may admit different conclusions on the same observations; universal
soundness covers every admitted conclusion, not a favourable selected run.
A relation may soundly admit both satisfied and indeterminate without always
deciding. Its shape supplies no probability distribution. A restricted checker
model retains its declared scope; the actual checker and observation acquisition
need their own conformance support. An idealised pi does not prove that an
instrument or actor acquired the material facts correctly.

A reported pass or failure is an observation until the applicable oracle and
observation justification support the claimed conclusion. Assess it on the
original predicate through the core, retaining actual performance and effects.
Insufficient evidence is not a failure of the predicate; an unperformed check
is not a performed but undecidable one, and unknown effects stay unknown.

A checker claiming always to decide q_t correctly from pi alone requires:

```text
For all s and s' in Omega:
  pi(s) = pi(s') implies q_t(s) = q_t(s').
```

If equally observed admissible cases disagree on q_t, acquire distinguishing
evidence, justify a narrower scope, or return indeterminate on that attempted
decision. In a classical set model the condition permits a predicate on the
image of pi; it provides neither an executable decision procedure nor a cost
bound. Additional independently admissible evidence retains its normal core
standing; the limited observation is not permission to erase it.


Source: [FOUNDATIONS.md — Parallel assurance and provenance](../FOUNDATIONS.md#parallel-assurance-and-provenance); SHA256 `a3e19f8a266b11ed4322ffe1516686a4dba7033850cb7e9c86b3de807e414336`.

### Parallel assurance and provenance

Construction and assertion paths can derive from a common obligation through
different refinements. Their assurance depends on each path's justification,
not its length or label. Requirement-derived assertions assess the requirement's
applicable conditions; refinement-derived assertions assess their more detailed
conditions. Neither path automatically covers the other.

Assertion provenance identifies the owning obligation, interpretation,
assumptions, derivation and shared dependencies that justify the expected
predicate. Execution provenance identifies the actual checker, exact subject,
applicable environment, inputs, acquired observations and result. Preserve both
relations in existing bindings and evidence; execution logs cannot justify an
expected answer's derivation. A shared derivation can serve a declared family
without a separate document for every test.

An implementation-derived assertion can support regression or a stated local
property. Repeating that implementation's decision supplies no independent
upstream justification. A shorter assertion path can reduce acquisition or
execution cost when demonstrated for that path, but it supplies no automatic
correctness, coverage or independence.

Mutual assurance compares justified constructions or assertions on their stated
scope. Agreement admits shared error as well as correctness; disagreement
requires diagnosis and does not identify the faulty party by itself. Account for
material shared specifications, interpretations, tools, fixtures, observations,
copied contributions and other failure causes. Different actors, families or
codebases do not establish statistical independence. Repeating an observation
does not make it new independent evidence; required authorship independence
retains its own conditions.

Agreement within an incorrect common model cannot validate that model against
the desired outcome. Validation uses the model's declared purpose and material
external observations through their owners. Preserve counterexamples and route
supported corrections under [Bounded construction](../FOUNDATIONS.md#bounded-construction).
The dependence account constrains [risk and assurance selection](../FOUNDATIONS.md#risk-and-assurance-selection).
