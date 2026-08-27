# STDO Representation Project Reference-Frame Basis

## Project Frame Basis

Identity:
`urn:stdo-representation:reference-frame-basis:source-project:2`

Status: acceptance-controlled project-defined configuration; this carrier
confers no acceptance

Proposed admitting authorities:

- `PRODUCT.md#product-authority` owns the Product-wide consumer, capability, and
  acceptance meaning projected here.
- `GOALS.md` owns the current bounded construction and repair outcomes.
- each active `REQ-P-*.md` requirement family owns the obligations evaluated by
  its applicable frames.
- an accepted tenant design owns only its carrier-specific construction frame.

This declaration projects those existing decisions. It creates no semantic,
operation, review, acceptance, or release authority of its own. Acceptance is a
separate exact `F_H` record under the gate below. Without such a record this is a
proposal and cannot open T-003; with one, the same unchanged bytes are the
accepted declaration.

## Exact method and project basis

- STDO release: `stdo://releases/v2.4.3-rc.3/`
- installed-manifest SHA-256:
  `312c84609866a4b8ea665bbbc87eb16ef3a3bb28acc234da6d081065af40d551`
- reference-frame method:
  `stdo://releases/v2.4.3-rc.3/standards/REFERENCE_FRAME_METHOD.md`
- baseline profile:
  `stdo://releases/v2.4.3-rc.3/standards/STDO_REFERENCE_FRAME_BASELINE.md`
- governed product definition:
  `urn:stdo:product-definition:stdo-representation`
- governed bounded context:
  `urn:stdo-representation:bounded-context:product`
- project configuration candidate authored: 2026-08-27

The governed outcome is an immutable, compact graph-and-constraint reasoning
program for `F_P` LLM consumption over separately supplied workspaces. This
frame basis governs the source project that defines, constructs, reviews, and
publishes that Product. It is not a reference frame encoded inside Source STDO
and is not a per-invocation LLM frame activation.

## Known evaluation inventory

| Evaluation | Material question | Governing owner |
|---|---|---|
| `E-PRODUCT` | Is the Product an ODD `F_P` reasoning program rather than a deterministic assessor or embedded runtime? | Intent and Product |
| `E-FUNCTIONS` | Are the exact Source STDO `F_D`, `F_P`, and `F_H` identities and their authority boundaries preserved? | Product and `REQ-P-FP-*` |
| `E-BASIS` | Are Source STDO, WHAT, tenant, carrier, profile, and content identities exact and non-cyclic? | Product identity and `REQ-P-BASIS-*` |
| `E-GRAPH` | Is the common representation a closed pure graph plus passive constraints with conserved source meaning? | `REQ-P-ALG-*` |
| `E-CONSUMER` | Can an LLM consume the program with a workspace, intent, frame, and budget without receiving false authority? | `REQ-P-FP-*` |
| `E-SELECTION` | Does durable `F_H` evidence bind the evaluated Source STDO population and every retained, omitted, or uncertain selection? | `REQ-P-SELECT-*` |
| `E-CARRIER` | Does a tenant realize the common program directly and lawfully in its exact carrier? | accepted tenant design and carrier authority |
| `E-COST` | Are byte, token, and cost reductions measured on exact comparable payloads? | `REQ-P-VERIFY-*` |
| `E-ASSURANCE` | Is the exact candidate independently reviewable, and are uncertainty and counterexamples visible to acceptance authority? | Product authority and selected STDO assurance law |

The inventory is current, not claimed universally complete. A newly discovered
material evaluation triggers the revision law below.

## Selected frames and capability envelopes

### `urn:stdo-representation:frame:product-boundary`

- Evaluation: `E-PRODUCT`.
- Intent: preserve the `F_P` program boundary and prevent assessment/runtime
  scope from entering the Product.
- Required capability: read exact Intent, Product, requirements, and consumer
  terminology; distinguish `F_P`, `F_D`, and `F_H` authority.
- Evidence: current constitutional surfaces and traced downstream design.
- Semantic and decision authority: Intent/Product owners; the frame only
  evaluates congruence.

### `urn:stdo-representation:frame:traversal-function-integrity`

- Evaluation: `E-FUNCTIONS`.
- Intent: prevent deterministic, probabilistic, and human traversal functions
  from being renamed, translated, collapsed, or granted one another's authority.
- Required capability: resolve the exact ODD `F_D`, `F_P`, and `F_H` identities,
  inspect the complete external traversal contract, and distinguish payload,
  invocation, structural evidence, semantic selection, and acceptance.
- Evidence: Product function binding, `REQ-P-FP-*`, invocation contracts,
  structural receipts, selection ledgers, and acceptance records.
