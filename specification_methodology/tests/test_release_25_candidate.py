from __future__ import annotations

import hashlib
import re
import subprocess
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
GIT_REPOSITORY = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=REPOSITORY,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
)
RELEASE_TAG = "v2.5.0-rc.1^{}"
RELEASE_NOTE = "releases/v2.5.0.md"
PREDECESSOR = "v2.4.3-rc.3"


def git_bytes(revision: str, relative: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{relative}"],
        cwd=GIT_REPOSITORY,
        check=True,
        capture_output=True,
    ).stdout


def git_paths(revision: str, prefix: str) -> list[str]:
    return subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", revision, prefix],
        cwd=GIT_REPOSITORY,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()


class Release25CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.note = git_bytes(RELEASE_TAG, RELEASE_NOTE).decode("utf-8")
        rows = re.findall(
            r"^\| (conserved|changed|added) \| `([^`]+)` \| `([0-9a-f]{64})` \|$",
            cls.note,
            flags=re.MULTILINE,
        )
        cls.inventory = {
            member: (disposition, digest) for disposition, member, digest in rows
        }

    def test_inventory_is_complete_exact_and_unique(self) -> None:
        members = sorted(
            path.removeprefix("specification/standards/")
            for path in git_paths(RELEASE_TAG, "specification/standards")
        )
        self.assertEqual(len(self.inventory), 51)
        self.assertEqual(sorted(self.inventory), members)
        for member in members:
            released = git_bytes(
                RELEASE_TAG,
                f"specification/standards/{member}",
            )
            self.assertEqual(
                self.inventory[member][1], hashlib.sha256(released).hexdigest()
            )

    def test_inventory_dispositions_match_predecessor(self) -> None:
        predecessor_members = set(git_paths(PREDECESSOR, "specification/standards"))
        current_members = {
            f"specification/standards/{member}" for member in self.inventory
        }
        self.assertTrue(predecessor_members <= current_members)

        counts = {"conserved": 0, "changed": 0, "added": 0}
        for member, (declared, current_digest) in self.inventory.items():
            repository_member = f"specification/standards/{member}"
            if repository_member not in predecessor_members:
                actual = "added"
            else:
                prior = git_bytes(PREDECESSOR, repository_member)
                actual = (
                    "conserved"
                    if hashlib.sha256(prior).hexdigest() == current_digest
                    else "changed"
                )
            self.assertEqual(declared, actual, member)
            counts[actual] += 1
        self.assertEqual(counts, {"conserved": 38, "changed": 9, "added": 4})

    def test_member_stream_aggregate_matches_release_note(self) -> None:
        members = sorted(git_paths(RELEASE_TAG, "specification/standards"))
        member_stream = b"".join(
            (
                f"{hashlib.sha256(git_bytes(RELEASE_TAG, path)).hexdigest()}  "
                f"{path}\n"
            ).encode()
            for path in members
        )
        aggregate = hashlib.sha256(member_stream).hexdigest()
        self.assertIn(f"`{aggregate}`", self.note)

    def test_protected_inputs_match_release_note(self) -> None:
        for relative in (
            "specification/INTENT.md",
            "specification/PRODUCT.md",
            "specification/REFERENCE_FRAME_BASIS.md",
            "stdo_default.json",
        ):
            pattern = rf"^\| `{re.escape(relative)}` \| `([0-9a-f]{{64}})` \|$"
            match = re.search(pattern, self.note, flags=re.MULTILINE)
            self.assertIsNotNone(match, relative)
            released = git_bytes(RELEASE_TAG, relative)
            self.assertEqual(match.group(1), hashlib.sha256(released).hexdigest())


if __name__ == "__main__":
    unittest.main()
