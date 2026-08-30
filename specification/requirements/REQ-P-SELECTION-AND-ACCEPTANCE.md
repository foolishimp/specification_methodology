# REQ-P-SELECTION-AND-ACCEPTANCE — `a_c.STDO` Semantic Authority

Family: `REQ-P-SELECT-*`
Status: Active
Category: Governance
Design ownership: WHAT owns the candidate, ledger, and external-judgment
contracts; a tenant may consume but cannot select them

Derives from: `../PRODUCT.md#symbolic-program-and-index-relation`,
`../PRODUCT.md#product-identity`,
`../PRODUCT.md#authority-acceptance-record`, and
`REQ-P-REPRESENTATION-ALGEBRA.md#exact-model-algebra`

## Purpose

Separate the `F_P[v_compile]` proposal, `F_D[v_candidate_structure]`
structural judgment, `F_H[v_select]` selection ledger, content-first
`a_c.STDO` identity, and external semantic-acceptance judgment. No stage may
grant itself the authority of the next.

## Semantic Compilation Proposal And Candidate

```text
Sha256 = "sha256:" + 64 lowercase hexadecimal characters
AbsoluteIdentity = non-empty absolute URI

SemanticCompilationCandidateIdentity =
  "urn:stdo-representation:semantic-compilation-candidate:sha256:" +
  64 lowercase hexadecimal characters

CandidatePayload = {
  calculus_basis_identity:
    "urn:stdo:axiomatic-calculus-basis:sha256:" + 64 lowercase hexadecimal,
  source_stdo_uri: "stdo://releases/v2.5.0-rc.1/",
  source_stdo_manifest_sha256:
    "sha256:3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338",
  source_member_set_sha256:
    "sha256:87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5",
  source_members: SourceMember[51],
  subject_basis_identity:
    "urn:stdo-representation:subject-basis:stdo:sha256:" + 64 lowercase hexadecimal,
  what_member_set_identity: Sha256,
  signature_identity: AbsoluteIdentity,
  signature_sha256: Sha256,
  interpretation_contract_identity: AbsoluteIdentity,
  interpretation_contract_sha256: Sha256,
  frame_basis_identity: AbsoluteIdentity,
  frame_basis_sha256: Sha256,
  selected_frame_refs: non-empty AbsoluteIdentity[],
  candidate_model: ACModel,
  candidate_model_content_identity: Sha256,
  proposed_record_provenance: RecordProvenanceBinding[],
  proposed_evaluated_members: EvaluatedMember[51],
  proposed_selections: Selection[],
  proposed_generated_source_keys: GeneratedSourceKeyBinding[],
  compilation_residuals: CompilationResidual[],
  stop_state: "urn:stdo-index:stdo:stop-kind:candidate:1"
}

SemanticCompilationProposal = {
  kind: "stdo-representation.semantic-compilation-proposal",
  schema_version: 2,
  payload: CandidatePayload
}

SemanticCompilationCandidate = {
  kind: "stdo-representation.semantic-compilation-candidate",
  schema_version: 3,
  proposal_content_sha256: Sha256,
  compiler_invocation: CompilerInvocation,
  ...CandidatePayload
}

ACModel = {
  model_basis_identity: AbsoluteIdentity,
  identities: AbsoluteIdentity[],
  semantic_objects: SemanticObject[],
  typed_relations: TypedRelation[],
  constraints: Constraint[],
  latitudes: Latitude[],
  residuals: Residual[],
  traversals: Traversal[],
  transformations: Transformation[],
  judgments: Judgment[],
  external_resolutions: ExternalResolution[]
}

RecordProvenanceBinding = {
  model_record_ref: AbsoluteIdentity,
  provenance_kind: "subject_derived",
  semantic_address: SemanticAddress,
  source_locators: SourceLocator[],
  derivation_evidence_refs: AbsoluteIdentity[]
}

CompilerProvenanceMember = {
  member_kind:
    "acquisition" | "basis" | "source_manifest" | "invocation" |
    "sealed_invocation" | "frame_acceptance" | "compile_grant" |
    "compile_activation" | "capability_envelope",
  member_ref: non-empty URI-reference,
  member_sha256: Sha256
}

CompilerProvenanceBundle = {
  kind: "stdo-representation.compiler-provenance-bundle",
  schema_version: 1,
  members: CompilerProvenanceMember[9]
}

SourceMember = {
  member_path: normalized relative POSIX path,
  member_sha256: Sha256
}

CompilerInvocation = {
  topology: "single_invocation",
  traversal_ref: AbsoluteIdentity,
  functor_ref: "urn:stdo:concept:axiomatic-calculus:f-p",
  host_identity: AbsoluteIdentity,
  model_identity: non-empty string,
  model_configuration_sha256: Sha256,
  instruction_sha256: Sha256,
  capability_envelope_ref: AbsoluteIdentity,
  context_budget_tokens: non-negative safe integer,
  invoked_at: RFC3339 timestamp,
  raw_output_ref: non-empty URI-reference,
  raw_output_sha256: Sha256,
  provenance_ref: non-empty URI-reference,
  provenance_sha256: Sha256
}
```

