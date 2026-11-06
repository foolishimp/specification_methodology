import io
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import unicodedata
import zipfile

import tooling
import tooling_materialize as materializer

PACKAGE = Path(__file__).resolve().parents[2] / "build_tenants/common"
BUNDLE = PACKAGE / "standards/tooling"


class ToolingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = materializer.read_bundle(BUNDLE)

    def temp(self):
        temporary = tempfile.TemporaryDirectory(prefix="stdo-tools-test-")
        self.addCleanup(temporary.cleanup)
        return Path(temporary.name).resolve()

    def copy(self, root, files=None):
        bundle = root / "release/standards/tooling"
        bundle.mkdir(parents=True)
        for name, raw in (files or self.files).items():
            (bundle / name).write_bytes(raw)
        return bundle

    def update_archive(self, transform):
        files = dict(self.files)
        buffer = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(files["sources.zip"])) as source, zipfile.ZipFile(buffer, "w") as out:
            entries = [(info, source.read(info)) for info in source.infolist()]
            for info, raw in transform(entries):
                out.writestr(info, raw)
        files["sources.zip"] = buffer.getvalue()
        meta = json.loads(files["TOOLING.json"])
        meta["distribution_members"]["sources.zip"] = {"bytes": len(files["sources.zip"]), "sha256": materializer.sha(files["sources.zip"])}
        files["TOOLING.json"] = materializer.encoded(meta)
        return files

    def test_exact_inventory_and_native_payload(self):
        result = tooling.check_payload({tooling.ROOT + p: b for p, b in self.files.items()})
        self.assertEqual(result["source_files"], 191)

    def test_arbitrary_cwd_materialize_verify_no_original_repository(self):
        root = self.temp(); bundle = self.copy(root); target = root / "workspace"
        before = materializer.read_bundle(bundle)
        for args in (["check"], ["materialize", "--destination", str(target)], ["verify-tree", "--destination", str(target)]):
            result = subprocess.run([sys.executable, "-I", "-B", str(bundle / "materialize.py"), *args],
                                    cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, materializer.read_bundle(bundle))
        self.assertFalse((target / "a_c/.ai-workspace").exists())
        (target / "a_c/build_tenants/graphify/code/ac_code.py").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "source bytes"):
            materializer.verify_tree(bundle, target)

    def test_destinations_existing_overlap_symlink_and_traversal(self):
        root = self.temp(); bundle = self.copy(root)
        existing = root / "existing"; existing.mkdir()
        link = root / "link"; link.symlink_to(existing, target_is_directory=True)
        for target in (existing, bundle / "workspace", bundle.parents[1] / "workspace", link / "child", root / "missing" / "child", root / "x" / ".." / "bad"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                materializer.materialize(bundle, target)
        self.assertEqual(list(existing.iterdir()), [])

    def test_actual_filesystem_aliases_cannot_write_under_installation(self):
        root = self.temp(); bundle = self.copy(root)
        alias = root / "RELEASE"
        if not alias.exists():
            self.skipTest("selected filesystem has no case alias")
        before = materializer.read_bundle(bundle)
        target = alias / "must-not-exist"
        with self.assertRaisesRegex(ValueError, "overlaps installed"):
            materializer.materialize(bundle, target)
        self.assertFalse(target.exists())
        target = root / "release/must-not-exist"
        with self.assertRaisesRegex(ValueError, "overlaps installed"):
            materializer.materialize(root / "release/STANDARDS/tooling", target)
        self.assertFalse(target.exists())
        self.assertEqual(before, materializer.read_bundle(bundle))
        accented = root / "reléase"
        (root / "release").rename(accented)
        normalized_alias = root / unicodedata.normalize("NFD", accented.name)
        if normalized_alias.exists():
            target = normalized_alias / "must-not-exist"
            with self.assertRaisesRegex(ValueError, "overlaps installed"):
                materializer.materialize(accented / "standards/tooling", target)
            self.assertFalse(target.exists())
            self.assertEqual(before, materializer.read_bundle(accented / "standards/tooling"))

    def test_missing_extra_and_tampered_bundle_refuse(self):
        cases = []
        for name in materializer.MEMBERS:
            files = dict(self.files); del files[name]; cases.append(files)
        files = dict(self.files); files["extra"] = b"x"; cases.append(files)
        files = dict(self.files); files["sources.zip"] += b"tamper"; cases.append(files)
        for files in cases:
            with self.assertRaises(ValueError):
                materializer.source_bytes(files)

    def test_self_consistent_narrowed_inventory_cannot_claim_source_cut(self):
        files = self.update_archive(lambda rows: rows[1:])
        meta = json.loads(files["TOOLING.json"]); meta["sources"] = meta["sources"][1:]
        files["TOOLING.json"] = materializer.encoded(meta)
        with self.assertRaisesRegex(ValueError, "inventory commitment"):
            materializer.source_bytes(files)

    def test_archive_path_type_duplicate_and_omission_refuse_before_output(self):
        def replace_first(rows, *, name=None, mode=None):
            info, raw = rows[0]
            if name is not None:
                info.filename = name
            if mode is not None:
                info.external_attr = mode << 16
            return [(info, raw), *rows[1:]]
        mutations = [lambda rows: replace_first(rows, name="../escape"),
                     lambda rows: replace_first(rows, name="/absolute"),
                     lambda rows: replace_first(rows, mode=stat.S_IFLNK | 0o777),
                     lambda rows: [rows[1], *rows[1:]], lambda rows: rows[1:]]
        for index, mutation in enumerate(mutations):
            root = self.temp(); bundle = self.copy(root, self.update_archive(mutation)); target = root / "target"
            with self.subTest(index=index), self.assertRaises(ValueError):
                materializer.materialize(bundle, target)
            self.assertFalse(target.exists())

    def test_archive_changed_content_rehashed_outer_still_refuses(self):
        def changed(rows):
            info, raw = rows[0]
            return [(info, raw[:-1] + b"X"), *rows[1:]]
        with self.assertRaisesRegex(ValueError, "source member digest"):
            materializer.source_bytes(self.update_archive(changed))


if __name__ == "__main__":
    unittest.main()
