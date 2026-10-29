"""Cheap synthetic transport controls; no actual proof input or private state."""
from copy import deepcopy
import gzip
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import transport as t


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="synthetic-", dir=Path(__file__).parent)
        self.addCleanup(self.tmp.cleanup); self.root = Path(self.tmp.name)
        self.source = self.root / "source"; self.source.mkdir()
        self.names = ["lean/one/A.olean.private", "lean/two/B.olean.private"]
        self.raw = b"synthetic compiled data\x00\xff\n" * 20
        files = []
        for name in self.names:
            p = self.source / name; p.parent.mkdir(parents=True); p.write_bytes(self.raw)
            files.append({"path": name, "sha256": t.raw_sha(self.raw), "bytes": len(self.raw)})
        self.selection = self.root / "selection.json"
        self.selection.write_bytes(t.encode({"schema": "a_c.evidence-transport-selection/1", "files": files, "historical_pins": []}))
        self.selection_hash = t.file_identity(self.selection)["sha256"]
        self.payload = self.root / "payload"
        self.result = t.prepare(self.source, self.selection, self.selection_hash, self.payload)
        self.manifest_hash = self.result["manifest_sha256"]

    def test_deduplicated_deterministic_roundtrip_and_no_rewrite(self):
        self.assertEqual(self.result["files"], 2); self.assertEqual(self.result["unique_payloads"], 1)
        other = self.root / "other"
        t.prepare(self.source, self.selection, self.selection_hash, other)
        first = next((self.payload / "members").iterdir()); second = next((other / "members").iterdir())
        self.assertEqual(first.read_bytes(), second.read_bytes())
        target = self.root / "restored"; result = t.restore(self.payload, self.manifest_hash, target)
        self.assertEqual(result["restored"], self.names)
        stamps = {name: ((target / name).stat().st_ino, (target / name).stat().st_mtime_ns) for name in self.names}
        again = t.restore(self.payload, self.manifest_hash, target)
        self.assertEqual(again["already_present_identical"], self.names); self.assertEqual(again["restored"], [])
        self.assertEqual(stamps, {name: ((target / name).stat().st_ino, (target / name).stat().st_mtime_ns) for name in self.names})
        for name in self.names: self.assertEqual((target / name).read_bytes(), self.raw)

    def test_conflicting_existing_target_is_not_overwritten(self):
        target = self.root / "restored"; bad = target / self.names[0]
        bad.parent.mkdir(parents=True); bad.write_bytes(b"keep existing mismatch")
        with self.assertRaisesRegex(ValueError, "differ"): t.restore(self.payload, self.manifest_hash, target)
        self.assertEqual(bad.read_bytes(), b"keep existing mismatch")
        self.assertFalse((target / self.names[1]).exists())

    def test_altered_compressed_payload_refuses_before_restore(self):
        first = next((self.payload / "members").iterdir()); data = bytearray(first.read_bytes()); data[-1] ^= 1; first.write_bytes(data)
        target = self.root / "restored"
        with self.assertRaisesRegex(ValueError, "changed"): t.restore(self.payload, self.manifest_hash, target)
        self.assertFalse(target.exists())

    def test_raw_expansion_bound_and_wrong_raw_hash_refuse(self):
        manifest, payloads = t.manifest_load(self.payload, self.manifest_hash)
        item = deepcopy(next(iter(payloads.values()))); item["raw_bytes"] = 2
        with self.assertRaisesRegex(ValueError, "exceeds bound"): t.stream_payload(self.payload, item)
        item["raw_bytes"] = len(self.raw); item["raw_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "identity mismatch"): t.stream_payload(self.payload, item)

    def test_safe_remote_bound_refuses_without_splitting(self):
        with patch.object(t, "MAX_COMPRESSED", 16):
            with self.assertRaisesRegex(ValueError, "safe remote bound"):
                t.prepare(self.source, self.selection, self.selection_hash, self.root / "too-large")
        self.assertFalse((self.root / "too-large/MANIFEST.json").exists())

    def test_path_boundaries_case_aliases_and_symlinks(self):
        for name in ("../outside.olean.private", "/lean/x.olean.private", "lean/.CACHE/x.olean.private",
                     "reuse/PRIVATE/x.olean.private", "reuse/formal-origin-v1/key.olean.private", "lean/a.json"):
            with self.subTest(name=name), self.assertRaises(ValueError): t.relative(name, True)
        alias = self.root / "alias"; alias.symlink_to(self.source, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"): t.verify(self.payload, self.manifest_hash, alias)
        with self.assertRaisesRegex(ValueError, "noncanonical"): t.rooted(self.root / "x/../source")
        target = self.root / "restored"; target.mkdir(); (target / "lean").symlink_to(self.source / "lean", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"): t.restore(self.payload, self.manifest_hash, target)

    def test_manifest_identity_and_complete_population_are_required(self):
        with self.assertRaisesRegex(ValueError, "digest mismatch"): t.verify(self.payload, "0" * 64)
        (self.payload / "members/unlisted.gz").write_bytes(gzip.compress(b"unlisted", mtime=0))
        with self.assertRaisesRegex(ValueError, "population"): t.verify(self.payload, self.manifest_hash)
        with self.assertRaisesRegex(ValueError, "duplicate JSON"): t.decode(b'{"a":1,"a":2}')

    def test_filesystem_identity_overlap_and_uncertain_identity_refuse(self):
        target = self.root / "fresh"
        with patch.object(Path, "samefile", return_value=True):
            with self.assertRaisesRegex(ValueError, "filesystem roots overlap"):
                t.restore(self.payload, self.manifest_hash, target)
        with patch.object(Path, "samefile", side_effect=OSError("identity unavailable")):
            with self.assertRaises(OSError): t.restore(self.payload, self.manifest_hash, target)
        self.assertFalse(target.exists())

    def test_normal_containing_checkpoint_root_is_allowed_but_payload_outputs_refuse(self):
        restored = t.restore(self.payload, self.manifest_hash, self.root)
        self.assertEqual(restored["restored"], self.names)
        for name in self.names: self.assertEqual((self.root / name).read_bytes(), self.raw)
        with self.assertRaisesRegex(ValueError, "roots overlap"):
            t.restore(self.payload, self.manifest_hash, self.payload)


if __name__ == "__main__": unittest.main()
