import {
  BUILD_TENANT_IDENTITY,
  type AcceptedBuildEvidence,
  type GtlBuildPlan,
  type ProgramRecord,
} from "./contracts.js";
import {
  canonicalJson,
  compareUnicodeCodeUnits,
  exactKeys,
  isRecord,
  sha256Bytes,
  sha256Canonical,
  type JsonValue,
} from "./canonical.js";

const F_H = "urn:stdo:concept:graph-native-odd:f-h";
const LEDGER_PREFIX = "urn:stdo-representation:semantic-selection-ledger:sha256:";
const ACCEPTANCE_PREFIX = "urn:stdo-representation:authority-acceptance:sha256:";

function fail(path: string, message: string): never {
  throw new TypeError(`${path}: ${message}`);
}

function requireExact(value: unknown, keys: readonly string[], path: string): asserts value is Readonly<Record<string, unknown>> {
  if (!isRecord(value) || !exactKeys(value, keys)) fail(path, `must contain exactly ${keys.join(", ")}`);
}

function stringValue(value: unknown, path: string): string {
  if (typeof value !== "string" || value.length === 0) fail(path, "must be one non-empty string");
  return value;
}

function stringArray(value: unknown, path: string, allowEmpty = true): readonly string[] {
  if (!Array.isArray(value) || (!allowEmpty && value.length === 0)) fail(path, "must be an array with the required cardinality");
  const values = value.map((entry, index) => stringValue(entry, `${path}[${index}]`));
  if (new Set(values).size !== values.length || values.join("\0") !== [...values].sort(compareUnicodeCodeUnits).join("\0")) {
    fail(path, "must be duplicate-free and canonically sorted");
  }
  return values;
}

function exactCanonicalBytes(value: unknown, bytes: Uint8Array, path: string): void {
  let decoded: string;
  try {
    decoded = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  } catch {
    fail(path, "is not valid UTF-8");
  }
  if (decoded !== canonicalJson(value as JsonValue)) fail(path, "bytes are not exact RFC 8785 canonical JSON without framing");
}

interface ManifestMember {
  readonly path: string;
  readonly sha256: string;
}

function validateManifest(plan: GtlBuildPlan, evidence: AcceptedBuildEvidence): readonly ManifestMember[] {
  if (sha256Bytes(evidence.source_manifest_bytes) !== plan.source_stdo.installed_manifest_sha256) {
    fail("source_manifest", "byte digest differs from selected installed manifest");
  }
  requireExact(evidence.source_manifest, ["auxiliary", "kind", "release", "schema_version", "standards"], "source_manifest");
  const standards = evidence.source_manifest.standards;
  if (!isRecord(standards) || !Array.isArray(standards.members)) fail("source_manifest.standards", "has no member inventory");
  if (standards.member_count !== standards.members.length || standards.members.length !== 47) fail("source_manifest.standards.members", "must contain exactly 47 declared members");
  if (`sha256:${standards.member_set_sha256}` !== plan.source_stdo.standards_member_set_sha256) fail("source_manifest.standards.member_set_sha256", "does not match the selected member set");
  return standards.members.map((member, index) => {
    requireExact(member, ["path", "sha256"], `source_manifest.standards.members[${index}]`);
    return {
      path: stringValue(member.path, `source_manifest.standards.members[${index}].path`),
      sha256: stringValue(member.sha256, `source_manifest.standards.members[${index}].sha256`),
    };
  });
}

