from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from stdo_toolchain.errors import StdoError
from stdo_toolchain.git_source import (
    GitSnapshot,
    cut_coordinates,
    ensure_channel_not_downgrade,
    normalize_cut,
    normalize_version_line,
    resolve_channel,
)
from stdo_toolchain.manifest import verify_materialization
from stdo_toolchain.product_definition import (
    adopt_definition,
    definition_status,
    discover_definitions,
    install_bootstrap,
    sync_definition,
)
from stdo_toolchain.store import Store
from stdo_toolchain.constants import (
    BOOTSTRAP_END,
    BOOTSTRAP_START,
    BOOTSTRAP_TEXT,
)
from stdo_toolchain.cli import _parser, run


def run_git(repository: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=repository,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def installed_payloads(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.relative_to(root).as_posix() != "manifest.json"
    }


class ReleaseFixture:
    def __init__(self, root: Path, *, project_prefix: str = ""):
        self.repository = root / "repository"
        self.repository.mkdir()
        self.project_root = (
            self.repository / project_prefix if project_prefix else self.repository
        )
        run_git(self.repository, "init", "-q")
        run_git(self.repository, "config", "user.name", "STDO Test")
        run_git(self.repository, "config", "user.email", "stdo-test@example.invalid")
        (self.project_root / "specification" / "standards").mkdir(parents=True)
        (self.project_root / "specification" / "standards" / "schemas").mkdir()
        (self.project_root / "plugins" / "spec" / "skills" / "refresh").mkdir(
            parents=True
        )
        (self.project_root / "releases").mkdir()
        (self.project_root / "LICENSE").write_text("test license\n", encoding="utf-8")
        (
            self.project_root / "specification" / "standards" / "SPEC_METHOD.md"
        ).write_text("# Spec one\n", encoding="utf-8")
        (self.project_root / "specification" / "standards" / "README.md").write_text(
            "# Standards\n", encoding="utf-8"
        )
        (
            self.project_root
            / "specification"
            / "standards"
            / "schemas"
            / "product-definition.schema.json"
        ).write_text(
            json.dumps(
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "type": "object",
                    "required": ["kind", "constitution"],
                    "properties": {
                        "kind": {"const": "stdo.product-definition"},
                        "constitution": {"type": "object"},
                    },
                }
            )
            + "\n",
            encoding="utf-8",
        )
        (
            self.project_root / "plugins" / "spec" / "skills" / "refresh" / "SKILL.md"
        ).write_text("# Refresh\n", encoding="utf-8")
        (self.project_root / "releases" / "v1.0.0.md").write_text(
            "# Release\n", encoding="utf-8"
        )
        if project_prefix:
            (self.repository / "MONOREPO.md").write_text(
                "# Repository root\n", encoding="utf-8"
            )
        run_git(self.repository, "add", ".")
        run_git(self.repository, "commit", "-qm", "release one")
        run_git(self.repository, "tag", "-a", "v1.0.0-rc.1", "-m", "RC1")
        run_git(self.repository, "tag", "-a", "v1.0.0", "-m", "line one")

    def add_rc2(self, *, advance_selector: bool = True) -> None:
        (
            self.project_root / "specification" / "standards" / "SPEC_METHOD.md"
        ).write_text("# Spec two\n", encoding="utf-8")
        run_git(self.repository, "add", ".")
        run_git(self.repository, "commit", "-qm", "release two")
        run_git(self.repository, "tag", "-a", "v1.0.0-rc.2", "-m", "RC2")
        if advance_selector:
            run_git(self.repository, "tag", "-fa", "v1.0.0", "-m", "line two")

    def add_qualified_rc2(self, *, advance_selector: bool = True) -> None:
        (
            self.project_root / "specification" / "standards" / "SPEC_METHOD.md"
        ).write_text("# Spec two\n", encoding="utf-8")
        run_git(self.repository, "add", ".")
        run_git(self.repository, "commit", "-qm", "release two")
        run_git(
            self.repository,
            "tag",
            "-a",
            "specification_methodology/v1.0.0-rc.2",
            "-m",
            "RC2",
        )
        if advance_selector:
            run_git(
                self.repository,
                "tag",
                "-fa",
                "specification_methodology/v1.0.0",
                "-m",
                "line two",
            )

    def add_rc3(self) -> None:
        (
            self.project_root / "specification" / "standards" / "SPEC_METHOD.md"
        ).write_text("# Spec three\n", encoding="utf-8")
        run_git(self.repository, "add", ".")
        run_git(self.repository, "commit", "-qm", "release three")
        run_git(self.repository, "tag", "-a", "v1.0.0-rc.3", "-m", "RC3")
        run_git(self.repository, "tag", "-fa", "v1.0.0", "-m", "line three")

    def make_selector_lightweight(self) -> None:
        run_git(self.repository, "tag", "-d", "v1.0.0")
        run_git(self.repository, "tag", "v1.0.0")

    def make_latest_cut_lightweight(self) -> None:
        run_git(self.repository, "tag", "-d", "v1.0.0-rc.2")
        run_git(self.repository, "tag", "v1.0.0-rc.2")


