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
  BUILD_TENANT_IDENTITY,
  CARRIER_BASIS_IDENTITY,
  GTL_MODULE_VERSION,
  PROFILE_IDENTITY,
  RECORD_CONTRACT_REF,
  type BuildReceipt,
  type AcceptedBuildEvidence,
  type ConstructedSemanticIndex,
  type GtlBuildPlan,
} from "./contracts.js";
import { canonicalJson, sha256Bytes, sha256Canonical, type JsonValue } from "./canonical.js";
import { encodeSemanticIndex } from "./encoding.js";
import { assertSelectedTenant, validateBuildPlan } from "./validation.js";
import { validateAcceptedBuildEvidence } from "./evidence.js";

const MODULE_CONTRACT_REF =
  "urn:abiogenesis:contract:gtl:module-publication:5.0.0";
const CONTRIBUTION_CONTRACT_REF =
  "urn:abiogenesis:contract:gtl:catalog-contribution:5.0.0";

export function constructStdoGtl(
  input: unknown,
  evidence: AcceptedBuildEvidence,
): ConstructedSemanticIndex {
  const plan = validateBuildPlan(input);
  assertSelectedTenant(plan);
  validateAcceptedBuildEvidence(plan, evidence);
  return constructValidatedStdoGtl(plan);
}

export function constructValidatedStdoGtl(
  plan: GtlBuildPlan,
): ConstructedSemanticIndex {
  const config = encodeSemanticIndex(plan);
  const moduleCoordinate = {
    source_stdo_uri: plan.source_stdo.release_uri,
    source_stdo_manifest_sha256: plan.source_stdo.installed_manifest_sha256,
    what_member_set_identity: plan.what_member_set_identity,
    build_tenant_identity: BUILD_TENANT_IDENTITY,
    carrier_basis_identity: CARRIER_BASIS_IDENTITY,
    representation_profile_identity: PROFILE_IDENTITY,
    representation_profile_sha256: plan.representation_profile_sha256,
    semantic_selection_ledger_identity: plan.semantic_selection_ledger_identity,
    semantic_index_config_sha256: sha256Canonical(config),
  };
  const moduleRef = `urn:stdo-representation:gtl-module:sha256:${sha256Canonical(
    moduleCoordinate as unknown as JsonValue,
  ).slice("sha256:".length)}`;
  const contract = contractDeclaration({
    contractRef: RECORD_CONTRACT_REF,
    contractVersion: GTL_MODULE_VERSION,
    contractKind: "input",
    valueKind: "stdo_programmatic_semantic_index_v1",
  });
  const contribution = catalogContribution({
    handle: "stdo.programmatic-semantic-index.v1",
    kind: "node_type",
    declarationOrContractRef: RECORD_CONTRACT_REF,
    owningProductId: plan.publisher.owning_product_id,
    programMembershipRefs: [],
    readinessPrerequisiteRefs: [],
    compatibilityRefs: [],
    provenanceRefs: [
      plan.publisher.artifact_digest,
      plan.publisher.product_manifest_digest,
    ],
  });
  const rule = ruleDeclaration({
    name: "stdo.programmatic-semantic-index.v1",
    kind: "stdo.programmatic_semantic_index",
    config: config as unknown as RuleDeclaration["config"],
    tags: [],
  });
  const publication = modulePublication({
    kind: "module_publication",
    moduleRef,
    moduleVersion: GTL_MODULE_VERSION,
    owningProductId: plan.publisher.owning_product_id,
    artifactDigest: plan.publisher.artifact_digest as `sha256:${string}`,
    productContentDigest: plan.publisher.product_content_digest as `sha256:${string}`,
    productManifestDigest: plan.publisher.product_manifest_digest as `sha256:${string}`,
    descriptorRef: plan.publisher.descriptor_ref,
    contributionManifestRef: plan.publisher.contribution_manifest_ref,
    productSemanticsBinding: productSemanticsBinding({
      kind: "product_semantics_binding",
      bindingRef: "urn:stdo-representation:product-semantics:gtl-programmatic-semantic-index:1",
      packageName: plan.publisher.package_name,
      packageVersion: plan.publisher.package_version,
      modulePath: plan.publisher.module_path,
      namedSymbol: plan.publisher.named_symbol,
    }),
    contracts: [contract],
    evaluators: [],
    rules: [rule],
    implementationBindings: [],
    closureContracts: [],
    programs: [],
    graphFunctions: [],
    contributions: [contribution],
  });
  const publicationAdmission = rawAdmitValue<ModulePublication>(
    publication,
    "module_publication",
    MODULE_CONTRACT_REF,
  );
  if (publicationAdmission.kind !== "raw_admitted_value") {
    throw new TypeError(`frozen GTL raw admission refused: ${publicationAdmission.message}`);
  }
  const contributionAdmission = rawAdmitValue<CatalogContribution>(
    contribution,
    "catalog_contribution",
    CONTRIBUTION_CONTRACT_REF,
  );
  if (contributionAdmission.kind !== "raw_admitted_value") {
    throw new TypeError(`frozen GTL contribution admission refused: ${contributionAdmission.message}`);
  }
  const validation = validatePublication(publicationAdmission, [contributionAdmission]);
  if (validation.kind !== "publication_validation" || validation.disposition !== "valid") {
    throw new TypeError(`frozen GTL publication validation refused: ${canonicalJson(validation as unknown as JsonValue)}`);
  }
  const typedBytes = canonicalJson(publication as unknown as JsonValue);
  const rawBytes = canonicalJson(publicationAdmission.value as unknown as JsonValue);
  if (typedBytes !== rawBytes) {
    throw new TypeError("typed declaration and raw-admitted GTL carrier differ");
  }
  const canonicalBytes = new TextEncoder().encode(`${rawBytes}\n`);
  const programContentIdentity = sha256Bytes(canonicalBytes);
  const productCoordinate = {
    source_stdo_uri: plan.source_stdo.release_uri,
    source_stdo_manifest_sha256: plan.source_stdo.installed_manifest_sha256,
    what_member_set_identity: plan.what_member_set_identity,
    build_tenant_identity: BUILD_TENANT_IDENTITY,
    carrier_basis_identity: CARRIER_BASIS_IDENTITY,
    representation_profile_identity: PROFILE_IDENTITY,
    representation_profile_sha256: plan.representation_profile_sha256,
    program_content_identity: programContentIdentity,
  };
  const productIdentity = `urn:stdo-representation:product:sha256:${sha256Canonical(
    productCoordinate as unknown as JsonValue,
  ).slice("sha256:".length)}`;
  const receipt: BuildReceipt = {
    kind: "stdo-representation.gtl-build-receipt",
    schema_version: 1,
    module_ref: moduleRef,
    publication_digest: publicationAdmission.subjectDigest,
    raw_admission_ref: publicationAdmission.admissionRef,
    validation_ref: validation.validationRef,
    program_content_identity: programContentIdentity,
    product_identity: productIdentity,
    source_record_counts: {
      atoms: plan.records.filter((record) => record.kind === "atom").length,
      edges: plan.records.filter((record) => record.kind === "edge").length,
      constraints: plan.records.filter((record) => record.kind === "constraint").length,
    },
    artifact_bytes: canonicalBytes.byteLength,
  };
  return {
    canonical_bytes: canonicalBytes,
    publication: publicationAdmission.value as unknown as Readonly<Record<string, JsonValue>>,
    receipt,
  };
}
