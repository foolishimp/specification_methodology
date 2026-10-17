# I5-03 reading batch 16

Rows: 32. Members: ['TRAVERSAL_OCCURRENCE_PROFILE.md', 'UX_METHOD.md', 'WORLD_MODEL_METHOD.md']. Each row gives the predecessor section at the installed rc.2 (whole, with its subsections) and the successor locus text at the current tree (whole), verbatim.


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation` at rc.2:

```text
## Mutable-Subject Effect Relation

Let `W` be an externally mutable subject bound by stable `SubjectBinding b_W`.
For occurrence `o_n`:

```text
observe(W_n, b_W) -> q_n

F_K[v_n] classifies one traversal application.
op_n is a separately identified domain operation.
g_n is the exact owner-issued grant for op_n over b_W.
inv_n = EffectInvocation(o_n, op_n, executor_n, actor_n, g_n, territory_n, inputs_n)
s_n = EffectSubject(o_n, b_W, q_n, inv_n, op_n, g_n, territory_n, invalidation_n)
j_ready = judge_effect_readiness(s_n)

j_ready.decision = ready
  -> dispatch(inv_n, W_n, b_W)
       -> (W_n_plus_1, disposition_n)

observe(W_n_plus_1, b_W) -> q_n_plus_1
judge(TransitionSubject(o_n, q_n, q_n_plus_1, disposition_n, ...)) -> Judgment
```

Functor kind, traversal, domain operation, executor, actor, grant, and effect
invocation are different coordinates. `F_P`, `F_D`, or `F_H` classification
does not by itself identify, authorize, or execute `op_n`.

No operation is lawful without a matching grant naming the subject binding,
operation kind, and effect territory. Profile construction and occurrence
admission mint no grant.

For invocation `inv_n`, operation instance `op_n`, grant `g_n`, and occurrence
`o_n`, all operation bindings are exact:

```text
inv_n.value.operation_ref = op_n.id
target(operation_of_kind(op_n)) = op_n.value.operation_kind_ref
target(targets_subject(op_n)) = op_n.value.subject_binding_ref
target(authorized_by(inv_n)) = inv_n.value.operation_grant_ref = g_n.id
op_n.value.subject_binding_ref = g_n.value.subject_binding_ref
                             = o_n.value.subject_binding_ref
op_n.value.operation_kind_ref in g_n.value.allowed_operation_kind_refs
op_n.value.operation_contract_ref
  = object(op_n.value.operation_kind_ref).value.operation_contract_ref
op_n.value.effect_territory_ref = inv_n.value.effect_territory_ref
                               = g_n.value.allowed_effect_territory_ref
```

The exact `OperationKind` object therefore closes the grant over both kind and
contract. A grant cannot authorize a same-labelled operation instance carrying
a different contract, target sort, invalidated kind, or unresolved kind ref.

An adopting Product may replace exact territory equality only through an
explicit, authority-owned containment relation in its compatible signature.
Nominal kind equality, a role label, executor access, or broad workspace access
does not satisfy the grant.

The disposition law is closed:

- `no_effect` has no dispatched invocation and records that no domain effect
  was attempted;
- `completed_effect` binds one dispatched invocation, bounded post-observation,
  and sufficient effect evidence;
- `partial_effect` binds one dispatched invocation, bounded post-observation,
  bounded evidence, the `partial_effect` residual and stop, and explicit
  re-entry before any further effect; and
- `refused_effect` binds the refused invocation attempt and `refusal` stop, with
  evidence that no authorized mutation began.

`invokes_effect` exists if and only if a concrete invocation was dispatched.
`unauthorized` or `stale` readiness never dispatches it. The immutable
`EffectInvocation` contains no future disposition; `EffectDisposition` records
the later outcome without rewriting the invocation.

`j_ready` judges the unchanged `EffectSubject` immediately before effect
dispatch under the application's declared currentness and invalidation law. If
the pre-observation or grant has become stale, the effect does not start; the
application re-observes and issues a new readiness subject and judgment or
stops. If an effect has begun and cannot establish complete disposition,
`partial_effect` remains explicit and bounded post-effect observation is
required. This law does not require a lock or transaction implementation.

### OP-005 Mutable Reality Conservation

`W` remains the mutable reality carrier. Observation, evidence, result,
checkpoint, event, projection, cache, or model content may describe `W`; none
replaces it. A later traversal application observes the then-current `W` under
the stable binding when authority is unchanged.

Snapshotting or rollback may be supplied by a separately authorized
application. This profile neither requires nor forbids it and does not infer
rollback from a new occurrence.

### OP-006 Immutable Iteration History

Iteration does not mutate an earlier occurrence. Each traversal reapplication
mints a fresh immutable occurrence over the evolving subject. The admitted
occurrence and event history is therefore append-only even when the external
subject changes repeatedly.
```

Successor, `TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation`:

```text
## Mutable-subject effect relation

Let `W` be an externally mutable subject bound by the stable
`SubjectBinding b_W`. For occurrence `o_n` (P3, P6):

```text
observe(W_n, b_W) -> q_n

F_K[v_n] classifies one traversal application.
op_n is a separately identified domain operation.
g_n is the exact owner-issued grant for op_n over b_W.
inv_n = EffectInvocation(o_n, op_n, executor_n, actor_n, g_n, territory_n, inputs_n)
s_n = EffectSubject(o_n, b_W, q_n, inv_n, op_n, g_n, territory_n, invalidation_n)
j_ready = judge_effect_readiness(s_n)

j_ready.decision = ready
  -> dispatch(inv_n, W_n, b_W)
       -> (W_n_plus_1, disposition_n)

observe(W_n_plus_1, b_W) -> q_n_plus_1
judge(TransitionSubject(o_n, q_n, q_n_plus_1, disposition_n, ...)) -> Judgment
```

Functor kind, traversal, domain operation, executor, actor, grant and
effect invocation are different coordinates. An `F_P`, `F_D` or `F_H`
classification does not by itself identify, authorise or execute `op_n`
(P6, P3).

No operation is lawful without a matching grant that names the subject
binding, the operation kind and the effect territory. Profile construction
and occurrence admission mint no grant (P6).

For invocation `inv_n`, operation instance `op_n`, grant `g_n` and
occurrence `o_n`, every operation binding is exact (P6, P3):

```text
inv_n.value.operation_ref = op_n.id
target(operation_of_kind(op_n)) = op_n.value.operation_kind_ref
target(targets_subject(op_n)) = op_n.value.subject_binding_ref
target(authorized_by(inv_n)) = inv_n.value.operation_grant_ref = g_n.id
op_n.value.subject_binding_ref = g_n.value.subject_binding_ref
                             = o_n.value.subject_binding_ref
op_n.value.operation_kind_ref in g_n.value.allowed_operation_kind_refs
op_n.value.operation_contract_ref
  = object(op_n.value.operation_kind_ref).value.operation_contract_ref
op_n.value.effect_territory_ref = inv_n.value.effect_territory_ref
                               = g_n.value.allowed_effect_territory_ref
```

The exact `OperationKind` object therefore closes the grant over both kind
and contract. A grant cannot authorise an operation instance that carries
the same label with a different contract, target sort, invalidated kind or
unresolved kind ref (P6, P3).

An adopting Product may replace exact territory equality only through an
explicit, authority-owned containment relation in its compatible
signature. Nominal kind equality, a role label, executor access or broad
workspace access does not satisfy the grant (P6, P1).

The disposition law is closed (P5, P6):

- `no_effect` has no dispatched invocation and records that no domain
  effect was attempted;
- `completed_effect` binds one dispatched invocation, a bounded
  post-observation and sufficient effect evidence;
- `partial_effect` binds one dispatched invocation, a bounded
  post-observation, bounded evidence, the `partial_effect` residual and
  stop, and explicit re-entry before any further effect; and
- `refused_effect` binds the refused invocation attempt and the `refusal`
  stop, with evidence that no authorised mutation began.

`invokes_effect` exists if and only if a concrete invocation was
dispatched; `unauthorized` or `stale` readiness never dispatches it. The
immutable `EffectInvocation` contains no future disposition, and
`EffectDisposition` records the later outcome without rewriting the
invocation (P3, P6).

