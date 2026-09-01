from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "plugins/spec/references/GETTING_STARTED.md"
QUICKSTART = ROOT / "QUICKSTART.md"


def setup_script() -> str:
    guide = GUIDE.read_text(encoding="utf-8")
    marker = (
        '"$STDO_FRAME_TEMPLATE_PATH" '
        "./specification/REFERENCE_FRAME_BASIS.md <<'PY'\n"
    )
    start = guide.index(marker) + len(marker)
    end = guide.index("\nPY\n```", start)
    return guide[start:end]


def snapshot(root: Path) -> dict[str, tuple[str, bytes | None]]:
    result: dict[str, tuple[str, bytes | None]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        result[relative] = (
            ("directory", None) if path.is_dir() else ("file", path.read_bytes())
        )
    return result


class GettingStartedSetupTests(unittest.TestCase):
    def test_quickstart_routes_to_the_one_atomic_setup_transaction(self) -> None:
        quickstart = QUICKSTART.read_text(encoding="utf-8")

        self.assertIn("## 3. Install Both Project Templates", quickstart)
        self.assertIn("Do not copy either target separately", quickstart)
        self.assertIn(
            "plugins/spec/references/GETTING_STARTED.md#new-project", quickstart
        )
        self.assertNotIn(
            'python3 - "$STDO_TEMPLATE_PATH" ./stdo_default.json', quickstart
        )
        self.assertNotIn('python3 - "$STDO_FRAME_BASIS_TEMPLATE"', quickstart)

    def test_second_target_collision_leaves_no_new_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first_source = root / "product-template.json"
            second_source = root / "frame-template.md"
            first_source.write_bytes(b'{"template": true}\n')
            second_source.write_bytes(b"# frame template\n")
            specification = root / "specification"
            specification.mkdir()
            collision = specification / "REFERENCE_FRAME_BASIS.md"
            collision.write_bytes(b"accepted existing basis\n")
            before = snapshot(root)

            result = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    setup_script(),
                    str(first_source),
                    str(root / "stdo_default.json"),
                    str(second_source),
                    str(collision),
                ],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("refusing to overwrite", result.stderr)
            self.assertEqual(snapshot(root), before)

    def test_success_publishes_both_exact_templates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first_source = root / "product-template.json"
            second_source = root / "frame-template.md"
            first_payload = b'{"template": true}\n'
            second_payload = b"# frame template\n"
            first_source.write_bytes(first_payload)
            second_source.write_bytes(second_payload)
            project = root / "new-project"
            first_target = project / "stdo_default.json"
            second_target = project / "specification/REFERENCE_FRAME_BASIS.md"

            result = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    setup_script(),
                    str(first_source),
                    str(first_target),
                    str(second_source),
                    str(second_target),
                ],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(first_target.read_bytes(), first_payload)
            self.assertEqual(second_target.read_bytes(), second_payload)
            self.assertEqual(list(project.rglob("*.stdo-stage-*")), [])

    def test_publish_failure_rolls_back_only_invocation_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first_source = root / "product-template.json"
            second_source = root / "frame-template.md"
            first_source.write_bytes(b'{"template": true}\n')
            second_source.write_bytes(b"# frame template\n")
            project = root / "new-project"
            first_target = project / "stdo_default.json"
            second_target = project / "specification/REFERENCE_FRAME_BASIS.md"
            before = snapshot(root)
            real_replace = os.replace
            replacements = 0

            def fail_second_replace(source: str, target: str) -> None:
                nonlocal replacements
                replacements += 1
                if replacements == 2:
                    raise OSError("injected second publish failure")
                real_replace(source, target)

            old_cwd = Path.cwd()
            try:
                os.chdir(root)
                with mock.patch.object(
                    sys,
                    "argv",
                    [
                        "setup",
                        str(first_source),
                        str(first_target),
                        str(second_source),
                        str(second_target),
                    ],
                ), mock.patch.object(os, "replace", fail_second_replace):
                    with self.assertRaisesRegex(
                        OSError, "injected second publish failure"
                    ):
                        exec(compile(setup_script(), str(GUIDE), "exec"), {})
            finally:
                os.chdir(old_cwd)

            self.assertEqual(snapshot(root), before)

    def test_guide_stops_on_old_toolchain_and_for_owner_ratification(self) -> None:
        guide = GUIDE.read_text(encoding="utf-8")
        shell_start = guide.index("STDO_CUT='v2.5.0-rc.3'")
        shell_end = guide.index("\n```", shell_start)
        toolchain_shell = guide[shell_start:shell_end]

        self.assertIn("STDO_TOOLCHAIN_MIN='0.1.2'", guide)
        self.assertIn(
            "git+https://github.com/foolishimp/specification_methodology.git@"
            "specification_methodology/v2.5.0-rc.3"
            "#subdirectory=specification_methodology",
            guide,
        )
        self.assertIn("pipx install --force", guide)
        self.assertGreaterEqual(guide.count("stdo --version"), 2)
        self.assertIn("Do not continue", guide)
        self.assertIn("stop for Product-owner ratification", guide)
        self.assertIn("drafting agent cannot record", guide)
        self.assertIn(
            "SPEC_PLUGIN_REF='specification_methodology/v2.5.0-rc.3'",
            guide,
        )
        self.assertIn("plugin version and immutable repository cut are aligned", guide)
        syntax = subprocess.run(
            ["bash", "-n"],
            input=toolchain_shell,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(syntax.returncode, 0, syntax.stderr)


if __name__ == "__main__":
    unittest.main()
