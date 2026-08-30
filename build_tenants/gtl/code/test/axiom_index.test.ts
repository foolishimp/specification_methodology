import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { gzipSync } from "node:zlib";

import {
  constructAxiomIndexGtlCandidate,
  decodeAxiomIndexConfig,
  modelRecordRefsForSourceKey,
  recordProvenanceForModelRecord,
  type AcceptedAxiomaticProgram,
  type AxiomIndexGtlInput,
  type AxiomModel,
} from "../src/axiom_index.js";
import { canonicalJson, sha256Bytes, sha256Canonical, type JsonValue } from "../src/canonical.js";
import type { PublisherArtifactBasis } from "../src/contracts.js";

const root = process.env.STDO_REPRESENTATION_ROOT ?? fileURLToPath(new URL("../../../../../", import.meta.url));
const installedManifestPath = "/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/manifest.json";
const encoder = new TextEncoder();
const decoder = new TextDecoder();

const STDO_RELEASE = "stdo://releases/v2.5.0-rc.1/";
const STDO_MANIFEST_SHA = "sha256:3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338";
const STDO_MEMBER_SET_SHA = "sha256:87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5";
const CALCULUS = "urn:stdo:axiomatic-calculus-basis:sha256:bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da";
const SUBJECT = "urn:stdo-representation:subject-basis:stdo:sha256:73f2581c2d8466a2c8e41b842c2178495431ff28450192f00368ec9fff8766a6";
const SUBJECT_SHA = "sha256:73f2581c2d8466a2c8e41b842c2178495431ff28450192f00368ec9fff8766a6";
const WHAT = "sha256:be6f3c244009d319c90588f8b403cd3379d6e135fcb29738d7aa3d49450a5379";
const FRAME = "urn:stdo-representation:reference-frame-basis:source-project:7";
const FRAME_SHA = "sha256:4b32e19c48dfa6df909f174603bbeb43f00559f9bc50b5d8e27a02397b6464c3";
const SIGNATURE = "urn:stdo-index:signature:stdo:7";
const SIGNATURE_SHA = "sha256:c64b731928529b7af3d43d9bb6a19a5524d60bf8c0b30060f0a5da6ffc5dd10a";
const CONTRACT = "urn:stdo-representation:traversal:semantic-compile:7";
const CONTRACT_SHA = "sha256:48ae6fb6bb0b4da6f91c71c0f4ba23a367a38b5b79fbdce54e67dd24c88ce02e";
const MODEL_BASIS = "urn:stdo-index:model-basis:sha256:fd7bf9c54310945240dd4173878d9ff42548b09c7d1f0f9ba5989e18cdc75a34";
const MODEL_EVIDENCE = "urn:stdo-index:evidence:model-basis-preimage:sha256:fd7bf9c54310945240dd4173878d9ff42548b09c7d1f0f9ba5989e18cdc75a34";
const SIGNATURE_EVIDENCE = "urn:stdo-index:evidence:target-signature:sha256:c64b731928529b7af3d43d9bb6a19a5524d60bf8c0b30060f0a5da6ffc5dd10a";
const COMPILE = "urn:stdo-representation:traversal:semantic-compile:7";
const STRUCTURE = "urn:stdo-representation:traversal:candidate-structure:3";
const SELECT = "urn:stdo-representation:traversal:semantic-selection:2";
const ACCEPT_INTERPRETATION = "urn:stdo-representation:traversal:accept-interpretation:1";
const F_D = "urn:stdo:concept:axiomatic-calculus:f-d";
const F_P = "urn:stdo:concept:axiomatic-calculus:f-p";
const OWNER = "https://github.com/foolishimp";
const OWNER_AUTHORITY = "urn:stdo-representation:authority:product-owner";
const OWNER_GRANT = "urn:stdo-representation:grant:product-owner:1";
const OWNER_SCOPE = "Select and accept project-owned frame bases, representation profiles, Source STDO semantic selections, candidate STDO.gtl Products, and tenant-qualified releases; authorize deterministic construction; and issue bounded build-time operation grants for proposal-only semantic-compilation and deterministic structural-evaluation traversals; excludes changing Source STDO or transferring semantic, review, acceptance, release, or runtime authority to a traversal.";
const OWNER_SOURCE = "./specification/PRODUCT.md#product-authority";
const STRUCTURE_EVALUATOR = "urn:stdo-index:evaluator:candidate-structure:4";
const STRUCTURE_GRANT_PREFIX = "urn:stdo-representation:candidate-structure-grant:sha256:";
const STRUCTURE_SCOPE = "Evaluate the exact unchanged SemanticCompilationCandidate under F_D[v_candidate_structure] for declared structural checks only; grants no construction, repair, semantic selection, acceptance, carrier, release, or runtime authority.";
const GRANT_PREFIX = "urn:stdo-index:authority-grant-artifact:sha256:";
const PROFILE = "urn:stdo-index:gtl-profile:axiom-index:7";
const CARRIER_BASIS_PREFIX = "urn:stdo-representation:carrier-basis:gtl:sha256:";
const CARRIER_BASIS = `${CARRIER_BASIS_PREFIX}b5becdf2801577f00bbc119a6bb23e0015a2007147818557ee2e770bc682b703`;
const SCOPE = "urn:test:stdo:scope";

const SORT = {
  authority: "urn:stdo-index:stdo:sort:authority:1",
  context: "urn:stdo-index:stdo:sort:bounded-context:1",
  concept: "urn:stdo-index:stdo:sort:concept:1",
  evidence: "urn:stdo-index:stdo:sort:evidence:1",
  role: "urn:stdo-index:stdo:sort:role:1",
} as const;
const RELATION = "urn:stdo-index:stdo:relation-kind:conserves:1";
const CONSTRAINT = "urn:stdo-index:stdo:constraint-kind:invariant:1";
const RESIDUAL = "urn:stdo-index:stdo:residual-kind:unresolved-semantics:1";
const JUDGMENT = "urn:stdo-index:stdo:judgment-kind:semantic-selection:1";
const STOP = "urn:stdo-index:stdo:stop-kind:accepted:1";
const MODEL_TARGET = "urn:stdo-index:external-target-kind:model-basis:1";
const SIGNATURE_TARGET = "urn:stdo-index:external-target-kind:target-signature-member:1";
const MODEL_RELATION = "urn:stdo-index:basis-relation:exact-model-basis:1";
const SIGNATURE_RELATION = "urn:stdo-index:basis-relation:exact-target-signature:1";

function sorted(values: readonly string[]): string[] {
  return [...values].sort();
}

function artifactBytes(value: unknown): Uint8Array {
  return encoder.encode(`${canonicalJson(value as JsonValue)}\n`);
}

function recordBytes(value: unknown): Uint8Array {
  return encoder.encode(canonicalJson(value as JsonValue));
}

function recordDigest(value: unknown): string {
  return sha256Bytes(recordBytes(value));
}

function contentIdentity(prefix: string, bytes: Uint8Array): string {
  return `${prefix}${sha256Bytes(bytes).slice("sha256:".length)}`;
}

function mutateBytes(value: Uint8Array, framed: boolean, mutate: (record: Record<string, unknown>) => void): Uint8Array {
  const record = JSON.parse(decoder.decode(value)) as Record<string, unknown>;
  mutate(record);
  return framed ? artifactBytes(record) : recordBytes(record);
}

function writeAscii(target: Uint8Array, offset: number, value: string): void {
  target.set(encoder.encode(value), offset);
}

function writeOctal(target: Uint8Array, offset: number, length: number, value: number): void {
  writeAscii(target, offset, `${value.toString(8).padStart(length - 1, "0")}\0`);
}

function npmArchive(members: readonly Readonly<{ path: string; bytes: Uint8Array }>[]): Uint8Array {
  const chunks: Uint8Array[] = [];
  for (const member of members) {
    const header = new Uint8Array(512);
    writeAscii(header, 0, `package/${member.path}`);
    writeOctal(header, 100, 8, 0o644);
    writeOctal(header, 108, 8, 0);
    writeOctal(header, 116, 8, 0);
    writeOctal(header, 124, 12, member.bytes.length);
    writeOctal(header, 136, 12, 0);
    header.fill(0x20, 148, 156);
    header[156] = "0".charCodeAt(0);
    writeAscii(header, 257, "ustar\0");
    writeAscii(header, 263, "00");
    const checksum = header.reduce((sum, byte) => sum + byte, 0);
    writeAscii(header, 148, `${checksum.toString(8).padStart(6, "0")}\0 `);
    chunks.push(header, member.bytes, new Uint8Array((512 - (member.bytes.length % 512)) % 512));
  }
  chunks.push(new Uint8Array(1024));
  return gzipSync(Buffer.concat(chunks.map((chunk) => Buffer.from(chunk))), { level: 9 });
}

