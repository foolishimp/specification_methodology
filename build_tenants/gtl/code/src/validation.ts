import {
  ATOM_CLASSES,
  BUILD_TENANT_IDENTITY,
  CARRIER_BASIS_IDENTITY,
  CONSTRAINT_CLASSES,
  CROSS_CONTEXT_CLASSES,
  FRAME_ADMITTING_AUTHORITIES,
  LATITUDE_FUNCTIONS,
  PROFILE_IDENTITY,
  type CrossContext,
  type DeclaredLatitude,
  type GtlBuildPlan,
  type PassiveConstraint,
  type ProgramRecord,
  type SemanticAddress,
  type SemanticAtom,
  type SemanticEdge,
  type SourceLocator,
} from "./contracts.js";
import {
  canonicalJson,
  compareUnicodeCodeUnits,
  exactKeys,
  isRecord,
  sha256Canonical,
  type JsonValue,
} from "./canonical.js";

const SHA256 = /^sha256:[0-9a-f]{64}$/u;
const IDENTITY = /^urn:stdo-representation:(atom|edge|constraint):sha256:[0-9a-f]{64}$/u;
const LEDGER_IDENTITY =
  /^urn:stdo-representation:semantic-selection-ledger:sha256:[0-9a-f]{64}$/u;
const ACCEPTANCE_IDENTITY =
  /^urn:stdo-representation:authority-acceptance:sha256:[0-9a-f]{64}$/u;

function fail(path: string, message: string): never {
  throw new TypeError(`${path}: ${message}`);
}

function requireString(value: unknown, path: string): asserts value is string {
  if (typeof value !== "string" || value.length === 0) {
    fail(path, "must be one non-empty string");
  }
}

function requireUri(value: unknown, path: string): asserts value is string {
  requireString(value, path);
  try {
    const parsed = new URL(value);
    if (parsed.protocol.length === 0) fail(path, "must be one absolute URI");
  } catch {
    fail(path, "must be one absolute URI");
  }
}

function requireSha(value: unknown, path: string): asserts value is string {
  if (typeof value !== "string" || !SHA256.test(value)) {
    fail(path, "must be sha256 followed by 64 lowercase hexadecimal characters");
  }
}

function requireIdentity(value: unknown, path: string): asserts value is string {
  if (typeof value !== "string" || !IDENTITY.test(value)) {
    fail(path, "must be one STDO Representation record identity");
  }
}

function requireExact(
  value: unknown,
  keys: readonly string[],
  path: string,
): asserts value is Readonly<Record<string, unknown>> {
  if (!isRecord(value) || !exactKeys(value, keys)) {
    fail(path, `must contain exactly ${keys.join(", ")}`);
  }
}

function requireStringSet(values: unknown, path: string): asserts values is readonly string[] {
  if (!Array.isArray(values)) fail(path, "must be one array");
  values.forEach((value, index) => requireIdentity(value, `${path}[${index}]`));
  const sorted = [...values].sort(compareUnicodeCodeUnits);
  if (new Set(values).size !== values.length || canonicalJson(values as JsonValue) !== canonicalJson(sorted)) {
    fail(path, "must be duplicate-free and sorted by unsigned UTF-16 code units");
  }
}

function validateAddress(value: unknown, plan: GtlBuildPlan, path: string): SemanticAddress {
  requireExact(
    value,
    [
      "source_key",
      "term",
      "bounded_context",
      "owning_authority",
      "selected_basis",
      "governed_scope",
    ],
    path,
  );
  requireUri(value.source_key, `${path}.source_key`);
  requireString(value.term, `${path}.term`);
  requireUri(value.bounded_context, `${path}.bounded_context`);
  requireUri(value.owning_authority, `${path}.owning_authority`);
  requireUri(value.governed_scope, `${path}.governed_scope`);
  requireExact(
    value.selected_basis,
    ["release_uri", "installed_manifest_sha256"],
    `${path}.selected_basis`,
  );
  requireUri(value.selected_basis.release_uri, `${path}.selected_basis.release_uri`);
  requireSha(
    value.selected_basis.installed_manifest_sha256,
    `${path}.selected_basis.installed_manifest_sha256`,
  );
  if (
    value.selected_basis.release_uri !== plan.source_stdo.release_uri ||
    value.selected_basis.installed_manifest_sha256 !==
      plan.source_stdo.installed_manifest_sha256
  ) {
    fail(path, "selects a different Source STDO basis");
  }
  return value as unknown as SemanticAddress;
}

