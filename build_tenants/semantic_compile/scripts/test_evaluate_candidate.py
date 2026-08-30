from __future__ import annotations

import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from acquire_basis import (
    CALCULUS_BASIS_IDENTITY,
    CAPABILITY_IDENTITY,
    COMPILE_GRANT_SCOPE,
    COMPILE_TRAVERSAL as ACQUIRE_COMPILE_TRAVERSAL,
    COMPILER_PROVENANCE_MEMBER_FILES,
    CONTEXT_BUDGET_TOKENS,
    DEFAULT_CALCULUS_BASIS,
    DEFAULT_DERIVATION_STDO,
    DEFAULT_STDO,
    F_P as ACQUIRE_F_P,
    FRAME_BASIS_IDENTITY,
    HOST_IDENTITY,
    MODEL_IDENTITY,
    PRODUCT_OWNER_ACTOR,
    PRODUCT_OWNER_AUTHORITY,
    PRODUCT_OWNER_GRANT,
    PRODUCT_OWNER_GRANT_SCOPE,
    PRODUCT_PATH,
    SUBJECT_BASIS_IDENTITY,
    build_compiler_provenance_bundle,
    build_sealed_invocation,
    canonical_bytes,
    compiler_provenance_bundle_ref,
    compiler_provenance_member_ref,
    digest_bytes,
    digest_file,
    load_json,
    model_basis_identity,
    model_basis_resolution,
    model_configuration_sha256,
    record_binding,
    semantic_compile_preflight,
    signature_member_resolution,
    utf16_key,
    verify_calculus_basis_candidate,
    verify_compilation_contract,
    verify_compiler_provenance_bundle,
    verify_frame_configuration,
    verify_manifest,
    verify_transport_schema,
    verify_run_compiler_provenance_bundle,
    what_member_set_identity,
)
from evaluate_candidate import (
    CANDIDATE_STRUCTURE_GRANT_SCOPE,
    CANDIDATE_STRUCTURE_GRANT_SOURCE_REF,
    CANDIDATE_PAYLOAD_FIELDS,
    COMPILE_TRAVERSAL,
    CONSTRAINT_KINDS,
    EVALUATOR_IDENTITY,
    F_P,
    JUDGMENT_KINDS,
    MODEL_FIELD_BY_POPULATION,
    PROPOSAL_SCHEMA_VERSION,
    RECORD_KIND_BY_POPULATION,
    RELATION_KINDS,
    RESIDUAL_KINDS,
    SIGNATURE_IDENTITY,
    SORTS,
    STOP_KINDS,
    candidate_structure_result_identity,
    candidate_artifact_path,
    candidate_structure_grant_identity,
    construct_candidate,
    decode_result_envelope,
    evaluation_artifact_root,
    generated_source_key,
    publish_immutable,
    publish_raw_output,
    raw_output_artifact_path,
    raw_output_identity,
    resolve_raw_output,
    semantic_compilation_candidate_identity,
    validate_candidate,
    validate_candidate_structure_grant,
    validate_signature,
    validate_stop,
    verify_run_acquisition,
)


TENANT = Path(__file__).resolve().parents[1]
HISTORICAL_RUN = TENANT / "runs" / "20260829T008000Z"
HISTORICAL_HASHES = {
    "acquisition.json": "42eec3ebe731752256813ee5483af53ef32c6f58be9d5f70a6af69eba2720d22",
    "basis.json": "8a7e2c362345b656559fec293607a3276cb37ca845d1d61057ab8abef33b0c1a",
    "candidate-structure-result.json": "26f4159ff46c52b7ec13534ed4942a3513f5adc217778621305ad2e2d798935e",
    "candidate.json": "eeb307136a3ad6d142792f7ef03e311228d5d525da0ee8b7507facd53e514bc4",
    "invocation.txt": "0a9905d4a8505e35fdde9b5a53280ad068cb3610dda8acb0608ee68990b4f5fc",
    "raw-output.json": "995b10eb3ace14846e2132b3af88d083566115d5819dec401ae5d48c12390dd1",
    "sealed-invocation.txt": "2609b4880b3b1e8df27fb3ea592e77326473ae401dd4e42b66cb95a95e1bb7a2",
    "source-manifest.json": "35497f1d3477951716fa6d8f3b37517659bf8314e2b607803a50b333d0177eab",
}
SORT_DOMAIN = "urn:stdo-index:reference-domain:stdo:sort:1"
RELATION_DOMAIN = "urn:stdo-index:reference-domain:stdo:relation-kind:1"
CONSTRAINT_DOMAIN = "urn:stdo-index:reference-domain:stdo:constraint-kind:1"
RESIDUAL_DOMAIN = "urn:stdo-index:reference-domain:stdo:residual-kind:1"
JUDGMENT_DOMAIN = "urn:stdo-index:reference-domain:stdo:judgment-kind:1"
STOP_DOMAIN = "urn:stdo-index:reference-domain:stdo:stop-kind:1"
GOVERNED_SCOPE = "urn:stdo-representation:scope:stdo-core"
TEST_PROVENANCE_MEMBER_BYTES = {
    compiler_provenance_member_ref("test", member_kind): (
        f"test compiler provenance member: {member_kind}\n".encode()
    )
    for member_kind in COMPILER_PROVENANCE_MEMBER_FILES
}
TEST_PROVENANCE_BUNDLE = {
    "kind": "stdo-representation.compiler-provenance-bundle",
    "schema_version": 1,
    "members": [
        {
            "member_kind": member_kind,
            "member_ref": compiler_provenance_member_ref("test", member_kind),
            "member_sha256": digest_bytes(
                TEST_PROVENANCE_MEMBER_BYTES[
                    compiler_provenance_member_ref("test", member_kind)
                ]
            ),
        }
        for member_kind in sorted(COMPILER_PROVENANCE_MEMBER_FILES, key=utf16_key)
    ],
}
TEST_PROVENANCE_BYTES = canonical_bytes(TEST_PROVENANCE_BUNDLE)


def selected_coordinates() -> tuple[dict, dict, dict, dict, str]:
    calculus = verify_calculus_basis_candidate(
        DEFAULT_CALCULUS_BASIS, DEFAULT_STDO, DEFAULT_DERIVATION_STDO
    )
    installed = load_json(DEFAULT_STDO / "manifest.json")
    verify_manifest(DEFAULT_STDO, installed)
    signature_path = TENANT / "profile" / "stdo-signature.json"
    contract_path = TENANT / "contract" / "v_compile.json"
    frame_path = TENANT / "profile" / "stdo-core-frame.json"
    signature = load_json(signature_path)
    contract = load_json(contract_path)
    frame = load_json(frame_path)
    subject = {
        "release_uri": "stdo://releases/v2.5.0-rc.1/",
        "installed_manifest_sha256": digest_file(DEFAULT_STDO / "manifest.json"),
        "standards_member_set_sha256": (
            "sha256:" + installed["standards"]["member_set_sha256"]
        ),
        "member_count": installed["standards"]["member_count"],
    }
    members = [
        {"path": row["path"], "sha256": "sha256:" + row["sha256"]}
        for row in installed["standards"]["members"]
    ]
    packet = {"release_uri": subject["release_uri"], "members": members}
    packet_sha = "sha256:" + hashlib.sha256(canonical_bytes(packet)).hexdigest()
    expected_basis = {
        "calculus": calculus,
        "subject": subject,
        "signature": {
            "identity": signature["identity"],
            "sha256": digest_file(signature_path),
        },
        "interpretation_contract": {
            "identity": contract["identity"],
            "sha256": digest_file(contract_path),
        },
        "frame": {
            "configuration_identity": frame["identity"],
            "configuration_sha256": digest_file(frame_path),
            "frame_basis_identity": frame["frame_basis_identity"],
            "frame_basis_sha256": frame["frame_basis_sha256"],
            "selected_frame_refs": frame["selected_frame_refs"],
            "status": frame["status"],
        },
        "source_packet": {
            "identity": (
                "urn:stdo-index:source-packet:sha256:"
                + packet_sha.removeprefix("sha256:")
            ),
            "sha256": packet_sha,
        },
        "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
        "what_member_set_identity": what_member_set_identity(),
    }
    source_manifest = {
        "kind": "stdo-index.source-manifest",
        "schema_version": 2,
        "release_uri": subject["release_uri"],
        "installed_root": str(DEFAULT_STDO / installed["standards"]["installed_root"]),
        "installed_manifest_sha256": subject["installed_manifest_sha256"],
        "standards_member_set_sha256": subject["standards_member_set_sha256"],
        "members": members,
        "supplied_members": copy.deepcopy(members),
    }
    return (
        expected_basis,
        source_manifest,
        signature,
        contract,
        model_basis_identity(expected_basis),
    )


def compiler_invocation() -> dict:
    return {
        "topology": "single_invocation",
        "traversal_ref": COMPILE_TRAVERSAL,
        "functor_ref": F_P,
        "host_identity": "urn:openai:codex-cli",
        "model_identity": "gpt-5.6-sol",
        "model_configuration_sha256": "sha256:" + "1" * 64,
        "instruction_sha256": "sha256:" + "2" * 64,
        "capability_envelope_ref": (
            "urn:axiom-indexer:capability:semantic-compilation-prototype:1"
        ),
        "context_budget_tokens": 1_000_000,
        "invoked_at": "2026-08-30T00:00:00Z",
        "raw_output_ref": (
            "urn:stdo-representation:semantic-compilation-run:test:raw-output"
        ),
        "raw_output_sha256": "sha256:" + "3" * 64,
        "provenance_ref": (compiler_provenance_bundle_ref("test")),
        "provenance_sha256": digest_bytes(TEST_PROVENANCE_BYTES),
    }


