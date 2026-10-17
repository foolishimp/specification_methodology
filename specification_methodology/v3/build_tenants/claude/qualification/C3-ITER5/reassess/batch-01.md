# I5-03 reading batch 01

Rows: 34. Members: ['AXIOMATIC_CALCULUS.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `AXIOMATIC_CALCULUS.md#ac-001-closed-signature` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-001-closed-signature` at rc.2:

```text
### AC-001 Closed Signature

Every admitted object, relation, constraint, latitude, residual, traversal,
transformation specialization, and judgment belongs to one declared signature.
Every fundamental record also occurs exactly once in the total
`Population_M` function under its declared `RecordKind_ac`. Missing, duplicate,
shadowed, or unknown record kinds and populations fail closed.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-001-closed-signature`:

```text
### AC-001 Closed signature

Every admitted object, relation, constraint, latitude, residual,
traversal, transformation specialisation and judgment belongs to one
declared signature. Every fundamental record also occurs exactly once in
the total `Population_M` function under its declared `RecordKind_ac`.
Missing, duplicate, shadowed or unknown record kinds and populations fail
closed (P3, P5; rc.2 #ac-001-closed-signature).
```


### Row `AXIOMATIC_CALCULUS.md#ac-002-scoped-identity` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-002-scoped-identity` at rc.2:

```text
### AC-002 Scoped Identity

An identity resolves one member under one type, context, owner, scope, and
basis. Equal spelling, payload equality, graph position, or carrier equality
does not establish semantic identity.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-002-scoped-identity`:

```text
### AC-002 Scoped identity

This law applies the scoped identity of
[IDENTITY §2](IDENTITY.md#scoped-identity), the identity of an Object of
FOUNDATIONS §2, to every identity in `I`. Its coordinates map to that
identity as follows: the owner is the identity's authority, the type is
its kind, and the member it resolves is what its value denotes; context,
scope and basis are further coordinates, which IDENTITY §2 permits and
`a_c` requires. So an identity resolves one member under one type,
context, owner, scope and basis. That equal representations do not
establish equal meaning is FOUNDATIONS §2, Representation. The `a_c`
binding beside it: equal spelling, payload equality, position in any
structure and carrier equality do not establish semantic identity (P3;
rc.2 #ac-002-scoped-identity).
```


### Row `AXIOMATIC_CALCULUS.md#ac-003-reference-closure` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-003-reference-closure` at rc.2:

```text
### AC-003 Reference Closure

Every referenced identity resolves exactly once in the applicable model or
through one explicit external relation. Resolution uses the exact
`RefDomain_Sigma(source_record_kind, field)` declaration across the model's
record populations. Dangling, duplicate, wrong-record-kind, wrong-sort,
wrong-basis, locally-and-externally ambiguous, or undeclared-field references
refuse structural admission.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-003-reference-closure`:

```text
### AC-003 Reference closure

Every referenced identity resolves exactly once in the applicable model or
through one explicit external relation. Resolution uses the exact
`RefDomain_Sigma(source_record_kind, field)` declaration across the
model's record populations. Dangling, duplicate, wrong-record-kind,
wrong-sort, wrong-basis, locally-and-externally ambiguous or
undeclared-field references refuse structural admission (P3, P5; rc.2
#ac-003-reference-closure).
```


### Row `AXIOMATIC_CALCULUS.md#ac-004-relation-typing` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-004-relation-typing` at rc.2:

```text
### AC-004 Relation Typing

A relation is lawful only when its kind admits the exact source and target
sorts and all required qualifiers are present. Direction is material unless the
relation kind explicitly declares symmetry.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-004-relation-typing`:

```text
### AC-004 Relation typing

A relation is lawful only when its kind admits the exact source and target
sorts and all required qualifiers are present. Direction is material
unless the relation kind explicitly declares symmetry (P4a, P3; rc.2
#ac-004-relation-typing).
```


### Row `AXIOMATIC_CALCULUS.md#ac-005-authority-conservation` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-005-authority-conservation` at rc.2:

```text
### AC-005 Authority Conservation

Objects, relations, constraints, latitude, residuals, traversals,
transformations, projections, and judgments retain their declared semantic,
operation, evaluation, and decision authority. Copying, interpreting, encoding,
evaluating, or transporting a record does not transfer authority.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-005-authority-conservation`:

```text
### AC-005 Authority conservation

Objects, relations, constraints, latitude, residuals, traversals,
transformations, projections and judgments retain their declared semantic,
operation, evaluation and decision authority (the kinds of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds)). What
creates no authority is listed there; in `a_c` its instances are copying,
interpreting, encoding, evaluating and transporting a record, none of
which transfers authority (P6, P4b; rc.2 #ac-005-authority-conservation).
```


### Row `AXIOMATIC_CALCULUS.md#ac-006-basis-coherence` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-006-basis-coherence` at rc.2:

```text
### AC-006 Basis Coherence

Every fundamental record, model, and result binds an exact basis. Mixed bases
require an explicitly owned composite-basis relation. Individually valid
coordinates do not create a coherent composite basis by proximity.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-006-basis-coherence`:

```text
### AC-006 Basis coherence

Every result binds its exact basis under
[RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates), which
owns the exact-basis rule for results; what a basis is, including that
mixed bases need an explicit composite relation, is FOUNDATIONS §2,
Basis. This law binds the same rule to every fundamental record and model
of `a_c`: each binds an exact basis, the composite-basis relation of a
mixed basis is an explicitly owned record, and individually valid
coordinates do not create a coherent composite basis by proximity (P6, P3;
rc.2 #ac-006-basis-coherence).
```


### Row `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` at rc.2:

```text
### AC-007 Constraint And Refusal

Each constraint names its governed subject, predicate, judgment kind,
latitude, and refusal. A failed, missing, indeterminate, out-of-scope, or
invalid-basis result follows the declared result algebra rather than being
coerced to success.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`:

```text
### AC-007 Constraint and refusal

Each constraint names its governed subject, predicate, judgment kind,
latitude and refusal (§3, Constraint). The judgment of a constraint
returns one value of the core result algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results), directly or through a
refinement that the owning signature declares and that maps each of its
values to exactly one core value. Under the no-coercion rule of
FOUNDATIONS §4 Results, a failed, missing, indeterminate, out-of-scope or
invalid-basis result of a constraint follows that algebra and is never
coerced to satisfied (P5, P6; rc.2 #ac-007-constraint-and-refusal). The
core values, the rule that no mapping raises a result's standing and the
boundary among out_of_frame, indeterminate and an evaluation that was not
performed are FOUNDATIONS §4 Results'. This law applies them to the
judgment of a constraint and to the outcomes of the operations of this
member, and adds no core value.

Constraint results. The outcomes of a constraint's judgment map for the
predicate "the constraint's predicate holds for its governed subject on
the exact basis" (P5, P6):

| Outcome | Core value | Ground |
|---|---|---|
| holds | satisfied | the judgment establishes the predicate on the exact basis |
| failed | falsified | a counterexample defeats the predicate; the judgment names it |
| indeterminate | indeterminate | the admissible evidence cannot decide the predicate; the judgment names the evidence that would decide |
| out of scope | out_of_frame | the predicate is asked of a subject or relation outside the constraint's declared `applies_to`, context or scope, so deciding it needs a relation the constraint does not declare; the judgment names that relation, with its owner where the subject gives one |
| invalid basis | invalid_basis | the subject or basis cannot support the judgment; the judgment names the basis repair |

A missing result is no value of this refinement: a judgment that was not
performed has no closed result, is never `indeterminate`, and enters every
conjunction over it as a planned assessment without a closed result
(FOUNDATIONS §4 Results, Not performed).

Operation outcomes. A closure (AC-010), a projection (AC-011), the
structural admission of a record, model or carrier, the application of a
transformation (AC-013) and an interpretation (§6) each end in their
declared result or in one of the stops `hold`, `gap` and `refusal` that
this member writes. Where this member says that a condition refuses, the
operation returns `refusal` naming the condition; the record, model or
carrier is not admitted, and nothing is dropped silently. Each outcome
maps for the predicate "the operation yields its declared result on the
exact basis" (P5, P6):

| Outcome | Core value | Ground |
|---|---|---|
| declared result | satisfied | the closure, the projection with its boundary, the admission, the proposed successor `M_b_prime*` or the proposed model `M_subject*` is returned on the exact basis; a proposed successor or model establishes that it is available, never its acceptance or admission (FOUNDATIONS §4 Results) |
| `hold` | indeterminate | the operation was applied and stops because evidence, an observation or a disposition it needs is not yet admitted, so the admissible evidence cannot decide whether it yields its result; its residual names what would decide |
| `gap` | invalid_basis | the result needs a member, reference, resolution or declaration whose resolution on the basis is still open: the declared relation that resolves it has not yet decided it, as for an external resolution not yet evaluated; the result is undefined on this basis until it is supplied. A reference evaluated to no target is dangling and refuses (AC-003): a local reference with no record in the model's closed population, and an external reference whose declared resolution has been evaluated and yields no target |
| `refusal(constraint)` | falsified | every refusal that is not `refusal(basis)`: the refusal names a demonstrated violation of a declared law of this member or a constraint of its signature by the record, model, carrier, transformation or application under judgment, including a missing record family (AC-001), a dangling reference (AC-003) and an application without its traversal (AC-015), or it names no condition of the basis; the violation or other defect it names is the counterexample |
| `refusal(basis)` | invalid_basis | the refusal names one or more conditions of the basis the operation acts on and no demonstrated violation of a declared law or constraint by the record, model, carrier, transformation or application under judgment: a seed set, relation family, required-edge semantics, basis or scope that is not exact; a fixed point that is not finite and unique; an input model, subject or carrier whose exact identity, basis or admission is not established; or mixed bases with no composite-basis relation (AC-006) |

The cause is part of a refusal's value, because a refusal would otherwise
map to falsified or to invalid_basis according to its cause, and a refined
value maps to exactly one core value (FOUNDATIONS §4 Results,
Refinements). A refusal that names a demonstrated violation of a declared
law or constraint by the record, model, carrier, transformation or
application under judgment is `refusal(constraint)`, whatever condition of
the basis it also names. The basis condition is recorded with the refusal
and reported beside it as its own `invalid_basis` result, which names the
basis repair and answers the predicate of the evaluation that the
condition leaves without a supporting basis, never the operation-outcome
predicate that the refusal answers
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Predicates travel). A refusal that names only conditions of the basis is
`refusal(basis)`. A violation inside an input that the operation acts on
as its basis is a condition of the basis for that operation, not a
violation by what it judges, as the projection below shows. Purpose and
material relation: a demonstrated violation is a known failure, which
survives every join only as a `falsified` result, so a basis condition
named beside it neither hides the failure nor discards its counterexample,
and the basis repair stays named (FOUNDATIONS §4 Conjunction of results,
Survival; P5, P6). A basis mismatch inside a model or a record, a
relation's qualifier record included, is mixed bases with no
composite-basis relation (AC-006): a coordinate of the model or record
binds, or a reference in it resolves on, a basis that the governing basis
relation does not admit, as a wrong-basis reference of AC-003 does. It is
a condition of the basis, in the structural admission that judges that
model or record as in every other operation, and never a violated
constraint of a signature, even where the signature declares the basis
relation; a refusal that names only such a mismatch is `refusal(basis)`.
One defect can bear on two predicates: a model that violates AC-001 is
`refusal(constraint)` in the structural admission that judges it and
`refusal(basis)` in a projection over it, and each outcome answers its own
predicate. An operation that was not applied has no outcome. A stop `gap`
is a closed result with the value invalid_basis; it is not the absence of
a result that
[FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)
records as a gap. A signature's stop contract and a traversal record map
stops of their own under §5.

The mappings of both tables are new. Purpose and material relation: a
constraint result or an operation's stop combines with results of other
members only through the one core, so a refusal, a hold or a gap is
neither read as success nor mistaken for another case; and a closure or
projection that is not established has the value invalid_basis here, as
the activation outcome `closure_unresolved` of
[ACTIVATION §3](ACTIVATION.md#admission-and-activation) has for its own
predicate (P5, P6).
```

Successor, `FOUNDATIONS.md#results`:

```text
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

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P5 (derived from P0 and P6), P6 (independent); (i), (ii) | every performed evaluation returns one closed value of one algebra shared by every member, with a value for a claim that holds, one that fails, one the evidence cannot decide, one that needs a relation or capability the frame lacks, and one whose basis cannot support it | [Results](#results), the value table | the value names, and the division of P5's outcomes other than success into `indeterminate`, `out_of_frame` and `invalid_basis`, conserved from RF-012; owner: this section | 3, 9 |
| P6 (independent), P5 (derived from P0 and P6) | a result claims no more than it establishes: only `satisfied` establishes the predicate, and no refinement or mapping raises a result's standing | [Results](#results), Standing, and the rule that nothing raises standing; for the choice, [Conjunction of results](#conjunction-of-results), Reported value | the order among the four other values within one combination; owner: the member or profile that applies the conjunction, in its declared rule | 9 |
| P1 (independent), P6 (independent); (iii) | a core value alone does not carry a refined value's domain meaning, so a result records its predicate and domain outcome, and the definer of a refined value keeps its meaning | [Results](#results), Recording | each refined value and its domain meaning; owner: the member, profile or adopting Product that defines it | 6, 3 |
| P6 (independent) | an evaluation that was not performed supports no claim, so it has no closed result and is never read as undecided | [Results](#results), Not performed, and the third item of the rule that nothing raises standing | recording non-performance as the absence of a closed result, not as a core value; owner: this section | 9 |
| P5 (derived from P0 and P6), P1 (independent); (ii), (iii) | results from different members combine only if every refined value reads as exactly one core value and `indeterminate`, `out_of_frame` and `invalid_basis` stay explicit | [Results](#results), Refinements | each refinement's question, predicate and values; owner: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) for admission, activation and steps, otherwise the member, profile, project or adopting Product that defines it | 3, 6 |
| P6 (independent), P0 (recovered, with its premise that a step's output is a candidate until evaluated) | that a candidate exists, that it meets its criteria and that its owner accepts it are three claims with three predicates, and producing a candidate establishes neither of the others | [Results](#results), availability, assessment and acceptance | the acceptance boundary and who accepts there; owner: the decision authority that [EVALUATION §5](EVALUATION.md#5-acceptance) names | 9 |
| P5 (derived from P0 and P6), P0 (recovered), P6 (independent) | a claim that needs a relation or capability the frame does not declare cannot be decided in that frame; one the admissible evidence cannot decide is a different case; and a declared capability left unexercised leaves its part without a result, while a counterexample already found stands | [Results](#results), Out of frame or indeterminate | the stop state that carries an unexercised capability; owner: [ACTIVATION §3](ACTIVATION.md#construction-availability), construction availability | 7, 9 |
| P1 (independent), P3 (independent), P5 (derived from P0 and P6) | for an evaluation that depends on a concept imported from another member, a missing source meaning, adoption or authority binding is a relation the frame does not declare, and a changed member or basis whose applicability is not re-established cannot support the evaluation | [Imports between members](#imports-between-members), the grounds of `out_of_frame` and `invalid_basis` | none | 6 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P6 (independent); (ii) | a combination keeps failures, unperformed assessments and uncovered obligations apart and carries each through every join; agreement among contributors discards no counterexample | [Conjunction of results](#conjunction-of-results): its three inputs, Gaps, Survival, Predicates travel | none | 3, 9 |
| P3 (independent), P5 (derived from P0 and P6), P6 (independent); (i), (ii) | a result supports its predicate only on the basis it binds, so a component held only on another basis has, on the basis the composite requires, no performed evaluation and is a gap, while an evaluation performed on a basis that cannot support it decides its own predicate as `invalid_basis`; one component is never answered both ways | [Conjunction of results](#conjunction-of-results), Stale results | none | 3, 9 |
| P5 (derived from P0 and P6), P6 (independent); (ii) | a composite with a gap or a non-satisfied mandatory result is never `satisfied`; where every mandatory result is `satisfied`, its own value is `invalid_basis` if the declared basis relations disagree, and otherwise `indeterminate` while a gap remains; with every mandatory result `satisfied`, agreeing bases and no gap, a material counterexample to a mandatory constraint falsifies it whichever contributor found it, and without one its value is the one its declared rule gives over the mandatory results; a `falsified` result that is not mandatory stays in its record | [Conjunction of results](#conjunction-of-results), Reported value | which non-satisfied value is reported; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P6 (independent), P4a (independent); (ii) | a conjunction decides only under a declared rule and transfers no contributor's semantic authority | [Conjunction of results](#conjunction-of-results), The declared rule | the mandatory results, the handling of conflict and indeterminacy, the basis relations that must agree, the decision authority that owns the conjunction, how results that are not mandatory count, and any veto or deferral; owner: the member or profile that applies the conjunction, in its declared rule | 3, 9 |
| P4a (independent), P4b (derived from P0 and P2) | composed steps exist only under typed composition; the composite carries both steps' step-produced facts, and its result for the outer predicate is the conjunction over the outer contract's obligations | [§4](#4-algebra) Composition; [Conjunction of results](#conjunction-of-results), Composition of results; [RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand), outside this member | whether a composition law is needed, under the conditions RF-010 states; owner: the governing evaluation | 3, 4 |
| P4b (derived from P0 and P2), P3 (independent) | every transformation records what it preserved, introduced and removed, its external witnesses and its residuals, so no fact is lost unrecorded | [§4](#4-algebra) Conservation accounting | the record's fields; owner: [AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation) | 3 |
| P4b (derived from P0 and P2), P5 (derived from P0 and P6), P0 (recovered) | a reference stands for a body only where it supports the same consuming decision; otherwise the shortfall is a residual, never success, and no carrier or budget limit trims a required member | [§4](#4-algebra) Reference versus body | none | 6, 7 |
| P1 (independent), P6 (independent) | two values differ lawfully only through a declared relation; preference, probabilistic choice and human presence supply none | [§4](#4-algebra) Latitude | each latitude or transformation relation; owner: the owner of the contract that declares it | 3 |
| P3 (independent), P6 (independent) | similar computation proposes shared machinery and never decides identity or authority; each instance keeps its responsibility and binding | [§4](#4-algebra) Shared machinery | whether one implementation serves several instances; owner: the accepted design of the realisation that would share it, which [DESIGN_MODULE §5](DESIGN_MODULE.md#capability-and-foundation-selection-up-023) refines for software design where that profile is selected | 4 |
| P6 (independent), P1 (independent) | a categorical claim is established only with its demonstration, and without it is a hypothesis | [§4](#4-algebra) Formal fragment | which categorical claims are made; owner: the member, profile or adopting Product that makes the claim | 3 |

RF-012 in [REFERENCE_FRAME §3](REFERENCE_FRAME.md#rf-012-closed-results),
AC-007 in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal)
and [EVALUATION §4](EVALUATION.md#4-review-results) apply the first row's
algebra to frames, constraints and reviews and add no choice of their own
beyond any refinement they map under the fifth row;
[ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition) holds the
step's refinements of the fifth row and the stop state of the seventh.

Consumers of these rows, one list per row, each consumer linked to its own
locus:

- Row 1, the value table: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), where a step returns each performed evaluation's core value, and [§1 Applicability](ACTIVATION.md#applicability), whose applicability decision is a core value; [REFERENCE_FRAME §3 RF-012](REFERENCE_FRAME.md#rf-012-closed-results); [AXIOMATIC_CALCULUS §4 AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) and [§9 Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces), required results; [EVALUATION §4](EVALUATION.md#4-review-results) and [Result and triage projection](EVALUATION.md#result-and-triage-projection), total over the core values; [RELEASE §1](RELEASE.md#1-context-and-position), Results, and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015), where qualification records a core value for each disposition; [CONFORMANCE](CONFORMANCE.md#conformance), its preamble, where an assessment returns a core value for the case's predicate; [ASSURANCE §7 The set](ASSURANCE.md#the-set); [DESIGN_MODULE §10 Totality](DESIGN_MODULE.md#totality); [SPEC_METHOD §2 Requirement categories and classification](SPEC_METHOD.md#requirement-categories-and-classification) and [Operational lifecycle sufficiency](SPEC_METHOD.md#operational-lifecycle-sufficiency), [§4 Change classes](SPEC_METHOD.md#change-classes) and [Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), and [TICKETS §4 Status](TICKETS.md#status) and [§7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity), where an evaluation that reads a declared state or classification returns its own core value; [EXECUTIVE_BASELINE §12 step 6](EXECUTIVE_BASELINE.md#6-reviewer-returns-to-executive), the Reviewer's core result; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where an evaluation returns a core value directly when none of the profile's values applies; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 50.
- Row 2, standing and the rule that nothing raises it: [ACTIVATION §3 Effects](ACTIVATION.md#effects), where success is never claimed for an effect that may still be acting; [ASSURANCE §13 Claim boundaries](ASSURANCE.md#claim-boundaries), where a claim with an unresolved condition is never `satisfied`; [EXECUTIVE_BASELINE §22 Closure](EXECUTIVE_BASELINE.md#22-closure), where `indeterminate` never maps to `satisfied`; [DESIGN_MODULE §10 Post-ticket design review](DESIGN_MODULE.md#post-ticket-design-review), where a falsified closure claim never becomes `satisfied`; [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), whose stop values never map to `satisfied`; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where no mapping raises a result's standing; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 47; for the choice, the consumers of row 11.
- Row 3, recording: [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where each value keeps its vocabulary, residual and re-entry law beside its core value; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), where each closure decision keeps its vocabulary and refs beside its core value; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where the value travels with the predicate and the outcome's meaning stays there; [ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), where each outcome keeps its domain outcome with the value; [DESIGN_MODULE §7 Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation), where a verdict recorded with its value keeps the distinction between not applying and meeting the axiom; [TICKETS §3 Close review](TICKETS.md#close-review), where the change class travels with the core value as the domain outcome; [ASSURANCE §7 The set](ASSURANCE.md#the-set), where a core result is recorded with the predicate the frame's claim states; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 47 and 48.
- Row 4, not performed: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), where an evaluation the step did not perform has no result, [§1 Roles and delegation](ACTIVATION.md#roles-and-delegation), where an actor cannot report an evaluation it did not perform, and [§5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account); [EVALUATION §4 Result and triage projection](EVALUATION.md#result-and-triage-projection), where a predicate not performed has no payload; [CONFORMANCE](CONFORMANCE.md#conformance), its preamble, and [§5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), Coverage, where a case not run and assessed on this revision has no result, and discriminator 39; [RELEASE §8 External qualification dependencies](RELEASE.md#external-qualification-dependencies), where a clean skip is an evaluation not performed, and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015), where an unresolved disposition has no result; [DESIGN_MODULE §7 Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation), where an applicable axiom the pack did not evaluate has no result; [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where an unrun verification has no closed result.
- Row 5, refinements: [ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition), which owns the refinements for admission, activation and steps in [Admission and activation](ACTIVATION.md#admission-and-activation), [Construction availability](ACTIVATION.md#construction-availability), [Disposition](ACTIVATION.md#disposition), [Ambiguity outcome](ACTIVATION.md#ambiguity-outcome) and [Effects](ACTIVATION.md#effects); [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), the outcomes of `activate`, `conjoin` and `translate`, and [§8 Coverage ledger](REFERENCE_FRAME.md#coverage-ledger), the statuses; [AXIOMATIC_CALCULUS §4 AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal), a refinement the owning signature declares, and [§5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), the stop algebra; [ASSURANCE §12](ASSURANCE.md#12-counterexample-localisation), the four forms; [DESIGN_MODULE](DESIGN_MODULE.md#design_module), its lead, with [§7 Invariant reconstruction sufficiency](DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018) and [Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation); [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds) and [Mutable-subject effect relation](TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation); [ODD §9](ODD.md#9-method-governance-and-audit) and [§11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop); [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile); [TICKETS §3 Close review](TICKETS.md#close-review), whose classifications each take one core value; [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method) and [§11](SPEC_METHOD.md#11-build-tenant-binding), where each operation outcome maps to exactly one core value; [PRODUCT_DEFINITION §4 Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update); [EXECUTIVE_BASELINE §5 Work result](EXECUTIVE_BASELINE.md#work-result) and [§9](EXECUTIVE_BASELINE.md#9-derived-worker-frame), which carry the construction-availability refinement; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 5, 47 and 48.
- Row 6, availability, assessment and acceptance: [ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability), whose `satisfied` establishes availability only, [Disposition](ACTIVATION.md#disposition), which consumes the availability and assessment results and stays separate from both, and [§1 Roles and delegation](ACTIVATION.md#roles-and-delegation), where an assessment is no disposition at a boundary owned elsewhere; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where `decision(holds)` is not acceptance; [TICKETS §3 Close review](TICKETS.md#close-review) and [§7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity), where acceptance stays separate from assessment; [EXECUTIVE_BASELINE §5 Work result](EXECUTIVE_BASELINE.md#work-result) and [§12 step 7](EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints), where no work-result value is an assessment or an acceptance; [DESIGN_MODULE §7 Gate and retrospective work](DESIGN_MODULE.md#gate-and-retrospective-work), where neither a passing matrix nor a produced pack is the verdict; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), where `close` and construction availability answer different predicates. The acceptance boundary and who accepts there are [EVALUATION §5](EVALUATION.md#5-acceptance)'s, as the choice column states.
- Row 7, out of frame or indeterminate: [Imports between members](#imports-between-members), whose result grounds the next row traces; [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), where a question owned by another member returns `out_of_frame` naming its owners, [§3 Construction availability](ACTIVATION.md#construction-availability), whose stop state carries an unexercised capability, as the choice column states, and [Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), which names the halting condition and what would lift it; [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), where an evaluation on unresolved meaning returns `out_of_frame`, or `indeterminate` where the evidence also cannot decide, naming the ground; [EXECUTIVE_BASELINE §5 Technical triage, severity, priority and boundary effect](EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect), where the Reviewer returns `indeterminate` or `out_of_frame` pressure and invents no precision, [Drift locks](EXECUTIVE_BASELINE.md#drift-locks), missing material scope, and [§15](EXECUTIVE_BASELINE.md#15-missing-frame-and-re-entry-application), whose closed result names the missing relation; [ODD §9](ODD.md#9-method-governance-and-audit) and [§11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop), where `valid and worth incorporating` and `reprice` carry the reconfiguration pressure of `out_of_frame`; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where a review returns `out_of_frame` naming the term and its owner; [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where stop `hold` is `indeterminate` naming the evidence that would decide; [DESIGN_MODULE §7 Invariant reconstruction sufficiency](DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018), where an undecided reconstruction names what would decide; [REFERENCE_FRAME §13 Minimal evaluation result](REFERENCE_FRAME.md#minimal-evaluation-result), whose residual field carries what an `out_of_frame` result names.
- Row 8, the result grounds of imports: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), where a question owned by another member is decided from those members at their current digests or returns `out_of_frame`; [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), which refines the import rule between bounded contexts, and the [PRODUCT_DEFINITION family table](PRODUCT_DEFINITION.md#foundation-to-law-binding-a-project-to-the-method), whose sixth row applies the rule to an activation that reports a missing binding before relying on the concept.
- Row 9, the three inputs, gaps, survival and predicates travel: [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), where a required result that is absent, stale or bound to another subject cannot satisfy a dependent conjunction and a `satisfied` for the declared disjunction counts toward no other predicate, and [§3](ACTIVATION.md#3-step-results-and-disposition); [EVALUATION §3](EVALUATION.md#3-independent-assessment), Protocol, where a result bound to another subject satisfies no planned assessment, and [§4](EVALUATION.md#4-review-results), which keeps findings apart from undecided predicates and uncovered coverage; [ASSURANCE §7 The set](ASSURANCE.md#the-set), [§10](ASSURANCE.md#10-testing-evidence-composition), where a missing result stays visible under aggregate green status, and [§13 Claim boundaries](ASSURANCE.md#claim-boundaries), where an unselected claim is uncovered coverage; [AXIOMATIC_CALCULUS §4 AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal), where a refusal keeps its predicate and `refusal(basis)` is a closed result, not a gap; [EXECUTIVE_BASELINE Drift locks](EXECUTIVE_BASELINE.md#drift-locks), coverage-and-return lock, and [§11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction), where a seam without a result is a gap; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where gaps are no outcome of `conjoin` and are recorded beside the reported value, [§6 Result conjunction](REFERENCE_FRAME.md#result-conjunction) and [§8 Coverage ledger](REFERENCE_FRAME.md#coverage-ledger), where an uncovered row is uncovered coverage, never a `falsified` component; [RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015), where an unresolved disposition is a gap in the qualification of the affected claim; [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), where a counterexample one frame finds survives the join, and [§11](SPEC_METHOD.md#11-build-tenant-binding), where tenant conformance is the conjunction of its assessments with the requirements calculus as required coverage; [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse), where the closing condition is the conjunction with the declared obligations as required coverage; [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) and [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where no value counts toward another predicate and a `partial_effect` residual survives every join; [UX §15](UX.md#15-results-of-this-profile) and [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), with the [WORLD_MODEL family table](WORLD_MODEL.md#foundation-to-law), whose row for the Markov-object construct lets a failed run falsify that run's predicate only; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 23 and 24, and [§2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), trial T-04.
- Row 10, stale results: [EXECUTIVE_BASELINE Drift locks](EXECUTIVE_BASELINE.md#drift-locks), where a stale held result before disposition is a gap, never relabelled `invalid_basis`, and [§11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction); [ACTIVATION §1 Applicability](ACTIVATION.md#applicability), for a required result bound to another basis; [REFERENCE_FRAME §8 Coverage ledger](REFERENCE_FRAME.md#coverage-ledger), where a stale coverage tuple returns `invalid_basis` for the audit's own predicate; [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), the `conjoin` row of its population table; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 24.
- Row 11, reported value: [EXECUTIVE_BASELINE §11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction), where a composite claim takes the value its declared conjunction gives, and [§12 step 7](EXECUTIVE_BASELINE.md#7-executive-disposes-and-checkpoints), where the Executive applies the declared conjunction before disposing; [DESIGN_MODULE §7 Gate and retrospective work](DESIGN_MODULE.md#gate-and-retrospective-work), where a combination with a non-satisfied mandatory result or a gap is never `satisfied`; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), where `conjoin` returns the outcome whose cause holds for the reported value, and [§6 Result conjunction](REFERENCE_FRAME.md#result-conjunction); [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), the `conjoin` row; [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse), where a work claim is complete only when every applicable obligation is satisfied; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), for a tenant's conformance; [ASSURANCE §13 Claim boundaries](ASSURANCE.md#claim-boundaries), where a usability claim needs all four results and their explicit conjunction; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 23 and check J55, where the decision owner applies the installed builder's result conjunction.
- Row 12, the declared rule: [EXECUTIVE_BASELINE §11 Refinement and conjunction](EXECUTIVE_BASELINE.md#refinement-and-conjunction), the profile's declared rule, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for specialist frames leaves which non-satisfied value a composite reports to the adopting project's rule; [REFERENCE_FRAME §6 Result conjunction](REFERENCE_FRAME.md#result-conjunction), where a declared decision rule consumes the closed results of several frames; [ASSURANCE §10](ASSURANCE.md#10-testing-evidence-composition), where bound results combine only through declared relations; [TICKETS §7 Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse), whose declared obligations are the mandatory results.
- Row 13, composition of steps: [ACTIVATION §1 Construction relation](ACTIVATION.md#construction-relation), Composition boundaries, where steps compose through compatible preconditions, effects, results and authority and a composition is distinct from a categorical join; [DESIGN_MODULE §5 Atomic functions and higher-order composition](DESIGN_MODULE.md#atomic-functions-and-higher-order-composition), where a design states its composition laws rather than hiding them in controller flow; [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), [ASSURANCE §7 The set](ASSURANCE.md#the-set) and [§10](ASSURANCE.md#10-testing-evidence-composition), where frames used together return closed results to one conjunction instead of composing; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 22, and [§2](CONFORMANCE.md#2-trials-from-the-comparative-baseline), trial T-03. What each step preserves and the law that licenses it are [ACTIVATION §4 Refinement](ACTIVATION.md#refinement)'s, as Composition of results states.
- Row 14, conservation accounting: [DESIGN_MODULE §5 Recursive Prime and root conservation](DESIGN_MODULE.md#recursive-prime-and-root-conservation-up-003), where a contraction records the total mapping from every projection to its accepted atoms; otherwise no separate consumer applies: the record's fields are [AXIOMATIC_CALCULUS §4 AC-013](AXIOMATIC_CALCULUS.md#ac-013-transformation)'s, as the choice column states, and the sections that record a transformation apply AC-013 directly.
- Row 15, reference versus body: [AXIOMATIC_CALCULUS §4 AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), where a projection is a reference that trims no required member; [DESIGN_MODULE §5 Ontology projection](DESIGN_MODULE.md#ontology-projection), where an intentional omission or flattening declares its accepted loss and a failure condition.
- Row 16, latitude: [EVALUATION §6 Conformance of realisations](EVALUATION.md#6-conformance-of-realisations), which applies it where a specification declares its latitude or is repaired; otherwise no separate consumer applies: each latitude is declared in the contract that admits it, whose owner the choice column names.
- Row 17, shared machinery: [DESIGN_MODULE §5 Capability and foundation selection](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), its selection procedure, and [§7 Computational realisation projection](DESIGN_MODULE.md#computational-realisation-projection-up-019), where a projection reveals repeated structure and decides no identity, ownership or authority; [ACTIVATION §1 Intake](ACTIVATION.md#intake), which binds which shared machinery serves the step and under what binding; the [DESIGN_MODULE family table](DESIGN_MODULE.md#foundation-to-law), whose row for recurrence extraction leaves whether one implementation serves several instances to this paragraph.
- Row 18, the formal fragment: [AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position), for category-theoretic status, and [§5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds), where a model claiming functor laws carries the demonstration; [EVALUATION §6](EVALUATION.md#6-conformance-of-realisations), Equivalence ladder, where a categorical equivalence claim meets each applicable item; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), rule 4, where a claim that a binding preserves categorical structure meets it; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 51.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude` at rc.2:

```text
### AC-008 Explicit Latitude

Two values may differ lawfully only through an applicable latitude or
transformation relation. An implementation preference, probabilistic choice,
or human presence is not implicit latitude.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude`:

```text
### AC-008 Explicit latitude

Two values may differ lawfully only through an applicable latitude record
or transformation relation. An implementation preference, a probabilistic
choice or a human presence is not implicit latitude. FOUNDATIONS §4 states
the same rule for any two values; this law is its form over `L` and `T`
(P6, P1; rc.2 #ac-008-explicit-latitude).
```


### Row `AXIOMATIC_CALCULUS.md#ac-009-residual-conservation` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-009-residual-conservation` at rc.2:

```text
### AC-009 Residual Conservation

Every material uncertainty, omission, translation loss, unresolved boundary,
or unproven relation remains in `X` until an authorized disposition creates an
exact successor model. Absence from a projection is not resolution.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-009-residual-conservation`:

```text
### AC-009 Residual conservation

Every material uncertainty, omission, translation loss, unresolved
boundary or unproven relation remains in `X` until an authorised
disposition creates an exact successor model. Absence from a projection is
not resolution (P4b; rc.2 #ac-009-residual-conservation).
```


### Row `AXIOMATIC_CALCULUS.md#ac-010-material-closure` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-010-material-closure` at rc.2:

```text
### AC-010 Material Closure

For model `M`, seed set `Z`, and exact dependency relation family `R`, material
closure is the least fixed point:

```text
closure_R(M, Z) = lfp(lambda Q: Z union required_R(M, Q))
```

The result is defined only when `Z`, `R`, required-edge semantics, basis, and
scope are exact and the fixed point is finite and unique. Failure to establish
those conditions returns a gap or refusal. Least closure means least lawful
record closure under `R`; it does not claim globally minimal prose, bytes,
tokens, cost, or cognitive effort.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-010-material-closure`:

```text
### AC-010 Material closure

For model `M`, seed set `Z` and exact dependency relation family `R`,
material closure is the least fixed point (P0, P2; rc.2
#ac-010-material-closure):

```text
closure_R(M, Z) = lfp(lambda Q: Z union required_R(M, Q))
```

The result is defined only when `Z`, `R`, required-edge semantics, basis
and scope are exact and the fixed point is finite and unique. Failure to
establish those conditions returns a gap or refusal: `gap` where a
condition is unresolved on the basis, otherwise `refusal(basis)`, because
each condition bears on the basis the closure acts on (AC-007). Least
closure means least lawful record closure under `R`; it does not claim
globally minimal prose, bytes, tokens, cost or cognitive effort.
ACTIVATION §2 applies this closure to the construction of a step's context
under an envelope.
```


### Row `AXIOMATIC_CALCULUS.md#ac-011-projection` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-011-projection` at rc.2:

```text
### AC-011 Projection

A projection selects a view of a model without changing selected meaning:

```text
project(M, Z, R) -> (M_Z, Boundary_Z) | gap | refusal
```

`M_Z` contains the material closure of `Z`. `Boundary_Z` records excluded,
external, unresolved, translated, and invalidation-sensitive seams. A
projection is not a new semantic owner and cannot silently trim a required
member to satisfy a carrier or capability budget.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-011-projection`:

```text
### AC-011 Projection

A projection selects a view of a model without changing selected meaning
(P4b, P2; rc.2 #ac-011-projection):

```text
project(M, Z, R) -> (M_Z, Boundary_Z) | gap | refusal
```

`M_Z` contains the material closure of `Z`, so a projection's `gap` or
`refusal` is that of the closure it contains or of the model it acts on:
`gap` or `refusal(basis)` (AC-007). `Boundary_Z` records excluded,
external, unresolved, translated and invalidation-sensitive seams. A
projection is not a new semantic owner. It is a reference, so the rule
that no reference trims a required member to fit a carrier or budget,
stated at [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Reference versus
body, applies to it: here the required members are those of the material
closure of `Z`, and a capability budget is one such budget. ACTIVATION §2
applies the projection to a step's context, and every projected frame of
this corpus is one.
```


### Row `AXIOMATIC_CALCULUS.md#ac-012-overlay` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-012-overlay` at rc.2:

```text
### AC-012 Overlay

An overlay adds explicit records to one or more declared `Population_M`
families of a basis model. It does not mutate the basis. Override,
disambiguation, equivalence, specialization, or translation exists only as a
typed relation with exact authority, direction, scope, basis, preservation,
loss, refusal, and invalidation semantics.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-012-overlay`:

```text
### AC-012 Overlay

An overlay adds explicit records to one or more declared `Population_M`
families of a basis model. It does not mutate the basis. Override,
disambiguation, equivalence, specialisation or translation exists only as
a typed relation with exact authority, direction, scope, basis,
preservation, loss, refusal and invalidation semantics (P3, P6; rc.2
#ac-012-overlay).
```


### Row `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation` at rc.2:

```text
### AC-014 Judgment Separation

A judgment points to an unchanged subject:

```text
Judgment = {
  id,
  kind,
  subject,
  subject_digest,
  context,
  owner,
  scope,
  basis,
  evaluator,
  authority,
  decision,
  evidence,
  provenance,
  decided_at
}
```

Issuing a judgment does not transform, rewrite, reissue, or rename its subject.
Promotion is an explicit relation between the unchanged subject and its
admission or acceptance judgment.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation`:

```text
### AC-014 Judgment separation

A judgment points to an unchanged subject; it is the Judgment of
FOUNDATIONS §2 carried as a model record (P6; rc.2
#ac-014-judgment-separation):

```text
Judgment = {
  id,
  kind,
  subject,
  subject_digest,
  context,
  owner,
  scope,
  basis,
  evaluator,
  authority,
  decision,
  evidence,
  provenance,
  decided_at
}
```

Issuing a judgment does not transform, rewrite, reissue or rename its
subject. Promotion is an explicit relation between the unchanged subject
and its admission or acceptance judgment (P6, P3).
```


### Row `AXIOMATIC_CALCULUS.md#ac-015-functor-classification` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-015-functor-classification` at rc.2:

```text
### AC-015 Functor Classification

Every functor application binds exactly one functor kind and one traversal
identity. Applying any `F_*` kind without bracketed traversal identity `[v]` is
incomplete.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-015-functor-classification`:

```text
### AC-015 Functor classification

Every functor application binds exactly one functor kind and one traversal
identity. Applying any `F_*` kind without the bracketed traversal identity
`[v]` is incomplete (P3; rc.2 #ac-015-functor-classification). Such an
application violates this law, and its outcome is `refusal(constraint)`
under AC-007; this sense of incomplete is not the construction-availability
value `incomplete` of a step
([ACTIVATION §3](ACTIVATION.md#construction-availability)). Purpose and
material relation: an application without its traversal has one core
value, and the shared word does not let it be read as a step's stop (P5).
```


### Row `AXIOMATIC_CALCULUS.md#ac-016-typed-composition` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-016-typed-composition` at rc.2:

```text
### AC-016 Typed Composition

Two traversals compose only when the first result type and judgment satisfy the
second traversal's exact domain and preconditions:

```text
F_K2[w] compose F_K1[v]
```

Composition retains both traversal identities, intermediate results,
judgments, evidence, authority, provenance, and stop states. It cannot flatten
probabilistic proposal, deterministic evaluation, and human decision into one
undifferentiated operation. `a_c` prescribes no universal `F_P -> F_D -> F_H`
sequence; each application owns its lawful topology.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-016-typed-composition`:

```text
### AC-016 Typed composition

Two traversals compose only when the first result type and judgment
satisfy the second traversal's exact domain and preconditions (P4a; rc.2
#ac-016-typed-composition):

```text
F_K2[w] compose F_K1[v]
```

Composition retains both traversal identities, intermediate results,
judgments, evidence, authority, provenance and stop states. It cannot
flatten probabilistic proposal, deterministic evaluation and human
decision into one undifferentiated operation. `a_c` prescribes no
universal `F_P -> F_D -> F_H` sequence; each application owns its lawful
topology (P4a, P4b, P6). FOUNDATIONS §3 P4a consumes this law.
```


### Row `AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity` at rc.2:

```text
### AC-017 Interpretation Fidelity

Every admitted model record maps to exact subject provenance or is explicitly
identified as model-local content under competent authority. Every evaluated
subject declaration has a retained, omitted, residual, inapplicable, or refused
disposition. Interpretation cannot treat absence as immateriality without a
recorded basis and authority.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity`:

```text
### AC-017 Interpretation fidelity

Every admitted model record maps to exact subject provenance or is
explicitly identified as model-local content under competent authority.
Every evaluated subject declaration has a retained, omitted, residual,
inapplicable or refused disposition. Interpretation cannot treat absence
as immateriality without a recorded basis and authority (P1, P4b, P6; rc.2
#ac-017-interpretation-fidelity).
```


### Row `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation` at rc.2:

```text
### AC-018 Structural And Semantic Separation

Structural conformance decides closed syntax, types, identities, references,
bases, and mechanically decidable predicates. Semantic fidelity decides the
meaning and materiality of the interpretation. Structural success is evidence
for semantic review, not a substitute for it.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation`:

```text
### AC-018 Structural and semantic separation

The separation of structural conformance from semantic fidelity, and the
rule that structural success is evidence for semantic review and no
substitute for it, are [EVALUATION §2](EVALUATION.md#2-separation)'s,
which owns them for every review. This law binds them to `a_c`: the
structural conformance of a model covers its closed syntax, types,
identities, references, bases and mechanically decidable predicates, and
the semantic fidelity of an interpretation covers its meaning and
materiality (P1, P6; rc.2
#ac-018-structural-and-semantic-separation).
```


### Row `AXIOMATIC_CALCULUS.md#ac-019-valid-model` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-019-valid-model` at rc.2:

```text
### AC-019 Valid Model

A model `M_b` is a valid model of `a_c` under signature `Sigma`, written:

```text
M_b satisfies a_c[Sigma]
```

only when:

1. `Sigma` and the exact `a_c` basis resolve;
2. every record satisfies AC-001 through AC-009;
3. every claimed closure, projection, overlay, transformation, judgment, and
   composition satisfies its applicable law;
4. interpretation fidelity and residual dispositions bind the exact subject;
5. structural evaluation and semantic acceptance remain distinct and both
   required where claimed; and
6. all evidence, provenance, invalidation, and re-entry coordinates resolve.

A checker may decide the structural subset. No generic checker may claim the
semantic or authority subset unless the model supplies an exact lawful decision
contract for it.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-019-valid-model`:

```text
### AC-019 Valid model

A model `M_b` is a valid model of `a_c` under signature `Sigma`, written
`M_b satisfies a_c[Sigma]`, only when (P6, P1; rc.2 #ac-019-valid-model):

1. `Sigma` and the exact `a_c` basis resolve;
2. every record satisfies AC-001 through AC-009;
3. every claimed closure, projection, overlay, transformation, judgment
   and composition satisfies its applicable law;
4. interpretation fidelity and residual dispositions bind the exact
   subject;
5. structural evaluation and semantic acceptance remain distinct and both
   required where claimed; and
6. all evidence, provenance, invalidation and re-entry coordinates
   resolve.

A checker may decide the structural subset. No generic checker may claim
the semantic or authority subset unless the model supplies an exact lawful
decision contract for it (P6, P1).
```


### Row `AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation` at rc.2:

```text
### AC-020 Layer And Release Separation

`a_c`, `a_c.X`, and `a_c.X.C` have independent content identities, judgments,
supersession relations, and proof obligations:

- `a_c` qualification evaluates internal coherence against its complete
  declared calculus-law set;
- `a_c.X` proves faithful interpretation of exact subject `X`; and
- `a_c.X.C` proves faithful, canonical encoding of the accepted model in
  carrier `C`.

An encoding failure does not change `a_c.X`. An interpretation failure does not
change `a_c`. A downstream success cannot ratify an upstream layer or basis.
None of these layers is automatically an independently released Product. The
external authority that selects and releases one owns that Product status.
```

Successor, `AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation`:

```text
### AC-020 Layer and release separation

`a_c`, `a_c.X` and `a_c.X.C` have independent content identities,
judgments, supersession relations and proof obligations (P3, P6; rc.2
#ac-020-layer-and-release-separation):

- `a_c` qualification evaluates internal coherence against its complete
  declared calculus-law set;
- `a_c.X` proves faithful interpretation of exact subject `X`; and
- `a_c.X.C` proves faithful, canonical encoding of the accepted model in
  carrier `C`.

An encoding failure does not change `a_c.X`. An interpretation failure
does not change `a_c`. A downstream success cannot ratify an upstream
layer or basis. None of these layers is automatically an independently
released Product. The external authority that selects and releases one
owns that Product status. SPEC_METHOD §6 applies this law to release
lineage.
```


### Row `AXIOMATIC_CALCULUS.md#application-boundary` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#application-boundary` at rc.2:

```text
## Application Boundary

This standard defines the generic relations `a_c.X` and `a_c.X.C`. It selects,
constructs, accepts, or releases no concrete interpretation or carrier. A
downstream authority owns its exact subject population, interpretation,
carrier, judgments, and Product or release status. The downstream identity is
never embedded back into the calculus or its publication basis.
```

Successor, `AXIOMATIC_CALCULUS.md#application-boundary`:

```text
### Application boundary

This member defines the generic relations `a_c.X` and `a_c.X.C`. It
selects, constructs, accepts or releases no concrete interpretation or
carrier. A downstream authority owns its exact subject population,
interpretation, carrier, judgments and Product or release status. The
downstream identity is never embedded back into the calculus or its
publication basis (P2, P6; rc.2 #application-boundary).
```


### Row `AXIOMATIC_CALCULUS.md#conformance-obligations` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#conformance-obligations` at rc.2:

```text
## Conformance Obligations

Review and qualification of this fundamental standard cover at least:

1. closed signature, `RecordKind_ac`, population, field, value-domain, and
   reference-domain definitions;
2. well-typed positive and refusal examples for every fundamental law;
3. identity uniqueness and cross-context collision cases;
4. closure, projection, overlay, transformation, and composition laws,
   including exact model identities, population partitions, basis equality,
   and byte-or-typed-equality preservation refusal;
5. strict separation of domain operations, functor kinds, actors, and
   judgments;
6. residual and authority conservation through interpretation and encoding;
7. exact calculus-basis identity reconstruction;
8. direct-coordinate, cross-family reference, wrong-family, duplicate-family,
   and dangling-reference refusal cases for every fundamental record family;
9. derivation-basis and publication-basis reconstruction with cyclic and
   same-carrier counterexamples; and
10. one neutral toy model demonstrating that the calculus has no hidden
    derivation-source record, application-profile, or carrier dependency.

No example, checker, model, or carrier can qualify a law outside the exact
claim it evaluates.
```

Successor, `AXIOMATIC_CALCULUS.md#10-conformance-obligations`:

```text
## 10. Conformance obligations

Review and qualification of this member cover at least (P6; rc.2
#conformance-obligations):

1. closed signature, `RecordKind_ac`, population, field, value-domain and
   reference-domain definitions;
2. well-typed positive and refusal examples for every fundamental law;
3. identity uniqueness and cross-context collision cases;
4. closure, projection, overlay, transformation and composition laws,
   including exact model identities, population partitions, basis
   equality, and byte-or-typed-equality preservation refusal;
5. strict separation of domain operations, functor kinds, actors and
   judgments;
6. residual and authority conservation through interpretation and
   encoding;
7. exact calculus-basis identity reconstruction;
8. direct-coordinate, cross-family reference, wrong-family,
   duplicate-family and dangling-reference refusal cases for every
   fundamental record family;
9. derivation-basis and publication-basis reconstruction with cyclic and
   same-carrier counterexamples; and
10. one neutral toy model demonstrating that the calculus has no hidden
    derivation-source record, application-profile or carrier dependency.

No example, checker, model or carrier can qualify a law outside the exact
claim it evaluates (P6; EVALUATION §1).
```


### Row `AXIOMATIC_CALCULUS.md#constraint` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#constraint` at rc.2:

```text
### Constraint

Every constraint has exactly:

```text
Constraint = {
  id,
  kind,
  applies_to,
  predicate,
  context,
  owner,
  scope,
  basis,
  judgment_kind,
  latitude_ref,
  refusal
}
```

`kind` resolves one declared `ConstraintKind`; `judgment_kind` resolves one
declared `JudgmentKind`. The owning signature defines the predicate language
and how its result is judged. A predicate that is not deterministically
decidable states the required probabilistic or human judgment kind rather than
pretending to be a machine proof.
```

Successor, `AXIOMATIC_CALCULUS.md#constraint`:

```text
### Constraint

Every constraint has exactly (P6, P5; rc.2 #constraint):

```text
Constraint = {
  id,
  kind,
  applies_to,
  predicate,
  context,
  owner,
  scope,
  basis,
  judgment_kind,
  latitude_ref,
  refusal
}
```

`kind` resolves one declared `ConstraintKind`; `judgment_kind` resolves
one declared `JudgmentKind`. The owning signature defines the predicate
language and how its result is judged. A predicate that is not
deterministically decidable states the required probabilistic or human
judgment kind rather than pretending to be a machine proof (P6, P1).
```


### Row `AXIOMATIC_CALCULUS.md#core-signature` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#core-signature` at rc.2:

```text
## Core Signature

An `a_c` signature is:

```text
Sigma = (
  RecordKind,
  Sort,
  RelationKind,
  ConstraintKind,
  ResidualKind,
  FunctorKind,
  JudgmentKind,
  StopKind
)
```

`a_c` fixes this finite core record-kind set:

```text
RecordKind_ac = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment
}
```

Every `a_c` signature imports those identities unchanged. A model-family
signature specializes their fields, value domains, reference domains, and
admissible kinds; it does not remove, rename, shadow, or silently add a core
record family. Another fundamental record family requires an explicit
compatible calculus extension rather than an extra subject sort.

Every signature member is a finite, closed identity set for one model family.
The signature defines:

- the fields and value domains of every sort and record family;
- the reference domain and cardinality of every identity-bearing field;
- the allowed source and target sorts for every relation kind;
- the subject and predicate domains of every constraint kind;
- the subject, uncertainty, consequence, and re-entry domains of every
  residual kind;
- the input, output, evidence, and stop contract of every judgment kind; and
- the functor kinds permitted for each traversal.

Unknown kinds and fields are not extensions. They require a new signature or
an explicit compatible extension relation.

An `a_c` model over exact basis `b` is:

```text
M_b = (b, I, O, E, C, L, X, V, T, J)

