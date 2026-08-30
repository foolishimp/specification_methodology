#!/usr/bin/env python3
"""Focused constitutional checks for the thin STDO Representation Product."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STDO_BASIS = "stdo://releases/v2.5.0-rc.1/"
STDO_MANIFEST = "3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338"
STDO_MEMBER_SET = "87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5"
CALCULUS_REF = "stdo://releases/v2.5.0-rc.1/standards/AXIOMATIC_CALCULUS.md"
AXIOM_TAG_OBJECT = "e7afc8a42a7123aebe91cb7582cb037b1aae612d"
AXIOM_COMMIT = "dc3e00998da36dae6ac7b76b340431a85096c83c"
AXIOM_TREE = "8c9ad5f5e99a60c18fb8c1802471753afb226272"
FRAME_URI = "urn:stdo-representation:reference-frame-basis:source-project:11"
FRAME_PATH = Path("specification/REFERENCE_FRAME_BASIS.md")
FRAME_SHA256 = "09db079c16758db8765452bd05f6b5de3ce831974e80fb9ea59ef876fab50ed9"
FRAME_DECISION_PATH = Path(
    ".ai-workspace/decisions/20260831T005313_frame_basis_rev11_acceptance.json"
)
FRAME_DECISION_SHA256 = (
    "371d0d031fa518a7c5a92a97c658e5c1bc5765b13d1c30f0d7938671c054b89e"
)

PROGRAM_PATH = Path(
    "build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/"
    "axiomatic-program.json"
)
MAP_PATH = PROGRAM_PATH.with_name("logical-constraint-map.json")
SKILL_ROOT = Path("skills/stdo-representation")
PRODUCT_FILES = (
    PROGRAM_PATH,
    MAP_PATH,
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "agents/openai.yaml",
    SKILL_ROOT / "references/codex.md",
    SKILL_ROOT / "references/claude.md",
)
PRODUCT_LINKS = {
    Path(".agents/skills/stdo-representation"): "../../skills/stdo-representation",
    Path(".claude/skills/stdo-representation"): "../../skills/stdo-representation",
}
ACTIVE_REQUIREMENTS = {
    "README.md",
    "REQ-P-BASIS-AND-IDENTITY.md",
    "REQ-P-CANDIDATE-VALIDATION.md",
    "REQ-P-DOGFOOD-VERIFICATION.md",
    "REQ-P-NATIVE-FRAME-USE.md",
    "REQ-P-STDO-AUTHORING-MAP.md",
}
HISTORICAL_ROOTS = (
    Path("build_tenants/semantic_compile"),
    Path("build_tenants/gtl"),
    Path("build_tenants/json_schema"),
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_overlay(overlay: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    basis = overlay.get("constitution", {}).get("stdo", {}).get("basis", {})
    if basis.get("uri") != STDO_BASIS:
        failures.append("Product Definition selects the wrong STDO basis")
    if basis.get("manifest_sha256") != STDO_MANIFEST:
        failures.append("Product Definition selects the wrong STDO manifest")
    if overlay.get("constitution", {}).get("additional_authorities") != []:
        failures.append("unexpected additional constitutional authority")

    expected_entrypoints = [
        "standards/authority_compressions/stdo_bootstrap.md",
        "standards/SPEC_METHOD.md",
        "standards/REFERENCE_FRAME_METHOD.md",
        "standards/STDO_REFERENCE_FRAME_BASELINE.md",
        "standards/AXIOMATIC_CALCULUS.md",
        "standards/IDENTITY_METHOD.md",
        "standards/RELEASE_METHOD.md",
    ]
    actual_entrypoints = [
        row.get("uri") for row in overlay.get("constitution", {}).get("entrypoints", [])
    ]
    if actual_entrypoints != expected_entrypoints:
        failures.append("constitutional entrypoints do not match the thin Product")

    expected_frame_bases = [
        {
            "uri": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
            "authority": [
                "./specification/PRODUCT.md#product-disposition-authority",
                "./.ai-workspace/decisions/"
                "20260831T005313_frame_basis_rev11_acceptance.json",
            ],
            "applies_to": ["urn:stdo:product-definition:stdo-representation"],
        }
    ]
    if overlay.get("reference_frame_bases") != expected_frame_bases:
        failures.append("accepted project frame basis binding is not exact")
    if overlay.get("composition") != []:
        failures.append("thin Product Definition unexpectedly selects composition")

    how = overlay.get("how", {})
    if how.get("common") != []:
        failures.append("thin Product unexpectedly selects common implementation")
    tenants = how.get("build_tenants")
    if not isinstance(tenants, list) or len(tenants) != 1:
        failures.append("thin Product must select exactly one build tenant")
    elif tenants[0] != {
        "id": "urn:stdo-representation:build-tenant:axiom-indexer",
        "root": "./build_tenants/axiom_indexer/",
        "design": ["./build_tenants/axiom_indexer/README.md"],
        "implementation": ["./build_tenants/axiom_indexer/representation/"],
    }:
        failures.append("active build tenant is not the thin Axiom Indexer tenant")

    role_uri = "./specification/requirements/REQ-P-NATIVE-FRAME-USE.md#role-bindings"
    roles = overlay.get("local_constitution", {}).get("disambiguations", [])
    if [row.get("term") for row in roles] != ["Executive", "Worker", "Reviewer"]:
        failures.append("role disambiguation population is wrong")
    if any(row.get("uri") != role_uri for row in roles):
        failures.append("role disambiguation does not route to native frame use")
    return failures


def validate_frame_acceptance(root: Path) -> list[str]:
    failures: list[str] = []
    frame_bytes = (root / FRAME_PATH).read_bytes()
    if hashlib.sha256(frame_bytes).hexdigest() != FRAME_SHA256:
        failures.append("accepted project frame basis bytes changed")

    decision_path = root / FRAME_DECISION_PATH
    decision_bytes = decision_path.read_bytes()
    if hashlib.sha256(decision_bytes).hexdigest() != FRAME_DECISION_SHA256:
        failures.append("project frame-basis acceptance record bytes changed")
        return failures

    decision = json.loads(decision_bytes)
    expected = {
        "subject_uri": FRAME_URI,
        "subject_ref": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
        "subject_sha256": "sha256:" + FRAME_SHA256,
        "actor_identity": "https://github.com/foolishimp",
        "authority_identity": "urn:stdo-representation:authority:product-owner",
        "decision": "accepted",
    }
    for key, value in expected.items():
        if decision.get(key) != value:
            failures.append(f"project frame-basis acceptance has wrong {key}")
    return failures


def validate_program_map(
    program: dict[str, Any], logical_map: dict[str, Any]
) -> list[str]:
    failures: list[str] = []
    if program.get("kind") != "axiom-indexer.axiomatic-program":
        failures.append("Product program has the wrong kind")
    if logical_map.get("kind") != "axiom-indexer.logical-constraint-map":
        failures.append("Product map has the wrong kind")
    if program.get("calculus_ref") != CALCULUS_REF:
        failures.append("Product program selects the wrong calculus")
    expected_source = STDO_BASIS + "standards/"
    if program.get("source_basis") != expected_source:
        failures.append("Product program selects the wrong source basis")
    if logical_map.get("source_basis") != expected_source:
        failures.append("Product map selects the wrong source basis")
    if logical_map.get("program_uri") != program.get("uri"):
        failures.append("Product map does not bind the Product program URI")
    program_digest = "sha256:" + canonical_sha256(program)
    if logical_map.get("program_sha256") != program_digest:
        failures.append("Product map does not bind the canonical Product program")
    if logical_map.get("frame_refs") != program.get("frame_refs"):
        failures.append("Product map changes the selected frame references")
    for name in ("symbols", "clauses", "residuals"):
        program_value = program.get(name)
        map_value = logical_map.get(name)
        if not isinstance(program_value, list):
            failures.append(f"Product program {name} is not an array")
            continue
        expected_count = len(program_value)
        actual_count = len(map_value) if isinstance(map_value, (list, dict)) else -1
        if actual_count != expected_count:
            failures.append(f"Product map changes the {name} population")
    local_uris = {
        row["uri"]
        for name in ("symbols", "clauses", "residuals")
        for row in program.get(name, [])
        if isinstance(row, dict) and isinstance(row.get("uri"), str)
    }
    if set(logical_map.get("source_routes", {})) != local_uris:
        failures.append("Product map source routes are not total over program items")
    if not logical_map.get("map_sha256", "").startswith("sha256:"):
        failures.append("Product map has no intrinsic digest")
    return failures


def git_value(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def audit(root: Path, axiom_root: Path) -> dict[str, Any]:
    failures: list[str] = []
    overlay = load_json(root / "stdo_representation.json")
    failures.extend(validate_overlay(overlay))
    failures.extend(validate_frame_acceptance(root))

    actual_requirements = {
        path.name for path in (root / "specification/requirements").glob("*.md")
    }
    if actual_requirements != ACTIVE_REQUIREMENTS:
        failures.append("active requirement inventory does not match the thin Product")

    for path in PRODUCT_FILES:
        if not (root / path).is_file():
            failures.append(f"missing Product file: {path}")
    for path, target in PRODUCT_LINKS.items():
        full_path = root / path
        if not full_path.is_symlink() or full_path.readlink().as_posix() != target:
            failures.append(f"wrong or missing Product symlink: {path}")

    if not failures and all(
        (root / path).is_file() for path in (PROGRAM_PATH, MAP_PATH)
    ):
        failures.extend(
            validate_program_map(
                load_json(root / PROGRAM_PATH), load_json(root / MAP_PATH)
            )
        )

    for historical in HISTORICAL_ROOTS:
        if not (root / historical).is_dir():
            failures.append(f"missing retained historical root: {historical}")
        readme = root / historical / "README.md"
        if readme.is_file() and "excluded" not in readme.read_text(encoding="utf-8"):
            failures.append(f"historical root is not explicitly excluded: {historical}")

    required_text = {
        "specification/GOALS.md": ["zero local", "v0.1.0-rc.1"],
        "specification/INTENT.md": [
            "LLM supplies every frame",
            "not part of the `0.1.0`",
        ],
        "specification/PRODUCT.md": ["eight repository entries", "adds no local"],
        ".ai-workspace/tickets/active/T-003-construct-stdo-gtl.md": [
            "change_class: product_reprice",
            "build-tenant:axiom-indexer",
        ],
    }
    for relative, needles in required_text.items():
        content = (root / relative).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in content:
                failures.append(f"{relative} lacks thin-Product claim: {needle}")

    try:
        if (
            git_value(axiom_root, "rev-parse", "refs/tags/v0.1.0-rc.1")
            != AXIOM_TAG_OBJECT
        ):
            failures.append("installed Axiom Indexer tag object mismatch")
        if (
            git_value(axiom_root, "rev-parse", "refs/tags/v0.1.0-rc.1^{}")
            != AXIOM_COMMIT
        ):
            failures.append("installed Axiom Indexer commit mismatch")
        if git_value(axiom_root, "rev-parse", "HEAD^{tree}") != AXIOM_TREE:
            failures.append("installed Axiom Indexer tree mismatch")
    except (FileNotFoundError, subprocess.CalledProcessError):
        failures.append("exact installed Axiom Indexer release is unavailable")

    program = load_json(root / PROGRAM_PATH) if (root / PROGRAM_PATH).is_file() else {}
    logical_map = load_json(root / MAP_PATH) if (root / MAP_PATH).is_file() else {}
    return {
        "valid": not failures,
        "failures": failures,
        "product": {
            "version_line": "0.1.0",
            "member_count": len(PRODUCT_FILES) + len(PRODUCT_LINKS),
            "program_sha256": "sha256:" + canonical_sha256(program)
            if program
            else None,
            "map_sha256": logical_map.get("map_sha256"),
        },
        "frame_basis": {
            "uri": FRAME_URI,
            "sha256": "sha256:" + FRAME_SHA256,
            "decision_sha256": "sha256:" + FRAME_DECISION_SHA256,
            "status": "accepted_and_bound",
        },
    }


def parse_args() -> argparse.Namespace:
    default_axiom = (
        Path.home() / "Library/Application Support/Axiom Indexer/releases/v0.1.0-rc.1"
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--axiom-indexer-root", type=Path, default=default_axiom)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = audit(args.root.resolve(), args.axiom_indexer_root.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