`...CandidatePayload` denotes exact disjoint record-field union, not a JSON
extension point; no additional or omitted field is permitted.

`F_P[v_compile]` returns exact `SemanticCompilationProposal` bytes or one
lawful stop. Domain HOW then applies the deterministic, non-evaluative
operation:

```text
ConstructCandidate(
  exact_raw_proposal_bytes,
  exact_invocation_and_provenance
) -> SemanticCompilationCandidate | refusal
```

The constructor parses one unique proposal, verifies
`proposal_content_sha256 = sha256(JCS(SemanticCompilationProposal))` and
`compiler_invocation.raw_output_sha256 = sha256(exact_raw_proposal_bytes)`,
requires all fixed payload coordinates to equal the sealed invocation, and
copies `CandidatePayload` without semantic modification. It cannot select,
repair, judge, or accept content. `F_D[v_candidate_structure]` evaluates only
the resulting unchanged candidate.

`compiler_invocation.provenance_sha256` equals the SHA-256 of the exact JCS
`CompilerProvenanceBundle` bytes resolved by `provenance_ref`. Its members are
duplicate-free, sorted by `member_kind`, contain exactly the nine declared
kinds, and bind the accepted frame, compile grant, activation, actor, authority,
scope, capability envelope, subject, bases, and exact invocation used by the
compiler. Candidate construction and carrier serialization each resolve every
member's exact bytes and reproduce its digest. Missing, mutable, mismatched,
synthetic-only, partial, or unresolved provenance refuses.

`ACModel` uses the exact imported `a_c` record shapes and the total
`Population_M` law. `candidate_model_content_identity` equals
`sha256(JCS(candidate_model))`. The candidate identity is the stated prefix
plus `sha256(JCS(SemanticCompilationCandidate))`; neither identity enters its
own bytes.

The source population equals the exact 51-member installed manifest in order.
Identity arrays are duplicate-free and sorted by unsigned UTF-16 code-unit
order. Every `SourceLocator[]` is duplicate-free and sorted by the UTF-16
code-unit order of `JCS(SourceLocator)`. Other arrays follow their signature or
common ordering law. If the complete
source and required context do not fit one invocation, the result is `hold` or
`gap`; sharding requires Product re-entry and an exact composition contract.

## Candidate Structure Result

```text
CandidateStructureEvaluationGrantIdentity =
  "urn:stdo-representation:candidate-structure-grant:sha256:" +
  64 lowercase hexadecimal characters

CandidateStructureEvaluationGrant = {
  kind: "stdo-representation.candidate-structure-evaluation-grant",
  schema_version: 1,
  parent_grant_identity: "urn:stdo-representation:grant:product-owner:1",
  issuer_actor_identity: "https://github.com/foolishimp",
  authority_identity: "urn:stdo-representation:authority:product-owner",
  grantee_identity: AbsoluteIdentity,
  grant_scope:
    "Evaluate the exact unchanged SemanticCompilationCandidate under F_D[v_candidate_structure] for declared structural checks only; grants no construction, repair, semantic selection, acceptance, carrier, release, or runtime authority.",
  traversal_ref: AbsoluteIdentity,
  functor_ref: "urn:stdo:concept:axiomatic-calculus:f-d",
  subject_identity: SemanticCompilationCandidateIdentity,
  subject_sha256: Sha256,
  calculus_basis_identity: AbsoluteIdentity,
  signature_identity: AbsoluteIdentity,
  signature_sha256: Sha256,
  interpretation_contract_identity: AbsoluteIdentity,
  interpretation_contract_sha256: Sha256,
  what_member_set_identity: Sha256,
  frame_basis_identity: AbsoluteIdentity,
  frame_basis_sha256: Sha256,
  evidence_refs: non-empty sorted duplicate-free URI-reference[],
  issued_at: RFC3339 timestamp,
  source_ref: "./specification/PRODUCT.md#product-authority",
  source_sha256: Sha256
}

CandidateStructureResultIdentity =
  "urn:stdo-representation:candidate-structure-result:sha256:" +
  64 lowercase hexadecimal characters

CandidateStructureResult = {
  kind: "stdo-representation.candidate-structure-result",
  schema_version: 2,
  semantic_compilation_candidate_identity: SemanticCompilationCandidateIdentity,
  semantic_compilation_candidate_sha256: Sha256,
  calculus_basis_identity: AbsoluteIdentity,
  signature_identity: AbsoluteIdentity,
  interpretation_contract_identity: AbsoluteIdentity,
  traversal_ref: AbsoluteIdentity,
  functor_ref: "urn:stdo:concept:axiomatic-calculus:f-d",
  evaluator_identity: AbsoluteIdentity,
  checks: {
    canonical_bytes: boolean,
    source_inventory: boolean,
    population_totality: boolean,
    record_shapes: boolean,
    identity_derivation: boolean,
    reference_domains: boolean,
    external_resolutions: boolean,
    basis_coherence: boolean,
    ordering: boolean,
    provenance_binding: boolean
  },
  decision: "eligible" | "refuse",
  evaluated_at: RFC3339 timestamp,
  evidence_refs: non-empty URI-reference[]
}
```

