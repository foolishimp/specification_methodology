# Axiom Indexer Project Reference-Frame Basis

Status: Accepted source-project basis, revision 3.

## Project Frame Basis

This declaration instantiates four read-only project frames for constitutional
extraction. It is a project configuration under the exact
STDO Reference Frame Method; it does not redefine that method or adopt an
optional role profile.

```text
frame_set_id = "urn:axiom-indexer:frame-set:constitutional-extraction:3"
method_basis = "stdo://releases/v2.4.3-rc.3/standards/REFERENCE_FRAME_METHOD.md"
method_sha256 = "sha256:a270453802ae03d6871c408d782094180b938aca22399ce817451fdd4551b174"
spec_method_basis = "stdo://releases/v2.4.3-rc.3/standards/SPEC_METHOD.md#collective-reference-frame-basis"
spec_method_sha256 = "sha256:50b825969ae23c5a42f7f3776fd2ab4146836349dfd4ef7a548dc2b6349b389c"
release_manifest_sha256 = "sha256:312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551"
governed_subject = "urn:axiom-indexer:bounded-context:product"
governed_outcome = "target-neutral constitutional extraction"
frame_set_authority = "urn:axiom-indexer:authority:product-owner"
frame_set_grant = "urn:axiom-indexer:grant:product-owner:1"
acceptance_record = "../.ai-workspace/decisions/20260829T184859_frame_basis_acceptance.json"
```

The Product authority and the digest-bound acceptance record admit this frame
set. Goals, Intent, Product, and requirements listed below are material basis
sources. Their inclusion supplies no frame-set, semantic, operation, or
decision authority.

## Governed Workspace And Basis Law

The governed workspace is the resolved Axiom Indexer source-project root. Each
activation shall bind:

- the exact candidate subject URI and content digest;
- this frame-set identity, revision, selected frame identity, declaration URI,
  and declaration content digest;
- the exact repository or source-project basis on which the candidate exists;
- the STDO release and method identities above;
- every material source URI and content digest required by the selected frame;
- the exact evaluation, actor identity, capability envelope, evaluation grant,
  evidence-acquisition boundary, and stop states; and
- any required assurance-independence conditions.

An unresolved or mutable method basis, missing material source, frame-
declaration mismatch, subject/digest mismatch, or ambiguous bounded context
returns `invalid_basis` before evaluation. A changed frame declaration,
subject, material-source byte set, actor, evidence boundary, or activation
grant requires a fresh activation.

## Known Evaluation Inventory

| Evaluation | Predicate | Material sources |
|---|---|---|
| `E-PRODUCT-BOUNDARY` | The candidate preserves the common Product, target-profile, carrier-tenant, target-Product, and consumer boundaries. | `GOALS.md`, `INTENT.md`, `PRODUCT.md` |
| `E-ALGEBRA-CLOSURE` | The candidate closes identities, references, accepted-population lineage, constraints, latitude, residuals, judgments, and source routes under the selected calculus and target profile. | `PRODUCT.md`; basis, algebra, selection, and projection requirements |
| `E-AUTHORITY-SEPARATION` | Proposal, structural inspection, semantic selection, encoding, carrier admission, artifact acceptance, release, invocation, and downstream decision authority remain distinct. | `PRODUCT.md`; compilation, selection, carrier, and projection requirements |
| `E-TARGET-CARRIER-ISOLATION` | Target meaning cannot select or be reshaped by carrier mechanics, and carrier law cannot ratify semantics. | `PRODUCT.md`; basis, algebra, carrier, and projection requirements |

Known material interactions are compilation-to-selection-to-encoding-to-
admission, candidate-to-accepted-population conservation, target-to-carrier
independence, and accepted-parent-to-projection closure. Frame-declaration and
activation validity are preconditions governed by the shared basis law above,
not an additional evaluation in this inventory.

## Shared Frame Relations

