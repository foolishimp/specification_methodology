import { gunzipSync } from "node:zlib";

import {
  catalogContribution,
  contractDeclaration,
  modulePublication,
  productSemanticsBinding,
  ruleDeclaration,
  type CatalogContribution,
  type ModulePublication,
  type RuleDeclaration,
} from "@abiogenesis/typescript-tenant/gtl";
import {
  rawAdmitValue,
  validatePublication,
} from "@abiogenesis/typescript-tenant/validator";
import {
  canonicalJson,
  compareUnicodeCodeUnits,
  exactKeys,
  isRecord,
  sha256Bytes,
  sha256Canonical,
  type JsonValue,
} from "./canonical.js";
import type { PublisherArtifactBasis } from "./contracts.js";
import { parseUniqueJson } from "./io.js";

const F_D = "urn:stdo:concept:axiomatic-calculus:f-d";
const F_P = "urn:stdo:concept:axiomatic-calculus:f-p";
const F_H = "urn:stdo:concept:axiomatic-calculus:f-h";
const COMPILE_TRAVERSAL = "urn:stdo-representation:traversal:semantic-compile:7";
const STRUCTURE_TRAVERSAL = "urn:stdo-representation:traversal:candidate-structure:3";
const SELECTION_TRAVERSAL = "urn:stdo-representation:traversal:semantic-selection:2";
const INTERPRETATION_ACCEPTANCE_TRAVERSAL = "urn:stdo-representation:traversal:accept-interpretation:1";
const COMPILE_CAPABILITY = "urn:axiom-indexer:capability:semantic-compilation-prototype:1";
const STDO_RELEASE_URI = "stdo://releases/v2.5.0-rc.1/";
const STDO_MANIFEST_SHA256 = "sha256:3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338";
const STDO_MEMBER_SET_SHA256 = "sha256:87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5";
const STDO_SUBJECT_BASIS_IDENTITY = "urn:stdo-representation:subject-basis:stdo:sha256:73f2581c2d8466a2c8e41b842c2178495431ff28450192f00368ec9fff8766a6";
const WHAT_MEMBER_SET_IDENTITY = "sha256:be6f3c244009d319c90588f8b403cd3379d6e135fcb29738d7aa3d49450a5379";
const FRAME_BASIS_IDENTITY = "urn:stdo-representation:reference-frame-basis:source-project:7";
const FRAME_BASIS_SHA256 = "sha256:4b32e19c48dfa6df909f174603bbeb43f00559f9bc50b5d8e27a02397b6464c3";
const COMPILATION_FRAME_IDENTITY = "urn:stdo-representation:frame:semantic-compilation";
const TARGET_SIGNATURE_IDENTITY = "urn:stdo-index:signature:stdo:7";
const TARGET_SIGNATURE_SHA256 = "sha256:c64b731928529b7af3d43d9bb6a19a5524d60bf8c0b30060f0a5da6ffc5dd10a";
const INTERPRETATION_CONTRACT_SHA256 = "sha256:48ae6fb6bb0b4da6f91c71c0f4ba23a367a38b5b79fbdce54e67dd24c88ce02e";
const MODEL_BASIS_IDENTITY = "urn:stdo-index:model-basis:sha256:fd7bf9c54310945240dd4173878d9ff42548b09c7d1f0f9ba5989e18cdc75a34";
const MODEL_BASIS_EVIDENCE_IDENTITY = "urn:stdo-index:evidence:model-basis-preimage:sha256:fd7bf9c54310945240dd4173878d9ff42548b09c7d1f0f9ba5989e18cdc75a34";
const SIGNATURE_EVIDENCE_IDENTITY = "urn:stdo-index:evidence:target-signature:sha256:c64b731928529b7af3d43d9bb6a19a5524d60bf8c0b30060f0a5da6ffc5dd10a";
const CALCULUS_CONCEPT_IDENTITY = "urn:stdo:concept:axiomatic-calculus:a-c";
const CALCULUS_BASIS_IDENTITY = "urn:stdo:axiomatic-calculus-basis:sha256:bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da";
const CALCULUS_BASIS_SHA256 = "sha256:bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da";
const EXACT_MODEL_BASIS_RELATION = "urn:stdo-index:basis-relation:exact-model-basis:1";
const PROFILE_IDENTITY = "urn:stdo-index:gtl-profile:axiom-index:7";
const PROFILE_SHA256 = "sha256:20dc8e7e17af3f5dd0c3814342d2f350b88193bede4598933ae4fcbdec361022";
const BUILD_TENANT_IDENTITY = "urn:stdo-representation:build-tenant:gtl";
const CARRIER_BASIS_PREFIX = "urn:stdo-representation:carrier-basis:gtl:sha256:";
const RECORD_CONTRACT_REF = "urn:stdo-index:gtl-contract:axiom-index:4";
const PROGRAM_PREFIX = "urn:stdo-index:axiomatic-program:sha256:";
const CANDIDATE_PREFIX = "urn:stdo-representation:semantic-compilation-candidate:sha256:";
const LEDGER_PREFIX = "urn:stdo-representation:semantic-selection-ledger:sha256:";
const STRUCTURE_PREFIX = "urn:stdo-representation:candidate-structure-result:sha256:";
const JUDGMENT_PREFIX = "urn:stdo-representation:authority-acceptance:sha256:";
const INTERPRETED_MODEL_PREFIX = "urn:stdo-representation:a-c-stdo:sha256:";
const GRANT_PREFIX = "urn:stdo-index:authority-grant-artifact:sha256:";
const SOURCE_KEY_PREFIX = "urn:stdo-representation:source-key:sha256:";
const PRODUCT_OWNER_ACTOR = "https://github.com/foolishimp";
const PRODUCT_OWNER_AUTHORITY = "urn:stdo-representation:authority:product-owner";
const PRODUCT_OWNER_GRANT = "urn:stdo-representation:grant:product-owner:1";
const PRODUCT_OWNER_GRANT_SCOPE = "Select and accept project-owned frame bases, representation profiles, Source STDO semantic selections, candidate STDO.gtl Products, and tenant-qualified releases; authorize deterministic construction; and issue bounded build-time operation grants for proposal-only semantic-compilation and deterministic structural-evaluation traversals; excludes changing Source STDO or transferring semantic, review, acceptance, release, or runtime authority to a traversal.";
const PRODUCT_OWNER_AUTHORITY_REF = "./specification/PRODUCT.md#product-authority";
const PRODUCT_OWNER_AUTHORITY_SHA256 = "sha256:1d08e5f9b870e6907ce44fc7b09c2d18696c975ea7a3d6e4394d5ad365e6a256";
const STRUCTURE_EVALUATOR = "urn:stdo-index:evaluator:candidate-structure:4";
const STRUCTURE_GRANT_PREFIX = "urn:stdo-representation:candidate-structure-grant:sha256:";
const STRUCTURE_GRANT_SCOPE = "Evaluate the exact unchanged SemanticCompilationCandidate under F_D[v_candidate_structure] for declared structural checks only; grants no construction, repair, semantic selection, acceptance, carrier, release, or runtime authority.";
const STRUCTURE_EVALUATOR_SOURCE_REF = "./build_tenants/semantic_compile/scripts/evaluate_candidate.py";
const STRUCTURE_EVALUATOR_SHA256 = "sha256:26afb60f77f93118d964371b921d5ef16f66de956826be810b8a9b09d0d4b19d";
const FROZEN_GTL_REPOSITORY = "https://github.com/foolishimp/abiogenesis.git";
const FROZEN_GTL_COMMIT = "8d7f965a3fae7d1acea6a9db298798480fd4cc2f";
const FROZEN_GTL_AUTHORITY_ROOT = "specification/requirements/gtl/";
const FROZEN_GTL_AUTHORITY_TREE = "21a44b1941a1055d6abd973937e65b83e359de1b";
const FROZEN_GTL_AUTHORITY_COUNT = 33;
const SOURCE_DISPOSITIONS = new Set(["retained", "represented_by_residual", "inapplicable", "refused"]);
const SOURCE_REASON_CODES = new Set(["modeled", "derived_read_model", "schema_or_template", "unresolved", "excluded_by_contract"]);
const COMPILER_PROVENANCE_MEMBER_KINDS = [
  "acquisition",
  "basis",
  "capability_envelope",
  "compile_activation",
  "compile_grant",
  "frame_acceptance",
  "invocation",
  "sealed_invocation",
  "source_manifest",
] as const;

interface CarrierBasisCoordinate extends Readonly<Record<string, JsonValue>> {
  readonly authority_inventory_count: number;
  readonly authority_root: string;
  readonly authority_tree_sha1: string;
  readonly commit_sha1: string;
  readonly repository: string;
}

interface TupleSchema extends Readonly<Record<string, JsonValue>> {
  readonly fields: readonly string[];
  readonly types: readonly string[];
}

interface SelectedAxiomIndexProfile extends Readonly<Record<string, unknown>> {
  readonly kind: "stdo-index.gtl-encoding-profile";
  readonly schema_version: 5;
  readonly identity: string;
  readonly build_tenant: Readonly<{
    identity: string;
    carrier_basis: Readonly<{
      identity: string;
      identity_rule: string;
      coordinate: CarrierBasisCoordinate;
    }>;
  }>;
  readonly canonicalization: Readonly<{
    coordinate_algorithm: string;
    carrier_value_algorithm: string;
    raw_admission_subject: string;
    artifact_framing: Readonly<{
      prefix_hex: string;
      suffix_hex: string;
      suffix_in_program_content_identity: boolean;
    }>;
    program_content_identity_rule: string;
    input_domain: string;
    duplicate_object_names: string;
    string_domain: string;
    unicode_normalization: string;
    number_domain: string;
  }>;
  readonly publication_contract: Readonly<{
    module_publication: Readonly<{
      raw_admission_contract_ref: string;
      kind: "module_publication";
      module_version: "5.0.0";
      exact_fields: readonly string[];
      inventory_cardinality: Readonly<Record<string, number>>;
    }>;
    product_semantics_binding: Readonly<{
      kind: "product_semantics_binding";
      binding_ref: string;
      exact_fields: readonly string[];
      publisher_fields: readonly string[];
    }>;
    record_contract: Readonly<{
      contract_ref: string;
      contract_version: "5.0.0";
      contract_kind: "input";
      value_kind: string;
      exact_fields: readonly string[];
    }>;
    rule: Readonly<{
      name: string;
      kind: string;
      tags: readonly string[];
      exact_fields: readonly string[];
    }>;
    contribution: Readonly<{
      raw_admission_contract_ref: string;
      handle: string;
      kind: "node_type";
      declaration_or_contract_ref: string;
      program_membership_refs: readonly string[];
      readiness_prerequisite_refs: readonly string[];
      compatibility_refs: readonly string[];
      provenance_refs: readonly string[];
      exact_fields: readonly string[];
    }>;
  }>;
  readonly configuration: Readonly<{
    kind: "stdo.axiom_index";
    version: 4;
    exact_keys: readonly string[];
    field_keys: Readonly<Record<string, string>>;
    basis_schema: Readonly<{
      exact_fields: readonly string[];
      coordinate_exact_fields: readonly string[];
    }>;
    table_laws: Readonly<Record<string, string>>;
    tuple_schemas: Readonly<Record<string, TupleSchema>>;
    record_schemas: Readonly<Record<string, Readonly<Record<string, JsonValue>>>>;
  }>;
}

interface ValidatedAxiomIndexProfile {
  readonly definition: SelectedAxiomIndexProfile;
  readonly digest: string;
  readonly carrier_basis_identity: string;
}

const FROZEN_GTL_CARRIER_COORDINATE: CarrierBasisCoordinate = Object.freeze({
  authority_inventory_count: FROZEN_GTL_AUTHORITY_COUNT,
  authority_root: FROZEN_GTL_AUTHORITY_ROOT,
  authority_tree_sha1: FROZEN_GTL_AUTHORITY_TREE,
  commit_sha1: FROZEN_GTL_COMMIT,
  repository: FROZEN_GTL_REPOSITORY,
});

export const AXIOM_INDEX_MACHINE = Object.freeze([
  "semantic_compilation_candidate",
  "structurally_eligible",
  "semantically_accepted",
  "gtl_carrier_candidate",
] as const);

export interface AxiomSemanticObject {
  readonly id: string;
  readonly sort: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly value: string;
}

export interface AxiomTypedRelation {
  readonly id: string;
  readonly kind: string;
  readonly source: string;
  readonly target: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly qualifiers: readonly string[];
}

export interface AxiomConstraint {
  readonly id: string;
  readonly kind: string;
  readonly applies_to: string;
  readonly predicate: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly judgment_kind: string;
  readonly latitude_ref: string | null;
  readonly refusal: string;
}

export interface AxiomLatitude {
  readonly id: string;
  readonly applies_to: string;
  readonly allowed_variation: readonly string[];
  readonly forbidden_variation: readonly string[];
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly invalidation: string;
}

export interface AxiomResidual {
  readonly id: string;
  readonly subject: string;
  readonly kind: string;
  readonly uncertainty: string;
  readonly consequence: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly re_entry: string;
  readonly invalidation: string;
}

export interface AxiomTraversal {
  readonly id: string;
  readonly domain: string;
  readonly codomain: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly preconditions: readonly string[];
  readonly postconditions: readonly string[];
  readonly authority: string;
  readonly evidence: readonly string[];
  readonly provenance: readonly string[];
  readonly stop_states: readonly string[];
}

export interface AxiomTransformation {
  readonly id: string;
  readonly traversal: string;
  readonly domain_model: string;
  readonly codomain_model: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly operation_authority: string;
  readonly preconditions: readonly string[];
  readonly preservation_relation: string;
  readonly preserved: readonly string[];
  readonly introduced: readonly string[];
  readonly removed: readonly string[];
  readonly external_preserved: readonly string[];
  readonly external_introduced: readonly string[];
  readonly external_removed: readonly string[];
  readonly external_resolution_witnesses: readonly AxiomExternalResolutionWitness[];
  readonly residuals: readonly string[];
  readonly evidence: readonly string[];
  readonly provenance: readonly string[];
  readonly stop_states: readonly string[];
  readonly invalidation: string;
  readonly re_entry: string;
}

export interface AxiomJudgment {
  readonly id: string;
  readonly kind: string;
  readonly subject: string;
  readonly subject_digest: string;
  readonly context: string;
  readonly owner: string;
  readonly scope: string;
  readonly basis: string;
  readonly evaluator: string;
  readonly authority: string;
  readonly decision: string;
  readonly evidence: readonly string[];
  readonly provenance: readonly string[];
  readonly decided_at: string;
}

export interface AxiomExternalResolution {
  readonly external_identity: string;
  readonly reference_domain: string;
  readonly external_target_kind: string;
  readonly resolved_target_identity: string;
  readonly basis_relation: string;
  readonly resolution_basis: string;
  readonly evidence_identity: string;
}

export interface AxiomExternalResolutionWitness {
  readonly external_resolution: string;
  readonly domain_model: string;
  readonly codomain_model: string;
  readonly domain_resolution: AxiomExternalResolution;
  readonly codomain_resolution: AxiomExternalResolution;
  readonly decision: "equal";
  readonly evidence: string;
}

export interface AxiomSourceBinding {
  readonly member_path: string;
  readonly member_sha256: string;
  readonly disposition: "retained" | "represented_by_residual" | "inapplicable" | "refused";
  readonly model_refs: readonly string[];
  readonly residual_refs: readonly string[];
  readonly reason_code: "modeled" | "derived_read_model" | "schema_or_template" | "unresolved" | "excluded_by_contract";
}

export interface AxiomSourceLocator {
  readonly basis_uri: string;
  readonly member_path: string;
  readonly member_sha256: string;
  readonly fragment: string | null;
}

export interface AxiomSemanticAddress {
  readonly source_key: string;
  readonly term: string;
  readonly bounded_context: string;
  readonly owning_authority: string;
  readonly selected_basis: string;
  readonly governed_scope: string;
}

export interface AxiomRecordProvenance {
  readonly model_record_ref: string;
  readonly provenance_kind: "subject_derived";
  readonly semantic_address: AxiomSemanticAddress;
  readonly source_locators: readonly AxiomSourceLocator[];
  readonly derivation_evidence_refs: readonly string[];
}

export interface AxiomModel {
  readonly b: string;
  readonly I: readonly string[];
  readonly O: readonly AxiomSemanticObject[];
  readonly E: readonly AxiomTypedRelation[];
  readonly C: readonly AxiomConstraint[];
  readonly L: readonly AxiomLatitude[];
  readonly X: readonly AxiomResidual[];
  readonly V: readonly AxiomTraversal[];
  readonly T: readonly AxiomTransformation[];
  readonly J: readonly AxiomJudgment[];
  readonly ResolutionSet_M: readonly AxiomExternalResolution[];
}

type AxiomLocalRecord = AxiomSemanticObject | AxiomTypedRelation | AxiomConstraint | AxiomLatitude | AxiomResidual | AxiomTraversal | AxiomTransformation | AxiomJudgment;

function localModelRecords(model: AxiomModel): readonly AxiomLocalRecord[] {
  return [...model.O, ...model.E, ...model.C, ...model.L, ...model.X, ...model.V, ...model.T, ...model.J];
}

function externalModelValue(model: AxiomModel): Readonly<Record<string, JsonValue>> {
  return {
    model_basis_identity: model.b,
    identities: model.I as unknown as JsonValue,
    semantic_objects: model.O as unknown as JsonValue,
    typed_relations: model.E as unknown as JsonValue,
    constraints: model.C as unknown as JsonValue,
    latitudes: model.L as unknown as JsonValue,
    residuals: model.X as unknown as JsonValue,
    traversals: model.V as unknown as JsonValue,
    transformations: model.T as unknown as JsonValue,
    judgments: model.J as unknown as JsonValue,
    external_resolutions: model.ResolutionSet_M as unknown as JsonValue,
  };
}

export interface BasisCoordinate {
  readonly identity: string;
  readonly sha256: string;
}

export interface AcceptedAxiomaticProgram extends Readonly<Record<string, unknown>> {
  readonly kind: "axiom-indexer.axiomatic-program";
  readonly schema_version: 2;
  readonly model_content_identity: string;
  readonly basis: Readonly<{
    corpus: BasisCoordinate;
    calculus: BasisCoordinate;
    subject_basis: BasisCoordinate;
    target_profile: BasisCoordinate;
    interpretation_contract: BasisCoordinate;
    semantic_compilation_candidate: BasisCoordinate;
    candidate_structure_result: BasisCoordinate;
  }>;
  readonly model: AxiomModel;
  readonly record_provenance: readonly AxiomRecordProvenance[];
  readonly source_bindings: readonly AxiomSourceBinding[];
}

export interface CandidateStructureResult extends Readonly<Record<string, unknown>> {
  readonly kind: "stdo-representation.candidate-structure-result";
  readonly schema_version: 2;
  readonly semantic_compilation_candidate_identity: string;
  readonly semantic_compilation_candidate_sha256: string;
  readonly calculus_basis_identity: string;
  readonly signature_identity: string;
  readonly interpretation_contract_identity: string;
  readonly traversal_ref: string;
  readonly functor_ref: string;
  readonly evaluator_identity: string;
  readonly checks: Readonly<Record<string, boolean>>;
  readonly decision: "eligible" | "refuse";
  readonly evaluated_at: string;
  readonly evidence_refs: readonly string[];
}

export interface SelectionLedger extends Readonly<Record<string, unknown>> {
  readonly kind: "stdo-representation.semantic-selection-ledger";
  readonly schema_version: 3;
  readonly calculus_basis_identity: string;
  readonly subject_basis_identity: string;
  readonly source_stdo_uri: string;
  readonly source_stdo_manifest_sha256: string;
  readonly source_member_set_sha256: string;
  readonly what_member_set_identity: string;
  readonly signature_identity: string;
  readonly interpretation_contract_identity: string;
  readonly semantic_compilation_candidate_identity: string;
  readonly semantic_compilation_candidate_sha256: string;
  readonly candidate_structure_result_identity: string;
  readonly candidate_structure_result_sha256: string;
  readonly candidate_model_content_identity: string;
  readonly record_provenance: readonly AxiomRecordProvenance[];
  readonly evaluated_members: readonly JsonValue[];
  readonly selections: readonly JsonValue[];
  readonly generated_source_keys: readonly JsonValue[];
  readonly compilation_residuals: readonly JsonValue[];
  readonly proposal_dispositions: readonly Readonly<{
    proposal_ref: string;
    proposal_kind: "evaluated_member" | "model_record" | "selection" | "generated_source_key" | "compilation_residual";
    decision: "accepted_unchanged" | "accepted_modified" | "rejected" | "resolved" | "retained_uncertain";
    final_refs: readonly string[];
    rationale: string;
  }>[];
  readonly author: Readonly<{
    traversal_ref: string;
    actor_identity: string;
    authority_identity: string;
    grant_identity: string;
    grant_scope: string;
    subject_identity: string;
    subject_sha256: string;
    basis_refs: readonly string[];
    decided_at: string;
    evidence_refs: readonly string[];
  }>;
  readonly supersedes: string | null;
}

export interface SemanticSelectionJudgment extends Readonly<Record<string, unknown>> {
  readonly kind: "stdo-representation.authority-acceptance";
  readonly schema_version: 1;
  readonly subject_kind: "interpreted_model";
  readonly subject_identity: string;
  readonly subject_sha256: string;
  readonly traversal_ref: string;
  readonly actor_identity: string;
  readonly authority_identity: string;
  readonly grant_identity: string;
  readonly grant_scope: string;
  readonly basis_refs: readonly string[];
  readonly admitting_authority_refs: null;
  readonly evidence_refs: readonly string[];
  readonly decision: "accepted" | "rejected";
  readonly decided_at: string;
  readonly supersedes: string | null;
}

export interface AuthorityGrantArtifact extends Readonly<Record<string, unknown>> {
  readonly kind: "stdo-index.authority-grant";
  readonly schema_version: 1;
  readonly grant_identity: string;
  readonly actor_identity: string;
  readonly authority_identity: string;
  readonly grant_scope: string;
  readonly basis_refs: readonly string[];
  readonly source_ref: string;
  readonly source_sha256: string;
}

interface CandidateStructureEvaluationGrant extends Readonly<Record<string, unknown>> {
  readonly kind: "stdo-representation.candidate-structure-evaluation-grant";
  readonly schema_version: 1;
  readonly issuer_actor_identity: string;
  readonly authority_identity: string;
  readonly parent_grant_identity: string;
  readonly grantee_identity: string;
  readonly grant_scope: string;
  readonly traversal_ref: string;
  readonly functor_ref: string;
  readonly subject_identity: string;
  readonly subject_sha256: string;
  readonly calculus_basis_identity: string;
  readonly signature_identity: string;
  readonly signature_sha256: string;
  readonly interpretation_contract_identity: string;
  readonly interpretation_contract_sha256: string;
  readonly what_member_set_identity: string;
  readonly frame_basis_identity: string;
  readonly frame_basis_sha256: string;
  readonly evidence_refs: readonly string[];
  readonly issued_at: string;
  readonly source_ref: string;
  readonly source_sha256: string;
}

interface SignatureRecordKind {
  readonly population: PopulationName;
  readonly identity: string;
  readonly required_nonempty: boolean;
  readonly maximum_records: number | null;
}

interface SignatureValueDomain extends Readonly<Record<string, unknown>> {
  readonly id: string;
  readonly kind: string;
}

interface SignatureRelationKind {
  readonly id: string;
  readonly source_sorts: readonly string[];
  readonly target_sorts: readonly string[];
  readonly qualifier_mode: "exactly_one_of" | "zero_or_more_of";
  readonly allowed_qualifiers: readonly string[];
}

interface SignatureConstraintKind {
  readonly id: string;
  readonly judgment_kind: string;
  readonly subject_populations: readonly PopulationName[];
  readonly predicate_domain: string;
  readonly refusal_domain: string;
}

interface SignatureResidualContract {
  readonly kind: string;
  readonly subject_populations: readonly PopulationName[];
  readonly external_target_kinds: readonly string[];
  readonly uncertainty_domain: string;
  readonly consequence_domain: string;
  readonly re_entry_domain: string;
  readonly invalidation_domain: string;
}

interface SignatureReferenceDomain {
  readonly identity: string;
  readonly population: PopulationName;
  readonly field: string;
  readonly cardinality: "exactly_one" | "zero_or_one" | "one_or_more" | "zero_or_more";
  readonly allowed_local_record_kinds: readonly string[];
  readonly allowed_semantic_object_sorts: readonly string[];
  readonly allowed_external_target_kinds: readonly string[];
  readonly required_basis_relation: string | null;
}

interface TargetSignature {
  readonly identity: string;
  readonly sha256: string;
  readonly recordKinds: ReadonlyMap<PopulationName, SignatureRecordKind>;
  readonly sorts: ReadonlySet<string>;
  readonly valueDomains: ReadonlyMap<string, SignatureValueDomain>;
  readonly sortValueDomains: ReadonlyMap<string, string>;
  readonly recordValueDomains: ReadonlyMap<string, string>;
  readonly relationKinds: ReadonlyMap<string, SignatureRelationKind>;
  readonly constraintKinds: ReadonlyMap<string, SignatureConstraintKind>;
  readonly residualContracts: ReadonlyMap<string, SignatureResidualContract>;
  readonly functorKinds: ReadonlySet<string>;
  readonly judgmentKinds: ReadonlySet<string>;
  readonly stopKinds: ReadonlySet<string>;
  readonly referenceDomains: ReadonlyMap<string, SignatureReferenceDomain>;
  readonly externalTargetKinds: ReadonlyMap<string, string>;
}

type PopulationName = "O" | "E" | "C" | "L" | "X" | "V" | "T" | "J";