function externalModel(model: AxiomModel): Readonly<Record<string, unknown>> {
  return {
    model_basis_identity: model.b,
    identities: model.I,
    semantic_objects: model.O,
    typed_relations: model.E,
    constraints: model.C,
    latitudes: model.L,
    residuals: model.X,
    traversals: model.V,
    transformations: model.T,
    judgments: model.J,
    external_resolutions: model.ResolutionSet_M,
  };
}

function modelFixture(): AxiomModel {
  const authority = "urn:test:stdo:authority";
  const context = "urn:test:stdo:context";
  const concept = "urn:test:stdo:concept";
  const role = "urn:test:stdo:role";
  const objectRows = [
    { id: authority, sort: SORT.authority, context, owner: authority, scope: SCOPE, basis: MODEL_BASIS, value: "authority" },
    { id: context, sort: SORT.context, context, owner: authority, scope: SCOPE, basis: MODEL_BASIS, value: "context" },
    { id: concept, sort: SORT.concept, context, owner: authority, scope: SCOPE, basis: MODEL_BASIS, value: "concept" },
    { id: MODEL_EVIDENCE, sort: SORT.evidence, context, owner: authority, scope: SCOPE, basis: MODEL_BASIS, value: "model_basis_evidence" },
    { id: SIGNATURE_EVIDENCE, sort: SORT.evidence, context, owner: authority, scope: SCOPE, basis: MODEL_BASIS, value: "signature_evidence" },
    { id: role, sort: SORT.role, context, owner: authority, scope: SCOPE, basis: MODEL_BASIS, value: "reviewer" },
  ].sort((left, right) => left.id.localeCompare(right.id));
  const relationRows = [{
    id: "urn:test:stdo:relation",
    kind: RELATION,
    source: concept,
    target: concept,
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    qualifiers: [],
  }];
  const constraintRows = [{
    id: "urn:test:stdo:constraint",
    kind: CONSTRAINT,
    applies_to: concept,
    predicate: "The selected subject remains unchanged.",
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    judgment_kind: JUDGMENT,
    latitude_ref: null,
    refusal: "refusal",
  }];
  const latitudeRows = [{
    id: "urn:test:stdo:latitude",
    applies_to: concept,
    allowed_variation: ["wording"],
    forbidden_variation: ["authority"],
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    invalidation: "semantic_change",
  }];
  const residualRows = [{
    id: "urn:test:stdo:residual",
    subject: concept,
    kind: RESIDUAL,
    uncertainty: "bounded_uncertainty",
    consequence: "review_required",
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    re_entry: "semantic_review",
    invalidation: "evidence_change",
  }, {
    id: "urn:test:stdo:source-native-residual",
    subject: concept,
    kind: RESIDUAL,
    uncertainty: "source_native_uncertainty",
    consequence: "source_reentry_required",
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    re_entry: "source_review",
    invalidation: "source_evidence_change",
  }].sort((left, right) => left.id.localeCompare(right.id));
  const traversalRows = [{
    id: "urn:test:stdo:traversal",
    domain: concept,
    codomain: concept,
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    preconditions: ["subject_available"],
    postconditions: ["subject_unchanged"],
    authority,
    evidence: [MODEL_EVIDENCE],
    provenance: [SIGNATURE_EVIDENCE],
    stop_states: [],
  }];
  const judgmentSubjectDigest = recordDigest(objectRows.find((row) => row.id === concept)!);
  const judgmentRows = [{
    id: "urn:test:stdo:judgment",
    kind: JUDGMENT,
    subject: concept,
    subject_digest: judgmentSubjectDigest,
    context,
    owner: authority,
    scope: SCOPE,
    basis: MODEL_BASIS,
    evaluator: role,
    authority,
    decision: STOP,
    evidence: [MODEL_EVIDENCE],
    provenance: [SIGNATURE_EVIDENCE],
    decided_at: "2026-08-30T00:00:00Z",
  }];
  const signatureResolutions = [
    [SORT.authority, "urn:stdo-index:reference-domain:stdo:sort:1"],
    [SORT.context, "urn:stdo-index:reference-domain:stdo:sort:1"],
    [SORT.concept, "urn:stdo-index:reference-domain:stdo:sort:1"],
    [SORT.evidence, "urn:stdo-index:reference-domain:stdo:sort:1"],
    [SORT.role, "urn:stdo-index:reference-domain:stdo:sort:1"],
    [RELATION, "urn:stdo-index:reference-domain:stdo:relation-kind:1"],
    [CONSTRAINT, "urn:stdo-index:reference-domain:stdo:constraint-kind:1"],
    [RESIDUAL, "urn:stdo-index:reference-domain:stdo:residual-kind:1"],
    [JUDGMENT, "urn:stdo-index:reference-domain:stdo:judgment-kind:1"],
  ].map(([external_identity, reference_domain]) => ({
    external_identity: external_identity!,
    reference_domain: reference_domain!,
    external_target_kind: SIGNATURE_TARGET,
    resolved_target_identity: external_identity!,
    basis_relation: SIGNATURE_RELATION,
    resolution_basis: SIGNATURE,
    evidence_identity: SIGNATURE_EVIDENCE,
  }));
  const resolutions = [{
    external_identity: MODEL_BASIS,
    reference_domain: "urn:stdo-index:reference-domain:model-basis:1",
    external_target_kind: MODEL_TARGET,
    resolved_target_identity: MODEL_BASIS,
    basis_relation: MODEL_RELATION,
    resolution_basis: CALCULUS,
    evidence_identity: MODEL_EVIDENCE,
  }, ...signatureResolutions].sort((left, right) => left.external_identity.localeCompare(right.external_identity));
  const localIdentities = [...objectRows, ...relationRows, ...constraintRows, ...latitudeRows, ...residualRows, ...traversalRows, ...judgmentRows].map((row) => row.id);
  return {
    b: MODEL_BASIS,
    I: sorted([...localIdentities, ...resolutions.map((row) => row.external_identity)]),
    O: objectRows,
    E: relationRows,
    C: constraintRows,
    L: latitudeRows,
    X: residualRows,
    V: traversalRows,
    T: [],
    J: judgmentRows,
    ResolutionSet_M: resolutions,
  };
}

interface BuiltFixture {
  readonly input: AxiomIndexGtlInput;
  readonly program: AcceptedAxiomaticProgram;
  readonly semanticJudgmentIdentity: string;
  readonly identities: Readonly<{
    selection: string;
    replacementSelection: string;
    compilationResidual: string;
    firstModelResidual: string;
    generatedSourceKey: string;
  }>;
}

interface FixtureOptions {
  readonly proposalIdentityCollision?: "selection_model" | "residual_selection" | "selection_evaluated_member";
  readonly selectionDisposition?: "retained" | "omitted" | "uncertain" | "inapplicable" | "refused";
  readonly evaluatedFirstDisposition?: "contains_retained_material" | "contains_no_retained_material" | "uncertain" | "inapplicable" | "refused";
  readonly compilationResidualModelRefs?: "exact" | "empty" | "unresolved";
  readonly ledgerResidualDecision?: "accepted_unchanged" | "retained_uncertain" | "resolved" | "rejected";
  readonly ledgerSelectionDecision?: "accepted_unchanged" | "accepted_modified";
  readonly mixedMemberDispositions?: boolean;
}

