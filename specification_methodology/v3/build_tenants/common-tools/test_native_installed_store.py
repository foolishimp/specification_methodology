"""Public installed-attestation input/output boundary regression controls."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get("STDO_NATIVE_RELEASE_TEST_SOURCE", HERE / "native_release.py"))


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class InstalledStoreTests(unittest.TestCase):
    def setUp(self):
        retained = os.environ.get("STDO_NATIVE_STORE_TEST_EVIDENCE")
        if retained:
            self.root = Path(retained) / self._testMethodName
            self.root.mkdir(parents=True, exist_ok=False)
        else:
            temporary = tempfile.TemporaryDirectory()
            self.addCleanup(temporary.cleanup)
            self.root = Path(temporary.name).resolve()
        self.calls = []

    def fixture(self, label="current", historical=False):
        root = self.root / label
        repo = root / "repo"
        tool = repo / "specification_methodology/v3/build_tenants/common-tools/native_release.py"
        tool.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE, tool)
        cut = "v3.0.4" if historical else "v3.0.5"
        territory = "STDO304_DELIVERY" if historical else "STDO305_DELIVERY"
        base = repo / ("specification_methodology/v3/.ai-workspace/work/" + territory + "/native-release")
        run = base / "run"
        run.mkdir(parents=True)
        store = base / "store" if historical else root / "external-store"
        native = store / "releases" / cut
        native.mkdir(parents=True)
        payload = b"exact installed fixture bytes\n"
        (native / "LICENSE").write_bytes(payload)
        manifest = {"kind": "fixture.native-manifest", "cut": cut}
        raw = encoded(manifest)
        (native / "manifest.json").write_bytes(raw)
        (run / ("stdo-" + cut + "-manifest.json")).write_bytes(raw)
        selection = {"native": {"commit": "a" * 40, "manifest_sha256": digest(raw)},
                     "files": [{"path": "LICENSE", "bytes": len(payload), "sha256": digest(payload)}]}
        selected = encoded(selection)
        (run / "SOURCE_SELECTION.json").write_bytes(selected)
        report = {"valid": True, "failures": [], "cut": cut, "path": str(native),
                  "manifest_sha256": digest(raw), "manifest": manifest}
        report_path = root / "verify.json"
        report_path.write_bytes(encoded(report))
        argv = [sys.executable, "-B", str(tool)]
        if not historical:
            configuration = {"kind": "stdo.native-preparation-config/1", "version": "3.0.5", "cut": cut,
                "source": {"path": "fixture/source.json", "sha256": "b" * 64, "source_identity_sha256": "c" * 64},
                "repository_url": "https://example.invalid/repo.git", "native_preparation": {
                    "manager_wheel": "stdo_toolchain-3.0.5-py3-none-any.whl",
                    "output_root": base.relative_to(repo).as_posix(), "package_path": "specification_methodology/v3",
                    "predecessor_native_commit": "d" * 40, "scope": "bounded installed-input fixture"}}
            config = root / "configuration.json"
            config.write_bytes(encoded(configuration))
            argv += ["--configuration", str(config), "--configuration-sha256", digest(config.read_bytes())]
        argv += ["installed", "--run", str(run), "--selection-sha256", digest(selected), "--store", str(store),
                 "--verify-report", str(report_path), "--label", "local"]
        return {"root": root, "repo": repo, "run": run, "store": store, "native": native, "argv": argv}

    @staticmethod
    def snapshot(root):
        return {str(p.relative_to(root)): {"mode": p.lstat().st_mode, "mtime_ns": p.lstat().st_mtime_ns,
                "target": os.readlink(p) if p.is_symlink() else None,
                "sha256": digest(p.read_bytes()) if p.is_file() and not p.is_symlink() else None}
                for p in sorted(root.rglob("*"))}

    def invoke(self, fixture, success=False, change=None):
        argv = fixture["argv"][:]
        if change:
            flag, value = change
            argv[argv.index(flag) + 1] = str(value)
        before = self.snapshot(fixture["store"])
        process = subprocess.run(argv, capture_output=True, cwd=fixture["repo"], timeout=15)
        after = self.snapshot(fixture["store"])
        self.assertEqual(before, after, "read-only attestation changed installed input")
        evidence = {"argv": argv, "returncode": process.returncode,
                    "stdout": process.stdout.decode(), "stderr": process.stderr.decode(),
                    "store_before": before, "store_after": after}
        (fixture["root"] / "execution.json").write_bytes(encoded(evidence))
        self.calls.append(evidence)
        if success:
            self.assertEqual(process.returncode, 0, process.stderr.decode())
            result = json.loads((fixture["run"] / "installed-local.json").read_bytes())
            self.assertTrue(result["exact_payload_and_manifest"])
            self.assertEqual(result["files"], 2)
            self.assertEqual(result["store"], str(fixture["store"]))
        else:
            self.assertNotEqual(process.returncode, 0)
            self.assertFalse((fixture["run"] / "installed-local.json").exists())
        return process

    def test_external_ordinary_store_passes(self):
        self.invoke(self.fixture(), success=True)

    def test_historical_internal_store_passes(self):
        self.invoke(self.fixture(historical=True), success=True)

    def test_historical_relative_internal_store_passes(self):
        f = self.fixture(historical=True)
        self.invoke(f, success=True, change=("--store", f["store"].relative_to(f["repo"])))

    def test_traversal_and_relative_stores_refuse(self):
        for label in ("traversal", "relative"):
            with self.subTest(label=label):
                f = self.fixture(label)
                path = f["store"] / ".." / "external-store" if label == "traversal" else Path("../external-store")
                self.invoke(f, change=("--store", path))

    def test_redirected_store_and_native_ancestors_refuse(self):
        for label in ("store", "store-ancestor", "releases", "native"):
            with self.subTest(label=label):
                f = self.fixture(label)
                if label == "store":
                    alias = f["root"] / "store-link"
                    alias.symlink_to(f["store"], target_is_directory=True)
                    self.invoke(f, change=("--store", alias))
                elif label == "store-ancestor":
                    alias = self.root / "ancestor-link"
                    alias.symlink_to(f["root"], target_is_directory=True)
                    self.invoke(f, change=("--store", alias / "external-store"))
                else:
                    selected = f["store"] / "releases" if label == "releases" else f["native"]
                    retained = f["root"] / (label + "-actual")
                    selected.rename(retained)
                    selected.symlink_to(retained, target_is_directory=True)
                    self.invoke(f)

    def test_output_outside_base_still_refuses(self):
        f = self.fixture()
        outside = f["root"] / "outside-output"
        self.invoke(f, change=("--run", outside))
        self.assertFalse(outside.exists())

    def test_altered_and_extra_members_refuse(self):
        for label in ("altered", "extra"):
            with self.subTest(label=label):
                f = self.fixture(label)
                (f["native"] / ("LICENSE" if label == "altered" else "EXTRA")).write_text("different\n")
                self.invoke(f)


if __name__ == "__main__":
    unittest.main()