def candidate_structure_grant(candidate: dict, expected_basis: dict) -> dict:
    candidate_identity, candidate_sha = semantic_compilation_candidate_identity(
        candidate
    )
    return {
        "kind": "stdo-representation.candidate-structure-evaluation-grant",
        "schema_version": 1,
        "parent_grant_identity": PRODUCT_OWNER_GRANT,
        "issuer_actor_identity": PRODUCT_OWNER_ACTOR,
        "authority_identity": PRODUCT_OWNER_AUTHORITY,
        "grantee_identity": EVALUATOR_IDENTITY,
        "grant_scope": CANDIDATE_STRUCTURE_GRANT_SCOPE,
        "traversal_ref": "urn:stdo-representation:traversal:candidate-structure:3",
        "functor_ref": "urn:stdo:concept:axiomatic-calculus:f-d",
        "subject_identity": candidate_identity,
        "subject_sha256": candidate_sha,
        "calculus_basis_identity": expected_basis["calculus"]["identity"],
        "signature_identity": expected_basis["signature"]["identity"],
        "signature_sha256": expected_basis["signature"]["sha256"],
        "interpretation_contract_identity": expected_basis["interpretation_contract"][
            "identity"
        ],
        "interpretation_contract_sha256": expected_basis["interpretation_contract"][
            "sha256"
        ],
        "what_member_set_identity": expected_basis["what_member_set_identity"],
        "frame_basis_identity": expected_basis["frame"]["frame_basis_identity"],
        "frame_basis_sha256": expected_basis["frame"]["frame_basis_sha256"],
        "evidence_refs": [
            "urn:stdo-representation:evidence:test:candidate-structure-grant"
        ],
        "issued_at": "2026-08-30T00:00:03Z",
        "source_ref": CANDIDATE_STRUCTURE_GRANT_SOURCE_REF,
        "source_sha256": digest_file(PRODUCT_PATH),
    }


def preflight_fixture(directory: Path, expected_basis: dict) -> tuple[dict, dict]:
    frame_path = TENANT / "profile" / "stdo-core-frame.json"
    prompt_path = TENANT / "prompt" / "v_compile.txt"
    schema_path = TENANT / "schema" / "candidate.schema.json"
    actor = "urn:openai:codex-cli:gpt-5.6-sol"
    overlay_authority = "./specification/PRODUCT.md"

    frame_acceptance = {
        "kind": "stdo-representation.authority-acceptance",
        "schema_version": 1,
        "subject_kind": "reference_frame_basis",
        "subject_identity": FRAME_BASIS_IDENTITY,
        "subject_sha256": expected_basis["frame"]["frame_basis_sha256"],
        "traversal_ref": ("urn:stdo-representation:traversal:accept-frame-basis:1"),
        "actor_identity": PRODUCT_OWNER_ACTOR,
        "authority_identity": PRODUCT_OWNER_AUTHORITY,
        "grant_identity": PRODUCT_OWNER_GRANT,
        "grant_scope": PRODUCT_OWNER_GRANT_SCOPE,
        "basis_refs": sorted(
            [CALCULUS_BASIS_IDENTITY, SUBJECT_BASIS_IDENTITY], key=utf16_key
        ),
        "admitting_authority_refs": [overlay_authority],
        "decision": "accepted",
        "decided_at": "2026-08-30T00:00:00Z",
        "evidence_refs": ["urn:stdo-representation:evidence:test:frame-basis-review"],
        "supersedes": None,
    }
    frame_binding = record_binding("authority-acceptance", frame_acceptance)

    capability = {
        "kind": "stdo-representation.semantic-compiler-capability-envelope",
        "schema_version": 1,
        "identity": CAPABILITY_IDENTITY,
        "actor_identity": actor,
        "host_identity": HOST_IDENTITY,
        "model_identity": MODEL_IDENTITY,
        "model_configuration_sha256": model_configuration_sha256(),
        "supported_traversal_refs": [ACQUIRE_COMPILE_TRAVERSAL],
        "maximum_context_tokens": CONTEXT_BUDGET_TOKENS,
        "output_schema_sha256": digest_file(schema_path),
        "evidence_refs": ["urn:stdo-representation:evidence:test:compiler-capability"],
    }
    capability_binding = {
        "identity": CAPABILITY_IDENTITY,
        "sha256": digest_bytes(canonical_bytes(capability)),
    }

    compile_grant = {
        "kind": "stdo-representation.semantic-compilation-operation-grant",
        "schema_version": 1,
        "issuer_actor_identity": PRODUCT_OWNER_ACTOR,
        "authority_identity": PRODUCT_OWNER_AUTHORITY,
        "parent_grant_identity": PRODUCT_OWNER_GRANT,
        "parent_grant_scope": PRODUCT_OWNER_GRANT_SCOPE,
        "grantee_actor_identity": actor,
        "traversal_ref": ACQUIRE_COMPILE_TRAVERSAL,
        "functor_ref": ACQUIRE_F_P,
        "frame_acceptance_identity": frame_binding["identity"],
        "frame_acceptance_sha256": frame_binding["sha256"],
        "frame_configuration_identity": expected_basis["frame"][
            "configuration_identity"
        ],
        "frame_configuration_sha256": digest_file(frame_path),
        "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
        "source_packet_identity": expected_basis["source_packet"]["identity"],
        "source_packet_sha256": expected_basis["source_packet"]["sha256"],
        "calculus_basis_identity": CALCULUS_BASIS_IDENTITY,
        "signature_identity": expected_basis["signature"]["identity"],
        "signature_sha256": expected_basis["signature"]["sha256"],
        "interpretation_contract_identity": expected_basis["interpretation_contract"][
            "identity"
        ],
        "interpretation_contract_sha256": expected_basis["interpretation_contract"][
            "sha256"
        ],
        "what_member_set_identity": expected_basis["what_member_set_identity"],
        "compiler_prompt_sha256": digest_file(prompt_path),
        "output_schema_sha256": digest_file(schema_path),
        "capability_envelope_identity": capability_binding["identity"],
        "capability_envelope_sha256": capability_binding["sha256"],
        "scope": COMPILE_GRANT_SCOPE,
        "issued_at": "2026-08-30T00:00:01Z",
        "evidence_refs": [
            "urn:stdo-representation:evidence:test:semantic-compile-grant"
        ],
    }
    compile_grant_binding = record_binding(
        "semantic-compilation-operation-grant", compile_grant
    )

    activation = {
        "kind": "stdo-representation.semantic-compilation-activation",
        "schema_version": 1,
        "traversal_ref": ACQUIRE_COMPILE_TRAVERSAL,
        "functor_ref": ACQUIRE_F_P,
        "frame_acceptance_identity": frame_binding["identity"],
        "frame_acceptance_sha256": frame_binding["sha256"],
        "frame_configuration_identity": expected_basis["frame"][
            "configuration_identity"
        ],
        "frame_configuration_sha256": digest_file(frame_path),
        "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
        "source_packet_identity": expected_basis["source_packet"]["identity"],
        "source_packet_sha256": expected_basis["source_packet"]["sha256"],
        "calculus_basis_identity": CALCULUS_BASIS_IDENTITY,
        "signature_identity": expected_basis["signature"]["identity"],
        "signature_sha256": expected_basis["signature"]["sha256"],
        "interpretation_contract_identity": expected_basis["interpretation_contract"][
            "identity"
        ],
        "interpretation_contract_sha256": expected_basis["interpretation_contract"][
            "sha256"
        ],
        "what_member_set_identity": expected_basis["what_member_set_identity"],
        "compiler_prompt_sha256": digest_file(prompt_path),
        "actor_identity": actor,
        "authority_identity": PRODUCT_OWNER_AUTHORITY,
        "grant_identity": compile_grant_binding["identity"],
        "grant_sha256": compile_grant_binding["sha256"],
        "grant_scope": COMPILE_GRANT_SCOPE,
        "activated_at": "2026-08-30T00:00:02Z",
        "capability_envelope_identity": capability_binding["identity"],
        "capability_envelope_sha256": capability_binding["sha256"],
        "evidence_refs": [
            "urn:stdo-representation:evidence:test:semantic-compile-activation"
        ],
    }

    paths = {
        "frame_acceptance": directory / "frame-acceptance.json",
        "compile_grant": directory / "compile-grant.json",
        "compile_activation": directory / "compile-activation.json",
        "capability_envelope": directory / "capability.json",
    }
    for name, value in (
        ("frame_acceptance", frame_acceptance),
        ("compile_grant", compile_grant),
        ("compile_activation", activation),
        ("capability_envelope", capability),
    ):
        paths[name].write_bytes(canonical_bytes(value))
    overlay = {
        "reference_frame_bases": [
            {
                "uri": "./specification/REFERENCE_FRAME_BASIS.md",
                "authority": [overlay_authority],
            }
        ]
    }
    return paths, overlay


def object_record(identity: str, sort: str, value: str, basis: str) -> dict:
    return {
        "id": identity,
        "sort": sort,
        "context": "urn:stdo-index:test:context",
        "owner": "urn:stdo-index:test:owner",
        "scope": GOVERNED_SCOPE,
        "basis": basis,
        "value": value,
    }