function fixture(options: FixtureOptions = {}): BuiltFixture {
  const sourceManifestBytes = readFileSync(installedManifestPath);
  assert.equal(sha256Bytes(sourceManifestBytes), STDO_MANIFEST_SHA);
  const sourceManifest = JSON.parse(decoder.decode(sourceManifestBytes)) as {
    standards: { members: readonly { path: string; sha256: string }[] };
  };
  const sourceMembers = sourceManifest.standards.members.map((row) => ({ member_path: row.path, member_sha256: `sha256:${row.sha256}` }));
  assert.equal(sourceMembers.length, 51);
  const targetSignatureBytes = readFileSync(`${root}/build_tenants/semantic_compile/profile/stdo-signature.json`);
  const interpretationContractBytes = readFileSync(`${root}/build_tenants/semantic_compile/contract/v_compile.json`);
  const frameBasisBytes = readFileSync(`${root}/specification/REFERENCE_FRAME_BASIS.md`);
  assert.equal(sha256Bytes(targetSignatureBytes), SIGNATURE_SHA);
  assert.equal(sha256Bytes(interpretationContractBytes), CONTRACT_SHA);
  assert.equal(sha256Bytes(frameBasisBytes), FRAME_SHA);

  const model = modelFixture();
  const candidateModel = externalModel(model);
  const modelContentIdentity = recordDigest(candidateModel);
  const localIds = sorted([...model.O, ...model.E, ...model.C, ...model.L, ...model.X, ...model.V, ...model.T, ...model.J].map((row) => row.id));
  const firstMember = sourceMembers[0]!;
  const secondMember = sourceMembers[1]!;
  const firstMemberIdentity = `${STDO_RELEASE}standards/${firstMember.member_path}`;
  const selectionRef = options.proposalIdentityCollision === "selection_model"
    ? localIds[0]!
    : options.proposalIdentityCollision === "selection_evaluated_member"
      ? firstMemberIdentity
      : "urn:test:stdo:selection:1";
  const residualSelectionRef = "urn:test:stdo:selection:residual";
  const replacementSelectionRef = "urn:test:stdo:selection:replacement";
  const compilationResidualRef = options.proposalIdentityCollision === "residual_selection" ? selectionRef : "urn:test:stdo:compilation-residual:1";
  const locator = { basis_uri: STDO_RELEASE, member_path: firstMember.member_path, member_sha256: firstMember.member_sha256, fragment: null };
  const residualLocator = { basis_uri: STDO_RELEASE, member_path: secondMember.member_path, member_sha256: secondMember.member_sha256, fragment: null };
  const generatedLocalDeclarationKey = "generated-record-address";
  const generatedSourceKey = `urn:stdo-representation:source-key:sha256:${recordDigest({ primary_source_locator: locator, local_declaration_key: generatedLocalDeclarationKey }).slice("sha256:".length)}`;
  const localRecords = [...model.O, ...model.E, ...model.C, ...model.L, ...model.X, ...model.V, ...model.T, ...model.J]
    .sort((left, right) => left.id.localeCompare(right.id));
  const recordProvenance = localRecords.map((row, index) => {
    const rowLocator = options.mixedMemberDispositions && model.X.some((residual) => residual.id === row.id) ? residualLocator : locator;
    return {
      model_record_ref: row.id,
      provenance_kind: "subject_derived" as const,
      semantic_address: {
        source_key: index === 0 ? generatedSourceKey : `${STDO_RELEASE}standards/${rowLocator.member_path}`,
        term: row.id,
        bounded_context: row.context,
        owning_authority: row.owner,
        selected_basis: SUBJECT,
        governed_scope: row.scope,
      },
      source_locators: [rowLocator],
      derivation_evidence_refs: [],
    };
  });
  const proposedGeneratedSourceKeys = [{
    source_key: generatedSourceKey,
    primary_source_locator: locator,
    local_declaration_key: generatedLocalDeclarationKey,
  }];
  const nonResidualIds = localIds.filter((identity) => !model.X.some((row) => row.id === identity));
  const proposedSelections = [{
    selection_ref: selectionRef,
    source_locators: [locator],
    disposition: options.selectionDisposition ?? "retained",
    model_record_refs: options.mixedMemberDispositions ? nonResidualIds : localIds,
    rationale: "Owns the complete bounded model fixture.",
    source_owner: OWNER_AUTHORITY,
  }, ...(options.mixedMemberDispositions ? [{
    selection_ref: residualSelectionRef,
    source_locators: [residualLocator],
    disposition: "retained",
    model_record_refs: model.X.map((row) => row.id),
    rationale: "Owns the explicit bounded residual population.",
    source_owner: OWNER_AUTHORITY,
  }] : [])].sort((left, right) => left.selection_ref.localeCompare(right.selection_ref));
  const evaluatedMembers = sourceMembers.map((member, index) => ({
    disposition: index === 0
      ? (options.evaluatedFirstDisposition ?? "contains_retained_material")
      : options.mixedMemberDispositions && index === 1
        ? "uncertain"
        : "inapplicable",
    member_path: member.member_path,
    member_sha256: member.member_sha256,
    rationale: index === 0 ? "The bounded fixture is sourced here." : options.mixedMemberDispositions && index === 1 ? "The explicit residual population is sourced here." : "No additional fixture content is selected.",
    selection_refs: index === 0 ? [selectionRef] : options.mixedMemberDispositions && index === 1 ? [residualSelectionRef] : [],
  }));
  const compilationResiduals = [{
    residual_ref: compilationResidualRef,
    source_locators: [locator],
    statement: "The bounded fixture retains one explicit uncertainty.",
    consequence: "Semantic review remains required.",
    model_residual_refs: options.compilationResidualModelRefs === "empty"
      ? []
      : options.compilationResidualModelRefs === "unresolved"
        ? ["urn:test:stdo:missing-model-residual"]
        : [model.X[0]!.id],
    re_entry_route: "Return through semantic selection.",
  }];
  const payload = {
    calculus_basis_identity: CALCULUS,
    source_stdo_uri: STDO_RELEASE,
    source_stdo_manifest_sha256: STDO_MANIFEST_SHA,
    source_member_set_sha256: STDO_MEMBER_SET_SHA,
    source_members: sourceMembers,
    subject_basis_identity: SUBJECT,
    what_member_set_identity: WHAT,
    signature_identity: SIGNATURE,
    signature_sha256: SIGNATURE_SHA,
    interpretation_contract_identity: CONTRACT,
    interpretation_contract_sha256: CONTRACT_SHA,
    frame_basis_identity: FRAME,
    frame_basis_sha256: FRAME_SHA,
    selected_frame_refs: ["urn:stdo-representation:frame:semantic-compilation"],
    candidate_model: candidateModel,
    candidate_model_content_identity: modelContentIdentity,
    proposed_record_provenance: recordProvenance,
    proposed_evaluated_members: evaluatedMembers,
    proposed_selections: proposedSelections,
    proposed_generated_source_keys: proposedGeneratedSourceKeys,
    compilation_residuals: compilationResiduals,
    stop_state: "urn:stdo-index:stdo:stop-kind:candidate:1",
  };
  const proposal = { kind: "stdo-representation.semantic-compilation-proposal", schema_version: 2, payload };
  const proposalBytes = artifactBytes(proposal);
  const compilerProvenanceKinds = [
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
  const compilerProvenanceEntries = compilerProvenanceKinds.map((memberKind) => {
    const memberRef = memberKind === "capability_envelope"
      ? "urn:axiom-indexer:capability:semantic-compilation-prototype:1"
      : `urn:test:compiler-provenance:${memberKind}:1`;
    const bytes = recordBytes({ kind: `stdo-index.test-${memberKind}`, schema_version: 1, member_ref: memberRef });
    return { memberKind, memberRef, bytes };
  });
  const compilerProvenanceMemberBytes = Object.fromEntries(compilerProvenanceEntries.map((entry) => [entry.memberRef, entry.bytes]));
  const compilerProvenanceBundleBytes = recordBytes({
    kind: "stdo-representation.compiler-provenance-bundle",
    schema_version: 1,
    members: compilerProvenanceEntries.map((entry) => ({
      member_kind: entry.memberKind,
      member_ref: entry.memberRef,
      member_sha256: sha256Bytes(entry.bytes),
    })),
  });
  const sealedInvocationSha256 = sha256Bytes(compilerProvenanceEntries.find((entry) => entry.memberKind === "sealed_invocation")!.bytes);
  const candidate = {
    kind: "stdo-representation.semantic-compilation-candidate",
    schema_version: 3,
    proposal_content_sha256: recordDigest(proposal),
    compiler_invocation: {
      topology: "single_invocation",
      traversal_ref: COMPILE,
      functor_ref: F_P,
      host_identity: "urn:test:compiler-host:1",
      model_identity: "test-model",
      model_configuration_sha256: `sha256:${"1".repeat(64)}`,
      instruction_sha256: sealedInvocationSha256,
      capability_envelope_ref: "urn:axiom-indexer:capability:semantic-compilation-prototype:1",
      context_budget_tokens: 100_000,
      invoked_at: "2026-08-30T00:00:00Z",
      raw_output_ref: "urn:test:semantic-compilation-proposal:1",
      raw_output_sha256: sha256Bytes(proposalBytes),
      provenance_ref: "urn:test:semantic-compilation-run:1",
      provenance_sha256: sha256Bytes(compilerProvenanceBundleBytes),
    },
    ...payload,
  };
  const candidateBytes = artifactBytes(candidate);
  const candidateDigest = recordDigest(candidate);
  const candidateIdentity = `urn:stdo-representation:semantic-compilation-candidate:sha256:${candidateDigest.slice("sha256:".length)}`;

  const stableBasis = sorted([CALCULUS, FRAME, CONTRACT, SUBJECT, SIGNATURE, WHAT]);
  const structureGrantSourceBytes = readFileSync(`${root}/specification/PRODUCT.md`);
  const structureGrant = {
    kind: "stdo-representation.candidate-structure-evaluation-grant",
    schema_version: 1,
    parent_grant_identity: OWNER_GRANT,
    issuer_actor_identity: OWNER,
    authority_identity: OWNER_AUTHORITY,
    grantee_identity: STRUCTURE_EVALUATOR,
    grant_scope: STRUCTURE_SCOPE,
    traversal_ref: STRUCTURE,
    functor_ref: F_D,
    subject_identity: candidateIdentity,
    subject_sha256: candidateDigest,
    calculus_basis_identity: CALCULUS,
    signature_identity: SIGNATURE,
    signature_sha256: SIGNATURE_SHA,
    interpretation_contract_identity: CONTRACT,
    interpretation_contract_sha256: CONTRACT_SHA,
    what_member_set_identity: WHAT,
    frame_basis_identity: FRAME,
    frame_basis_sha256: FRAME_SHA,
    evidence_refs: [candidateIdentity],
    issued_at: "2026-08-30T00:00:30Z",
    source_ref: OWNER_SOURCE,
    source_sha256: sha256Bytes(structureGrantSourceBytes),
  };
  const structureGrantBytes = recordBytes(structureGrant);
  const structureGrantIdentity = contentIdentity(STRUCTURE_GRANT_PREFIX, structureGrantBytes);
  const structureResult = {
    kind: "stdo-representation.candidate-structure-result",
    schema_version: 2,
    semantic_compilation_candidate_identity: candidateIdentity,
    semantic_compilation_candidate_sha256: candidateDigest,
    calculus_basis_identity: CALCULUS,
    signature_identity: SIGNATURE,
    interpretation_contract_identity: CONTRACT,
    traversal_ref: STRUCTURE,
    functor_ref: F_D,
    evaluator_identity: STRUCTURE_EVALUATOR,
    checks: {
      canonical_bytes: true,
      source_inventory: true,
      population_totality: true,
      record_shapes: true,
      identity_derivation: true,
      reference_domains: true,
      external_resolutions: true,
      basis_coherence: true,
      ordering: true,
      provenance_binding: true,
    },
    decision: "eligible",
    evaluated_at: "2026-08-30T00:01:00Z",
    evidence_refs: [structureGrantIdentity],
  };
  const structureBytes = artifactBytes(structureResult);
  const structureDigest = recordDigest(structureResult);
  const structureIdentity = `urn:stdo-representation:candidate-structure-result:sha256:${structureDigest.slice("sha256:".length)}`;

  const ledgerSelectionDecision = options.ledgerSelectionDecision ?? "accepted_unchanged";
  const finalSelectionRef = ledgerSelectionDecision === "accepted_modified" ? replacementSelectionRef : selectionRef;
  const finalSelections = proposedSelections.map((row) => ({
    ...row,
    selection_ref: row.selection_ref === selectionRef ? finalSelectionRef : row.selection_ref,
    rationale: ledgerSelectionDecision === "accepted_modified" && row.selection_ref === selectionRef ? "Accepted with an exact final selection-row replacement." : row.rationale,
  }));
  const finalEvaluatedMembers = evaluatedMembers.map((row) => ({
    ...row,
    selection_refs: row.selection_refs.map((ref) => ref === selectionRef ? finalSelectionRef : ref),
  }));
  const ledgerResidualDecision = options.ledgerResidualDecision ?? "retained_uncertain";
  const finalCompilationResiduals = ledgerResidualDecision === "accepted_unchanged" ? compilationResiduals : [];
  const sourceBindings = sourceMembers.map((member, index) => ({
    member_path: member.member_path,
    member_sha256: member.member_sha256,
    disposition: index === 0
      ? "retained" as const
      : options.mixedMemberDispositions && index === 1
        ? "represented_by_residual" as const
        : "inapplicable" as const,
    model_refs: index === 0 ? (options.mixedMemberDispositions ? nonResidualIds : localIds) : options.mixedMemberDispositions && index === 1 ? model.X.map((row) => row.id) : [],
    residual_refs: index === 0 ? (options.mixedMemberDispositions ? [] : model.X.map((row) => row.id)) : options.mixedMemberDispositions && index === 1 ? model.X.map((row) => row.id) : [],
    reason_code: index === 0 ? "modeled" as const : options.mixedMemberDispositions && index === 1 ? "unresolved" as const : "excluded_by_contract" as const,
  }));
  const program: AcceptedAxiomaticProgram = {
    kind: "axiom-indexer.axiomatic-program",
    schema_version: 2,
    model_content_identity: modelContentIdentity,
    basis: {
      corpus: { identity: STDO_RELEASE, sha256: STDO_MANIFEST_SHA },
      calculus: { identity: CALCULUS, sha256: `sha256:${CALCULUS.slice(CALCULUS.lastIndexOf(":") + 1)}` },
      subject_basis: { identity: SUBJECT, sha256: SUBJECT_SHA },
      target_profile: { identity: SIGNATURE, sha256: SIGNATURE_SHA },
      interpretation_contract: { identity: CONTRACT, sha256: CONTRACT_SHA },
      semantic_compilation_candidate: { identity: candidateIdentity, sha256: candidateDigest },
      candidate_structure_result: { identity: structureIdentity, sha256: structureDigest },
    },
    model,
    record_provenance: recordProvenance,
    source_bindings: sourceBindings,
  };
  const programBytes = artifactBytes(program);
  const programIdentity = contentIdentity("urn:stdo-index:axiomatic-program:sha256:", programBytes);

  const semanticGrantSourceBytes = readFileSync(`${root}/specification/PRODUCT.md`);
  const semanticGrant = {
    kind: "stdo-index.authority-grant",
    schema_version: 1,
    grant_identity: OWNER_GRANT,
    actor_identity: OWNER,
    authority_identity: OWNER_AUTHORITY,
    grant_scope: OWNER_SCOPE,
    basis_refs: stableBasis,
    source_ref: OWNER_SOURCE,
    source_sha256: sha256Bytes(semanticGrantSourceBytes),
  };
  const semanticGrantBytes = recordBytes(semanticGrant);
  const semanticGrantIdentity = contentIdentity(GRANT_PREFIX, semanticGrantBytes);
  const proposalDispositions = [
    ...evaluatedMembers.map((row, index) => {
      const proposal_ref = `${STDO_RELEASE}standards/${sourceMembers[index]!.member_path}`;
      const modified = canonicalJson(row as unknown as JsonValue) !== canonicalJson(finalEvaluatedMembers[index] as unknown as JsonValue);
      return {
        proposal_ref,
        proposal_kind: "evaluated_member",
        decision: modified ? "accepted_modified" : "accepted_unchanged",
        final_refs: [proposal_ref],
        rationale: modified ? "Accepted with an exact final evaluated-member replacement." : "Accepted unchanged.",
      };
    }),
    ...localIds.map((proposal_ref) => ({ proposal_ref, proposal_kind: "model_record", decision: "accepted_unchanged", final_refs: [proposal_ref], rationale: "Accepted unchanged." })),
    ...proposedSelections.map((selection) => ({
      proposal_ref: selection.selection_ref,
      proposal_kind: "selection",
      decision: selection.selection_ref === selectionRef ? ledgerSelectionDecision : "accepted_unchanged",
      final_refs: [selection.selection_ref === selectionRef ? finalSelectionRef : selection.selection_ref],
      rationale: selection.selection_ref === selectionRef && ledgerSelectionDecision === "accepted_modified" ? "Accepted with an exact final replacement." : "Accepted unchanged.",
    })),
    { proposal_ref: generatedSourceKey, proposal_kind: "generated_source_key", decision: "accepted_unchanged", final_refs: [generatedSourceKey], rationale: "Accepted unchanged." },
    {
      proposal_ref: compilationResidualRef,
      proposal_kind: "compilation_residual",
      decision: ledgerResidualDecision,
      final_refs: ledgerResidualDecision === "accepted_unchanged"
        ? [compilationResidualRef]
        : ledgerResidualDecision === "retained_uncertain"
          ? [model.X[0]!.id]
          : [],
      rationale: ledgerResidualDecision === "retained_uncertain" ? "Uncertainty remains explicit in model X." : `Compilation residual ${ledgerResidualDecision}.`,
    },
  ].sort((left, right) => left.proposal_ref < right.proposal_ref ? -1 : left.proposal_ref > right.proposal_ref ? 1 : 0);
  const ledger = {
    kind: "stdo-representation.semantic-selection-ledger",
    schema_version: 3,
    calculus_basis_identity: CALCULUS,
    subject_basis_identity: SUBJECT,
    source_stdo_uri: STDO_RELEASE,
    source_stdo_manifest_sha256: STDO_MANIFEST_SHA,
    source_member_set_sha256: STDO_MEMBER_SET_SHA,
    what_member_set_identity: WHAT,
    signature_identity: SIGNATURE,
    interpretation_contract_identity: CONTRACT,
    semantic_compilation_candidate_identity: candidateIdentity,
    semantic_compilation_candidate_sha256: candidateDigest,
    candidate_structure_result_identity: structureIdentity,
    candidate_structure_result_sha256: structureDigest,
    candidate_model_content_identity: modelContentIdentity,
    record_provenance: recordProvenance,
    evaluated_members: finalEvaluatedMembers,
    selections: finalSelections,
    generated_source_keys: proposedGeneratedSourceKeys,
    compilation_residuals: finalCompilationResiduals,
    proposal_dispositions: proposalDispositions,
    author: {
      traversal_ref: SELECT,
      actor_identity: OWNER,
      authority_identity: OWNER_AUTHORITY,
      grant_identity: OWNER_GRANT,
      grant_scope: OWNER_SCOPE,
      subject_identity: candidateIdentity,
      subject_sha256: candidateDigest,
      basis_refs: sorted([...stableBasis, candidateIdentity, structureIdentity]),
      decided_at: "2026-08-30T00:02:00Z",
      evidence_refs: sorted([candidateIdentity, semanticGrantIdentity, structureIdentity]),
    },
    supersedes: null,
  };
  const ledgerBytes = recordBytes(ledger);
  const ledgerDigest = sha256Bytes(ledgerBytes);
  const ledgerIdentity = `urn:stdo-representation:semantic-selection-ledger:sha256:${ledgerDigest.slice("sha256:".length)}`;
  const interpretedCoordinate = {
    calculus_basis_identity: CALCULUS,
    subject_basis_identity: SUBJECT,
    signature_identity: SIGNATURE,
    interpretation_contract_identity: CONTRACT,
    model_content_identity: modelContentIdentity,
    semantic_selection_ledger_identity: ledgerIdentity,
    semantic_selection_ledger_sha256: ledgerDigest,
  };
  const interpretedDigest = recordDigest(interpretedCoordinate);
  const interpretedIdentity = `urn:stdo-representation:a-c-stdo:sha256:${interpretedDigest.slice("sha256:".length)}`;
  const judgment = {
    kind: "stdo-representation.authority-acceptance",
    schema_version: 1,
    subject_kind: "interpreted_model",
    subject_identity: interpretedIdentity,
    subject_sha256: modelContentIdentity,
    traversal_ref: ACCEPT_INTERPRETATION,
    actor_identity: OWNER,
    authority_identity: OWNER_AUTHORITY,
    grant_identity: OWNER_GRANT,
    grant_scope: OWNER_SCOPE,
    basis_refs: sorted([...stableBasis, ledgerIdentity, candidateIdentity, programIdentity, structureIdentity]),
    admitting_authority_refs: null,
    evidence_refs: sorted([semanticGrantIdentity, ledgerIdentity, candidateIdentity, programIdentity, structureIdentity]),
    decision: "accepted",
    decided_at: "2026-08-30T00:03:00Z",
    supersedes: null,
  };
  const judgmentBytes = recordBytes(judgment);
  const semanticJudgmentIdentity = contentIdentity("urn:stdo-representation:authority-acceptance:sha256:", judgmentBytes);

  const publisherMembers = [
    { path: "build/src/axiom_index.js", bytes: encoder.encode("export const encodedAxiomIndex = true;\n") },
    { path: "build/src/index.js", bytes: encoder.encode("export const STDO_AXIOM_INDEX_GTL_PRODUCT_SEMANTICS = Object.freeze({kind: 'test'});\n") },
    { path: "package.json", bytes: recordBytes({ name: "@foolishimp/stdo-representation-gtl", version: "0.1.0", type: "module", exports: { ".": { import: "./build/src/index.js" } } }) },
  ];
  const publisherArtifactBytes = npmArchive(publisherMembers);
  const publisherMemberRows = publisherMembers.map((member) => ({ path: member.path, sha256: sha256Bytes(member.bytes) }));
  const productContentDigest = sha256Bytes(publisherMemberRows.map((row) => `${row.path}\0${row.sha256}\n`).join(""));
  const publisherManifest = {
    kind: "stdo-representation.gtl-toolchain-product",
    schema_version: 2,
    repository: "https://github.com/foolishimp/stdo_representation.git",
    commit_sha1: "1".repeat(40),
    tree_sha1: "2".repeat(40),
    carrier_basis: {
      identity: CARRIER_BASIS,
      repository: "https://github.com/foolishimp/abiogenesis.git",
      commit_sha1: "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
      authority_root: "specification/requirements/gtl/",
      authority_tree_sha1: "21a44b1941a1055d6abd973937e65b83e359de1b",
      authority_inventory_count: 33,
    },
    artifact_digest: sha256Bytes(publisherArtifactBytes),
    product_content_digest: productContentDigest,
    descriptor_ref: "urn:test:publisher:descriptor:1",
    contribution_manifest_ref: "urn:test:publisher:contributions:1",
    package_name: "@foolishimp/stdo-representation-gtl",
    package_version: "0.1.0",
    module_path: ".",
    named_symbol: "STDO_AXIOM_INDEX_GTL_PRODUCT_SEMANTICS",
    members: publisherMemberRows,
    supersedes: null,
  };
  const publisherManifestBytes = recordBytes(publisherManifest);
  const publisherManifestDigest = sha256Bytes(publisherManifestBytes);
  const publisher: PublisherArtifactBasis = {
    owning_product_id: `urn:stdo-representation:gtl-toolchain-product:sha256:${publisherManifestDigest.slice("sha256:".length)}`,
    artifact_digest: publisherManifest.artifact_digest,
    product_content_digest: productContentDigest,
    product_manifest_digest: publisherManifestDigest,
    descriptor_ref: publisherManifest.descriptor_ref,
    contribution_manifest_ref: publisherManifest.contribution_manifest_ref,
    package_name: publisherManifest.package_name,
    package_version: publisherManifest.package_version,
    module_path: publisherManifest.module_path,
    named_symbol: publisherManifest.named_symbol,
  };
  return {
    program,
    semanticJudgmentIdentity,
    identities: {
      selection: selectionRef,
      replacementSelection: replacementSelectionRef,
      compilationResidual: compilationResidualRef,
      firstModelResidual: model.X[0]!.id,
      generatedSourceKey,
    },
    input: {
      semantic_compilation_proposal_bytes: proposalBytes,
      semantic_compilation_candidate_bytes: candidateBytes,
      compiler_provenance_bundle_bytes: compilerProvenanceBundleBytes,
      compiler_provenance_member_bytes: compilerProvenanceMemberBytes,
      accepted_program_bytes: programBytes,
      selection_ledger_bytes: ledgerBytes,
      semantic_judgment_bytes: judgmentBytes,
      candidate_structure_result_bytes: structureBytes,
      source_manifest_bytes: sourceManifestBytes,
      target_signature_bytes: targetSignatureBytes,
      interpretation_contract_bytes: interpretationContractBytes,
      frame_basis_bytes: frameBasisBytes,
      structure_grant_bytes: structureGrantBytes,
      structure_grant_source_bytes: structureGrantSourceBytes,
      semantic_grant_bytes: semanticGrantBytes,
      semantic_grant_source_bytes: semanticGrantSourceBytes,
      profile_bytes: readFileSync(`${root}/build_tenants/gtl/design/GTL_AXIOM_INDEX_PROFILE.json`),
      publisher,
      publisher_manifest_bytes: publisherManifestBytes,
      publisher_artifact_bytes: publisherArtifactBytes,
    },
  };
}

test("the exact accepted O/E/C/L/X/V/T/J model, P_B, and ResolutionSet_M round-trip losslessly", () => {
  const { input, program, identities } = fixture();
  const first = constructAxiomIndexGtlCandidate(input);
  const second = constructAxiomIndexGtlCandidate(input);
  assert.deepEqual(first.canonical_bytes, second.canonical_bytes);
  assert.equal(first.receipt.frozen_gtl_validation, "valid");
  assert.equal(first.receipt.profile_round_trip, "valid");
  assert.equal(first.receipt.carrier_admission, "not_evaluated");
  const config = first.publication.rules[0]!.config as Readonly<Record<string, unknown>>;
  assert.equal(config.v, 4);
  for (const [field, expected] of [["o", program.model.O.length], ["e", program.model.E.length], ["c", program.model.C.length], ["l", program.model.L.length], ["x", program.model.X.length], ["V", program.model.V.length], ["T", 0], ["J", program.model.J.length], ["q", program.model.ResolutionSet_M.length], ["p", program.record_provenance.length], ["r", 51]] as const) {
    assert.equal((config[field] as readonly unknown[]).length, expected);
  }
  const decoded = decodeAxiomIndexConfig(config, input.target_signature_bytes, input.source_manifest_bytes, input.profile_bytes);
  assert.equal(canonicalJson(decoded as unknown as JsonValue), canonicalJson(program as unknown as JsonValue));
  assert.equal(program.model.X.length, 2, "a lawful source-native X need not be introduced by compiler uncertainty");
  const generatedBinding = program.record_provenance.find((row) => row.semantic_address.source_key === identities.generatedSourceKey)!;
  assert.deepEqual(modelRecordRefsForSourceKey(decoded, identities.generatedSourceKey), [generatedBinding.model_record_ref]);
  assert.deepEqual(recordProvenanceForModelRecord(decoded, generatedBinding.model_record_ref), generatedBinding);
});

test("profile 7 is a self-contained exact GTL tenant and carrier contract", () => {
  const profileBytes = readFileSync(`${root}/build_tenants/gtl/design/GTL_AXIOM_INDEX_PROFILE.json`);
  const profile = JSON.parse(decoder.decode(profileBytes)) as {
    identity: string;
    build_tenant: { identity: string; carrier_basis: { identity: string; coordinate: Record<string, JsonValue> } };
    canonicalization: { carrier_value_algorithm: string; artifact_framing: { suffix_hex: string; suffix_in_program_content_identity: boolean }; number_domain: string };
    publication_contract: { module_publication: { raw_admission_contract_ref: string; inventory_cardinality: Record<string, number> }; record_contract: { contract_ref: string }; rule: { kind: string }; contribution: { kind: string } };
    configuration: { version: number; tuple_schemas: Record<string, { fields: string[]; types: string[] }> };
  };
  const coordinateDigest = sha256Canonical(profile.build_tenant.carrier_basis.coordinate);
  assert.equal(profile.identity, PROFILE);
  assert.equal(profile.build_tenant.identity, "urn:stdo-representation:build-tenant:gtl");
  assert.equal(`${CARRIER_BASIS_PREFIX}${coordinateDigest.slice("sha256:".length)}`, CARRIER_BASIS);
  assert.equal(profile.build_tenant.carrier_basis.identity, CARRIER_BASIS);
  assert.deepEqual(profile.build_tenant.carrier_basis.coordinate, {
    authority_inventory_count: 33,
    authority_root: "specification/requirements/gtl/",
    authority_tree_sha1: "21a44b1941a1055d6abd973937e65b83e359de1b",
    commit_sha1: "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
    repository: "https://github.com/foolishimp/abiogenesis.git",
  });
  assert.equal(profile.canonicalization.carrier_value_algorithm, "RFC8785_JCS");
  assert.deepEqual(profile.canonicalization.artifact_framing, { prefix_hex: "", suffix_hex: "0a", suffix_in_program_content_identity: true });
  assert.equal(profile.canonicalization.number_domain, "non_negative_safe_integers_excluding_negative_zero");
  assert.equal(profile.publication_contract.module_publication.raw_admission_contract_ref, "urn:abiogenesis:contract:gtl:module-publication:5.0.0");
  assert.deepEqual(profile.publication_contract.module_publication.inventory_cardinality, { contracts: 1, evaluators: 0, rules: 1, implementationBindings: 0, closureContracts: 0, programs: 0, graphFunctions: 0, contributions: 1 });
  assert.equal(profile.publication_contract.record_contract.contract_ref, "urn:stdo-index:gtl-contract:axiom-index:4");
  assert.equal(profile.publication_contract.rule.kind, "stdo.axiom_index");
  assert.equal(profile.publication_contract.contribution.kind, "node_type");
  assert.equal(profile.configuration.version, 4);
  assert.deepEqual(Object.keys(profile.configuration.tuple_schemas).sort(), ["J", "T", "V", "c", "e", "l", "m", "o", "p", "q", "r", "source_locator", "x"].sort());
  for (const schema of Object.values(profile.configuration.tuple_schemas)) assert.equal(schema.fields.length, schema.types.length);
});

test("the exact 51-member STDO source and frozen signature/contract/frame bases are load-bearing", () => {
  const { input } = fixture();
  const missingMember = mutateBytes(input.semantic_compilation_candidate_bytes, true, (candidate) => {
    (candidate.source_members as unknown[]).pop();
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, semantic_compilation_candidate_bytes: missingMember }), /complete exact installed subject inventory|unchanged exact proposal payload/u);
  const changedSignature = new Uint8Array(input.target_signature_bytes);
  const signatureIndex = changedSignature.length - 2;
  changedSignature[signatureIndex] = (changedSignature[signatureIndex] ?? 0) ^ 1;
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, target_signature_bytes: changedSignature }), /frozen STDO 2\.5 target signature|signature coordinate/u);
  const changedFrame = new Uint8Array(input.frame_basis_bytes);
  changedFrame[0] = (changedFrame[0] ?? 0) ^ 1;
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, frame_basis_bytes: changedFrame }), /frozen project frame basis/u);
});

