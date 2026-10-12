# AXIOMATIC_CALCULUS

Tier 1. Owns the a_c theory in full: position and scope, the signature,
the typed records, the laws AC-001 to AC-020, traversals and functor
kinds, interpretation and models, the three governed layers, the law of
calculus identity, the application boundary, external imports, exclusions
and the conformance obligations of this member. Consumes the ontology of
[FOUNDATIONS §2](FOUNDATIONS.md) (subject, representation, interpretation,
context, object, claim, evidence, judgment, authority, residual, basis,
material) and the result algebra of [ACTIVATION §3](ACTIVATION.md); it
states laws over those objects and defines none of them a second time.
Every clause names the principle that requires it (P0 to P6, FOUNDATIONS
§3). A route written `rc.2 #anchor` is into
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; a route
written `rc.2 MEMBER #anchor` is into that member of the same cut. Routes
are provenance only; nothing here depends on that cut to be applied.

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
declared fragment, model or relation (P6).

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
  probabilistic-construction premise and ACTIVATION §1; derived from rc.2
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
  RF-007 and the algebra of ACTIVATION §3 under RF-012; derived from the
  rc.2 REFERENCE_FRAME_METHOD laws of the same numbers;
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
scope, basis and invalidation law (P6).

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

## 4. Fundamental laws

The objects these laws govern are the records of §2, §3 and §5 and the
ontology of FOUNDATIONS §2; where a law names identity, authority, basis
or residual, the definition is FOUNDATIONS' and the law is this member's.

### AC-001 Closed signature

