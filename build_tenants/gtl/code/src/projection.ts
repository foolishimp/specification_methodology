import type {
  AcceptedBuildEvidence,
  ProgramRecord,
  ProjectionCandidate,
} from "./contracts.js";
import {
  canonicalJson,
  compareUnicodeCodeUnits,
  exactKeys,
  isRecord,
  sha256Bytes,
  type JsonValue,
} from "./canonical.js";
import { constructValidatedStdoGtl } from "./construct.js";
import { validateAcceptedBuildEvidence } from "./evidence.js";
import { validateBuildPlan } from "./validation.js";

function directReferences(record: ProgramRecord): readonly string[] {
  if (record.kind === "atom") return [];
  if (record.kind === "edge") {
    const refs = [record.source_ref, record.relation_kind_ref, record.target_ref];
    if (record.context_ref !== null) refs.push(record.context_ref);
    if (record.owner_ref !== null) refs.push(record.owner_ref);
    if (record.scope_ref !== null) refs.push(record.scope_ref);
    if (record.cross_context !== null) {
      refs.push(
        record.cross_context.source_context_ref,
        record.cross_context.target_context_ref,
        ...record.cross_context.preserved_meaning_refs,
        ...record.cross_context.changed_meaning_refs,
        ...record.cross_context.refusal_refs,
        ...record.cross_context.invalidation_refs,
      );
      if (record.cross_context.inverse_ref !== null) {
        refs.push(record.cross_context.inverse_ref);
      }
    }
    return refs;
  }
  const refs = [...record.applies_to_refs];
  if (record.context_ref !== null) refs.push(record.context_ref);
  if (record.owner_ref !== null) refs.push(record.owner_ref);
  if (record.scope_ref !== null) refs.push(record.scope_ref);
  if (record.declared_latitude !== null) {
    refs.push(
      record.declared_latitude.decision_owner_ref,
      record.declared_latitude.re_entry_ref,
    );
  }
  return refs;
}

export function leastContextClosure(
  records: readonly ProgramRecord[],
  seedRefs: readonly string[],
): readonly ProgramRecord[] {
  if (seedRefs.length === 0 || new Set(seedRefs).size !== seedRefs.length) {
    throw new TypeError("projection seeds must be non-empty and duplicate-free");
  }
  const index = new Map(records.map((record) => [record.id, record]));
  const included = new Set<string>();
  for (const ref of seedRefs) {
    if (!index.has(ref)) {
      throw new TypeError(`projection seed is outside I_B: ${ref}`);
    }
    included.add(ref);
  }
  let changed = true;
  while (changed) {
    changed = false;
    for (const ref of [...included]) {
      const record = index.get(ref)!;
      for (const dependency of directReferences(record)) {
        if (!included.has(dependency)) {
          included.add(dependency);
          changed = true;
        }
      }
    }
    for (const record of records) {
      if (
        record.kind === "constraint" &&
        !included.has(record.id) &&
        record.applies_to_refs.some((ref) => included.has(ref))
      ) {
        included.add(record.id);
        changed = true;
      }
    }
  }
  return records
    .filter((record) => included.has(record.id))
    .sort((left, right) => compareUnicodeCodeUnits(left.id, right.id));
}

const ENGAGEMENT_ROLES = new Map([
  [
    "stdo://releases/v2.4.3-rc.3/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive",
    "executive",
  ],
  [
    "stdo://releases/v2.4.3-rc.3/standards/STDO_REFERENCE_FRAME_BASELINE.md#worker",
    "worker",
  ],
  [
    "stdo://releases/v2.4.3-rc.3/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer",
    "reviewer",
  ],
]);