export interface AxiomIndexGtlInput {
  readonly semantic_compilation_proposal_bytes: Uint8Array;
  readonly semantic_compilation_candidate_bytes: Uint8Array;
  readonly compiler_provenance_bundle_bytes: Uint8Array;
  readonly compiler_provenance_member_bytes: Readonly<Record<string, Uint8Array>>;
  readonly accepted_program_bytes: Uint8Array;
  readonly selection_ledger_bytes: Uint8Array;
  readonly semantic_judgment_bytes: Uint8Array;
  readonly candidate_structure_result_bytes: Uint8Array;
  readonly source_manifest_bytes: Uint8Array;
  readonly target_signature_bytes: Uint8Array;
  readonly interpretation_contract_bytes: Uint8Array;
  readonly frame_basis_bytes: Uint8Array;
  readonly structure_grant_bytes: Uint8Array;
  readonly structure_grant_source_bytes: Uint8Array;
  readonly semantic_grant_bytes: Uint8Array;
  readonly semantic_grant_source_bytes: Uint8Array;
  readonly profile_bytes: Uint8Array;
  readonly publisher: PublisherArtifactBasis;
  readonly publisher_manifest_bytes: Uint8Array;
  readonly publisher_artifact_bytes: Uint8Array;
}

export interface AxiomIndexGtlCandidate {
  readonly canonical_bytes: Uint8Array;
  readonly publication: ModulePublication;
  readonly receipt: Readonly<{
    kind: "stdo-index.gtl-carrier-candidate";
    schema_version: 1;
    machine_path: typeof AXIOM_INDEX_MACHINE;
    interpreted_model_identity: string;
    interpreted_model_sha256: string;
    accepted_program_identity: string;
    accepted_program_sha256: string;
    selection_ledger_identity: string;
    selection_ledger_sha256: string;
    semantic_judgment_identity: string;
    semantic_judgment_sha256: string;
    profile_identity: string;
    profile_sha256: string;
    publisher_product_identity: string;
    publisher_manifest_sha256: string;
    carrier_sha256: string;
    frozen_gtl_validation: "valid";
    profile_round_trip: "valid";
    carrier_admission: "not_evaluated";
  }>;
}

export const STDO_AXIOM_INDEX_GTL_PRODUCT_SEMANTICS = Object.freeze({
  kind: "stdo_axiom_index_gtl_product_semantics",
  schemaVersion: 4,
  profileIdentity: PROFILE_IDENTITY,
  contractRef: RECORD_CONTRACT_REF,
});

function fail(path: string, message: string): never {
  throw new TypeError(`${path}: ${message}`);
}

function requireExact(value: unknown, keys: readonly string[], path: string): asserts value is Readonly<Record<string, unknown>> {
  if (!isRecord(value) || !exactKeys(value, keys)) fail(path, `must contain exactly ${keys.join(", ")}`);
}

function requireString(value: unknown, path: string): string {
  if (typeof value !== "string" || value.length === 0) fail(path, "must be a non-empty string");
  return value;
}

function requireIdentity(value: unknown, path: string): string {
  const identity = requireString(value, path);
  if (!/^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$/u.test(identity)) fail(path, "must be an absolute identity URI");
  return identity;
}

function requireUriReference(value: unknown, path: string): string {
  const reference = requireString(value, path);
  if (/\s/u.test(reference)) fail(path, "must be a URI reference without whitespace");
  return reference;
}

function requireTimestamp(value: unknown, path: string): string {
  const timestamp = requireString(value, path);
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/u.test(timestamp) || Number.isNaN(Date.parse(timestamp))) {
    fail(path, "must be an RFC3339 timestamp");
  }
  return timestamp;
}

function requireSha256(value: unknown, path: string): string {
  const text = requireString(value, path);
  if (!/^sha256:[0-9a-f]{64}$/u.test(text)) fail(path, "must be one lowercase sha256 digest");
  return text;
}

function requireStringArray(value: unknown, path: string, allowEmpty = true): readonly string[] {
  if (!Array.isArray(value) || (!allowEmpty && value.length === 0)) fail(path, "must be an array with the required cardinality");
  return value.map((entry, index) => requireString(entry, `${path}[${index}]`));
}

function requireStrings(value: unknown, path: string, allowEmpty = true): readonly string[] {
  const result = requireStringArray(value, path, allowEmpty);
  if (new Set(result).size !== result.length || result.join("\0") !== [...result].sort(compareUnicodeCodeUnits).join("\0")) {
    fail(path, "must be duplicate-free and canonically sorted");
  }
  return result;
}

function requireJsonSet(value: unknown, path: string): readonly JsonValue[] {
  if (!Array.isArray(value)) fail(path, "must be an array");
  const result = value as readonly JsonValue[];
  const canonical = result.map((entry, index) => {
    try {
      return canonicalJson(entry);
    } catch {
      fail(`${path}[${index}]`, "must be canonical JSON data");
    }
  });
  if (new Set(canonical).size !== canonical.length || canonical.join("\0") !== [...canonical].sort(compareUnicodeCodeUnits).join("\0")) {
    fail(path, "must be duplicate-free and canonically sorted");
  }
  return result;
}

function artifactBytes(value: JsonValue): Uint8Array {
  return new TextEncoder().encode(`${canonicalJson(value)}\n`);
}

function canonicalRecordBytes(value: JsonValue): Uint8Array {
  return new TextEncoder().encode(canonicalJson(value));
}

function parseCanonicalArtifact(bytes: Uint8Array, path: string): Readonly<Record<string, unknown>> {
  const value = parseUniqueJson(bytes, path);
  if (!isRecord(value)) fail(path, "must be a JSON object");
  const expected = artifactBytes(value as JsonValue);
  if (expected.length !== bytes.length || expected.some((byte, index) => byte !== bytes[index])) {
    fail(path, "must be exact canonical JSON followed by one LF");
  }
  return value;
}

function parseCanonicalRecord(bytes: Uint8Array, path: string): Readonly<Record<string, unknown>> {
  const value = parseUniqueJson(bytes, path);
  if (!isRecord(value)) fail(path, "must be a JSON object");
  const expected = canonicalRecordBytes(value as JsonValue);
  if (expected.length !== bytes.length || expected.some((byte, index) => byte !== bytes[index])) fail(path, "must be exact unframed canonical JSON");
  return value;
}

function contentIdentity(prefix: string, bytes: Uint8Array): string {
  return `${prefix}${sha256Bytes(bytes).slice("sha256:".length)}`;
}

function carrierBasisIdentity(coordinate: CarrierBasisCoordinate): string {
  return `${CARRIER_BASIS_PREFIX}${sha256Canonical(coordinate).slice("sha256:".length)}`;
}

function requireCarrierBasisCoordinate(value: unknown, path: string): CarrierBasisCoordinate {
  requireExact(value, ["authority_inventory_count", "authority_root", "authority_tree_sha1", "commit_sha1", "repository"], path);
  if (!Number.isSafeInteger(value.authority_inventory_count) || (value.authority_inventory_count as number) <= 0) fail(`${path}.authority_inventory_count`, "must be one positive safe integer");
  const coordinate: CarrierBasisCoordinate = {
    authority_inventory_count: value.authority_inventory_count as number,
    authority_root: requireString(value.authority_root, `${path}.authority_root`),
    authority_tree_sha1: requireString(value.authority_tree_sha1, `${path}.authority_tree_sha1`),
    commit_sha1: requireString(value.commit_sha1, `${path}.commit_sha1`),
    repository: requireIdentity(value.repository, `${path}.repository`),
  };
  if (!/^[0-9a-f]{40}$/u.test(coordinate.authority_tree_sha1)) fail(`${path}.authority_tree_sha1`, "must be one lowercase Git SHA-1");
  if (!/^[0-9a-f]{40}$/u.test(coordinate.commit_sha1)) fail(`${path}.commit_sha1`, "must be one lowercase Git SHA-1");
  if (coordinate.authority_root.startsWith("/") || !coordinate.authority_root.endsWith("/") || coordinate.authority_root.includes("\\") || coordinate.authority_root.split("/").slice(0, -1).some((part) => !part || part === "..")) fail(`${path}.authority_root`, "must be one normalized relative directory ending in slash");
  return coordinate;
}

function requireCoordinate(value: unknown, path: string): BasisCoordinate {
  requireExact(value, ["identity", "sha256"], path);
  return {
    identity: requireString(value.identity, `${path}.identity`),
    sha256: requireSha256(value.sha256, `${path}.sha256`),
  };
}

function validateSubjectManifest(bytes: Uint8Array): ReadonlyMap<string, string> {
  if (sha256Bytes(bytes) !== STDO_MANIFEST_SHA256) fail("source_manifest", "does not equal the exact installed STDO 2.5 manifest bytes");
  const value = parseUniqueJson(bytes, "source_manifest");
  requireExact(value, ["auxiliary", "kind", "release", "schema_version", "standards"], "source_manifest");
  if (value.kind !== "stdo.installed-release-manifest" || value.schema_version !== 1) fail("source_manifest", "has the wrong installed-manifest contract");
  requireExact(value.release, ["commit", "cut", "standards_tree", "tag_object", "tree"], "source_manifest.release");
  const releaseExpected = {
    commit: "ca6694314c4e9a56d3facae3eef06fe2792104c9",
    cut: "v2.5.0-rc.1",
    standards_tree: "48a3e52b0aaf24b6d1d38ff551349e19b9b3c208",
    tag_object: "42f59b6cd24071d9c445a29ae2a691cf0828211e",
    tree: "f0fac91f195b1f1506423060556bd36b3256d835",
  } as const;
  for (const [field, expected] of Object.entries(releaseExpected)) if (value.release[field] !== expected) fail(`source_manifest.release.${field}`, "does not bind the selected immutable release");
  requireExact(value.standards, ["installed_root", "member_count", "member_set_sha256", "members", "source_root"], "source_manifest.standards");
  if (value.standards.installed_root !== "standards" || value.standards.source_root !== "specification/standards" || value.standards.member_count !== 51 || value.standards.member_set_sha256 !== STDO_MEMBER_SET_SHA256.slice("sha256:".length)) {
    fail("source_manifest.standards", "does not bind the exact selected 51-member standards population");
  }
  const members = requireRecordRows(value.standards.members, ["path", "sha256"], "source_manifest.standards.members");
  if (members.length !== 51) fail("source_manifest.standards.members", "must contain exactly 51 members");
  const result = new Map<string, string>();
  const aggregateRows: string[] = [];
  let previous = "";
  for (const [index, member] of members.entries()) {
    const path = requireRelativePath(member.path, `source_manifest.standards.members[${index}].path`);
    const digest = requireSha256(`sha256:${requireString(member.sha256, `source_manifest.standards.members[${index}].sha256`)}`, `source_manifest.standards.members[${index}].sha256`);
    if (result.has(path) || (index > 0 && compareUnicodeCodeUnits(previous, path) >= 0)) fail("source_manifest.standards.members", "must be path-sorted and duplicate-free");
    previous = path;
    result.set(path, digest);
    aggregateRows.push(`${digest.slice("sha256:".length)}  specification/standards/${path}\n`);
  }
  if (sha256Bytes(aggregateRows.join("")) !== STDO_MEMBER_SET_SHA256) fail("source_manifest.standards.member_set_sha256", "does not reproduce from the exact member inventory");
  return result;
}

function requireRelativePath(value: unknown, path: string): string {
  const memberPath = requireString(value, path);
  if (memberPath.startsWith("/") || memberPath.includes("\\") || memberPath.split("/").some((part) => !part || part === "." || part === "..")) {
    fail(path, "must be a normalized relative path");
  }
  return memberPath;
}

interface ValidatedCompilerProvenanceBundle {
  readonly digest: string;
  readonly members: ReadonlyMap<string, Readonly<{ member_ref: string; member_sha256: string }>>;
}

function validateCompilerProvenanceBundle(
  bundleBytes: Uint8Array,
  suppliedMemberBytes: Readonly<Record<string, Uint8Array>>,
): ValidatedCompilerProvenanceBundle {
  const path = "compiler_provenance_bundle";
  const value = parseCanonicalRecord(bundleBytes, path);
  requireExact(value, ["kind", "members", "schema_version"], path);
  if (value.kind !== "stdo-representation.compiler-provenance-bundle" || value.schema_version !== 1) fail(path, "has the wrong compiler-provenance bundle contract");
  const rows = requireRecordRows(value.members, ["member_kind", "member_ref", "member_sha256"], `${path}.members`);
  if (rows.length !== COMPILER_PROVENANCE_MEMBER_KINDS.length) fail(`${path}.members`, "must contain exactly the nine declared provenance members");
  const members = new Map<string, Readonly<{ member_ref: string; member_sha256: string }>>();
  const refs = new Set<string>();
  for (const [index, row] of rows.entries()) {
    const rowPath = `${path}.members[${index}]`;
    const memberKind = requireString(row.member_kind, `${rowPath}.member_kind`);
    if (memberKind !== COMPILER_PROVENANCE_MEMBER_KINDS[index]) fail(`${path}.members`, "must be member-kind sorted and contain exactly the nine declared kinds");
    const memberRef = requireUriReference(row.member_ref, `${rowPath}.member_ref`);
    if (refs.has(memberRef)) fail(`${path}.members`, "must resolve nine duplicate-free member references");
    refs.add(memberRef);
    const memberSha256 = requireSha256(row.member_sha256, `${rowPath}.member_sha256`);
    const memberBytes = suppliedMemberBytes[memberRef];
    if (!(memberBytes instanceof Uint8Array) || memberBytes.length === 0) fail(`${rowPath}.member_ref`, "does not resolve supplied exact non-empty member bytes");
    if (sha256Bytes(memberBytes) !== memberSha256) fail(`${rowPath}.member_sha256`, "does not reproduce from the supplied exact member bytes");
    members.set(memberKind, { member_ref: memberRef, member_sha256: memberSha256 });
  }
  const suppliedRefs = Object.keys(suppliedMemberBytes).sort(compareUnicodeCodeUnits);
  const declaredRefs = [...refs].sort(compareUnicodeCodeUnits);
  if (suppliedRefs.join("\0") !== declaredRefs.join("\0")) fail("compiler_provenance_member_bytes", "must resolve exactly the declared bundle-member references without extras or omissions");
  return { digest: sha256Bytes(bundleBytes), members };
}

function populationName(value: unknown, path: string): PopulationName {
  const name = requireString(value, path);
  if (!(["O", "E", "C", "L", "X", "V", "T", "J"] as const).includes(name as PopulationName)) fail(path, "must name one core population");
  return name as PopulationName;
}

function exactStringSet(value: unknown, path: string, allowEmpty = true): readonly string[] {
  const result = requireStringArray(value, path, allowEmpty);
  if (new Set(result).size !== result.length) fail(path, "must be duplicate-free");
  return result;
}

function validateTargetSignature(bytes: Uint8Array, coordinate: BasisCoordinate): TargetSignature {
  const digest = sha256Bytes(bytes);
  if (digest !== coordinate.sha256) fail("target_signature", "bytes do not match the candidate signature coordinate");
  if (coordinate.identity !== TARGET_SIGNATURE_IDENTITY || coordinate.sha256 !== TARGET_SIGNATURE_SHA256) fail("target_signature", "does not bind the frozen STDO 2.5 target signature identity and bytes");
  const value = parseUniqueJson(bytes, "target_signature");
  requireExact(value, ["calculus_concept", "constraint_kinds", "external_target_kinds", "functor_kinds", "identity", "judgment_contracts", "judgment_kinds", "kind", "record_kinds", "record_value_domains", "reference_domains", "relation_kinds", "residual_contracts", "residual_kinds", "schema_version", "sort_value_domains", "sorts", "stop_kinds", "traversal_permissions", "value_domains"], "target_signature");
  if (value.kind !== "stdo-index.target-signature" || value.schema_version !== 2 || value.identity !== coordinate.identity || value.calculus_concept !== CALCULUS_CONCEPT_IDENTITY) fail("target_signature", "does not bind the selected closed a_c signature");

  const coreKinds = new Map<PopulationName, string>([
    ["O", "urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object"],
    ["E", "urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation"],
    ["C", "urn:stdo:concept:axiomatic-calculus:record-kind:constraint"],
    ["L", "urn:stdo:concept:axiomatic-calculus:record-kind:latitude"],
    ["X", "urn:stdo:concept:axiomatic-calculus:record-kind:residual"],
    ["V", "urn:stdo:concept:axiomatic-calculus:record-kind:traversal"],
    ["T", "urn:stdo:concept:axiomatic-calculus:record-kind:transformation"],
    ["J", "urn:stdo:concept:axiomatic-calculus:record-kind:judgment"],
  ]);
  const recordKinds = new Map<PopulationName, SignatureRecordKind>();
  for (const [index, row] of requireRecordRows(value.record_kinds, ["identity", "maximum_records", "name", "population", "required_nonempty"], "target_signature.record_kinds").entries()) {
    const population = populationName(row.population, `target_signature.record_kinds[${index}].population`);
    const identity = requireIdentity(row.identity, `target_signature.record_kinds[${index}].identity`);
    requireString(row.name, `target_signature.record_kinds[${index}].name`);
    const maximumRecords = row.maximum_records === null ? null : Number(row.maximum_records);
    if (
      typeof row.required_nonempty !== "boolean"
      || (maximumRecords !== null && (!Number.isSafeInteger(maximumRecords) || maximumRecords < 0))
      || (row.required_nonempty === true && maximumRecords === 0)
      || coreKinds.get(population) !== identity
      || recordKinds.has(population)
    ) fail(`target_signature.record_kinds[${index}]`, "does not preserve one exact core record-kind mapping and cardinality");
    recordKinds.set(population, { population, identity, required_nonempty: row.required_nonempty, maximum_records: maximumRecords });
  }
  if (recordKinds.size !== coreKinds.size) fail("target_signature.record_kinds", "must map all eight core populations exactly once");
  if (recordKinds.get("T")?.maximum_records !== 0) fail("target_signature.record_kinds", "must declare T maximum_records = 0 until an exact AC-013 specialization exists");

  const sorts = new Set(exactStringSet(value.sorts, "target_signature.sorts", false));
  const valueDomains = new Map<string, SignatureValueDomain>();
  for (const [index, raw] of (Array.isArray(value.value_domains) ? value.value_domains : fail("target_signature.value_domains", "must be an array")).entries()) {
    if (!isRecord(raw)) fail(`target_signature.value_domains[${index}]`, "must be an object");
    const id = requireString(raw.id, `target_signature.value_domains[${index}].id`);
    const kind = requireString(raw.kind, `target_signature.value_domains[${index}].kind`);
    if (valueDomains.has(id)) fail("target_signature.value_domains", "contains a duplicate identity");
    if (kind === "nonempty_string") {
      requireExact(raw, ["id", "kind", "max_length"], `target_signature.value_domains[${index}]`);
      if (!Number.isSafeInteger(raw.max_length) || (raw.max_length as number) < 1) fail(`target_signature.value_domains[${index}].max_length`, "must be a positive integer");
    } else if (kind === "pattern_string") {
      requireExact(raw, ["id", "kind", "pattern"], `target_signature.value_domains[${index}]`);
      try { new RegExp(requireString(raw.pattern, `target_signature.value_domains[${index}].pattern`), "u"); } catch { fail(`target_signature.value_domains[${index}].pattern`, "must be a valid regular expression"); }
    } else if (kind === "sorted_unique_array") {
      requireExact(raw, ["id", "item_domain", "kind"], `target_signature.value_domains[${index}]`);
      requireString(raw.item_domain, `target_signature.value_domains[${index}].item_domain`);
    } else fail(`target_signature.value_domains[${index}].kind`, "is not supported by this encoding profile");
    valueDomains.set(id, raw as SignatureValueDomain);
  }

  const sortValueDomains = new Map<string, string>();
  for (const [index, row] of requireRecordRows(value.sort_value_domains, ["sort", "domain"], "target_signature.sort_value_domains").entries()) {
    const sort = requireString(row.sort, `target_signature.sort_value_domains[${index}].sort`);
    const domain = requireString(row.domain, `target_signature.sort_value_domains[${index}].domain`);
    if (!sorts.has(sort) || !valueDomains.has(domain) || sortValueDomains.has(sort)) fail(`target_signature.sort_value_domains[${index}]`, "does not resolve one declared sort and value domain");
    sortValueDomains.set(sort, domain);
  }
  if (sortValueDomains.size !== sorts.size) fail("target_signature.sort_value_domains", "must disposition every declared sort exactly once");

  const recordValueDomains = new Map<string, string>();
  for (const [index, row] of requireRecordRows(value.record_value_domains, ["population", "field", "domain"], "target_signature.record_value_domains").entries()) {
    const population = populationName(row.population, `target_signature.record_value_domains[${index}].population`);
    const field = requireString(row.field, `target_signature.record_value_domains[${index}].field`);
    const domain = requireString(row.domain, `target_signature.record_value_domains[${index}].domain`);
    const key = `${population}.${field}`;
    if (!valueDomains.has(domain) || recordValueDomains.has(key)) fail(`target_signature.record_value_domains[${index}]`, "does not resolve one unique value domain");
    recordValueDomains.set(key, domain);
  }

  const relationKinds = new Map<string, SignatureRelationKind>();
  for (const [index, row] of requireRecordRows(value.relation_kinds, ["allowed_qualifiers", "id", "qualifier_mode", "source_sorts", "target_sorts"], "target_signature.relation_kinds").entries()) {
    const id = requireString(row.id, `target_signature.relation_kinds[${index}].id`);
    const sourceSorts = exactStringSet(row.source_sorts, `target_signature.relation_kinds[${index}].source_sorts`, false);
    const targetSorts = exactStringSet(row.target_sorts, `target_signature.relation_kinds[${index}].target_sorts`, false);
    const allowedQualifiers = exactStringSet(row.allowed_qualifiers, `target_signature.relation_kinds[${index}].allowed_qualifiers`);
    const qualifierMode = requireString(row.qualifier_mode, `target_signature.relation_kinds[${index}].qualifier_mode`);
    if (!(["exactly_one_of", "zero_or_more_of"] as const).includes(qualifierMode as SignatureRelationKind["qualifier_mode"]) || relationKinds.has(id)) fail(`target_signature.relation_kinds[${index}]`, "has a duplicate or unknown qualifier mode");
    for (const sort of [...sourceSorts, ...targetSorts]) if (sort !== "*" && !sorts.has(sort)) fail(`target_signature.relation_kinds[${index}]`, "references an undeclared sort");
    relationKinds.set(id, { id, source_sorts: sourceSorts, target_sorts: targetSorts, qualifier_mode: qualifierMode as SignatureRelationKind["qualifier_mode"], allowed_qualifiers: allowedQualifiers });
  }

  const judgmentKinds = new Set(exactStringSet(value.judgment_kinds, "target_signature.judgment_kinds", false));
  const constraintKinds = new Map<string, SignatureConstraintKind>();
  for (const [index, row] of requireRecordRows(value.constraint_kinds, ["id", "judgment_kind", "predicate_domain", "refusal_domain", "subject_populations"], "target_signature.constraint_kinds").entries()) {
    const id = requireString(row.id, `target_signature.constraint_kinds[${index}].id`);
    const judgmentKind = requireString(row.judgment_kind, `target_signature.constraint_kinds[${index}].judgment_kind`);
    const predicateDomain = requireString(row.predicate_domain, `target_signature.constraint_kinds[${index}].predicate_domain`);
    const refusalDomain = requireString(row.refusal_domain, `target_signature.constraint_kinds[${index}].refusal_domain`);
    const subjectPopulations = (Array.isArray(row.subject_populations) ? row.subject_populations : fail(`target_signature.constraint_kinds[${index}].subject_populations`, "must be an array")).map((entry, subjectIndex) => populationName(entry, `target_signature.constraint_kinds[${index}].subject_populations[${subjectIndex}]`));
    if (constraintKinds.has(id) || !judgmentKinds.has(judgmentKind) || !valueDomains.has(predicateDomain) || !valueDomains.has(refusalDomain)) fail(`target_signature.constraint_kinds[${index}]`, "does not resolve its declared domains");
    constraintKinds.set(id, { id, judgment_kind: judgmentKind, subject_populations: subjectPopulations, predicate_domain: predicateDomain, refusal_domain: refusalDomain });
  }

  const residualContracts = new Map<string, SignatureResidualContract>();
  for (const [index, row] of requireRecordRows(value.residual_contracts, ["consequence_domain", "external_target_kinds", "invalidation_domain", "kind", "re_entry_domain", "subject_populations", "uncertainty_domain"], "target_signature.residual_contracts").entries()) {
    const kind = requireString(row.kind, `target_signature.residual_contracts[${index}].kind`);
    const subjectPopulations = (Array.isArray(row.subject_populations) ? row.subject_populations : fail(`target_signature.residual_contracts[${index}].subject_populations`, "must be an array")).map((entry, subjectIndex) => populationName(entry, `target_signature.residual_contracts[${index}].subject_populations[${subjectIndex}]`));
    const externalTargetKinds = exactStringSet(row.external_target_kinds, `target_signature.residual_contracts[${index}].external_target_kinds`);
    const domains = ["uncertainty_domain", "consequence_domain", "re_entry_domain", "invalidation_domain"] as const;
    for (const domain of domains) if (!valueDomains.has(requireString(row[domain], `target_signature.residual_contracts[${index}].${domain}`))) fail(`target_signature.residual_contracts[${index}].${domain}`, "does not resolve a value domain");
    if (residualContracts.has(kind)) fail("target_signature.residual_contracts", "contains a duplicate kind");
    residualContracts.set(kind, { kind, subject_populations: subjectPopulations, external_target_kinds: externalTargetKinds, uncertainty_domain: row.uncertainty_domain as string, consequence_domain: row.consequence_domain as string, re_entry_domain: row.re_entry_domain as string, invalidation_domain: row.invalidation_domain as string });
  }
  const residualKinds = exactStringSet(value.residual_kinds, "target_signature.residual_kinds");
  if (canonicalJson(residualKinds as unknown as JsonValue) !== canonicalJson([...residualContracts.keys()].sort(compareUnicodeCodeUnits) as unknown as JsonValue)) fail("target_signature.residual_kinds", "must equal the residual contract kinds");

  const externalTargetKinds = new Map<string, string>();
  for (const [index, row] of requireRecordRows(value.external_target_kinds, ["identity", "required_basis_relation"], "target_signature.external_target_kinds").entries()) {
    const identity = requireIdentity(row.identity, `target_signature.external_target_kinds[${index}].identity`);
    const relation = requireIdentity(row.required_basis_relation, `target_signature.external_target_kinds[${index}].required_basis_relation`);
    if (externalTargetKinds.has(identity)) fail("target_signature.external_target_kinds", "contains a duplicate identity");
    externalTargetKinds.set(identity, relation);
  }

  const referenceDomains = new Map<string, SignatureReferenceDomain>();
  for (const [index, row] of requireRecordRows(value.reference_domains, ["allowed_external_target_kinds", "allowed_local_record_kinds", "allowed_semantic_object_sorts", "cardinality", "field", "identity", "population", "required_basis_relation"], "target_signature.reference_domains").entries()) {
    const identity = requireIdentity(row.identity, `target_signature.reference_domains[${index}].identity`);
    const population = populationName(row.population, `target_signature.reference_domains[${index}].population`);
    const field = requireString(row.field, `target_signature.reference_domains[${index}].field`);
    const cardinality = requireString(row.cardinality, `target_signature.reference_domains[${index}].cardinality`);
    if (!(["exactly_one", "zero_or_one", "one_or_more", "zero_or_more"] as const).includes(cardinality as SignatureReferenceDomain["cardinality"])) fail(`target_signature.reference_domains[${index}].cardinality`, "is unknown");
    const localKinds = exactStringSet(row.allowed_local_record_kinds, `target_signature.reference_domains[${index}].allowed_local_record_kinds`);
    const objectSorts = exactStringSet(row.allowed_semantic_object_sorts, `target_signature.reference_domains[${index}].allowed_semantic_object_sorts`);
    const externalKinds = exactStringSet(row.allowed_external_target_kinds, `target_signature.reference_domains[${index}].allowed_external_target_kinds`);
    for (const kind of localKinds) if (![...coreKinds.values()].includes(kind)) fail(`target_signature.reference_domains[${index}].allowed_local_record_kinds`, "contains an undeclared record kind");
    for (const sort of objectSorts) if (sort !== "*" && !sorts.has(sort)) fail(`target_signature.reference_domains[${index}].allowed_semantic_object_sorts`, "contains an undeclared sort");
    for (const kind of externalKinds) if (!externalTargetKinds.has(kind)) fail(`target_signature.reference_domains[${index}].allowed_external_target_kinds`, "contains an undeclared external target kind");
    const requiredBasisRelation = row.required_basis_relation === null ? null : requireIdentity(row.required_basis_relation, `target_signature.reference_domains[${index}].required_basis_relation`);
    const key = `${population}.${field}`;
    if (referenceDomains.has(key)) fail("target_signature.reference_domains", "contains a duplicate field domain");
    referenceDomains.set(key, { identity, population, field, cardinality: cardinality as SignatureReferenceDomain["cardinality"], allowed_local_record_kinds: localKinds, allowed_semantic_object_sorts: objectSorts, allowed_external_target_kinds: externalKinds, required_basis_relation: requiredBasisRelation });
  }

  const functorKinds = new Set(exactStringSet(value.functor_kinds, "target_signature.functor_kinds", false));
  for (const functor of [F_D, F_P, F_H]) if (!functorKinds.has(functor)) fail("target_signature.functor_kinds", "must contain the three exact a_c functor kinds");
  const stopKinds = new Set(exactStringSet(value.stop_kinds, "target_signature.stop_kinds", false));
  for (const [section, keys] of [["judgment_contracts", ["evidence", "inputs", "kind", "outputs", "stops"]], ["traversal_permissions", ["codomain", "domain", "functor", "stops", "traversal"]]] as const) {
    for (const [index, row] of requireRecordRows(value[section], keys, `target_signature.${section}`).entries()) {
      for (const key of keys) if (key !== "kind" && key !== "functor" && key !== "traversal") exactStringSet(row[key], `target_signature.${section}[${index}].${key}`);
      if (section === "judgment_contracts" && !judgmentKinds.has(requireString(row.kind, `target_signature.${section}[${index}].kind`))) fail(`target_signature.${section}[${index}].kind`, "is undeclared");
      if (section === "traversal_permissions" && !functorKinds.has(requireIdentity(row.functor, `target_signature.${section}[${index}].functor`))) fail(`target_signature.${section}[${index}].functor`, "is undeclared");
    }
  }
  return { identity: coordinate.identity, sha256: digest, recordKinds, sorts, valueDomains, sortValueDomains, recordValueDomains, relationKinds, constraintKinds, residualContracts, functorKinds, judgmentKinds, stopKinds, referenceDomains, externalTargetKinds };
}