test("closed sort, reference, value, model-basis, and empty-T laws refuse counterexamples", () => {
  const { input } = fixture();
  const cases = [
    mutateBytes(input.accepted_program_bytes, true, (program) => {
      (((program.model as Record<string, unknown>).O as Record<string, unknown>[])[0]!).sort = "urn:test:unknown-sort";
    }),
    mutateBytes(input.accepted_program_bytes, true, (program) => {
      const model = program.model as { O: Record<string, unknown>[] };
      const concept = model.O.find((row) => row.sort === SORT.concept)!;
      const authority = model.O.find((row) => row.sort === SORT.authority)!;
      authority.owner = concept.id;
    }),
    mutateBytes(input.accepted_program_bytes, true, (program) => {
      (((program.model as Record<string, unknown>).O as Record<string, unknown>[])[0]!).value = "not a symbol";
    }),
    mutateBytes(input.accepted_program_bytes, true, (program) => {
      (program.model as Record<string, unknown>).b = `urn:stdo-index:model-basis:sha256:${"0".repeat(64)}`;
    }),
    mutateBytes(input.accepted_program_bytes, true, (program) => {
      const model = program.model as { T: Record<string, unknown>[] };
      model.T.push({ id: "urn:test:forbidden-transformation" });
    }),
  ];
  for (const changed of cases) assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, accepted_program_bytes: changed }));
});

