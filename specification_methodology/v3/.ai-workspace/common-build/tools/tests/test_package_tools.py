"""Targeted positive/negative controls; fixtures are not candidate qualification."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "package_tools.py"
INSTALLED_PYTHON = Path("/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python")
INSTALLED_MANIFEST_SCHEMA = Path("/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/schemas/installed-release-manifest.schema.json")

# This trusted inline launcher reads and authenticates all project code as bytes
# before executing any of it. Only Python's isolated standard library runs first.
LAUNCHER = """import hashlib, pathlib, sys
p = pathlib.Path(sys.argv[1])
b = p.read_bytes()
if hashlib.sha256(b).hexdigest() != sys.argv[2]:
    raise SystemExit('checker digest mismatch before execution')
sys.argv = [str(p)] + sys.argv[3:]
exec(compile(b, str(p), 'exec'), {'__name__': '__main__', '__file__': str(p), '__authenticated_checker_sha256__': hashlib.sha256(b).hexdigest()})
"""


def sha(data):
    return hashlib.sha256(data).hexdigest()


class PackageToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="stdo-common-gates-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "package"
        self.root.mkdir()
        self.script_sha = sha(SCRIPT.read_bytes())
        self.freeze_count = 0
        self.put("standards/README.md", "# Package\n[Rules](RULES.md#stop-rule)\n[Same](#package)\n")
        self.put("standards/RULES.md", "# Rules\n\n## Stop rule\nA predecessor result stays historical; a reuse decision establishes applicability.\n")
        self.put("standards/schemas/example.json", '{"$defs":{"entry":{"type":"string"}},"$ref":"#/$defs/entry"}\n')
        self.put("standards/templates/STARTER.md", "# Project template\nAuthor: <author>\nDate: <date>\nStatus: <status>\nUse `.ai-workspace/tickets/` for selected ticket records.\n\n```text\nStatus: under construction\n```\n")
        self.put("plugins/spec/references/GUIDE.md", "# Guide\n[Rules](../../../standards/RULES.md#stop-rule)\n")
        self.put("release/release-note.md", "# V3 package\n[Entry](../standards/README.md)\n")
        self.put("LICENSE", "Fixture attribution: Example Author\n")
        self.inventory, self.inventory_sha = self.freeze()

    def put(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def invoke(self, *args, script=SCRIPT, expected=None, cwd=None):
        process = subprocess.run(
            [sys.executable, "-I", "-S", "-c", LAUNCHER, str(script), expected or self.script_sha, *map(str, args)],
            cwd=cwd or self.base, text=True, capture_output=True, timeout=30,
        )
        try:
            result = json.loads(process.stdout)
        except json.JSONDecodeError:
            result = {"stdout": process.stdout, "stderr": process.stderr}
        return process.returncode, result

    def freeze(self):
        self.freeze_count += 1
        target = self.base / f"freeze-{self.freeze_count}.json"
        code, result = self.invoke("freeze", "--root", self.root, "--inventory", target)
        self.assertEqual(code, 0, result)
        return target, result["inventory_sha256"]

    def check(self, *, refreeze=False):
        if refreeze:
            self.inventory, self.inventory_sha = self.freeze()
        return self.invoke("check", "--root", self.root, "--inventory", self.inventory, "--inventory-sha256", self.inventory_sha)

    def assert_failure(self, code, result, fragment):
        self.assertNotEqual(code, 0, result)
        self.assertIn(fragment, json.dumps(result))

    def coordinates(self):
        # Deliberately fictional test-only coordinates; no actual tag is made.
        release = {
            "cut": "v3.0.0-rc.999999",
            "tag_object": "a" * 40,
            "commit": "b" * 40,
            "tree": "c" * 40,
            "standards_tree": "d" * 40,
            "project_release_namespace": "specification_methodology",
            "qualified_ref": "refs/tags/specification_methodology/v3.0.0-rc.999999",
            "project_subtree_root": "specification_methodology/v3",
            "project_subtree_tree": "e" * 40,
        }
        return {"release": release, "release_note": {"package_path": "release/release-note.md", "source_path": "releases/v3.0.0.md", "installed_path": "release/release-note.md"}}

    def materialize(self, coordinates=None):
        coord_path = self.base / "coordinates.json"
        coord_path.write_text(json.dumps(coordinates or self.coordinates()))
        target = self.base / "materialized"
        code, report = self.invoke("materialize", "--root", self.root, "--inventory", self.inventory, "--inventory-sha256", self.inventory_sha, "--coordinates", coord_path, "--coordinates-sha256", sha(coord_path.read_bytes()), "--destination", target)
        return code, report, target

    def test_unchanged_from_arbitrary_cwd(self):
        unrelated = self.base / "unrelated"
        unrelated.mkdir()
        code, report = self.invoke("check", "--root", self.root, "--inventory", self.inventory, "--inventory-sha256", self.inventory_sha, cwd=unrelated)
        self.assertEqual(code, 0, report)
        self.assertTrue(report["valid"])
        self.assertEqual(report["member_count"], 7)
        self.assertGreater(report["checked_local_reference_count"], 3)
        self.assertEqual(report["checker_authentication"], "pinned inline launcher before execution")

    def test_one_byte_mutation(self):
        with (self.root / "LICENSE").open("ab") as file:
            file.write(b"!")
        self.assert_failure(*self.check(), "member bytes/digest changed")

    def test_added_member(self):
        self.put("standards/EXTRA.md", "# Extra\n")
        self.assert_failure(*self.check(), "extra member")

    def test_missing_member(self):
        (self.root / "LICENSE").unlink()
        self.assert_failure(*self.check(), "missing member")

    def test_added_empty_directory(self):
        (self.root / "empty").mkdir()
        self.assert_failure(*self.check(), "directory membership changed")

    def test_modified_pinned_inventory(self):
        self.inventory.write_bytes(self.inventory.read_bytes() + b" ")
        self.assert_failure(*self.check(), "pinned input digest mismatch")

    def test_duplicate_member_in_inventory(self):
        content = json.loads(self.inventory.read_bytes())
        content["members"].append(content["members"][0])
        content["member_count"] += 1
        self.inventory.write_text(json.dumps(content))
        self.inventory_sha = sha(self.inventory.read_bytes())
        self.assert_failure(*self.check(), "duplicate or unsorted inventory members")

    def test_file_broken_and_directory_symlinks(self):
        for target in ("standards/RULES.md", "does-not-exist", "standards"):
            with self.subTest(target=target):
                link = self.root / "redirect"
                link.symlink_to(target)
                self.assert_failure(*self.check(), "symlink forbidden")
                link.unlink()

    def test_symlink_package_root(self):
        link = self.base / "root-link"
        link.symlink_to(self.root)
        code, result = self.invoke("check", "--root", link, "--inventory", self.inventory, "--inventory-sha256", self.inventory_sha)
        self.assert_failure(code, result, "physical directory")

    def test_special_entry_is_rejected_without_reading_it(self):
        os.mkfifo(self.root / "pipe")
        self.assert_failure(*self.check(), "special filesystem entry forbidden")

    def test_malformed_json(self):
        self.put("standards/schemas/example.json", "{broken}")
        self.assert_failure(*self.check(refreeze=True), "invalid JSON")

    def test_duplicate_json_key(self):
        self.put("standards/schemas/example.json", '{"x":1,"x":2}')
        self.assert_failure(*self.check(refreeze=True), "duplicate JSON key")

    def test_missing_anchor(self):
        self.put("standards/README.md", "# Entry\n[Stop](RULES.md#absent)\n")
        self.assert_failure(*self.check(refreeze=True), "missing or unsupported local anchor")

    def test_escaping_and_missing_references(self):
        for target, error in (("../../outside.md", "escapes package"), ("ABSENT.md", "missing local target"), ("/tmp/local.md", "absolute local reference"), ("%2e%2e/%2e%2e/secret", "escapes package")):
            with self.subTest(target=target):
                self.put("standards/README.md", f"# Entry\n[Target]({target})\n")
                self.assert_failure(*self.check(refreeze=True), error)

    def test_reference_style_and_json_routes(self):
        self.put("standards/README.md", "# Entry\n[Stop][stop]\n\n[stop]: RULES.md#absent\n")
        self.assert_failure(*self.check(refreeze=True), "missing or unsupported local anchor")
        self.put("standards/README.md", "# Entry\n")
        self.put("standards/routes.json", '{"owner":"standards/RULES.md","anchor":"absent"}')
        self.assert_failure(*self.check(refreeze=True), "missing or unsupported local anchor")

    def test_publication_metadata_without_template_or_generic_law_false_positives(self):
        code, result = self.check()
        self.assertEqual(code, 0, result)
        self.put("standards/README.md", "# STDO RC9\nStatus: under construction\n")
        self.assert_failure(*self.check(refreeze=True), "stale construction/version header")

    def test_prior_version_and_build_history_routes(self):
        for text in ("Basis: `stdo://releases/v2.5.1-rc.2/`\n", "Source: build_tenants/claude/standards/\n", "Interpretation: a_c/i3/\n", "**Status**: under construction\n"):
            with self.subTest(text=text):
                self.put("standards/README.md", "# Entry\n" + text)
                code, result = self.check(refreeze=True)
                self.assertNotEqual(code, 0, result)
                self.assertTrue(any(item["check"] == "metadata" for item in result["failures"]), result)

    def test_external_citations_are_reported_not_rejected(self):
        self.put("standards/README.md", "# Entry\n[Attribution](https://example.org/license)\n")
        code, result = self.check(refreeze=True)
        self.assertEqual(code, 0, result)
        self.assertEqual(result["external_or_template_references"][0]["target"], "https://example.org/license")

    def test_declared_json_path_cannot_escape(self):
        self.put("standards/routes.json", '{"path":"../../outside.md"}')
        self.assert_failure(*self.check(refreeze=True), "escapes package")

    def test_advisories_visible_but_not_failure(self):
        self.put("standards/RULES.md", "# Rules\n## Stop rule\nA complete Product view is discussed here.\n")
        code, result = self.check(refreeze=True)
        self.assertEqual(code, 0, result)
        self.assertTrue(any("complete Product view" in item["text"] for item in result["advisory_signals"]))

    def test_tampered_checker_cannot_execute(self):
        marker = self.base / "executed"
        altered = self.base / "altered.py"
        altered.write_text(SCRIPT.read_text().replace("from __future__ import annotations\n", f"from __future__ import annotations\nopen({str(marker)!r}, 'w').write('executed')\n", 1))
        compile(altered.read_bytes(), str(altered), "exec")
        code, result = self.invoke("--help", script=altered, expected=self.script_sha)
        self.assertNotEqual(code, 0)
        self.assertIn("checker digest mismatch before execution", result["stderr"])
        self.assertFalse(marker.exists())

    def test_project_module_cannot_shadow_stdlib(self):
        marker = self.base / "shadow-ran"
        (self.base / "json.py").write_text(f"open({str(marker)!r}, 'w').write('ran')\nraise RuntimeError('shadow')\n")
        code, result = self.check()
        self.assertEqual(code, 0, result)
        self.assertFalse(marker.exists())

    def test_materialization_covers_every_byte_and_path(self):
        code, report, target = self.materialize()
        self.assertEqual(code, 0, report)
        expected = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        actual = {p.relative_to(target).as_posix(): p.read_bytes() for p in target.rglob("*") if p.is_file() and p.name != "manifest.json"}
        self.assertEqual(actual, expected)
        manifest = json.loads((target / "manifest.json").read_bytes())
        entries = manifest["standards"]["members"]
        exact = "".join(f"{m['sha256']}  specification/standards/{m['path']}\n" for m in sorted(entries, key=lambda value: value["path"]))
        wrong = "".join(f"{m['sha256']}  standards/{m['path']}\n" for m in sorted(entries, key=lambda value: value["path"]))
        self.assertEqual(manifest["standards"]["member_set_sha256"], sha(exact.encode()))
        self.assertNotEqual(manifest["standards"]["member_set_sha256"], sha(wrong.encode()))

    def test_unmapped_member_refused_before_output(self):
        self.put("README.md", "# Unsupported root entry\n")
        self.inventory, self.inventory_sha = self.freeze()
        code, result, target = self.materialize()
        self.assert_failure(code, result, "no canonical installed-manifest slot")
        self.assertFalse(target.exists())

    def test_hardcoded_donor_coordinates_rejected(self):
        coordinates = self.coordinates()
        coordinates["release"]["project_release_namespace"] = "stdo-claude"
        code, result, target = self.materialize(coordinates)
        self.assert_failure(code, result, "requires namespace")
        self.assertFalse(target.exists())

    def test_coordinate_pin_checked_before_materialization(self):
        path = self.base / "coordinates.json"
        path.write_text(json.dumps(self.coordinates()))
        target = self.base / "materialized"
        code, result = self.invoke("materialize", "--root", self.root, "--inventory", self.inventory, "--inventory-sha256", self.inventory_sha, "--coordinates", path, "--coordinates-sha256", "0" * 64, "--destination", target)
        self.assert_failure(code, result, "pinned input digest mismatch")
        self.assertFalse(target.exists())

    def test_empty_directory_has_no_installed_slot(self):
        (self.root / "empty").mkdir()
        self.inventory, self.inventory_sha = self.freeze()
        code, result, target = self.materialize()
        self.assert_failure(code, result, "no installed-manifest slot")
        self.assertFalse(target.exists())

    def test_outputs_cannot_pollute_candidate(self):
        code, result = self.invoke("freeze", "--root", self.root, "--inventory", self.root / "freeze.json")
        self.assert_failure(code, result, "outside the candidate")
        self.assertFalse((self.root / "freeze.json").exists())

    @unittest.skipUnless(INSTALLED_PYTHON.exists(), "installed toolchain Python unavailable")
    def test_installed_verifier_positive_and_wrong_digest_negative(self):
        self.put("standards/naïve.md", "# Unicode filename\n")
        self.inventory, self.inventory_sha = self.freeze()
        code, result, target = self.materialize()
        self.assertEqual(code, 0, result)
        verifier = """import hashlib, json, sys
