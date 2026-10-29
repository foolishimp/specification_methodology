"""Synthetic file custody/packaging controls; never loads the tenant or support."""
from copy import deepcopy
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import package_source as p


class SourcePackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="synthetic-", dir=Path(__file__).parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"; self.source.mkdir()
        (self.source / "code").mkdir()
        (self.source / "code/helper.py").write_bytes(b"print('synthetic only')\n")
        (self.source / "notes.md").write_bytes(b"# Synthetic package\n")
        self.plan = {"schema": "a_c.lean.package-plan/1", "state": "proposed",
                     "entries": [{"source": name, "path": name, "role": "synthetic"}
                                 for name in ("code/helper.py", "notes.md")],
                     "closed_directories": ["code"]}
        self.freeze = {"schema": "a_c.lean.package-freeze/1", "kind": "synthetic",
                       "selection_ref": "synthetic-test-only",
                       "runtime_identity": {"sha256": p.sha(p.canonical({})), "pins": {}}}
        self.plan_path = self.root / "plan.json"; self.plan_path.write_bytes(p.encode(self.plan))
        self.freeze_path = self.root / "freeze.json"; self.freeze_path.write_bytes(p.encode(self.freeze))
        self.selection = self.root / "selection.json"
        self.digest = p.select(self.source, self.plan_path, self.freeze_path, self.selection)["manifest_sha256"]
        self.tree = self.root / "bundle"
        self.tar = self.root / "bundle.tar"

    def build(self):
        return p.build(self.source, self.selection, self.digest, self.tree)

    def malicious_archive(self, members):
        with tarfile.open(self.tar, "w") as tar:
            for name, content, kind in members:
                info = tarfile.TarInfo(name); info.type = kind
                info.size = len(content) if kind == tarfile.REGTYPE else 0
                if kind in (tarfile.SYMTYPE, tarfile.LNKTYPE): info.linkname = "../outside"
                tar.addfile(info, io.BytesIO(content) if kind == tarfile.REGTYPE else None)

    def test_roundtrip_and_reproducible_archive(self):
        self.build(); first = p.archive(self.tree, self.digest, self.tar)
        second = p.archive(self.tree, self.digest, self.root / "second.tar")
        self.assertEqual(first["archive_sha256"], second["archive_sha256"])
        out = self.root / "extracted"
        self.assertEqual(p.extract(self.tar, self.digest, out)["files"], 3)
        self.assertEqual((out / "code/helper.py").read_bytes(), (self.source / "code/helper.py").read_bytes())
        # Directory verification is independent of source checkout and archive.
        self.tar.unlink(); (self.source / "code/helper.py").unlink()
        self.assertEqual(p.verify_tree(out, self.digest)["status"], "source_bytes_verified")

    def test_overlap_refused_before_output_write(self):
        with self.assertRaisesRegex(ValueError, "overlapping"):
            p.build(self.source, self.selection, self.digest, self.source / "bundle")
        self.assertFalse((self.source / "bundle").exists())
        self.build()
        with self.assertRaisesRegex(ValueError, "overlapping"):
            p.archive(self.tree, self.digest, self.tree / "inside.tar")
        self.assertFalse((self.tree / "inside.tar").exists())

    def test_changed_source_and_wrong_trust_anchor(self):
        (self.source / "code/helper.py").write_bytes(b"changed\n")
        with self.assertRaisesRegex(ValueError, "member changed"):
            self.build()
        self.assertFalse(self.tree.exists())
        with self.assertRaisesRegex(ValueError, "manifest byte/hash"):
            p.load_manifest(self.selection.read_bytes(), "0" * 64)

    def test_existing_destinations_refuse(self):
        self.build()
        with self.assertRaisesRegex(ValueError, "destination exists"):
            self.build()
        p.archive(self.tree, self.digest, self.tar)
        with self.assertRaisesRegex(ValueError, "destination exists"):
            p.archive(self.tree, self.digest, self.tar)
        with self.assertRaisesRegex(ValueError, "destination exists"):
            p.extract(self.tar, self.digest, self.tree)

    def test_symlink_file_parent_and_output_refuse(self):
        original = self.source / "code/helper.py"; original.unlink()
        original.symlink_to(self.source / "notes.md")
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.build()
        original.unlink(); (self.source / "code").rmdir()
        (self.source / "code").symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.build()
        alias = self.root / "alias"; alias.symlink_to(self.source, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            p.root_path(alias / "new", False)

    def test_tree_mutation_extra_file_empty_directory_and_symlink_refuse(self):
        self.build(); helper = self.tree / "code/helper.py"
        old = helper.read_bytes(); helper.write_bytes(b"wrong\n")
        with self.assertRaises(ValueError): p.verify_tree(self.tree, self.digest)
        helper.write_bytes(old)
        extra = self.tree / "extra"; extra.mkdir()
        with self.assertRaisesRegex(ValueError, "exact inventory"): p.verify_tree(self.tree, self.digest)
        extra.rmdir(); extra.write_bytes(b"extra")
        with self.assertRaisesRegex(ValueError, "exact inventory"): p.verify_tree(self.tree, self.digest)
        extra.unlink(); helper.unlink(); helper.symlink_to(self.source / "code/helper.py")
        with self.assertRaises(ValueError): p.verify_tree(self.tree, self.digest)

    def test_closed_namespace_catches_new_helper_without_glob_inclusion(self):
        (self.source / "code/reuse.py").write_bytes(b"new helper\n")
        with self.assertRaisesRegex(ValueError, "unselected source"):
            p.select(self.source, self.plan_path, self.freeze_path, self.root / "new.json")
        plan = deepcopy(self.plan)
        plan["entries"].append({"source": "code/reuse.py", "path": "code/reuse.py", "role": "explicit new helper"})
        self.plan_path.write_bytes(p.encode(plan))
        result = p.select(self.source, self.plan_path, self.freeze_path, self.root / "new.json")
        self.assertEqual(result["files"], 3)

    def test_path_and_case_file_directory_collisions(self):
        for name in ("../escape", "/absolute", "x//y", "x/./y", "x\\y", "x/.cache/data",
                     "x/.lake/module", "x/.toolchain/binary", "private/key.json", "entries/one.json",
                     "x/origin-selection.json", "x/origin.key", "x/module.olean.private"):
            with self.subTest(name=name), self.assertRaises(ValueError): p.relative(name)
        for names in (("a", "a"), ("Code/a", "code/b"), ("a", "a/b")):
            with self.subTest(names=names), self.assertRaises(ValueError): p.paths_unique(names)

    def test_duplicate_json_and_metadata_contradiction_refuse(self):
        with self.assertRaisesRegex(ValueError, "duplicate"): p.decode(b'{"x":1,"x":2}')
        for broken in (b'{"n":NaN}', b'\xff'):
            with self.assertRaises(ValueError): p.decode(broken)
        manifest = p.decode(self.selection.read_bytes())
        manifest["freeze"]["selection_ref"] = "changed"
        with self.assertRaisesRegex(ValueError, "freeze identity"): p.validate_manifest(manifest)

    def test_runtime_pin_cannot_disagree_with_selected_source(self):
        manifest = p.decode(self.selection.read_bytes())
        manifest["freeze"]["kind"] = "candidate"
        pins = {"scripts/formal_gate.py": "a" * 64}
        manifest["freeze"]["runtime_identity"] = {"sha256": p.sha(p.canonical(pins)), "pins": pins}
        manifest["freeze_sha256"] = p.sha(p.canonical(manifest["freeze"]))
        manifest["portable_runtime_identity"] = p.portable_identity(manifest["freeze"])
        with self.assertRaisesRegex(ValueError, "runtime identity absent"): p.validate_manifest(manifest)

    def test_malicious_archive_never_starts_extraction(self):
        for name, kind in (("../escape", tarfile.REGTYPE), ("/escape", tarfile.REGTYPE),
                           ("link", tarfile.SYMTYPE), ("hard", tarfile.LNKTYPE),
                           ("dir", tarfile.DIRTYPE), ("device", tarfile.CHRTYPE)):
            with self.subTest(name=name):
                self.malicious_archive([(name, b"bad", kind)])
                out = self.root / "bad-extract"
                with self.assertRaises(ValueError): p.extract(self.tar, self.digest, out)
                self.assertFalse(out.exists()); self.tar.unlink()

    def test_duplicate_missing_extra_and_tampered_archive_members(self):
        manifest = self.selection.read_bytes()
        cases = [
            [(p.MANIFEST, manifest, tarfile.REGTYPE)] * 2,
            [("notes.md", b"absent manifest", tarfile.REGTYPE)],
            [(p.MANIFEST, manifest, tarfile.REGTYPE), ("extra", b"unknown", tarfile.REGTYPE)],
            [(p.MANIFEST, manifest, tarfile.REGTYPE), ("notes.md", b"bad", tarfile.REGTYPE),
             ("code/helper.py", (self.source / "code/helper.py").read_bytes(), tarfile.REGTYPE)],
        ]
        for members in cases:
            self.malicious_archive(members)
            with self.assertRaises(ValueError): p.inspect_archive(self.tar, self.digest)
            self.tar.unlink()

    def test_trailing_payload_and_resource_bounds_refuse(self):
        self.build(); p.archive(self.tree, self.digest, self.tar)
        with self.tar.open("ab") as stream: stream.write(b"unlisted payload")
        with self.assertRaisesRegex(ValueError, "trailing payload"):
            p.inspect_archive(self.tar, self.digest)
        manifest = p.decode(self.selection.read_bytes())
        manifest["files"][0]["bytes"] = p.MAX_FILE + 1
        with self.assertRaisesRegex(ValueError, "byte bound"): p.validate_manifest(manifest)
        manifest["files"][0]["bytes"] = True
        with self.assertRaisesRegex(ValueError, "byte bound"): p.validate_manifest(manifest)

    def test_origin_enabled_identity_has_fixed_origin_free_package_projection(self):
        # Public synthetic source only. No origin directory, selection or key is made/read.
        source_name = "a_c/build_tenants/lean/scripts/formal_gate.py"
        source = self.source / source_name; source.parent.mkdir(parents=True)
        source.write_bytes(b"# synthetic public gate source\n")
        profile_name = "a_c/build_tenants/lean/profiles/proof-support-v1.json"
        profile = self.source / profile_name; profile.parent.mkdir(parents=True)
        profile.write_bytes(b'{"synthetic":true}\n')
        pins = {"scripts/formal_gate.py": p.sha(source.read_bytes()),
                "profiles/proof-support-v1.json": p.sha(profile.read_bytes()),
                p.ORIGIN_SELECTION: "f" * 64}
        freeze = deepcopy(self.freeze)
        freeze["runtime_identity"] = {"sha256": p.sha(p.canonical(pins)), "pins": pins}
        self.freeze_path.write_bytes(p.encode(freeze))
        plan = deepcopy(self.plan)
        plan["entries"] = [{"source": name, "path": name, "role": "synthetic public source"}
                           for name in (source_name, profile_name)]
        plan["closed_directories"] = ["a_c/build_tenants/lean/scripts", "a_c/build_tenants/lean/profiles"]
        self.plan_path.write_bytes(p.encode(plan))
        selected = self.root / "origin-enabled-selection.json"
        result = p.select(self.source, self.plan_path, self.freeze_path, selected)
        manifest = p.decode(selected.read_bytes())
        self.assertEqual(manifest["freeze"]["runtime_identity"], freeze["runtime_identity"])
        portable_pins = {name: value for name, value in pins.items() if name != p.ORIGIN_SELECTION}
        expected = {"sha256": p.sha(p.canonical(portable_pins)), "pins": portable_pins}
        self.assertEqual(manifest["portable_runtime_identity"], expected)
        self.assertNotEqual(expected["sha256"], freeze["runtime_identity"]["sha256"])
        p.build(self.source, selected, result["manifest_sha256"], self.tree)
        self.assertFalse((self.tree / "a_c/build_tenants/lean/.cache").exists())
        self.assertEqual(p.verify_tree(self.tree, result["manifest_sha256"])["files"], 3)
        # Byte-currentness applies to every public pin despite the fixed omission.
        source.write_bytes(b"changed synthetic public source\n")
        with self.assertRaisesRegex(ValueError, "portable runtime identity absent/changed"):
            p.select(self.source, self.plan_path, self.freeze_path, self.root / "changed-selection.json")

    def test_portable_projection_cannot_omit_other_pins_or_accept_private_aliases(self):
        manifest = p.decode(self.selection.read_bytes())
        pins = {"scripts/formal_gate.py": "a" * 64, p.ORIGIN_SELECTION: "f" * 64}
        manifest["freeze"]["runtime_identity"] = {"sha256": p.sha(p.canonical(pins)), "pins": pins}
        manifest["freeze_sha256"] = p.sha(p.canonical(manifest["freeze"]))
        manifest["portable_runtime_identity"] = {"sha256": p.sha(p.canonical({})), "pins": {}}
        with self.assertRaisesRegex(ValueError, "fixed origin-free projection"):
            p.validate_manifest(manifest)
        manifest["ignore_pins"] = ["scripts/formal_gate.py"]
        with self.assertRaisesRegex(ValueError, "bad package manifest fields"):
            p.validate_manifest(manifest)
        for name in (".CACHE/formal-origin-v1/selection.json", ".cache/formal-origin-v1/other.json",
                     "private/selection.json", "formal-origin-v1/origin.KEY"):
            freeze = deepcopy(self.freeze); alias = {name: "f" * 64}
            freeze["runtime_identity"] = {"sha256": p.sha(p.canonical(alias)), "pins": alias}
            with self.subTest(name=name), self.assertRaises(ValueError): p.portable_identity(freeze)

    def test_casefolded_exclusions_precede_any_source_metadata_or_content_access(self):
        names = ("x/.CACHE/formal-origin-v1/origin.KEY", "x/.LaKe/object", "x/.ToOlChAiN/bin",
                 "x/PRIVATE/value", "x/EnTrIeS/value", "x/TeMp/value", "x/__PYCACHE__/module",
                 "x/.ds_store", "x/origin.KEY", "x/certificate.PEM", "x/module.OLEAN.PRIVATE",
                 "x/ORIGIN-SELECTION.json", "x/Origin-Key-Local.json")
        with patch.object(Path, "lstat", side_effect=AssertionError("must reject before acquisition")):
            for name in names:
                with self.subTest(name=name), self.assertRaises(ValueError): p.regular(self.source, name)

    def test_noncanonical_roots_refuse_for_both_sides_of_build_archive_extract(self):
        alias = self.root / "alias"; alias.mkdir()
        self.build(); p.archive(self.tree, self.digest, self.tar)
        calls = [
            lambda: p.build(alias / ".." / "source", self.selection, self.digest, self.source / "nested"),
            lambda: p.build(self.source, self.selection, self.digest, alias / ".." / "source/nested"),
            lambda: p.archive(alias / ".." / "bundle", self.digest, self.tree / "inside.tar"),
            lambda: p.archive(self.tree, self.digest, alias / ".." / "bundle/inside.tar"),
            lambda: p.extract(alias / ".." / "bundle.tar", self.digest, self.root / "extracted"),
            lambda: p.extract(self.tar, self.digest, alias / ".." / "extracted"),
        ]
        for index, call in enumerate(calls):
            with self.subTest(index=index), self.assertRaisesRegex(ValueError, "noncanonical root"):
                call()
        self.assertFalse((self.source / "nested").exists())
        self.assertFalse((self.tree / "inside.tar").exists())
        self.assertFalse((self.root / "extracted").exists())


if __name__ == "__main__":
    unittest.main()
