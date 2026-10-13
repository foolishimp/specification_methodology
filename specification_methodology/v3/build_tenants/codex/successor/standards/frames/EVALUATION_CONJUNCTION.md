# Evaluation and Conjunction Frame

Scope: Judge and combine declared material predicates without erasing a failed relation, its original citations, incompatible basis or uncovered coverage. This frame supplies no acceptance or repair grant.

Bind this scope to the exact subject, selected governing basis, actor, capability
envelope, required coverage and existing grant before use. Any missing material
relation remains unresolved. The excerpts below are derived acquisition views of
the named owners; those owners retain authority. Section text is retained, with
relative links relocated to the same targets. A source digest binds the entire
owner, not proof that this selection suffices for another task.

Source: [FOUNDATIONS.md — Result algebra](../FOUNDATIONS.md#result-algebra); SHA256 `12d3dfbb4fcea4da6c7e4b0054c24be6d73f14b19b297f00dd14efa8fe9b196a`.

## Result algebra

A result makes a claim about one predicate on one subject and basis. Its core
record contains the predicate, exact subject and basis, verdict, performance,
original qualified domain outcome, supporting evidence and citations, unresolved
obligations and material effect observations. A reference can carry these when
its resolution preserves their meaning and availability. This is a semantic
contract, not a mandatory serialization format or additional work carrier.

The verdict has exactly these values:

| Value | Meaning for the bound predicate |
|---|---|
| `satisfied` | Admissible evidence establishes the predicate under its declared evaluation rule. |
| `falsified` | Admissible evidence establishes a counterexample or failure of that predicate. |
| `indeterminate` | The available admissible evidence does not decide the predicate. |
| `out_of_frame` | The predicate is outside the evaluation's bound scope or capability; it is not silently omitted from the wider obligation. |
| `invalid_basis` | The subject, governing basis or required interpretation is invalid for the claimed evaluation. |

Performance records whether the named predicate's declared evaluation procedure
reached its conclusion; it is `performed`, `not_performed` or `unconfirmed`.
The activation binds that procedure and its conclusion boundary before use. The legal pairs are:

| Performance | Permitted verdicts | Meaning |
|---|---|---|
| `performed` | Any of the five verdicts | The procedure concluded, including a scoped basis or capability diagnosis. |
| `not_performed` | `indeterminate` only | Evidence establishes no conclusion: it never started or aborted; retain which occurred. |
| `unconfirmed` | `indeterminate` only | Whether the procedure concluded is not established. |

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
`reverted` means that every begun part is observed to have been reversed within
the declared boundary, with the reversal and any unstarted remainder retained
as evidence. Irreversible messages or other material external effects must not
be excluded from that boundary to claim reversal. `partial` means an observed
completed part and an observed unexecuted or reverted remainder.
If any material remainder has unknown completion, the state is `unknown`,
retaining the completed parts as evidence. An effect can be completed while
the intended product outcome is falsified.
An empty local log or discarded context does not establish no effect. When no
effect is part of the operation, `not_requested` states that scope.

A refined value is the pair of original domain outcome and cause in its
declared reason domain, including an explicit missing-reason case. A domain
refinement preserves that qualified original outcome and supplies a
total, reason-sensitive map into this record. If the original outcome is too
coarse to determine a verdict, its required reason distinguishes the cases; a
consumer cannot guess from a word such as `refused`, `ready` or `accepted`.
A missing required reason maps the claimed predicate to indeterminate and
leaves that contribution inadmissible as deciding support for its slot;
retain its raw outcome and unresolved authentication. Its claimed predicate
remains indeterminate until admissible evidence decides it. An independently
established invalid basis instead yields invalid_basis for that diagnosis.
Requested effects without sufficient observation are unknown, never defaulted
to not_requested. Unconfirmed evaluation performance stays unconfirmed. Domain meaning stays with its domain owner.
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


Source: [FOUNDATIONS.md — Result conjunction](../FOUNDATIONS.md#result-conjunction); SHA256 `12d3dfbb4fcea4da6c7e4b0054c24be6d73f14b19b297f00dd14efa8fe9b196a`.

## Result conjunction

Conjunction evaluates whether all required predicates and their material joins
hold on the declared composite subject and basis. It retains the contributing
results, their authentication and predicate mapping, known failures and their
citations, uncovered required coverage, uncertain effects and invalidators.
The aggregate is another result in the same algebra, with those components
available through sufficient references. Its summary never replaces them.

The aggregate evaluation has performance performed when its combining rule is
applied; this does not change component performance. Aggregate effect state is
computed over the declared composite effect scope: any unknown gives unknown;
all not_requested gives not_requested; completed with only completed or
not_requested gives completed; not_started with only not_started or
not_requested gives not_started; reverted with only reverted, not_started or
not_requested gives reverted; every remaining fully observed mixture gives
partial. Retain which component each observation concerns. The combining
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

If the composite subject or governing basis itself cannot be interpreted, the
aggregate is `invalid_basis`; independently valid component failures and their
scope remain exposed. This does not pronounce them false or forgotten.
Effect uncertainty prevents satisfaction where the predicate requires a known
effect state. An unrelated effect does not automatically invalidate a different
predicate; the dependency relation must justify its relevance.

A declared operator states its truth and falsity conditions over exact leaf
predicates and joins. Its result can be satisfied only when authenticated
evidence establishes its truth condition and the material joins and coverage
needed for that condition. It can be falsified only on an established falsity
condition. Otherwise the invalid_basis, out_of_frame, indeterminate order
applies to dependencies that could decide it. Authentication, original failure
retention, performance and effect composition remain the rules above. Negation
or disjunction evaluates a different predicate; it cannot erase a failed leaf
or pass that result off as conjunction of all leaves. A first-nonfailure rule
cannot turn an undecided fallback into success.

Sequential composition records an unreturned dependent evaluation as an absent
slot, with known non-conclusion or unconfirmed conclusion as observed. A lawful regrouping requires the same interpretable composite basis, required
leaf predicates, joins and authentication, with no intermediate basis failure
hidden by the grouping. On that fixed domain, retained component sets combine
by union and the above verdict/effect operations are associative. An invalid
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


Source: [REFERENCE_FRAME_METHOD.md — Reference Frame Laws](../REFERENCE_FRAME_METHOD.md#reference-frame-laws); SHA256 `951e48d65137b7fe34d341e55937765ee8278ce93f5313adab37bd38419ddff6`.

## Reference Frame Laws

### RF-001 Evaluation Relativity

Every frame declares the evaluation family it supports. A frame with no
declared evaluation family has no testable sufficiency boundary.

### RF-002 Finite Attention

An activated frame contains a finite attention surface that fits the selected
actor's declared capability envelope. A frame that requires undeclared ambient
memory, conversation history, or an effectively global workspace context is
not reconstructable for that actor.

### RF-003 Material Sufficiency

Every known relation whose lawful change can alter the evaluation result,
basis validity, evidence sufficiency, operation authority, or decision
authority appears in the frame or enters through a declared authoritative
input.

Omitting a material relation makes the frame insufficient. The method does not
require proving that no undiscovered material relation exists.

### RF-004 Irrelevance Exclusion

Relations that cannot affect the declared evaluation remain outside active
attention unless they are required to establish irrelevance. A frame does not
expand merely because adjacent workspace material exists.

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
verdict for the declared predicate. An unclassified finer outcome is not
silently treated as satisfaction.

An activation attempt and the work it would authorize are different subjects.
A refused activation records its own result with the failed admission
predicate, cause and evidence; it does not fabricate a performed work result.
Missing capability maps to `out_of_frame`, an unusable subject/basis to
`invalid_basis`, an established admission prohibition to `falsified`, and
unresolved admissible admission evidence to `indeterminate`. Successful
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

A frame compresses accumulated practice when its declaration preserves the
material distinctions and failure detections required by its evaluation family
while fitting its capability envelope.

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


Source: [REFERENCE_FRAME_METHOD.md — Applicability And Required Results](../REFERENCE_FRAME_METHOD.md#applicability-and-required-results); SHA256 `951e48d65137b7fe34d341e55937765ee8278ce93f5313adab37bd38419ddff6`.

### Applicability And Required Results

The owning evaluation and scope declarations determine which frame obligations
apply to the exact subject. Evaluate their declared predicates from sufficient
basis-bound facts. A true predicate requires the applicable evaluation and
result; a false predicate excludes only that obligation under its cited
authority. Missing or ambiguous premises leave applicability unresolved, not
false. A frame name, available tool or listed family is no activation trigger
by itself. Where applicability needs residual semantic judgment, retain that
judgment and its evidence rather than representing it as a computed fact.

A required result that is absent, stale, bound to another subject/basis or
incapable of establishing its claim cannot satisfy a dependent conjunction.
Unresolved applicability withholds the dependent claim until sufficient
evidence or the owning decision resolves it. Other applicable constraints
remain in force even if only one evaluation detects them. Qualification of an
applicability rule must distinguish true, false and unknown premises, required
missing or wrong-subject results, and a sufficient positive result under a
finite declared fixture; always skipping or always activating cannot satisfy
those different expected outcomes.


Source: [REFERENCE_FRAME_METHOD.md — Using Frames In Conjunction](../REFERENCE_FRAME_METHOD.md#using-frames-in-conjunction); SHA256 `951e48d65137b7fe34d341e55937765ee8278ce93f5313adab37bd38419ddff6`.

## Using Frames In Conjunction

Frames participate together through four distinct relations.

### Independently Activated Co-Evaluation

Several frames may evaluate the same subject through separate activations and
return closed results. They may overlap in subject, manifold, or evidence
sources, but neither evaluation consumes or influences the other's unclosed
working result. This is useful for assurance independence, different evidence
altitudes, or distinct failure perspectives.

### Result Conjunction

A declared decision rule consumes closed frame results through
[core conjunction](../FOUNDATIONS.md#result-conjunction). Its frame-specific
binding states:

- which results are mandatory;
- how conflict and indeterminacy are handled;
- which basis relations must agree;
- what decision authority owns the conjunction; and
- whether any result may veto or defer the decision.

Conjunction does not transfer the semantic authority of a contributing frame.
The core rule retains both a known falsification and any uncovered required
coverage. This consumer binds the mandatory claim set before aggregation and
returns its coverage and residuals with the verdict. Counting agreeing frames
cannot discharge another frame's applicable constraint.

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


Source: [REFERENCE_FRAME_METHOD.md — Minimal Evaluation Result](../REFERENCE_FRAME_METHOD.md#minimal-evaluation-result); SHA256 `951e48d65137b7fe34d341e55937765ee8278ce93f5313adab37bd38419ddff6`.

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


Source: [TRANSFORMATION_LIBRARY.md — Bind](../TRANSFORMATION_LIBRARY.md#bind); SHA256 `6abf317ef235b08778e3ff5edc2477effab8fd05f328b91f14fcfb4953a0c3de`.

## Bind

Recover the current purpose, subject identity, governing specification, role,
authority, state and required relations. Conflicting, missing or stale bindings
are explicit results. A name, path, cached result or available tool is no grant.


Source: [TRANSFORMATION_LIBRARY.md — Acquire](../TRANSFORMATION_LIBRARY.md#acquire); SHA256 `6abf317ef235b08778e3ff5edc2477effab8fd05f328b91f14fcfb4953a0c3de`.

## Acquire

Apply [Workspace and context](../FOUNDATIONS.md#workspace-and-context) to the
selected task. Bind the current subject, requirements, grant and destination;
resolve sufficient authentic material and material dependencies; reconcile stale
summaries with observations. Measure context where the execution binding selects
it, and assess actual adequacy separately. For capacity misfit, apply [the admitted response rule](../FOUNDATIONS.md#finite-capacity-and-total-handling);
the selected grant determines available refinement, reassignment or escalation.
Capacity does not license omission.


Source: [TRANSFORMATION_LIBRARY.md — Evaluate](../TRANSFORMATION_LIBRARY.md#evaluate); SHA256 `6abf317ef235b08778e3ff5edc2477effab8fd05f328b91f14fcfb4953a0c3de`.

## Evaluate

Apply the [core result algebra](../FOUNDATIONS.md#result-algebra) to the exact
predicate, subject and basis. Preserve the original domain outcome, performance,
effect observations, citations and residual coverage. A domain's evaluation
rule determines what evidence decides its predicate; it does not introduce a
parallel result algebra. Required independent authorship remains part of that
rule. Evaluation supplies no new operation or decision grant. A function may
exercise decision authority already admitted by its own contract, while the [Baseline Reviewer](../STDO_REFERENCE_FRAME_BASELINE.md) retains the
grant defined by that profile.

For an UP-020 assessment, the original assessor classification is a
reason-qualified outcome on the exact cone-preservation predicate. The
[Spec disposition consumer](../SPEC_METHOD.md#proportional-disposition) owns its
mapping and conditions. The actor with bound decision authority separately
returns the authorised disposition; the library supplies no second table.


Source: [TRANSFORMATION_LIBRARY.md — Conjoin](../TRANSFORMATION_LIBRARY.md#conjoin); SHA256 `6abf317ef235b08778e3ff5edc2477effab8fd05f328b91f14fcfb4953a0c3de`.

## Conjoin

Apply [Result conjunction](../FOUNDATIONS.md#result-conjunction) to the selected
composite predicate, required coverage and material joins. Authenticate each
contribution and retain its predicate, original outcome and supporting evidence.
Known failure and required uncovered coverage both survive the aggregate. A
planned but absent judgment is not confused with uncovered coverage outside an
authenticated plan. Another declared logical operator uses the same core result
record on its own predicate; it cannot silently weaken conjunction.
