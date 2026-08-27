#!/usr/bin/env python3
"""Check decidable STDO Representation source-project invariants.

This checker validates structure, metadata, identity inputs, and the explicit
F_P/F_D boundary. It does not assess semantic adequacy or an LLM response.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def metadata(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in text.splitlines():
        if ": " not in line:
            continue
        key, value = line.split(": ", 1)
        if re.fullmatch(r"[a-z_]+", key):
            values[key] = value
    return values


def active_requirement_members() -> list[Path]:
    members: list[Path] = []
    seen_ids: dict[str, Path] = {}
    for path in sorted((SPEC / "requirements").glob("REQ-P-*.md")):
        text = path.read_text(encoding="utf-8")
        status_match = re.search(r"^Status: (.+)$", text, re.MULTILINE)
        category_match = re.search(r"^Category: (.+)$", text, re.MULTILINE)
        assert status_match, f"missing requirement Status: {path}"
        assert category_match, f"missing requirement Category: {path}"
        status = status_match.group(1)
        category = category_match.group(1)
        assert status in REQUIREMENT_STATUSES, (path, status)
        assert category in REQUIREMENT_CATEGORIES, (path, category)

        ids = re.findall(r"\*\*(REQ-P-[A-Z]+-\d{3})\*\*", text)
        assert ids, f"no requirement identities: {path}"
        for requirement_id in ids:
            assert requirement_id not in seen_ids, (
                requirement_id,
                path,
                seen_ids[requirement_id],
            )
            seen_ids[requirement_id] = path
        if status == "Active":
            members.append(path)
    return members


def what_member_set_identity(requirements: list[Path]) -> tuple[str, list[str]]:
    members = [SPEC / "INTENT.md", SPEC / "PRODUCT.md", *requirements]
    ordered = members[:2] + sorted(members[2:], key=lambda p: p.relative_to(SPEC).as_posix())
    identity_input = bytearray()
    paths: list[str] = []
    for path in ordered:
        relative = path.relative_to(SPEC).as_posix()
        paths.append(relative)
        digest = sha256_bytes(path.read_bytes())
        identity_input.extend(relative.encode("utf-8"))
        identity_input.append(0)
        identity_input.extend(digest.encode("ascii"))
        identity_input.extend(b"\n")
    return sha256_bytes(bytes(identity_input)), paths


def check_tickets() -> int:
    count = 0
    ticket_root = ROOT / ".ai-workspace" / "tickets"
    for path in sorted(ticket_root.glob("*/*.md")):
        if path.name == "README.md":
            continue
        values = metadata(path.read_text(encoding="utf-8"))
        missing = TICKET_FIELDS - values.keys()
        assert not missing, (path, sorted(missing))
        assert values["type"] in TICKET_TYPES, (path, values["type"])
        assert values["ticket_category"] in TICKET_CATEGORIES, (
            path,
            values["ticket_category"],
        )
        assert values["change_class"] in CHANGE_CLASSES, (
            path,
            values["change_class"],
        )
        lane = path.parent.name
        assert lane in LANE_STATUS, (path, lane)
        assert values["status"] == LANE_STATUS[lane], (
            path,
            values["status"],
            lane,
        )
        count += 1
    return count


def main() -> None:
    definition = json.loads((ROOT / "stdo_representation.json").read_text(encoding="utf-8"))
    frame_basis = definition["reference_frame_bases"]
    assert len(frame_basis) == 1
    assert frame_basis[0]["uri"] == (
        "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis"
    )

    required_files = [
        SPEC / "INTENT.md",
        SPEC / "PRODUCT.md",
        SPEC / "REFERENCE_FRAME_BASIS.md",
        SPEC / "requirements" / "REQ-P-BASIS-AND-IDENTITY.md",
        SPEC / "requirements" / "REQ-P-REPRESENTATION-ALGEBRA.md",
        SPEC / "requirements" / "REQ-P-FP-CONSUMPTION.md",
        SPEC / "requirements" / "REQ-P-COMPRESSION-VERIFICATION.md",
        ROOT / "build_tenants" / "gtl" / "design" / "GTL_REPRESENTATION_PROFILE.md",
    ]
    for path in required_files:
        assert path.is_file(), f"missing required file: {path}"

    assert not (
        SPEC / "requirements" / "REQ-P-PROJECTION-AND-CONFORMANCE.md"
    ).exists(), "retired deterministic-assessment requirement remains live"

    product = (SPEC / "PRODUCT.md").read_text(encoding="utf-8")
    intent = (SPEC / "INTENT.md").read_text(encoding="utf-8")
    algebra = (
        SPEC / "requirements" / "REQ-P-REPRESENTATION-ALGEBRA.md"
    ).read_text(encoding="utf-8")
    assert "F_P(P_B, W, I, F, K) -> J" in product
    assert "probabilistic LLM (`F_P`) consumption" in intent
    assert "P_B = (B, I_B, V_B, E_B, C_B)" in algebra
    assert "Assessment Disposition" not in product
    assert "REQ-P-CONF" not in "\n".join(
        path.read_text(encoding="utf-8") for path in required_files
    )

    requirements = active_requirement_members()
    what_digest, what_members = what_member_set_identity(requirements)
    ticket_count = check_tickets()
    profile = ROOT / "build_tenants" / "gtl" / "design" / "GTL_REPRESENTATION_PROFILE.md"

    print(
        json.dumps(
            {
                "definition_id": definition["product"]["definition_id"],
                "requirement_members": len(requirements),
                "ticket_records": ticket_count,
                "what_member_set_identity": f"sha256:{what_digest}",
                "what_members": what_members,
                "gtl_profile_sha256": f"sha256:{sha256_bytes(profile.read_bytes())}",
                "valid": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
