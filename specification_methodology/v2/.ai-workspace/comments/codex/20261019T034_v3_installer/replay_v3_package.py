"""Replay frozen common bytes through real Git tags and an isolated CLI store.

Run with the toolchain's dependency-complete Python. The default exercises this
checkout's source. Pass --cli /absolute/path/to/stdo to exercise an installed
executable instead. No refs or stores in the source repository are changed.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

SOURCE_COMMIT = "494451522072ec34381c644f1ccfa2331f2b1e27"
SOURCE_PATH = "specification_methodology/v3/build_tenants/common"
PACKAGE_TREE = "082df4ea2b7b3658aab528bbfbcfe81234ccc810"
STANDARDS_DIGEST = "c60b469b34e80c61e8e8ce5d4f48eb4f12777dfda37ce88f561cf9c12609a1fb"
CUT = "v3.0.0-rc.9999"
PROJECT = "specification_methodology/v3"


def require(condition: bool, detail: str) -> None:
    if not condition:
        raise RuntimeError(detail)


def git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    environment = dict(os.environ)
    environment.update(
        GIT_AUTHOR_DATE="2026-10-19T00:00:00+00:00",
        GIT_COMMITTER_DATE="2026-10-19T00:00:00+00:00",
        GIT_AUTHOR_NAME="STDO Installer Fixture",
        GIT_AUTHOR_EMAIL="fixture@example.invalid",
        GIT_COMMITTER_NAME="STDO Installer Fixture",
        GIT_COMMITTER_EMAIL="fixture@example.invalid",
    )
    return subprocess.run(
        [
            "git",
            "-c",
            "commit.gpgsign=false",
            "-c",
            "tag.gpgsign=false",
            "-c",
            "core.autocrlf=false",
            *args,
        ],
        cwd=root,
        env=environment,
        check=True,
        capture_output=True,
        text=not binary,
    ).stdout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repository", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cli", type=Path)
    args = parser.parse_args()
    source = args.source_repository.resolve()
    require(
        git(source, "rev-parse", f"{SOURCE_COMMIT}:{SOURCE_PATH}").strip()
        == PACKAGE_TREE,
        "source pin mismatch",
    )
    inventory: dict[str, bytes] = {}
    for record in git(source, "ls-tree", "-rz", PACKAGE_TREE, binary=True).split(b"\0"):
        if not record:
            continue
        metadata, encoded_path = record.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        require(mode == "100644" and kind == "blob", "unexpected package member mode")
        relative = encoded_path.decode()
        require(
            not Path(relative).is_absolute() and ".." not in Path(relative).parts,
            "unsafe member",
        )
        inventory[relative] = git(source, "cat-file", "blob", oid, binary=True)
    require(len(inventory) == 81, "frozen member count changed")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    calls = []
    with tempfile.TemporaryDirectory(prefix="stdo-v3-cli-") as temporary:
        root = Path(temporary)
        repository = root / "repository"
        project = repository / PROJECT
        for relative, data in inventory.items():
            target = project / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        sibling = (
            repository
            / "specification_methodology/v2/specification/standards/README.md"
        )
        sibling.parent.mkdir(parents=True)
        sibling.write_text("# Unselected sibling\n")
        git(repository, "init", "-q", "--object-format=sha1", "-b", "fixture")
        git(repository, "add", ".")
        git(
            repository,
            "commit",
            "-qm",
            "Isolated common-package installer fixture; not a release",
        )
        git(
            repository,
            "tag",
            "-a",
            f"specification_methodology/{CUT}",
            "-m",
            "Isolated installer test only",
        )
        require(
            git(repository, "rev-parse", f"HEAD:{PROJECT}").strip() == PACKAGE_TREE,
            "re-rooting changed package bytes",
        )
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        if args.cli:
            command = [str(args.cli.resolve())]
            environment.pop("PYTHONPATH", None)
        else:
            command = [sys.executable, "-m", "stdo_toolchain.cli"]
            project_source = Path(__file__).resolve().parents[4]
            environment["PYTHONPATH"] = str(project_source / "src")

        def cli(*arguments: str, expected: int = 0, store: str = "store") -> dict:
            completed = subprocess.run(
                [*command, "--store", str(root / store), *arguments],
                env=environment,
                cwd=root,
                capture_output=True,
                text=True,
            )
            require(
                completed.returncode == expected,
                f"{arguments}: exit {completed.returncode}, expected {expected}\n{completed.stdout}\n{completed.stderr}",
            )
            value = json.loads(completed.stdout)
            calls.append(
                {
                    "arguments": list(arguments),
                    "store": store,
                    "exit_code": completed.returncode,
                    "result": value,
                }
            )
            return value

        version = subprocess.run(
            [*command, "--version"],
            env=environment,
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        planned = cli("manifest", CUT, "--repository", str(repository))
        manifest = planned["manifest"]
        digest = planned["manifest_sha256"]
        require(manifest["standards"]["member_count"] == 62, "standards count")
        require(manifest["auxiliary"]["plugin"]["member_count"] == 17, "plugin count")
        require(
            manifest["standards"]["member_set_sha256"] == STANDARDS_DIGEST,
            "canonical digest changed",
        )
        require(
            manifest["release"]["project_subtree_tree"] == PACKAGE_TREE,
            "wrong project tree",
        )
        cli(
            "install", CUT, "--repository", str(repository), "--manifest-sha256", digest
        )
        installed_root = root / "store/releases" / CUT
        observed = {
            path.relative_to(installed_root).as_posix(): path.read_bytes()
            for path in installed_root.rglob("*")
            if path.is_file() and path.name != "manifest.json"
        }
        require(observed == inventory, "installed bytes differ from frozen common")
        require(
            json.loads((installed_root / "manifest.json").read_bytes()) == manifest,
            "planned manifest differs from installed",
        )
        require(
            cli("verify", CUT, "--manifest-sha256", digest)["valid"], "verify failed"
        )
        cli("list")
        require(
            cli(
                "install",
                CUT,
                "--repository",
                str(repository),
                "--manifest-sha256",
                digest,
            )["status"]
            == "already_installed",
            "repeat install changed behavior",
        )
        for relative in (
            "standards/README.md",
            "standards/frames/bootstrap.md",
            "plugins/spec/skills/stdo-work/SKILL.md",
        ):
            cli("resolve", f"stdo://releases/{CUT}/{relative}")

        consumer = root / "consumer"
        consumer.mkdir()
        template = inventory[
            "standards/templates/PRODUCT_DEFINITION_TEMPLATE.json"
        ].decode()
        definition = json.loads(
            template.replace("REPLACE_WITH_IMMUTABLE_CUT", CUT)
            .replace("REPLACE_WITH_VERSION_LINE", "3.0.0")
            .replace("REPLACE_WITH_64_LOWERCASE_HEX_SHA256", digest)
        )
        definition["constitution"]["stdo"]["source"]["repository"] = str(repository)
        definition_path = consumer / "stdo_default.json"
        definition_path.write_text(json.dumps(definition, indent=2) + "\n")
        definition_before = definition_path.read_bytes()
        cli("sync", "--definition", str(definition_path), store="consumer-store")
        require(
            definition_path.read_bytes() == definition_before, "sync edited consumer"
        )
        require(
            cli(
                "status",
                "--definition",
                str(definition_path),
                "--verify",
                store="consumer-store",
            )["valid"],
            "consumer schema/integrity check failed",
        )
        for entry in definition["constitution"]["entrypoints"]:
            cli(
                "resolve",
                f"stdo://releases/{CUT}/{entry['uri']}",
                store="consumer-store",
            )
        cli("bootstrap", "--definition", str(definition_path), store="consumer-store")
        before = {
            name: (consumer / name).read_bytes() for name in ("AGENTS.md", "CLAUDE.md")
        }
        cli("bootstrap", "--definition", str(definition_path), store="consumer-store")
        require(
            before == {name: (consumer / name).read_bytes() for name in before},
            "bootstrap not idempotent",
        )
        for relative in (
            "authority_compressions/stdo_bootstrap.md",
            "REFERENCE_FRAME_METHOD.md",
            "STDO_REFERENCE_FRAME_BASELINE.md",
        ):
            cli("resolve", f"stdo://releases/{CUT}/standards/{relative}", expected=2)

        damaged = installed_root / "standards/EXECUTIVE_BASELINE.md"
        original_mode = damaged.stat().st_mode & 0o777
        damaged.chmod(0o644)
        damaged.write_bytes(damaged.read_bytes() + b"\nchanged\n")
        require(
            not cli("verify", CUT, "--manifest-sha256", digest, expected=1)["valid"],
            "tamper was accepted",
        )
        cli(
            "resolve",
            f"stdo://releases/{CUT}/standards/EXECUTIVE_BASELINE.md",
            expected=2,
        )
        cli(
            "install",
            CUT,
            "--repository",
            str(repository),
            "--manifest-sha256",
            digest,
            expected=2,
        )
        damaged.write_bytes(inventory["standards/EXECUTIVE_BASELINE.md"])
        damaged.chmod(original_mode)
        require(
            cli("verify", CUT, "--manifest-sha256", digest)["valid"],
            "restored fixture failed",
        )
        receipt = {
            "result": "pass",
            "scope": "installer compatibility only; isolated test refs, stores and consumers",
            "toolchain": version,
            "source_commit": SOURCE_COMMIT,
            "source_path": SOURCE_PATH,
            "package_tree": PACKAGE_TREE,
            "payload_members": len(inventory),
            "standards_members": 62,
            "plugin_members": 17,
            "fixture_manifest_sha256": digest,
            "fixture_release": manifest["release"],
            "canonical_standards_digest": STANDARDS_DIGEST,
            "excluded_products_present": False,
            "calls": calls,
        }
        # Machine-local temporary coordinates are observations, not replay inputs.
        serialized = (
            json.dumps(receipt, indent=2, sort_keys=True).replace(
                str(root), "<fixture>"
            )
            + "\n"
        )
        (output / "cli-replay.json").write_text(serialized)
        (output / "fixture-manifest.json").write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n"
        )
        print(
            json.dumps(
                {key: value for key, value in receipt.items() if key != "calls"},
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