def proposal_fixture(
    expected_basis: dict, source_manifest: dict, model_basis: str
) -> dict:
    objects = [
        object_record(
            "urn:stdo-index:test:codomain",
            SORTS["concept"],
            "model_candidate",
            model_basis,
        ),
        object_record(
            "urn:stdo-index:test:context", SORTS["bounded_context"], "stdo", model_basis
        ),
        object_record(
            "urn:stdo-index:test:domain", SORTS["concept"], "source_packet", model_basis
        ),
        object_record(
            "urn:stdo-index:test:evidence",
            SORTS["evidence"],
            "exact_source",
            model_basis,
        ),
        object_record(
            "urn:stdo-index:test:owner",
            SORTS["authority"],
            "product_authority",
            model_basis,
        ),
        object_record(
            "urn:stdo-index:test:subject",
            SORTS["method"],
            "specification_method",
            model_basis,
        ),
    ]
    relation = {
        "id": "urn:stdo-index:test:relation",
        "kind": RELATION_KINDS["defines"],
        "source": "urn:stdo-index:test:subject",
        "target": "urn:stdo-index:test:domain",
        "context": "urn:stdo-index:test:context",
        "owner": "urn:stdo-index:test:owner",
        "scope": GOVERNED_SCOPE,
        "basis": model_basis,
        "qualifiers": ["directional"],
    }
    constraint = {
        "id": "urn:stdo-index:test:constraint",
        "kind": CONSTRAINT_KINDS["axiom"],
        "applies_to": "urn:stdo-index:test:subject",
        "predicate": "authority_is_conserved",
        "context": "urn:stdo-index:test:context",
        "owner": "urn:stdo-index:test:owner",
        "scope": GOVERNED_SCOPE,
        "basis": model_basis,
        "judgment_kind": JUDGMENT_KINDS["semantic_selection"],
        "latitude_ref": None,
        "refusal": "authority_gap",
    }
    traversal = {
        "id": "urn:stdo-index:test:traversal",
        "domain": "urn:stdo-index:test:domain",
        "codomain": "urn:stdo-index:test:codomain",
        "context": "urn:stdo-index:test:context",
        "owner": "urn:stdo-index:test:owner",
        "scope": GOVERNED_SCOPE,
        "basis": model_basis,
        "preconditions": ["exact_basis"],
        "postconditions": ["proposal_only"],
        "authority": "urn:stdo-index:test:owner",
        "evidence": ["urn:stdo-index:test:evidence"],
        "provenance": ["urn:stdo-index:test:evidence"],
        "stop_states": [
            STOP_KINDS["gap"],
            STOP_KINDS["hold"],
            STOP_KINDS["refusal"],
        ],
    }
    locals_ = [*objects, relation, constraint, traversal]
    local_ids = sorted([row["id"] for row in locals_], key=utf16_key)
    signature_refs = {
        **{row["sort"]: SORT_DOMAIN for row in objects},
        relation["kind"]: RELATION_DOMAIN,
        constraint["kind"]: CONSTRAINT_DOMAIN,
        constraint["judgment_kind"]: JUDGMENT_DOMAIN,
        **{stop: STOP_DOMAIN for stop in traversal["stop_states"]},
    }
    resolutions = [model_basis_resolution(model_basis, expected_basis)]
    resolutions.extend(
        signature_member_resolution(identity, domain, expected_basis)
        for identity, domain in signature_refs.items()
    )
    external_ids = [row["external_identity"] for row in resolutions]
    model = {
        "model_basis_identity": model_basis,
        "identities": sorted([*local_ids, *external_ids], key=utf16_key),
        "semantic_objects": objects,
        "typed_relations": [relation],
        "constraints": [constraint],
        "latitudes": [],
        "residuals": [],
        "traversals": [traversal],
        "transformations": [],
        "judgments": [],
        "external_resolutions": sorted(
            resolutions, key=lambda row: utf16_key(row["external_identity"])
        ),
    }
    selection_ref = "urn:stdo-representation:selection:test"
    first = source_manifest["members"][0]
    evaluated = []
    for index, member in enumerate(source_manifest["members"]):
        evaluated.append(
            {
                "member_path": member["path"],
                "member_sha256": member["sha256"],
                "disposition": (
                    "contains_retained_material"
                    if index == 0
                    else "contains_no_retained_material"
                ),
                "selection_refs": [selection_ref] if index == 0 else [],
                "rationale": "retained" if index == 0 else "no retained material",
            }
        )
    locator = {
        "basis_uri": expected_basis["subject"]["release_uri"],
        "member_path": first["path"],
        "member_sha256": first["sha256"],
        "fragment": None,
    }
    provenance = [
        {
            "model_record_ref": row["id"],
            "provenance_kind": "subject_derived",
            "semantic_address": {
                "source_key": (
                    "stdo://releases/v2.5.0-rc.1/standards/" + first["path"]
                ),
                "term": row["id"],
                "bounded_context": row["context"],
                "owning_authority": row["owner"],
                "selected_basis": expected_basis["subject_basis_identity"],
                "governed_scope": row["scope"],
            },
            "source_locators": [copy.deepcopy(locator)],
            "derivation_evidence_refs": [],
        }
        for row in sorted(locals_, key=lambda item: utf16_key(item["id"]))
    ]
    payload = {
        "calculus_basis_identity": expected_basis["calculus"]["identity"],
        "source_stdo_uri": expected_basis["subject"]["release_uri"],
        "source_stdo_manifest_sha256": expected_basis["subject"][
            "installed_manifest_sha256"
        ],
        "source_member_set_sha256": expected_basis["subject"][
            "standards_member_set_sha256"
        ],
        "source_members": [
            {"member_path": row["path"], "member_sha256": row["sha256"]}
            for row in source_manifest["members"]
        ],
        "subject_basis_identity": expected_basis["subject_basis_identity"],
        "what_member_set_identity": expected_basis["what_member_set_identity"],
        "signature_identity": expected_basis["signature"]["identity"],
        "signature_sha256": expected_basis["signature"]["sha256"],
        "interpretation_contract_identity": expected_basis["interpretation_contract"][
            "identity"
        ],
        "interpretation_contract_sha256": expected_basis["interpretation_contract"][
            "sha256"
        ],
        "frame_basis_identity": expected_basis["frame"]["frame_basis_identity"],
        "frame_basis_sha256": expected_basis["frame"]["frame_basis_sha256"],
        "selected_frame_refs": expected_basis["frame"]["selected_frame_refs"],
        "candidate_model": model,
        "candidate_model_content_identity": (
            "sha256:" + hashlib.sha256(canonical_bytes(model)).hexdigest()
        ),
        "proposed_record_provenance": provenance,
        "proposed_evaluated_members": evaluated,
        "proposed_selections": [
            {
                "selection_ref": selection_ref,
                "source_locators": [locator],
                "disposition": "retained",
                "model_record_refs": local_ids,
                "rationale": "candidate model records",
                "source_owner": "urn:stdo-index:test:owner",
            }
        ],
        "proposed_generated_source_keys": [],
        "compilation_residuals": [],
        "stop_state": STOP_KINDS["candidate"],
    }
    return {
        "kind": "stdo-representation.semantic-compilation-proposal",
        "schema_version": PROPOSAL_SCHEMA_VERSION,
        "payload": payload,
    }


def add_local_record(candidate: dict, population: str, row: dict) -> None:
    model = candidate["candidate_model"]
    field = MODEL_FIELD_BY_POPULATION[population]
    model[field].append(row)
    model[field].sort(key=lambda item: utf16_key(item["id"]))
    model["identities"] = sorted([*model["identities"], row["id"]], key=utf16_key)
    selection = candidate["proposed_selections"][0]
    derivation_locator = selection["source_locators"][0]
    derivation_source = (
        derivation_locator["basis_uri"]
        + "standards/"
        + derivation_locator["member_path"]
    )
    if derivation_locator["fragment"] is not None:
        derivation_source += "#" + derivation_locator["fragment"]
    selection["model_record_refs"] = sorted(
        [*selection["model_record_refs"], row["id"]], key=utf16_key
    )
    candidate["proposed_record_provenance"].append(
        {
            "model_record_ref": row["id"],
            "provenance_kind": "subject_derived",
            "semantic_address": {
                "source_key": derivation_source,
                "term": row["id"],
                "bounded_context": row["context"],
                "owning_authority": row["owner"],
                "selected_basis": candidate["subject_basis_identity"],
                "governed_scope": row["scope"],
            },
            "source_locators": [copy.deepcopy(derivation_locator)],
            "derivation_evidence_refs": [],
        }
    )
    candidate["proposed_record_provenance"].sort(
        key=lambda item: utf16_key(item["model_record_ref"])
    )
    candidate["candidate_model_content_identity"] = (
        "sha256:" + hashlib.sha256(canonical_bytes(model)).hexdigest()
    )
    refresh_proposal_identity(candidate)


def refresh_proposal_identity(candidate: dict) -> None:
    proposal = {
        "kind": "stdo-representation.semantic-compilation-proposal",
        "schema_version": PROPOSAL_SCHEMA_VERSION,
        "payload": {field: candidate[field] for field in CANDIDATE_PAYLOAD_FIELDS},
    }
    candidate["proposal_content_sha256"] = (
        "sha256:" + hashlib.sha256(canonical_bytes(proposal)).hexdigest()
    )