These relations are inherited by each declaration below and complete its
`F = <Q,B,M,C,I,A,E,X,R,J,K,D>` tuple.

### Coordinates And Equality `C`

Material identities are compared by exact semantic address, content digest,
bounded context, owner, scope, and basis. Same spelling, filename, or prose is
not equality. Cross-surface claims require exact cited relations rather than
textual similarity.

### Authority `A`

- Source owners and the current WHAT surfaces own their meaning.
- The frame-set authority declares and accepts this reusable configuration.
- An exact work instruction grants a capable actor read-only evaluation
  authority for one activation.
- These frames declare no operation authority.
- The activated evaluator returns a result and cannot accept the Product,
  semantic subject, artifact, or release.
- The Product owner retains disposition authority over source-project changes.
- Actor, semantic, evaluation, operation, and decision identities never
  collapse by role name or participation.

### Evidence `E`

Admissible evidence consists of exact candidate and basis bytes or immutable
reacquisition routes, semantic-addressed citations, explicit counterexamples,
and independently identified judgments or receipts where required. Hashes,
schema success, parsing, and deterministic structural checks prove only their
declared properties. They cannot prove semantic sufficiency or acceptance.

### Results `R`

Every completed evaluation returns exactly one of:

- `satisfied`;
- `falsified` with at least one material counterexample;
- `indeterminate` with the undecidable evidence boundary;
- `out_of_frame` with the missing material relation or capability; or
- `invalid_basis` with the failed subject or basis relation.

`activation_refusal` is a pre-evaluation outcome, not an evaluation result. It
applies when actor capability, evaluation authority, independence, or the
evidence-acquisition boundary is absent or conflicting.

### Invalidation And Revision `J`

An activation is invalidated by any change to its subject, basis, actor,
capability, grant, evidence law, or required material bytes. This frame-set
declaration requires revision and new acceptance when the governing STDO
method, evaluation inventory, frame tuple, authority split, capability law,
result algebra, material topology, coverage map, or known blind spots change.

### Common Capability Envelope `K`

The actor must fit the bounded material surface; resolve and verify the exact
STDO and project bases; traverse semantic addresses and authority relations;
distinguish probabilistic proposal, semantic adjudication, deterministic
inspection, construction, and admission; cite exact evidence; retain
uncertainty; and refuse when the frame is insufficient. No ambient
conversation history may be required.

## Frame Declarations

### `F-PRODUCT-BOUNDARY`

- `Q`: evaluate `E-PRODUCT-BOUNDARY`.
- `B`: exact candidate plus Goals, Intent, Product, and this declaration.
- `M`: Product terms, owned capabilities, extension axes, outputs, non-goals,
  target/tenant/consumer relations, and source-project authority.
- `I`: target neutrality, carrier neutrality, one common Product authority,
  and no unselected target, carrier, implementation, artifact, or release.
- `X`: generated views, comments, target-specific precedent, and implementation
  convenience cannot redefine the common Product.
- `K`: common envelope plus Product-boundary and recursive-Product-taxonomy
  competence.
- `D`: overlaps `F-AUTHORITY-SEPARATION` and
  `F-TARGET-CARRIER-ISOLATION`; its closed result may feed a Product-owner
  disposition but does not decide it.

### `F-ALGEBRA-CLOSURE`

- `Q`: evaluate `E-ALGEBRA-CLOSURE`.
- `B`: exact candidate plus Product and the basis, algebra, selection, and
  projection requirements; a selected calculus or target profile is mandatory
  when the subject claims their concrete conformance.
- `M`: candidate population, accepted model, source bindings, selection ledger,
  semantic-selection judgment, identities, references, constraints, latitude,
  residuals, projection closure, and re-entry routes.
- `I`: finite closed signature, unique typed resolution, total source-preserving
  candidate disposition, explicit uncertainty, and no silent semantic loss.