function validateAcceptance(
  value: unknown,
  bytes: Uint8Array,
  expectedIdentity: string,
  expectedKind: string,
  expectedSubjectIdentity: string,
  expectedSubjectSha: string,
  frameAcceptance: boolean,
  expectedFrameAuthorities: readonly string[],
  path: string,
): void {
  requireExact(
    value,
    ["kind", "schema_version", "subject_kind", "subject_identity", "subject_sha256", "traversal_ref", "actor_identity", "authority_identity", "grant_identity", "grant_scope", "basis_refs", "admitting_authority_refs", "decision", "decided_at", "evidence_refs", "supersedes"],
    path,
  );
  exactCanonicalBytes(value, bytes, path);
  const derived = `${ACCEPTANCE_PREFIX}${sha256Bytes(bytes).slice("sha256:".length)}`;
  if (derived !== expectedIdentity) fail(path, "identity does not reproduce from exact record bytes");
  if (
    value.kind !== "stdo-representation.authority-acceptance" ||
    value.schema_version !== 1 ||
    value.subject_kind !== expectedKind ||
    value.subject_identity !== expectedSubjectIdentity ||
    value.subject_sha256 !== expectedSubjectSha ||
    value.traversal_ref !== F_H ||
    value.decision !== "accepted"
  ) {
    fail(path, "does not accept the exact required subject under F_H");
  }
  for (const key of ["actor_identity", "authority_identity", "grant_identity", "grant_scope", "decided_at"] as const) stringValue(value[key], `${path}.${key}`);
  stringArray(value.basis_refs, `${path}.basis_refs`, false);
  stringArray(value.evidence_refs, `${path}.evidence_refs`, false);
  if (frameAcceptance) {
    const observed = stringArray(value.admitting_authority_refs, `${path}.admitting_authority_refs`, false);
    if (observed.join("\0") !== expectedFrameAuthorities.join("\0")) fail(`${path}.admitting_authority_refs`, "does not equal the complete Product Definition authority set");
  }
  else if (value.admitting_authority_refs !== null) fail(`${path}.admitting_authority_refs`, "must be null outside frame-basis acceptance");
  if (value.supersedes !== null) stringValue(value.supersedes, `${path}.supersedes`);
}

function locatorKey(value: unknown, path: string): string {
  requireExact(value, ["basis_uri", "member_path", "member_sha256", "fragment"], path);
  const basis = stringValue(value.basis_uri, `${path}.basis_uri`);
  const member = stringValue(value.member_path, `${path}.member_path`);
  const digest = stringValue(value.member_sha256, `${path}.member_sha256`);
  const fragment = value.fragment === null ? "" : stringValue(value.fragment, `${path}.fragment`);
  void basis;
  return `${member}\0${fragment}\0${digest}`;
}