test("F_D eligibility must be an unchanged external result under an exact resolved grant", () => {
  const { input } = fixture();
  const falseCheck = mutateBytes(input.candidate_structure_result_bytes, true, (result) => {
    (result.checks as Record<string, unknown>).population_totality = false;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, candidate_structure_result_bytes: falseCheck }), /all exact deterministic checks/u);
  const wrongSubject = mutateBytes(input.candidate_structure_result_bytes, true, (result) => {
    result.semantic_compilation_candidate_sha256 = `sha256:${"0".repeat(64)}`;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, candidate_structure_result_bytes: wrongSubject }), /unchanged supplied candidate bytes/u);
  const wrongGrant = mutateBytes(input.structure_grant_bytes, false, (grant) => {
    grant.grantee_identity = "urn:test:self-asserted-evaluator";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, structure_grant_bytes: wrongGrant }), /Product-owner-issued candidate-structure evaluation authority/u);
  const wrongGrantScope = mutateBytes(input.structure_grant_bytes, false, (grant) => {
    grant.grant_scope = "Caller-selected structure authority.";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, structure_grant_bytes: wrongGrantScope }), /Product-owner-issued candidate-structure evaluation authority/u);
  const callerEvaluatorBytes = recordBytes({ kind: "caller-evaluator", schema_version: 1 });
  const callerEvaluatorGrant = mutateBytes(input.structure_grant_bytes, false, (grant) => {
    grant.source_sha256 = sha256Bytes(callerEvaluatorBytes);
  });
  assert.throws(
    () => constructAxiomIndexGtlCandidate({
      ...input,
      structure_grant_bytes: callerEvaluatorGrant,
      structure_grant_source_bytes: callerEvaluatorBytes,
    }),
    /Product-owner-issued candidate-structure evaluation authority/u,
  );
  const changedCompilerProvenance = new Uint8Array(input.compiler_provenance_bundle_bytes);
  changedCompilerProvenance[0] = (changedCompilerProvenance[0] ?? 0) ^ 1;
  assert.throws(
    () => constructAxiomIndexGtlCandidate({ ...input, compiler_provenance_bundle_bytes: changedCompilerProvenance }),
    /compiler_provenance_bundle/u,
  );
  const framedCompilerProvenance = new Uint8Array(input.compiler_provenance_bundle_bytes.length + 1);
  framedCompilerProvenance.set(input.compiler_provenance_bundle_bytes);
  framedCompilerProvenance[framedCompilerProvenance.length - 1] = 0x0a;
  assert.throws(
    () => constructAxiomIndexGtlCandidate({ ...input, compiler_provenance_bundle_bytes: framedCompilerProvenance }),
    /exact unframed canonical JSON/u,
  );
  const duplicateKeyCompilerProvenance = encoder.encode(
    decoder.decode(input.compiler_provenance_bundle_bytes).replace(
      /^\{/u,
      '{"kind":"stdo-representation.compiler-provenance-bundle",',
    ),
  );
  assert.throws(
    () => constructAxiomIndexGtlCandidate({ ...input, compiler_provenance_bundle_bytes: duplicateKeyCompilerProvenance }),
    /duplicate JSON object name/u,
  );
  const missingCompilerMember = { ...input.compiler_provenance_member_bytes };
  delete (missingCompilerMember as Record<string, Uint8Array>)[Object.keys(missingCompilerMember)[0]!];
  assert.throws(
    () => constructAxiomIndexGtlCandidate({ ...input, compiler_provenance_member_bytes: missingCompilerMember }),
    /does not resolve supplied exact non-empty member bytes|extras or omissions/u,
  );
});