from pathlib import Path
from stdo_toolchain.manifest import verify_materialization, manifest_bytes
from jsonschema import Draft202012Validator
p = Path(sys.argv[1])
m = json.loads((p / 'manifest.json').read_bytes())
assert manifest_bytes(m) == (p / 'manifest.json').read_bytes(), 'canonical JSON differs'
Draft202012Validator(json.loads(Path(sys.argv[2]).read_bytes())).validate(m)
if len(sys.argv) > 3:
    wrong = ''.join(f"{item['sha256']}  standards/{item['path']}\\n" for item in sorted(m['standards']['members'], key=lambda item: item['path']))
    m['standards']['member_set_sha256'] = hashlib.sha256(wrong.encode()).hexdigest()
print(json.dumps(verify_materialization(p, m)))
"""
        positive = subprocess.run([str(INSTALLED_PYTHON), "-I", "-c", verifier, str(target), str(INSTALLED_MANIFEST_SCHEMA)], capture_output=True, text=True, timeout=30)
        self.assertEqual(positive.returncode, 0, positive.stderr)
        self.assertEqual(json.loads(positive.stdout), [])
        negative = subprocess.run([str(INSTALLED_PYTHON), "-I", "-c", verifier, str(target), str(INSTALLED_MANIFEST_SCHEMA), "mutate"], capture_output=True, text=True, timeout=30)
        self.assertEqual(negative.returncode, 0, negative.stderr)
        self.assertIn("standards member-set digest does not reproduce", json.loads(negative.stdout))


if __name__ == "__main__":
    unittest.main()