function validateLocator(value: unknown, plan: GtlBuildPlan, path: string): SourceLocator {
  requireExact(
    value,
    ["basis_uri", "member_path", "member_sha256", "fragment"],
    path,
  );
  requireUri(value.basis_uri, `${path}.basis_uri`);
  requireString(value.member_path, `${path}.member_path`);
  requireSha(value.member_sha256, `${path}.member_sha256`);
  if (value.fragment !== null) requireString(value.fragment, `${path}.fragment`);
  if (
    value.basis_uri !== plan.source_stdo.release_uri ||
    value.member_path.startsWith("/") ||
    value.member_path.includes("\\") ||
    value.member_path.includes("#") ||
    value.member_path
      .split("/")
      .some((part) => part.length === 0 || part === "." || part === "..")
  ) {
    fail(path, "is not a normalized locator in the selected Source STDO basis");
  }
  return value as unknown as SourceLocator;
}

function locatorKey(locator: SourceLocator): string {
  return `${locator.member_path}\0${locator.fragment ?? ""}\0${locator.member_sha256}`;
}

function validateLocators(value: unknown, plan: GtlBuildPlan, path: string): readonly SourceLocator[] {
  if (!Array.isArray(value) || value.length === 0) fail(path, "must be non-empty");
  const locators = value.map((locator, index) =>
    validateLocator(locator, plan, `${path}[${index}]`),
  );
  const keys = locators.map(locatorKey);
  const sorted = [...keys].sort(compareUnicodeCodeUnits);
  if (new Set(keys).size !== keys.length || keys.join("\0") !== sorted.join("\0")) {
    fail(path, "must be duplicate-free and canonically sorted");
  }
  return locators;
}

function validateCrossContext(value: unknown, path: string): CrossContext | null {
  if (value === null) return null;
  requireExact(
    value,
    [
      "classification",
      "source_context_ref",
      "target_context_ref",
      "preserved_meaning_refs",
      "changed_meaning_refs",
      "refusal_refs",
      "inverse_ref",
      "invalidation_refs",
    ],
    path,
  );
  if (
    typeof value.classification !== "string" ||
    !CROSS_CONTEXT_CLASSES.includes(value.classification as never)
  ) {
    fail(`${path}.classification`, "is not a selected cross-context relation");
  }
  requireIdentity(value.source_context_ref, `${path}.source_context_ref`);
  requireIdentity(value.target_context_ref, `${path}.target_context_ref`);
  requireStringSet(value.preserved_meaning_refs, `${path}.preserved_meaning_refs`);
  requireStringSet(value.changed_meaning_refs, `${path}.changed_meaning_refs`);
  requireStringSet(value.refusal_refs, `${path}.refusal_refs`);
  if (value.inverse_ref !== null) requireIdentity(value.inverse_ref, `${path}.inverse_ref`);
  requireStringSet(value.invalidation_refs, `${path}.invalidation_refs`);
  return value as unknown as CrossContext;
}

function validateLatitude(value: unknown, path: string): DeclaredLatitude | null {
  if (value === null) return null;
  requireExact(value, ["function_ref", "decision_owner_ref", "re_entry_ref"], path);
  if (
    typeof value.function_ref !== "string" ||
    !LATITUDE_FUNCTIONS.includes(value.function_ref as never)
  ) {
    fail(`${path}.function_ref`, "must be exact Source STDO F_P or F_H");
  }
  requireIdentity(value.decision_owner_ref, `${path}.decision_owner_ref`);
  requireIdentity(value.re_entry_ref, `${path}.re_entry_ref`);
  return value as unknown as DeclaredLatitude;
}

