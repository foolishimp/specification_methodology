# STDO Representation Project Reference-Frame Basis

## Project Frame Basis

Identity:
`urn:stdo-representation:reference-frame-basis:source-project:7`

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
separate exact `F_H[v_accept_frame_basis]` record under the gate below. Without
such a record this is a proposal and cannot open T-003; with one, the same
unchanged bytes are the accepted declaration.

## Exact method and project basis

- STDO release: `stdo://releases/v2.5.0-rc.1/`
- installed-manifest SHA-256:
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`
- standards-member count and aggregate: 51;
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`
- reference-frame method:
  `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md`;
  SHA-256 `90b5ea5e486c1c0e75883db5a15fba3f524cc5d5718c42108a548279e725d51f`
- baseline profile:
  `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md`;
  SHA-256 `f6a4e2be637df6c2dd5c69c6da7e77cefd8d8cde93af65ca686608ec43555e3f`
- axiomatic calculus:
  `stdo://releases/v2.5.0-rc.1/standards/AXIOMATIC_CALCULUS.md`;
  SHA-256 `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`
- governed product definition:
  `urn:stdo:product-definition:stdo-representation`
- governed bounded context:
  `urn:stdo-representation:bounded-context:product`
- project configuration candidate authored: 2026-08-30

The governed outcome is an immutable, compact carrier encoding of accepted
`a_c.STDO` for `F_P[v_reason]` LLM consumption
over separately supplied workspaces. Its creation includes a distinct
carrier-neutral `F_P[v_compile]` semantic-compilation candidate followed by
structural evaluation and exact human selection. It includes proportionate
role-bound context projections through which an Executive sets frames for
itself, Workers, and Reviewers. This frame basis governs the source project that
defines, constructs, reviews, and publishes that Product. It is not a reference
frame encoded inside Source STDO and is not a per-invocation LLM frame
activation.

## Known evaluation inventory

| Evaluation | Material question | Governing owner |
|---|---|---|
| `E-PRODUCT` | Is exact Source STDO interpreted as candidate `a_c.STDO`, externally accepted, then independently carrier-encoded rather than treated as deterministic extraction or runtime? | Intent and Product |
| `E-FUNCTIONS` | Are the exact generic `a_c` `F_D`, `F_P`, and `F_H` identities and authority boundaries preserved without implicit ODD equivalence? | Product and `REQ-P-FP-*` |
| `E-BASIS` | Are Source STDO, WHAT, tenant, carrier, profile, and content identities exact and non-cyclic? | Product identity and `REQ-P-BASIS-*` |
| `E-MODEL` | Is the common representation a full `M=(b,I,O,E,C,L,X,V,T,J)` model with total populations, exact external resolutions, source routes, and no hidden carrier meaning? | `REQ-P-ALG-*` |
| `E-COMPILATION` | Does one declared `F_P[v_compile]` traversal receive the complete exact Source STDO population and return one immutable carrier-neutral proposal with provenance and residual uncertainty, without selecting meaning or importing tenant constraints? | Product, `REQ-P-FP-*`, and `REQ-P-SELECT-*` |
| `E-CONSUMER` | Can an LLM consume the index with a workspace, intent, frame, and budget without receiving false authority? | `REQ-P-FP-*` |
| `E-CONTEXT` | Can an authorized Executive produce a reconstructable, role-bound, least-closure packet for itself, a Worker, or a Reviewer without silent omission or authority collapse? | `REQ-P-CONTEXT-*` and Source STDO frame law |
| `E-SELECTION` | Does durable `F_H[v_select]` evidence bind the exact immutable semantic-compilation candidate and every accepted, modified, rejected, resolved, or uncertain proposal? | `REQ-P-SELECT-*` |
| `E-CARRIER` | Does a tenant realize the common index directly and lawfully in its exact carrier? | accepted tenant design and carrier authority |
| `E-COST` | Are byte, token, and cost reductions measured on exact comparable payloads? | `REQ-P-VERIFY-*` |
| `E-ASSURANCE` | Is the exact candidate independently reviewable, and are uncertainty and counterexamples visible to acceptance authority? | Product authority and selected STDO assurance law |

The inventory is current, not claimed universally complete. A newly discovered
material evaluation triggers the revision law below.

## Closed frame algebra

Every selected frame below has `revision = 7` and instantiates the unchanged
method tuple:

```text
F_i^7 = <Q_i, B_7, M_i, C_7, I_i, A_i, E_i, X_i, R_7, J_i, K_i, D_i>

B_7 = {
  stdo_release: stdo://releases/v2.5.0-rc.1/,
  product_definition: urn:stdo:product-definition:stdo-representation,
  product_what: sha256:be6f3c244009d319c90588f8b403cd3379d6e135fcb29738d7aa3d49450a5379,
  frame_set: urn:stdo-representation:reference-frame-basis:source-project:7
}

C_7 = exact absolute identity + exact basis/revision + exact subject bytes or
      RFC-8785 identity preimage; equality requires all applicable coordinates
R_7 = {satisfied, falsified, indeterminate, out_of_frame, invalid_basis}
J_i = J_7 union row-specific J_delta
J_7 = any changed B_7 coordinate, frame revision, governed subject bytes,
      grant, capability envelope, or evidence boundary invalidates the result
      and requires a new activation or frame-set revision
```

`A_i` always separates semantic (`S`), evaluation (`Ev`), operation (`Op`), and
decision (`D`) authority. `none` is an explicit absence, not an unbound grant.
The operation output inspected by a frame is evidence; it is not the frame's
closed result.

| Frame | `Q_i` | `M_i` | `I_i` | `A_i = {S, Ev, Op, D}` | `E_i` | `X_i` | `K_i` | `D_i / J_delta` |
|---|---|---|---|---|---|---|---|---|
| product-boundary | `E-PRODUCT` | Intent, Product, requirements, exclusions, consumer contract | constitutional chain and Product boundary conserved | Product owners, Product owners, none, human Product owner | exact current WHAT and traced design | runtime or carrier meaning as Product meaning | constitutional trace analysis | overlaps functions/model/carrier; rechart on Product reprice |
| traversal-functor-integrity | `E-FUNCTIONS` | generic functor identities, classified traversals, grants, results | functor kind, actor, traversal, operation, and authority stay distinct | a_c, applicable requirement owner, none, human Product owner | exact a_c clauses and invocation/decision records | ODD aliases or domain operations as generic functors | a_c identity and authority analysis | input to compilation/selection/carrier/context; rechart on functor or traversal-contract change |
| basis-and-identity | `E-BASIS` | release, manifest, model, profile, carrier, and dependency identities | exact content identity; acyclic derivation/publication order | owning source, identity requirements, none, human Product owner | immutable bytes, manifests, canonical preimages | mutable, unresolved, circular, or cross-basis substitution | digest, URI, JCS, and dependency reconstruction | input to every other frame; rechart on any basis coordinate |
| graph-and-constraint-fidelity | `E-MODEL` | `I/O/E/C/L/X/V/T/J`, RefDomain, ResolutionSet, `P_B` source routes | total populations, reference closure, basis coherence, explicit residuals | Source STDO, algebra requirements, none, human semantic selection | source clauses, model records, provenance rows, resolution witnesses, counterexamples | hidden carrier meaning or silent ambiguity repair | a_c model and semantic analysis | input to compilation/selection/carrier; rechart on signature or model-family change |
| semantic-compilation | `E-COMPILATION` | 51 source members, invocation, proposed model/mappings/residuals | complete source disposition; proposal only; lawful stop | Source STDO, compilation requirements, exact compile grant, F_H selection owner | sealed input, raw output, canonical candidate, F_D result | selection, acceptance, encoding, runtime, or silent omission | full-context semantic proposal construction | outputs candidate to selection; rechart on source/contract/frame/model change |
| fp-consumption | `E-CONSUMER` and probabilistic `E-COST` | admitted index/projection, workspace, intent, activation, response | no output-derived authority; uncertainty and source return preserved | accepted index owners, consumption requirements, host grant, human Product owner | exact invocation/output plus representative and adversarial observations | semantic acceptance, deterministic truth, or runtime authority from response | LLM context, graph reasoning, instruction following | consumes context projection; rechart on model/configuration/intent/frame change |
| carrier-realization | `E-CARRIER` | accepted `Index_B=(M_B,P_B)`/ledger/judgment, profile, basis, carrier, validation | lossless typed encoding; carrier cannot select or repair semantics | accepted model owners, carrier requirements, accepted tenant ticket/design, human Product owner | exact `I/O/E/C/L/X/V/T/J`, resolutions, `P_B`, input bytes, carrier bytes, decode and validation | private dialect, hidden semantics, admission by construction | carrier law, canonical encoding, round-trip analysis | consumes selection; outputs carrier evidence; rechart on profile/basis/codec change |
| executive-context-projection | `E-CONTEXT` and deterministic `E-COST` | parent index, assignment, seeds, least closure, budget, packet | exact grant; least closure; no trimming; frame/role separation | accepted index/frame owners, context requirements, host projection grant, exact Executive grant | assignment, activation, closure proof, packet, token result | ambient role authority, self-grant, or budget trimming | frame, grant, fixed-point, and token analysis | feeds consumption; rechart on assignment/parent/budget/frame change |
| semantic-selection | `E-SELECTION` | candidate, F_D result, proposal population, ledger, external judgment | every model record accepted unchanged or rework; total disposition | Source STDO, selection requirements, none, exact F_H grant | unchanged candidate, structural result, ledger, evidence, judgment | F_D semantic choice, self-acceptance, in-ledger model edits | exact-source semantic review and authority resolution | consumes compilation; outputs accepted unchanged relation or rework; rechart on any subject/evidence/grant change |
| compression-measurement | deterministic `E-COST` | exact payloads, tokenizer, pricing basis, measurements | like-for-like immutable inputs; measurement has no semantic authority | payload owners, verification requirements, measurement grant, human Product owner | bytes, tokenizer/configuration, counts, prices | usefulness or acceptance inferred from size | deterministic byte/token/cost reproduction | overlaps consumption; rechart on any measured input or price basis |
| independent-assurance | `E-ASSURANCE` | exact subject, authorities, evidence, claims, counterexamples, findings | non-authorship; exact reacquisition; no repair while claiming independence | owning authorities, assurance requirements, none, human Product owner | independent acquisition and exact-subject review result | implementation, mutation, disposition, or acceptance by Reviewer | applicable specialist competence and independent access | separately activated over every material frame; rechart on subject/evidence/reviewer change |