test("Ledger_B is the external F_H v_select decision and conserves the complete proposal population", () => {
  const { input } = fixture();
  const omitted = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    (ledger.proposal_dispositions as unknown[]).pop();
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: omitted }), /complete candidate proposal population/u);
  const changedModelDecision = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const rows = ledger.proposal_dispositions as Record<string, unknown>[];
    const row = rows.find((entry) => entry.proposal_kind === "model_record")!;
    row.decision = "retained_uncertain";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: changedModelDecision }), /only accepted unchanged/u);
  const selfAsserted = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    (ledger.author as Record<string, unknown>).traversal_ref = ACCEPT_INTERPRETATION;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: selfAsserted }), /F_H\[v_select\]/u);
  const missingEvidence = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    (ledger.author as Record<string, unknown>).evidence_refs = ["urn:test:insufficient"];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: missingEvidence }), /required unchanged evidence/u);
});

test("non-model final surfaces support exact acceptance, replacement, resolution, and retained uncertainty", () => {
  for (const options of [
    { ledgerResidualDecision: "accepted_unchanged" as const },
    { ledgerResidualDecision: "resolved" as const },
    { ledgerResidualDecision: "rejected" as const },
    { ledgerSelectionDecision: "accepted_modified" as const },
  ]) {
    const { input } = fixture(options);
    assert.equal(constructAxiomIndexGtlCandidate(input).receipt.frozen_gtl_validation, "valid");
  }
});