function requireRecordRows(value: unknown, keys: readonly string[], path: string): readonly Readonly<Record<string, unknown>>[] {
  if (!Array.isArray(value)) fail(path, "must be an array");
  return value.map((row, index) => {
    requireExact(row, keys, `${path}[${index}]`);
    return row;
  });
}

function validateExternalResolution(value: unknown, path: string): AxiomExternalResolution {
  requireExact(value, ["external_identity", "reference_domain", "external_target_kind", "resolved_target_identity", "basis_relation", "resolution_basis", "evidence_identity"], path);
  for (const field of ["external_identity", "reference_domain", "external_target_kind", "resolved_target_identity", "basis_relation", "resolution_basis", "evidence_identity"] as const) requireString(value[field], `${path}.${field}`);
  return value as unknown as AxiomExternalResolution;
}

function validateExternalResolutionWitness(value: unknown, path: string): AxiomExternalResolutionWitness {
  requireExact(value, ["external_resolution", "domain_model", "codomain_model", "domain_resolution", "codomain_resolution", "decision", "evidence"], path);
  for (const field of ["external_resolution", "domain_model", "codomain_model", "evidence"] as const) requireString(value[field], `${path}.${field}`);
  if (value.decision !== "equal") fail(`${path}.decision`, "must be equal");
  const domainResolution = validateExternalResolution(value.domain_resolution, `${path}.domain_resolution`);
  const codomainResolution = validateExternalResolution(value.codomain_resolution, `${path}.codomain_resolution`);
  return {
    external_resolution: value.external_resolution as string,
    domain_model: value.domain_model as string,
    codomain_model: value.codomain_model as string,
    domain_resolution: domainResolution,
    codomain_resolution: codomainResolution,
    decision: "equal",
    evidence: value.evidence as string,
  };
}

function validateDomainValue(value: unknown, domainIdentity: string, signature: TargetSignature, path: string): void {
  const domain = signature.valueDomains.get(domainIdentity);
  if (domain === undefined) fail(path, `uses undeclared value domain ${domainIdentity}`);
  if (domain.kind === "nonempty_string") {
    const text = requireString(value, path);
    if (text.length > (domain.max_length as number)) fail(path, `exceeds ${String(domain.max_length)} characters`);
    return;
  }
  if (domain.kind === "pattern_string") {
    const text = requireString(value, path);
    if (!new RegExp(domain.pattern as string, "u").test(text)) fail(path, `does not satisfy ${String(domain.pattern)}`);
    return;
  }
  if (domain.kind === "sorted_unique_array") {
    const values = requireStrings(value, path);
    for (const [index, member] of values.entries()) validateDomainValue(member, domain.item_domain as string, signature, `${path}[${index}]`);
    return;
  }
  fail(path, `uses unsupported value domain ${domain.kind}`);
}

function recordDomain(signature: TargetSignature, population: PopulationName, field: string, value: unknown, path: string): void {
  const domain = signature.recordValueDomains.get(`${population}.${field}`);
  if (domain === undefined) fail(path, "has no declared signature value domain");
  validateDomainValue(value, domain, signature, path);
}

function referenceDomainIdentity(domain: SignatureReferenceDomain): string {
  return domain.identity;
}

function validateModel(value: unknown, signature: TargetSignature): AxiomModel {
  requireExact(value, ["b", "I", "O", "E", "C", "L", "X", "V", "T", "J", "ResolutionSet_M"], "accepted_program.model");
  const b = requireIdentity(value.b, "accepted_program.model.b");
  if (b !== MODEL_BASIS_IDENTITY) fail("accepted_program.model.b", "does not equal the exact basis identity derived from calculus, subject, signature, and interpretation-contract coordinates");
  const I = requireStrings(value.I, "accepted_program.model.I", false);
  const O = requireRecordRows(value.O, ["id", "sort", "context", "owner", "scope", "basis", "value"], "accepted_program.model.O") as unknown as readonly AxiomSemanticObject[];
  const E = requireRecordRows(value.E, ["id", "kind", "source", "target", "context", "owner", "scope", "basis", "qualifiers"], "accepted_program.model.E") as unknown as readonly AxiomTypedRelation[];
  const C = requireRecordRows(value.C, ["id", "kind", "applies_to", "predicate", "context", "owner", "scope", "basis", "judgment_kind", "latitude_ref", "refusal"], "accepted_program.model.C") as unknown as readonly AxiomConstraint[];
  const L = requireRecordRows(value.L, ["id", "applies_to", "allowed_variation", "forbidden_variation", "context", "owner", "scope", "basis", "invalidation"], "accepted_program.model.L") as unknown as readonly AxiomLatitude[];
  const X = requireRecordRows(value.X, ["id", "subject", "kind", "uncertainty", "consequence", "context", "owner", "scope", "basis", "re_entry", "invalidation"], "accepted_program.model.X") as unknown as readonly AxiomResidual[];
  const V = requireRecordRows(value.V, ["id", "domain", "codomain", "context", "owner", "scope", "basis", "preconditions", "postconditions", "authority", "evidence", "provenance", "stop_states"], "accepted_program.model.V") as unknown as readonly AxiomTraversal[];
  const T = requireRecordRows(value.T, ["id", "traversal", "domain_model", "codomain_model", "context", "owner", "scope", "basis", "operation_authority", "preconditions", "preservation_relation", "preserved", "introduced", "removed", "external_preserved", "external_introduced", "external_removed", "external_resolution_witnesses", "residuals", "evidence", "provenance", "stop_states", "invalidation", "re_entry"], "accepted_program.model.T") as unknown as readonly AxiomTransformation[];
  const J = requireRecordRows(value.J, ["id", "kind", "subject", "subject_digest", "context", "owner", "scope", "basis", "evaluator", "authority", "decision", "evidence", "provenance", "decided_at"], "accepted_program.model.J") as unknown as readonly AxiomJudgment[];
  const ResolutionSet_M = requireRecordRows(value.ResolutionSet_M, ["external_identity", "reference_domain", "external_target_kind", "resolved_target_identity", "basis_relation", "resolution_basis", "evidence_identity"], "accepted_program.model.ResolutionSet_M") as unknown as readonly AxiomExternalResolution[];
  const populations = { O, E, C, L, X, V, T, J } as const;
  for (const population of Object.keys(populations) as PopulationName[]) {
    const recordKind = signature.recordKinds.get(population);
    if (recordKind?.required_nonempty === true && populations[population].length === 0) fail(`accepted_program.model.${population}`, "is required to be non-empty by the selected signature");
    if (recordKind?.maximum_records !== null && recordKind?.maximum_records !== undefined && populations[population].length > recordKind.maximum_records) fail(`accepted_program.model.${population}`, `exceeds the selected signature maximum of ${String(recordKind.maximum_records)}`);
    const rowIds = populations[population].map((row) => requireIdentity(row.id, `accepted_program.model.${population}.id`));
    if (rowIds.join("\0") !== [...rowIds].sort(compareUnicodeCodeUnits).join("\0")) fail(`accepted_program.model.${population}`, "must be identity-sorted");
  }
  if (T.length !== 0) fail("accepted_program.model.T", "non-empty transformations require exact domain/codomain model artifacts and AC-013 delta evidence; this profile currently permits only the lawful empty T population");
  const identities = new Set(I);
  const records = [...O, ...E, ...C, ...L, ...X, ...V, ...T, ...J];
  const seen = new Set<string>();
  const local = new Map<string, { population: PopulationName; row: Readonly<Record<string, unknown>> }>();
  for (const population of Object.keys(populations) as PopulationName[]) {
    for (const row of populations[population]) local.set(row.id, { population, row: row as unknown as Readonly<Record<string, unknown>> });
  }
  for (const [index, row] of records.entries()) {
    const id = requireIdentity(row.id, `accepted_program.model.records[${index}].id`);
    if (!identities.has(id) || seen.has(id)) fail(`accepted_program.model.records[${index}].id`, "must resolve exactly once in I");
    seen.add(id);
    if (requireIdentity(row.basis, `accepted_program.model.records[${index}].basis`) !== b) fail(`accepted_program.model.records[${index}].basis`, "must equal model.b");
    requireString(row.scope, `accepted_program.model.records[${index}].scope`);
  }

  for (const [index, row] of O.entries()) {
    const sort = requireString(row.sort, `accepted_program.model.O[${index}].sort`);
    if (!signature.sorts.has(sort)) fail(`accepted_program.model.O[${index}].sort`, "is outside the closed signature");
    const valueDomain = signature.sortValueDomains.get(sort);
    if (valueDomain === undefined) fail(`accepted_program.model.O[${index}].sort`, "has no declared value domain");
    validateDomainValue(row.value, valueDomain, signature, `accepted_program.model.O[${index}].value`);
    recordDomain(signature, "O", "scope", row.scope, `accepted_program.model.O[${index}].scope`);
  }
  for (const [index, row] of E.entries()) {
    const contract = signature.relationKinds.get(requireString(row.kind, `accepted_program.model.E[${index}].kind`));
    if (contract === undefined) fail(`accepted_program.model.E[${index}].kind`, "is outside the closed signature");
    recordDomain(signature, "E", "scope", row.scope, `accepted_program.model.E[${index}].scope`);
    recordDomain(signature, "E", "qualifiers", row.qualifiers, `accepted_program.model.E[${index}].qualifiers`);
    const qualifiers = row.qualifiers as readonly string[];
    if (contract.qualifier_mode === "exactly_one_of" && qualifiers.length !== 1) fail(`accepted_program.model.E[${index}].qualifiers`, "must contain exactly one declared qualifier");
    if (qualifiers.some((qualifier) => !contract.allowed_qualifiers.includes(qualifier))) fail(`accepted_program.model.E[${index}].qualifiers`, "contains an undeclared qualifier");
    for (const [field, admittedSorts] of [["source", contract.source_sorts], ["target", contract.target_sorts]] as const) {
      const endpoint = local.get(requireIdentity(row[field], `accepted_program.model.E[${index}].${field}`));
      if (endpoint?.population !== "O") fail(`accepted_program.model.E[${index}].${field}`, "must resolve one semantic object");
      const sort = requireString(endpoint.row.sort, `accepted_program.model.E[${index}].${field}.sort`);
      if (!admittedSorts.includes("*") && !admittedSorts.includes(sort)) fail(`accepted_program.model.E[${index}].${field}`, "has a sort refused by the relation kind");
    }
  }
  for (const [index, row] of C.entries()) {
    const contract = signature.constraintKinds.get(requireString(row.kind, `accepted_program.model.C[${index}].kind`));
    if (contract === undefined) fail(`accepted_program.model.C[${index}].kind`, "is outside the closed signature");
    if (row.judgment_kind !== contract.judgment_kind) fail(`accepted_program.model.C[${index}].judgment_kind`, "does not equal the constraint-kind judgment");
    const subject = local.get(requireIdentity(row.applies_to, `accepted_program.model.C[${index}].applies_to`));
    if (subject === undefined || !contract.subject_populations.includes(subject.population)) fail(`accepted_program.model.C[${index}].applies_to`, "has a record kind refused by the constraint kind");
    validateDomainValue(row.predicate, contract.predicate_domain, signature, `accepted_program.model.C[${index}].predicate`);
    validateDomainValue(row.refusal, contract.refusal_domain, signature, `accepted_program.model.C[${index}].refusal`);
    recordDomain(signature, "C", "scope", row.scope, `accepted_program.model.C[${index}].scope`);
  }
  for (const [index, row] of L.entries()) {
    for (const field of ["allowed_variation", "forbidden_variation", "scope", "invalidation"] as const) recordDomain(signature, "L", field, row[field], `accepted_program.model.L[${index}].${field}`);
  }
  for (const [index, row] of X.entries()) {
    const contract = signature.residualContracts.get(requireString(row.kind, `accepted_program.model.X[${index}].kind`));
    if (contract === undefined) fail(`accepted_program.model.X[${index}].kind`, "is outside the closed signature");
    validateDomainValue(row.uncertainty, contract.uncertainty_domain, signature, `accepted_program.model.X[${index}].uncertainty`);
    validateDomainValue(row.consequence, contract.consequence_domain, signature, `accepted_program.model.X[${index}].consequence`);
    validateDomainValue(row.re_entry, contract.re_entry_domain, signature, `accepted_program.model.X[${index}].re_entry`);
    validateDomainValue(row.invalidation, contract.invalidation_domain, signature, `accepted_program.model.X[${index}].invalidation`);
    recordDomain(signature, "X", "scope", row.scope, `accepted_program.model.X[${index}].scope`);
  }
  for (const [index, row] of V.entries()) {
    for (const field of ["preconditions", "postconditions"] as const) {
      recordDomain(signature, "V", field, row[field], `accepted_program.model.V[${index}].${field}`);
    }
    recordDomain(signature, "V", "scope", row.scope, `accepted_program.model.V[${index}].scope`);
  }
  for (const [index, row] of J.entries()) {
    if (!signature.judgmentKinds.has(requireString(row.kind, `accepted_program.model.J[${index}].kind`))) fail(`accepted_program.model.J[${index}].kind`, "is outside the closed signature");
    if (!signature.stopKinds.has(requireString(row.decision, `accepted_program.model.J[${index}].decision`))) fail(`accepted_program.model.J[${index}].decision`, "is outside the closed stop algebra");
    for (const field of ["subject_digest", "scope", "decision", "decided_at"] as const) recordDomain(signature, "J", field, row[field], `accepted_program.model.J[${index}].${field}`);
    const subject = local.get(requireIdentity(row.subject, `accepted_program.model.J[${index}].subject`));
    if (subject === undefined || sha256Canonical(subject.row as unknown as JsonValue) !== row.subject_digest) fail(`accepted_program.model.J[${index}].subject_digest`, "does not bind the unchanged local subject under the profile record grammar");
  }

  const externalIdentities = new Set<string>();
  const resolutions = new Map<string, AxiomExternalResolution>();
  let previousExternal = "";
  for (const [index, row] of ResolutionSet_M.entries()) {
    const resolution = validateExternalResolution(row, `accepted_program.model.ResolutionSet_M[${index}]`);
    const externalIdentity = requireIdentity(resolution.external_identity, `accepted_program.model.ResolutionSet_M[${index}].external_identity`);
    if (externalIdentities.has(externalIdentity) || (index > 0 && compareUnicodeCodeUnits(previousExternal, externalIdentity) >= 0)) fail("accepted_program.model.ResolutionSet_M", "must be external-identity sorted and duplicate-free");
    previousExternal = externalIdentity;
    externalIdentities.add(externalIdentity);
    resolutions.set(externalIdentity, resolution);
    if (seen.has(externalIdentity)) fail(`accepted_program.model.ResolutionSet_M[${index}].external_identity`, "cannot resolve both locally and externally");
    const requiredRelation = signature.externalTargetKinds.get(requireIdentity(resolution.external_target_kind, `accepted_program.model.ResolutionSet_M[${index}].external_target_kind`));
    if (requiredRelation === undefined || resolution.basis_relation !== requiredRelation) fail(`accepted_program.model.ResolutionSet_M[${index}]`, "does not use one declared external target and basis relation");
    requireIdentity(resolution.reference_domain, `accepted_program.model.ResolutionSet_M[${index}].reference_domain`);
    requireIdentity(resolution.resolved_target_identity, `accepted_program.model.ResolutionSet_M[${index}].resolved_target_identity`);
    requireIdentity(resolution.basis_relation, `accepted_program.model.ResolutionSet_M[${index}].basis_relation`);
    requireIdentity(resolution.resolution_basis, `accepted_program.model.ResolutionSet_M[${index}].resolution_basis`);
    const evidence = local.get(requireIdentity(resolution.evidence_identity, `accepted_program.model.ResolutionSet_M[${index}].evidence_identity`));
    if (evidence?.population !== "O" || ![
      "urn:stdo-index:stdo:sort:evidence:1",
      "urn:stdo-index:stdo:sort:source-member:1",
    ].includes(requireString(evidence.row.sort, `accepted_program.model.ResolutionSet_M[${index}].evidence_identity.sort`))) fail(`accepted_program.model.ResolutionSet_M[${index}].evidence_identity`, "must resolve one evidence semantic object");
    if (resolution.resolved_target_identity !== externalIdentity) fail(`accepted_program.model.ResolutionSet_M[${index}].resolved_target_identity`, "must preserve the exact external identity in this same-coordinate profile");
    if (resolution.basis_relation === EXACT_MODEL_BASIS_RELATION) {
      if (externalIdentity !== MODEL_BASIS_IDENTITY || resolution.resolution_basis !== CALCULUS_BASIS_IDENTITY || resolution.evidence_identity !== MODEL_BASIS_EVIDENCE_IDENTITY) fail(`accepted_program.model.ResolutionSet_M[${index}]`, "does not equal the exact model-basis preimage resolution");
    }
    if (resolution.basis_relation === "urn:stdo-index:basis-relation:exact-target-signature:1") {
      if (resolution.resolution_basis !== signature.identity || resolution.evidence_identity !== SIGNATURE_EVIDENCE_IDENTITY) fail(`accepted_program.model.ResolutionSet_M[${index}].resolution_basis`, "must bind the exact selected target signature and its evidence identity");
      const declaredSignatureMember = signature.sorts.has(externalIdentity)
        || signature.relationKinds.has(externalIdentity)
        || signature.constraintKinds.has(externalIdentity)
        || signature.residualContracts.has(externalIdentity)
        || signature.functorKinds.has(externalIdentity)
        || signature.judgmentKinds.has(externalIdentity)
        || signature.stopKinds.has(externalIdentity);
      if (!declaredSignatureMember) fail(`accepted_program.model.ResolutionSet_M[${index}].external_identity`, "is not a member of the exact selected target signature");
    }
  }

  const recordKindByPopulation = new Map([...signature.recordKinds.values()].map((entry) => [entry.population, entry.identity]));
  const referencedExternal = new Map<string, string>();
  for (const domain of signature.referenceDomains.values()) {
    for (const [index, row] of populations[domain.population].entries()) {
      const raw = (row as unknown as Readonly<Record<string, unknown>>)[domain.field];
      let refs: readonly string[];
      if (domain.cardinality === "exactly_one") refs = [requireIdentity(raw, `accepted_program.model.${domain.population}[${index}].${domain.field}`)];
      else if (domain.cardinality === "zero_or_one") refs = raw === null ? [] : [requireIdentity(raw, `accepted_program.model.${domain.population}[${index}].${domain.field}`)];
      else {
        refs = requireStrings(raw, `accepted_program.model.${domain.population}[${index}].${domain.field}`, domain.cardinality !== "one_or_more").map((ref, refIndex) => requireIdentity(ref, `accepted_program.model.${domain.population}[${index}].${domain.field}[${refIndex}]`));
      }
      for (const ref of refs) {
        const target = local.get(ref);
        if (target !== undefined) {
          const targetKind = recordKindByPopulation.get(target.population)!;
          if (!domain.allowed_local_record_kinds.includes(targetKind)) fail(`accepted_program.model.${domain.population}[${index}].${domain.field}`, "resolves to a refused local record kind");
          if (target.population === "O") {
            const sort = requireString(target.row.sort, `accepted_program.model.${domain.population}[${index}].${domain.field}.sort`);
            if (!domain.allowed_semantic_object_sorts.includes("*") && !domain.allowed_semantic_object_sorts.includes(sort)) fail(`accepted_program.model.${domain.population}[${index}].${domain.field}`, "resolves to a refused semantic-object sort");
          }
          continue;
        }
        const resolution = resolutions.get(ref);
        if (resolution === undefined || !domain.allowed_external_target_kinds.includes(resolution.external_target_kind)) fail(`accepted_program.model.${domain.population}[${index}].${domain.field}`, "has no lawful external resolution under its field domain");
        if (domain.required_basis_relation !== resolution.basis_relation || referenceDomainIdentity(domain) !== resolution.reference_domain) fail(`accepted_program.model.${domain.population}[${index}].${domain.field}`, "uses the wrong external basis or reference-domain relation");
        const prior = referencedExternal.get(ref);
        if (prior !== undefined && prior !== resolution.reference_domain) fail(`accepted_program.model.${domain.population}[${index}].${domain.field}`, "resolves one external identity through multiple reference domains");
        referencedExternal.set(ref, resolution.reference_domain);
      }
    }
  }
  const unresolved = I.filter((identity) => !seen.has(identity));
  if (unresolved.length !== referencedExternal.size || unresolved.some((identity) => !referencedExternal.has(identity)) || resolutions.size !== referencedExternal.size || [...resolutions.keys()].some((identity) => !referencedExternal.has(identity))) fail("accepted_program.model.I", "must equal the disjoint union of local records and the least exact ResolutionSet_M closure");
  return { b, I, O, E, C, L, X, V, T, J, ResolutionSet_M };
}

function validateCandidateModel(value: unknown, signature: TargetSignature): AxiomModel {
  requireExact(value, [
    "constraints",
    "external_resolutions",
    "identities",
    "judgments",
    "latitudes",
    "model_basis_identity",
    "residuals",
    "semantic_objects",
    "transformations",
    "traversals",
    "typed_relations",
  ], "semantic_compilation_candidate.candidate_model");
  return validateModel({
    b: value.model_basis_identity,
    I: value.identities,
    O: value.semantic_objects,
    E: value.typed_relations,
    C: value.constraints,
    L: value.latitudes,
    X: value.residuals,
    V: value.traversals,
    T: value.transformations,
    J: value.judgments,
    ResolutionSet_M: value.external_resolutions,
  }, signature);
}