function validateLedger(
  plan: GtlBuildPlan,
  evidence: AcceptedBuildEvidence,
  members: readonly ManifestMember[],
): void {
  const ledger = evidence.semantic_selection_ledger;
  requireExact(
    ledger,
    ["kind", "schema_version", "source_stdo_uri", "source_stdo_manifest_sha256", "source_member_set_sha256", "what_member_set_identity", "build_tenant_identity", "representation_profile_identity", "representation_profile_sha256", "representation_records_sha256", "evaluated_members", "selections", "generated_source_keys", "residual_uncertainty", "author", "supersedes"],
    "semantic_selection_ledger",
  );
  exactCanonicalBytes(ledger, evidence.semantic_selection_ledger_bytes, "semantic_selection_ledger");
  const ledgerDigest = sha256Bytes(evidence.semantic_selection_ledger_bytes);
  if (ledgerDigest !== plan.semantic_selection_ledger_sha256 || `${LEDGER_PREFIX}${ledgerDigest.slice("sha256:".length)}` !== plan.semantic_selection_ledger_identity) {
    fail("semantic_selection_ledger", "digest or identity does not reproduce");
  }
  if (
    ledger.kind !== "stdo-representation.semantic-selection-ledger" ||
    ledger.schema_version !== 1 ||
    ledger.source_stdo_uri !== plan.source_stdo.release_uri ||
    ledger.source_stdo_manifest_sha256 !== plan.source_stdo.installed_manifest_sha256 ||
    ledger.source_member_set_sha256 !== plan.source_stdo.standards_member_set_sha256 ||
    ledger.what_member_set_identity !== plan.what_member_set_identity ||
    ledger.build_tenant_identity !== BUILD_TENANT_IDENTITY ||
    ledger.representation_profile_identity !== plan.representation_profile_identity ||
    ledger.representation_profile_sha256 !== plan.representation_profile_sha256
  ) {
    fail("semantic_selection_ledger", "selects a different Product basis");
  }
  const canonicalRecords = [...plan.records].sort((left, right) =>
    compareUnicodeCodeUnits(left.id, right.id),
  );
  if (
    ledger.representation_records_sha256 !==
    sha256Canonical(canonicalRecords as unknown as JsonValue)
  ) {
    fail(
      "semantic_selection_ledger.representation_records_sha256",
      "does not bind the complete ID-sorted canonical build-plan record array",
    );
  }
  if (!Array.isArray(ledger.evaluated_members) || ledger.evaluated_members.length !== members.length) fail("semantic_selection_ledger.evaluated_members", "does not equal the exact manifest population");
  if (!Array.isArray(ledger.selections) || ledger.selections.length === 0) fail("semantic_selection_ledger.selections", "must be non-empty");
  const memberDigests = new Map(
    members.map((member) => [member.path, `sha256:${member.sha256}`]),
  );
  const selections = new Map<string, {
    disposition: string;
    refs: readonly string[];
    members: readonly string[];
    locatorKeys: ReadonlySet<string>;
  }>();
  for (const [index, raw] of ledger.selections.entries()) {
    const path = `semantic_selection_ledger.selections[${index}]`;
    requireExact(raw, ["selection_ref", "source_locators", "disposition", "representation_refs", "rationale", "source_owner", "ordered_relation"], path);
    const selectionRef = stringValue(raw.selection_ref, `${path}.selection_ref`);
    if (!Array.isArray(raw.source_locators) || raw.source_locators.length === 0) fail(`${path}.source_locators`, "must be non-empty");
    const locatorKeys = raw.source_locators.map((locator, locatorIndex) => {
      const locatorPath = `${path}.source_locators[${locatorIndex}]`;
      const key = locatorKey(locator, locatorPath);
      const row = locator as { basis_uri: string; member_path: string; member_sha256: string };
      if (
        row.basis_uri !== plan.source_stdo.release_uri ||
        memberDigests.get(row.member_path) !== row.member_sha256
      ) {
        fail(locatorPath, "does not resolve in the exact installed member inventory");
      }
      return key;
    });
    if (new Set(locatorKeys).size !== locatorKeys.length || locatorKeys.join("\0") !== [...locatorKeys].sort(compareUnicodeCodeUnits).join("\0")) fail(`${path}.source_locators`, "must be duplicate-free and canonically sorted");
    const sourceOwner = stringValue(raw.source_owner, `${path}.source_owner`);
    const expectedRef = `urn:stdo-representation:selection:sha256:${sha256Canonical({ source_locators: raw.source_locators, source_owner: sourceOwner } as unknown as JsonValue).slice("sha256:".length)}`;
    if (selectionRef !== expectedRef || selections.has(selectionRef)) fail(`${path}.selection_ref`, "does not reproduce or is duplicated");
    if (!["retained", "omitted", "uncertain"].includes(String(raw.disposition))) fail(`${path}.disposition`, "is invalid");
    const refs = stringArray(raw.representation_refs, `${path}.representation_refs`);
    stringValue(raw.rationale, `${path}.rationale`);
    if (typeof raw.ordered_relation !== "boolean") fail(`${path}.ordered_relation`, "must be boolean");
    if ((raw.disposition === "retained") !== (refs.length > 0)) fail(path, "retained rows require refs and non-retained rows prohibit them");
    if (raw.disposition === "uncertain") fail(path, "uncertain semantic selection cannot enter a complete production build");
    selections.set(selectionRef, {
      disposition: String(raw.disposition),
      refs,
      members: raw.source_locators.map((locator) => (locator as { member_path: string }).member_path),
      locatorKeys: new Set(locatorKeys),
    });
  }
  if ([...selections.keys()].join("\0") !== [...selections.keys()].sort(compareUnicodeCodeUnits).join("\0")) fail("semantic_selection_ledger.selections", "must sort by selection_ref");
  for (const [index, raw] of ledger.evaluated_members.entries()) {
    const path = `semantic_selection_ledger.evaluated_members[${index}]`;
    requireExact(raw, ["member_path", "member_sha256", "disposition", "selection_refs", "rationale"], path);
    if (raw.member_path !== members[index]!.path || raw.member_sha256 !== `sha256:${members[index]!.sha256}`) fail(path, "does not match installed-manifest order and digest");
    const refs = stringArray(raw.selection_refs, `${path}.selection_refs`);
    const expected = [...selections.entries()].filter(([, row]) => row.members.includes(members[index]!.path)).map(([ref]) => ref).sort(compareUnicodeCodeUnits);
    if (refs.join("\0") !== expected.join("\0")) fail(`${path}.selection_refs`, "does not equal the selections locating this member");
    const expectedDisposition = refs.some((ref) => selections.get(ref)?.disposition === "retained") ? "contains_retained_material" : "contains_no_retained_material";
    if (raw.disposition !== expectedDisposition) fail(`${path}.disposition`, "does not follow its selection rows");
    stringValue(raw.rationale, `${path}.rationale`);
  }
  const retained = new Map<string, number>();
  const retainedOwner = new Map<string, { locatorKeys: ReadonlySet<string> }>();
  for (const row of selections.values()) if (row.disposition === "retained") for (const ref of row.refs) retained.set(ref, (retained.get(ref) ?? 0) + 1);
  for (const row of selections.values()) {
    if (row.disposition !== "retained") continue;
    for (const ref of row.refs) retainedOwner.set(ref, row);
  }
  const recordIds = plan.records.map((record) => record.id).sort(compareUnicodeCodeUnits);
  if ([...retained.keys()].sort(compareUnicodeCodeUnits).join("\0") !== recordIds.join("\0") || [...retained.values()].some((count) => count !== 1)) fail("semantic_selection_ledger.selections", "retained-reference ownership is not exactly I_B once");
  for (const record of plan.records) {
    const owner = retainedOwner.get(record.id);
    if (
      owner === undefined ||
      record.source_locators.some(
        (locator, index) =>
          !owner.locatorKeys.has(
            locatorKey(locator, `records[${record.id}].source_locators[${index}]`),
          ),
      )
    ) {
      fail("semantic_selection_ledger.selections", `selection for ${record.id} does not contain every represented source locator`);
    }
  }
  if (!Array.isArray(ledger.residual_uncertainty) || ledger.residual_uncertainty.length !== 0) fail("semantic_selection_ledger.residual_uncertainty", "must be empty for a complete production build");
  validateGeneratedKeys(plan.records, ledger.generated_source_keys, retainedOwner);
  requireExact(ledger.author, ["traversal_ref", "actor_identity", "authority_identity", "grant_identity", "grant_scope", "subject", "basis_refs"], "semantic_selection_ledger.author");
  if (ledger.author.traversal_ref !== F_H) fail("semantic_selection_ledger.author.traversal_ref", "must be exact F_H");
  for (const key of ["actor_identity", "authority_identity", "grant_identity", "grant_scope", "subject"] as const) stringValue(ledger.author[key], `semantic_selection_ledger.author.${key}`);
  stringArray(ledger.author.basis_refs, "semantic_selection_ledger.author.basis_refs", false);
  if (ledger.supersedes !== null) stringValue(ledger.supersedes, "semantic_selection_ledger.supersedes");
}