Mapping of the dispositions to the core, new in this corpus. Purpose:
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) places the results of
effects in the core. Material relation: whether an occurrence's effect
may be repeated or relied on, which is the material relation of
[ACTIVATION §3 Effects](ACTIVATION.md#effects) (P5, P6). An occurrence
intends an effect when an `EffectInvocation` names it. For such an
occurrence the disposition refines ACTIVATION §3 Effects and maps for its
predicate, "the intended effect occurred"; the causes of the two
`partial_effect` values are those stated under
[Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds):

| Disposition | Effects value | Core value | Ground |
|---|---|---|---|
| `completed_effect` | `completed` | satisfied | the bounded post-observation and sufficient effect evidence establish that the intended effect occurred and that the effect has ended |
| `partial_effect(not_attained)` | `not_effected` | falsified | the admitted evidence establishes that the intended outcome is not attained and that no later completion of the effect can attain it; the part that did occur is named with the value, and an end of the effect that the evidence does not establish is recorded beside it, not in it |
| `partial_effect(undecided)` | `completion_unknown` | indeterminate | the evidence cannot decide whether the intended outcome is or will be reached |
| `refused_effect` | `not_effected` | falsified | the evidence shows that no authorised mutation began |
| `no_effect` | `not_effected` | falsified | the admitted disposition records that no invocation was dispatched, and the record is exact because `invokes_effect` exists if and only if one was; so the occurrence effected nothing on the subject |

An occurrence that no `EffectInvocation` names intends no effect.
ACTIVATION §3 Effects poses no predicate for it, and its `no_effect`
records only that no domain effect was attempted: it is a record, not an
effect result (P5, P6).

`j_ready` judges the unchanged `EffectSubject` immediately before effect
dispatch under the application's declared currentness and invalidation
law. If the pre-observation or the grant has become stale, the effect does
not start; the application re-observes and issues a new readiness subject
and judgment, or stops. If an effect has begun and cannot establish a
complete disposition, `partial_effect` stays explicit and a bounded
post-effect observation is required. This law requires no lock or
transaction implementation (P5, P6).

### OP-005 Mutable reality conservation

`W` remains the carrier of mutable reality. Observation, evidence, result,
checkpoint, event, projection, cache or model content may describe `W`;
none replaces it. A later traversal application observes the then-current
`W` under the stable binding when authority is unchanged (P3, P0).

Snapshotting or rollback may be supplied by a separately authorised
application. This profile neither requires nor forbids it and does not
infer rollback from a new occurrence (P6).

### OP-006 Immutable iteration history

Iteration does not mutate an earlier occurrence. Each traversal
reapplication mints a fresh immutable occurrence over the evolving
subject, so the admitted occurrence and event history is append-only even
when the external subject changes repeatedly (P3, P4b).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#occurrence-identity` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#occurrence-identity` at rc.2:

```text
## Occurrence Identity

One occurrence identity binds only facts available before that occurrence is
admitted:

```text
id(o_n) binds (
  exact traversal-occurrence-profile basis,
  application identity,
  traversal identity,
  functor-kind identity,
  subject-binding identity,
  intended-outcome identity,
  declared lineage inputs,
  declared identity-dependency inputs
)
```

Post-effect observations, effect evidence, judgments, admitted events,
timestamps, admission ordinals, and projection results do not enter the seed.
They may point to the occurrence after their own identities exist.

`application identity` is the exact pre-existing `TraversalApplication`
identity. Its traversal and functor-kind fields equal the occurrence fields.
`declared lineage inputs` and `declared identity-dependency inputs` are the
exact source and target populations stated by the relation-congruence law.
The relation records are minted only after the occurrence identity exists and
therefore do not enter the seed; their endpoints must reproduce it exactly.

Two applications of one traversal over one subject are two occurrences. A
retry or continuation creates a fresh occurrence only when it reapplies the
traversal. A controller step, observation, wait, or correlation record does not
become an occurrence merely because it happens later.

For composition, every retained bracketed traversal application under AC-016
has its own occurrence. If a declared composite traversal is itself applied,
it also has one aggregate occurrence. Each component application relates to
that aggregate through `component_of_occurrence`; that relation is not material
cause by implication. Intermediate results, judgments, evidence, authority,
provenance, and stops required by AC-016 remain explicit.

### OP-001 Seed Acyclicity

The directed graph formed by `identity_depends_on` is finite and acyclic.
Every dependency target exists before the dependent identity is minted. A
future result or event cannot be smuggled into its own occurrence seed.
```

Successor, `TRAVERSAL_OCCURRENCE.md#occurrence-identity`:

```text
## Occurrence identity

One occurrence identity binds only facts available before that occurrence
is admitted (P3):

```text
id(o_n) binds (
  exact traversal-occurrence-profile basis,
  application identity,
  traversal identity,
  functor-kind identity,
  subject-binding identity,
  intended-outcome identity,
  declared lineage inputs,
  declared identity-dependency inputs
)
```

Post-effect observations, effect evidence, judgments, admitted events,
timestamps, admission ordinals and projection results stay out of the
seed. They may point to the occurrence once their own identities exist
(P3, P4b).

`application identity` is the exact pre-existing `TraversalApplication`
identity, whose traversal and functor-kind fields equal the occurrence's.
`declared lineage inputs` and `declared identity-dependency inputs` are the
exact source and target populations that the relation-congruence law
states. The relation records are minted only after the occurrence identity
exists, so they do not enter the seed; their endpoints must reproduce it
exactly (P3).

Two applications of one traversal over one subject are two occurrences. A
retry or a continuation creates a fresh occurrence only when it reapplies
the traversal. A controller step, an observation, a wait or a correlation
record does not become an occurrence merely because it happens later (P3).

Under composition, every retained bracketed traversal application under
AC-016 has its own occurrence. A declared composite traversal that is
itself applied also has one aggregate occurrence. Each component
application relates to that aggregate through `component_of_occurrence`,
which is not material cause by implication. The intermediate results,
judgments, evidence, authority, provenance and stops that AC-016 requires
stay explicit (P4a, P4b).

### OP-001 Seed acyclicity

The directed graph formed by `identity_depends_on` is finite and acyclic.
Every dependency target exists before the dependent identity is minted. A
future result or event cannot be smuggled into its own occurrence seed
(P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#op-001-seed-acyclicity` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#op-001-seed-acyclicity` at rc.2:

```text
### OP-001 Seed Acyclicity

The directed graph formed by `identity_depends_on` is finite and acyclic.
Every dependency target exists before the dependent identity is minted. A
future result or event cannot be smuggled into its own occurrence seed.
```

Successor, `TRAVERSAL_OCCURRENCE.md#op-001-seed-acyclicity`:

```text
### OP-001 Seed acyclicity

The directed graph formed by `identity_depends_on` is finite and acyclic.
Every dependency target exists before the dependent identity is minted. A
future result or event cannot be smuggled into its own occurrence seed
(P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#op-002-atomic-semantic-admission` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#op-002-atomic-semantic-admission` at rc.2:

```text
### OP-002 Atomic Semantic Admission

For a relation claim, one admitted semantic cut contains the unchanged claim,
its admission judgment, the event and its scope/admission judgment, the
deterministic materialized relation, the exact source frontier, and the unique
successor frontier. The source frontier named by the claim, event, and cut is
identical. The successor equals that frontier plus exactly the admitted event.
Missing, conflicting, or inconsistent members refuse the cut. This is semantic
atomicity; the profile does not prescribe a storage or transaction mechanism.
```

Successor, `TRAVERSAL_OCCURRENCE.md#op-002-atomic-semantic-admission`:

```text
### OP-002 Atomic semantic admission

For a relation claim, one admitted semantic cut contains the unchanged
claim, its admission judgment, the event and its scope and admission
judgment, the deterministic materialised relation, the exact source
frontier, and the unique successor frontier. The source frontier that the
claim, the event and the cut name is one identical frontier, and the
successor equals that frontier plus exactly the admitted event. Missing,
conflicting or inconsistent members refuse the cut. This atomicity is
semantic; the profile prescribes no storage or transaction mechanism (P3,
P4b, P6).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#op-004-precedence-is-not-authority` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#op-004-precedence-is-not-authority` at rc.2:

```text
### OP-004 Precedence Is Not Authority

A projection may use a declared precedence coordinate to select current truth.
The coordinate, comparison law, basis, and admitting authority are explicit.
The coordinate orders eligible facts; it does not gain semantic, admission,
causal, or decision authority.
```

Successor, `TRAVERSAL_OCCURRENCE.md#op-004-precedence-is-not-authority`:

```text
### OP-004 Precedence is not authority

A projection may use a declared precedence coordinate to select current
truth. The coordinate, its comparison law, its basis and its admitting
authority are explicit. The coordinate orders eligible facts; it gains no
semantic, admission, causal or decision authority (P6, P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#op-005-mutable-reality-conservation` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#op-005-mutable-reality-conservation` at rc.2:

```text
### OP-005 Mutable Reality Conservation

`W` remains the mutable reality carrier. Observation, evidence, result,
checkpoint, event, projection, cache, or model content may describe `W`; none
replaces it. A later traversal application observes the then-current `W` under
the stable binding when authority is unchanged.

Snapshotting or rollback may be supplied by a separately authorized
application. This profile neither requires nor forbids it and does not infer
rollback from a new occurrence.
```

Successor, `TRAVERSAL_OCCURRENCE.md#op-005-mutable-reality-conservation`:

```text
### OP-005 Mutable reality conservation

`W` remains the carrier of mutable reality. Observation, evidence, result,
checkpoint, event, projection, cache or model content may describe `W`;
none replaces it. A later traversal application observes the then-current
`W` under the stable binding when authority is unchanged (P3, P0).

Snapshotting or rollback may be supplied by a separately authorised
application. This profile neither requires nor forbids it and does not
infer rollback from a new occurrence (P6).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#op-006-immutable-iteration-history` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#op-006-immutable-iteration-history` at rc.2:

```text
### OP-006 Immutable Iteration History

Iteration does not mutate an earlier occurrence. Each traversal reapplication
mints a fresh immutable occurrence over the evolving subject. The admitted
occurrence and event history is therefore append-only even when the external
subject changes repeatedly.
```

Successor, `TRAVERSAL_OCCURRENCE.md#op-006-immutable-iteration-history`:

```text
### OP-006 Immutable iteration history

Iteration does not mutate an earlier occurrence. Each traversal
reapplication mints a fresh immutable occurrence over the evolving
subject, so the admitted occurrence and event history is append-only even
when the external subject changes repeatedly (P3, P4b).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#op-007-scope-conservation` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#op-007-scope-conservation` at rc.2:

```text
### OP-007 Scope Conservation

Every event carries its declared scope class. `event_for` is present only when
the scope law names one exact occurrence. Subject-wide, publication-wide, or
otherwise occurrence-independent facts remain independent.
```

Successor, `TRAVERSAL_OCCURRENCE.md#op-007-scope-conservation`:

```text
### OP-007 Scope conservation

Every event carries its declared scope class. `event_for` is present only
when the scope law names one exact occurrence. Facts that are
subject-wide, publication-wide or otherwise independent of any occurrence
stay independent (P3).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#position` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#position` at rc.2:

```text
## Position

The **Traversal Occurrence Profile** defines an application-neutral
model-family signature for immutable application histories over an externally
mutable subject.

Its stable concept identity is:

```text
urn:stdo:concept:traversal-occurrence-profile
```

This standard owns that concept in bounded context:

```text
urn:stdo:bounded-context:traversal-occurrence-profile
```

Adoption of the profile is optional. The profile imports one exact `a_c` basis
and instantiates one closed model-family signature under its record and model
laws. It does not amend `a_c`, become part of every `a_c` model, or define a
universal execution theory.

Availability is not adoption. A Product that adopts the profile owns its
subject interpretation, concrete vocabulary, authorities, requirements,
design, implementation, and evidence. This standard imports none of those
consumer identities.
```

Successor, `TRAVERSAL_OCCURRENCE.md#position`:

```text
## Position

The traversal occurrence profile defines an application-neutral
model-family signature for immutable application histories over a subject
that changes outside the model. Its stable concept identity is (P3):

```text
urn:stdo:concept:traversal-occurrence-profile
```

This member owns that concept in the bounded context (P1, P3):

```text
urn:stdo:bounded-context:traversal-occurrence-profile
```

Adoption is optional. The profile imports one exact `a_c` basis and
instantiates one closed model-family signature under that basis's record
and model laws. It does not amend `a_c`, does not become part of every
`a_c` model and defines no universal execution theory (P1, P6).

Availability is not adoption. A Product that adopts the profile owns its
subject interpretation, concrete vocabulary, authorities, requirements,
design, implementation and evidence; this member imports none of those
consumer identities (P6, P1).

### Foundation to law

This member is material family F19, traversal occurrence. The table below
shows which of its rules follow from which premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. The family imports
two families under [PROFILES §1](PROFILES.md#1-the-boundary): F3, results
and their combination ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)),
and F9, the `a_c` calculus ([AXIOMATIC_CALCULUS §1](AXIOMATIC_CALCULUS.md#1-position)).
Its instance premises hold where a Product adopts the profile; they are
adopted with it and do not follow from the foundations (P1, P6):

- I1: a subject's reality changes outside the model, and a stable binding
  names that subject;
- I2: the adopting Product selects one exact `a_c` basis;
- I3: an effect on the subject is a separately identified operation under
  an owner-issued grant.

Standing of the commitments cited: P0 recovered; P1, P3 and P6
independent; P4b derived from P0 and P2, and P5 derived from P0 and P6
([FOUNDATIONS §3](FOUNDATIONS.md#3-commitments)).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent); F9 imported; I2 | By P3 a value binds one exact basis, and I2 selects one exact `a_c` basis, so an occurrence model is an ordinary `a_c` model on that basis. The profile adds sorts and value domains but no record kind, because a new record kind would be a second calculus beside F9. With closed populations, an unknown, missing or mistyped element is detected and refused, not read | [Imported calculus boundary](#imported-calculus-boundary); [Closed semantic-object sorts](#closed-semantic-object-sorts), [Finite reference-domain table](#finite-reference-domain-table), [Closed event-kind population](#closed-event-kind-population), [Closed relation families](#closed-relation-families); [Exact profile identity](#exact-profile-identity) | closing the sorts, reference domains, event kinds, relation families and qualifier domains, and their members: a policy of this member, chosen so that refusal of an unknown element is decidable | 2, 3, 10 |
| P3 (independent); P4b (derived from P0 and P2); I1 | By P3 an identity binds its exact inputs, so a traversal applied again to any changed input is a different occurrence; by P4b an established fact is not erased. So each application is one immutable occurrence, a reapplication mints a new one, and a correction appends without erasing | [Occurrence identity](#occurrence-identity), [OP-003](#op-003-correction-without-erasure), [OP-006](#op-006-immutable-iteration-history) | the identity inputs of an occurrence: this member | 2, 9 |
| P0 (recovered); P3 (independent); I1 | By I1 the subject's reality changes outside the model, and by P0 an actor holds only finite observations of it, so an observation, event or projection describes the subject and replaces none of it; the external subject stays the carrier of its reality | [OP-005](#op-005-mutable-reality-conservation) | whether snapshot or rollback exists: a separately authorised application of the adopting Product | 2, 6 |
| P6 (independent); I3 | By P6 authority exists only through an admitted grant, and by I3 an effect is a separately identified operation under such a grant, so no operation is lawful without a matching grant, and functor kind, traversal, operation, executor, actor, grant and invocation stay distinct coordinates | [Mutable-subject effect relation](#mutable-subject-effect-relation) | a territory containment relation in place of exact equality: the adopting Product, in its compatible signature | 4, 8, 9 |
| P1 (independent); P6 (independent) | By P1 a representation does not carry its meaning, and by P6 evaluation, admission and decision are separate authorities, so a candidate, its judgment, its admitting event and the materialised relation stay distinct; precedence orders admitted facts and decides no authority | [Candidate, judgment, event and relation separation](#candidate-judgment-event-and-relation-separation), [OP-004](#op-004-precedence-is-not-authority) | the precedence law, evaluators and authorities of an application: the adopting Product | 2, 9 |
| P3 (independent); P6 (independent) | By P3 a relation holds only on its declared basis, and by P6 only an authority admits it, so cause is admitted typed lineage and is never inferred from time, order, adjacency, containment or correlation | [Causality and typed lineage](#causality-and-typed-lineage), [OP-001](#op-001-seed-acyclicity) | which causal claims an application admits: the adopting Product, under its authorities; that each identity or causal subgraph is acyclic: a policy of this member, chosen so that every lineage walk ends at a first cause | 2, 9 |
| P3 (independent); P4b (derived from P0 and P2); P5 (derived from P0 and P6) | By P3 a projection binds its exact inputs, and by P4b admitted events persist, so a projection binds one complete event frontier, and a new event makes a new frontier rather than advancing an old projection; for the same reason the members of one admitted semantic cut name one identical source frontier, its successor is that frontier plus exactly the admitted event, and a cut with missing or inconsistent members refuses; by P5 a projection is not read beyond the frontier it binds | [Event frontier and projection](#event-frontier-and-projection), [OP-002](#op-002-atomic-semantic-admission), [OP-007](#op-007-scope-conservation) | the event scope and frontier laws: the adopting Product | 2, 6, 9 |
| P5 (derived from P0 and P6); F3 and F9 imported | By P5 a value decides only what its evidence establishes, and F3 gives one core, so every judgment decision and stop, and every effect disposition of an occurrence that intends an effect, maps to exactly one core value for a named predicate; an effect whose outcome the evidence cannot decide stays indeterminate, an established non-attainment of its intended outcome is falsified whether or not its end is established, and no refusal maps to success | [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), [Mutable-subject effect relation](#mutable-subject-effect-relation) | the decision, stop and residual vocabularies and their mapping, and the exclusion of `out_of_frame` from the constraint value set: this member; the meanings and core values of `hold`, `gap` and the two `refusal` values, and the cause of each refusal: [AXIOMATIC_CALCULUS AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal); a refinement of those four values by cause for one traversal, each refined value keeping its parent's core value: that traversal record, under [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds) | 3, 9, 10 |
| P6 (independent) | By P6 authority exists only through an admitted grant, and inclusion in a method cut is no grant, so availability is not adoption, and the profile grants no authority | [Authority and adoption](#authority-and-adoption) | who adopts: Product authority, under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the subject interpretation, vocabulary mappings and authorities an adoption declares: the adopting Product | 1, 7, 9 |

The Scope, the Exclusions and the Conformance obligations apply these
consequences, and every clause names the principle that requires it
([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)). The table is
new in this corpus. Purpose and material relation: an actor started on
this member sees which rules follow from the foundations and which are
choices, and who owns each choice, so no choice is presented as derived
(P6, P1).

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the imported calculus boundary and the closed populations: [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), where a defect against any of the five closed populations refuses as a falsified structural constraint and a basis mismatch at model validation or structural admission carries `refuse_invalid_basis`; [Exclusions](#exclusions), under which the profile is no change to pure `a_c`; [Conformance obligations](#conformance-obligations), items 1, 2, 9 and 21.
- Row 2, occurrence identity, correction without erasure and immutable iteration history: [Closed relation families](#closed-relation-families), whose `application_of` target equals the exact application seed and whose `corrects_event` does not erase its target; [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), constraint `occurrence_seed_complete` and judgment `occurrence_admission`, where a missing seed retains `hold`; [Conformance obligations](#conformance-obligations), items 3, 14 and 15, and item 18 for correction selection.
- Row 3, mutable reality conservation: [Scope](#scope), whose closing paragraph defines no state store or rollback mechanism; [Conformance obligations](#conformance-obligations), item 13; otherwise no separate consumer applies, because whether snapshot or rollback exists is a separately authorised application of the adopting Product, as the choice column states.
- Row 4, the effect relation and its grant: [Closed relation families](#closed-relation-families), whose `invokes_effect` requires an exact operation grant and whose `authorized_by` checks the grant against operation kind, target and territory; [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), constraints `pre_effect_current` and `operation_grant_contains_effect` and judgment `effect_readiness`, whose `unauthorized` or `stale` value never dispatches an effect; [Conformance obligations](#conformance-obligations), items 10, 11 and 16.
- Row 5, candidate, judgment, event and relation separation, and precedence: [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), judgments `claim_admission`, `event_admission` and `semantic_cut_admission` with constraint `relation_claim_admissible`, and the refusal cause of a cross-basis required edge; [Exclusions](#exclusions), under which the profile is no admission, evaluation or decision authority; [Conformance obligations](#conformance-obligations), items 4, 5 and 6.
- Row 6, causality, typed lineage and seed acyclicity: [Closed relation families](#closed-relation-families), whose `identity_depends_on`, `causally_precedes_occurrence` and `causally_precedes_event` are acyclic and carry only admitted material cause; [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), constraints `identity_dependency_acyclic`, `occurrence_causation_acyclic` and `event_causation_acyclic` and residual `unresolved_cause`; [Exclusions](#exclusions), under which the profile claims no acyclicity for every typed lineage graph; [Conformance obligations](#conformance-obligations), items 3, 7, 8 and 19.
- Row 7, event frontier, projection, atomic semantic admission and scope conservation: [Closed relation families](#closed-relation-families), whose `event_for` is permitted only by the event's declared scope law, whose `frontier_contains` is complete membership under one exact frontier basis and whose `projects_frontier` binds exactly one unchanged frontier; [Closed constraint, judgment, residual and stop kinds](#closed-constraint-judgment-residual-and-stop-kinds), constraints `semantic_cut_complete`, `event_scope_compatible` and `frontier_complete`, judgment `frontier_projection` and residuals `unresolved_scope`, `competing_lineage` and `stale_frontier`; [Exclusions](#exclusions), under which the profile is no event store or projection implementation and no guarantee that every framework event belongs to an occurrence; [Conformance obligations](#conformance-obligations), items 9, 17 and 18.
- Row 8, the closed kinds and the effect dispositions in the core: [Conformance obligations](#conformance-obligations), item 12; otherwise no separate consumer applies. The mapped values are returned by the judgments, stops and dispositions that this row's sections close, and the core they map to is [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), which owns it and applies no rule of this row.
- Row 9, authority and adoption: [Conformance obligations](#conformance-obligations), item 20, and its closing paragraph, under which a representative example or checker becomes no occurrence engine or semantic authority; [Exclusions](#exclusions), under which the profile is no mandatory profile and no mutation, admission, evaluation or decision authority. No section of another member applies a rule of this profile; an adopting Product does, under the declarations this section lists, and its adoption is Product authority's under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis), as the choice column states, which names every available profile and applies no rule of this section.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `TRAVERSAL_OCCURRENCE_PROFILE.md#scope` (disposition `conserved`)

Predecessor, `TRAVERSAL_OCCURRENCE_PROFILE.md#scope` at rc.2:

```text
## Scope

The profile represents:

- one immutable occurrence for one exact traversal application;
- a stable binding to an external subject whose reality may change;
- bounded pre-effect and post-effect observations;
- intended typed outcomes;
- separately authorized effect operations and their evidence;
- immutable admitted framework-event facts;
- candidate claims, judgments, and materialized typed relations;
- explicit event frontiers and frontier-bound projections; and
- distinct identity dependency, causal subgraphs, and wider typed lineage.

It does not define a process scheduler, event-log carrier, state store,
workspace format, rollback mechanism, actor topology, or prospective Reference
Frame profile.
```

Successor, `TRAVERSAL_OCCURRENCE.md#scope`:

```text
## Scope

The profile represents (P3, P4b):

- one immutable occurrence for one exact traversal application;
- a stable binding to an external subject whose reality may change;
- bounded pre-effect and post-effect observations;
- intended typed outcomes;
- separately authorised effect operations and their evidence;
- immutable admitted framework-event facts;
- candidate claims, judgments and materialised typed relations;
- explicit event frontiers and projections bound to a frontier; and
- distinct identity dependency, causal subgraphs and wider typed lineage.

It defines no process scheduler, event-log carrier, state store, workspace
format, rollback mechanism, actor topology or prospective reference-frame
profile (P6, P0).
```


### Row `UX_METHOD.md#1-position` (disposition `conserved`)

Predecessor, `UX_METHOD.md#1-position` at rc.2:

```text
## 1. Position

`UX_METHOD.md` exists to make one instruction precise:

`using UX_METHOD, build this UI surface`

The method adopts the **Elm Architecture (TEA)** as its constitutional process model:

- the view is a pure projection of typed state
- state transitions are pure reductions over typed messages
- side effects are values described by the reducer and interpreted at a declared effect membrane
- the runtime owns lifecycle; the view does not own continuation

The view is not a state owner.

Stateful local mutation in views, two-way bindings without action emission, and effect-handlers-as-controllers are method violations even when they are conventionally accepted in the surrounding ecosystem.

### 1A. Constitutional Authority Rule

When a product, ticket, design module, or review adopts this method for a UX
surface, `UX_METHOD.md` is the sole UX realization authority for that surface.

Project-local ADRs may choose the stack. They may not weaken the process model.

Existing code, component-library convention, screenshots, comments, design
history, prototype behavior, and generated artifacts are evidence only. They do
not override this method.

If this method appears ambiguous in a concrete case, the surface fails closed:
the work must either satisfy the stricter interpretation, reprice through the
governing constitutional method, or record a scoped exemption in the design
module before implementation proceeds.

---
```

Successor, `UX.md#1-position`:

```text
## 1. Position

This profile exists to make one instruction precise: "using the UX
profile, build this UI surface" (P2; rc.2 #1-position). It adopts the Elm
Architecture (TEA) as its constitutional process model: the view is a
pure projection of typed state; state transitions are pure reductions
over typed messages; side effects are values the reducer describes and a
declared effect membrane interprets; the runtime owns lifecycle and the
view does not own continuation (P0, P1). The view is not a state owner.
Stateful local mutation in views, two-way bindings without action
emission, and effect handlers used as controllers are violations of this
profile even when the surrounding ecosystem conventionally accepts them
(P6).

### Authority

When Product authority adopts this profile for a UX surface
([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)),
recording the adoption in a product definition, ticket, design module or
review, this profile is the sole UX realisation authority for that
surface (P6; rc.2 #1a-constitutional-authority-rule). Project-local ADRs
may choose the stack; they may not weaken the process model. Existing
code, component-library convention, screenshots, comments, design
history, prototype behaviour and generated artifacts are evidence only
and do not override this profile (P6). If this profile appears ambiguous
in a concrete case, the surface fails closed under SPEC_METHOD §5: the
work either satisfies the stricter interpretation, reprices through the
governing constitutional method, or records a scoped exemption in the
design module before implementation proceeds (P5, P6; §15 states the
result). Each exit is an outcome of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome):
satisfying the stricter interpretation is `resolved`, under this
profile's fail-closed policy; repricing is `escalated` to the owner of the
governing surface; a scoped exemption is `carried`, the exemption being
its recorded residual; until one of them is taken, the ambiguity is
`blocked` and implementation does not proceed.

### Foundation to law

This member is material family F20, UX. The table below shows which of
its rules follow from which premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. The family imports
five families under [PROFILES §1](PROFILES.md#1-the-boundary): F2,
transitions, steps and configuration
([ACTIVATION §1](ACTIVATION.md#1-the-step)); F3, results and their
combination ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)); F4,
work state, resumption and reuse
([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)); F11, change
management and ambiguity
([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); and F13, work
carriers ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution)). It
refines the software-design profile, family F17
([DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position)), for
modules that realise a UX surface (§2); where a row's rule refines a
DESIGN_MODULE rule, its choice column names that rule. Its instance
premises hold where a UX surface is realised under this profile; they are
adopted with it and do not follow from the foundations (P1, P6):

- I1: a product exposes UX surfaces, through which people and systems
  observe the product's admitted truth and request changes to it;
- I2: the product's design, outside the UX layer, declares the admitted
  truth and the carriers that change it;
- I3: UI stacks differ by project, and their ecosystems accept patterns
  that keep state, continuation or effects in the view;
- I4: data reaches a UX surface across seams that the surface does not
  control;
- I5: UX work iterates in short cycles, in which proof for each change
  can cost more than the expected correction.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 (independent), P1 (independent); F2 imported ([ACTIVATION §1](ACTIVATION.md#1-the-step)), F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); I1, I2 | By P6 a change to product truth needs an admitted authority, and by I2 the product's design declares the carriers that change it, so a UX surface renders admitted truth and changes it only through an admitted carrier, and the UX layer never becomes the hidden constructive carrier; by P1 a control's appearance carries no authority, so where no carrier exists the surface is blocked and the work re-enters to author the carrier or reprice the requirement instead of inventing one | [§3](#3-product-truth-and-admitted-carriers); [§7](#7-carrier-binding) | the five carrier kinds and the five binding requirements: this profile; which carriers and contracts exist: the product's design | 4, 5, 9 |
| P0 (recovered), P1 (independent), P4a (independent); F2 imported ([ACTIVATION §1](ACTIVATION.md#1-the-step)); I3 | By P0 an actor holds only finite context, and by P4a separately declared parts compose only through declared relations, so product-meaningful state changes only through typed transitions over declared inputs, and a surface's behaviour follows from those inputs; I3 makes the choice of one process model a policy, because stacks differ | [§1](#1-position); [§4](#4-process-model); [§5](#5-state-transitions); [§9](#9-view-shape) | a policy of this profile: the Elm Architecture as the process model, with State, Msg, Update, View, Cmd and Sub, transitions computed without effects from the current state and a declared message, and a view that is a function of state alone; the unmount test for view-local ephemera: this profile | 3, 4 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise); F2 imported ([ACTIVATION §1](ACTIVATION.md#1-the-step)) | By P0 an effect not visible at a declared point cannot be found by a later actor, and by P5 an undeclared effect cannot be evaluated, so effects occur only at a declared boundary and none hides in rendering or in decision logic | [§6](#6-effect-membrane) | the effect membrane, a refinement of [DESIGN_MODULE §10 Effect edge](DESIGN_MODULE.md#effect-edge), which interprets declared Cmd values and returns their outcomes as typed messages, and the handler forms it names: this profile; the interpreter mechanism: the project | 4, 8 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); F4 imported ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)) | By P4b the record of a step is not re-acquirable from memory, so a surface's behaviour must be reproducible from its recorded inputs; continuation therefore never leaks into the view, and by P6 a closure claim needs its evidence, so a product surface claims closure only with an executable replay proof for each product-meaningful interaction family | [§8](#8-continuation-and-replay); [§8 Msg-replay proof](#msg-replay-proof) | the Msg-replay test, which replays messages against an empty state, and the six contents of a replay proof: this profile; the proof surface: the project's design module ([§12](#12-adoption), step 7) | 6, 8, 9 |
| P3 (independent), P1 (independent), P6 (independent); I4 | By P3 a value binds one exact basis, and by I4 data crosses seams the surface does not control, so UX-consumed types come from the contract shared by front end and back end, and by P6 data crossing an untrusted or out-of-process seam is validated at runtime before it enters state | [§10](#10-type-sharing) | the six seams, at which this profile makes the preference of [DESIGN_MODULE §4](DESIGN_MODULE.md#4-functional-bias-and-typing) for parsing foreign data once at ingress an obligation, and one typed schema yielding both compile-time types and runtime validators: this profile; the schema mechanism: the project | 2, 3, 4 |
| P2 (independent), P6 (independent); I1 | By P2 obligations follow the outcome, and by I1 a public surface is how people reach the product's capability, so a surface that is the public face of a product capability declares the accessibility minimum; by P6 an exemption needs an authority, so an internal debug surface is exempt only with its exemption recorded | [§11](#11-accessibility-minimum) | the five declarations, with WCAG AA as the recommended default for web: this profile; a stricter accessibility refinement: the project | 1, 9 |
| P2 (independent), P1 (independent); I3 | By P2 the method fixes only what the outcome needs, and by P1 a stack's name carries no meaning, so the stack is free while the process model is preserved, and realisations are tested against the model, never ranked | [§4 Process model without stack mandate](#process-model-without-stack-mandate); [§4 Realisation discretion](#realisation-discretion) | the process model without stack mandate, mirroring [DESIGN_MODULE §4 Functional bias without language mandate](DESIGN_MODULE.md#functional-bias-without-language-mandate): this profile; which of the two compliance tests governs, the test over §4 to §10 with no §13 failure pattern or the test over §4 to §8: pending the product owner's ruling; §15 applies the stricter while the ruling is pending, under the fail-closed rule of [§1 Authority](#authority); the language, framework, state container, effect interpreter, runtime validator and toolchain: the project, in its design module | 4, 8 |
| P6 (independent); F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); I3 | By P6 authority exists only through an admitted grant, so an adopting surface has one UX realisation authority, and existing code, conventions and artifacts are evidence only; by F11 an ambiguity is resolved, carried, escalated or blocked, so an ambiguity fails closed through those outcomes instead of weakening the process model | [§1 Authority](#authority); [§2](#2-role-and-composition) | who adopts: Product authority, under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the adopted surfaces and scope, recorded in the adopting project's design modules ([§12](#12-adoption)); the stack: the project's ADRs, which may not weaken the process model; the map of the three exits to the ambiguity outcomes: this profile, under [ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome) | 1, 7, 9 |
| P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F4 imported ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)), F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)), F13 imported ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution)); I5 | By P6 an exemption needs an authority and by P4b a deferred obligation persists until paid, so a scaffold is exempt only with a recorded scope and retirement condition and never becomes production by accumulation; I5 makes per-change proof costly, so a UX sprint defers proof only as visible escrow that closure still pays, and closes only with every finding classified | [§12 Scaffold and exemption](#scaffold-and-exemption); [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow) | the five default-governance conditions, the escrowable and non-escrowable items and the close triggers: this profile; the generic escrow law and the six close classifications: [TICKETS §3](TICKETS.md#3-sprint-rules); the sprint boundary: [SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) | 1, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a value decides only what its evidence establishes, and F3 gives one core, so each verdict of this profile is a refined value mapped to exactly one core value for a named predicate, and a review, a replay proof, a closure claim and a carrier check combine with other results without one being read as another or coerced to success | [§15](#15-results-of-this-profile) | the four refinements and their values: this profile | 3, 9 |

No row cites the adoption steps and scope at the opening of §12, the
failure patterns (§13) or the review questions (§14); these sections
apply the consequences above, and every clause names the principle that
requires it ([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)).
§16 records source dispositions and decides nothing. The table is
new in this corpus. Purpose and material relation: an actor started on
this member sees which rules follow from the foundations and the imported
families, and which are choices of this profile, the product or the
project, with their owners, so no choice is presented as derived (P6,
P1).

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, product truth and carrier binding: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), which routes prompt construction for UX work to §7; [§2 Relationship to other members](#relationship-to-other-members), where a UX surface over world-model state still binds under §7; [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), whose compliance tests require §7 to hold; [§12](#12-adoption), step 5; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which escrows no product-truth-changing Msg variant that lacks an admitted carrier and keeps the UX layer from becoming the hidden constructive carrier under §3; [§13](#13-failure-patterns), patterns 7 and 13; [§14](#14-review-questions), questions 3 and 4; [§15](#15-results-of-this-profile), carrier admission and Blocked for want of a carrier.
- Row 2, the process model, state transitions and view shape: [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), which test a realisation against the §4 process model, the first requiring §4 to §8 and the second §4 to §10 to hold; [§12](#12-adoption), steps 4 and 9; [§13](#13-failure-patterns), patterns 1, 2, 8 and 10; [§14](#14-review-questions), questions 1, 2, 6, 10 and 11; [§15](#15-results-of-this-profile), surface review.
- Row 3, the effect membrane: [§4 Realisation discretion](#realisation-discretion), whose choices are justified against the §6 effect-membrane rule; [§5](#5-state-transitions), which places effects at the effect membrane of §6; [§9](#9-view-shape), where an out-of-render mutation violates §6 unless it is part of the declared effect membrane; [§12](#12-adoption), steps 6 and 9; [§13](#13-failure-patterns), patterns 3, 5 and 11; [§14](#14-review-questions), questions 5 and 10; [§15](#15-results-of-this-profile), surface review.
- Row 4, continuation and the replay proof: [§12](#12-adoption), step 7; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which may defer and cannot erase the §8 Msg-replay proof that closure requires; [§13](#13-failure-patterns), patterns 4 and 12; [§14](#14-review-questions), questions 7 and 12; [§15](#15-results-of-this-profile), replay proof and closure obligations.
- Row 5, type sharing: [§4 Realisation discretion](#realisation-discretion), whose compliance test requires §10 to hold; [§13](#13-failure-patterns), patterns 6 and 14; [§14](#14-review-questions), questions 8 and 9; [§15](#15-results-of-this-profile), surface review.
- Row 6, the accessibility minimum: [§12](#12-adoption), step 8; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which may defer and cannot erase the §11 obligations that closure requires; [§13](#13-failure-patterns), pattern 9; [§14](#14-review-questions), question 10; [§15](#15-results-of-this-profile), closure obligations.
- Row 7, the process model without stack mandate and realisation discretion: [§12](#12-adoption), step 2; [§14](#14-review-questions), question 11; [§15](#15-results-of-this-profile), surface review, which applies the stricter of the two compliance tests while the product owner's ruling is pending.
- Row 8, authority and composition: [§12](#12-adoption), where Product authority adopts the profile under §1 Authority and records the adoption per project; [§13](#13-failure-patterns), pattern 16; [§15](#15-results-of-this-profile), Fail closed, which returns the surface review's value under the stricter interpretation and leaves the other two exits of §1 Authority as a re-entry or a recorded scope.
- Row 9, scaffold exemption and sprint compliance escrow: [§2 Relationship to other members](#relationship-to-other-members), where UX work may use sprint compliance escrow under §12; [§13](#13-failure-patterns), patterns 15 and 17; [§14](#14-review-questions), questions 10 and 14; [§15](#15-results-of-this-profile), closure obligations, and its closing paragraph, where an exempt scaffold is a recorded scope and the six close classifications stay TICKETS §3's.
- Row 10, the results of this profile: [§1 Authority](#authority), [§3](#3-product-truth-and-admitted-carriers), [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), each of which states its test or exit and leaves the result to §15; no section of another member returns these values, and the core they map to is [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), which owns it and applies no rule of this section.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```


### Row `UX_METHOD.md#10-type-sharing-rule` (disposition `conserved`)

Predecessor, `UX_METHOD.md#10-type-sharing-rule` at rc.2:

```text
## 10. Type Sharing Rule

UX-consumed types come from the shared front-end / back-end contract.

A UX surface does not re-declare back-end record shapes. It imports them from the shared contract module (typically the same package or a dedicated `contracts/` package).

Runtime validation is mandatory at every untrusted or out-of-process seam:

- HTTP or RPC responses
- MCP payloads
- file-loaded records
- websocket or event-stream messages
- agent or worker outputs
- URL, storage, clipboard, or browser integration payloads

The project uses a typed-schema mechanism so the same type definition is the
source of both compile-time types and runtime validators. The mechanism choice
is project-local. Compile-time TypeScript alone is not sufficient at these
seams.

UX-local types are allowed for view-local concerns: form input draft state, sort order enums, filter strings. UX-local types do not shadow back-end types.

---
```

Successor, `UX.md#10-type-sharing`:

```text
## 10. Type sharing

UX-consumed types come from the shared front-end and back-end contract
(P3, P1; rc.2 #10-type-sharing-rule). A UX surface does not re-declare
back-end record shapes; it imports them from the shared contract module,
typically the same package or a dedicated `contracts/` package.

Runtime validation is mandatory at every untrusted or out-of-process seam
(P6; it makes DESIGN_MODULE §4's preference for parsing and admitting
foreign data once at ingress an obligation at these seams):

- HTTP or RPC responses;
- MCP payloads;
- file-loaded records;
- websocket or event-stream messages;
- agent or worker outputs;
- URL, storage, clipboard or browser integration payloads.

The project uses a typed-schema mechanism so that the same type
definition is the source of both compile-time types and runtime
validators; the mechanism choice is project-local. Compile-time
TypeScript alone is not sufficient at these seams (P6, P1). UX-local types
are allowed for view-local concerns: form input draft state, sort order
enums, filter strings. UX-local types do not shadow back-end types (P3).
```


### Row `UX_METHOD.md#11-accessibility-minimum` (disposition `conserved`)

Predecessor, `UX_METHOD.md#11-accessibility-minimum` at rc.2:

```text
## 11. Accessibility Minimum

A UX surface that is the public face of a product capability declares:

- semantic structure (heading levels, landmarks, lists, or platform-equivalent affordances)
- keyboard or platform-equivalent navigability for every action that has a pointer interaction
- focus management on dynamic content changes
- accessibility annotations for any custom interactive element that lacks a native semantic equivalent
- color contrast at the project's declared accessibility standard (WCAG AA is the recommended default for web)

Accessibility is not optional for product capabilities. It is optional for internal-only debug surfaces; the design module records the exemption.

This section is intentionally minimal. Projects with stricter accessibility obligations (regulated industry, public-sector procurement) author a project-local accessibility refinement and cite it from their design modules.

---
```

Successor, `UX.md#11-accessibility-minimum`:

```text
## 11. Accessibility minimum

A UX surface that is the public face of a product capability declares
(P2, P6; rc.2 #11-accessibility-minimum):

- semantic structure (heading levels, landmarks, lists, or
  platform-equivalent affordances);
- keyboard or platform-equivalent navigability for every action that has
  a pointer interaction;
- focus management on dynamic content changes;
- accessibility annotations for any custom interactive element that lacks
  a native semantic equivalent;
- colour contrast at the project's declared accessibility standard (WCAG
  AA is the recommended default for web).

Accessibility is not optional for product capabilities. It is optional
for internal-only debug surfaces, and the design module records the
exemption (P2, P6). This section is intentionally minimal. Projects with
stricter accessibility obligations (regulated industry, public-sector
procurement) author a project-local accessibility refinement and cite it
from their design modules (P2).
```


### Row `UX_METHOD.md#12-realization-discretion` (disposition `conserved`)

Predecessor, `UX_METHOD.md#12-realization-discretion` at rc.2:

```text
## 12. Realization Discretion

The method is opinionated about the process model. It is not opinionated about the realization stack.

The project chooses:

- the language
- the framework or runtime
- the state-container library (if any)
- the effect-interpreter mechanism
- the runtime validator (if any)
- the build, bundling, and deployment toolchain

The project records its choices in the design module along with a short justification of how each choice preserves the §4 Elm process model and the §6 effect-membrane rule.

The method does not rank stacks. It tests realizations. A realization is method-compliant when §4–§10 hold under inspection and the §14 failure patterns are absent.

---
```

Successor, `UX.md#realisation-discretion`:

```text
### Realisation discretion

The profile is opinionated about the process model and not about the
realisation stack (P1, P2; rc.2 #12-realization-discretion). The project
chooses:

- the language;
- the framework or runtime;
- the state-container library, if any;
- the effect-interpreter mechanism;
- the runtime validator, if any;
- the build, bundling and deployment toolchain.

The project records its choices in the design module with a short
justification of how each choice preserves the §4 Elm process model and
the §6 effect-membrane rule. The profile does not rank stacks; it tests
realisations. A realisation is compliant with this profile when §4 to §10
hold under inspection and the §13 failure patterns are absent (P6, P1).
This test differs from the test of §4 Process model without stack
mandate; §15 states which test applies while the product owner's ruling
between them is pending.
```

Successor, `UX.md#15-results-of-this-profile`:

```text
## 15. Results of this profile

This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `UX_METHOD.md#14-failure-pattern` (disposition `conserved`)

Predecessor, `UX_METHOD.md#14-failure-pattern` at rc.2:

```text
## 14. Failure Pattern

A UX surface is violating this method when any of these are true:

1. render code mutates state directly (assignments inside the render body, mutating a prop or context value)
2. view-local state cells carry product-meaningful state instead of view-local ephemera
3. an effect handler contains conditional logic that decides state transitions
4. multi-step state machines live in the view rather than in the reducer
5. mutable refs are read during render outside the declared effect membrane
6. UX-local types shadow or re-declare back-end types instead of importing from the shared contract
7. selection or action emission writes to file or network without going through an `AssetSurface` action
8. view-shape exemptions (per §9) are taken without a recorded design-module entry
9. accessibility is omitted on a public product capability without a recorded exemption
10. two-way binding emits no typed `Msg` action and the reducer is bypassed
11. logic that should be a `Cmd` is implemented imperatively inside an effect handler
12. the view's behavior cannot be replayed by replaying its `Msg` log against an empty `State`
13. a product-truth-changing UX message has no admitted carrier, graph function, runtime command, or typed product contract
14. external data crosses into UX state without runtime validation
15. a scaffold or debug surface is reachable, mutating, or used as proof without the §13A exemption record
16. a project-local ADR, component convention, or existing code pattern is used to weaken this method
17. a UX sprint claims closure while deferred proof, accessibility, carrier,
    scaffold, or authority debt remains unclassified or un-ticketed

Any of these is a method violation. Repeated violations are not normalized by usage; they are repaired or the surface is repriced.

---
```

Successor, `UX.md#13-failure-patterns`:

```text
## 13. Failure patterns

A UX surface violates this profile when any of these are true (P6, P5;
rc.2 #14-failure-pattern):

1. render code mutates state directly (assignments inside the render
   body, mutating a prop or context value);
2. view-local state cells carry product-meaningful state instead of
   view-local ephemera;
3. an effect handler contains conditional logic that decides state
   transitions;
4. multi-step state machines live in the view rather than in the reducer;
5. mutable refs are read during render outside the declared effect
   membrane;
6. UX-local types shadow or re-declare back-end types instead of
   importing from the shared contract;
7. selection or action emission writes to file or network without going
   through an AssetSurface action;
8. view-shape exemptions (§9) are taken without a recorded design-module
   entry;
9. accessibility is omitted on a public product capability without a
   recorded exemption;
10. two-way binding emits no typed Msg action and the reducer is
    bypassed;
11. logic that should be a Cmd is implemented imperatively inside an
    effect handler;
12. the view's behaviour cannot be replayed by replaying its Msg log
    against an empty State;
13. a product-truth-changing UX message has no admitted carrier, graph
    function, runtime command or typed product contract;
14. external data crosses into UX state without runtime validation;
15. a scaffold or debug surface is reachable, mutating or used as proof
    without the exemption record of §12 Scaffold and exemption;
16. a project-local ADR, component convention or existing code pattern is
    used to weaken this profile;
17. a UX sprint claims closure while deferred proof, accessibility,
    carrier, scaffold or authority debt remains unclassified or
    un-ticketed.

Any of these is a violation of this profile. Repeated violations are not
normalised by usage; they are repaired or the surface is repriced (P6,
P4b).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
## 15. Results of this profile

This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `UX_METHOD.md#15-review-questions` (disposition `conserved`)

Predecessor, `UX_METHOD.md#15-review-questions` at rc.2:

```text
## 15. Review Questions

A UX surface review under this method should answer:

1. What is the surface's `State`, `Msg`, and `Update`?
2. What is the surface's `Cmd` and `Sub` algebra?
3. Which `AssetSurface` or equivalent typed contracts does it bind to?
4. Which product-truth-changing messages map to admitted carriers?
5. Where is the effect membrane, and what `Cmd` values does it interpret?
6. Is `View = f(State)` provably pure for this surface?
7. Can the surface's behavior be replayed from a `Msg` log (the §8A Msg-replay proof)?
8. Are all UX-consumed types imported from the shared contract?
9. Are all out-of-process payloads runtime-validated before entering UX state?
10. Are view-shape, effect-membrane, accessibility, scaffold, or debug exemptions documented?
11. What realization stack is chosen, and how does it preserve the §4 Elm process model?
12. Does the surface honor the §8 view-does-not-own-continuation rule under user replay?
13. Does the design module include the `DESIGN_MODULE_METHOD.md` carrier set and structural carrier diagram required for closure?
14. If the work used a UX sprint, did close review classify every deferred proof,
    accessibility, carrier, scaffold, and authority finding?

If any of these cannot be answered, the design module is incomplete.

---
```

Successor, `UX.md#14-review-questions`:

```text
## 14. Review questions

A UX surface review under this profile should answer (P6, P2;
rc.2 #15-review-questions):

1. What is the surface's State, Msg and Update?
2. What is the surface's Cmd and Sub algebra?
3. Which AssetSurface or equivalent typed contracts does it bind to?
4. Which product-truth-changing messages map to admitted carriers?
5. Where is the effect membrane, and what Cmd values does it interpret?
6. Is `View = f(State)` provably pure for this surface?
7. Can the surface's behaviour be replayed from a Msg log (the Msg-replay
   proof of §8)?
8. Are all UX-consumed types imported from the shared contract?
9. Are all out-of-process payloads runtime-validated before entering UX
   state?
10. Are view-shape, effect-membrane, accessibility, scaffold or debug
    exemptions documented?
11. What realisation stack is chosen, and how does it preserve the §4 Elm
    process model?
12. Does the surface honour the §8 rule that the view does not own
    continuation under user replay?
13. Does the design module include the design profile's carrier set and
    structural carrier diagram required for closure (DESIGN_MODULE §6 and
    §7)?
14. If the work used a UX sprint, did close review classify every deferred
    proof, accessibility, carrier, scaffold and authority finding?

If any of these cannot be answered, the design module is incomplete (P6,
P5).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
## 15. Results of this profile

This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `UX_METHOD.md#16-relationship-to-other-method-surfaces` (disposition `conserved`)

Predecessor, `UX_METHOD.md#16-relationship-to-other-method-surfaces` at rc.2:

```text
## 16. Relationship To Other Method Surfaces

- `SPEC_METHOD.md` governs constitutional process, authority flow, repricing, and migration law.
- `ODD_METHOD.md` governs graph-native constructive carrier law. UX surfaces are projection / query surfaces under §10 of that method.
- `DESIGN_MODULE_METHOD.md` governs deterministic realization discipline at the module level. `UX_METHOD.md` refines it for UX modules.
- `TICKET_METHOD.md` governs ticket and sprint lifecycle. UX work may use sprint compliance escrow under §13B when the sprint boundary makes deferred proof visible, bounded, and payable.
- `WORLD_MODEL_METHOD.md` governs world-model semantic law for products that have a world-model dimension. UX surfaces over world-model state still bind through `AssetSurface` (or equivalent) per §7.

A UX-touching design module reads `DESIGN_MODULE_METHOD.md` plus `UX_METHOD.md`. A non-UX design module reads `DESIGN_MODULE_METHOD.md` only and ignores this surface.

---
```

Successor, `UX.md#relationship-to-other-members`:

```text
### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law. The graph-execution profile governs graph-native
constructive carrier law, and UX surfaces are projection and query
surfaces under it. DESIGN_MODULE governs deterministic realisation
discipline at module level, and this profile refines it for UX modules.
TICKETS governs ticket and sprint lifecycle; UX work may use sprint
compliance escrow under §12 when the sprint boundary makes deferred proof
visible, bounded and payable. The world-model profile
([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
products that have a world-model dimension; UX surfaces over world-model
state still bind through AssetSurface, or its equivalent, under §7 (P6;
rc.2 #16-relationship-to-other-method-surfaces).
```

Successor, `UX.md#2-role-and-composition`:

```text
## 2. Role and composition

SPEC_METHOD defines constitutional process and lawful re-entry; the
graph-execution profile defines graph-native constructive carrier law;
DESIGN_MODULE defines deterministic module-level realisation discipline
(P6; rc.2 #2-method-role). This profile refines DESIGN_MODULE with the
additional rules a module needs when it realises a UX surface (render
purity, state-transition algebra, effect-membrane discipline and
accessibility minimums) under the Elm process model. It does not
duplicate DESIGN_MODULE: where the parent already governs (immutability,
totality, effect-edge discipline, no semantic centre, coupling;
DESIGN_MODULE §10), this profile cites and extends it; where UX has
concerns the parent does not address (render lifecycle, browser events,
layout, accessibility), this profile is authoritative (P6, P4a).

This profile composes with the upstream members per surface (P4a, P0;
rc.2 #3-method-composition):

- when a module realises a UX surface, DESIGN_MODULE and this profile both
  apply, and its design module reads both;
- when a module realises a non-UX surface, only DESIGN_MODULE applies, and
  its design module ignores this profile;
- when a graph-execution product publishes a projection or query surface
  that includes UX, this profile governs that surface's realisation.

The composition rule: the graph-execution profile answers what
graph-native shape the product takes; DESIGN_MODULE what realisation
discipline the modules follow; this profile what additional discipline UX
surfaces follow (P6).

### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law. The graph-execution profile governs graph-native
constructive carrier law, and UX surfaces are projection and query
surfaces under it. DESIGN_MODULE governs deterministic realisation
discipline at module level, and this profile refines it for UX modules.
TICKETS governs ticket and sprint lifecycle; UX work may use sprint
compliance escrow under §12 when the sprint boundary makes deferred proof
visible, bounded and payable. The world-model profile
([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
products that have a world-model dimension; UX surfaces over world-model
state still bind through AssetSurface, or its equivalent, under §7 (P6;
rc.2 #16-relationship-to-other-method-surfaces).

### Non-goals

This profile is not a styling guide or design-system specification, a
component library, a brand or visual-identity surface, a wireframing or
prototyping process, a research method for user studies, or a stack
ranking or framework recommendation. Those are valid concerns; they
belong in product-local surfaces, not in this constitutional profile (P2;
rc.2 #17-non-goals).
```


### Row `UX_METHOD.md#17-non-goals` (disposition `conserved`)

Predecessor, `UX_METHOD.md#17-non-goals` at rc.2:

```text
## 17. Non-Goals

`UX_METHOD.md` is not:

- a styling guide or design system specification
- a component library
- a brand or visual-identity surface
- a wireframing or prototyping process
- a research method for user studies
- a stack ranking or framework recommendation

Those are valid concerns; they belong in product-local surfaces, not in this constitutional method.

---
```

Successor, `UX.md#non-goals`:

```text
### Non-goals

This profile is not a styling guide or design-system specification, a
component library, a brand or visual-identity surface, a wireframing or
prototyping process, a research method for user studies, or a stack
ranking or framework recommendation. Those are valid concerns; they
belong in product-local surfaces, not in this constitutional profile (P2;
rc.2 #17-non-goals).
```


### Row `UX_METHOD.md#18-canonical-compression` (disposition `conserved`)

Predecessor, `UX_METHOD.md#18-canonical-compression` at rc.2:

```text
## 18. Canonical Compression

`UX_METHOD.md` adopts the **Elm Architecture** as the constitutional UX process model and refines `DESIGN_MODULE_METHOD.md` for UX surfaces. The model: typed `State` held by the runtime, typed `Msg` algebra, pure `Update : (Msg, State) → (State, Cmd)`, pure `View : State → ViewTree`, side effects as `Cmd` values interpreted at a declared effect membrane that returns `Msg` to the reducer. The view does not own continuation (UX twin of `ODD_METHOD.md` §11.5A); the **Msg-replay test** is the discipline check. The realization stack is the project's choice, recorded in the design module along with justification of model preservation. The method tests realizations against §4–§10 and the §14 failure patterns; it does not rank stacks, languages, or frameworks.

When adopted, this method is the sole UX realization authority for the covered
surface. Product-truth-changing UX messages must map to admitted product
carriers; the UX layer must not become the hidden constructive carrier. External
payloads are runtime-validated before entering UX state. Scaffolds and debug
surfaces are governed unless explicitly exempted, bounded, and retired. UX
sprints may defer local proof and cleanup only as visible compliance escrow;
close review must classify and pay down the debt before method closure is
claimed.
```

Successor, `UX.md#1-position`:

```text
## 1. Position

This profile exists to make one instruction precise: "using the UX
profile, build this UI surface" (P2; rc.2 #1-position). It adopts the Elm
Architecture (TEA) as its constitutional process model: the view is a
pure projection of typed state; state transitions are pure reductions
over typed messages; side effects are values the reducer describes and a
declared effect membrane interprets; the runtime owns lifecycle and the
view does not own continuation (P0, P1). The view is not a state owner.
Stateful local mutation in views, two-way bindings without action
emission, and effect handlers used as controllers are violations of this
profile even when the surrounding ecosystem conventionally accepts them
(P6).

### Authority

When Product authority adopts this profile for a UX surface
([PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis)),
recording the adoption in a product definition, ticket, design module or
review, this profile is the sole UX realisation authority for that
surface (P6; rc.2 #1a-constitutional-authority-rule). Project-local ADRs
may choose the stack; they may not weaken the process model. Existing
code, component-library convention, screenshots, comments, design
history, prototype behaviour and generated artifacts are evidence only
and do not override this profile (P6). If this profile appears ambiguous
in a concrete case, the surface fails closed under SPEC_METHOD §5: the
work either satisfies the stricter interpretation, reprices through the
governing constitutional method, or records a scoped exemption in the
design module before implementation proceeds (P5, P6; §15 states the
result). Each exit is an outcome of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome):
satisfying the stricter interpretation is `resolved`, under this
profile's fail-closed policy; repricing is `escalated` to the owner of the
governing surface; a scoped exemption is `carried`, the exemption being
its recorded residual; until one of them is taken, the ambiguity is
`blocked` and implementation does not proceed.

### Foundation to law

This member is material family F20, UX. The table below shows which of
its rules follow from which premises, in the format of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law),
which also states the standing of the consequences. The family imports
five families under [PROFILES §1](PROFILES.md#1-the-boundary): F2,
transitions, steps and configuration
([ACTIVATION §1](ACTIVATION.md#1-the-step)); F3, results and their
combination ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)); F4,
work state, resumption and reuse
([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)); F11, change
management and ambiguity
([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); and F13, work
carriers ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution)). It
refines the software-design profile, family F17
([DESIGN_MODULE §1](DESIGN_MODULE.md#1-purpose-and-position)), for
modules that realise a UX surface (§2); where a row's rule refines a
DESIGN_MODULE rule, its choice column names that rule. Its instance
premises hold where a UX surface is realised under this profile; they are
adopted with it and do not follow from the foundations (P1, P6):

- I1: a product exposes UX surfaces, through which people and systems
  observe the product's admitted truth and request changes to it;
- I2: the product's design, outside the UX layer, declares the admitted
  truth and the carriers that change it;
- I3: UI stacks differ by project, and their ecosystems accept patterns
  that keep state, continuation or effects in the view;
- I4: data reaches a UX surface across seams that the surface does not
  control;
- I5: UX work iterates in short cycles, in which proof for each change
  can cost more than the expected correction.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P6 (independent), P1 (independent); F2 imported ([ACTIVATION §1](ACTIVATION.md#1-the-step)), F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); I1, I2 | By P6 a change to product truth needs an admitted authority, and by I2 the product's design declares the carriers that change it, so a UX surface renders admitted truth and changes it only through an admitted carrier, and the UX layer never becomes the hidden constructive carrier; by P1 a control's appearance carries no authority, so where no carrier exists the surface is blocked and the work re-enters to author the carrier or reprice the requirement instead of inventing one | [§3](#3-product-truth-and-admitted-carriers); [§7](#7-carrier-binding) | the five carrier kinds and the five binding requirements: this profile; which carriers and contracts exist: the product's design | 4, 5, 9 |
| P0 (recovered), P1 (independent), P4a (independent); F2 imported ([ACTIVATION §1](ACTIVATION.md#1-the-step)); I3 | By P0 an actor holds only finite context, and by P4a separately declared parts compose only through declared relations, so product-meaningful state changes only through typed transitions over declared inputs, and a surface's behaviour follows from those inputs; I3 makes the choice of one process model a policy, because stacks differ | [§1](#1-position); [§4](#4-process-model); [§5](#5-state-transitions); [§9](#9-view-shape) | a policy of this profile: the Elm Architecture as the process model, with State, Msg, Update, View, Cmd and Sub, transitions computed without effects from the current state and a declared message, and a view that is a function of state alone; the unmount test for view-local ephemera: this profile | 3, 4 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise); F2 imported ([ACTIVATION §1](ACTIVATION.md#1-the-step)) | By P0 an effect not visible at a declared point cannot be found by a later actor, and by P5 an undeclared effect cannot be evaluated, so effects occur only at a declared boundary and none hides in rendering or in decision logic | [§6](#6-effect-membrane) | the effect membrane, a refinement of [DESIGN_MODULE §10 Effect edge](DESIGN_MODULE.md#effect-edge), which interprets declared Cmd values and returns their outcomes as typed messages, and the handler forms it names: this profile; the interpreter mechanism: the project | 4, 8 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); F4 imported ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)) | By P4b the record of a step is not re-acquirable from memory, so a surface's behaviour must be reproducible from its recorded inputs; continuation therefore never leaks into the view, and by P6 a closure claim needs its evidence, so a product surface claims closure only with an executable replay proof for each product-meaningful interaction family | [§8](#8-continuation-and-replay); [§8 Msg-replay proof](#msg-replay-proof) | the Msg-replay test, which replays messages against an empty state, and the six contents of a replay proof: this profile; the proof surface: the project's design module ([§12](#12-adoption), step 7) | 6, 8, 9 |
| P3 (independent), P1 (independent), P6 (independent); I4 | By P3 a value binds one exact basis, and by I4 data crosses seams the surface does not control, so UX-consumed types come from the contract shared by front end and back end, and by P6 data crossing an untrusted or out-of-process seam is validated at runtime before it enters state | [§10](#10-type-sharing) | the six seams, at which this profile makes the preference of [DESIGN_MODULE §4](DESIGN_MODULE.md#4-functional-bias-and-typing) for parsing foreign data once at ingress an obligation, and one typed schema yielding both compile-time types and runtime validators: this profile; the schema mechanism: the project | 2, 3, 4 |
| P2 (independent), P6 (independent); I1 | By P2 obligations follow the outcome, and by I1 a public surface is how people reach the product's capability, so a surface that is the public face of a product capability declares the accessibility minimum; by P6 an exemption needs an authority, so an internal debug surface is exempt only with its exemption recorded | [§11](#11-accessibility-minimum) | the five declarations, with WCAG AA as the recommended default for web: this profile; a stricter accessibility refinement: the project | 1, 9 |
| P2 (independent), P1 (independent); I3 | By P2 the method fixes only what the outcome needs, and by P1 a stack's name carries no meaning, so the stack is free while the process model is preserved, and realisations are tested against the model, never ranked | [§4 Process model without stack mandate](#process-model-without-stack-mandate); [§4 Realisation discretion](#realisation-discretion) | the process model without stack mandate, mirroring [DESIGN_MODULE §4 Functional bias without language mandate](DESIGN_MODULE.md#functional-bias-without-language-mandate): this profile; which of the two compliance tests governs, the test over §4 to §10 with no §13 failure pattern or the test over §4 to §8: pending the product owner's ruling; §15 applies the stricter while the ruling is pending, under the fail-closed rule of [§1 Authority](#authority); the language, framework, state container, effect interpreter, runtime validator and toolchain: the project, in its design module | 4, 8 |
| P6 (independent); F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)); I3 | By P6 authority exists only through an admitted grant, so an adopting surface has one UX realisation authority, and existing code, conventions and artifacts are evidence only; by F11 an ambiguity is resolved, carried, escalated or blocked, so an ambiguity fails closed through those outcomes instead of weakening the process model | [§1 Authority](#authority); [§2](#2-role-and-composition) | who adopts: Product authority, under [PRODUCT_DEFINITION §7](PRODUCT_DEFINITION.md#7-collective-reference-frame-basis); the adopted surfaces and scope, recorded in the adopting project's design modules ([§12](#12-adoption)); the stack: the project's ADRs, which may not weaken the process model; the map of the three exits to the ambiguity outcomes: this profile, under [ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome) | 1, 7, 9 |
| P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); F4 imported ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)), F11 imported ([SPEC_METHOD §4](SPEC_METHOD.md#4-change-management)), F13 imported ([TICKETS §5](TICKETS.md#5-from-carrier-to-execution)); I5 | By P6 an exemption needs an authority and by P4b a deferred obligation persists until paid, so a scaffold is exempt only with a recorded scope and retirement condition and never becomes production by accumulation; I5 makes per-change proof costly, so a UX sprint defers proof only as visible escrow that closure still pays, and closes only with every finding classified | [§12 Scaffold and exemption](#scaffold-and-exemption); [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow) | the five default-governance conditions, the escrowable and non-escrowable items and the close triggers: this profile; the generic escrow law and the six close classifications: [TICKETS §3](TICKETS.md#3-sprint-rules); the sprint boundary: [SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) | 1, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); F3 imported ([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) | By P5 a value decides only what its evidence establishes, and F3 gives one core, so each verdict of this profile is a refined value mapped to exactly one core value for a named predicate, and a review, a replay proof, a closure claim and a carrier check combine with other results without one being read as another or coerced to success | [§15](#15-results-of-this-profile) | the four refinements and their values: this profile | 3, 9 |

No row cites the adoption steps and scope at the opening of §12, the
failure patterns (§13) or the review questions (§14); these sections
apply the consequences above, and every clause names the principle that
requires it ([FOUNDATIONS §1](FOUNDATIONS.md#1-vocabulary-of-standing)).
§16 records source dispositions and decides nothing. The table is
new in this corpus. Purpose and material relation: an actor started on
this member sees which rules follow from the foundations and the imported
families, and which are choices of this profile, the product or the
project, with their owners, so no choice is presented as derived (P6,
P1).

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, product truth and carrier binding: [ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope), which routes prompt construction for UX work to §7; [§2 Relationship to other members](#relationship-to-other-members), where a UX surface over world-model state still binds under §7; [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), whose compliance tests require §7 to hold; [§12](#12-adoption), step 5; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which escrows no product-truth-changing Msg variant that lacks an admitted carrier and keeps the UX layer from becoming the hidden constructive carrier under §3; [§13](#13-failure-patterns), patterns 7 and 13; [§14](#14-review-questions), questions 3 and 4; [§15](#15-results-of-this-profile), carrier admission and Blocked for want of a carrier.
- Row 2, the process model, state transitions and view shape: [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), which test a realisation against the §4 process model, the first requiring §4 to §8 and the second §4 to §10 to hold; [§12](#12-adoption), steps 4 and 9; [§13](#13-failure-patterns), patterns 1, 2, 8 and 10; [§14](#14-review-questions), questions 1, 2, 6, 10 and 11; [§15](#15-results-of-this-profile), surface review.
- Row 3, the effect membrane: [§4 Realisation discretion](#realisation-discretion), whose choices are justified against the §6 effect-membrane rule; [§5](#5-state-transitions), which places effects at the effect membrane of §6; [§9](#9-view-shape), where an out-of-render mutation violates §6 unless it is part of the declared effect membrane; [§12](#12-adoption), steps 6 and 9; [§13](#13-failure-patterns), patterns 3, 5 and 11; [§14](#14-review-questions), questions 5 and 10; [§15](#15-results-of-this-profile), surface review.
- Row 4, continuation and the replay proof: [§12](#12-adoption), step 7; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which may defer and cannot erase the §8 Msg-replay proof that closure requires; [§13](#13-failure-patterns), patterns 4 and 12; [§14](#14-review-questions), questions 7 and 12; [§15](#15-results-of-this-profile), replay proof and closure obligations.
- Row 5, type sharing: [§4 Realisation discretion](#realisation-discretion), whose compliance test requires §10 to hold; [§13](#13-failure-patterns), patterns 6 and 14; [§14](#14-review-questions), questions 8 and 9; [§15](#15-results-of-this-profile), surface review.
- Row 6, the accessibility minimum: [§12](#12-adoption), step 8; [§12 UX sprint compliance escrow](#ux-sprint-compliance-escrow), which may defer and cannot erase the §11 obligations that closure requires; [§13](#13-failure-patterns), pattern 9; [§14](#14-review-questions), question 10; [§15](#15-results-of-this-profile), closure obligations.
- Row 7, the process model without stack mandate and realisation discretion: [§12](#12-adoption), step 2; [§14](#14-review-questions), question 11; [§15](#15-results-of-this-profile), surface review, which applies the stricter of the two compliance tests while the product owner's ruling is pending.
- Row 8, authority and composition: [§12](#12-adoption), where Product authority adopts the profile under §1 Authority and records the adoption per project; [§13](#13-failure-patterns), pattern 16; [§15](#15-results-of-this-profile), Fail closed, which returns the surface review's value under the stricter interpretation and leaves the other two exits of §1 Authority as a re-entry or a recorded scope.
- Row 9, scaffold exemption and sprint compliance escrow: [§2 Relationship to other members](#relationship-to-other-members), where UX work may use sprint compliance escrow under §12; [§13](#13-failure-patterns), patterns 15 and 17; [§14](#14-review-questions), questions 10 and 14; [§15](#15-results-of-this-profile), closure obligations, and its closing paragraph, where an exempt scaffold is a recorded scope and the six close classifications stay TICKETS §3's.
- Row 10, the results of this profile: [§1 Authority](#authority), [§3](#3-product-truth-and-admitted-carriers), [§4 Process model without stack mandate](#process-model-without-stack-mandate) and [§4 Realisation discretion](#realisation-discretion), each of which states its test or exit and leaves the result to §15; no section of another member returns these values, and the core they map to is [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), which owns it and applies no rule of this section.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).
```

Successor, `UX.md#2-role-and-composition`:

```text
## 2. Role and composition

SPEC_METHOD defines constitutional process and lawful re-entry; the
graph-execution profile defines graph-native constructive carrier law;
DESIGN_MODULE defines deterministic module-level realisation discipline
(P6; rc.2 #2-method-role). This profile refines DESIGN_MODULE with the
additional rules a module needs when it realises a UX surface (render
purity, state-transition algebra, effect-membrane discipline and
accessibility minimums) under the Elm process model. It does not
duplicate DESIGN_MODULE: where the parent already governs (immutability,
totality, effect-edge discipline, no semantic centre, coupling;
DESIGN_MODULE §10), this profile cites and extends it; where UX has
concerns the parent does not address (render lifecycle, browser events,
layout, accessibility), this profile is authoritative (P6, P4a).

This profile composes with the upstream members per surface (P4a, P0;
rc.2 #3-method-composition):

- when a module realises a UX surface, DESIGN_MODULE and this profile both
  apply, and its design module reads both;
- when a module realises a non-UX surface, only DESIGN_MODULE applies, and
  its design module ignores this profile;
- when a graph-execution product publishes a projection or query surface
  that includes UX, this profile governs that surface's realisation.

The composition rule: the graph-execution profile answers what
graph-native shape the product takes; DESIGN_MODULE what realisation
discipline the modules follow; this profile what additional discipline UX
surfaces follow (P6).

### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law. The graph-execution profile governs graph-native
constructive carrier law, and UX surfaces are projection and query
surfaces under it. DESIGN_MODULE governs deterministic realisation
discipline at module level, and this profile refines it for UX modules.
TICKETS governs ticket and sprint lifecycle; UX work may use sprint
compliance escrow under §12 when the sprint boundary makes deferred proof
visible, bounded and payable. The world-model profile
([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
products that have a world-model dimension; UX surfaces over world-model
state still bind through AssetSurface, or its equivalent, under §7 (P6;
rc.2 #16-relationship-to-other-method-surfaces).

### Non-goals

This profile is not a styling guide or design-system specification, a
component library, a brand or visual-identity surface, a wireframing or
prototyping process, a research method for user studies, or a stack
ranking or framework recommendation. Those are valid concerns; they
belong in product-local surfaces, not in this constitutional profile (P2;
rc.2 #17-non-goals).
```

Successor, `UX.md#3-product-truth-and-admitted-carriers`:

```text
## 3. Product truth and admitted carriers

UX surfaces are projection and control surfaces: they render admitted
truth and emit typed messages (P6, P0;
rc.2 #3a-ux-projection-and-constructive-carrier-boundary). A UX-local Msg
may govern view-local concerns such as expansion state, sort order,
filter text, focus movement or draft input. A Msg that changes product
truth is not merely a UX concern. Product-truth changes include:

- writing, creating, moving or deleting assets;
- changing Context, selection authority, pinning or global product state;
- spawning, attaching or resuming sessions;
- dispatching agents, jobs, workorders, graph calls or runtime commands;
- changing closure, approval, continuation, lineage, provenance or
  evidence;
- publishing, accepting, rejecting or superseding product records.

Such a message maps to one admitted product carrier (P6, P4a):

- an AssetSurface action;
- a published graph function or lawful graph-function composition;
- a workorder, job or runtime command admitted by the product's design;
- an ABG event or command boundary where ABG is the runtime authority;
- another typed product contract named by the design module.

The UX layer does not become the hidden constructive carrier. If no
admitted carrier exists for a product-truth-changing message, the UX
surface is blocked until the carrier is authored or the requirement is
repriced (P6, P5; §15 states the result).
```

Successor, `UX.md#4-process-model`:

```text
## 4. Process model

The constitutional process model is the Elm Architecture (P0, P1;
rc.2 #4-process-model-elm-architecture):

- State: the typed state shape, held by the runtime, not by the view;
- Msg: the typed message algebra naming every action a user or system can
  emit;
- Update: the pure reducer of signature `(Msg, State) → (State, Cmd)`; it
  describes side effects as Cmd values and does not perform them;
- View: the pure function of signature `State → ViewTree`; given the same
  state, it produces the same output;
- Cmd and Sub: typed descriptions of side effects to schedule and of
  external sources to subscribe to, interpreted by the runtime at the
  effect membrane.

The runtime owns the loop (P0):

`current State → render View → user emits Msg → Update produces new State and Cmds → runtime interprets Cmds → repeat`

This loop is the Elm Architecture and the constitutional process model of
UX work under this profile (P1).

### Process model without stack mandate

The process model is the Elm Architecture; the implementation stack is
the project's choice, recorded in its design module. This mirrors
DESIGN_MODULE §4 Functional bias without language mandate: the process
model is constitutional and not negotiable; the stack is project-local
and free, provided it preserves the model (P1, P6;
rc.2 #4a-process-model-without-language-or-framework-mandate). Any
realisation that preserves §4 to §8 is compliant with this profile. This
test differs from the test of §4 Realisation discretion; §15 states which
test applies while the product owner's ruling between them is pending.
Examples (non-normative):

- a language-integrated reducer runtime, which enables typed state,
  message, update, command and view relations as native runtime
  capabilities;
- a typed reducer with an effect interpreter, which enables a
  host-language UI stack to preserve pure update and an explicit effect
  membrane;
- a reactive-signal realisation behind a reducer, which enables reactive
  projection while forbidding signal mutation outside the reducer;
- a server-rendered hypermedia realisation, which enables server-side
  state derivation as the reducer and uses the request and response
  boundary as the effect membrane.

Constitutionally rejected: any realisation that lets the view own state
continuation, performs side effects in render code, mutates state outside
a typed reducer, or carries multi-step view-local state machines that
bypass Msg. Two-way binding without Msg emission, imperative DOM
manipulation in render code, and effect handlers used as controllers are
violations regardless of stack (P6). A project that selects a framework
records the choice in its design module with a short justification of how
the framework preserves the §4 process model. The profile does not rank
frameworks; it tests realisations against §4 to §8 (P1).

### Realisation discretion

The profile is opinionated about the process model and not about the
realisation stack (P1, P2; rc.2 #12-realization-discretion). The project
chooses:

- the language;
- the framework or runtime;
- the state-container library, if any;
- the effect-interpreter mechanism;
- the runtime validator, if any;
- the build, bundling and deployment toolchain.

The project records its choices in the design module with a short
justification of how each choice preserves the §4 Elm process model and
the §6 effect-membrane rule. The profile does not rank stacks; it tests
realisations. A realisation is compliant with this profile when §4 to §10
hold under inspection and the §13 failure patterns are absent (P6, P1).
This test differs from the test of §4 Process model without stack
mandate; §15 states which test applies while the product owner's ruling
between them is pending.
```

Successor, `UX.md#5-state-transitions`:

```text
## 5. State transitions

State changes through typed messages applied by the pure reducer, the
Update of §4 (P4a, P1; rc.2 #5-state-transition-law). A UX surface
declares:

- its State shape;
- its Msg algebra;
- its `Update : (Msg, State) → (State, Cmd)`;
- its Cmd algebra;
- its Sub algebra when the surface subscribes to external or runtime
  events.

Each Cmd declaration names (P5, P4b):

- the effect kind;
- the typed input payload;
- the admitted carrier or external boundary it targets;
- the success Msg emitted back to the reducer;
- the failure Msg emitted back to the reducer;
- any deterministic correlation key required for replay.

The reducer is pure: it does not perform I/O, log to side channels or
mutate global state. Effects scheduled by Cmd are interpreted by the
runtime at the effect membrane (§6) (P0, P1).

View-local ephemera (open or closed flags, hover state, draft input) may
be held in implementation-local state cells where the framework provides
them, but only when the value is genuinely view-local: not observed by
other views, not part of the product's state surface, and not
consequential after the view unmounts. Product-meaningful state goes
through the reducer without exception (P6, P3). The discipline test for
whether state belongs in the reducer or in view-local ephemera: if losing
the value on unmount changes the product's behaviour or another part of
the UI's view, it belongs in the reducer (P3).
```

Successor, `UX.md#6-effect-membrane`:

```text
## 6. Effect membrane

Side effects are isolated to a declared effect membrane, which refines
DESIGN_MODULE §10 Effect edge for UX surfaces (P0, P5;
rc.2 #6-effect-membrane-rule). The membrane interprets Cmd values
produced by the reducer and translates side-effect outcomes back into Msg
values delivered to the reducer. Inside the membrane, I/O, subscriptions
to external sources, and imperative interop with the host platform (DOM,
file system, native APIs) are allowed. Outside it, in render code, in
pure helpers consumed by render, and in the reducer, there is no I/O, no
subscription and no imperative platform manipulation (P0).

The membrane has one job: interpret declared Cmd values. It is not where
logic lives. Branching, conditional state derivation and multi-step
business decisions belong in the reducer; the membrane interprets a
single declared Cmd per effect (P6). A platform-specific effect handler,
whatever name the chosen framework gives it (`useEffect`,
`createEffect`, `onMount`, `subscribe`, a server-action handler), is part
of the membrane only when it interprets a declared Cmd. A handler that
contains conditional logic deciding state transitions is a violation: the
logic moves to the reducer, and the handler interprets one Cmd (P6, P1).
```

Successor, `UX.md#7-carrier-binding`:

```text
## 7. Carrier binding

When the product publishes typed asset surfaces under the graph-execution
profile's carrier law and the local product's design, a UX surface binds
to one or more AssetSurface contracts as its data source and action
target (P6, P3; rc.2 #7-assetsurface-binding-rule). Binding requirements:

- the surface's State is derived from AssetSurface projections, not from
  a UX-local re-declaration of the asset shape;
- its product-truth-changing Msg variants map one to one to AssetSurface
  action-registry entries, or wrap them through a documented projection
  with no hidden semantic change;
- UX-local Msg variants are reserved for view-local concerns (open or
  closed, sort order, filter input);
- selection within the surface emits a Context update, or equivalent,
  consistent with the product's selection contract;
- writes from the surface go through the AssetSurface action registry,
  not through direct file or service calls.

This is the rule that produces strong functional consistency between
front end and back end: the same typed contract is the ground truth on
both sides (P1, P3). If the product does not publish AssetSurface
contracts, the design module names the equivalent typed contract and
applies the same binding law to that contract. Absence of an admitted
contract blocks product-truth-changing UX actions (P6, P5).

A prompt for UI or operator-surface work must carry the governing UX law
the task needs, acquired as
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
Acquisition states: a current derived surface or projected frame of this
member where one serves the task, otherwise the deciding sections of this
member carried in the prompt, rather than require the worker to rediscover
it from the raw member. If a worker
changes product truth through UI behaviour, the prompt must name the
admitted carrier and action path. If the prompt cannot identify that
carrier and action path, the correct result is a block or re-entry, not
local UI invention (P6, P5; provenance rc.2
authority_compressions/ux_method.compressed.md, a claim no rc.2 body
states; prompt construction is
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)).
```

Successor, `UX.md#8-continuation-and-replay`:

```text
## 8. Continuation and replay

In the graph-execution profile the runtime owns continuation (PROFILES
§2) and the product is a cooperative bounded-step subsystem. The UX
twin: the view does not own state continuation (P0, P6;
rc.2 #8-ux-twin-of-odd-115a-view-does-not-own-continuation). State
transitions flow through declared Msg actions interpreted by the reducer.
A view does not:

- decide on its own what the next state will be after a user event;
- chain several state updates locally without emitting them as separate
  Msg values;
- carry hidden inter-event state in refs, closures or module-level
  variables.

If a view appears to need a multi-step local state machine, that machine
belongs in the reducer as part of State, with explicit Msg transitions
between phases; the view becomes a pure projection of which phase it is
in (P1). The discipline test is the Msg-replay test: can the view's
behaviour be replayed by replaying its Msg log against an empty State? If
the answer is no, continuation has leaked into the view (P4b).

### Msg-replay proof

Every product UX surface carries at least one executable Msg-replay proof
for each product-meaningful interaction family before claiming closure
under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement).
Purpose and material relation: the Msg log is the surface's recorded work
state, and replay is resumption from it
([ACTIVATION §5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account)).
A surface whose behaviour cannot be reproduced from its log holds state
that no later actor or session can recover or check, so the proof is the
evidence that the view owns no hidden continuation (P0, P4b). A
replay proof includes:

- an initial State fixture;
- an ordered Msg log;
- the expected final State;
- the expected ordered Cmd values;
- the success and failure Msg values returned by interpreted Cmds;
- injected deterministic values for time, randomness, generated ids and
  external payloads.

The proof fails if correctness depends on (P5, P4b):

- DOM state not represented in State;
- mutable refs, module variables, closures, timers or effect-handler
  memory;
- network or file results that bypass typed Msg;
- view-local state that changes product behaviour after unmount or
  replay.

For a pure projection-only surface, the replay proof may be a no-effect
proof: a Msg log plus the final State and an empty Cmd sequence (P2).
```

Successor, `UX.md#9-view-shape`:

```text
## 9. View shape

A view is a pure function from typed state to a view tree (P1;
rc.2 #9-view-shape-rule). The view:

- accepts typed input (state, props, context);
- returns a typed view tree;
- declares its consumed inputs explicitly;
- does not capture mutable state in closures across renders;
- does not read from sources outside its declared input.

Whether the implementation expresses this as a function, a function
component, a template, a server-rendered handler, a signal-derived
expression or another framework-specific shape is a stack decision
recorded in the design module. The constitutional rule is the function
signature `State → ViewTree` and the absence of side effects in the body
(P1, P0). A view that depends on out-of-render mutation, for example a
ref written from inside an effect handler and read during render,
violates §6 unless the mutation is part of the declared effect membrane,
for example a platform handle for imperative interop already named in the
design module (P6).
```

Successor, `UX.md#10-type-sharing`:

```text
## 10. Type sharing

UX-consumed types come from the shared front-end and back-end contract
(P3, P1; rc.2 #10-type-sharing-rule). A UX surface does not re-declare
back-end record shapes; it imports them from the shared contract module,
typically the same package or a dedicated `contracts/` package.

Runtime validation is mandatory at every untrusted or out-of-process seam
(P6; it makes DESIGN_MODULE §4's preference for parsing and admitting
foreign data once at ingress an obligation at these seams):

- HTTP or RPC responses;
- MCP payloads;
- file-loaded records;
- websocket or event-stream messages;
- agent or worker outputs;
- URL, storage, clipboard or browser integration payloads.

The project uses a typed-schema mechanism so that the same type
definition is the source of both compile-time types and runtime
validators; the mechanism choice is project-local. Compile-time
TypeScript alone is not sufficient at these seams (P6, P1). UX-local types
are allowed for view-local concerns: form input draft state, sort order
enums, filter strings. UX-local types do not shadow back-end types (P3).
```

Successor, `UX.md#11-accessibility-minimum`:

```text
## 11. Accessibility minimum

A UX surface that is the public face of a product capability declares
(P2, P6; rc.2 #11-accessibility-minimum):

- semantic structure (heading levels, landmarks, lists, or
  platform-equivalent affordances);
- keyboard or platform-equivalent navigability for every action that has
  a pointer interaction;
- focus management on dynamic content changes;
- accessibility annotations for any custom interactive element that lacks
  a native semantic equivalent;
- colour contrast at the project's declared accessibility standard (WCAG
  AA is the recommended default for web).

Accessibility is not optional for product capabilities. It is optional
for internal-only debug surfaces, and the design module records the
exemption (P2, P6). This section is intentionally minimal. Projects with
stricter accessibility obligations (regulated industry, public-sector
procurement) author a project-local accessibility refinement and cite it
from their design modules (P2).
```

Successor, `UX.md#12-adoption`:

```text
## 12. Adoption

Product authority adopts this profile for a project (§1 Authority), and
the adoption is recorded by (P6, P4b; rc.2 #13-adoption-guidance):

1. naming the profile in the project's UX-related design modules;
2. recording the realisation stack choice (§4 Realisation discretion) and
   the justification;
3. declaring the irreducible architectural carrier set and the structural
   carrier diagram the design profile requires (DESIGN_MODULE §6 and §7);
4. declaring the State, Msg, Update, Cmd and Sub shapes for each UX
   surface in the design module before implementation;
5. declaring the AssetSurface or equivalent typed-contract bindings (§7)
   the surface consumes and emits to;
6. naming the effect-membrane mechanism (§6) and the Cmd algebra it
   interprets;
7. naming the executable Msg-replay proof surface required by §8;
8. naming any §11 accessibility refinement the project requires;
9. noting any §9 view-shape or §6 effect-membrane exemptions explicitly.

Adoption is per project. A project may adopt this profile only for some
UX surfaces, for example the production UI but not internal debug tools,
with the scope recorded in the design module (P2, P6).

### Scaffold and exemption

A UX surface is governed by this profile by default when any of these are
true (P6, P5; rc.2 #13a-scaffold-and-exemption-law):

- it is reachable from the product shell;
- it is used as proof for a ticket, requirement, design module, release or
  review;
- it can mutate product truth;
- it can spawn, attach, resume or dispatch work;
- it can change Context, selection authority, closure, continuation,
  evidence or provenance.

A scaffold, prototype, debug pane or temporary proof surface may be
exempt only when the design module or ticket records (P6, P4b):

- the exemption scope;
- the permitted operations;
- whether mutation is forbidden or explicitly bounded;
- a visible scaffold or debug label where user-facing;
- the authoritative surface that will supersede it;
- the retirement condition and owning ticket;
- the non-closure condition preventing release if the scaffold remains.

An exempt scaffold cannot become the production UX by accumulation. It is
retired, repriced into a governed UX surface, or kept outside product
closure (P4b, P6).

### UX sprint compliance escrow

UX is the primary governed use case for sprint compliance escrow. This
subsection is the profile's statement, which SPEC_METHOD §4 Sprint
execution boundary admits, of when that escrow is an appropriate cost
optimisation for UX; the generic escrow law and the close mechanics are
TICKETS §3 Compliance escrow and Close review (P2, P6;
rc.2 #13b-ux-sprint-compliance-escrow). A UX sprint may defer local UX
compliance proof during a short iteration window when per-change proof
cost is higher than expected correction cost. This is a cost-optimisation
rule; it does not weaken the UX process model (P2).

A UX sprint may escrow (P2, P4b):

- screenshots or walkthrough capture;
- visual review;
- copy, spacing, density and layout cleanup;
- accessibility review and remediation;
- Msg-replay proof updates for product-meaningful interaction families;
- design-module wording cleanup;
- trace cleanup between changed UX states and governing authority.

A UX sprint may not escrow (P6):

- product-truth-changing Msg variants that lack an admitted carrier;
- new or changed AssetSurface contracts or equivalent typed product
  contracts;
- new navigation, information architecture or selection authority that
  changes product meaning;
- runtime, governance, closure, continuation, lineage, provenance or
  evidence semantics;
- release criteria or method law.

If one of those appears, the sprint records the finding and the work
exits the UX sprint path through standalone repricing or sprint
supersession. The UX layer still does not become the hidden constructive
carrier (P6; §3).

A UX sprint should close when continued iteration is more expensive or
less trustworthy than review. Valid close triggers include (P2, P6):

- the declared timebox ends;
- accumulated changed states are too numerous for casual review;
- screenshots or walkthrough evidence no longer explain the current
  surface;
- interaction behaviour changed beyond visual polish;
- reviewer uncertainty makes more iteration unsafe without
  reconciliation.

UX sprint close is a forensic walkthrough: it reviews each changed
screen, state and product-meaningful interaction against the cited
authority (P6). Each finding takes one of the six classifications of
TICKETS §3 Close review (`accepted`, `local_paydown`, `design_reframe`,
`requirement_reprice`, `product_reprice`, `remove`); for a UX finding,
`accepted` reads as compliant with this profile and the cited design,
and `local_paydown` as local UX debt captured by a paydown ticket (P6,
P5). The sprint may close with explicit local paydown tickets only where
the debt is local to UX realisation and the governing method allows
follow-up. It may not close while product-truth carrier gaps, hidden
state continuation or authority drift remain unclassified (P6, P4b).

Closure under this profile for a product UX surface still requires the
§8 Msg-replay proof and the §11 accessibility obligations unless an
explicit exemption is recorded. The sprint can defer those obligations
during iteration; it cannot erase them (P4b, P6).
```

Successor, `UX.md#13-failure-patterns`:

```text
## 13. Failure patterns

A UX surface violates this profile when any of these are true (P6, P5;
rc.2 #14-failure-pattern):

1. render code mutates state directly (assignments inside the render
   body, mutating a prop or context value);
2. view-local state cells carry product-meaningful state instead of
   view-local ephemera;
3. an effect handler contains conditional logic that decides state
   transitions;
4. multi-step state machines live in the view rather than in the reducer;
5. mutable refs are read during render outside the declared effect
   membrane;
6. UX-local types shadow or re-declare back-end types instead of
   importing from the shared contract;
7. selection or action emission writes to file or network without going
   through an AssetSurface action;
8. view-shape exemptions (§9) are taken without a recorded design-module
   entry;
9. accessibility is omitted on a public product capability without a
   recorded exemption;
10. two-way binding emits no typed Msg action and the reducer is
    bypassed;
11. logic that should be a Cmd is implemented imperatively inside an
    effect handler;
12. the view's behaviour cannot be replayed by replaying its Msg log
    against an empty State;
13. a product-truth-changing UX message has no admitted carrier, graph
    function, runtime command or typed product contract;
14. external data crosses into UX state without runtime validation;
15. a scaffold or debug surface is reachable, mutating or used as proof
    without the exemption record of §12 Scaffold and exemption;
16. a project-local ADR, component convention or existing code pattern is
    used to weaken this profile;
17. a UX sprint claims closure while deferred proof, accessibility,
    carrier, scaffold or authority debt remains unclassified or
    un-ticketed.

Any of these is a violation of this profile. Repeated violations are not
normalised by usage; they are repaired or the surface is repriced (P6,
P4b).
```


### Row `UX_METHOD.md#2-method-role` (disposition `conserved`)

Predecessor, `UX_METHOD.md#2-method-role` at rc.2:

```text
## 2. Method Role

`SPEC_METHOD.md` defines constitutional process and lawful re-entry.

`ODD_METHOD.md` defines graph-native constructive carrier law.

`DESIGN_MODULE_METHOD.md` defines deterministic module-level realization discipline.

`UX_METHOD.md` refines `DESIGN_MODULE_METHOD.md` with the additional rules required when a module realizes a UX surface — render purity, state-transition algebra, effect-membrane discipline, and accessibility minimums — under the Elm Architecture process model.

`UX_METHOD.md` does not duplicate `DESIGN_MODULE_METHOD.md`. Where the parent method already governs (immutability, totality, effect-edge discipline, no-semantic-center, coupling), `UX_METHOD.md` cites and extends it. Where UX has concerns the parent does not address (render lifecycle, browser events, layout, accessibility), `UX_METHOD.md` is authoritative.

---
```

Successor, `UX.md#2-role-and-composition`:

```text
## 2. Role and composition

SPEC_METHOD defines constitutional process and lawful re-entry; the
graph-execution profile defines graph-native constructive carrier law;
DESIGN_MODULE defines deterministic module-level realisation discipline
(P6; rc.2 #2-method-role). This profile refines DESIGN_MODULE with the
additional rules a module needs when it realises a UX surface (render
purity, state-transition algebra, effect-membrane discipline and
accessibility minimums) under the Elm process model. It does not
duplicate DESIGN_MODULE: where the parent already governs (immutability,
totality, effect-edge discipline, no semantic centre, coupling;
DESIGN_MODULE §10), this profile cites and extends it; where UX has
concerns the parent does not address (render lifecycle, browser events,
layout, accessibility), this profile is authoritative (P6, P4a).

This profile composes with the upstream members per surface (P4a, P0;
rc.2 #3-method-composition):

- when a module realises a UX surface, DESIGN_MODULE and this profile both
  apply, and its design module reads both;
- when a module realises a non-UX surface, only DESIGN_MODULE applies, and
  its design module ignores this profile;
- when a graph-execution product publishes a projection or query surface
  that includes UX, this profile governs that surface's realisation.

The composition rule: the graph-execution profile answers what
graph-native shape the product takes; DESIGN_MODULE what realisation
discipline the modules follow; this profile what additional discipline UX
surfaces follow (P6).

### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law. The graph-execution profile governs graph-native
constructive carrier law, and UX surfaces are projection and query
surfaces under it. DESIGN_MODULE governs deterministic realisation
discipline at module level, and this profile refines it for UX modules.
TICKETS governs ticket and sprint lifecycle; UX work may use sprint
compliance escrow under §12 when the sprint boundary makes deferred proof
visible, bounded and payable. The world-model profile
([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
products that have a world-model dimension; UX surfaces over world-model
state still bind through AssetSurface, or its equivalent, under §7 (P6;
rc.2 #16-relationship-to-other-method-surfaces).

### Non-goals

This profile is not a styling guide or design-system specification, a
component library, a brand or visual-identity surface, a wireframing or
prototyping process, a research method for user studies, or a stack
ranking or framework recommendation. Those are valid concerns; they
belong in product-local surfaces, not in this constitutional profile (P2;
rc.2 #17-non-goals).
```


### Row `UX_METHOD.md#3-method-composition` (disposition `conserved`)

Predecessor, `UX_METHOD.md#3-method-composition` at rc.2:

```text
## 3. Method Composition

`UX_METHOD.md` composes with the upstream methods on a per-surface basis:

- when a module realizes a UX surface, both `DESIGN_MODULE_METHOD.md` and `UX_METHOD.md` apply
- when a module realizes a non-UX surface, only `DESIGN_MODULE_METHOD.md` applies
- when an ODD product publishes a projection / query surface that includes UX (`§10` of `ODD_METHOD.md`), `UX_METHOD.md` governs that surface's realization

The composition rule is:

- `ODD_METHOD.md` answers what graph-native shape the product takes
- `DESIGN_MODULE_METHOD.md` answers what realization discipline the modules follow
- `UX_METHOD.md` answers what additional discipline UX surfaces follow

### 3A. UX Projection And Constructive Carrier Boundary

UX surfaces are projection and control surfaces. They render admitted truth and
emit typed messages.

A UX-local `Msg` may govern view-local concerns such as expansion state, sort
order, filter text, focus movement, or draft input.

A UX `Msg` that changes product truth is not merely a UX concern. Product-truth
changes include:

- writing, creating, moving, or deleting assets
- changing Context, selection authority, pinning, or global product state
- spawning, attaching, or resuming sessions
- dispatching agents, jobs, workorders, graph calls, or runtime commands
- changing closure, approval, continuation, lineage, provenance, or evidence
- publishing, accepting, rejecting, or superseding product records

Such a message must map to one admitted product carrier:

- an `AssetSurface` action
- a published graph function or lawful graph-function composition
- a workorder, job, or runtime command admitted by the product's design
- an ABG event or command boundary where ABG is the runtime authority
- another typed product contract named by the design module

The UX layer must not become the hidden constructive carrier. If no admitted
carrier exists for a product-truth-changing message, the UX surface is blocked
until the carrier is authored or the requirement is repriced.

---
```

Successor, `UX.md#2-role-and-composition`:

```text
## 2. Role and composition

SPEC_METHOD defines constitutional process and lawful re-entry; the
graph-execution profile defines graph-native constructive carrier law;
DESIGN_MODULE defines deterministic module-level realisation discipline
(P6; rc.2 #2-method-role). This profile refines DESIGN_MODULE with the
additional rules a module needs when it realises a UX surface (render
purity, state-transition algebra, effect-membrane discipline and
accessibility minimums) under the Elm process model. It does not
duplicate DESIGN_MODULE: where the parent already governs (immutability,
totality, effect-edge discipline, no semantic centre, coupling;
DESIGN_MODULE §10), this profile cites and extends it; where UX has
concerns the parent does not address (render lifecycle, browser events,
layout, accessibility), this profile is authoritative (P6, P4a).

This profile composes with the upstream members per surface (P4a, P0;
rc.2 #3-method-composition):

- when a module realises a UX surface, DESIGN_MODULE and this profile both
  apply, and its design module reads both;
- when a module realises a non-UX surface, only DESIGN_MODULE applies, and
  its design module ignores this profile;
- when a graph-execution product publishes a projection or query surface
  that includes UX, this profile governs that surface's realisation.

The composition rule: the graph-execution profile answers what
graph-native shape the product takes; DESIGN_MODULE what realisation
discipline the modules follow; this profile what additional discipline UX
surfaces follow (P6).

### Relationship to other members

SPEC_METHOD governs constitutional process, authority flow, repricing and
migration law. The graph-execution profile governs graph-native
constructive carrier law, and UX surfaces are projection and query
surfaces under it. DESIGN_MODULE governs deterministic realisation
discipline at module level, and this profile refines it for UX modules.
TICKETS governs ticket and sprint lifecycle; UX work may use sprint
compliance escrow under §12 when the sprint boundary makes deferred proof
visible, bounded and payable. The world-model profile
([WORLD_MODEL](WORLD_MODEL.md)) governs world-model semantic law for
products that have a world-model dimension; UX surfaces over world-model
state still bind through AssetSurface, or its equivalent, under §7 (P6;
rc.2 #16-relationship-to-other-method-surfaces).

### Non-goals

This profile is not a styling guide or design-system specification, a
component library, a brand or visual-identity surface, a wireframing or
prototyping process, a research method for user studies, or a stack
ranking or framework recommendation. Those are valid concerns; they
belong in product-local surfaces, not in this constitutional profile (P2;
rc.2 #17-non-goals).
```


### Row `UX_METHOD.md#4-process-model-elm-architecture` (disposition `conserved`)

Predecessor, `UX_METHOD.md#4-process-model-elm-architecture` at rc.2:

```text
(predecessor anchor not resolved at rc.2; tenant child row: judge on the successor text alone, answer indeterminate)
```

Successor, `UX.md#4-process-model`:

```text
## 4. Process model

The constitutional process model is the Elm Architecture (P0, P1;
rc.2 #4-process-model-elm-architecture):

- State: the typed state shape, held by the runtime, not by the view;
- Msg: the typed message algebra naming every action a user or system can
  emit;
- Update: the pure reducer of signature `(Msg, State) → (State, Cmd)`; it
  describes side effects as Cmd values and does not perform them;
- View: the pure function of signature `State → ViewTree`; given the same
  state, it produces the same output;
- Cmd and Sub: typed descriptions of side effects to schedule and of
  external sources to subscribe to, interpreted by the runtime at the
  effect membrane.

The runtime owns the loop (P0):

`current State → render View → user emits Msg → Update produces new State and Cmds → runtime interprets Cmds → repeat`

This loop is the Elm Architecture and the constitutional process model of
UX work under this profile (P1).

### Process model without stack mandate

The process model is the Elm Architecture; the implementation stack is
the project's choice, recorded in its design module. This mirrors
DESIGN_MODULE §4 Functional bias without language mandate: the process
model is constitutional and not negotiable; the stack is project-local
and free, provided it preserves the model (P1, P6;
rc.2 #4a-process-model-without-language-or-framework-mandate). Any
realisation that preserves §4 to §8 is compliant with this profile. This
test differs from the test of §4 Realisation discretion; §15 states which
test applies while the product owner's ruling between them is pending.
Examples (non-normative):

- a language-integrated reducer runtime, which enables typed state,
  message, update, command and view relations as native runtime
  capabilities;
- a typed reducer with an effect interpreter, which enables a
  host-language UI stack to preserve pure update and an explicit effect
  membrane;
- a reactive-signal realisation behind a reducer, which enables reactive
  projection while forbidding signal mutation outside the reducer;
- a server-rendered hypermedia realisation, which enables server-side
  state derivation as the reducer and uses the request and response
  boundary as the effect membrane.

Constitutionally rejected: any realisation that lets the view own state
continuation, performs side effects in render code, mutates state outside
a typed reducer, or carries multi-step view-local state machines that
bypass Msg. Two-way binding without Msg emission, imperative DOM
manipulation in render code, and effect handlers used as controllers are
violations regardless of stack (P6). A project that selects a framework
records the choice in its design module with a short justification of how
the framework preserves the §4 process model. The profile does not rank
frameworks; it tests realisations against §4 to §8 (P1).

### Realisation discretion

The profile is opinionated about the process model and not about the
realisation stack (P1, P2; rc.2 #12-realization-discretion). The project
chooses:

- the language;
- the framework or runtime;
- the state-container library, if any;
- the effect-interpreter mechanism;
- the runtime validator, if any;
- the build, bundling and deployment toolchain.

The project records its choices in the design module with a short
justification of how each choice preserves the §4 Elm process model and
the §6 effect-membrane rule. The profile does not rank stacks; it tests
realisations. A realisation is compliant with this profile when §4 to §10
hold under inspection and the §13 failure patterns are absent (P6, P1).
This test differs from the test of §4 Process model without stack
mandate; §15 states which test applies while the product owner's ruling
between them is pending.
```


### Row `UX_METHOD.md#4a-process-model-without-language-or-framework-mandate` (disposition `conserved`)

Predecessor, `UX_METHOD.md#4a-process-model-without-language-or-framework-mandate` at rc.2:

```text
## 4A. Process Model Without Language Or Framework Mandate

The process model is the Elm Architecture. The implementation stack is the project's choice, recorded in the project's design module.

This mirrors `DESIGN_MODULE_METHOD.md` §4 ("Functional Bias Without Language Mandate"). The rule is:

- the **process model** is constitutional and not negotiable
- the **stack** is project-local and free, provided it preserves the model

Any realization that preserves §4–§8 is method-compliant. Examples (non-normative):

- **A language-integrated reducer runtime** — enables typed state, message,
  update, command, and view relations as native runtime capabilities.
- **A typed reducer with an effect interpreter** — enables a host-language UI
  stack to preserve pure update and an explicit effect membrane.
- **A reactive-signal realization behind a reducer** — enables reactive
  projection while forbidding signal mutation outside the reducer.
- **A server-rendered hypermedia realization** — enables server-side state
  derivation as the reducer and uses the request/response boundary as the
  effect membrane.

What is constitutionally rejected: any realization that lets the view own state continuation, performs side effects in render code, mutates state outside a typed reducer, or carries multi-step view-local state machines that bypass `Msg`. Two-way binding without `Msg` emission, imperative DOM manipulation in render code, and effect-handlers used as controllers are violations regardless of stack.

A project that selects a framework records the choice in its design module along with a short justification of how the framework preserves the §4 process model. The method does not rank frameworks. The method tests realizations against §4–§8.

---
```

Successor, `UX.md#process-model-without-stack-mandate`:

```text
### Process model without stack mandate

The process model is the Elm Architecture; the implementation stack is
the project's choice, recorded in its design module. This mirrors
DESIGN_MODULE §4 Functional bias without language mandate: the process
model is constitutional and not negotiable; the stack is project-local
and free, provided it preserves the model (P1, P6;
rc.2 #4a-process-model-without-language-or-framework-mandate). Any
realisation that preserves §4 to §8 is compliant with this profile. This
test differs from the test of §4 Realisation discretion; §15 states which
test applies while the product owner's ruling between them is pending.
Examples (non-normative):

- a language-integrated reducer runtime, which enables typed state,
  message, update, command and view relations as native runtime
  capabilities;
- a typed reducer with an effect interpreter, which enables a
  host-language UI stack to preserve pure update and an explicit effect
  membrane;
- a reactive-signal realisation behind a reducer, which enables reactive
  projection while forbidding signal mutation outside the reducer;
- a server-rendered hypermedia realisation, which enables server-side
  state derivation as the reducer and uses the request and response
  boundary as the effect membrane.

Constitutionally rejected: any realisation that lets the view own state
continuation, performs side effects in render code, mutates state outside
a typed reducer, or carries multi-step view-local state machines that
bypass Msg. Two-way binding without Msg emission, imperative DOM
manipulation in render code, and effect handlers used as controllers are
violations regardless of stack (P6). A project that selects a framework
records the choice in its design module with a short justification of how
the framework preserves the §4 process model. The profile does not rank
frameworks; it tests realisations against §4 to §8 (P1).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
## 15. Results of this profile

This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `UX_METHOD.md#5-state-transition-law` (disposition `conserved`)

Predecessor, `UX_METHOD.md#5-state-transition-law` at rc.2:

```text
## 5. State Transition Law

State changes through typed messages applied by the pure reducer (`Update` of §4).

A UX surface declares:

- its `State` shape
- its `Msg` algebra
- its `Update : (Msg, State) → (State, Cmd)`
- its `Cmd` algebra
- its `Sub` algebra when the surface subscribes to external or runtime events

Each `Cmd` declaration names:

- the effect kind
- the typed input payload
- the admitted carrier or external boundary it targets
- the success `Msg` emitted back to the reducer
- the failure `Msg` emitted back to the reducer
- any deterministic correlation key required for replay

The reducer is pure. It does not perform I/O, log to side channels, or mutate global state. Effects scheduled by `Cmd` are interpreted by the runtime at the effect membrane (see §6).

View-local ephemera (open/closed flags, hover state, draft input) may be held in implementation-local state cells where the framework provides them, but only when the value is genuinely view-local (not observed by other views, not part of the product's state surface, not consequential after the view unmounts). Product-meaningful state goes through the reducer without exception.

The discipline test for whether state belongs in the reducer or in view-local ephemera: if losing the value on unmount changes the product's behavior or another part of the UI's view, it belongs in the reducer.

---
```

Successor, `UX.md#5-state-transitions`:

```text
## 5. State transitions

State changes through typed messages applied by the pure reducer, the
Update of §4 (P4a, P1; rc.2 #5-state-transition-law). A UX surface
declares:

- its State shape;
- its Msg algebra;
- its `Update : (Msg, State) → (State, Cmd)`;
- its Cmd algebra;
- its Sub algebra when the surface subscribes to external or runtime
  events.

Each Cmd declaration names (P5, P4b):

- the effect kind;
- the typed input payload;
- the admitted carrier or external boundary it targets;
- the success Msg emitted back to the reducer;
- the failure Msg emitted back to the reducer;
- any deterministic correlation key required for replay.

The reducer is pure: it does not perform I/O, log to side channels or
mutate global state. Effects scheduled by Cmd are interpreted by the
runtime at the effect membrane (§6) (P0, P1).

View-local ephemera (open or closed flags, hover state, draft input) may
be held in implementation-local state cells where the framework provides
them, but only when the value is genuinely view-local: not observed by
other views, not part of the product's state surface, and not
consequential after the view unmounts. Product-meaningful state goes
through the reducer without exception (P6, P3). The discipline test for
whether state belongs in the reducer or in view-local ephemera: if losing
the value on unmount changes the product's behaviour or another part of
the UI's view, it belongs in the reducer (P3).
```


### Row `UX_METHOD.md#6-effect-membrane-rule` (disposition `conserved`)

Predecessor, `UX_METHOD.md#6-effect-membrane-rule` at rc.2:

```text
## 6. Effect Membrane Rule

Side effects are isolated to a declared effect membrane.

The membrane interprets `Cmd` values produced by the reducer and translates side-effect outcomes back into `Msg` values delivered to the reducer.

Inside the membrane:

- I/O is allowed
- subscriptions to external sources are allowed
- imperative interop with the host platform is allowed (DOM, file system, native APIs)

Outside the membrane (in render code, in pure helpers consumed by render, in the reducer):

- no I/O
- no subscriptions
- no imperative platform manipulation

The membrane has one job: interpret declared `Cmd` values. It is not where logic lives. Branching, conditional state derivation, and multi-step business decisions belong in the reducer; the membrane interprets a single declared `Cmd` per effect.

A platform-specific effect handler (whatever name the chosen framework gives it: `useEffect`, `createEffect`, `onMount`, `subscribe`, server-action handler) is part of the membrane only when it interprets a declared `Cmd`. A handler that contains conditional logic deciding state transitions is a method violation. Move the logic to the reducer; let the handler interpret one `Cmd`.

---
```

Successor, `UX.md#6-effect-membrane`:

```text
## 6. Effect membrane

Side effects are isolated to a declared effect membrane, which refines
DESIGN_MODULE §10 Effect edge for UX surfaces (P0, P5;
rc.2 #6-effect-membrane-rule). The membrane interprets Cmd values
produced by the reducer and translates side-effect outcomes back into Msg
values delivered to the reducer. Inside the membrane, I/O, subscriptions
to external sources, and imperative interop with the host platform (DOM,
file system, native APIs) are allowed. Outside it, in render code, in
pure helpers consumed by render, and in the reducer, there is no I/O, no
subscription and no imperative platform manipulation (P0).

The membrane has one job: interpret declared Cmd values. It is not where
logic lives. Branching, conditional state derivation and multi-step
business decisions belong in the reducer; the membrane interprets a
single declared Cmd per effect (P6). A platform-specific effect handler,
whatever name the chosen framework gives it (`useEffect`,
`createEffect`, `onMount`, `subscribe`, a server-action handler), is part
of the membrane only when it interprets a declared Cmd. A handler that
contains conditional logic deciding state transitions is a violation: the
logic moves to the reducer, and the handler interprets one Cmd (P6, P1).
```


### Row `UX_METHOD.md#7-assetsurface-binding-rule` (disposition `conserved`)

Predecessor, `UX_METHOD.md#7-assetsurface-binding-rule` at rc.2:

```text
## 7. AssetSurface Binding Rule

When the product publishes typed asset surfaces (per `ODD_METHOD.md` §11 carrier law and the local product's design), a UX surface binds to one or more `AssetSurface` contracts as its data source and action target.

Binding requirements:

- the UX surface's `State` is derived from `AssetSurface` projections, not from a UX-local re-declaration of the asset shape
- the UX surface's product-truth-changing `Msg` variants map one-to-one to `AssetSurface` action-registry entries or wrap them through a documented projection with no hidden semantic change
- UX-local `Msg` variants are reserved for view-local concerns (open/closed, sort order, filter input)
- selection within the UX surface emits a Context update (or equivalent) consistent with the product's selection contract
- writes from the UX surface go through the `AssetSurface` action registry, not through direct file or service calls

This is the rule that produces strong functional consistency between front-end and back-end: the same typed contract is the ground truth on both sides.

If the product does not publish `AssetSurface` contracts, the design module must
name the equivalent typed contract and apply the same binding law to that
contract. Absence of an admitted contract blocks product-truth-changing UX
actions.

---
```

Successor, `UX.md#7-carrier-binding`:

```text
## 7. Carrier binding

When the product publishes typed asset surfaces under the graph-execution
profile's carrier law and the local product's design, a UX surface binds
to one or more AssetSurface contracts as its data source and action
target (P6, P3; rc.2 #7-assetsurface-binding-rule). Binding requirements:

- the surface's State is derived from AssetSurface projections, not from
  a UX-local re-declaration of the asset shape;
- its product-truth-changing Msg variants map one to one to AssetSurface
  action-registry entries, or wrap them through a documented projection
  with no hidden semantic change;
- UX-local Msg variants are reserved for view-local concerns (open or
  closed, sort order, filter input);
- selection within the surface emits a Context update, or equivalent,
  consistent with the product's selection contract;
- writes from the surface go through the AssetSurface action registry,
  not through direct file or service calls.

This is the rule that produces strong functional consistency between
front end and back end: the same typed contract is the ground truth on
both sides (P1, P3). If the product does not publish AssetSurface
contracts, the design module names the equivalent typed contract and
applies the same binding law to that contract. Absence of an admitted
contract blocks product-truth-changing UX actions (P6, P5).

A prompt for UI or operator-surface work must carry the governing UX law
the task needs, acquired as
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)
Acquisition states: a current derived surface or projected frame of this
member where one serves the task, otherwise the deciding sections of this
member carried in the prompt, rather than require the worker to rediscover
it from the raw member. If a worker
changes product truth through UI behaviour, the prompt must name the
admitted carrier and action path. If the prompt cannot identify that
carrier and action path, the correct result is a block or re-entry, not
local UI invention (P6, P5; provenance rc.2
authority_compressions/ux_method.compressed.md, a claim no rc.2 body
states; prompt construction is
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)).
```


### Row `UX_METHOD.md#8-ux-twin-of-odd-115a-view-does-not-own-continuation` (disposition `conserved`)

Predecessor, `UX_METHOD.md#8-ux-twin-of-odd-115a-view-does-not-own-continuation` at rc.2:

```text
(predecessor anchor not resolved at rc.2; tenant child row: judge on the successor text alone, answer indeterminate)
```

Successor, `UX.md#8-continuation-and-replay`:

```text
## 8. Continuation and replay

In the graph-execution profile the runtime owns continuation (PROFILES
§2) and the product is a cooperative bounded-step subsystem. The UX
twin: the view does not own state continuation (P0, P6;
rc.2 #8-ux-twin-of-odd-115a-view-does-not-own-continuation). State
transitions flow through declared Msg actions interpreted by the reducer.
A view does not:

- decide on its own what the next state will be after a user event;
- chain several state updates locally without emitting them as separate
  Msg values;
- carry hidden inter-event state in refs, closures or module-level
  variables.

If a view appears to need a multi-step local state machine, that machine
belongs in the reducer as part of State, with explicit Msg transitions
between phases; the view becomes a pure projection of which phase it is
in (P1). The discipline test is the Msg-replay test: can the view's
behaviour be replayed by replaying its Msg log against an empty State? If
the answer is no, continuation has leaked into the view (P4b).

### Msg-replay proof

Every product UX surface carries at least one executable Msg-replay proof
for each product-meaningful interaction family before claiming closure
under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement).
Purpose and material relation: the Msg log is the surface's recorded work
state, and replay is resumption from it
([ACTIVATION §5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account)).
A surface whose behaviour cannot be reproduced from its log holds state
that no later actor or session can recover or check, so the proof is the
evidence that the view owns no hidden continuation (P0, P4b). A
replay proof includes:

- an initial State fixture;
- an ordered Msg log;
- the expected final State;
- the expected ordered Cmd values;
- the success and failure Msg values returned by interpreted Cmds;
- injected deterministic values for time, randomness, generated ids and
  external payloads.

The proof fails if correctness depends on (P5, P4b):

- DOM state not represented in State;
- mutable refs, module variables, closures, timers or effect-handler
  memory;
- network or file results that bypass typed Msg;
- view-local state that changes product behaviour after unmount or
  replay.

For a pure projection-only surface, the replay proof may be a no-effect
proof: a Msg log plus the final State and an empty Cmd sequence (P2).
```


### Row `UX_METHOD.md#9-view-shape-rule` (disposition `conserved`)

Predecessor, `UX_METHOD.md#9-view-shape-rule` at rc.2:

```text
## 9. View Shape Rule

A view is a pure function from typed state to a view tree.

The view:

- accepts typed input (state, props, context)
- returns a typed view tree
- declares its consumed inputs explicitly
- does not capture mutable state in closures across renders
- does not read from sources outside its declared input

Whether the implementation expresses this as a function, a function component, a template, a server-rendered handler, a signal-derived expression, or another framework-specific shape is a stack decision recorded in the design module. The constitutional rule is the function signature `State → ViewTree` and the absence of side effects in the body.

A view that depends on out-of-render mutation (e.g., a ref written from inside an effect handler and read during render) is a method violation under §6 unless the mutation is part of the declared effect membrane (e.g., a platform handle for imperative interop already named in the design module).

---
```

Successor, `UX.md#9-view-shape`:

```text
## 9. View shape

A view is a pure function from typed state to a view tree (P1;
rc.2 #9-view-shape-rule). The view:

- accepts typed input (state, props, context);
- returns a typed view tree;
- declares its consumed inputs explicitly;
- does not capture mutable state in closures across renders;
- does not read from sources outside its declared input.

Whether the implementation expresses this as a function, a function
component, a template, a server-rendered handler, a signal-derived
expression or another framework-specific shape is a stack decision
recorded in the design module. The constitutional rule is the function
signature `State → ViewTree` and the absence of side effects in the body
(P1, P0). A view that depends on out-of-render mutation, for example a
ref written from inside an effect handler and read during render,
violates §6 unless the mutation is part of the declared effect membrane,
for example a platform handle for imperative interop already named in the
design module (P6).
```


### Row `WORLD_MODEL_METHOD.md#1-observe` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#1-observe` at rc.2:

```text
### 1. Observe

Gather source evidence from the strongest available surfaces:

- runtime behavior
- source records and events
- code and configuration when available
- interfaces and schemas
- docs and metadata
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#1-paired-evidence-collection` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#1-paired-evidence-collection` at rc.2:

```text
### 1. Paired Evidence Collection

For a candidate object, assemble attribute-ledger evidence across
context variation together with evidence for at least one null peer:

- multiple contexts in which the candidate is instantiated
- a null-peer instance: a structurally similar thing that lacks the
  candidate's identity content, observed in the same contexts
- paired ledger entries covering `(candidate, context)` and
  `(null, context)` so identity-carrying signal can be separated from
  context-carrying signal

The paired evidence is the raw material of the cut. The ledger entries
remain distributed; they are not the object.
```

Successor, `WORLD_MODEL.md#paired-evidence-collection`:

```text
### Paired evidence collection

For a candidate object, assemble attribute-ledger evidence across context
variation together with evidence for at least one null peer (P3, P6;
rc.2 #1-paired-evidence-collection):

- multiple contexts in which the candidate is instantiated;
- a null-peer instance: a structurally similar thing that lacks the
  candidate's identity content, observed in the same contexts;
- paired ledger entries covering `(candidate, context)` and
  `(null, context)`, so identity-carrying signal can be separated from
  context-carrying signal.

The paired evidence is the raw material of the cut. The ledger entries
remain distributed; they are not the object (P3).
```


### Row `WORLD_MODEL_METHOD.md#10-compose` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#10-compose` at rc.2:

```text
### 10. Compose

Stitch published domain artifacts, their fragments, and their published
entity cuts into higher-order world models without erasing local
authority.

Composition is recursive, inspectable, and bounded.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```


### Row `WORLD_MODEL_METHOD.md#11-align-optional` (disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#11-align-optional` at rc.2:

```text
### 11. Align (Optional)

Use the semantic kernel as a tether for probabilistic alignment across domains,
entity cuts, artifacts, and projections.

This stage may produce:

- correspondence candidates
- confidence-ranked alignments
- ambiguity overlays
- mapping suggestions
- anomaly or mismatch overlays

These outputs are epistemic overlays, not yet published semantic truth.
```

Successor, `WORLD_MODEL.md#7-flow`:

```text
## 7. Flow

The profile proceeds through these stages (P4b, P6; rc.2 #method-flow and
the stage anchors named in §15):

1. Observe. Gather source evidence from the strongest available surfaces
   (§3 Evidence hierarchy): runtime behaviour; source records and events;
   code and configuration when available; interfaces and schemas; docs and
   metadata.
2. Trace. Index and locate the source surfaces that may support semantic
   claims. Tracing should make it possible to point from a later
   world-model attribute claim back to the concrete source span, field,
   locator, code path or record that supports it.
3. Extract. Produce reviewable intermediate surfaces from traced source
   objects: source inventories; object candidates; event and lifecycle
   candidates; treatment candidates; authority candidates; ambiguity
   registers. These are not the world model yet; they are the auditable
   path toward it.
4. Assure. Qualify traced observations into lawful world-model claims.
   Assurance should make explicit what is being claimed; whether the
   claim is observed, derived, interpreted or composed; which source
   surfaces support it; which source is authoritative for which aspect of
   the claim; and what ambiguity or missingness remains.
5. Ledger. Write the accepted qualified claims into the attribute ledger.
   The ledger is append-only: new understanding is recorded as new
   qualified claims and later object cuts, not by mutating prior accepted
   entries in place.
6. Bound. Identify bounded contexts and the candidate entities that
   actually cohere inside them. Reject schema-first modelling and
   vocabulary-cluster modelling. Define local boundaries in terms of
   function, authority, state and adjacency.
7. Materialise. Project entity cuts from the attribute ledger with enough
   semantic context for alignment and reasoning. Sparse first publication
   is lawful if the object is bounded, distinguishable and evidence-backed
   (§9 Admissibility).
8. Relate. Add treatment surfaces, covariance edges, adjoint mappings and
   temporal reference artifacts. This is where cross-domain meaning
   becomes explicit.
9. Publish. Publish immutable cuts of the published domain artifact; do
   not mutate prior published truth in place. In the low-volume lane, Git
   and the filesystem are sufficient as publication authority (§8
   Publication law).
10. Compose. Stitch published domain artifacts, their fragments and their
    published entity cuts into higher-order world models without erasing
    local authority. Composition is recursive, inspectable and bounded
    (§11 Composition law).
11. Align (optional). Use the semantic kernel as a tether for
    probabilistic alignment across domains, entity cuts, artifacts and
    projections. This stage may produce correspondence candidates,
    confidence-ranked alignments, ambiguity overlays, mapping suggestions,
    and anomaly or mismatch overlays. These outputs are epistemic
    overlays, not yet published semantic truth.
12. Project. Emit familiar outputs from the same semantic kernel: tables;
    schema contracts; API contracts; event contracts; mapping documents;
    transformation specifications; covariant transforms; tests and
    application scaffolds where applicable.
13. Compile (optional). Where delivery requires real execution, compile
    accepted semantic understanding into deterministic executable
    artifacts. Examples may include data-movement specifications,
    transformation jobs, high-volume ETL or ELT plans, deterministic
    mapping-tool records and generated implementation artifacts. The
    important rule: probabilistic correspondence may help comprehension;
    accepted semantic understanding governs compilation; execution at
    scale should run through deterministic compiled artifacts rather than
    through row-by-row probabilistic inference (P0, P6).
14. Serve or query (optional). If delivery needs justify it, expose
    traversal or query capability over published domain artifacts and
    composed world models. This may remain filesystem-first in the
    low-volume lane or later move behind a dedicated query plane.
```