function validateSourceBindings(value: unknown, model: AxiomModel, subjectMembers: ReadonlyMap<string, string>, accepted: boolean): readonly AxiomSourceBinding[] {
  const rows = requireRecordRows(value, ["member_path", "member_sha256", "disposition", "model_refs", "residual_refs", "reason_code"], "accepted_program.source_bindings") as unknown as readonly AxiomSourceBinding[];
  const recordIdentities = new Set([...model.O, ...model.E, ...model.C, ...model.L, ...model.X, ...model.V, ...model.T, ...model.J].map((row) => row.id));
  const residualIdentities = new Set(model.X.map((row) => row.id));
  const paths: string[] = [];
  for (const [index, row] of rows.entries()) {
    paths.push(requireString(row.member_path, `accepted_program.source_bindings[${index}].member_path`));
    const digest = requireSha256(row.member_sha256, `accepted_program.source_bindings[${index}].member_sha256`);
    if (subjectMembers.get(row.member_path) !== digest) fail(`accepted_program.source_bindings[${index}]`, "does not bind one exact installed source member");
    const disposition = requireString(row.disposition, `accepted_program.source_bindings[${index}].disposition`);
    if (!SOURCE_DISPOSITIONS.has(disposition)) fail(`accepted_program.source_bindings[${index}].disposition`, "is not declared");
    if (accepted && disposition === "refused") fail(`accepted_program.source_bindings[${index}].disposition`, "cannot enter an accepted program");
    if (!SOURCE_REASON_CODES.has(requireString(row.reason_code, `accepted_program.source_bindings[${index}].reason_code`))) fail(`accepted_program.source_bindings[${index}].reason_code`, "is not declared");
    for (const [field, refs] of [["model_refs", row.model_refs], ["residual_refs", row.residual_refs]] as const) {
      const allowed = field === "residual_refs" ? residualIdentities : recordIdentities;
      for (const ref of requireStrings(refs, `accepted_program.source_bindings[${index}].${field}`)) if (!allowed.has(ref)) fail(`accepted_program.source_bindings[${index}].${field}`, `must resolve in ${field === "residual_refs" ? "model.X" : "the model record population"}`);
    }
    if (disposition === "retained" && row.model_refs.length === 0) fail(`accepted_program.source_bindings[${index}].model_refs`, "retained source requires represented model content");
    if (disposition === "represented_by_residual" && row.residual_refs.length === 0) fail(`accepted_program.source_bindings[${index}].residual_refs`, "residual disposition requires one retained residual");
    if (disposition === "inapplicable" && (row.model_refs.length !== 0 || row.residual_refs.length !== 0)) fail(`accepted_program.source_bindings[${index}]`, "inapplicable source cannot carry model or residual references");
  }
  if (paths.join("\0") !== [...paths].sort(compareUnicodeCodeUnits).join("\0") || new Set(paths).size !== paths.length) fail("accepted_program.source_bindings", "must be path-sorted and duplicate-free");
  if (paths.length !== subjectMembers.size || [...subjectMembers.keys()].some((path) => !paths.includes(path))) fail("accepted_program.source_bindings", "must disposition the complete exact installed subject inventory once");
  return rows;
}

function validateProgram(value: Readonly<Record<string, unknown>>, signature: TargetSignature, subjectMembers: ReadonlyMap<string, string>): AcceptedAxiomaticProgram {
  requireExact(value, ["basis", "kind", "model", "model_content_identity", "record_provenance", "schema_version", "source_bindings"], "accepted_program");
  if (value.kind !== "axiom-indexer.axiomatic-program" || value.schema_version !== 2) fail("accepted_program", "has the wrong kind or schema version");
  requireExact(value.basis, ["calculus", "candidate_structure_result", "corpus", "interpretation_contract", "semantic_compilation_candidate", "subject_basis", "target_profile"], "accepted_program.basis");
  const basis = {
    corpus: requireCoordinate(value.basis.corpus, "accepted_program.basis.corpus"),
    calculus: requireCoordinate(value.basis.calculus, "accepted_program.basis.calculus"),
    subject_basis: requireCoordinate(value.basis.subject_basis, "accepted_program.basis.subject_basis"),
    target_profile: requireCoordinate(value.basis.target_profile, "accepted_program.basis.target_profile"),
    interpretation_contract: requireCoordinate(value.basis.interpretation_contract, "accepted_program.basis.interpretation_contract"),
    semantic_compilation_candidate: requireCoordinate(value.basis.semantic_compilation_candidate, "accepted_program.basis.semantic_compilation_candidate"),
    candidate_structure_result: requireCoordinate(value.basis.candidate_structure_result, "accepted_program.basis.candidate_structure_result"),
  };
  if (basis.corpus.identity !== STDO_RELEASE_URI || basis.corpus.sha256 !== STDO_MANIFEST_SHA256) fail("accepted_program.basis.corpus", "does not bind the exact selected STDO 2.5 cut");
  if (basis.calculus.identity !== CALCULUS_BASIS_IDENTITY || basis.calculus.sha256 !== CALCULUS_BASIS_SHA256) fail("accepted_program.basis.calculus", "does not bind the exact selected 2.5 calculus basis");
  if (basis.subject_basis.identity !== STDO_SUBJECT_BASIS_IDENTITY || basis.subject_basis.sha256 !== `sha256:${STDO_SUBJECT_BASIS_IDENTITY.slice(STDO_SUBJECT_BASIS_IDENTITY.lastIndexOf(":") + 1)}`) fail("accepted_program.basis.subject_basis", "does not bind the exact STDO subject-basis record");
  if (basis.target_profile.identity !== signature.identity || basis.target_profile.sha256 !== signature.sha256) fail("accepted_program.basis.target_profile", "does not bind the verified signature bytes");
  const model = validateModel(value.model, signature);
  const model_content_identity = requireSha256(value.model_content_identity, "accepted_program.model_content_identity");
  if (model_content_identity !== sha256Canonical(externalModelValue(model) as unknown as JsonValue)) fail("accepted_program.model_content_identity", "does not bind the exact external a_c model record");
  const record_provenance = validateRecordProvenance(value.record_provenance, model, subjectMembers, "accepted_program.record_provenance");
  const source_bindings = validateSourceBindings(value.source_bindings, model, subjectMembers, true);
  return { kind: "axiom-indexer.axiomatic-program", schema_version: 2, model_content_identity, basis, model, record_provenance, source_bindings };
}

interface ValidatedCompilationCandidate {
  readonly identity: string;
  readonly digest: string;
  readonly corpus: BasisCoordinate;
  readonly calculus: BasisCoordinate;
  readonly subjectBasis: BasisCoordinate;
  readonly targetProfile: BasisCoordinate;
  readonly interpretationContract: BasisCoordinate;
  readonly whatMemberSetIdentity: string;
  readonly frameBasisIdentity: string;
  readonly frameBasisSha256: string;
  readonly modelContentIdentity: string;
  readonly model: AxiomModel;
  readonly sourceMembers: ReadonlyMap<string, string>;
  readonly recordProvenance: readonly AxiomRecordProvenance[];
  readonly evaluatedMembers: readonly JsonValue[];
  readonly selections: readonly JsonValue[];
  readonly generatedSourceKeys: readonly JsonValue[];
  readonly compilationResiduals: readonly JsonValue[];
}

function validateInterpretationContract(bytes: Uint8Array, coordinate: BasisCoordinate): void {
  if (sha256Bytes(bytes) !== coordinate.sha256) fail("interpretation_contract", "bytes do not match the candidate interpretation-contract coordinate");
  if (coordinate.identity !== COMPILE_TRAVERSAL || coordinate.sha256 !== INTERPRETATION_CONTRACT_SHA256) fail("interpretation_contract", "does not bind the frozen semantic-compilation contract identity and bytes");
  const value = parseUniqueJson(bytes, "interpretation_contract");
  requireExact(value, ["authority", "carrier", "codomain", "domain", "functor_ref", "identity", "kind", "model_coordinates", "postconditions", "record_kinds", "runtime", "schema_version", "semantic_acceptance", "source_disposition_unit", "source_packet_relation", "source_population", "stop_reason_codes", "stop_states"], "interpretation_contract");
  if (value.kind !== "stdo-representation.semantic-compilation-contract" || value.schema_version !== 2 || value.identity !== coordinate.identity || value.identity !== COMPILE_TRAVERSAL || value.functor_ref !== F_P || value.authority !== "proposal_only" || value.semantic_acceptance !== "external_f_h_v_select_over_unchanged_candidate" || value.carrier !== "excluded" || value.runtime !== "excluded") fail("interpretation_contract", "does not declare the exact proposal-only F_P semantic-compilation boundary");
  const populations = requireStringArray(value.model_coordinates, "interpretation_contract.model_coordinates", false);
  if (populations.join("\0") !== ["b", "I", "O", "E", "C", "L", "X", "V", "T", "J", "ResolutionSet_M"].join("\0")) fail("interpretation_contract.model_coordinates", "does not name the complete ordered a_c model coordinate");
  requireStringArray(value.domain, "interpretation_contract.domain", false);
  requireStringArray(value.codomain, "interpretation_contract.codomain", false);
  requireStringArray(value.postconditions, "interpretation_contract.postconditions", false);
  requireStringArray(value.stop_states, "interpretation_contract.stop_states", false);
  requireStringArray(value.stop_reason_codes, "interpretation_contract.stop_reason_codes", false);
  if (!isRecord(value.record_kinds) || Object.keys(value.record_kinds).sort(compareUnicodeCodeUnits).join("\0") !== ["C", "E", "J", "L", "O", "T", "V", "X"].sort(compareUnicodeCodeUnits).join("\0")) fail("interpretation_contract.record_kinds", "does not name all eight exact record families");
}

function validateSourceMemberRows(value: unknown, subjectMembers: ReadonlyMap<string, string>, path: string): ReadonlyMap<string, string> {
  const rows = requireRecordRows(value, ["member_path", "member_sha256"], path);
  if (rows.length !== subjectMembers.size) fail(path, "must contain the complete exact installed subject inventory");
  const result = new Map<string, string>();
  for (const [index, row] of rows.entries()) {
    const memberPath = requireRelativePath(row.member_path, `${path}[${index}].member_path`);
    const digest = requireSha256(row.member_sha256, `${path}[${index}].member_sha256`);
    if (result.has(memberPath) || subjectMembers.get(memberPath) !== digest) fail(`${path}[${index}]`, "does not equal one exact installed subject member");
    result.set(memberPath, digest);
  }
  if ([...result.keys()].join("\0") !== [...subjectMembers.keys()].join("\0")) fail(path, "does not preserve the exact installed subject order");
  return result;
}

function validateSourceLocator(value: unknown, subjectMembers: ReadonlyMap<string, string>, path: string): AxiomSourceLocator {
  requireExact(value, ["basis_uri", "fragment", "member_path", "member_sha256"], path);
  const memberPath = requireRelativePath(value.member_path, `${path}.member_path`);
  if (value.basis_uri !== STDO_RELEASE_URI || value.member_sha256 !== subjectMembers.get(memberPath)) fail(path, "does not bind one exact selected STDO source member");
  const memberSha256 = requireSha256(value.member_sha256, `${path}.member_sha256`);
  if (value.fragment !== null) fail(`${path}.fragment`, "must be exact null for the selected STDO cut");
  const fragment = null;
  return { basis_uri: STDO_RELEASE_URI, member_path: memberPath, member_sha256: memberSha256, fragment };
}

function validateSourceLocators(value: unknown, subjectMembers: ReadonlyMap<string, string>, path: string): readonly AxiomSourceLocator[] {
  if (!Array.isArray(value)) fail(path, "must be an array");
  const rows = value.map((row, index) => validateSourceLocator(row, subjectMembers, `${path}[${index}]`));
  const canonical = rows.map((row) => canonicalJson(row as unknown as JsonValue));
  if (new Set(canonical).size !== canonical.length || canonical.join("\0") !== [...canonical].sort(compareUnicodeCodeUnits).join("\0")) fail(path, "must be JCS-sorted and duplicate-free");
  return rows;
}

function sourceLocatorIdentity(locator: AxiomSourceLocator): string {
  return `${locator.basis_uri}standards/${locator.member_path}${locator.fragment === null ? "" : `#${locator.fragment}`}`;
}

function validateRecordProvenance(
  value: unknown,
  model: AxiomModel,
  subjectMembers: ReadonlyMap<string, string>,
  path: string,
): readonly AxiomRecordProvenance[] {
  const records = new Map(localModelRecords(model).map((row) => [row.id, row]));
  const exactDerivationBasis = new Set([CALCULUS_BASIS_IDENTITY, STDO_SUBJECT_BASIS_IDENTITY, TARGET_SIGNATURE_IDENTITY, COMPILE_TRAVERSAL, WHAT_MEMBER_SET_IDENTITY]);
  const rows = requireRecordRows(value, ["derivation_evidence_refs", "model_record_ref", "provenance_kind", "semantic_address", "source_locators"], path);
  if (rows.length !== records.size) fail(path, "must be total over the exact local model record population");
  const result: AxiomRecordProvenance[] = [];
  let previous = "";
  for (const [index, row] of rows.entries()) {
    const rowPath = `${path}[${index}]`;
    const modelRecordRef = requireIdentity(row.model_record_ref, `${rowPath}.model_record_ref`);
    if (index > 0 && compareUnicodeCodeUnits(previous, modelRecordRef) >= 0) fail(path, "must be model-record-ref sorted and duplicate-free");
    previous = modelRecordRef;
    const record = records.get(modelRecordRef);
    if (record === undefined) fail(`${rowPath}.model_record_ref`, "does not resolve one exact local model record");
    const provenanceKind = requireString(row.provenance_kind, `${rowPath}.provenance_kind`);
    if (provenanceKind !== "subject_derived") fail(`${rowPath}.provenance_kind`, "must be subject_derived for the selected STDO cut");
    requireExact(row.semantic_address, ["bounded_context", "governed_scope", "owning_authority", "selected_basis", "source_key", "term"], `${rowPath}.semantic_address`);
    const semanticAddress: AxiomSemanticAddress = {
      source_key: requireIdentity(row.semantic_address.source_key, `${rowPath}.semantic_address.source_key`),
      term: requireString(row.semantic_address.term, `${rowPath}.semantic_address.term`),
      bounded_context: requireIdentity(row.semantic_address.bounded_context, `${rowPath}.semantic_address.bounded_context`),
      owning_authority: requireIdentity(row.semantic_address.owning_authority, `${rowPath}.semantic_address.owning_authority`),
      selected_basis: requireIdentity(row.semantic_address.selected_basis, `${rowPath}.semantic_address.selected_basis`),
      governed_scope: requireIdentity(row.semantic_address.governed_scope, `${rowPath}.semantic_address.governed_scope`),
    };
    if (semanticAddress.bounded_context !== record.context || semanticAddress.owning_authority !== record.owner || semanticAddress.governed_scope !== record.scope || semanticAddress.selected_basis !== STDO_SUBJECT_BASIS_IDENTITY) fail(`${rowPath}.semantic_address`, "is not congruent with the record context, owner, governed scope, and exact subject basis");
    const sourceLocators = validateSourceLocators(row.source_locators, subjectMembers, `${rowPath}.source_locators`);
    const derivationEvidenceRefs = requireStrings(row.derivation_evidence_refs, `${rowPath}.derivation_evidence_refs`).map((identity, evidenceIndex) => requireIdentity(identity, `${rowPath}.derivation_evidence_refs[${evidenceIndex}]`));
    for (const [evidenceIndex, identity] of derivationEvidenceRefs.entries()) {
      const sourceIdentity = [...subjectMembers.keys()].some((memberPath) => identity === `${STDO_RELEASE_URI}standards/${memberPath}`);
      if (!exactDerivationBasis.has(identity) && !sourceIdentity) fail(`${rowPath}.derivation_evidence_refs[${evidenceIndex}]`, "does not resolve in the exact derivation-evidence domain");
    }
    if (sourceLocators.length === 0) fail(`${rowPath}.source_locators`, "subject-derived provenance requires an exact Source STDO locator");
    if (!semanticAddress.source_key.startsWith(SOURCE_KEY_PREFIX)) {
      const exactSourceIdentity = sourceLocators.some((locator) => semanticAddress.source_key === sourceLocatorIdentity(locator));
      if (!exactSourceIdentity) fail(`${rowPath}.semantic_address.source_key`, "is neither an exact row-local Source STDO identity nor a governed generated key");
    }
    result.push({ model_record_ref: modelRecordRef, provenance_kind: provenanceKind, semantic_address: semanticAddress, source_locators: sourceLocators, derivation_evidence_refs: derivationEvidenceRefs });
  }
  if ([...records.keys()].some((identity) => !result.some((row) => row.model_record_ref === identity))) fail(path, "does not bind every local model record exactly once");
  return result;
}

interface ValidatedRows {
  readonly rows: readonly JsonValue[];
  readonly identities: ReadonlySet<string>;
}

function validateSelections(
  value: unknown,
  model: AxiomModel,
  recordProvenance: readonly AxiomRecordProvenance[],
  subjectMembers: ReadonlyMap<string, string>,
  path: string,
): ValidatedRows {
  const localIds = new Set(localModelRecords(model).map((row) => row.id));
  const provenance = new Map(recordProvenance.map((row) => [row.model_record_ref, row]));
  const rows = requireRecordRows(value, ["disposition", "model_record_refs", "rationale", "selection_ref", "source_locators", "source_owner"], path);
  const identities = new Set<string>();
  const recordOwners = new Map<string, number>();
  let previous = "";
  for (const [index, row] of rows.entries()) {
    const rowPath = `${path}[${index}]`;
    const identity = requireIdentity(row.selection_ref, `${rowPath}.selection_ref`);
    if (identities.has(identity) || (index > 0 && compareUnicodeCodeUnits(previous, identity) >= 0)) fail(path, "must be selection-ref sorted and duplicate-free");
    previous = identity;
    identities.add(identity);
    const disposition = requireString(row.disposition, `${rowPath}.disposition`);
    if (!["retained", "omitted", "uncertain", "inapplicable", "refused"].includes(disposition)) fail(`${rowPath}.disposition`, "is not declared");
    const refs = requireStrings(row.model_record_refs, `${rowPath}.model_record_refs`);
    if (disposition === "retained" && refs.length === 0) fail(rowPath, "retained selection must own at least one model record");
    if (disposition !== "retained" && refs.length !== 0) fail(`${rowPath}.model_record_refs`, "must be empty unless the selection disposition is retained");
    for (const ref of refs) {
      if (!localIds.has(ref)) fail(`${rowPath}.model_record_refs`, "contains a reference outside the exact candidate model");
      recordOwners.set(ref, (recordOwners.get(ref) ?? 0) + 1);
    }
    const sourceLocators = validateSourceLocators(row.source_locators, subjectMembers, `${rowPath}.source_locators`);
    if (sourceLocators.length === 0) fail(`${rowPath}.source_locators`, "must be non-empty");
    const locatorKeys = new Set(sourceLocators.map((locator) => canonicalJson(locator as unknown as JsonValue)));
    for (const ref of refs) {
      const binding = provenance.get(ref);
      if (binding === undefined) fail(`${rowPath}.model_record_refs`, `has no exact record-provenance binding for ${ref}`);
      if (binding.provenance_kind === "subject_derived" && binding.source_locators.some((locator) => !locatorKeys.has(canonicalJson(locator as unknown as JsonValue)))) fail(`${rowPath}.source_locators`, `does not include every direct provenance locator for ${ref}`);
    }
    requireString(row.rationale, `${rowPath}.rationale`);
    requireIdentity(row.source_owner, `${rowPath}.source_owner`);
  }
  for (const identity of localIds) if (recordOwners.get(identity) !== 1) fail(path, `must assign local model record ${identity} exactly once through a retained selection`);
  return { rows: rows as unknown as readonly JsonValue[], identities };
}

function validateEvaluatedMembers(
  value: unknown,
  selectionRows: readonly JsonValue[],
  subjectMembers: ReadonlyMap<string, string>,
  path: string,
): readonly JsonValue[] {
  const selections = new Map<string, Readonly<Record<string, unknown>>>();
  for (const [index, raw] of selectionRows.entries()) {
    if (!isRecord(raw)) fail(`${path}.selections[${index}]`, "must be an object");
    selections.set(requireIdentity(raw.selection_ref, `${path}.selections[${index}].selection_ref`), raw);
  }
  const rows = requireRecordRows(value, ["disposition", "member_path", "member_sha256", "rationale", "selection_refs"], path);
  if (rows.length !== subjectMembers.size) fail(path, "must disposition all 51 exact source members");
  const referencedSelections = new Set<string>();
  const memberIncidence = new Set<string>();
  const memberPaths = [...subjectMembers.keys()];
  for (const [index, row] of rows.entries()) {
    const rowPath = `${path}[${index}]`;
    const memberPath = requireRelativePath(row.member_path, `${rowPath}.member_path`);
    if (memberPath !== memberPaths[index] || row.member_sha256 !== subjectMembers.get(memberPath)) fail(rowPath, "does not preserve the exact source inventory order and digest");
    requireSha256(row.member_sha256, `${rowPath}.member_sha256`);
    if (!["contains_retained_material", "contains_no_retained_material", "uncertain", "inapplicable", "refused"].includes(requireString(row.disposition, `${rowPath}.disposition`))) fail(`${rowPath}.disposition`, "is not declared");
    for (const ref of requireStrings(row.selection_refs, `${rowPath}.selection_refs`)) {
      const selection = selections.get(ref);
      if (selection === undefined) fail(`${rowPath}.selection_refs`, "does not resolve one selection in the same surface");
      const locators = Array.isArray(selection.source_locators) ? selection.source_locators : [];
      if (!locators.some((locator) => isRecord(locator) && locator.member_path === memberPath && locator.member_sha256 === row.member_sha256)) fail(`${rowPath}.selection_refs`, `selection ${ref} has no source locator for the evaluated member`);
      referencedSelections.add(ref);
      memberIncidence.add(`${ref}\0${memberPath}\0${String(row.member_sha256)}`);
    }
    requireString(row.rationale, `${rowPath}.rationale`);
  }
  for (const [identity, selection] of selections) {
    if (!referencedSelections.has(identity)) fail(path, `does not connect selection ${identity} to a source member`);
    for (const locator of selection.source_locators as readonly Readonly<Record<string, unknown>>[]) {
      if (!memberIncidence.has(`${identity}\0${String(locator.member_path)}\0${String(locator.member_sha256)}`)) fail(path, `does not include the reverse evaluated-member incidence for selection ${identity}`);
    }
  }
  return rows as unknown as readonly JsonValue[];
}

function evaluatedMemberIdentity(row: JsonValue, path: string): string {
  if (!isRecord(row)) fail(path, "must be an object");
  return `${STDO_RELEASE_URI}standards/${requireRelativePath(row.member_path, `${path}.member_path`)}`;
}

function validateGeneratedSourceKeys(
  value: unknown,
  recordProvenance: readonly AxiomRecordProvenance[],
  subjectMembers: ReadonlyMap<string, string>,
  path: string,
): ValidatedRows {
  const provenanceByKey = new Map<string, AxiomRecordProvenance[]>();
  for (const binding of recordProvenance) {
    const key = binding.semantic_address.source_key;
    provenanceByKey.set(key, [...(provenanceByKey.get(key) ?? []), binding]);
  }
  const rows = requireRecordRows(value, ["local_declaration_key", "primary_source_locator", "source_key"], path);
  const identities = new Set<string>();
  let previous = "";
  for (const [index, row] of rows.entries()) {
    const rowPath = `${path}[${index}]`;
    const identity = requireIdentity(row.source_key, `${rowPath}.source_key`);
    if (identities.has(identity) || (index > 0 && compareUnicodeCodeUnits(previous, identity) >= 0)) fail(path, "must be source-key sorted and duplicate-free");
    previous = identity;
    identities.add(identity);
    const primarySourceLocator = validateSourceLocator(row.primary_source_locator, subjectMembers, `${rowPath}.primary_source_locator`);
    const localDeclarationKey = requireString(row.local_declaration_key, `${rowPath}.local_declaration_key`);
    const expected = `${SOURCE_KEY_PREFIX}${sha256Canonical({
      primary_source_locator: primarySourceLocator as unknown as JsonValue,
      local_declaration_key: localDeclarationKey,
    } as unknown as JsonValue).slice("sha256:".length)}`;
    if (identity !== expected) fail(`${rowPath}.source_key`, "does not reproduce from the exact source-key preimage");
    const represented = provenanceByKey.get(identity) ?? [];
    if (represented.length === 0) fail(`${rowPath}.source_key`, "does not resolve one represented semantic address");
    const addresses = new Set(represented.map((binding) => canonicalJson(binding.semantic_address as unknown as JsonValue)));
    if (addresses.size !== 1) fail(`${rowPath}.source_key`, "resolves more than one represented semantic address");
    const locatorKey = canonicalJson(primarySourceLocator as unknown as JsonValue);
    if (represented.some((binding) => !binding.source_locators.some((locator) => canonicalJson(locator as unknown as JsonValue) === locatorKey))) fail(`${rowPath}.primary_source_locator`, "does not occur in every corresponding record-provenance row");
  }
  for (const key of provenanceByKey.keys()) if (key.startsWith(SOURCE_KEY_PREFIX) && !identities.has(key)) fail(path, `does not bind generated-prefix record-provenance source key ${key}`);
  return { rows: rows as unknown as readonly JsonValue[], identities };
}

