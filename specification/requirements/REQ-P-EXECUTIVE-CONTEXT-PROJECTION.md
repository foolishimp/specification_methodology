# REQ-P-EXECUTIVE-CONTEXT-PROJECTION — Role-Bound Context Setting

Family: `REQ-P-CONTEXT-*`
Status: Active
Category: Capability
Design ownership: common assignment, projection, and refusal contract owned by
WHAT; carrier realization and prompt assembly are owned by each build tenant or
external consuming host

Derives from: `../INTENT.md#desired-outcomes`,
`../PRODUCT.md#product-terms`, `../PRODUCT.md#program-boundary`,
`REQ-P-REPRESENTATION-ALGEBRA.md#closed-algebra`,
`REQ-P-FP-CONSUMPTION.md#external-traversal-contract`, and exact Source STDO
`REFERENCE_FRAME_METHOD.md` and `STDO_REFERENCE_FRAME_BASELINE.md`

## Purpose

Define how an authorized Executive uses an STDO Reasoning Program to set a
finite reference-frame configuration and provide proportionate constitutional
context to itself, a Worker, or a Reviewer. The result is a role-bound context
packet derived from one immutable parent program. It is not a second
constitution, a universal prompt, a deterministic semantic assessor, or an
embedded frame runtime.

The primary optimization is lower LLM context cost subject to declared
material-sufficiency, authority, capability, evidence, refusal, and source
re-entry constraints. A smaller packet that violates one of those constraints
is not an optimization.

## Exact Source STDO role bindings

The Product imports the selected Source STDO engagement-frame meanings
unchanged:

```text
ExecutiveRoleRef =
  stdo://releases/v2.4.3-rc.3/standards/
    STDO_REFERENCE_FRAME_BASELINE.md#executive

WorkerRoleRef =
  stdo://releases/v2.4.3-rc.3/standards/
    STDO_REFERENCE_FRAME_BASELINE.md#worker

ReviewerRoleRef =
  stdo://releases/v2.4.3-rc.3/standards/
    STDO_REFERENCE_FRAME_BASELINE.md#reviewer

EngagementRoleRef = ExecutiveRoleRef | WorkerRoleRef | ReviewerRoleRef
```

Line wrapping above is presentational; each role reference is one absolute URI.
The Executive selects or confirms a bounded activation configuration and
consumes closed results. The Worker performs bounded construction and
self-review under inherited operation authority. The Reviewer performs a
separately activated exact-subject evaluation without implementation or
disposition authority. These labels create no authority by themselves.

## Cross-context role import

The three role labels are unchanged semantic imports from Source STDO's
`urn:stdo:bounded-context:reference-frame-evaluation` context into this
Product's `urn:stdo-representation:bounded-context:product` context for the
scope `urn:stdo:product-definition:stdo-representation`:

| Local term | Exact source and resolved concept |
|---|---|
| `Executive` | `ExecutiveRoleRef` |
| `Worker` | `WorkerRoleRef` |
| `Reviewer` | `ReviewerRoleRef` |

The direction is Source STDO to this Product. The import preserves the complete
source-owned definition, activation relation, capability envelope, authority,
evidence, exclusions, result, stop, return, invalidation, and re-entry meaning.
It changes and loses nothing, has no inverse that makes this Product a Source
STDO authority, and mints no target concept identity. This Product owns only
the context-assignment use of those resolved concepts. The relation is
invalidated by a change to the selected Source STDO basis, a cited role clause,
this Product's bounded context or governed scope, or this requirement's role
contract. The Product Definition records each exact term resolution and both
the source and local authorities; nominal role spelling supplies no fallback.

## Executive context assignment

An executable assignment is an external immutable record. It contains exactly:

