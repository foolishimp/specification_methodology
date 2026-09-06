from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_stack_release.py"
SPEC = importlib.util.spec_from_file_location("check_stack_release", SCRIPT)
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


def run(root: Path, *arguments: str) -> str:
    return subprocess.run(
        list(arguments),
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(checker.canonical_json_bytes(value))


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def create_product_subject(
    root: Path,
    subtree: str,
    members: list[tuple[str, str, str | None]],
) -> dict[str, object]:
    descriptors = []
    for kind, relative, target in sorted(members, key=lambda row: row[1]):
        path = root / subtree / relative
        if kind == "symlink":
            assert target is not None
            path.parent.mkdir(parents=True, exist_ok=True)
            path.symlink_to(target)
            value = target.encode("utf-8")
        else:
            if not path.is_file():
                write_text(path, f"{subtree}:{relative}\n")
            value = path.read_bytes()
        descriptor = {
            "type": kind,
            "path": relative,
            "sha256": checker.sha256(value),
        }
        if target is not None:
            descriptor["target"] = target
        descriptors.append(descriptor)
    return {
        "member_count": len(descriptors),
        "member_set_sha256": checker.product_member_stream(descriptors),
        "members": descriptors,
    }


def release_inventory_rows(subject: dict[str, object]) -> list[str]:
    rows = []
    for member in subject["members"]:
        label = f"`{member['path']}`"
        if member["type"] == "symlink":
            label += f" -> `{member['target']}`"
        rows.append(f"| {member['type']} | {label} | `{member['sha256']}` |")
    rows.append(str(subject["member_set_sha256"]))
    return rows


class CohortFixture:
    version = "1.2.3-rc.4"
    cut = f"v{version}"
    semantic = "1.2.3"

    def __init__(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "source"
        self.remote = Path(self.temporary.name) / "remote.git"
        self.root.mkdir()
        run(self.root, "git", "init", "-q")
        run(self.root, "git", "config", "user.name", "Test")
        run(self.root, "git", "config", "user.email", "test@example.invalid")
        run(self.root, "git", "init", "--bare", "-q", str(self.remote))
        run(self.root, "git", "remote", "add", "origin", str(self.remote))
        self._commit_a()
        self._commit_b()

    def close(self) -> None:
        self.temporary.cleanup()

    def _commit_a(self) -> None:
        write_text(
            self.root / "specification_methodology/specification/standards/A.md",
            "# A\n",
        )
        write_text(self.root / "specification_methodology/LICENSE", "license\n")
        for relative in (
            ".claude-plugin/plugin.json",
            ".codex-plugin/plugin.json",
        ):
            write_json(
                self.root / f"specification_methodology/plugins/spec/{relative}",
                {"name": "spec", "version": self.version},
            )
        write_text(
            self.root / f"specification_methodology/releases/v{self.semantic}.md",
            "\n".join(
                (
                    f"product-local cut name is `{self.cut}`",
                    f"`refs/tags/specification_methodology/{self.cut}`",
                    "",
                )
            ),
        )
        run(self.root, "git", "add", "specification_methodology")
        run(self.root, "git", "commit", "-qm", "commit A")
        run(
            self.root,
            "git",
            "tag",
            "-a",
            f"specification_methodology/{self.cut}",
            "-m",
            "STDO cut",
        )

    def _product(self, namespace: str, subtree: str) -> dict[str, object]:
        return {
            "namespace": namespace,
            "subtree": subtree,
            "version": self.version,
            "release_ref": f"refs/tags/{namespace}/{self.cut}",
            "selector_ref": f"refs/tags/{namespace}/v{self.semantic}",
            "rc_branch": f"refs/heads/rc/{namespace}/{self.semantic}",
            "release_branch": f"refs/heads/release/{namespace}/{self.semantic}",
            "release_note": f"{subtree}/releases/v{self.semantic}.md",
        }

    def _commit_b(self) -> None:
        spec_product = self._product(
            "specification_methodology", "specification_methodology"
        )
        identity = checker.local_tag_identity(
            self.root,
            str(spec_product["release_ref"]),
            str(spec_product["subtree"]),
        )
        tag_view = checker.View(self.root, f"{spec_product['release_ref']}^{{}}")
        standards, plugin = checker.inventories(tag_view, str(spec_product["subtree"]))
        freeze: dict[str, object] = {
            **identity,
            "standards_member_count": len(standards),
            "standards_member_set_sha256": checker.member_stream(
                (f"specification/standards/{row['path']}", row["sha256"])
                for row in standards
            ),
            "plugin_member_count": len(plugin),
            "plugin_member_set_sha256": checker.member_stream(
                (f"./{row['path']}", row["sha256"]) for row in plugin
            ),
        }
        installed = checker.expected_installed_manifest(
            tag_view, spec_product, freeze, standards, plugin, self.cut
        )
        freeze["installed_manifest_sha256"] = checker.sha256(
            checker.canonical_json_bytes(installed)
        )
        spec_product["freeze"] = freeze
        spec_product["release_note_markers"] = [
            f"product-local cut name is `{self.cut}`",
            f"`refs/tags/specification_methodology/{self.cut}`",
        ]

        axiom = self._product("axiom_indexer", "axiom_indexer")
        axiom_markers = [
            f"product-local cut: {self.cut}",
            f"qualified immutable tag ref: refs/tags/axiom_indexer/{self.cut}",
            "matched Source STDO cut: "
            f"refs/tags/specification_methodology/{self.cut}",
            f"public basis: stdo://releases/{self.cut}/",
        ]
        axiom["release_note_markers"] = axiom_markers
        axiom["subject"] = create_product_subject(
            self.root,
            "axiom_indexer",
            [
                (
                    "symlink",
                    ".agents/skills/axiomatize-corpus",
                    "../../skills/axiomatize-corpus",
                ),
                (
                    "symlink",
                    ".claude/skills/axiomatize-corpus",
                    "../../skills/axiomatize-corpus",
                ),
                ("file", "build_tenants/core/code/ac.py", None),
                ("file", "skills/axiomatize-corpus/SKILL.md", None),
                ("file", "skills/axiomatize-corpus/agents/openai.yaml", None),
                (
                    "file",
                    "skills/axiomatize-corpus/references/output-contract.md",
                    None,
                ),
                (
                    "file",
                    "skills/axiomatize-corpus/references/program.schema.json",
                    None,
                ),
            ],
        )
        write_text(
            self.root / str(axiom["release_note"]),
            "\n".join((*axiom_markers, *release_inventory_rows(axiom["subject"])))
            + "\n",
        )

        representation = self._product("stdo_representation", "stdo_representation")
        representation_markers = [
            f"release version: {self.version}",
            f"product-local cut: {self.cut}",
            "qualified immutable tag ref: " f"refs/tags/stdo_representation/{self.cut}",
            "matched Source STDO cut: "
            f"refs/tags/specification_methodology/{self.cut}",
            f"public basis: stdo://releases/{self.cut}/",
            f"exact Axiom dependency: refs/tags/axiom_indexer/{self.cut}",
        ]
        representation["release_note_markers"] = representation_markers

        semantic_root = (
            "stdo_representation/build_tenants/axiom_indexer/representation/"
            f"stdo-{self.cut}"
        )
        relative_root = semantic_root.removeprefix("stdo_representation/")
        source_uri = f"stdo://releases/{self.cut}/"
        source_basis = f"{source_uri}standards/"
        source_corpus = {
            "kind": "stdo-representation.source-corpus",
            "schema_version": 1,
            "representation_version": self.version,
            "source_release": {
                "cut": self.cut,
                "uri": source_uri,
                "qualified_ref": spec_product["release_ref"],
                "tag_object": freeze["tag_object"],
                "commit": freeze["commit"],
                "tree": freeze["tree"],
                "project_subtree_root": spec_product["subtree"],
                "project_subtree_tree": freeze["project_subtree_tree"],
                "standards_tree": freeze["standards_tree"],
                "installed_manifest_sha256": freeze["installed_manifest_sha256"],
                "standards_member_count": freeze["standards_member_count"],
                "standards_member_set_sha256": freeze["standards_member_set_sha256"],
                "standards_members": standards,
            },
        }
        program_uri = f"urn:test:program:stdo-v{self.version}"
        program = {
            "kind": "axiom-indexer.axiomatic-program",
            "schema_version": 1,
            "uri": program_uri,
            "calculus_ref": f"{source_basis}A.md",
            "source_basis": source_basis,
        }
        program_sha = "sha256:" + checker.canonical_value_sha256(program)
        source_row = {
            "uri": f"{source_basis}A.md",
            "sha256": f"sha256:{standards[0]['sha256']}",
        }
        constraint_map = {
            "kind": "axiom-indexer.logical-constraint-map",
            "schema_version": 1,
            "program_uri": program_uri,
            "program_sha256": program_sha,
            "source_basis": source_basis,
            "resolved_sources": [source_row],
        }
        constraint_map["map_sha256"] = "sha256:" + checker.canonical_value_sha256(
            constraint_map
        )
        report = {
            "kind": "axiom-indexer.validation-report",
            "schema_version": 1,
            "status": "valid",
            "program_uri": program_uri,
            "program_sha256": program_sha,
            "diagnostics": [],
            "resolved_sources": [source_row],
        }
        files = {
            "source-corpus.json": source_corpus,
            "axiomatic-program.json": program,
            "logical-constraint-map.json": constraint_map,
            "validation-report.json": report,
        }
        for name, payload in files.items():
            write_json(self.root / semantic_root / name, payload)

        representation["subject"] = create_product_subject(
            self.root,
            "stdo_representation",
            [
                (
                    "symlink",
                    ".agents/skills/stdo-representation",
                    "../../skills/stdo-representation",
                ),
                (
                    "symlink",
                    ".claude/skills/stdo-representation",
                    "../../skills/stdo-representation",
                ),
                ("file", f"{relative_root}/axiomatic-program.json", None),
                ("file", f"{relative_root}/logical-constraint-map.json", None),
                ("file", "skills/stdo-representation/SKILL.md", None),
                ("file", "skills/stdo-representation/agents/openai.yaml", None),
                ("file", "skills/stdo-representation/references/claude.md", None),
                ("file", "skills/stdo-representation/references/codex.md", None),
            ],
        )
        axiom_members = {
            member["path"]: member for member in axiom["subject"]["members"]
        }
        mechanics = []
        for role, path in (
            ("executable", "build_tenants/core/code/ac.py"),
            (
                "output_contract",
                "skills/axiomatize-corpus/references/output-contract.md",
            ),
            ("schema", "skills/axiomatize-corpus/references/program.schema.json"),
        ):
            mechanics.append(
                {"role": role, "path": path, "sha256": axiom_members[path]["sha256"]}
            )
        axiom_release_digest = checker.sha256(
            (self.root / str(axiom["release_note"])).read_bytes()
        )
        representation["dependencies"] = {
            "axiom_indexer": {
                "version": self.version,
                "release_ref": axiom["release_ref"],
                "product_member_count": axiom["subject"]["member_count"],
                "product_member_set_sha256": axiom["subject"]["member_set_sha256"],
                "release_record": {
                    "path": axiom["release_note"],
                    "sha256": axiom_release_digest,
                },
                "mechanics": mechanics,
            }
        }

        release_member_paths = [
            f"{relative_root}/axiomatic-program.json",
            f"{relative_root}/logical-constraint-map.json",
        ]
        bound_paths = [
            f"{relative_root}/source-corpus.json",
            *release_member_paths,
            f"{relative_root}/validation-report.json",
        ]
        bound_rows = []
        for relative in bound_paths:
            digest = checker.sha256(
                (self.root / "stdo_representation" / relative).read_bytes()
            )
            bound_rows.append(f"{relative} {digest}")
        write_text(
            self.root / str(representation["release_note"]),
            "\n".join(
                (
                    *representation_markers,
                    *bound_rows,
                    *release_inventory_rows(representation["subject"]),
                    str(axiom["subject"]["member_set_sha256"]),
                    axiom_release_digest,
                    *(row["path"] for row in mechanics),
                    *(row["sha256"] for row in mechanics),
                    "",
                )
            ),
        )

        products = {
            "specification_methodology": spec_product,
            "axiom_indexer": axiom,
            "stdo_representation": representation,
        }
        required_refs = {"refs/heads/main"}
        for product in products.values():
            required_refs.update(
                str(product[field])
                for field in (
                    "release_ref",
                    "selector_ref",
                    "rc_branch",
                    "release_branch",
                )
            )
        repository_url = str(self.remote)
        expected_version_lines = {key: [] for key in sorted(products)}
        manifest = {
            "kind": "specification-stack.release-matched-cohort",
            "schema_version": 1,
            "cohort": {
                "version": self.version,
                "cut": self.cut,
                "publication_mode": "atomic",
                "status": "candidate",
                "carrier_ref": "refs/heads/main",
            },
            "products": products,
            "assets": {
                "spec_plugin": {
                    "version": self.version,
                    "root": "specification_methodology/plugins/spec",
                    "manifests": [
                        ".claude-plugin/plugin.json",
                        ".codex-plugin/plugin.json",
                    ],
                },
                "stdo_semantic_index": {
                    "version": self.version,
                    "root": semantic_root,
                    "source_corpus": "source-corpus.json",
                    "program": "axiomatic-program.json",
                    "map": "logical-constraint-map.json",
                    "validation_report": "validation-report.json",
                    "release_member_paths": release_member_paths,
                },
            },
            "publication": {
                "repository_url": repository_url,
                "expected_remote": {ref: None for ref in sorted(required_refs)},
                "expected_version_lines": expected_version_lines,
                "expected_version_lines_sha256": checker.canonical_value_sha256(
                    {
                        "repository_url": repository_url,
                        "version_lines": expected_version_lines,
                    }
                ),
            },
        }
        write_json(self.root / "stack_release.json", manifest)
        run(self.root, "git", "add", ".")
        run(self.root, "git", "commit", "-qm", "commit B")
        self.revision = run(self.root, "git", "rev-parse", "HEAD")

    def create_local_ref_graph(self) -> None:
        for namespace in ("axiom_indexer", "stdo_representation"):
            run(
                self.root,
                "git",
                "tag",
                "-a",
                f"{namespace}/{self.cut}",
                self.revision,
                "-m",
                f"{namespace} cut",
            )
        targets = {
            "specification_methodology": run(
                self.root,
                "git",
                "rev-parse",
                f"refs/tags/specification_methodology/{self.cut}^{{}}",
            ),
            "axiom_indexer": self.revision,
            "stdo_representation": self.revision,
        }
        for namespace, target in targets.items():
            run(
                self.root,
                "git",
                "tag",
                "-a",
                "-f",
                f"{namespace}/v{self.semantic}",
                target,
                "-m",
                f"{namespace} selector",
            )
            for ref in (
                f"refs/heads/rc/{namespace}/{self.semantic}",
                f"refs/heads/release/{namespace}/{self.semantic}",
            ):
                run(self.root, "git", "update-ref", ref, target)

    def publish_atomic(self) -> None:
        manifest = json.loads((self.root / "stack_release.json").read_text())
        refs = [manifest["cohort"]["carrier_ref"]]
        for product in manifest["products"].values():
            refs.extend(
                product[field]
                for field in (
                    "release_ref",
                    "selector_ref",
                    "rc_branch",
                    "release_branch",
                )
            )
        run(self.root, "git", "push", "--atomic", "origin", *refs)


class StackReleaseCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CohortFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def check(self, phase: str = "content") -> list[str]:
        return checker.check(
            self.fixture.root,
            "stack_release.json",
            phase,
            None if phase == "content" else self.fixture.revision,
            "origin",
        )

    def test_content_gate_accepts_exact_complete_cohort(self) -> None:
        self.assertEqual(self.check(), [])

    def replace_representation_members(self, members: list[dict[str, str]]) -> None:
        manifest_path = self.fixture.root / "stack_release.json"
        manifest = json.loads(manifest_path.read_text())
        product = manifest["products"]["stdo_representation"]
        old_rows = "\n".join(release_inventory_rows(product["subject"]))
        product["subject"] = {
            "member_count": len(members),
            "member_set_sha256": checker.product_member_stream(members),
            "members": sorted(members, key=lambda row: row["path"]),
        }
        note_path = self.fixture.root / product["release_note"]
        note = note_path.read_text()
        self.assertIn(old_rows, note)
        note_path.write_text(note.replace(
            old_rows, "\n".join(release_inventory_rows(product["subject"]))
        ))
        write_json(manifest_path, manifest)

    def representation_members(self) -> list[dict[str, str]]:
        manifest = json.loads((self.fixture.root / "stack_release.json").read_text())
        return manifest["products"]["stdo_representation"]["subject"]["members"]

    def test_successor_complete_native_bundle_accepts_nine_members(self) -> None:
        relative = "skills/stdo-representation/references/frame-index-use.md"
        path = self.fixture.root / "stdo_representation" / relative
        write_text(path, "# Frame-index use\n")
        members = self.representation_members()
        members.append({"type": "file", "path": relative,
                        "sha256": checker.sha256(path.read_bytes())})
        self.replace_representation_members(members)
        self.assertEqual(self.check(), [])

    def test_native_file_omitted_from_recomputed_inventory_refuses(self) -> None:
        relative = "skills/stdo-representation/references/frame-index-use.md"
        write_text(self.fixture.root / "stdo_representation" / relative, "# Guide\n")
        self.assertIn(
            f"stdo_representation: Product inventory omits required member: {relative}",
            self.check(),
        )

    def test_missing_referenced_native_file_refuses_even_without_descriptor(self) -> None:
        relative = "skills/stdo-representation/SKILL.md"
        path = self.fixture.root / "stdo_representation" / relative
        write_text(path, "Read [frame use](references/frame-index-use.md).\n")
        members = self.representation_members()
        for member in members:
            if member["path"] == relative:
                member["sha256"] = checker.sha256(path.read_bytes())
        self.replace_representation_members(members)
        self.assertIn(
            "stdo_representation: Product inventory omits required member: "
            "skills/stdo-representation/references/frame-index-use.md",
            self.check(),
        )

    def test_nested_native_bundle_member_cannot_hide_behind_old_count(self) -> None:
        relative = "skills/stdo-representation/references/support/selection.md"
        write_text(self.fixture.root / "stdo_representation" / relative, "# Support\n")
        self.assertIn(
            f"stdo_representation: Product inventory omits required member: {relative}",
            self.check(),
        )

    def test_recomputed_inventory_cannot_add_excluded_source_document(self) -> None:
        relative = "specification/PRODUCT.md"
        path = self.fixture.root / "stdo_representation" / relative
        write_text(path, "# Product source\n")
        members = self.representation_members()
        members.append({"type": "file", "path": relative,
                        "sha256": checker.sha256(path.read_bytes())})
        self.replace_representation_members(members)
        self.assertIn(
            f"stdo_representation: Product inventory includes nonmember: {relative}",
            self.check(),
        )

    def test_recomputed_discovery_link_cannot_leave_canonical_native_bundle(self) -> None:
        relative = ".claude/skills/stdo-representation"
        path = self.fixture.root / "stdo_representation" / relative
        path.unlink()
        target = "../../other-skill"
        path.symlink_to(target)
        members = self.representation_members()
        for member in members:
            if member["path"] == relative:
                member["target"] = target
                member["sha256"] = checker.sha256(target.encode())
        self.replace_representation_members(members)
        self.assertIn(
            f"stdo_representation: Product discovery link leaves canonical skill: {relative}",
            self.check(),
        )

    def test_version_mismatch_fails_closed(self) -> None:
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["assets"]["spec_plugin"]["version"] = "1.2.3-rc.3"
        write_json(path, payload)
        self.assertTrue(any("version mismatch" in row for row in self.check()))

    def test_representation_axiom_dependency_version_mismatch_fails_closed(
        self,
    ) -> None:
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["products"]["stdo_representation"]["dependencies"]["axiom_indexer"][
            "version"
        ] = "1.2.3-rc.3"
        write_json(path, payload)
        self.assertIn(
            "Representation Axiom dependency version mismatch",
            self.check(),
        )

    def test_child_product_member_digest_drift_fails_closed(self) -> None:
        write_text(
            self.fixture.root / "axiom_indexer/build_tenants/core/code/ac.py",
            "changed mechanics\n",
        )
        self.assertTrue(
            any("Product member digest mismatch" in row for row in self.check())
        )

    def test_missing_child_product_member_fails_closed(self) -> None:
        (
            self.fixture.root
            / "stdo_representation/skills/stdo-representation/references/codex.md"
        ).unlink()
        self.assertTrue(
            any("Product member type mismatch" in row for row in self.check())
        )

    def test_content_gate_requires_exact_remote_expectation_set(self) -> None:
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["publication"]["expected_remote"].pop("refs/heads/main")
        write_json(path, payload)
        self.assertIn("remote expectation set is not exact", self.check())

    def test_content_gate_binds_version_line_digest(self) -> None:
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["publication"]["expected_version_lines_sha256"] = "0" * 64
        write_json(path, payload)
        self.assertIn(
            "publication.expected_version_lines_sha256 mismatch",
            self.check(),
        )

    def test_stale_source_member_digest_fails_closed(self) -> None:
        path = (
            self.fixture.root
            / "stdo_representation/build_tenants/axiom_indexer/representation"
            / f"stdo-{self.fixture.cut}/source-corpus.json"
        )
        payload = json.loads(path.read_text())
        payload["source_release"]["standards_members"][0]["sha256"] = "0" * 64
        write_json(path, payload)
        self.assertTrue(
            any("exact ordered STDO inventory" in row for row in self.check())
        )

    def test_stale_program_digest_fails_closed(self) -> None:
        path = (
            self.fixture.root
            / "stdo_representation/build_tenants/axiom_indexer/representation"
            / f"stdo-{self.fixture.cut}/axiomatic-program.json"
        )
        payload = json.loads(path.read_text())
        payload["tampered"] = True
        write_json(path, payload)
        self.assertTrue(any("canonical program digest" in row for row in self.check()))

    def test_missing_semantic_map_fails_closed(self) -> None:
        path = (
            self.fixture.root
            / "stdo_representation/build_tenants/axiom_indexer/representation"
            / f"stdo-{self.fixture.cut}/logical-constraint-map.json"
        )
        path.unlink()
        self.assertTrue(any("missing JSON asset" in row for row in self.check()))

    def test_local_ref_graph_binds_remote_absence(self) -> None:
        self.fixture.create_local_ref_graph()
        self.assertEqual(self.check("refs"), [])
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(self.fixture.root),
                "--phase",
                "refs",
                "--revision",
                self.fixture.revision,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["repository_url"], str(self.fixture.remote))
        self.assertRegex(receipt["remote_expectations_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(receipt["version_lines_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(receipt["qualified_push_sha256"], r"^[0-9a-f]{64}$")
        leases = [
            value
            for value in receipt["push_argv"]
            if value.startswith("--force-with-lease=")
        ]
        self.assertEqual(len(leases), 13)
        expected_refs = set(
            json.loads((self.fixture.root / "stack_release.json").read_text())[
                "publication"
            ]["expected_remote"]
        )
        refspecs = receipt["push_argv"][-13:]
        self.assertEqual(receipt["push_argv"][-14], str(self.fixture.remote))
        self.assertNotIn("origin", receipt["push_argv"])
        self.assertEqual({value.split(":", 1)[1] for value in refspecs}, expected_refs)
        self.assertTrue(
            all(checker.HEX40.fullmatch(value.split(":", 1)[0]) for value in refspecs)
        )
        run(
            self.fixture.root,
            "git",
            "push",
            "origin",
            f"refs/tags/axiom_indexer/{self.fixture.cut}",
        )
        self.assertTrue(any("remote drift" in row for row in self.check("refs")))

    def test_frozen_endpoint_blocks_alias_and_pushurl_retarget(self) -> None:
        self.fixture.create_local_ref_graph()
        qualified = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(self.fixture.root),
                "--phase",
                "refs",
                "--revision",
                self.fixture.revision,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        receipt = json.loads(qualified.stdout)
        self.assertEqual(receipt["push_argv"][-14], str(self.fixture.remote))

        wrong_fetch = self.fixture.root.parent / "wrong-fetch.git"
        wrong_push = self.fixture.root.parent / "wrong-push.git"
        for path in (wrong_fetch, wrong_push):
            run(self.fixture.root, "git", "init", "--bare", "-q", str(path))
        run(
            self.fixture.root,
            "git",
            "remote",
            "set-url",
            "origin",
            str(wrong_fetch),
        )
        run(
            self.fixture.root,
            "git",
            "remote",
            "set-url",
            "--push",
            "origin",
            str(wrong_push),
        )

        ref_failures = self.check("refs")
        self.assertTrue(any("configured fetch endpoint" in row for row in ref_failures))
        self.assertTrue(any("configured push endpoint" in row for row in ref_failures))
        blocked = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(self.fixture.root),
                "--phase",
                "refs",
                "--revision",
                self.fixture.revision,
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(blocked.returncode, 1)
        self.assertNotIn("push_argv", json.loads(blocked.stdout))

        subprocess.run(
            receipt["push_argv"],
            cwd=self.fixture.root,
            check=True,
            capture_output=True,
            text=True,
        )
        published_failures = self.check("published")
        self.assertTrue(
            any("configured fetch endpoint" in row for row in published_failures)
        )
        self.assertTrue(
            any("configured push endpoint" in row for row in published_failures)
        )
        self.assertFalse(
            any("remote cohort missing" in row for row in published_failures)
        )
        self.assertEqual(
            run(self.fixture.root, "git", "ls-remote", "--refs", str(wrong_fetch)),
            "",
        )
        self.assertEqual(
            run(self.fixture.root, "git", "ls-remote", "--refs", str(wrong_push)),
            "",
        )

    def test_refs_and_published_refuse_undeclared_higher_rc(self) -> None:
        self.fixture.create_local_ref_graph()
        run(
            self.fixture.root,
            "git",
            "tag",
            "-a",
            "undeclared-higher-rc",
            self.fixture.revision,
            "-m",
            "undeclared higher RC",
        )
        higher_refs = (
            f"refs/tags/axiom_indexer/v{self.fixture.semantic}-rc.5",
            f"refs/tags/v{self.fixture.semantic}-rc.5",
        )
        for higher_ref in higher_refs:
            run(
                self.fixture.root,
                "git",
                "push",
                str(self.fixture.remote),
                f"refs/tags/undeclared-higher-rc:{higher_ref}",
            )

        ref_failures = self.check("refs")
        self.assertTrue(
            any(
                "higher remote RC ordinal already exists" in row for row in ref_failures
            )
        )
        self.assertTrue(any("target RC is not greater" in row for row in ref_failures))
        self.assertTrue(
            any(
                row.startswith("specification_methodology: higher remote RC")
                for row in ref_failures
            )
        )

        self.fixture.publish_atomic()
        published_failures = self.check("published")
        self.assertTrue(
            any(
                "higher remote RC ordinal already exists" in row
                for row in published_failures
            )
        )
        self.assertTrue(
            any(
                "published target is not the greatest" in row
                for row in published_failures
            )
        )

    def test_refs_require_selector_at_greatest_existing_lower_rc(self) -> None:
        commit_a = run(
            self.fixture.root,
            "git",
            "rev-parse",
            f"refs/tags/specification_methodology/{self.fixture.cut}^{{}}",
        )
        lower_refs = (
            ("lower-rc2", 2, commit_a),
            ("lower-rc3", 3, self.fixture.revision),
        )
        for local_name, ordinal, target in lower_refs:
            run(
                self.fixture.root,
                "git",
                "tag",
                "-a",
                local_name,
                target,
                "-m",
                local_name,
            )
            run(
                self.fixture.root,
                "git",
                "push",
                str(self.fixture.remote),
                f"refs/tags/{local_name}:refs/tags/axiom_indexer/"
                f"v{self.fixture.semantic}-rc.{ordinal}",
            )
        run(
            self.fixture.root,
            "git",
            "tag",
            "-a",
            "stale-selector",
            commit_a,
            "-m",
            "stale selector",
        )
        selector_ref = f"refs/tags/axiom_indexer/v{self.fixture.semantic}"
        run(
            self.fixture.root,
            "git",
            "push",
            str(self.fixture.remote),
            f"refs/tags/stale-selector:{selector_ref}",
        )

        rows = checker.remote_version_line(
            self.fixture.root,
            str(self.fixture.remote),
            "axiom_indexer",
            self.fixture.semantic,
            include_unqualified=False,
        )
        selector_object, _ = checker.remote_ref(
            self.fixture.root, str(self.fixture.remote), selector_ref
        )
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["publication"]["expected_remote"][selector_ref] = selector_object
        payload["publication"]["expected_version_lines"]["axiom_indexer"] = rows
        payload["publication"][
            "expected_version_lines_sha256"
        ] = checker.canonical_value_sha256(
            {
                "repository_url": payload["publication"]["repository_url"],
                "version_lines": payload["publication"]["expected_version_lines"],
            }
        )
        write_json(path, payload)
        run(self.fixture.root, "git", "add", "stack_release.json")
        run(self.fixture.root, "git", "commit", "-qm", "bind lower version line")
        self.fixture.revision = run(self.fixture.root, "git", "rev-parse", "HEAD")
        self.fixture.create_local_ref_graph()

        self.assertIn(
            "axiom_indexer: current selector does not resolve to the greatest lower RC",
            self.check("refs"),
        )

    def test_local_ref_graph_binds_existing_mutable_ref_lease(self) -> None:
        commit_a = run(
            self.fixture.root,
            "git",
            "rev-parse",
            f"refs/tags/specification_methodology/{self.fixture.cut}^{{}}",
        )
        run(
            self.fixture.root,
            "git",
            "push",
            "origin",
            f"{commit_a}:refs/heads/main",
        )
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["publication"]["expected_remote"]["refs/heads/main"] = commit_a
        write_json(path, payload)
        run(self.fixture.root, "git", "add", "stack_release.json")
        run(self.fixture.root, "git", "commit", "-qm", "bind mutable remote")
        self.fixture.revision = run(self.fixture.root, "git", "rev-parse", "HEAD")
        self.fixture.create_local_ref_graph()
        self.assertEqual(self.check("refs"), [])
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(self.fixture.root),
                "--phase",
                "refs",
                "--revision",
                self.fixture.revision,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        receipt = json.loads(result.stdout)
        self.assertIn(
            f"--force-with-lease=refs/heads/main:{commit_a}",
            receipt["push_argv"],
        )

    def test_frozen_commit_refuses_construction_status(self) -> None:
        path = self.fixture.root / "stack_release.json"
        payload = json.loads(path.read_text())
        payload["cohort"]["status"] = "child_construction"
        write_json(path, payload)
        run(self.fixture.root, "git", "add", "stack_release.json")
        run(self.fixture.root, "git", "commit", "-qm", "bad status")
        revision = run(self.fixture.root, "git", "rev-parse", "HEAD")
        failures = checker.check(
            self.fixture.root,
            "stack_release.json",
            "content",
            revision,
            "origin",
        )
        self.assertIn(
            "a frozen commit-B cohort must have status candidate",
            failures,
        )

    def test_published_gate_accepts_complete_atomic_remote_and_refuses_partial(
        self,
    ) -> None:
        self.fixture.create_local_ref_graph()
        run(
            self.fixture.root,
            "git",
            "push",
            "origin",
            f"refs/tags/axiom_indexer/{self.fixture.cut}",
        )
        partial = self.check("published")
        self.assertTrue(any("remote cohort missing" in row for row in partial))

        run(
            self.fixture.root,
            "git",
            "push",
            "origin",
            f":refs/tags/axiom_indexer/{self.fixture.cut}",
        )
        self.assertEqual(self.check("refs"), [])
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--root",
                str(self.fixture.root),
                "--phase",
                "refs",
                "--revision",
                self.fixture.revision,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        receipt = json.loads(result.stdout)
        subprocess.run(
            receipt["push_argv"],
            cwd=self.fixture.root,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(self.check("published"), [])

        run(
            self.fixture.root,
            "git",
            "tag",
            "-a",
            "same-peel-different-object",
            self.fixture.revision,
            "-m",
            "different selector annotation",
        )
        alternate = run(
            self.fixture.root,
            "git",
            "rev-parse",
            "refs/tags/same-peel-different-object",
        )
        selector = f"refs/tags/axiom_indexer/v{self.fixture.semantic}"
        run(
            self.fixture.root,
            "git",
            "push",
            "--force",
            "origin",
            f"{alternate}:{selector}",
        )
        self.assertTrue(
            any("selector tag object differs" in row for row in self.check("published"))
        )


if __name__ == "__main__":
    unittest.main()