function validateCompilationResiduals(
  value: unknown,
  model: AxiomModel,
  subjectMembers: ReadonlyMap<string, string>,
  path: string,
  requireModelResidual: boolean,
): ValidatedRows {
  const modelResidualIds = new Set(model.X.map((row) => row.id));
  const rows = requireRecordRows(value, ["consequence", "model_residual_refs", "re_entry_route", "residual_ref", "source_locators", "statement"], path);
  const identities = new Set<string>();
  let previous = "";
  for (const [index, row] of rows.entries()) {
    const rowPath = `${path}[${index}]`;
    const identity = requireIdentity(row.residual_ref, `${rowPath}.residual_ref`);
    if (identities.has(identity) || (index > 0 && compareUnicodeCodeUnits(previous, identity) >= 0)) fail(path, "must be residual-ref sorted and duplicate-free");
    previous = identity;
    identities.add(identity);
    const sourceLocators = validateSourceLocators(row.source_locators, subjectMembers, `${rowPath}.source_locators`);
    if (sourceLocators.length === 0) fail(`${rowPath}.source_locators`, "must be non-empty");
    const refs = requireStrings(row.model_residual_refs, `${rowPath}.model_residual_refs`, !requireModelResidual);
    for (const ref of refs) if (!modelResidualIds.has(ref)) fail(`${rowPath}.model_residual_refs`, "does not resolve one exact model X residual");
    requireString(row.statement, `${rowPath}.statement`);
    requireString(row.consequence, `${rowPath}.consequence`);
    requireString(row.re_entry_route, `${rowPath}.re_entry_route`);
  }
  return { rows: rows as unknown as readonly JsonValue[], identities };
}

function validateCandidateProposalSurfaces(
  provenanceValue: unknown,
  evaluatedValue: unknown,
  selectionsValue: unknown,
  generatedValue: unknown,
  residualsValue: unknown,
  model: AxiomModel,
  subjectMembers: ReadonlyMap<string, string>,
): { recordProvenance: readonly AxiomRecordProvenance[]; evaluatedMembers: readonly JsonValue[]; selections: readonly JsonValue[]; generatedSourceKeys: readonly JsonValue[]; compilationResiduals: readonly JsonValue[] } {
  const recordProvenance = validateRecordProvenance(provenanceValue, model, subjectMembers, "semantic_compilation_candidate.proposed_record_provenance");
  const selections = validateSelections(selectionsValue, model, recordProvenance, subjectMembers, "semantic_compilation_candidate.proposed_selections");
  const evaluated = validateEvaluatedMembers(evaluatedValue, selections.rows, subjectMembers, "semantic_compilation_candidate.proposed_evaluated_members");
  deriveSourceBindings(model, recordProvenance, evaluated, selections.rows, "semantic_compilation_candidate");
  const generated = validateGeneratedSourceKeys(generatedValue, recordProvenance, subjectMembers, "semantic_compilation_candidate.proposed_generated_source_keys");
  const residuals = validateCompilationResiduals(residualsValue, model, subjectMembers, "semantic_compilation_candidate.compilation_residuals", false);
  const proposalFamilies = new Map<string, string>();
  const addProposalIdentity = (identity: string, family: string): void => {
    const prior = proposalFamilies.get(identity);
    if (prior !== undefined) fail("semantic_compilation_candidate", `proposal identity ${identity} collides across ${prior} and ${family}`);
    proposalFamilies.set(identity, family);
  };
  evaluated.forEach((row, index) => addProposalIdentity(evaluatedMemberIdentity(row, `semantic_compilation_candidate.proposed_evaluated_members[${index}]`), "evaluated members"));
  for (const row of [...model.O, ...model.E, ...model.C, ...model.L, ...model.X, ...model.V, ...model.T, ...model.J]) addProposalIdentity(row.id, "model records");
  for (const identity of selections.identities) addProposalIdentity(identity, "selections");
  for (const identity of generated.identities) addProposalIdentity(identity, "generated source keys");
  for (const identity of residuals.identities) addProposalIdentity(identity, "compilation residuals");
  return {
    recordProvenance,
    evaluatedMembers: evaluated,
    selections: selections.rows,
    generatedSourceKeys: generated.rows,
    compilationResiduals: residuals.rows,
  };
}

function candidatePayload(value: Readonly<Record<string, unknown>>): Readonly<Record<string, unknown>> {
  const { kind: _kind, schema_version: _schema, proposal_content_sha256: _proposal, compiler_invocation: _invocation, ...payload } = value;
  return payload;
}

function validateCompilationCandidate(
  value: Readonly<Record<string, unknown>>,
  proposalBytes: Uint8Array,
  compilerProvenance: ValidatedCompilerProvenanceBundle,
  signature: TargetSignature,
  subjectMembers: ReadonlyMap<string, string>,
  interpretationContractBytes: Uint8Array,
  frameBasisBytes: Uint8Array,
): ValidatedCompilationCandidate {
  requireExact(value, [
    "calculus_basis_identity", "candidate_model", "candidate_model_content_identity",
    "compilation_residuals", "compiler_invocation", "frame_basis_identity",
    "frame_basis_sha256", "interpretation_contract_identity",
    "interpretation_contract_sha256", "kind", "proposal_content_sha256",
    "proposed_evaluated_members", "proposed_generated_source_keys", "proposed_record_provenance",
    "proposed_selections", "schema_version", "selected_frame_refs",
    "signature_identity", "signature_sha256", "source_member_set_sha256",
    "source_members", "source_stdo_manifest_sha256", "source_stdo_uri",
    "stop_state", "subject_basis_identity", "what_member_set_identity",
  ], "semantic_compilation_candidate");
  if (value.kind !== "stdo-representation.semantic-compilation-candidate" || value.schema_version !== 3 || value.stop_state !== "urn:stdo-index:stdo:stop-kind:candidate:1") fail("semantic_compilation_candidate", "is not one exact candidate result");
  const calculusIdentity = requireIdentity(value.calculus_basis_identity, "semantic_compilation_candidate.calculus_basis_identity");
  if (calculusIdentity !== CALCULUS_BASIS_IDENTITY) fail("semantic_compilation_candidate.calculus_basis_identity", "does not bind the exact selected 2.5 calculus basis");
  if (value.source_stdo_uri !== STDO_RELEASE_URI || value.source_stdo_manifest_sha256 !== STDO_MANIFEST_SHA256 || value.source_member_set_sha256 !== STDO_MEMBER_SET_SHA256) fail("semantic_compilation_candidate", "does not bind the exact selected STDO 2.5 source population");
  const sourceMembers = validateSourceMemberRows(value.source_members, subjectMembers, "semantic_compilation_candidate.source_members");
  if (value.subject_basis_identity !== STDO_SUBJECT_BASIS_IDENTITY || value.what_member_set_identity !== WHAT_MEMBER_SET_IDENTITY) fail("semantic_compilation_candidate", "does not bind the frozen subject and WHAT member-set identities");
  const targetProfile = {
    identity: requireIdentity(value.signature_identity, "semantic_compilation_candidate.signature_identity"),
    sha256: requireSha256(value.signature_sha256, "semantic_compilation_candidate.signature_sha256"),
  };
  if (targetProfile.identity !== signature.identity || targetProfile.sha256 !== signature.sha256) fail("semantic_compilation_candidate.signature_identity", "does not bind the verified exact target signature bytes");
  const interpretationContract = {
    identity: requireIdentity(value.interpretation_contract_identity, "semantic_compilation_candidate.interpretation_contract_identity"),
    sha256: requireSha256(value.interpretation_contract_sha256, "semantic_compilation_candidate.interpretation_contract_sha256"),
  };
  validateInterpretationContract(interpretationContractBytes, interpretationContract);
  if (value.frame_basis_identity !== FRAME_BASIS_IDENTITY || value.frame_basis_sha256 !== FRAME_BASIS_SHA256 || sha256Bytes(frameBasisBytes) !== FRAME_BASIS_SHA256) fail("semantic_compilation_candidate.frame_basis_identity", "does not bind the frozen project frame basis bytes");
  const selectedFrames = requireStrings(value.selected_frame_refs, "semantic_compilation_candidate.selected_frame_refs", false).map((entry, index) => requireIdentity(entry, `semantic_compilation_candidate.selected_frame_refs[${index}]`));
  if (selectedFrames.length !== 1 || selectedFrames[0] !== COMPILATION_FRAME_IDENTITY) fail("semantic_compilation_candidate.selected_frame_refs", "does not select exactly the semantic-compilation frame");
  const proposal = parseUniqueJson(proposalBytes, "semantic_compilation_proposal");
  requireExact(proposal, ["kind", "payload", "schema_version"], "semantic_compilation_proposal");
  if (proposal.kind !== "stdo-representation.semantic-compilation-proposal" || proposal.schema_version !== 2 || !isRecord(proposal.payload)) fail("semantic_compilation_proposal", "has the wrong proposal contract");
  if (value.proposal_content_sha256 !== sha256Bytes(canonicalRecordBytes(proposal as unknown as JsonValue)) || canonicalJson(proposal.payload as unknown as JsonValue) !== canonicalJson(candidatePayload(value) as unknown as JsonValue)) fail("semantic_compilation_candidate.proposal_content_sha256", "does not bind an unchanged exact proposal payload");
  requireExact(value.compiler_invocation, ["capability_envelope_ref", "context_budget_tokens", "functor_ref", "host_identity", "instruction_sha256", "invoked_at", "model_configuration_sha256", "model_identity", "provenance_ref", "provenance_sha256", "raw_output_ref", "raw_output_sha256", "topology", "traversal_ref"], "semantic_compilation_candidate.compiler_invocation");
  if (value.compiler_invocation.topology !== "single_invocation" || value.compiler_invocation.traversal_ref !== COMPILE_TRAVERSAL || value.compiler_invocation.functor_ref !== F_P || value.compiler_invocation.capability_envelope_ref !== COMPILE_CAPABILITY || value.compiler_invocation.raw_output_sha256 !== sha256Bytes(proposalBytes)) fail("semantic_compilation_candidate.compiler_invocation", "does not bind the exact single F_P invocation and raw proposal bytes");
  requireIdentity(value.compiler_invocation.host_identity, "semantic_compilation_candidate.compiler_invocation.host_identity");
  requireString(value.compiler_invocation.model_identity, "semantic_compilation_candidate.compiler_invocation.model_identity");
  requireSha256(value.compiler_invocation.model_configuration_sha256, "semantic_compilation_candidate.compiler_invocation.model_configuration_sha256");
  requireSha256(value.compiler_invocation.instruction_sha256, "semantic_compilation_candidate.compiler_invocation.instruction_sha256");
  if (!Number.isSafeInteger(value.compiler_invocation.context_budget_tokens) || (value.compiler_invocation.context_budget_tokens as number) < 0) fail("semantic_compilation_candidate.compiler_invocation.context_budget_tokens", "must be a non-negative safe integer");
  requireTimestamp(value.compiler_invocation.invoked_at, "semantic_compilation_candidate.compiler_invocation.invoked_at");
  requireUriReference(value.compiler_invocation.raw_output_ref, "semantic_compilation_candidate.compiler_invocation.raw_output_ref");
  requireUriReference(value.compiler_invocation.provenance_ref, "semantic_compilation_candidate.compiler_invocation.provenance_ref");
  const provenanceSha256 = requireSha256(value.compiler_invocation.provenance_sha256, "semantic_compilation_candidate.compiler_invocation.provenance_sha256");
  if (provenanceSha256 !== compilerProvenance.digest) fail("semantic_compilation_candidate.compiler_invocation.provenance_sha256", "does not bind the exact supplied compiler-provenance bundle bytes");
  const sealedInvocation = compilerProvenance.members.get("sealed_invocation")!;
  if (value.compiler_invocation.instruction_sha256 !== sealedInvocation.member_sha256) fail("semantic_compilation_candidate.compiler_invocation.instruction_sha256", "does not bind the exact sealed-invocation provenance member");
  const capabilityEnvelope = compilerProvenance.members.get("capability_envelope")!;
  if (value.compiler_invocation.capability_envelope_ref !== capabilityEnvelope.member_ref) fail("semantic_compilation_candidate.compiler_invocation.capability_envelope_ref", "does not resolve the exact capability-envelope provenance member");
  const model = validateCandidateModel(value.candidate_model, signature);
  const modelContentIdentity = requireSha256(value.candidate_model_content_identity, "semantic_compilation_candidate.candidate_model_content_identity");
  if (modelContentIdentity !== sha256Canonical(externalModelValue(model) as unknown as JsonValue)) fail("semantic_compilation_candidate.candidate_model_content_identity", "does not bind the exact complete a_c model");
  const { recordProvenance, evaluatedMembers, selections, generatedSourceKeys, compilationResiduals } = validateCandidateProposalSurfaces(
    value.proposed_record_provenance,
    value.proposed_evaluated_members,
    value.proposed_selections,
    value.proposed_generated_source_keys,
    value.compilation_residuals,
    model,
    subjectMembers,
  );
  const digest = sha256Bytes(canonicalRecordBytes(value as unknown as JsonValue));
  return {
    identity: `${CANDIDATE_PREFIX}${digest.slice("sha256:".length)}`,
    digest,
    corpus: { identity: STDO_RELEASE_URI, sha256: STDO_MANIFEST_SHA256 },
    calculus: { identity: CALCULUS_BASIS_IDENTITY, sha256: CALCULUS_BASIS_SHA256 },
    subjectBasis: { identity: STDO_SUBJECT_BASIS_IDENTITY, sha256: `sha256:${STDO_SUBJECT_BASIS_IDENTITY.slice(STDO_SUBJECT_BASIS_IDENTITY.lastIndexOf(":") + 1)}` },
    targetProfile,
    interpretationContract,
    whatMemberSetIdentity: WHAT_MEMBER_SET_IDENTITY,
    frameBasisIdentity: FRAME_BASIS_IDENTITY,
    frameBasisSha256: FRAME_BASIS_SHA256,
    modelContentIdentity,
    model,
    sourceMembers,
    recordProvenance,
    evaluatedMembers,
    selections,
    generatedSourceKeys,
    compilationResiduals,
  };
}

interface ValidatedGrant {
  readonly artifact: AuthorityGrantArtifact;
  readonly artifactIdentity: string;
  readonly digest: string;
}

interface ValidatedStructureGrant {
  readonly artifact: CandidateStructureEvaluationGrant;
  readonly artifactIdentity: string;
  readonly digest: string;
}

function validateGrant(bytes: Uint8Array, sourceBytes: Uint8Array, path: string): ValidatedGrant {
  const value = parseCanonicalRecord(bytes, path);
  requireExact(value, ["actor_identity", "authority_identity", "basis_refs", "grant_identity", "grant_scope", "kind", "schema_version", "source_ref", "source_sha256"], path);
  if (value.kind !== "stdo-index.authority-grant" || value.schema_version !== 1) fail(path, "has the wrong grant contract");
  const artifact: AuthorityGrantArtifact = {
    kind: "stdo-index.authority-grant",
    schema_version: 1,
    grant_identity: requireIdentity(value.grant_identity, `${path}.grant_identity`),
    actor_identity: requireIdentity(value.actor_identity, `${path}.actor_identity`),
    authority_identity: requireIdentity(value.authority_identity, `${path}.authority_identity`),
    grant_scope: requireString(value.grant_scope, `${path}.grant_scope`),
    basis_refs: requireStrings(value.basis_refs, `${path}.basis_refs`, false).map((entry, index) => requireIdentity(entry, `${path}.basis_refs[${index}]`)),
    source_ref: requireUriReference(value.source_ref, `${path}.source_ref`),
    source_sha256: requireSha256(value.source_sha256, `${path}.source_sha256`),
  };
  if (artifact.source_sha256 !== sha256Bytes(sourceBytes)) fail(`${path}.source_sha256`, "does not bind the supplied exact authority source bytes");
  const digest = sha256Bytes(bytes);
  return { artifact, digest, artifactIdentity: `${GRANT_PREFIX}${digest.slice("sha256:".length)}` };
}

function validateStructureGrant(
  bytes: Uint8Array,
  authoritySourceBytes: Uint8Array,
  candidate: ValidatedCompilationCandidate,
): ValidatedStructureGrant {
  const path = "structure_grant";
  const value = parseCanonicalRecord(bytes, path);
  requireExact(value, [
    "authority_identity",
    "calculus_basis_identity", "evidence_refs",
    "frame_basis_identity", "frame_basis_sha256", "functor_ref",
    "grant_scope", "grantee_identity",
    "interpretation_contract_identity", "interpretation_contract_sha256",
    "issued_at", "issuer_actor_identity", "kind", "parent_grant_identity",
    "schema_version", "signature_identity", "source_ref", "source_sha256",
    "signature_sha256", "subject_identity", "subject_sha256", "traversal_ref",
    "what_member_set_identity",
  ], path);
  if (value.kind !== "stdo-representation.candidate-structure-evaluation-grant" || value.schema_version !== 1) fail(path, "has the wrong candidate-structure grant contract");
  const artifact: CandidateStructureEvaluationGrant = {
    kind: "stdo-representation.candidate-structure-evaluation-grant",
    schema_version: 1,
    issuer_actor_identity: requireIdentity(value.issuer_actor_identity, `${path}.issuer_actor_identity`),
    authority_identity: requireIdentity(value.authority_identity, `${path}.authority_identity`),
    parent_grant_identity: requireIdentity(value.parent_grant_identity, `${path}.parent_grant_identity`),
    grantee_identity: requireIdentity(value.grantee_identity, `${path}.grantee_identity`),
    grant_scope: requireString(value.grant_scope, `${path}.grant_scope`),
    traversal_ref: requireIdentity(value.traversal_ref, `${path}.traversal_ref`),
    functor_ref: requireIdentity(value.functor_ref, `${path}.functor_ref`),
    subject_identity: requireIdentity(value.subject_identity, `${path}.subject_identity`),
    subject_sha256: requireSha256(value.subject_sha256, `${path}.subject_sha256`),
    calculus_basis_identity: requireIdentity(value.calculus_basis_identity, `${path}.calculus_basis_identity`),
    signature_identity: requireIdentity(value.signature_identity, `${path}.signature_identity`),
    signature_sha256: requireSha256(value.signature_sha256, `${path}.signature_sha256`),
    interpretation_contract_identity: requireIdentity(value.interpretation_contract_identity, `${path}.interpretation_contract_identity`),
    interpretation_contract_sha256: requireSha256(value.interpretation_contract_sha256, `${path}.interpretation_contract_sha256`),
    what_member_set_identity: requireSha256(value.what_member_set_identity, `${path}.what_member_set_identity`),
    frame_basis_identity: requireIdentity(value.frame_basis_identity, `${path}.frame_basis_identity`),
    frame_basis_sha256: requireSha256(value.frame_basis_sha256, `${path}.frame_basis_sha256`),
    evidence_refs: requireStrings(value.evidence_refs, `${path}.evidence_refs`, false).map((entry, index) => requireUriReference(entry, `${path}.evidence_refs[${index}]`)),
    issued_at: requireTimestamp(value.issued_at, `${path}.issued_at`),
    source_ref: requireUriReference(value.source_ref, `${path}.source_ref`),
    source_sha256: requireSha256(value.source_sha256, `${path}.source_sha256`),
  };
  const exactCoordinates: readonly [unknown, unknown, string][] = [
    [artifact.issuer_actor_identity, PRODUCT_OWNER_ACTOR, "issuer_actor_identity"],
    [artifact.authority_identity, PRODUCT_OWNER_AUTHORITY, "authority_identity"],
    [artifact.parent_grant_identity, PRODUCT_OWNER_GRANT, "parent_grant_identity"],
    [artifact.grantee_identity, STRUCTURE_EVALUATOR, "grantee_identity"],
    [artifact.grant_scope, STRUCTURE_GRANT_SCOPE, "grant_scope"],
    [artifact.traversal_ref, STRUCTURE_TRAVERSAL, "traversal_ref"],
    [artifact.functor_ref, F_D, "functor_ref"],
    [artifact.subject_identity, candidate.identity, "subject_identity"],
    [artifact.subject_sha256, candidate.digest, "subject_sha256"],
    [artifact.calculus_basis_identity, candidate.calculus.identity, "calculus_basis_identity"],
    [artifact.signature_identity, candidate.targetProfile.identity, "signature_identity"],
    [artifact.signature_sha256, candidate.targetProfile.sha256, "signature_sha256"],
    [artifact.interpretation_contract_identity, candidate.interpretationContract.identity, "interpretation_contract_identity"],
    [artifact.interpretation_contract_sha256, candidate.interpretationContract.sha256, "interpretation_contract_sha256"],
    [artifact.what_member_set_identity, candidate.whatMemberSetIdentity, "what_member_set_identity"],
    [artifact.frame_basis_identity, candidate.frameBasisIdentity, "frame_basis_identity"],
    [artifact.frame_basis_sha256, candidate.frameBasisSha256, "frame_basis_sha256"],
    [artifact.source_ref, PRODUCT_OWNER_AUTHORITY_REF, "source_ref"],
    [artifact.source_sha256, PRODUCT_OWNER_AUTHORITY_SHA256, "source_sha256"],
  ];
  for (const [actual, expected, field] of exactCoordinates) if (actual !== expected) fail(`${path}.${field}`, "does not bind the exact Product-owner-issued candidate-structure evaluation authority");
  if (artifact.source_sha256 !== sha256Bytes(authoritySourceBytes)) fail(`${path}.source_sha256`, "does not bind the supplied exact Product authority bytes");
  const digest = sha256Bytes(bytes);
  return { artifact, digest, artifactIdentity: `${STRUCTURE_GRANT_PREFIX}${digest.slice("sha256:".length)}` };
}

function validateStructure(value: Readonly<Record<string, unknown>>, candidate: ValidatedCompilationCandidate, grant: ValidatedStructureGrant): { identity: string; digest: string; subjectIdentity: string; subjectDigest: string } {
  requireExact(value, ["calculus_basis_identity", "checks", "decision", "evaluated_at", "evaluator_identity", "evidence_refs", "functor_ref", "interpretation_contract_identity", "kind", "schema_version", "semantic_compilation_candidate_identity", "semantic_compilation_candidate_sha256", "signature_identity", "traversal_ref"], "candidate_structure_result");
  if (value.kind !== "stdo-representation.candidate-structure-result" || value.schema_version !== 2 || value.functor_ref !== F_D || value.decision !== "eligible") fail("candidate_structure_result", "is not an eligible exact F_D result");
  if (value.traversal_ref !== STRUCTURE_TRAVERSAL || value.evaluator_identity !== STRUCTURE_EVALUATOR) fail("candidate_structure_result", "does not bind the selected deterministic structure traversal and evaluator");
  if (value.semantic_compilation_candidate_identity !== candidate.identity || value.semantic_compilation_candidate_sha256 !== candidate.digest) fail("candidate_structure_result", "does not point to the unchanged supplied candidate bytes");
  if (value.calculus_basis_identity !== candidate.calculus.identity || value.signature_identity !== candidate.targetProfile.identity || value.interpretation_contract_identity !== candidate.interpretationContract.identity) fail("candidate_structure_result", "does not bind the candidate's exact structural basis");
  if (grant.artifact.grantee_identity !== value.evaluator_identity || grant.artifact.authority_identity !== PRODUCT_OWNER_AUTHORITY) fail("candidate_structure_result", "does not resolve its exact external deterministic evaluation grant");
  requireExact(value.checks, ["basis_coherence", "canonical_bytes", "external_resolutions", "identity_derivation", "ordering", "population_totality", "provenance_binding", "record_shapes", "reference_domains", "source_inventory"], "candidate_structure_result.checks");
  if (Object.values(value.checks).some((decision) => decision !== true)) fail("candidate_structure_result.checks", "all exact deterministic checks must be true for eligibility");
  const evidence = requireStrings(value.evidence_refs, "candidate_structure_result.evidence_refs", false).map((entry, index) => requireUriReference(entry, `candidate_structure_result.evidence_refs[${index}]`));
  if (!evidence.includes(grant.artifactIdentity)) fail("candidate_structure_result.evidence_refs", "does not cite the exact resolved evaluation-grant artifact");
  requireTimestamp(value.evaluated_at, "candidate_structure_result.evaluated_at");
  const digest = sha256Bytes(canonicalRecordBytes(value as unknown as JsonValue));
  return { identity: `${STRUCTURE_PREFIX}${digest.slice("sha256:".length)}`, digest, subjectIdentity: candidate.identity, subjectDigest: candidate.digest };
}

function identityField(row: JsonValue, field: string, path: string): string {
  if (!isRecord(row)) fail(path, "must be an object");
  return requireIdentity(row[field], `${path}.${field}`);
}