```text
ExternalIdentity = non-empty absolute URI

ContextBudget = {
  tokenizer_identity: ExternalIdentity,
  tokenizer_version: non-empty string,
  tokenizer_configuration_sha256: Sha256,
  model_context_limit_tokens: positive safe integer,
  reserved_non_program_tokens: non-negative safe integer,
  maximum_projection_tokens: positive safe integer
}

FrameActivationBinding = {
  activation_ref: ExternalIdentity,
  frame_identity: ExternalIdentity,
  frame_sha256: Sha256,
  mandatory_program_refs: non-empty Identity[],
  evaluation_refs: non-empty ExternalIdentity[],
  required_capability_envelope_ref: ExternalIdentity
}

ExecutiveContextAssignment = {
  kind: "stdo-representation.executive-context-assignment",
  schema_version: 1,
  program_product_identity: ExternalIdentity,
  program_content_identity: Sha256,
  workspace_subject_identity: ExternalIdentity,
  workspace_basis_refs: non-empty ExternalIdentity[],
  governed_outcome_ref: ExternalIdentity,
  reasoning_intent_ref: ExternalIdentity,
  engagement_role_ref: EngagementRoleRef,
  target_actor_identity: ExternalIdentity,
  target_capability_envelope_ref: ExternalIdentity,
  assigning_actor_identity: ExternalIdentity,
  frame_set_authority_identity: ExternalIdentity,
  assignment_grant_identity: ExternalIdentity,
  assignment_grant_scope: non-empty string,
  frame_activations: non-empty FrameActivationBinding[],
  role_program_refs: non-empty Identity[],
  explicit_program_seed_refs: Identity[],
  inherited_operation_grant_refs: ExternalIdentity[],
  decision_grant_refs: ExternalIdentity[],
  required_evidence_refs: ExternalIdentity[],
  stop_state_refs: non-empty ExternalIdentity[],
  context_budget: ContextBudget,
  supersedes: ExecutiveContextAssignmentIdentity | null
}

ExecutiveContextAssignmentIdentity =
  "urn:stdo-representation:executive-context-assignment:sha256:" +
  sha256(JCS(ExecutiveContextAssignment))
```

Its canonical bytes are exact RFC 8785 JCS bytes without prefix, suffix, or
trailing line feed. Duplicate object names or duplicate array members refuse
admission. URI, identity, and digest arrays sort by ascending unsigned UTF-16
code units. `frame_activations` sort by `activation_ref`. Every
`mandatory_program_ref`, `role_program_ref`, and explicit seed resolves to one
member of `I_B`. At least one mandatory ref per activation targets an atom in
`P_B` with `atom_class = "reference_frame"`; every `role_program_ref` is bound
by the accepted Semantic Selection Ledger to the exact selected Source STDO
engagement-role clause.

`maximum_projection_tokens + reserved_non_program_tokens` shall not exceed
`model_context_limit_tokens`. The reservation covers workspace, host
instructions, activation material, and other non-program input. A changed
tokenizer, configuration, reservation, model limit, parent program, frame,
actor, outcome, evaluation, grant, or workspace basis creates a new assignment.
`supersedes` may name only an older assignment for the same parent/subject
relation and shall not create a self-reference or cycle.

The assignment binds an already-declared Reference Frame Method activation. It
does not replace the complete activation record or mint its frame, authority,
capability, operation, decision, or evidence meaning.

## Least declared program closure

For assignment `A`, the program seed set is:

```text
Z(A) = union(
  every A.frame_activations[*].mandatory_program_refs,
  A.role_program_refs,
  A.explicit_program_seed_refs
)
```

`Z(A)` shall be non-empty. The projected program is the unique least fixed
point:

```text
P_A = least_closure(P_B, Z(A), L_context)
```

Each `mandatory_program_refs` set is the frame authority's explicit declaration
of the program records material to that activation. `role_program_refs` is the
corresponding exact Source STDO engagement-role set. Selecting semantic
materiality is therefore an authorized frame decision, not a hidden graph walk.

`L_context` is the following structural reference closure:

1. include every record named by `Z(A)`;
2. for an included edge, include its source, relation-kind, target, context,
   owner, scope, cross-context, inverse, refusal, and invalidation references;
3. for an included constraint, include every applies-to, context, owner, scope,
   decision-owner, and re-entry reference;
4. include every constraint in `C_B` whose `applies_to_refs` names an included
   record; and
5. repeat steps 2 through 4 until no identity is added.

The authorized mandatory sets shall name the records needed to preserve:

1. each seed's semantic address, definition, bounded context, owner, scope, and
   selected basis;
2. relation-kind identities and every endpoint or typed reference of an
   included edge or constraint;
3. constraints applying to an included record and the records referenced by
   those constraints;
4. frame intent, evaluation family, capability envelope, evidence, exclusion,
   result, dependency, overlap, translation, invalidation, and re-entry
   relations represented in `P_B`;
5. authority, grant-kind, decision, operation, refusal, and provenance
   distinctions material to the selected engagement role; and
