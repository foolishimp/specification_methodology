from __future__ import annotations

import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GIT_ROOT = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
)
PROJECT_SUBTREE = PROJECT_ROOT.relative_to(GIT_ROOT).as_posix()
PREDECESSOR = "refs/tags/specification_methodology/v2.5.0-rc.3^{}"
TARGET_VERSION = "2.5.0-rc.4"
TARGET_CUT = f"v{TARGET_VERSION}"
RELEASE_NOTE = PROJECT_ROOT / "releases/v2.5.0.md"
STANDARDS = PROJECT_ROOT / "specification/standards"
PLUGIN = PROJECT_ROOT / "plugins/spec"


def git_bytes(revision: str, project_relative: str) -> bytes:
    repository_relative = f"{PROJECT_SUBTREE}/{project_relative}"
    return subprocess.run(
        ["git", "show", f"{revision}:{repository_relative}"],
        cwd=GIT_ROOT,
        check=True,
        capture_output=True,
    ).stdout


def aggregate(rows: list[tuple[str, str]]) -> str:
    stream = "".join(f"{digest}  {path}\n" for path, digest in sorted(rows))
    return hashlib.sha256(stream.encode()).hexdigest()


class Release25RC4CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.note = RELEASE_NOTE.read_text(encoding="utf-8")

    def test_release_identity_is_successor_not_rc3_rewrite(self) -> None:
        for value in (
            "fourth immutable candidate",
            f"product-local cut name is `{TARGET_CUT}`",
            f"`refs/tags/specification_methodology/{TARGET_CUT}`",
            f"`stdo://releases/{TARGET_CUT}/`",
            "exact RC3 record\nremains the blob selected by its immutable tag",
        ):
            self.assertIn(value, self.note)

    def test_standard_inventory_is_exact_and_matches_rc3_delta(self) -> None:
        rows = re.findall(
            r"^\| (conserved|changed|added) \| `([^`]+)` \| `([0-9a-f]{64})` \|$",
            self.note,
            flags=re.MULTILINE,
        )
        inventory = {
            member: (disposition, digest) for disposition, member, digest in rows
        }
        members = sorted(
            path.relative_to(STANDARDS).as_posix()
            for path in STANDARDS.rglob("*")
            if path.is_file()
        )
        self.assertEqual(len(inventory), 52)
        self.assertEqual(sorted(inventory), members)

        counts = {"conserved": 0, "changed": 0, "added": 0}
        stream_rows: list[tuple[str, str]] = []
        for member in members:
            current = (STANDARDS / member).read_bytes()
            digest = hashlib.sha256(current).hexdigest()
            self.assertEqual(inventory[member][1], digest, member)
            prior = git_bytes(PREDECESSOR, f"specification/standards/{member}")
            actual = "conserved" if current == prior else "changed"
            self.assertEqual(inventory[member][0], actual, member)
            counts[actual] += 1
            stream_rows.append((f"specification/standards/{member}", digest))

        self.assertEqual(counts, {"conserved": 49, "changed": 3, "added": 0})
        self.assertIn(f"`{aggregate(stream_rows)}`", self.note)

    def test_plugin_inventory_and_versions_are_exact(self) -> None:
        rows = re.findall(
            r"^\| plugin \| `([^`]+)` \| `([0-9a-f]{64})` \|$",
            self.note,
            flags=re.MULTILINE,
        )
        inventory = dict(rows)
        members = sorted(
            path.relative_to(PLUGIN).as_posix()
            for path in PLUGIN.rglob("*")
            if path.is_file()
        )
        self.assertEqual(len(inventory), 17)
        self.assertEqual(sorted(inventory), members)

        stream_rows: list[tuple[str, str]] = []
        changed = 0
        for member in members:
            current = (PLUGIN / member).read_bytes()
            digest = hashlib.sha256(current).hexdigest()
            self.assertEqual(inventory[member], digest, member)
            prior = git_bytes(PREDECESSOR, f"plugins/spec/{member}")
            changed += current != prior
            stream_rows.append((f"./{member}", digest))
        self.assertEqual(changed, 3)
        self.assertIn(f"`{aggregate(stream_rows)}`", self.note)

        for relative in (
            ".claude-plugin/plugin.json",
            ".codex-plugin/plugin.json",
        ):
            self.assertEqual(
                json.loads((PLUGIN / relative).read_bytes())["version"], TARGET_VERSION
            )

    def test_release_method_and_owned_compression_are_the_only_standard_changes(
        self,
    ) -> None:
        changed = re.findall(
            r"^\| changed \| `([^`]+)` \| `[0-9a-f]{64}` \|$",
            self.note,
            flags=re.MULTILINE,
        )
        self.assertEqual(
            changed,
            [
                "RELEASE_METHOD.md",
                "authority_compressions/stdo_bootstrap.md",
                "authority_compressions/stdo_compressed.md",
            ],
        )


if __name__ == "__main__":
    unittest.main()