function deriveSourceBindings(
  model: AxiomModel,
  recordProvenance: readonly AxiomRecordProvenance[],
  evaluatedMembers: readonly JsonValue[],
  selectionRows: readonly JsonValue[],
  path: string,
): readonly AxiomSourceBinding[] {
  const selections = new Map<string, Readonly<Record<string, unknown>>>();
  for (const [index, raw] of selectionRows.entries()) {
    if (!isRecord(raw)) fail(`${path}.selections[${index}]`, "must be an object");
    selections.set(requireIdentity(raw.selection_ref, `${path}.selections[${index}].selection_ref`), raw);
  }
  const provenance = new Map(recordProvenance.map((row) => [row.model_record_ref, row]));
  const residualIds = new Set(model.X.map((row) => row.id));
  return evaluatedMembers.map((raw, index): AxiomSourceBinding => {
    const rowPath = `${path}.evaluated_members[${index}]`;
    if (!isRecord(raw)) fail(rowPath, "must be an object");
    const refs = requireStrings(raw.selection_refs, `${rowPath}.selection_refs`);
    const selectedRecordRefs = new Set(refs.flatMap((ref) => {
      const selection = selections.get(ref);
      if (selection === undefined) fail(`${rowPath}.selection_refs`, `does not resolve final selection ${ref}`);
      return requireStrings(selection.model_record_refs, `${path}.selections.${ref}.model_record_refs`);
    }));
    const memberPath = String(raw.member_path);
    const memberSha256 = String(raw.member_sha256);
    const directlyRepresented = recordProvenance
      .filter((binding) => binding.source_locators.some((locator) => locator.member_path === memberPath && locator.member_sha256 === memberSha256))
      .map((binding) => binding.model_record_ref)
      .sort(compareUnicodeCodeUnits);
    for (const ref of directlyRepresented) if (!selectedRecordRefs.has(ref)) fail(rowPath, `does not cite the retained selection owning direct record-provenance binding ${ref}`);
    const modelRefs = [...selectedRecordRefs]
      .filter((ref) => provenance.get(ref)?.source_locators.some((locator) => locator.member_path === memberPath && locator.member_sha256 === memberSha256) === true)
      .sort(compareUnicodeCodeUnits);
    const residualRefs = modelRefs.filter((ref) => residualIds.has(ref));
    const disposition = requireString(raw.disposition, `${rowPath}.disposition`);
    if (disposition === "contains_retained_material") {
      if (modelRefs.length === 0) fail(rowPath, "contains_retained_material has no final represented model record");
      return { member_path: memberPath, member_sha256: memberSha256, disposition: "retained", model_refs: modelRefs, residual_refs: residualRefs, reason_code: "modeled" };
    }
    if (disposition === "uncertain" || disposition === "refused") {
      if (residualRefs.length === 0 || residualRefs.length !== modelRefs.length) fail(rowPath, "uncertain or refused source member must resolve only exact model X residuals");
      return { member_path: memberPath, member_sha256: memberSha256, disposition: "represented_by_residual", model_refs: modelRefs, residual_refs: residualRefs, reason_code: "unresolved" };
    }
    if (modelRefs.length !== 0) fail(rowPath, "inapplicable or no-retained-material source member cannot resolve final model records");
    return { member_path: memberPath, member_sha256: memberSha256, disposition: "inapplicable", model_refs: [], residual_refs: [], reason_code: "excluded_by_contract" };
  });
}

function validateLedger(value: Readonly<Record<string, unknown>>, candidate: ValidatedCompilationCandidate, structure: { identity: string; digest: string }, program: AcceptedAxiomaticProgram, grant: ValidatedGrant): SelectionLedger {
  requireExact(value, ["author", "calculus_basis_identity", "candidate_model_content_identity", "candidate_structure_result_identity", "candidate_structure_result_sha256", "compilation_residuals", "evaluated_members", "generated_source_keys", "interpretation_contract_identity", "kind", "proposal_dispositions", "record_provenance", "schema_version", "selections", "semantic_compilation_candidate_identity", "semantic_compilation_candidate_sha256", "signature_identity", "source_member_set_sha256", "source_stdo_manifest_sha256", "source_stdo_uri", "subject_basis_identity", "supersedes", "what_member_set_identity"], "selection_ledger");
  if (value.kind !== "stdo-representation.semantic-selection-ledger" || value.schema_version !== 3 || value.supersedes !== null) fail("selection_ledger", "is not one first exact semantic-selection ledger");
  const exactBindings: readonly [unknown, unknown, string][] = [
    [value.calculus_basis_identity, candidate.calculus.identity, "calculus_basis_identity"],
    [value.subject_basis_identity, candidate.subjectBasis.identity, "subject_basis_identity"],
    [value.source_stdo_uri, candidate.corpus.identity, "source_stdo_uri"],
    [value.source_stdo_manifest_sha256, candidate.corpus.sha256, "source_stdo_manifest_sha256"],
    [value.source_member_set_sha256, STDO_MEMBER_SET_SHA256, "source_member_set_sha256"],
    [value.what_member_set_identity, candidate.whatMemberSetIdentity, "what_member_set_identity"],
    [value.signature_identity, candidate.targetProfile.identity, "signature_identity"],
    [value.interpretation_contract_identity, candidate.interpretationContract.identity, "interpretation_contract_identity"],
    [value.semantic_compilation_candidate_identity, candidate.identity, "semantic_compilation_candidate_identity"],
    [value.semantic_compilation_candidate_sha256, candidate.digest, "semantic_compilation_candidate_sha256"],
    [value.candidate_structure_result_identity, structure.identity, "candidate_structure_result_identity"],
    [value.candidate_structure_result_sha256, structure.digest, "candidate_structure_result_sha256"],
    [value.candidate_model_content_identity, candidate.modelContentIdentity, "candidate_model_content_identity"],
  ];
  for (const [actual, expected, field] of exactBindings) if (actual !== expected) fail(`selection_ledger.${field}`, "does not preserve the exact selection subject and basis");
  if (program.model_content_identity !== candidate.modelContentIdentity || canonicalJson(program.model as unknown as JsonValue) !== canonicalJson(candidate.model as unknown as JsonValue)) fail("accepted_program.model", "does not preserve the selected candidate model unchanged");
  const finalRecordProvenance = validateRecordProvenance(value.record_provenance, candidate.model, candidate.sourceMembers, "selection_ledger.record_provenance");
  if (canonicalJson(finalRecordProvenance as unknown as JsonValue) !== canonicalJson(candidate.recordProvenance as unknown as JsonValue)) fail("selection_ledger.record_provenance", "does not preserve the candidate record-provenance relation unchanged");
  if (canonicalJson(program.record_provenance as unknown as JsonValue) !== canonicalJson(finalRecordProvenance as unknown as JsonValue)) fail("accepted_program.record_provenance", "does not preserve the final ledger record-provenance relation unchanged");
  const finalSelections = validateSelections(value.selections, candidate.model, finalRecordProvenance, candidate.sourceMembers, "selection_ledger.selections");
  const finalEvaluatedMembers = validateEvaluatedMembers(value.evaluated_members, finalSelections.rows, candidate.sourceMembers, "selection_ledger.evaluated_members");
  const finalGeneratedSourceKeys = validateGeneratedSourceKeys(value.generated_source_keys, finalRecordProvenance, candidate.sourceMembers, "selection_ledger.generated_source_keys");
  const finalCompilationResiduals = validateCompilationResiduals(value.compilation_residuals, candidate.model, candidate.sourceMembers, "selection_ledger.compilation_residuals", true);
  const expectedSourceBindings = deriveSourceBindings(candidate.model, finalRecordProvenance, finalEvaluatedMembers, finalSelections.rows, "selection_ledger");
  if (canonicalJson(program.source_bindings as unknown as JsonValue) !== canonicalJson(expectedSourceBindings as unknown as JsonValue)) fail("accepted_program.source_bindings", "is not the deterministic source-binding projection of the selection ledger");

  requireExact(value.author, ["actor_identity", "authority_identity", "basis_refs", "decided_at", "evidence_refs", "grant_identity", "grant_scope", "subject_identity", "subject_sha256", "traversal_ref"], "selection_ledger.author");
  if (value.author.traversal_ref !== SELECTION_TRAVERSAL || value.author.actor_identity !== PRODUCT_OWNER_ACTOR || value.author.authority_identity !== PRODUCT_OWNER_AUTHORITY || value.author.grant_identity !== PRODUCT_OWNER_GRANT || value.author.grant_scope !== PRODUCT_OWNER_GRANT_SCOPE || value.author.subject_identity !== candidate.identity || value.author.subject_sha256 !== candidate.digest) fail("selection_ledger.author", "does not record exact authorized F_H[v_select] over the unchanged candidate");
  if (grant.artifact.grant_identity !== value.author.grant_identity || grant.artifact.actor_identity !== value.author.actor_identity || grant.artifact.authority_identity !== value.author.authority_identity || grant.artifact.grant_scope !== value.author.grant_scope || grant.artifact.source_ref !== PRODUCT_OWNER_AUTHORITY_REF || grant.artifact.source_sha256 !== PRODUCT_OWNER_AUTHORITY_SHA256) fail("selection_ledger.author", "does not resolve the exact external Product-owner grant");
  const grantBasis = [candidate.calculus.identity, candidate.frameBasisIdentity, candidate.interpretationContract.identity, candidate.subjectBasis.identity, candidate.targetProfile.identity, candidate.whatMemberSetIdentity].sort(compareUnicodeCodeUnits);
  const expectedBasis = [...grantBasis, candidate.identity, structure.identity].sort(compareUnicodeCodeUnits);
  const authorBasis = requireStrings(value.author.basis_refs, "selection_ledger.author.basis_refs", false).map((entry, index) => requireIdentity(entry, `selection_ledger.author.basis_refs[${index}]`));
  if (canonicalJson(authorBasis as unknown as JsonValue) !== canonicalJson(expectedBasis as unknown as JsonValue)) fail("selection_ledger.author.basis_refs", "does not bind the exact candidate, structure result, WHAT, frame, and calculus basis");
  if (canonicalJson(grant.artifact.basis_refs as unknown as JsonValue) !== canonicalJson(grantBasis as unknown as JsonValue)) fail("semantic_grant.basis_refs", "does not bind the exact stable Product-owner grant basis");
  requireTimestamp(value.author.decided_at, "selection_ledger.author.decided_at");
  const authorEvidence = requireStrings(value.author.evidence_refs, "selection_ledger.author.evidence_refs", false).map((entry, index) => requireUriReference(entry, `selection_ledger.author.evidence_refs[${index}]`));
  for (const required of [candidate.identity, grant.artifactIdentity, structure.identity]) {
    if (!authorEvidence.includes(required)) fail("selection_ledger.author.evidence_refs", `does not cite required unchanged evidence ${required}`);
  }

  type ProposalKind = SelectionLedger["proposal_dispositions"][number]["proposal_kind"];
  interface ProposalEntry { readonly kind: ProposalKind; readonly row: JsonValue }
  const proposals = new Map<string, ProposalEntry>();
  const addProposal = (identity: string, kind: ProposalKind, row: JsonValue): void => {
    if (proposals.has(identity)) fail("selection_ledger.proposal_dispositions", `candidate proposal identity ${identity} occurs in more than one proposal family`);
    proposals.set(identity, { kind, row });
  };
  candidate.evaluatedMembers.forEach((row, index) => addProposal(evaluatedMemberIdentity(row, `semantic_compilation_candidate.proposed_evaluated_members[${index}]`), "evaluated_member", row));
  for (const row of [...candidate.model.O, ...candidate.model.E, ...candidate.model.C, ...candidate.model.L, ...candidate.model.X, ...candidate.model.V, ...candidate.model.T, ...candidate.model.J]) addProposal(row.id, "model_record", row as unknown as JsonValue);
  candidate.selections.forEach((row, index) => addProposal(identityField(row, "selection_ref", `semantic_compilation_candidate.proposed_selections[${index}]`), "selection", row));
  candidate.generatedSourceKeys.forEach((row, index) => addProposal(identityField(row, "source_key", `semantic_compilation_candidate.proposed_generated_source_keys[${index}]`), "generated_source_key", row));
  candidate.compilationResiduals.forEach((row, index) => addProposal(identityField(row, "residual_ref", `semantic_compilation_candidate.compilation_residuals[${index}]`), "compilation_residual", row));

  const finals = new Map<string, ProposalEntry>();
  const addFinal = (identity: string, kind: ProposalKind, row: JsonValue): void => {
    if (finals.has(identity)) fail("selection_ledger", `final identity ${identity} occurs in more than one non-model family`);
    finals.set(identity, { kind, row });
  };
  finalEvaluatedMembers.forEach((row, index) => addFinal(evaluatedMemberIdentity(row, `selection_ledger.evaluated_members[${index}]`), "evaluated_member", row));
  finalSelections.rows.forEach((row, index) => addFinal(identityField(row, "selection_ref", `selection_ledger.selections[${index}]`), "selection", row));
  finalGeneratedSourceKeys.rows.forEach((row, index) => addFinal(identityField(row, "source_key", `selection_ledger.generated_source_keys[${index}]`), "generated_source_key", row));
  finalCompilationResiduals.rows.forEach((row, index) => addFinal(identityField(row, "residual_ref", `selection_ledger.compilation_residuals[${index}]`), "compilation_residual", row));

  const dispositions = requireRecordRows(value.proposal_dispositions, ["decision", "final_refs", "proposal_kind", "proposal_ref", "rationale"], "selection_ledger.proposal_dispositions");
  const seen = new Set<string>();
  const finalReachability = new Map<string, number>();
  const modelResidualIds = new Set(candidate.model.X.map((row) => row.id));
  const reachFinal = (identity: string): void => {
    finalReachability.set(identity, (finalReachability.get(identity) ?? 0) + 1);
  };
  let previous = "";
  for (const [index, row] of dispositions.entries()) {
    const path = `selection_ledger.proposal_dispositions[${index}]`;
    const ref = requireIdentity(row.proposal_ref, `${path}.proposal_ref`);
    if (seen.has(ref) || (index > 0 && compareUnicodeCodeUnits(previous, ref) >= 0)) fail("selection_ledger.proposal_dispositions", "must be proposal-ref sorted and duplicate-free");
    seen.add(ref);
    previous = ref;
    const kind = requireString(row.proposal_kind, `${path}.proposal_kind`);
    const proposal = proposals.get(ref);
    if (proposal?.kind !== kind) fail(`${path}.proposal_kind`, "does not classify one exact candidate proposal");
    const decision = requireString(row.decision, `${path}.decision`);
    requireString(row.rationale, `${path}.rationale`);
    const finalRefs = requireStrings(row.final_refs, `${path}.final_refs`);
    if (kind === "model_record") {
      if (decision !== "accepted_unchanged") fail(`${path}.decision`, "model records may enter encoding only accepted unchanged");
      if (finalRefs.length !== 1 || finalRefs[0] !== ref) fail(`${path}.final_refs`, "an unchanged model record must preserve itself exactly");
      continue;
    }
    if (decision === "accepted_unchanged") {
      const final = finalRefs.length === 1 ? finals.get(finalRefs[0]!) : undefined;
      if (finalRefs[0] !== ref || final?.kind !== kind || canonicalJson(final.row) !== canonicalJson(proposal.row)) fail(`${path}.final_refs`, "accepted_unchanged must preserve the exact non-model proposal row and identity");
      reachFinal(ref);
      continue;
    }
    if (decision === "accepted_modified") {
      const replacement = finalRefs.length === 1 ? finalRefs[0]! : "";
      const final = finals.get(replacement);
      if (kind === "evaluated_member") {
        if (replacement !== ref || final?.kind !== kind || canonicalJson(final.row) === canonicalJson(proposal.row)) fail(`${path}.final_refs`, "accepted_modified evaluated member must preserve its exact Source member URI and name one changed final row");
      } else if (replacement === ref || proposals.has(replacement) || final?.kind !== kind) {
        fail(`${path}.final_refs`, "accepted_modified must name one new exact final replacement of the same proposal kind");
      }
      reachFinal(replacement);
      continue;
    }
    if (decision === "rejected" || decision === "resolved") {
      if (finalRefs.length !== 0) fail(`${path}.final_refs`, `${decision} must name no final reference`);
      continue;
    }
    if (decision === "retained_uncertain") {
      if (finalRefs.length === 0 || finalRefs.some((identity) => !modelResidualIds.has(identity))) fail(`${path}.final_refs`, "retained_uncertain must name one or more exact model X residual records");
      continue;
    }
    fail(`${path}.decision`, "is not one declared proposal disposition");
  }
  if (seen.size !== proposals.size || [...proposals.keys()].some((identity) => !seen.has(identity))) fail("selection_ledger.proposal_dispositions", "does not disposition the complete candidate proposal population exactly once");
  for (const identity of finals.keys()) if (finalReachability.get(identity) !== 1) fail("selection_ledger.proposal_dispositions", `must reach final non-model row ${identity} exactly once`);
  return value as unknown as SelectionLedger;
}

interface InterpretedModelCoordinate extends Readonly<Record<string, JsonValue>> {
  readonly calculus_basis_identity: string;
  readonly subject_basis_identity: string;
  readonly signature_identity: string;
  readonly interpretation_contract_identity: string;
  readonly model_content_identity: string;
  readonly semantic_selection_ledger_identity: string;
  readonly semantic_selection_ledger_sha256: string;
}

function interpretedModelCoordinate(program: AcceptedAxiomaticProgram, ledgerIdentity: string, ledgerDigest: string): { coordinate: InterpretedModelCoordinate; identity: string; digest: string } {
  const coordinate: InterpretedModelCoordinate = {
    calculus_basis_identity: program.basis.calculus.identity,
    subject_basis_identity: program.basis.subject_basis.identity,
    signature_identity: program.basis.target_profile.identity,
    interpretation_contract_identity: program.basis.interpretation_contract.identity,
    model_content_identity: program.model_content_identity,
    semantic_selection_ledger_identity: ledgerIdentity,
    semantic_selection_ledger_sha256: ledgerDigest,
  };
  const digest = sha256Canonical(coordinate);
  return { coordinate, digest, identity: `${INTERPRETED_MODEL_PREFIX}${digest.slice("sha256:".length)}` };
}

function validateJudgment(value: Readonly<Record<string, unknown>>, program: AcceptedAxiomaticProgram, programIdentity: string, ledger: SelectionLedger, ledgerIdentity: string, ledgerDigest: string, structure: { identity: string; digest: string; subjectIdentity: string; subjectDigest: string }, grant: ValidatedGrant): { judgment: SemanticSelectionJudgment; interpretedModel: { coordinate: InterpretedModelCoordinate; identity: string; digest: string } } {
  const keys = ["admitting_authority_refs", "actor_identity", "authority_identity", "basis_refs", "decided_at", "decision", "evidence_refs", "grant_identity", "grant_scope", "kind", "schema_version", "subject_identity", "subject_kind", "subject_sha256", "supersedes", "traversal_ref"] as const;
  requireExact(value, keys, "semantic_judgment");
  if (value.kind !== "stdo-representation.authority-acceptance" || value.schema_version !== 1 || value.subject_kind !== "interpreted_model" || value.decision !== "accepted") fail("semantic_judgment", "is not an accepting external interpreted-model judgment");
  if (value.traversal_ref !== INTERPRETATION_ACCEPTANCE_TRAVERSAL) fail("semantic_judgment.traversal_ref", "does not bind the selected interpretation-acceptance traversal");
  for (const key of ["subject_identity", "actor_identity", "authority_identity", "grant_identity"] as const) requireIdentity(value[key], `semantic_judgment.${key}`);
  requireSha256(value.subject_sha256, "semantic_judgment.subject_sha256");
  requireString(value.grant_scope, "semantic_judgment.grant_scope");
  requireTimestamp(value.decided_at, "semantic_judgment.decided_at");
  if (value.admitting_authority_refs !== null || value.supersedes !== null) fail("semantic_judgment", "first interpreted-model acceptance requires null admitting authorities and supersession");
  if (value.actor_identity !== PRODUCT_OWNER_ACTOR || value.authority_identity !== PRODUCT_OWNER_AUTHORITY || value.grant_identity !== PRODUCT_OWNER_GRANT || value.grant_scope !== PRODUCT_OWNER_GRANT_SCOPE) fail("semantic_judgment", "does not bind the exact Product-owner interpretation-acceptance grant");
  if (value.grant_identity !== grant.artifact.grant_identity || grant.artifact.actor_identity !== value.actor_identity || grant.artifact.authority_identity !== value.authority_identity || grant.artifact.grant_scope !== value.grant_scope) fail("semantic_judgment", "does not resolve its exact external authority-grant artifact");
  if (grant.artifact.source_ref !== PRODUCT_OWNER_AUTHORITY_REF) fail("semantic_grant.source_ref", "does not locate the Product authority clause");
  const evidenceRefs = requireStrings(value.evidence_refs, "semantic_judgment.evidence_refs", false).map((entry, index) => requireUriReference(entry, `semantic_judgment.evidence_refs[${index}]`));
  for (const required of [grant.artifactIdentity, ledgerIdentity, program.basis.semantic_compilation_candidate.identity, programIdentity, structure.identity]) {
    if (!evidenceRefs.includes(required)) fail("semantic_judgment.evidence_refs", `does not cite required unchanged evidence ${required}`);
  }
  const interpretedModel = interpretedModelCoordinate(program, ledgerIdentity, ledgerDigest);
  if (value.subject_identity !== interpretedModel.identity || value.subject_sha256 !== program.model_content_identity) fail("semantic_judgment.subject_identity", "does not point to the unchanged interpreted-model identity and exact model content");
  const grantBasisRefs = [program.basis.calculus.identity, FRAME_BASIS_IDENTITY, program.basis.interpretation_contract.identity, program.basis.subject_basis.identity, program.basis.target_profile.identity, WHAT_MEMBER_SET_IDENTITY].sort(compareUnicodeCodeUnits);
  const expectedBasisRefs = [...grantBasisRefs, ledgerIdentity, program.basis.semantic_compilation_candidate.identity, programIdentity, structure.identity].sort(compareUnicodeCodeUnits);
  const basisRefs = requireStrings(value.basis_refs, "semantic_judgment.basis_refs", false).map((entry, index) => requireIdentity(entry, `semantic_judgment.basis_refs[${index}]`));
  if (canonicalJson(basisRefs as unknown as JsonValue) !== canonicalJson(expectedBasisRefs as unknown as JsonValue)) fail("semantic_judgment.basis_refs", "does not bind the complete interpreted-model activation basis");
  if (canonicalJson(grant.artifact.basis_refs as unknown as JsonValue) !== canonicalJson(grantBasisRefs as unknown as JsonValue)) fail("semantic_grant.basis_refs", "does not bind the exact stable Product-owner grant basis");
  if (ledger.semantic_compilation_candidate_identity !== structure.subjectIdentity || ledger.semantic_compilation_candidate_sha256 !== structure.subjectDigest) fail("selection_ledger", "does not bind the structure result's exact candidate");
  if (ledger.candidate_structure_result_identity !== structure.identity || ledger.candidate_structure_result_sha256 !== structure.digest) fail("selection_ledger", "does not bind the exact structure result");
  if (program.basis.semantic_compilation_candidate.identity !== ledger.semantic_compilation_candidate_identity || program.basis.semantic_compilation_candidate.sha256 !== ledger.semantic_compilation_candidate_sha256) fail("accepted_program.basis.semantic_compilation_candidate", "does not bind the selected candidate");
  if (program.basis.candidate_structure_result.identity !== structure.identity || program.basis.candidate_structure_result.sha256 !== structure.digest) fail("accepted_program.basis.candidate_structure_result", "does not bind the exact structure result");
  return { judgment: value as unknown as SemanticSelectionJudgment, interpretedModel };
}