6. every SourceLocator carried by an included atom, edge, or constraint.

Since `I_B` is finite, the structural relation terminates. It does not infer
semantic materiality from spelling or topology. No record outside that fixed
point is included unless frame authority names it in a mandatory set or the
Executive names it in `explicit_program_seed_refs`; no member of the fixed point
may be removed to meet a token budget.

This is token-minimal only relative to one frozen assignment, seed set, parent
program, and closure law. It does not claim that one globally smallest or
semantically unique frame set exists. Source STDO frame-set authority may
lawfully retain overlap or additional frames for risk reduction, independent
activation, actor fit, or failure detection.

## Projection manifest and context packet

The identity-set digest of a duplicate-free sorted identity set `S` is:

```text
identity_set_sha256(S) =
  "sha256:" + sha256(for each id in S: utf8(id) + LF)
```

One admitted carrier-native projection has this external manifest:

```text
ContextProjectionManifest = {
  kind: "stdo-representation.context-projection-manifest",
  schema_version: 1,
  assignment_identity: ExecutiveContextAssignmentIdentity,
  program_product_identity: ExternalIdentity,
  program_content_identity: Sha256,
  included_identity_refs: non-empty Identity[],
  included_identity_set_sha256: Sha256,
  omitted_identity_count: non-negative safe integer,
  omitted_identity_set_sha256: Sha256,
  projection_carrier_sha256: Sha256,
  projection_token_count: positive safe integer,
  source_reentry_refs: non-empty ExternalIdentity[],
  residual_uncertainty_refs: ExternalIdentity[],
  disposition: "admitted"
}

ContextProjectionIdentity =
  "urn:stdo-representation:context-projection:sha256:" +
  sha256(JCS(ContextProjectionManifest))
```

The included set equals exactly `ids(P_A)`. The omitted set equals exactly
`I_B - ids(P_A)`. Both digests are independently reproduced from their sorted
sets; counts and set relations are checked against the exact parent program.
The token count is reproduced with the tokenizer identity, version, and
configuration bound by the assignment and does not exceed
`maximum_projection_tokens`. A manifest is not issued for a budget or
capability hold. The manifest's canonical bytes and ordering use the
assignment's JCS law.

A **Context Packet** is the consumer-selected bundle of:

- the exact Executive Context Assignment;
- the exact selected frame declarations or reacquisition routes;
- the carrier-native serialization of `P_A`;
- the Context Projection Manifest;
- required externally owned evidence selected for the activation; and
- explicit stop, refusal, residual, and source re-entry routes.

The packet is an invocation input, not a new STDO Reasoning Program Product.
Workspace evidence, prompt assembly, model configuration, reasoning output,
HoG execution, and ABG runtime truth remain external. Qualification and replay
records may retain the complete packet, but an ordinary consumer need not pay
the token cost of the manifest or evidence that its activation does not require.

## Role-specific context law

### Executive target

An Executive packet carries the governed outcome, evaluation inventory,
current subject and basis, frame configuration, actor and capability relations,
authority and grant boundaries, closed Worker or Reviewer inputs where
available, coverage residuals, disposition routes, and invalidation conditions.
It does not make the Executive a universal semantic owner or grant operation
authority by visibility.

The assigning actor may also be the target Executive. Self-targeting repeats
all authority, capability, closure, and budget checks. It cannot self-issue a
grant, create Reviewer independence, accept its own unsupported claim, or omit
material law merely because the same actor selected the packet.

### Worker target

A Worker packet carries the exact authorized outcome and sufficient execution
intake, selected engagement and specialist frames, affected-boundary and
authority constraints represented by the program, inherited operation grants,
required evidence, stop and re-entry conditions, and the closed return route to
Executive. It grants no admission, publication, acceptance, continuation, or
next-frame authority.

### Reviewer target

A Reviewer packet carries the exact candidate or other review subject, claim,
basis, composition boundary, evidence population and acquisition routes,
selected assurance and specialist frames, independence conditions, known
counterexamples, falsifiers, exclusions, invalidation conditions, and the
closed return route to Executive. It carries no construction, mutation,
disposition, or next-activation grant. Worker narrative or hidden reasoning may
be identified as evidence but cannot substitute for independent acquisition of
the exact subject and material live surfaces.

## Function and authority allocation

