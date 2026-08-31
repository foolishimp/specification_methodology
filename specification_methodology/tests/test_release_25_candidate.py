from __future__ import annotations

import hashlib
import re
import subprocess
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GIT_REPOSITORY = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
)
PROJECT_SUBTREE = PROJECT_ROOT.relative_to(GIT_REPOSITORY).as_posix()
PROJECT_NAMESPACE = "specification_methodology"
RELEASE_REF = "refs/tags/specification_methodology/v2.5.0-rc.2"
SELECTOR_REF = "refs/tags/specification_methodology/v2.5.0"
RC_BRANCH = "refs/heads/rc/specification_methodology/2.5.0"
RELEASE_BRANCH = "refs/heads/release/specification_methodology/2.5.0"
PREDECESSOR_REF = "refs/tags/v2.5.0-rc.1"
PREDECESSOR_TAG_OBJECT = "42f59b6cd24071d9c445a29ae2a691cf0828211e"
PREDECESSOR_COMMIT = "ca6694314c4e9a56d3facae3eef06fe2792104c9"
RELEASE_NOTE = "releases/v2.5.0.md"


def run_git(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *arguments],
        cwd=GIT_REPOSITORY,
        check=check,
        capture_output=True,
        text=True,
    )


def ref_exists(ref: str) -> bool:
    return run_git("show-ref", "--verify", "--quiet", ref, check=False).returncode == 0


def git_revision(revision: str) -> str:
    return run_git("rev-parse", revision).stdout.strip()


def git_type(revision: str) -> str:
    return run_git("cat-file", "-t", revision).stdout.strip()


def git_bytes(revision: str, repository_relative: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{repository_relative}"],
        cwd=GIT_REPOSITORY,
        check=True,
        capture_output=True,
    ).stdout


def git_paths(revision: str, repository_prefix: str) -> list[str]:
    return run_git(
        "ls-tree", "-r", "--name-only", revision, repository_prefix
    ).stdout.splitlines()


def qualified_path(project_relative: str) -> str:
    if PROJECT_SUBTREE == ".":
        return project_relative
    return f"{PROJECT_SUBTREE}/{project_relative}"


PUBLISHED = ref_exists(RELEASE_REF)
SUBJECT_REVISION = f"{RELEASE_REF}^{{}}" if PUBLISHED else None


def subject_bytes(project_relative: str) -> bytes:
    if SUBJECT_REVISION is not None:
        return git_bytes(SUBJECT_REVISION, qualified_path(project_relative))
    return (PROJECT_ROOT / project_relative).read_bytes()


def subject_paths(project_prefix: str) -> list[str]:
    if SUBJECT_REVISION is not None:
        repository_prefix = qualified_path(project_prefix)
        paths = git_paths(SUBJECT_REVISION, repository_prefix)
        if PROJECT_SUBTREE == ".":
            return paths
        subtree_prefix = f"{PROJECT_SUBTREE}/"
        return [path.removeprefix(subtree_prefix) for path in paths]

    root = PROJECT_ROOT / project_prefix
    return sorted(
        file.relative_to(PROJECT_ROOT).as_posix()
        for file in root.rglob("*")
        if file.is_file()
    )


def predecessor_bytes(project_relative: str) -> bytes:
    return git_bytes(f"{PREDECESSOR_REF}^{{}}", project_relative)


