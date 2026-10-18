# The STDO Axiomatic Calculus for Governed Symbolic Systems

## Position

The **STDO Axiomatic Calculus for Governed Symbolic Systems**, written `a_c`,
is STDO's domain-specific, carrier-neutral constitutional calculus for
representing and relating governed symbolic systems.

The [foundational commitments](FOUNDATIONS.md#foundational-commitments) supply
purpose (F1), interpretation (F2), identity (F3), composition (F4),
finite-capacity (F5) and authority (F6) premises. Given an explicit interpretation and
typed subject, AC-003, AC-004 and AC-006 require resolved, compatible references
on one exact basis before a model's judgment can be consumed. The signature,
record kinds, closure operator and functor-kind classification below are the
calculus's additional choices, owned by this standard's semantic authority;
finite capacity alone does not derive them. The family arguments below separate
these choices from their conditional consequences.

AC-007 and AC-014 consume the shared
[result algebra](FOUNDATIONS.md#result-algebra); AC-016 consumes its
[conjunction](FOUNDATIONS.md#result-conjunction) where a composite claim needs
several judgments. The [transformation library](TRANSFORMATION_LIBRARY.md)
provides reusable responsibilities. It does not replace AC-013's exact
transformation contract or establish category-theoretic functor laws.

Its stable concept identity is:

```text
urn:stdo:concept:axiomatic-calculus:a-c
```

This standard owns that concept in bounded context:

```text
urn:stdo:bounded-context:axiomatic-calculus
```

`a_c` is a separately identifiable specialization of STDO principles. It
defines sorts, typed objects, relations, constraints, latitude, residual
uncertainty, traversals, functor kinds, judgments, closure, projections,
transformations, models, and validity laws. Those definitions do not depend on
a derivation-source record layout, a selected subject interpretation, a
particular carrier, a model provider, a runtime, or a repository topology.

`a_c` makes no claim of universal applicability, logical completeness,
consistency, decidability, soundness, or category-theoretic status except where
an exact, separately identified proof establishes that claim for a declared
fragment, model, or relation.

The predecessor STDO clauses record the calculus's historical derivation
provenance. The selected cut's F1–F6 commitments and shared laws are its operative
premises; this member owns its additional definitions. Neither source uniquely
forces the chosen signature or classification. Application to an exact subject
is a separately owned downstream relation. Those relations are distinct:

```text
exact predecessor STDO principles ──provenance──> a_c
a_c + exact subject X              ──interpret──> a_c.X
a_c.X + exact accepted semantic judgment J_X
      + exact carrier C            ──encode─────> a_c.X.C
```

The calculus, an interpreted model, and an encoded carrier are distinct
governed layers with separate content identities and proof boundaries. A layer
becomes a released Product only through separately authorized Product
acceptance and release. Neither interpretation nor encoding can redefine the
calculus.

## Derivation Provenance

The following clause families document the design provenance of the calculus:

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

These references establish provenance. The definitions and laws below own the
`a_c` specialization within the selected complete STDO cut and explicitly
consume its common result and composition owners. A consumer does not need an
implicit STDO representation, GTL carrier, or downstream implementation to
interpret the calculus.

This standard introduces the generic calculus identities `F_D`, `F_P`, and
`F_H`. It does not import those identities from an equal-spelled graph,
runtime, ODD, or application shorthand. The predecessor clauses motivated the
substrate-neutral evaluation, probabilistic-processing, human-adjudication,
authority, evidence, and refusal distinctions. This member selects the three
generic kinds below; their inventory is a calculus policy, not a theorem forced
by those predecessor clauses. Nominal equality with a predecessor or downstream shorthand
creates no concept-identity, import, or equivalence relation.

The relative links above identify derivation clause families in this authoring
source. Issuance of an exact `AxiomaticCalculusBasis` resolves and records their
absolute predecessor-cut semantic addresses under
`derivation_basis.principle_refs`, resolved within `derivation_basis.release_uri`.
The mutable authoring links are not themselves
the digest-bound derivation references.

The derivation direction is one-way. A model of STDO under `a_c`, an encoded
carrier, a proof tool, or a successful application cannot amend the source
principles or this calculus.

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

## Fundamental Laws

These arguments apply [F1–F6](FOUNDATIONS.md#foundational-commitments)
to a governed symbolic model under a declared signature and interpretation.
The model's records represent a separately identified subject; some predicates
admit mechanical decision and others require semantic judgment. These are the
calculus's instance conditions. Its finite signature and record choices do not
follow from an actor's finite capacity. Selection authority remains bound by
[Interpretation And Models](#interpretation-and-models).

| Determination and consuming law | Conditional argument | Additional choice and owner |
|---|---|---|
| Record admission: [AC-001](#ac-001-closed-signature), [AC-003](#ac-003-reference-closure), [AC-004](#ac-004-relation-typing) | Information and interpretation require the referent of a claim to be recoverable (F2/F3); algebraic composition requires the declared endpoint sorts and qualifiers (F4). Under the selected closed signature, an ambiguous or mistyped reference cannot support admission. | This calculus chooses the record families, total population function and structural refusal rules. The signature owner supplies the concrete sorts, cardinalities and reference domains; closed syntax does not establish their semantic adequacy. |
| Identity, authority and basis: [AC-002](#ac-002-scoped-identity), [AC-005](#ac-005-authority-conservation), [AC-006](#ac-006-basis-coherence) | Identity distinguishes a scoped object from its encoding (F2/F3). Evidence and authority distinguish a supported claim from an operation grant (F6). Consequently equal bytes, copied records or individually valid bases supply neither semantic identity, transferred authority nor a compatible composite basis. | The context owner defines identity and any composite-basis relation. The calculus chooses exact basis binding; each referenced owner retains its meaning and grants. |
| Constraint and judgment: [AC-007](#ac-007-constraint-and-refusal), [AC-014](#ac-014-judgment-separation) | A constraint supplies its own predicate; evidence supports that predicate on an unchanged subject (F2/F3/F6), while finite evaluation admits missing support and non-performance (F5). The axiomatic representation must therefore retain the predicate, cause, performance and effects. A refused operation does not determine the unevaluated constraint's truth. | Foundations owns the result algebra. This calculus owns the judgment record and cause-sensitive mappings; the interpretation binds each domain predicate. Admission and acceptance additionally require their own competent decision mandate. |
| Latitude and residuals: [AC-008](#ac-008-explicit-latitude), [AC-009](#ac-009-residual-conservation) | Information-preserving interpretation must distinguish permitted variation from unresolved meaning (F2/F4); uncertainty creates no permission or disposition authority (F5/F6). Removing a residual from a view therefore cannot resolve it, and an implementation preference cannot supply latitude. | The calculus chooses explicit `L` and `X` records. Subject and interpretation authorities determine the allowed variation, material residuals and authorized successor dispositions. |
| Task closure and projection: [AC-010](#ac-010-material-closure), [AC-011](#ac-011-projection) | A reference frame needs the dependencies material to its question within finite capacity (F1/F2/F5); algebraic conservation keeps those dependencies and their external seams intact (F4). A selected view can support that question only through its exact `Z`, `R`, closure and boundary. Capacity does not authorize dropping a required member. | The calculus chooses least-fixed-point closure and `Boundary_Z`. The applying interpretation selects seeds and required-edge semantics; finiteness and uniqueness remain conditions to establish, not consequences of F5 or claims of minimum acquisition cost. |
| Overlay and transformation: [AC-012](#ac-012-overlay), [AC-013](#ac-013-transformation) | Algebraic and functional composition preserve declared relations across exact source and target identities (F3/F4). Authority belongs to the bound operation, not to the resulting bytes (F6). Consequently an overlay cannot mutate its basis, and producing a successor does not admit it. | This calculus chooses typed overlays and total local/external delta accounting. The transformation owner binds the equality witnesses, authorized loss and operation grant; these choices do not establish categorical functor laws. |
| Traversal classification and composition: [AC-015](#ac-015-functor-classification), [AC-016](#ac-016-typed-composition) | Computational execution binding distinguishes an operation from its actor and mechanism. Typed composition preserves each traversal's preconditions, judgments, stops and material effects (F4/F6); a shared executor cannot turn a proposal into assessment or adjudication. | This calculus chooses `F_D`, `F_P`, `F_H` and bracketed traversal identity. The application selects the lawful topology and outer predicate; no universal kind sequence or category-theoretic status follows. |
| Interpretation and model validity: [AC-017](#ac-017-interpretation-fidelity), [AC-018](#ac-018-structural-and-semantic-separation), [AC-019](#ac-019-valid-model) | Information and interpretation distinguish encoded structure from the subject's meaning (F2), and evidence supports only its tested claim (F6). Thus a structurally valid model may still omit a governing premise, narrow latitude or conceal a residual; those defects remain fidelity failures under the declared use. | The interpretation authority selects material subject declarations and admitted loss. This calculus chooses source-linked treatment dispositions and requires each applicable validity relation; the shared projection and conjunction laws decide preservation and combination. |
| Layer and release separation: [AC-020](#ac-020-layer-and-release-separation) | Specification ownership, identity and authority keep calculus, interpreted model and encoded carrier distinct (F3/F6). Evidence about one layer cannot accept another or confer Product standing. | This calculus chooses separately bound layer identities and judgments. Downstream Product authorities select applications, carriers, acceptance and release. |

### AC-001 Closed Signature

Every admitted object, relation, constraint, latitude, residual, traversal,
transformation specialization, and judgment belongs to one declared signature.
Every fundamental record also occurs exactly once in the total
`Population_M` function under its declared `RecordKind_ac`. Missing, duplicate,
shadowed, or unknown record kinds and populations fail closed.

### AC-002 Scoped Identity

An identity resolves one member under one type, context, owner, scope, and
basis. Equal spelling, payload equality, graph position, or carrier equality
does not establish semantic identity.

### AC-003 Reference Closure

Every referenced identity resolves exactly once in the applicable model or
through one explicit external relation. Resolution uses the exact
`RefDomain_Sigma(source_record_kind, field)` declaration across the model's
record populations. Dangling, duplicate, wrong-record-kind, wrong-sort,
wrong-basis, locally-and-externally ambiguous, or undeclared-field references
refuse structural admission.

### AC-004 Relation Typing

A relation is lawful only when its kind admits the exact source and target
sorts and all required qualifiers are present. Direction is material unless the
relation kind explicitly declares symmetry.

### AC-005 Authority Conservation

Objects, relations, constraints, latitude, residuals, traversals,
transformations, projections, and judgments retain their declared semantic,
operation, evaluation, and decision authority. Copying, interpreting, encoding,
evaluating, or transporting a record does not transfer authority.

### AC-006 Basis Coherence

Every fundamental record, model, and result binds an exact basis. Mixed bases
require an explicitly owned composite-basis relation. Individually valid
coordinates do not create a coherent composite basis by proximity.

### AC-007 Constraint And Refusal

Each `Constraint` binds its `applies_to`, `predicate`, `basis`, `judgment_kind`,
`latitude_ref` and `refusal` to [Evaluate](TRANSFORMATION_LIBRARY.md#evaluate).
The [core result](FOUNDATIONS.md#result-algebra) owns all five verdict meanings,
legal performance pairs, effects and missing-reason handling; AC-014 carries
that record. The constraint's declared predicate on `applies_to` is the evaluated
claim. Its reason domain and mapping are:

| Supported constraint-evaluation case | Core verdict |
|---|---|
| the exact predicate is established under its governing latitude | `satisfied` |
| an admissible counterexample defeats that predicate | `falsified` |
| evidence cannot decide that predicate, including a missing required reason | `indeterminate` |
| deciding the predicate needs material scope or capability outside the evaluation contract | `out_of_frame` |
| its subject or governing basis cannot support interpretation of the predicate | `invalid_basis` |

The core diagnosis and missing-reason rules retain independent counterevidence;
multiple required predicates use core conjunction, not an arbitrary row choice.

The outcome shorthands used by projection, transformation, interpretation and
admission below retain their original meaning and bind the predicate actually
claimed. A returned projection, proposed successor or model candidate maps to
`satisfied` only when its declared production predicate is established; absence
of a required output defeats that predicate only when supported by its contract
and evidence. `accepted` and `admitted` use the core decision predicate over the
exact unchanged subject, mandate and bound authority. A supported lawful
decision maps to `satisfied`; an established violation of that decision contract
maps to `falsified`; an undecided decision or grant maps to `indeterminate`.
Scope/capability and unusable-basis diagnoses map to `out_of_frame` and
`invalid_basis` on the evaluation that lacks them. Missing causes use the core
missing-reason rule. None of these outcomes establishes another model's
semantic truth or upgrades its own actual performance or effects.

`hold`, `gap`, `refusal` and `refuse` always carry a declared cause: an undecided
predicate maps to `indeterminate`; missing material frame scope or capability
to `out_of_frame`; an unusable basis to `invalid_basis`; and an admissible
counterexample to that predicate to `falsified`. An established prohibition
falsifies only the permission or admission predicate it defeats. Refusing an
interpreter because its grant is absent does not falsify the model's constraint
predicate. On that constraint, retain the actual evaluation performance and
any separately admissible counterevidence or supported scope/basis diagnosis;
without deciding support the unevaluated predicate remains `indeterminate`.
The refusal of permission is a separately bound result.

The pair of original outcome and cause, not the shorthand alone, identifies one
refinement case. A bare stop word cannot satisfy a consumer. Implementations
bind these mappings before execution and retain performance, known effects,
evidence and residuals.

### AC-008 Explicit Latitude

Two values may differ lawfully only through an applicable latitude or
transformation relation. An implementation preference, probabilistic choice,
or human presence is not implicit latitude.

### AC-009 Residual Conservation

Every material uncertainty, omission, translation loss, unresolved boundary,
or unproven relation remains in `X` until an authorized disposition creates an
exact successor model. Absence from a projection is not resolution.

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

### AC-011 Projection

A projection selects an exact view without changing selected meaning. Apply
[Faithful projection](TRANSFORMATION_LIBRARY.md#faithful-projection) from model
`M` to that view for the declared consumer task:

```text
project(M, Z, R) -> (M_Z, Boundary_Z) | gap | refusal
```

`M_Z` contains AC-010's material closure of `Z` under `R`. `Boundary_Z` records
excluded, external, unresolved, translated and invalidation-sensitive seams.
Those coordinates bind the shared contract's support and loss boundary; a
carrier or capability budget supplies no permission to trim required members.

### AC-012 Overlay

An overlay adds explicit records to one or more declared `Population_M`
families of a basis model. It does not mutate the basis. Override,
disambiguation, equivalence, specialization, or translation exists only as a
typed relation with exact authority, direction, scope, basis, preservation,
loss, refusal, and invalidation semantics.

### AC-013 Transformation

A transformation is an operation-bearing specialization of one exact traversal
record `v`:

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

`t.traversal` resolves one `v`; its context, owner, scope, basis, operation
authority, evidence, provenance, and stop contract must equal or lawfully
restrict the corresponding traversal coordinates. A broader or mismatched
coordinate refuses.

`domain_model` and `codomain_model` resolve exact content identities of the
complete input and proposed successor models. Each model identity commits to
its exact calculus basis, signature identity, complete finite `Population_M`,
complete `External_M`, exact external-resolution map, and selected
model-content identity under the owning identity law. A mutable locator,
model-family name, partial projection, or population digest without the exact
model identity refuses.

For each `x in External_M`, the model's exact resolution relation determines:

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
resolution tuple in one model; a missing, ambiguous, or extra tuple refuses.

For an ordinary same-basis transformation:

```text
basis(domain_model) = basis(codomain_model) = t.basis = basis(t.traversal)
signature(domain_model) = signature(codomain_model)
```

A cross-basis or cross-signature migration requires a separately identified
transformation specialization whose exact composite-basis and compatible
signature-extension relations name both sides. No identity whose basis or
record kind changes belongs to `preserved`; the source identity is removed and
the successor identity is introduced, with their continuity represented only
by the exact migration relation.

`preservation_relation` resolves one exact typed equality relation applicable
to the declared domain and codomain model identities and record kinds. It binds
both model identities, both exact bases, comparison domain, direction,
authority, scope, evidence, and equality law. Equivalence or
meaning-preservation may relate a removed identity to an introduced identity;
it cannot retain one identity in `preserved`.

Let `Local_b` be the complete input-model local-record identity set, `P_t` the
identities named by `preserved`, `R_t` those named by `removed`, and `N_t` the
identities of the complete records named by `introduced`. A lawful
transformation proves the closed local-record delta:

```text
Local_b       = P_t disjoint_union R_t
Local_b_prime = P_t disjoint_union N_t
N_t intersect Local_b = empty
R_t intersect Local_b_prime = empty
```

For every identity in `P_t`, the input and successor records have the same
record kind, identity, context, owner, scope, and basis. They are either:

1. byte-identical under one exact canonical record grammar selected for both
   models; or
2. equal under the exact `preservation_relation` when the abstract records do
   not share such a byte grammar.

Canonical-byte equality and typed record equality are alternative proofs of
identity preservation, not carrier selection by the calculus. A changed field,
changed basis, changed record kind, nominally equal identifier, equivalence,
or unbound assertion of preserved meaning refuses membership in `P_t`.

Every removed identity is absent from the successor. Every introduced identity
is absent from the input and carries a complete lawful record in exactly one
successor population. Every input local-record identity is classified exactly
once as preserved or removed; no local record may be silently dropped,
retained, or duplicated.

The external-resolution coordinates form a distinct closed delta. Let `E_b`
and `E_b_prime` be `ResolutionSet_M` for the domain and codomain models;
`EP_t`, `ER_t`, and `EN_t` are exactly the resolution coordinates named by
`external_preserved`, `external_removed`, and `external_introduced`:

```text
E_b       = EP_t disjoint_union ER_t
E_b_prime = EP_t disjoint_union EN_t
EN_t intersect E_b = empty
ER_t intersect E_b_prime = empty
```

For every `x in EP_t`, `external_resolution_witnesses` contains exactly one:

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

The two resolution tuples are exactly field-equal. A nominally equal external
identifier, equivalent target, changed target kind, changed resolved target,
changed reference domain, changed basis relation, changed resolution basis, or
missing witness cannot enter `EP_t`. Every member of `ER_t` has its complete
resolution only in the domain model; every member of `EN_t` has its complete
resolution only in the codomain model. A changed external resolution is a
removal followed by introduction of the new resolution coordinate and any
separately declared continuity relation; the referenced external identity may
remain unchanged, but the resolution is not preserved. Witnesses are total and
unique over `EP_t` and name no other resolution coordinate.

Material residuals remain in the successor residual set unless an exact
authorized disposition is included in the transformation evidence. Failure to
establish any model identity, basis, population, local or external partition,
equality, external-resolution witness, residual, or codomain equation refuses.

Application is:

```text
T[t](M_b, inputs) -> M_b_prime* | hold | gap | refusal
```

The exact transformation identity `t` declares every mutation it may perform.
The input model remains unchanged; `M_b_prime*` is a proposed successor. A
proposed successor does not accept or admit itself.

### AC-014 Judgment Separation

Under F2, F3 and F6, evidence about an exact subject and an authorized decision
about it cannot acquire the identity or authority of a changed subject.
Consequently a judgment retains its predicate and unchanged subject. This
calculus chooses the record fields below; Foundations owns their result
semantics, and the interpretation owner binds domain decisions before use.

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
  predicate,
  verdict,
  decision,
  performance,
  effects,
  evidence,
  residuals,
  provenance,
  decided_at
}
```

Issuing a judgment does not transform, rewrite, reissue, or rename its subject.
Promotion is an explicit relation between the unchanged subject and its
admission or acceptance judgment.

`predicate`, `verdict`, `performance`, `effects`, `evidence` and `residuals`
bind the shared result contract. `decision` retains the original calculus or
interpreted-domain outcome; it is not another verdict enum. The exact
interpretation declares its map before the judgment is used. A carrier may
encode these relations through resolved records rather than repeated bodies.
Each field is required by this semantic contract. The selected signature closes
its value domain, cardinality and identity-bearing reference domains. The core
result contract determines performance, observed extent and effect state.

`predicate` resolves the adopted predicate contract; identity-bearing
`residuals` resolve the calculus's existing residual records. `effects` records
the shared effect state at the boundary named by that predicate and its
evidence. Existing subject, evidence and provenance identities identify the
observed operation and owning observation; this relation introduces no nested
effect-identity schema. These are semantic obligations of the selected
calculus contract, not a mandatory serialisation layout for every external
model or carrier. A subject interpretation declares its exact bindings.

An external checker remains bound to its own released schema and semantics.
Passing an older pinned checker proves only that checker's declared predicate.
It does not silently upgrade an older judgment record to this successor
contract, or establish semantic acceptance of an `a_c.X` interpretation.

## Traversals And Functor Kinds

F2 and F6 distinguish evidence, proposals and authorized decisions; F4 requires
typed composition preserving each constituent claim; F5 requires explicit
handling of undecidable work. Given those premises, AC-015–016 require exact
traversal contracts and preserved stops and joins. This calculus additionally
chooses the three `F_D`, `F_P`, `F_H` kinds and bracketed identity syntax. Each
application owner chooses its traversal topology and operator under
[Composition law](TRANSFORMATION_LIBRARY.md#composition-law); neither that law
nor the three-kind classification proves categorical functor laws.

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
refinement. The traversal binds each outcome in `Y_v` or `Omega_v` to one core
verdict on an explicit predicate and preserves the original outcome. Its
declared domain includes graceful refusal, uncertainty and recovery or
termination dispositions for observations it cannot decide. This total
handling contract does not prove an external actor or world will terminate.

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

For a construction traversal, satisfying `an exact candidate is available`
does not satisfy `the candidate conforms` or `the candidate is accepted`.
Evaluation and authorised disposition require their own predicates and
evidence. Likewise, a completed human decision records that exact decision;
human presence does not turn a rejected candidate into a conforming one.

### AC-015 Functor Classification

Every functor application binds exactly one functor kind and one traversal
identity. Applying any `F_*` kind without bracketed traversal identity `[v]` is
incomplete.

### AC-016 Typed Composition

Apply [Composition law](TRANSFORMATION_LIBRARY.md#composition-law) to the two
exact traversal contracts:

```text
F_K2[w] compose F_K1[v]
```

The typed join requires `v`'s result type and judgment to satisfy `w`'s domain
and preconditions. Bind the outer predicate to the required leaf predicates,
intermediate results and material joins, retaining both traversal identities,
judgments, evidence, authority, provenance and stop states. Its result uses the
core conjunction or declared-operator rule selected by that predicate; its
effect boundary includes the traversals' material effects under the shared
currentness law.

The kinds retain their distinct proposal, evaluation and human-decision
contracts. `a_c` prescribes no universal `F_P -> F_D -> F_H` sequence. An
application chooses its lawful topology and outer operator without changing
the constituent predicates or AC-007 refinements. Categorical claims additionally
meet the complete demonstration standard in
[Orthogonal descriptions](FOUNDATIONS.md#orthogonal-descriptions).

## Interpretation And Models

F1 selects a use, F2 requires meaning supported by an exact subject, F3 keeps
that subject distinct from a representation, F4 preserves material dependencies,
F5 retains what cannot be decided, and F6 separates structural evidence from
semantic authority. If AC-017–019 claim a faithful valid model for that use,
source meaning and unresolved conditions must survive the declared relation.
This calculus selects the provenance, constraint-surface and validity conditions
below. The interpretation owner separately chooses the subject, signature,
material selection and admitted loss; competent source and acceptance owners
retain those decisions. No generic checker supplies that semantic selection.

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

Apply [Faithful projection](TRANSFORMATION_LIBRARY.md#faithful-projection)
with the exact subject declarations as source, the selected signature and
interpretation contract as target meaning, and the declared use of `M_subject`
as consumer. Every admitted record maps to exact subject provenance or is
identified as model-local content under competent authority. Every evaluated
declaration has a retained, omitted, residual, inapplicable or refused
disposition; omission or inapplicability needs its recorded basis and authority.

Those five dispositions are declaration-treatment data, not five verdicts.
For each claimed treatment, evaluate “this treatment preserves the declaration's
material meaning for the declared use under the interpretation contract”.
Established preservation, including authorized omission or admitted loss, maps
to `satisfied`; an admissible fidelity counterexample maps to `falsified`;
undecided preservation, authority or materiality maps to `indeterminate`.
Missing evaluation scope/capability maps to `out_of_frame`; an unusable subject
or interpretation basis maps to `invalid_basis`; a missing reason uses AC-007's
core missing-reason rule. The overall fidelity claim conjoins its required
declaration and dependency predicates under core conjunction. Faithfully
representing a source uncertainty can satisfy fidelity while the source claim
remains unresolved. A refused treatment's permission result is separately
bound; it does not determine the source predicate's truth.

The interpretation preserves source logic through the existing populations:
`O` identifies the subject objects and meanings; `E` carries typed dependency
and preservation relations; `C` binds predicates and consequences; `L` states
permitted and forbidden variation; `X` retains unresolved conditions and their
consequences; and `V`, `T` and `J` bind operations, transformations and judgments.
Signature-defined sorts, qualifiers and predicates distinguish premises,
derived consequences, policy choices, observations and unresolved claims.
This adds no record family or fixed dependency-tree shape.

A task consumes that model through AC-011, selecting `Z` for its question and
`R` for the material dependency closure. The resulting view and `Boundary_Z`
instantiate the library's [Constraint surface](TRANSFORMATION_LIBRARY.md#constraint-surface):
the source-owned obligations, permitted choices, required evidence and open
conditions remain recoverable. The consumer separately acquires the actual
material subject and authoritative inputs under its applicable acquisition
owner; an activated reference-frame consumer uses the Frame Method. Model facts
are claims with source/currentness support, not the world state or an effect
grant. Changing observations reopens affected reliance under the shared
currentness rule; unchanged independent support remains reusable.

Fidelity evidence compares source and model on independently specified
permissible, prohibited and unresolved decisions for the claimed scope. The
model retains latitude material to that use unless the interpretation contract
records admitted loss with basis and authority. A model or task projection that
omits a required premise, turns an unknown into permission, or narrows source
latitude to the author's preferred implementation without that admitted loss
fails that relation even if its structure validates. The selected source,
interpretation, projection and admitted approximation bounds identify the
scope of this evidence.

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

## Subject And Carrier Boundaries

F2 and F3 distinguish interpreted meaning from its carriers and content identity;
F4 requires declared preservation across their joins; F6 keeps acceptance with
the granted owner. Consequently evidence for one layer cannot ratify another.
AC-020 and [Exact Calculus Identity](#exact-calculus-identity) add this member's
three-layer split, exact equality and canonical identity policies. The external
Product/release owner separately chooses whether to accept or release any
layer; the encoding owner chooses a lawful carrier under that basis.

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

The exact historical addresses and byte predicates can resolve through
successor-owned [derivation verification material](IDENTITY_METHOD.md#derivation-verification-material).
Its immutable publication membership binds the evidence; its reconstructed
historical bytes bind the original predecessor manifest and fragments. This
resolution keeps the derivation record and its identity unchanged and requires
no predecessor installation or remote retrieval. Evidence does not make the
historical clauses operative for a successor consumer.

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

## Application Boundary

This standard defines the generic relations `a_c.X` and `a_c.X.C`. It selects,
constructs, accepts, or releases no concrete interpretation or carrier. A
downstream authority owns its exact subject population, interpretation,
carrier, judgments, and Product or release status. The downstream identity is
never embedded back into the calculus or its publication basis.

## External Imports And Specializations

An application may declare a typed import, translation, or specialization of
an `a_c` concept under that application's own exact authority, context, basis,
scope, preservation, loss, refusal, and invalidation law. Such a relation is
external to the calculus. It neither changes `a_c` nor enters this standard by
being useful to an application.

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
