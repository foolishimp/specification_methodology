STEP B-P4b | cap 40000 bytes | measured 25588 bytes | fits
BLOCKS: TENANT SECTION FOUNDATIONS §3 variant V, RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-009-residual-conservation, RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-013-transformation, RC.2 SECTION AXIOMATIC_CALCULUS.md#ac-005-authority-conservation, RC.2 SECTION DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017, RC.2 SECTION SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021
# Step card: route check of a tenant section

You are one bounded step of a larger check. You hold only this card, one
section of a draft standard (the tenant section) and, for each route, the
section of the STDO v2.5.1-rc.2 member that the tenant section cites (the
rc.2 section). You cannot acquire anything else and you have no memory of
other steps. The line above this card states the byte size of your whole
input as measured before you were started.

## Task

For each rc.2 section given, judge whether the tenant section's
characterisation of the cited rc.2 clause is consistent with the rc.2
section, under this contract. Consistent means all of:

1. nothing the tenant section says about the cited clause contradicts a
   statement in the rc.2 section;
2. the rc.2 section's subject is the subject the tenant section attributes
   to it;
3. where the tenant section states an obligation as the clause's content,
   the rc.2 section states that obligation.

A tenant section that only names the clause as conserved, reframed or
superseded without restating its content is judged on 1 and 2 only; mark it
"by reference". A tenant section that restates content is judged on all
three; mark it "restated". Cross-paragraph relations within the rc.2
section are material: judge over the whole section as given, never over a
summary. Judge only the sentences of the tenant section that concern the
cited clause; the rest of the tenant section is context.

## Result algebra

Return exactly one member per route:

- satisfied: the contract holds on the given text;
- falsified: a statement in the given text defeats it; quote the statement;
- indeterminate: the given text is complete for the route but cannot decide
  it; say why;
- out_of_frame: deciding needs text or a relation not given to you, for
  example a definition in another section; name it;
- invalid_basis: the given material cannot support the judgment, for example
  a section is missing or malformed.

Never report satisfied because material is missing or a point seems minor.
Do not shorten, summarise or skip any given text. Do not ask for more.

## Output

Return only these lines, nothing else:

ROUTE <member>#<slug> | <result> | <by reference | restated> | evidence: <one or two quoted phrases from the rc.2 section and the tenant statement they bear on> | residual: <none | text>

one line per route, then one final line:

STEP <step id from the first line of your input> | routes <count> | bytes_seen <the measured byte count from the first line of your input>

===== TENANT SECTION FOUNDATIONS §3 variant V =====
# FOUNDATIONS §3, variant V (test subject for case T-03-04)

This file is a fixture test subject, not a standard. It is FOUNDATIONS §3 of
the Claude tenant at digest 2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22
with one seeded change, declared in the case design. Nothing here is part of
the corpus under test; the corpus is applied to it.

## 3. Commitments

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope. The
actor's internal path within a step is its own. Recovered as a composite;
the generic statement is reframed from the ODD profile's graph functions.
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Independent: with purpose, identity, evidence and authority fixed, two
contracts give one representation two meanings. "Algorithmic" means explicit
and structurally checkable; a semantic decision is lawful only under an exact
decision contract; structural success never establishes fidelity. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit material
obligations from the transformation they serve; an obligation with no route
to the outcome is unjustified, and every activation declares a token
allowance before it begins, as UP-014 requires. Independent: identical
capacity serves opposite purposes. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; current state, historical observation and
representation identity stay separate; a boundary is a claim with a proof
obligation. Independent: equal capacity admits identity by persistence or by
digest. Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's domain and preconditions; composition
retains both identities, intermediate results, judgments, evidence,
authority, provenance and stop states. Independent. Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

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

P5 Totality. A step can meet a condition outside its context; it cannot
report success on one; so its result algebra carries indeterminate,
out_of_frame and invalid_basis as first-class outcomes and its control model
names the next move. Derived from P0 with the open-world premise and P6.
Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in CALCULUS §3 and continue to govern.

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope;
neither is minted by the other. Independent: a bounded actor satisfying all
else can still take a green label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004,
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).


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


===== RC.2 SECTION DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 =====
### Bounded Frame Conservation (`STDO-UP-017`)

`M(B)` closes one governed boundary. A bounded local action is taken inside a
frame that derives from other accepted frames, and its lawfulness depends on
relations the acting frame does not itself own.

`Global` and `local` are relative to the selected frame. Each material design
frame must identify:

- the governing frames and accepted relations from which it derives;
- the bounded affected relation set of the proposed action;
- the applicable inherited invariants;
- the authority and composition seams crossing that set; and
- the subordinate frames opened by unresolved material distinctions.

A frame may derive from more than one governing frame. A persistence component
belongs to an entity lifecycle boundary and an operational consistency
boundary; an admission function belongs to a domain transition and a
runtime-authority boundary; a shared callable may be consumed by several
sibling domains without becoming subordinate to one. A single governing frame
is lawful where the structure is genuinely hierarchical, and is not required.
Governing frames form a constraint network for the same reason `M(B)` does.

Every seam crossing the affected set must either include its causally relevant
far-side relation in that set, or state why that relation cannot affect, and
cannot be affected by, the bounded action. This makes the declared set testable
against its own declared seams without requiring a closure algorithm or
recursive expansion through irrelevant relations.

The result is evaluated against every affected governing frame, preserves each
applicable accepted relation, and updates only affected subordinate
projections. A bounded local action conserves governing truth; it does not
rewrite it. A result that changes a governing relation re-enters at that
relation before acceptance.

