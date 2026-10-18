"""Install standalone V3 packages without selecting tenants or companions."""

from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from stdo_toolchain.errors import StdoError
from stdo_toolchain.git_source import GitSnapshot
from stdo_toolchain.manifest import build_manifest, manifest_sha256
from stdo_toolchain.product_definition import (
    adopt_definition,
    definition_status,
    install_bootstrap,
    sync_definition,
)
from stdo_toolchain.store import Store

from test_toolchain import definition_document, installed_payloads, run_git


PROJECT = "specification_methodology/v3"
CUT = "v3.0.0-rc.1"
URI = f"stdo://releases/{CUT}/"
SCHEMAS = Path(__file__).resolve().parents[1] / "specification/standards/schemas"


class PackageFixture:
    def __init__(self, root: Path) -> None:
        self.repository = root / "repository"
        self.project = self.repository / PROJECT
        self.project.mkdir(parents=True)
        self.payloads = {
            "standards/README.md": b"# Standalone V3\n",
            "standards/SPEC_METHOD.md": b"# Method\n",
            "standards/REFERENCE_FRAME.md": b"# Reference frames\n",
            "standards/EXECUTIVE_BASELINE.md": b"# Executive\n",
            "standards/frames/bootstrap.md": b"# V3 bootstrap\n",
            "standards/frames/task with spaces.md": b"# Space in member path\n",
            "standards/schemas/product-definition.schema.json": (
                SCHEMAS / "product-definition.schema.json"
            ).read_bytes(),
            "standards/schemas/installed-release-manifest.schema.json": (
                SCHEMAS / "installed-release-manifest.schema.json"
            ).read_bytes(),
            "plugins/spec/.codex-plugin/plugin.json": b'{"name":"spec"}\n',
            "plugins/spec/skills/stdo-work/SKILL.md": b"# V3 work\n",
            "LICENSE": b"fixture license\n",
            "release/release-note.md": b"# V3 fixture release\n",
        }
        for relative, data in self.payloads.items():
            path = self.project / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        # A sibling version and unpublished tenant never become V3 members.
        for relative in (
            "specification_methodology/v2/specification/standards/README.md",
            f"{PROJECT}/build_tenants/common/standards/README.md",
        ):
            path = self.repository / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("not the selected distribution\n", encoding="utf-8")
        run_git(self.repository, "init", "-q")
        run_git(self.repository, "config", "user.name", "STDO Test")
        run_git(self.repository, "config", "user.email", "test@example.invalid")
        self.commit()
        self.tag(CUT)

    def commit(self) -> None:
        run_git(self.repository, "add", ".")
        run_git(self.repository, "commit", "-qm", "fixture package")

    def tag(self, cut: str) -> None:
        run_git(
            self.repository, "tag", "-a", f"specification_methodology/{cut}", "-m", cut
        )

    def revision(self, cut: str = "v3.0.0-rc.2") -> None:
        self.commit()
        self.tag(cut)


