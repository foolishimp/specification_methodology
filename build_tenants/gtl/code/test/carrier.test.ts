import assert from "node:assert/strict";
import test from "node:test";

import { constructStdoGtl } from "../src/construct.js";
import {
  constructProjectionCandidate,
  leastContextClosure,
} from "../src/projection.js";
import {
  canonicalJson,
  compareUnicodeCodeUnits,
  sha256Bytes,
  sha256Canonical,
  type JsonValue,
} from "../src/canonical.js";
import type {
  AcceptedBuildEvidence,
  GtlBuildPlan,
  ProgramRecord,
  SemanticAddress,
  SourceLocator,
} from "../src/contracts.js";

const SOURCE_URI = "stdo://releases/v2.4.3-rc.3/";
const MEMBER_DIGEST = "2".repeat(64);
const MEMBER_SET = `sha256:${"3".repeat(64)}`;
const PROFILE_ID = "urn:stdo-representation:gtl-profile:stdo-gtl:0.7.0";
const FRAME_ID = "urn:stdo-representation:reference-frame-basis:source-project:3";
const FRAME_AUTHORITIES = [
  "./specification/GOALS.md",
  "./specification/PRODUCT.md#product-authority",
  "./specification/requirements/REQ-P-BASIS-AND-IDENTITY.md",
  "./specification/requirements/REQ-P-COMPRESSION-VERIFICATION.md",
  "./specification/requirements/REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
  "./specification/requirements/REQ-P-FP-CONSUMPTION.md",
  "./specification/requirements/REQ-P-REPRESENTATION-ALGEBRA.md",
  "./specification/requirements/REQ-P-SELECTION-AND-ACCEPTANCE.md",
];
const encoder = new TextEncoder();

function identity(kind: ProgramRecord["kind"], semanticAddress: SemanticAddress): string {
  return `urn:stdo-representation:${kind}:sha256:${sha256Canonical({
    record_kind: kind,
    semantic_address: semanticAddress,
  } as unknown as JsonValue).slice("sha256:".length)}`;
}

function canonicalBytes(value: JsonValue): Uint8Array {
  return encoder.encode(canonicalJson(value));
}

function acceptance(
  subjectKind: string,
  subjectIdentity: string,
  subjectSha: string,
  frame = false,
): { value: JsonValue; bytes: Uint8Array; identity: string } {
  const value = {
    kind: "stdo-representation.authority-acceptance",
    schema_version: 1,
    subject_kind: subjectKind,
    subject_identity: subjectIdentity,
    subject_sha256: subjectSha,
    traversal_ref: "urn:stdo:concept:graph-native-odd:f-h",
    actor_identity: "urn:test:actor:owner",
    authority_identity: "urn:test:authority:product",
    grant_identity: "urn:test:grant:accept",
    grant_scope: "synthetic frozen-carrier conformance fixture",
    basis_refs: [SOURCE_URI],
    admitting_authority_refs: frame ? FRAME_AUTHORITIES : null,
    decision: "accepted",
    decided_at: "2026-08-28T00:00:00+10:00",
    evidence_refs: ["urn:test:evidence:review"],
    supersedes: null,
  } as const;
  const bytes = canonicalBytes(value as unknown as JsonValue);
  return {
    value: value as unknown as JsonValue,
    bytes,
    identity: `urn:stdo-representation:authority-acceptance:sha256:${sha256Bytes(bytes).slice("sha256:".length)}`,
  };
}