The result identity is the stated prefix plus
`sha256(JCS(CandidateStructureResult))` and remains external to the result
bytes. Any ledger binding reproduces both that identity and the exact result
digest from the same unchanged canonical bytes.

The evaluation-grant identity is its stated prefix plus
`sha256(JCS(CandidateStructureEvaluationGrant))`. The grant resolves the exact
Product-owner source bytes and every unchanged candidate and evaluation basis
coordinate. `CandidateStructureResult.evidence_refs` includes that exact grant
identity. Without it, `F_D[v_candidate_structure]` issues no result.

`eligible` holds iff every named check is true. This result is an external
judgment over unchanged candidate bytes. It does not select meaning.
`provenance_binding` includes the total `P_B` bijection, address congruence,
source-key relation, selection incidence, and canonical ordering laws.

## Semantic Selection Ledger

```text
SelectionLedgerIdentity =
  "urn:stdo-representation:semantic-selection-ledger:sha256:" +
  64 lowercase hexadecimal characters

SelectionLedger = {
  kind: "stdo-representation.semantic-selection-ledger",
  schema_version: 3,
  calculus_basis_identity: AbsoluteIdentity,
  subject_basis_identity: AbsoluteIdentity,
  source_stdo_uri: "stdo://releases/v2.5.0-rc.1/",
  source_stdo_manifest_sha256: Sha256,
  source_member_set_sha256: Sha256,
  what_member_set_identity: Sha256,
  signature_identity: AbsoluteIdentity,
  interpretation_contract_identity: AbsoluteIdentity,
  semantic_compilation_candidate_identity: SemanticCompilationCandidateIdentity,
  semantic_compilation_candidate_sha256: Sha256,
  candidate_structure_result_identity: CandidateStructureResultIdentity,
  candidate_structure_result_sha256: Sha256,
  candidate_model_content_identity: Sha256,
  record_provenance: RecordProvenanceBinding[],
  evaluated_members: EvaluatedMember[51],
  selections: Selection[],
  generated_source_keys: GeneratedSourceKeyBinding[],
  compilation_residuals: CompilationResidual[],
  proposal_dispositions: ProposalDisposition[],
  author: AuthorityBinding,
  supersedes: SelectionLedgerIdentity | null
}

EvaluatedMember = {
  member_path: string,
  member_sha256: Sha256,
  disposition:
    "contains_retained_material" |
    "contains_no_retained_material" |
    "uncertain" |
    "inapplicable" |
    "refused",
  selection_refs: string[],
  rationale: non-empty string
}

Selection = {
  selection_ref: AbsoluteIdentity,
  source_locators: non-empty SourceLocator[],
  disposition: "retained" | "omitted" | "uncertain" | "inapplicable" | "refused",
  model_record_refs: AbsoluteIdentity[],
  rationale: non-empty string,
  source_owner: AbsoluteIdentity
}

GeneratedSourceKeyBinding = {
  source_key:
    "urn:stdo-representation:source-key:sha256:" + 64 lowercase hexadecimal,
  primary_source_locator: SourceLocator,
  local_declaration_key: non-empty string
}

source_key = "urn:stdo-representation:source-key:sha256:" +
  sha256(JCS({primary_source_locator, local_declaration_key}))

CompilationResidual = {
  residual_ref: AbsoluteIdentity,
  source_locators: non-empty SourceLocator[],
  statement: non-empty string,
  consequence: non-empty string,
  model_residual_refs: AbsoluteIdentity[],
  re_entry_route: non-empty string
}

ProposalDisposition = {
  proposal_ref: AbsoluteIdentity,
  proposal_kind:
    "evaluated_member" | "model_record" | "selection" |
    "generated_source_key" | "compilation_residual",
  decision:
    "accepted_unchanged" | "accepted_modified" | "rejected" |
    "resolved" | "retained_uncertain",
  final_refs: AbsoluteIdentity[],
  rationale: non-empty string
}

AuthorityBinding = {
  traversal_ref: AbsoluteIdentity,
  actor_identity: AbsoluteIdentity,
  authority_identity: AbsoluteIdentity,
  grant_identity: AbsoluteIdentity,
  grant_scope: non-empty string,
  subject_identity: SemanticCompilationCandidateIdentity,
  subject_sha256: Sha256,
  basis_refs: non-empty AbsoluteIdentity[],
  decided_at: RFC3339 timestamp,
  evidence_refs: non-empty sorted duplicate-free URI-reference[]
}
```