function validateProfile(bytes: Uint8Array): ValidatedAxiomIndexProfile {
  const value = parseUniqueJson(bytes, "profile");
  requireExact(value, [
    "acceptance_gate", "authority_grants", "build_tenant", "calculus_basis", "canonicalization", "carrier",
    "carrier_admission", "configuration", "frame_basis", "identity", "index_mapping", "index_relation", "input",
    "interpretation_contract", "kind", "projection_relation", "publication_contract", "publisher_membership",
    "schema_version", "semantic_acceptance", "signature_validation", "source_basis", "source_binding_projection",
    "status", "structural_judgment", "structure_evaluator", "subject_basis_identity", "subject_inventory",
    "target_signature", "transformation_population", "what_member_set_identity",
  ], "profile");
  if (value.kind !== "stdo-index.gtl-encoding-profile" || value.schema_version !== 5 || value.identity !== PROFILE_IDENTITY) fail("profile", "does not identify the selected Axiom Index GTL profile");

  requireExact(value.build_tenant, ["carrier_basis", "identity"], "profile.build_tenant");
  if (value.build_tenant.identity !== BUILD_TENANT_IDENTITY) fail("profile.build_tenant.identity", "does not bind the GTL build tenant");
  requireExact(value.build_tenant.carrier_basis, ["coordinate", "identity", "identity_rule"], "profile.build_tenant.carrier_basis");
  const carrierCoordinate = requireCarrierBasisCoordinate(value.build_tenant.carrier_basis.coordinate, "profile.build_tenant.carrier_basis.coordinate");
  const derivedCarrierIdentity = carrierBasisIdentity(carrierCoordinate);
  if (value.build_tenant.carrier_basis.identity !== derivedCarrierIdentity) fail("profile.build_tenant.carrier_basis.identity", "does not reproduce sha256(RFC8785_JCS(coordinate))");
  if (value.build_tenant.carrier_basis.identity_rule !== `${CARRIER_BASIS_PREFIX}<sha256(RFC8785_JCS(coordinate))>`) fail("profile.build_tenant.carrier_basis.identity_rule", "does not declare the selected carrier-basis identity law");
  if (canonicalJson(carrierCoordinate) !== canonicalJson(FROZEN_GTL_CARRIER_COORDINATE)) fail("profile.build_tenant.carrier_basis.coordinate", "does not bind the selected frozen GTL coordinate");

  requireExact(value.source_basis, ["manifest_sha256", "release_uri"], "profile.source_basis");
  requireExact(value.target_signature, ["identity", "sha256"], "profile.target_signature");
  requireExact(value.interpretation_contract, ["identity", "sha256"], "profile.interpretation_contract");
  requireExact(value.frame_basis, ["identity", "sha256"], "profile.frame_basis");
  requireExact(value.calculus_basis, ["identity", "sha256"], "profile.calculus_basis");
  const exactBasisBindings: readonly [unknown, unknown, string][] = [
    [value.source_basis.release_uri, STDO_RELEASE_URI, "source_basis.release_uri"],
    [value.source_basis.manifest_sha256, STDO_MANIFEST_SHA256, "source_basis.manifest_sha256"],
    [value.subject_basis_identity, STDO_SUBJECT_BASIS_IDENTITY, "subject_basis_identity"],
    [value.what_member_set_identity, WHAT_MEMBER_SET_IDENTITY, "what_member_set_identity"],
    [value.target_signature.identity, TARGET_SIGNATURE_IDENTITY, "target_signature.identity"],
    [value.target_signature.sha256, TARGET_SIGNATURE_SHA256, "target_signature.sha256"],
    [value.interpretation_contract.identity, COMPILE_TRAVERSAL, "interpretation_contract.identity"],
    [value.interpretation_contract.sha256, INTERPRETATION_CONTRACT_SHA256, "interpretation_contract.sha256"],
    [value.frame_basis.identity, FRAME_BASIS_IDENTITY, "frame_basis.identity"],
    [value.frame_basis.sha256, FRAME_BASIS_SHA256, "frame_basis.sha256"],
    [value.calculus_basis.identity, CALCULUS_BASIS_IDENTITY, "calculus_basis.identity"],
    [value.calculus_basis.sha256, CALCULUS_BASIS_SHA256, "calculus_basis.sha256"],
  ];
  for (const [actual, expected, path] of exactBasisBindings) if (actual !== expected) fail(`profile.${path}`, "does not bind the selected exact basis");

  requireExact(value.canonicalization, ["artifact_framing", "carrier_value_algorithm", "coordinate_algorithm", "duplicate_object_names", "input_domain", "number_domain", "program_content_identity_rule", "raw_admission_subject", "string_domain", "unicode_normalization"], "profile.canonicalization");
  requireExact(value.canonicalization.artifact_framing, ["prefix_hex", "suffix_hex", "suffix_in_program_content_identity"], "profile.canonicalization.artifact_framing");
  const canonicalizationExpected = {
    coordinate_algorithm: "RFC8785_JCS_SHA256", carrier_value_algorithm: "RFC8785_JCS",
    raw_admission_subject: "canonical_module_publication_value_bytes_without_framing",
    artifact_framing: { prefix_hex: "", suffix_hex: "0a", suffix_in_program_content_identity: true },
    program_content_identity_rule: "sha256(RFC8785_JCS(raw_admitted_ModulePublication) || 0x0a)",
    input_domain: "I-JSON", duplicate_object_names: "reject_before_canonicalization",
    string_domain: "Unicode_scalar_values", unicode_normalization: "none", number_domain: "non_negative_safe_integers_excluding_negative_zero",
  } as const;
  if (canonicalJson(value.canonicalization as JsonValue) !== canonicalJson(canonicalizationExpected)) fail("profile.canonicalization", "does not bind the exact identity and carrier framing law");

  requireExact(value.publication_contract, ["contribution", "module_publication", "product_semantics_binding", "record_contract", "rule"], "profile.publication_contract");
  requireExact(value.publication_contract.module_publication, ["exact_fields", "inventory_cardinality", "kind", "module_version", "raw_admission_contract_ref"], "profile.publication_contract.module_publication");
  requireExact(value.publication_contract.product_semantics_binding, ["binding_ref", "exact_fields", "kind", "publisher_fields"], "profile.publication_contract.product_semantics_binding");
  requireExact(value.publication_contract.record_contract, ["contract_kind", "contract_ref", "contract_version", "exact_fields", "value_kind"], "profile.publication_contract.record_contract");
  requireExact(value.publication_contract.rule, ["exact_fields", "kind", "name", "tags"], "profile.publication_contract.rule");
  requireExact(value.publication_contract.contribution, ["compatibility_refs", "declaration_or_contract_ref", "exact_fields", "handle", "kind", "program_membership_refs", "provenance_refs", "raw_admission_contract_ref", "readiness_prerequisite_refs"], "profile.publication_contract.contribution");

  requireExact(value.configuration, ["basis_schema", "exact_keys", "field_keys", "kind", "record_schemas", "table_laws", "tuple_schemas", "version"], "profile.configuration");
  requireExact(value.configuration.basis_schema, ["coordinate_exact_fields", "exact_fields"], "profile.configuration.basis_schema");
  requireExact(value.configuration.field_keys, ["basis", "constraints", "external_resolutions", "identities", "judgments", "latitudes", "legend", "metadata", "objects", "record_provenance", "relations", "residuals", "source_bindings", "strings", "transformations", "traversals"], "profile.configuration.field_keys");
  requireExact(value.configuration.table_laws, ["identities", "indexes", "record_rows", "reference_sets", "strings"], "profile.configuration.table_laws");
  requireExact(value.configuration.tuple_schemas, ["J", "T", "V", "c", "e", "l", "m", "o", "p", "q", "r", "source_locator", "x"], "profile.configuration.tuple_schemas");
  for (const [name, schema] of Object.entries(value.configuration.tuple_schemas)) {
    requireExact(schema, ["fields", "types"], `profile.configuration.tuple_schemas.${name}`);
    const fields = requireStringArray(schema.fields, `profile.configuration.tuple_schemas.${name}.fields`, false);
    const types = requireStringArray(schema.types, `profile.configuration.tuple_schemas.${name}.types`, false);
    if (fields.length !== types.length || new Set(fields).size !== fields.length) fail(`profile.configuration.tuple_schemas.${name}`, "must bind one unique type for every tuple position");
  }
  requireExact(value.configuration.record_schemas, ["external_resolution", "external_resolution_witness"], "profile.configuration.record_schemas");
  for (const [name, schema] of Object.entries(value.configuration.record_schemas)) {
    requireExact(schema, ["exact_fields", "field_types"], `profile.configuration.record_schemas.${name}`);
    const fields = requireStringArray(schema.exact_fields, `profile.configuration.record_schemas.${name}.exact_fields`, false);
    const types = requireStringArray(schema.field_types, `profile.configuration.record_schemas.${name}.field_types`, false);
    if (fields.length !== types.length || new Set(fields).size !== fields.length) fail(`profile.configuration.record_schemas.${name}`, "must bind one unique type for every record field");
  }

  requireExact(value.structure_evaluator, ["authority_source_ref", "grant_identity_rule", "grant_kind", "grant_scope", "identity", "implementation_ref", "implementation_sha256"], "profile.structure_evaluator");
  for (const [actual, expected, path] of [
    [value.structure_evaluator.identity, STRUCTURE_EVALUATOR, "identity"],
    [value.structure_evaluator.implementation_ref, STRUCTURE_EVALUATOR_SOURCE_REF, "implementation_ref"],
    [value.structure_evaluator.implementation_sha256, STRUCTURE_EVALUATOR_SHA256, "implementation_sha256"],
    [value.structure_evaluator.grant_scope, STRUCTURE_GRANT_SCOPE, "grant_scope"],
    [value.structure_evaluator.authority_source_ref, PRODUCT_OWNER_AUTHORITY_REF, "authority_source_ref"],
  ] as const) if (actual !== expected) fail(`profile.structure_evaluator.${path}`, "does not bind the selected structural evaluator");

  const digest = sha256Bytes(bytes);
  if (digest !== PROFILE_SHA256) fail("profile", "is not the complete selected Axiom Index GTL profile bytes");
  return {
    definition: value as unknown as SelectedAxiomIndexProfile,
    digest,
    carrier_basis_identity: derivedCarrierIdentity,
  };
}

function tarString(bytes: Uint8Array, start: number, length: number): string {
  const slice = bytes.slice(start, start + length);
  const end = slice.indexOf(0);
  return new TextDecoder("utf-8", { fatal: true }).decode(end === -1 ? slice : slice.slice(0, end));
}

function tarOctal(bytes: Uint8Array, start: number, length: number, path: string): number {
  const raw = tarString(bytes, start, length).trim();
  if (!/^[0-7]+$/u.test(raw)) fail(path, "has an invalid tar octal field");
  const value = Number.parseInt(raw, 8);
  if (!Number.isSafeInteger(value) || value < 0) fail(path, "has an unsafe tar size");
  return value;
}

interface PackedMember {
  readonly sha256: string;
  readonly bytes: Uint8Array;
}

function npmTarMembers(artifact: Uint8Array): ReadonlyMap<string, PackedMember> {
  let tar: Uint8Array;
  try { tar = gunzipSync(artifact); } catch { fail("publisher_artifact", "must be one readable gzip-compressed npm tar archive"); }
  const members = new Map<string, PackedMember>();
  let offset = 0;
  let zeroBlocks = 0;
  while (offset + 512 <= tar.length) {
    const header = tar.slice(offset, offset + 512);
    if (header.every((byte) => byte === 0)) {
      zeroBlocks += 1;
      offset += 512;
      if (zeroBlocks === 2) break;
      continue;
    }
    if (zeroBlocks !== 0) fail("publisher_artifact", "contains data after a tar end marker");
    const storedChecksum = tarOctal(header, 148, 8, "publisher_artifact.header.checksum");
    const checksumHeader = new Uint8Array(header);
    checksumHeader.fill(0x20, 148, 156);
    const actualChecksum = checksumHeader.reduce((sum, byte) => sum + byte, 0);
    if (storedChecksum !== actualChecksum) fail("publisher_artifact", "contains a tar header with the wrong checksum");
    const type = header[156] === 0 ? "0" : String.fromCharCode(header[156]!);
    if (type !== "0") fail("publisher_artifact", "contains a non-regular npm package member");
    const name = tarString(header, 0, 100);
    const prefix = tarString(header, 345, 155);
    const archivePath = prefix ? `${prefix}/${name}` : name;
    if (!archivePath.startsWith("package/")) fail("publisher_artifact", "contains a member outside the npm package root");
    const path = requireRelativePath(archivePath.slice("package/".length), "publisher_artifact.member.path");
    const size = tarOctal(header, 124, 12, `publisher_artifact.${path}.size`);
    const contentStart = offset + 512;
    const contentEnd = contentStart + size;
    if (contentEnd > tar.length || members.has(path)) fail(`publisher_artifact.${path}`, "is truncated or duplicated");
    const bytes = tar.slice(contentStart, contentEnd);
    members.set(path, { sha256: sha256Bytes(bytes), bytes });
    offset = contentStart + Math.ceil(size / 512) * 512;
  }
  if (zeroBlocks !== 2 || offset > tar.length || tar.slice(offset).some((byte) => byte !== 0)) fail("publisher_artifact", "does not end with the required tar zero blocks");
  return members;
}

function validatePublisher(input: AxiomIndexGtlInput, profile: ValidatedAxiomIndexProfile): { identity: string; digest: string } {
  const manifest = parseCanonicalRecord(input.publisher_manifest_bytes, "publisher_manifest");
  requireExact(manifest, ["artifact_digest", "carrier_basis", "commit_sha1", "contribution_manifest_ref", "descriptor_ref", "kind", "members", "module_path", "named_symbol", "package_name", "package_version", "product_content_digest", "repository", "schema_version", "supersedes", "tree_sha1"], "publisher_manifest");
  if (manifest.kind !== "stdo-representation.gtl-toolchain-product" || manifest.schema_version !== 2) fail("publisher_manifest", "has the wrong kind or schema version");
  const digest = sha256Bytes(input.publisher_manifest_bytes);
  const identity = `urn:stdo-representation:gtl-toolchain-product:sha256:${digest.slice("sha256:".length)}`;
  const artifactDigest = sha256Bytes(input.publisher_artifact_bytes);
  if (manifest.artifact_digest !== artifactDigest) fail("publisher_manifest.artifact_digest", "does not bind the exact publisher artifact bytes");
  if (manifest.repository !== "https://github.com/foolishimp/stdo_representation.git" || !/^[0-9a-f]{40}$/u.test(requireString(manifest.commit_sha1, "publisher_manifest.commit_sha1")) || !/^[0-9a-f]{40}$/u.test(requireString(manifest.tree_sha1, "publisher_manifest.tree_sha1"))) fail("publisher_manifest", "does not bind one immutable publisher repository coordinate");
  requireExact(manifest.carrier_basis, ["authority_inventory_count", "authority_root", "authority_tree_sha1", "commit_sha1", "identity", "repository"], "publisher_manifest.carrier_basis");
  const carrierBasisCoordinate = requireCarrierBasisCoordinate({
    authority_inventory_count: manifest.carrier_basis.authority_inventory_count,
    authority_root: manifest.carrier_basis.authority_root,
    authority_tree_sha1: manifest.carrier_basis.authority_tree_sha1,
    commit_sha1: manifest.carrier_basis.commit_sha1,
    repository: manifest.carrier_basis.repository,
  }, "publisher_manifest.carrier_basis.coordinate");
  const suppliedCarrierIdentity = requireIdentity(manifest.carrier_basis.identity, "publisher_manifest.carrier_basis.identity");
  const derivedCarrierIdentity = carrierBasisIdentity(carrierBasisCoordinate);
  if (suppliedCarrierIdentity !== derivedCarrierIdentity) fail("publisher_manifest.carrier_basis.identity", "does not reproduce sha256(RFC8785_JCS(carrier_basis coordinate))");
  if (canonicalJson(carrierBasisCoordinate) !== canonicalJson(profile.definition.build_tenant.carrier_basis.coordinate) || suppliedCarrierIdentity !== profile.carrier_basis_identity) fail("publisher_manifest.carrier_basis", "does not bind the selected profile carrier basis");
  requireExact(input.publisher as unknown as Readonly<Record<string, unknown>>, ["owning_product_id", "artifact_digest", "product_content_digest", "product_manifest_digest", "descriptor_ref", "contribution_manifest_ref", "package_name", "package_version", "module_path", "named_symbol"], "publisher");
  const bindings: readonly [unknown, unknown, string][] = [
    [input.publisher.owning_product_id, identity, "owning_product_id"],
    [input.publisher.artifact_digest, artifactDigest, "artifact_digest"],
    [input.publisher.product_manifest_digest, digest, "product_manifest_digest"],
    [input.publisher.product_content_digest, manifest.product_content_digest, "product_content_digest"],
    [input.publisher.descriptor_ref, manifest.descriptor_ref, "descriptor_ref"],
    [input.publisher.contribution_manifest_ref, manifest.contribution_manifest_ref, "contribution_manifest_ref"],
    [input.publisher.package_name, manifest.package_name, "package_name"],
    [input.publisher.package_version, manifest.package_version, "package_version"],
    [input.publisher.module_path, manifest.module_path, "module_path"],
    [input.publisher.named_symbol, manifest.named_symbol, "named_symbol"],
  ];
  for (const [actual, expected, field] of bindings) if (actual !== expected) fail(`publisher.${field}`, "does not match the exact publisher manifest");
  if (manifest.module_path !== "." || manifest.named_symbol !== "STDO_AXIOM_INDEX_GTL_PRODUCT_SEMANTICS") fail("publisher_manifest", "does not publish the Axiom Index semantics binding");
  if (!Array.isArray(manifest.members) || manifest.members.length === 0) fail("publisher_manifest.members", "must be non-empty");
  const paths: string[] = [];
  const rows: string[] = [];
  const manifestMembers = new Map<string, string>();
  for (const [index, member] of manifest.members.entries()) {
    requireExact(member, ["path", "sha256"], `publisher_manifest.members[${index}]`);
    const path = requireString(member.path, `publisher_manifest.members[${index}].path`);
    const memberDigest = requireSha256(member.sha256, `publisher_manifest.members[${index}].sha256`);
    if (path.startsWith("/") || path.includes("\\") || path.split("/").some((part) => !part || part === "..")) fail(`publisher_manifest.members[${index}].path`, "must be normalized and relative");
    paths.push(path);
    rows.push(`${path}\0${memberDigest}\n`);
    manifestMembers.set(path, memberDigest);
  }
  if (new Set(paths).size !== paths.length || paths.join("\0") !== [...paths].sort(compareUnicodeCodeUnits).join("\0")) fail("publisher_manifest.members", "must be path-sorted and duplicate-free");
  for (const required of ["build/src/axiom_index.js", "build/src/index.js", "package.json"]) if (!paths.includes(required)) fail("publisher_manifest.members", `does not contain ${required}`);
  if (sha256Bytes(rows.join("")) !== manifest.product_content_digest) fail("publisher_manifest.product_content_digest", "does not reproduce the member inventory");
  const packedMembers = npmTarMembers(input.publisher_artifact_bytes);
  if (packedMembers.size !== manifestMembers.size || paths.some((path) => packedMembers.get(path)?.sha256 !== manifestMembers.get(path))) fail("publisher_artifact", "member bytes do not equal the publisher manifest inventory");
  const packageMember = packedMembers.get("package.json");
  if (packageMember === undefined) fail("publisher_artifact", "does not contain package.json");
  const packageJson = parseUniqueJson(packageMember.bytes, "publisher_artifact.package.json");
  if (!isRecord(packageJson) || packageJson.name !== manifest.package_name || packageJson.version !== manifest.package_version || packageJson.type !== "module") fail("publisher_artifact.package.json", "does not identify the exact declared ESM package");
  if (!isRecord(packageJson.exports) || !isRecord(packageJson.exports["."]) || packageJson.exports["."].import !== "./build/src/index.js") fail("publisher_artifact.package.json", "does not export the declared package root from build/src/index.js");
  const indexMember = packedMembers.get("build/src/index.js");
  if (indexMember === undefined || !new TextDecoder("utf-8", { fatal: true }).decode(indexMember.bytes).includes(requireString(manifest.named_symbol, "publisher_manifest.named_symbol"))) fail("publisher_artifact.build/src/index.js", "does not export the declared named semantics symbol");
  if (manifest.supersedes !== null) requireString(manifest.supersedes, "publisher_manifest.supersedes");
  return { identity, digest };
}

function strings(model: AxiomModel, provenance: readonly AxiomRecordProvenance[], bindings: readonly AxiomSourceBinding[]): readonly string[] {
  const values = new Set<string>();
  for (const row of model.O) for (const value of [row.sort, row.scope, row.value]) values.add(value);
  for (const row of model.E) for (const value of [row.kind, row.scope, ...row.qualifiers]) values.add(value);
  for (const row of model.C) for (const value of [row.kind, row.predicate, row.scope, row.judgment_kind, row.refusal]) values.add(value);
  for (const row of model.L) for (const value of [row.scope, row.invalidation, ...row.allowed_variation, ...row.forbidden_variation]) values.add(value);
  for (const row of model.X) for (const value of [row.kind, row.uncertainty, row.consequence, row.scope, row.re_entry, row.invalidation]) values.add(value);
  for (const row of model.V) for (const value of [row.scope, ...row.preconditions, ...row.postconditions, ...row.stop_states]) values.add(value);
  for (const row of model.T) for (const value of [row.scope, row.invalidation, row.re_entry, ...row.preconditions, ...row.stop_states]) values.add(value);
  for (const row of model.J) for (const value of [row.kind, row.subject_digest, row.scope, row.decision, row.decided_at]) values.add(value);
  for (const row of model.ResolutionSet_M) for (const value of [row.reference_domain, row.external_target_kind, row.resolved_target_identity, row.basis_relation, row.resolution_basis, row.evidence_identity]) values.add(value);
  for (const row of provenance) {
    for (const value of [row.provenance_kind, row.semantic_address.source_key, row.semantic_address.term, row.semantic_address.bounded_context, row.semantic_address.owning_authority, row.semantic_address.selected_basis, row.semantic_address.governed_scope, ...row.derivation_evidence_refs]) values.add(value);
    for (const locator of row.source_locators) for (const value of [locator.basis_uri, locator.member_path, locator.member_sha256]) values.add(value);
    for (const locator of row.source_locators) if (locator.fragment !== null) values.add(locator.fragment);
  }
  for (const row of bindings) for (const value of [row.member_path, row.member_sha256, row.disposition, row.reason_code]) values.add(value);
  return [...values].sort(compareUnicodeCodeUnits);
}

function encodingLegend(profile: SelectedAxiomIndexProfile): Readonly<Record<string, JsonValue>> {
  return {
    tuple_schemas: profile.configuration.tuple_schemas as unknown as JsonValue,
    record_schemas: profile.configuration.record_schemas as unknown as JsonValue,
  };
}

function encodeProgram(
  program: AcceptedAxiomaticProgram,
  programIdentity: string,
  programSha256: string,
  ledgerIdentity: string,
  ledgerSha256: string,
  interpretedModel: { readonly identity: string; readonly digest: string },
  profile: SelectedAxiomIndexProfile,
): Readonly<Record<string, JsonValue>> {
  const model = program.model;
  const identities = [...model.I];
  const stringTable = strings(model, program.record_provenance, program.source_bindings);
  const identityIndex = new Map(identities.map((value, index) => [value, index]));
  const stringIndex = new Map(stringTable.map((value, index) => [value, index]));
  const ii = (value: string | null): number | null => {
    if (value === null) return null;
    const index = identityIndex.get(value);
    if (index === undefined) fail("accepted_program.model", `identity outside I: ${value}`);
    return index;
  };
  const si = (value: string): number => {
    const index = stringIndex.get(value);
    if (index === undefined) fail("accepted_program.model", `string outside table: ${value}`);
    return index;
  };
  const ss = (value: readonly string[]): readonly number[] => value.map(si);
  const ids = (value: readonly string[]): readonly number[] => value.map((entry) => ii(entry)!);
  return {
    k: profile.configuration.kind,
    v: profile.configuration.version,
    m: [interpretedModel.identity, interpretedModel.digest, programIdentity, programSha256, ledgerIdentity, ledgerSha256, model.b],
    b: program.basis as unknown as JsonValue,
    z: encodingLegend(profile),
    s: stringTable,
    i: identities,
    o: model.O.map((r) => [ii(r.id), si(r.sort), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), si(r.value)]),
    e: model.E.map((r) => [ii(r.id), si(r.kind), ii(r.source), ii(r.target), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), ss(r.qualifiers)]),
    c: model.C.map((r) => [ii(r.id), si(r.kind), ii(r.applies_to), si(r.predicate), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), si(r.judgment_kind), ii(r.latitude_ref), si(r.refusal)]),
    l: model.L.map((r) => [ii(r.id), ii(r.applies_to), ss(r.allowed_variation), ss(r.forbidden_variation), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), si(r.invalidation)]),
    x: model.X.map((r) => [ii(r.id), ii(r.subject), si(r.kind), si(r.uncertainty), si(r.consequence), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), si(r.re_entry), si(r.invalidation)]),
    V: model.V.map((r) => [ii(r.id), ii(r.domain), ii(r.codomain), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), ss(r.preconditions), ss(r.postconditions), ii(r.authority), ids(r.evidence), ids(r.provenance), ss(r.stop_states)]),
    T: model.T.map((r) => [ii(r.id), ii(r.traversal), ii(r.domain_model), ii(r.codomain_model), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), ii(r.operation_authority), ss(r.preconditions), ii(r.preservation_relation), ids(r.preserved), ids(r.introduced), ids(r.removed), ids(r.external_preserved), ids(r.external_introduced), ids(r.external_removed), r.external_resolution_witnesses as unknown as JsonValue, ids(r.residuals), ids(r.evidence), ids(r.provenance), ss(r.stop_states), si(r.invalidation), si(r.re_entry)]),
    J: model.J.map((r) => [ii(r.id), si(r.kind), ii(r.subject), si(r.subject_digest), ii(r.context), ii(r.owner), si(r.scope), ii(r.basis), ii(r.evaluator), ii(r.authority), si(r.decision), ids(r.evidence), ids(r.provenance), si(r.decided_at)]),
    q: model.ResolutionSet_M.map((r) => [ii(r.external_identity), si(r.reference_domain), si(r.external_target_kind), si(r.resolved_target_identity), si(r.basis_relation), si(r.resolution_basis), si(r.evidence_identity)]),
    p: program.record_provenance.map((row) => [
      ii(row.model_record_ref),
      si(row.provenance_kind),
      si(row.semantic_address.source_key),
      si(row.semantic_address.term),
      si(row.semantic_address.bounded_context),
      si(row.semantic_address.owning_authority),
      si(row.semantic_address.selected_basis),
      si(row.semantic_address.governed_scope),
      row.source_locators.map((locator) => [si(locator.basis_uri), si(locator.member_path), si(locator.member_sha256), locator.fragment === null ? null : si(locator.fragment)]),
      ss(row.derivation_evidence_refs),
    ]),
    r: program.source_bindings.map((row) => [si(row.member_path), si(row.member_sha256), si(row.disposition), row.model_refs.map(ii), row.residual_refs.map(ii), si(row.reason_code)]),
  };
}

function tuple(value: unknown, length: number, path: string): readonly unknown[] {
  if (!Array.isArray(value) || value.length !== length) fail(path, `must be one ${length}-field tuple`);
  return value;
}

function indexedString(value: unknown, table: readonly string[], path: string): string {
  if (!Number.isSafeInteger(value) || (value as number) < 0 || (value as number) >= table.length) fail(path, "is outside its table");
  return table[value as number]!;
}

function indexedIdentity(value: unknown, table: readonly string[], path: string, nullable = false): string | null {
  if (nullable && value === null) return null;
  return indexedString(value, table, path);
}

function indexedStrings(value: unknown, table: readonly string[], path: string): readonly string[] {
  if (!Array.isArray(value)) fail(path, "must be an index array");
  return value.map((member, index) => indexedString(member, table, `${path}[${index}]`));
}

function tupleRows(value: unknown, length: number, path: string): readonly (readonly unknown[])[] {
  if (!Array.isArray(value)) fail(path, "must be an array");
  return value.map((row, index) => tuple(row, length, `${path}[${index}]`));
}

function profileTupleLength(profile: SelectedAxiomIndexProfile, name: string): number {
  const schema = profile.configuration.tuple_schemas[name];
  if (schema === undefined || schema.fields.length !== schema.types.length) fail(`profile.configuration.tuple_schemas.${name}`, "does not define one complete tuple schema");
  return schema.fields.length;
}

export function recordProvenanceForModelRecord(program: AcceptedAxiomaticProgram, modelRecordRef: string): AxiomRecordProvenance | undefined {
  return program.record_provenance.find((binding) => binding.model_record_ref === modelRecordRef);
}

export function modelRecordRefsForSourceKey(program: AcceptedAxiomaticProgram, sourceKey: string): readonly string[] {
  return program.record_provenance
    .filter((binding) => binding.semantic_address.source_key === sourceKey)
    .map((binding) => binding.model_record_ref)
    .sort(compareUnicodeCodeUnits);
}