- `X`: cardinality alone, structural eligibility, carrier success, similarity,
  or omission-by-silence cannot establish semantic closure.
- `K`: common envelope plus competence in the selected calculus, identity law,
  fixed-point closure, and counterexample construction.
- `D`: consumes the exact accepted-population and projection claims and overlaps
  `F-AUTHORITY-SEPARATION` at the semantic-selection gate.

### `F-AUTHORITY-SEPARATION`

- `Q`: evaluate `E-AUTHORITY-SEPARATION`.
- `B`: exact candidate plus Product and compilation, selection, carrier, and
  projection requirements.
- `M`: actors, subjects, grants, evidence boundaries, judgments, construction
  operations, admissions, acceptances, release, invocation, and closure.
- `I`: semantic compilation proposes; structural inspection proves only
  declared form; semantic selection issues an external exact-subject judgment;
  encoding constructs under that judgment; carrier admission judges unchanged
  bytes; downstream owners retain their own authority.
- `X`: authorship, visibility, human presence, schema success, successful use,
  deterministic admission, or role labels cannot mint authority.
- `K`: common envelope plus authority-graph, judgment-identity, and operation-
  versus-evaluation competence.
- `D`: overlaps every other frame where a material claim could collapse owner,
  evaluator, constructor, admitter, or disposer.

### `F-TARGET-CARRIER-ISOLATION`

- `Q`: evaluate `E-TARGET-CARRIER-ISOLATION`.
- `B`: exact candidate plus Product and basis, algebra, carrier, and projection
  requirements; selected target and carrier profiles are required only when a
  concrete extension is being evaluated.
- `M`: target population and interpretation laws, common accepted semantics,
  carrier mappings, canonicalization, admission, projection encoding, gaps,
  and refusal paths.
- `I`: target profiles do not select carriers; carrier profiles do not shape
  compilation or accepted meaning; unsupported accepted meaning produces an
  explicit carrier gap or refusal.
- `X`: first-implementation precedent, carrier schema, token budget, storage,
  and runtime convenience cannot become semantic-selection input.
- `K`: common envelope plus target/profile and carrier/admission boundary
  competence.
- `D`: overlaps `F-PRODUCT-BOUNDARY` and `F-AUTHORITY-SEPARATION`; a selected
  target or carrier may add separately owned specialist frames.

## Coverage, Exclusions And Residuals

| Evaluation or interaction | Primary frame | Overlapping frame | Coverage status | Residual |
|---|---|---|---|---|
| Product and extension boundary | `F-PRODUCT-BOUNDARY` | `F-TARGET-CARRIER-ISOLATION` | covered | Concrete target, tenant, and consumer claims require their own selected bases. |
| Candidate and accepted-program closure | `F-ALGEBRA-CLOSURE` | `F-AUTHORITY-SEPARATION` | covered | Concrete calculus conformance requires a selected calculus basis. |
| Proposal, judgment, construction, and admission chain | `F-AUTHORITY-SEPARATION` | `F-ALGEBRA-CLOSURE` | covered | Effectful realization and downstream authority require separate frames. |
| Target/carrier bidirectional isolation | `F-TARGET-CARRIER-ISOLATION` | `F-PRODUCT-BOUNDARY` | covered | Concrete profile conformance requires selected target and carrier bases. |
| Accepted parent and bounded projection | `F-ALGEBRA-CLOSURE` | `F-TARGET-CARRIER-ISOLATION` | covered | Runtime usefulness and invocation behavior remain downstream evaluations. |

This frame set covers the known constitutional-extraction evaluations above.
It does not claim universal completeness, design or implementation
qualification, calculus conformance without a selected calculus, target or
carrier conformance without their selected profiles, target-artifact
acceptance, release qualification, runtime behavior, or downstream migration.
Those are explicit residuals requiring fresh bases and, where material,
additional specialist frames. A discovered blind spot returns `out_of_frame`
and triggers frame-set repricing rather than silent expansion.