class Release25CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.note = subject_bytes(RELEASE_NOTE).decode("utf-8")
        rows = re.findall(
            r"^\| (conserved|changed|added) \| `([^`]+)` \| `([0-9a-f]{64})` \|$",
            cls.note,
            flags=re.MULTILINE,
        )
        cls.inventory = {
            member: (disposition, digest) for disposition, member, digest in rows
        }

    def test_accepted_predecessor_identity_is_exact(self) -> None:
        self.assertEqual(git_type(PREDECESSOR_REF), "tag")
        self.assertEqual(git_revision(PREDECESSOR_REF), PREDECESSOR_TAG_OBJECT)
        self.assertEqual(git_revision(f"{PREDECESSOR_REF}^{{}}"), PREDECESSOR_COMMIT)

    def test_inventory_is_complete_exact_and_unique(self) -> None:
        members = sorted(
            path.removeprefix("specification/standards/")
            for path in subject_paths("specification/standards")
        )
        self.assertEqual(len(self.inventory), 52)
        self.assertEqual(sorted(self.inventory), members)
        for member in members:
            released = subject_bytes(f"specification/standards/{member}")
            self.assertEqual(
                self.inventory[member][1], hashlib.sha256(released).hexdigest()
            )

    def test_inventory_dispositions_match_accepted_rc1(self) -> None:
        predecessor_members = set(
            git_paths(f"{PREDECESSOR_REF}^{{}}", "specification/standards")
        )
        current_members = {
            f"specification/standards/{member}" for member in self.inventory
        }
        self.assertTrue(predecessor_members <= current_members)

        counts = {"conserved": 0, "changed": 0, "added": 0}
        for member, (declared, current_digest) in self.inventory.items():
            project_relative = f"specification/standards/{member}"
            if project_relative not in predecessor_members:
                actual = "added"
            else:
                prior_digest = hashlib.sha256(
                    predecessor_bytes(project_relative)
                ).hexdigest()
                actual = "conserved" if prior_digest == current_digest else "changed"
            self.assertEqual(declared, actual, member)
            counts[actual] += 1
        self.assertEqual(counts, {"conserved": 36, "changed": 15, "added": 1})

    def test_project_relative_member_stream_aggregate_matches_note(self) -> None:
        members = sorted(subject_paths("specification/standards"))
        member_stream = b"".join(
            (
                f"{hashlib.sha256(subject_bytes(member)).hexdigest()}  " f"{member}\n"
            ).encode()
            for member in members
        )
        aggregate = hashlib.sha256(member_stream).hexdigest()
        self.assertEqual(
            aggregate,
            "a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7",
        )
        self.assertIn(f"`{aggregate}`", self.note)

    def test_protected_inputs_match_release_note(self) -> None:
        for project_relative in (
            "specification/INTENT.md",
            "specification/PRODUCT.md",
            "specification/REFERENCE_FRAME_BASIS.md",
            "stdo_default.json",
        ):
            pattern = rf"^\| `{re.escape(project_relative)}` \| `([0-9a-f]{{64}})` \|$"
            match = re.search(pattern, self.note, flags=re.MULTILINE)
            self.assertIsNotNone(match, project_relative)
            self.assertEqual(
                match.group(1),
                hashlib.sha256(subject_bytes(project_relative)).hexdigest(),
            )

    def test_toolchain_012_delta_is_digest_bound(self) -> None:
        for project_relative in (
            "pyproject.toml",
            "src/stdo_toolchain/__init__.py",
            "src/stdo_toolchain/git_source.py",
            "src/stdo_toolchain/manifest.py",
            "design/TOOLCHAIN_MANAGER.md",
            "tests/test_toolchain.py",
        ):
            pattern = rf"^\| `{re.escape(project_relative)}` \| `([0-9a-f]{{64}})` \|$"
            match = re.search(pattern, self.note, flags=re.MULTILINE)
            self.assertIsNotNone(match, project_relative)
            self.assertEqual(
                match.group(1),
                hashlib.sha256(subject_bytes(project_relative)).hexdigest(),
            )
        self.assertIn('version = "0.1.2"', subject_bytes("pyproject.toml").decode())
        self.assertIn(
            '__version__ = "0.1.2"',
            subject_bytes("src/stdo_toolchain/__init__.py").decode(),
        )

    def test_release_identity_uses_project_qualified_transport(self) -> None:
        for exact_text in (
            "Project Release Namespace | `specification_methodology`",
            "Project Subtree root | `specification_methodology`",
            "`refs/tags/specification_methodology/v2.5.0-rc.2`",
            "`refs/tags/specification_methodology/v2.5.0`",
            "`refs/heads/rc/specification_methodology/2.5.0`",
            "`refs/heads/release/specification_methodology/2.5.0`",
            "`stdo://releases/v2.5.0-rc.2/`",
        ):
            self.assertIn(exact_text, self.note)

    @unittest.skipUnless(PUBLISHED, "qualified RC2 has not been published locally")
    def test_published_rc2_is_annotated_and_subtree_bound(self) -> None:
        self.assertEqual(git_type(RELEASE_REF), "tag")
        self.assertEqual(git_type(SELECTOR_REF), "tag")
        released_commit = git_revision(f"{RELEASE_REF}^{{}}")
        self.assertEqual(git_revision(f"{SELECTOR_REF}^{{}}"), released_commit)
        self.assertEqual(git_revision(RC_BRANCH), released_commit)
        self.assertEqual(git_revision(RELEASE_BRANCH), released_commit)
        self.assertEqual(git_type(f"{released_commit}:{PROJECT_SUBTREE}"), "tree")


if __name__ == "__main__":
    unittest.main()