function validateRecord(value: unknown, plan: GtlBuildPlan, path: string): ProgramRecord {
  if (!isRecord(value)) fail(path, "must be one record object");
  if (value.kind === "atom") {
    requireExact(value, ["kind", "id", "atom_class", "label", "semantic_address", "source_locators"], path);
    requireIdentity(value.id, `${path}.id`);
    if (typeof value.atom_class !== "string" || !ATOM_CLASSES.includes(value.atom_class as never)) {
      fail(`${path}.atom_class`, "is not a selected atom class");
    }
    requireString(value.label, `${path}.label`);
    validateAddress(value.semantic_address, plan, `${path}.semantic_address`);
    validateLocators(value.source_locators, plan, `${path}.source_locators`);
    return value as unknown as SemanticAtom;
  }
  if (value.kind === "edge") {
    requireExact(
      value,
      ["kind", "id", "semantic_address", "source_ref", "relation_kind_ref", "target_ref", "context_ref", "owner_ref", "scope_ref", "cross_context", "source_locators"],
      path,
    );
    requireIdentity(value.id, `${path}.id`);
    validateAddress(value.semantic_address, plan, `${path}.semantic_address`);
    requireIdentity(value.source_ref, `${path}.source_ref`);
    requireIdentity(value.relation_kind_ref, `${path}.relation_kind_ref`);
    requireIdentity(value.target_ref, `${path}.target_ref`);
    for (const key of ["context_ref", "owner_ref", "scope_ref"] as const) {
      if (value[key] !== null) requireIdentity(value[key], `${path}.${key}`);
    }
    validateCrossContext(value.cross_context, `${path}.cross_context`);
    validateLocators(value.source_locators, plan, `${path}.source_locators`);
    return value as unknown as SemanticEdge;
  }
  if (value.kind === "constraint") {
    requireExact(
      value,
      ["kind", "id", "semantic_address", "constraint_class", "statement", "applies_to_refs", "context_ref", "owner_ref", "scope_ref", "declared_latitude", "source_locators"],
      path,
    );
    requireIdentity(value.id, `${path}.id`);
    validateAddress(value.semantic_address, plan, `${path}.semantic_address`);
    if (typeof value.constraint_class !== "string" || !CONSTRAINT_CLASSES.includes(value.constraint_class as never)) {
      fail(`${path}.constraint_class`, "is not a selected constraint class");
    }
    requireString(value.statement, `${path}.statement`);
    requireStringSet(value.applies_to_refs, `${path}.applies_to_refs`);
    if (value.applies_to_refs.length === 0) fail(`${path}.applies_to_refs`, "must be non-empty");
    for (const key of ["context_ref", "owner_ref", "scope_ref"] as const) {
      if (value[key] !== null) requireIdentity(value[key], `${path}.${key}`);
    }
    validateLatitude(value.declared_latitude, `${path}.declared_latitude`);
    validateLocators(value.source_locators, plan, `${path}.source_locators`);
    return value as unknown as PassiveConstraint;
  }
  fail(`${path}.kind`, "must be atom, edge, or constraint");
}

function requiredTargetClass(
  index: ReadonlyMap<string, ProgramRecord>,
  ref: string,
  atomClass: string,
  path: string,
): void {
  const target = index.get(ref);
  if (target?.kind !== "atom" || target.atom_class !== atomClass) {
    fail(path, `must target one ${atomClass} atom`);
  }
}

function validateReferences(records: readonly ProgramRecord[]): void {
  const index = new Map(records.map((record) => [record.id, record]));
  const requireAny = (ref: string, path: string): void => {
    if (!index.has(ref)) fail(path, "is dangling or outside I_B");
  };
  records.forEach((record, row) => {
    const path = `$.records[${row}]`;
    if (record.kind === "edge") {
      requireAny(record.source_ref, `${path}.source_ref`);
      requireAny(record.target_ref, `${path}.target_ref`);
      requiredTargetClass(index, record.relation_kind_ref, "relation_kind", `${path}.relation_kind_ref`);
      if (record.context_ref !== null) requiredTargetClass(index, record.context_ref, "bounded_context", `${path}.context_ref`);
      if (record.owner_ref !== null) requiredTargetClass(index, record.owner_ref, "authority", `${path}.owner_ref`);
      if (record.scope_ref !== null) requiredTargetClass(index, record.scope_ref, "scope", `${path}.scope_ref`);
      if (record.cross_context !== null) {
        requiredTargetClass(index, record.cross_context.source_context_ref, "bounded_context", `${path}.cross_context.source_context_ref`);
        requiredTargetClass(index, record.cross_context.target_context_ref, "bounded_context", `${path}.cross_context.target_context_ref`);
        [...record.cross_context.preserved_meaning_refs, ...record.cross_context.changed_meaning_refs].forEach((ref) => requireAny(ref, `${path}.cross_context`));
        [...record.cross_context.refusal_refs, ...record.cross_context.invalidation_refs].forEach((ref) => {
          if (index.get(ref)?.kind !== "constraint") fail(`${path}.cross_context`, "refusal and invalidation refs must target constraints");
        });
        if (record.cross_context.inverse_ref !== null && index.get(record.cross_context.inverse_ref)?.kind !== "edge") {
          fail(`${path}.cross_context.inverse_ref`, "must target an edge");
        }
      }
    } else if (record.kind === "constraint") {
      record.applies_to_refs.forEach((ref) => requireAny(ref, `${path}.applies_to_refs`));
      if (record.context_ref !== null) requiredTargetClass(index, record.context_ref, "bounded_context", `${path}.context_ref`);
      if (record.owner_ref !== null) requiredTargetClass(index, record.owner_ref, "authority", `${path}.owner_ref`);
      if (record.scope_ref !== null) requiredTargetClass(index, record.scope_ref, "scope", `${path}.scope_ref`);
      if (record.declared_latitude !== null) {
        requiredTargetClass(index, record.declared_latitude.decision_owner_ref, "authority", `${path}.declared_latitude.decision_owner_ref`);
        const reentry = index.get(record.declared_latitude.re_entry_ref);
        if (reentry?.kind !== "atom" || !["clause", "design", "intent", "method", "product", "requirement", "ticket"].includes(reentry.atom_class)) {
          fail(`${path}.declared_latitude.re_entry_ref`, "must target an allowed re-entry atom");
        }
      }
    }
  });
}

