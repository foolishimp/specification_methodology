"""Stable release identity, legacy conservation, and actual acquisition paths."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError

from stdo_toolchain.errors import StdoError
from stdo_toolchain.git_source import (
    GitSnapshot, STABLE_TAG_MARKER, cut_coordinates,
    ensure_channel_not_downgrade, normalize_cut, resolve_channel,
)
from stdo_toolchain.manifest import build_manifest, manifest_sha256, verify_materialization
from stdo_toolchain.product_definition import (
    adopt_definition, definition_status, sync_definition,
)
from stdo_toolchain.store import Store

from test_toolchain import definition_document, installed_payloads, run_git
from test_v3_package import PackageFixture


CUT = "v3.0.2"
REF = f"specification_methodology/{CUT}"
URI = f"stdo://releases/{CUT}/"
SCHEMAS = Path(__file__).resolve().parents[2] / "v3/build_tenants/common/standards/schemas"


class StableReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="stdo-stable-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.fixture = PackageFixture(self.root)
        for name in ("product-definition.schema.json", "installed-release-manifest.schema.json"):
            relative = f"standards/schemas/{name}"
            data = (SCHEMAS / name).read_bytes()
            (self.fixture.project / relative).write_bytes(data)
            self.fixture.payloads[relative] = data
        self.fixture.commit()
        self.tag(STABLE_TAG_MARKER)
        self.store = Store(self.root / "store")

    def tag(self, message: str) -> None:
        run_git(self.fixture.repository, "tag", "-fa", REF, "-m", message)

    def manifest(self) -> dict:
        with GitSnapshot(str(self.fixture.repository), CUT) as snapshot:
            return build_manifest(snapshot)

    def definition(self, digest: str) -> Path:
        document = definition_document(self.fixture.repository, URI, digest)
        document.pop("unrelated")
        document["$schema"] = URI + "standards/schemas/product-definition.schema.json"
        document["constitution"]["stdo"]["selector"] = "stdo://channels/3.0.2"
        consumer = self.root / "consumer"
        consumer.mkdir()
        path = consumer / "stdo_default.json"
        path.write_text(json.dumps(document, indent=2) + "\n")
        return path

    def test_exact_manifest_install_uri_verify_and_pinned_definition(self) -> None:
        manifest = self.manifest()
        self.assertEqual(manifest["release"]["profile"], "stable-v1")
        self.assertEqual(manifest["release"]["qualified_ref"], f"refs/tags/{REF}")
        self.assertEqual(manifest["auxiliary"]["release_note"]["source_path"], "releases/v3.0.2.md")
        Draft202012Validator(json.loads((SCHEMAS / "installed-release-manifest.schema.json").read_bytes())).validate(manifest)
        digest = manifest_sha256(manifest)
        path = self.definition(digest)
        original = path.read_bytes()
        result = sync_definition(path, self.store)
        self.assertEqual(result["status"], "installed")
        self.assertEqual(path.read_bytes(), original)
        self.assertTrue(definition_status(path, self.store, verify=True)["valid"])
        self.assertEqual(installed_payloads(Path(result["path"])), self.fixture.payloads)
        for name, data in self.fixture.payloads.items():
            self.assertEqual(self.store.resolve(URI + name).read_bytes(), data)
        self.assertTrue(self.store.verify(CUT, expected_manifest_sha256=digest)["valid"])
        repeat = self.store.install(str(self.fixture.repository), CUT, expected_manifest_sha256=digest)
        self.assertEqual(repeat.status, "already_installed")
        channel = resolve_channel(str(self.fixture.repository), "3.0.2")
        self.assertIsNone(channel.cut_ordinal)
        self.assertEqual(channel.cut_ref, channel.selector_ref)
        self.assertEqual(channel.cut_tag_object, manifest["release"]["tag_object"])
        self.assertFalse(adopt_definition(path, self.store, dry_run=True)["changed"])

    def test_wrong_digest_and_changed_member_refuse(self) -> None:
        with self.assertRaisesRegex(StdoError, "manifest digest differs"):
            self.store.install(str(self.fixture.repository), CUT, expected_manifest_sha256="0" * 64)
        self.assertFalse(self.store.registry_path.exists())
        installed = self.store.install(str(self.fixture.repository), CUT)
        member = installed.path / "standards/SPEC_METHOD.md"
        member.chmod(0o644)  # Deliberate isolated-fixture tampering after immutable install.
        member.write_text("changed\n")
        self.assertFalse(self.store.verify(CUT)["valid"])

    def test_marker_must_be_unique_exact_and_supported(self) -> None:
        for message in (
            "release", "STDO-Release-Profile: stable-v2",
            STABLE_TAG_MARKER + "\n" + STABLE_TAG_MARKER,
            " " + STABLE_TAG_MARKER,
            STABLE_TAG_MARKER + "\n " + STABLE_TAG_MARKER,
        ):
            with self.subTest(message=message):
                self.tag(message)
                with self.assertRaisesRegex(StdoError, "exactly one explicit"):
                    self.manifest()
                with self.assertRaises(StdoError):
                    resolve_channel(str(self.fixture.repository), "3.0.2")

    def test_lightweight_stable_ref_refuses(self) -> None:
        run_git(self.fixture.repository, "tag", "-d", REF)
        run_git(self.fixture.repository, "tag", REF)
        with self.assertRaisesRegex(StdoError, "annotated"):
            self.manifest()

    def test_same_line_rc_presence_forbids_stable_identity(self) -> None:
        for ref in ("v3.0.2-rc.1", "specification_methodology/v3.0.2-rc.1"):
            with self.subTest(ref=ref):
                run_git(self.fixture.repository, "tag", "-a", ref, "-m", "legacy RC")
                with self.assertRaisesRegex(StdoError, "fresh version line"):
                    self.manifest()
                with self.assertRaises(StdoError):
                    resolve_channel(str(self.fixture.repository), "3.0.2")
                run_git(self.fixture.repository, "tag", "-d", ref)

    def test_historical_bare_alias_refuses_even_same_tag_object(self) -> None:
        run_git(self.fixture.repository, "update-ref", "refs/tags/v3.0.2", run_git(self.fixture.repository, "rev-parse", REF))
        with self.assertRaisesRegex(StdoError, "historical bare aliases"):
            self.manifest()
        with self.assertRaises(StdoError):
            resolve_channel(str(self.fixture.repository), "3.0.2")

    def test_tag_name_and_direct_commit_binding(self) -> None:
        other = "specification_methodology/v3.0.3"
        run_git(self.fixture.repository, "update-ref", f"refs/tags/{other}", run_git(self.fixture.repository, "rev-parse", REF))
        with self.assertRaisesRegex(StdoError, "tag name"):
            with GitSnapshot(str(self.fixture.repository), "v3.0.3"):
                pass
        run_git(self.fixture.repository, "tag", "-fa", other, REF, "-m", STABLE_TAG_MARKER)
        with self.assertRaisesRegex(StdoError, "directly annotate a commit"):
            with GitSnapshot(str(self.fixture.repository), "v3.0.3"):
                pass

    def test_legacy_bare_selector_is_not_an_exact_stable_cut(self) -> None:
        run_git(self.fixture.repository, "tag", "-a", "specification_methodology/v3.0.0", "-m", "legacy selector", "specification_methodology/v3.0.0-rc.1^{}")
        legacy = resolve_channel(str(self.fixture.repository), "3.0.0")
        self.assertEqual(legacy.cut, "v3.0.0-rc.1")
        self.assertEqual(legacy.cut_ordinal, 1)
        with self.assertRaisesRegex(StdoError, "fresh version line"):
            self.store.install(str(self.fixture.repository), "v3.0.0")
        with GitSnapshot(str(self.fixture.repository), legacy.cut) as snapshot:
            manifest = build_manifest(snapshot)
        self.assertNotIn("profile", manifest["release"])
        self.assertTrue(self.store.install(str(self.fixture.repository), legacy.cut).manifest == manifest)

    def test_stable_marker_cannot_be_reinterpreted_as_legacy_selector(self) -> None:
        run_git(self.fixture.repository, "tag", "-a", "specification_methodology/v3.0.2-rc.1", "-m", "RC")
        with self.assertRaisesRegex(StdoError, "cannot be used as a legacy RC selector"):
            resolve_channel(str(self.fixture.repository), "3.0.2")

    def test_manifest_profile_is_required_only_for_stable_cuts(self) -> None:
        manifest = self.manifest()
        installed = self.store.install(str(self.fixture.repository), CUT)
        schema = Draft202012Validator(json.loads((SCHEMAS / "installed-release-manifest.schema.json").read_bytes()))
        for profile in (None, "stable-v2"):
            bad = copy.deepcopy(manifest)
            if profile is None:
                del bad["release"]["profile"]
            else:
                bad["release"]["profile"] = profile
            with self.assertRaises(ValidationError):
                schema.validate(bad)
            self.assertIn("stable release requires stable-v1 manifest profile", verify_materialization(installed.path, bad))
        bad = copy.deepcopy(manifest)
        bad["release"]["cut"] = "v3.0.2-rc.1"
        bad["release"]["qualified_ref"] += "-rc.1"
        with self.assertRaises(ValidationError):
            schema.validate(bad)
        self.assertIn("legacy RC release cannot claim a stable release profile", verify_materialization(installed.path, bad))

    def test_stable_syntax_and_same_line_downgrade(self) -> None:
        self.assertEqual(normalize_cut(CUT), CUT)
        self.assertEqual(cut_coordinates(CUT), ("3.0.2", None))
        for value in ("v03.0.2", "v3.0", "v3.0.2-final", "v3.0.2+build", "v3.0.2-rc.0"):
            with self.subTest(value=value), self.assertRaises(StdoError):
                normalize_cut(value)
        ensure_channel_not_downgrade(CUT, CUT)
        with self.assertRaisesRegex(StdoError, "cannot move backward"):
            ensure_channel_not_downgrade(CUT, "v3.0.2-rc.9")


if __name__ == "__main__":
    unittest.main()