function validateGeneratedKeys(
  records: readonly ProgramRecord[],
  rawBindings: unknown,
  retainedOwner: ReadonlyMap<string, { locatorKeys: ReadonlySet<string> }>,
): void {
  if (!Array.isArray(rawBindings)) fail("semantic_selection_ledger.generated_source_keys", "must be an array");
  const used = records.filter((record) => record.semantic_address.source_key.startsWith("urn:stdo-representation:source-key:sha256:")).map((record) => record.semantic_address.source_key).sort(compareUnicodeCodeUnits);
  const observed: string[] = [];
  const primaryByKey = new Map<string, string>();
  for (const [index, raw] of rawBindings.entries()) {
    const path = `semantic_selection_ledger.generated_source_keys[${index}]`;
    requireExact(raw, ["source_key", "primary_source_locator", "local_declaration_key"], path);
    const sourceKey = stringValue(raw.source_key, `${path}.source_key`);
    const localKey = stringValue(raw.local_declaration_key, `${path}.local_declaration_key`);
    locatorKey(raw.primary_source_locator, `${path}.primary_source_locator`);
    const expected = `urn:stdo-representation:source-key:sha256:${sha256Canonical({ primary_source_locator: raw.primary_source_locator, local_declaration_key: localKey } as unknown as JsonValue).slice("sha256:".length)}`;
    if (sourceKey !== expected) fail(`${path}.source_key`, "does not reproduce from its preimage");
    observed.push(sourceKey);
    primaryByKey.set(sourceKey, locatorKey(raw.primary_source_locator, `${path}.primary_source_locator`));
  }
  if (new Set(observed).size !== observed.length || observed.join("\0") !== [...observed].sort(compareUnicodeCodeUnits).join("\0") || observed.join("\0") !== used.join("\0")) fail("semantic_selection_ledger.generated_source_keys", "must bind every generated key exactly once in canonical order");
  for (const record of records) {
    const primary = primaryByKey.get(record.semantic_address.source_key);
    if (primary === undefined) continue;
    const representedLocators = new Set(
      record.source_locators.map((locator, index) =>
        locatorKey(locator, `records[${record.id}].source_locators[${index}]`),
      ),
    );
    if (
      !representedLocators.has(primary) ||
      !retainedOwner.get(record.id)?.locatorKeys.has(primary)
    ) {
      fail("semantic_selection_ledger.generated_source_keys", `primary locator for ${record.id} is not bound by its record and selection`);
    }
  }
}

