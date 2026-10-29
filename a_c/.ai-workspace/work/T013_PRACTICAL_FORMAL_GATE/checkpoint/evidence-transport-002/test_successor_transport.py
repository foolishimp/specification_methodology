"""Exact successor alias controls on disposable small byte strings."""
from pathlib import Path
import tempfile
import unittest

import transport as t


class SuccessorAliases(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="alias-control-", dir=Path(__file__).parent)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.names = sorted(t.EXACT_COMPILED_ALIASES)
        self.raw = b"bounded synthetic public compiled bytes\x00\xff" * 4

    def prepare(self):
        rows = []
        for name in self.names:
            p = self.source / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(self.raw)
            rows.append({"path": name, "sha256": t.raw_sha(self.raw), "bytes": len(self.raw)})
        selected = self.root / "selected.json"
        selected.write_bytes(t.encode({"schema": "a_c.evidence-transport-selection/1",
                                      "files": rows, "historical_pins": []}))
        payload = self.root / "payload"
        result = t.prepare(self.source, selected, t.file_identity(selected)["sha256"], payload)
        return payload, result["manifest_sha256"]

    def test_exact_new_aliases_restore_and_repeat_without_rewrite(self):
        self.assertEqual(len(self.names), 10)
        payload, digest = self.prepare()
        target = self.root / "restored"
        result = t.restore(payload, digest, target)
        self.assertEqual(result["restored"], self.names)
        stamps = {}
        for name in self.names:
            p = target / name
            self.assertEqual(p.read_bytes(), self.raw)
            stamps[name] = (p.stat().st_ino, p.stat().st_mtime_ns)
        again = t.restore(payload, digest, target)
        self.assertEqual(again["restored"], [])
        self.assertEqual(again["already_present_identical"], self.names)
        for name in self.names:
            p = target / name
            self.assertEqual((p.stat().st_ino, p.stat().st_mtime_ns), stamps[name])

    def test_nearby_unlisted_aliases_and_case_changes_refuse(self):
        for name in self.names:
            for other in (name.replace(".olean.private", "Other.olean.private"),
                          name.replace("/Gate", "/other/Gate"), name.upper()):
                with self.subTest(other=other), self.assertRaises(ValueError):
                    t.relative(other, True)
        for name in ("real-use/new/GateLocalNames.olean.private",
                     "package/delivery-003/installed-29-evidence/GateLocalNames.olean.private"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                t.relative(name, True)
        self.assertEqual(t.relative("lean/new/Old.olean.private", True), "lean/new/Old.olean.private")
        self.assertEqual(t.relative("reuse/new/Old.olean.private", True), "reuse/new/Old.olean.private")

    def test_traversal_private_and_symlink_refuse_on_new_aliases(self):
        for name in self.names:
            for part in ("..", ".CACHE", "PRIVATE", "formal-origin-v1", "keys"):
                other = name.replace("/Gate", "/" + part + "/Gate")
                with self.subTest(other=other), self.assertRaises(ValueError):
                    t.relative(other, True)
        payload, digest = self.prepare()
        target = self.root / "target"
        target.mkdir()
        (target / "real-use").symlink_to(self.source / "real-use", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            t.restore(payload, digest, target)
        self.assertFalse((target / "package").exists())

    def test_new_alias_conflict_refuses_without_any_replacement(self):
        payload, digest = self.prepare()
        target = self.root / "target"
        bad = target / self.names[-1]
        bad.parent.mkdir(parents=True)
        bad.write_bytes(b"retain conflicting target")
        with self.assertRaisesRegex(ValueError, "differ"):
            t.restore(payload, digest, target)
        self.assertEqual(bad.read_bytes(), b"retain conflicting target")
        self.assertFalse((target / self.names[0]).exists())


if __name__ == "__main__":
    unittest.main()