function fail(path: string, message: string): never {
  throw new TypeError(`${path}: ${message}`);
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

function requireString(value: unknown, path: string): string {
  if (typeof value !== "string" || value.length === 0) {
    fail(path, "must be one non-empty string");
  }
  return value;
}

function requireUri(value: unknown, path: string): string {
  const result = requireString(value, path);
  try {
    if (new URL(result).protocol.length === 0) fail(path, "must be absolute URI");
  } catch {
    fail(path, "must be absolute URI");
  }
  return result;
}

function requireStrings(
  value: unknown,
  path: string,
  nonEmpty: boolean,
): readonly string[] {
  if (!Array.isArray(value) || (nonEmpty && value.length === 0)) {
    fail(path, "has invalid cardinality");
  }
  const result = value.map((entry, index) =>
    requireString(entry, `${path}[${index}]`),
  );
  if (
    new Set(result).size !== result.length ||
    result.join("\0") !== [...result].sort(compareUnicodeCodeUnits).join("\0")
  ) {
    fail(path, "must be duplicate-free and canonically sorted");
  }
  return result;
}

function validateAssignment(
  value: unknown,
  bytes: Uint8Array,
  records: readonly ProgramRecord[],
  parentProductIdentity: string,
  parentContentIdentity: string,
): {
  readonly identity: string;
  readonly seeds: readonly string[];
} {
  requireExact(
    value,
    [
      "kind",
      "schema_version",
      "program_product_identity",
      "program_content_identity",
      "workspace_subject_identity",
      "workspace_basis_refs",
      "governed_outcome_ref",
      "reasoning_intent_ref",
      "engagement_role_ref",
      "target_actor_identity",
      "target_capability_envelope_ref",
      "assigning_actor_identity",
      "frame_set_authority_identity",
      "assignment_grant_identity",
      "assignment_grant_scope",
      "frame_activations",
      "role_program_refs",
      "explicit_program_seed_refs",
      "inherited_operation_grant_refs",
      "decision_grant_refs",
      "required_evidence_refs",
      "stop_state_refs",
      "context_budget",
      "supersedes",
    ],
    "assignment",
  );
  let decoded: string;
  try {
    decoded = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  } catch {
    fail("assignment", "bytes are not valid UTF-8");
  }
  if (decoded !== canonicalJson(value as JsonValue)) {
    fail("assignment", "bytes are not exact RFC 8785 JCS without framing");
  }
  if (
    value.kind !== "stdo-representation.executive-context-assignment" ||
    value.schema_version !== 1 ||
    value.program_product_identity !== parentProductIdentity ||
    value.program_content_identity !== parentContentIdentity
  ) {
    fail("assignment", "does not select the exact parent index Product");
  }
  for (const key of [
    "workspace_subject_identity",
    "governed_outcome_ref",
    "reasoning_intent_ref",
    "target_actor_identity",
    "target_capability_envelope_ref",
    "assigning_actor_identity",
    "frame_set_authority_identity",
    "assignment_grant_identity",
  ] as const) {
    requireUri(value[key], `assignment.${key}`);
  }
  requireString(value.assignment_grant_scope, "assignment.assignment_grant_scope");
  for (const key of [
    "workspace_basis_refs",
    "inherited_operation_grant_refs",
    "decision_grant_refs",
    "required_evidence_refs",
    "stop_state_refs",
  ] as const) {
    const nonEmpty = key === "workspace_basis_refs" || key === "stop_state_refs";
    requireStrings(value[key], `assignment.${key}`, nonEmpty).forEach(
      (entry, index) => requireUri(entry, `assignment.${key}[${index}]`),
    );
  }
  const role = requireString(value.engagement_role_ref, "assignment.engagement_role_ref");
  const roleFragment = ENGAGEMENT_ROLES.get(role);
  if (roleFragment === undefined) {
    fail("assignment.engagement_role_ref", "is not an exact Source STDO engagement role");
  }
  const recordIndex = new Map(records.map((record) => [record.id, record]));
  const programRefs = (
    raw: unknown,
    path: string,
    nonEmpty: boolean,
  ): readonly string[] => {
    const refs = requireStrings(raw, path, nonEmpty);
    for (const ref of refs) {
      if (!recordIndex.has(ref)) fail(path, `contains identity outside I_B: ${ref}`);
    }
    return refs;
  };
  const roleSeeds = programRefs(
    value.role_program_refs,
    "assignment.role_program_refs",
    true,
  );
  for (const ref of roleSeeds) {
    const record = recordIndex.get(ref)!;
    if (
      !record.source_locators.some(
        (locator) =>
          locator.member_path === "STDO_REFERENCE_FRAME_BASELINE.md" &&
          locator.fragment === roleFragment,
      )
    ) {
      fail(
        "assignment.role_program_refs",
        `${ref} is not source-bound to the selected engagement-role clause`,
      );
    }
  }
  const explicitSeeds = programRefs(
    value.explicit_program_seed_refs,
    "assignment.explicit_program_seed_refs",
    false,
  );
  if (!Array.isArray(value.frame_activations) || value.frame_activations.length === 0) {
    fail("assignment.frame_activations", "must be non-empty");
  }
  const activationRefs: string[] = [];
  const frameSeeds: string[] = [];
  for (const [activationIndex, raw] of value.frame_activations.entries()) {
    const path = `assignment.frame_activations[${activationIndex}]`;
    requireExact(
      raw,
      [
        "activation_ref",
        "frame_identity",
        "frame_sha256",
        "mandatory_program_refs",
        "evaluation_refs",
        "required_capability_envelope_ref",
      ],
      path,
    );
    activationRefs.push(requireUri(raw.activation_ref, `${path}.activation_ref`));
    requireUri(raw.frame_identity, `${path}.frame_identity`);
    if (
      typeof raw.frame_sha256 !== "string" ||
      !/^sha256:[0-9a-f]{64}$/u.test(raw.frame_sha256)
    ) {
      fail(`${path}.frame_sha256`, "is invalid");
    }
    const mandatory = programRefs(
      raw.mandatory_program_refs,
      `${path}.mandatory_program_refs`,
      true,
    );
    if (
      !mandatory.some(
        (ref) => {
          const record = recordIndex.get(ref);
          return record?.kind === "atom" && record.atom_class === "reference_frame";
        },
      )
    ) {
      fail(`${path}.mandatory_program_refs`, "must include a reference_frame atom");
    }
    frameSeeds.push(...mandatory);
    requireStrings(raw.evaluation_refs, `${path}.evaluation_refs`, true).forEach(
      (entry, index) => requireUri(entry, `${path}.evaluation_refs[${index}]`),
    );
    requireUri(
      raw.required_capability_envelope_ref,
      `${path}.required_capability_envelope_ref`,
    );
  }
  if (
    new Set(activationRefs).size !== activationRefs.length ||
    activationRefs.join("\0") !==
      [...activationRefs].sort(compareUnicodeCodeUnits).join("\0")
  ) {
    fail("assignment.frame_activations", "must be unique and sorted by activation_ref");
  }
  requireExact(
    value.context_budget,
    [
      "tokenizer_identity",
      "tokenizer_version",
      "tokenizer_configuration_sha256",
      "model_context_limit_tokens",
      "reserved_non_program_tokens",
      "maximum_projection_tokens",
    ],
    "assignment.context_budget",
  );
  requireUri(
    value.context_budget.tokenizer_identity,
    "assignment.context_budget.tokenizer_identity",
  );
  requireString(
    value.context_budget.tokenizer_version,
    "assignment.context_budget.tokenizer_version",
  );
  if (
    typeof value.context_budget.tokenizer_configuration_sha256 !== "string" ||
    !/^sha256:[0-9a-f]{64}$/u.test(
      value.context_budget.tokenizer_configuration_sha256,
    )
  ) {
    fail("assignment.context_budget.tokenizer_configuration_sha256", "is invalid");
  }
  for (const key of [
    "model_context_limit_tokens",
    "reserved_non_program_tokens",
    "maximum_projection_tokens",
  ] as const) {
    const number = value.context_budget[key];
    if (
      !Number.isSafeInteger(number) ||
      (key === "reserved_non_program_tokens"
        ? Number(number) < 0
        : Number(number) <= 0)
    ) {
      fail(`assignment.context_budget.${key}`, "has invalid bounds");
    }
  }
  if (
    Number(value.context_budget.maximum_projection_tokens) +
      Number(value.context_budget.reserved_non_program_tokens) >
    Number(value.context_budget.model_context_limit_tokens)
  ) {
    fail(
      "assignment.context_budget",
      "projection and reservation exceed the model context limit",
    );
  }
  const identity =
    `urn:stdo-representation:executive-context-assignment:sha256:${sha256Bytes(bytes).slice("sha256:".length)}`;
  if (value.supersedes !== null) {
    const supersedes = requireUri(value.supersedes, "assignment.supersedes");
    if (supersedes === identity) fail("assignment.supersedes", "cannot self-reference");
  }
  return {
    identity,
    seeds: [...new Set([...frameSeeds, ...roleSeeds, ...explicitSeeds])].sort(
      compareUnicodeCodeUnits,
    ),
  };
}

function identitySetDigest(refs: readonly string[]): string {
  return sha256Bytes(refs.map((ref) => `${ref}\n`).join(""));
}

export function constructProjectionCandidate(
  input: unknown,
  evidence: AcceptedBuildEvidence,
  assignmentInput: unknown,
  assignmentBytes: Uint8Array,
): ProjectionCandidate {
  const plan = validateBuildPlan(input);
  validateAcceptedBuildEvidence(plan, evidence);
  const parent = constructValidatedStdoGtl(plan);
  const assignment = validateAssignment(
    assignmentInput,
    assignmentBytes,
    plan.records,
    parent.receipt.product_identity,
    parent.receipt.program_content_identity,
  );
  const selected = leastContextClosure(plan.records, assignment.seeds);
  const included = selected
    .map((record) => record.id)
    .sort(compareUnicodeCodeUnits);
  const includedSet = new Set(included);
  const omitted = plan.records
    .map((record) => record.id)
    .filter((ref) => !includedSet.has(ref))
    .sort(compareUnicodeCodeUnits);
  const projected = constructValidatedStdoGtl({ ...plan, records: selected });
  return {
    kind: "stdo-representation.gtl-projection-candidate",
    schema_version: 1,
    assignment_identity: assignment.identity,
    parent_product_identity: parent.receipt.product_identity,
    parent_program_content_identity: parent.receipt.program_content_identity,
    included_identity_refs: included,
    included_identity_set_sha256: identitySetDigest(included),
    omitted_identity_refs: omitted,
    omitted_identity_set_sha256: identitySetDigest(omitted),
    projection_carrier_sha256: sha256Bytes(projected.canonical_bytes),
    canonical_bytes: projected.canonical_bytes,
  };
}
