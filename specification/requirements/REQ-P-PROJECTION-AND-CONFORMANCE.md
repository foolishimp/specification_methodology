# REQ-P-PROJECTION-AND-CONFORMANCE — Coverage, Projection, And Evidence

Family: `REQ-P-CONF-*`
Status: active
Category: assurance / acceptance
Design ownership: deferred independently to each registered build tenant; no
tenant design is accepted

Derives from: `../PRODUCT.md#product-statement`,
`../PRODUCT.md#product-contents`,
`../PRODUCT.md#reference-frame-basis`

## Purpose

Make carrier adequacy, context compression, comparison, and Product disposition
decidable without requiring execution or treating a favorable metric as
semantic proof.

## Coverage states

Every required source subject and relation receives exactly one state:

- `represented`: the tenant mapping preserves every applicable algebraic
  identity, relation, law, and refusal without material loss;
- `limited`: a usable mapping exists, but an identified algebraic obligation is
  weakened, indirect, expanded, or lost within an explicit boundary;
- `unresolved`: the source meaning, mapping decision, or evidence is ambiguous
  or insufficient to decide;
- `unrepresentable`: no faithful mapping exists under the exact carrier basis
  and representation profile without violating the common algebra or carrier
  law.

## Requirements

**REQ-P-CONF-001**: Every tenant assessment shall publish a total coverage
matrix over the complete source census and every required relation. Each row
shall bind the source semantic address, algebraic obligation, tenant mapping,
coverage state, evidence, and any residual. Missing, duplicate, or
multiply-classified rows block disposition.

**REQ-P-CONF-002**: A `represented` row shall identify the exact carrier
constructs and evidence closing every applicable algebraic obligation. Presence
of a similarly named field, type, node, schema, or graph edge is insufficient.

**REQ-P-CONF-003**: A `limited` row shall identify preserved meaning, changed or
lost meaning, affected scope, user-visible consequence, refusal conditions,
and why the limitation does not make the row unresolved.

**REQ-P-CONF-004**: An `unresolved` row shall identify the ambiguity or missing
decision and the authority capable of resolving it. An unresolved row blocks
both `complete` and `limited` Product admission.

**REQ-P-CONF-005**: An `unrepresentable` row shall include the exact carrier and
profile basis, attempted lawful mappings, the violated algebraic or carrier
law, and a reproducible falsifier. It is a carrier-boundary finding, not
authority to change the common algebra.

**REQ-P-CONF-006**: Assessment disposition shall be derived as follows:

- `complete` requires total coverage, zero `limited`, zero `unresolved`, zero
  `unrepresentable`, successful regeneration, and all required conformance
  evidence;
- `limited` requires total coverage, zero `unresolved`, at least one `limited`
  or `unrepresentable`, successful regeneration of every published artifact,
  and all required evidence for its bounded claims;
- `blocked` applies when either admission predicate is not satisfied.

A `limited` Product shall state that it is an assessment and partial
representation; it shall not be presented as a complete STDO representation.

**REQ-P-CONF-007**: Every projection shall bind its exact parent Product or
candidate identity, projection identity, intent, reference frame, governed
scope, source closure, capability budget, selection rule, included subjects and
relations, and residual inventory.

**REQ-P-CONF-008**: Projection closure shall include all identities, owners,
contexts, bases, relation kinds, and dependencies needed to interpret its
included material under the declared intent. Material outside that closure
shall remain reachable through residuals and source semantic addresses.

**REQ-P-CONF-009**: A projection exceeding its declared budget, lacking required
closure, containing cross-basis material, or omitting a material residual shall
fail closed. A projection shall not silently trim itself to pass a budget.

**REQ-P-CONF-010**: Every size report shall bind the exact byte inventories and
measurement procedure for Source STDO, the canonical tenant representation,
and each projection. It shall report at least member count, raw bytes, canonical
bytes where applicable, and the corresponding ratios.

**REQ-P-CONF-011**: A claim about LLM context fit or token compression shall
bind the exact tokenizer identity and version, acquisition or digest, encoding
configuration, normalization rules, context limit, and measured input bytes.
Token counts produced under different bases shall not be directly compared
without an explicit translation frame.

**REQ-P-CONF-012**: Carrier usefulness shall be assessed with a frozen,
carrier-independent question and falsification set selected before tenant
results are examined. It shall cover at least semantic resolution, owner and
basis identification, bounded-context isolation, dependency closure,
cross-context relations, projection scope, and residual discovery.

**REQ-P-CONF-013**: When an LLM participates in usefulness assessment, the run
shall bind model and deployment identity, model configuration, prompt and tool
surface, context budget, carrier projection identity, question-set identity,
and raw result evidence. An LLM answer is assessment evidence and never source
semantic authority.

**REQ-P-CONF-014**: Cross-tenant comparison shall use the same Source STDO
basis, source census, Product WHAT and requirements-member-set identity,
question set, assessment frames, and measurement definitions. Differences in
carrier basis or profile shall remain explicit coordinates rather than being
normalized away.

**REQ-P-CONF-015**: Every representation and projection shall be independently
regenerable from its exact Source STDO, Product WHAT, carrier basis,
representation profile, and declared construction inputs. Regeneration shall
reproduce the canonical member inventory and root digests.

**REQ-P-CONF-016**: Positive conformance cases shall demonstrate faithful
semantic addresses, authority, contexts, dependencies, composition, overlays,
projections, and residuals across representative and boundary-bearing Source
STDO subjects.

**REQ-P-CONF-017**: Negative cases shall reject at least cross-basis references,
context-free term resolution, owner transfer, undeclared cross-context
equivalence, missing dependency closure, silent projection omission, duplicate
coverage, unbound carrier constructs, nondeterministic canonical identity, and
unsupported complete claims.

**REQ-P-CONF-018**: Mutation cases shall delete or alter admitted identities,
owners, contexts, relation kinds, dependencies, projection residuals, coverage
states, profile mappings, and evidence bindings. A surviving material mutant
blocks the affected conformance claim.

**REQ-P-CONF-019**: Evidence required for disposition shall be durable and
reacquirable through tracked content-addressed artifacts or tracked manifests
with exact acquisition and retention rules. Temporary files, console output,
or unbound summaries are not closure evidence.

**REQ-P-CONF-020**: Representation construction, projection, measurement, and
assessment shall not execute Source STDO, invoke HoG traversal, create ABG
runtime truth, or use runtime success as a substitute for representational
conformance.
