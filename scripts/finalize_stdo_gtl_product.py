#!/usr/bin/env python3
"""Construct STDO.gtl only from an exact external F_H authorization."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "build_tenants" / "gtl" / "design" / "GTL_REPRESENTATION_PROFILE.md"
FRAME_BASIS = ROOT / "specification" / "REFERENCE_FRAME_BASIS.md"
F_H = "urn:stdo:concept:graph-native-odd:f-h"
SOURCE_URI = "stdo://releases/v2.4.3-rc.3/"
FRAME_AUTHORITIES = (
    "./specification/GOALS.md",
    "./specification/PRODUCT.md#product-authority",
    "./specification/requirements/REQ-P-BASIS-AND-IDENTITY.md",
    "./specification/requirements/REQ-P-COMPRESSION-VERIFICATION.md",
    "./specification/requirements/REQ-P-EXECUTIVE-CONTEXT-PROJECTION.md",
    "./specification/requirements/REQ-P-FP-CONSUMPTION.md",
    "./specification/requirements/REQ-P-REPRESENTATION-ALGEBRA.md",
    "./specification/requirements/REQ-P-SELECTION-AND-ACCEPTANCE.md",
)


class FinalizationFailure(RuntimeError):
    """The accepted candidate cannot be constructed exactly."""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def load_unique(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    duplicates: list[str] = []

    def pairs(rows: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in rows:
            if key in result:
                duplicates.append(key)
            result[key] = value
        return result

    value = json.loads(raw, object_pairs_hook=pairs)
    if duplicates or not isinstance(value, dict):
        raise FinalizationFailure(f"duplicate keys or non-object JSON in {path}")
    return value, raw


def require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise FinalizationFailure(f"{label} has an unexpected field set")


def run(argv: list[str], *, cwd: Path, capture: bool = False) -> str:
    completed = subprocess.run(
        argv,
        cwd=cwd,
        check=False,
        text=True,
        capture_output=capture,
    )
    if completed.returncode != 0:
        detail = completed.stderr if capture else "see command output above"
        raise FinalizationFailure(f"{' '.join(argv)} failed: {detail}")
    return completed.stdout if capture else ""


def validate_request(request: dict[str, Any]) -> None:
    require_exact_keys(
        request,
        {
            "kind",
            "schema_version",
            "status",
            "requested_actor_identity",
            "requested_authority_identity",
            "requested_grant_identity",
            "requested_grant_scope",
            "required_basis_refs",
            "subjects",
            "evidence_refs",
            "effect_of_acceptance",
        },
        "acceptance request",
    )
    if (
        request["kind"] != "stdo-representation.f-h-acceptance-request"
        or request["schema_version"] != 1
        or request["status"] != "pending"
    ):
        raise FinalizationFailure("acceptance request has the wrong identity or state")
    for key in (
        "requested_actor_identity",
        "requested_authority_identity",
        "requested_grant_identity",
        "requested_grant_scope",
        "effect_of_acceptance",
    ):
        if not isinstance(request[key], str) or not request[key]:
            raise FinalizationFailure(f"acceptance request {key} is empty")
    if (
        not isinstance(request["required_basis_refs"], list)
        or not request["required_basis_refs"]
        or request["required_basis_refs"] != sorted(set(request["required_basis_refs"]))
        or SOURCE_URI not in request["required_basis_refs"]
        or not isinstance(request["evidence_refs"], list)
        or not request["evidence_refs"]
        or request["evidence_refs"] != sorted(set(request["evidence_refs"]))
    ):
        raise FinalizationFailure(
            "acceptance request bases and evidence are not exact canonical sets"
        )
    subjects = request.get("subjects")
    if not isinstance(subjects, list) or len(subjects) != 3:
        raise FinalizationFailure(
            "acceptance request must contain exactly three subjects"
        )
    kinds: set[str] = set()
    for row in subjects:
        if not isinstance(row, dict):
            raise FinalizationFailure("acceptance request subject is not an object")
        require_exact_keys(
            row,
            {"subject_kind", "subject_identity", "subject_sha256", "path"},
            "acceptance request subject",
        )
        if any(not isinstance(row[key], str) or not row[key] for key in row):
            raise FinalizationFailure(
                "acceptance request subject contains an empty field"
            )
        kinds.add(row["subject_kind"])
    if kinds != {
        "reference_frame_basis",
        "representation_profile",
        "semantic_selection_ledger",
    }:
        raise FinalizationFailure("acceptance request subject kinds are incomplete")


def accepted_subjects(
    request: dict[str, Any], decision: dict[str, Any]
) -> dict[str, dict[str, str]]:
    rows = decision.get("accepted_subjects")
    if not isinstance(rows, list) or len(rows) != 3:
        raise FinalizationFailure(
            "authorization does not contain exactly three accepted subjects"
        )
    for row in rows:
        if not isinstance(row, dict):
            raise FinalizationFailure("accepted subject is not an object")
        require_exact_keys(
            row,
            {"subject_kind", "subject_identity", "subject_sha256"},
            "accepted subject",
        )
    expected = {
        (row["subject_kind"], row["subject_identity"], row["subject_sha256"])
        for row in request["subjects"]
    }
    observed = {
        (row["subject_kind"], row["subject_identity"], row["subject_sha256"])
        for row in rows
    }
    if expected != observed or len(expected) != 3 or len(observed) != len(rows):
        raise FinalizationFailure(
            "authorization does not accept exactly the three requested subjects"
        )
    return {row["subject_kind"]: row for row in rows}


def acceptance_record(
    subject: dict[str, str],
    decision: dict[str, Any],
    *,
    frame: bool,
) -> tuple[dict[str, Any], bytes, str]:
    record = {
        "kind": "stdo-representation.authority-acceptance",
        "schema_version": 1,
        "subject_kind": subject["subject_kind"],
        "subject_identity": subject["subject_identity"],
        "subject_sha256": subject["subject_sha256"],
        "traversal_ref": F_H,
        "actor_identity": decision["actor_identity"],
        "authority_identity": decision["authority_identity"],
        "grant_identity": decision["grant_identity"],
        "grant_scope": decision["grant_scope"],
        "basis_refs": sorted(decision["basis_refs"]),
        "admitting_authority_refs": list(FRAME_AUTHORITIES) if frame else None,
        "decision": "accepted",
        "decided_at": decision["decided_at"],
        "evidence_refs": sorted(decision["evidence_refs"]),
        "supersedes": None,
    }
    raw = canonical_bytes(record)
    identity = "urn:stdo-representation:authority-acceptance:sha256:" f"{sha256(raw)}"
    return record, raw, identity


def acquire_frozen_gtl(configured: Path | None, workspace: Path) -> Path:
    commit = "8d7f965a3fae7d1acea6a9db298798480fd4cc2f"
    if configured is not None:
        repository = configured.resolve()
    else:
        sibling = ROOT.parent / "abiogenesis"
        if (sibling / ".git").exists():
            repository = sibling.resolve()
        else:
            repository = workspace / "abiogenesis.git"
            run(
                [
                    "git",
                    "clone",
                    "--filter=blob:none",
                    "--no-checkout",
                    "https://github.com/foolishimp/abiogenesis.git",
                    str(repository),
                ],
                cwd=workspace,
            )
            run(["git", "fetch", "origin", commit], cwd=repository)
    resolved = run(
        ["git", "rev-parse", f"{commit}^{{commit}}"],
        cwd=repository,
        capture=True,
    ).strip()
    if resolved != commit:
        raise FinalizationFailure("frozen GTL commit does not resolve exactly")
    archive = workspace / "frozen-gtl.tar"
    run(
        [
            "git",
            "archive",
            "--format=tar",
            "--output",
            str(archive),
            commit,
            "build_tenants/abiogenesis/typescript",
        ],
        cwd=repository,
    )
    source = workspace / "frozen-source"
    source.mkdir()
    with tarfile.open(archive, "r:") as bundle:
        bundle.extractall(source, filter="data")
    tenant = source / "build_tenants" / "abiogenesis" / "typescript"
    run(["npm", "ci", "--ignore-scripts"], cwd=tenant)
    run(["npm", "run", "build"], cwd=tenant)
    return tenant


def construct(
    candidate: Path,
    build_plan: Path,
    acceptances: dict[str, Path],
    output: Path,
    configured_abiogenesis: Path | None,
) -> None:
    artifact = candidate / "publisher" / "gtl-toolchain-product.tgz"
    with tempfile.TemporaryDirectory(prefix="stdo-gtl-finalize-") as directory:
        workspace = Path(directory)
        frozen_tenant = acquire_frozen_gtl(configured_abiogenesis, workspace)
        package_root = workspace / "publisher"
        package_root.mkdir()
        with tarfile.open(artifact, "r:gz") as bundle:
            bundle.extractall(package_root, filter="data")
        package = package_root / "package"
        run(
            ["npm", "install", "--ignore-scripts", "--legacy-peer-deps"],
            cwd=package,
        )
        scope = package / "node_modules" / "@abiogenesis"
        scope.mkdir(parents=True, exist_ok=True)
        peer = scope / "typescript-tenant"
        if peer.exists() or peer.is_symlink():
            if peer.is_dir() and not peer.is_symlink():
                shutil.rmtree(peer)
            else:
                peer.unlink()
        os.symlink(frozen_tenant, peer, target_is_directory=True)
        cli = package / "build" / "src" / "cli.js"
        run(
            [
                "node",
                str(cli),
                "build",
                "--plan",
                str(build_plan),
                "--source-manifest",
                str(candidate / "source-manifest.json"),
                "--profile",
                str(PROFILE),
                "--frame-basis",
                str(FRAME_BASIS),
                "--selection-ledger",
                str(candidate / "semantic-selection-ledger.json"),
                "--profile-acceptance",
                str(acceptances["representation_profile"]),
                "--frame-basis-acceptance",
                str(acceptances["reference_frame_basis"]),
                "--selection-acceptance",
                str(acceptances["semantic_selection_ledger"]),
                "--publisher-manifest",
                str(candidate / "publisher" / "gtl-toolchain-product.json"),
                "--publisher-artifact",
                str(artifact),
                "--output-directory",
                str(output),
            ],
            cwd=package,
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-directory", type=Path, required=True)
    parser.add_argument("--authorization", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--abiogenesis-repository", type=Path)
    args = parser.parse_args()
    candidate = args.candidate_directory.resolve()
    output = args.output_directory.resolve()
    if output.exists():
        raise FinalizationFailure(f"output already exists: {output}")
    request, _ = load_unique(candidate / "acceptance-request.json")
    validate_request(request)
    decision, decision_bytes = load_unique(args.authorization.resolve())
    require_exact_keys(
        decision,
        {
            "kind",
            "schema_version",
            "request_sha256",
            "actor_identity",
            "authority_identity",
            "grant_identity",
            "grant_scope",
            "basis_refs",
            "accepted_subjects",
            "decision",
            "decided_at",
            "evidence_refs",
        },
        "authorization",
    )
    decision_canonical = canonical_bytes(decision)
    if decision_bytes not in (decision_canonical, decision_canonical + b"\n"):
        raise FinalizationFailure(
            "authorization is not exact canonical JSON with optional final LF"
        )
    request_sha = f"sha256:{sha256(canonical_bytes(request))}"
    if (
        decision["kind"] != "stdo-representation.f-h-construction-authorization"
        or decision["schema_version"] != 1
        or decision["request_sha256"] != request_sha
        or decision["decision"] != "accepted"
        or decision["actor_identity"] != request["requested_actor_identity"]
        or decision["authority_identity"] != request["requested_authority_identity"]
        or decision["grant_identity"] != request["requested_grant_identity"]
        or decision["grant_scope"] != request["requested_grant_scope"]
    ):
        raise FinalizationFailure(
            "authorization does not accept the exact requested authority binding"
        )
    if (
        decision["basis_refs"] != request["required_basis_refs"]
        or decision["evidence_refs"] != request["evidence_refs"]
    ):
        raise FinalizationFailure(
            "authorization bases and evidence do not equal the exact request"
        )
    subjects = accepted_subjects(request, decision)
    base, _ = load_unique(candidate / "build-plan-base.json")
    require_exact_keys(
        base,
        {
            "kind",
            "schema_version",
            "source_stdo",
            "what_member_set_identity",
            "representation_profile_identity",
            "representation_profile_sha256",
            "frame_basis_identity",
            "frame_basis_sha256",
            "frame_admitting_authority_refs",
            "semantic_selection_ledger_identity",
            "semantic_selection_ledger_sha256",
            "publisher",
            "records",
        },
        "build plan base",
    )
    temporary = output.parent / f".{output.name}.tmp-{os.getpid()}"
    temporary.mkdir(parents=True)
    try:
        acceptance_directory = temporary / "acceptance"
        acceptance_directory.mkdir()
        acceptance_paths: dict[str, Path] = {}
        acceptance_identities: dict[str, str] = {}
        for subject_kind in (
            "representation_profile",
            "reference_frame_basis",
            "semantic_selection_ledger",
        ):
            _, raw, identity = acceptance_record(
                subjects[subject_kind],
                decision,
                frame=subject_kind == "reference_frame_basis",
            )
            path = acceptance_directory / f"{subject_kind}.json"
            path.write_bytes(raw)
            acceptance_paths[subject_kind] = path
            acceptance_identities[subject_kind] = identity
        plan = dict(base)
        plan["kind"] = "stdo-representation.gtl-build-plan"
        plan["profile_acceptance_identity"] = acceptance_identities[
            "representation_profile"
        ]
        plan["frame_basis_acceptance_identity"] = acceptance_identities[
            "reference_frame_basis"
        ]
        plan["selection_acceptance_identity"] = acceptance_identities[
            "semantic_selection_ledger"
        ]
        build_plan = temporary / "build-plan.json"
        build_plan.write_bytes(canonical_bytes(plan))
        product = temporary / "product"
        construct(
            candidate,
            build_plan,
            acceptance_paths,
            product,
            args.abiogenesis_repository,
        )
        (temporary / "authorization.json").write_bytes(decision_canonical)
        summary = {
            "kind": "stdo-representation.gtl-construction",
            "schema_version": 1,
            "authorization_sha256": f"sha256:{sha256(decision_canonical)}",
            "build_plan_sha256": f"sha256:{sha256(build_plan.read_bytes())}",
            "acceptance_identities": acceptance_identities,
            "stdo_gtl_sha256": f"sha256:{sha256((product / 'stdo.gtl').read_bytes())}",
            "build_receipt_sha256": f"sha256:{sha256((product / 'build-receipt.json').read_bytes())}",
        }
        (temporary / "construction-summary.json").write_text(
            f"{json.dumps(summary, indent=2, sort_keys=True)}\n",
            encoding="utf-8",
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary.rename(output)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (FinalizationFailure, KeyError, OSError, TypeError, ValueError) as error:
        raise SystemExit(f"STDO.gtl finalization failed: {error}") from None
