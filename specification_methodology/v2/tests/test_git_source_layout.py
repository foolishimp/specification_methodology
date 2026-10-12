"""Project-root selection across the legacy, nested and versioned layouts."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from stdo_toolchain.errors import StdoError
from stdo_toolchain.git_source import GitSnapshot


def _git(root: Path, *arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


class LayoutRepository:
    """One throwaway repository whose commits carry selected STDO layouts."""

    def __init__(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="stdo-layout-")
        self.root = Path(self.temporary.name)
        _git(self.root, "init", "-q")
        _git(self.root, "config", "user.name", "Test")
        _git(self.root, "config", "user.email", "test@example.invalid")

    def close(self) -> None:
        self.temporary.cleanup()

    def commit_layouts(self, *project_roots: str) -> None:
        for project_root in project_roots:
            standards = self.root / project_root / "specification" / "standards"
            standards.mkdir(parents=True, exist_ok=True)
            (standards / "README.md").write_text(
                f"# {project_root or 'legacy'}\n", encoding="utf-8"
            )
        _git(self.root, "add", ".")
        _git(self.root, "commit", "-qm", f"layouts: {', '.join(project_roots)}")

    def tag(self, cut: str) -> None:
        _git(
            self.root,
            "tag",
            "-a",
            f"specification_methodology/{cut}",
            "-m",
            cut,
        )

    def remove_layout(self, project_root: str) -> None:
        _git(self.root, "rm", "-rq", project_root or "specification")
        _git(self.root, "commit", "-qm", f"remove {project_root or 'legacy'}")


class ProjectRootSelectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = LayoutRepository()

    def tearDown(self) -> None:
        self.repository.close()

    def snapshot_root(self, cut: str) -> str:
        with GitSnapshot(str(self.repository.root), cut) as snapshot:
            return snapshot.project_root

    def test_nested_root_still_selected_for_historical_cuts(self) -> None:
        self.repository.commit_layouts("specification_methodology")
        self.repository.tag("v2.5.1-rc.9")
        self.assertEqual(
            self.snapshot_root("v2.5.1-rc.9"), "specification_methodology"
        )

    def test_versioned_root_selected_by_major_version(self) -> None:
        self.repository.commit_layouts(
            "specification_methodology/v2", "specification_methodology/v3"
        )
        self.repository.tag("v2.6.0-rc.1")
        self.repository.tag("v3.0.0-rc.1")
        self.assertEqual(
            self.snapshot_root("v2.6.0-rc.1"), "specification_methodology/v2"
        )
        self.assertEqual(
            self.snapshot_root("v3.0.0-rc.1"), "specification_methodology/v3"
        )

    def test_nested_and_versioned_roots_together_are_ambiguous(self) -> None:
        self.repository.commit_layouts(
            "specification_methodology", "specification_methodology/v2"
        )
        self.repository.tag("v2.6.0-rc.1")
        with self.assertRaises(StdoError) as raised:
            self.snapshot_root("v2.6.0-rc.1")
        self.assertIn("exactly one STDO project layout", str(raised.exception))

    def test_missing_version_line_is_reported(self) -> None:
        self.repository.commit_layouts("specification_methodology/v2")
        self.repository.tag("v3.0.0-rc.1")
        with self.assertRaises(StdoError) as raised:
            self.snapshot_root("v3.0.0-rc.1")
        self.assertIn("specification_methodology/v3", str(raised.exception))
        self.assertIn("found none", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