- Semantic authority: Source STDO ODD Method. Evaluation authority: Product and
  `REQ-P-FP-*`. The frame cannot mint a local traversal function.

### `urn:stdo-representation:frame:basis-and-identity`

- Evaluation: `E-BASIS`.
- Intent: detect mutable, cross-basis, unresolved, cyclic, or invocation-bound
  Product identity.
- Required capability: resolve the installed release and carrier objects,
  reproduce manifests/digests, and reason over identity issuance order.
- Evidence: Product Definition, installed manifest, carrier basis, canonical
  program bytes, and one-way records referencing Product identity.
- Semantic and decision authority: Source STDO, Product identity requirements,
  and human Product acceptance.

### `urn:stdo-representation:frame:graph-and-constraint-fidelity`

- Evaluation: `E-GRAPH`.
- Intent: preserve semantic atoms, typed relations, passive constraints,
  bounded contexts, owners, scopes, and source routes without hidden carrier
  meaning.
- Required capability: semantic and graph-model analysis across the complete
  affected Source STDO span and common algebra.
- Evidence: source clauses, program declarations, source routes, and explicit
  adversarial seams such as equal spelling across contexts.
- Semantic authority: Source STDO. Evaluation authority: the applicable
  requirement owner. The frame cannot repair source ambiguity.

### `urn:stdo-representation:frame:fp-consumption`

- Evaluations: `E-CONSUMER` and the probabilistic part of `E-COST`.
- Intent: observe whether a capable LLM can reason over workspace inputs using
  the program at lower context cost while respecting declared constraints.
- Required capability: an `F_P` model with sufficient context, instruction
  following, semantic disambiguation, graph reasoning, and source-route use,
  plus a host capable of binding the complete ODD traversal contract.
- Evidence: exact program/workspace/intent/frame/model coordinates, target,
  gates, provenance, stop states, and retained outputs from representative and
  adversarial trials.
- Evaluation result: probabilistic observation with uncertainty and
  counterexamples; never deterministic semantic or closure truth.
- Decision authority: human Product authority decides whether observations are
  adequate for publication.

### `urn:stdo-representation:frame:carrier-realization`

- Evaluation: `E-CARRIER`.
- Intent: verify direct lawful realization in one exact carrier without a
  private dialect, rival authority, shared serialized IR, or runtime expansion.
- Required capability: complete knowledge of the selected carrier authority and
  the common program algebra.
- Evidence: accepted profile, canonical artifact, carrier validation, and exact
  mapping from `I_B`, `V_B`, `E_B`, and `C_B`.
- Operation authority: the accepted tenant work ticket and design only.

### `urn:stdo-representation:frame:semantic-selection`

- Evaluation: `E-SELECTION`.
- Intent: expose the human semantic compression boundary without pretending it
  is deterministic extraction or a complete occurrence census.
- Required capability: read every exact Source STDO standards member, author
  source-addressed declarations and omission rationale, record residual
  uncertainty, and distinguish `F_H` decision from `F_D` shape validation.
- Evidence: exact Semantic Selection Ledger, Source STDO manifest, program
  identity universe, authority identity and grant, and acceptance record.
- Decision authority: the exact `F_H` actor and grant named by the ledger;
  structural validation checks coordinates but cannot accept semantic choices.

### `urn:stdo-representation:frame:compression-measurement`

- Evaluation: deterministic portions of `E-COST`.
- Intent: reproduce byte, token, and price calculations over exact like-for-like
  consumer payloads.
- Required capability: reacquire exact bytes, tokenizer/version/configuration,
  and price basis and execute the declared counting procedure.
- Evidence: content identities, inventories, measurement procedure, and results.
- Limit: measurements cannot decide semantic usefulness.

### `urn:stdo-representation:frame:independent-assurance`

- Evaluation: `E-ASSURANCE` and independent activation over every other
  material evaluation before Product acceptance.
- Intent: challenge the exact candidate, claimed boundaries, hidden omissions,
  identity, token comparison, and `F_P` observations.
- Required capability: independent access to exact immutable bases and candidate
  bytes, applicable specialist competence, and no authorship of the reviewed
  candidate.
- Evidence: exact-subject review result with findings, uncertainty, and cited
  evidence.
- Acceptance authority remains human and is not transferred to the Reviewer.

## Actor binding and authority relations

- The Executive is the human Product/work authority or an explicitly bounded
  proxy capable of selecting work, frames, actors, and lawful re-entry.
- A Worker is a human, LLM, deterministic tool, or composition capable of the
  activated construction or evaluation. Capability never grants authority.
- An independent Reviewer must not have authored the exact candidate it reviews.
- One actor may occupy multiple non-independent frames in separate activations;
  claimed independent assurance requires a distinct eligible activation.
