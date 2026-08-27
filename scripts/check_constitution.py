#!/usr/bin/env python3
"""Check decidable STDO Representation source-project invariants.

The checker proves only the structural and declared-boundary conditions named in
its output. It does not assess semantic compression adequacy, accept a reference
frame or representation profile, or judge an LLM response.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, NoReturn


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specification"

REQUIREMENT_STATUSES = {"Active", "Deferred", "Superseded", "Orphaned"}
REQUIREMENT_CATEGORIES = {
    "Capability",
    "Constraint / Guarantee",
    "Governance",
    "Verification",
}
TICKET_FIELDS = {
    "id",
    "title",
    "type",
    "ticket_category",
    "status",
    "goal",
    "change_intent",
    "change_class",
    "re_entry_point",
    "triaged_at",
    "created_at",
    "updated_at",
}
TICKET_TYPES = {"feature", "bug", "spike", "chore"}
TICKET_CATEGORIES = {"ordinary", "implementation_migration"}
CHANGE_CLASSES = {
    "goal_reprice",
    "intent_reprice",
    "product_reprice",
    "requirement_reprice",
    "design_reframe",
    "realization_refactor",
}
LANE_STATUS = {
    "backlog": "backlog",
    "active": "active",
    "completed": "completed",
}
EXPECTED_REQUIREMENTS = {
    "REQ-P-BASIS-AND-IDENTITY.md",
    "REQ-P-COMPRESSION-VERIFICATION.md",
    "REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
    "REQ-P-FP-CONSUMPTION.md",
    "REQ-P-REPRESENTATION-ALGEBRA.md",
    "REQ-P-SELECTION-AND-ACCEPTANCE.md",
}
TRAVERSAL_IDENTITIES = {
    "F_D": "urn:stdo:concept:graph-native-odd:f-d",
    "F_P": "urn:stdo:concept:graph-native-odd:f-p",
    "F_H": "urn:stdo:concept:graph-native-odd:f-h",
}
ROLE_IDENTITIES = {
    "Executive": (
        "stdo://releases/v2.4.3-rc.3/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#executive"
    ),
    "Worker": (
        "stdo://releases/v2.4.3-rc.3/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#worker"
    ),
    "Reviewer": (
        "stdo://releases/v2.4.3-rc.3/standards/"
        "STDO_REFERENCE_FRAME_BASELINE.md#reviewer"
    ),
}
FRAME_BASIS_IDENTITY = "urn:stdo-representation:reference-frame-basis:source-project:3"
GTL_PROFILE_IDENTITY = "urn:stdo-representation:gtl-profile:stdo-gtl:0.4.0"
FRAME_AUTHORITIES = {
    "./specification/GOALS.md",
    "./specification/PRODUCT.md#product-authority",
    "./specification/requirements/REQ-P-BASIS-AND-IDENTITY.md",
    "./specification/requirements/REQ-P-COMPRESSION-VERIFICATION.md",
    "./specification/requirements/REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
    "./specification/requirements/REQ-P-FP-CONSUMPTION.md",
    "./specification/requirements/REQ-P-REPRESENTATION-ALGEBRA.md",
    "./specification/requirements/REQ-P-SELECTION-AND-ACCEPTANCE.md",
}
FUNCTION_BINDING_URI = (
    "./specification/PRODUCT.md#fundamental-traversal-function-binding"
)
FUNCTION_BINDING_AUTHORITY = [
    "stdo://releases/v2.4.3-rc.3/standards/ODD_METHOD.md#probabilistic-compute",
    FUNCTION_BINDING_URI,
]
ROLE_BINDING_URI = (
    "./specification/requirements/"
    "REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md#cross-context-role-import"
)
EXPECTED_DISAMBIGUATIONS = {
    term: {
        "uri": FUNCTION_BINDING_URI,
        "term": term,
        "context": "urn:stdo-representation:bounded-context:product",
        "disambiguates": [identity],
        "resolves_to": identity,
        "authority": FUNCTION_BINDING_AUTHORITY,
        "basis": ["#/constitution/stdo/basis"],
        "applies_to": ["urn:stdo:product-definition:stdo-representation"],
    }
    for term, identity in TRAVERSAL_IDENTITIES.items()
}
EXPECTED_DISAMBIGUATIONS.update(
    {
        term: {
            "uri": ROLE_BINDING_URI,
            "term": term,
            "context": "urn:stdo-representation:bounded-context:product",
            "disambiguates": [identity],
            "resolves_to": identity,
            "authority": [identity, ROLE_BINDING_URI],
            "basis": ["#/constitution/stdo/basis"],
            "applies_to": ["urn:stdo:product-definition:stdo-representation"],
        }
        for term, identity in ROLE_IDENTITIES.items()
    }
)
GTL_CARRIER_COORDINATE = {
    "authority_inventory_count": 33,
    "authority_root": "specification/requirements/gtl/",
    "authority_tree_sha1": "21a44b1941a1055d6abd973937e65b83e359de1b",
    "commit_sha1": "8d7f965a3fae7d1acea6a9db298798480fd4cc2f",
    "repository": "https://github.com/foolishimp/abiogenesis.git",
}


class CheckFailure(RuntimeError):
    """One explicit source-project invariant failed."""


def fail(message: str) -> NoReturn:
    raise CheckFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_ascii_coordinate_bytes(value: object) -> bytes:
    """Serialize the closed ASCII GTL basis coordinate in its RFC 8785 form.

    This helper is intentionally not advertised as a general JCS implementation.
    The governed coordinate contains only ASCII object names/strings and one
    non-negative integer, for which this serialization is the exact JCS result.
    """

    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def reject_duplicate_object_names(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


def load_json_unique(path: Path) -> Any:
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_object_names,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"cannot read unique-name JSON {path}: {exc}")


def parse_ticket_metadata(text: str, source: str) -> dict[str, str]:
    """Parse only the contiguous metadata header immediately below the H1."""

    lines = text.splitlines()
    require(bool(lines) and lines[0].startswith("# "), f"missing ticket H1: {source}")
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    values: dict[str, str] = {}
    metadata_pattern = re.compile(r"([a-z][a-z0-9_]*): (.+)")
    while index < len(lines) and lines[index].strip():
        match = metadata_pattern.fullmatch(lines[index])
        require(
            match is not None, f"invalid ticket metadata line {index + 1}: {source}"
        )
        key, value = match.groups()
        require(key not in values, f"duplicate ticket metadata key {key}: {source}")
        values[key] = value
        index += 1

    require(bool(values), f"missing ticket metadata header: {source}")
    return values


def one_metadata_value(text: str, key: str, source: Path) -> str:
    matches = re.findall(rf"^{re.escape(key)}: (.+)$", text, re.MULTILINE)
    require(len(matches) == 1, f"expected one {key} metadata value: {source}")
    return matches[0]


def active_requirement_members(spec_root: Path = SPEC) -> list[Path]:
    members: list[Path] = []
    seen_ids: dict[str, Path] = {}
    requirement_paths = sorted((spec_root / "requirements").glob("REQ-P-*.md"))
    require(
        {path.name for path in requirement_paths} == EXPECTED_REQUIREMENTS,
        "active requirement file inventory differs from the closed expected set",
    )

    for path in requirement_paths:
        text = path.read_text(encoding="utf-8")
        status = one_metadata_value(text, "Status", path)
        category = one_metadata_value(text, "Category", path)
        require(
            status in REQUIREMENT_STATUSES,
            f"invalid requirement status {status}: {path}",
        )
        require(
            category in REQUIREMENT_CATEGORIES,
            f"invalid requirement category {category}: {path}",
        )

        ids = re.findall(r"\*\*(REQ-P-[A-Z]+-\d{3})\*\*", text)
        require(bool(ids), f"no requirement identities: {path}")
        require(len(ids) == len(set(ids)), f"duplicate requirement identity in {path}")
        for requirement_id in ids:
            require(
                requirement_id not in seen_ids,
                f"duplicate requirement identity {requirement_id}: {path} and "
                f"{seen_ids.get(requirement_id)}",
            )
            seen_ids[requirement_id] = path
        if status == "Active":
            members.append(path)
    return members


def what_member_set_identity(
    requirements: list[Path], spec_root: Path = SPEC
) -> tuple[str, list[str]]:
    members = [spec_root / "INTENT.md", spec_root / "PRODUCT.md", *requirements]
    ordered = members[:2] + sorted(
        members[2:], key=lambda path: path.relative_to(spec_root).as_posix()
    )
    identity_input = bytearray()
    paths: list[str] = []
    for path in ordered:
        require(path.is_file(), f"missing WHAT member: {path}")
        relative = path.relative_to(spec_root).as_posix()
        paths.append(relative)
        digest = sha256_bytes(path.read_bytes())
        identity_input.extend(relative.encode("utf-8"))
        identity_input.append(0)
        identity_input.extend(digest.encode("ascii"))
        identity_input.extend(b"\n")
    return sha256_bytes(bytes(identity_input)), paths


def validate_ticket_metadata(values: dict[str, str], path: Path) -> None:
    missing = TICKET_FIELDS - values.keys()
    require(not missing, f"missing ticket metadata {sorted(missing)}: {path}")
    require(values["type"] in TICKET_TYPES, f"invalid ticket type: {path}")
    require(
        values["ticket_category"] in TICKET_CATEGORIES,
        f"invalid ticket category: {path}",
    )
    require(
        values["change_class"] in CHANGE_CLASSES,
        f"invalid ticket change class: {path}",
    )
    lane = path.parent.name
    require(lane in LANE_STATUS, f"invalid ticket lane {lane}: {path}")
    require(
        values["status"] == LANE_STATUS[lane],
        f"ticket status/lane mismatch: {path}",
    )


def check_tickets(root: Path = ROOT) -> tuple[int, dict[str, dict[str, str]]]:
    count = 0
    records: dict[str, dict[str, str]] = {}
    ticket_root = root / ".ai-workspace" / "tickets"
    for path in sorted(ticket_root.glob("*/*.md")):
        if path.name == "README.md":
            continue
        values = parse_ticket_metadata(path.read_text(encoding="utf-8"), str(path))
        validate_ticket_metadata(values, path)
        require(values["id"] not in records, f"duplicate ticket id {values['id']}")
        records[values["id"]] = values
        count += 1
    return count, records


def require_text(text: str, needle: str, source: Path) -> None:
    require(needle in text, f"missing required declaration {needle!r}: {source}")


def check_definition(root: Path = ROOT) -> dict[str, Any]:
    definition_path = root / "stdo_representation.json"
    definition = load_json_unique(definition_path)
    require(isinstance(definition, dict), "Product Definition root is not an object")

    frame_bases = definition.get("reference_frame_bases")
    require(
        isinstance(frame_bases, list) and len(frame_bases) == 1,
        "expected one frame basis",
    )
    frame_basis = frame_bases[0]
    require(isinstance(frame_basis, dict), "frame basis entry is not an object")
    require(
        frame_basis.get("uri")
        == "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
        "unexpected Project Reference-Frame Basis URI",
    )
    frame_authorities = frame_basis.get("authority")
    require(
        isinstance(frame_authorities, list), "frame basis authority is not an array"
    )
    require(
        len(frame_authorities) == len(FRAME_AUTHORITIES)
        and set(frame_authorities) == FRAME_AUTHORITIES,
        "Project Reference-Frame Basis authority set is incomplete or unexpected",
    )

    local_constitution = definition.get("local_constitution")
    require(isinstance(local_constitution, dict), "local constitution is not an object")
    disambiguations = local_constitution.get("disambiguations")
    require(isinstance(disambiguations, list), "missing local disambiguations")
    require(
        len(disambiguations) == len(EXPECTED_DISAMBIGUATIONS),
        "unexpected semantic disambiguation count",
    )
    observed: dict[str, dict[str, Any]] = {}
    for item in disambiguations:
        require(isinstance(item, dict), "semantic resolution is not an object")
        term = item.get("term")
        require(isinstance(term, str), "invalid semantic resolution term")
        require(term not in observed, f"duplicate semantic resolution for {term}")
        observed[term] = item
    require(
        observed == EXPECTED_DISAMBIGUATIONS,
        "function and engagement-role disambiguation records are not exact",
    )
    return definition


def main() -> None:
    definition = check_definition()
    required_files = [
        SPEC / "INTENT.md",
        SPEC / "PRODUCT.md",
        SPEC / "REFERENCE_FRAME_BASIS.md",
        *(SPEC / "requirements" / name for name in sorted(EXPECTED_REQUIREMENTS)),
        ROOT / "build_tenants" / "gtl" / "design" / "GTL_REPRESENTATION_PROFILE.md",
        ROOT / "scripts" / "test_check_constitution.py",
    ]
    for path in required_files:
        require(path.is_file(), f"missing required file: {path}")

    retired = SPEC / "requirements" / "REQ-P-PROJECTION-AND-CONFORMANCE.md"
    require(
        not retired.exists(),
        "retired deterministic-assessment requirement remains live",
    )

    product_path = SPEC / "PRODUCT.md"
    intent_path = SPEC / "INTENT.md"
    algebra_path = SPEC / "requirements" / "REQ-P-REPRESENTATION-ALGEBRA.md"
    context_path = SPEC / "requirements" / "REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md"
    fp_path = SPEC / "requirements" / "REQ-P-FP-CONSUMPTION.md"
    selection_path = SPEC / "requirements" / "REQ-P-SELECTION-AND-ACCEPTANCE.md"
    frame_path = SPEC / "REFERENCE_FRAME_BASIS.md"
    profile_path = (
        ROOT / "build_tenants" / "gtl" / "design" / "GTL_REPRESENTATION_PROFILE.md"
    )

    product = product_path.read_text(encoding="utf-8")
    intent = intent_path.read_text(encoding="utf-8")
    algebra = algebra_path.read_text(encoding="utf-8")
    context_contract = context_path.read_text(encoding="utf-8")
    fp_contract = fp_path.read_text(encoding="utf-8")
    selection_contract = selection_path.read_text(encoding="utf-8")
    frame_basis = frame_path.read_text(encoding="utf-8")
    profile = profile_path.read_text(encoding="utf-8")

    require_text(product, "F_P(P_B, W, I, F, K) -> J", product_path)
    require_text(intent, "Outcome-Driven Development", intent_path)
    require_text(algebra, "P_B = (B, I_B, V_B, E_B, C_B)", algebra_path)
    require_text(algebra, "## Reference-kind law", algebra_path)
    require_text(algebra, "Every record contains exactly", algebra_path)
    require_text(context_contract, "ExecutiveContextAssignment = {", context_path)
    require_text(context_contract, "ContextProjectionManifest = {", context_path)
    require_text(
        context_contract,
        "P_A = least_closure(P_B, Z(A), L_context)",
        context_path,
    )
    require_text(
        context_contract,
        "STDO_REFERENCE_FRAME_BASELINE.md#executive",
        context_path,
    )
    require_text(
        context_contract,
        "STDO_REFERENCE_FRAME_BASELINE.md#worker",
        context_path,
    )
    require_text(
        context_contract,
        "STDO_REFERENCE_FRAME_BASELINE.md#reviewer",
        context_path,
    )
    require_text(selection_contract, "GeneratedSourceKeyBinding = {", selection_path)
    require_text(product, "admitting_authority_refs", product_path)
    require_text(product, "ReleaseRecord = {", product_path)
    require_text(frame_basis, "Status: acceptance-controlled", frame_path)
    require_text(profile, "STDO.gtl 0.4.0", profile_path)
    require_text(profile, "Status: acceptance-controlled candidate", profile_path)
    require_text(profile, "A Rule has no `.id`", profile_path)
    require_text(profile, "canonical_program_bytes = JCS(Module) + LF", profile_path)
    require("Assessment Disposition" not in product, "assessment Product term returned")
    require(
        "REQ-P-CONF"
        not in "\n".join(path.read_text(encoding="utf-8") for path in required_files),
        "retired assessment requirement identity returned",
    )

    for identity in TRAVERSAL_IDENTITIES.values():
        require_text(product, identity, product_path)
        require_text(fp_contract, identity, fp_path)

    carrier_digest = sha256_bytes(
        canonical_ascii_coordinate_bytes(GTL_CARRIER_COORDINATE)
    )
    require_text(profile, carrier_digest, profile_path)

    requirements = active_requirement_members()
    what_digest, what_members = what_member_set_identity(requirements)
    ticket_count, tickets = check_tickets()
    require(
        "T-002" in tickets and "T-003" in tickets,
        "required T-002/T-003 records missing",
    )
    require(tickets["T-002"]["status"] == "active", "T-002 must remain active")
    require(tickets["T-003"]["status"] == "backlog", "T-003 must remain backlog")

    what_identity = f"sha256:{what_digest}"
    frame_digest = f"sha256:{sha256_bytes(frame_path.read_bytes())}"
    profile_digest = f"sha256:{sha256_bytes(profile_path.read_bytes())}"
    expected_ticket_bindings = {
        "T-002": {
            "candidate_what_member_set_identity": what_identity,
            "candidate_frame_basis_identity": FRAME_BASIS_IDENTITY,
            "candidate_frame_basis_sha256": frame_digest,
            "candidate_gtl_profile_identity": GTL_PROFILE_IDENTITY,
            "candidate_gtl_profile_sha256": profile_digest,
        },
        "T-003": {
            "required_what_member_set_identity": what_identity,
            "required_frame_basis_identity": FRAME_BASIS_IDENTITY,
            "required_frame_basis_sha256": frame_digest,
            "required_profile_identity": GTL_PROFILE_IDENTITY,
            "required_profile_sha256": profile_digest,
        },
    }
    for ticket_id, expected in expected_ticket_bindings.items():
        for key, value in expected.items():
            require(
                tickets[ticket_id].get(key) == value,
                f"{ticket_id} {key} does not bind the exact current candidate",
            )

    print(
        json.dumps(
            {
                "check_scope": (
                    "source-project structure, metadata, identity inputs, and "
                    "declared traversal boundaries; semantic adequacy and human "
                    "acceptance are not evaluated"
                ),
                "definition_id": definition["product"]["definition_id"],
                "requirement_members": len(requirements),
                "ticket_records": ticket_count,
                "what_member_set_identity": what_identity,
                "what_members": what_members,
                "gtl_carrier_basis_identity": (
                    "urn:stdo-representation:carrier-basis:gtl:sha256:" + carrier_digest
                ),
                "frame_basis_sha256": frame_digest,
                "gtl_profile_sha256": profile_digest,
                "frame_basis_status": "candidate carrier; acceptance not evaluated",
                "gtl_profile_status": "candidate carrier; acceptance not evaluated",
                "context_projection_contract": "Executive, Worker, Reviewer",
                "structural_checks_pass": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except CheckFailure as exc:
        print(f"constitution check failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
