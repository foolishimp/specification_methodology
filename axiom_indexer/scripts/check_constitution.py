#!/usr/bin/env python3
"""Verify the release-coupled Axiom Indexer candidate constitution."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
TARGET_STDO_BASIS = "stdo://releases/v2.5.0-rc.4/"
TARGET_STDO_MANIFEST = (
    "4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e"
)
TARGET_STDO_CUT = "v2.5.0-rc.4"
TRANSITION_STDO_BASIS = "stdo://releases/v2.5.0-rc.3/"
TRANSITION_STDO_MANIFEST = (
    "7feb297337644bc8ba7fc350395c05bfa4f6ee364f906154d8b8c4ebc7bdafdf"
)
AXIOM_CUT = "v2.5.0-rc.4"
AXIOM_QUALIFIED_REF = "refs/tags/axiom_indexer/v2.5.0-rc.4"
SOURCE_STDO_QUALIFIED_REF = "refs/tags/specification_methodology/v2.5.0-rc.4"
SOURCE_STDO_TAG_OBJECT = "032dac0c833111547f7dd4b290c5316ed9b70f97"
SOURCE_STDO_COMMIT = "7a25668a8fecfd26f895759af3bec4708727964a"
SOURCE_STDO_REPOSITORY_TREE = "737af9a7a2779dbf59e7c81232e7efd4dd98692a"
SOURCE_STDO_SUBTREE_TREE = "a9565f923213759984f936d087cd7cebd0f44a74"
SOURCE_STDO_STANDARDS_TREE = "d6642edac9fb509a68b2ffc81d3404f2360b34e4"
SOURCE_STDO_MEMBER_SET_SHA256 = (
    "504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656"
)
AXIOMATIC_CALCULUS_SHA256 = (
    "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d"
)
PRODUCT_INVENTORY_SHA256 = (
    "7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6"
)
RELEASE_PATH = Path("releases/v2.5.0.md")
RELEASE_SHA256 = "2f4643a5b184a33ab9cd65c1de09b53ffee747012cd1108b795fc6df92263e8d"
FRAME_BASIS_PATH = Path("specification/REFERENCE_FRAME_BASIS.md")
FRAME_BASIS_SHA256 = "100c71ba8bd8f64a50efff656ef5004edf6b06f27fa2bc9dcd7dd1e7d039009a"
FRAME_DECISION_PATH = Path(
    ".ai-workspace/decisions/20260901T142728Z_frame_basis_v7_acceptance.json"
)
FRAME_DECISION_SHA256 = (
    "951c8a40b9be8655e2e1a225d6c6db2f6be5e089b868375709fa168717e58f5c"
)
FRAME_DECISION_SCOPE = (
    "Qualify and publish only the unchanged seven-member Axiom Indexer mechanics "
    "as the release-coupled v2.5.0-rc.4 member of the coordinated Specification "
    "Stack cohort; excludes sibling semantic program or map bytes and any "
    "Product-scope expansion."
)
FRAME_DECISION_TIME = "2026-09-01T14:50:53Z"
FRAME_DECISION_SOURCE = (
    "Direct human Product-owner instruction in the active workstream granted "
    "Codex authority, once completion and proportional qualification were "
    "achieved, to release this same-version coordinated cohort. This proxy "
    "decision applies that pre-existing bounded grant after accepted cold-review "
    "findings; it does not claim separate human inspection or acceptance of the "
    "exact repaired bytes."
)
FRAME_DECISION_EVIDENCE_REFS = (
    "./specification/PRODUCT.md#product-disposition-authority",
    "./specification/PRODUCT.md#coordinated-release-identity",
    "./specification/GOALS.md#goal-004--cut-the-release-coupled-axiom-mechanics-for-stdo-rc4",
    "./specification/REFERENCE_FRAME_BASIS.md#acceptance-gate",
    "./releases/v2.5.0.md",
    "./stdo_default.json",
)
RELEASE_STATUS = (
    "Status: mutable coordinated candidate; no Axiom Indexer `2.5.0` cut is\n"
    "published or accepted by this record."
)
RELEASE_SEMANTIC_CLAIM = (
    "- `AXIOM-2.5-RC4-C03`: the conserved executable late-binds declared URIs,\n"
    "  checks the Product's mechanical laws, emits deterministic diagnostics,\n"
    "  instantiates the unchanged valid program as a logical map, and joins exact\n"
    "  caller-supplied labeled text."
)
RELEASE_PREDECESSOR_DISPOSITION = (
    "- `AXIOM-0.1-C02`: **conserved** by the byte-identical executable and\n"
    "  reproduced normal and optimized test results;"
)

STDOStatusRunner = Callable[[Path, Path], dict[str, Any]]


@dataclass(frozen=True)
class ProductMember:
    kind: str
    path: str
    sha256: str
    target: str | None = None

    @property
    def release_member(self) -> str:
        if self.target is None:
            return f"`{self.path}`"
        return f"`{self.path}` -> `{self.target}`"


PRODUCT_MEMBERS = (
    ProductMember(
        "symlink",
        ".agents/skills/axiomatize-corpus",
        "94f7720145baa135bb3d88ec352b4fe32e9841fcfc9a23dbf00ea54ab0fa7c40",
        "../../skills/axiomatize-corpus",
    ),
    ProductMember(
        "symlink",
        ".claude/skills/axiomatize-corpus",
        "94f7720145baa135bb3d88ec352b4fe32e9841fcfc9a23dbf00ea54ab0fa7c40",
        "../../skills/axiomatize-corpus",
    ),
    ProductMember(
        "file",
        "build_tenants/core/code/ac.py",
        "dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672",
    ),
    ProductMember(
        "file",
        "skills/axiomatize-corpus/SKILL.md",
        "dcd2294e7de7ae5bfb4a70b3980594a36f9a3b28b42236523a86cbc42aa7babe",
    ),
    ProductMember(
        "file",
        "skills/axiomatize-corpus/agents/openai.yaml",
        "409721119552f3e1ffded2a2aed5f81a92b40389c81f77c0792f305e507be990",
    ),
    ProductMember(
        "file",
        "skills/axiomatize-corpus/references/output-contract.md",
        "fd0996009b890e464399863e1f16bb9b9ca7820cb5aa04e95244618849983694",
    ),
    ProductMember(
        "file",
        "skills/axiomatize-corpus/references/program.schema.json",
        "61c9d26fabb1d844f643712632f6a6551a1c6f7f8ddfef604673e57b7c6b3b7b",
    ),
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def derive_cut_from_basis(basis: str) -> str | None:
    match = re.fullmatch(r"stdo://releases/(v[^/]+)/", basis)
    return match.group(1) if match else None


def validate_cut_alignment(axiom_cut: str, stdo_basis: str) -> list[str]:
    represented_cut = derive_cut_from_basis(stdo_basis)
    if represented_cut is None:
        return ["Source STDO basis does not name one exact release cut"]
    if axiom_cut != represented_cut:
        return ["Axiom product-local cut does not match Source STDO cut"]
    return []


def run_stdo_status(store: Path, definition: Path) -> dict[str, Any]:
    """Run exact Product Definition verification against one explicit store."""

    command = (
        "stdo",
        "--store",
        str(store),
        "status",
        "--definition",
        str(definition),
        "--verify",
    )
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        raise RuntimeError(f"cannot execute stdo status: {exc}") from exc
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(
            f"stdo status --verify exited {completed.returncode}: {detail}"
        )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"stdo status returned invalid JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("stdo status did not return one JSON object")
    return payload


def verify_stdo_status(
    store: Path | None,
    failures: list[str],
    status_runner: STDOStatusRunner | None = None,
) -> dict[str, Any] | None:
    """Require live exact-cut evidence before declaring the child release ready."""

    if store is None:
        failures.append("explicit STDO store is required for release readiness")
        return None
    resolved_store = store.expanduser().absolute()
    definition = (ROOT / "stdo_default.json").resolve()
    runner = status_runner or run_stdo_status
    try:
        status = runner(resolved_store, definition)
    except (OSError, RuntimeError, ValueError) as exc:
        failures.append(f"STDO status evidence unavailable: {exc}")
        return None
    if not isinstance(status, dict):
        failures.append("STDO status evidence is not one JSON object")
        return None

    expected = {
        "basis": TARGET_STDO_BASIS,
        "cut": TARGET_STDO_CUT,
        "definition": str(definition),
        "definition_id": "urn:stdo:product-definition:axiom-indexer",
        "failures": [],
        "installed": True,
        "manifest_sha256": TARGET_STDO_MANIFEST,
        "path": str(resolved_store / "releases" / TARGET_STDO_CUT),
        "schema": str(
            resolved_store
            / "releases"
            / TARGET_STDO_CUT
            / "standards"
            / "schemas"
            / "product-definition.schema.json"
        ),
        "valid": True,
    }
    for key, value in expected.items():
        if status.get(key) != value:
            failures.append(f"STDO status mismatch: {key}")

    release = status.get("release")
    if not isinstance(release, dict):
        failures.append("STDO status release identity is missing")
        return status
    expected_release = {
        "commit": SOURCE_STDO_COMMIT,
        "cut": TARGET_STDO_CUT,
        "project_release_namespace": "specification_methodology",
        "project_subtree_root": "specification_methodology",
        "project_subtree_tree": SOURCE_STDO_SUBTREE_TREE,
        "qualified_ref": SOURCE_STDO_QUALIFIED_REF,
        "standards_tree": SOURCE_STDO_STANDARDS_TREE,
        "tag_object": SOURCE_STDO_TAG_OBJECT,
        "tree": SOURCE_STDO_REPOSITORY_TREE,
    }
    for key, value in expected_release.items():
        if release.get(key) != value:
            failures.append(f"STDO status release mismatch: {key}")
    return status


def _member_bytes(path: Path, member: ProductMember) -> bytes:
    if member.kind == "symlink":
        if not path.is_symlink():
            raise ValueError("expected symlink")
        return os.readlink(path).encode("utf-8")
    if member.kind == "file":
        if not path.is_file() or path.is_symlink():
            raise ValueError("expected regular file")
        return path.read_bytes()
    raise ValueError(f"unsupported member kind: {member.kind}")


def verify_product_members(root: Path = ROOT) -> tuple[list[str], str]:
    failures: list[str] = []
    rows: list[str] = []
    for member in sorted(PRODUCT_MEMBERS, key=lambda item: item.path):
        path = root / member.path
        try:
            value = _member_bytes(path, member)
        except (OSError, ValueError) as exc:
            failures.append(f"invalid Product member {member.path}: {exc}")
            continue
        observed = sha256_bytes(value)
        if observed != member.sha256:
            failures.append(f"Product member digest mismatch: {member.path}")
        if member.target is not None and value.decode("utf-8") != member.target:
            failures.append(f"Product symlink target mismatch: {member.path}")
        rows.append(f"{observed}  {member.kind}  {member.path}\n")
    inventory = sha256_bytes("".join(rows).encode("utf-8"))
    if inventory != PRODUCT_INVENTORY_SHA256:
        failures.append("Product inventory digest mismatch")
    return failures, inventory


def _load_json(path: Path, failures: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"cannot read JSON {path.relative_to(ROOT)}: {exc}")
        return None


def verify_definition(failures: list[str]) -> tuple[str, dict[str, Any] | None]:
    definition = _load_json(ROOT / "stdo_default.json", failures)
    if not isinstance(definition, dict):
        return "invalid", None
    stdo = definition.get("constitution", {}).get("stdo", {})
    basis = stdo.get("basis", {})
    basis_uri = str(basis.get("uri", ""))
    manifest = basis.get("manifest_sha256")
    schema = definition.get("$schema")

    if basis_uri == TRANSITION_STDO_BASIS:
        expected_schema = (
            f"{TRANSITION_STDO_BASIS}standards/schemas/product-definition.schema.json"
        )
        if schema != expected_schema:
            failures.append("Product Definition transition schema mismatch")
        if manifest != TRANSITION_STDO_MANIFEST:
            failures.append("Product Definition transition manifest mismatch")
        failures.append(
            "Product Definition remains on verified RC3 transition basis; "
            "exact RC4 adoption required"
        )
        return "transition", definition

    if basis_uri == TARGET_STDO_BASIS:
        expected_schema = (
            f"{TARGET_STDO_BASIS}standards/schemas/product-definition.schema.json"
        )
        if schema != expected_schema:
            failures.append("Product Definition target schema mismatch")
        if TARGET_STDO_MANIFEST is None:
            failures.append("exact RC4 installed-manifest digest is not recorded")
            return "target_unpinned", definition
        if manifest != TARGET_STDO_MANIFEST:
            failures.append("Product Definition target manifest mismatch")
        failures.extend(validate_cut_alignment(AXIOM_CUT, basis_uri))
        return "target", definition

    failures.append("Product Definition selects neither transition nor target basis")
    return "invalid", definition


def validate_frame_decision(decision: Any) -> list[str]:
    failures: list[str] = []
    if not isinstance(decision, dict):
        return ["frame-basis decision is not one JSON object"]
    expected_decision = {
        "kind": "axiom-indexer.frame-basis-acceptance",
        "schema_version": 2,
        "subject_uri": "urn:axiom-indexer:frame-set:release-readiness:7",
        "subject_ref": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
        "subject_sha256": f"sha256:{FRAME_BASIS_SHA256}",
        "method_basis_uri": (f"{TARGET_STDO_BASIS}standards/REFERENCE_FRAME_METHOD.md"),
        "method_basis_sha256": (
            "sha256:c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8"
        ),
        "actor_identity": "urn:openai:codex:delegated-release-authority",
        "authority_identity": "urn:axiom-indexer:authority:product-owner",
        "authority_mode": "explicitly-user-granted-bounded-release-authority-proxy",
        "decision": "accepted",
        "scope": FRAME_DECISION_SCOPE,
        "decided_at": FRAME_DECISION_TIME,
        "grant_source_kind": "direct-human-product-owner-conversation",
        "decision_source": FRAME_DECISION_SOURCE,
        "self_expansion_prohibited": True,
        "human_exact_byte_inspection_claimed": False,
    }
    for key, value in expected_decision.items():
        if decision.get(key) != value:
            failures.append(f"frame-basis decision mismatch: {key}")

    if decision.get("evidence_refs") != list(FRAME_DECISION_EVIDENCE_REFS):
        failures.append("frame-basis decision mismatch: evidence_refs")
    for evidence_ref in FRAME_DECISION_EVIDENCE_REFS:
        relative = evidence_ref.removeprefix("./").split("#", maxsplit=1)[0]
        if not (ROOT / relative).is_file():
            failures.append(
                f"frame-basis decision evidence unavailable: {evidence_ref}"
            )

    decided_at = decision.get("decided_at")
    try:
        parsed_time = datetime.fromisoformat(str(decided_at).replace("Z", "+00:00"))
    except ValueError:
        failures.append("frame-basis decision time is not ISO-8601")
    else:
        if (
            parsed_time.tzinfo is None
            or parsed_time.utcoffset() != timezone.utc.utcoffset(parsed_time)
        ):
            failures.append("frame-basis decision time is not explicit UTC")
    return failures


def verify_frame_governance(
    definition: dict[str, Any] | None, failures: list[str]
) -> None:
    try:
        frame_bytes = (ROOT / FRAME_BASIS_PATH).read_bytes()
    except OSError as exc:
        failures.append(f"cannot read {FRAME_BASIS_PATH}: {exc}")
        return
    if sha256_bytes(frame_bytes) != FRAME_BASIS_SHA256:
        failures.append("accepted frame-basis digest mismatch")

    decision_path = ROOT / FRAME_DECISION_PATH
    try:
        decision_bytes = decision_path.read_bytes()
    except OSError as exc:
        failures.append(f"cannot read {FRAME_DECISION_PATH}: {exc}")
        return
    if sha256_bytes(decision_bytes) != FRAME_DECISION_SHA256:
        failures.append("frame-basis decision digest mismatch")
    try:
        decision = json.loads(decision_bytes)
    except json.JSONDecodeError as exc:
        failures.append(f"cannot parse {FRAME_DECISION_PATH}: {exc}")
        return
    failures.extend(validate_frame_decision(decision))

    if definition is None:
        return
    expected_frame_binding = {
        "uri": "./specification/REFERENCE_FRAME_BASIS.md#project-frame-basis",
        "authority": [
            "./specification/PRODUCT.md#product-disposition-authority",
            f"./{FRAME_DECISION_PATH.as_posix()}",
        ],
        "applies_to": ["urn:stdo:product-definition:axiom-indexer"],
    }
    if definition.get("reference_frame_bases") != [expected_frame_binding]:
        failures.append("Product Definition frame-basis binding mismatch")


def _section(text: str, start: str, end: str) -> str:
    before, separator, remainder = text.partition(start)
    del before
    if not separator:
        return ""
    section, end_separator, tail = remainder.partition(end)
    del tail
    return section if end_separator else ""


def validate_release_record_bytes(release_bytes: bytes) -> list[str]:
    failures: list[str] = []
    if sha256_bytes(release_bytes) != RELEASE_SHA256:
        failures.append("release record digest mismatch")
    try:
        text = release_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        failures.append(f"release record is not UTF-8: {exc}")
        return failures

    if not text.startswith(f"# Axiom Indexer 2.5.0 RC4\n\n{RELEASE_STATUS}\n"):
        failures.append("release record candidate status mismatch")
    if RELEASE_SEMANTIC_CLAIM not in text:
        failures.append("release record semantic claim mismatch")
    if RELEASE_PREDECESSOR_DISPOSITION not in text:
        failures.append("release record predecessor disposition mismatch")

    required = (
        f"| product-local cut | `{AXIOM_CUT}` |",
        f"| qualified immutable tag ref | `{AXIOM_QUALIFIED_REF}` |",
        f"| matched Source STDO cut | `{SOURCE_STDO_QUALIFIED_REF}` |",
        f"| public Source STDO basis | `{TARGET_STDO_BASIS}` |",
        f"`{TARGET_STDO_MANIFEST}`",
        f"`{SOURCE_STDO_TAG_OBJECT}`",
        f"`{SOURCE_STDO_COMMIT}`",
        f"`{SOURCE_STDO_REPOSITORY_TREE}`",
        f"`{SOURCE_STDO_SUBTREE_TREE}`",
        f"`{SOURCE_STDO_STANDARDS_TREE}`",
        f"`{SOURCE_STDO_MEMBER_SET_SHA256}`",
        f"`{AXIOMATIC_CALCULUS_SHA256}`",
        f"`{PRODUCT_INVENTORY_SHA256}`",
        "The sibling STDO Representation Axiomatic Program and logical map are not Axiom",
        "| annotated Axiom RC tag object | `pending-freeze` |",
        "| peeled monorepo commit | `pending-freeze` |",
        "| monorepo repository tree | `pending-freeze` |",
        "| Axiom Project Subtree tree | `pending-freeze` |",
        "Before immutable publication, candidate qualifying-byte\n"
        "repair remains local to this RC4 construction and requires renewed\n"
        "qualification, not a higher cut.",
    )
    for fragment in required:
        if fragment not in text:
            failures.append(f"release record missing exact fragment: {fragment}")

    subject = _section(text, "## Candidate Product subject", "## Release claims")
    if not subject:
        failures.append("release record has no closed Candidate Product subject")
        return failures
    rows = tuple(
        line
        for line in subject.splitlines()
        if line.startswith("| file |") or line.startswith("| symlink |")
    )
    expected_rows = tuple(
        f"| {member.kind} | {member.release_member} | `{member.sha256}` |"
        for member in PRODUCT_MEMBERS
    )
    if rows != expected_rows:
        failures.append("release record Product member table mismatch")
    return failures


def verify_release_record(failures: list[str]) -> None:
    path = ROOT / RELEASE_PATH
    try:
        release_bytes = path.read_bytes()
    except OSError as exc:
        failures.append(f"cannot read {RELEASE_PATH}: {exc}")
        return
    failures.extend(validate_release_record_bytes(release_bytes))


def verify_live_law(failures: list[str]) -> None:
    surfaces = {
        "specification/PRODUCT.md": (
            "## Coordinated release identity",
            "refs/tags/axiom_indexer/v<version>-rc.<n>",
            "does not claim, copy, or accept those sibling bytes.",
        ),
        "specification/GOALS.md": (
            "## GOAL-004 — Cut the release-coupled Axiom mechanics for STDO RC4",
            AXIOM_QUALIFIED_REF,
        ),
        "specification/requirements/REQ-P-RELEASE-COUPLING.md": (
            "REQ-P-RELEASE-COUPLING-001",
            "REQ-P-RELEASE-COUPLING-005",
            "axiom_indexer",
        ),
        "build_tenants/core/design/README.md": (
            "## Release-Coupled Realization",
            "STDO Representation supplies and owns the corpus-specific Axiomatic Program.",
        ),
        "specification/REFERENCE_FRAME_BASIS.md": (
            "urn:axiom-indexer:frame-set:release-readiness:7",
            f'method_basis = "{TARGET_STDO_BASIS}standards/REFERENCE_FRAME_METHOD.md"',
            f'release_method = "{TARGET_STDO_BASIS}standards/RELEASE_METHOD.md"',
            f'stdo_manifest_sha256 = "sha256:{TARGET_STDO_MANIFEST}"',
        ),
    }
    for relative, fragments in surfaces.items():
        try:
            text = (ROOT / relative).read_text(encoding="utf-8")
        except OSError as exc:
            failures.append(f"cannot read {relative}: {exc}")
            continue
        for fragment in fragments:
            if fragment not in text:
                failures.append(f"{relative} missing exact law: {fragment}")


def check_constitution(
    root: Path = ROOT,
    *,
    stdo_store: Path | None = None,
    status_runner: STDOStatusRunner | None = None,
) -> dict[str, Any]:
    if root != ROOT:
        raise ValueError("alternate roots are unsupported")
    basis_failures: list[str] = []
    basis_state, definition = verify_definition(basis_failures)
    dependency_failures: list[str] = []
    verify_stdo_status(stdo_store, dependency_failures, status_runner)
    governance_failures: list[str] = []
    verify_frame_governance(definition, governance_failures)
    mechanics_failures: list[str] = []
    member_failures, inventory = verify_product_members(root)
    mechanics_failures.extend(member_failures)
    verify_release_record(mechanics_failures)
    verify_live_law(mechanics_failures)
    failures = (
        basis_failures + dependency_failures + governance_failures + mechanics_failures
    )
    return {
        "axiom_cut": AXIOM_CUT,
        "basis_state": basis_state,
        "dependency_valid": not dependency_failures,
        "failures": failures,
        "governance_valid": not governance_failures,
        "mechanics_valid": not mechanics_failures,
        "product_member_count": len(PRODUCT_MEMBERS),
        "product_member_inventory_sha256": inventory,
        "release_ready": not failures,
        "release_record": RELEASE_PATH.as_posix(),
        "stdo_basis": TARGET_STDO_BASIS,
        "stdo_manifest_sha256": TARGET_STDO_MANIFEST,
        "stdo_status_store": (
            str(stdo_store.expanduser().absolute()) if stdo_store is not None else None
        ),
        "stdo_status_valid": not dependency_failures,
        "valid": not failures,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify the release-coupled Axiom Indexer candidate"
    )
    parser.add_argument(
        "--stdo-store",
        required=True,
        type=Path,
        help="explicit installed-release store used by stdo status --verify",
    )
    args = parser.parse_args(argv)
    result = check_constitution(stdo_store=args.stdo_store)
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