Frame recommendation or packet critique by an LLM is `F_P` output. It becomes
an executable assignment only when an existing human or admitted bounded-proxy
frame-set authority exercises the exact recorded grant. Such an exercise is
`F_H` only when it satisfies Source STDO's exact human-function contract.

Tenant or host domain mechanics compute the least closure, serialize the
carrier, and count its tokens. Those mechanics are not `F_D` merely because
they are deterministic. `F_D` may evaluate or prove declared properties of the
assignment, closure, identity sets, carrier admission, token measurement, and
budget relation under its own exact traversal contract.

Neither successful construction nor `F_D` admission proves that human frame
selection was semantically complete. Neither Executive status nor context
visibility enlarges semantic, operation, decision, acceptance, release, or
closure authority.

## Requirements

**REQ-P-CONTEXT-001**: An Executive shall set context for itself, a Worker, or a
Reviewer only through an exact Executive Context Assignment binding the parent
program, workspace subject and basis, outcome, intent, engagement role, target
actor and capability, selected frame activations, authority and grant, evidence,
stop states, and token budget.

**REQ-P-CONTEXT-002**: Every executable assignment shall be authorized by the
existing frame-set authority and grant it records. An ungranted LLM suggestion,
persona label, repository role, or prior assignment is a proposal and shall not
activate work.

**REQ-P-CONTEXT-003**: The projected program shall equal the least fixed point
of the declared structural reference closure over the exact authorized seed
set. A dangling reference, missing applicable constraint, unresolved mandatory
or role ref, unresolved frame, or unequal included set refuses admission.

Semantic sufficiency of the mandatory sets remains an `F_H` frame-selection
decision subject to review; structural closure does not prove it.

**REQ-P-CONTEXT-004**: The projection shall preserve source routes and expose
its exact parent, included set, omitted-set digest and count, residuals, and
re-entry routes. It shall not imply authority or sufficiency outside its exact
assignment.

**REQ-P-CONTEXT-005**: The Executive may optimize frame selection for outcome,
risk, actor fit, evidence, and context cost, but shall not claim a globally
unique minimum. After assignment freezes, no mandatory closure member may be
removed for token savings.

**REQ-P-CONTEXT-006**: If the least lawful projection exceeds the declared
budget or the actor cannot operate its selected frames, context construction
shall return a hold identifying `budget_exceeded` or `capability_mismatch`.
Lawful responses include revising the frame set under authority, selecting
another capable actor, sequencing activations, increasing the budget, or
re-entering the owning Product relation.

**REQ-P-CONTEXT-007**: Executive, Worker, and Reviewer packets shall preserve
their distinct Source STDO authority, evidence, result, independence, stop, and
return relations. Equal access to the same parent program shall not collapse
their roles.

**REQ-P-CONTEXT-008**: An Executive self-packet shall not self-grant authority,
claim independent review, absorb Worker operation authority, or bypass the same
capability and material-sufficiency checks applied to another target actor.

**REQ-P-CONTEXT-009**: A Worker packet shall bind inherited operation grants and
return to Executive without admission, acceptance, publication, continuation,
or inferred next-work authority.

**REQ-P-CONTEXT-010**: A Reviewer packet shall bind the exact subject, claim,
evidence acquisition boundary, and independence conditions and shall prohibit
candidate repair or mutation while retaining the Reviewer claim.

**REQ-P-CONTEXT-011**: Context projection shall remain carrier-neutral common
WHAT. Each build tenant shall realize the same assignment and closure relation
directly in its admitted carrier without introducing a shared serialized
intermediate graph or a second carrier validator.

**REQ-P-CONTEXT-012**: Domain mechanics may construct a projection; `F_D` may
evaluate or prove only its declared deterministic properties; `F_P` performs
bounded probabilistic reasoning; and `F_H` selects or accepts only under its
exact grant. No function may absorb another function's authority.

**REQ-P-CONTEXT-013**: A changed parent program, assignment, frame revision,
workspace basis, actor capability, grant, evidence population, tokenizer,
budget, projection carrier, or closure result invalidates the earlier packet
for claims dependent on that coordinate.

**REQ-P-CONTEXT-014**: A host unable to reacquire the exact assignment, selected
frames, parent program, projection bytes, required evidence, or source re-entry
routes shall refuse reconstructable activation rather than depend on hidden
conversation or ambient memory.