class SemanticCompileV3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        (
            cls.expected_basis,
            cls.source_manifest,
            cls.signature,
            cls.contract,
            cls.model_basis,
        ) = selected_coordinates()
        cls.base_compiler_invocation = compiler_invocation()

    def setUp(self) -> None:
        self.proposal = proposal_fixture(
            self.expected_basis, self.source_manifest, self.model_basis
        )
        self.raw_proposal_bytes = canonical_bytes(self.proposal) + b"\n"
        self.compiler_invocation = copy.deepcopy(self.base_compiler_invocation)
        self.compiler_invocation["raw_output_sha256"] = (
            "sha256:" + hashlib.sha256(self.raw_proposal_bytes).hexdigest()
        )
        self.candidate = construct_candidate(
            self.proposal,
            self.raw_proposal_bytes,
            self.expected_basis,
            self.source_manifest,
            self.compiler_invocation,
            TEST_PROVENANCE_BUNDLE,
            TEST_PROVENANCE_BYTES,
            TEST_PROVENANCE_MEMBER_BYTES,
        )

    def issues(
        self, candidate: dict | None = None, signature: dict | None = None
    ) -> list[dict[str, str]]:
        return validate_candidate(
            candidate or self.candidate,
            self.expected_basis,
            self.source_manifest,
            signature or self.signature,
            self.model_basis,
            self.compiler_invocation,
        )

    def test_exact_25_candidate_is_structurally_eligible(self) -> None:
        self.assertEqual(self.issues(), [])
        self.assertEqual(self.expected_basis["subject"]["member_count"], 51)
        self.assertEqual(
            self.candidate["kind"], "stdo-representation.semantic-compilation-candidate"
        )
        self.assertEqual(self.candidate["schema_version"], 3)
        self.assertEqual(self.signature["identity"], "urn:stdo-index:signature:stdo:7")
        self.assertEqual(
            self.contract["identity"],
            "urn:stdo-representation:traversal:semantic-compile:7",
        )
        self.assertEqual(
            self.candidate["candidate_model_content_identity"],
            "sha256:"
            + hashlib.sha256(
                canonical_bytes(self.candidate["candidate_model"])
            ).hexdigest(),
        )

    def test_constructor_copies_semantic_payload_and_adds_exact_what(self) -> None:
        for field in (
            "candidate_model",
            "proposed_record_provenance",
            "proposed_evaluated_members",
            "proposed_selections",
            "proposed_generated_source_keys",
            "compilation_residuals",
        ):
            self.assertEqual(self.candidate[field], self.proposal["payload"][field])
        self.assertEqual(
            self.candidate["proposal_content_sha256"],
            "sha256:" + hashlib.sha256(canonical_bytes(self.proposal)).hexdigest(),
        )
        self.assertEqual(
            self.candidate["subject_basis_identity"], SUBJECT_BASIS_IDENTITY
        )
        self.assertEqual(
            self.candidate["frame_basis_identity"],
            "urn:stdo-representation:reference-frame-basis:source-project:7",
        )
        self.assertEqual(
            self.candidate["selected_frame_refs"],
            ["urn:stdo-representation:frame:semantic-compilation"],
        )

        forged = copy.deepcopy(self.proposal)
        forged["payload"]["what_member_set_identity"] = "sha256:" + "0" * 64
        forged_bytes = canonical_bytes(forged) + b"\n"
        forged_invocation = copy.deepcopy(self.compiler_invocation)
        forged_invocation["raw_output_sha256"] = (
            "sha256:" + hashlib.sha256(forged_bytes).hexdigest()
        )
        with self.assertRaisesRegex(ValueError, "what_member_set_identity"):
            construct_candidate(
                forged,
                forged_bytes,
                self.expected_basis,
                self.source_manifest,
                forged_invocation,
                TEST_PROVENANCE_BUNDLE,
                TEST_PROVENANCE_BYTES,
                TEST_PROVENANCE_MEMBER_BYTES,
            )
        with self.assertRaisesRegex(ValueError, "raw proposal digest"):
            construct_candidate(
                self.proposal,
                self.raw_proposal_bytes + b" ",
                self.expected_basis,
                self.source_manifest,
                self.compiler_invocation,
                TEST_PROVENANCE_BUNDLE,
                TEST_PROVENANCE_BYTES,
                TEST_PROVENANCE_MEMBER_BYTES,
            )
        with self.assertRaisesRegex(ValueError, "provenance bytes"):
            construct_candidate(
                self.proposal,
                self.raw_proposal_bytes,
                self.expected_basis,
                self.source_manifest,
                self.compiler_invocation,
                TEST_PROVENANCE_BUNDLE,
                TEST_PROVENANCE_BYTES + b" ",
                TEST_PROVENANCE_MEMBER_BYTES,
            )

        framed_bytes = TEST_PROVENANCE_BYTES + b"\n"
        framed_invocation = copy.deepcopy(self.compiler_invocation)
        framed_invocation["provenance_sha256"] = digest_bytes(framed_bytes)
        with self.assertRaisesRegex(ValueError, "unframed JCS"):
            construct_candidate(
                self.proposal,
                self.raw_proposal_bytes,
                self.expected_basis,
                self.source_manifest,
                framed_invocation,
                TEST_PROVENANCE_BUNDLE,
                framed_bytes,
                TEST_PROVENANCE_MEMBER_BYTES,
            )

        changed_members = copy.deepcopy(TEST_PROVENANCE_MEMBER_BYTES)
        first_member_ref = TEST_PROVENANCE_BUNDLE["members"][0]["member_ref"]
        changed_members[first_member_ref] += b"changed"
        with self.assertRaisesRegex(ValueError, "unresolved compiler provenance"):
            construct_candidate(
                self.proposal,
                self.raw_proposal_bytes,
                self.expected_basis,
                self.source_manifest,
                self.compiler_invocation,
                TEST_PROVENANCE_BUNDLE,
                TEST_PROVENANCE_BYTES,
                changed_members,
            )

    def test_exact_what_and_frame_configuration_are_bound(self) -> None:
        self.assertEqual(
            what_member_set_identity(),
            "sha256:be6f3c244009d319c90588f8b403cd3379d6e135fcb29738d7aa3d49450a5379",
        )
        frame_path = TENANT / "profile" / "stdo-core-frame.json"
        verify_frame_configuration(load_json(frame_path), frame_path)
        self.assertEqual(
            load_json(frame_path)["frame_basis_sha256"],
            "sha256:4b32e19c48dfa6df909f174603bbeb43f00559f9bc50b5d8e27a02397b6464c3",
        )
        contract_path = TENANT / "contract" / "v_compile.json"
        verify_compilation_contract(load_json(contract_path), contract_path)

    def test_calculus_basis_candidate_reconstructs_exact_bytes(self) -> None:
        calculus = self.expected_basis["calculus"]
        self.assertEqual(
            calculus["identity"],
            "urn:stdo:axiomatic-calculus-basis:sha256:bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da",
        )
        forged = copy.deepcopy(calculus["record"])
        forged["publication_basis"]["member_sha256"] = "sha256:" + "0" * 64
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "basis.json"
            path.write_bytes(canonical_bytes(forged))
            with self.assertRaisesRegex(
                ValueError, "differs from exact installed bytes"
            ):
                verify_calculus_basis_candidate(
                    path, DEFAULT_STDO, DEFAULT_DERIVATION_STDO
                )

    def test_preflight_holds_before_missing_authority_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result, bindings, records = semantic_compile_preflight(
                frame_acceptance_path=root / "missing-frame.json",
                compile_grant_path=root / "missing-grant.json",
                compile_activation_path=root / "missing-activation.json",
                capability_envelope_path=root / "missing-capability.json",
                overlay={"reference_frame_bases": []},
                frame=load_json(TENANT / "profile" / "stdo-core-frame.json"),
                calculus=self.expected_basis["calculus"],
                signature_ref=self.expected_basis["signature"],
                contract_ref=self.expected_basis["interpretation_contract"],
                source_packet_ref=self.expected_basis["source_packet"],
                prompt_sha256=digest_file(TENANT / "prompt" / "v_compile.txt"),
                schema_sha256=digest_file(TENANT / "schema" / "candidate.schema.json"),
            )
        self.assertEqual(result["decision"], "hold")
        self.assertEqual(bindings, {})
        self.assertEqual(records, {})
        self.assertEqual(
            {row["code"] for row in result["issues"]},
            {
                "frame_basis_not_admitted",
                "missing_capability_envelope",
                "missing_compile_grant",
                "missing_compile_activation",
                "missing_frame_acceptance",
            },
        )

    def test_preflight_accepts_only_exact_external_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths, overlay = preflight_fixture(root, self.expected_basis)

            def evaluate() -> tuple[dict, dict, dict]:
                return semantic_compile_preflight(
                    frame_acceptance_path=paths["frame_acceptance"],
                    compile_grant_path=paths["compile_grant"],
                    compile_activation_path=paths["compile_activation"],
                    capability_envelope_path=paths["capability_envelope"],
                    overlay=overlay,
                    frame=load_json(TENANT / "profile" / "stdo-core-frame.json"),
                    calculus=self.expected_basis["calculus"],
                    signature_ref=self.expected_basis["signature"],
                    contract_ref=self.expected_basis["interpretation_contract"],
                    source_packet_ref=self.expected_basis["source_packet"],
                    prompt_sha256=digest_file(TENANT / "prompt" / "v_compile.txt"),
                    schema_sha256=digest_file(
                        TENANT / "schema" / "candidate.schema.json"
                    ),
                )

            result, bindings, records = evaluate()
            self.assertEqual(
                result,
                {
                    "kind": "stdo-representation.semantic-compilation-preflight-result",
                    "schema_version": 1,
                    "decision": "ready",
                    "issues": [],
                },
            )
            self.assertEqual(
                set(bindings),
                {
                    "frame_acceptance",
                    "compile_grant",
                    "compile_activation",
                    "capability_envelope",
                },
            )
            self.assertEqual(set(records), set(bindings))

            originals = {name: load_json(path) for name, path in paths.items()}

            def assert_mutation_refuses(
                name: str, field: str, value: object, expected_code: str
            ) -> None:
                mutated = copy.deepcopy(originals[name])
                mutated[field] = value
                paths[name].write_bytes(canonical_bytes(mutated))
                refused, refused_bindings, _ = evaluate()
                self.assertEqual(refused["decision"], "hold")
                self.assertEqual(refused_bindings, {})
                self.assertIn(expected_code, {row["code"] for row in refused["issues"]})
                paths[name].write_bytes(canonical_bytes(originals[name]))

            for field, value in {
                "actor_identity": "urn:test:forged-frame-actor",
                "authority_identity": "urn:test:forged-frame-authority",
                "grant_identity": "urn:test:forged-frame-grant",
                "grant_scope": "forged scope",
                "basis_refs": ["urn:test:forged-frame-basis"],
            }.items():
                assert_mutation_refuses(
                    "frame_acceptance", field, value, "frame_acceptance_mismatch"
                )

            for field, value in {
                "issuer_actor_identity": "urn:test:forged-grant-issuer",
                "authority_identity": "urn:test:forged-grant-authority",
                "parent_grant_identity": PRODUCT_OWNER_GRANT,
                "parent_grant_scope": "forged parent scope",
                "grantee_actor_identity": "urn:test:forged-grantee",
                "traversal_ref": "urn:test:forged-traversal",
                "functor_ref": "urn:stdo:concept:axiomatic-calculus:f-d",
                "subject_basis_identity": "urn:test:forged-subject-basis",
                "scope": "forged operation scope",
            }.items():
                if field == "parent_grant_identity":
                    value = "urn:stdo-representation:grant:semantic-compilation:1"
                assert_mutation_refuses(
                    "compile_grant",
                    field,
                    value,
                    "compile_grant_authority_mismatch",
                )

            assert_mutation_refuses(
                "compile_activation",
                "grant_identity",
                PRODUCT_OWNER_GRANT,
                "compile_activation_mismatch",
            )

            capability = load_json(paths["capability_envelope"])
            capability["output_schema_sha256"] = "sha256:" + "0" * 64
            paths["capability_envelope"].write_bytes(canonical_bytes(capability))
            refused, refused_bindings, _ = evaluate()
            self.assertEqual(refused["decision"], "hold")
            self.assertEqual(refused_bindings, {})
            self.assertIn(
                "capability_envelope_mismatch",
                {row["code"] for row in refused["issues"]},
            )

    def test_signature_is_absolute_closed_and_refdomain_total(self) -> None:
        self.assertEqual(validate_signature(self.signature), [])
        self.assertEqual(self.signature["identity"], SIGNATURE_IDENTITY)
        self.assertEqual(
            {
                row["population"]: row["identity"]
                for row in self.signature["record_kinds"]
            },
            RECORD_KIND_BY_POPULATION,
        )
        for family in ("sorts", "residual_kinds", "judgment_kinds", "stop_kinds"):
            self.assertTrue(all(":" in value for value in self.signature[family]))
        refs = {
            (row["population"], row["field"]): row
            for row in self.signature["reference_domains"]
        }
        for coordinate in {
            ("O", "sort"),
            ("E", "kind"),
            ("C", "kind"),
            ("C", "judgment_kind"),
            ("X", "kind"),
            ("J", "kind"),
            ("V", "stop_states"),
            ("T", "stop_states"),
        }:
            self.assertIn(coordinate, refs)
            self.assertTrue(refs[coordinate]["identity"].startswith("urn:"))
        transformation = next(
            row for row in self.signature["record_kinds"] if row["population"] == "T"
        )
        self.assertEqual(transformation["maximum_records"], 0)
        structure_permission = next(
            row
            for row in self.signature["traversal_permissions"]
            if row["traversal"]
            == "urn:stdo-representation:traversal:candidate-structure:3"
        )
        self.assertIn(
            "candidate_structure_evaluation_grant",
            structure_permission["domain"],
        )
        ungranted = copy.deepcopy(self.signature)
        next(
            row
            for row in ungranted["traversal_permissions"]
            if row["traversal"]
            == "urn:stdo-representation:traversal:candidate-structure:3"
        )["domain"].remove("candidate_structure_evaluation_grant")
        self.assertIn(
            "invalid_structure_traversal_permission",
            {row["code"] for row in validate_signature(ungranted)},
        )

    def test_nonempty_transformation_population_refuses_without_profile(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate["candidate_model"]["transformations"] = [{}]
        self.assertIn(
            "population_exceeds_declared_maximum",
            {row["code"] for row in self.issues(candidate)},
        )

    def test_identity_partition_and_signature_resolution_are_closed(self) -> None:
        missing = copy.deepcopy(self.candidate)
        missing["candidate_model"]["external_resolutions"] = []
        codes = {row["code"] for row in self.issues(missing)}
        self.assertTrue(
            any(code.startswith("missing_external_resolution:") for code in codes)
        )
        self.assertIn("model_basis_resolution_mismatch", codes)

        forged = copy.deepcopy(self.candidate)
        row = next(
            item
            for item in forged["candidate_model"]["external_resolutions"]
            if item["external_target_kind"].endswith("target-signature-member:1")
        )
        row["resolution_basis"] = "urn:stdo-index:signature:forged:1"
        self.assertIn(
            "signature_member_resolution_mismatch",
            {item["code"] for item in self.issues(forged)},
        )

    def test_kind_sort_and_stop_fields_use_refdomain(self) -> None:
        wrong_sort = copy.deepcopy(self.candidate)
        wrong_sort["candidate_model"]["semantic_objects"][0]["sort"] = RELATION_KINDS[
            "defines"
        ]
        self.assertIn(
            "wrong_external_reference_domain",
            {row["code"] for row in self.issues(wrong_sort)},
        )

        wrong_relation = copy.deepcopy(self.candidate)
        wrong_relation["candidate_model"]["typed_relations"][0][
            "kind"
        ] = CONSTRAINT_KINDS["axiom"]
        self.assertIn(
            "wrong_external_reference_domain",
            {row["code"] for row in self.issues(wrong_relation)},
        )

        wrong_stop = copy.deepcopy(self.candidate)
        wrong_stop["candidate_model"]["traversals"][0]["stop_states"] = [
            RELATION_KINDS["defines"]
        ]
        self.assertIn(
            "wrong_external_reference_domain",
            {row["code"] for row in self.issues(wrong_stop)},
        )

    def test_f_d_does_not_evaluate_semantic_truth(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        candidate["candidate_model"]["constraints"][0][
            "predicate"
        ] = "authority_is_not_conserved"
        candidate["candidate_model_content_identity"] = (
            "sha256:"
            + hashlib.sha256(canonical_bytes(candidate["candidate_model"])).hexdigest()
        )
        refresh_proposal_identity(candidate)
        self.assertEqual(self.issues(candidate), [])

    def test_judgment_population_cannot_smuggle_f_p_acceptance(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        subject = candidate["candidate_model"]["semantic_objects"][0]
        judgment = {
            "id": "urn:stdo-index:test:judgment",
            "kind": JUDGMENT_KINDS["semantic_selection"],
            "subject": subject["id"],
            "subject_digest": "sha256:"
            + hashlib.sha256(canonical_bytes(subject)).hexdigest(),
            "context": "urn:stdo-index:test:context",
            "owner": "urn:stdo-index:test:owner",
            "scope": GOVERNED_SCOPE,
            "basis": self.model_basis,
            "evaluator": "urn:stdo-index:test:owner",
            "authority": "urn:stdo-index:test:owner",
            "decision": "accepted",
            "evidence": ["urn:stdo-index:test:evidence"],
            "provenance": ["urn:stdo-index:test:evidence"],
            "decided_at": "2026-08-30T00:00:00Z",
        }
        add_local_record(candidate, "J", judgment)
        self.assertIn(
            "f_p_semantic_acceptance_judgment",
            {row["code"] for row in self.issues(candidate)},
        )

    def test_source_and_selection_population_are_conserved(self) -> None:
        missing_member = copy.deepcopy(self.candidate)
        missing_member["proposed_evaluated_members"].pop()
        self.assertIn(
            "source_inventory_mismatch",
            {row["code"] for row in self.issues(missing_member)},
        )

        unowned = copy.deepcopy(self.candidate)
        unowned["proposed_selections"][0]["model_record_refs"].pop()
        self.assertTrue(
            any(
                row["code"].startswith("record_selection_cardinality:")
                for row in self.issues(unowned)
            )
        )

    def test_non_retained_selection_cannot_own_model_records(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        retained = candidate["proposed_selections"][0]
        omitted = {
            **copy.deepcopy(retained),
            "selection_ref": "urn:stdo-representation:selection:omitted",
            "disposition": "omitted",
            "model_record_refs": [retained["model_record_refs"][0]],
            "rationale": "omitted material",
        }
        candidate["proposed_selections"].append(omitted)
        candidate["proposed_selections"].sort(
            key=lambda row: utf16_key(row["selection_ref"])
        )
        candidate["proposed_evaluated_members"][0]["selection_refs"] = sorted(
            [retained["selection_ref"], omitted["selection_ref"]], key=utf16_key
        )
        refresh_proposal_identity(candidate)
        codes = {row["code"] for row in self.issues(candidate)}
        self.assertIn("non_retained_selection_has_model_refs", codes)
        self.assertFalse(
            any(code.startswith("record_selection_cardinality:") for code in codes)
        )

    def test_record_provenance_is_total_subject_derived_and_congruent(self) -> None:
        model = self.candidate["candidate_model"]
        local_ids = {
            row["id"]
            for field in MODEL_FIELD_BY_POPULATION.values()
            for row in model[field]
        }
        self.assertEqual(
            {
                row["model_record_ref"]
                for row in self.candidate["proposed_record_provenance"]
            },
            local_ids,
        )

        missing = copy.deepcopy(self.candidate)
        missing_ref = missing["proposed_record_provenance"].pop()["model_record_ref"]
        refresh_proposal_identity(missing)
        self.assertIn(
            f"missing_record_provenance:{missing_ref}",
            {row["code"] for row in self.issues(missing)},
        )

        wrong_kind = copy.deepcopy(self.candidate)
        wrong_kind["proposed_record_provenance"][0]["provenance_kind"] = "model_local"
        refresh_proposal_identity(wrong_kind)
        self.assertIn(
            "unknown_provenance_kind",
            {row["code"] for row in self.issues(wrong_kind)},
        )

        wrong_address = copy.deepcopy(self.candidate)
        wrong_address["proposed_record_provenance"][0]["semantic_address"][
            "bounded_context"
        ] = "urn:stdo-index:test:wrong-context"
        refresh_proposal_identity(wrong_address)
        self.assertIn(
            "semantic_address_record_mismatch",
            {row["code"] for row in self.issues(wrong_address)},
        )

        unresolved_source = copy.deepcopy(self.candidate)
        unresolved_source["proposed_record_provenance"][0]["semantic_address"][
            "source_key"
        ] = "urn:test:caller-invented-source"
        refresh_proposal_identity(unresolved_source)
        self.assertIn(
            "unresolved_semantic_source_key",
            {row["code"] for row in self.issues(unresolved_source)},
        )

        unresolved_evidence = copy.deepcopy(self.candidate)
        unresolved_evidence["proposed_record_provenance"][0][
            "derivation_evidence_refs"
        ] = ["urn:test:caller-invented-evidence"]
        refresh_proposal_identity(unresolved_evidence)
        self.assertTrue(
            any(
                row["code"].startswith("unresolved_derivation_evidence:")
                for row in self.issues(unresolved_evidence)
            )
        )

        fragment = copy.deepcopy(self.candidate)
        fragment["proposed_record_provenance"][0]["source_locators"][0][
            "fragment"
        ] = "invented-anchor"
        refresh_proposal_identity(fragment)
        self.assertIn(
            "source_locator_fragment_not_null",
            {row["code"] for row in self.issues(fragment)},
        )

    def test_source_locator_order_and_selection_incidence_are_exact(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        first, second = candidate["source_members"][:2]
        second_locator = {
            "basis_uri": candidate["source_stdo_uri"],
            "member_path": second["member_path"],
            "member_sha256": second["member_sha256"],
            "fragment": None,
        }
        first_locator = {
            "basis_uri": candidate["source_stdo_uri"],
            "member_path": first["member_path"],
            "member_sha256": first["member_sha256"],
            "fragment": None,
        }
        candidate["proposed_selections"][0]["source_locators"] = sorted(
            [first_locator, second_locator], key=canonical_bytes, reverse=True
        )
        refresh_proposal_identity(candidate)
        codes = {row["code"] for row in self.issues(candidate)}
        self.assertIn("source_locators_not_sorted_unique", codes)
        self.assertTrue(
            any(
                code.startswith("selection_locator_without_member_reference:")
                for code in codes
            )
        )

        missing_incidence = copy.deepcopy(self.candidate)
        row = missing_incidence["proposed_record_provenance"][0]
        row["source_locators"] = [second_locator]
        row["semantic_address"]["source_key"] = (
            candidate["source_stdo_uri"] + "standards/" + second["member_path"]
        )
        refresh_proposal_identity(missing_incidence)
        self.assertTrue(
            any(
                code.startswith("selection_missing_record_source_locator:")
                for code in {
                    issue_row["code"] for issue_row in self.issues(missing_incidence)
                }
            )
        )

    def test_source_native_residual_does_not_require_compilation_residual(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        residual_kind = RESIDUAL_KINDS["unresolved_semantics"]
        resolution = signature_member_resolution(
            residual_kind, RESIDUAL_DOMAIN, self.expected_basis
        )
        model = candidate["candidate_model"]
        model["identities"] = sorted(
            [*model["identities"], residual_kind], key=utf16_key
        )
        model["external_resolutions"].append(resolution)
        model["external_resolutions"].sort(
            key=lambda row: utf16_key(row["external_identity"])
        )
        residual = {
            "id": "urn:stdo-index:test:source-native-residual",
            "subject": "urn:stdo-index:test:subject",
            "kind": residual_kind,
            "uncertainty": "source_native_uncertainty",
            "consequence": "preserve_uncertainty",
            "context": "urn:stdo-index:test:context",
            "owner": "urn:stdo-index:test:owner",
            "scope": GOVERNED_SCOPE,
            "basis": self.model_basis,
            "re_entry": "semantic_selection",
            "invalidation": "source_change",
        }
        add_local_record(candidate, "X", residual)
        self.assertEqual(candidate["compilation_residuals"], [])
        self.assertEqual(self.issues(candidate), [])

        unresolved = copy.deepcopy(candidate)
        unresolved["compilation_residuals"] = [
            {
                "residual_ref": "urn:stdo-representation:compilation-residual:test",
                "source_locators": copy.deepcopy(
                    unresolved["proposed_selections"][0]["source_locators"]
                ),
                "statement": "bad model residual reference",
                "consequence": "hold",
                "model_residual_refs": ["urn:stdo-index:test:subject"],
                "re_entry_route": "semantic_selection",
            }
        ]
        refresh_proposal_identity(unresolved)
        self.assertIn(
            "unknown_residual_ref", {row["code"] for row in self.issues(unresolved)}
        )

    def test_compilation_residual_identity_must_be_absolute_and_typed(self) -> None:
        for residual_ref in ("relative-id", 7):
            candidate = copy.deepcopy(self.candidate)
            candidate["compilation_residuals"] = [
                {
                    "residual_ref": residual_ref,
                    "source_locators": copy.deepcopy(
                        candidate["proposed_selections"][0]["source_locators"]
                    ),
                    "statement": "identity falsifier",
                    "consequence": "hold",
                    "model_residual_refs": [],
                    "re_entry_route": "semantic_selection",
                }
            ]
            refresh_proposal_identity(candidate)
            with self.subTest(residual_ref=residual_ref):
                self.assertIn(
                    "invalid_compilation_residual_identity",
                    {row["code"] for row in self.issues(candidate)},
                )

    def test_generated_source_key_reproduces_jcs_then_fails_closed(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        locator = copy.deepcopy(
            candidate["proposed_selections"][0]["source_locators"][0]
        )
        local_key = "specification-method"
        source_key = generated_source_key(locator, local_key)
        self.assertEqual(
            source_key,
            "urn:stdo-representation:source-key:sha256:"
            "a948cac0a8d1dbb3886d85bdb2e2bd46f8dcf7e42c5bacefb45690311968a2e2",
        )
        candidate["proposed_generated_source_keys"] = [
            {
                "source_key": source_key,
                "primary_source_locator": locator,
                "local_declaration_key": local_key,
            }
        ]
        candidate["proposed_record_provenance"][0]["semantic_address"][
            "source_key"
        ] = source_key
        refresh_proposal_identity(candidate)
        self.assertEqual(self.issues(candidate), [])

        repeated_local_key = copy.deepcopy(candidate)
        second_member = repeated_local_key["source_members"][1]
        second_locator = {
            "basis_uri": repeated_local_key["source_stdo_uri"],
            "member_path": second_member["member_path"],
            "member_sha256": second_member["member_sha256"],
            "fragment": None,
        }
        second_source_key = generated_source_key(second_locator, local_key)
        repeated_local_key["proposed_generated_source_keys"].append(
            {
                "source_key": second_source_key,
                "primary_source_locator": second_locator,
                "local_declaration_key": local_key,
            }
        )
        repeated_local_key["proposed_generated_source_keys"].sort(
            key=lambda row: utf16_key(row["source_key"])
        )
        repeated_local_key["proposed_record_provenance"][1]["semantic_address"][
            "source_key"
        ] = second_source_key
        repeated_local_key["proposed_record_provenance"][1]["source_locators"] = [
            second_locator
        ]
        repeated_local_key["proposed_selections"][0]["source_locators"] = sorted(
            [locator, second_locator], key=canonical_bytes
        )
        repeated_local_key["proposed_evaluated_members"][1][
            "disposition"
        ] = "contains_retained_material"
        repeated_local_key["proposed_evaluated_members"][1]["selection_refs"] = [
            repeated_local_key["proposed_selections"][0]["selection_ref"]
        ]
        refresh_proposal_identity(repeated_local_key)
        self.assertEqual(self.issues(repeated_local_key), [])

        unlinked = copy.deepcopy(candidate)
        provenance = unlinked["proposed_record_provenance"][0]
        locator_for_source = provenance["source_locators"][0]
        provenance["semantic_address"]["source_key"] = (
            locator_for_source["basis_uri"]
            + "standards/"
            + locator_for_source["member_path"]
        )
        refresh_proposal_identity(unlinked)
        self.assertTrue(
            any(
                row["code"].startswith("generated_source_key_coverage_mismatch:")
                for row in self.issues(unlinked)
            )
        )

        wrong_digest = copy.deepcopy(candidate)
        wrong_digest["proposed_generated_source_keys"][0]["source_key"] = (
            "urn:stdo-representation:source-key:sha256:" + "0" * 64
        )
        refresh_proposal_identity(wrong_digest)
        self.assertIn(
            "generated_source_key_derivation_mismatch",
            {row["code"] for row in self.issues(wrong_digest)},
        )

    def test_proposal_identity_families_are_disjoint(self) -> None:
        candidate = copy.deepcopy(self.candidate)
        colliding_identity = candidate["candidate_model"]["semantic_objects"][0]["id"]
        old_selection_ref = candidate["proposed_selections"][0]["selection_ref"]
        candidate["proposed_selections"][0]["selection_ref"] = colliding_identity
        candidate["proposed_evaluated_members"][0]["selection_refs"] = [
            colliding_identity
        ]
        self.assertNotEqual(colliding_identity, old_selection_ref)
        refresh_proposal_identity(candidate)
        self.assertTrue(
            any(
                row["code"].startswith("cross_kind_identity_collision:")
                for row in self.issues(candidate)
            )
        )

        evaluated_collision = copy.deepcopy(self.candidate)
        first_member = evaluated_collision["proposed_evaluated_members"][0]
        evaluated_member_identity = (
            evaluated_collision["source_stdo_uri"]
            + "standards/"
            + first_member["member_path"]
        )
        evaluated_collision["proposed_selections"][0][
            "selection_ref"
        ] = evaluated_member_identity
        first_member["selection_refs"] = [evaluated_member_identity]
        refresh_proposal_identity(evaluated_collision)
        self.assertTrue(
            any(
                row["code"] == "cross_kind_identity_collision:"
                f"{evaluated_member_identity}:evaluated_member,selection"
                for row in self.issues(evaluated_collision)
            )
        )

    def test_evaluated_member_summary_matches_reached_material(self) -> None:
        selection_ref = self.candidate["proposed_selections"][0]["selection_ref"]

        no_material = copy.deepcopy(self.candidate)
        no_material["proposed_evaluated_members"][1]["selection_refs"] = [selection_ref]
        refresh_proposal_identity(no_material)
        self.assertIn(
            "no_material_disposition_has_selection_refs",
            {row["code"] for row in self.issues(no_material)},
        )

        no_reached_material = copy.deepcopy(self.candidate)
        no_reached_material["proposed_evaluated_members"][0]["selection_refs"] = []
        refresh_proposal_identity(no_reached_material)
        self.assertIn(
            "retained_material_not_reached",
            {row["code"] for row in self.issues(no_reached_material)},
        )

        for disposition in ("uncertain", "refused"):
            non_residual = copy.deepcopy(self.candidate)
            non_residual["proposed_evaluated_members"][1]["disposition"] = disposition
            non_residual["proposed_evaluated_members"][1]["selection_refs"] = [
                selection_ref
            ]
            refresh_proposal_identity(non_residual)
            with self.subTest(disposition=disposition):
                self.assertIn(
                    "uncertain_or_refused_member_not_residual_only",
                    {row["code"] for row in self.issues(non_residual)},
                )

    def test_candidate_coordinate_and_provenance_forgery_refuse(self) -> None:
        forged = copy.deepcopy(self.candidate)
        forged["frame_basis_sha256"] = "sha256:" + "0" * 64
        forged["candidate_model_content_identity"] = "sha256:" + "0" * 64
        forged["compiler_invocation"]["raw_output_sha256"] = "sha256:" + "0" * 64
        codes = {row["code"] for row in self.issues(forged)}
        self.assertIn("basis_mismatch", codes)
        self.assertIn("model_content_identity_mismatch", codes)
        self.assertIn("provenance_binding_mismatch", codes)

    def test_candidate_structure_grant_is_exact_external_authority(self) -> None:
        grant = candidate_structure_grant(self.candidate, self.expected_basis)
        grant_bytes = canonical_bytes(grant)
        grant_identity = validate_candidate_structure_grant(
            grant,
            grant_bytes,
            self.candidate,
            self.expected_basis,
        )
        self.assertEqual(grant_identity, candidate_structure_grant_identity(grant))
        self.assertTrue(
            grant_identity.startswith(
                "urn:stdo-representation:candidate-structure-grant:sha256:"
            )
        )
        self.assertNotIn("identity", grant)

        with self.assertRaisesRegex(ValueError, "invalid candidate-structure"):
            validate_candidate_structure_grant(
                None,
                b"null",
                self.candidate,
                self.expected_basis,
            )
        with self.assertRaisesRegex(ValueError, "unframed JCS"):
            validate_candidate_structure_grant(
                grant,
                grant_bytes + b"\n",
                self.candidate,
                self.expected_basis,
            )

        falsifiers = {
            "parent_grant_identity": "urn:test:self-issued-grant",
            "grantee_identity": "urn:test:wrong-evaluator",
            "subject_sha256": "sha256:" + "0" * 64,
            "signature_sha256": "sha256:" + "1" * 64,
            "interpretation_contract_sha256": "sha256:" + "2" * 64,
            "what_member_set_identity": "sha256:" + "3" * 64,
            "frame_basis_sha256": "sha256:" + "4" * 64,
            "source_sha256": "sha256:" + "5" * 64,
            "grant_scope": "ambient structural authority",
        }
        for field, value in falsifiers.items():
            forged = {**grant, field: value}
            with self.subTest(field=field):
                with self.assertRaisesRegex(ValueError, field):
                    validate_candidate_structure_grant(
                        forged,
                        canonical_bytes(forged),
                        self.candidate,
                        self.expected_basis,
                    )

        bad_evidence = {
            **grant,
            "evidence_refs": ["urn:test:z", "urn:test:a"],
        }
        with self.assertRaisesRegex(ValueError, "grant evidence"):
            validate_candidate_structure_grant(
                bad_evidence,
                canonical_bytes(bad_evidence),
                self.candidate,
                self.expected_basis,
            )
        bad_time = {**grant, "issued_at": "not-a-time"}
        with self.assertRaisesRegex(ValueError, "issue time"):
            validate_candidate_structure_grant(
                bad_time,
                canonical_bytes(bad_time),
                self.candidate,
                self.expected_basis,
            )

    def test_candidate_structure_result_identity_is_external_and_content_derived(
        self,
    ) -> None:
        checks = {
            "canonical_bytes": True,
            "source_inventory": True,
            "population_totality": True,
            "record_shapes": True,
            "identity_derivation": True,
            "reference_domains": True,
            "external_resolutions": True,
            "basis_coherence": True,
            "ordering": True,
            "provenance_binding": True,
        }
        result = {
            "kind": "stdo-representation.candidate-structure-result",
            "schema_version": 2,
            "semantic_compilation_candidate_identity": (
                "urn:stdo-representation:semantic-compilation-candidate:sha256:"
                + "1" * 64
            ),
            "semantic_compilation_candidate_sha256": "sha256:" + "1" * 64,
            "calculus_basis_identity": self.expected_basis["calculus"]["identity"],
            "signature_identity": self.signature["identity"],
            "interpretation_contract_identity": self.contract["identity"],
            "traversal_ref": (
                "urn:stdo-representation:traversal:candidate-structure:3"
            ),
            "functor_ref": "urn:stdo:concept:axiomatic-calculus:f-d",
            "evaluator_identity": "urn:stdo-index:evaluator:candidate-structure:4",
            "checks": checks,
            "decision": "eligible",
            "evaluated_at": "2026-08-30T00:00:00Z",
            "evidence_refs": ["urn:stdo-representation:evidence:test"],
        }
        identity, result_sha = candidate_structure_result_identity(result)
        self.assertEqual(result_sha, digest_bytes(canonical_bytes(result)))
        self.assertEqual(
            identity,
            "urn:stdo-representation:candidate-structure-result:sha256:"
            + result_sha.removeprefix("sha256:"),
        )
        self.assertNotIn("candidate_structure_result_identity", result)

    def test_immutable_publication_refuses_changed_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "artifact.json"
            publish_immutable(path, b'{"value":1}')
            publish_immutable(path, b'{"value":1}')
            self.assertEqual(path.read_bytes(), b'{"value":1}')
            with self.assertRaisesRegex(ValueError, "immutable publication conflict"):
                publish_immutable(path, b'{"value":2}')
            self.assertEqual(path.read_bytes(), b'{"value":1}')

    def test_raw_output_binding_is_write_once_and_content_addressed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "20260830T000000Z"
            run.mkdir()
            first = root / "first.json"
            first.write_bytes(b'{"answer":1}\n')
            artifact, identity, raw_sha = publish_raw_output(run, first)
            self.assertEqual(artifact, raw_output_artifact_path(run, raw_sha))
            self.assertEqual(identity, raw_output_identity(raw_sha))
            self.assertEqual(resolve_raw_output(run), (artifact, identity, raw_sha))

            publish_raw_output(run, first)
            second = root / "second.json"
            second.write_bytes(b'{"answer":2}\n')
            with self.assertRaisesRegex(ValueError, "immutable publication conflict"):
                publish_raw_output(run, second)
            self.assertEqual(resolve_raw_output(run), (artifact, identity, raw_sha))
            self.assertEqual(artifact.read_bytes(), first.read_bytes())
            second_sha = "sha256:" + hashlib.sha256(second.read_bytes()).hexdigest()
            self.assertFalse(raw_output_artifact_path(run, second_sha).exists())

    def test_candidate_and_result_coordinates_preserve_prior_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory) / "20260830T000000Z"
            run.mkdir()
            what = "sha256:" + "1" * 64
            first_candidate_sha = "sha256:" + "2" * 64
            second_candidate_sha = "sha256:" + "3" * 64
            first_candidate = candidate_artifact_path(run, what, first_candidate_sha)
            second_candidate = candidate_artifact_path(run, what, second_candidate_sha)
            self.assertNotEqual(first_candidate, second_candidate)
            publish_immutable(first_candidate, b'{"candidate":1}')
            publish_immutable(second_candidate, b'{"candidate":2}')

            first_result = (
                evaluation_artifact_root(run, first_candidate_sha, "sha256:" + "4" * 64)
                / "candidate-structure-result.json"
            )
            second_result = (
                evaluation_artifact_root(run, first_candidate_sha, "sha256:" + "5" * 64)
                / "candidate-structure-result.json"
            )
            publish_immutable(first_result, b'{"result":1}')
            publish_immutable(second_result, b'{"result":2}')
            self.assertEqual(first_candidate.read_bytes(), b'{"candidate":1}')
            self.assertEqual(first_result.read_bytes(), b'{"result":1}')
            self.assertEqual(second_result.read_bytes(), b'{"result":2}')

    def test_invalid_evaluation_grant_cannot_change_candidate_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory) / "20260830T000000Z"
            run.mkdir()
            candidate_identity, candidate_sha = semantic_compilation_candidate_identity(
                self.candidate
            )
            self.assertTrue(
                candidate_identity.endswith(candidate_sha.removeprefix("sha256:"))
            )
            path = candidate_artifact_path(
                run,
                self.expected_basis["what_member_set_identity"],
                candidate_sha,
            )
            original = canonical_bytes(self.candidate)
            publish_immutable(path, original)
            invalid_grant = {
                **candidate_structure_grant(self.candidate, self.expected_basis),
                "subject_sha256": "sha256:" + "0" * 64,
            }
            with self.assertRaisesRegex(ValueError, "subject_sha256"):
                validate_candidate_structure_grant(
                    invalid_grant,
                    canonical_bytes(invalid_grant),
                    self.candidate,
                    self.expected_basis,
                )
            self.assertEqual(path.read_bytes(), original)

    def test_transport_schema_is_api_subset_and_evaluator_keeps_lost_law(self) -> None:
        schema = load_json(TENANT / "schema" / "candidate.schema.json")
        verify_transport_schema(schema, TENANT / "schema" / "candidate.schema.json")

        def keywords(value: object) -> set[str]:
            if isinstance(value, dict):
                return set(value) | {
                    keyword for child in value.values() for keyword in keywords(child)
                }
            if isinstance(value, list):
                return {keyword for child in value for keyword in keywords(child)}
            return set()

        self.assertTrue({"uniqueItems", "minLength"}.isdisjoint(keywords(schema)))
        self.assertEqual(schema["required"], ["kind", "schema_version", "payload"])
        self.assertEqual(set(schema["properties"]), set(schema["required"]))

        def assert_api_subset(value: object) -> None:
            if isinstance(value, dict):
                if value.get("type") == "object":
                    self.assertFalse(value.get("additionalProperties", True))
                    self.assertEqual(
                        set(value.get("properties", {})),
                        set(value.get("required", [])),
                    )
                if "const" in value or "enum" in value:
                    self.assertIn("type", value)
                for child in value.values():
                    assert_api_subset(child)
            elif isinstance(value, list):
                for child in value:
                    assert_api_subset(child)

        assert_api_subset(schema)
        for path in (
            ("properties", "kind"),
            ("$defs", "externalResolutionWitness", "properties", "decision"),
        ):
            invalid = copy.deepcopy(schema)
            node = invalid
            for key in path:
                node = node[key]
            del node["type"]
            with self.subTest(path=".".join(path)):
                with self.assertRaisesRegex(ValueError, "lacks explicit type"):
                    verify_transport_schema(
                        invalid, TENANT / "schema" / "candidate.schema.json"
                    )

        invalid = copy.deepcopy(schema)
        invalid["$defs"]["stopPayload"]["properties"]["reason_code"]["type"] = "integer"
        with self.assertRaisesRegex(ValueError, "enum disagrees with type"):
            verify_transport_schema(
                invalid, TENANT / "schema" / "candidate.schema.json"
            )
        decoded, issues = decode_result_envelope(self.proposal)
        self.assertEqual(issues, [])
        self.assertEqual(decoded, self.proposal)
        wrong_branch = copy.deepcopy(self.proposal)
        wrong_branch["kind"] = "stdo-representation.semantic-compilation-stop"
        self.assertIsNone(decode_result_envelope(wrong_branch)[0])

        duplicate = copy.deepcopy(self.candidate)
        duplicate["candidate_model"]["identities"].append(
            duplicate["candidate_model"]["identities"][-1]
        )
        self.assertIn(
            "duplicate_array_value", {row["code"] for row in self.issues(duplicate)}
        )

        empty = copy.deepcopy(self.candidate)
        empty["candidate_model"]["semantic_objects"][0]["value"] = ""
        self.assertIn(
            "expected_nonempty_string", {row["code"] for row in self.issues(empty)}
        )

    def test_lawful_stop_is_distinct_from_proposal(self) -> None:
        envelope = {
            "kind": "stdo-representation.semantic-compilation-stop",
            "schema_version": PROPOSAL_SCHEMA_VERSION,
            "payload": {
                "stop_state": STOP_KINDS["gap"],
                "reason_code": "basis_gap",
                "re_entry_refs": ["stdo://releases/v2.5.0-rc.1/"],
            },
        }
        stop, envelope_issues = decode_result_envelope(envelope)
        self.assertEqual(envelope_issues, [])
        self.assertIsNotNone(stop)
        self.assertEqual(
            validate_stop(stop, self.expected_basis, self.signature, self.model_basis),
            [],
        )
        stop["payload"]["re_entry_refs"] *= 2
        self.assertIn(
            "duplicate_array_value",
            {
                row["code"]
                for row in validate_stop(
                    stop, self.expected_basis, self.signature, self.model_basis
                )
            },
        )
        stop["payload"]["re_entry_refs"] = ["not-an-identity"]
        self.assertIn(
            "invalid_re_entry_identity",
            {
                row["code"]
                for row in validate_stop(
                    stop, self.expected_basis, self.signature, self.model_basis
                )
            },
        )

    def test_acquisition_reconstructs_what_and_model_basis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths, overlay = preflight_fixture(root, self.expected_basis)
            (
                preflight,
                preflight_bindings,
                preflight_records,
            ) = semantic_compile_preflight(
                frame_acceptance_path=paths["frame_acceptance"],
                compile_grant_path=paths["compile_grant"],
                compile_activation_path=paths["compile_activation"],
                capability_envelope_path=paths["capability_envelope"],
                overlay=overlay,
                frame=load_json(TENANT / "profile" / "stdo-core-frame.json"),
                calculus=self.expected_basis["calculus"],
                signature_ref=self.expected_basis["signature"],
                contract_ref=self.expected_basis["interpretation_contract"],
                source_packet_ref=self.expected_basis["source_packet"],
                prompt_sha256=digest_file(TENANT / "prompt" / "v_compile.txt"),
                schema_sha256=digest_file(TENANT / "schema" / "candidate.schema.json"),
            )
            self.assertEqual(preflight["decision"], "ready")
            run = root / "20260830T000000Z"
            run.mkdir()
            basis = {
                **copy.deepcopy(self.expected_basis),
                "kind": "stdo-index.prototype-basis",
                "schema_version": 3,
                "compiler_prompt_sha256": "sha256:" + "4" * 64,
                "transport_schema_sha256": "sha256:" + "5" * 64,
                "preflight": preflight_bindings,
            }
            (run / "basis.json").write_bytes(canonical_bytes(basis) + b"\n")
            (run / "source-manifest.json").write_bytes(
                canonical_bytes(self.source_manifest) + b"\n"
            )
            (run / "invocation.txt").write_text("invocation", encoding="utf-8")
            (run / "sealed-invocation.txt").write_text("sealed", encoding="utf-8")
            preflight_root = run / "preflight"
            preflight_root.mkdir()
            for name, record in preflight_records.items():
                (preflight_root / f"{name}.json").write_bytes(canonical_bytes(record))
            receipt = {
                "kind": "stdo-index.prototype-acquisition",
                "schema_version": 3,
                "run_id": run.name,
                "basis_sha256": digest_file(run / "basis.json"),
                "source_manifest_sha256": digest_file(run / "source-manifest.json"),
                "invocation_sha256": digest_file(run / "invocation.txt"),
                "sealed_invocation_sha256": digest_file(run / "sealed-invocation.txt"),
                "calculus_basis_sha256": self.expected_basis["calculus"][
                    "record_sha256"
                ],
                "calculus_basis_identity": self.expected_basis["calculus"]["identity"],
                "preflight": preflight_bindings,
                "model_basis": self.model_basis,
                "status": "inputs_acquired",
            }
            self.assertEqual(
                verify_run_acquisition(
                    run,
                    run / "basis.json",
                    run / "source-manifest.json",
                    receipt,
                    self.expected_basis,
                    self.source_manifest,
                ),
                self.model_basis,
            )
            (run / "acquisition.json").write_bytes(canonical_bytes(receipt) + b"\n")
            provenance_bundle = build_compiler_provenance_bundle(run)
            provenance_bytes = canonical_bytes(provenance_bundle)
            resolved_members = verify_run_compiler_provenance_bundle(
                run,
                provenance_bundle,
                provenance_bytes,
            )
            verify_compiler_provenance_bundle(
                provenance_bundle,
                provenance_bytes,
                resolved_members,
            )
            self.assertEqual(
                [row["member_kind"] for row in provenance_bundle["members"]],
                sorted(COMPILER_PROVENANCE_MEMBER_FILES, key=utf16_key),
            )
            self.assertEqual(
                self.expected_basis["what_member_set_identity"],
                what_member_set_identity(),
            )

    def test_full_sealed_packet_is_lossless_and_within_codex_limit(self) -> None:
        frame = load_json(TENANT / "profile" / "stdo-core-frame.json")
        prompt = (
            (TENANT / "prompt" / "v_compile.txt").read_text(encoding="utf-8").strip()
        )
        sealed = build_sealed_invocation(
            prompt,
            self.model_basis,
            model_basis_resolution(self.model_basis, self.expected_basis),
            self.compiler_invocation,
            self.expected_basis,
            self.signature,
            self.contract,
            frame,
            self.source_manifest,
        )
        self.assertLessEqual(len(sealed), 1_048_576)
        self.assertNotIn("<calculus_source>", sealed)
        source_root = Path(self.source_manifest["installed_root"])
        for member in self.source_manifest["supplied_members"]:
            marker = (
                f"<member path={json.dumps(member['path'])} "
                f"sha256={json.dumps(member['sha256'])}>"
            )
            self.assertEqual(sealed.count(marker), 1)
            member_bytes = (source_root / member["path"]).read_bytes()
            self.assertEqual(
                "sha256:" + hashlib.sha256(member_bytes).hexdigest(),
                member["sha256"],
            )
            self.assertIn(member_bytes.decode("utf-8"), sealed)
        calculus = (source_root / "AXIOMATIC_CALCULUS.md").read_text(encoding="utf-8")
        self.assertEqual(sealed.count(calculus), 1)

    def test_historical_rc3_run_is_byte_for_byte_unchanged(self) -> None:
        actual = {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in HISTORICAL_RUN.iterdir()
            if path.is_file()
        }
        self.assertEqual(actual, HISTORICAL_HASHES)


if __name__ == "__main__":
    unittest.main()