## Selected frames and capability envelopes

### `urn:stdo-representation:frame:product-boundary`

- Evaluation: `E-PRODUCT`.
- Intent: preserve the `F_P` programmatic-index boundary and prevent assessment/runtime
  scope from entering the Product.
- Required capability: read exact Intent, Product, requirements, and consumer
  terminology; distinguish `F_P`, `F_D`, and `F_H` functor kinds, traversals,
  and authority.
- Evidence: current constitutional surfaces and traced downstream design.
- Semantic and decision authority: Intent/Product owners; the frame only
  evaluates congruence.

### `urn:stdo-representation:frame:traversal-functor-integrity`

- Evaluation: `E-FUNCTIONS`.
- Intent: prevent deterministic, probabilistic, and human traversal functor
  kinds from being renamed, translated, collapsed, confused with named domain
  operations, or granted one another's authority.
- Required capability: resolve the exact generic `a_c` `F_D`, `F_P`, and `F_H` identities,
  inspect the complete external traversal contract, and distinguish payload,
  invocation, structural evidence, semantic selection, and acceptance.
- Evidence: Product function binding, `REQ-P-FP-*`, invocation contracts,
  structural receipts, selection ledgers, and acceptance records.
- Semantic authority: Source STDO Axiomatic Calculus. Evaluation authority: Product and
  `REQ-P-FP-*`. The frame cannot mint a local functor kind.

### `urn:stdo-representation:frame:basis-and-identity`

- Evaluation: `E-BASIS`.
- Intent: detect mutable, cross-basis, unresolved, cyclic, or invocation-bound
  Product identity.
- Required capability: resolve the installed release and carrier objects,
  reproduce manifests/digests, and reason over identity issuance order.
- Evidence: Product Definition, installed manifest, carrier basis, canonical
  index bytes, and one-way records referencing Product identity.
- Semantic and decision authority: Source STDO, Product identity requirements,
  and human Product acceptance.

### `urn:stdo-representation:frame:graph-and-constraint-fidelity`

- Evaluation: `E-MODEL`.
- Intent: preserve all eight `a_c` populations, total identity and external
  resolution law, bounded contexts, owners, scopes, and source routes without
  hidden carrier meaning.