Population_M = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object  -> O,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation  -> E,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint      -> C,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude        -> L,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual        -> X,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal       -> V,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation  -> T,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment        -> J
}
```

where:

- `I` is the closed identity universe;
- `O` is the finite set of typed semantic objects;
- `E` is the finite set of typed directed relations;
- `C` is the finite set of constitutional constraints;
- `L` is the finite set of declared latitude records; and
- `X` is the finite set of residual uncertainty records;
- `V` is the finite set of traversal records;
- `T` is the finite set of transformation records; and
- `J` is the finite set of judgment records.

`Population_M` is a total function over `RecordKind_ac`. Every population is
finite, every fundamental record belongs to exactly one population, and record
identities are unique across their disjoint union. Let `Local_M` be that union.
Then `I = Local_M disjoint_union External_M`, where every member of
`External_M` is admitted only through one signature-declared external reference
domain and exact resolution relation. A hidden record, an unpopulated extra
record family, an identity occurring in two populations, or an identity in `I`
with neither one local record nor one lawful external resolution refuses the
model. A population may be empty only when the selected signature does not
require a member of that record kind.

The signature declares a finite reference-domain function:

```text
RefDomain_Sigma(record_kind, field)
  -> (cardinality,
      allowed_local_record_kinds,
      allowed_semantic_object_sorts,
      allowed_external_target_kinds,
      required_basis_relation)