function fixture(): { plan: GtlBuildPlan; evidence: AcceptedBuildEvidence } {
  const manifestMembers = [
    { path: "ODD_METHOD.md", sha256: MEMBER_DIGEST },
    { path: "STDO_REFERENCE_FRAME_BASELINE.md", sha256: "5".repeat(64) },
    ...Array.from({ length: 45 }, (_, index) => ({
      path: `fixture/member-${String(index).padStart(2, "0")}.md`,
      sha256: (index + 10).toString(16).padStart(64, "0"),
    })),
  ];
  const manifest = {
    auxiliary: [],
    kind: "installed_release_manifest",
    release: { cut: "v2.4.3-rc.3" },
    schema_version: 1,
    standards: {
      installed_root: "standards",
      member_count: 47,
      member_set_sha256: MEMBER_SET.slice("sha256:".length),
      members: manifestMembers,
      source_root: "specification/standards",
    },
  };
  const manifestBytes = canonicalBytes(manifest as unknown as JsonValue);
  const manifestSha = sha256Bytes(manifestBytes);
  const profileBytes = encoder.encode("# synthetic profile fixture\n");
  const frameBytes = encoder.encode("# synthetic frame-basis fixture\n");
  const profileSha = sha256Bytes(profileBytes);
  const frameSha = sha256Bytes(frameBytes);
  const address = (term: string, sourceKey: string): SemanticAddress => ({
    source_key: sourceKey,
    term,
    bounded_context: "urn:stdo:bounded-context:graph-native-odd",
    owning_authority: "urn:stdo:authority:odd-method",
    selected_basis: {
      release_uri: SOURCE_URI,
      installed_manifest_sha256: manifestSha,
    },
    governed_scope: "urn:stdo:scope:reasoning",
  });
  const locator = (fragment: string): SourceLocator => ({
    basis_uri: SOURCE_URI,
    member_path: "ODD_METHOD.md",
    member_sha256: `sha256:${MEMBER_DIGEST}`,
    fragment,
  });
  const frameLocator = (fragment: string): SourceLocator => ({
    basis_uri: SOURCE_URI,
    member_path: "STDO_REFERENCE_FRAME_BASELINE.md",
    member_sha256: `sha256:${"5".repeat(64)}`,
    fragment,
  });
  const contextAddress = address("Graph-native ODD context", "urn:stdo:context:graph-native-odd");
  const authorityAddress = address("ODD semantic authority", "urn:stdo:authority:odd-method");
  const scopeAddress = address("Reasoning scope", "urn:stdo:scope:reasoning");
  const relationAddress = address("constrains", "urn:stdo:relation:constrains");
  const conceptAddress = address("F_P", "urn:stdo:concept:graph-native-odd:f-p");
  const clauseAddress = address("F_P consumer boundary", "urn:stdo:clause:f-p-consumer-boundary");
  const frameAddress = address("Purpose frame", "urn:stdo:reference-frame:purpose");
  const workerAddress = address(
    "Worker engagement role",
    "stdo://releases/v2.4.3-rc.3/standards/STDO_REFERENCE_FRAME_BASELINE.md#worker",
  );
  const contextId = identity("atom", contextAddress);
  const authorityId = identity("atom", authorityAddress);
  const scopeId = identity("atom", scopeAddress);
  const relationId = identity("atom", relationAddress);
  const conceptId = identity("atom", conceptAddress);
  const clauseId = identity("atom", clauseAddress);
  const frameId = identity("atom", frameAddress);
  const workerId = identity("atom", workerAddress);
  const edgeAddress = address("F_P is governed by ODD", "urn:stdo:edge:f-p-governed-by-odd");
  const edgeId = identity("edge", edgeAddress);
  const constraintAddress = address("F_P grants no authority", "urn:stdo:constraint:f-p-no-authority");
  const constraintId = identity("constraint", constraintAddress);
  const records: ProgramRecord[] = [
    { kind: "atom", id: contextId, atom_class: "bounded_context", label: "Graph-native ODD", semantic_address: contextAddress, source_locators: [locator("bounded-context")] },
    { kind: "atom", id: authorityId, atom_class: "authority", label: "ODD Method", semantic_address: authorityAddress, source_locators: [locator("authority")] },
    { kind: "atom", id: scopeId, atom_class: "scope", label: "Reasoning", semantic_address: scopeAddress, source_locators: [locator("scope")] },
    { kind: "atom", id: relationId, atom_class: "relation_kind", label: "constrains", semantic_address: relationAddress, source_locators: [locator("relation")] },
    { kind: "atom", id: conceptId, atom_class: "concept", label: "F_P", semantic_address: conceptAddress, source_locators: [locator("probabilistic-compute/f-p")] },
    { kind: "atom", id: clauseId, atom_class: "clause", label: "F_P consumer boundary", semantic_address: clauseAddress, source_locators: [locator("probabilistic-compute/consumer")] },
    { kind: "atom", id: frameId, atom_class: "reference_frame", label: "Purpose", semantic_address: frameAddress, source_locators: [frameLocator("purpose")] },
    { kind: "atom", id: workerId, atom_class: "role", label: "Worker", semantic_address: workerAddress, source_locators: [frameLocator("worker")] },
    { kind: "edge", id: edgeId, semantic_address: edgeAddress, source_ref: conceptId, relation_kind_ref: relationId, target_ref: authorityId, context_ref: contextId, owner_ref: authorityId, scope_ref: scopeId, cross_context: null, source_locators: [locator("probabilistic-compute/governed-by")] },
    { kind: "constraint", id: constraintId, semantic_address: constraintAddress, constraint_class: "prohibition", statement: "F_P output grants no semantic, decision, operation, acceptance, or closure authority.", applies_to_refs: [conceptId], context_ref: contextId, owner_ref: authorityId, scope_ref: scopeId, declared_latitude: { function_ref: "urn:stdo:concept:graph-native-odd:f-p", decision_owner_ref: authorityId, re_entry_ref: clauseId }, source_locators: [locator("probabilistic-compute/no-authority")] },
  ];
  const sourceOwner = "urn:stdo:authority:odd-method";
  const selections = records.map((record) => {
    const sourceLocators = record.source_locators;
    const selectionRef = `urn:stdo-representation:selection:sha256:${sha256Canonical({
      source_locators: sourceLocators,
      source_owner: sourceOwner,
    } as unknown as JsonValue).slice("sha256:".length)}`;
    return {
      selection_ref: selectionRef,
      source_locators: sourceLocators,
      disposition: "retained",
      representation_refs: [record.id],
      rationale: "Synthetic row exercises exact carrier admission.",
      source_owner: sourceOwner,
      ordered_relation: false,
    } as const;
  }).sort((left, right) => compareUnicodeCodeUnits(left.selection_ref, right.selection_ref));
  const evaluatedMembers = manifestMembers.map((member) => {
    const selectionRefs = selections
      .filter((row) => row.source_locators.some((locator) => locator.member_path === member.path))
      .map((row) => row.selection_ref)
      .sort(compareUnicodeCodeUnits);
    return {
      member_path: member.path,
      member_sha256: `sha256:${member.sha256}`,
      disposition: selectionRefs.length > 0
        ? "contains_retained_material"
        : "contains_no_retained_material",
      selection_refs: selectionRefs,
      rationale: selectionRefs.length > 0
        ? "Carries synthetic retained records."
        : "Synthetic member contains no fixture material.",
    };
  });
  const ledgerBase = {
    kind: "stdo-representation.semantic-selection-ledger",
    schema_version: 1,
    source_stdo_uri: SOURCE_URI,
    source_stdo_manifest_sha256: manifestSha,
    source_member_set_sha256: MEMBER_SET,
    what_member_set_identity: `sha256:${"4".repeat(64)}`,
    build_tenant_identity: "urn:stdo-representation:build-tenant:gtl",
    representation_profile_identity: PROFILE_ID,
    representation_profile_sha256: profileSha,
    representation_records_sha256: sha256Canonical(
      [...records].sort((left, right) =>
        compareUnicodeCodeUnits(left.id, right.id),
      ) as unknown as JsonValue,
    ),
    evaluated_members: evaluatedMembers,
    selections,
    generated_source_keys: [],
    residual_uncertainty: [],
    author: {
      traversal_ref: "urn:stdo:concept:graph-native-odd:f-h",
      actor_identity: "urn:test:actor:owner",
      authority_identity: "urn:test:authority:product",
      grant_identity: "urn:test:grant:select",
      grant_scope: "synthetic conformance selection",
      subject: "synthetic frozen-carrier fixture",
      basis_refs: [SOURCE_URI],
    },
    supersedes: null,
  } as const;
  const ledgerBytes = canonicalBytes(ledgerBase as unknown as JsonValue);
  const ledgerSha = sha256Bytes(ledgerBytes);
  const ledgerIdentity = `urn:stdo-representation:semantic-selection-ledger:sha256:${ledgerSha.slice("sha256:".length)}`;
  const profileAcceptance = acceptance("representation_profile", PROFILE_ID, profileSha);
  const frameAcceptance = acceptance("reference_frame_basis", FRAME_ID, frameSha, true);
  const selectionAcceptance = acceptance("semantic_selection_ledger", ledgerIdentity, ledgerSha);
  const publisherArtifactBytes = encoder.encode("synthetic immutable publisher artifact");
  const publisherArtifactDigest = sha256Bytes(publisherArtifactBytes);
  const publisherMembers = [
    { path: "build/src/contracts.js", sha256: `sha256:${"a".repeat(64)}` },
    { path: "package.json", sha256: `sha256:${"b".repeat(64)}` },
  ];
  const publisherContentDigest = sha256Bytes(
    publisherMembers.map((member) => `${member.path}\0${member.sha256}\n`).join(""),
  );
  const publisherManifest = {
    kind: "stdo-representation.gtl-toolchain-product",
    schema_version: 1,
    repository: "https://example.test/stdo-representation.git",
    commit_sha1: "1".repeat(40),
    tree_sha1: "2".repeat(40),
    artifact_digest: publisherArtifactDigest,
    product_content_digest: publisherContentDigest,
    descriptor_ref: "urn:stdo-representation:descriptor:gtl-toolchain:test",
    contribution_manifest_ref: "urn:stdo-representation:contribution-manifest:gtl-toolchain:test",
    package_name: "@foolishimp/stdo-representation-gtl",
    package_version: "0.1.0-test",
    module_path: "./semantics",
    named_symbol: "STDO_GTL_PRODUCT_SEMANTICS",
    members: publisherMembers,
    supersedes: null,
  } as const;
  const publisherManifestBytes = canonicalBytes(publisherManifest as unknown as JsonValue);
  const publisherManifestDigest = sha256Bytes(publisherManifestBytes);
  const publisherProductId = `urn:stdo-representation:gtl-toolchain-product:sha256:${publisherManifestDigest.slice("sha256:".length)}`;
  const plan: GtlBuildPlan = {
    kind: "stdo-representation.gtl-build-plan",
    schema_version: 1,
    source_stdo: {
      release_uri: SOURCE_URI,
      installed_manifest_sha256: manifestSha,
      standards_member_set_sha256: MEMBER_SET,
    },
    what_member_set_identity: `sha256:${"4".repeat(64)}`,
    representation_profile_identity: PROFILE_ID,
    representation_profile_sha256: profileSha,
    frame_basis_identity: FRAME_ID,
    frame_basis_sha256: frameSha,
    frame_admitting_authority_refs: FRAME_AUTHORITIES,
    semantic_selection_ledger_identity: ledgerIdentity,
    semantic_selection_ledger_sha256: ledgerSha,
    profile_acceptance_identity: profileAcceptance.identity,
    frame_basis_acceptance_identity: frameAcceptance.identity,
    selection_acceptance_identity: selectionAcceptance.identity,
    publisher: {
      owning_product_id: publisherProductId,
      artifact_digest: publisherArtifactDigest,
      product_content_digest: publisherContentDigest,
      product_manifest_digest: publisherManifestDigest,
      descriptor_ref: "urn:stdo-representation:descriptor:gtl-toolchain:test",
      contribution_manifest_ref: "urn:stdo-representation:contribution-manifest:gtl-toolchain:test",
      package_name: "@foolishimp/stdo-representation-gtl",
      package_version: "0.1.0-test",
      module_path: "./semantics",
      named_symbol: "STDO_GTL_PRODUCT_SEMANTICS",
    },
    records,
  };
  const evidence: AcceptedBuildEvidence = {
    source_manifest: manifest,
    source_manifest_bytes: manifestBytes,
    profile_bytes: profileBytes,
    frame_basis_bytes: frameBytes,
    semantic_selection_ledger: ledgerBase,
    semantic_selection_ledger_bytes: ledgerBytes,
    profile_acceptance: profileAcceptance.value,
    profile_acceptance_bytes: profileAcceptance.bytes,
    frame_basis_acceptance: frameAcceptance.value,
    frame_basis_acceptance_bytes: frameAcceptance.bytes,
    selection_acceptance: selectionAcceptance.value,
    selection_acceptance_bytes: selectionAcceptance.bytes,
    publisher_manifest: publisherManifest,
    publisher_manifest_bytes: publisherManifestBytes,
    publisher_artifact_bytes: publisherArtifactBytes,
  };
  return { plan, evidence };
}