function validatePublisher(plan: GtlBuildPlan, evidence: AcceptedBuildEvidence): void {
  const manifest = evidence.publisher_manifest;
  requireExact(
    manifest,
    ["kind", "schema_version", "repository", "commit_sha1", "tree_sha1", "artifact_digest", "product_content_digest", "descriptor_ref", "contribution_manifest_ref", "package_name", "package_version", "module_path", "named_symbol", "members", "supersedes"],
    "publisher_manifest",
  );
  exactCanonicalBytes(manifest, evidence.publisher_manifest_bytes, "publisher_manifest");
  const manifestDigest = sha256Bytes(evidence.publisher_manifest_bytes);
  const artifactDigest = sha256Bytes(evidence.publisher_artifact_bytes);
  const expectedOwner = `urn:stdo-representation:gtl-toolchain-product:sha256:${manifestDigest.slice("sha256:".length)}`;
  if (
    manifest.kind !== "stdo-representation.gtl-toolchain-product" ||
    manifest.schema_version !== 1 ||
    manifestDigest !== plan.publisher.product_manifest_digest ||
    artifactDigest !== plan.publisher.artifact_digest ||
    manifest.artifact_digest !== artifactDigest ||
    manifest.product_content_digest !== plan.publisher.product_content_digest ||
    expectedOwner !== plan.publisher.owning_product_id
  ) {
    fail("publisher_manifest", "does not reproduce the selected immutable publisher Product basis");
  }
  for (const key of ["descriptor_ref", "contribution_manifest_ref", "package_name", "package_version", "module_path", "named_symbol"] as const) {
    if (manifest[key] !== plan.publisher[key]) fail(`publisher_manifest.${key}`, "differs from the build plan");
  }
  for (const key of ["repository", "commit_sha1", "tree_sha1"] as const) stringValue(manifest[key], `publisher_manifest.${key}`);
  if (!Array.isArray(manifest.members) || manifest.members.length === 0) fail("publisher_manifest.members", "must be non-empty");
  const memberRows: string[] = [];
  const paths: string[] = [];
  for (const [index, raw] of manifest.members.entries()) {
    const path = `publisher_manifest.members[${index}]`;
    requireExact(raw, ["path", "sha256"], path);
    const memberPath = stringValue(raw.path, `${path}.path`);
    const digest = stringValue(raw.sha256, `${path}.sha256`);
    if (!/^sha256:[0-9a-f]{64}$/u.test(digest) || memberPath.startsWith("/") || memberPath.includes("\\") || memberPath.split("/").some((part) => part.length === 0 || part === "..")) fail(path, "is not one normalized content member");
    paths.push(memberPath);
    memberRows.push(`${memberPath}\0${digest}\n`);
  }
  if (new Set(paths).size !== paths.length || paths.join("\0") !== [...paths].sort(compareUnicodeCodeUnits).join("\0")) fail("publisher_manifest.members", "must be unique and path-sorted");
  if (sha256Bytes(memberRows.join("")) !== plan.publisher.product_content_digest) fail("publisher_manifest.product_content_digest", "does not reproduce from its member inventory");
  if (manifest.supersedes !== null) stringValue(manifest.supersedes, "publisher_manifest.supersedes");
}

export function validateAcceptedBuildEvidence(plan: GtlBuildPlan, evidence: AcceptedBuildEvidence): void {
  if (sha256Bytes(evidence.profile_bytes) !== plan.representation_profile_sha256) fail("profile", "bytes differ from the selected profile digest");
  if (sha256Bytes(evidence.frame_basis_bytes) !== plan.frame_basis_sha256) fail("frame_basis", "bytes differ from the selected frame-basis digest");
  const members = validateManifest(plan, evidence);
  validatePublisher(plan, evidence);
  validateLedger(plan, evidence, members);
  validateAcceptance(evidence.profile_acceptance, evidence.profile_acceptance_bytes, plan.profile_acceptance_identity, "representation_profile", plan.representation_profile_identity, plan.representation_profile_sha256, false, [], "profile_acceptance");
  validateAcceptance(evidence.frame_basis_acceptance, evidence.frame_basis_acceptance_bytes, plan.frame_basis_acceptance_identity, "reference_frame_basis", plan.frame_basis_identity, plan.frame_basis_sha256, true, plan.frame_admitting_authority_refs, "frame_basis_acceptance");
  validateAcceptance(evidence.selection_acceptance, evidence.selection_acceptance_bytes, plan.selection_acceptance_identity, "semantic_selection_ledger", plan.semantic_selection_ledger_identity, plan.semantic_selection_ledger_sha256, false, [], "selection_acceptance");
}