```

Every scalar or collection member that carries an identity reference is
checked through that function. A local reference resolves across the exact
`Population_M` family named by its target record kind; a reference to a
semantic object also satisfies the declared target sort. An external reference
resolves through exactly one declared external target kind and basis relation.
No reference may resolve both locally and externally. Missing field domains,
wrong-family targets, wrong-sort targets, ambiguous targets, and dangling
external identities refuse structural admission.

The tuple is abstract. A carrier may use records, tables, graphs, terms,
clauses, code, or another representation only when its encoding profile proves
that every tuple relation is preserved or explicitly refused.
```

Successor, `AXIOMATIC_CALCULUS.md#2-signature`:

```text
## 2. Signature

An `a_c` signature is (P3, P1; rc.2 #core-signature):

```text
Sigma = (
  RecordKind,
  Sort,
  RelationKind,
  ConstraintKind,
  ResidualKind,
  FunctorKind,
  JudgmentKind,
  StopKind
)
```

`a_c` fixes this finite core record-kind set:

```text
RecordKind_ac = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment
}
```

Every `a_c` signature imports those identities unchanged. A model-family
signature specialises their fields, value domains, reference domains and
admissible kinds; it does not remove, rename, shadow or silently add a
core record family. Another fundamental record family requires an explicit
compatible calculus extension, never an extra subject sort (P3).

Every signature member is a finite, closed identity set for one model
family. The signature defines:

- the fields and value domains of every sort and record family;
- the reference domain and cardinality of every identity-bearing field;
- the allowed source and target sorts for every relation kind;
- the subject and predicate domains of every constraint kind;
- the subject, uncertainty, consequence and re-entry domains of every
  residual kind;
- the input, output, evidence and stop contract of every judgment kind;
  and
- the functor kinds permitted for each traversal.

Unknown kinds and fields are not extensions. They require a new signature
or an explicit compatible extension relation (P1, P6).

An `a_c` model over exact basis `b` is:

```text
M_b = (b, I, O, E, C, L, X, V, T, J)