def definition_document(repository: Path, basis_uri: str, digest: str) -> dict:
    return {
        "$schema": "stdo://releases/v1.0.0-rc.1/standards/schemas/product-definition.schema.json",
        "kind": "stdo.product-definition",
        "product": {
            "definition_id": "urn:test:product-definition:one",
            "name": "Test Product",
            "source_project": "./",
            "bounded_context": None,
        },
        "constitution": {
            "stdo": {
                "source": {"repository": str(repository)},
                "selector": "stdo://channels/1.0.0",
                "basis": {
                    "uri": basis_uri,
                    "manifest_sha256": digest,
                },
            },
            "additional_authorities": [],
            "entrypoints": [
                {
                    "basis": "#/constitution/stdo/basis",
                    "uri": "standards/SPEC_METHOD.md",
                }
            ],
            "agent_bootstrap": {
                "entrypoint": "#/constitution/entrypoints/0",
                "targets": ["./AGENTS.md", "./CLAUDE.md"],
            },
        },
        "local_constitution": {
            "axioms": [],
            "overrides": [],
            "disambiguations": [],
        },
        "reference_frame_bases": [
            {
                "uri": "./specification/PRODUCT.md#frames",
                "authority": ["./specification/PRODUCT.md"],
                "applies_to": ["urn:test:product-definition:one"],
            }
        ],
        "what": {
            "intent": "./specification/INTENT.md",
            "product": "./specification/PRODUCT.md",
            "specification": ["./specification/requirements/"],
        },
        "how": {
            "common": [],
            "build_tenants": [
                {
                    "id": "urn:test:build-tenant:default",
                    "root": "./",
                    "design": ["./design/"],
                    "implementation": ["./src/"],
                }
            ],
        },
        "ticketing": {
            "goals": "./specification/PRODUCT.md",
            "tickets": {
                "root": "./.ai-workspace/tickets/",
                "lanes": {
                    "backlog": "./.ai-workspace/tickets/backlog/",
                    "active": "./.ai-workspace/tickets/active/",
                    "completed": "./.ai-workspace/tickets/completed/",
                },
            },
            "comments": {"root": "./.ai-workspace/comments/"},
        },
        "composition": [],
        "unrelated": {"preserved": True},
    }