test("typed passive ModulePublication survives exact evidence, raw admission, and frozen GTL validation", () => {
  const firstFixture = fixture();
  const secondFixture = fixture();
  const first = constructStdoGtl(firstFixture.plan, firstFixture.evidence);
  const second = constructStdoGtl(secondFixture.plan, secondFixture.evidence);
  assert.deepEqual(first.canonical_bytes, second.canonical_bytes);
  assert.deepEqual(first.receipt, second.receipt);
  assert.equal(first.canonical_bytes.at(-1), 0x0a);
  const publication = JSON.parse(new TextDecoder().decode(first.canonical_bytes));
  assert.equal(publication.kind, "module_publication");
  assert.deepEqual(publication.programs, []);
  assert.deepEqual(publication.graphFunctions, []);
  assert.deepEqual(publication.evaluators, []);
  assert.deepEqual(publication.implementationBindings, []);
  assert.deepEqual(publication.closureContracts, []);
  assert.equal(publication.rules.length, 1);
  assert.equal(publication.rules[0].kind, "stdo.programmatic_semantic_index");
  assert.equal(publication.rules[0].config.a.length, 8);
  assert.equal(publication.rules[0].config.e.length, 1);
  assert.equal(publication.rules[0].config.c.length, 1);
  assert.equal(first.receipt.source_record_counts.atoms, 8);
});