A subordinate frame opens only when a material distinction cannot be resolved
at the governing altitude. This rule does not require recursively documenting
irrelevant descendants.

This law is false if a change is locally valid inside the selected frame but
violates, duplicates, or silently reinterprets an invariant in any affected
governing frame.

Discovered functionality is evidence about required behavior. It is not yet an
architectural operation. A discovered verb, screen action, endpoint, command,
ticket phrase, or use case shall not be promoted directly into a public
operation identity, peer carrier, module, or implementation function. It must
first be derived through the Ontology.

The required derivation order is:

```text
constitutional functionality
  -> candidate Ontology
  -> logical completeness
  -> whole-family Prime contraction
  -> accepted Ontology basis
  -> Irreducible Architectural Carrier Set
  -> target design and domain, sequence, and state projections
  -> public contract and adapter projections
  -> implementation and test projections
```


===== RC.2 SECTION SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 =====
## Complete Enclosing-Relation Admission (`STDO-UP-021`)

For a material transition, each admission owner is independently responsible
for deriving and validating the complete enclosing relation from authoritative
inputs. The relation contains every participant and equality join whose
identity, validity, authority, currentness, or transition can affect or be
affected by admission; each crossing seam includes its relevant far side or
authoritatively establishes
that the far side cannot participate. Caller or owner assertions of
completeness, validity, prior admission, or authority do not establish truth.

An owner may consume established facts when their exact subject, basis, scope,
provenance and validity remain applicable to its relation. Their production and
invalidation must be recoverable; an unsupported assertion of prior success is
not such a fact. A function, component, role, conversation or status boundary
alone invalidates none of those coordinates and requires no repeated derivation.
Material mutation, rollback, changed authority or basis, expired validity, and
an actual trust boundary trigger the applicable validation before reliance or
effect. Reuse does not transfer the owner's admission responsibility, omit a
participant or satisfy a separately required independent judgment.

Derivation and validation bind one exact admission-valid authoritative basis
identity through admission. If validity or currentness can advance after
preflight, admission remains conditional on the declared predecessor and
currentness law for that basis or re-enters derivation and validation without
effect. Participating owners bind an equal basis or a design-declared coherent
composite basis; independently valid mixed-basis judgments cannot combine.

Every participant and join is validated before any transition effect. Internal
evaluation order and lawful reuse are implementation-owned, but no participant
subset or nested constituent becomes admitted truth. Admission is one semantic
commit of the complete transition, bound to its exact basis identity; failure
or interruption admits the complete transition or none, never a subset. No realization
mechanism or participant count is prescribed.

Direct and every supported composite or nested boundary preserve this law. A
partial result cannot substitute for an owner's derivation and validation, and
a competing same-scope path cannot establish the transition outside the
governing admission relation. Fresh reconstruction and replay over the same
basis reproduce the enclosing relation, basis identity, and complete outcome
or refusal exactly at semantic altitude.

This law is false if completeness is asserted rather than derived; a relevant
participant, join, or seam is omitted; validation and admission use an
unidentified, stale, or incoherently mixed basis; currentness can advance
without a commit condition or effect-free re-entry; any effect precedes
complete validation; failure or interruption exposes a subset; fresh
reconstruction differs; or competing same-scope authority remains.

### Standing Structural Qualification

Qualification is instantiated for every admission owner and supported boundary
declared by accepted design. Case applicability follows the supported input,
state and operating/threat model. An excluded threat alone cannot create an
acceptance predicate or require defensive work; any proposed scope expansion
returns to its owning authority. Supported malformed inputs, stale state and
effect boundaries retain their required checks:

| Form | Required observation |
|---|---|
| direct | the complete direct relation is derived, validated, and admitted once |
| supported composite / nested | every supported constituent and owning boundary satisfies the same law; unsupported forms have a design-grounded `not_applicable` disposition and no weaker or competing path |
| forged | forged identity, membership, equality, or authority reachable within the supported operating/threat model is refused without effect; exclusion requires its owning authority, not a helper's inability to construct the case |
| ambiguous enclosing relation | unresolved participant, join, seam, or relation identity ambiguity is refused without effect |
| stale / advanced basis | stale input is refused, and basis advancement between preflight and admission causes effect-free re-entry rather than mixed-basis admission |
| incoherent multi-owner basis | owner judgments on bases that are neither equal nor joined by a design-declared coherent composite basis cannot combine and are refused without effect |
| competing same-scope admission authority | an undisposed competing same-scope path cannot establish the transition |
| reconstructed / fresh-process | the same basis reconstructs the same relation, basis identity, and outcome or refusal |
| exact replay equality | replay over the same basis reproduces exactly the enclosing relation, basis identity, and complete outcome or refusal |
| atomic publication failure | after validation succeeds, failure or interruption is observed at every materially distinct commit or publication boundary capable of exposing a subset and followed by fresh reconstruction showing the complete transition or none; named representative observations suffice only under a design-declared dominance/equivalence proof covering the complete partial-failure surface |

For an indivisible commit unit, the atomic test establishes that boundary and
observes failure immediately on both sides. Final-participant validation
failure does not substitute for post-validation atomic-failure evidence. A
standing claim is false if an owner or supported boundary is omitted, a
materially distinct partial-failure boundary lacks an observation or declared
coverage proof, a case uses a weaker helper or manufactured refusal, or fresh
reconstruction does not compare the complete semantic result.

---