test("proposal disposition final_refs obey kind- and decision-specific conservation", () => {
  const { input, identities } = fixture();
  const selfRetainedUncertain = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const row = (ledger.proposal_dispositions as Record<string, unknown>[]).find((entry) => entry.proposal_ref === identities.compilationResidual)!;
    row.final_refs = [identities.compilationResidual];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: selfRetainedUncertain }), /retained_uncertain must name one or more exact model X/u);

  const rejectedWithFinalRef = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const row = (ledger.proposal_dispositions as Record<string, unknown>[]).find((entry) => entry.proposal_ref === identities.compilationResidual)!;
    row.decision = "rejected";
    row.final_refs = [identities.firstModelResidual];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: rejectedWithFinalRef }), /rejected must name no final reference/u);

  const modifiedToCandidateIdentity = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const row = (ledger.proposal_dispositions as Record<string, unknown>[]).find((entry) => entry.proposal_ref === identities.selection)!;
    row.decision = "accepted_modified";
    row.final_refs = [identities.selection];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: modifiedToCandidateIdentity }), /accepted_modified must name one new exact final replacement/u);
});

test("candidate selection and uncertainty populations conserve records without reverse X-to-U totality", () => {
  const { input, program } = fixture();
  const candidate = JSON.parse(decoder.decode(input.semantic_compilation_candidate_bytes)) as {
    compilation_residuals: readonly { model_residual_refs: readonly string[] }[];
  };
  assert.equal(program.model.X.length, 2);
  assert.deepEqual(candidate.compilation_residuals[0]!.model_residual_refs, [program.model.X[0]!.id]);
  assert.equal(constructAxiomIndexGtlCandidate(input).receipt.frozen_gtl_validation, "valid");

  assert.throws(() => constructAxiomIndexGtlCandidate(fixture({ compilationResidualModelRefs: "unresolved" }).input), /does not resolve one exact model X residual/u);
  assert.throws(
    () => constructAxiomIndexGtlCandidate(fixture({ compilationResidualModelRefs: "empty", ledgerResidualDecision: "accepted_unchanged" }).input),
    /required cardinality/u,
  );
  assert.throws(() => constructAxiomIndexGtlCandidate(fixture({ selectionDisposition: "omitted" }).input), /must be empty unless the selection disposition is retained/u);
});

test("candidate proposal identities are disjoint across all proposal families", () => {
  assert.throws(() => constructAxiomIndexGtlCandidate(fixture({ proposalIdentityCollision: "selection_model" }).input), /proposal identity .* collides across model records and selections/u);
  assert.throws(() => constructAxiomIndexGtlCandidate(fixture({ proposalIdentityCollision: "residual_selection" }).input), /proposal identity .* collides across selections and compilation residuals/u);
  assert.throws(() => constructAxiomIndexGtlCandidate(fixture({ proposalIdentityCollision: "selection_evaluated_member" }).input), /proposal identity .* collides across evaluated members and selections/u);
});

test("evaluated-member rows are congruent with exact final selection incidence", () => {
  assert.throws(
    () => constructAxiomIndexGtlCandidate(fixture({ evaluatedFirstDisposition: "inapplicable" }).input),
    /inapplicable or no-retained-material source member cannot resolve final model records/u,
  );
  assert.throws(
    () => constructAxiomIndexGtlCandidate(fixture({ evaluatedFirstDisposition: "uncertain" }).input),
    /uncertain or refused source member must resolve only exact model X residuals/u,
  );

  const { input } = fixture();
  const missingReverseIncidence = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const first = (ledger.evaluated_members as Record<string, unknown>[])[0]!;
    first.selection_refs = [];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: missingReverseIncidence }), /does not connect selection .* to a source member/u);

  const mixed = fixture({ mixedMemberDispositions: true });
  const constructed = constructAxiomIndexGtlCandidate(mixed.input);
  const decoded = decodeAxiomIndexConfig(
    constructed.publication.rules[0]!.config as Readonly<Record<string, unknown>>,
    mixed.input.target_signature_bytes,
    mixed.input.source_manifest_bytes,
    mixed.input.profile_bytes,
  );
  assert.equal(decoded.source_bindings[0]!.disposition, "retained");
  assert.equal(decoded.source_bindings[1]!.disposition, "represented_by_residual");
  assert(decoded.source_bindings[1]!.model_refs.every((identity) => decoded.model.X.some((row) => row.id === identity)));
});