class StandaloneV3Tests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="stdo-v3-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.fixture = PackageFixture(self.root)
        self.store = Store(self.root / "store")

    def test_install_manifest_resolve_and_reinstall_exact_package(self) -> None:
        with GitSnapshot(str(self.fixture.repository), CUT) as snapshot:
            self.assertEqual(snapshot.project_root, PROJECT)
            manifest = build_manifest(snapshot)
            self.assertEqual(
                snapshot.list_files("specification/standards/frames"),
                [
                    "specification/standards/frames/bootstrap.md",
                    "specification/standards/frames/task with spaces.md",
                ],
            )
        # Independently reproduce the established logical digest, not a digest
        # over the new physical location or a call back to the implementation.
        lines = "".join(
            f"{hashlib.sha256(data).hexdigest()}  specification/{path}\n"
            for path, data in sorted(self.fixture.payloads.items())
            if path.startswith("standards/")
        )
        self.assertEqual(
            manifest["standards"]["member_set_sha256"],
            hashlib.sha256(lines.encode()).hexdigest(),
        )
        self.assertEqual(
            manifest["standards"]["source_root"], "specification/standards"
        )
        self.assertEqual(
            manifest["auxiliary"]["release_note"]["source_path"], "releases/v3.0.0.md"
        )
        self.assertEqual(manifest["release"]["project_subtree_root"], PROJECT)
        for field, path in (
            ("standards_tree", f"{PROJECT}/standards"),
            ("project_subtree_tree", PROJECT),
        ):
            self.assertEqual(
                manifest["release"][field],
                run_git(self.fixture.repository, "rev-parse", f"HEAD:{path}"),
            )
        schema = json.loads(
            (SCHEMAS / "installed-release-manifest.schema.json").read_bytes()
        )
        Draft202012Validator(schema).validate(manifest)
        digest = manifest_sha256(manifest)
        installed = self.store.install(
            str(self.fixture.repository), CUT, expected_manifest_sha256=digest
        )
        self.assertEqual(installed.manifest, manifest)
        self.assertEqual(installed_payloads(installed.path), self.fixture.payloads)
        for path, data in self.fixture.payloads.items():
            self.assertEqual(self.store.resolve(URI + path).read_bytes(), data)
        self.assertTrue(
            self.store.verify(CUT, expected_manifest_sha256=digest)["valid"]
        )
        repeat = self.store.install(
            str(self.fixture.repository), CUT, expected_manifest_sha256=digest
        )
        self.assertEqual(repeat.status, "already_installed")
        self.assertEqual(installed_payloads(repeat.path), self.fixture.payloads)

    def test_canonical_v3_source_and_standalone_package_have_same_members(self) -> None:
        with GitSnapshot(str(self.fixture.repository), CUT) as snapshot:
            package = build_manifest(snapshot)
        (self.fixture.project / "specification").mkdir()
        (self.fixture.project / "standards").rename(
            self.fixture.project / "specification/standards"
        )
        (self.fixture.project / "releases").mkdir()
        (self.fixture.project / "release/release-note.md").rename(
            self.fixture.project / "releases/v3.0.0.md"
        )
        self.fixture.revision()
        with GitSnapshot(str(self.fixture.repository), "v3.0.0-rc.2") as snapshot:
            canonical = build_manifest(snapshot)
        self.assertEqual(package["standards"], canonical["standards"])
        self.assertEqual(package["auxiliary"], canonical["auxiliary"])
        self.assertEqual(
            package["release"]["standards_tree"], canonical["release"]["standards_tree"]
        )

    def test_two_v3_layouts_refuse_before_installation(self) -> None:
        path = self.fixture.project / "specification/standards/README.md"
        path.parent.mkdir(parents=True)
        path.write_text("competing package\n")
        self.fixture.revision()
        with self.assertRaisesRegex(StdoError, "exactly one STDO project layout"):
            self.store.install(str(self.fixture.repository), "v3.0.0-rc.2")
        self.assertFalse(self.store.registry_path.exists())
        self.assertFalse((self.store.releases_root / "v3.0.0-rc.2").exists())

    def test_tenant_is_never_selected_as_release_root(self) -> None:
        shutil.rmtree(self.fixture.project / "standards")
        self.fixture.revision()
        with self.assertRaisesRegex(StdoError, "found none"):
            self.store.install(str(self.fixture.repository), "v3.0.0-rc.2")
        self.assertFalse(self.store.registry_path.exists())

    def test_v3_package_cannot_supply_another_major_version(self) -> None:
        self.fixture.tag("v4.0.0-rc.1")
        with self.assertRaisesRegex(StdoError, "found none"):
            self.store.install(str(self.fixture.repository), "v4.0.0-rc.1")

    def test_missing_package_note_cannot_fall_back_to_old_source_note(self) -> None:
        (self.fixture.project / "release/release-note.md").unlink()
        (self.fixture.project / "releases").mkdir()
        (self.fixture.project / "releases/v3.0.0.md").write_text("wrong note\n")
        self.fixture.revision()
        with self.assertRaisesRegex(StdoError, "has no release note"):
            self.store.install(str(self.fixture.repository), "v3.0.0-rc.2")
        self.assertFalse(self.store.registry_path.exists())

    def test_wrong_manifest_and_tampering_refuse(self) -> None:
        with self.assertRaises(StdoError):
            self.store.install(
                str(self.fixture.repository), CUT, expected_manifest_sha256="0" * 64
            )
        self.assertFalse(self.store.registry_path.exists())
        installed = self.store.install(str(self.fixture.repository), CUT)
        member = installed.path / "standards/EXECUTIVE_BASELINE.md"
        member.chmod(0o644)
        member.write_text("one changed word\n")
        self.assertFalse(self.store.verify(CUT)["valid"])
        with self.assertRaises(StdoError):
            self.store.install(str(self.fixture.repository), CUT)
        with self.assertRaises(StdoError):
            self.store.resolve(URI + "standards/EXECUTIVE_BASELINE.md")

    def test_v3_consumer_sync_bootstrap_and_explicit_same_line_adoption(self) -> None:
        with GitSnapshot(str(self.fixture.repository), CUT) as snapshot:
            digest = manifest_sha256(build_manifest(snapshot))
        document = definition_document(self.fixture.repository, URI, digest)
        document.pop("unrelated")
        document["$schema"] = URI + "standards/schemas/product-definition.schema.json"
        document["constitution"]["stdo"]["selector"] = "stdo://channels/3.0.0"
        document["constitution"]["entrypoints"] = [
            {"basis": "#/constitution/stdo/basis", "uri": "standards/" + member}
            for member in (
                "frames/bootstrap.md",
                "SPEC_METHOD.md",
                "REFERENCE_FRAME.md",
                "EXECUTIVE_BASELINE.md",
            )
        ]
        consumer = self.root / "consumer"
        consumer.mkdir()
        definition = consumer / "stdo_default.json"
        before = (json.dumps(document, indent=2) + "\n").encode()
        definition.write_bytes(before)
        sync_definition(definition, self.store)
        self.assertEqual(definition.read_bytes(), before)
        self.assertTrue(definition_status(definition, self.store, verify=True)["valid"])
        for entry in document["constitution"]["entrypoints"]:
            self.assertTrue(self.store.resolve(URI + entry["uri"]).is_file())
        install_bootstrap(definition, self.store)
        bootstraps = {path.name: path.read_bytes() for path in consumer.glob("*.md")}
        self.assertEqual(set(bootstraps), {"AGENTS.md", "CLAUDE.md"})
        install_bootstrap(definition, self.store)
        self.assertEqual(
            {path.name: path.read_bytes() for path in consumer.glob("*.md")}, bootstraps
        )
        (self.fixture.project / "standards/SPEC_METHOD.md").write_text(
            "# Revised method\n"
        )
        self.fixture.revision()
        run_git(
            self.fixture.repository,
            "tag",
            "-a",
            "specification_methodology/v3.0.0",
            "-m",
            "selector",
        )
        plan = adopt_definition(definition, self.store, dry_run=True)
        self.assertFalse(self.store.is_installed("v3.0.0-rc.2"))
        self.assertEqual(definition.read_bytes(), before)
        with self.assertRaisesRegex(StdoError, "requires --accept-plan-sha256"):
            adopt_definition(definition, self.store)
        adopt_definition(
            definition, self.store, accepted_plan_sha256=plan["plan_sha256"]
        )
        updated = json.loads(definition.read_bytes())
        self.assertEqual(
            updated["constitution"]["stdo"]["basis"]["uri"],
            "stdo://releases/v3.0.0-rc.2/",
        )
        updated["constitution"]["stdo"]["basis"] = document["constitution"]["stdo"][
            "basis"
        ]
        updated["$schema"] = document["$schema"]
        self.assertEqual(updated, document)


if __name__ == "__main__":
    unittest.main()