- Required capability: semantic and `a_c` model analysis across the complete
  affected Source STDO span and `Sigma_STDO`.
- Evidence: source clauses, index declarations, source routes, and explicit
  adversarial seams such as equal spelling across contexts.
- Semantic authority: Source STDO. Evaluation authority: the applicable
  requirement owner. The frame cannot repair source ambiguity.

### `urn:stdo-representation:frame:semantic-compilation`

- Evaluation: `E-COMPILATION`.
- Intent: govern one bounded carrier-neutral `F_P[v_compile]` traversal from the
  exact ordered Source STDO member population and bytes to one immutable
  `SemanticCompilationProposal`; deterministic `ConstructCandidate` then binds
  its unchanged payload to exact invocation and provenance coordinates.
- Required capability: receive the complete exact source population, exact
  `a_c` basis, `Sigma_STDO`, `I_STDO`, compilation intent, selected frames,
  declared model and context envelope, and closed candidate output contract;
  propose the complete `O/E/C/L/X/V/T/J` populations, total external `P_B`,
  source routes, selection rows, generated-key
  preimages, and explicit residual uncertainty without silently omitting a
  source member.
- Evidence: exact candidate identity and bytes, exact source-member order and
  digests, common algebra identity, compiler invocation and raw-output
  provenance, model/capability coordinates, stop state, and
  `F_D[v_candidate_structure]` result.
- Result: proposal, hold, gap, or refusal. The frame cannot select semantic
  content, accept a generated key, admit a carrier, or claim completeness.
- Semantic authority: Source STDO. Proposal authority: the exact
  `F_P[v_compile]` traversal contract. Selection authority remains exclusively
  with `F_H[v_select]` under its recorded grant.

### `urn:stdo-representation:frame:fp-consumption`

- Evaluations: `E-CONSUMER` and the probabilistic part of `E-COST`.
- Intent: observe whether a capable LLM can reason over workspace inputs using
  the index at lower context cost while respecting declared constraints.
- Required capability: an `F_P` model with sufficient context, instruction
  following, semantic disambiguation, graph reasoning, and source-route use,
  plus a host capable of binding the complete generic `a_c` `F_P[v_reason]` traversal
  contract.
- Evidence: exact index/workspace/intent/frame/model coordinates, target,
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
  the common programmatic-index algebra.
- Evidence: accepted profile, canonical artifact, carrier validation, and exact
  mapping from `I`, `O`, `E`, `C`, `L`, `X`, `V`, `T`, `J`, and external
  resolutions.
- Operation authority: the accepted tenant work ticket and design only.

### `urn:stdo-representation:frame:executive-context-projection`

- Evaluation: `E-CONTEXT` and the deterministic projection portion of
  `E-COST`.
- Intent: preserve Source STDO frame selection, activation, capability,
  authority, evidence, independence, stop, and return relations while deriving
  the least declared index closure that fits one target actor's context.
- Required capability: resolve exact Executive, Worker, Reviewer, frame,
  activation, actor, grant, parent-index, tokenizer, and closure identities;
  compute graph fixed points and distinguish role access from role authority.
- Evidence: Executive Context Assignment, exact selected frame carriers,
  parent index, Context Projection Manifest, carrier admission, identity-set
  equality, token measurement, holds, and source re-entry routes.
- Operation authority: context assembly uses the consuming host's existing
  bounded operation grant. The frame creates no construction or mutation grant.
- Decision authority: the exact frame-set authority and grant recorded by the
  assignment. `F_D[v_context_admission]` may evaluate declared closure and
  budget properties but
  cannot select the frames or accept semantic sufficiency.

### `urn:stdo-representation:frame:semantic-selection`

- Evaluation: `E-SELECTION`.
- Intent: expose the human semantic selection boundary without pretending it is
  deterministic extraction or a complete occurrence census.
- Required capability: inspect the exact immutable semantic-compilation
  candidate, its complete Source STDO population and raw provenance, accept,
  reject, or revise every proposed selection and generated-key binding, record
  residual uncertainty, and distinguish `F_H[v_select]` decision from
  `F_D[v_candidate_structure]` shape validation.
- Evidence: exact Semantic Compilation Candidate, structural result, Semantic
  Selection Ledger, Source STDO manifest and member bytes, common identity
  universe, authority identity and grant, and external interpreted-model
  `J_B` acceptance record.