test("P_B is total, canonical, source-resolved, record-congruent, and unchanged", () => {
  const { input } = fixture();
  const missingRow = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    (ledger.record_provenance as unknown[]).pop();
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: missingRow }), /total over the exact local model record population/u);

  const changedOwner = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const binding = (ledger.record_provenance as Record<string, unknown>[])[0]!;
    (binding.semantic_address as Record<string, unknown>).owning_authority = "urn:test:wrong-owner";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: changedOwner }), /not congruent with the record context, owner, governed scope/u);

  const fragmentLocator = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const binding = (ledger.record_provenance as Record<string, unknown>[])[0]!;
    ((binding.source_locators as Record<string, unknown>[])[0]!).fragment = "heading";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: fragmentLocator }), /must be exact null/u);

  const unresolvedEvidence = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const binding = (ledger.record_provenance as Record<string, unknown>[])[0]!;
    binding.derivation_evidence_refs = ["urn:test:caller-invented-evidence"];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: unresolvedEvidence }), /exact derivation-evidence domain/u);

  const duplicateEvidence = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const binding = (ledger.record_provenance as Record<string, unknown>[])[0]!;
    binding.derivation_evidence_refs = [WHAT, WHAT];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: duplicateEvidence }), /duplicate-free and canonically sorted/u);

  const changedFinalTerm = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const binding = (ledger.record_provenance as Record<string, unknown>[])[0]!;
    (binding.semantic_address as Record<string, unknown>).term = "changed-term";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: changedFinalTerm }), /does not preserve the candidate record-provenance relation unchanged/u);

  const changedProgramTerm = mutateBytes(input.accepted_program_bytes, true, (program) => {
    const binding = (program.record_provenance as Record<string, unknown>[])[0]!;
    (binding.semantic_address as Record<string, unknown>).term = "changed-term";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, accepted_program_bytes: changedProgramTerm }), /does not preserve the final ledger record-provenance relation unchanged/u);
});

test("generated source keys reproduce exact preimages and cover exact P_B semantic addresses", () => {
  const { input } = fixture();
  const wrongDigest = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    ((ledger.generated_source_keys as Record<string, unknown>[])[0]!).source_key = `urn:stdo-representation:source-key:sha256:${"0".repeat(64)}`;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: wrongDigest }), /does not reproduce from the exact source-key preimage/u);

  const missingBinding = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    ledger.generated_source_keys = [];
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: missingBinding }), /does not bind generated-prefix record-provenance source key/u);

  const arbitrarySourceIdentity = mutateBytes(input.selection_ledger_bytes, false, (ledger) => {
    const binding = (ledger.record_provenance as Record<string, unknown>[])[1]!;
    (binding.semantic_address as Record<string, unknown>).source_key = "urn:test:caller-invented-source-key";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: arbitrarySourceIdentity }), /neither an exact row-local Source STDO identity nor a governed generated key/u);
});

test("external J_B alone opens encoding for the unchanged interpreted model", () => {
  const { input } = fixture();
  const wrongSubject = mutateBytes(input.semantic_judgment_bytes, false, (judgment) => {
    judgment.subject_sha256 = `sha256:${"0".repeat(64)}`;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, semantic_judgment_bytes: wrongSubject }), /unchanged interpreted-model identity and exact model content/u);
  const wrongTraversal = mutateBytes(input.semantic_judgment_bytes, false, (judgment) => {
    judgment.traversal_ref = SELECT;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, semantic_judgment_bytes: wrongTraversal }), /interpretation-acceptance traversal/u);
  const wrongGrant = mutateBytes(input.semantic_grant_bytes, false, (grant) => {
    grant.authority_identity = "urn:test:self-issued";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, semantic_grant_bytes: wrongGrant }), /Product-owner grant|authority-grant artifact/u);
  const callerAuthorityBytes = recordBytes({ kind: "caller-authority", schema_version: 1 });
  const callerAuthorityGrant = mutateBytes(input.semantic_grant_bytes, false, (grant) => {
    grant.source_sha256 = sha256Bytes(callerAuthorityBytes);
  });
  assert.throws(
    () => constructAxiomIndexGtlCandidate({
      ...input,
      semantic_grant_bytes: callerAuthorityGrant,
      semantic_grant_source_bytes: callerAuthorityBytes,
    }),
    /exact external Product-owner grant/u,
  );
});

test("J_B remains external to carrier bytes, module identity, and compact configuration", () => {
  const { input, semanticJudgmentIdentity } = fixture();
  const first = constructAxiomIndexGtlCandidate(input);
  const changedJudgmentBytes = mutateBytes(input.semantic_judgment_bytes, false, (judgment) => {
    judgment.decided_at = "2026-08-30T00:04:00Z";
  });
  const second = constructAxiomIndexGtlCandidate({ ...input, semantic_judgment_bytes: changedJudgmentBytes });
  assert.notEqual(first.receipt.semantic_judgment_identity, second.receipt.semantic_judgment_identity);
  assert.equal(first.publication.moduleRef, second.publication.moduleRef);
  assert.deepEqual(first.canonical_bytes, second.canonical_bytes);
  const carrierText = decoder.decode(first.canonical_bytes);
  assert.equal(carrierText.includes(semanticJudgmentIdentity), false);
  assert.equal(carrierText.includes(first.receipt.semantic_judgment_sha256), false);
});

test("publisher identity requires exact manifest-to-tgz membership and the frozen GTL basis", () => {
  const { input } = fixture();
  const corruptArtifact = new Uint8Array(input.publisher_artifact_bytes);
  const artifactIndex = corruptArtifact.length - 1;
  corruptArtifact[artifactIndex] = (corruptArtifact[artifactIndex] ?? 0) ^ 1;
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, publisher_artifact_bytes: corruptArtifact }), /publisher artifact bytes|gzip-compressed npm tar/u);
  const wrongCarrierBasis = mutateBytes(input.publisher_manifest_bytes, false, (manifest) => {
    (manifest.carrier_basis as Record<string, unknown>).authority_tree_sha1 = "0".repeat(40);
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, publisher_manifest_bytes: wrongCarrierBasis }), /does not reproduce/u);
  const selfConsistentWrongCarrierBasis = mutateBytes(input.publisher_manifest_bytes, false, (manifest) => {
    const basis = manifest.carrier_basis as Record<string, JsonValue>;
    basis.authority_inventory_count = 34;
    const coordinate = {
      authority_inventory_count: basis.authority_inventory_count,
      authority_root: basis.authority_root!,
      authority_tree_sha1: basis.authority_tree_sha1!,
      commit_sha1: basis.commit_sha1!,
      repository: basis.repository!,
    };
    basis.identity = `${CARRIER_BASIS_PREFIX}${sha256Canonical(coordinate).slice("sha256:".length)}`;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, publisher_manifest_bytes: selfConsistentWrongCarrierBasis }), /selected profile carrier basis/u);
  const wrongMember = mutateBytes(input.publisher_manifest_bytes, false, (manifest) => {
    ((manifest.members as Record<string, unknown>[])[0]!).sha256 = `sha256:${"0".repeat(64)}`;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, publisher_manifest_bytes: wrongMember }), /member inventory|publisher manifest/u);
});

test("noncanonical evidence bytes and profile drift fail closed", () => {
  const { input } = fixture();
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, selection_ledger_bytes: new Uint8Array([...input.selection_ledger_bytes, 0x0a]) }), /unframed canonical JSON/u);
  const changedProfile = mutateBytes(input.profile_bytes, true, (profile) => {
    profile.semantic_acceptance = "self_accepting";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, profile_bytes: changedProfile }), /complete selected Axiom Index GTL profile/u);
  const changedTupleSchema = mutateBytes(input.profile_bytes, true, (profile) => {
    (((profile.configuration as Record<string, unknown>).tuple_schemas as Record<string, Record<string, unknown>>).o!.fields as string[])[1] = "semantic_sort";
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, profile_bytes: changedTupleSchema }), /complete selected Axiom Index GTL profile/u);
  const selfConsistentWrongProfileBasis = mutateBytes(input.profile_bytes, true, (profile) => {
    const basis = ((profile.build_tenant as Record<string, unknown>).carrier_basis as Record<string, unknown>);
    const coordinate = basis.coordinate as Record<string, JsonValue>;
    coordinate.authority_inventory_count = 34;
    basis.identity = `${CARRIER_BASIS_PREFIX}${sha256Canonical(coordinate).slice("sha256:".length)}`;
  });
  assert.throws(() => constructAxiomIndexGtlCandidate({ ...input, profile_bytes: selfConsistentWrongProfileBasis }), /selected frozen GTL coordinate/u);
});