test("domain admission rejects a dangling semantic reference", () => {
  const { plan, evidence } = fixture();
  const edge = plan.records.find((record) => record.kind === "edge");
  assert(edge !== undefined && edge.kind === "edge");
  (edge as { target_ref: string }).target_ref = `urn:stdo-representation:atom:sha256:${"f".repeat(64)}`;
  assert.throws(() => constructStdoGtl(plan, evidence), /dangling or outside I_B/u);
});

test("accepted selection rejects payload drift under unchanged record identities", () => {
  const { plan, evidence } = fixture();
  const constraint = plan.records.find((record) => record.kind === "constraint");
  assert(constraint !== undefined && constraint.kind === "constraint");
  (constraint as { statement: string }).statement =
    "Mutated statement with the same semantic address and record identity.";
  assert.throws(
    () => constructStdoGtl(plan, evidence),
    /representation_records_sha256/u,
  );
});

test("domain admission rejects an identity with the wrong preimage", () => {
  const { plan, evidence } = fixture();
  (plan.records[0] as { id: string }).id = `urn:stdo-representation:atom:sha256:${"e".repeat(64)}`;
  assert.throws(() => constructStdoGtl(plan, evidence), /does not reproduce/u);
});

test("domain admission rejects a record identity with the wrong kind prefix", () => {
  const { plan, evidence } = fixture();
  const edge = plan.records.find((record) => record.kind === "edge");
  assert(edge !== undefined);
  (edge as { id: string }).id = edge.id.replace(":edge:", ":atom:");
  assert.throws(() => constructStdoGtl(plan, evidence), /does not reproduce/u);
});