Population_M = {
  urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object  -> O,
  urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation  -> E,
  urn:stdo:concept:axiomatic-calculus:record-kind:constraint      -> C,
  urn:stdo:concept:axiomatic-calculus:record-kind:latitude        -> L,
  urn:stdo:concept:axiomatic-calculus:record-kind:residual        -> X,
  urn:stdo:concept:axiomatic-calculus:record-kind:traversal       -> V,
  urn:stdo:concept:axiomatic-calculus:record-kind:transformation  -> T,
  urn:stdo:concept:axiomatic-calculus:record-kind:judgment        -> J
}
```

where `I` is the closed identity universe; `O` the finite set of typed
semantic objects; `E` the finite set of typed directed relations; `C` the
finite set of constitutional constraints; `L` the finite set of declared
latitude records; `X` the finite set of residual uncertainty records; `V`
the finite set of traversal records; `T` the finite set of transformation
records; and `J` the finite set of judgment records.

`Population_M` is a total function over `RecordKind_ac`. Every population
is finite, every fundamental record belongs to exactly one population, and
record identities are unique across their disjoint union. Let `Local_M` be
that union. Then `I = Local_M disjoint_union External_M`, where every
member of `External_M` is admitted only through one signature-declared
external reference domain and exact resolution relation. A hidden record,
an unpopulated extra record family, an identity occurring in two
populations, or an identity in `I` with neither one local record nor one
lawful external resolution refuses the model. A population may be empty
only when the selected signature does not require a member of that record
kind (P3, P5).

The signature declares a finite reference-domain function:

```text
RefDomain_Sigma(record_kind, field)
  -> (cardinality,
      allowed_local_record_kinds,
      allowed_semantic_object_sorts,
      allowed_external_target_kinds,
      required_basis_relation)