Every admitted object, relation, constraint, latitude, residual,
traversal, transformation specialisation and judgment belongs to one
declared signature. Every fundamental record also occurs exactly once in
the total `Population_M` function under its declared `RecordKind_ac`.
Missing, duplicate, shadowed or unknown record kinds and populations fail
closed (P3, P5; rc.2 #ac-001-closed-signature).

### AC-002 Scoped identity

An identity resolves one member under one type, context, owner, scope and
basis. Equal spelling, payload equality, position in any structure or
carrier equality does not establish semantic identity. Scoped identity
(authority, kind, value) is defined at FOUNDATIONS §2, Object; this law
applies it to every identity in `I` (P3; rc.2 #ac-002-scoped-identity).

### AC-003 Reference closure

Every referenced identity resolves exactly once in the applicable model or
through one explicit external relation. Resolution uses the exact
`RefDomain_Sigma(source_record_kind, field)` declaration across the
model's record populations. Dangling, duplicate, wrong-record-kind,
wrong-sort, wrong-basis, locally-and-externally ambiguous or
undeclared-field references refuse structural admission (P3, P5; rc.2
#ac-003-reference-closure).

### AC-004 Relation typing

A relation is lawful only when its kind admits the exact source and target
sorts and all required qualifiers are present. Direction is material
unless the relation kind explicitly declares symmetry (P4a, P3; rc.2
#ac-004-relation-typing).

### AC-005 Authority conservation

Objects, relations, constraints, latitude, residuals, traversals,
transformations, projections and judgments retain their declared semantic,
operation, evaluation and decision authority (the kinds of FOUNDATIONS §2,
Authority kinds). Copying, interpreting, encoding, evaluating or
transporting a record does not transfer authority (P6, P4b; rc.2
#ac-005-authority-conservation).

### AC-006 Basis coherence

Every fundamental record, model and result binds an exact basis
(FOUNDATIONS §2, Basis). Mixed bases require an explicitly owned
composite-basis relation. Individually valid coordinates do not create a
coherent composite basis by proximity (P6, P3; rc.2
#ac-006-basis-coherence).

### AC-007 Constraint and refusal

Each constraint names its governed subject, predicate, judgment kind,
latitude and refusal (§3, Constraint). The judgment of a constraint
returns a member of its declared result algebra, which is the core algebra
of ACTIVATION §3 or a declared refinement with a total mapping to it. A
failed, missing, indeterminate, out-of-scope or invalid-basis result
returns its member under that algebra and is never coerced to satisfied.
ACTIVATION §3 defines the members, the no-coercion rule and the boundary
among out_of_frame, indeterminate and a judgment that was not performed;
this law uses that definition and adds nothing to the algebra. Where this
member says that a condition refuses, the applicable structural or
semantic evaluation returns a non-satisfied member naming the condition;
the record, model or carrier is not admitted, and nothing is dropped
silently (P5, P6; rc.2 #ac-007-constraint-and-refusal).

### AC-008 Explicit latitude

Two values may differ lawfully only through an applicable latitude record
or transformation relation. An implementation preference, a probabilistic
choice or a human presence is not implicit latitude. FOUNDATIONS §4 states
the same rule for any two values; this law is its form over `L` and `T`
(P6, P1; rc.2 #ac-008-explicit-latitude).

### AC-009 Residual conservation

Every material uncertainty, omission, translation loss, unresolved
boundary or unproven relation remains in `X` until an authorised
disposition creates an exact successor model. Absence from a projection is
not resolution (P4b; rc.2 #ac-009-residual-conservation).

### AC-010 Material closure

For model `M`, seed set `Z` and exact dependency relation family `R`,
material closure is the least fixed point (P0, P2; rc.2
#ac-010-material-closure):

```text
closure_R(M, Z) = lfp(lambda Q: Z union required_R(M, Q))
```

The result is defined only when `Z`, `R`, required-edge semantics, basis
and scope are exact and the fixed point is finite and unique. Failure to
establish those conditions returns a gap or refusal. Least closure means
least lawful record closure under `R`; it does not claim globally minimal
prose, bytes, tokens, cost or cognitive effort. ACTIVATION §2 applies this
closure to the construction of a step's context under an envelope.

### AC-011 Projection

A projection selects a view of a model without changing selected meaning
(P4b, P2; rc.2 #ac-011-projection):

```text
project(M, Z, R) -> (M_Z, Boundary_Z) | gap | refusal
```

`M_Z` contains the material closure of `Z`. `Boundary_Z` records excluded,
external, unresolved, translated and invalidation-sensitive seams. A
projection is not a new semantic owner and cannot silently trim a required
member to satisfy a carrier or capability budget. FOUNDATIONS §4 states
the trimming rule for any reference; ACTIVATION §2 applies the projection
to a step's context, and every projected frame of this corpus is one.

### AC-012 Overlay

An overlay adds explicit records to one or more declared `Population_M`
families of a basis model. It does not mutate the basis. Override,
disambiguation, equivalence, specialisation or translation exists only as
a typed relation with exact authority, direction, scope, basis,
preservation, loss, refusal and invalidation semantics (P3, P6; rc.2
#ac-012-overlay).

### AC-013 Transformation

A transformation is an operation-bearing specialisation of one exact
traversal record `v` (§5). Its record is (P4b, P3; rc.2
#ac-013-transformation):

```text
t = {
  id,
  traversal,
  domain_model,
  codomain_model,
  context,
  owner,
  scope,
  basis,
  operation_authority,
  preconditions,
  preservation_relation,
  preserved,
  introduced,
  removed,
  external_preserved,
  external_introduced,
  external_removed,
  external_resolution_witnesses,
  residuals,
  evidence,
  provenance,
  stop_states,
  invalidation,
  re_entry
}
```

`t.traversal` resolves one `v`; its context, owner, scope, basis,
operation authority, evidence, provenance and stop contract equal or
lawfully restrict the corresponding traversal coordinates. A broader or
mismatched coordinate refuses (P6).

`domain_model` and `codomain_model` resolve exact content identities of
the complete input and proposed successor models. Each model identity
commits to its exact calculus basis, signature identity, complete finite
`Population_M`, complete `External_M`, exact external-resolution map and
selected model-content identity under the owning identity law. A mutable
locator, a model-family name, a partial projection or a population digest
without the exact model identity refuses (P3).

For each `x in External_M`, the model's exact resolution relation
determines:

```text
Resolution_M(x) = {
  external_identity,
  reference_domain,
  external_target_kind,
  resolved_target_identity,
  basis_relation,
  resolution_basis,
  evidence_identity
}

ResolutionSet_M = { Resolution_M(x) | x in External_M }
```

`Resolution_M` is a model coordinate supplied by the signature-declared
external reference relation, not a ninth fundamental record family. Every
field is identity-bearing and exact. One external identity has exactly one
resolution tuple in one model; a missing, ambiguous or extra tuple refuses
(P3).

For an ordinary same-basis transformation:

```text
basis(domain_model) = basis(codomain_model) = t.basis = basis(t.traversal)
signature(domain_model) = signature(codomain_model)
```

A cross-basis or cross-signature migration requires a separately
identified transformation specialisation whose exact composite-basis and
compatible signature-extension relations name both sides. No identity
whose basis or record kind changes belongs to `preserved`; the source
identity is removed and the successor identity is introduced, with their
continuity represented only by the exact migration relation (P3, P6).

`preservation_relation` resolves one exact typed equality relation
applicable to the declared domain and codomain model identities and record
kinds. It binds both model identities, both exact bases, comparison
domain, direction, authority, scope, evidence and equality law.
Equivalence or meaning-preservation may relate a removed identity to an
introduced identity; it cannot retain one identity in `preserved` (P1,
P3).

Let `Local_b` be the complete input-model local-record identity set, `P_t`
the identities named by `preserved`, `R_t` those named by `removed`, and
`N_t` the identities of the complete records named by `introduced`. A
lawful transformation proves the closed local-record delta (P4b):

```text
Local_b       = P_t disjoint_union R_t
Local_b_prime = P_t disjoint_union N_t
N_t intersect Local_b = empty
R_t intersect Local_b_prime = empty
```

For every identity in `P_t`, the input and successor records have the
same record kind, identity, context, owner, scope and basis. They are
either:

1. byte-identical under one exact canonical record grammar selected for
   both models; or
2. equal under the exact `preservation_relation` when the abstract
   records do not share such a byte grammar.

Canonical-byte equality and typed record equality are alternative proofs
of identity preservation, not carrier selection by the calculus. A changed
field, changed basis, changed record kind, nominally equal identifier,
equivalence or unbound assertion of preserved meaning refuses membership
in `P_t` (P3, P1).

Every removed identity is absent from the successor. Every introduced
identity is absent from the input and carries a complete lawful record in
exactly one successor population. Every input local-record identity is
classified exactly once as preserved or removed; no local record may be
silently dropped, retained or duplicated (P4b).

The external-resolution coordinates form a distinct closed delta. Let
`E_b` and `E_b_prime` be `ResolutionSet_M` for the domain and codomain
models; `EP_t`, `ER_t` and `EN_t` are exactly the resolution coordinates
named by `external_preserved`, `external_removed` and
`external_introduced`:

```text
E_b       = EP_t disjoint_union ER_t
E_b_prime = EP_t disjoint_union EN_t
EN_t intersect E_b = empty
ER_t intersect E_b_prime = empty
```

For every `x in EP_t`, `external_resolution_witnesses` contains exactly
one:

```text
ExternalResolutionPreservationWitness = {
  external_resolution: x,
  domain_model,
  codomain_model,
  domain_resolution: Resolution_domain_model(x),
  codomain_resolution: Resolution_codomain_model(x),
  decision: equal,
  evidence
}
```

The two resolution tuples are exactly field-equal. A nominally equal
external identifier, an equivalent target, a changed target kind, a
changed resolved target, a changed reference domain, a changed basis
relation, a changed resolution basis or a missing witness cannot enter
`EP_t`. Every member of `ER_t` has its complete resolution only in the
domain model; every member of `EN_t` has its complete resolution only in
the codomain model. A changed external resolution is a removal followed by
introduction of the new resolution coordinate and any separately declared
continuity relation; the referenced external identity may remain
unchanged, but the resolution is not preserved. Witnesses are total and
unique over `EP_t` and name no other resolution coordinate (P4b, P3).

Material residuals remain in the successor residual set unless an exact
authorised disposition is included in the transformation evidence.
Failure to establish any model identity, basis, population, local or
external partition, equality, external-resolution witness, residual or
codomain equation refuses (P4b, P5).

Application is:

```text
T[t](M_b, inputs) -> M_b_prime* | hold | gap | refusal
```

The exact transformation identity `t` declares every mutation it may
perform. The input model remains unchanged; `M_b_prime*` is a proposed
successor. A proposed successor does not accept or admit itself (P6).
FOUNDATIONS §4 consumes this law as the conservation accounting of every
step: what was preserved, introduced and removed, the external resolution
witnesses and the residuals.

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
its closed stop algebra. `Omega_v` is declared by the signature's stop
contract as a refinement of the core result algebra of ACTIVATION §3 with
a total mapping to it; it adds no core member and coerces none to
satisfied. The signature's stop contract constrains the kinds; the
traversal record's `stop_states` declares, per traversal, which of `hold`,
`gap` and `refusal` map to which non-satisfied core member. The stop
members this member writes, `hold`, `gap` and `refusal`, are
non-satisfied members under that mapping (P5).

- `F_D` classifies deterministic evaluation or proof over declared
  properties. It returns a judgment and does not perform the domain
  construction being judged (P6).
- `F_P` classifies bounded probabilistic interpretation, construction or
  proposal under an exact traversal contract. Its result has no semantic,
  admission, acceptance or closure authority merely because it is useful
  or repeatable (P6, P0 with the probabilistic-construction premise).
- `F_H` classifies explicit human adjudication under an exact identity,
  authority grant, subject, basis and decision contract. Human presence
  grants no ambient authority (P6).

The actor, the executor, the domain operation and the functor kind are
different coordinates. `Encode`, `Interpret`, `Serialize`, `Measure` and
other named domain operations are not aliases for `F_D`, `F_P` or `F_H`.
Different traversals may share one functor kind without sharing identity,
semantics, inputs, outputs, authority or evidence (P3, P6).

"Functor kind" is an `a_c` term for this traversal classification. It does
not by itself assert a category-theoretic functor. A model claiming
categorical functor laws additionally defines its source and target
categories and proves identity and composition preservation; FOUNDATIONS
§4's formal fragment carries that obligation for the method's own
hypothesis (P6, P1).

### AC-015 Functor classification

Every functor application binds exactly one functor kind and one traversal
identity. Applying any `F_*` kind without the bracketed traversal identity
`[v]` is incomplete (P3; rc.2 #ac-015-functor-classification).

### AC-016 Typed composition

Two traversals compose only when the first result type and judgment
satisfy the second traversal's exact domain and preconditions (P4a; rc.2
#ac-016-typed-composition):

```text
F_K2[w] compose F_K1[v]
```

Statement of reading, not new law (P4a): the first result of a binary
composition may be the cumulative carried result of the traversals before
the second, so this binary rule and the cumulative input of
[ACTIVATION §4](ACTIVATION.md#4-totality-and-refinement) are the same law;
the chained reading, in which nothing but the last output is carried, is
the special case.

Composition retains both traversal identities, intermediate results,
judgments, evidence, authority, provenance and stop states. It cannot
flatten probabilistic proposal, deterministic evaluation and human
decision into one undifferentiated operation. `a_c` prescribes no
universal `F_P -> F_D -> F_H` sequence; each application owns its lawful
topology (P4a, P4b, P6). FOUNDATIONS §3 P4a states AC-016's generic form over steps under the cumulative reading (ACTIVATION §4); this
clause is its form over traversals.

## 6. Interpretation and models

An interpretation applies `a_c` to an exact subject (P1; rc.2
#interpretation-and-models):

```text
Interpret_a_c(subject_basis, signature, interpretation_contract)
  -> M_subject* | hold | gap | refusal
```

The trailing `*` marks a proposed model that has not received the
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

Structural conformance of a model decides closed syntax, types,
identities, references, bases and mechanically decidable predicates.
Semantic fidelity decides the meaning and materiality of the
interpretation. Structural success is evidence for semantic review, not a
substitute for it. EVALUATION §2 applies this separation to every review;
this law is its form over `a_c` models (P1, P6; rc.2
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
subject (P6, P3).

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
this member is issued under the tier-2 RELEASE member (constructed at its
own activation; until then SPEC_METHOD §6 carries release law by
reference) and under AC-020, after the release bytes exist, with
`publication_basis` naming that release and this member's bytes in it and
`derivation_basis` naming the predecessor cut and the derivation account
of §1. This authoring text is a source project surface, not the
identity-bearing release, and it is not the identity-bearing source of the
released calculus that the common dependency contract pins
([A_C_DEPENDENCY](../../../specification/requirements/A_C_DEPENDENCY.md)).
The predecessor edition's coordinates are recorded here as provenance of
this edition's derivation, not as this edition's identity: cut
`stdo://releases/v2.5.1-rc.2/`, manifest SHA-256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`,
member `AXIOMATIC_CALCULUS.md` SHA-256
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`,
concept identity unchanged (P3, P6).

## 9. Application boundary, imports and exclusions

### Application boundary

This member defines the generic relations `a_c.X` and `a_c.X.C`. It
selects, constructs, accepts or releases no concrete interpretation or
carrier. A downstream authority owns its exact subject population,
interpretation, carrier, judgments and Product or release status. The
downstream identity is never embedded back into the calculus or its
publication basis (P2, P6; rc.2 #application-boundary).

### External imports and specialisations

An application may declare a typed import, translation or specialisation
of an `a_c` concept under that application's own exact authority, context,
basis, scope, preservation, loss, refusal and invalidation law. Such a
relation is external to the calculus. It neither changes `a_c` nor enters
this member by being useful to an application (P6, P2; rc.2
#external-imports-and-specializations). PROFILES §1 states the same
rule from the profile's side as the declared-binding rule.

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

## 11. Source dispositions

Rows received by this member. Anchors are into rc.2
AXIOMATIC_CALCULUS.md; a locus is a section of this file unless another
member is named. Every row is restated in this member's own text; a route
is provenance only.

| Anchor | Disposition | Locus |
|---|---|---|
| #position | conserved; the derivation diagram is written with plain arrows | §1 |
| #derivation-provenance | conserved; the derivation account is carried with absolute rc.2 routes beside the successor member that now states each commitment; "ODD" and "GTL" are generalised to profile, realisation and carrier, losing no determination; "graph, runtime, ODD, or application shorthand" is generalised to a runtime, a profile, a realisation or an application, which include the graph case; field correction: the predecessor says the resolved address array is recorded under `derivation_basis.release_uri`, this member says `derivation_basis.principle_refs`, the array field that the record shape in both editions actually declares for it (`release_uri` holds one URI); that is a correction that tightens the text to the record, not a change of law | §1 Derivation provenance |
| #scope | conserved | §1 Scope |
| #core-signature | conserved; the carrier list "records, tables, graphs, terms" is generalised to records, tables, terms, clauses, code or any other representation, which includes graphs | §2 |
| #typed-records | conserved | §3 |
| #semantic-object | conserved; related to FOUNDATIONS §2 Object | §3 Semantic object |
| #typed-relation | conserved | §3 Typed relation |
| #constraint | conserved | §3 Constraint |
| #latitude | conserved | §3 Latitude |
| #residual | conserved; related to FOUNDATIONS §2 Residual | §3 Residual |
| #fundamental-laws | not applicable: heading with no claim text (20 bytes); its children are disposed individually | §4 |
| #ac-001-closed-signature | conserved | §4 AC-001 |
| #ac-002-scoped-identity | conserved; scoped identity is defined at FOUNDATIONS §2 Object and P3, the law is here; "graph position" is generalised to position in any structure, which includes it | §4 AC-002 |
| #ac-003-reference-closure | conserved | §4 AC-003 |
| #ac-004-relation-typing | conserved | §4 AC-004 |
| #ac-005-authority-conservation | conserved; authority kinds are defined at FOUNDATIONS §2, the law is here; P4b consumes it | §4 AC-005 |
| #ac-006-basis-coherence | conserved; basis is defined at FOUNDATIONS §2, the law is here | §4 AC-006 |
| #ac-007-constraint-and-refusal | conserved; stated as a law over constraints using the algebra defined once in ACTIVATION §3, consistent with its three-case boundary; the declared algebra is tightened to the core or a declared refinement with a total mapping | §4 AC-007; algebra at ACTIVATION §3 |
| #ac-008-explicit-latitude | conserved; the generic form over any two values is FOUNDATIONS §4 | §4 AC-008 |
| #ac-009-residual-conservation | conserved; P4b consumes it | §4 AC-009 |
| #ac-010-material-closure | conserved; applied by ACTIVATION §2 | §4 AC-010 |
| #ac-011-projection | conserved; applied by ACTIVATION §2; the trimming rule's generic form is FOUNDATIONS §4 | §4 AC-011 |
| #ac-012-overlay | conserved | §4 AC-012 |
| #ac-013-transformation | conserved in full; FOUNDATIONS §4 conservation accounting consumes its delta fields | §4 AC-013 |
| #ac-014-judgment-separation | conserved; the judgment object is defined at FOUNDATIONS §2, the record and the law are here | §4 AC-014 |
| #traversals-and-functor-kinds | conserved; the stop algebra is tied to the one result algebra of ACTIVATION §3 (tightening, P5); the traversal record's ownership against same-spelled terms is made explicit (P3) | §5 |
| #ac-015-functor-classification | conserved | §5 AC-015 |
| #ac-016-typed-composition | conserved; P4a states AC-016's generic form over steps under the cumulative reading (ACTIVATION §4) | §5 AC-016 |
| #interpretation-and-models | conserved; the interpretation contract is related to FOUNDATIONS §2 Interpretation | §6 |
| #ac-017-interpretation-fidelity | conserved; P1 consumes it | §6 AC-017 |
| #ac-018-structural-and-semantic-separation | conserved; the generic form over every review is EVALUATION §2 | §6 AC-018 |
| #ac-019-valid-model | conserved; the checker rule's generic form is EVALUATION §2 | §6 AC-019 |
| #subject-and-carrier-boundaries | conserved | §7 |
| #ac-020-layer-and-release-separation | conserved; applied to release lineage by SPEC_METHOD §6 | §7 AC-020 |
| #exact-calculus-identity | conserved; every determination of the identity law and the record shape is restated; the record instance (the coordinates) is a release artefact issued after the bytes exist, not a claim of the section, so this edition's identity is bound at its release under RELEASE and AC-020 and the predecessor's coordinates are recorded as provenance | §8 |
| #application-boundary | conserved | §9 Application boundary |
| #external-imports-and-specializations | conserved | §9 External imports and specialisations |
| #exclusions | conserved; "graph storage topology" and "world-model ontology" are generalised to any storage topology and any domain ontology, which include them | §9 Exclusions |
| #conformance-obligations | conserved | §10 |
