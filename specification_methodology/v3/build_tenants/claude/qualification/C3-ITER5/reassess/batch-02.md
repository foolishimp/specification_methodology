# I5-03 reading batch 02

Rows: 14. Members: ['AXIOMATIC_CALCULUS.md', 'DESIGN_MODULE_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds` at rc.2:

```text
## Traversals And Functor Kinds

A traversal is a typed contract:

```text
v = {
  id,
  domain,
  codomain,
  context,
  owner,
  scope,
  basis,
  preconditions,
  postconditions,
  authority,
  evidence,
  provenance,
  stop_states
}
```

`a_c` defines three fundamental functor-kind identities:

```text
F_D = urn:stdo:concept:axiomatic-calculus:f-d
F_P = urn:stdo:concept:axiomatic-calculus:f-p
F_H = urn:stdo:concept:axiomatic-calculus:f-h
```

Application notation is:

```text
F_K[v](X_v) -> Y_v | Omega_v
```

where `F_K` is one functor kind, `v` is one exact traversal identity, `X_v` and
`Y_v` are its typed input and result domains, and `Omega_v` is its closed stop
algebra.

- `F_D` classifies deterministic evaluation or proof over declared properties.
  It returns a judgment and does not perform the domain construction being
  judged.
- `F_P` classifies bounded probabilistic interpretation, construction, or
  proposal under an exact traversal contract. Its result has no semantic,
  admission, acceptance, or closure authority merely because it is useful or
  repeatable.
- `F_H` classifies explicit human adjudication under an exact identity,
  authority grant, subject, basis, and decision contract. Human presence grants
  no ambient authority.

The actor, executor, domain operation, and functor kind are different
coordinates. `Encode`, `Interpret`, `Serialize`, `Measure`, and other named
domain operations are not aliases for `F_D`, `F_P`, or `F_H`. Different
traversals may share one functor kind without sharing identity, semantics,
inputs, outputs, authority, or evidence.

`Functor Kind` is an `a_c` term for this traversal classification. It does not
by itself assert a category-theoretic functor. A model claiming categorical
functor laws additionally defines its source and target categories and proves
identity and composition preservation.

### AC-015 Functor Classification

Every functor application binds exactly one functor kind and one traversal
identity. Applying any `F_*` kind without bracketed traversal identity `[v]` is
incomplete.

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

Successor, `AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds`:

```text
## 5. Traversals and functor kinds

A traversal is a typed contract (P4a, P6; rc.2
#traversals-and-functor-kinds):

```text
v = {
  id,
  domain,
  codomain,
  context,
  owner,
  scope,
  basis,
  preconditions,
  postconditions,
  authority,
  evidence,
  provenance,
  stop_states
}
```

The traversal record is this member's own concept. A same-spelled term
owned by a profile, a realisation or a runtime is not imported by nominal
equality and does not specialise this record except through a declared
binding under that owner's authority (§9; P3, P1).

`a_c` defines three fundamental functor-kind identities (P3):

```text
F_D = urn:stdo:concept:axiomatic-calculus:f-d
F_P = urn:stdo:concept:axiomatic-calculus:f-p
F_H = urn:stdo:concept:axiomatic-calculus:f-h
```

Application notation is:

```text
F_K[v](X_v) -> Y_v | Omega_v
```

where `F_K` is one functor kind, `v` is one exact traversal identity,
`X_v` and `Y_v` are its typed input and result domains, and `Omega_v` is
its closed stop algebra. `Omega_v` is a refinement of the core result
algebra of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results): it adds no
core value, and each of its stop values maps to exactly one core value,
never to `satisfied`. A stop this member writes, `hold`, `gap`,
`refusal(constraint)` or `refusal(basis)`, has the meaning and the core
value that AC-007 gives it. The signature's stop contract declares any
further stop value with the one core value it maps to, and may refine a
stop value by cause. A traversal record's `stop_states` binds the stop
mapping of that traversal, exactly one core value for each stop value; it
may refine a value of the signature's stop contract further by cause for
that traversal. Each refined value, whether the stop contract or a
`stop_states` declares it, names its parent value and its cause and maps
to its parent's core value: a value refined from `hold` to indeterminate,
from `gap` or `refusal(basis)` to invalid_basis, and from
`refusal(constraint)` to falsified. No refined value takes `satisfied`. A
different core value needs a different parent value, which only the member
that owns the parent declares; for these four stops that member is this
one. Neither the stop contract nor a traversal's `stop_states` raises a
result's standing (P5, P6). Purpose and material relation: one stop of one
traversal has one core value, so its consumers cannot read it two ways,
and no refinement gives a stop another core value, so a violated
constraint never becomes a case that the evidence merely cannot decide.

- `F_D` classifies deterministic evaluation or proof over declared
  properties. It returns a judgment and does not perform the domain
  construction being judged (P6).
- `F_P` classifies bounded probabilistic interpretation, construction or
  proposal under an exact traversal contract. Its result has no semantic,
  admission, acceptance or closure authority merely because it is useful
  or repeatable (P6, P0; instance premise (iii) of §1 Foundation to law).
- `F_H` classifies explicit human adjudication under an exact identity,
  authority grant, subject, basis and decision contract. Human presence
  grants no ambient authority (P6).

The actor, the executor, the domain operation and the functor kind are
different coordinates. `Encode`, `Interpret`, `Serialize`, `Measure` and
other named domain operations are not aliases for `F_D`, `F_P` or `F_H`.
Different traversals may share one functor kind without sharing identity,
semantics, inputs, outputs, authority or evidence (P3, P6).

"Functor kind" is an `a_c` term for this traversal classification. It does
not by itself assert a category-theoretic functor. A model that claims
categorical functor laws carries the demonstration that
[FOUNDATIONS §4](FOUNDATIONS.md#4-algebra), Formal fragment, requires of
every categorical claim (P6, P1).

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

Successor, `FOUNDATIONS.md#4-algebra`:

```text
## 4. Algebra

Composition. For steps s₁: X → Y and s₂: Y → Z, s₂ ∘ s₁ exists only under P4a.
The composite's output carries both steps' step-produced facts; its result
is composed as [Conjunction of results](#conjunction-of-results) states.
[RF-010](REFERENCE_FRAME.md#rf-010-composition-on-demand) states once
when a composition law is required and when independently activated
evaluations may instead return closed results to one declared conjunction
or decision rule (P4a).

Conservation accounting. Every transformation records what it preserved,
introduced and removed, its external resolution witnesses and its residuals
(AC-013). How results, known failures and uncovered coverage combine is
[Conjunction of results](#conjunction-of-results).

Reference versus body. A reference conserves a relation when its owner,
exact selector, authenticity, availability and completeness support the same
consuming decision. An inaccessible or insufficient reference is a residual,
not success. A projection cannot trim a required member to fit a carrier or
budget
([AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection)).

Latitude. Two values differ lawfully only through a declared latitude or
transformation relation; preference, probabilistic choice and human presence
are not implicit latitude
([AC-008](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude)).

Shared machinery. Computational similarity yields a commonisation candidate,
never an adjudication of identity or authority; one implementation may serve
many instances while each instance keeps its responsibility and binding
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019),
[UP-023](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#capability-and-foundation-selection-stdo-up-023)).

Formal fragment (P6, P1). A categorical claim, about this method or about a
construction made with it, is established only with the demonstration it
requires, as far as each part applies to it:

- each category it claims states its objects, its arrows, when two arrows
  are equal, an identity arrow on each object, and a composition of arrows
  that is associative and has those identities as units;
- each map between categories is defined on objects and on arrows, and is
  called a functor only after its preservation of identities and
  composition is proved;
- its laws, records and maps are represented in a_c
  ([AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md)), keeping apart which
  statements are premises, which are consequences and which are declared
  choices; the separate identities of a_c, its interpretations and their
  carriers are
  [AC-020](AXIOMATIC_CALCULUS.md#ac-020-layer-and-release-separation)'s,
  and what a structural check of the representation establishes is
  [EVALUATION §2](EVALUATION.md#2-separation)'s;
- it names its supporting evidence and its scope, distinguishing mechanical
  checks, mathematical arguments and tests against independently specified
  oracles; what that evidence leaves unresolved is recorded separately, not
  as a fourth kind of support.

Whether a claim asserts conformance, an equivalence or a map's preservation
of structure, and how those claims differ, is the equivalence ladder of
[EVALUATION §6](EVALUATION.md#6-conformance-of-realisations). What a
refinement or rewrite step preserves, and the law that licenses it, are
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement), Refinement. A
categorical statement without the demonstration it requires is a
hypothesis: it is not law and is carried for falsification with §5. This
conserves
[functor kinds](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds),
which requires a model claiming functor laws to define its source and
target categories and prove identity and composition preservation, and
asserts no categorical functor itself. Purpose and material relation of
arrow equality, associativity, the representation in a_c and the supporting
evidence: a categorical statement is useful only where its constructions
preserve meaning, and these are what preservation must show (P1, P6).

Formal fragment, hypothesis H1, categorical structure: with 𝒜 the free category on typed primitives, ℐ the selected
carrier sets with total functions and 𝒞_H pairs of functions with additive
costs, S: 𝒜 → ℐ and R_H: 𝒜 → 𝒞_H would be
functors, S neither faithful nor an equivalence. It has no supporting
evidence and the whole claim is unresolved: no rc.2 clause and no argument in this corpus establishes it,
S and R_H are not defined on arrows, and no preservation of identities or
composition is proved. Until its objects, arrows, arrow equality,
identities and composition are written and preservation is proved, the
diagram is notation; it is not law and is carried for falsification with
§5. H names an architecture, never a runtime.

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

Stale results. A held result is stale for a composite when the basis it
binds is not the basis the composite requires of that component, because
a later state has superseded or advanced it or because it binds another
subject or basis (§2, Basis). Two questions stay apart, so that one
composite has one reported value (P3, P5, P6):

- an evaluation performed on a subject or basis that is stale, advanced,
  ambiguous or mismatched against the one it must bind returns
  `invalid_basis` for its own predicate, or is reactivated on the current
  basis; [RF-005](REFERENCE_FRAME.md#rf-005-exact-basis-and-coordinates)
  states this law over frames, and a conjunction that receives that
  `invalid_basis` holds it as a returned result;
- a component whose only held result is stale has no closed result
  applicable to the composite: on the basis the composite requires, its
  evaluation was not performed. It is a planned assessment without a
  closed result, in the second input, and a gap. Its stale value is
  neither counted as a returned result nor relabelled `invalid_basis` for
  the composite, and it stays in the record with its own basis;
- the declared basis relations disagree (Reported value below) only among
  returned results, each bound to the basis the composite requires of it,
  whose bases the declared rule requires to agree or to join in a coherent
  composite basis, and which do not.

A stale `satisfied` never counts toward the composite. Purpose and
material relation: answering one stale component as a gap in one place and
as `invalid_basis` in another would give one composite two reported
values; keeping the evaluation's own value apart from the composite's gap
keeps the reported value unique and the stale result visible.

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

### Assurance relations

The relations below connect construction to the assertions, observations
and evidence that support claims about it. They are the shared owner for
the preservation, assertion, provenance, quantified-assurance, reuse and
formal-representation obligations in this corpus; ACTIVATION §1, §4, §5 and §7, EVALUATION §1 and §3,
ASSURANCE §3, §10, §11 and §14, RELEASE §8 and §9, SPEC_METHOD §4 and
the a_c interpretation apply them and state no second relation (P6). They are law
carried from the common assurance requirement. A tenant chooses its
representation and execution within these obligations. The notation
states proof obligations; writing an implication does not discharge it.

Foundation to law. This family, assurance relations, covers the six
subsections that follow. Its instance premises are: (a) a construction
with the governing basis bound at intake under ACTIVATION §1 and the
material assumptions, together written Γ here; (b) a declared domain Ω of cases, each with the inputs,
behaviour and environment material to an obligation; (c) a checker with
declared observations and an admitted evaluation relation. They are
conditions of the situations the family governs, not commitments.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P4a (independent), P1 (independent), P6 (independent); instance premise a | By P4a a composite exists only where each boundary is compatible, by P1 a relation written down is not thereby discharged, and by P6 a preservation claim is a claim on evidence, so each claimed step states its domains, relation and property, the implication is a proof obligation, and a relation covering completion alone says nothing about refusal, failure, interruption or unknown effects | [Preservation through construction](#preservation-through-construction) | the adequacy relation and bound of an approximate step: the owner of the step's law | 3, 4, 9 |
| P4a (independent), P2 (independent), P6 (independent); instance premise a | By P4a the composite's property follows only through compatible boundaries, by P2 the final property matters only through its connection to Z, and by P6 that connection is argued, not assumed, so an end-to-end argument establishes the initial condition, each step's premises, compatibility at each boundary and the connection to Z, and preservation is distinct from progress and termination | [Preservation through construction](#preservation-through-construction) | the composition law for concurrency, branches and external effects: the owner of the construction's design | 3, 4, 7 |
| P1 (independent), P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premises a, b | By P1 an assertion's predicate is distinct from the obligation it is derived from, by P6 passing a necessary condition establishes no more than that condition, and by P5 a conjunction's coverage is a claim of its own, so each assertion states whether its predicate is the obligation, a necessary condition or part of a sufficient conjunction, conditional on Γ and Ω | [Assertions and observation](#assertions-and-observation) | the declared domain Ω and the interpretation: the owner of the obligation and the assessor's activation | 6, 9 |
| P3 (independent), P1 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premises b, c | By P3 two admissible cases can differ while their observations agree, by P1 agreement of observations is not agreement of meaning, by P5 an undecidable case is `indeterminate` and never `satisfied`, and by P6 soundness covers every admitted conclusion, so a checker is sound only where its observation separates the cases, and otherwise acquires evidence, narrows its scope or returns `indeterminate` | [Assertions and observation](#assertions-and-observation), Observation sufficiency | the checker's admitted relation T and its observation π: the owner of the assessment frame | 6, 7, 9 |
| P6 (independent), P1 (independent), P4a (independent); instance premises a, c | By P6 an expected answer is justified by its derivation from the obligation and an execution by its record, by P1 a copied answer carries no independent interpretation, and by P4a shared dependencies compose into shared causes of error, so assertion provenance and execution provenance are both required, agreement among paths with shared causes is not independent evidence, and disagreement requires diagnosis | [Parallel derivation and mutual assurance](#parallel-derivation-and-mutual-assurance) | which paths are run and compared: the strategy's owner; the authorship of ported material: EVALUATION §3 and the Cross-Synthesis rule of the owning Product | 6, 9 |
| P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P1 (independent); instance premise c | By P6 a number is a claim on its model and evidence, by P5 an unsupported estimate stays unknown, and by P1 a probability over outcomes is distinct from the truth of the predicate, so a quantified assurance claim states its population, priors, likelihoods, shared causes and calibration limits, and no threshold is imposed by this member | [Quantified assurance](#quantified-assurance) | the risk policy and any threshold: the actor exercising the admitted work authority, under the adopting Product | 9 |
| P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise a | By P3 a changed dependency changes what an earlier observation applies to, by P4b retained evidence is conserved with its subject, by P5 unknown impact leaves the dependent assurance undecided, and by P6 retention is justified and not assumed, so validity dependencies are kept apart from justification links, affected checks are selected conservatively, and evidence is retained only under its validity conditions while mandatory gates stay applicable, which ACTIVATION §7 applies to closed results and handoffs | [Change impact and evidence reuse](#change-impact-and-evidence-reuse) | the representation of dependencies and the selection model: the realisation; mandatory gates: RELEASE §8 and the adopting Product | 2, 9 |
| P1 (independent), P6 (independent); instance premise a | By P1 a representation is distinct from the meaning it carries, and by P6 a label is not evidence, so the formal interpretation distinguishes a stated formula, a discharged argument, checked structure, an external predicate and execution evidence, and finite examples prove no universal implication | [Formal representation](#formal-representation) | the carrier, checker and projections: the tenant's a_c design under AXIOMATIC_CALCULUS | 6, 10 |

Consumers of these rows, one list per row, each consumer linked to its own
locus:

- Row 1, the step obligation: [ACTIVATION §1 Composition boundaries](ACTIVATION.md#construction-relation); [ACTIVATION §4 Refinement](ACTIVATION.md#refinement).
- Row 2, the end-to-end argument: [ACTIVATION §1 Composition boundaries](ACTIVATION.md#construction-relation) and [ACTIVATION §4 Refinement](ACTIVATION.md#refinement), as for row 1.
- Row 3, assertion directions: [EVALUATION §1](EVALUATION.md#1-claims); [ASSURANCE §3](ASSURANCE.md#3-test-authority); [ASSURANCE §10](ASSURANCE.md#10-testing-evidence-composition).
- Row 4, observation sufficiency: [ASSURANCE §11](ASSURANCE.md#11-assurance-subject-acquisition-and-evaluation).
- Row 5, provenance and mutual assurance: [EVALUATION §1](EVALUATION.md#1-claims); [EVALUATION §3](EVALUATION.md#3-independent-assessment); [ASSURANCE §3](ASSURANCE.md#3-test-authority); [ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route); the Cross-Synthesis rule of the Product that owns this corpus.
- Row 6, quantified assurance: [EXECUTIVE_BASELINE Technical triage](EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect), whose causal assessment records a confidence; [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), where a probability informs priority; [ASSURANCE §8](ASSURANCE.md#8-combinatorial-coverage-and-testing-value), where a project may define a testing-value scalar. At each, an unsupported numeric confidence remains unresolved.
- Row 7, change impact and reuse: [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), through which [ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart) and [EVALUATION §3](EVALUATION.md#3-independent-assessment) reach it; [RELEASE §8](RELEASE.md#8-acceptance) and [§9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015); [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage), whose determination of the surfaces and evidence to re-derive is the selection `S_Δ`.
- Row 8, formal representation: [AXIOMATIC_CALCULUS Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces), whose first condition of use keeps each element's kind of support; [CONFORMANCE §4](CONFORMANCE.md#4-cases-from-the-common-discriminators), cases AR-01 to AR-04, which carry the demonstration cases this owner requires. The interpretation that records the kinds is a derived view under AXIOMATIC_CALCULUS, not a consumer of the rule.

Each consumer applies the rule and decides nothing this section does not
(P2, P6).

### Preservation through construction

A construction binds its starting state A and required outcome Z under
[ACTIVATION §1 Construction relation](ACTIVATION.md#construction-relation);
the governing basis bound at its intake and the material assumptions are
together written Γ here. The
predicate for Z includes required effects and trace properties where
these matter.

For a sequence of transformations, let `X_i` be the state or trace domain
at boundary i, `F_i ⊆ X_i × X_(i+1)` the declared transition relation, and
`P_i` the property to retain or establish there. A claimed preservation
step has the form:

```text
For all x, x':  P_i(x) and F_i(x, x')  implies  P_(i+1)(x').
```

The relation accounts for the outcomes, effects and assumptions material
to the claim. A relation covering successful completion alone supplies no
claim about refusal, failure, interruption or unknown effects; those
cases follow Results above and the result, authority and recovery
contracts of ACTIVATION §3 and §5. The real execution's conformance to
the relation is a separate obligation (P4a, P1, P6).

An end-to-end argument establishes the initial condition, each step's
applicable premises, compatibility at each composition boundary, and the
connection from the final property to Z. The preceding postcondition
must establish the next precondition, or the missing condition must be
acquired and justified. Concurrency, alternative branches and external effects
require their applicable composition law; a sequential drawing does not
establish one. Local success alone establishes neither composition
compatibility nor Z. Preservation is distinct from progress, termination
and the availability of a suitable next step (P4a, P2, P6).

Exact transformations preserve the declared meaning. Approximate
transformations state their adequacy relation and an established bound
for the complete composition; local tolerances cannot be assumed to add or
to remain unchanged. [ACTIVATION §4 Refinement](ACTIVATION.md#refinement),
Exact and approximate steps, owns the per-step law and applies this
obligation to refinement steps. A
change to the governing outcome or meaning follows its owner and the
successor rules of SPEC_METHOD §4 and RELEASE §9 (P1, P6).

The algorithmic account states the required operation, the informational
account the meaning and distinctions retained, and the computational
binding how work and observations are realised
([§2 Accounts of a construction](#accounts-of-a-construction)). A claim
across these accounts identifies its maps and preservation obligations;
execution by a person, a machine or a mixed arrangement does not
discharge them by itself. A commuting diagram, functor or equivalence
claim requires the categorical demonstration above (P1, P6).

### Assertions and observation

For a selected source obligation r, let `Q_r = interpret(r, Γ, Ω)` be its
required predicate over the declared domain Ω of cases. The interpretation
retains the obligation's scope, conditions, exceptions and permitted
alternatives. A source identifier or digest authenticates the selected
text; it does not prove the interpretation faithful (P1, P3).

An assertion targets a predicate `q_t` and states whether that predicate
is the full obligation or a narrower claim. The directions differ:

```text
Q_r implies q_t                   : q_t is a necessary condition of Q_r.
q_t implies Q_r                   : establishing q_t is sufficient for Q_r.
(q_1 and ... and q_n) implies Q_r : the stated conjunction is sufficient.
```

These implications are conditional on Γ and Ω. Passing a check of a
necessary condition does not establish the full obligation. A conjunction
requires its own coverage and compatibility argument; a collection of
passing tests does not supply it by its count (P1, P6, P5).

Let `π: Ω → O` describe the observations available to a checker and
`T ⊆ O × R` its admitted evaluation relation, where R is the core result
algebra of Results above. A deterministic checker is a functional special
case. A human or probabilistic checker can admit different conclusions on
the same observations; a universal soundness claim covers all admitted
conclusions, not a favourable selected run. `indeterminate` is the core
judgment whose admissible evidence cannot decide the predicate (Results).
It is distinct from an evaluation that was not performed, and from work
or coverage that remains unresolved, which is a state of the work
([ACTIVATION §3](ACTIVATION.md#3-step-results-and-disposition),
[§5](ACTIVATION.md#5-work-state-and-restart)) and not a judgment value.
Writing `sat` and `fal` for the satisfied and falsified judgments about
`q_t`, not new execution states:

```text
For every s in Ω:
  (π(s), sat) in T  implies  q_t(s).
  (π(s), fal) in T  implies  not q_t(s).
```

The candidate identifies what supports each claimed direction and where
it is unresolved. A relation admitting both a sound satisfied judgment
and an indeterminate judgment need not always decide the case. A
restricted deterministic model retains its scope, and an actual checker
requires its own conformance account. An observed test pass remains an
observation while the oracle's fidelity is unestablished; it does not
become established satisfaction of the source obligation, and a reported
failure is treated the same way. The observation binding itself needs
support: an idealised π does not establish that the instrument, actor or
execution acquired the required facts correctly. A probabilistic claim
uses its declared distribution over outcomes under Quantified assurance
below; the relation alone supplies no probabilities (P6, P5, P1).

Observation sufficiency. A checker that always decides `q_t` correctly
from π alone requires:

```text
For all s, s' in Ω:
  π(s) = π(s')  implies  q_t(s) = q_t(s').
```

If two admissible cases have the same observation but opposite truth
values, that observation cannot support a sound complete decision between
them; further evidence, a justified narrower scope or an indeterminate
judgment is required. In a classical set model this condition permits a
predicate on the image of π; it establishes neither an executable decision
procedure nor its cost. Unknown effects and unavailable observations
retain their distinctions from falsehood and from an evaluation that was
not performed (Results) (P3, P1, P5, P6).

### Parallel derivation and mutual assurance

Construction and assurance can follow different paths from a common
obligation. For `requirement → refinement → realisation`, assertions
derived from the requirement check its applicable conditions in the
realisation; assertions derived from the refinement check its more
detailed obligations there. Acceptance tests and build-level tests can
instantiate these paths
([ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route)); the
roles identify the selected sources and subject in this example and
prescribe no stage names or test classes (P1, P6).

An expected result or acceptance predicate has assertion provenance: the
owning obligation, its interpretation, assumptions, derivation and shared
dependencies, which give it meaning. An execution has execution
provenance: the actual checker, exact subject, applicable environment,
inputs, observations and result. Both are needed for the claims they
support; execution records alone cannot establish that the expected
answer follows from the requirement. Authentication of a returned
assessment, which binds a result to its producer, subject, basis and
evidence ([EVALUATION §3](EVALUATION.md#3-independent-assessment)), is a
third thing and establishes neither provenance (P6, P3).

An implementation-derived test can be useful for regression or a stated
local property. Repeating the implementation's decision supplies no
independent justification of its fidelity to an upstream obligation. A
shorter assertion path can be easier to inspect and execute than
construction; that is a supported design claim for the selected path, not
a guarantee of correctness, coverage or independence. Valid distinct
implementations can produce different outputs within the same acceptable
relation; equality of outputs is not always the oracle (P1, P6).

Mutual assurance compares independently justified constructions or
assertions within their stated scope. Agreement is compatible with both
being correct and with a shared error; disagreement requires diagnosis
([ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation))
and does not identify the faulty party by itself. Assurance accounts for
shared specifications, interpretations, tools, fixtures, observations,
copied material and other material failure causes. Different actors,
model families or codebases do not establish statistical independence.
Porting retains authorship and common dependencies (EVALUATION §3 and the
Cross-Synthesis rule of the Product that owns this corpus). Repeating
evidence does not create a new independent observation. Agreement with
an incorrect common model cannot validate that model against the desired
real-world outcome; validation of the governing expectations uses its
declared purpose and external observations through their owners, and
proposed corrections preserve counterexamples and follow the applicable
change authority ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management))
(P4a, P6, P1).

These relationships are recoverable from the existing sources, bindings
and evidence carriers. Shared derivations can be recorded once and applied
to a declared family. No new per-test document, parallel ledger, fixed
number of reviewers or prescribed provenance format is required (P6).

### Quantified assurance

Risk model. The actor exercising the admitted work authority selects the required
assurance for the stated risk, obligations and resource limits. That
selection identifies material failure consequences, coverage and
uncertainty, and the conditions for action or acceptance. Additional
evidence can strengthen a claim only within its applicability and
dependence account; neither a test count nor an assumed preference for more checks
substitutes for that account (P6, P5).

Where quantified assurance is claimed, its model states the population or
uncertainty being modelled, prior information, likelihoods, shared causes
and calibration limits. For a specified violation event V and evidence
event E:

```text
P(V | E, Γ) =
  P(E | V, Γ) P(V | Γ)
  / [P(E | V, Γ) P(V | Γ) + P(E | not V, Γ) P(not V | Γ)].
```

The denominator must be nonzero. E can include agreement, disagreement or other
observations; its likelihood under both faulty and non-faulty conditions
matters. The formula supplies no missing likelihood or prior, and a
numerical posterior is no stronger than its model and evidence.

Let `M_i` mean that check i misses V under the specified evaluation
conditions. The joint miss probability factors exactly by conditional
probabilities:

```text
P(M_1 and ... and M_n | V, Γ)
  = product over i of P(M_i | V, Γ, M_1, ..., M_(i-1)).
```

Conditional terms require defined conditioning events; zero-probability
prefixes are handled without inventing a conditional value. Replacing
those terms with `P(M_i | V, Γ)` requires conditional independence under
the declared model. One minus the joint miss probability is the chance of
at least one detection under those same conditions; it is not the
probability that the whole product is correct. Agreement does not
necessarily increase confidence when shared causes or new information
change the model (P6, P1).

Calibration from sampled cases or injected defects supports only its
justified relationship to operational failures. Unsupported numeric
confidence remains unresolved; qualitative evidence and stated limits
remain usable within the governing policy. No universal probability
threshold is imposed and no probability estimate is required for every
test. Required safety, authority and acceptance conditions cannot be
waived by a cheaper assurance plan (P5, P6).

### Change impact and evidence reuse

Assertion justification and evidence validity are related but distinct
dependency relations. The former explains why a check expresses an
obligation. The latter identifies what can affect the check's behaviour,
conclusion or applicability: implementation, shared libraries, data,
instruments, environments and governing assumptions. A
requirements-to-test link alone is not a complete impact model (P3, P6).

Let Δ be a change to material facts or dependencies, including a newly
discovered invalid assumption. Let `I(Δ)`, the impact cover, conservatively cover the changed
facts and their affected dependents. For each check t, let `D*(t)` cover
the transitive dependencies material to its assertion, execution and use
of evidence. A candidate selection is:

```text
S_Δ = { t : D*(t) intersects I(Δ) }.
```

The representation of these dependencies is the tenant's choice; no
exhaustive graph database is required. Excluding a check requires
supported coverage of its material dependencies and a reason the change
cannot invalidate the intended reused claim; an absent edge is not
evidence of non-influence. Unknown impact widens reassessment or leaves
the dependent assurance unresolved. New obligations or cases create
assessment work even when no existing check covers them. A mandatory
gate, an assessment that the governing policy requires irrespective of
selection ([RELEASE §8](RELEASE.md#8-acceptance)), remains applicable
(P5, P6).

For a new subject and basis, let `E_old` be the existing evidence records,
`E_reassessed` the evidence newly produced by reassessment, and `E_new`
the resulting account. Reassessment includes the checks selected in
`S_Δ`, the assessment of new obligations and the applicable mandatory
gates. Selection alone produces no execution evidence; failed and
indeterminate results retain their standing:

```text
E_new = retain_applicable(E_old, new_subject, new_basis) union E_reassessed.
```

Retention establishes the material validity conditions on the new
subject: the claim and its scope still apply, its assertion and
observation basis remain justified, and the affected dependencies are
unchanged or covered by an established preservation relation. The
original evidence keeps its original subject; a new applicability
relation permits its use. A changed hash alone establishes neither
invalidity nor equivalence. A corrected run is not an unchanged independent
test of the correction: the corrected subject carries its own evidence.
Known failures, unresolved coverage and their
citations remain visible until a supported repair, a reassessment or an
authorised change of obligation disposes of them (P3, P4b, P6).

If a governing requirement changes, dependent expectations may need
authorised revision as well as new execution. A correction in a
refinement revisits the affected obligations and their links to both the
requirement and the realisation. A correction in the realisation
reassesses the affected implementation and integration under the
still-applicable obligations. These are semantic dependency boundaries,
not file or directory boundaries. Recovery reacquires current reality and
invalidates affected claims; it need not erase valid work or rerun every
check ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)) (P3, P6).

The governing assurance can be established from applicable retained
evidence together with new evidence; the completeness of that account is
distinct from the freshness of every execution. Selection considers
impact-analysis, acquisition, execution and assessment costs together,
with anticipated costs distinguished from measurements
([ACTIVATION §6](ACTIVATION.md#6-cost-and-proportionality)). The
required assurance, risk policy and mandatory gates constrain that
optimisation; a cheap selection that leaves a required obligation
uncovered is insufficient. Broad or
uncertain impact, a change to the selection model, an applicable release
rule or evidence that selection missed a dependency can justify wider
testing; full-suite execution remains available and may itself have
coverage gaps. No universal full-suite cadence follows, and no
optimisation removes a separately required gate. Failures enter diagnosis
and an authorised response
([ACTIVATION §1 Feedback and diagnosis](ACTIVATION.md#construction-relation));
the next selected action may acquire evidence before any repair is
justified. [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse)
applies this relation to closed results and handoffs; its three
invalidators are kinds of change Δ, and a closed result is affected when
its `D*(t)` meets `I(Δ)` (P5, P6).

### Formal representation

The candidate's a_c interpretation represents the material obligations
and dependency relationships of these subsections under the
constraint-surface fidelity rule of the Product that owns this corpus,
through [AXIOMATIC_CALCULUS](AXIOMATIC_CALCULUS.md) and the acquired
views that project it. It distinguishes five kinds of support for a statement: a
stated formula, a discharged mathematical argument, mechanically checked
structure, an externally assessed predicate, and evidence from execution.
An external predicate retains the source, scope and evidence required to
establish it; an arbitrary truth label does not discharge the obligation.
No particular proof assistant, probability library or execution engine is
selected (P1, P6).

The candidate demonstrates the applicable positive, negative and
unresolved cases in [CONFORMANCE](CONFORMANCE.md), including weak
assertions, insufficient observations, shared error, and change selection
that either retains valid evidence or invalidates affected evidence.
Mathematical proof, exhaustive checks of a finite model, sampled tests and
observed use retain their distinct scopes. Finite examples do not prove
the universal implications above. An unproved universal claim can remain
unresolved while bounded construction and assurance proceed where their
governing conditions permit them (P5, P6).

The existing member and integrated criteria assess these owners and their
consumers ([EVALUATION §6](EVALUATION.md#6-conformance-of-realisations)).
Source semantics, formal fidelity and actual use retain their separate
evidence; these obligations create no seventh criterion and do not make
each test a theorem-proving exercise (P6).

Purpose and material relation of the assurance relations: they connect
construction results to the obligations they support, expose shared
errors, and direct reassessment to affected claims while retaining
evidence whose applicability is established (P6, P2).
```


### Row `AXIOMATIC_CALCULUS.md#typed-records` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#typed-records` at rc.2:

```text
## Typed Records

The following sections define the exact shapes of the eight core record
families. `SemanticObject`, `TypedRelation`, `Constraint`, `Latitude`, and
`Residual` populate `O`, `E`, `C`, `L`, and `X`. The traversal,
transformation, and judgment records defined below populate `V`, `T`, and `J`.
A traversal, transformation, or judgment is not placed in `O` merely by
reifying its name as a semantic object. A subject model may independently
represent the concept of a record kind, but that representation does not
satisfy the core population law.

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

### Typed Relation

Every relation has exactly:

```text
TypedRelation = {
  id,
  kind,
  source,
  target,
  context,
  owner,
  scope,
  basis,
  qualifiers
}
```

`source` and `target` resolve to members of `I`. `qualifiers` is the closed
kind-specific record declaring direction, cardinality, preservation, loss,
inverse, invalidation, or other relation semantics required by the signature.

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

Successor, `AXIOMATIC_CALCULUS.md#3-typed-records`:

```text
## 3. Typed records

The following subsections define the exact shapes of five of the eight
core record families. `SemanticObject`, `TypedRelation`, `Constraint`,
`Latitude` and `Residual` populate `O`, `E`, `C`, `L` and `X`. The
traversal record (§5), the transformation record (AC-013) and the judgment
record (AC-014) populate `V`, `T` and `J`. A traversal, transformation or
judgment is not placed in `O` merely by reifying its name as a semantic
object. A subject model may independently represent the concept of a
record kind, but that representation does not satisfy the core population
law (P3, P1; rc.2 #typed-records).

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

### Typed relation

Every relation has exactly (P3, P4a; rc.2 #typed-relation):

```text
TypedRelation = {
  id,
  kind,
  source,
  target,
  context,
  owner,
  scope,
  basis,
  qualifiers
}
```

`source` and `target` resolve to members of `I`. `qualifiers` is the
closed kind-specific record declaring direction, cardinality,
preservation, loss, inverse, invalidation or other relation semantics
required by the signature.

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


### Row `AXIOMATIC_CALCULUS.md#typed-relation` (disposition `conserved`)

Predecessor, `AXIOMATIC_CALCULUS.md#typed-relation` at rc.2:

```text
### Typed Relation

Every relation has exactly:

```text
TypedRelation = {
  id,
  kind,
  source,
  target,
  context,
  owner,
  scope,
  basis,
  qualifiers
}
```

`source` and `target` resolve to members of `I`. `qualifiers` is the closed
kind-specific record declaring direction, cardinality, preservation, loss,
inverse, invalidation, or other relation semantics required by the signature.
```

Successor, `AXIOMATIC_CALCULUS.md#typed-relation`:

```text
### Typed relation

Every relation has exactly (P3, P4a; rc.2 #typed-relation):

```text
TypedRelation = {
  id,
  kind,
  source,
  target,
  context,
  owner,
  scope,
  basis,
  qualifiers
}
```

`source` and `target` resolve to members of `I`. `qualifiers` is the
closed kind-specific record declaring direction, cardinality,
preservation, loss, inverse, invalidation or other relation semantics
required by the signature.
```


### Row `DESIGN_MODULE_METHOD.md#12-interface-bleed-prohibition` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#12-interface-bleed-prohibition` at rc.2:

```text
## 12. Interface Bleed Prohibition

No interface should bleed semantic authority into another interface family.

Interface bleed exists when:

- one interface reconstructs another interface's source truth
- projection logic becomes closure logic
- report or prompt logic becomes admission logic
- public wrappers decide kernel semantics
- adapters invent meaning instead of translating boundaries

The required shape is:

- each interface family has one authoritative source truth
- downstream interfaces consume that truth
- crossing an interface boundary does not create a new semantic center

Low coupling requires semantic non-bleed, not only small functions.

---
```

Successor, `DESIGN_MODULE.md#interface-bleed-prohibition`:

```text
### Interface bleed prohibition

No interface should bleed semantic authority into another interface family
(P6; rc.2 #12-interface-bleed-prohibition). Interface bleed exists when one
interface reconstructs another interface's source truth; projection logic
becomes closure logic; report or prompt logic becomes admission logic;
public wrappers decide kernel semantics; or adapters invent meaning instead
of translating boundaries. The required shape: each interface family has
one authoritative source truth; downstream interfaces consume that truth;
crossing an interface boundary does not create a new semantic centre. Low
coupling requires semantic non-bleed, not only small functions.
```


### Row `DESIGN_MODULE_METHOD.md#14-design-review-questions` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#14-design-review-questions` at rc.2:

```text
## 14. Design Review Questions

When reviewing code under this method, ask:

1. Does semantic law live in typed carriers or in orchestration code?
2. Are the main steps readable as transforms over admitted truth?
3. Are effects isolated to explicit edge modules?
4. Can projections or reports invent closure independently?
5. Does each projection/query module derive from an admitted source carrier, or
   can it reconstruct a same-name but structurally different truth surface?
6. Is mutation justified, bounded, and local?
7. Can consumers pattern-match the source carrier directly?
8. Is any proxy or compatibility surface still silently authoritative?
9. Would removing the authoritative carrier make the system fail closed rather
   than silently rebuilding truth?
10. Does each new function project accepted Prime atoms without convenience
    aggregation or rival semantic authority?
11. Does any interface bleed semantic authority into another interface family?
12. For Python, does any governed semantic surface still rely on `Any`, open
    dict payloads, or untyped defs?
13. Has the boundary declared its Irreducible Architectural Carrier Set?
14. Which shapes are Subordinate Payloads, and why are they not staying
    subordinate?
15. Does every promoted top-level type pass the Promotion Test?
16. Has typed closure caused Boundary Inflation by multiplying peer types or
    parallel schema migrations?
17. Does this change avoid increasing truth surfaces, and reduce duplicate truth
    where duplicate truth exists?
18. Is any foreign or open payload still trusted past ingress?
19. Did enforcement follow proof, or is the typing/schema work cosmetic?
20. If this boundary governs another actor, is it publishing state and
    admissible routes, or imperatively prescribing strategy?
21. If a reference realization exists, has the target boundary been derived
    explicitly from reference design to target design to target module assets
    rather than from code drift?
22. Does a module-bounded domain projection exist and accurately show IACS
    carriers, their Prime-atom projection mappings, subordinate payloads,
    visibility, ownership, and deferred families from the accepted Ontology?
23. Do the unit tests derive from module ownership and module assets rather
    than from helper layout or incidental code shape?
24. If the change claims cleanup or optimization, does it stay boundary-local,
    behavior-preserving, and authority-neutral rather than becoming silent
    redesign?
25. If a cross-boundary opportunity was discovered, was it kept out of the
    current change unless the owning authority admitted it at the lawful
    re-entry point?
26. If the same realization pattern has already appeared elsewhere, did review
    make an explicit library/commonization decision rather than allowing
    another silent local rebuild?
27. If this would be the third local rebuild of the same realization pattern,
    is the change design-method conformant because it consumes or extends the
    governing library or records an explicit do-not-commonize decision?
28. If the ticket is making a design-method closure claim, did the bounded
    design check cover the exact claim and applicable hard stops without
    automatically absorbing optional discovery?
29. If the project is ODD-governed, is this module realizing a declared
    outcome traversal rather than substituting for the graph function?
30. Has review checked whether a deterministic module boundary is actually an
    operative edge traversal that should be declared under `ODD_METHOD.md`?
31. Do `F_D` evaluators, deterministic transforms, and effect shells remain
    subordinate to the GTL/ABG graph carrier rather than becoming the hidden
    program?
32. Does the boundary have a lifecycle confirmation against the canonical
    `SPEC_METHOD.md` operational lifecycle chain, or named `Gap:` /
    `Unanswered:` items for unresolved phases?
33. Are release, deployment, live usage, observed telemetry, and retirement
    questions answered by the proper authority surface rather than invented by
    implementation, prompt prose, local convention, or fixtures?
34. If a lifecycle phase is declared not applicable, is the reason explicit and
    compatible with the product and requirement authority?
35. Does the boundary have distinct Mermaid domain, sequence, and state-machine
    views rather than one carrier inventory or broad flowchart?
36. Does every sequence participant exist in the domain model, and does every
    message bind to a declared transform, graph/C constructor, interpreter act,
    or effect boundary?
37. Does every state transition derive from admitted carrier, event, or
    projection truth rather than controller-local memory?
38. Does the axiom matrix evaluate every applicable product, graph, language,
    runtime, handler, and module law with `pass`, `fail`, or reasoned
    `not_applicable`?
39. Is any relied-on graph, batch, retry, recursion, or workflow constructor
    still `semantic_not_realized`, and if so are promotion and closure blocked
    rather than bypassed with imperative glue?
40. Is the proportional sequencing relation justified, and is the design
    verdict explicitly `accepted` before promotion or closure and, where
    design-gated, before retained implementation establishes an unresolved or
    contradictory relation or chooses a materially non-equivalent network?
41. Does one accepted Ontology exist before IACS, public operation, schema,
    module, or implementation promotion?
42. Does the Ontology enumerate entities, identities, relationships,
    invariants, and logical lifecycle completeness without treating mutable CRUD
    as the default?
43. Does every Ontology function or transition declare proposer, evaluator,
    verifier, admitter, executor, projector, and retirement authority as
    applicable, with actor and capability kept distinct from authority?
44. Has every discovered functionality item been derived through an atomic
    function or higher-order composition, explicitly deferred or excluded, or
    assigned to a named gap?
45. Was Prime contraction applied to the complete candidate semantic-atom
    family and all proposed realization projections, with every accepted
    atom's admitted domain recorded, rather than only to functions, carriers,
    or isolated units?
46. Does the boundary declare its composition and effect algebra and prove
    identity, closure, cardinality, effect, and authority conservation where
    applicable?
47. Are the class, sequence, state, IACS, public contract, adapter, code, and
    test surfaces traceable projections of the Ontology with any accepted loss
    declared?
48. Would removing the Ontology reveal ungrounded meaning in a downstream view,
    operation register, controller, or implementation branch?
49. Before constructing a material generic capability or common mechanic, was
    it stated without Product, domain, module, vendor, file, or incumbent labels,
    with declared semantic or authority-bearing relations distinguished from
    generic mechanics?
50. Does bounded discovery record every searched source or category, cutoff
    time and version basis, applicability criteria, exclusions, predecessor or
    incumbent status, and residual unknown, with later material candidates
    invalidating affected selection evidence?
51. Did foundation selection compare credible candidate compositions across
    the decision-relevant lifecycle dimensions without incumbent, source-order,
    local-code, or dependency-count preference?
52. Are hard authority, Product-contract, safety, security, licensing, and
    constructability failures eliminative, while unknown evidence remains
    explicit rather than becoming a favorable score?
53. Does every reused foundation hold only explicitly assigned roles, preserving
    each declared relation's owner, role kind, subject, scope, basis, lifecycle,
    and refusal invariants without authority widening?
54. Is the selected composition undominated under the evidence, and did the
    existing tradeoff owner apply declared priorities and risk tolerances rather
    than asserting an undefined total ordering?
55. Does every rejected material candidate carry decisive evidence or a
    falsifier, while an unresolved frontier remains a gap rather than an
    unsupported preference?
56. Did any newly exposed material generic subproblem recursively re-enter the
    foundation-selection relation before its implementation was retained?

If these questions cannot be answered cleanly, the realization is too coupled
or too imperative.

---
```

Successor, `DESIGN_MODULE.md#design-review-questions`:

```text
### Design review questions

When reviewing code under this profile, ask (P6;
rc.2 #14-design-review-questions):

1. Does semantic law live in typed carriers or in orchestration code?
2. Are the main steps readable as transforms over admitted truth?
3. Are effects isolated to explicit edge modules?
4. Can projections or reports invent closure independently?
5. Does each projection or query module derive from an admitted source
   carrier, or can it reconstruct a same-name but structurally different
   truth surface?
6. Is mutation justified, bounded and local?
7. Can consumers pattern-match the source carrier directly?
8. Is any proxy or compatibility surface still silently authoritative?
9. Would removing the authoritative carrier make the system fail closed
   rather than silently rebuilding truth?
10. Does each new function project accepted Prime atoms without
    convenience aggregation or rival semantic authority?
11. Does any interface bleed semantic authority into another interface
    family?
12. For Python, does any governed semantic surface still rely on `Any`,
    open dictionary payloads or untyped definitions?
13. Has the boundary declared its IACS?
14. Which shapes are Subordinate Payloads, and why are they not staying
    subordinate?
15. Does every promoted top-level type pass the Promotion Test?
16. Has typed closure caused Boundary Inflation by multiplying peer types
    or parallel schema migrations?
17. Does this change avoid increasing truth surfaces, and reduce duplicate
    truth where duplicate truth exists?
18. Is any foreign or open payload still trusted past ingress?
19. Did enforcement follow proof, or is the typing or schema work
    cosmetic?
20. If this boundary governs another actor, is it publishing state and
    admissible routes, or imperatively prescribing strategy?
21. If a reference realisation exists, has the target boundary been
    derived explicitly from reference design to target design to target
    module assets rather than from code drift?
22. Does a module-bounded domain projection exist and accurately show IACS
    carriers, their Prime-atom projection mappings, subordinate payloads,
    visibility, ownership and deferred families from the accepted
    Ontology?
23. Do the unit tests derive from module ownership and module assets
    rather than from helper layout or incidental code shape?
24. If the change claims clean-up or optimisation, does it stay
    boundary-local, behaviour-preserving and authority-neutral rather than
    becoming silent redesign?
25. If a cross-boundary opportunity was discovered, was it kept out of the
    current change unless the owning authority admitted it at the lawful
    re-entry point?
26. If the same realisation pattern has already appeared elsewhere, did
    review make an explicit library or commonisation decision rather than
    allowing another silent local rebuild?
27. If this would be the third local rebuild of the same realisation
    pattern, is the change design-method conformant because it consumes or
    extends the governing library or records an explicit do-not-commonise
    decision?
28. If the ticket is making a design-method closure claim, did the bounded
    design check cover the exact claim and applicable hard stops without
    automatically absorbing optional discovery?
29. If the project is governed by the graph-execution profile, is this
    module realising a declared outcome traversal rather than substituting
    for the graph function?
30. Has review checked whether a deterministic module boundary is actually
    an operative edge traversal that should be declared under the
    graph-execution profile?
31. Do `F_D` evaluators, deterministic transforms and effect shells remain
    subordinate to the GTL and ABG graph carrier rather than becoming the
    hidden program?
32. Does the boundary have a lifecycle confirmation against the canonical
    operational lifecycle chain of SPEC_METHOD §2, or named `Gap:` or
    `Unanswered:` items for unresolved phases?
33. Are release, deployment, live usage, observed telemetry and retirement
    questions answered by the proper authority surface rather than invented
    by implementation, prompt prose, local convention or fixtures?
34. If a lifecycle phase is declared not applicable, is the reason explicit
    and compatible with the product and requirement authority?
35. Does the boundary have distinct Mermaid domain, sequence and
    state-machine views rather than one carrier inventory or broad
    flowchart?
36. Does every sequence participant exist in the domain model, and does
    every message bind to a declared transform, graph or computation
    constructor, interpreter act or effect boundary?
37. Does every state transition derive from admitted carrier, event or
    projection truth rather than controller-local memory?
38. Does the axiom matrix evaluate every applicable product, graph,
    language, runtime, handler and module law with `pass`, `fail` or
    reasoned `not_applicable`?
39. Is any relied-on graph, batch, retry, recursion or workflow
    constructor still `semantic_not_realized`, and if so are promotion and
    closure blocked rather than bypassed with imperative glue?
40. Is the proportional sequencing relation justified, and is the design
    verdict explicitly `accepted` before promotion or closure and, where
    design-gated, before retained implementation establishes an unresolved
    or contradictory relation or chooses a materially non-equivalent
    network?
41. Does one accepted Ontology exist before IACS, public operation, schema,
    module or implementation promotion?
42. Does the Ontology enumerate entities, identities, relationships,
    invariants and logical lifecycle completeness without treating mutable
    CRUD as the default?
43. Does every Ontology function or transition declare proposer,
    evaluator, verifier, admitter, executor, projector and retirement
    authority as applicable, with actor and capability kept distinct from
    authority?
44. Has every discovered functionality item been derived through an atomic
    function or higher-order composition, explicitly deferred or excluded,
    or assigned to a named gap?
45. Was Prime contraction applied to the complete candidate semantic-atom
    family and all proposed realisation projections, with every accepted
    atom's admitted domain recorded, rather than only to functions,
    carriers or isolated units?
46. Does the boundary declare its composition and effect algebra and prove
    identity, closure, cardinality, effect and authority conservation where
    applicable?
47. Are the class, sequence, state, IACS, public contract, adapter, code
    and test surfaces traceable projections of the Ontology with any
    accepted loss declared?
48. Would removing the Ontology reveal ungrounded meaning in a downstream
    view, operation register, controller or implementation branch?
49. Before constructing a material generic capability or common mechanic,
    was it stated without Product, domain, module, vendor, file or
    incumbent labels, with declared semantic or authority-bearing
    relations distinguished from generic mechanics?
50. Does bounded discovery record every searched source or category,
    cutoff time and version basis, applicability criteria, exclusions,
    predecessor or incumbent status, and residual unknown, with later
    material candidates invalidating affected selection evidence?
51. Did foundation selection compare credible candidate compositions
    across the decision-relevant lifecycle dimensions without incumbent,
    source-order, local-code or dependency-count preference?
52. Are hard authority, Product-contract, safety, security, licensing and
    constructability failures eliminative, while unknown evidence remains
    explicit rather than becoming a favourable score?
53. Does every reused foundation hold only explicitly assigned roles,
    preserving each declared relation's owner, role kind, subject, scope,
    basis, lifecycle and refusal invariants without authority widening?
54. Is the selected composition undominated under the evidence, and did
    the existing trade-off owner apply declared priorities and risk
    tolerances rather than asserting an undefined total ordering?
55. Does every rejected material candidate carry decisive evidence or a
    falsifier, while an unresolved frontier remains a gap rather than an
    unsupported preference?
56. Did any newly exposed material generic subproblem recursively re-enter
    the foundation-selection relation before its implementation was
    retained?

If these questions cannot be answered cleanly, the realisation is too
coupled or too imperative (P6, P2).
```


### Row `DESIGN_MODULE_METHOD.md#16-relationship-to-other-method-surfaces` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#16-relationship-to-other-method-surfaces` at rc.2:

```text
## 16. Relationship To Other Method Surfaces

- `SPEC_METHOD.md` governs constitutional process, authority flow, repricing,
  and migration law
- `RELEASE_METHOD.md` governs release-cut, Product, install, qualification, and
  version-line promotion evaluation
- `ODD_METHOD.md` governs graph-native constructive carrier law
- `DESIGN_MODULE_METHOD.md` governs preferred realization structure inside
  implementation and design modules
- `UX_METHOD.md` refines this method for UX surfaces with rendering,
  state-transition, and effect-membrane rules; load it only when the work
  realizes a UX surface

So:

- `SPEC_METHOD.md` answers what is lawful process
- `RELEASE_METHOD.md` answers what is a lawful release, Product, install,
  exact-cut acceptance, and selector-promotion decision
- `ODD_METHOD.md` answers what is lawful graph-native product shape
- `DESIGN_MODULE_METHOD.md` answers what is the preferred implementation design
  discipline when you want Ontology-first derivation, low coupling, no
  interface bleed, and explicit authority and effect management
- `UX_METHOD.md` answers the additional discipline that applies when a module
  realizes a UI surface

For ODD-governed products, `ODD_METHOD.md` decides whether the operative unit is
an outcome traversal, graph function, GTL module, or ABG runtime boundary.
`DESIGN_MODULE_METHOD.md` then governs the deterministic module structure that
realizes, evaluates, adapts, or projects inside that ODD boundary. When that
boundary includes a UX surface, `UX_METHOD.md` adds the render-purity,
reducer-purity, effect-membrane, and AssetSurface-binding rules required for
strong functional consistency between front-end and back-end.

The module lifecycle confirmation rule in this method detects whether the
realization has enough lifecycle signal to be safely built and reviewed. It
does not decide release eligibility, exact-cut acceptance, selector promotion,
install policy, or operational rollout. Those decisions remain governed by
`RELEASE_METHOD.md` and project-owned release, deployment, or operational
surfaces.

---
```

Successor, `DESIGN_MODULE.md#relationship-to-other-members`:

```text
### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law; RELEASE governs release cut, Product, install,
qualification and version-line promotion evaluation; the graph-execution
profile ([ODD](ODD.md)) governs graph-native constructive carrier law; this
profile governs preferred realisation structure inside implementation and
design modules; the UX profile ([UX](UX.md)) refines this profile for UX
surfaces with rendering, state-transition and effect-membrane rules and is
loaded only when the work realises a UX surface (P6;
rc.2 #16-relationship-to-other-method-surfaces). So SPEC_METHOD answers what is
lawful process; RELEASE what is a lawful release, Product, install,
exact-cut acceptance and selector-promotion decision; the graph-execution
profile what is lawful graph-native product shape; this profile what is
the preferred implementation design discipline when you want
Ontology-first derivation, low coupling, no interface bleed, and explicit
authority and effect management; and the UX profile the additional
discipline that applies when a module realises a UI surface.

For products governed by the graph-execution profile, that profile decides
whether the operative unit is an outcome traversal, graph function, GTL
module or ABG runtime boundary; this profile then governs the
deterministic module structure that realises, evaluates, adapts or
projects inside that boundary (§2). When that boundary includes a UX
surface, the UX profile adds the render-purity, reducer-purity,
effect-membrane and AssetSurface-binding rules required for strong
functional consistency between front end and back end (P6).

The module lifecycle confirmation rule (ASSURANCE §16) detects whether the
realisation has enough lifecycle signal to be safely built and reviewed.
It does not decide release eligibility, exact-cut acceptance, selector
promotion, install policy or operational rollout; those remain governed by
RELEASE and project-owned release, deployment or operational surfaces
(P6).
```


### Row `DESIGN_MODULE_METHOD.md#17-non-goals` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#17-non-goals` at rc.2:

```text
## 17. Non-Goals

This method does not require:

- one specific programming language
- elimination of all imperative code
- monadic or category-theory vocabulary
- replacing every exception with a custom algebraic type

It does require that the implementation shape remain readable, modular, and
honest about where meaning lives and where effects happen.

Where a boundary composes higher-order functions or effectful computation, it
does require an explicit composition and effect algebra with its applicable
identity, closure, cardinality, effect, and authority-conservation laws. The
vocabulary is optional; the law is not.
```

Successor, `SPEC_METHOD.md#realisation-shape`:

```text
### Realisation shape

For a realisation boundary that the design profile governs (DESIGN_MODULE,
tier 3, adopted under its own adoption rule), the core rule is: semantic
steps should read as transforms over admitted truth; effects should be
explicit and pushed to the edge. If a reader has to inspect orchestration
code, mutable workspace state, service methods or fallback defaults to
determine what the system means, the design is too imperative and too
coupled (P1, P6; provenance rc.2 DESIGN_MODULE_METHOD #3-core-rule).

Non-goals of that profile (P1, P4a; provenance rc.2
DESIGN_MODULE_METHOD #17-non-goals): it does not require one specific programming language,
elimination of all imperative code, monadic or category-theory vocabulary,
or replacing every exception with a custom algebraic type. It does require
that the implementation shape remain readable, modular and honest about
where meaning lives and where effects happen. Where a boundary composes
higher-order functions or effectful computation, it does require an
explicit composition and effect algebra with its applicable identity,
closure, cardinality, effect and authority-conservation laws (FOUNDATIONS
§4 Composition). The vocabulary is optional; the law is not.
```

Successor, `DESIGN_MODULE.md#non-goals`:

```text
### Non-goals

What this profile does not require (one specific programming language,
elimination of all imperative code, monadic or category-theory vocabulary,
replacing every exception with a custom algebraic type), what it does
require of implementation shape, and the composition and effect algebra
that remains required where a boundary composes higher-order or effectful
computation are stated once in
[SPEC_METHOD §2 Realisation shape](SPEC_METHOD.md#realisation-shape) (P1,
P4a; rc.2 #17-non-goals).
```


### Row `DESIGN_MODULE_METHOD.md#2-essential-carrier-consolidation` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#2-essential-carrier-consolidation` at rc.2:

```text
### 2. Essential Carrier Consolidation

Each change should collapse the slice to the few real identity-bearing carrier
families.

This means:

- declare the Irreducible Architectural Carrier Set first
- keep Subordinate Payloads subordinate by default
- avoid fragment classes, interfaces, or result records created only to satisfy
  typing, serialization, or convenience extraction

Progress here is:

- fewer sharper carrier families
- less duplicate authority
- less boundary inflation

Not:

- one more wrapper layer
- one more branch-local peer type
- one more public record that only mirrors payload detail
```

Successor, `DESIGN_MODULE.md#essential-carrier-consolidation`:

```text
### Essential carrier consolidation

Each change should collapse the slice to the few real identity-bearing
carrier families (P3, P2; rc.2 #2-essential-carrier-consolidation). This
means declaring the IACS first (§6), keeping Subordinate Payloads
subordinate by default, and avoiding fragment classes, interfaces or result
records created only to satisfy typing, serialisation or convenience
extraction. Progress is fewer, sharper carrier families, less duplicate
authority and less boundary inflation; not one more wrapper layer, one more
branch-local peer type, or one more public record that only mirrors
payload detail.
```


### Row `DESIGN_MODULE_METHOD.md#2-position` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#2-position` at rc.2:

```text
## 2. Position

The preferred realization shape is functionally biased.

That means:

- semantic meaning should live in typed carriers and explicit transforms
- imperative coordination should be subordinate to admitted truth
- side effects should be isolated to explicit boundary modules
- mutable shared state should be minimized and justified

This method does **not** require a functional programming language.

It does require a functional design discipline.

A Python, Scala, TypeScript, Kotlin, or Java implementation may all satisfy
this method if they keep semantic law in explicit carriers and transforms rather
than hidden orchestration.

---
```

Successor, `DESIGN_MODULE.md#position`:

```text
### Position

The preferred realisation shape is functionally biased (P1, P6;
rc.2 #2-position). That means semantic meaning should live in typed carriers and
explicit transforms; imperative coordination should be subordinate to
admitted truth; side effects should be isolated to explicit boundary
modules; and mutable shared state should be minimised and justified. The
profile does not require a functional programming language; it does
require a functional design discipline. A Python, Scala, TypeScript,
Kotlin or Java implementation may each satisfy it if it keeps semantic law
in explicit carriers and transforms rather than hidden orchestration.
```


### Row `DESIGN_MODULE_METHOD.md#3-enforcement-after-proof` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#3-enforcement-after-proof` at rc.2:

```text
### 3. Enforcement After Proof

Typing, schemas, validators, contracts, or codecs exist to lock in a seam that
has already been made real.

This means:

- parse, validate, or construct first
- admit and narrow the boundary explicitly
- then use types or schemas to enforce the proved shape

It does **not** mean:

- relabel an open payload and call it closed
- wrap loose data in a typed envelope while keeping the same authority path
- use casts, unchecked assertions, or dynamic mutation as fake closure

This evaluator is language-agnostic.

In one language it may be `mypy --strict`, in another a sealed ADT plus a
schema parser, in another a compiler-enforced sum type plus decoder. The rule
is the same: proof first, enforcement second.
```

Successor, `DESIGN_MODULE.md#enforcement-after-proof`:

```text
### Enforcement after proof

Typing, schemas, validators, contracts and codecs exist to lock in a seam
that has already been made real (P6, P1; rc.2 #3-enforcement-after-proof).
Parse, validate or construct first; admit and narrow the boundary
explicitly; then use types or schemas to enforce the proved shape. It does
not mean relabelling an open payload and calling it closed, wrapping loose
data in a typed envelope while keeping the same authority path, or using
casts, unchecked assertions or dynamic mutation as fake closure. The
evaluator is language-agnostic: in one language it may be `mypy --strict`,
in another a sealed algebraic type plus a schema parser, in another a
compiler-enforced sum type plus decoder. The rule is the same: proof
first, enforcement second.
```


### Row `DESIGN_MODULE_METHOD.md#3b-boundary-closure-evaluators` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#3b-boundary-closure-evaluators` at rc.2:

```text
## 3B. Boundary Closure Evaluators

When this method governs a boundary, each design or implementation change
should be judged against three overriding evaluators.

These are not optional heuristics.

If a change improves local ergonomics, test output, or static-checker output
but fails one of these evaluators, it is not real progress under this method.

### 1. Authority Seam Closure

Each change must not increase the number of truth surfaces.

When duplicate or rival truth surfaces already exist, seam-closure work should
reduce them.

This means:

- one authoritative carrier or contract at each semantic boundary
- no controller-side reconstruction of already-admitted truth
- no downstream surface silently rebuilding source truth from raw artifacts
- no raw or open payload trusted past ingress

The test is:

- if the authoritative carrier were removed, would the system fail closed, or
  would another path silently reconstruct the same meaning?

If meaning survives by reconstruction, the seam is not closed.

For projection and query modules, seam closure also requires source coherence:

- the projection must name the admitted carrier, runtime, event, or source truth
  it derives from
- reconstructed catalog, ownership, route, status, or closure truth must be
  structurally compared against the admitted source carrier before publication
- same-name but different-shape carriers must fail closed unless an explicit
  migration design makes the divergence lawful
- negative tests must cover structural drift, not only missing source truth

### 2. Essential Carrier Consolidation

Each change should collapse the slice to the few real identity-bearing carrier
families.

This means:

- declare the Irreducible Architectural Carrier Set first
- keep Subordinate Payloads subordinate by default
- avoid fragment classes, interfaces, or result records created only to satisfy
  typing, serialization, or convenience extraction

Progress here is:

- fewer sharper carrier families
- less duplicate authority
- less boundary inflation

Not:

- one more wrapper layer
- one more branch-local peer type
- one more public record that only mirrors payload detail

### 3. Enforcement After Proof

Typing, schemas, validators, contracts, or codecs exist to lock in a seam that
has already been made real.

This means:

- parse, validate, or construct first
- admit and narrow the boundary explicitly
- then use types or schemas to enforce the proved shape

It does **not** mean:

- relabel an open payload and call it closed
- wrap loose data in a typed envelope while keeping the same authority path
- use casts, unchecked assertions, or dynamic mutation as fake closure

This evaluator is language-agnostic.

In one language it may be `mypy --strict`, in another a sealed ADT plus a
schema parser, in another a compiler-enforced sum type plus decoder. The rule
is the same: proof first, enforcement second.
```

Successor, `DESIGN_MODULE.md#3-boundary-closure-evaluators`:

```text
## 3. Boundary closure evaluators

When this profile governs a boundary, each design or implementation change
should be judged against three overriding evaluators (P6, P2;
rc.2 #3b-boundary-closure-evaluators). They are not optional heuristics. A
change that improves local ergonomics, test output or static-checker
output but fails one of them is not real progress under this profile.

### Authority seam closure

Each change does not increase the number of truth surfaces; where
duplicate or rival truth surfaces already exist, seam-closure work should
reduce them (P6, P3; rc.2 #1-authority-seam-closure). This means one
authoritative carrier or contract at each semantic boundary; no
controller-side reconstruction of already-admitted truth; no downstream
surface silently rebuilding source truth from raw artifacts; and no raw or
open payload trusted past ingress. The test: if the authoritative carrier
were removed, would the system fail closed, or would another path silently
reconstruct the same meaning? If meaning survives by reconstruction, the
seam is not closed.

For projection and query modules, seam closure also requires source
coherence (P6, P1): the projection names the admitted carrier, runtime,
event or source truth it derives from; reconstructed catalogue, ownership,
route, status or closure truth is structurally compared against the
admitted source carrier before publication; same-name but different-shape
carriers fail closed unless an explicit migration design makes the
divergence lawful; and negative tests cover structural drift, not only
missing source truth.

### Essential carrier consolidation

Each change should collapse the slice to the few real identity-bearing
carrier families (P3, P2; rc.2 #2-essential-carrier-consolidation). This
means declaring the IACS first (§6), keeping Subordinate Payloads
subordinate by default, and avoiding fragment classes, interfaces or result
records created only to satisfy typing, serialisation or convenience
extraction. Progress is fewer, sharper carrier families, less duplicate
authority and less boundary inflation; not one more wrapper layer, one more
branch-local peer type, or one more public record that only mirrors
payload detail.

### Enforcement after proof

Typing, schemas, validators, contracts and codecs exist to lock in a seam
that has already been made real (P6, P1; rc.2 #3-enforcement-after-proof).
Parse, validate or construct first; admit and narrow the boundary
explicitly; then use types or schemas to enforce the proved shape. It does
not mean relabelling an open payload and calling it closed, wrapping loose
data in a typed envelope while keeping the same authority path, or using
casts, unchecked assertions or dynamic mutation as fake closure. The
evaluator is language-agnostic: in one language it may be `mypy --strict`,
in another a sealed algebraic type plus a schema parser, in another a
compiler-enforced sum type plus decoder. The rule is the same: proof
first, enforcement second.

### Ingress collapse

Foreign, dynamic or weakly typed input is lawful only at ingress (P1, P5;
rc.2 #3b-ingress-collapse-rule). Once admitted, it collapses immediately
into local carrier truth before semantic transforms begin. The required
shape: receive foreign input; parse, validate or normalise it once;
construct local admitted carrier truth; consume only that local truth in
semantic kernels. Not lawful seam closure: repeated parsing of the same
loose payload in several modules; `from_dict(...).to_dict()` or equivalent
round-trip ceremony that preserves the same open authority; loaders that
merely relabel stored JSON or map data without validating it; semantic
kernels that continue to inspect open payload fragments directly.
```


### Row `DESIGN_MODULE_METHOD.md#5f-theoretical-framing-for-boundary-law` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#5f-theoretical-framing-for-boundary-law` at rc.2:

```text
## 5F. Theoretical Framing For Boundary Law

This method is operational and stands on its own. It does not require a user to
adopt the world-model domain or accept any empirical ontology program before
using it.

The capitalized `Ontology` in section 4B is the engineering Ontology of one
designed boundary. It does not require adoption of the Constraint-Emergence
Ontology, a world-model theory, or any other metaphysical or empirical claim.

The current world-model work does, however, provide a useful theoretical
framing for why these rules are shaped this way.

`WORLD_MODEL_METHOD.md` treats a Markov object as a candidate
identity-bearing cut: a stable self-bounding pattern whose effective blanket
separates what is load-bearing for identity from what is load-bearing for
context. Under that framing, the engineering problem is not "how do I name more
field groups?" but "what is the smallest lawful boundary that preserves the
thing's identity under variation?"

Read that framing into this method carefully:

- the **Irreducible Architectural Carrier Set** is the software-design analogue
  of the smallest identity-bearing cut
- the **Promotion Test** asks whether a subordinate payload has enough
  independent authority to count as its own boundary rather than as evidence
  carried inside another one
- **Boundary Inflation** is the software-design form of mistaking many sensed
  fragments, attributes, or payload groupings for many real peer objects
- strong typing at the semantic boundary prevents the identity-bearing cut from
  remaining fuzzy, reconstructive, or controller-owned

This is a theoretical justification, not an extra prerequisite.

The rules in this file remain engineering law even where the Markov-object
construct is irrelevant, unavailable, or still only candidate-class. The
theoretical framing sharpens the ask; it does not expand the scope of the
method.
```

Successor, `DESIGN_MODULE.md#8-theoretical-framing`:

```text
## 8. Theoretical framing

This profile is operational and stands on its own. It does not require a
user to adopt the world-model domain or accept any empirical ontology
programme before using it (P1;
rc.2 #5f-theoretical-framing-for-boundary-law). The capitalised Ontology of §5
is the engineering Ontology of one designed boundary; it does not require
adoption of the Constraint-Emergence Ontology, a world-model theory, or
any other metaphysical or empirical claim.

The world-model profile ([WORLD_MODEL](WORLD_MODEL.md)) does provide a useful theoretical
framing for why these rules are shaped this way. It treats a Markov object
as a candidate identity-bearing cut: a stable self-bounding pattern whose
effective blanket separates what is load-bearing for identity from what is
load-bearing for context. Under that framing the engineering problem is
not "how do I name more field groups?" but "what is the smallest lawful
boundary that preserves the thing's identity under variation?" Read into
this profile carefully: the IACS is the software-design analogue of the
smallest identity-bearing cut; the Promotion Test asks whether a
subordinate payload has enough independent authority to count as its own
boundary rather than as evidence carried inside another one; Boundary
Inflation is the software-design form of mistaking many sensed fragments,
attributes or payload groupings for many real peer objects; and strong
typing at the semantic boundary prevents the identity-bearing cut from
remaining fuzzy, reconstructive or controller-owned (P1, P3).

This is a theoretical justification, not an extra prerequisite. The rules
of this profile remain engineering law even where the Markov-object
construct is irrelevant, unavailable or still only candidate-class
(FOUNDATIONS §5). The framing sharpens the ask; it does not expand the
scope of the profile (P1).
```


### Row `DESIGN_MODULE_METHOD.md#6-design-module-taxonomy` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#6-design-module-taxonomy` at rc.2:

```text
## 6. Design Module Taxonomy

When this method governs a realization boundary, modules should be classified by
role.

Recommended roles are:

- **Carrier module**: defines typed immutable inputs, outputs, contracts,
  transitions, records, or envelopes
- **Semantic kernel module**: implements the main transforms over carriers
  without performing side effects
- **Effect shell module**: performs event emission, file publication, network
  calls, subprocess execution, persistence, or operator delivery
- **Projection module**: derives read models or reports from authoritative
  source truth
- **Binding or adapter module**: converts between external boundaries and the
  project's internal carriers without inventing semantic law
- **Constructor or materialization module**: writes generated or built artifacts
  from admitted carriers and explicit plans

The point of the taxonomy is not naming ceremony.

Modules are realization-level tools for bounding graph-traversal reasoning.

The point is to give reviewers, maintainers, and future refactor work a stable
cut for global reasoning without letting semantic law smear across mixed
authority surfaces.

A good module boundary improves the likelihood of correct traversal because the
computation and evaluation surface is better constrained. This is true for any
intermediate traversal of the graph under finite context, attention, and time.
Review can ask what the bounded unit owns, what it consumes, what it emits, and
what proof is sufficient without re-reading the whole system.

That same constrained surface makes later consolidation into reusable libraries
easier. Repeated module-local computations are visible as recurrence candidates
instead of disappearing into broad orchestration code.
```

Successor, `DESIGN_MODULE.md#9-module-taxonomy`:

```text
## 9. Module taxonomy

When this profile governs a realisation boundary, modules should be
classified by role (P0, P6; rc.2 #6-design-module-taxonomy). Recommended
roles are:

- carrier module: defines typed immutable inputs, outputs, contracts,
  transitions, records or envelopes;
- semantic kernel module: implements the main transforms over carriers
  without performing side effects;
- effect shell module: performs event emission, file publication, network
  calls, subprocess execution, persistence or operator delivery;
- projection module: derives read models or reports from authoritative
  source truth;
- binding or adapter module: converts between external boundaries and the
  project's internal carriers without inventing semantic law; and
- constructor or materialisation module: writes generated or built
  artifacts from admitted carriers and explicit plans.

The point of the taxonomy is not naming ceremony. Modules are
realisation-level tools for bounding traversal reasoning: they give
reviewers, maintainers and future refactor work a stable cut for global
reasoning without letting semantic law smear across mixed authority
surfaces. A good module boundary improves the likelihood of correct
traversal because the computation and evaluation surface is better
constrained; this holds for any intermediate traversal under finite
context, attention and time (P0). Review can ask what the bounded unit
owns, what it consumes, what it emits and what proof is sufficient without
re-reading the whole system. The same constrained surface makes later
consolidation into reusable libraries easier: repeated module-local
computations are visible as recurrence candidates instead of disappearing
into broad orchestration code (P2; §10 Recurrence extraction).

The design-to-module evidence route, the module-derived unit-test rule and
the module lifecycle confirmation rule are assurance law, stated in
[ASSURANCE §14](ASSURANCE.md#14-design-to-module-evidence-route),
[§15](ASSURANCE.md#15-module-derived-unit-tests) and
[§16](ASSURANCE.md#16-module-lifecycle-confirmation); for a boundary this
profile governs they read through the binding declared at the head of this
member (P6, P1).
```


### Row `DESIGN_MODULE_METHOD.md#7-immutable-carrier-rule` (disposition `conserved`)

Predecessor, `DESIGN_MODULE_METHOD.md#7-immutable-carrier-rule` at rc.2:

```text
## 7. Immutable Carrier Rule

Source truth should be carried in typed immutable values unless mutation is
materially necessary.

Preferred shape:

- constructor or parser produces a typed carrier
- transforms consume one carrier and return another carrier or a closed result
- projections read those carriers without mutating them

Mutable carrier state requires explicit justification when it is:

- performance-critical
- required by the host runtime or framework
- modeling a genuinely stateful boundary rather than semantic truth

Convenience is not sufficient justification.

---
```

Successor, `DESIGN_MODULE.md#immutable-carriers`:

```text
### Immutable carriers

Source truth should be carried in typed immutable values unless mutation
is materially necessary (P3, P4b; rc.2 #7-immutable-carrier-rule). The
preferred shape: a constructor or parser produces a typed carrier;
transforms consume one carrier and return another carrier or a closed
result; projections read those carriers without mutating them. Mutable
carrier state requires explicit justification when it is
performance-critical, required by the host runtime or framework, or
modelling a genuinely stateful boundary rather than semantic truth.
Convenience is not sufficient justification.
```
