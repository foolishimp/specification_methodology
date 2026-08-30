#!/usr/bin/env python3
"""Rebuild the exact frozen GTL carrier and test this tenant against it."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "build_tenants" / "gtl" / "code"
GTL_REPOSITORY = "https://github.com/foolishimp/abiogenesis.git"
GTL_COMMIT = "8d7f965a3fae7d1acea6a9db298798480fd4cc2f"
GTL_AUTHORITY_ROOT = "specification/requirements/gtl"
GTL_AUTHORITY_TREE = "21a44b1941a1055d6abd973937e65b83e359de1b"
GTL_AUTHORITY_COUNT = 33
GTL_TENANT_ROOT = "build_tenants/abiogenesis/typescript"


class ProbeFailure(RuntimeError):
    pass


def run(
    argv: list[str],
    *,
    cwd: Path,
    capture: bool = False,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        argv,
        cwd=cwd,
        check=False,
        text=True,
        capture_output=capture,
        env=env,
    )
    if completed.returncode != 0:
        detail = completed.stderr if capture else "see command output above"
        raise ProbeFailure(f"{' '.join(argv)} failed: {detail}")
    return completed


def git(repo: Path, *args: str) -> str:
    return run(["git", *args], cwd=repo, capture=True).stdout.strip()


def verify_basis(repo: Path) -> None:
    if git(repo, "rev-parse", f"{GTL_COMMIT}^{{commit}}") != GTL_COMMIT:
        raise ProbeFailure("frozen GTL commit does not resolve exactly")
    tree = git(repo, "rev-parse", f"{GTL_COMMIT}:{GTL_AUTHORITY_ROOT}")
    if tree != GTL_AUTHORITY_TREE:
        raise ProbeFailure(f"GTL authority tree mismatch: {tree}")
    rows = git(repo, "ls-tree", "-r", GTL_COMMIT, GTL_AUTHORITY_ROOT).splitlines()
    if len(rows) != GTL_AUTHORITY_COUNT:
        raise ProbeFailure(
            f"expected {GTL_AUTHORITY_COUNT} GTL members, found {len(rows)}"
        )
    for row in rows:
        metadata, separator, path = row.partition("\t")
        fields = metadata.split()
        if (
            separator != "\t"
            or len(fields) != 3
            or fields[0] not in {"100644", "100755"}
            or fields[1] != "blob"
        ):
            raise ProbeFailure(f"non-regular GTL authority entry: {path or row}")


def acquire_repository(configured: Path | None, workspace: Path) -> Path:
    if configured is not None:
        if not (configured / ".git").exists():
            raise ProbeFailure(f"not a Git repository: {configured}")
        return configured.resolve()
    sibling = ROOT.parent / "abiogenesis"
    if (sibling / ".git").exists():
        return sibling.resolve()
    clone = workspace / "abiogenesis.git"
    run(
        [
            "git",
            "clone",
            "--filter=blob:none",
            "--no-checkout",
            GTL_REPOSITORY,
            str(clone),
        ],
        cwd=workspace,
    )
    run(["git", "fetch", "origin", GTL_COMMIT], cwd=clone)
    return clone


def extract_frozen_tenant(repo: Path, workspace: Path) -> Path:
    archive = workspace / "frozen-gtl.tar"
    run(
        [
            "git",
            "archive",
            "--format=tar",
            "--output",
            str(archive),
            GTL_COMMIT,
            GTL_TENANT_ROOT,
        ],
        cwd=repo,
    )
    source = workspace / "source"
    source.mkdir()
    with tarfile.open(archive, "r:") as bundle:
        bundle.extractall(source, filter="data")
    tenant = source / GTL_TENANT_ROOT
    if not (tenant / "package-lock.json").is_file():
        raise ProbeFailure("frozen GTL tenant archive is incomplete")
    return tenant


def test_tenant(frozen_tenant: Path, workspace: Path) -> None:
    run(["npm", "ci", "--ignore-scripts"], cwd=frozen_tenant)
    run(["npm", "run", "build"], cwd=frozen_tenant)
    probe = workspace / "probe"
    shutil.copytree(CODE, probe)
    run(["npm", "ci", "--ignore-scripts", "--legacy-peer-deps"], cwd=probe)
    scope = probe / "node_modules" / "@abiogenesis"
    scope.mkdir(parents=True, exist_ok=True)
    os.symlink(frozen_tenant, scope / "typescript-tenant", target_is_directory=True)
    run(["npm", "run", "build"], cwd=probe)
    test_env = dict(os.environ)
    test_env["STDO_REPRESENTATION_ROOT"] = str(ROOT)
    run(["npm", "test"], cwd=probe, env=test_env)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--abiogenesis-repository",
        type=Path,
        help="optional local repository containing the exact frozen GTL commit",
    )
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="stdo-gtl-conformance-") as directory:
        workspace = Path(directory)
        repository = acquire_repository(args.abiogenesis_repository, workspace)
        verify_basis(repository)
        frozen_tenant = extract_frozen_tenant(repository, workspace)
        test_tenant(frozen_tenant, workspace)
    print(
        json.dumps(
            {
                "carrier_repository": GTL_REPOSITORY,
                "carrier_commit": GTL_COMMIT,
                "authority_tree": GTL_AUTHORITY_TREE,
                "authority_members": GTL_AUTHORITY_COUNT,
                "typed_declaration_compiles": True,
                "raw_admission_and_frozen_validation_pass": True,
                "domain_negative_tests_pass": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except ProbeFailure as exc:
        raise SystemExit(f"frozen GTL tenant probe failed: {exc}") from None
