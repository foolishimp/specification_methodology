"""Source-independent boundary controls; all temporary files stay in this territory."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("native_release", HERE / "native_release.py")
n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n)


def sample():
    blobs = {"LICENSE": b"license\n", "release/release-note.md": b"test candidate\n", "standards/README.md": b"method\n",
             "plugins/spec/.claude-plugin/plugin.json": b'{"version":"3.0.1-rc.1"}\n',
             "plugins/spec/.codex-plugin/plugin.json": b'{"version":"3.0.1-rc.1"}\n'}
    rows = [{"path": path, "bytes": len(raw), "sha256": n.sha(raw), "git_mode": "100644", "git_blob": str(i + 1).zfill(40)} for i, (path, raw) in enumerate(sorted(blobs.items()))]
    return rows, blobs


class BoundaryControls(unittest.TestCase):
    def setUp(self):
        (HERE / "scratch").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="controls-", dir=HERE / "scratch")
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_git_mutations_are_refused_before_subprocess(self):
        with patch.object(n.subprocess, "run") as run:
            for action in ("push", "tag", "commit-tree", "update-index", "fetch", "checkout"):
                with self.assertRaises(ValueError):
                    n.git(self.root, action)
            run.assert_not_called()

    def test_member_path_traversal_and_control_characters_refuse(self):
        for value in ("../x", "/x", "x//y", "x/./y", "x\\y", "x\ny", ""):
            with self.assertRaises(ValueError):
                n.safe_member(value)

    def test_output_escape_and_symlink_refuse(self):
        for path in (Path("/tmp/outside-native-proof"), self.root / ".." / "escape"):
            with self.assertRaises(ValueError):
                n.output_path(path)
        (self.root / "redirect").symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            n.output_path(self.root / "redirect" / "new.json")

    def test_symlink_git_mode_refuses(self):
        raw = b"120000 blob " + b"1" * 40 + b"\tstandards/link\0"
        with patch.object(n, "git", return_value=raw), self.assertRaises(ValueError):
            n.tree_rows(self.root, "tree")

    def test_payload_required_members_and_extras(self):
        rows, data = sample()
        n.validate_payload(rows, data)
        with self.assertRaises(ValueError):
            n.validate_payload([r for r in rows if r["path"] != "release/release-note.md"], data)
        with self.assertRaises(ValueError):
            n.validate_payload(rows + [{"path": "source-record.json"}], data)

    def test_plugin_wrong_version_refuses(self):
        rows, data = sample()
        data["plugins/spec/.claude-plugin/plugin.json"] = b'{"version":"3.0.0-rc.1"}'
        with self.assertRaises(ValueError):
            n.validate_payload(rows, data)

    def test_case_collision_refuses(self):
        rows, data = sample()
        with self.assertRaises(ValueError):
            n.validate_payload(rows + [{"path": "standards/readme.md"}], data)

    def test_inventory_digest_covers_bytes_not_just_paths(self):
        rows, _ = sample()
        original = n.inventory_digest(rows)
        changed = [dict(row) for row in rows]
        changed[0]["sha256"] = "0" * 64
        self.assertNotEqual(original, n.inventory_digest(changed))

    def test_file_comparison_refuses_omission_extra_and_mutation(self):
        expected = {"a": {"bytes": 1, "sha256": "a"}}
        n.compare_files(dict(expected), expected)
        for actual in ({}, {**expected, "b": expected["a"]}, {"a": {"bytes": 1, "sha256": "b"}}):
            with self.assertRaises(ValueError):
                n.compare_files(actual, expected)

    def test_native_wrong_parent_refuses(self):
        with patch.object(n, "commit"), patch.object(n, "text_git", return_value="2" * 40), self.assertRaises(ValueError):
            n.native_facts(self.root, "1" * 40, {})

    def test_native_extra_root_path_refuses(self):
        rows, _ = sample()
        actual = [{"path": n.PREFIX + "/" + r["path"], "git_mode": r["git_mode"], "git_blob": r["git_blob"]} for r in rows]
        actual.append({"path": "unrelated/file", "git_mode": "100644", "git_blob": "a" * 40})
        with patch.object(n, "commit"), patch.object(n, "text_git", return_value=n.PREDECESSOR), patch.object(n, "tree_rows", return_value=actual), self.assertRaises(ValueError):
            n.native_facts(self.root, "1" * 40, {"files": rows})

    def test_native_changed_mode_refuses(self):
        rows, _ = sample()
        actual = [{"path": n.PREFIX + "/" + r["path"], "git_mode": r["git_mode"], "git_blob": r["git_blob"]} for r in rows]
        actual[0]["git_mode"] = "100755"
        with patch.object(n, "commit"), patch.object(n, "text_git", return_value=n.PREDECESSOR), patch.object(n, "tree_rows", return_value=actual), self.assertRaises(ValueError):
            n.native_facts(self.root, "1" * 40, {"files": rows})

    def native_fixture(self, *, annotation=None, tag_type="tag"):
        rows, _ = sample()
        selected = {"commit": "a" * 40, "package_path": "source/common", "package_tree": "b" * 40}
        source = {"files": rows, "source_candidate": selected}
        actual = [{"path": n.PREFIX + "/" + r["path"], "git_mode": r["git_mode"], "git_blob": r["git_blob"]} for r in rows]
        message = "\n".join(f"{k}: {v}" for k, v in (("Frozen-Source-Commit", selected["commit"]), ("Frozen-Source-Path", selected["package_path"]), ("Frozen-Source-Tree", selected["package_tree"]), ("Predecessor-Native-Commit", n.PREDECESSOR)))
        values = {("show", "-s", "--format=%P", "1" * 40): n.PREDECESSOR,
                  ("show", "-s", "--format=%B", "1" * 40): message,
                  ("cat-file", "-t", n.TAG): tag_type,
                  ("rev-parse", n.TAG + "^{commit}"): "1" * 40,
                  ("rev-parse", n.TAG): "2" * 40,
                  ("rev-parse", "1" * 40 + "^{tree}"): "3" * 40,
                  ("rev-parse", "1" * 40 + ":" + n.PREFIX): "4" * 40,
                  ("rev-parse", "1" * 40 + ":" + n.PREFIX + "/standards"): "5" * 40}
        raw = b"object " + b"1" * 40 + b"\ntype commit\n\n" + (n.tag_message(selected) if annotation is None else annotation)
        return source, actual, values, raw

    def test_native_exact_projection_parent_and_annotation_pass(self):
        source, actual, values, raw = self.native_fixture()
        with patch.object(n, "commit"), patch.object(n, "tree_rows", return_value=actual), patch.object(n, "text_git", side_effect=lambda repo, *args: values[args]), patch.object(n, "git", return_value=raw):
            result = n.native_facts(self.root, "1" * 40, source)
        self.assertEqual(result["parent"], n.PREDECESSOR)
        self.assertEqual(result["package_path"], n.PREFIX)

    def test_native_annotation_cannot_claim_another_standing(self):
        source, actual, values, raw = self.native_fixture(annotation=b"accepted final\n")
        with patch.object(n, "commit"), patch.object(n, "tree_rows", return_value=actual), patch.object(n, "text_git", side_effect=lambda repo, *args: values[args]), patch.object(n, "git", return_value=raw), self.assertRaises(ValueError):
            n.native_facts(self.root, "1" * 40, source)

    def test_native_lightweight_tag_refuses(self):
        source, actual, values, raw = self.native_fixture(tag_type="commit")
        with patch.object(n, "commit"), patch.object(n, "tree_rows", return_value=actual), patch.object(n, "text_git", side_effect=lambda repo, *args: values[args]), patch.object(n, "git", return_value=raw), self.assertRaises(ValueError):
            n.native_facts(self.root, "1" * 40, source)

    def test_canonical_manifest_uses_logical_digest_paths(self):
        rows, _ = sample()
        native = dict(cut=n.CUT, commit="1" * 40, tag_object="2" * 40, tree="3" * 40, standards_tree="4" * 40, qualified_ref=n.TAG, package_tree="5" * 40)
        manifest = n.expected_manifest({"files": rows}, native)
        digest = next(r["sha256"] for r in rows if r["path"] == "standards/README.md")
        self.assertEqual(manifest["standards"]["member_set_sha256"], n.sha(f"{digest}  specification/standards/README.md\n".encode()))
        self.assertNotEqual(manifest["standards"]["member_set_sha256"], n.sha(f"{digest}  standards/README.md\n".encode()))
        self.assertEqual(manifest["auxiliary"]["release_note"]["source_path"], "releases/v3.0.1.md")

    def installed_fixture(self):
        rows, data = sample()
        run = self.root / "run"
        run.mkdir()
        manifest = n.canonical({"synthetic": "byte-boundary fixture only"})
        selected = {"files": rows, "native": {"manifest_sha256": n.sha(manifest), "commit": "1" * 40}}
        selection_raw = n.canonical(selected)
        (run / "SOURCE_SELECTION.json").write_bytes(selection_raw)
        (run / n.MANIFEST_NAME).write_bytes(manifest)
        store = run / "store"
        installed = store / "releases" / n.CUT
        for path, raw in {**data, "manifest.json": manifest}.items():
            target = installed / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        report = {"valid": True, "failures": [], "cut": n.CUT, "path": str(installed), "manifest_sha256": n.sha(manifest), "manifest": json.loads(manifest)}
        (run / "verify.json").write_bytes(n.canonical(report))
        args = SimpleNamespace(run=run, selection_sha256=n.sha(selection_raw), store=store, verify_report=run / "verify.json", label="local")
        return args, installed

    def test_installed_exact_files_pass_bounded_byte_proof(self):
        args, _ = self.installed_fixture()
        receipt = n.installed(args)
        self.assertTrue(Path(receipt["path"]).is_file())

    def test_stale_passing_verifier_does_not_hide_payload_mutation(self):
        args, installed = self.installed_fixture()
        (installed / "standards/README.md").write_bytes(b"changed\n")
        with self.assertRaises(ValueError):
            n.installed(args)

    def test_installed_manifest_tampering_refuses(self):
        args, installed = self.installed_fixture()
        (installed / "manifest.json").write_bytes(b"{}\n")
        with self.assertRaises(ValueError):
            n.installed(args)

    def test_preserve_existing_output(self):
        path = self.root / "once.json"
        n.save(path, b"first")
        with self.assertRaises(FileExistsError):
            n.save(path, b"second")
        self.assertEqual(path.read_bytes(), b"first")


if __name__ == "__main__":
    unittest.main(verbosity=2)