class StoreTests(unittest.TestCase):
    def test_release_identity_parsing_reserves_the_rc_suffix(self) -> None:
        self.assertEqual(normalize_version_line("v2.4.3"), "2.4.3")
        self.assertEqual(normalize_cut("v2.4.3-rc.2"), "v2.4.3-rc.2")
        with self.assertRaises(StdoError):
            normalize_version_line("2.4.3-rc.2")
        with self.assertRaises(StdoError):
            normalize_cut("v2.4.3-rc.1-rc.2")
        self.assertEqual(cut_coordinates("v2.4.3-rc.12"), ("2.4.3", 12))

    def test_channel_refuses_a_lagging_selector(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            fixture.add_rc2(advance_selector=False)

            with self.assertRaisesRegex(
                StdoError,
                "latest published immutable cut is v1.0.0-rc.2",
            ):
                resolve_channel(str(fixture.repository), "1.0.0")

    def test_channel_and_install_cross_into_project_qualified_refs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(
                root,
                project_prefix="specification_methodology",
            )
            fixture.add_qualified_rc2()

            resolution = resolve_channel(str(fixture.repository), "1.0.0")
            self.assertEqual(resolution.cut, "v1.0.0-rc.2")
            self.assertEqual(resolution.cut_ordinal, 2)
            self.assertEqual(
                resolution.cut_ref,
                "refs/tags/specification_methodology/v1.0.0-rc.2",
            )
            self.assertEqual(
                resolution.selector_ref,
                "refs/tags/specification_methodology/v1.0.0",
            )

            installed = Store(root / "store").install(
                str(fixture.repository),
                resolution.cut,
            )
            self.assertEqual(installed.cut, "v1.0.0-rc.2")
            self.assertEqual(installed.manifest["release"]["cut"], "v1.0.0-rc.2")
            self.assertEqual(
                installed.manifest["release"]["tag_object"],
                run_git(
                    fixture.repository,
                    "rev-parse",
                    "specification_methodology/v1.0.0-rc.2",
                ),
            )
            self.assertEqual(
                installed.manifest["release"]["project_release_namespace"],
                "specification_methodology",
            )
            self.assertEqual(
                installed.manifest["release"]["qualified_ref"],
                "refs/tags/specification_methodology/v1.0.0-rc.2",
            )
            self.assertEqual(
                installed.manifest["release"]["project_subtree_root"],
                "specification_methodology",
            )
            self.assertEqual(
                installed.manifest["release"]["project_subtree_tree"],
                run_git(
                    fixture.repository,
                    "rev-parse",
                    "specification_methodology/v1.0.0-rc.2^{}:specification_methodology",
                ),
            )
            incomplete = json.loads(json.dumps(installed.manifest))
            del incomplete["release"]["qualified_ref"]
            self.assertIn(
                "incomplete shared-source release coordinates",
                verify_materialization(installed.path, incomplete),
            )
            from jsonschema import Draft202012Validator

            schema = json.loads(
                (
                    Path(__file__).resolve().parents[1]
                    / "specification/standards/schemas/installed-release-manifest.schema.json"
                ).read_text(encoding="utf-8")
            )
            self.assertTrue(
                list(Draft202012Validator(schema).iter_errors(incomplete)),
                "schema accepted incomplete shared-source release coordinates",
            )

    def test_channel_refuses_qualified_cut_without_qualified_selector(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(
                root,
                project_prefix="specification_methodology",
            )
            fixture.add_qualified_rc2()
            run_git(
                fixture.repository,
                "tag",
                "-d",
                "specification_methodology/v1.0.0",
            )
            run_git(
                fixture.repository,
                "tag",
                "-fa",
                "v1.0.0",
                "-m",
                "invalid moved historical selector",
                "specification_methodology/v1.0.0-rc.2^{}",
            )

            with self.assertRaisesRegex(
                StdoError,
                "must create its qualified selector",
            ):
                resolve_channel(str(fixture.repository), "1.0.0")

    def test_channel_refuses_qualified_selector_without_qualified_cut(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            run_git(
                fixture.repository,
                "tag",
                "-a",
                "specification_methodology/v1.0.0",
                "-m",
                "invalid qualified selector",
                "v1.0.0-rc.1^{}",
            )

            with self.assertRaisesRegex(
                StdoError,
                "has no project-qualified immutable cuts",
            ):
                resolve_channel(str(fixture.repository), "1.0.0")

    def test_channel_preserves_historical_selector_after_transition(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(
                root,
                project_prefix="specification_methodology",
            )
            fixture.add_qualified_rc2()
            run_git(
                fixture.repository,
                "tag",
                "-fa",
                "v1.0.0",
                "-m",
                "invalid moved historical selector",
                "specification_methodology/v1.0.0-rc.2^{}",
            )

            with self.assertRaisesRegex(
                StdoError,
                "Historical STDO channel selector must remain",
            ):
                resolve_channel(str(fixture.repository), "1.0.0")

    def test_channel_refuses_duplicate_local_cut_across_ref_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            fixture.add_rc2()
            run_git(
                fixture.repository,
                "tag",
                "-a",
                "specification_methodology/v1.0.0-rc.2",
                "-m",
                "duplicate RC2",
            )
            run_git(
                fixture.repository,
                "tag",
                "-a",
                "specification_methodology/v1.0.0",
                "-m",
                "qualified line two",
            )

            with self.assertRaisesRegex(StdoError, "ambiguous across refs"):
                resolve_channel(str(fixture.repository), "1.0.0")

            with self.assertRaisesRegex(
                StdoError,
                "ambiguous across historical and project-qualified refs",
            ):
                with GitSnapshot(str(fixture.repository), "v1.0.0-rc.2"):
                    self.fail("ambiguous cut unexpectedly opened")

    def test_channel_accepts_an_additional_ref_to_the_same_tag_object(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            fixture.add_rc2()
            store = Store(root / "store")
            before_alias = store.install(
                str(fixture.repository),
                "v1.0.0-rc.2",
            )
            run_git(
                fixture.repository,
                "update-ref",
                "refs/tags/specification_methodology/v1.0.0-rc.2",
                "refs/tags/v1.0.0-rc.2",
            )
            run_git(
                fixture.repository,
                "update-ref",
                "refs/tags/specification_methodology/v1.0.0",
                "refs/tags/v1.0.0",
            )

            resolution = resolve_channel(str(fixture.repository), "1.0.0")
            self.assertEqual(
                resolution.cut_ref,
                "refs/tags/specification_methodology/v1.0.0-rc.2",
            )
            after_alias = store.install(
                str(fixture.repository),
                resolution.cut,
            )
            self.assertEqual(after_alias.status, "already_installed")
            self.assertEqual(after_alias.manifest_sha256, before_alias.manifest_sha256)
            self.assertEqual(after_alias.manifest, before_alias.manifest)
            with GitSnapshot(str(fixture.repository), "v1.0.0-rc.2") as snapshot:
                self.assertEqual(snapshot.ref, "refs/tags/v1.0.0-rc.2")
                self.assertEqual(snapshot.tag_object, resolution.cut_tag_object)

    def test_channel_refuses_a_lightweight_latest_cut(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            fixture.add_rc2()
            fixture.make_latest_cut_lightweight()

            with self.assertRaisesRegex(
                StdoError,
                "Latest published STDO cut v1.0.0-rc.2 must be an annotated tag",
            ):
                resolve_channel(str(fixture.repository), "1.0.0")

    def test_channel_adoption_refuses_downgrade_but_exact_cut_remains_valid(
        self,
    ) -> None:
        with self.assertRaisesRegex(StdoError, "cannot move backward"):
            ensure_channel_not_downgrade("v1.0.0-rc.2", "v1.0.0-rc.1")

        ensure_channel_not_downgrade("v1.0.0-rc.1", "v1.0.0-rc.2")
        self.assertEqual(normalize_cut("v1.0.0-rc.1"), "v1.0.0-rc.1")

    def test_install_resolve_reinstall_and_detect_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")

            first = store.install(str(fixture.repository), "v1.0.0-rc.1")
            self.assertEqual(first.status, "installed")
            self.assertEqual(first.manifest["standards"]["member_count"], 3)
            self.assertTrue(
                store.resolve(first.uri + "standards/SPEC_METHOD.md").is_file()
            )
            self.assertTrue(store.verify(first.cut)["valid"])

            second = store.install(str(fixture.repository), "v1.0.0-rc.1")
            self.assertEqual(second.status, "already_installed")
            self.assertEqual(second.manifest_sha256, first.manifest_sha256)

            method = first.path / "standards" / "SPEC_METHOD.md"
            method.chmod(0o644)
            method.write_text("tampered\n", encoding="utf-8")
            report = store.verify(first.cut)
            self.assertFalse(report["valid"])
            self.assertTrue(
                any("changed standards member" in item for item in report["failures"])
            )
            with self.assertRaises(StdoError):
                store.resolve(first.uri + "standards/SPEC_METHOD.md")

    def test_install_projects_the_exact_nested_monorepo_layout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(
                root,
                project_prefix="specification_methodology",
            )
            store = Store(root / "store")

            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")

            self.assertEqual(
                installed.manifest["release"]["tree"],
                run_git(fixture.repository, "rev-parse", "v1.0.0-rc.1^{tree}"),
            )
            self.assertEqual(
                installed.manifest["release"]["standards_tree"],
                run_git(
                    fixture.repository,
                    "rev-parse",
                    "v1.0.0-rc.1:specification_methodology/specification/standards",
                ),
            )
            self.assertEqual(
                installed.manifest["standards"]["source_root"],
                "specification/standards",
            )
            self.assertEqual(
                installed.manifest["auxiliary"]["plugin"]["source_root"],
                "plugins/spec",
            )
            self.assertEqual(
                installed.manifest["auxiliary"]["release_note"]["source_path"],
                "releases/v1.0.0.md",
            )
            self.assertEqual(
                [
                    member["path"]
                    for member in installed.manifest["standards"]["members"]
                ],
                [
                    "README.md",
                    "SPEC_METHOD.md",
                    "schemas/product-definition.schema.json",
                ],
            )
            self.assertEqual(
                (installed.path / "standards" / "SPEC_METHOD.md").read_text(
                    encoding="utf-8"
                ),
                "# Spec one\n",
            )
            self.assertTrue(store.verify(installed.cut)["valid"])

            legacy_root = root / "legacy"
            legacy_root.mkdir()
            legacy_fixture = ReleaseFixture(legacy_root)
            legacy = Store(root / "legacy-store").install(
                str(legacy_fixture.repository),
                "v1.0.0-rc.1",
            )
            self.assertEqual(
                installed.manifest["standards"],
                legacy.manifest["standards"],
            )
            self.assertEqual(
                installed.manifest["auxiliary"],
                legacy.manifest["auxiliary"],
            )
            self.assertEqual(
                installed_payloads(installed.path),
                installed_payloads(legacy.path),
            )

    def test_install_refuses_ambiguous_legacy_and_nested_layouts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(
                root,
                project_prefix="specification_methodology",
            )
            legacy_standards = fixture.repository / "specification" / "standards"
            legacy_standards.mkdir(parents=True)
            (legacy_standards / "README.md").write_text(
                "# Ambiguous\n", encoding="utf-8"
            )
            run_git(fixture.repository, "add", ".")
            run_git(fixture.repository, "commit", "-qm", "ambiguous layout")
            run_git(
                fixture.repository,
                "tag",
                "-a",
                "v1.0.1-rc.1",
                "-m",
                "ambiguous",
            )

            with self.assertRaisesRegex(
                StdoError,
                "exactly one STDO project layout.*legacy root and nested root",
            ):
                Store(root / "store").install(
                    str(fixture.repository),
                    "v1.0.1-rc.1",
                )

    def test_install_refuses_a_cut_without_a_recognized_layout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repository = root / "repository"
            repository.mkdir()
            run_git(repository, "init", "-q")
            run_git(repository, "config", "user.name", "STDO Test")
            run_git(repository, "config", "user.email", "stdo-test@example.invalid")
            (repository / "README.md").write_text("# Not STDO\n", encoding="utf-8")
            run_git(repository, "add", ".")
            run_git(repository, "commit", "-qm", "not an STDO release")
            run_git(
                repository,
                "tag",
                "-a",
                "v1.0.0-rc.1",
                "-m",
                "not STDO",
            )

            snapshot = GitSnapshot(str(repository), "v1.0.0-rc.1")
            with self.assertRaisesRegex(
                StdoError,
                "exactly one STDO project layout.*found none",
            ):
                with snapshot:
                    self.fail("unrecognized layout unexpectedly opened")
            self.assertIsNone(snapshot.git_dir)
            self.assertIsNone(snapshot._temporary)

    def test_verify_detects_extra_release_member(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            extra = installed.path / "unexpected.txt"
            extra.write_text("not admitted\n", encoding="utf-8")
            report = store.verify(installed.cut)
            self.assertFalse(report["valid"])
            self.assertIn(
                "extra installed release member: unexpected.txt",
                report["failures"],
            )

    def test_install_refuses_unexpected_manifest_digest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            with self.assertRaises(StdoError):
                store.install(
                    str(fixture.repository),
                    "v1.0.0-rc.1",
                    expected_manifest_sha256="0" * 64,
                )
            self.assertEqual(store.list_releases(), [])

    def test_resolver_refuses_path_escape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            store.install(str(fixture.repository), "v1.0.0-rc.1")
            with self.assertRaises(StdoError):
                store.resolve("stdo://releases/v1.0.0-rc.1/%2E%2E/registry.json")

    def test_resolver_refuses_registry_redirection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            store.install(str(fixture.repository), "v1.0.0-rc.1")
            registry = json.loads(store.registry_path.read_text(encoding="utf-8"))
            registry["releases"]["v1.0.0-rc.1"]["path"] = "../redirected"
            store.registry_path.write_text(
                json.dumps(registry) + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(StdoError):
                store.resolve("stdo://releases/v1.0.0-rc.1/standards/SPEC_METHOD.md")

    def test_store_refuses_a_redirected_releases_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            store.install(str(fixture.repository), "v1.0.0-rc.1")
            physical_releases = root / "physical-releases"
            store.releases_root.rename(physical_releases)
            store.releases_root.symlink_to(physical_releases, target_is_directory=True)

            with self.assertRaises(StdoError):
                store.verify("v1.0.0-rc.1")
            with self.assertRaises(StdoError):
                store.resolve("stdo://releases/v1.0.0-rc.1/standards/SPEC_METHOD.md")

    def test_verify_detects_an_unmanifested_directory_symlink_alias(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            outside = root / "outside"
            outside.mkdir()
            (outside / "authority.md").write_text("not admitted\n", encoding="utf-8")
            (installed.path / "alias").symlink_to(outside, target_is_directory=True)

            report = store.verify(installed.cut)
            self.assertFalse(report["valid"])
            self.assertTrue(
                any("alias (redirect)" in failure for failure in report["failures"]),
                report["failures"],
            )
            with self.assertRaises(StdoError):
                store.resolve(installed.uri + "alias/authority.md")

    def test_lightweight_version_line_selector_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            fixture.make_selector_lightweight()
            with self.assertRaisesRegex(StdoError, "annotated tag"):
                resolve_channel(str(fixture.repository), "1.0.0")


class ProductDefinitionTests(unittest.TestCase):
    def test_fleet_sync_requires_all_and_materializes_each_selected_definition(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            planning_store = Store(root / "planning-store")
            planned = planning_store.install(str(fixture.repository), "v1.0.0-rc.1")
            fleet_root = root / "fleet"
            for label in ("one", "two"):
                project = fleet_root / label
                project.mkdir(parents=True)
                document = definition_document(
                    fixture.repository,
                    planned.uri,
                    planned.manifest_sha256,
                )
                document["product"]["definition_id"] = f"urn:test:fleet:{label}"
                (project / "stdo_default.json").write_text(
                    json.dumps(document, indent=2) + "\n",
                    encoding="utf-8",
                )

            parser = _parser()
            refused = parser.parse_args(
                [
                    "--store",
                    str(root / "store"),
                    "fleet",
                    "sync",
                    "--root",
                    str(fleet_root),
                ]
            )
            with self.assertRaises(StdoError):
                run(refused)

            permitted = parser.parse_args(
                [
                    "--store",
                    str(root / "store"),
                    "fleet",
                    "sync",
                    "--root",
                    str(fleet_root),
                    "--all",
                ]
            )
            result, exit_code = run(permitted)
            self.assertEqual(exit_code, 0)
            self.assertEqual(len(result["definitions"]), 2)
            self.assertTrue(
                all(
                    definition["status"] in {"installed", "verified"}
                    for definition in result["definitions"]
                )
            )

    def test_fleet_adoption_requires_the_externally_accepted_fleet_plan(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            rc1 = store.install(str(fixture.repository), "v1.0.0-rc.1")
            fleet_root = root / "fleet"
            definitions: list[Path] = []
            for label in ("one", "two"):
                project = fleet_root / label
                project.mkdir(parents=True)
                document = definition_document(
                    fixture.repository,
                    rc1.uri,
                    rc1.manifest_sha256,
                )
                document["product"]["definition_id"] = f"urn:test:fleet:{label}"
                definition = project / "stdo_default.json"
                definition.write_text(
                    json.dumps(document, indent=2) + "\n",
                    encoding="utf-8",
                )
                definitions.append(definition)
            fixture.add_rc2()
            parser = _parser()

            unaccepted = parser.parse_args(
                [
                    "--store",
                    str(store.root),
                    "fleet",
                    "adopt",
                    "--root",
                    str(fleet_root),
                    "--all",
                ]
            )
            with self.assertRaisesRegex(StdoError, "prior dry-run"):
                run(unaccepted)
            for definition in definitions:
                self.assertIn(
                    "v1.0.0-rc.1",
                    definition.read_text(encoding="utf-8"),
                )

            dry_run = parser.parse_args(
                [
                    "--store",
                    str(store.root),
                    "fleet",
                    "adopt",
                    "--root",
                    str(fleet_root),
                    "--all",
                    "--dry-run",
                ]
            )
            plan, exit_code = run(dry_run)
            self.assertEqual(exit_code, 0)

            accepted = parser.parse_args(
                [
                    "--store",
                    str(store.root),
                    "fleet",
                    "adopt",
                    "--root",
                    str(fleet_root),
                    "--all",
                    "--accept-plan-sha256",
                    plan["plan_sha256"],
                ]
            )
            applied, exit_code = run(accepted)
            self.assertEqual(exit_code, 0)
            self.assertEqual(
                applied["accepted_plan_sha256"],
                plan["plan_sha256"],
            )
            for definition in definitions:
                self.assertIn(
                    "v1.0.0-rc.2",
                    definition.read_text(encoding="utf-8"),
                )

    def test_definition_refuses_a_schema_from_another_release_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            definition = root / "stdo_default.json"
            document = definition_document(
                fixture.repository,
                installed.uri,
                installed.manifest_sha256,
            )
            document["$schema"] = (
                "stdo://releases/v1.0.0-rc.2/standards/schemas/"
                "product-definition.schema.json"
            )
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(StdoError):
                definition_status(definition, store)

    def test_definition_refuses_uppercase_scheme_schema_from_another_basis(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            rc1 = store.install(str(fixture.repository), "v1.0.0-rc.1")
            fixture.add_rc2()
            store.install(str(fixture.repository), "v1.0.0-rc.2")
            definition = root / "stdo_default.json"
            document = definition_document(
                fixture.repository,
                rc1.uri,
                rc1.manifest_sha256,
            )
            document["$schema"] = (
                "STDO://releases/v1.0.0-rc.2/standards/schemas/"
                "product-definition.schema.json"
            )
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(StdoError, "differs from its basis"):
                definition_status(definition, store)

    def test_agent_templates_match_the_manager_bootstrap_exactly(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        expected = f"{BOOTSTRAP_START}\n{BOOTSTRAP_TEXT}\n{BOOTSTRAP_END}\n"
        for name in ("AGENTS_TEMPLATE.md", "CLAUDE_TEMPLATE.md"):
            actual = (
                repository / "specification/standards/templates" / name
            ).read_text(encoding="utf-8")
            self.assertEqual(actual, expected)

    def test_sync_installs_only_the_selected_exact_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            planning_store = Store(root / "planning-store")
            planned = planning_store.install(str(fixture.repository), "v1.0.0-rc.1")
            definition = root / "project" / "stdo_default.json"
            definition.parent.mkdir()
            document = definition_document(
                fixture.repository,
                planned.uri,
                planned.manifest_sha256,
            )
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            fixture.add_rc2()
            store = Store(root / "store")

            dry_run = sync_definition(definition, store, dry_run=True)
            self.assertEqual(dry_run["status"], "would_install")
            self.assertEqual(store.list_releases(), [])

            synced = sync_definition(definition, store)
            self.assertEqual(synced["status"], "installed")
            self.assertTrue(definition_status(definition, store)["valid"])
            self.assertEqual(
                json.loads(definition.read_text(encoding="utf-8")),
                document,
            )
            self.assertEqual(
                [release["cut"] for release in store.list_releases()],
                ["v1.0.0-rc.1"],
            )

    def test_definition_resolves_a_relative_repository_from_its_own_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            planning_store = Store(root / "planning-store")
            planned = planning_store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            document = definition_document(
                Path("../repository"),
                planned.uri,
                planned.manifest_sha256,
            )
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            store = Store(root / "store")
            synced = sync_definition(definition, store)
            self.assertEqual(synced["status"], "installed")

    def test_sync_refuses_a_cut_that_differs_from_the_selected_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            definition = root / "project" / "stdo_default.json"
            definition.parent.mkdir()
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        "stdo://releases/v1.0.0-rc.1/",
                        "0" * 64,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            store = Store(root / "store")
            with self.assertRaises(StdoError):
                sync_definition(definition, store)
            self.assertEqual(store.list_releases(), [])

    def test_sync_preserves_an_explicit_older_cut_when_the_channel_is_newer(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            planning_store = Store(root / "planning-store")
            rc1 = planning_store.install(str(fixture.repository), "v1.0.0-rc.1")
            fixture.add_rc2()

            definition = root / "project" / "stdo_default.json"
            definition.parent.mkdir()
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        rc1.uri,
                        rc1.manifest_sha256,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )

            store = Store(root / "store")
            synced = sync_definition(definition, store)
            self.assertEqual(synced["basis"], "stdo://releases/v1.0.0-rc.1/")
            self.assertEqual(
                [release["cut"] for release in store.list_releases()],
                ["v1.0.0-rc.1"],
            )

    def test_adopt_refuses_a_same_line_downgrade_before_install_or_write(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            fixture.add_rc2()
            store = Store(root / "store")
            rc2 = store.install(str(fixture.repository), "v1.0.0-rc.2")
            definition = root / "project" / "stdo_default.json"
            definition.parent.mkdir()
            document = definition_document(
                fixture.repository,
                rc2.uri,
                rc2.manifest_sha256,
            )
            document["$schema"] = document["$schema"].replace(
                "v1.0.0-rc.1",
                "v1.0.0-rc.2",
            )
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            original = definition.read_bytes()

            rc1_commit = run_git(
                fixture.repository,
                "rev-parse",
                "v1.0.0-rc.1^{commit}",
            )
            run_git(fixture.repository, "tag", "-d", "v1.0.0-rc.2")
            run_git(
                fixture.repository,
                "tag",
                "-fa",
                "v1.0.0",
                "-m",
                "line rollback",
                rc1_commit,
            )

            with self.assertRaisesRegex(StdoError, "cannot move backward"):
                adopt_definition(definition, store, dry_run=True)

            self.assertEqual(definition.read_bytes(), original)
            self.assertEqual(
                [release["cut"] for release in store.list_releases()],
                ["v1.0.0-rc.2"],
            )

    def test_adopt_updates_only_basis_and_schema_release(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            rc1 = store.install(str(fixture.repository), "v1.0.0-rc.1")
            definition = root / "project" / "stdo_default.json"
            definition.parent.mkdir()
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        rc1.uri,
                        rc1.manifest_sha256,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            fixture.add_rc2()

            plan = adopt_definition(definition, store, dry_run=True)
            self.assertTrue(plan["changed"])
            self.assertEqual(plan["to"]["cut"], "v1.0.0-rc.2")
            self.assertEqual(len(store.list_releases()), 1)

            original = definition.read_bytes()
            with self.assertRaisesRegex(StdoError, "accept-plan-sha256"):
                adopt_definition(definition, store)
            self.assertEqual(definition.read_bytes(), original)

            applied = adopt_definition(
                definition,
                store,
                accepted_plan_sha256=plan["plan_sha256"],
            )
            self.assertTrue(applied["changed"])
            self.assertEqual(
                applied["accepted_plan_sha256"],
                plan["plan_sha256"],
            )
            updated = json.loads(definition.read_text(encoding="utf-8"))
            self.assertEqual(
                updated["constitution"]["stdo"]["basis"]["uri"],
                "stdo://releases/v1.0.0-rc.2/",
            )
            self.assertEqual(updated["unrelated"], {"preserved": True})
            self.assertIn(
                "v1.0.0-rc.2",
                updated["$schema"],
            )
            self.assertTrue(definition_status(definition, store, verify=True)["valid"])

    def test_adopt_replaces_a_candidate_local_schema_when_the_basis_advances(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            rc1 = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            candidate_schema = project / "candidate-product-definition.schema.json"
            candidate_schema.write_bytes(
                (
                    fixture.repository
                    / "specification/standards/schemas/product-definition.schema.json"
                ).read_bytes()
            )
            definition = project / "stdo_default.json"
            document = definition_document(
                fixture.repository,
                rc1.uri,
                rc1.manifest_sha256,
            )
            document["$schema"] = f"./{candidate_schema.name}"
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            fixture.add_rc2()

            plan = adopt_definition(definition, store, dry_run=True)
            adopt_definition(
                definition,
                store,
                accepted_plan_sha256=plan["plan_sha256"],
            )
            updated = json.loads(definition.read_text(encoding="utf-8"))
            self.assertEqual(
                updated["$schema"],
                "stdo://releases/v1.0.0-rc.2/standards/schemas/"
                "product-definition.schema.json",
            )

    def test_adopt_refuses_a_plan_after_the_selector_moves(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            rc1 = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            document = definition_document(
                fixture.repository,
                rc1.uri,
                rc1.manifest_sha256,
            )
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            fixture.add_rc2()
            accepted = adopt_definition(definition, store, dry_run=True)
            fixture.add_rc3()

            with self.assertRaisesRegex(StdoError, "explicitly accepted plan"):
                adopt_definition(
                    definition,
                    store,
                    accepted_plan_sha256=accepted["plan_sha256"],
                )
            self.assertEqual(
                json.loads(definition.read_text(encoding="utf-8")),
                document,
            )
            self.assertEqual(
                [release["cut"] for release in store.list_releases()],
                ["v1.0.0-rc.1"],
            )

    def test_bootstrap_is_marker_bounded_and_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        installed.uri,
                        installed.manifest_sha256,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            (project / "AGENTS.md").write_text("# Local Rules\n", encoding="utf-8")

            first = install_bootstrap(definition, store)
            second = install_bootstrap(definition, store)
            self.assertEqual(first["targets"][0]["action"], "appended")
            self.assertEqual(second["targets"][0]["action"], "unchanged")
            agents = (project / "AGENTS.md").read_text(encoding="utf-8")
            self.assertTrue(agents.startswith("# Local Rules\n"))
            self.assertEqual(agents.count("<!-- STDO_BOOTSTRAP_START -->"), 1)
            self.assertTrue((project / "CLAUDE.md").is_file())

    def test_bootstrap_refuses_malformed_existing_markers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        installed.uri,
                        installed.manifest_sha256,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            (project / "AGENTS.md").write_text(
                "<!-- STDO_BOOTSTRAP_START -->\n",
                encoding="utf-8",
            )
            with self.assertRaises(StdoError):
                install_bootstrap(definition, store)

    def test_bootstrap_refuses_reversed_markers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        installed.uri,
                        installed.manifest_sha256,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            target = project / "CLAUDE.md"
            original = f"{BOOTSTRAP_END}\nowned\n{BOOTSTRAP_START}\n".encode()
            target.write_bytes(original)
            with self.assertRaises(StdoError):
                install_bootstrap(definition, store)
            self.assertEqual(target.read_bytes(), original)
            self.assertFalse((project / "AGENTS.md").exists())

    def test_bootstrap_preserves_existing_prefix_suffix_and_trailing_whitespace(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            definition.write_text(
                json.dumps(
                    definition_document(
                        fixture.repository,
                        installed.uri,
                        installed.manifest_sha256,
                    ),
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            target = project / "AGENTS.md"
            prefix = b"# Owned prefix\n \t\n"
            suffix = b"\n# Owned suffix\n\t  \n"
            target.write_bytes(
                prefix
                + BOOTSTRAP_START.encode()
                + b"\nstale\n"
                + BOOTSTRAP_END.encode()
                + suffix
            )

            install_bootstrap(definition, store)
            updated = target.read_bytes()
            self.assertTrue(updated.startswith(prefix))
            self.assertTrue(updated.endswith(suffix))

            unmarked = project / "CLAUDE.md"
            owned = b"# Owned\n \t\n"
            unmarked.write_bytes(owned)
            install_bootstrap(definition, store)
            self.assertTrue(unmarked.read_bytes().startswith(owned))

    def test_bootstrap_refuses_target_escape(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            project = root / "project"
            project.mkdir()
            definition = project / "stdo_default.json"
            document = definition_document(
                fixture.repository,
                installed.uri,
                installed.manifest_sha256,
            )
            document["constitution"]["agent_bootstrap"]["targets"] = ["../../victim.md"]
            definition.write_text(
                json.dumps(document, indent=2) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(StdoError, "confined relative path"):
                install_bootstrap(definition, store)
            self.assertFalse((root.parent / "victim.md").exists())

    def test_fleet_bootstrap_preflights_all_source_project_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = ReleaseFixture(root)
            store = Store(root / "store")
            installed = store.install(str(fixture.repository), "v1.0.0-rc.1")
            fleet = root / "fleet"
            first = fleet / "first"
            second = fleet / "second"
            outside = root / "outside"
            first.mkdir(parents=True)
            second.mkdir(parents=True)
            outside.mkdir()
            for label, project in (("first", first), ("second", second)):
                document = definition_document(
                    fixture.repository,
                    installed.uri,
                    installed.manifest_sha256,
                )
                document["product"]["definition_id"] = f"urn:test:fleet:{label}"
                if label == "second":
                    document["product"]["source_project"] = "../../outside"
                (project / "stdo_default.json").write_text(
                    json.dumps(document, indent=2) + "\n",
                    encoding="utf-8",
                )

            arguments = _parser().parse_args(
                [
                    "--store",
                    str(store.root),
                    "fleet",
                    "bootstrap",
                    "--root",
                    str(fleet),
                    "--all",
                ]
            )
            with self.assertRaisesRegex(StdoError, "authorized fleet root"):
                run(arguments)
            self.assertFalse((first / "AGENTS.md").exists())
            self.assertFalse((outside / "AGENTS.md").exists())

    def test_discovery_skips_managed_and_dependency_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "a").mkdir()
            (root / "a" / "stdo_one.json").write_text("{}\n", encoding="utf-8")
            for skipped in (
                ".hg",
                ".stdo",
                ".venv",
                "build",
                "dist",
                "node_modules",
                "vendor",
            ):
                (root / skipped).mkdir()
                (root / skipped / "stdo_hidden.json").write_text(
                    "{}\n", encoding="utf-8"
                )
            self.assertEqual(
                discover_definitions(root),
                [(root / "a" / "stdo_one.json").resolve()],
            )


if __name__ == "__main__":
    unittest.main()