The ledger identity is the stated prefix plus `sha256(JCS(SelectionLedger))`.
The ledger is itself the exact `F_H[v_select]` decision and requires no second
acceptance record. Its `author` binding carries the exact traversal, actor,
authority, grant, subject, basis, subject digest, decision time, and evidence
boundary exercised by that decision.
The interpreted-model identity is then constructed from the exact calculus,
subject, signature, interpretation contract, model content, and ledger
identity/digest coordinates in `PRODUCT.md#product-identity`. External `J_B`
uses `AuthorityAcceptanceRecord` with `subject_kind = "interpreted_model"` and
points to that unchanged identity and model-content digest.

The ledger's `evaluated_members`, `selections`, `generated_source_keys`, and
`compilation_residuals` are the final `F_H[v_select]` surfaces. They need not
equal the proposed non-model surfaces; `proposal_dispositions` is their total
proposed-to-final, final-`X`, or no-final mapping. An evaluated-member proposal
uses its exact Source STDO member URI as `proposal_ref`. Final source bindings
derive only from these ledger surfaces. `record_provenance` is different: it
remains byte-exact with `proposed_record_provenance` because the selected model
is unchanged.

Ledger arrays are duplicate-free and ordered exactly: `evaluated_members` by
the installed manifest; `record_provenance` by `model_record_ref`; `selections`
by `selection_ref`; `generated_source_keys` by `source_key`;
`compilation_residuals` by `residual_ref`; and `proposal_dispositions` by
`proposal_ref`, whose global family partition makes that key unique. Nested
identity/evidence arrays use unsigned UTF-16 code-unit order and locator arrays
use the UTF-16 code-unit order of `JCS(SourceLocator)`.

A conforming ledger does not edit the candidate model or its record-provenance
relation. Every
`proposal_kind = "model_record"` disposition is exactly
`accepted_unchanged` with `final_refs = [proposal_ref]` and preserves the
corresponding `P_B` row byte-exact. Any proposed record or corresponding
provenance-row rejection, replacement, resolution, or modification returns
`rework`; the replacement is emitted only through a new
`SemanticCompilationCandidate` with a new candidate identity.

## Requirements

**REQ-P-SELECT-001**: `F_P[v_compile]` shall receive every exact Source STDO
member and return one exact proposal payload that dispositions every member.
Missing, duplicate, reordered, or digest-mismatched population refuses.

**REQ-P-SELECT-001A**: `ConstructCandidate` shall bind the exact raw proposal,
canonical proposal content, sealed invocation, WHAT, frame, source, signature,
contract, and provenance coordinates without changing `CandidatePayload`.
Construction failure refuses before `F_D`; successful construction grants no
semantic or acceptance authority.

**REQ-P-SELECT-002**: Every local model record shall be owned by exactly one
retained selection row. The retained `model_record_refs` union shall equal
`Local_M`; every external identity and `Resolution_M` coordinate shall be
reachable from at least one retained record or explicit basis row.

The proposed and final `P_B` populations shall each be sorted, duplicate-free,
and total over exactly `Local_M`. The final ledger shall preserve the proposed
`P_B` bytes unchanged.