test("production construction rejects acceptance evidence for another profile", () => {
  const { plan, evidence } = fixture();
  (evidence.profile_acceptance as { subject_sha256: string }).subject_sha256 = `sha256:${"f".repeat(64)}`;
  assert.throws(() => constructStdoGtl(plan, evidence), /not exact RFC 8785|does not accept/u);
});

test("least context closure includes typed dependencies and applicable constraints", () => {
  const { plan } = fixture();
  const edge = plan.records.find((record) => record.kind === "edge");
  const frame = plan.records.find(
    (record) => record.kind === "atom" && record.atom_class === "reference_frame",
  );
  const role = plan.records.find(
    (record) => record.kind === "atom" && record.atom_class === "role",
  );
  assert(edge !== undefined && frame !== undefined && role !== undefined);
  const closure = leastContextClosure(plan.records, [edge.id, frame.id, role.id]);
  assert.deepEqual(
    closure.map((record) => record.id).sort(compareUnicodeCodeUnits),
    plan.records.map((record) => record.id).sort(compareUnicodeCodeUnits),
  );
});

test("role-bound projection derives seeds from an exact canonical assignment", () => {
  const { plan, evidence } = fixture();
  const parent = constructStdoGtl(plan, evidence);
  const frame = plan.records.find(
    (record) => record.kind === "atom" && record.atom_class === "reference_frame",
  );
  const role = plan.records.find(
    (record) => record.kind === "atom" && record.atom_class === "role",
  );
  assert(frame !== undefined && role !== undefined);
  const assignment = {
    kind: "stdo-representation.executive-context-assignment",
    schema_version: 1,
    program_product_identity: parent.receipt.product_identity,
    program_content_identity: parent.receipt.program_content_identity,
    workspace_subject_identity: "urn:test:workspace:subject",
    workspace_basis_refs: ["urn:test:workspace:basis"],
    governed_outcome_ref: "urn:test:outcome:one",
    reasoning_intent_ref: "urn:test:intent:one",
    engagement_role_ref: "stdo://releases/v2.4.3-rc.3/standards/STDO_REFERENCE_FRAME_BASELINE.md#worker",
    target_actor_identity: "urn:test:actor:worker",
    target_capability_envelope_ref: "urn:test:capability:worker",
    assigning_actor_identity: "urn:test:actor:executive",
    frame_set_authority_identity: "urn:test:authority:frames",
    assignment_grant_identity: "urn:test:grant:assignment",
    assignment_grant_scope: "synthetic worker projection",
    frame_activations: [{
      activation_ref: "urn:test:activation:purpose",
      frame_identity: "urn:stdo:reference-frame:purpose",
      frame_sha256: `sha256:${"6".repeat(64)}`,
      mandatory_program_refs: [frame.id],
      evaluation_refs: ["urn:test:evaluation:purpose"],
      required_capability_envelope_ref: "urn:test:capability:worker",
    }],
    role_program_refs: [role.id],
    explicit_program_seed_refs: [],
    inherited_operation_grant_refs: ["urn:test:grant:operation"],
    decision_grant_refs: [],
    required_evidence_refs: ["urn:test:evidence:workspace"],
    stop_state_refs: ["urn:test:stop:return-to-executive"],
    context_budget: {
      tokenizer_identity: "urn:test:tokenizer:one",
      tokenizer_version: "1",
      tokenizer_configuration_sha256: `sha256:${"7".repeat(64)}`,
      model_context_limit_tokens: 8192,
      reserved_non_program_tokens: 2048,
      maximum_projection_tokens: 4096,
    },
    supersedes: null,
  } as const;
  const assignmentBytes = canonicalBytes(assignment as unknown as JsonValue);
  const projection = constructProjectionCandidate(
    plan,
    evidence,
    assignment,
    assignmentBytes,
  );
  assert(projection.included_identity_refs.includes(frame.id));
  assert(projection.included_identity_refs.includes(role.id));
  assert.equal(
    projection.assignment_identity,
    `urn:stdo-representation:executive-context-assignment:sha256:${sha256Bytes(assignmentBytes).slice("sha256:".length)}`,
  );
  assert.equal(JSON.parse(new TextDecoder().decode(projection.canonical_bytes)).kind, "module_publication");
});

test("least context closure does not infer inbound semantic edges", () => {
  const { plan } = fixture();
  const concept = plan.records.find(
    (record) => record.kind === "atom" && record.label === "F_P",
  );
  const edge = plan.records.find((record) => record.kind === "edge");
  assert(concept !== undefined && edge !== undefined);
  const closure = leastContextClosure(plan.records, [concept.id]);
  assert(!closure.some((record) => record.id === edge.id));
  assert(closure.some((record) => record.kind === "constraint"));
});
