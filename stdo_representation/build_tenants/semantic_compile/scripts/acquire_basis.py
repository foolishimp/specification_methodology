#!/usr/bin/env python3
"""Acquire exact STDO 2.5 semantic-compilation inputs without interpretation."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any


TENANT = Path(__file__).resolve().parents[1]
REPO = TENANT.parents[1]
SUBJECT_BASIS_IDENTITY = (
    "urn:stdo-representation:subject-basis:stdo:sha256:"
    "73f2581c2d8466a2c8e41b842c2178495431ff28450192f00368ec9fff8766a6"
)
SIGNATURE_EXTERNAL_KIND = (
    "urn:stdo-index:external-target-kind:target-signature-member:1"
)
SIGNATURE_BASIS_RELATION = "urn:stdo-index:basis-relation:exact-target-signature:1"
DEFAULT_STDO = Path.home() / "Library/Application Support/STDO/releases/v2.5.0-rc.1"
DEFAULT_DERIVATION_STDO = (
    Path.home() / "Library/Application Support/STDO/releases/v2.4.3-rc.3"
)
DEFAULT_CALCULUS_BASIS = TENANT / "profile" / "axiomatic-calculus-basis.candidate.json"
FRAME_BASIS_PATH = REPO / "specification" / "REFERENCE_FRAME_BASIS.md"
PRODUCT_PATH = REPO / "specification" / "PRODUCT.md"
BASIS_REQUIREMENT_PATH = (
    REPO / "specification" / "requirements" / "REQ-P-BASIS-AND-IDENTITY.md"
)
OVERLAY_PATH = REPO / "stdo_representation.json"
DEFAULT_FRAME_ACCEPTANCE = TENANT / "authority" / "frame-basis.acceptance.json"
DEFAULT_COMPILE_GRANT = TENANT / "authority" / "semantic-compile.grant.json"
DEFAULT_COMPILE_ACTIVATION = TENANT / "authority" / "semantic-compile.activation.json"
DEFAULT_CAPABILITY_ENVELOPE = TENANT / "authority" / "semantic-compile.capability.json"
FRAME_BASIS_IDENTITY = "urn:stdo-representation:reference-frame-basis:source-project:7"
SEMANTIC_COMPILATION_FRAME = "urn:stdo-representation:frame:semantic-compilation"
COMPILE_TRAVERSAL = "urn:stdo-representation:traversal:semantic-compile:7"
ACCEPT_FRAME_TRAVERSAL = "urn:stdo-representation:traversal:accept-frame-basis:1"
F_P = "urn:stdo:concept:axiomatic-calculus:f-p"
CALCULUS_BASIS_IDENTITY = (
    "urn:stdo:axiomatic-calculus-basis:sha256:"
    "bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da"
)
CAPABILITY_IDENTITY = "urn:axiom-indexer:capability:semantic-compilation-prototype:1"
HOST_IDENTITY = "urn:openai:codex-cli"
MODEL_IDENTITY = "gpt-5.6-sol"
CONTEXT_BUDGET_TOKENS = 1_000_000
PRODUCT_OWNER_ACTOR = "https://github.com/foolishimp"
PRODUCT_OWNER_AUTHORITY = "urn:stdo-representation:authority:product-owner"
PRODUCT_OWNER_GRANT = "urn:stdo-representation:grant:product-owner:1"
PRODUCT_OWNER_GRANT_SCOPE = (
    "Select and accept project-owned frame bases, representation profiles, Source "
    "STDO semantic selections, candidate STDO.gtl Products, and tenant-qualified "
    "releases; authorize deterministic construction; and issue bounded build-time "
    "operation grants for proposal-only semantic-compilation and deterministic "
    "structural-evaluation traversals; excludes changing Source STDO or transferring "
    "semantic, review, acceptance, release, or runtime authority to a traversal."
)
COMPILE_GRANT_SCOPE = (
    "Invoke one proposal-only F_P[v_compile] traversal over the exact sealed "
    "subject; grants no semantic, selection, acceptance, carrier, source-mutation, "
    "release, or runtime authority."
)
COMPILER_PROVENANCE_MEMBER_FILES = {
    "acquisition": "acquisition.json",
    "basis": "basis.json",
    "source_manifest": "source-manifest.json",
    "invocation": "invocation.txt",
    "sealed_invocation": "sealed-invocation.txt",
    "frame_acceptance": "preflight/frame_acceptance.json",
    "compile_grant": "preflight/compile_grant.json",
    "compile_activation": "preflight/compile_activation.json",
    "capability_envelope": "preflight/capability_envelope.json",
}
IDENTITY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:[^\s]+$")
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
TIMESTAMP_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
RECORD_KINDS = {
    "O": "urn:stdo:concept:axiomatic-calculus:record-kind:semantic-object",
    "E": "urn:stdo:concept:axiomatic-calculus:record-kind:typed-relation",
    "C": "urn:stdo:concept:axiomatic-calculus:record-kind:constraint",
    "L": "urn:stdo:concept:axiomatic-calculus:record-kind:latitude",
    "X": "urn:stdo:concept:axiomatic-calculus:record-kind:residual",
    "V": "urn:stdo:concept:axiomatic-calculus:record-kind:traversal",
    "T": "urn:stdo:concept:axiomatic-calculus:record-kind:transformation",
    "J": "urn:stdo:concept:axiomatic-calculus:record-kind:judgment",
}
CALCULUS_MEMBER = "AXIOMATIC_CALCULUS.md"
CALCULUS_CONCEPT = "urn:stdo:concept:axiomatic-calculus:a-c"
EXPECTED_DERIVATION_TARGETS = {
    "IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004",
    "IDENTITY_METHOD.md#core-law",
    "REFERENCE_FRAME_METHOD.md#evaluation",
    "REFERENCE_FRAME_METHOD.md#position",
    "REFERENCE_FRAME_METHOD.md#reference-frame-laws",
    "REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates",
    "REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation",
    "REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation",
    "REFERENCE_FRAME_METHOD.md#rf-012-closed-results",
    "SPEC_METHOD.md#agentic-construction-execution-stdo-up-020",
    "SPEC_METHOD.md#ambiguity-governance-rule",
    "SPEC_METHOD.md#bounded-context-semantic-resolution",
    "SPEC_METHOD.md#constitutional-chain",
    "SPEC_METHOD.md#one-constitutional-surface-and-version-boundary-stdo-surface-001",
}


class DuplicateKey(ValueError):
    pass


def unique_pairs(values: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in values:
        if key in result:
            raise DuplicateKey(key)
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_bytes(), object_pairs_hook=unique_pairs)


def utf16_key(value: str) -> bytes:
    return value.encode("utf-16-be", "surrogatepass")


def canonical_bytes(value: Any) -> bytes:
    if value is None:
        return b"null"
    if value is True:
        return b"true"
    if value is False:
        return b"false"
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > 9_007_199_254_740_991:
            raise ValueError("non_i_json_integer")
        return str(value).encode("ascii")
    if isinstance(value, float):
        raise ValueError("unsupported_or_non_i_json_number")
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()
    if isinstance(value, list):
        return b"[" + b",".join(canonical_bytes(item) for item in value) + b"]"
    if isinstance(value, dict):
        members = [
            canonical_bytes(key) + b":" + canonical_bytes(value[key])
            for key in sorted(value, key=utf16_key)
        ]
        return b"{" + b",".join(members) + b"}"
    raise ValueError("non_i_json_value")


def digest_bytes(value: bytes) -> str:
    return f"sha256:{hashlib.sha256(value).hexdigest()}"


def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def write_canonical(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_bytes(value) + b"\n")


def model_configuration_sha256() -> str:
    return digest_bytes(
        canonical_bytes(
            {
                "model": MODEL_IDENTITY,
                "reasoning_effort": "xhigh",
                "sandbox": "read-only",
                "ephemeral": True,
            }
        )
    )


def is_identity(value: Any) -> bool:
    return isinstance(value, str) and IDENTITY_RE.fullmatch(value) is not None


def is_sorted_unique_strings(value: Any, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (not nonempty or bool(value))
        and all(isinstance(item, str) and item for item in value)
        and value == sorted(set(value), key=utf16_key)
    )


def record_binding(kind: str, record: dict[str, Any]) -> dict[str, str]:
    sha = digest_bytes(canonical_bytes(record))
    return {
        "identity": f"urn:stdo-representation:{kind}:sha256:{sha[7:]}",
        "sha256": sha,
    }


def compiler_provenance_member_ref(run_id: str, member_kind: str) -> str:
    label = member_kind.replace("_", "-")
    return f"urn:stdo-representation:semantic-compilation-run:{run_id}:{label}"


def compiler_provenance_bundle_ref(run_id: str) -> str:
    return (
        f"urn:stdo-representation:semantic-compilation-run:{run_id}:"
        "compiler-provenance-bundle"
    )


def build_compiler_provenance_bundle(run_root: Path) -> dict[str, Any]:
    members = []
    for member_kind in sorted(COMPILER_PROVENANCE_MEMBER_FILES, key=utf16_key):
        member_path = run_root / COMPILER_PROVENANCE_MEMBER_FILES[member_kind]
        if not member_path.is_file():
            raise ValueError(f"missing compiler provenance member: {member_kind}")
        members.append(
            {
                "member_kind": member_kind,
                "member_ref": compiler_provenance_member_ref(
                    run_root.name, member_kind
                ),
                "member_sha256": digest_file(member_path),
            }
        )
    return {
        "kind": "stdo-representation.compiler-provenance-bundle",
        "schema_version": 1,
        "members": members,
    }


def verify_compiler_provenance_bundle(
    bundle: Any,
    bundle_bytes: bytes,
    resolved_member_bytes: dict[str, bytes],
) -> None:
    if (
        not isinstance(bundle, dict)
        or set(bundle) != {"kind", "schema_version", "members"}
        or bundle.get("kind") != "stdo-representation.compiler-provenance-bundle"
        or bundle.get("schema_version") != 1
        or not isinstance(bundle.get("members"), list)
    ):
        raise ValueError("invalid compiler provenance bundle")
    if bundle_bytes != canonical_bytes(bundle):
        raise ValueError("compiler provenance bundle is not exact unframed JCS")
    expected_kinds = sorted(COMPILER_PROVENANCE_MEMBER_FILES, key=utf16_key)
    observed_kinds: list[str] = []
    observed_refs: list[str] = []
    for member in bundle["members"]:
        if not isinstance(member, dict) or set(member) != {
            "member_kind",
            "member_ref",
            "member_sha256",
        }:
            raise ValueError("invalid compiler provenance member")
        member_kind = member["member_kind"]
        member_ref = member["member_ref"]
        member_sha256 = member["member_sha256"]
        if (
            not isinstance(member_kind, str)
            or not isinstance(member_ref, str)
            or not member_ref
            or not isinstance(member_sha256, str)
            or SHA256_RE.fullmatch(member_sha256) is None
        ):
            raise ValueError("invalid compiler provenance member coordinate")
        member_bytes = resolved_member_bytes.get(member_ref)
        if member_bytes is None or digest_bytes(member_bytes) != member_sha256:
            raise ValueError(f"unresolved compiler provenance member: {member_kind}")
        observed_kinds.append(member_kind)
        observed_refs.append(member_ref)
    if observed_kinds != expected_kinds:
        raise ValueError("compiler provenance member population mismatch")
    if len(observed_refs) != len(set(observed_refs)):
        raise ValueError("duplicate compiler provenance member reference")
    if set(resolved_member_bytes) != set(observed_refs):
        raise ValueError("compiler provenance resolution population mismatch")


def verify_run_compiler_provenance_bundle(
    run_root: Path,
    bundle: Any,
    bundle_bytes: bytes,
) -> dict[str, bytes]:
    expected = build_compiler_provenance_bundle(run_root)
    if bundle != expected:
        raise ValueError("compiler provenance bundle differs from run evidence")
    resolved = {
        compiler_provenance_member_ref(run_root.name, member_kind): (
            run_root / member_path
        ).read_bytes()
        for member_kind, member_path in COMPILER_PROVENANCE_MEMBER_FILES.items()
    }
    verify_compiler_provenance_bundle(bundle, bundle_bytes, resolved)
    return resolved


def product_selected_calculus_basis(calculus: dict[str, Any]) -> None:
    if CALCULUS_BASIS_IDENTITY != (
        "urn:stdo:axiomatic-calculus-basis:sha256:"
        + digest_bytes(canonical_bytes(calculus))[7:]
    ):
        raise ValueError("calculus basis identity differs from Product selection")
    product = PRODUCT_PATH.read_text(encoding="utf-8")
    requirement = BASIS_REQUIREMENT_PATH.read_text(encoding="utf-8")
    required_product_fragments = {
        "This source definition selects the following immutable `a_c` basis identity:",
        "bac18f57d655ce730462b84d62306d4af9ef3ebe1292f9889d67fe877f31d0da",
        calculus["derivation_basis"]["manifest_sha256"],
        calculus["publication_basis"]["manifest_sha256"],
        calculus["publication_basis"]["member_sha256"],
    }
    required_product_fragments.update(calculus["derivation_basis"]["principle_refs"])
    if any(fragment not in product for fragment in required_product_fragments):
        raise ValueError("calculus basis differs from exact Product basis")
    if CALCULUS_BASIS_IDENTITY not in requirement:
        raise ValueError("calculus basis differs from REQ-P-BASIS-014")


def _load_preflight_record(
    path: Path, coordinate: str, issues: list[dict[str, str]]
) -> dict[str, Any] | None:
    if not path.is_file():
        issues.append({"code": f"missing_{coordinate}", "coordinate": coordinate})
        return None
    try:
        raw = path.read_bytes()
        value = load_json(path)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, DuplicateKey):
        issues.append({"code": f"invalid_{coordinate}", "coordinate": coordinate})
        return None
    if not isinstance(value, dict) or raw != canonical_bytes(value):
        issues.append({"code": f"noncanonical_{coordinate}", "coordinate": coordinate})
        return None
    return value


def semantic_compile_preflight(
    *,
    frame_acceptance_path: Path,
    compile_grant_path: Path,
    compile_activation_path: Path,
    capability_envelope_path: Path,
    overlay: dict[str, Any],
    frame: dict[str, Any],
    calculus: dict[str, Any],
    signature_ref: dict[str, str],
    contract_ref: dict[str, str],
    source_packet_ref: dict[str, str],
    prompt_sha256: str,
    schema_sha256: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    """Resolve execution authority before any run artifact or F_P invocation exists."""

    issues: list[dict[str, str]] = []
    records: dict[str, dict[str, Any]] = {}
    for coordinate, path in (
        ("frame_acceptance", frame_acceptance_path),
        ("compile_grant", compile_grant_path),
        ("compile_activation", compile_activation_path),
        ("capability_envelope", capability_envelope_path),
    ):
        value = _load_preflight_record(path, coordinate, issues)
        if value is not None:
            records[coordinate] = value

    overlay_rows = overlay.get("reference_frame_bases")
    authorities: list[str] = []
    if isinstance(overlay_rows, list):
        for row in overlay_rows:
            if not isinstance(row, dict):
                continue
            if row.get("uri") not in {
                FRAME_BASIS_IDENTITY,
                "./specification/REFERENCE_FRAME_BASIS.md",
            }:
                continue
            value = row.get("authority")
            if isinstance(value, list):
                authorities.extend(item for item in value if isinstance(item, str))
            elif isinstance(value, str):
                authorities.append(value)
    authorities = sorted(set(authorities), key=utf16_key)
    if not authorities:
        issues.append(
            {"code": "frame_basis_not_admitted", "coordinate": "product_overlay"}
        )
    product_text = PRODUCT_PATH.read_text(encoding="utf-8")
    product_owner_grant_declared = all(
        value in product_text
        for value in (
            PRODUCT_OWNER_ACTOR,
            PRODUCT_OWNER_AUTHORITY,
            PRODUCT_OWNER_GRANT,
            PRODUCT_OWNER_GRANT_SCOPE,
        )
    )
    if not product_owner_grant_declared:
        issues.append(
            {
                "code": "product_owner_grant_unresolved",
                "coordinate": "product_authority",
            }
        )

    frame_acceptance = records.get("frame_acceptance")
    frame_binding: dict[str, str] | None = None
    if frame_acceptance is not None:
        fields = {
            "kind",
            "schema_version",
            "subject_kind",
            "subject_identity",
            "subject_sha256",
            "traversal_ref",
            "actor_identity",
            "authority_identity",
            "grant_identity",
            "grant_scope",
            "basis_refs",
            "admitting_authority_refs",
            "decision",
            "decided_at",
            "evidence_refs",
            "supersedes",
        }
        valid = (
            set(frame_acceptance) == fields
            and product_owner_grant_declared
            and frame_acceptance.get("kind")
            == "stdo-representation.authority-acceptance"
            and frame_acceptance.get("schema_version") == 1
            and frame_acceptance.get("subject_kind") == "reference_frame_basis"
            and frame_acceptance.get("subject_identity") == FRAME_BASIS_IDENTITY
            and frame_acceptance.get("subject_sha256") == frame["frame_basis_sha256"]
            and frame_acceptance.get("decision") == "accepted"
            and frame_acceptance.get("traversal_ref") == ACCEPT_FRAME_TRAVERSAL
            and frame_acceptance.get("actor_identity") == PRODUCT_OWNER_ACTOR
            and frame_acceptance.get("authority_identity") == PRODUCT_OWNER_AUTHORITY
            and frame_acceptance.get("grant_identity") == PRODUCT_OWNER_GRANT
            and frame_acceptance.get("grant_scope") == PRODUCT_OWNER_GRANT_SCOPE
            and frame_acceptance.get("basis_refs")
            == sorted([CALCULUS_BASIS_IDENTITY, SUBJECT_BASIS_IDENTITY], key=utf16_key)
            and frame_acceptance.get("admitting_authority_refs") == authorities
            and TIMESTAMP_RE.fullmatch(frame_acceptance.get("decided_at", ""))
            is not None
            and is_sorted_unique_strings(
                frame_acceptance.get("evidence_refs"), nonempty=True
            )
            and (
                frame_acceptance.get("supersedes") is None
                or (
                    isinstance(frame_acceptance.get("supersedes"), str)
                    and frame_acceptance["supersedes"].startswith(
                        "urn:stdo-representation:authority-acceptance:sha256:"
                    )
                )
            )
        )
        if not valid:
            issues.append(
                {"code": "frame_acceptance_mismatch", "coordinate": "frame_acceptance"}
            )
        else:
            sha = digest_bytes(canonical_bytes(frame_acceptance))
            frame_binding = {
                "identity": (
                    "urn:stdo-representation:authority-acceptance:sha256:" + sha[7:]
                ),
                "sha256": sha,
            }

    capability = records.get("capability_envelope")
    capability_binding: dict[str, str] | None = None
    if capability is not None:
        fields = {
            "kind",
            "schema_version",
            "identity",
            "actor_identity",
            "host_identity",
            "model_identity",
            "model_configuration_sha256",
            "supported_traversal_refs",
            "maximum_context_tokens",
            "output_schema_sha256",
            "evidence_refs",
        }
        valid = (
            set(capability) == fields
            and capability.get("kind")
            == "stdo-representation.semantic-compiler-capability-envelope"
            and capability.get("schema_version") == 1
            and capability.get("identity") == CAPABILITY_IDENTITY
            and is_identity(capability.get("actor_identity"))
            and capability.get("host_identity") == HOST_IDENTITY
            and capability.get("model_identity") == MODEL_IDENTITY
            and capability.get("model_configuration_sha256")
            == model_configuration_sha256()
            and is_sorted_unique_strings(
                capability.get("supported_traversal_refs"), nonempty=True
            )
            and COMPILE_TRAVERSAL in capability.get("supported_traversal_refs", [])
            and isinstance(capability.get("maximum_context_tokens"), int)
            and not isinstance(capability.get("maximum_context_tokens"), bool)
            and capability.get("maximum_context_tokens", 0) >= CONTEXT_BUDGET_TOKENS
            and capability.get("output_schema_sha256") == schema_sha256
            and is_sorted_unique_strings(capability.get("evidence_refs"), nonempty=True)
        )
        if not valid:
            issues.append(
                {
                    "code": "capability_envelope_mismatch",
                    "coordinate": "capability_envelope",
                }
            )
        else:
            capability_binding = {
                "identity": capability["identity"],
                "sha256": digest_bytes(canonical_bytes(capability)),
            }

    compile_grant = records.get("compile_grant")
    compile_grant_binding: dict[str, str] | None = None
    if compile_grant is not None:
        fields = {
            "kind",
            "schema_version",
            "issuer_actor_identity",
            "authority_identity",
            "parent_grant_identity",
            "parent_grant_scope",
            "grantee_actor_identity",
            "traversal_ref",
            "functor_ref",
            "frame_acceptance_identity",
            "frame_acceptance_sha256",
            "frame_configuration_identity",
            "frame_configuration_sha256",
            "subject_basis_identity",
            "source_packet_identity",
            "source_packet_sha256",
            "calculus_basis_identity",
            "signature_identity",
            "signature_sha256",
            "interpretation_contract_identity",
            "interpretation_contract_sha256",
            "what_member_set_identity",
            "compiler_prompt_sha256",
            "output_schema_sha256",
            "capability_envelope_identity",
            "capability_envelope_sha256",
            "scope",
            "issued_at",
            "evidence_refs",
        }
        expected = {
            "issuer_actor_identity": PRODUCT_OWNER_ACTOR,
            "authority_identity": PRODUCT_OWNER_AUTHORITY,
            "parent_grant_identity": PRODUCT_OWNER_GRANT,
            "parent_grant_scope": PRODUCT_OWNER_GRANT_SCOPE,
            "grantee_actor_identity": (capability or {}).get("actor_identity"),
            "traversal_ref": COMPILE_TRAVERSAL,
            "functor_ref": F_P,
            "frame_acceptance_identity": (frame_binding or {}).get("identity"),
            "frame_acceptance_sha256": (frame_binding or {}).get("sha256"),
            "frame_configuration_identity": frame["identity"],
            "frame_configuration_sha256": digest_file(
                TENANT / "profile" / "stdo-core-frame.json"
            ),
            "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
            "source_packet_identity": source_packet_ref["identity"],
            "source_packet_sha256": source_packet_ref["sha256"],
            "calculus_basis_identity": calculus["identity"],
            "signature_identity": signature_ref["identity"],
            "signature_sha256": signature_ref["sha256"],
            "interpretation_contract_identity": contract_ref["identity"],
            "interpretation_contract_sha256": contract_ref["sha256"],
            "what_member_set_identity": what_member_set_identity(),
            "compiler_prompt_sha256": prompt_sha256,
            "output_schema_sha256": schema_sha256,
            "capability_envelope_identity": (capability_binding or {}).get("identity"),
            "capability_envelope_sha256": (capability_binding or {}).get("sha256"),
            "scope": COMPILE_GRANT_SCOPE,
        }
        valid = (
            set(compile_grant) == fields
            and product_owner_grant_declared
            and compile_grant.get("kind")
            == "stdo-representation.semantic-compilation-operation-grant"
            and compile_grant.get("schema_version") == 1
            and all(
                compile_grant.get(field) == value for field, value in expected.items()
            )
            and TIMESTAMP_RE.fullmatch(compile_grant.get("issued_at", "")) is not None
            and is_sorted_unique_strings(
                compile_grant.get("evidence_refs"), nonempty=True
            )
        )
        if not valid:
            issues.append(
                {
                    "code": "compile_grant_authority_mismatch",
                    "coordinate": "compile_grant",
                }
            )
        else:
            compile_grant_binding = record_binding(
                "semantic-compilation-operation-grant", compile_grant
            )

    activation = records.get("compile_activation")
    activation_binding: dict[str, str] | None = None
    if activation is not None:
        fields = {
            "kind",
            "schema_version",
            "traversal_ref",
            "functor_ref",
            "frame_acceptance_identity",
            "frame_acceptance_sha256",
            "frame_configuration_identity",
            "frame_configuration_sha256",
            "subject_basis_identity",
            "source_packet_identity",
            "source_packet_sha256",
            "calculus_basis_identity",
            "signature_identity",
            "signature_sha256",
            "interpretation_contract_identity",
            "interpretation_contract_sha256",
            "what_member_set_identity",
            "compiler_prompt_sha256",
            "actor_identity",
            "authority_identity",
            "grant_identity",
            "grant_sha256",
            "grant_scope",
            "activated_at",
            "capability_envelope_identity",
            "capability_envelope_sha256",
            "evidence_refs",
        }
        expected = {
            "traversal_ref": COMPILE_TRAVERSAL,
            "functor_ref": F_P,
            "frame_acceptance_identity": (frame_binding or {}).get("identity"),
            "frame_acceptance_sha256": (frame_binding or {}).get("sha256"),
            "frame_configuration_identity": frame["identity"],
            "frame_configuration_sha256": digest_file(
                TENANT / "profile" / "stdo-core-frame.json"
            ),
            "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
            "source_packet_identity": source_packet_ref["identity"],
            "source_packet_sha256": source_packet_ref["sha256"],
            "calculus_basis_identity": calculus["identity"],
            "signature_identity": signature_ref["identity"],
            "signature_sha256": signature_ref["sha256"],
            "interpretation_contract_identity": contract_ref["identity"],
            "interpretation_contract_sha256": contract_ref["sha256"],
            "what_member_set_identity": what_member_set_identity(),
            "compiler_prompt_sha256": prompt_sha256,
            "capability_envelope_identity": (capability_binding or {}).get("identity"),
            "capability_envelope_sha256": (capability_binding or {}).get("sha256"),
            "actor_identity": (compile_grant or {}).get("grantee_actor_identity"),
            "authority_identity": (compile_grant or {}).get("authority_identity"),
            "grant_identity": (compile_grant_binding or {}).get("identity"),
            "grant_sha256": (compile_grant_binding or {}).get("sha256"),
            "grant_scope": (compile_grant or {}).get("scope"),
        }
        valid = (
            set(activation) == fields
            and activation.get("kind")
            == "stdo-representation.semantic-compilation-activation"
            and activation.get("schema_version") == 1
            and all(activation.get(field) == value for field, value in expected.items())
            and capability is not None
            and compile_grant is not None
            and activation.get("actor_identity") == capability.get("actor_identity")
            and TIMESTAMP_RE.fullmatch(activation.get("activated_at", "")) is not None
            and is_sorted_unique_strings(activation.get("evidence_refs"), nonempty=True)
        )
        if not valid:
            issues.append(
                {
                    "code": "compile_activation_mismatch",
                    "coordinate": "compile_activation",
                }
            )
        else:
            activation_binding = record_binding(
                "semantic-compilation-activation", activation
            )

    issues.sort(key=lambda row: (row["coordinate"], row["code"]))
    bindings: dict[str, Any] = {}
    if not issues:
        bindings = {
            "frame_acceptance": frame_binding,
            "compile_grant": compile_grant_binding,
            "compile_activation": activation_binding,
            "capability_envelope": capability_binding,
        }
    result = {
        "kind": "stdo-representation.semantic-compilation-preflight-result",
        "schema_version": 1,
        "decision": "ready" if not issues else "hold",
        "issues": issues,
    }
    return result, bindings, records


def verify_frame_configuration(frame: Any, frame_path: Path) -> None:
    expected = {
        "kind": "stdo-representation.semantic-compilation-frame-configuration",
        "schema_version": 2,
        "identity": "urn:stdo-representation:frame-configuration:semantic-compilation:3",
        "frame_basis_identity": FRAME_BASIS_IDENTITY,
        "frame_basis_sha256": digest_file(FRAME_BASIS_PATH),
        "selected_frame_refs": [SEMANTIC_COMPILATION_FRAME],
        "status": "candidate",
    }
    if frame != expected:
        raise ValueError(f"frame configuration differs from exact basis: {frame_path}")


def verify_compilation_contract(contract: Any, contract_path: Path) -> None:
    if not isinstance(contract, dict) or set(contract) != {
        "kind",
        "schema_version",
        "identity",
        "functor_ref",
        "domain",
        "codomain",
        "record_kinds",
        "model_coordinates",
        "source_population",
        "source_packet_relation",
        "source_disposition_unit",
        "postconditions",
        "authority",
        "semantic_acceptance",
        "carrier",
        "runtime",
        "stop_states",
        "stop_reason_codes",
    }:
        raise ValueError(f"invalid semantic compilation contract: {contract_path}")
    required = {
        "kind": "stdo-representation.semantic-compilation-contract",
        "schema_version": 2,
        "identity": COMPILE_TRAVERSAL,
        "functor_ref": F_P,
        "domain": [
            "product_selected_calculus_basis",
            "exact_subject_basis",
            "target_signature",
            "compilation_frame_configuration",
            "exact_source_packet",
            "compile_grant",
            "capability_envelope",
        ],
        "codomain": ["semantic_compilation_proposal"],
        "record_kinds": RECORD_KINDS,
        "model_coordinates": [
            "b",
            "I",
            "O",
            "E",
            "C",
            "L",
            "X",
            "V",
            "T",
            "J",
            "ResolutionSet_M",
        ],
        "source_population": "complete_installed_manifest",
        "source_packet_relation": (
            "full_population_or_exact_projection_with_residuals"
        ),
        "source_disposition_unit": "manifest_member",
        "postconditions": [
            "proposal_implies_total_population_M",
            "proposal_implies_signature_population_cardinalities",
            "T_is_empty_until_exact_transformation_specialization",
            "I_equals_disjoint_union_Local_M_and_External_M",
            "ResolutionSet_M_is_total_unique_over_External_M",
            "every_reference_uses_declared_RefDomain_Sigma",
            "every_source_member_dispositioned",
            "P_B_is_total_bijection_over_Local_M",
            "every_P_B_semantic_address_is_record_congruent",
            "every_generated_source_key_is_exactly_represented",
            "five_proposal_identity_families_are_globally_disjoint",
            "candidate_construction_requires_exact_compiler_provenance_bundle",
            "unmodeled_materiality_implies_X",
        ],
        "authority": "proposal_only",
        "semantic_acceptance": ("external_f_h_v_select_over_unchanged_candidate"),
        "carrier": "excluded",
        "runtime": "excluded",
        "stop_states": [
            "urn:stdo-index:stdo:stop-kind:gap:1",
            "urn:stdo-index:stdo:stop-kind:hold:1",
            "urn:stdo-index:stdo:stop-kind:refusal:1",
        ],
        "stop_reason_codes": [
            "basis_gap",
            "capability_mismatch",
            "insufficient_evidence",
            "output_contract_mismatch",
        ],
    }
    if any(contract.get(field) != value for field, value in required.items()):
        raise ValueError(f"invalid semantic compilation contract: {contract_path}")


def verify_transport_schema(schema: Any, schema_path: Path) -> None:
    if (
        not isinstance(schema, dict)
        or schema.get("type") != "object"
        or schema.get("additionalProperties") is not False
        or schema.get("required") != ["kind", "schema_version", "payload"]
        or set(schema.get("properties", {})) != set(schema["required"])
        or schema["properties"]["schema_version"] != {"type": "integer", "const": 2}
    ):
        raise ValueError(
            f"invalid semantic compilation transport schema: {schema_path}"
        )

    def matches_type(value: Any, declared_type: str) -> bool:
        if declared_type == "null":
            return value is None
        if declared_type == "boolean":
            return isinstance(value, bool)
        if declared_type == "integer":
            return isinstance(value, int) and not isinstance(value, bool)
        if declared_type == "number":
            return isinstance(value, (int, float)) and not isinstance(value, bool)
        if declared_type == "string":
            return isinstance(value, str)
        if declared_type == "array":
            return isinstance(value, list)
        if declared_type == "object":
            return isinstance(value, dict)
        return False

    def walk(value: Any, path: str = "$") -> None:
        if isinstance(value, dict):
            if {"uniqueItems", "minLength"} & set(value):
                raise ValueError(
                    f"unsupported structured-output keyword in schema: {schema_path}"
                )
            declared = value.get("type")
            declared_types = declared if isinstance(declared, list) else [declared]
            if declared is not None and (
                not declared_types
                or not all(isinstance(item, str) for item in declared_types)
            ):
                raise ValueError(
                    f"invalid explicit type at {path} in transport schema: {schema_path}"
                )
            for keyword in ("const", "enum"):
                if keyword not in value:
                    continue
                if declared is None:
                    raise ValueError(
                        f"{keyword} lacks explicit type at {path} in transport schema: "
                        f"{schema_path}"
                    )
                constrained = value[keyword] if keyword == "enum" else [value[keyword]]
                if not isinstance(constrained, list) or not constrained:
                    raise ValueError(
                        f"invalid {keyword} at {path} in transport schema: {schema_path}"
                    )
                if any(
                    not any(
                        matches_type(item, candidate) for candidate in declared_types
                    )
                    for item in constrained
                ):
                    raise ValueError(
                        f"{keyword} disagrees with type at {path} in transport schema: "
                        f"{schema_path}"
                    )
            if value.get("type") == "object" and (
                value.get("additionalProperties") is not False
                or set(value.get("properties", {})) != set(value.get("required", []))
            ):
                raise ValueError(
                    f"open or optional object in transport schema: {schema_path}"
                )
            for key, child in value.items():
                walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")

    walk(schema)


def release_uri(manifest: dict[str, Any]) -> str:
    cut = manifest.get("release", {}).get("cut")
    if not isinstance(cut, str) or not cut:
        raise ValueError("installed manifest lacks release.cut")
    return f"stdo://releases/{cut}/"


def verify_manifest(stdo_root: Path, manifest: dict[str, Any]) -> None:
    if manifest.get("kind") != "stdo.installed-release-manifest":
        raise ValueError("wrong installed manifest kind")
    if manifest.get("schema_version") != 1:
        raise ValueError("wrong installed manifest schema")
    if stdo_root.name != manifest.get("release", {}).get("cut"):
        raise ValueError("installed root and release cut differ")
    standards = manifest.get("standards")
    if not isinstance(standards, dict):
        raise ValueError("installed manifest lacks standards")
    members = standards.get("members")
    if not isinstance(members, list) or standards.get("member_count") != len(members):
        raise ValueError("installed manifest member count mismatch")
    paths = [member.get("path") for member in members if isinstance(member, dict)]
    if len(paths) != len(members) or len(paths) != len(set(paths)):
        raise ValueError("installed manifest member paths are not unique")
    for member in members:
        path = stdo_root / standards["installed_root"] / member["path"]
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != member["sha256"]:
            raise ValueError(f"installed member digest mismatch: {member['path']}")


def markdown_heading_fragments(raw: bytes) -> set[str]:
    fragments: set[str] = set()
    counts: dict[str, int] = {}
    for line in raw.decode("utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match is None:
            continue
        title = re.sub(r"[`*_~]", "", match.group(1)).lower()
        base = "".join(
            character
            for character in title
            if character.isalnum() or character in {"-", "_", " "}
        )
        base = re.sub(r"\s+", "-", base.strip())
        occurrence = counts.get(base, 0)
        counts[base] = occurrence + 1
        fragments.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return fragments


def expected_calculus_basis(
    publication_root: Path, derivation_root: Path
) -> dict[str, Any]:
    publication_manifest_path = publication_root / "manifest.json"
    derivation_manifest_path = derivation_root / "manifest.json"
    publication_manifest = load_json(publication_manifest_path)
    derivation_manifest = load_json(derivation_manifest_path)
    verify_manifest(publication_root, publication_manifest)
    verify_manifest(derivation_root, derivation_manifest)
    publication_release = release_uri(publication_manifest)
    derivation_release = release_uri(derivation_manifest)
    principle_refs = sorted(
        (
            derivation_release + "standards/" + target
            for target in EXPECTED_DERIVATION_TARGETS
        ),
        key=utf16_key,
    )
    return {
        "kind": "stdo.axiomatic-calculus-basis",
        "schema_version": 1,
        "concept_identity": CALCULUS_CONCEPT,
        "derivation_basis": {
            "release_uri": derivation_release,
            "manifest_sha256": digest_file(derivation_manifest_path),
            "principle_refs": principle_refs,
        },
        "publication_basis": {
            "release_uri": publication_release,
            "manifest_sha256": digest_file(publication_manifest_path),
            "member_uri": publication_release + "standards/" + CALCULUS_MEMBER,
            "member_sha256": digest_file(
                publication_root / "standards" / CALCULUS_MEMBER
            ),
        },
    }


def verify_calculus_basis_candidate(
    candidate_path: Path, publication_root: Path, derivation_root: Path
) -> dict[str, Any]:
    candidate = load_json(candidate_path)
    expected = expected_calculus_basis(publication_root, derivation_root)
    if candidate != expected:
        raise ValueError("calculus basis candidate differs from exact installed bytes")
    if (
        candidate["derivation_basis"]["release_uri"]
        == candidate["publication_basis"]["release_uri"]
    ):
        raise ValueError("calculus derivation and publication carriers must differ")
    derivation_release = candidate["derivation_basis"]["release_uri"]
    for principle_ref in candidate["derivation_basis"]["principle_refs"]:
        relative = principle_ref.removeprefix(derivation_release + "standards/")
        member, separator, fragment = relative.partition("#")
        if not separator or not member or not fragment:
            raise ValueError(f"invalid derivation principle reference: {principle_ref}")
        member_path = derivation_root / "standards" / member
        if fragment not in markdown_heading_fragments(member_path.read_bytes()):
            raise ValueError(
                f"unresolved derivation principle reference: {principle_ref}"
            )
    record_bytes = canonical_bytes(candidate)
    record_sha = digest_bytes(record_bytes)
    digest = record_sha.removeprefix("sha256:")
    product_selected_calculus_basis(candidate)
    return {
        "identity": f"urn:stdo:axiomatic-calculus-basis:sha256:{digest}",
        "record": candidate,
        "record_sha256": record_sha,
        "status": "product_selected",
    }


def model_basis_identity(expected_basis: dict[str, Any]) -> str:
    coordinate = {
        "calculus_basis_identity": expected_basis["calculus"]["identity"],
        "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
        "signature_identity": expected_basis["signature"]["identity"],
        "interpretation_contract_identity": expected_basis["interpretation_contract"][
            "identity"
        ],
    }
    digest = digest_bytes(canonical_bytes(coordinate)).removeprefix("sha256:")
    return f"urn:stdo-index:model-basis:sha256:{digest}"


def model_basis_resolution(
    model_basis: str, expected_basis: dict[str, Any]
) -> dict[str, str]:
    digest = model_basis.rsplit(":", 1)[-1]
    return {
        "external_identity": model_basis,
        "reference_domain": "urn:stdo-index:reference-domain:model-basis:1",
        "external_target_kind": "urn:stdo-index:external-target-kind:model-basis:1",
        "resolved_target_identity": model_basis,
        "basis_relation": "urn:stdo-index:basis-relation:exact-model-basis:1",
        "resolution_basis": expected_basis["calculus"]["identity"],
        "evidence_identity": (
            "urn:stdo-index:evidence:model-basis-preimage:sha256:" + digest
        ),
    }


def signature_member_resolution(
    member_identity: str,
    reference_domain: str,
    expected_basis: dict[str, Any],
) -> dict[str, str]:
    signature_sha = expected_basis["signature"]["sha256"].removeprefix("sha256:")
    return {
        "external_identity": member_identity,
        "reference_domain": reference_domain,
        "external_target_kind": SIGNATURE_EXTERNAL_KIND,
        "resolved_target_identity": member_identity,
        "basis_relation": SIGNATURE_BASIS_RELATION,
        "resolution_basis": expected_basis["signature"]["identity"],
        "evidence_identity": (
            "urn:stdo-index:evidence:target-signature:sha256:" + signature_sha
        ),
    }


def what_member_set_identity() -> str:
    members = [
        REPO / "specification" / "INTENT.md",
        REPO / "specification" / "PRODUCT.md",
    ]
    members.extend(sorted((REPO / "specification" / "requirements").glob("REQ-P-*.md")))
    preimage = bytearray()
    for member in members:
        relative = member.relative_to(REPO / "specification").as_posix()
        preimage.extend(relative.encode("utf-8"))
        preimage.extend(b"\0")
        preimage.extend(digest_file(member).removeprefix("sha256:").encode("ascii"))
        preimage.extend(b"\n")
    return digest_bytes(bytes(preimage))


def build_sealed_invocation(
    prompt: str,
    model_basis: str,
    resolution: dict[str, str],
    invocation_coordinates: dict[str, Any],
    expected_basis: dict[str, Any],
    signature: dict[str, Any],
    contract: dict[str, Any],
    frame: dict[str, Any],
    source_manifest: dict[str, Any],
    preflight_records: dict[str, dict[str, Any]] | None = None,
) -> str:
    sealed_parts = [
        prompt,
        "",
        "This is a sealed semantic-computation packet. Use no tools.",
        "Return only the schema-conforming result.",
        "",
        f"candidate_model_basis: {model_basis}",
        "required_model_basis_resolution: "
        + json.dumps(resolution, separators=(",", ":"), ensure_ascii=False),
        "invocation: "
        + json.dumps(invocation_coordinates, separators=(",", ":"), ensure_ascii=False),
        "",
        "<basis>",
        json.dumps(expected_basis, separators=(",", ":"), ensure_ascii=False),
        "</basis>",
        "<signature>",
        json.dumps(signature, separators=(",", ":"), ensure_ascii=False),
        "</signature>",
        "<interpretation_contract>",
        json.dumps(contract, separators=(",", ":"), ensure_ascii=False),
        "</interpretation_contract>",
        "<compilation_frame_configuration>",
        json.dumps(frame, separators=(",", ":"), ensure_ascii=False),
        "</compilation_frame_configuration>",
        "<source_manifest>",
        json.dumps(source_manifest, separators=(",", ":"), ensure_ascii=False),
        "</source_manifest>",
        "<preflight_records>",
        json.dumps(preflight_records or {}, separators=(",", ":"), ensure_ascii=False),
        "</preflight_records>",
        "<subject_sources>",
    ]
    source_root = Path(source_manifest["installed_root"])
    for member in source_manifest["supplied_members"]:
        member_path = source_root / member["path"]
        member_bytes = member_path.read_bytes()
        member_text = member_bytes.decode("utf-8")
        if member_text.encode("utf-8") != member_bytes:
            raise ValueError(f"source member is not exact UTF-8: {member_path}")
        if digest_bytes(member_bytes) != member["sha256"]:
            raise ValueError(f"source member differs from manifest: {member_path}")
        sealed_parts.extend(
            [
                f"<member path={json.dumps(member['path'])} sha256={json.dumps(member['sha256'])}>",
                member_text,
                "</member>",
            ]
        )
    sealed_parts.extend(["</subject_sources>", ""])
    return "\n".join(sealed_parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdo-root", type=Path, default=DEFAULT_STDO)
    parser.add_argument(
        "--derivation-stdo-root", type=Path, default=DEFAULT_DERIVATION_STDO
    )
    parser.add_argument(
        "--calculus-basis-candidate", type=Path, default=DEFAULT_CALCULUS_BASIS
    )
    parser.add_argument(
        "--frame-acceptance", type=Path, default=DEFAULT_FRAME_ACCEPTANCE
    )
    parser.add_argument("--compile-grant", type=Path, default=DEFAULT_COMPILE_GRANT)
    parser.add_argument(
        "--compile-activation", type=Path, default=DEFAULT_COMPILE_ACTIVATION
    )
    parser.add_argument(
        "--capability-envelope", type=Path, default=DEFAULT_CAPABILITY_ENVELOPE
    )
    parser.add_argument("--source-mode", choices=("full", "core"), default="full")
    parser.add_argument("--run-id")
    args = parser.parse_args()

    run_id = args.run_id or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_root = TENANT / "runs" / run_id

    manifest_path = args.stdo_root / "manifest.json"
    manifest = load_json(manifest_path)
    verify_manifest(args.stdo_root, manifest)
    subject_release = release_uri(manifest)
    calculus = verify_calculus_basis_candidate(
        args.calculus_basis_candidate,
        args.stdo_root,
        args.derivation_stdo_root,
    )

    signature_path = TENANT / "profile" / "stdo-signature.json"
    contract_path = TENANT / "contract" / "v_compile.json"
    prompt_path = TENANT / "prompt" / "v_compile.txt"
    output_schema_path = TENANT / "schema" / "candidate.schema.json"
    frame_path = TENANT / "profile" / "stdo-core-frame.json"
    signature = load_json(signature_path)
    contract = load_json(contract_path)
    frame = load_json(frame_path)
    schema = load_json(output_schema_path)
    verify_compilation_contract(contract, contract_path)
    verify_frame_configuration(frame, frame_path)
    verify_transport_schema(schema, output_schema_path)

    subject = {
        "release_uri": subject_release,
        "installed_manifest_sha256": digest_file(manifest_path),
        "standards_member_set_sha256": (
            f"sha256:{manifest['standards']['member_set_sha256']}"
        ),
        "member_count": manifest["standards"]["member_count"],
    }
    signature_ref = {
        "identity": signature["identity"],
        "sha256": digest_file(signature_path),
    }
    contract_ref = {
        "identity": contract["identity"],
        "sha256": digest_file(contract_path),
    }
    frame_ref = {
        "configuration_identity": frame["identity"],
        "configuration_sha256": digest_file(frame_path),
        "frame_basis_identity": frame["frame_basis_identity"],
        "frame_basis_sha256": frame["frame_basis_sha256"],
        "selected_frame_refs": frame["selected_frame_refs"],
        "status": frame["status"],
    }
    supplied_members = (
        list(manifest["standards"]["members"])
        if args.source_mode == "full"
        else [
            row
            for row in manifest["standards"]["members"]
            if row["path"] == "authority_compressions/stdo_compressed.md"
        ]
    )
    packet_preimage = {
        "release_uri": subject["release_uri"],
        "members": [
            {"path": row["path"], "sha256": f"sha256:{row['sha256']}"}
            for row in supplied_members
        ],
    }
    packet_sha = digest_bytes(canonical_bytes(packet_preimage))
    source_packet_ref = {
        "identity": (
            "urn:stdo-index:source-packet:sha256:" + packet_sha.removeprefix("sha256:")
        ),
        "sha256": packet_sha,
    }
    basis = {
        "kind": "stdo-index.prototype-basis",
        "schema_version": 3,
        "calculus": calculus,
        "subject": subject,
        "signature": signature_ref,
        "interpretation_contract": contract_ref,
        "frame": frame_ref,
        "source_packet": source_packet_ref,
        "subject_basis_identity": SUBJECT_BASIS_IDENTITY,
        "what_member_set_identity": what_member_set_identity(),
        "compiler_prompt_sha256": digest_file(prompt_path),
        "transport_schema_sha256": digest_file(output_schema_path),
    }
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
    model_basis = model_basis_identity(expected_basis)
    resolution = model_basis_resolution(model_basis, expected_basis)

    source_manifest = {
        "kind": "stdo-index.source-manifest",
        "schema_version": 2,
        "release_uri": subject["release_uri"],
        "installed_root": str(args.stdo_root / manifest["standards"]["installed_root"]),
        "installed_manifest_sha256": subject["installed_manifest_sha256"],
        "standards_member_set_sha256": subject["standards_member_set_sha256"],
        "members": [
            {"path": row["path"], "sha256": f"sha256:{row['sha256']}"}
            for row in manifest["standards"]["members"]
        ],
        "supplied_members": packet_preimage["members"],
    }

    preflight, preflight_bindings, preflight_records = semantic_compile_preflight(
        frame_acceptance_path=args.frame_acceptance,
        compile_grant_path=args.compile_grant,
        compile_activation_path=args.compile_activation,
        capability_envelope_path=args.capability_envelope,
        overlay=load_json(OVERLAY_PATH),
        frame=frame,
        calculus=calculus,
        signature_ref=signature_ref,
        contract_ref=contract_ref,
        source_packet_ref=source_packet_ref,
        prompt_sha256=digest_file(prompt_path),
        schema_sha256=digest_file(output_schema_path),
    )
    if preflight["decision"] != "ready":
        print(canonical_bytes(preflight).decode("utf-8"))
        raise SystemExit(2)

    basis["preflight"] = preflight_bindings
    run_root.mkdir(parents=True, exist_ok=False)
    preflight_root = run_root / "preflight"
    preflight_root.mkdir()
    for name, record in preflight_records.items():
        (preflight_root / f"{name}.json").write_bytes(canonical_bytes(record))

    write_canonical(run_root / "basis.json", basis)
    write_canonical(run_root / "source-manifest.json", source_manifest)

    invocation_coordinates = {
        "topology": "single_invocation",
        "traversal_ref": contract["identity"],
        "functor_ref": contract["functor_ref"],
        "actor_identity": preflight_records["compile_activation"]["actor_identity"],
        "host_identity": HOST_IDENTITY,
        "model_identity": MODEL_IDENTITY,
        "model_configuration_sha256": model_configuration_sha256(),
        "authority_identity": preflight_records["compile_activation"][
            "authority_identity"
        ],
        "grant_identity": preflight_records["compile_activation"]["grant_identity"],
        "grant_sha256": preflight_records["compile_activation"]["grant_sha256"],
        "grant_scope": preflight_records["compile_activation"]["grant_scope"],
        "activated_at": preflight_records["compile_activation"]["activated_at"],
        "frame_acceptance_identity": preflight_bindings["frame_acceptance"]["identity"],
        "frame_acceptance_sha256": preflight_bindings["frame_acceptance"]["sha256"],
        "compile_activation_identity": preflight_bindings["compile_activation"][
            "identity"
        ],
        "compile_activation_sha256": preflight_bindings["compile_activation"]["sha256"],
        "capability_envelope_ref": preflight_bindings["capability_envelope"][
            "identity"
        ],
        "capability_envelope_sha256": preflight_bindings["capability_envelope"][
            "sha256"
        ],
        "context_budget_tokens": CONTEXT_BUDGET_TOKENS,
    }
    prompt = prompt_path.read_text(encoding="utf-8").strip()
    invocation = "\n".join(
        [
            prompt,
            "",
            "Exact input coordinates:",
            f"- calculus source: {args.stdo_root / 'standards' / CALCULUS_MEMBER}",
            f"- subject root: {source_manifest['installed_root']}",
            f"- source manifest: {run_root / 'source-manifest.json'}",
            f"- selected signature: {signature_path}",
            f"- interpretation contract: {contract_path}",
            f"- candidate model basis: {model_basis}",
            "",
            "Use these exact invocation coordinates:",
            json.dumps(invocation_coordinates, indent=2, ensure_ascii=False),
            "",
            "Use this exact basis object:",
            json.dumps(expected_basis, indent=2, ensure_ascii=False),
            "",
            "Use this exact required model-basis resolution:",
            json.dumps(resolution, indent=2, ensure_ascii=False),
            "",
        ]
    )
    (run_root / "invocation.txt").write_text(invocation, encoding="utf-8")

    (run_root / "sealed-invocation.txt").write_text(
        build_sealed_invocation(
            prompt,
            model_basis,
            resolution,
            invocation_coordinates,
            expected_basis,
            signature,
            contract,
            frame,
            source_manifest,
            preflight_records,
        ),
        encoding="utf-8",
    )

    receipt = {
        "kind": "stdo-index.prototype-acquisition",
        "schema_version": 3,
        "run_id": run_id,
        "basis_sha256": digest_file(run_root / "basis.json"),
        "source_manifest_sha256": digest_file(run_root / "source-manifest.json"),
        "invocation_sha256": digest_file(run_root / "invocation.txt"),
        "sealed_invocation_sha256": digest_file(run_root / "sealed-invocation.txt"),
        "calculus_basis_sha256": calculus["record_sha256"],
        "calculus_basis_identity": calculus["identity"],
        "preflight": preflight_bindings,
        "model_basis": model_basis,
        "status": "inputs_acquired",
    }
    write_canonical(run_root / "acquisition.json", receipt)
    provenance_bundle = build_compiler_provenance_bundle(run_root)
    (run_root / "compiler-provenance-bundle.json").write_bytes(
        canonical_bytes(provenance_bundle)
    )
    print(run_root)


if __name__ == "__main__":
    main()
