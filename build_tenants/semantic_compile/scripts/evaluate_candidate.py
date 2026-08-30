#!/usr/bin/env python3
"""Evaluate structure of an unchanged semantic-compilation proposal."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any

from acquire_basis import (
    compiler_provenance_bundle_ref,
    DEFAULT_CALCULUS_BASIS,
    DEFAULT_DERIVATION_STDO,
    DEFAULT_STDO,
    canonical_bytes,
    digest_bytes,
    digest_file,
    load_json,
    model_basis_identity,
    model_basis_resolution,
    PRODUCT_OWNER_ACTOR,
    PRODUCT_OWNER_AUTHORITY,
    PRODUCT_OWNER_GRANT,
    PRODUCT_OWNER_GRANT_SCOPE,
    PRODUCT_PATH,
    signature_member_resolution,
    SUBJECT_BASIS_IDENTITY,
    TIMESTAMP_RE,
    utf16_key,
    verify_calculus_basis_candidate,
    verify_compilation_contract,
    verify_compiler_provenance_bundle,
    verify_frame_configuration,
    verify_manifest,
    verify_run_compiler_provenance_bundle,
    verify_transport_schema,
    what_member_set_identity,
)


TENANT = Path(__file__).resolve().parents[1]
CANDIDATE_SCHEMA_VERSION = 3
PROPOSAL_SCHEMA_VERSION = 2
SIGNATURE_SCHEMA_VERSION = 2
STRUCTURE_RESULT_SCHEMA_VERSION = 2
COMPILE_TRAVERSAL = "urn:stdo-representation:traversal:semantic-compile:7"
STRUCTURE_TRAVERSAL = "urn:stdo-representation:traversal:candidate-structure:3"
SELECTION_TRAVERSAL = "urn:stdo-representation:traversal:semantic-selection:2"
F_D = "urn:stdo:concept:axiomatic-calculus:f-d"
F_P = "urn:stdo:concept:axiomatic-calculus:f-p"
F_H = "urn:stdo:concept:axiomatic-calculus:f-h"
SIGNATURE_IDENTITY = "urn:stdo-index:signature:stdo:7"
EVALUATOR_IDENTITY = "urn:stdo-index:evaluator:candidate-structure:4"
CANDIDATE_STRUCTURE_GRANT_SCOPE = (
    "Evaluate the exact unchanged SemanticCompilationCandidate under "
    "F_D[v_candidate_structure] for declared structural checks only; grants no "
    "construction, repair, semantic selection, acceptance, carrier, release, or "
    "runtime authority."
)
CANDIDATE_STRUCTURE_GRANT_SOURCE_REF = "./specification/PRODUCT.md#product-authority"


def signature_member(family: str, label: str) -> str:
    return f"urn:stdo-index:stdo:{family}:{label.replace('_', '-')}:1"


SORTS = {
    label: signature_member("sort", label)
    for label in (
        "authority",
        "bounded_context",
        "capability",
        "concept",
        "constraint_law",
        "evidence",
        "frame",
        "functor_kind",
        "judgment_kind",
        "lifecycle_state",
        "method",
        "product_kind",
        "relation_kind",
        "role",
        "source_member",
        "stop_kind",
        "work_surface",
    )
}
RELATION_KINDS = {
    label: signature_member("relation-kind", label)
    for label in (
        "binds",
        "classifies",
        "conserves",
        "defines",
        "derives_from",
        "excludes",
        "governs",
        "invalidates",
        "owns",
        "precedes",
        "projects",
        "refines",
        "requires",
        "specializes",
        "supersedes",
    )
}
CONSTRAINT_KINDS = {
    label: signature_member("constraint-kind", label)
    for label in (
        "admission",
        "axiom",
        "invariant",
        "obligation",
        "prohibition",
        "refusal",
    )
}
RESIDUAL_KINDS = {
    label: signature_member("residual-kind", label)
    for label in (
        "basis_gap",
        "possible_compression_loss",
        "unmodeled_member",
        "unresolved_semantics",
    )
}
JUDGMENT_KINDS = {
    label: signature_member("judgment-kind", label)
    for label in (
        "candidate_structure",
        "carrier_admission",
        "frame_evaluation",
        "semantic_selection",
    )
}
STOP_KINDS = {
    label: signature_member("stop-kind", label)
    for label in (
        "accepted",
        "admitted",
        "candidate",
        "eligible",
        "gap",
        "hold",
        "refusal",
        "rejected",
        "rework",
        "satisfied",
        "falsified",
        "indeterminate",
    )
}
POPULATIONS = ("O", "E", "C", "L", "X", "V", "T", "J")
MODEL_FIELD_BY_POPULATION = {
    "O": "semantic_objects",
    "E": "typed_relations",
    "C": "constraints",
    "L": "latitudes",
    "X": "residuals",
    "V": "traversals",
    "T": "transformations",
    "J": "judgments",
}
CANDIDATE_PAYLOAD_FIELDS = {
    "calculus_basis_identity",
    "source_stdo_uri",
    "source_stdo_manifest_sha256",
    "source_member_set_sha256",
    "source_members",
    "subject_basis_identity",
    "what_member_set_identity",
    "signature_identity",
    "signature_sha256",
    "interpretation_contract_identity",
    "interpretation_contract_sha256",
    "frame_basis_identity",
    "frame_basis_sha256",
    "selected_frame_refs",
    "candidate_model",
    "candidate_model_content_identity",
    "proposed_record_provenance",
    "proposed_evaluated_members",
    "proposed_selections",
    "proposed_generated_source_keys",
    "compilation_residuals",
    "stop_state",
}
RECORD_KIND_BY_POPULATION = {
    "O": "urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object",
    "E": "urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation",
    "C": "urn:stdo:concept:axiomatic-calculus:record-kind:constraint",
    "L": "urn:stdo:concept:axiomatic-calculus:record-kind:latitude",
    "X": "urn:stdo:concept:axiomatic-calculus:record-kind:residual",
    "V": "urn:stdo:concept:axiomatic-calculus:record-kind:traversal",
    "T": "urn:stdo:concept:axiomatic-calculus:record-kind:transformation",
    "J": "urn:stdo:concept:axiomatic-calculus:record-kind:judgment",
}
POPULATION_BY_RECORD_KIND = {
    record_kind: population
    for population, record_kind in RECORD_KIND_BY_POPULATION.items()
}
RECORD_FIELDS = {
    "O": {"id", "sort", "context", "owner", "scope", "basis", "value"},
    "E": {
        "id",
        "kind",
        "source",
        "target",
        "context",
        "owner",
        "scope",
        "basis",
        "qualifiers",
    },
    "C": {
        "id",
        "kind",
        "applies_to",
        "predicate",
        "context",
        "owner",
        "scope",
        "basis",
        "judgment_kind",
        "latitude_ref",
        "refusal",
    },
    "L": {
        "id",
        "applies_to",
        "allowed_variation",
        "forbidden_variation",
        "context",
        "owner",
        "scope",
        "basis",
        "invalidation",
    },
    "X": {
        "id",
        "subject",
        "kind",
        "uncertainty",
        "consequence",
        "context",
        "owner",
        "scope",
        "basis",
        "re_entry",
        "invalidation",
    },
    "V": {
        "id",
        "domain",
        "codomain",
        "context",
        "owner",
        "scope",
        "basis",
        "preconditions",
        "postconditions",
        "authority",
        "evidence",
        "provenance",
        "stop_states",
    },
    "T": {
        "id",
        "traversal",
        "domain_model",
        "codomain_model",
        "context",
        "owner",
        "scope",
        "basis",
        "operation_authority",
        "preconditions",
        "preservation_relation",
        "preserved",
        "introduced",
        "removed",
        "external_preserved",
        "external_introduced",
        "external_removed",
        "external_resolution_witnesses",
        "residuals",
        "evidence",
        "provenance",
        "stop_states",
        "invalidation",
        "re_entry",
    },
    "J": {
        "id",
        "kind",
        "subject",
        "subject_digest",
        "context",
        "owner",
        "scope",
        "basis",
        "evaluator",
        "authority",
        "decision",
        "evidence",
        "provenance",
        "decided_at",
    },
}
ARRAY_FIELDS = {
    "E": {"qualifiers"},
    "L": {"allowed_variation", "forbidden_variation"},
    "V": {"preconditions", "postconditions", "evidence", "provenance", "stop_states"},
    "T": {
        "preconditions",
        "preserved",
        "introduced",
        "removed",
        "external_preserved",
        "external_introduced",
        "external_removed",
        "residuals",
        "evidence",
        "provenance",
        "stop_states",
    },
    "J": {"evidence", "provenance"},
}
REFERENCE_FIELDS = {
    "O": {"sort", "context", "owner", "basis"},
    "E": {"kind", "source", "target", "context", "owner", "basis"},
    "C": {
        "kind",
        "applies_to",
        "context",
        "owner",
        "basis",
        "judgment_kind",
        "latitude_ref",
    },
    "L": {"applies_to", "context", "owner", "basis"},
    "X": {"kind", "subject", "context", "owner", "basis"},
    "V": {
        "domain",
        "codomain",
        "context",
        "owner",
        "basis",
        "authority",
        "evidence",
        "provenance",
        "stop_states",
    },
    "T": {
        "traversal",
        "domain_model",
        "codomain_model",
        "context",
        "owner",
        "basis",
        "operation_authority",
        "preservation_relation",
        "preserved",
        "introduced",
        "removed",
        "external_preserved",
        "external_introduced",
        "external_removed",
        "residuals",
        "evidence",
        "provenance",
        "stop_states",
    },
    "J": {
        "kind",
        "subject",
        "context",
        "owner",
        "basis",
        "evaluator",
        "authority",
        "evidence",
        "provenance",
    },
}
RESOLUTION_FIELDS = {
    "external_identity",
    "reference_domain",
    "external_target_kind",
    "resolved_target_identity",
    "basis_relation",
    "resolution_basis",
    "evidence_identity",
}
WITNESS_FIELDS = {
    "external_resolution",
    "domain_model",
    "codomain_model",
    "domain_resolution",
    "codomain_resolution",
    "decision",
    "evidence",
}
EXPECTED_RECORD_VALUE_DOMAINS = {
    ("O", "scope"),
    ("E", "qualifiers"),
    ("E", "scope"),
    ("C", "predicate"),
    ("C", "refusal"),
    ("C", "scope"),
    ("L", "allowed_variation"),
    ("L", "forbidden_variation"),
    ("L", "invalidation"),
    ("L", "scope"),
    ("X", "uncertainty"),
    ("X", "consequence"),
    ("X", "re_entry"),
    ("X", "invalidation"),
    ("X", "scope"),
    ("V", "preconditions"),
    ("V", "postconditions"),
    ("V", "scope"),
    ("T", "preconditions"),
    ("T", "scope"),
    ("T", "invalidation"),
    ("T", "re_entry"),
    ("J", "subject_digest"),
    ("J", "scope"),
    ("J", "decision"),
    ("J", "decided_at"),
}
IDENTITY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:.+$")
GENERATED_SOURCE_KEY_PREFIX = "urn:stdo-representation:source-key:sha256:"
GENERATED_SOURCE_KEY_RE = re.compile(
    rf"^{re.escape(GENERATED_SOURCE_KEY_PREFIX)}[0-9a-f]{{64}}$"
)
SIGNATURE_FIELDS = {
    "kind",
    "schema_version",
    "identity",
    "calculus_concept",
    "record_kinds",
    "external_target_kinds",
    "sorts",
    "value_domains",
    "sort_value_domains",
    "relation_kinds",
    "constraint_kinds",
    "residual_kinds",
    "functor_kinds",
    "judgment_kinds",
    "stop_kinds",
    "record_value_domains",
    "residual_contracts",
    "judgment_contracts",
    "traversal_permissions",
    "reference_domains",
}


def sha256(value: bytes) -> str:
    return digest_bytes(value)


def digest_component(value: str) -> str:
    if (
        not isinstance(value, str)
        or re.fullmatch(r"sha256:[0-9a-f]{64}", value) is None
    ):
        raise ValueError("invalid sha256 coordinate")
    return value.removeprefix("sha256:")


def publish_immutable(path: Path, value: bytes) -> Path:
    """Atomically publish bytes once; an existing coordinate must be byte-identical."""

    path.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, staged_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".staged", dir=path.parent
    )
    staged = Path(staged_name)
    try:
        with os.fdopen(file_descriptor, "wb") as stream:
            stream.write(value)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(staged, path)
        except FileExistsError:
            if path.read_bytes() != value:
                raise ValueError(f"immutable publication conflict: {path}")
        return path
    finally:
        staged.unlink(missing_ok=True)


def raw_output_identity(raw_sha256: str) -> str:
    return (
        "urn:stdo-representation:semantic-compilation-raw-output:sha256:"
        + digest_component(raw_sha256)
    )


def raw_output_artifact_path(run: Path, raw_sha256: str) -> Path:
    run = run.resolve()
    return (
        run
        / "artifacts"
        / "raw-output"
        / digest_component(raw_sha256)
        / "raw-output.json"
    )


def proposal_artifact_path(run: Path, proposal_sha256: str) -> Path:
    run = run.resolve()
    return (
        run
        / "artifacts"
        / "proposal"
        / digest_component(proposal_sha256)
        / "semantic-compilation-proposal.json"
    )


def candidate_artifact_path(
    run: Path, what_member_set_identity: str, candidate_sha256: str
) -> Path:
    run = run.resolve()
    return (
        run
        / "candidates"
        / digest_component(what_member_set_identity)
        / digest_component(candidate_sha256)
        / "candidate.json"
    )


def evaluation_artifact_root(
    run: Path, candidate_sha256: str, result_sha256: str
) -> Path:
    run = run.resolve()
    return (
        run
        / "evaluations"
        / digest_component(candidate_sha256)
        / digest_component(result_sha256)
    )


def publish_raw_output(run: Path, source: Path) -> tuple[Path, str, str]:
    run = run.resolve()
    raw_bytes = source.read_bytes()
    raw_sha = sha256(raw_bytes)
    identity = raw_output_identity(raw_sha)
    binding_path = run / "raw-output-binding.json"
    if binding_path.exists():
        artifact, bound_identity, bound_sha = resolve_raw_output(run)
        if raw_sha != bound_sha or identity != bound_identity:
            raise ValueError(f"immutable publication conflict: {binding_path}")
        return artifact, bound_identity, bound_sha
    artifact = raw_output_artifact_path(run, raw_sha)
    publish_immutable(artifact, raw_bytes)
    binding = {
        "kind": "stdo-representation.semantic-compilation-raw-output-binding",
        "schema_version": 1,
        "raw_output_identity": identity,
        "raw_output_sha256": raw_sha,
        "artifact_path": artifact.relative_to(run).as_posix(),
    }
    publish_immutable(binding_path, canonical_bytes(binding))
    return artifact, identity, raw_sha


def resolve_raw_output(run: Path) -> tuple[Path, str, str]:
    run = run.resolve()
    binding_path = run / "raw-output-binding.json"
    binding_bytes = binding_path.read_bytes()
    binding = load_json(binding_path)
    fields = {
        "kind",
        "schema_version",
        "raw_output_identity",
        "raw_output_sha256",
        "artifact_path",
    }
    if (
        not isinstance(binding, dict)
        or set(binding) != fields
        or binding_bytes != canonical_bytes(binding)
        or binding["kind"]
        != "stdo-representation.semantic-compilation-raw-output-binding"
        or binding["schema_version"] != 1
    ):
        raise ValueError("invalid raw-output binding")
    raw_sha = binding["raw_output_sha256"]
    identity = binding["raw_output_identity"]
    if identity != raw_output_identity(raw_sha):
        raise ValueError("raw-output identity mismatch")
    relative = binding["artifact_path"]
    if not isinstance(relative, str):
        raise ValueError("invalid raw-output artifact path")
    artifact = (run / relative).resolve()
    expected = raw_output_artifact_path(run, raw_sha).resolve()
    if artifact != expected or run not in artifact.parents:
        raise ValueError("raw-output artifact path mismatch")
    if digest_file(artifact) != raw_sha:
        raise ValueError("raw-output artifact digest mismatch")
    return artifact, identity, raw_sha


def generated_source_key(
    primary_source_locator: dict[str, Any], local_declaration_key: str
) -> str:
    preimage = {
        "primary_source_locator": primary_source_locator,
        "local_declaration_key": local_declaration_key,
    }
    digest = sha256(canonical_bytes(preimage)).removeprefix("sha256:")
    return GENERATED_SOURCE_KEY_PREFIX + digest


def issue(issues: list[dict[str, str]], path: str, code: str) -> None:
    issues.append({"path": path, "code": code})


def exact_keys(
    issues: list[dict[str, str]], value: Any, expected: set[str], path: str
) -> bool:
    if not isinstance(value, dict):
        issue(issues, path, "expected_object")
        return False
    actual = set(value)
    for key in sorted(expected - actual):
        issue(issues, f"{path}.{key}", "missing_field")
    for key in sorted(actual - expected):
        issue(issues, f"{path}.{key}", "unexpected_field")
    return actual == expected


def string_set(
    issues: list[dict[str, str]], value: Any, path: str, *, allow_empty: bool = True
) -> list[str]:
    if not isinstance(value, list) or any(
        not isinstance(row, str) or not row for row in value
    ):
        issue(issues, path, "expected_nonempty_string_array")
        return []
    if not allow_empty and not value:
        issue(issues, path, "empty_array")
    if len(value) != len(set(value)):
        issue(issues, path, "duplicate_array_value")
    if value != sorted(set(value), key=utf16_key):
        issue(issues, path, "not_sorted_unique")
    return value


def decode_result_envelope(
    value: Any,
) -> tuple[dict[str, Any] | None, list[dict[str, str]]]:
    issues: list[dict[str, str]] = []
    fields = {"kind", "schema_version", "payload"}
    if not exact_keys(issues, value, fields, "$"):
        return None, issues
    if value["schema_version"] != PROPOSAL_SCHEMA_VERSION:
        issue(issues, "$.schema_version", "wrong_transport_schema_version")
    payload = value["payload"]
    if value["kind"] == "stdo-representation.semantic-compilation-proposal":
        if not exact_keys(issues, payload, CANDIDATE_PAYLOAD_FIELDS, "$.payload"):
            return None, issues
        if payload["stop_state"] != STOP_KINDS["candidate"]:
            issue(issues, "$.payload.stop_state", "proposal_not_candidate")
        if issues:
            return None, issues
        return value, []
    if value["kind"] == "stdo-representation.semantic-compilation-stop":
        stop_fields = {"stop_state", "reason_code", "re_entry_refs"}
        if not exact_keys(issues, payload, stop_fields, "$.payload"):
            return None, issues
        if not isinstance(payload["reason_code"], str):
            issue(issues, "$.payload.reason_code", "stop_missing_reason")
        if not isinstance(payload["re_entry_refs"], list):
            issue(issues, "$.payload.re_entry_refs", "stop_missing_re_entry")
        if issues:
            return None, issues
        return value, []
    issue(issues, "$.kind", "wrong_kind")
    return None, issues


def invocation_timestamp(run_id: str) -> str:
    parsed = dt.datetime.strptime(run_id, "%Y%m%dT%H%M%SZ").replace(
        tzinfo=dt.timezone.utc
    )
    return parsed.isoformat().replace("+00:00", "Z")


def candidate_structure_result_identity(result: dict[str, Any]) -> tuple[str, str]:
    result_sha = sha256(canonical_bytes(result))
    return (
        "urn:stdo-representation:candidate-structure-result:sha256:"
        + result_sha.removeprefix("sha256:"),
        result_sha,
    )


def semantic_compilation_candidate_identity(
    candidate: dict[str, Any],
) -> tuple[str, str]:
    candidate_sha = sha256(canonical_bytes(candidate))
    return (
        "urn:stdo-representation:semantic-compilation-candidate:sha256:"
        + candidate_sha.removeprefix("sha256:"),
        candidate_sha,
    )


def candidate_structure_grant_identity(grant: dict[str, Any]) -> str:
    grant_sha = sha256(canonical_bytes(grant))
    return (
        "urn:stdo-representation:candidate-structure-grant:sha256:"
        + grant_sha.removeprefix("sha256:")
    )


def validate_candidate_structure_grant(
    grant: Any,
    grant_bytes: bytes,
    candidate: dict[str, Any],
    expected_basis: dict[str, Any],
) -> str:
    fields = {
        "kind",
        "schema_version",
        "parent_grant_identity",
        "issuer_actor_identity",
        "authority_identity",
        "grantee_identity",
        "grant_scope",
        "traversal_ref",
        "functor_ref",
        "subject_identity",
        "subject_sha256",
        "calculus_basis_identity",
        "signature_identity",
        "signature_sha256",
        "interpretation_contract_identity",
        "interpretation_contract_sha256",
        "what_member_set_identity",
        "frame_basis_identity",
        "frame_basis_sha256",
        "evidence_refs",
        "issued_at",
        "source_ref",
        "source_sha256",
    }
    if not isinstance(grant, dict) or set(grant) != fields:
        raise ValueError("invalid candidate-structure evaluation grant")
    if grant_bytes != canonical_bytes(grant):
        raise ValueError("candidate-structure grant is not exact unframed JCS")
    product_text = PRODUCT_PATH.read_text(encoding="utf-8")
    if not all(
        value in product_text
        for value in (
            PRODUCT_OWNER_ACTOR,
            PRODUCT_OWNER_AUTHORITY,
            PRODUCT_OWNER_GRANT,
            PRODUCT_OWNER_GRANT_SCOPE,
        )
    ):
        raise ValueError("candidate-structure parent authority is unresolved")
    candidate_identity, candidate_sha = semantic_compilation_candidate_identity(
        candidate
    )
    expected = {
        "kind": "stdo-representation.candidate-structure-evaluation-grant",
        "schema_version": 1,
        "parent_grant_identity": PRODUCT_OWNER_GRANT,
        "issuer_actor_identity": PRODUCT_OWNER_ACTOR,
        "authority_identity": PRODUCT_OWNER_AUTHORITY,
        "grantee_identity": EVALUATOR_IDENTITY,
        "grant_scope": CANDIDATE_STRUCTURE_GRANT_SCOPE,
        "traversal_ref": STRUCTURE_TRAVERSAL,
        "functor_ref": F_D,
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
        "source_ref": CANDIDATE_STRUCTURE_GRANT_SOURCE_REF,
        "source_sha256": digest_file(PRODUCT_PATH),
    }
    mismatches = sorted(
        field
        for field, expected_value in expected.items()
        if grant[field] != expected_value
    )
    if mismatches:
        raise ValueError(
            "candidate-structure grant coordinate mismatch: " + ", ".join(mismatches)
        )
    evidence_refs = grant["evidence_refs"]
    if (
        not isinstance(evidence_refs, list)
        or not evidence_refs
        or any(not isinstance(ref, str) or not ref for ref in evidence_refs)
        or evidence_refs != sorted(set(evidence_refs), key=utf16_key)
    ):
        raise ValueError("invalid candidate-structure grant evidence")
    if (
        not isinstance(grant["issued_at"], str)
        or TIMESTAMP_RE.fullmatch(grant["issued_at"]) is None
    ):
        raise ValueError("invalid candidate-structure grant issue time")
    return candidate_structure_grant_identity(grant)


def expected_invocation(
    run: Path,
    acquisition: dict[str, Any],
    raw_output_path: Path,
    raw_output_ref: str,
) -> dict[str, Any]:
    return {
        "topology": "single_invocation",
        "traversal_ref": COMPILE_TRAVERSAL,
        "functor_ref": F_P,
        "host_identity": "urn:openai:codex-cli",
        "model_identity": "gpt-5.6-sol",
        "model_configuration_sha256": sha256(
            canonical_bytes(
                {
                    "model": "gpt-5.6-sol",
                    "reasoning_effort": "xhigh",
                    "sandbox": "read-only",
                    "ephemeral": True,
                }
            )
        ),
        "instruction_sha256": acquisition["sealed_invocation_sha256"],
        "capability_envelope_ref": (
            "urn:axiom-indexer:capability:semantic-compilation-prototype:1"
        ),
        "context_budget_tokens": 1_000_000,
        "invoked_at": invocation_timestamp(run.name),
        "raw_output_ref": raw_output_ref,
        "raw_output_sha256": digest_file(raw_output_path),
        "provenance_ref": (compiler_provenance_bundle_ref(run.name)),
        "provenance_sha256": digest_file(run / "compiler-provenance-bundle.json"),
    }


def construct_candidate(
    proposal: dict[str, Any],
    raw_proposal_bytes: bytes,
    expected_basis: dict[str, Any],
    source_manifest: dict[str, Any],
    compiler_invocation: dict[str, Any],
    provenance_bundle: dict[str, Any],
    provenance_bytes: bytes,
    provenance_member_bytes: dict[str, bytes],
) -> dict[str, Any]:
    if (
        set(proposal) != {"kind", "schema_version", "payload"}
        or proposal.get("kind") != "stdo-representation.semantic-compilation-proposal"
        or proposal.get("schema_version") != PROPOSAL_SCHEMA_VERSION
        or not isinstance(proposal.get("payload"), dict)
        or set(proposal["payload"]) != CANDIDATE_PAYLOAD_FIELDS
    ):
        raise ValueError("invalid semantic compilation proposal")
    if compiler_invocation.get("raw_output_sha256") != sha256(raw_proposal_bytes):
        raise ValueError("raw proposal digest differs from compiler invocation")
    if (
        not isinstance(compiler_invocation.get("provenance_ref"), str)
        or not compiler_invocation["provenance_ref"]
        or compiler_invocation.get("provenance_sha256") != sha256(provenance_bytes)
    ):
        raise ValueError("provenance bytes differ from compiler invocation")
    verify_compiler_provenance_bundle(
        provenance_bundle,
        provenance_bytes,
        provenance_member_bytes,
    )
    payload = proposal["payload"]
    model = payload["candidate_model"]
    expected_coordinates = {
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
        "candidate_model_content_identity": sha256(canonical_bytes(model)),
        "stop_state": STOP_KINDS["candidate"],
    }
    mismatches = sorted(
        field
        for field, expected in expected_coordinates.items()
        if payload.get(field) != expected
    )
    if mismatches:
        raise ValueError("candidate payload mismatch: " + ", ".join(mismatches))
    return {
        "kind": "stdo-representation.semantic-compilation-candidate",
        "schema_version": CANDIDATE_SCHEMA_VERSION,
        "proposal_content_sha256": sha256(canonical_bytes(proposal)),
        "compiler_invocation": compiler_invocation,
        **copy.deepcopy(payload),
    }


def verify_run_acquisition(
    run: Path,
    basis_path: Path,
    source_manifest_path: Path,
    acquisition: dict[str, Any],
    expected_basis: dict[str, Any],
    source_manifest: dict[str, Any],
) -> str:
    derived_model_basis = model_basis_identity(expected_basis)
    basis = load_json(basis_path)
    preflight = basis.get("preflight")
    expected_receipt = {
        "kind": "stdo-index.prototype-acquisition",
        "schema_version": 3,
        "run_id": run.name,
        "basis_sha256": digest_file(basis_path),
        "source_manifest_sha256": digest_file(source_manifest_path),
        "invocation_sha256": digest_file(run / "invocation.txt"),
        "sealed_invocation_sha256": digest_file(run / "sealed-invocation.txt"),
        "calculus_basis_sha256": expected_basis["calculus"]["record_sha256"],
        "calculus_basis_identity": expected_basis["calculus"]["identity"],
        "preflight": preflight,
        "model_basis": derived_model_basis,
        "status": "inputs_acquired",
    }
    mismatches = [
        field
        for field, expected in expected_receipt.items()
        if acquisition.get(field) != expected
    ]
    if set(acquisition) != set(expected_receipt):
        mismatches.append("receipt_shape")
    expected_basis_fields = {
        "kind",
        "schema_version",
        "calculus",
        "subject",
        "signature",
        "interpretation_contract",
        "frame",
        "source_packet",
        "subject_basis_identity",
        "what_member_set_identity",
        "compiler_prompt_sha256",
        "transport_schema_sha256",
        "preflight",
    }
    if (
        not isinstance(basis, dict)
        or set(basis) != expected_basis_fields
        or basis.get("kind") != "stdo-index.prototype-basis"
        or basis.get("schema_version") != 3
    ):
        mismatches.append("basis_shape")
    if not isinstance(preflight, dict) or set(preflight) != {
        "frame_acceptance",
        "compile_grant",
        "compile_activation",
        "capability_envelope",
    }:
        mismatches.append("preflight_shape")
    else:
        for name, binding in preflight.items():
            record_path = run / "preflight" / f"{name}.json"
            if (
                not isinstance(binding, dict)
                or set(binding) != {"identity", "sha256"}
                or not record_path.is_file()
                or digest_file(record_path) != binding.get("sha256")
            ):
                mismatches.append(f"preflight.{name}")
    subject = expected_basis["subject"]
    for field in (
        "release_uri",
        "installed_manifest_sha256",
        "standards_member_set_sha256",
    ):
        if source_manifest.get(field) != subject[field]:
            mismatches.append(f"source_manifest.{field}")
    members = source_manifest.get("members")
    if not isinstance(members, list) or len(members) != subject["member_count"]:
        mismatches.append("source_manifest.members")
    packet_preimage = {
        "release_uri": source_manifest.get("release_uri"),
        "members": source_manifest.get("supplied_members"),
    }
    packet_sha = sha256(canonical_bytes(packet_preimage))
    packet_ref = {
        "identity": (
            "urn:stdo-index:source-packet:sha256:" + packet_sha.removeprefix("sha256:")
        ),
        "sha256": packet_sha,
    }
    if expected_basis["source_packet"] != packet_ref:
        mismatches.append("source_packet")
    calculus = expected_basis.get("calculus")
    if not isinstance(calculus, dict) or set(calculus) != {
        "identity",
        "record",
        "record_sha256",
        "status",
    }:
        mismatches.append("calculus_shape")
    else:
        record_sha = sha256(canonical_bytes(calculus["record"]))
        expected_identity = (
            "urn:stdo:axiomatic-calculus-basis:sha256:"
            + record_sha.removeprefix("sha256:")
        )
        if calculus["record_sha256"] != record_sha:
            mismatches.append("calculus_record_sha256")
        if calculus["identity"] != expected_identity:
            mismatches.append("calculus_identity")
        if calculus["status"] != "product_selected":
            mismatches.append("calculus_status")
    if mismatches:
        raise ValueError("acquisition mismatch: " + ", ".join(sorted(set(mismatches))))
    return derived_model_basis


def validate_signature(signature: Any) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    if not isinstance(signature, dict):
        return [{"path": "$.basis.signature", "code": "expected_object"}]
    exact_keys(issues, signature, SIGNATURE_FIELDS, "$.basis.signature")
    if (
        signature.get("kind") != "stdo-index.target-signature"
        or signature.get("schema_version") != SIGNATURE_SCHEMA_VERSION
        or signature.get("identity") != SIGNATURE_IDENTITY
        or signature.get("calculus_concept")
        != "urn:stdo:concept:axiomatic-calculus:a-c"
    ):
        issue(issues, "$.basis.signature", "signature_coordinate_mismatch")
    record_rows = signature.get("record_kinds")
    record_map: dict[str, str] = {}
    if not isinstance(record_rows, list):
        issue(issues, "$.basis.signature.record_kinds", "expected_array")
    else:
        for index, row in enumerate(record_rows):
            path = f"$.basis.signature.record_kinds[{index}]"
            if not exact_keys(
                issues,
                row,
                {
                    "population",
                    "identity",
                    "name",
                    "required_nonempty",
                    "maximum_records",
                },
                path,
            ):
                continue
            if row["population"] in record_map:
                issue(issues, f"{path}.population", "duplicate_record_population")
            record_map[row["population"]] = row["identity"]
            if not isinstance(row["required_nonempty"], bool):
                issue(issues, f"{path}.required_nonempty", "expected_boolean")
            if row["maximum_records"] is not None and (
                not isinstance(row["maximum_records"], int)
                or isinstance(row["maximum_records"], bool)
                or row["maximum_records"] < 0
            ):
                issue(issues, f"{path}.maximum_records", "invalid_maximum_records")
    if record_map != RECORD_KIND_BY_POPULATION:
        issue(issues, "$.basis.signature.record_kinds", "record_kind_set_mismatch")

    external_rows = signature.get("external_target_kinds")
    external_kinds: dict[str, str] = {}
    if not isinstance(external_rows, list):
        issue(issues, "$.basis.signature.external_target_kinds", "expected_array")
    else:
        for index, row in enumerate(external_rows):
            path = f"$.basis.signature.external_target_kinds[{index}]"
            if exact_keys(issues, row, {"identity", "required_basis_relation"}, path):
                if row["identity"] in external_kinds:
                    issue(issues, f"{path}.identity", "duplicate_external_target_kind")
                external_kinds[row["identity"]] = row["required_basis_relation"]
    if external_kinds != {
        "urn:stdo-index:external-target-kind:model-basis:1": (
            "urn:stdo-index:basis-relation:exact-model-basis:1"
        ),
        "urn:stdo-index:external-target-kind:target-signature-member:1": (
            "urn:stdo-index:basis-relation:exact-target-signature:1"
        ),
        "urn:stdo-index:external-target-kind:complete-model:1": (
            "urn:stdo-index:basis-relation:exact-complete-model:1"
        ),
    }:
        issue(
            issues,
            "$.basis.signature.external_target_kinds",
            "external_target_kind_set_mismatch",
        )

    expected_ref_fields = {
        (population, field)
        for population, fields in REFERENCE_FIELDS.items()
        for field in fields
    }
    seen_ref_fields: set[tuple[str, str]] = set()
    for index, row in enumerate(signature.get("reference_domains", [])):
        path = f"$.basis.signature.reference_domains[{index}]"
        expected = {
            "identity",
            "population",
            "field",
            "cardinality",
            "allowed_local_record_kinds",
            "allowed_semantic_object_sorts",
            "allowed_external_target_kinds",
            "required_basis_relation",
        }
        if not exact_keys(issues, row, expected, path):
            continue
        coordinate = (row["population"], row["field"])
        if coordinate in seen_ref_fields:
            issue(issues, path, "duplicate_reference_domain")
        seen_ref_fields.add(coordinate)
        if (
            not isinstance(row["identity"], str)
            or IDENTITY_RE.fullmatch(row["identity"]) is None
        ):
            issue(issues, f"{path}.identity", "invalid_reference_domain_identity")
        if row["cardinality"] not in {
            "exactly_one",
            "zero_or_one",
            "zero_or_more",
            "one_or_more",
        }:
            issue(issues, f"{path}.cardinality", "unknown_cardinality")
        for field in (
            "allowed_local_record_kinds",
            "allowed_semantic_object_sorts",
            "allowed_external_target_kinds",
        ):
            values = row[field]
            if not isinstance(values, list) or len(values) != len(set(values)):
                issue(issues, f"{path}.{field}", "expected_unique_array")
        if not set(row["allowed_local_record_kinds"]) <= set(POPULATION_BY_RECORD_KIND):
            issue(issues, f"{path}.allowed_local_record_kinds", "unknown_record_kind")
        if not set(row["allowed_external_target_kinds"]) <= set(external_kinds):
            issue(
                issues,
                f"{path}.allowed_external_target_kinds",
                "unknown_external_target_kind",
            )
        if row["allowed_external_target_kinds"]:
            relations = {
                external_kinds[kind] for kind in row["allowed_external_target_kinds"]
            }
            if relations != {row["required_basis_relation"]}:
                issue(
                    issues, f"{path}.required_basis_relation", "basis_relation_mismatch"
                )
        elif row["required_basis_relation"] is not None:
            issue(
                issues, f"{path}.required_basis_relation", "unexpected_basis_relation"
            )
    if seen_ref_fields != expected_ref_fields:
        issue(
            issues,
            "$.basis.signature.reference_domains",
            "reference_domain_set_mismatch",
        )

    record_domains = {
        (row.get("population"), row.get("field"))
        for row in signature.get("record_value_domains", [])
        if isinstance(row, dict)
    }
    if record_domains != EXPECTED_RECORD_VALUE_DOMAINS:
        issue(
            issues,
            "$.basis.signature.record_value_domains",
            "record_value_domain_set_mismatch",
        )
    if set(signature.get("functor_kinds", [])) != {F_D, F_P, F_H}:
        issue(issues, "$.basis.signature.functor_kinds", "functor_kind_set_mismatch")

    exact_signature_sets = {
        "sorts": set(SORTS.values()),
        "relation_kinds": set(RELATION_KINDS.values()),
        "constraint_kinds": set(CONSTRAINT_KINDS.values()),
        "residual_kinds": set(RESIDUAL_KINDS.values()),
        "judgment_kinds": set(JUDGMENT_KINDS.values()),
        "stop_kinds": set(STOP_KINDS.values()),
    }
    actual_signature_sets = {
        "sorts": set(signature.get("sorts", [])),
        "relation_kinds": {
            row.get("id")
            for row in signature.get("relation_kinds", [])
            if isinstance(row, dict)
        },
        "constraint_kinds": {
            row.get("id")
            for row in signature.get("constraint_kinds", [])
            if isinstance(row, dict)
        },
        "residual_kinds": set(signature.get("residual_kinds", [])),
        "judgment_kinds": set(signature.get("judgment_kinds", [])),
        "stop_kinds": set(signature.get("stop_kinds", [])),
    }
    for family, expected_members in exact_signature_sets.items():
        if actual_signature_sets[family] != expected_members:
            issue(
                issues, f"$.basis.signature.{family}", "signature_member_set_mismatch"
            )
        if any(
            not isinstance(member, str) or IDENTITY_RE.fullmatch(member) is None
            for member in actual_signature_sets[family]
        ):
            issue(
                issues, f"$.basis.signature.{family}", "non_absolute_signature_member"
            )

    permissions = {
        row.get("traversal"): row
        for row in signature.get("traversal_permissions", [])
        if isinstance(row, dict)
    }
    compile_permission = permissions.get(COMPILE_TRAVERSAL)
    if (
        compile_permission is None
        or compile_permission.get("functor") != F_P
        or compile_permission.get("codomain") != ["semantic_compilation_proposal"]
    ):
        issue(issues, "$.basis.signature", "invalid_compile_traversal_permission")
    structure_permission = permissions.get(STRUCTURE_TRAVERSAL)
    if (
        structure_permission is None
        or structure_permission.get("functor") != F_D
        or structure_permission.get("domain")
        != [
            "semantic_compilation_candidate",
            "candidate_structure_evaluation_grant",
            "target_signature",
            "exact_basis",
        ]
        or structure_permission.get("codomain") != ["candidate_structure_result"]
    ):
        issue(issues, "$.basis.signature", "invalid_structure_traversal_permission")
    selection_permission = permissions.get(SELECTION_TRAVERSAL)
    if (
        selection_permission is None
        or selection_permission.get("functor") != F_H
        or selection_permission.get("codomain") != ["semantic_selection_result"]
    ):
        issue(issues, "$.basis.signature", "invalid_selection_traversal_permission")
    selection_contract = next(
        (
            row
            for row in signature.get("judgment_contracts", [])
            if row.get("kind") == JUDGMENT_KINDS["semantic_selection"]
        ),
        None,
    )
    if selection_contract is None or selection_contract.get("outputs") != [
        STOP_KINDS["accepted"],
        STOP_KINDS["rework"],
        STOP_KINDS["rejected"],
    ]:
        issue(issues, "$.basis.signature", "inconsistent_selection_contract")
    structure_contract = next(
        (
            row
            for row in signature.get("judgment_contracts", [])
            if row.get("kind") == JUDGMENT_KINDS["candidate_structure"]
        ),
        None,
    )
    if (
        structure_contract is None
        or structure_contract.get("inputs")
        != [
            "semantic_compilation_candidate",
            "candidate_structure_evaluation_grant",
            "target_signature",
            "exact_basis",
        ]
        or structure_contract.get("evidence")
        != [
            "exact_subject_bytes",
            "exact_basis",
            "candidate_structure_evaluation_grant",
        ]
    ):
        issue(issues, "$.basis.signature", "inconsistent_structure_contract")
    return issues


def validate_candidate(
    candidate: Any,
    expected_basis: dict[str, Any],
    source_manifest: dict[str, Any],
    signature: dict[str, Any],
    model_basis: str,
    expected_compiler_invocation: dict[str, Any],
) -> list[dict[str, str]]:
    issues = validate_signature(signature)
    derived_model_basis = model_basis_identity(expected_basis)
    if model_basis != derived_model_basis:
        issue(
            issues,
            "$.candidate_model.model_basis_identity",
            "unverified_model_basis_argument",
        )
    model_basis = derived_model_basis
    top = {
        "kind",
        "schema_version",
        "proposal_content_sha256",
        "calculus_basis_identity",
        "source_stdo_uri",
        "source_stdo_manifest_sha256",
        "source_member_set_sha256",
        "source_members",
        "subject_basis_identity",
        "what_member_set_identity",
        "signature_identity",
        "signature_sha256",
        "interpretation_contract_identity",
        "interpretation_contract_sha256",
        "frame_basis_identity",
        "frame_basis_sha256",
        "selected_frame_refs",
        "compiler_invocation",
        "candidate_model",
        "candidate_model_content_identity",
        "proposed_record_provenance",
        "proposed_evaluated_members",
        "proposed_selections",
        "proposed_generated_source_keys",
        "compilation_residuals",
        "stop_state",
    }
    if not exact_keys(issues, candidate, top, "$"):
        return sorted(issues, key=lambda row: (row["path"], row["code"]))
    if candidate["kind"] != "stdo-representation.semantic-compilation-candidate":
        issue(issues, "$.kind", "wrong_kind")
    if candidate["schema_version"] != CANDIDATE_SCHEMA_VERSION:
        issue(issues, "$.schema_version", "wrong_schema_version")
    reconstructed_proposal = {
        "kind": "stdo-representation.semantic-compilation-proposal",
        "schema_version": PROPOSAL_SCHEMA_VERSION,
        "payload": {field: candidate[field] for field in CANDIDATE_PAYLOAD_FIELDS},
    }
    if candidate["proposal_content_sha256"] != sha256(
        canonical_bytes(reconstructed_proposal)
    ):
        issue(issues, "$.proposal_content_sha256", "proposal_content_mismatch")
    coordinates = {
        "calculus_basis_identity": expected_basis["calculus"]["identity"],
        "source_stdo_uri": expected_basis["subject"]["release_uri"],
        "source_stdo_manifest_sha256": expected_basis["subject"][
            "installed_manifest_sha256"
        ],
        "source_member_set_sha256": expected_basis["subject"][
            "standards_member_set_sha256"
        ],
        "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
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
    }
    for field, expected in coordinates.items():
        if candidate[field] != expected:
            issue(issues, f"$.{field}", "basis_mismatch")
    expected_members = [
        {"member_path": row["path"], "member_sha256": row["sha256"]}
        for row in source_manifest["members"]
    ]
    if candidate["source_members"] != expected_members:
        issue(issues, "$.source_members", "source_inventory_mismatch")
    if (
        candidate["selected_frame_refs"]
        != expected_basis["frame"]["selected_frame_refs"]
    ):
        issue(issues, "$.selected_frame_refs", "selected_frame_mismatch")
    if candidate["compiler_invocation"] != expected_compiler_invocation:
        issue(issues, "$.compiler_invocation", "provenance_binding_mismatch")

    model_fields = {
        "model_basis_identity",
        "identities",
        "semantic_objects",
        "typed_relations",
        "constraints",
        "latitudes",
        "residuals",
        "traversals",
        "transformations",
        "judgments",
        "external_resolutions",
    }
    raw_model = candidate["candidate_model"]
    if not exact_keys(issues, raw_model, model_fields, "$.candidate_model"):
        return sorted(issues, key=lambda row: (row["path"], row["code"]))
    model = {
        "b": raw_model["model_basis_identity"],
        "I": raw_model["identities"],
        "O": raw_model["semantic_objects"],
        "E": raw_model["typed_relations"],
        "C": raw_model["constraints"],
        "L": raw_model["latitudes"],
        "X": raw_model["residuals"],
        "V": raw_model["traversals"],
        "T": raw_model["transformations"],
        "J": raw_model["judgments"],
        "ResolutionSet_M": raw_model["external_resolutions"],
    }
    if candidate["candidate_model_content_identity"] != sha256(
        canonical_bytes(raw_model)
    ):
        issue(
            issues,
            "$.candidate_model_content_identity",
            "model_content_identity_mismatch",
        )
    if model["b"] != model_basis:
        issue(issues, "$.candidate_model.model_basis_identity", "model_basis_mismatch")
    identities = string_set(issues, model["I"], "$.candidate_model.identities")
    identity_set = set(identities)

    record_by_id: dict[str, tuple[str, dict[str, Any]]] = {}
    record_kind_rows = {
        row["population"]: row
        for row in signature.get("record_kinds", [])
        if isinstance(row, dict) and "population" in row
    }
    for population in POPULATIONS:
        rows = model[population]
        path = f"$.candidate_model.{MODEL_FIELD_BY_POPULATION[population]}"
        if not isinstance(rows, list):
            issue(issues, path, "expected_array")
            continue
        if record_kind_rows.get(population, {}).get("required_nonempty") and not rows:
            issue(issues, path, "required_nonempty_population")
        maximum_records = record_kind_rows.get(population, {}).get("maximum_records")
        if isinstance(maximum_records, int) and len(rows) > maximum_records:
            issue(issues, path, "population_exceeds_declared_maximum")
        row_ids: list[str] = []
        for index, row in enumerate(rows):
            row_path = f"{path}[{index}]"
            if not exact_keys(issues, row, RECORD_FIELDS[population], row_path):
                continue
            row_id = row.get("id")
            if not isinstance(row_id, str) or IDENTITY_RE.fullmatch(row_id) is None:
                issue(issues, f"{row_path}.id", "invalid_record_identity")
                continue
            row_ids.append(row_id)
            safe = True
            for field in RECORD_FIELDS[population] - ARRAY_FIELDS.get(
                population, set()
            ):
                value = row[field]
                if population == "C" and field == "latitude_ref":
                    if value is not None and (not isinstance(value, str) or not value):
                        issue(issues, f"{row_path}.{field}", "expected_string_or_null")
                        safe = False
                elif field == "external_resolution_witnesses":
                    if not isinstance(value, list):
                        issue(issues, f"{row_path}.{field}", "expected_array")
                        safe = False
                    continue
                elif not isinstance(value, str) or not value:
                    issue(issues, f"{row_path}.{field}", "expected_nonempty_string")
                    safe = False
            for field in ARRAY_FIELDS.get(population, set()):
                if not isinstance(row[field], list) or any(
                    not isinstance(value, str) or not value for value in row[field]
                ):
                    safe = False
                string_set(issues, row[field], f"{row_path}.{field}")
            if not safe:
                continue
            if row_id in record_by_id:
                issue(issues, f"{row_path}.id", "duplicate_record_identity")
            else:
                record_by_id[row_id] = (population, row)
            if row.get("basis") != model_basis:
                issue(issues, f"{row_path}.basis", "mixed_model_basis")
        if row_ids != sorted(row_ids, key=utf16_key):
            issue(issues, path, "records_not_sorted_by_id")

    local_set = set(record_by_id)
    if not local_set <= identity_set:
        for missing in sorted(local_set - identity_set, key=utf16_key):
            issue(
                issues,
                "$.candidate_model.identities",
                f"missing_record_identity:{missing}",
            )
    if model_basis in local_set:
        issue(
            issues,
            "$.candidate_model.model_basis_identity",
            "model_basis_is_local_record",
        )
    external_set = identity_set - local_set
    if local_set & external_set:
        issue(issues, "$.candidate_model.identities", "local_external_identity_overlap")
    if model_basis not in external_set:
        issue(issues, "$.candidate_model.identities", "missing_model_basis_identity")

    resolutions = model["ResolutionSet_M"]
    resolution_by_external: dict[str, dict[str, str]] = {}
    resolution_ids: list[str] = []
    external_kind_rows = {
        row["identity"]: row
        for row in signature.get("external_target_kinds", [])
        if isinstance(row, dict) and "identity" in row
    }
    if not isinstance(resolutions, list):
        issue(issues, "$.candidate_model.external_resolutions", "expected_array")
    else:
        for index, row in enumerate(resolutions):
            path = f"$.candidate_model.external_resolutions[{index}]"
            if not exact_keys(issues, row, RESOLUTION_FIELDS, path):
                continue
            if any(not isinstance(row[field], str) or not row[field] for field in row):
                issue(issues, path, "resolution_field_not_identity")
                continue
            if any(IDENTITY_RE.fullmatch(row[field]) is None for field in row):
                issue(issues, path, "resolution_field_not_identity")
                continue
            external_identity = row["external_identity"]
            resolution_ids.append(external_identity)
            if external_identity in resolution_by_external:
                issue(
                    issues, f"{path}.external_identity", "duplicate_external_resolution"
                )
            resolution_by_external[external_identity] = row
            if external_identity in local_set:
                issue(issues, f"{path}.external_identity", "local_external_ambiguity")
            target_kind = external_kind_rows.get(row["external_target_kind"])
            if target_kind is None:
                issue(
                    issues,
                    f"{path}.external_target_kind",
                    "unknown_external_target_kind",
                )
            elif row["basis_relation"] != target_kind["required_basis_relation"]:
                issue(
                    issues, f"{path}.basis_relation", "external_basis_relation_mismatch"
                )
        if resolution_ids != sorted(resolution_ids, key=utf16_key):
            issue(
                issues,
                "$.candidate_model.external_resolutions",
                "resolutions_not_sorted",
            )
    if set(resolution_by_external) != external_set:
        for missing in sorted(
            external_set - set(resolution_by_external), key=utf16_key
        ):
            issue(
                issues,
                "$.candidate_model.external_resolutions",
                f"missing_external_resolution:{missing}",
            )
        for extra in sorted(set(resolution_by_external) - external_set, key=utf16_key):
            issue(
                issues,
                "$.candidate_model.external_resolutions",
                f"extra_external_resolution:{extra}",
            )
    expected_basis_resolution = model_basis_resolution(model_basis, expected_basis)
    if resolution_by_external.get(model_basis) != expected_basis_resolution:
        issue(
            issues,
            "$.candidate_model.external_resolutions",
            "model_basis_resolution_mismatch",
        )

    signature_members = {
        *signature.get("sorts", []),
        *signature.get("residual_kinds", []),
        *signature.get("functor_kinds", []),
        *signature.get("judgment_kinds", []),
        *signature.get("stop_kinds", []),
        *(
            row.get("id")
            for family in ("relation_kinds", "constraint_kinds")
            for row in signature.get(family, [])
            if isinstance(row, dict)
        ),
    }
    for external_identity, resolution in resolution_by_external.items():
        if resolution.get("external_target_kind") != (
            "urn:stdo-index:external-target-kind:target-signature-member:1"
        ):
            continue
        path = f"$.candidate_model.external_resolutions[external_identity={external_identity}]"
        if external_identity not in signature_members:
            issue(issues, path, "unknown_resolved_signature_member")
            continue
        expected = signature_member_resolution(
            external_identity, resolution["reference_domain"], expected_basis
        )
        if resolution != expected:
            issue(issues, path, "signature_member_resolution_mismatch")

    sorts = set(signature.get("sorts", []))
    value_domains = {
        row["id"]: row
        for row in signature.get("value_domains", [])
        if isinstance(row, dict) and "id" in row
    }
    sort_value_domains = {
        row["sort"]: row["domain"]
        for row in signature.get("sort_value_domains", [])
        if isinstance(row, dict) and {"sort", "domain"} <= set(row)
    }
    record_value_domains = {
        (row["population"], row["field"]): row["domain"]
        for row in signature.get("record_value_domains", [])
        if isinstance(row, dict) and {"population", "field", "domain"} <= set(row)
    }
    relation_kinds = {
        row["id"]: row
        for row in signature.get("relation_kinds", [])
        if isinstance(row, dict) and "id" in row
    }
    constraint_kinds = {
        row["id"]: row
        for row in signature.get("constraint_kinds", [])
        if isinstance(row, dict) and "id" in row
    }
    residual_contracts = {
        row["kind"]: row
        for row in signature.get("residual_contracts", [])
        if isinstance(row, dict) and "kind" in row
    }
    judgment_kinds = set(signature.get("judgment_kinds", []))
    stop_kinds = set(signature.get("stop_kinds", []))
    reference_domains = {
        (row["population"], row["field"]): row
        for row in signature.get("reference_domains", [])
        if isinstance(row, dict) and {"population", "field"} <= set(row)
    }

    def value_in_domain(value: Any, domain_id: str, path: str) -> bool:
        domain = value_domains.get(domain_id)
        if domain is None:
            issue(issues, path, "unknown_value_domain")
            return False
        kind = domain.get("kind")
        if kind == "nonempty_string":
            valid = (
                isinstance(value, str)
                and bool(value)
                and len(value) <= domain.get("max_length", 0)
            )
        elif kind == "pattern_string":
            valid = (
                isinstance(value, str)
                and re.fullmatch(domain.get("pattern", ""), value) is not None
            )
        elif kind == "sorted_unique_array":
            valid = isinstance(value, list)
            if valid:
                members = string_set(issues, value, path)
                valid = all(
                    value_in_domain(
                        member, domain.get("item_domain", ""), f"{path}[{index}]"
                    )
                    for index, member in enumerate(members)
                )
        else:
            issue(issues, path, "unknown_value_domain_kind")
            return False
        if not valid:
            issue(issues, path, "value_outside_domain")
        return valid

    def resolve_field(population: str, field: str, value: Any, path: str) -> None:
        declared = reference_domains.get((population, field))
        if declared is None:
            issue(issues, path, "undeclared_reference_domain")
            return
        cardinality = declared["cardinality"]
        if cardinality in {"zero_or_more", "one_or_more"}:
            refs = string_set(
                issues, value, path, allow_empty=cardinality == "zero_or_more"
            )
        elif cardinality == "zero_or_one":
            refs = [] if value is None else [value]
        else:
            refs = [value]
        for ref in refs:
            if not isinstance(ref, str) or not ref:
                issue(issues, path, "invalid_reference")
                continue
            if IDENTITY_RE.fullmatch(ref) is None:
                issue(issues, path, "invalid_reference_identity")
                continue
            if ref not in identity_set:
                issue(issues, path, "reference_outside_I")
                continue
            local = record_by_id.get(ref)
            external = resolution_by_external.get(ref)
            if local is not None and external is not None:
                issue(issues, path, "ambiguous_local_external_reference")
                continue
            if local is not None:
                target_population, target_row = local
                target_kind = RECORD_KIND_BY_POPULATION[target_population]
                if target_kind not in set(declared["allowed_local_record_kinds"]):
                    issue(issues, path, "wrong_reference_record_kind")
                allowed_sorts = set(declared["allowed_semantic_object_sorts"])
                if (
                    target_population == "O"
                    and allowed_sorts
                    and "*" not in allowed_sorts
                ):
                    if target_row["sort"] not in allowed_sorts:
                        issue(issues, path, "wrong_reference_sort")
                continue
            if external is not None:
                if external["external_target_kind"] not in set(
                    declared["allowed_external_target_kinds"]
                ):
                    issue(issues, path, "wrong_external_reference_kind")
                if external["basis_relation"] != declared["required_basis_relation"]:
                    issue(issues, path, "wrong_external_basis_relation")
                if external["reference_domain"] != declared["identity"]:
                    issue(issues, path, "wrong_external_reference_domain")
                continue
            issue(issues, path, "unresolved_reference")

    for row_id, (population, row) in record_by_id.items():
        path = f"$.candidate_model.{MODEL_FIELD_BY_POPULATION[population]}[id={row_id}]"
        for field in REFERENCE_FIELDS[population]:
            resolve_field(population, field, row[field], f"{path}.{field}")
        for (domain_population, field), domain_id in record_value_domains.items():
            if domain_population == population:
                value_in_domain(row[field], domain_id, f"{path}.{field}")
        if population == "O":
            if row["sort"] not in sorts:
                issue(issues, f"{path}.sort", "unknown_sort")
            else:
                value_in_domain(
                    row["value"],
                    sort_value_domains.get(row["sort"], ""),
                    f"{path}.value",
                )
        elif population == "E":
            declared = relation_kinds.get(row["kind"])
            if declared is None:
                issue(issues, f"{path}.kind", "unknown_relation_kind")
            else:
                qualifiers = row["qualifiers"]
                if any(
                    q not in set(declared["allowed_qualifiers"]) for q in qualifiers
                ):
                    issue(issues, f"{path}.qualifiers", "unknown_qualifier")
                if (
                    declared["qualifier_mode"] == "exactly_one_of"
                    and len(qualifiers) != 1
                ):
                    issue(issues, f"{path}.qualifiers", "wrong_qualifier_cardinality")
                for endpoint, allowed_field in (
                    ("source", "source_sorts"),
                    ("target", "target_sorts"),
                ):
                    resolved = record_by_id.get(row[endpoint])
                    if resolved and resolved[0] == "O":
                        allowed = set(declared[allowed_field])
                        if "*" not in allowed and resolved[1]["sort"] not in allowed:
                            issue(
                                issues, f"{path}.{endpoint}", f"wrong_{endpoint}_sort"
                            )
        elif population == "C":
            declared = constraint_kinds.get(row["kind"])
            if declared is None:
                issue(issues, f"{path}.kind", "unknown_constraint_kind")
            else:
                if row["judgment_kind"] != declared["judgment_kind"]:
                    issue(issues, f"{path}.judgment_kind", "wrong_constraint_judgment")
                value_in_domain(
                    row["predicate"], declared["predicate_domain"], f"{path}.predicate"
                )
                value_in_domain(
                    row["refusal"], declared["refusal_domain"], f"{path}.refusal"
                )
                target = record_by_id.get(row["applies_to"])
                if target and target[0] not in set(declared["subject_populations"]):
                    issue(
                        issues,
                        f"{path}.applies_to",
                        "wrong_constraint_subject_population",
                    )
            if row["judgment_kind"] not in judgment_kinds:
                issue(issues, f"{path}.judgment_kind", "unknown_judgment_kind")
        elif population == "L":
            if set(row["allowed_variation"]) & set(row["forbidden_variation"]):
                issue(issues, path, "latitude_overlap")
        elif population == "X":
            declared = residual_contracts.get(row["kind"])
            if declared is None:
                issue(issues, f"{path}.kind", "unknown_residual_kind")
            else:
                target = record_by_id.get(row["subject"])
                if target and target[0] not in set(declared["subject_populations"]):
                    issue(
                        issues, f"{path}.subject", "wrong_residual_subject_population"
                    )
        elif population == "V":
            if any(stop not in stop_kinds for stop in row["stop_states"]):
                issue(issues, f"{path}.stop_states", "unknown_traversal_stop")
        elif population == "T":
            traversal = record_by_id.get(row["traversal"])
            if traversal and traversal[0] == "V":
                traversal_row = traversal[1]
                for field, traversal_field in (
                    ("context", "context"),
                    ("owner", "owner"),
                    ("scope", "scope"),
                    ("basis", "basis"),
                    ("operation_authority", "authority"),
                ):
                    if row[field] != traversal_row[traversal_field]:
                        issue(
                            issues,
                            f"{path}.{field}",
                            "transformation_traversal_mismatch",
                        )
                if not set(row["stop_states"]) <= set(traversal_row["stop_states"]):
                    issue(issues, f"{path}.stop_states", "broader_transformation_stops")
            for left, right in (
                ("preserved", "introduced"),
                ("preserved", "removed"),
                ("introduced", "removed"),
                ("external_preserved", "external_introduced"),
                ("external_preserved", "external_removed"),
                ("external_introduced", "external_removed"),
            ):
                if set(row[left]) & set(row[right]):
                    issue(
                        issues, path, f"overlapping_transformation_delta:{left}:{right}"
                    )
            witnesses = row["external_resolution_witnesses"]
            if not isinstance(witnesses, list):
                issue(issues, f"{path}.external_resolution_witnesses", "expected_array")
            else:
                witnessed: list[str] = []
                for index, witness in enumerate(witnesses):
                    witness_path = f"{path}.external_resolution_witnesses[{index}]"
                    if not exact_keys(issues, witness, WITNESS_FIELDS, witness_path):
                        continue
                    for resolution_field in (
                        "domain_resolution",
                        "codomain_resolution",
                    ):
                        exact_keys(
                            issues,
                            witness[resolution_field],
                            RESOLUTION_FIELDS,
                            f"{witness_path}.{resolution_field}",
                        )
                    if witness["decision"] != "equal":
                        issue(
                            issues, f"{witness_path}.decision", "wrong_witness_decision"
                        )
                    if (
                        witness["domain_model"] != row["domain_model"]
                        or witness["codomain_model"] != row["codomain_model"]
                    ):
                        issue(issues, witness_path, "witness_model_mismatch")
                    if witness["domain_resolution"] != witness["codomain_resolution"]:
                        issue(issues, witness_path, "external_resolution_not_equal")
                    selected_resolution = resolution_by_external.get(
                        witness["external_resolution"]
                    )
                    if witness["domain_resolution"] != selected_resolution:
                        issue(issues, witness_path, "witness_resolution_mismatch")
                    witnessed.append(witness["external_resolution"])
                if witnessed != sorted(row["external_preserved"], key=utf16_key):
                    issue(
                        issues,
                        f"{path}.external_resolution_witnesses",
                        "witness_population_mismatch",
                    )
        elif population == "J":
            if row["kind"] not in judgment_kinds:
                issue(issues, f"{path}.kind", "unknown_judgment_kind")
            if (
                row["kind"] == JUDGMENT_KINDS["semantic_selection"]
                and row["decision"] == "accepted"
            ):
                issue(issues, path, "f_p_semantic_acceptance_judgment")
            subject = record_by_id.get(row["subject"])
            if subject is not None:
                expected_subject_digest = sha256(canonical_bytes(subject[1]))
                if row["subject_digest"] != expected_subject_digest:
                    issue(
                        issues,
                        f"{path}.subject_digest",
                        "judgment_subject_digest_mismatch",
                    )

    expected_member_map = {
        row["path"]: row["sha256"] for row in source_manifest.get("members", [])
    }
    expected_member_order = list(expected_member_map)
    supplied_members = {
        row["path"] for row in source_manifest.get("supplied_members", [])
    }

    def validate_locator(locator: Any, path: str) -> str | None:
        fields = {"basis_uri", "member_path", "member_sha256", "fragment"}
        if not exact_keys(issues, locator, fields, path):
            return None
        if locator["basis_uri"] != expected_basis["subject"]["release_uri"]:
            issue(issues, f"{path}.basis_uri", "source_locator_basis_mismatch")
        member_path = locator["member_path"]
        if not isinstance(member_path, str) or not member_path:
            issue(issues, f"{path}.member_path", "expected_nonempty_string")
            return None
        if expected_member_map.get(member_path) != locator["member_sha256"]:
            issue(issues, f"{path}.member_sha256", "source_member_mismatch")
        if locator["fragment"] is not None:
            issue(issues, f"{path}.fragment", "source_locator_fragment_not_null")
        return member_path

    def validate_locator_array(value: Any, path: str, *, nonempty: bool) -> list[bytes]:
        if not isinstance(value, list):
            issue(issues, path, "expected_array")
            return []
        if nonempty and not value:
            issue(issues, path, "expected_nonempty_array")
        locator_keys: list[bytes] = []
        for index, locator in enumerate(value):
            locator_path = f"{path}[{index}]"
            if validate_locator(locator, locator_path) is not None:
                try:
                    locator_keys.append(canonical_bytes(locator))
                except ValueError:
                    issue(issues, locator_path, "noncanonical_source_locator")
        if len(locator_keys) == len(value) and locator_keys != sorted(
            set(locator_keys)
        ):
            issue(issues, path, "source_locators_not_sorted_unique")
        return locator_keys

    def source_locator_identity(locator: dict[str, Any]) -> str:
        identity = locator["basis_uri"] + "standards/" + locator["member_path"]
        if locator["fragment"] is not None:
            identity += "#" + locator["fragment"]
        return identity

    source_member_identities = {
        expected_basis["subject"]["release_uri"] + "standards/" + member_path
        for member_path in expected_member_map
    }
    declared_source_identities = set(source_member_identities)
    raw_provenance = candidate["proposed_record_provenance"]
    if isinstance(raw_provenance, list):
        for raw_row in raw_provenance:
            if not isinstance(raw_row, dict):
                continue
            raw_locators = raw_row.get("source_locators")
            if not isinstance(raw_locators, list):
                continue
            for locator in raw_locators:
                if (
                    isinstance(locator, dict)
                    and set(locator)
                    == {"basis_uri", "member_path", "member_sha256", "fragment"}
                    and locator["basis_uri"] == expected_basis["subject"]["release_uri"]
                    and isinstance(locator["member_path"], str)
                    and expected_member_map.get(locator["member_path"])
                    == locator["member_sha256"]
                    and locator["fragment"] is None
                ):
                    declared_source_identities.add(source_locator_identity(locator))
    derivation_evidence_domain = {
        expected_basis["calculus"]["identity"],
        SUBJECT_BASIS_IDENTITY,
        expected_basis["signature"]["identity"],
        expected_basis["interpretation_contract"]["identity"],
        expected_basis["what_member_set_identity"],
        *declared_source_identities,
    }

    provenance = candidate["proposed_record_provenance"]
    provenance_refs: list[str] = []
    provenance_by_record: dict[str, dict[str, Any]] = {}
    if not isinstance(provenance, list):
        issue(issues, "$.proposed_record_provenance", "expected_array")
    else:
        for index, row in enumerate(provenance):
            path = f"$.proposed_record_provenance[{index}]"
            fields = {
                "model_record_ref",
                "provenance_kind",
                "semantic_address",
                "source_locators",
                "derivation_evidence_refs",
            }
            if not exact_keys(issues, row, fields, path):
                continue
            model_record_ref = row["model_record_ref"]
            if (
                not isinstance(model_record_ref, str)
                or IDENTITY_RE.fullmatch(model_record_ref) is None
            ):
                issue(
                    issues,
                    f"{path}.model_record_ref",
                    "invalid_provenance_model_ref",
                )
                continue
            provenance_refs.append(model_record_ref)
            if model_record_ref not in record_by_id:
                issue(
                    issues,
                    f"{path}.model_record_ref",
                    "unknown_provenance_model_ref",
                )
            if model_record_ref in provenance_by_record:
                issue(
                    issues,
                    f"{path}.model_record_ref",
                    "duplicate_record_provenance",
                )
            else:
                provenance_by_record[model_record_ref] = row

            address_path = f"{path}.semantic_address"
            address_fields = {
                "source_key",
                "term",
                "bounded_context",
                "owning_authority",
                "selected_basis",
                "governed_scope",
            }
            address = row["semantic_address"]
            address_valid = exact_keys(issues, address, address_fields, address_path)
            if address_valid:
                for field in (
                    "source_key",
                    "bounded_context",
                    "owning_authority",
                    "selected_basis",
                    "governed_scope",
                ):
                    if (
                        not isinstance(address[field], str)
                        or IDENTITY_RE.fullmatch(address[field]) is None
                    ):
                        issue(
                            issues,
                            f"{address_path}.{field}",
                            "invalid_semantic_address_identity",
                        )
                if not isinstance(address["term"], str) or not address["term"]:
                    issue(
                        issues,
                        f"{address_path}.term",
                        "expected_nonempty_string",
                    )
                if address["selected_basis"] != SUBJECT_BASIS_IDENTITY:
                    issue(
                        issues,
                        f"{address_path}.selected_basis",
                        "semantic_address_subject_basis_mismatch",
                    )
                record = record_by_id.get(model_record_ref)
                if record is not None:
                    record_row = record[1]
                    for address_field, record_field in (
                        ("bounded_context", "context"),
                        ("owning_authority", "owner"),
                        ("governed_scope", "scope"),
                    ):
                        if address[address_field] != record_row[record_field]:
                            issue(
                                issues,
                                f"{address_path}.{address_field}",
                                "semantic_address_record_mismatch",
                            )

            source_locators = row["source_locators"]
            validate_locator_array(
                source_locators, f"{path}.source_locators", nonempty=True
            )

            evidence_refs = string_set(
                issues,
                row["derivation_evidence_refs"],
                f"{path}.derivation_evidence_refs",
            )
            if any(IDENTITY_RE.fullmatch(ref) is None for ref in evidence_refs):
                issue(
                    issues,
                    f"{path}.derivation_evidence_refs",
                    "invalid_derivation_evidence_identity",
                )
            for evidence_ref in evidence_refs:
                if evidence_ref not in derivation_evidence_domain:
                    issue(
                        issues,
                        f"{path}.derivation_evidence_refs",
                        f"unresolved_derivation_evidence:{evidence_ref}",
                    )
            if row["provenance_kind"] != "subject_derived":
                issue(issues, f"{path}.provenance_kind", "unknown_provenance_kind")
            if not isinstance(source_locators, list) or not source_locators:
                issue(
                    issues,
                    f"{path}.source_locators",
                    "subject_derived_without_source_locator",
                )
            if address_valid and isinstance(address["source_key"], str):
                source_key = address["source_key"]
                if not source_key.startswith(GENERATED_SOURCE_KEY_PREFIX):
                    row_source_identities = set()
                    if isinstance(source_locators, list):
                        row_source_identities = {
                            source_locator_identity(locator)
                            for locator in source_locators
                            if isinstance(locator, dict)
                            and set(locator)
                            == {
                                "basis_uri",
                                "member_path",
                                "member_sha256",
                                "fragment",
                            }
                            and locator["basis_uri"]
                            == expected_basis["subject"]["release_uri"]
                            and isinstance(locator["member_path"], str)
                            and expected_member_map.get(locator["member_path"])
                            == locator["member_sha256"]
                            and locator["fragment"] is None
                        }
                    if source_key not in row_source_identities:
                        issue(
                            issues,
                            f"{address_path}.source_key",
                            "unresolved_semantic_source_key",
                        )
        if provenance_refs != sorted(set(provenance_refs), key=utf16_key):
            issue(
                issues,
                "$.proposed_record_provenance",
                "record_provenance_not_sorted_unique",
            )
    for missing in sorted(local_set - set(provenance_by_record), key=utf16_key):
        issue(
            issues,
            "$.proposed_record_provenance",
            f"missing_record_provenance:{missing}",
        )
    for extra in sorted(set(provenance_by_record) - local_set, key=utf16_key):
        issue(
            issues,
            "$.proposed_record_provenance",
            f"extra_record_provenance:{extra}",
        )

    selections = candidate["proposed_selections"]
    selection_by_id: dict[str, dict[str, Any]] = {}
    record_selection_count = {identity: 0 for identity in local_set}
    selection_ids: list[str] = []
    selection_dispositions = {
        "retained",
        "omitted",
        "uncertain",
        "inapplicable",
        "refused",
    }
    if not isinstance(selections, list):
        issue(issues, "$.proposed_selections", "expected_array")
    else:
        for index, row in enumerate(selections):
            path = f"$.proposed_selections[{index}]"
            fields = {
                "selection_ref",
                "source_locators",
                "disposition",
                "model_record_refs",
                "rationale",
                "source_owner",
            }
            if not exact_keys(issues, row, fields, path):
                continue
            selection_ref = row["selection_ref"]
            if (
                not isinstance(selection_ref, str)
                or IDENTITY_RE.fullmatch(selection_ref) is None
            ):
                issue(issues, f"{path}.selection_ref", "invalid_selection_identity")
                continue
            selection_ids.append(selection_ref)
            if selection_ref in selection_by_id:
                issue(issues, f"{path}.selection_ref", "duplicate_selection")
            selection_by_id[selection_ref] = row
            locators = row["source_locators"]
            validate_locator_array(locators, f"{path}.source_locators", nonempty=True)
            refs = string_set(
                issues, row["model_record_refs"], f"{path}.model_record_refs"
            )
            for ref in refs:
                if ref not in record_by_id:
                    issue(issues, f"{path}.model_record_refs", "unknown_model_ref")
                elif row["disposition"] == "retained":
                    record_selection_count[ref] += 1
            if row["disposition"] == "retained" and not refs:
                issue(issues, path, "retained_without_model_ref")
            if row["disposition"] in selection_dispositions - {"retained"} and refs:
                issue(issues, path, "non_retained_selection_has_model_refs")
            if row["disposition"] not in selection_dispositions:
                issue(issues, f"{path}.disposition", "unknown_disposition")
            for field in ("rationale", "source_owner"):
                value = row[field]
                if not isinstance(value, str) or not value:
                    issue(issues, f"{path}.{field}", "expected_nonempty_string")
            if IDENTITY_RE.fullmatch(row["source_owner"] or "") is None:
                issue(issues, f"{path}.source_owner", "invalid_source_owner")
        if selection_ids != sorted(set(selection_ids), key=utf16_key):
            issue(issues, "$.proposed_selections", "selections_not_sorted_unique")

    for selection_ref, selection in selection_by_id.items():
        if selection["disposition"] != "retained":
            continue
        selection_locators = selection["source_locators"]
        model_record_refs = selection["model_record_refs"]
        if not isinstance(selection_locators, list) or not isinstance(
            model_record_refs, list
        ):
            continue
        try:
            selection_locator_keys = {
                canonical_bytes(locator) for locator in selection_locators
            }
        except ValueError:
            continue
        for model_record_ref in model_record_refs:
            provenance_row = provenance_by_record.get(model_record_ref)
            if provenance_row is None:
                continue
            if provenance_row["provenance_kind"] == "subject_derived":
                try:
                    required_locator_keys = {
                        canonical_bytes(locator)
                        for locator in provenance_row["source_locators"]
                    }
                except (TypeError, ValueError):
                    continue
                if not required_locator_keys <= selection_locator_keys:
                    issue(
                        issues,
                        "$.proposed_selections",
                        f"selection_missing_record_source_locator:{selection_ref}:"
                        f"{model_record_ref}",
                    )

    evaluated = candidate["proposed_evaluated_members"]
    evaluated_paths: list[str] = []
    evaluated_member_ids: list[str] = []
    evaluated_refs_by_source: dict[tuple[str, str], set[str]] = {}
    referenced_selections: set[str] = set()
    if not isinstance(evaluated, list):
        issue(issues, "$.proposed_evaluated_members", "expected_array")
    else:
        for index, row in enumerate(evaluated):
            path = f"$.proposed_evaluated_members[{index}]"
            fields = {
                "member_path",
                "member_sha256",
                "disposition",
                "selection_refs",
                "rationale",
            }
            if not exact_keys(issues, row, fields, path):
                continue
            member_path = row["member_path"]
            evaluated_paths.append(member_path)
            if expected_member_map.get(member_path) != row["member_sha256"]:
                issue(issues, f"{path}.member_sha256", "source_member_mismatch")
            elif isinstance(member_path, str):
                evaluated_member_ids.append(
                    expected_basis["subject"]["release_uri"]
                    + "standards/"
                    + member_path
                )
            refs = string_set(issues, row["selection_refs"], f"{path}.selection_refs")
            if isinstance(member_path, str) and isinstance(row["member_sha256"], str):
                evaluated_refs_by_source[(member_path, row["member_sha256"])] = set(
                    refs
                )
            for ref in refs:
                if ref not in selection_by_id:
                    issue(issues, f"{path}.selection_refs", "unknown_selection_ref")
                else:
                    selection_locators = selection_by_id[ref]["source_locators"]
                    if not isinstance(selection_locators, list) or not any(
                        isinstance(locator, dict)
                        and locator.get("member_path") == member_path
                        and locator.get("member_sha256") == row["member_sha256"]
                        for locator in selection_locators
                    ):
                        issue(
                            issues,
                            f"{path}.selection_refs",
                            f"member_selection_without_matching_locator:{ref}",
                        )
                referenced_selections.add(ref)
            if row["disposition"] not in {
                "contains_retained_material",
                "contains_no_retained_material",
                "uncertain",
                "inapplicable",
                "refused",
            }:
                issue(issues, f"{path}.disposition", "unknown_disposition")
            known_selections = [
                selection_by_id[ref] for ref in refs if ref in selection_by_id
            ]
            if (
                row["disposition"]
                in {
                    "contains_no_retained_material",
                    "inapplicable",
                }
                and refs
            ):
                issue(
                    issues,
                    f"{path}.selection_refs",
                    "no_material_disposition_has_selection_refs",
                )
            if row["disposition"] == "contains_retained_material" and not any(
                selection["disposition"] == "retained"
                and bool(selection["model_record_refs"])
                for selection in known_selections
            ):
                issue(
                    issues,
                    f"{path}.selection_refs",
                    "retained_material_not_reached",
                )
            if row["disposition"] in {"uncertain", "refused"}:
                reaches_only_retained_residuals = bool(refs) and len(
                    known_selections
                ) == len(refs)
                for selection in known_selections:
                    model_refs = selection["model_record_refs"]
                    reaches_only_retained_residuals = (
                        reaches_only_retained_residuals
                        and selection["disposition"] == "retained"
                        and bool(model_refs)
                        and all(
                            ref in record_by_id and record_by_id[ref][0] == "X"
                            for ref in model_refs
                        )
                    )
                if not reaches_only_retained_residuals:
                    issue(
                        issues,
                        f"{path}.selection_refs",
                        "uncertain_or_refused_member_not_residual_only",
                    )
            if not isinstance(row["rationale"], str) or not row["rationale"]:
                issue(issues, f"{path}.rationale", "expected_nonempty_string")
            if member_path not in supplied_members and row["disposition"] not in {
                "uncertain",
                "refused",
            }:
                issue(issues, path, "unsupplied_member_not_uncertain")
        if evaluated_paths != expected_member_order:
            issue(issues, "$.proposed_evaluated_members", "source_inventory_mismatch")
    for selection_ref, selection in selection_by_id.items():
        source_locators = selection["source_locators"]
        if not isinstance(source_locators, list):
            continue
        for locator in source_locators:
            if not isinstance(locator, dict):
                continue
            source = (locator.get("member_path"), locator.get("member_sha256"))
            if not all(isinstance(value, str) for value in source):
                continue
            if selection_ref not in evaluated_refs_by_source.get(source, set()):
                issue(
                    issues,
                    "$.proposed_evaluated_members",
                    f"selection_locator_without_member_reference:{selection_ref}:"
                    f"{source[0]}",
                )
    for selection_ref in sorted(
        set(selection_by_id) - referenced_selections, key=utf16_key
    ):
        issue(
            issues,
            "$.proposed_evaluated_members",
            f"selection_without_member:{selection_ref}",
        )
    for record_id, count in sorted(
        record_selection_count.items(), key=lambda row: utf16_key(row[0])
    ):
        if count != 1:
            issue(
                issues,
                "$.proposed_selections",
                f"record_selection_cardinality:{record_id}:{count}",
            )

    generated = candidate["proposed_generated_source_keys"]
    generated_keys: list[str] = []
    generated_by_key: dict[str, list[dict[str, Any]]] = {}
    generated_preimages: list[bytes] = []
    if not isinstance(generated, list):
        issue(issues, "$.proposed_generated_source_keys", "expected_array")
    else:
        for index, row in enumerate(generated):
            path = f"$.proposed_generated_source_keys[{index}]"
            fields = {
                "source_key",
                "primary_source_locator",
                "local_declaration_key",
            }
            if not exact_keys(issues, row, fields, path):
                continue
            source_key = row["source_key"]
            if (
                not isinstance(source_key, str)
                or GENERATED_SOURCE_KEY_RE.fullmatch(source_key) is None
            ):
                issue(issues, f"{path}.source_key", "invalid_generated_source_key")
            else:
                generated_keys.append(source_key)
                generated_by_key.setdefault(source_key, []).append(row)
            locator_valid = (
                validate_locator(
                    row["primary_source_locator"], f"{path}.primary_source_locator"
                )
                is not None
            )
            local_declaration_key = row["local_declaration_key"]
            local_key_valid = isinstance(local_declaration_key, str) and bool(
                local_declaration_key
            )
            if not local_key_valid:
                issue(
                    issues, f"{path}.local_declaration_key", "expected_nonempty_string"
                )
            if locator_valid and local_key_valid:
                generated_preimages.append(
                    canonical_bytes(
                        {
                            "primary_source_locator": row["primary_source_locator"],
                            "local_declaration_key": local_declaration_key,
                        }
                    )
                )
            if (
                isinstance(source_key, str)
                and locator_valid
                and local_key_valid
                and source_key
                != generated_source_key(
                    row["primary_source_locator"], local_declaration_key
                )
            ):
                issue(
                    issues,
                    f"{path}.source_key",
                    "generated_source_key_derivation_mismatch",
                )
        if generated_keys != sorted(set(generated_keys), key=utf16_key):
            issue(
                issues,
                "$.proposed_generated_source_keys",
                "generated_source_keys_not_sorted_unique",
            )
        if len(generated_preimages) != len(set(generated_preimages)):
            issue(
                issues,
                "$.proposed_generated_source_keys",
                "duplicate_generated_source_key_preimage",
            )

    represented_generated_by_key: dict[str, list[dict[str, Any]]] = {}
    for provenance_row in provenance_by_record.values():
        address = provenance_row.get("semantic_address")
        if not isinstance(address, dict):
            continue
        source_key = address.get("source_key")
        if isinstance(source_key, str) and source_key.startswith(
            GENERATED_SOURCE_KEY_PREFIX
        ):
            represented_generated_by_key.setdefault(source_key, []).append(
                provenance_row
            )
    for source_key in sorted(
        set(generated_by_key) | set(represented_generated_by_key), key=utf16_key
    ):
        bindings = generated_by_key.get(source_key, [])
        represented = represented_generated_by_key.get(source_key, [])
        if len(bindings) != 1 or len(represented) != 1:
            issue(
                issues,
                "$.proposed_generated_source_keys",
                f"generated_source_key_coverage_mismatch:{source_key}",
            )
            continue
        try:
            primary_locator = canonical_bytes(bindings[0]["primary_source_locator"])
            represented_locators = {
                canonical_bytes(locator)
                for locator in represented[0]["source_locators"]
            }
        except (TypeError, ValueError):
            continue
        if primary_locator not in represented_locators:
            issue(
                issues,
                "$.proposed_generated_source_keys",
                f"generated_source_key_primary_locator_mismatch:{source_key}",
            )

    compilation_residuals = candidate["compilation_residuals"]
    residual_ids: list[str] = []
    if not isinstance(compilation_residuals, list):
        issue(issues, "$.compilation_residuals", "expected_array")
    else:
        for index, row in enumerate(compilation_residuals):
            path = f"$.compilation_residuals[{index}]"
            fields = {
                "residual_ref",
                "source_locators",
                "statement",
                "consequence",
                "model_residual_refs",
                "re_entry_route",
            }
            if not exact_keys(issues, row, fields, path):
                continue
            residual_ref = row["residual_ref"]
            if (
                not isinstance(residual_ref, str)
                or IDENTITY_RE.fullmatch(residual_ref) is None
            ):
                issue(
                    issues,
                    f"{path}.residual_ref",
                    "invalid_compilation_residual_identity",
                )
            else:
                residual_ids.append(residual_ref)
            validate_locator_array(
                row["source_locators"],
                f"{path}.source_locators",
                nonempty=True,
            )
            refs = string_set(
                issues, row["model_residual_refs"], f"{path}.model_residual_refs"
            )
            for ref in refs:
                if ref not in record_by_id or record_by_id[ref][0] != "X":
                    issue(issues, f"{path}.model_residual_refs", "unknown_residual_ref")
            for field in ("statement", "consequence", "re_entry_route"):
                if not isinstance(row[field], str) or not row[field]:
                    issue(issues, f"{path}.{field}", "expected_nonempty_string")
        if residual_ids != sorted(set(residual_ids), key=utf16_key):
            issue(issues, "$.compilation_residuals", "residuals_not_sorted_unique")

    identity_kinds: dict[str, set[str]] = {}
    for kind, identities_for_kind in (
        ("evaluated_member", set(evaluated_member_ids)),
        ("model_record", local_set),
        ("selection", set(selection_ids)),
        ("generated_source_key", set(generated_keys)),
        ("compilation_residual", set(residual_ids)),
    ):
        for identity in identities_for_kind:
            identity_kinds.setdefault(identity, set()).add(kind)
    for identity, kinds in sorted(
        identity_kinds.items(), key=lambda row: utf16_key(row[0])
    ):
        if len(kinds) > 1:
            issue(
                issues,
                "$.proposal_identity_partition",
                f"cross_kind_identity_collision:{identity}:{','.join(sorted(kinds))}",
            )

    if candidate["stop_state"] != STOP_KINDS["candidate"]:
        issue(issues, "$.stop_state", "not_a_compilation_candidate")
    if candidate["stop_state"] not in stop_kinds:
        issue(issues, "$.stop_state", "stop_not_in_signature")
    if not local_set:
        issue(issues, "$.candidate_model", "empty_candidate_model")
    return sorted(issues, key=lambda row: (row["path"], row["code"]))


def validate_stop(
    value: Any,
    expected_basis: dict[str, Any],
    signature: dict[str, Any],
    model_basis: str,
) -> list[dict[str, str]]:
    issues = validate_signature(signature)
    if model_basis != model_basis_identity(expected_basis):
        issue(issues, "$.basis", "unverified_model_basis_argument")
    top = {"kind", "schema_version", "payload"}
    if not exact_keys(issues, value, top, "$"):
        return sorted(issues, key=lambda row: (row["path"], row["code"]))
    if value["kind"] != "stdo-representation.semantic-compilation-stop":
        issue(issues, "$.kind", "wrong_kind")
    if value["schema_version"] != PROPOSAL_SCHEMA_VERSION:
        issue(issues, "$.schema_version", "wrong_schema_version")
    payload = value["payload"]
    if not exact_keys(
        issues,
        payload,
        {"stop_state", "reason_code", "re_entry_refs"},
        "$.payload",
    ):
        return sorted(issues, key=lambda row: (row["path"], row["code"]))
    if payload["stop_state"] not in {
        STOP_KINDS["hold"],
        STOP_KINDS["gap"],
        STOP_KINDS["refusal"],
    }:
        issue(issues, "$.payload.stop_state", "wrong_stop_state")
    if payload["reason_code"] not in {
        "basis_gap",
        "capability_mismatch",
        "insufficient_evidence",
        "output_contract_mismatch",
    }:
        issue(issues, "$.payload.reason_code", "unknown_stop_reason")
    re_entry_refs = string_set(
        issues,
        payload["re_entry_refs"],
        "$.payload.re_entry_refs",
        allow_empty=False,
    )
    if any(IDENTITY_RE.fullmatch(ref) is None for ref in re_entry_refs):
        issue(issues, "$.payload.re_entry_refs", "invalid_re_entry_identity")
    permission = next(
        (
            row
            for row in signature.get("traversal_permissions", [])
            if row.get("traversal") == COMPILE_TRAVERSAL
        ),
        None,
    )
    if permission is None:
        issue(issues, "$.stop_state", "undeclared_traversal")
    elif payload["stop_state"] not in set(permission.get("stops", [])):
        issue(issues, "$.payload.stop_state", "stop_not_permitted_by_traversal")
    return sorted(issues, key=lambda row: (row["path"], row["code"]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=("construct", "evaluate"))
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--raw-output", type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--candidate-structure-grant", type=Path)
    args = parser.parse_args()
    run = args.run.resolve()
    if args.operation == "construct":
        if args.raw_output is None:
            parser.error("construct requires --raw-output")
        if args.candidate is not None or args.candidate_structure_grant is not None:
            parser.error("construct does not accept candidate evaluation inputs")
    else:
        if args.raw_output is not None:
            parser.error("evaluate resolves the immutable raw-output binding")
        if args.candidate is None or args.candidate_structure_grant is None:
            parser.error(
                "evaluate requires --candidate and --candidate-structure-grant"
            )

    basis_path = run / "basis.json"
    source_manifest_path = run / "source-manifest.json"
    provenance_bundle_path = run / "compiler-provenance-bundle.json"
    basis = load_json(basis_path)
    acquisition = load_json(run / "acquisition.json")
    source_manifest = load_json(source_manifest_path)
    signature_path = TENANT / "profile" / "stdo-signature.json"
    contract_path = TENANT / "contract" / "v_compile.json"
    frame_path = TENANT / "profile" / "stdo-core-frame.json"
    prompt_path = TENANT / "prompt" / "v_compile.txt"
    schema_path = TENANT / "schema" / "candidate.schema.json"
    signature = load_json(signature_path)
    expected_basis = {
        key: basis[key]
        for key in (
            "calculus",
            "subject",
            "signature",
            "interpretation_contract",
            "frame",
            "source_packet",
            "subject_basis_identity",
            "what_member_set_identity",
        )
    }
    try:
        derived_model_basis = verify_run_acquisition(
            run,
            basis_path,
            source_manifest_path,
            acquisition,
            expected_basis,
            source_manifest,
        )
        provenance_bundle_bytes = provenance_bundle_path.read_bytes()
        provenance_bundle = load_json(provenance_bundle_path)
        provenance_member_bytes = verify_run_compiler_provenance_bundle(
            run,
            provenance_bundle,
            provenance_bundle_bytes,
        )
        live_calculus = verify_calculus_basis_candidate(
            DEFAULT_CALCULUS_BASIS, DEFAULT_STDO, DEFAULT_DERIVATION_STDO
        )
        installed_manifest_path = DEFAULT_STDO / "manifest.json"
        installed_manifest = load_json(installed_manifest_path)
        verify_manifest(DEFAULT_STDO, installed_manifest)
        live_contract = load_json(contract_path)
        verify_compilation_contract(live_contract, contract_path)
        live_frame = load_json(frame_path)
        verify_frame_configuration(live_frame, frame_path)
        verify_transport_schema(load_json(schema_path), schema_path)
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
    live_subject = {
        "release_uri": "stdo://releases/v2.5.0-rc.1/",
        "installed_manifest_sha256": digest_file(installed_manifest_path),
        "standards_member_set_sha256": (
            "sha256:" + installed_manifest["standards"]["member_set_sha256"]
        ),
        "member_count": installed_manifest["standards"]["member_count"],
    }
    live_bindings = {
        "calculus": live_calculus,
        "subject": live_subject,
        "signature": {
            "identity": signature["identity"],
            "sha256": digest_file(signature_path),
        },
        "interpretation_contract": {
            "identity": live_contract["identity"],
            "sha256": digest_file(contract_path),
        },
        "frame": {
            "configuration_identity": live_frame["identity"],
            "configuration_sha256": digest_file(frame_path),
            "frame_basis_identity": live_frame["frame_basis_identity"],
            "frame_basis_sha256": live_frame["frame_basis_sha256"],
            "selected_frame_refs": live_frame["selected_frame_refs"],
            "status": live_frame["status"],
        },
    }
    for field, expected in live_bindings.items():
        if expected_basis[field] != expected:
            raise SystemExit(f"selected {field} bytes differ from the run basis")
    if expected_basis["subject_basis_identity"] != SUBJECT_BASIS_IDENTITY:
        raise SystemExit("selected subject-basis identity differs from the Product")
    if expected_basis["what_member_set_identity"] != what_member_set_identity():
        raise SystemExit("selected WHAT member-set identity differs from the Product")
    live_members = [
        {"path": row["path"], "sha256": "sha256:" + row["sha256"]}
        for row in installed_manifest["standards"]["members"]
    ]
    if source_manifest.get("members") != live_members:
        raise SystemExit("selected source inventory differs from the installed release")
    if basis.get("compiler_prompt_sha256") != digest_file(prompt_path):
        raise SystemExit("selected prompt bytes differ from the run basis")
    if basis.get("transport_schema_sha256") != digest_file(schema_path):
        raise SystemExit("selected transport schema bytes differ from the run basis")

    try:
        if args.operation == "construct":
            raw_path, raw_identity, raw_sha = publish_raw_output(
                run, args.raw_output.resolve()
            )
        else:
            raw_path, raw_identity, raw_sha = resolve_raw_output(run)
        raw_bytes = raw_path.read_bytes()
        if sha256(raw_bytes) != raw_sha:
            raise ValueError("raw-output publication changed after binding")
        output = load_json(raw_path)
        domain_result, envelope_issues = decode_result_envelope(output)
        raw_canonical = canonical_bytes(output)
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error

    if domain_result is None:
        if args.operation != "construct":
            raise SystemExit("bound raw output does not construct a candidate")
        subject_sha = sha256(raw_canonical)
        result = {
            "kind": "stdo-index.semantic-compilation-envelope-structure-result",
            "schema_version": STRUCTURE_RESULT_SCHEMA_VERSION,
            "traversal_ref": "urn:stdo-index:traversal:compile-output-structure:2",
            "functor_ref": F_D,
            "subject_identity": (
                "urn:stdo-index:semantic-compilation-envelope:sha256:"
                + subject_sha.removeprefix("sha256:")
            ),
            "subject_sha256": subject_sha,
            "decision": "refusal",
            "issues": sorted(
                envelope_issues, key=lambda row: (row["path"], row["code"])
            ),
            "semantic_acceptance": "not_evaluated",
        }
        result_bytes = canonical_bytes(result)
        result_sha = sha256(result_bytes)
        result_path = (
            run
            / "evaluations"
            / "envelope"
            / digest_component(subject_sha)
            / digest_component(result_sha)
            / "semantic-compilation-envelope-structure-result.json"
        )
        publish_immutable(result_path, result_bytes)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        raise SystemExit(2)

    canonical = canonical_bytes(domain_result)
    if domain_result["kind"] == "stdo-representation.semantic-compilation-stop":
        if args.operation != "construct":
            raise SystemExit("bound raw output is a stop, not a candidate")
        issues = envelope_issues + validate_stop(
            domain_result, expected_basis, signature, derived_model_basis
        )
        issues = sorted(issues, key=lambda row: (row["path"], row["code"]))
        stop_sha = sha256(canonical)
        stop_path = (
            run
            / "artifacts"
            / "stop"
            / digest_component(stop_sha)
            / "semantic-compilation-stop.json"
        )
        publish_immutable(stop_path, canonical)
        result = {
            "kind": "stdo-index.semantic-compilation-stop-structure-result",
            "schema_version": STRUCTURE_RESULT_SCHEMA_VERSION,
            "traversal_ref": "urn:stdo-index:traversal:compile-stop-structure:2",
            "functor_ref": F_D,
            "subject_identity": (
                "urn:stdo-index:semantic-compilation-stop:sha256:"
                + stop_sha.removeprefix("sha256:")
            ),
            "subject_sha256": stop_sha,
            "decision": "valid" if not issues else "refusal",
            "issues": issues,
            "semantic_acceptance": "not_evaluated",
        }
        result_bytes = canonical_bytes(result)
        result_sha = sha256(result_bytes)
        result_path = (
            run
            / "evaluations"
            / "stop"
            / digest_component(stop_sha)
            / digest_component(result_sha)
            / "semantic-compilation-stop-structure-result.json"
        )
        publish_immutable(result_path, result_bytes)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        raise SystemExit(0 if not issues else 2)

    proposal = domain_result
    proposal_sha = sha256(canonical)
    proposal_path = proposal_artifact_path(run, proposal_sha)
    compiler_invocation = expected_invocation(run, acquisition, raw_path, raw_identity)
    try:
        candidate = construct_candidate(
            proposal,
            raw_bytes,
            expected_basis,
            source_manifest,
            compiler_invocation,
            provenance_bundle,
            provenance_bundle_bytes,
            provenance_member_bytes,
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    candidate_bytes = canonical_bytes(candidate)
    candidate_identity, candidate_sha = semantic_compilation_candidate_identity(
        candidate
    )
    candidate_path = candidate_artifact_path(
        run, expected_basis["what_member_set_identity"], candidate_sha
    )
    if args.operation == "construct":
        publish_immutable(proposal_path, canonical)
        publish_immutable(candidate_path, candidate_bytes)
        receipt = {
            "kind": "stdo-representation.semantic-compilation-construction-receipt",
            "schema_version": 1,
            "raw_output_identity": raw_identity,
            "raw_output_sha256": raw_sha,
            "proposal_sha256": proposal_sha,
            "semantic_compilation_candidate_identity": candidate_identity,
            "semantic_compilation_candidate_sha256": candidate_sha,
            "what_member_set_identity": expected_basis["what_member_set_identity"],
            "candidate_artifact_path": candidate_path.relative_to(run).as_posix(),
        }
        receipt_path = candidate_path.with_name("construction-receipt.json")
        publish_immutable(receipt_path, canonical_bytes(receipt))
        print(json.dumps(receipt, indent=2, ensure_ascii=False))
        raise SystemExit(0)

    supplied_candidate_path = args.candidate.resolve()
    if supplied_candidate_path != candidate_path.resolve():
        raise SystemExit(
            "candidate locator is not the exact WHAT-and-candidate digest coordinate"
        )
    try:
        if supplied_candidate_path.read_bytes() != candidate_bytes:
            raise ValueError("candidate artifact differs from reconstructed candidate")
    except (OSError, ValueError) as error:
        raise SystemExit(str(error)) from error
    try:
        grant_path = args.candidate_structure_grant.resolve()
        grant_bytes = grant_path.read_bytes()
        grant = load_json(grant_path)
        grant_identity = validate_candidate_structure_grant(
            grant,
            grant_bytes,
            candidate,
            expected_basis,
        )
    except (OSError, ValueError) as error:
        raise SystemExit(
            f"invalid candidate-structure evaluation grant: {error}"
        ) from error
    issues = envelope_issues + validate_candidate(
        candidate,
        expected_basis,
        source_manifest,
        signature,
        derived_model_basis,
        compiler_invocation,
    )
    issues = sorted(issues, key=lambda row: (row["path"], row["code"]))
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
    for row in issues:
        path = row["path"]
        code = row["code"]
        if "source" in path or "selection" in path or "residual" in path:
            checks["source_inventory"] = False
        if "missing_field" in code or "population" in code or "empty_candidate" in code:
            checks["population_totality"] = False
        if code.startswith("expected_") or code in {
            "missing_field",
            "unexpected_field",
            "invalid_record_identity",
        }:
            checks["record_shapes"] = False
        if "identity" in code or "identity" in path:
            checks["identity_derivation"] = False
        if "reference" in code or "reference_domains" in path:
            checks["reference_domains"] = False
        if "resolution" in code or "ResolutionSet_M" in path:
            checks["external_resolutions"] = False
        if "basis" in code or "basis" in path:
            checks["basis_coherence"] = False
        if "sorted" in code or "ordering" in code or "inventory_mismatch" in code:
            checks["ordering"] = False
        if (
            "provenance" in code
            or "compiler_invocation" in path
            or path.startswith("$.proposed_record_provenance")
            or path.startswith("$.proposed_generated_source_keys")
            or path.startswith("$.proposed_selections")
            or path.startswith("$.proposed_evaluated_members")
        ):
            checks["provenance_binding"] = False
    decision = "eligible" if all(checks.values()) and not issues else "refuse"
    result = {
        "kind": "stdo-representation.candidate-structure-result",
        "schema_version": STRUCTURE_RESULT_SCHEMA_VERSION,
        "semantic_compilation_candidate_identity": (candidate_identity),
        "semantic_compilation_candidate_sha256": candidate_sha,
        "calculus_basis_identity": candidate["calculus_basis_identity"],
        "signature_identity": candidate["signature_identity"],
        "interpretation_contract_identity": candidate[
            "interpretation_contract_identity"
        ],
        "traversal_ref": STRUCTURE_TRAVERSAL,
        "functor_ref": F_D,
        "evaluator_identity": EVALUATOR_IDENTITY,
        "checks": checks,
        "decision": decision,
        "evaluated_at": dt.datetime.now(dt.timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "evidence_refs": sorted(
            [
                grant_identity,
                compiler_provenance_bundle_ref(run.name),
                candidate_identity,
                raw_identity,
            ],
            key=utf16_key,
        ),
    }
    result_identity, result_sha = candidate_structure_result_identity(result)
    diagnostics = {
        "kind": "stdo-index.candidate-structure-diagnostics",
        "schema_version": STRUCTURE_RESULT_SCHEMA_VERSION,
        "semantic_compilation_candidate_sha256": candidate_sha,
        "candidate_structure_result_identity": result_identity,
        "candidate_structure_result_sha256": result_sha,
        "issues": issues,
    }
    result_root = evaluation_artifact_root(run, candidate_sha, result_sha)
    publish_immutable(
        result_root / "candidate-structure-diagnostics.json",
        canonical_bytes(diagnostics),
    )
    publish_immutable(
        result_root / "candidate-structure-result.json", canonical_bytes(result)
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if decision == "eligible" else 2)


if __name__ == "__main__":
    main()
