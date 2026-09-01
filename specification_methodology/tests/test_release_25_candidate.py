from __future__ import annotations

import hashlib
import json
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
RELEASE_REF = "refs/tags/specification_methodology/v2.5.0-rc.3"
SELECTOR_REF = "refs/tags/specification_methodology/v2.5.0"
RC_BRANCH = "refs/heads/rc/specification_methodology/2.5.0"
RELEASE_BRANCH = "refs/heads/release/specification_methodology/2.5.0"
IMMEDIATE_PREDECESSOR_REF = "refs/tags/specification_methodology/v2.5.0-rc.2"
IMMEDIATE_PREDECESSOR_TAG_OBJECT = "5ebd2d87ff0c0d9fcca96ba42d90253ba6fec7e3"
IMMEDIATE_PREDECESSOR_COMMIT = "2c9a11701d567d01320482100979c9fcd54ab846"
IMMEDIATE_PREDECESSOR_REPOSITORY_TREE = "374813552b319254d615de8b1c29fa0a99ec4e9b"
IMMEDIATE_PREDECESSOR_SUBTREE = "b416e6f6819e8dbff7497a5ab92f32df131804f8"
IMMEDIATE_PREDECESSOR_STANDARDS_TREE = "f636fd8dcc234e05b8aa464a35f24d843c258dc9"
ACCEPTED_BASELINE_REF = "refs/tags/v2.5.0-rc.1"
ACCEPTED_BASELINE_TAG_OBJECT = "42f59b6cd24071d9c445a29ae2a691cf0828211e"
ACCEPTED_BASELINE_COMMIT = "ca6694314c4e9a56d3facae3eef06fe2792104c9"
RELEASE_NOTE = "releases/v2.5.0.md"
STANDARDS_AGGREGATE = "8492f66bba93a1e4559b2275f01df277b5e49c24bc0a76feb028e85e4bdf5c2f"
PLUGIN_AGGREGATE = "687d2be85872a839c581d5a53aa076f8cd3cfd57b3991b4a95365ce46cad9e61"


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


def immediate_predecessor_bytes(project_relative: str) -> bytes:
    return git_bytes(
        f"{IMMEDIATE_PREDECESSOR_REF}^{{}}", qualified_path(project_relative)
    )


def immediate_predecessor_paths(project_prefix: str) -> list[str]:
    repository_prefix = qualified_path(project_prefix)
    paths = git_paths(f"{IMMEDIATE_PREDECESSOR_REF}^{{}}", repository_prefix)
    if PROJECT_SUBTREE == ".":
        return paths
    subtree_prefix = f"{PROJECT_SUBTREE}/"
    return [path.removeprefix(subtree_prefix) for path in paths]


def member_stream_aggregate(members: list[str]) -> str:
    stream = b"".join(
        (
            f"{hashlib.sha256(subject_bytes(member)).hexdigest()}  " f"{member}\n"
        ).encode()
        for member in sorted(members)
    )
    return hashlib.sha256(stream).hexdigest()


def plugin_root_member_stream_aggregate(members: set[str]) -> str:
    stream = b"".join(
        (
            f"{hashlib.sha256(subject_bytes(member)).hexdigest()}  "
            f"./{member.removeprefix('plugins/spec/')}\n"
        ).encode()
        for member in sorted(members)
    )
    return hashlib.sha256(stream).hexdigest()