- Every activation binds exact subject, outcome, basis, frame, actor capability,
  evidence boundary, and expected result relation.

Source STDO retains semantic authority. Product and requirements retain
constitutional decision authority. Accepted design and ticket authority grant
bounded construction operations. Human Product authority alone accepts or
releases the resulting Product.

## Overlap, conjunction, and translation

- Product-boundary and graph-fidelity frames intentionally overlap on semantic
  scope so carrier or assessment concepts cannot silently redefine WHAT.
- Traversal-function integrity overlaps Product boundary, consumption,
  selection, and carrier realization so `F_D`, `F_P`, and `F_H` cannot absorb
  one another's authority.
- Basis-and-identity and carrier-realization frames intentionally overlap on
  exact carrier/profile coordinates.
- Compression measurement and `F_P` consumption remain separate: deterministic
  token reduction does not imply probabilistic usefulness, and one useful LLM
  response does not prove the measurement.
- Independent assurance is activated separately over the exact candidate and
  cited claims.
- Product acceptance conjoins exact-basis, graph/constraint, carrier,
  semantic-selection, measurement, and applicable `F_P` observations under
  human authority. No single frame supplies the whole decision.
- No semantic translation between frames is currently selected. A future
  translation must name source and target frame identities, owner, preserved and
  changed meaning, evidence, and invalidation conditions.

## Coverage and residual uncertainty

| Evaluation | Covering frames | Current residual |
|---|---|---|
| `E-PRODUCT` | product-boundary, independent-assurance | constitutional repair remains active until accepted |
| `E-FUNCTIONS` | traversal-function-integrity, product-boundary, independent-assurance | revised binding awaits exact frame/profile review |
| `E-BASIS` | basis-and-identity, independent-assurance | no released Product identity exists |
| `E-GRAPH` | graph-and-constraint-fidelity, independent-assurance | GTL mapping is proposed, not accepted |
| `E-CONSUMER` | fp-consumption, independent-assurance | no constructed program or frozen workspace trial exists |
| `E-SELECTION` | semantic-selection, independent-assurance | no accepted Semantic Selection Ledger exists |
| `E-CARRIER` | carrier-realization, independent-assurance | GTL is proposed; JSON Schema basis is unselected |
| `E-COST` | compression-measurement, fp-consumption, independent-assurance | no canonical program bytes exist to measure |
| `E-ASSURANCE` | independent-assurance | exact candidate review occurs only after construction |

These residuals prevent claims that depend on missing evidence. They do not
authorize a frame to absorb another owner's decision.

## Evidence coordinates

- Product Definition: `../stdo_representation.json`
- Intent and Product: `INTENT.md`, `PRODUCT.md`
- Common requirements: `requirements/`
- Semantic Selection Ledgers: future immutable records under the selected
  tenant's construction evidence surface
- Goals: `GOALS.md`
- Tickets: `../.ai-workspace/tickets/`
- Tenant designs and artifacts: `../build_tenants/<tenant>/`
- Exact Source STDO and carrier coordinates: the Product Definition and selected
  tenant basis/profile

Temporary conversation, hidden model context, and console-only output do not
replace those durable coordinates for an accepted claim.

## Invalidation, re-entry, and revision

This configuration is invalidated or requires revision when any of these change
materially:

- selected STDO or Reference Frame Method basis;
- Product intent, traversal-function binding, `F_P` consumer, program boundary,
  or authority allocation;
- graph-and-constraint algebra or identity issuance law;
- selected carrier basis or accepted representation profile;
- semantic-selection population or authority, Product acceptance claims,
  ordinary consumer payload, or measurement basis;
- actor capability or independence needed by a claimed evaluation; or
- a counterexample reveals a missing evaluation, frame, relation, or evidence
  boundary.

Re-entry goes to the first owning constitutional layer: Goals, Intent, Product,
Requirements, accepted Design, construction, or evidence. A frame may report
`out_of_frame`, `indeterminate`, or `invalid_basis`; it shall not enlarge itself
to decide an upstream authority gap.

## Acceptance gate

Acceptance requires an external `AuthorityAcceptanceRecord` conforming to
`PRODUCT.md#authority-acceptance-record` with:

- `subject_kind = "reference_frame_basis"`;
- this declared basis identity as `subject_identity`;
- the SHA-256 of this file's exact bytes as `subject_sha256`;
- the exact accepting human or bounded-proxy identity, authority identity and
  grant;
- the complete admitting-authority set recorded by the Product Definition;
- the selected STDO and frame-method basis; and
- an explicit `accepted` decision and decision time.

Until that record exists and the overlay authority set matches it, this basis
remains proposed and T-003 remains non-executable.
