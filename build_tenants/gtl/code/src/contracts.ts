import type { JsonValue } from "./canonical.js";

export const PROFILE_IDENTITY =
  "urn:stdo-representation:gtl-profile:stdo-gtl:0.7.0";
export const BUILD_TENANT_IDENTITY =
  "urn:stdo-representation:build-tenant:gtl";
export const CARRIER_BASIS_IDENTITY =
  "urn:stdo-representation:carrier-basis:gtl:sha256:b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703";
export const GTL_MODULE_VERSION = "5.0.0" as const;
export const RECORD_CONTRACT_REF =
  "urn:stdo-representation:gtl-contract:programmatic-semantic-index:1";
export const FRAME_ADMITTING_AUTHORITIES = Object.freeze([
  "./specification/GOALS.md",
  "./specification/PRODUCT.md#product-authority",
  "./specification/requirements/REQ-P-BASIS-AND-IDENTITY.md",
  "./specification/requirements/REQ-P-COMPRESSION-VERIFICATION.md",
  "./specification/requirements/REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
  "./specification/requirements/REQ-P-FP-CONSUMPTION.md",
  "./specification/requirements/REQ-P-REPRESENTATION-ALGEBRA.md",
  "./specification/requirements/REQ-P-SELECTION-AND-ACCEPTANCE.md",
]);

export const ATOM_CLASSES = [
  "authority",
  "basis",
  "bounded_context",
  "capability",
  "clause",
  "concept",
  "design",
  "document",
  "evidence",
  "intent",
  "method",
  "product",
  "product_definition",
  "reference_frame",
  "relation_kind",
  "requirement",
  "role",
  "scope",
  "state",
  "term",
  "ticket",
] as const;

export const CONSTRAINT_CLASSES = [
  "admission_condition",
  "axiom",
  "guarantee",
  "invariant",
  "latitude",
  "obligation",
  "prohibition",
  "refusal",
] as const;

export const CROSS_CONTEXT_CLASSES = [
  "unchanged_import",
  "disambiguation",
  "directional_translation",
  "specialization",
  "authority_equivalence",
] as const;

export const LATITUDE_FUNCTIONS = [
  "urn:stdo:concept:graph-native-odd:f-p",
  "urn:stdo:concept:graph-native-odd:f-h",
] as const;

export type AtomClass = (typeof ATOM_CLASSES)[number];
export type ConstraintClass = (typeof CONSTRAINT_CLASSES)[number];
export type CrossContextClass = (typeof CROSS_CONTEXT_CLASSES)[number];
export type LatitudeFunction = (typeof LATITUDE_FUNCTIONS)[number];

export interface SelectedBasis {
  readonly release_uri: string;
  readonly installed_manifest_sha256: string;
}

export interface SemanticAddress {
  readonly source_key: string;
  readonly term: string;
  readonly bounded_context: string;
  readonly owning_authority: string;
  readonly selected_basis: SelectedBasis;
  readonly governed_scope: string;
}

export interface SourceLocator {
  readonly basis_uri: string;
  readonly member_path: string;
  readonly member_sha256: string;
  readonly fragment: string | null;
}

export interface SemanticAtom {
  readonly kind: "atom";
  readonly id: string;
  readonly atom_class: AtomClass;
  readonly label: string;
  readonly semantic_address: SemanticAddress;
  readonly source_locators: readonly SourceLocator[];
}

export interface CrossContext {
  readonly classification: CrossContextClass;
  readonly source_context_ref: string;
  readonly target_context_ref: string;
  readonly preserved_meaning_refs: readonly string[];
  readonly changed_meaning_refs: readonly string[];
  readonly refusal_refs: readonly string[];
  readonly inverse_ref: string | null;
  readonly invalidation_refs: readonly string[];
}

export interface SemanticEdge {
  readonly kind: "edge";
  readonly id: string;
  readonly semantic_address: SemanticAddress;
  readonly source_ref: string;
  readonly relation_kind_ref: string;
  readonly target_ref: string;
  readonly context_ref: string | null;
  readonly owner_ref: string | null;
  readonly scope_ref: string | null;
  readonly cross_context: CrossContext | null;
  readonly source_locators: readonly SourceLocator[];
}

export interface DeclaredLatitude {
  readonly function_ref: LatitudeFunction;
  readonly decision_owner_ref: string;
  readonly re_entry_ref: string;
}

