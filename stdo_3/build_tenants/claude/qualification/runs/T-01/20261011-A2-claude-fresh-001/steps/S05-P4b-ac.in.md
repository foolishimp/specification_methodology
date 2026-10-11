STEP S05-P4b-ac | cap 20000 bytes | measured 11199 bytes | fits
ROUTES: AXIOMATIC_CALCULUS.md:ac-009-residual-conservation, AXIOMATIC_CALCULUS.md:ac-013-transformation, AXIOMATIC_CALCULUS.md:ac-005-authority-conservation
# Step card: FOUNDATIONS §3 route check

You are one bounded step of a larger check. You hold only this card, one or
more paragraphs of a draft standard (the tenant paragraphs, from FOUNDATIONS
§3) and, for each route, the section of the STDO v2.5.1-rc.2 member that the
paragraph cites (the rc.2 section). You cannot acquire anything else and you
have no memory of other steps. The line above this card states the byte size
of your whole input as measured before you were started.

## Task

For each route listed under ROUTES, judge whether the tenant paragraph's
characterisation of the cited rc.2 clause is consistent with the rc.2
section, under this contract. Consistent means all of:

1. nothing the tenant paragraph says about the cited clause contradicts a
   statement in the rc.2 section;
2. the rc.2 section's subject is the subject the tenant paragraph attributes
   to it;
3. where the tenant paragraph states an obligation as the clause's content,
   the rc.2 section states that obligation.

A paragraph that only names the clause as conserved, reframed or superseded
without restating its content is judged on 1 and 2 only; mark it "by
reference". A paragraph that restates content is judged on all three; mark
it "restated". Cross-paragraph relations within the rc.2 section are
material: judge over the whole section as given, never over a summary.

## Result algebra

Return exactly one member per route:

- satisfied: the contract holds on the given text;
- falsified: a statement in the given text defeats it; quote the statement;
- indeterminate: the given text is complete for the route but cannot decide
  it; say why;
- out_of_frame: deciding needs text or a relation not given to you, for
  example a definition in another section; name it;
- invalid_basis: the given material cannot support the judgment, for example
  a paragraph or section is missing or malformed.

Never report satisfied because material is missing or a point seems minor.
Do not shorten, summarise or skip any given text. Do not ask for more.

## Output

Return only these lines, nothing else:

ROUTE <member>#<slug> | <result> | <by reference | restated> | evidence: <one or two quoted phrases from the rc.2 section and the tenant statement they bear on> | residual: <none | text>

one line per route, then one final line:

STEP <step id from the first line of your input> | routes <count> | bytes_seen <the measured byte count from the first line of your input>

===== TENANT PARAGRAPH P4b (FOUNDATIONS §3) =====
P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them; sources a later step can re-acquire are governed by
sufficiency, not conservation. Derived from P0 with P2 and the
step-produced-facts premise. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each continues to govern its own scope.

===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-009-residual-conservation =====
### AC-009 Residual Conservation

Every material uncertainty, omission, translation loss, unresolved boundary,
or unproven relation remains in `X` until an authorized disposition creates an
exact successor model. Absence from a projection is not resolution.


===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-013-transformation =====
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


===== RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-005-authority-conservation =====
### AC-005 Authority Conservation

Objects, relations, constraints, latitude, residuals, traversals,
transformations, projections, and judgments retain their declared semantic,
operation, evaluation, and decision authority. Copying, interpreting, encoding,
evaluating, or transporting a record does not transfer authority.