- Decision authority: the exact `F_H[v_select]` actor and grant named by the
  ledger; structural validation checks coordinates but cannot accept semantic
  choices.

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
  identity, token comparison, and `F_P[v_reason]` observations.
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
- Every role-bound packet binds the exact activation configuration selected for
  its target. An Executive self-packet repeats the same grant and capability
  checks and creates neither self-grant nor Reviewer independence.

Source STDO retains semantic authority. Product and requirements retain
constitutional decision authority. Accepted design and ticket authority grant
bounded construction operations. Human Product authority alone accepts or
releases the resulting Product.

### Local engagement-role envelopes

| Role | Capability and binding | Exact grant boundary | Closed return |
|---|---|---|---|
| Executive | Resolve `B_7`, evaluation inventory, frames, actors, evidence, and grants; select and conjoin activated frames | Exact frame-set/work grant only; no self-grant, inherited operation authority, Reviewer independence, or ambient semantic/acceptance authority | activation, reconfiguration, disposition request, or one Product-owner decision under a separate exact grant |
| Worker | Perform one activated bounded operation with the required competence, evidence access, stop states, and return contract | Exact inherited owner-issued operation grant naming subject and write territory; the Worker label grants no mutation, next-work, admission, acceptance, publication, continuation, or disposition authority | candidate, hold, gap, refusal, or re-entry to Executive |
| Reviewer | Independently reacquire the exact subject, basis, authority, evidence, and applicable specialist competence; prove non-authorship | Review/evaluation only; no repair, mutation, implementation, disposition, next activation, or acceptance while retaining Reviewer independence | one closed exact-subject result and findings to Executive |

Every activation binds the exact role envelope, frame identity and revision,
evaluation, subject identity/digest, basis, actor identity, capability,
semantic/evaluation/operation/decision grants, evidence-acquisition boundary,
expected result relation, and stop/re-entry contract. A missing or mismatched
coordinate returns `activation_refusal`; it does not produce a frame result.

### Generic specialist-family disposition

| Baseline family | Local frame or acquisition route | Current disposition and authority |
|---|---|---|
| Product | product-boundary | material; Intent/Product own meaning and human Product authority owns acceptance |
| Design | carrier-realization via accepted tenant design | material but residual until one exact tenant design is accepted |
| Design Component | carrier-realization via tenant component declaration | material but residual until exact components and their owner are accepted |
| Public Boundary | fp-consumption plus executive-context-projection | material; Product/requirements own supported inputs, outputs, and ordinary route |
| Entity | graph-and-constraint-fidelity | material; Source STDO and algebra requirements own identity/population meaning |
| Operator | traversal-functor-integrity, semantic-compilation, and carrier-realization | material; a_c owns functor kinds, domain contracts own operations |
| Owner | product-boundary plus traversal-functor-integrity | material; each cited authority retains its bounded decision |
| Effect | semantic-compilation and carrier-realization only for construction/selection effects | runtime effects are non-material and excluded; construction effects require an exact operation grant |
| Reuse/Foundation | basis-and-identity | material; exact selected STDO and GTL bases only, with no authority transfer by reuse |
| Install | basis-and-identity | material; exact verified STDO/GTL installs and manifests, never mutable source substitutes |
| Proof | independent-assurance plus the applicable testing frame | material; claim owner supplies meaning, proof/review owners supply bounded evidence only |

### Testing-frame acquisition

Testing frames use `B_7`, `C_7`, `R_7`, and `J_7`; each activation additionally
binds one exact Product/module claim, subject, supported path, population,
oracle, forbidden-path inventory, evidence source, and falsification condition.

| Testing family | Material subject and ordinary path | Capability and exclusions | Authority / dependency |
|---|---|---|---|
| user-acceptance | one supported user outcome through the public Product boundary | operate as the declared user without private APIs, injected state, hidden administrator power, fixtures, or test-only endpoints | Product/requirement meaning; depends on accepted runnable Product and public-boundary frame |
| end-to-end | one complete supported entry-to-result path including material persistence/recovery boundaries | execute the real assembled path; no source-only substitute, below-boundary entry, hidden repair, or omitted fresh-process boundary | accepted design/requirements; depends on carrier and public-boundary frames |
| integration | one declared interaction among exact components and real boundary contracts | observe participating interfaces and failures; a test double proves only an explicitly narrower claim | accepted design/component owners; depends on exact component declarations |
| unit | one module-owned public contract and internal law under the module's accepted design | exercise module-owned behavior and falsifiers; no Product, cross-component, semantic, or acceptance claim by test volume | module/design owner; cannot substitute for integration, end-to-end, or user acceptance |