export interface PassiveConstraint {
  readonly kind: "constraint";
  readonly id: string;
  readonly semantic_address: SemanticAddress;
  readonly constraint_class: ConstraintClass;
  readonly statement: string;
  readonly applies_to_refs: readonly string[];
  readonly context_ref: string | null;
  readonly owner_ref: string | null;
  readonly scope_ref: string | null;
  readonly declared_latitude: DeclaredLatitude | null;
  readonly source_locators: readonly SourceLocator[];
}

export type ProgramRecord = SemanticAtom | SemanticEdge | PassiveConstraint;

export interface SourceBasis {
  readonly release_uri: string;
  readonly installed_manifest_sha256: string;
  readonly standards_member_set_sha256: string;
}

export interface PublisherArtifactBasis {
  readonly owning_product_id: string;
  readonly artifact_digest: string;
  readonly product_content_digest: string;
  readonly product_manifest_digest: string;
  readonly descriptor_ref: string;
  readonly contribution_manifest_ref: string;
  readonly package_name: string;
  readonly package_version: string;
  readonly module_path: string;
  readonly named_symbol: string;
}

export interface GtlBuildPlan {
  readonly kind: "stdo-representation.gtl-build-plan";
  readonly schema_version: 1;
  readonly source_stdo: SourceBasis;
  readonly what_member_set_identity: string;
  readonly representation_profile_identity: string;
  readonly representation_profile_sha256: string;
  readonly frame_basis_identity: string;
  readonly frame_basis_sha256: string;
  readonly frame_admitting_authority_refs: readonly string[];
  readonly semantic_selection_ledger_identity: string;
  readonly semantic_selection_ledger_sha256: string;
  readonly profile_acceptance_identity: string;
  readonly frame_basis_acceptance_identity: string;
  readonly selection_acceptance_identity: string;
  readonly publisher: PublisherArtifactBasis;
  readonly records: readonly ProgramRecord[];
}

export interface AcceptedBuildEvidence {
  readonly source_manifest: unknown;
  readonly source_manifest_bytes: Uint8Array;
  readonly profile_bytes: Uint8Array;
  readonly frame_basis_bytes: Uint8Array;
  readonly semantic_selection_ledger: unknown;
  readonly semantic_selection_ledger_bytes: Uint8Array;
  readonly profile_acceptance: unknown;
  readonly profile_acceptance_bytes: Uint8Array;
  readonly frame_basis_acceptance: unknown;
  readonly frame_basis_acceptance_bytes: Uint8Array;
  readonly selection_acceptance: unknown;
  readonly selection_acceptance_bytes: Uint8Array;
  readonly publisher_manifest: unknown;
  readonly publisher_manifest_bytes: Uint8Array;
  readonly publisher_artifact_bytes: Uint8Array;
}

export interface CompactSemanticIndexConfig extends Readonly<Record<string, JsonValue>> {
  readonly k: "stdo.programmatic_semantic_index";
  readonly v: 1;
  readonly m: readonly string[];
  readonly l: Readonly<Record<string, JsonValue>>;
  readonly s: readonly string[];
  readonly i: readonly string[];
  readonly a: readonly JsonValue[];
  readonly e: readonly JsonValue[];
  readonly c: readonly JsonValue[];
}

export interface BuildReceipt {
  readonly kind: "stdo-representation.gtl-build-receipt";
  readonly schema_version: 1;
  readonly module_ref: string;
  readonly publication_digest: string;
  readonly raw_admission_ref: string;
  readonly validation_ref: string;
  readonly program_content_identity: string;
  readonly product_identity: string;
  readonly source_record_counts: Readonly<{
    atoms: number;
    edges: number;
    constraints: number;
  }>;
  readonly artifact_bytes: number;
}

export interface ConstructedSemanticIndex {
  readonly canonical_bytes: Uint8Array;
  readonly publication: Readonly<Record<string, JsonValue>>;
  readonly receipt: BuildReceipt;
}

export interface ProjectionCandidate {
  readonly kind: "stdo-representation.gtl-projection-candidate";
  readonly schema_version: 1;
  readonly assignment_identity: string;
  readonly parent_product_identity: string;
  readonly parent_program_content_identity: string;
  readonly included_identity_refs: readonly string[];
  readonly included_identity_set_sha256: string;
  readonly omitted_identity_refs: readonly string[];
  readonly omitted_identity_set_sha256: string;
  readonly projection_carrier_sha256: string;
  readonly canonical_bytes: Uint8Array;
}

export const STDO_GTL_PRODUCT_SEMANTICS = Object.freeze({
  kind: "stdo_gtl_product_semantics",
  schemaVersion: 1,
  profileIdentity: PROFILE_IDENTITY,
  recordContractRef: RECORD_CONTRACT_REF,
});