class Release25RC3CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.note = subject_bytes(RELEASE_NOTE).decode("utf-8")
        standard_rows = re.findall(
            r"^\| (conserved|changed|added) \| `([^`]+)` \| `([0-9a-f]{64})` \|$",
            cls.note,
            flags=re.MULTILINE,
        )
        cls.inventory = {
            member: (disposition, digest)
            for disposition, member, digest in standard_rows
        }
        plugin_rows = re.findall(
            r"^\| plugin \| `([^`]+)` \| `([0-9a-f]{64})` \|$",
            cls.note,
            flags=re.MULTILINE,
        )
        cls.plugin_inventory = {member: digest for member, digest in plugin_rows}

    def test_accepted_rc1_baseline_identity_is_exact(self) -> None:
        self.assertEqual(git_type(ACCEPTED_BASELINE_REF), "tag")
        self.assertEqual(
            git_revision(ACCEPTED_BASELINE_REF), ACCEPTED_BASELINE_TAG_OBJECT
        )
        self.assertEqual(
            git_revision(f"{ACCEPTED_BASELINE_REF}^{{}}"), ACCEPTED_BASELINE_COMMIT
        )
        self.assertIn("The accepted Product baseline remains `v2.5.0-rc.1`", self.note)
        self.assertIn("No accepted\nbaseline claim is silently dropped.", self.note)

    def test_immediate_rc2_predecessor_identity_is_exact(self) -> None:
        self.assertEqual(git_type(IMMEDIATE_PREDECESSOR_REF), "tag")
        self.assertEqual(
            git_revision(IMMEDIATE_PREDECESSOR_REF),
            IMMEDIATE_PREDECESSOR_TAG_OBJECT,
        )
        self.assertEqual(
            git_revision(f"{IMMEDIATE_PREDECESSOR_REF}^{{}}"),
            IMMEDIATE_PREDECESSOR_COMMIT,
        )
        self.assertEqual(
            git_revision(f"{IMMEDIATE_PREDECESSOR_REF}^{{}}^{{tree}}"),
            IMMEDIATE_PREDECESSOR_REPOSITORY_TREE,
        )
        self.assertEqual(
            git_revision(f"{IMMEDIATE_PREDECESSOR_REF}^{{}}:{PROJECT_SUBTREE}"),
            IMMEDIATE_PREDECESSOR_SUBTREE,
        )
        self.assertEqual(
            git_revision(
                f"{IMMEDIATE_PREDECESSOR_REF}^{{}}:"
                f"{qualified_path('specification/standards')}"
            ),
            IMMEDIATE_PREDECESSOR_STANDARDS_TREE,
        )
        self.assertIn(
            "RC2 is the byte-diff basis for\nRC3; RC1 remains the accepted semantic baseline.",
            self.note,
        )

    def test_standard_inventory_is_complete_exact_and_unique(self) -> None:
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

    def test_standard_dispositions_match_immediate_rc2(self) -> None:
        predecessor_members = set(
            immediate_predecessor_paths("specification/standards")
        )
        current_members = {
            f"specification/standards/{member}" for member in self.inventory
        }
        self.assertEqual(predecessor_members, current_members)

        counts = {"conserved": 0, "changed": 0, "added": 0}
        for member, (declared, current_digest) in self.inventory.items():
            project_relative = f"specification/standards/{member}"
            prior_digest = hashlib.sha256(
                immediate_predecessor_bytes(project_relative)
            ).hexdigest()
            actual = "conserved" if prior_digest == current_digest else "changed"
            self.assertEqual(declared, actual, member)
            counts[actual] += 1
        self.assertEqual(counts, {"conserved": 49, "changed": 3, "added": 0})

    def test_accepted_rc1_standard_members_remain_present(self) -> None:
        accepted_members = set(
            git_paths(f"{ACCEPTED_BASELINE_REF}^{{}}", "specification/standards")
        )
        current_members = {
            f"specification/standards/{member}" for member in self.inventory
        }
        self.assertTrue(accepted_members <= current_members)

    def test_standard_member_stream_aggregate_matches_note(self) -> None:
        members = subject_paths("specification/standards")
        self.assertEqual(member_stream_aggregate(members), STANDARDS_AGGREGATE)
        self.assertIn(f"`{STANDARDS_AGGREGATE}`", self.note)

    def test_plugin_inventory_is_complete_exact_and_version_aligned(self) -> None:
        members = subject_paths("plugins/spec")
        relative_members = sorted(
            path.removeprefix("plugins/spec/") for path in members
        )
        self.assertEqual(len(self.plugin_inventory), 17)
        self.assertEqual(sorted(self.plugin_inventory), relative_members)
        for member in relative_members:
            released = subject_bytes(f"plugins/spec/{member}")
            self.assertEqual(
                self.plugin_inventory[member], hashlib.sha256(released).hexdigest()
            )

        for manifest in (
            "plugins/spec/.claude-plugin/plugin.json",
            "plugins/spec/.codex-plugin/plugin.json",
        ):
            payload = json.loads(subject_bytes(manifest))
            self.assertEqual(payload["version"], "2.5.0-rc.3")

    def test_plugin_member_stream_aggregate_and_rc2_delta_match_note(self) -> None:
        current_members = set(subject_paths("plugins/spec"))
        predecessor_members = set(immediate_predecessor_paths("plugins/spec"))
        counts = {"conserved": 0, "changed": 0, "added": 0, "removed": 0}
        for member in current_members:
            if member not in predecessor_members:
                counts["added"] += 1
            elif (
                hashlib.sha256(subject_bytes(member)).digest()
                == hashlib.sha256(immediate_predecessor_bytes(member)).digest()
            ):
                counts["conserved"] += 1
            else:
                counts["changed"] += 1
        counts["removed"] = len(predecessor_members - current_members)
        self.assertEqual(
            counts, {"conserved": 1, "changed": 1, "added": 15, "removed": 1}
        )
        self.assertEqual(
            plugin_root_member_stream_aggregate(current_members), PLUGIN_AGGREGATE
        )
        self.assertIn(f"`{PLUGIN_AGGREGATE}`", self.note)

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

    def test_toolchain_012_is_conserved_and_proof_is_digest_bound(self) -> None:
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
        for executable_input in (
            "pyproject.toml",
            "src/stdo_toolchain/__init__.py",
            "src/stdo_toolchain/git_source.py",
            "src/stdo_toolchain/manifest.py",
            "design/TOOLCHAIN_MANAGER.md",
        ):
            self.assertEqual(
                hashlib.sha256(subject_bytes(executable_input)).hexdigest(),
                hashlib.sha256(
                    immediate_predecessor_bytes(executable_input)
                ).hexdigest(),
            )

    def test_release_identity_uses_rc3_project_qualified_transport(self) -> None:
        for exact_text in (
            "Project Release Namespace | `specification_methodology`",
            "Project Subtree root | `specification_methodology`",
            "`refs/tags/specification_methodology/v2.5.0-rc.3`",
            "`refs/tags/specification_methodology/v2.5.0`",
            "`refs/heads/rc/specification_methodology/2.5.0`",
            "`refs/heads/release/specification_methodology/2.5.0`",
            "`stdo://releases/v2.5.0-rc.3/`",
        ):
            self.assertIn(exact_text, self.note)
        self.assertEqual(self.note.count("`pending-freeze`"), 6)

    @unittest.skipUnless(PUBLISHED, "qualified RC3 has not been published locally")
    def test_published_rc3_is_annotated_subtree_bound_and_retained(self) -> None:
        self.assertEqual(git_type(RELEASE_REF), "tag")
        self.assertEqual(git_type(SELECTOR_REF), "tag")
        released_commit = git_revision(f"{RELEASE_REF}^{{}}")
        for moving_ref in (SELECTOR_REF, RC_BRANCH, RELEASE_BRANCH):
            moving_commit = git_revision(f"{moving_ref}^{{}}")
            self.assertEqual(
                run_git(
                    "merge-base",
                    "--is-ancestor",
                    released_commit,
                    moving_commit,
                    check=False,
                ).returncode,
                0,
                moving_ref,
            )
        self.assertEqual(git_type(f"{released_commit}:{PROJECT_SUBTREE}"), "tree")
        self.assertNotEqual(released_commit, IMMEDIATE_PREDECESSOR_COMMIT)


if __name__ == "__main__":
    unittest.main()