function decodeAxiomIndexConfigForProfile(value: unknown, targetSignatureBytes: Uint8Array, sourceManifestBytes: Uint8Array, profile: SelectedAxiomIndexProfile): AcceptedAxiomaticProgram {
  requireExact(value, profile.configuration.exact_keys, "config");
  if (value.k !== profile.configuration.kind || value.v !== profile.configuration.version) fail("config", "has the wrong profile-bound kind or version");
  if (canonicalJson(value.z as JsonValue) !== canonicalJson(encodingLegend(profile) as unknown as JsonValue)) fail("config.z", "does not equal the selected profile encoding legend");
  if (!Array.isArray(value.m) || value.m.length !== profileTupleLength(profile, "m")) fail("config.m", "does not satisfy the selected metadata tuple schema");
  const metadata = value.m.map((entry, index) => requireString(entry, `config.m[${index}]`));
  const strings = requireStrings(value.s, "config.s");
  const identities = requireStrings(value.i, "config.i", false);
  requireExact(value.b, profile.configuration.basis_schema.exact_fields, "config.b");
  const basis = {
    corpus: requireCoordinate(value.b.corpus, "config.b.corpus"),
    calculus: requireCoordinate(value.b.calculus, "config.b.calculus"),
    subject_basis: requireCoordinate(value.b.subject_basis, "config.b.subject_basis"),
    target_profile: requireCoordinate(value.b.target_profile, "config.b.target_profile"),
    interpretation_contract: requireCoordinate(value.b.interpretation_contract, "config.b.interpretation_contract"),
    semantic_compilation_candidate: requireCoordinate(value.b.semantic_compilation_candidate, "config.b.semantic_compilation_candidate"),
    candidate_structure_result: requireCoordinate(value.b.candidate_structure_result, "config.b.candidate_structure_result"),
  };
  const O = tupleRows(value.o, profileTupleLength(profile, "o"), "config.o").map((row, index): AxiomSemanticObject => ({
    id: indexedIdentity(row[0], identities, `config.o[${index}][0]`)! ,
    sort: indexedString(row[1], strings, `config.o[${index}][1]`),
    context: indexedIdentity(row[2], identities, `config.o[${index}][2]`)!,
    owner: indexedIdentity(row[3], identities, `config.o[${index}][3]`)!,
    scope: indexedString(row[4], strings, `config.o[${index}][4]`),
    basis: indexedIdentity(row[5], identities, `config.o[${index}][5]`)!,
    value: indexedString(row[6], strings, `config.o[${index}][6]`),
  }));
  const E = tupleRows(value.e, profileTupleLength(profile, "e"), "config.e").map((row, index): AxiomTypedRelation => ({
    id: indexedIdentity(row[0], identities, `config.e[${index}][0]`)!,
    kind: indexedString(row[1], strings, `config.e[${index}][1]`),
    source: indexedIdentity(row[2], identities, `config.e[${index}][2]`)!,
    target: indexedIdentity(row[3], identities, `config.e[${index}][3]`)!,
    context: indexedIdentity(row[4], identities, `config.e[${index}][4]`)!,
    owner: indexedIdentity(row[5], identities, `config.e[${index}][5]`)!,
    scope: indexedString(row[6], strings, `config.e[${index}][6]`),
    basis: indexedIdentity(row[7], identities, `config.e[${index}][7]`)!,
    qualifiers: indexedStrings(row[8], strings, `config.e[${index}][8]`),
  }));
  const C = tupleRows(value.c, profileTupleLength(profile, "c"), "config.c").map((row, index): AxiomConstraint => ({
    id: indexedIdentity(row[0], identities, `config.c[${index}][0]`)!,
    kind: indexedString(row[1], strings, `config.c[${index}][1]`),
    applies_to: indexedIdentity(row[2], identities, `config.c[${index}][2]`)!,
    predicate: indexedString(row[3], strings, `config.c[${index}][3]`),
    context: indexedIdentity(row[4], identities, `config.c[${index}][4]`)!,
    owner: indexedIdentity(row[5], identities, `config.c[${index}][5]`)!,
    scope: indexedString(row[6], strings, `config.c[${index}][6]`),
    basis: indexedIdentity(row[7], identities, `config.c[${index}][7]`)!,
    judgment_kind: indexedString(row[8], strings, `config.c[${index}][8]`),
    latitude_ref: indexedIdentity(row[9], identities, `config.c[${index}][9]`, true),
    refusal: indexedString(row[10], strings, `config.c[${index}][10]`),
  }));
  const L = tupleRows(value.l, profileTupleLength(profile, "l"), "config.l").map((row, index): AxiomLatitude => ({
    id: indexedIdentity(row[0], identities, `config.l[${index}][0]`)!,
    applies_to: indexedIdentity(row[1], identities, `config.l[${index}][1]`)!,
    allowed_variation: indexedStrings(row[2], strings, `config.l[${index}][2]`),
    forbidden_variation: indexedStrings(row[3], strings, `config.l[${index}][3]`),
    context: indexedIdentity(row[4], identities, `config.l[${index}][4]`)!,
    owner: indexedIdentity(row[5], identities, `config.l[${index}][5]`)!,
    scope: indexedString(row[6], strings, `config.l[${index}][6]`),
    basis: indexedIdentity(row[7], identities, `config.l[${index}][7]`)!,
    invalidation: indexedString(row[8], strings, `config.l[${index}][8]`),
  }));
  const X = tupleRows(value.x, profileTupleLength(profile, "x"), "config.x").map((row, index): AxiomResidual => ({
    id: indexedIdentity(row[0], identities, `config.x[${index}][0]`)!,
    subject: indexedIdentity(row[1], identities, `config.x[${index}][1]`)!,
    kind: indexedString(row[2], strings, `config.x[${index}][2]`),
    uncertainty: indexedString(row[3], strings, `config.x[${index}][3]`),
    consequence: indexedString(row[4], strings, `config.x[${index}][4]`),
    context: indexedIdentity(row[5], identities, `config.x[${index}][5]`)!,
    owner: indexedIdentity(row[6], identities, `config.x[${index}][6]`)!,
    scope: indexedString(row[7], strings, `config.x[${index}][7]`),
    basis: indexedIdentity(row[8], identities, `config.x[${index}][8]`)!,
    re_entry: indexedString(row[9], strings, `config.x[${index}][9]`),
    invalidation: indexedString(row[10], strings, `config.x[${index}][10]`),
  }));
  const V = tupleRows(value.V, profileTupleLength(profile, "V"), "config.V").map((row, index): AxiomTraversal => ({
    id: indexedIdentity(row[0], identities, `config.V[${index}][0]`)!,
    domain: indexedIdentity(row[1], identities, `config.V[${index}][1]`)!,
    codomain: indexedIdentity(row[2], identities, `config.V[${index}][2]`)!,
    context: indexedIdentity(row[3], identities, `config.V[${index}][3]`)!,
    owner: indexedIdentity(row[4], identities, `config.V[${index}][4]`)!,
    scope: indexedString(row[5], strings, `config.V[${index}][5]`),
    basis: indexedIdentity(row[6], identities, `config.V[${index}][6]`)!,
    preconditions: indexedStrings(row[7], strings, `config.V[${index}][7]`),
    postconditions: indexedStrings(row[8], strings, `config.V[${index}][8]`),
    authority: indexedIdentity(row[9], identities, `config.V[${index}][9]`)!,
    evidence: indexedStrings(row[10], identities, `config.V[${index}][10]`),
    provenance: indexedStrings(row[11], identities, `config.V[${index}][11]`),
    stop_states: indexedStrings(row[12], strings, `config.V[${index}][12]`),
  }));
  const T = tupleRows(value.T, profileTupleLength(profile, "T"), "config.T").map((row, index): AxiomTransformation => ({
    id: indexedIdentity(row[0], identities, `config.T[${index}][0]`)!,
    traversal: indexedIdentity(row[1], identities, `config.T[${index}][1]`)!,
    domain_model: indexedIdentity(row[2], identities, `config.T[${index}][2]`)!,
    codomain_model: indexedIdentity(row[3], identities, `config.T[${index}][3]`)!,
    context: indexedIdentity(row[4], identities, `config.T[${index}][4]`)!,
    owner: indexedIdentity(row[5], identities, `config.T[${index}][5]`)!,
    scope: indexedString(row[6], strings, `config.T[${index}][6]`),
    basis: indexedIdentity(row[7], identities, `config.T[${index}][7]`)!,
    operation_authority: indexedIdentity(row[8], identities, `config.T[${index}][8]`)!,
    preconditions: indexedStrings(row[9], strings, `config.T[${index}][9]`),
    preservation_relation: indexedIdentity(row[10], identities, `config.T[${index}][10]`)!,
    preserved: indexedStrings(row[11], identities, `config.T[${index}][11]`),
    introduced: indexedStrings(row[12], identities, `config.T[${index}][12]`),
    removed: indexedStrings(row[13], identities, `config.T[${index}][13]`),
    external_preserved: indexedStrings(row[14], identities, `config.T[${index}][14]`),
    external_introduced: indexedStrings(row[15], identities, `config.T[${index}][15]`),
    external_removed: indexedStrings(row[16], identities, `config.T[${index}][16]`),
    external_resolution_witnesses: requireJsonSet(row[17], `config.T[${index}][17]`).map((witness, witnessIndex) => validateExternalResolutionWitness(witness, `config.T[${index}][17][${witnessIndex}]`)),
    residuals: indexedStrings(row[18], identities, `config.T[${index}][18]`),
    evidence: indexedStrings(row[19], identities, `config.T[${index}][19]`),
    provenance: indexedStrings(row[20], identities, `config.T[${index}][20]`),
    stop_states: indexedStrings(row[21], strings, `config.T[${index}][21]`),
    invalidation: indexedString(row[22], strings, `config.T[${index}][22]`),
    re_entry: indexedString(row[23], strings, `config.T[${index}][23]`),
  }));
  const J = tupleRows(value.J, profileTupleLength(profile, "J"), "config.J").map((row, index): AxiomJudgment => ({
    id: indexedIdentity(row[0], identities, `config.J[${index}][0]`)!,
    kind: indexedString(row[1], strings, `config.J[${index}][1]`),
    subject: indexedIdentity(row[2], identities, `config.J[${index}][2]`)!,
    subject_digest: indexedString(row[3], strings, `config.J[${index}][3]`),
    context: indexedIdentity(row[4], identities, `config.J[${index}][4]`)!,
    owner: indexedIdentity(row[5], identities, `config.J[${index}][5]`)!,
    scope: indexedString(row[6], strings, `config.J[${index}][6]`),
    basis: indexedIdentity(row[7], identities, `config.J[${index}][7]`)!,
    evaluator: indexedIdentity(row[8], identities, `config.J[${index}][8]`)!,
    authority: indexedIdentity(row[9], identities, `config.J[${index}][9]`)!,
    decision: indexedString(row[10], strings, `config.J[${index}][10]`),
    evidence: indexedStrings(row[11], identities, `config.J[${index}][11]`),
    provenance: indexedStrings(row[12], identities, `config.J[${index}][12]`),
    decided_at: indexedString(row[13], strings, `config.J[${index}][13]`),
  }));
  const ResolutionSet_M = tupleRows(value.q, profileTupleLength(profile, "q"), "config.q").map((row, index): AxiomExternalResolution => ({
    external_identity: indexedIdentity(row[0], identities, `config.q[${index}][0]`)!,
    reference_domain: indexedString(row[1], strings, `config.q[${index}][1]`),
    external_target_kind: indexedString(row[2], strings, `config.q[${index}][2]`),
    resolved_target_identity: indexedString(row[3], strings, `config.q[${index}][3]`),
    basis_relation: indexedString(row[4], strings, `config.q[${index}][4]`),
    resolution_basis: indexedString(row[5], strings, `config.q[${index}][5]`),
    evidence_identity: indexedString(row[6], strings, `config.q[${index}][6]`),
  }));
  const record_provenance = tupleRows(value.p, profileTupleLength(profile, "p"), "config.p").map((row, index): AxiomRecordProvenance => ({
    model_record_ref: indexedIdentity(row[0], identities, `config.p[${index}][0]`)!,
    provenance_kind: indexedString(row[1], strings, `config.p[${index}][1]`) as AxiomRecordProvenance["provenance_kind"],
    semantic_address: {
      source_key: indexedString(row[2], strings, `config.p[${index}][2]`),
      term: indexedString(row[3], strings, `config.p[${index}][3]`),
      bounded_context: indexedString(row[4], strings, `config.p[${index}][4]`),
      owning_authority: indexedString(row[5], strings, `config.p[${index}][5]`),
      selected_basis: indexedString(row[6], strings, `config.p[${index}][6]`),
      governed_scope: indexedString(row[7], strings, `config.p[${index}][7]`),
    },
    source_locators: tupleRows(row[8], profileTupleLength(profile, "source_locator"), `config.p[${index}][8]`).map((locator, locatorIndex): AxiomSourceLocator => ({
      basis_uri: indexedString(locator[0], strings, `config.p[${index}][8][${locatorIndex}][0]`),
      member_path: indexedString(locator[1], strings, `config.p[${index}][8][${locatorIndex}][1]`),
      member_sha256: indexedString(locator[2], strings, `config.p[${index}][8][${locatorIndex}][2]`),
      fragment: locator[3] === null ? null : indexedString(locator[3], strings, `config.p[${index}][8][${locatorIndex}][3]`),
    })),
    derivation_evidence_refs: indexedStrings(row[9], strings, `config.p[${index}][9]`),
  }));
  const source_bindings = tupleRows(value.r, profileTupleLength(profile, "r"), "config.r").map((row, index): AxiomSourceBinding => ({
    member_path: indexedString(row[0], strings, `config.r[${index}][0]`),
    member_sha256: indexedString(row[1], strings, `config.r[${index}][1]`),
    disposition: indexedString(row[2], strings, `config.r[${index}][2]`) as AxiomSourceBinding["disposition"],
    model_refs: indexedStrings(row[3], identities, `config.r[${index}][3]`),
    residual_refs: indexedStrings(row[4], identities, `config.r[${index}][4]`),
    reason_code: indexedString(row[5], strings, `config.r[${index}][5]`) as AxiomSourceBinding["reason_code"],
  }));
  const program: AcceptedAxiomaticProgram = {
    kind: "axiom-indexer.axiomatic-program",
    schema_version: 2,
    model_content_identity: sha256Canonical(externalModelValue({ b: metadata[6]!, I: identities, O, E, C, L, X, V, T, J, ResolutionSet_M }) as unknown as JsonValue),
    basis,
    model: { b: metadata[6]!, I: identities, O, E, C, L, X, V, T, J, ResolutionSet_M },
    record_provenance,
    source_bindings,
  };
  const subjectMembers = validateSubjectManifest(sourceManifestBytes);
  const signature = validateTargetSignature(targetSignatureBytes, basis.target_profile);
  const checked = validateProgram(program as unknown as Readonly<Record<string, unknown>>, signature, subjectMembers);
  const bytes = artifactBytes(checked as unknown as JsonValue);
  if (contentIdentity(PROGRAM_PREFIX, bytes) !== metadata[2] || sha256Bytes(bytes) !== metadata[3]) fail("config.m", "does not reproduce the accepted program");
  const interpretedModel = interpretedModelCoordinate(checked, metadata[4]!, requireSha256(metadata[5], "config.m[5]"));
  if (interpretedModel.identity !== metadata[0] || interpretedModel.digest !== metadata[1]) fail("config.m", "does not reproduce the interpreted-model coordinate");
  return checked;
}

export function decodeAxiomIndexConfig(
  value: unknown,
  targetSignatureBytes: Uint8Array,
  sourceManifestBytes: Uint8Array,
  profileBytes: Uint8Array,
): AcceptedAxiomaticProgram {
  const profile = validateProfile(profileBytes);
  return decodeAxiomIndexConfigForProfile(value, targetSignatureBytes, sourceManifestBytes, profile.definition);
}

export function constructAxiomIndexGtlCandidate(input: AxiomIndexGtlInput): AxiomIndexGtlCandidate {
  const selectedProfile = validateProfile(input.profile_bytes);
  const candidateValue = parseCanonicalArtifact(input.semantic_compilation_candidate_bytes, "semantic_compilation_candidate");
  const programValue = parseCanonicalArtifact(input.accepted_program_bytes, "accepted_program");
  const structureValue = parseCanonicalArtifact(input.candidate_structure_result_bytes, "candidate_structure_result");
  const ledgerValue = parseCanonicalRecord(input.selection_ledger_bytes, "selection_ledger");
  const judgmentValue = parseCanonicalRecord(input.semantic_judgment_bytes, "semantic_judgment");
  const subjectMembers = validateSubjectManifest(input.source_manifest_bytes);
  const targetProfile = {
    identity: requireIdentity(candidateValue.signature_identity, "semantic_compilation_candidate.signature_identity"),
    sha256: requireSha256(candidateValue.signature_sha256, "semantic_compilation_candidate.signature_sha256"),
  };
  const signature = validateTargetSignature(input.target_signature_bytes, targetProfile);
  const compilerProvenance = validateCompilerProvenanceBundle(
    input.compiler_provenance_bundle_bytes,
    input.compiler_provenance_member_bytes,
  );
  const candidate = validateCompilationCandidate(
    candidateValue,
    input.semantic_compilation_proposal_bytes,
    compilerProvenance,
    signature,
    subjectMembers,
    input.interpretation_contract_bytes,
    input.frame_basis_bytes,
  );
  const structureGrant = validateStructureGrant(input.structure_grant_bytes, input.structure_grant_source_bytes, candidate);
  const structure = validateStructure(structureValue, candidate, structureGrant);
  const program = validateProgram(programValue, signature, subjectMembers);
  const programDigest = sha256Bytes(input.accepted_program_bytes);
  const programIdentity = contentIdentity(PROGRAM_PREFIX, input.accepted_program_bytes);
  for (const [actual, expected, path] of [
    [program.basis.corpus, candidate.corpus, "accepted_program.basis.corpus"],
    [program.basis.calculus, candidate.calculus, "accepted_program.basis.calculus"],
    [program.basis.subject_basis, candidate.subjectBasis, "accepted_program.basis.subject_basis"],
    [program.basis.target_profile, candidate.targetProfile, "accepted_program.basis.target_profile"],
    [program.basis.interpretation_contract, candidate.interpretationContract, "accepted_program.basis.interpretation_contract"],
  ] as const) if (canonicalJson(actual as unknown as JsonValue) !== canonicalJson(expected as unknown as JsonValue)) fail(path, "does not preserve the candidate basis");
  if (program.basis.semantic_compilation_candidate.identity !== candidate.identity || program.basis.semantic_compilation_candidate.sha256 !== candidate.digest) fail("accepted_program.basis.semantic_compilation_candidate", "does not bind the unchanged semantic-compilation candidate");
  if (program.basis.candidate_structure_result.identity !== structure.identity || program.basis.candidate_structure_result.sha256 !== structure.digest) fail("accepted_program.basis.candidate_structure_result", "does not bind the unchanged candidate-structure result");
  const semanticGrant = validateGrant(input.semantic_grant_bytes, input.semantic_grant_source_bytes, "semantic_grant");
  const ledger = validateLedger(ledgerValue, candidate, structure, program, semanticGrant);
  const ledgerDigest = sha256Bytes(input.selection_ledger_bytes);
  const ledgerIdentity = `${LEDGER_PREFIX}${ledgerDigest.slice("sha256:".length)}`;
  const judgment = validateJudgment(judgmentValue, program, programIdentity, ledger, ledgerIdentity, ledgerDigest, structure, semanticGrant);
  const judgmentDigest = sha256Bytes(input.semantic_judgment_bytes);
  const judgmentIdentity = contentIdentity(JUDGMENT_PREFIX, input.semantic_judgment_bytes);
  const profile = selectedProfile.definition;
  const publisher = validatePublisher(input, selectedProfile);
  const config = encodeProgram(program, programIdentity, programDigest, ledgerIdentity, ledgerDigest, judgment.interpretedModel, profile);
  const coordinate = {
    interpreted_model_identity: judgment.interpretedModel.identity,
    interpreted_model_sha256: judgment.interpretedModel.digest,
    accepted_program_identity: programIdentity,
    accepted_program_sha256: programDigest,
    selection_ledger_identity: ledgerIdentity,
    selection_ledger_sha256: ledgerDigest,
    carrier_basis_identity: selectedProfile.carrier_basis_identity,
    profile_identity: profile.identity,
    profile_sha256: selectedProfile.digest,
    publisher: input.publisher,
    config_sha256: sha256Canonical(config),
  };
  const moduleRef = `urn:stdo-index:gtl-module:sha256:${sha256Canonical(coordinate as unknown as JsonValue).slice("sha256:".length)}`;
  const carrierContract = profile.publication_contract;
  const recordContract = carrierContract.record_contract;
  const contract = contractDeclaration({
    contractRef: recordContract.contract_ref,
    contractVersion: recordContract.contract_version,
    contractKind: recordContract.contract_kind,
    valueKind: recordContract.value_kind,
  });
  const contributionContract = carrierContract.contribution;
  const provenanceRefs = contributionContract.provenance_refs.map((reference) => {
    if (reference === "publisher.artifact_digest") return input.publisher.artifact_digest;
    if (reference === "publisher.product_manifest_digest") return input.publisher.product_manifest_digest;
    return fail("profile.publication_contract.contribution.provenance_refs", `contains an unresolved binding ${reference}`);
  });
  const contribution = catalogContribution({
    handle: contributionContract.handle,
    kind: contributionContract.kind,
    declarationOrContractRef: contributionContract.declaration_or_contract_ref,
    owningProductId: input.publisher.owning_product_id,
    programMembershipRefs: contributionContract.program_membership_refs,
    readinessPrerequisiteRefs: contributionContract.readiness_prerequisite_refs,
    compatibilityRefs: contributionContract.compatibility_refs,
    provenanceRefs,
  });
  const ruleContract = carrierContract.rule;
  const rule = ruleDeclaration({ name: ruleContract.name, kind: ruleContract.kind, config: config as RuleDeclaration["config"], tags: ruleContract.tags });
  const semanticsContract = carrierContract.product_semantics_binding;
  const moduleContract = carrierContract.module_publication;
  const publication = modulePublication({
    kind: moduleContract.kind, moduleRef, moduleVersion: moduleContract.module_version,
    owningProductId: input.publisher.owning_product_id,
    artifactDigest: input.publisher.artifact_digest as `sha256:${string}`,
    productContentDigest: input.publisher.product_content_digest as `sha256:${string}`,
    productManifestDigest: input.publisher.product_manifest_digest as `sha256:${string}`,
    descriptorRef: input.publisher.descriptor_ref,
    contributionManifestRef: input.publisher.contribution_manifest_ref,
    productSemanticsBinding: productSemanticsBinding({
      kind: semanticsContract.kind,
      bindingRef: semanticsContract.binding_ref,
      packageName: input.publisher.package_name,
      packageVersion: input.publisher.package_version,
      modulePath: input.publisher.module_path,
      namedSymbol: input.publisher.named_symbol,
    }),
    contracts: [contract], evaluators: [], rules: [rule], implementationBindings: [],
    closureContracts: [], programs: [], graphFunctions: [], contributions: [contribution],
  });
  requireExact(publication as unknown as Readonly<Record<string, unknown>>, moduleContract.exact_fields, "publication");
  requireExact(publication.productSemanticsBinding as unknown as Readonly<Record<string, unknown>>, semanticsContract.exact_fields, "publication.productSemanticsBinding");
  requireExact(contract as unknown as Readonly<Record<string, unknown>>, recordContract.exact_fields, "publication.contracts[0]");
  requireExact(rule as unknown as Readonly<Record<string, unknown>>, ruleContract.exact_fields, "publication.rules[0]");
  requireExact(contribution as unknown as Readonly<Record<string, unknown>>, contributionContract.exact_fields, "publication.contributions[0]");
  const publicationRecord = publication as unknown as Readonly<Record<string, unknown>>;
  for (const [field, cardinality] of Object.entries(moduleContract.inventory_cardinality)) {
    const inventory = publicationRecord[field];
    if (!Array.isArray(inventory) || inventory.length !== cardinality) fail(`publication.${field}`, `must contain exactly ${cardinality} members under the selected profile`);
  }
  const admitted = rawAdmitValue<ModulePublication>(publication, "module_publication", moduleContract.raw_admission_contract_ref);
  if (admitted.kind !== "raw_admitted_value") fail("gtl", `raw admission refused: ${admitted.message}`);
  const contributionAdmission = rawAdmitValue<CatalogContribution>(contribution, "catalog_contribution", contributionContract.raw_admission_contract_ref);
  if (contributionAdmission.kind !== "raw_admitted_value") fail("gtl", `contribution admission refused: ${contributionAdmission.message}`);
  const validation = validatePublication(admitted, [contributionAdmission]);
  if (validation.kind !== "publication_validation" || validation.disposition !== "valid") fail("gtl", "frozen publication validation refused");
  const decoded = decodeAxiomIndexConfigForProfile(config, input.target_signature_bytes, input.source_manifest_bytes, profile);
  if (canonicalJson(decoded as unknown as JsonValue) !== canonicalJson(program as unknown as JsonValue)) fail("gtl", "profile round trip changed the accepted program");
  const canonicalBytes = artifactBytes(admitted.value as unknown as JsonValue);
  return {
    canonical_bytes: canonicalBytes,
    publication: admitted.value,
    receipt: {
      kind: "stdo-index.gtl-carrier-candidate",
      schema_version: 1,
      machine_path: AXIOM_INDEX_MACHINE,
      interpreted_model_identity: judgment.interpretedModel.identity,
      interpreted_model_sha256: judgment.interpretedModel.digest,
      accepted_program_identity: programIdentity,
      accepted_program_sha256: programDigest,
      selection_ledger_identity: ledgerIdentity,
      selection_ledger_sha256: ledgerDigest,
      semantic_judgment_identity: judgmentIdentity,
      semantic_judgment_sha256: judgmentDigest,
      profile_identity: profile.identity,
      profile_sha256: selectedProfile.digest,
      publisher_product_identity: publisher.identity,
      publisher_manifest_sha256: publisher.digest,
      carrier_sha256: sha256Bytes(canonicalBytes),
      frozen_gtl_validation: "valid",
      profile_round_trip: "valid",
      carrier_admission: "not_evaluated",
    },
  };
}