```

Every scalar or collection member that carries an identity reference is
checked through that function. A local reference resolves across the exact
`Population_M` family named by its target record kind; a reference to a
semantic object also satisfies the declared target sort. An external
reference resolves through exactly one declared external target kind and
basis relation. No reference may resolve both locally and externally.
Missing field domains, wrong-family targets, wrong-sort targets, ambiguous
targets and dangling external identities refuse structural admission (P3,
P6).

The tuple is abstract. A carrier may use records, tables, terms, clauses,
code or any other representation only when its encoding profile proves
that every tuple relation is preserved or explicitly refused (P1, P4b).
```


### Row `AXIOMATIC_CALCULUS.md#derivation-provenance` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#derivation-provenance` at rc.2:

```text
## Derivation Provenance

The calculus contracts recurring principles already established by STDO:

- scoped identity and authority conservation from
  [`IDENTITY_METHOD.md#core-law`](IDENTITY_METHOD.md#core-law) and
  [`IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004`](IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004);
- exact bounded-context meaning and explicit cross-context relations from
  [`SPEC_METHOD.md#bounded-context-semantic-resolution`](SPEC_METHOD.md#bounded-context-semantic-resolution);
- probabilistic construction as a bounded evaluation class from
  [`REFERENCE_FRAME_METHOD.md#position`](REFERENCE_FRAME_METHOD.md#position)
  and
  [`REFERENCE_FRAME_METHOD.md#evaluation`](REFERENCE_FRAME_METHOD.md#evaluation);
- delegated probabilistic construction, exact candidate production, and
  construction-versus-assessment separation from
  [`SPEC_METHOD.md#agentic-construction-execution-stdo-up-020`](SPEC_METHOD.md#agentic-construction-execution-stdo-up-020);
- governed ambiguity, bounded probabilistic processing, explicit human
  adjudication, and hard-stop separation from
  [`SPEC_METHOD.md#ambiguity-governance-rule`](SPEC_METHOD.md#ambiguity-governance-rule);
- exact-basis evaluation, evidence-and-verdict separation, authority
  conservation, and closed results from
  [`REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates`](REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates),
  [`REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation`](REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
  [`REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation`](REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation),
  and
  [`REFERENCE_FRAME_METHOD.md#rf-012-closed-results`](REFERENCE_FRAME_METHOD.md#rf-012-closed-results);
- constitutional derivation and re-entry from
  [`SPEC_METHOD.md#constitutional-chain`](SPEC_METHOD.md#constitutional-chain);
- finite material closure, projection, authority conservation, residual
  uncertainty, and capability fit from
  [`REFERENCE_FRAME_METHOD.md#reference-frame-laws`](REFERENCE_FRAME_METHOD.md#reference-frame-laws); and
- singular released authority from
  [`SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001`](SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001).

These references establish provenance. The definitions and laws below are the
sole normative authority for the meaning of `a_c` within the selected complete
STDO cut. A consumer does not need an implicit STDO representation, GTL
carrier, or downstream implementation to interpret the calculus.

This standard introduces the generic calculus identities `F_D`, `F_P`, and
`F_H`. It does not import those identities from an equal-spelled graph,
runtime, ODD, or application shorthand. The predecessor clauses establish the
substrate-neutral evaluation, probabilistic-processing, human-adjudication,
authority, evidence, and refusal principles from which the generic definitions
below are derived. Nominal equality with a predecessor or downstream shorthand
creates no concept-identity, import, or equivalence relation.

The relative links above identify derivation clause families in this authoring
source. Issuance of an exact `AxiomaticCalculusBasis` resolves and records their
absolute predecessor-cut semantic addresses under
`derivation_basis.release_uri`. The mutable authoring links are not themselves
the digest-bound derivation references.

The derivation direction is one-way. A model of STDO under `a_c`, an encoded
carrier, a proof tool, or a successful application cannot amend the source
principles or this calculus.
```

Successor, `AXIOMATIC_CALCULUS.md#derivation-provenance`:

```text
### Derivation provenance

The calculus contracts recurring commitments the method already
establishes. In this corpus each is law in a member of this candidate, so
applying the calculus needs no predecessor clause; the rc.2 clause family
from which this edition derived each one is listed beside it as the
derivation account that the identity record of §8 binds (P6; rc.2
#derivation-provenance):

- scoped identity and authority conservation: FOUNDATIONS §2 (Object,
  Authority) under P3 and P6; derived from rc.2 IDENTITY_METHOD
  #core-law and #authority-identity-and-conservation-stdo-up-004;
- exact bounded-context meaning and explicit cross-context relations:
  FOUNDATIONS §2 (Interpretation, Context) under P1; derived from rc.2
  SPEC_METHOD #bounded-context-semantic-resolution;
- probabilistic construction as a bounded evaluation class: P0 with the
  work boundary of FOUNDATIONS §2 and ACTIVATION §1; derived from rc.2
  REFERENCE_FRAME_METHOD #position and #evaluation;
- delegated probabilistic construction, exact candidate production and
  construction-versus-assessment separation: ACTIVATION §1 (Output and
  roles) and EVALUATION §3; derived from rc.2 SPEC_METHOD
  #agentic-construction-execution-stdo-up-020;
- governed ambiguity, bounded probabilistic processing, explicit human
  adjudication and hard-stop separation: ACTIVATION §4; derived from rc.2
  SPEC_METHOD #ambiguity-governance-rule;
- exact-basis evaluation, evidence-and-verdict separation, authority
  conservation and closed results: REFERENCE_FRAME RF-005, RF-006 and
  RF-007 and the core result algebra of FOUNDATIONS §4 Results, which
  restates RF-012; derived from the rc.2 REFERENCE_FRAME_METHOD laws of
  the same numbers;
- constitutional derivation and re-entry: SPEC_METHOD §1 and §4; derived
  from rc.2 SPEC_METHOD #constitutional-chain;
- finite material closure, projection, authority conservation, residual
  uncertainty and capability fit: REFERENCE_FRAME §3 with AC-010 and
  AC-011 below; derived from rc.2 REFERENCE_FRAME_METHOD
  #reference-frame-laws; and
- singular released authority: SPEC_METHOD §6, with the one-surface rule
  received by the tier-2 PRODUCT_DEFINITION member at its activation;
  derived from rc.2 SPEC_METHOD
  #one-constitutional-surface-and-version-boundary-stdo-surface-001.

These references establish provenance. The definitions and laws of this
member are the sole normative authority for the meaning of `a_c` within
the selected complete cut. A consumer needs no implicit representation of
the method, no particular carrier and no downstream implementation to
interpret the calculus (P1, P6).

This member introduces the generic calculus identities `F_D`, `F_P` and
`F_H` (§5). It does not import them from an equal-spelled shorthand owned
by a runtime, a profile, a realisation or an application. The predecessor
clauses establish the substrate-neutral evaluation,
probabilistic-processing, human-adjudication, authority, evidence and
refusal principles from which the generic definitions are derived. Nominal
equality with a predecessor or downstream shorthand creates no
concept-identity, import or equivalence relation (P3, P1).

The routes above identify derivation clause families in this authoring
source. Issuance of an exact `AxiomaticCalculusBasis` (§8) resolves and
records their absolute predecessor-cut semantic addresses under
`derivation_basis.principle_refs`. The mutable authoring routes are not
themselves the digest-bound derivation references (P3).

The derivation direction is one-way. A model of the method under `a_c`,
an encoded carrier, a proof tool or a successful application cannot amend
the source principles or this calculus (P6).
```


### Row `AXIOMATIC_CALCULUS.md#exact-calculus-identity` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#exact-calculus-identity` at rc.2:

```text
## Exact Calculus Identity

The stable concept identity does not identify one immutable calculus edition.
An exact released calculus basis is an external record created after the
publication bytes exist. It keeps the predecessor authority from which the
edition was derived distinct from the successor carrier that publishes it:

```text
AxiomaticCalculusBasis = {
  kind: "stdo.axiomatic-calculus-basis",
  schema_version: 1,
  concept_identity: "urn:stdo:concept:axiomatic-calculus:a-c",
  derivation_basis: {
    release_uri: absolute immutable predecessor release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    principle_refs: non-empty absolute semantic-address URI[]
  },
  publication_basis: {
    release_uri: absolute immutable successor release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    member_uri: absolute URI for this member in that release,
    member_sha256: "sha256:" + 64 lowercase hexadecimal characters
  }
}
```

The record uses RFC 8785 JSON Canonicalization Scheme bytes. Duplicate object
names are rejected before canonicalization. `derivation_basis.principle_refs`
is duplicate-free and sorted by ascending unsigned UTF-16 code units. Its
identity is:

```text
urn:stdo:axiomatic-calculus-basis:sha256:
  + sha256(JCS(AxiomaticCalculusBasis))
```

`derivation_basis` binds one exact accepted predecessor cut and the complete
finite set of clauses from which this edition was derived. Every principle
reference is one clause identified under `Derivation Provenance`, resolves
inside that predecessor cut, and is retained without a hard-coded member count.
The set is recomputed when the derivation account changes. It cannot depend on
the publication carrier or calculus-basis identity being created.

`publication_basis` binds the distinct immutable successor carrier and this
standard's exact bytes. Its member URI resolves inside its release URI. The
record is external because this standard cannot contain its own final byte
digest. Same-release references that cite this calculus are publication or
cross-context relations, not derivation provenance.

An interpreted-subject identity binds at least:

```text
id(a_c.X) binds
  exact id(a_c)
  + exact subject basis id(X)
  + exact interpretation contract
  + selected model content identity
  + semantic-selection ledger identity and digest
```

An external semantic-acceptance judgment points to that unchanged identity and
content digest. It is not embedded in `id(a_c.X)`. The accepted interpretation
is the pair `(a_c.X, J_X)` where `J_X` is the applicable accepted judgment. This
one-way relation prevents the acceptance record and its subject from requiring
each other's final identity.

An encoded-carrier identity binds at least:

```text
id(a_c.X.C) binds
  exact id(a_c.X)
  + exact carrier Product or cut
  + exact encoding profile
  + canonical carrier content identity
```

The accepted semantic judgment remains external to both content identities.
Encoding mechanically verifies its subject identity and digest against the
unchanged interpreted model and retains it in the evidence relation. The
carrier-admission judgment points to the unchanged carrier identity and digest
and is not embedded in `id(a_c.X.C)`. The admitted encoding relation is the
triple `(a_c.X.C, J_X, D_C)`. Any Product acceptance and release likewise point
to the unchanged content-first layer identity rather than entering it.

The owning Product defines the canonical record grammar and issuance authority
for those downstream identities. It cannot omit the upstream identities or
replace them with mutable locators.
```

Successor, `AXIOMATIC_CALCULUS.md#8-calculus-identity`:

```text
## 8. Calculus identity

The stable concept identity does not identify one immutable calculus
edition. An exact released calculus basis is an external record created
after the publication bytes exist. It keeps the predecessor authority from
which the edition was derived distinct from the successor carrier that
publishes it (P3, P6; rc.2 #exact-calculus-identity):

```text
AxiomaticCalculusBasis = {
  kind: "stdo.axiomatic-calculus-basis",
  schema_version: 1,
  concept_identity: "urn:stdo:concept:axiomatic-calculus:a-c",
  derivation_basis: {
    release_uri: absolute immutable predecessor release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    principle_refs: non-empty absolute semantic-address URI[]
  },
  publication_basis: {
    release_uri: absolute immutable successor release URI,
    manifest_sha256: "sha256:" + 64 lowercase hexadecimal characters,
    member_uri: absolute URI for this member in that release,
    member_sha256: "sha256:" + 64 lowercase hexadecimal characters
  }
}
```

The record uses RFC 8785 JSON Canonicalization Scheme bytes. Duplicate
object names are rejected before canonicalisation.
`derivation_basis.principle_refs` is duplicate-free and sorted by
ascending unsigned UTF-16 code units. The record's identity is:

```text
urn:stdo:axiomatic-calculus-basis:sha256:
  + sha256(JCS(AxiomaticCalculusBasis))
```

`derivation_basis` binds one exact accepted predecessor cut and the
complete finite set of clauses from which this edition was derived. Every
principle reference is one clause identified under §1 Derivation
provenance, resolves inside that predecessor cut, and is retained without
a hard-coded member count. The set is recomputed when the derivation
account changes. It cannot depend on the publication carrier or on the
calculus-basis identity being created (P3, P6).

`publication_basis` binds the distinct immutable successor carrier and
this member's exact bytes. Its member URI resolves inside its release URI.
The record is external because this member cannot contain its own final
byte digest. Same-release references that cite this calculus are
publication or cross-context relations, not derivation provenance (P3).

An interpreted-subject identity binds at least:

```text
id(a_c.X) binds
  exact id(a_c)
  + exact subject basis id(X)
  + exact interpretation contract
  + selected model content identity
  + semantic-selection ledger identity and digest
```

An external semantic-acceptance judgment points to that unchanged identity
and content digest. It is not embedded in `id(a_c.X)`. The accepted
interpretation is the pair `(a_c.X, J_X)` where `J_X` is the applicable
accepted judgment. This one-way relation prevents the acceptance record
and its subject from requiring each other's final identity (P3, P6).

An encoded-carrier identity binds at least:

```text
id(a_c.X.C) binds
  exact id(a_c.X)
  + exact carrier Product or cut
  + exact encoding profile
  + canonical carrier content identity
```

The accepted semantic judgment remains external to both content
identities. Encoding mechanically verifies its subject identity and digest
against the unchanged interpreted model and retains it in the evidence
relation. The carrier-admission judgment points to the unchanged carrier
identity and digest and is not embedded in `id(a_c.X.C)`. The admitted
encoding relation is the triple `(a_c.X.C, J_X, D_C)`. Any Product
acceptance and release likewise point to the unchanged content-first layer
identity rather than entering it (P3, P6).

The owning Product defines the canonical record grammar and issuance
authority for those downstream identities. It cannot omit the upstream
identities or replace them with mutable locators (P3).

Binding of this edition. The identity of this corpus's calculus is bound
at its own release and nowhere earlier: the `AxiomaticCalculusBasis` for
this member is issued under the tier-2
[RELEASE](RELEASE.md) member and under AC-020, after the release bytes exist, with
`publication_basis` naming that release and this member's bytes in it and
`derivation_basis` naming the predecessor cut and the derivation account
of §1. This authoring text is a source project surface. It is neither the
identity-bearing release of this edition nor the identity-bearing source
of any released calculus edition: a dependency on a released edition
binds that edition's identity under this section, with its release,
manifest digest and member digest, and never an authoring text (P3, P6).
The predecessor edition's coordinates are recorded here as provenance of
this edition's derivation, not as this edition's identity: cut
`stdo://releases/v2.5.1-rc.2/`, manifest SHA-256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`,
member `AXIOMATIC_CALCULUS.md` SHA-256
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`,
concept identity unchanged (P3, P6).
```


### Row `AXIOMATIC_CALCULUS.md#exclusions` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#exclusions` at rc.2:

```text
## Exclusions

`a_c` is not:

- a representation or compression of its derivation source;
- a selected semantic model of any subject;
- a carrier profile or carrier instance;
- an executable language, interpreter, compiler implementation, or runtime;
- a deterministic semantic assessor or theorem prover;
- a required graph storage topology;
- a world-model ontology;
- an authority registry; or
- a claim that all governed systems share one vocabulary or relation set.
```

Successor, `AXIOMATIC_CALCULUS.md#exclusions`:

```text
### Exclusions

`a_c` is not (P2; rc.2 #exclusions):

- a representation or compression of its derivation source;
- a selected semantic model of any subject;
- a carrier profile or carrier instance;
- an executable language, interpreter, compiler implementation or
  runtime;
- a deterministic semantic assessor or theorem prover;
- a required storage topology of any shape;
- an ontology of any domain;
- an authority registry; or
- a claim that all governed systems share one vocabulary or relation set.
```


### Row `AXIOMATIC_CALCULUS.md#external-imports-and-specializations` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#external-imports-and-specializations` at rc.2:

```text
## External Imports And Specializations

An application may declare a typed import, translation, or specialization of
an `a_c` concept under that application's own exact authority, context, basis,
scope, preservation, loss, refusal, and invalidation law. Such a relation is
external to the calculus. It neither changes `a_c` nor enters this standard by
being useful to an application.
```

Successor, `AXIOMATIC_CALCULUS.md#external-imports-and-specialisations`:

```text
### External imports and specialisations

An application may declare a typed import, translation or specialisation
of an `a_c` concept under that application's own exact authority, context,
basis, scope, preservation, loss, refusal and invalidation law. Such a
relation is external to the calculus. It neither changes `a_c` nor enters
this member by being useful to an application (P6, P2; rc.2
#external-imports-and-specializations). PROFILES §1 states the same
rule from the profile's side as the declared-binding rule.
```


### Row `AXIOMATIC_CALCULUS.md#interpretation-and-models` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#interpretation-and-models` at rc.2:

```text
## Interpretation And Models

An interpretation applies `a_c` to an exact subject:

```text
Interpret_a_c(subject_basis, signature, interpretation_contract)
  -> M_subject* | hold | gap | refusal
```

The trailing `*` marks a proposed model that has not received the applicable
semantic acceptance judgment.

The interpretation contract declares:

- exact `a_c` basis;
- exact subject identity, inventory, and bytes or semantic addresses;
- selected signature and any compatible extension relation;
- mapping from subject declarations to every applicable model record population,
  including objects, relations, constraints, latitude, residuals, traversals,
  transformations, and judgments;
- interpreter identity, capability, provenance, and stop states;
- structural evaluation contract;
- semantic selection and acceptance authority; and
- source re-entry and invalidation rules.

The proposed model `M_subject*` does not become accepted through construction.
Structural evaluation can prove closed shape, reference typing, identity
derivation, and basis coherence. It cannot prove that probabilistic semantic
selection retained every material subject meaning. Semantic acceptance remains
a separately recorded authority judgment.

### AC-017 Interpretation Fidelity

Every admitted model record maps to exact subject provenance or is explicitly
identified as model-local content under competent authority. Every evaluated
subject declaration has a retained, omitted, residual, inapplicable, or refused
disposition. Interpretation cannot treat absence as immateriality without a
recorded basis and authority.

### AC-018 Structural And Semantic Separation

Structural conformance decides closed syntax, types, identities, references,
bases, and mechanically decidable predicates. Semantic fidelity decides the
meaning and materiality of the interpretation. Structural success is evidence
for semantic review, not a substitute for it.

### AC-019 Valid Model

A model `M_b` is a valid model of `a_c` under signature `Sigma`, written:

```text
M_b satisfies a_c[Sigma]
```

only when:

1. `Sigma` and the exact `a_c` basis resolve;
2. every record satisfies AC-001 through AC-009;
3. every claimed closure, projection, overlay, transformation, judgment, and
   composition satisfies its applicable law;
4. interpretation fidelity and residual dispositions bind the exact subject;
5. structural evaluation and semantic acceptance remain distinct and both
   required where claimed; and
6. all evidence, provenance, invalidation, and re-entry coordinates resolve.

A checker may decide the structural subset. No generic checker may claim the
semantic or authority subset unless the model supplies an exact lawful decision
contract for it.
```

Successor, `AXIOMATIC_CALCULUS.md#6-interpretation-and-models`:

```text
## 6. Interpretation and models

An interpretation applies `a_c` to an exact subject (P1; rc.2
#interpretation-and-models):

```text
Interpret_a_c(subject_basis, signature, interpretation_contract)
  -> M_subject* | hold | gap | refusal
```

The stops `hold`, `gap` and `refusal` take their core values under AC-007
by their causes. The trailing `*` marks a proposed model that has not
received the
applicable semantic acceptance judgment. The interpretation contract is
the Interpretation of FOUNDATIONS §2 made exact for one subject and one
signature. It declares:

- the exact `a_c` basis;
- the exact subject identity, inventory, and bytes or semantic addresses;
- the selected signature and any compatible extension relation;
- the mapping from subject declarations to every applicable model record
  population, including objects, relations, constraints, latitude,
  residuals, traversals, transformations and judgments;
- the interpreter identity, capability, provenance and stop states;
- the structural evaluation contract;
- the semantic selection and acceptance authority; and
- the source re-entry and invalidation rules.

The proposed model `M_subject*` does not become accepted through
construction. Structural evaluation can prove closed shape, reference
typing, identity derivation and basis coherence. It cannot prove that
probabilistic semantic selection retained every material subject meaning.
Semantic acceptance remains a separately recorded authority judgment (P6,
P1).

### AC-017 Interpretation fidelity

Every admitted model record maps to exact subject provenance or is
explicitly identified as model-local content under competent authority.
Every evaluated subject declaration has a retained, omitted, residual,
inapplicable or refused disposition. Interpretation cannot treat absence
as immateriality without a recorded basis and authority (P1, P4b, P6; rc.2
#ac-017-interpretation-fidelity).

### AC-018 Structural and semantic separation

The separation of structural conformance from semantic fidelity, and the
rule that structural success is evidence for semantic review and no
substitute for it, are [EVALUATION §2](EVALUATION.md#2-separation)'s,
which owns them for every review. This law binds them to `a_c`: the
structural conformance of a model covers its closed syntax, types,
identities, references, bases and mechanically decidable predicates, and
the semantic fidelity of an interpretation covers its meaning and
materiality (P1, P6; rc.2
#ac-018-structural-and-semantic-separation).

### AC-019 Valid model

A model `M_b` is a valid model of `a_c` under signature `Sigma`, written
`M_b satisfies a_c[Sigma]`, only when (P6, P1; rc.2 #ac-019-valid-model):

1. `Sigma` and the exact `a_c` basis resolve;
2. every record satisfies AC-001 through AC-009;
3. every claimed closure, projection, overlay, transformation, judgment
   and composition satisfies its applicable law;
4. interpretation fidelity and residual dispositions bind the exact
   subject;
5. structural evaluation and semantic acceptance remain distinct and both
   required where claimed; and
6. all evidence, provenance, invalidation and re-entry coordinates
   resolve.

A checker may decide the structural subset. No generic checker may claim
the semantic or authority subset unless the model supplies an exact lawful
decision contract for it (P6, P1).
```


### Row `AXIOMATIC_CALCULUS.md#latitude` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#latitude` at rc.2:

```text
### Latitude

Latitude is an explicit permission set inside a constraint boundary:

```text
Latitude = {
  id,
  applies_to,
  allowed_variation,
  forbidden_variation,
  context,
  owner,
  scope,
  basis,
  invalidation
}
```

Silence is not latitude. Latitude grants no authority beyond its owner, scope,
basis, and invalidation law.
```

Successor, `AXIOMATIC_CALCULUS.md#latitude`:

```text
### Latitude

Latitude is an explicit permission set inside a constraint boundary (P6;
rc.2 #latitude):

```text
Latitude = {
  id,
  applies_to,
  allowed_variation,
  forbidden_variation,
  context,
  owner,
  scope,
  basis,
  invalidation
}
```

Silence is not latitude. Latitude grants no authority beyond its owner,
scope, basis and invalidation law, an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority (P6).
```


### Row `AXIOMATIC_CALCULUS.md#position` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#position` at rc.2:

```text
## Position

The **STDO Axiomatic Calculus for Governed Symbolic Systems**, written `a_c`,
is STDO's domain-specific, carrier-neutral constitutional calculus for
representing and relating governed symbolic systems.

Its stable concept identity is:

```text
urn:stdo:concept:axiomatic-calculus:a-c
```

This standard owns that concept in bounded context:

```text
urn:stdo:bounded-context:axiomatic-calculus
```

`a_c` is a separately identifiable calculus derived from STDO principles. It
defines sorts, typed objects, relations, constraints, latitude, residual
uncertainty, traversals, functor kinds, judgments, closure, projections,
transformations, models, and validity laws. Those definitions do not depend on
a derivation-source record layout, a selected subject interpretation, a
particular carrier, a model provider, a runtime, or a repository topology.

`a_c` makes no claim of universal applicability, logical completeness,
consistency, decidability, soundness, or category-theoretic status except where
an exact, separately identified proof establishes that claim for a declared
fragment, model, or relation.

STDO principles are the derivation provenance of the calculus. Application of
the calculus to any exact subject is a separately owned downstream relation.
Those relations are distinct:

```text
exact predecessor STDO principles ──derive──> a_c
a_c + exact subject X              ──interpret──> a_c.X
a_c.X + exact accepted semantic judgment J_X
      + exact carrier C            ──encode─────> a_c.X.C
```

The calculus, an interpreted model, and an encoded carrier are distinct
governed layers with separate content identities and proof boundaries. A layer
becomes a released Product only through separately authorized Product
acceptance and release. Neither interpretation nor encoding can redefine the
calculus.
```

Successor, `AXIOMATIC_CALCULUS.md#1-position`:

```text
## 1. Position

The STDO Axiomatic Calculus for Governed Symbolic Systems, written `a_c`,
is this method's domain-specific, carrier-neutral constitutional calculus
for representing and relating governed symbolic systems. Its stable
concept identity is `urn:stdo:concept:axiomatic-calculus:a-c`. This member
owns that concept in the bounded context
`urn:stdo:bounded-context:axiomatic-calculus`. Both identifiers are
declared identities and do not change with the carrier or the directory
that publishes them (P3; rc.2 #position).

`a_c` is a separately identifiable calculus derived from the method's
principles. It defines sorts, typed objects, relations, constraints,
latitude, residual uncertainty, traversals, functor kinds, judgments,
closure, projections, transformations, models and validity laws. Those
definitions depend on no derivation-source record layout, no selected
subject interpretation, no particular carrier, no model provider, no
runtime and no repository topology (P1, P2).

`a_c` claims no universal applicability, logical completeness,
consistency, decidability, soundness or category-theoretic status except
where an exact, separately identified proof establishes that claim for a
declared fragment, model or relation; for category-theoretic status that
proof is the demonstration of
[FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Formal fragment (P6).

The principles are the derivation provenance of the calculus. Application
of the calculus to any exact subject is a separately owned downstream
relation. The relations are distinct (P3, P6):

```text
exact predecessor principles                 -> derive    -> a_c
a_c + exact subject X                        -> interpret -> a_c.X
a_c.X + exact accepted semantic judgment J_X
      + exact carrier C                      -> encode    -> a_c.X.C
```

The calculus, an interpreted model and an encoded carrier are distinct
governed layers with separate content identities and proof boundaries
(§7). A layer becomes a released Product only through separately
authorised Product acceptance and release. Neither interpretation nor
encoding can redefine the calculus (P6).

### Derivation provenance

The calculus contracts recurring commitments the method already
establishes. In this corpus each is law in a member of this candidate, so
applying the calculus needs no predecessor clause; the rc.2 clause family
from which this edition derived each one is listed beside it as the
derivation account that the identity record of §8 binds (P6; rc.2
#derivation-provenance):

- scoped identity and authority conservation: FOUNDATIONS §2 (Object,
  Authority) under P3 and P6; derived from rc.2 IDENTITY_METHOD
  #core-law and #authority-identity-and-conservation-stdo-up-004;
- exact bounded-context meaning and explicit cross-context relations:
  FOUNDATIONS §2 (Interpretation, Context) under P1; derived from rc.2
  SPEC_METHOD #bounded-context-semantic-resolution;
- probabilistic construction as a bounded evaluation class: P0 with the
  work boundary of FOUNDATIONS §2 and ACTIVATION §1; derived from rc.2
  REFERENCE_FRAME_METHOD #position and #evaluation;
- delegated probabilistic construction, exact candidate production and
  construction-versus-assessment separation: ACTIVATION §1 (Output and
  roles) and EVALUATION §3; derived from rc.2 SPEC_METHOD
  #agentic-construction-execution-stdo-up-020;
- governed ambiguity, bounded probabilistic processing, explicit human
  adjudication and hard-stop separation: ACTIVATION §4; derived from rc.2
  SPEC_METHOD #ambiguity-governance-rule;
- exact-basis evaluation, evidence-and-verdict separation, authority
  conservation and closed results: REFERENCE_FRAME RF-005, RF-006 and
  RF-007 and the core result algebra of FOUNDATIONS §4 Results, which
  restates RF-012; derived from the rc.2 REFERENCE_FRAME_METHOD laws of
  the same numbers;
- constitutional derivation and re-entry: SPEC_METHOD §1 and §4; derived
  from rc.2 SPEC_METHOD #constitutional-chain;
- finite material closure, projection, authority conservation, residual
  uncertainty and capability fit: REFERENCE_FRAME §3 with AC-010 and
  AC-011 below; derived from rc.2 REFERENCE_FRAME_METHOD
  #reference-frame-laws; and
- singular released authority: SPEC_METHOD §6, with the one-surface rule
  received by the tier-2 PRODUCT_DEFINITION member at its activation;
  derived from rc.2 SPEC_METHOD
  #one-constitutional-surface-and-version-boundary-stdo-surface-001.

These references establish provenance. The definitions and laws of this
member are the sole normative authority for the meaning of `a_c` within
the selected complete cut. A consumer needs no implicit representation of
the method, no particular carrier and no downstream implementation to
interpret the calculus (P1, P6).

This member introduces the generic calculus identities `F_D`, `F_P` and
`F_H` (§5). It does not import them from an equal-spelled shorthand owned
by a runtime, a profile, a realisation or an application. The predecessor
clauses establish the substrate-neutral evaluation,
probabilistic-processing, human-adjudication, authority, evidence and
refusal principles from which the generic definitions are derived. Nominal
equality with a predecessor or downstream shorthand creates no
concept-identity, import or equivalence relation (P3, P1).

The routes above identify derivation clause families in this authoring
source. Issuance of an exact `AxiomaticCalculusBasis` (§8) resolves and
records their absolute predecessor-cut semantic addresses under
`derivation_basis.principle_refs`. The mutable authoring routes are not
themselves the digest-bound derivation references (P3).

The derivation direction is one-way. A model of the method under `a_c`,
an encoded carrier, a proof tool or a successful application cannot amend
the source principles or this calculus (P6).

### Scope

`a_c` governs the form of a symbolic axiomatic model (P2; rc.2 #scope). It
answers:

- what identities and typed objects exist;
- how relations bind exact endpoints;
- how constraints, latitude and residuals remain explicit;
- how traversals and judgments are typed;
- how material closure, projection, overlay and transformation behave;
- what a model must preserve from its subject; and
- which claims are structural, semantic or authority decisions.

`a_c` does not choose the subject vocabulary, decide which source
declarations are material, supply semantic acceptance, select a carrier,
execute a model or prove that one interpretation is uniquely correct (P2,
P6).

### Foundation to law

This member is material family F9, the `a_c` calculus. The table below
shows which of its rules follow from which premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. Instance premises,
which the commitments do not supply:

- (i) a governed symbolic system is represented by a finite model whose
  records stand for its objects, relations, constraints, residuals,
  traversals, transformations and judgments;
- (ii) a model is interpreted from an exact subject and may be encoded in
  a carrier, and subject, model and carrier are separately identified;
- (iii) some predicates over a model are decided mechanically, and others
  need bounded probabilistic construction or explicit human adjudication.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P1 (independent), P6 (independent); (i) | By P1 a model is a representation of its subject, by P6 encoding and interpreting are separate authorities, and by (i) a governed system is represented by a finite model, so the calculus is derived one way from the method's principles and is separate from its application: interpreting a subject and encoding a model are distinct relations, and no model, carrier, proof tool or successful application amends the calculus or the principles | [§1](#1-position), [Derivation provenance](#derivation-provenance) | the concept identity, its bounded context and the name `a_c`: this member | 6, 10 |
| P2 (independent), P6 (independent) | By P2 the calculus serves only the form a model needs, and by P6 a status needs its own proof, so the calculus governs the form of a symbolic model and claims no status that a separately identified proof has not established; it chooses no subject vocabulary or materiality, supplies no semantic acceptance, selects no carrier and executes nothing | [§1](#1-position), the claims it does not make; [Scope](#scope); [Exclusions](#exclusions) | none | 10 |
| P3 (independent), P5 (derived from P0 and P6); (i) | By P3 every element binds one identity and basis, by P5 an unclosed population would leave results undecided, and by (i) the model is finite, so every model belongs to one closed, finite signature; every record occurs once in one population of eight fixed record families, every identity resolves once, locally or through one declared external relation, and an unknown, hidden, duplicated or dangling element refuses | [§2](#2-signature), [§3](#3-typed-records), [AC-001](#ac-001-closed-signature), [AC-003](#ac-003-reference-closure) | the eight core record kinds and the fields of each record: this member; a model family's sorts, value domains, reference domains and admissible kinds: the owning signature | 3, 10 |
| P3 (independent), P4a (independent) | By P3 identity is declared and scoped, and by P4a relations compose only by the types they declare, so identity is scoped, so equal spelling, payload, position or carrier establishes none; a relation is lawful only between the sorts its kind admits, with its required qualifiers, and its direction is material unless declared symmetric | [AC-002](#ac-002-scoped-identity), [AC-004](#ac-004-relation-typing) | each relation kind's sorts, qualifiers and any declared symmetry: the owning signature | 2, 3, 10 |
| P6 (independent), P4b (derived from P0 and P2), P3 (independent) | By P6 authority is not transferred by handling a record, by P3 every record binds its basis, and by P4b recorded facts persist, so copying, interpreting, encoding, evaluating or transporting a record transfers no authority, and every record, model and result binds an exact basis, mixed bases only under an owned composite-basis relation | [AC-005](#ac-005-authority-conservation), [AC-006](#ac-006-basis-coherence) | each composite-basis relation: the owner it names | 9, 10 |
| P5 (derived from P0 and P6), P6 (independent) | By P5 a value decides only what its evidence establishes, and by P6 a judgment is separate from its acceptance, so a constraint's judgment and every outcome of an operation of this member read as exactly one core value for a named predicate; no failed, missing or undecided result and no stop becomes success; a refusal's cause is part of its value, a demonstrated violation it names mapping to falsified and a condition of the basis the operation acts on to invalid_basis | [AC-007](#ac-007-constraint-and-refusal); [§5](#5-traversals-and-functor-kinds), the stop algebra | the cause of a refusal that names both a demonstrated violation and a condition of the basis, `refusal(constraint)`, with the basis condition reported beside it as its own invalid_basis result: this member, in AC-007; the predicate language and judgment of each constraint kind: the owning signature; further stop values and their refinement: the signature's stop contract; the stop mapping of one traversal: its record, under §5 | 3, 9, 10 |
| P1 (independent), P6 (independent) | By P1 a difference in representation is not a difference in meaning unless declared, and by P6 latitude is granted only by its owner, so two values differ only through a declared latitude or transformation relation; silence is not latitude, and latitude grants no authority beyond its owner, scope, basis and invalidation law | [Latitude](#latitude), [AC-008](#ac-008-explicit-latitude) | each latitude record: its owner | 6, 10 |
| P4b (derived from P0 and P2), P6 (independent) | By P4b an unresolved condition persists until disposed, and by P6 only an authority disposes it, so a material uncertainty stays in the model until an authorised disposition; no projection, compression, interpretation or encoding erases a residual, and absence from a projection is not resolution | [Residual](#residual), [AC-009](#ac-009-residual-conservation) | each residual kind's domains: the owning signature; each disposition: the competent authority | 9, 10 |
| P0 (recovered), P2 (independent), P4b (derived from P0 and P2) | By P0 an actor holds a bounded set of records, by P2 it needs those its task requires, and by P4b established records persist, so material closure is the least lawful record closure, defined only on exact inputs and claiming no minimal size or cost; a projection contains the closure, records its seams and never silently trims a required member to fit a carrier or capability budget | [AC-010](#ac-010-material-closure), [AC-011](#ac-011-projection) | the seed set and the relation family: the evaluation that applies them, for a step [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) | 7, 10 |
| P3 (independent), P6 (independent) | By P3 a basis is immutable once bound, and by P6 a change to its meaning needs an owned relation, so an overlay adds records without mutating its basis; override, disambiguation, equivalence, specialisation or translation exists only as a typed relation with its authority | [AC-012](#ac-012-overlay) | each overlay relation: its owner | 2, 10 |
| P4b (derived from P0 and P2), P3 (independent), P6 (independent) | By P4b a transformation's effects are facts that persist, by P3 they bind exact records, and by P6 their classification is accountable, so a transformation proves a closed delta over local records and external resolutions, each classified once as preserved or removed, with preservation shown by byte or typed equality; its result is a proposed successor that admits nothing | [AC-013](#ac-013-transformation) | each transformation, with its operation authority and preservation relation: the owner of the transformation record | 3, 4, 10 |
| P6 (independent), P3 (independent) | By P6 judgment and promotion are separate authorities, and by P3 a judgment binds its exact subject, so a judgment points to an unchanged subject, and promotion is a separate relation between that subject and its admission or acceptance judgment | [AC-014](#ac-014-judgment-separation) | none | 9, 10 |
| P4a (independent), P3 (independent), P6 (independent); (iii) | By P4a a traversal composes only through its declared contract, by P3 it binds one functor kind, by P6 its authority is separate, and by (iii) some predicates are decided mechanically and others not, so a traversal is a typed contract applied under exactly one functor kind; deterministic evaluation, probabilistic construction and human adjudication are distinct kinds, each distinct from actor, executor and domain operation, and the name asserts no categorical functor; traversals compose only under typed composition, which keeps both identities and every intermediate fact | [§5](#5-traversals-and-functor-kinds), [AC-015](#ac-015-functor-classification), [AC-016](#ac-016-typed-composition) | the functor kinds permitted for each traversal: the owning signature; the order of kinds in an application: that application | 4, 8, 10 |
| P1 (independent), P6 (independent), P4b (derived from P0 and P2); (ii), (iii) | By P1 an interpretation is a proposal about meaning, by P6 its acceptance is separate, by P4b its provenance persists, and by (ii) and (iii) models are interpreted from exact subjects and partly checked mechanically, so an interpretation proposes a model that its construction does not accept; every admitted record has exact provenance or is identified as model-local, every evaluated subject declaration has a disposition, structural success is evidence for semantic review and never a substitute, and a valid model satisfies every applicable law | [§6](#6-interpretation-and-models), [AC-017](#ac-017-interpretation-fidelity), [AC-018](#ac-018-structural-and-semantic-separation), [AC-019](#ac-019-valid-model) | the interpretation contract and the semantic selection and acceptance authority: the downstream authority of the subject; a decision contract for a semantic subset: the model that supplies it | 6, 10 |
| P3 (independent), P6 (independent); (ii) | By P3 the calculus, a model and a carrier are distinct objects, by P6 each has its own proof obligation, and by (ii) a model may be encoded in several carriers, so the calculus, an interpreted model and an encoded carrier have separate identities, judgments and proof obligations; encoding needs an accepted judgment over the unchanged model, and a downstream success ratifies no upstream layer | [§7](#7-layers), [AC-020](#ac-020-layer-and-release-separation) | Product status of a layer: the external authority that selects and releases it | 6, 10 |
| P3 (independent), P6 (independent) | By P3 an edition binds its exact published bytes, and by P6 its identity record is a separate authority, so an edition's identity is an external record over its published bytes and its derivation clauses, created after the bytes exist; interpreted and encoded identities bind their upstream identities, and judgments stay outside the identities they judge | [§8](#8-calculus-identity) | the record shape, RFC 8785 canonicalisation, SHA-256 and the order of principle references: this member; the record grammar and issuance authority for interpreted and encoded identities: the owning Product; issuance of this edition's record: its release, under [RELEASE](RELEASE.md) | 2, 10 |
| P2 (independent), P6 (independent) | By P2 the calculus serves applications without choosing for them, and by P6 selection and release belong to their owners, so the calculus selects, constructs, accepts or releases no concrete interpretation or carrier, and an application's import, translation or specialisation stays external to it | [Application boundary](#application-boundary), [External imports and specialisations](#external-imports-and-specialisations) | each application's subject, interpretation, carrier and imports: the downstream authority that owns the application | 1, 10 |
| P0 (recovered), P2 (independent), P4b (derived from P0 and P2), P6 (independent); (i), (iii) | P0 bounds what an actor can hold and P2 fixes the task's destination, so an actor needs the constraints of one task, not the whole model, and the material closure and projection of AC-010 and AC-011 supply them as a constraint surface. P4b keeps every residual until an authorised disposition, so unresolved conditions travel with the surface and block the work that depends on them; P6 keeps authority, evidence and acceptance apart, so a surface grants no authority and its validity, fidelity and sufficiency for a task are separate claims | [Constraint surfaces](#constraint-surfaces) | the interpretation used and which one is current: the downstream authority of the subject; the seed set and relation family of a task: the activation that applies them, for a step [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope); a mechanical projection: a separately selected checking contract | 7, 10 |
| P6 (independent) | By P6 a claim about this member holds only on evidence that tests each law, so a review or qualification of this member covers each law with positive and refusal cases, and no example, checker, model or carrier qualifies a law beyond the claim it evaluates | [§10](#10-conformance-obligations) | the ten obligations as the minimum coverage: this member; a policy of this member: each law is covered by positive and refusal cases | 9, 10 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, position and derivation provenance: [§8 Calculus identity](#8-calculus-identity), whose `derivation_basis` names the clauses identified under Derivation provenance and keeps the predecessor authority distinct from the publishing carrier; the family tables of [ODD](ODD.md#foundation-to-law), [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md#foundation-to-law) and [WORLD_MODEL](WORLD_MODEL.md#foundation-to-law), whose rows import F9.
- Row 2, scope and exclusions: [SPEC_METHOD §11 Build-tenant binding](SPEC_METHOD.md#11-build-tenant-binding), rule 6, where a representation in a_c prescribes no executor and establishes no execution conformance by itself; otherwise no separate consumer applies: the claims the calculus does not make are limits on this member's own rules, and what an application selects, accepts or executes is that application's under [Application boundary](#application-boundary), traced in row 17.
- Row 3, closed signature, typed records and reference closure: [TRAVERSAL_OCCURRENCE Imported calculus boundary](TRAVERSAL_OCCURRENCE.md#imported-calculus-boundary), which instantiates its signature over `RecordKind_ac` and `Population_M` unchanged and refuses hidden records and ambiguous references, [Closed semantic-object sorts](TRAVERSAL_OCCURRENCE.md#closed-semantic-object-sorts), where every `_ref` resolves exactly once under AC-003, and [Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), where a dangling reference refuses under AC-003; [AC-007](#ac-007-constraint-and-refusal), whose `refusal(constraint)` names a missing record family and a dangling reference; [AC-019](#ac-019-valid-model), clause 2.
- Row 4, scoped identity and relation typing: [Constraint surfaces](#constraint-surfaces), whose objects carry identity under AC-002 and whose predicates and dependencies include the typed relations of AC-004; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 22. IDENTITY's lead records that AC-002 applies the scoped identity of IDENTITY §2 and applies nothing of AC-002.
- Row 5, authority conservation and basis coherence: [AC-007](#ac-007-constraint-and-refusal), whose `refusal(basis)` names mixed bases with no composite-basis relation; [Constraint surfaces](#constraint-surfaces), where the surface grants no authority and binds the calculus basis as a separate coordinate; [AC-019](#ac-019-valid-model), clause 2. No section of another member applies them: the generic rules they bind to a_c records are FOUNDATIONS §2 Authority kinds', RF-005's and RF-006's, each applied by its own consumers.
- Row 6, constraint judgment and the stop algebra: [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), which maps its stops under AC-007 and refines them under the parent-value rule of §5; [AC-010](#ac-010-material-closure), [AC-011](#ac-011-projection), [AC-013](#ac-013-transformation), [AC-015](#ac-015-functor-classification), [§6 Interpretation and models](#6-interpretation-and-models) and [§7 Layers](#7-layers), each of which takes the core value of its stops or judgments under AC-007; [Constraint surfaces](#constraint-surfaces), required results and condition 2.
- Row 7, latitude: [Constraint surfaces](#constraint-surfaces), permitted freedom and condition 1; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 17 and 18. The generic rule over any two values is FOUNDATIONS §4 Algebra, Latitude's, which cites AC-008 as provenance only.
- Row 8, residual conservation: [Constraint surfaces](#constraint-surfaces), unresolved conditions and condition 2; [AC-013](#ac-013-transformation), where material residuals remain in the successor unless an authorised disposition is in the transformation evidence; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminator 16.
- Row 9, material closure and projection: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), steps 1 and 2, and [§3 Admission and activation](ACTIVATION.md#admission-and-activation), `closure_unresolved`; [Constraint surfaces](#constraint-surfaces), whose surface is the projection over the material closure of a task's seed set; [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md#traversal_occurrence), its lead, which keeps its `Projection` record apart from an AC-011 projection. The rule that no reference trims a required member is FOUNDATIONS §4 Algebra, Reference versus body's, which AC-011 applies.
- Row 10, overlay: [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution), which relates its four semantic-resolution kinds to the typed relations AC-012 names; [AC-019](#ac-019-valid-model), clause 3.
- Row 11, transformation: [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Conservation accounting; [REFERENCE_FRAME §6 Evidence or coordinate translation](REFERENCE_FRAME.md#evidence-or-coordinate-translation), where a translation represented in a_c is recorded in the fields of AC-013; [SPEC_METHOD §11 Build-tenant binding](SPEC_METHOD.md#11-build-tenant-binding), rule 7; [Constraint surfaces](#constraint-surfaces), admissible operations.
- Row 12, judgment separation: [Constraint surfaces](#constraint-surfaces), evidence; [§7 Layers](#7-layers), where the acceptance judgment is over the unchanged model and neither judgment enters the identity of its subject; [§8 Calculus identity](#8-calculus-identity), where the semantic-acceptance and carrier-admission judgments point to unchanged identities and are embedded in neither. No section of another member applies it; EVALUATION §5 Acceptance states that a disposition is over an unchanged subject as its own rule and cites AC-014 as provenance only.
- Row 13, traversals, functor kinds and typed composition: [ACTIVATION §4 Refinement](ACTIVATION.md#refinement), where each output satisfies the next step's declared domain and preconditions as AC-016 requires; [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds), whose functor-kind refs leave their laws with §5, and [Occurrence identity](TRAVERSAL_OCCURRENCE.md#occurrence-identity), where every retained application under AC-016 has its own occurrence; [ODD](ODD.md#odd), its lead, and [ODD §5 Probabilistic compute](ODD.md#probabilistic-compute), which keep the profile's F_D, F_P and F_H shorthands apart from the functor kinds of §5, and [ODD §5 Graph functions](ODD.md#graph-functions), where each inner function's input satisfies its declared domain as AC-016 requires; [PROFILES §1](PROFILES.md#1-the-boundary), which keeps the traversal record and the functor kinds as this member's terms and binds them only by declaration; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 22 and 51; [AC-013](#ac-013-transformation), as a specialisation of one traversal record, and [AC-007](#ac-007-constraint-and-refusal), whose `refusal(constraint)` names an application without its traversal.
- Row 14, interpretation and models: [EVALUATION §2](EVALUATION.md#2-separation), which binds its separation to a_c models through AC-018 and AC-019; [SPEC_METHOD §11 Build-tenant binding](SPEC_METHOD.md#11-build-tenant-binding), rule 6; [TRAVERSAL_OCCURRENCE Imported calculus boundary](TRAVERSAL_OCCURRENCE.md#imported-calculus-boundary), where an occurrence model satisfies a_c under its signature; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 13, 14, 20, 40 and 45; [§7 Layers](#7-layers) and [§8 Calculus identity](#8-calculus-identity), where an interpreted model awaits a separate acceptance judgment and its identity binds the interpretation contract; [Constraint surfaces](#constraint-surfaces), which an interpretation yields, conditions 5 and 6.
- Row 15, layers and release separation: [SPEC_METHOD §6 Lineage and release](SPEC_METHOD.md#6-lineage-and-release), where layer and release separation holds for release lineage; [FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Formal fragment, where the separate identities of a_c, its interpretations and their carriers are AC-020's; [§8 Calculus identity](#8-calculus-identity), which binds the identity of each layer and issues this edition's record under AC-020. RELEASE's lead imports §7 and §8 and applies no rule of them.
- Row 16, calculus identity: [TRAVERSAL_OCCURRENCE Closed profile signature](TRAVERSAL_OCCURRENCE.md#closed-profile-signature), whose calculus-basis identity resolves the record and the derivation account that §8 defines; otherwise no separate consumer applies: issuance of this edition's record is its release's act under RELEASE, whose lead imports §8 and applies no rule of it, and IDENTITY's lead leaves the identity of a calculus edition to §8 without restating it.
- Row 17, application boundary and external imports: [§5 Traversals and functor kinds](#5-traversals-and-functor-kinds), where a same-spelled term specialises the traversal record only through a declared binding under its owner's authority; [Constraint surfaces](#constraint-surfaces), which selects, constructs and accepts no interpretation under the Application boundary; [§8 Calculus identity](#8-calculus-identity), where the owning Product defines the record grammar and issuance authority of the downstream identities. No section of another member applies them: [PROFILES §1](PROFILES.md#1-the-boundary) states the declared-binding rule from the profile's side as its own, under which TRAVERSAL_OCCURRENCE imports this member, and ACTIVATION §4 Refinement states the declaration conditions of a specialised contract as its own, with the predecessor section as provenance only.
- Row 18, constraint surfaces: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), Acquisition, where a step acquires a current surface as a derived surface under this section's conditions; [CONFORMANCE §5](CONFORMANCE.md#5-coverage-of-the-common-discriminators), discriminators 15 to 18.
- Row 19, conformance obligations: no separate consumer applies. The obligations bind a review or qualification of this member and are read where that claim is made; the conformance obligations of [TRAVERSAL_OCCURRENCE](TRAVERSAL_OCCURRENCE.md#conformance-obligations) are that profile's own, over its signature, and name this section nowhere.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

§11 records where each predecessor claim is carried and decides nothing.
The table is new in this corpus. Purpose and material relation: an actor
started on this member sees which rules of the calculus follow from the
foundations and which are choices, with the owner of each choice, so no
choice is presented as derived (P6, P1).
```


### Row `AXIOMATIC_CALCULUS.md#residual` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#residual` at rc.2:

```text
### Residual

Residual uncertainty is first-class model content:

```text
Residual = {
  id,
  subject,
  kind,
  uncertainty,
  consequence,
  context,
  owner,
  scope,
  basis,
  re_entry,
  invalidation
}
```

Projection, compression, interpretation, or encoding cannot erase a residual.
It remains represented, is explicitly dispositioned by competent authority, or
causes refusal.

`kind` resolves one declared `ResidualKind`. The owning signature defines its
lawful subject, uncertainty, consequence, re-entry, and invalidation domains.
An undeclared residual kind or value refuses structural admission.
```

Successor, `AXIOMATIC_CALCULUS.md#residual`:

```text
### Residual

Residual uncertainty is first-class model content; a residual record is
the Residual of FOUNDATIONS §2 carried inside a model (P4b; rc.2
#residual):

```text
Residual = {
  id,
  subject,
  kind,
  uncertainty,
  consequence,
  context,
  owner,
  scope,
  basis,
  re_entry,
  invalidation
}
```

Projection, compression, interpretation or encoding cannot erase a
residual. It remains represented, is explicitly dispositioned by competent
authority, or causes refusal (P4b, P6).

`kind` resolves one declared `ResidualKind`. The owning signature defines
its lawful subject, uncertainty, consequence, re-entry and invalidation
domains. An undeclared residual kind or value refuses structural admission
(P3).
```


### Row `AXIOMATIC_CALCULUS.md#scope` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#scope` at rc.2:

```text
## Scope

`a_c` governs the form of a symbolic axiomatic model. It answers:

- what identities and typed objects exist;
- how relations bind exact endpoints;
- how constraints, latitude, and residuals remain explicit;
- how traversals and judgments are typed;
- how material closure, projection, overlay, and transformation behave;
- what a model must preserve from its subject; and
- which claims are structural, semantic, or authority decisions.

`a_c` does not choose the subject vocabulary, decide which source declarations
are material, supply semantic acceptance, select a carrier, execute a model, or
prove that one interpretation is uniquely correct.
```

Successor, `AXIOMATIC_CALCULUS.md#scope`:

```text
### Scope

`a_c` governs the form of a symbolic axiomatic model (P2; rc.2 #scope). It
answers:

- what identities and typed objects exist;
- how relations bind exact endpoints;
- how constraints, latitude and residuals remain explicit;
- how traversals and judgments are typed;
- how material closure, projection, overlay and transformation behave;
- what a model must preserve from its subject; and
- which claims are structural, semantic or authority decisions.

`a_c` does not choose the subject vocabulary, decide which source
declarations are material, supply semantic acceptance, select a carrier,
execute a model or prove that one interpretation is uniquely correct (P2,
P6).
```


### Row `AXIOMATIC_CALCULUS.md#semantic-object` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#semantic-object` at rc.2:

```text
### Semantic Object

Every semantic object has exactly:

```text
SemanticObject = {
  id,
  sort,
  context,
  owner,
  scope,
  basis,
  value
}
```

`id`, `sort`, `context`, `owner`, and `basis` are identities. `scope` is the
closed governed domain. `value` is sort-defined carrier-neutral content or a
reference to exact content.
```

Successor, `AXIOMATIC_CALCULUS.md#semantic-object`:

```text
### Semantic object

Every semantic object has exactly (P3; rc.2 #semantic-object):

```text
SemanticObject = {
  id,
  sort,
  context,
  owner,
  scope,
  basis,
  value
}
```

`id`, `sort`, `context`, `owner` and `basis` are identities. `scope` is
the closed governed domain. `value` is sort-defined carrier-neutral content
or a reference to exact content. A semantic object is an Object of
FOUNDATIONS §2 whose scoped identity is carried by `id`, `owner` and
`sort` and whose boundary is `scope`.
```


### Row `AXIOMATIC_CALCULUS.md#subject-and-carrier-boundaries` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#subject-and-carrier-boundaries` at rc.2:

```text
## Subject And Carrier Boundaries

The three governed layers are:

```text
a_c       = the pure calculus
a_c.X     = subject X interpreted as a model of a_c
a_c.X.C   = that accepted model encoded in carrier C
```

Their relations are:

```text
M_X = Interpret_a_c(X)
J_X = Accept_X(M_X) -> accepted | refuse
G_C = Encode_C(M_X, J_X) where J_X = accepted
D_C = F_D[v_carrier_admission](G_C, Profile_C, CarrierBasis_C)
      -> admitted | refuse
```

`J_X` is an external semantic-acceptance judgment over unchanged `M_X`.
Encoding requires `J_X.decision = accepted` and exact equality between the
judgment subject identity and digest and `M_X`; hold or refusal cannot be
encoded. `D_C` is a judgment over unchanged carrier bytes. It is not a
transformed carrier. The admitted encoding evidence relation is the exact
triple `(G_C, J_X, D_C)`; neither judgment enters the identity of its subject.

### AC-020 Layer And Release Separation

`a_c`, `a_c.X`, and `a_c.X.C` have independent content identities, judgments,
supersession relations, and proof obligations:

- `a_c` qualification evaluates internal coherence against its complete
  declared calculus-law set;
- `a_c.X` proves faithful interpretation of exact subject `X`; and
- `a_c.X.C` proves faithful, canonical encoding of the accepted model in
  carrier `C`.

An encoding failure does not change `a_c.X`. An interpretation failure does not
change `a_c`. A downstream success cannot ratify an upstream layer or basis.
None of these layers is automatically an independently released Product. The
external authority that selects and releases one owns that Product status.
```

Successor, `AXIOMATIC_CALCULUS.md#7-layers`:

```text
## 7. Layers

The three governed layers are (P3; rc.2 #subject-and-carrier-boundaries):

```text
a_c       = the pure calculus
a_c.X     = subject X interpreted as a model of a_c
a_c.X.C   = that accepted model encoded in carrier C
```

Their relations are:

```text
M_X = Interpret_a_c(X)
J_X = Accept_X(M_X) -> accepted | refuse
G_C = Encode_C(M_X, J_X) where J_X = accepted
D_C = F_D[v_carrier_admission](G_C, Profile_C, CarrierBasis_C)
      -> admitted | refuse
```

`J_X` is an external semantic-acceptance judgment over unchanged `M_X`.
Encoding requires `J_X.decision = accepted` and exact equality between the
judgment subject identity and digest and `M_X`; hold or refusal cannot be
encoded. `D_C` is a judgment over unchanged carrier bytes; it is not a
transformed carrier. The admitted encoding evidence relation is the exact
triple `(G_C, J_X, D_C)`; neither judgment enters the identity of its
subject (P6, P3). Each judgment answers its own predicate, that `M_X` is
accepted and that the carrier bytes are admitted: `accepted` and
`admitted` map to satisfied, a hold maps as AC-007's `hold`, and `refuse`
is a `refusal` that takes its core value under AC-007 by its cause (P5,
P6). The mapping is new; its purpose is that an acceptance or admission
judgment combines with other results only through the one core, so a
withheld or refused judgment is never read as accepted.

### AC-020 Layer and release separation

`a_c`, `a_c.X` and `a_c.X.C` have independent content identities,
judgments, supersession relations and proof obligations (P3, P6; rc.2
#ac-020-layer-and-release-separation):

- `a_c` qualification evaluates internal coherence against its complete
  declared calculus-law set;
- `a_c.X` proves faithful interpretation of exact subject `X`; and
- `a_c.X.C` proves faithful, canonical encoding of the accepted model in
  carrier `C`.

An encoding failure does not change `a_c.X`. An interpretation failure
does not change `a_c`. A downstream success cannot ratify an upstream
layer or basis. None of these layers is automatically an independently
released Product. The external authority that selects and releases one
owns that Product status. SPEC_METHOD §6 applies this law to release
lineage.
```