Every retained selection shall include every `P_B.source_locators` value of
each record it owns. Every derivation-evidence ref shall resolve in the exact
candidate's `DerivationEvidenceDomain_B`; unresolved or caller-invented evidence
refuses. Non-retained selections own no model record. Record-to-source re-entry
is derived from `P_B`, never inferred from selection membership.

Each ledger `EvaluatedMember` and final `Selection` relation is bidirectional:
every member-to-selection reference is backed by a locator for that same member
path and digest, and every selection locator's member row references that
selection. `contains_retained_material` reaches at least one final model record;
`uncertain` or `refused` reaches at least one final `X` record;
`contains_no_retained_material` and `inapplicable` reach no model record.

**REQ-P-SELECT-003**: Every generated source key shall bind exactly one complete
deterministic preimage and exactly one represented semantic address. `F_D`
reproduces the hash; only `F_H[v_select]` may accept its semantic use.
Every generated-prefix `P_B.semantic_address.source_key` shall have exactly one
`GeneratedSourceKeyBinding`; its primary locator shall occur in that same
`P_B` row. Complete preimages and resulting source keys are unique; a local
declaration key may recur under different primary locators. Every other source
key shall resolve as an exact Source STDO identity under `B_STDO` at the row's
address or locator; arbitrary non-generated source identities refuse.

**REQ-P-SELECT-004**: Omission or inapplicability shall identify the exact
source span and competent rationale. Token reduction, repetition, filename,
document kind, or author intuition alone is insufficient.

**REQ-P-SELECT-005**: Every material compilation residual shall map to one or
more model `X` records, be resolved or rejected with exact authority and
rationale, or block acceptance. No residual disappears between candidate and
ledger.

**REQ-P-SELECT-006**: `F_D[v_selection_structure]` may verify shape, population,
digests, totality, ordering, references, and set equality. It shall not decide
semantic truth, omission rationale, residual disposition, or acceptance.

`F_D[v_candidate_structure]` may issue `CandidateStructureResult` only under
the exact content-identified `CandidateStructureEvaluationGrant` above. The
grant supplies no construction, repair, semantic, selection, acceptance, or
carrier authority.

**REQ-P-SELECT-007**: Ledger authorship and `J_B` shall each bind exact actor,
authority, grant, subject, basis, evidence, traversal, and unchanged subject
bytes. Model production or repository ownership grants no `F_H` authority.

**REQ-P-SELECT-008**: Ledger, candidate, structural result, and `J_B` are
qualification evidence external to the ordinary reasoning payload unless a
host explicitly selects them for assurance.

**REQ-P-SELECT-009**: A change to any basis, WHAT member, signature,
interpretation contract, candidate model field, source disposition, selection,
residual, author, or acceptance binding creates a new subject. Prior acceptance
does not flow to changed bytes.

**REQ-P-SELECT-010**: Empty, partial, conversation-only, self-accepted, or
non-reproducing selection evidence refuses interpretation acceptance and
carrier construction.

**REQ-P-SELECT-011**: Product acceptance shall cite the exact candidate,
structural result, ledger, interpreted-model identity, `J_B`, carrier result,
measurements, and applicable `F_P[v_reason]` observations. No evidence class
substitutes for another.

**REQ-P-SELECT-012**: Every candidate evaluated member, model record, selection,
generated key, and compilation residual shall receive exactly one proposal
disposition. A proposal identity shall occur in exactly one of those five
families; a
cross-family identity collision refuses. A
ledger exists only when every model record and its `P_B` row are accepted
unchanged and the final model and provenance populations equal the candidate
populations by identity and bytes.
Every final evaluated member, selection, key, and residual shall have exactly
one incoming proposal disposition; merging has no law in this Product.

**REQ-P-SELECT-013**: `accepted_unchanged` shall have
`final_refs = [proposal_ref]`. For non-model proposals, `accepted_modified`
shall name exactly one final row in the same evaluated-member, selection,
generated-key, or compilation-residual family and its rationale; an evaluated
member retains its exact Source STDO member URI while its disposition row may
change. `rejected` and `resolved` name no final reference.
`retained_uncertain` names one or more exact final model `X` records. Applying
any of those four decisions to a model record refuses ledger construction and
returns `rework` for a new candidate.

**REQ-P-SELECT-014**: A missing or mismatched candidate, basis, source, WHAT,
signature, interpretation contract, compiler provenance, structural result,
record-provenance row, proposal disposition, ledger, or non-`eligible` result
refuses `J_B` and all carrier construction.