export function validateBuildPlan(value: unknown): GtlBuildPlan {
  requireExact(
    value,
    ["kind", "schema_version", "source_stdo", "what_member_set_identity", "representation_profile_identity", "representation_profile_sha256", "frame_basis_identity", "frame_basis_sha256", "frame_admitting_authority_refs", "semantic_selection_ledger_identity", "semantic_selection_ledger_sha256", "profile_acceptance_identity", "frame_basis_acceptance_identity", "selection_acceptance_identity", "publisher", "records"],
    "$",
  );
  if (value.kind !== "stdo-representation.gtl-build-plan" || value.schema_version !== 1) {
    fail("$", "has an unsupported build-plan kind or version");
  }
  requireExact(value.source_stdo, ["release_uri", "installed_manifest_sha256", "standards_member_set_sha256"], "$.source_stdo");
  requireUri(value.source_stdo.release_uri, "$.source_stdo.release_uri");
  requireSha(value.source_stdo.installed_manifest_sha256, "$.source_stdo.installed_manifest_sha256");
  requireSha(value.source_stdo.standards_member_set_sha256, "$.source_stdo.standards_member_set_sha256");
  requireSha(value.what_member_set_identity, "$.what_member_set_identity");
  if (value.representation_profile_identity !== PROFILE_IDENTITY) fail("$.representation_profile_identity", `must equal ${PROFILE_IDENTITY}`);
  requireSha(value.representation_profile_sha256, "$.representation_profile_sha256");
  requireUri(value.frame_basis_identity, "$.frame_basis_identity");
  requireSha(value.frame_basis_sha256, "$.frame_basis_sha256");
  if (
    !Array.isArray(value.frame_admitting_authority_refs) ||
    value.frame_admitting_authority_refs.join("\0") !==
      FRAME_ADMITTING_AUTHORITIES.join("\0")
  ) {
    fail("$.frame_admitting_authority_refs", "does not equal the complete Product Definition authority set");
  }
  if (typeof value.semantic_selection_ledger_identity !== "string" || !LEDGER_IDENTITY.test(value.semantic_selection_ledger_identity)) fail("$.semantic_selection_ledger_identity", "is invalid");
  requireSha(value.semantic_selection_ledger_sha256, "$.semantic_selection_ledger_sha256");
  for (const key of ["profile_acceptance_identity", "frame_basis_acceptance_identity", "selection_acceptance_identity"] as const) {
    if (typeof value[key] !== "string" || !ACCEPTANCE_IDENTITY.test(value[key])) fail(`$.${key}`, "is invalid");
  }
  requireExact(value.publisher, ["owning_product_id", "artifact_digest", "product_content_digest", "product_manifest_digest", "descriptor_ref", "contribution_manifest_ref", "package_name", "package_version", "module_path", "named_symbol"], "$.publisher");
  for (const key of ["owning_product_id", "descriptor_ref", "contribution_manifest_ref"] as const) requireUri(value.publisher[key], `$.publisher.${key}`);
  for (const key of ["artifact_digest", "product_content_digest", "product_manifest_digest"] as const) requireSha(value.publisher[key], `$.publisher.${key}`);
  for (const key of ["package_name", "package_version", "module_path", "named_symbol"] as const) requireString(value.publisher[key], `$.publisher.${key}`);
  if (!Array.isArray(value.records) || value.records.length === 0) fail("$.records", "must be non-empty");
  const provisional = value as unknown as GtlBuildPlan;
  const records = value.records.map((record, index) => validateRecord(record, provisional, `$.records[${index}]`));
  const ids = records.map((record) => record.id);
  if (new Set(ids).size !== ids.length) fail("$.records", "contains duplicate identities");
  records.forEach((record, index) => {
    const expected = `urn:stdo-representation:${record.kind}:sha256:${sha256Canonical({
      record_kind: record.kind,
      semantic_address: record.semantic_address,
    } as unknown as JsonValue).slice("sha256:".length)}`;
    if (record.id !== expected) fail(`$.records[${index}].id`, "does not reproduce from its semantic address");
  });
  validateReferences(records);
  return { ...provisional, records };
}

export function assertSelectedTenant(plan: GtlBuildPlan): void {
  if (BUILD_TENANT_IDENTITY !== "urn:stdo-representation:build-tenant:gtl" || CARRIER_BASIS_IDENTITY.length === 0) {
    fail("$", "compiled tenant constants are invalid");
  }
}