No current accepted runnable `a_c.STDO.GTL` Product exists, so these four
families are acquired declarations with `indeterminate` current results; their
activations remain blocked until their exact subjects and prerequisite designs
exist.

## Overlap, conjunction, and translation

- Product-boundary and graph-fidelity frames intentionally overlap on semantic
  scope so carrier or assessment concepts cannot silently redefine WHAT.
- Traversal-functor integrity overlaps Product boundary, semantic compilation,
  consumption,
  context projection, selection, and carrier realization so `F_D`, `F_P`, and
  `F_H` cannot absorb one another's authority.
- Executive context projection overlaps graph fidelity, `F_P` consumption,
  basis/identity, capability, and compression measurement because a cheap packet
  is lawful only when its selected role and mandatory closure remain exact.
- Basis-and-identity and carrier-realization frames intentionally overlap on
  exact carrier/profile coordinates.
- Compression measurement and `F_P` consumption remain separate: deterministic
  token reduction does not imply probabilistic usefulness, and one useful LLM
  response does not prove the measurement.
- Independent assurance is activated separately over the exact candidate and
  cited claims.
- Product acceptance conjoins exact-basis, graph/constraint, semantic
  compilation, semantic selection, carrier, measurement, and applicable `F_P`
  observations under human authority. No single frame supplies the whole
  decision.
- No semantic translation between frames is currently selected. A future
  translation must name source and target frame identities, owner, preserved and
  changed meaning, evidence, and invalidation conditions.

## Coverage and residual uncertainty

| Evaluation | Covering frames | Current residual |
|---|---|---|
| `E-PRODUCT` | product-boundary, independent-assurance | constitutional repair remains active until accepted |
| `E-FUNCTIONS` | traversal-functor-integrity, product-boundary, independent-assurance | revised binding awaits exact frame review |
| `E-BASIS` | basis-and-identity, independent-assurance | no released Product identity exists |
| `E-MODEL` | graph-and-constraint-fidelity, independent-assurance | exact current-WHAT `Sigma_STDO`, candidate model, and GTL mapping remain unaccepted |
| `E-COMPILATION` | semantic-compilation, traversal-functor-integrity, semantic-selection, independent-assurance | no immutable current-WHAT semantic-compilation candidate exists |
| `E-CONSUMER` | fp-consumption, independent-assurance | no constructed index or frozen workspace trial exists |
| `E-CONTEXT` | executive-context-projection, traversal-functor-integrity, independent-assurance | no accepted parent index, assignment, or projected packet exists |
| `E-SELECTION` | semantic-selection, independent-assurance | no accepted Semantic Selection Ledger exists |
| `E-CARRIER` | carrier-realization, independent-assurance | GTL is proposed; JSON Schema basis is unselected |
| `E-COST` | compression-measurement, fp-consumption, independent-assurance | no canonical index bytes exist to measure |
| `E-ASSURANCE` | independent-assurance | pre-construction constitutional/profile review is active; post-construction Product-candidate review has no subject yet |

These residuals prevent claims that depend on missing evidence. They do not
authorize a frame to absorb another owner's decision.

## Evidence coordinates

- Product Definition: `../stdo_representation.json`
- Intent and Product: `INTENT.md`, `PRODUCT.md`
- Common requirements: `requirements/`
- Executive Context Assignments and Context Projection Manifests: future
  immutable records under the consuming host or qualification evidence surface
- Semantic Compilation Candidates and Semantic Selection Ledgers: future
  immutable carrier-neutral records under the Product construction evidence
  surface
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
- Product intent, traversal-functor binding, semantic compiler or candidate
  contract, `F_P[v_reason]` consumer, index boundary, or authority allocation;
- graph-and-constraint algebra or identity issuance law;
- selected carrier basis or accepted representation profile;
- semantic-selection population or authority, Product acceptance claims,
  ordinary consumer payload, or measurement basis;
- Executive context-assignment law, selected engagement roles, frame
  activations, closure law, context budget, or packet evidence;
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
