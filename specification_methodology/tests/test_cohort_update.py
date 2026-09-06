from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from stdo_toolchain.cohort_update import cohort_update, _axiom_digest, _materialize
from stdo_toolchain.errors import StdoError
from stdo_toolchain.git_source import GitSnapshot
from stdo_toolchain.manifest import build_manifest, manifest_sha256
from stdo_toolchain.product_definition import definition_status
from stdo_toolchain.store import Store
from stdo_toolchain.util import sha256_bytes
from test_toolchain import ReleaseFixture, definition_document, run_git


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


class CohortFixture:
    """Two exact published companions and an independently existing consumer."""

    def __init__(self, root: Path):
        self.root = root
        fixture = ReleaseFixture(root, project_prefix="specification_methodology")
        self.repository = fixture.repository
        self.store = Store(root / "stdo-store")
        old = self.store.install(str(self.repository), "v1.0.0-rc.1")
        for name in (".claude-plugin", ".codex-plugin"):
            path = fixture.project_root / "plugins/spec" / name / "plugin.json"
            payload = json.loads(path.read_text())
            payload["version"] = "1.0.0-rc.2"
            write_json(path, payload)
        fixture.add_rc2()
        run_git(self.repository, "tag", "-a", "specification_methodology/v1.0.0-rc.2", "-m", "qualified STDO")
        run_git(self.repository, "tag", "-d", "v1.0.0-rc.2")
        with GitSnapshot(str(self.repository), "v1.0.0-rc.2") as source:
            installed_manifest = build_manifest(source)
            self.digest = manifest_sha256(installed_manifest)
            stdo = {"namespace": "specification_methodology", "subtree": "specification_methodology",
                    "version": "1.0.0-rc.2", "release_ref": source.ref,
                    "freeze": {"tag_object": source.tag_object, "commit": source.commit, "tree": source.tree,
                               "project_subtree_tree": installed_manifest["release"]["project_subtree_tree"],
                               "standards_tree": installed_manifest["release"]["standards_tree"],
                               "standards_member_count": installed_manifest["standards"]["member_count"],
                               "standards_member_set_sha256": installed_manifest["standards"]["member_set_sha256"],
                               "installed_manifest_sha256": self.digest}}
        self.consumer = root / "consumer"
        self.consumer.mkdir()
        self.definition = self.consumer / "stdo.json"
        self.document = definition_document(self.repository, old.uri, old.manifest_sha256)
        self.document["composition"] = []
        self.document["unrelated"] = {"keep": "local work"}
        self.names = ["axiom_indexer", "stdo_representation"]
        products = {"specification_methodology": stdo}
        for name in self.names:
            definition = {"product": {"definition_id": "urn:test:" + name},
                          "constitution": {"stdo": {"basis": {"uri": Store.release_uri("v1.0.0-rc.2"),
                                                               "manifest_sha256": self.digest}}}}
            base = self.repository / name
            write_json(base / "stdo.json", definition)
            (base / "skills" / name).mkdir(parents=True)
            (base / "skills" / name / "SKILL.md").write_text("# Exact native route\n")
            (base / "releases").mkdir()
            (base / "releases" / "v1.0.0.md").write_text("# Immutable companion release\n")
            members = [{"type": "file", "path": p.relative_to(base).as_posix(),
                        "sha256": sha256_bytes(p.read_bytes())} for p in sorted(base.rglob("*")) if p.is_file()]
            digest = sha256_bytes("".join(f"{m['sha256']}  file  {m['path']}\n" for m in members).encode())
            products[name] = {"namespace": name, "subtree": name, "version": "1.0.0-rc.2",
                              "release_ref": f"refs/tags/{name}/v1.0.0-rc.2",
                              "release_note": f"{name}/releases/v1.0.0.md",
                              "subject": {"members": members, "member_count": len(members), "member_set_sha256": digest}}
            self.document["composition"].append({"target_definition_id": "urn:test:" + name,
                                                  "relation": "urn:test:substrate",
                                                  "product_definition": "https://example.invalid/old/" + name,
                                                  "contracts": ["https://example.invalid/old-contract"]})
            old_install = root / "historical" / name
            (old_install / "skills" / name).mkdir(parents=True)
            (old_install / "skills" / name / "SKILL.md").write_text("# Prior usable skill\n")
            for relative, target in [(f".products/{name}", old_install),
                                     (f".agents/skills/{name}", old_install / "skills" / name)]:
                path = self.consumer / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.symlink_to(target)
        asset_root = "stdo_representation/representation/stdo-v1.0.0-rc.2"
        source_uri = Store.release_uri("v1.0.0-rc.2")
        program = {"uri": "urn:test:stdo-v1.0.0-rc.2", "source_basis": source_uri + "standards/",
                   "source_ref": source_uri + "standards/SPEC_METHOD.md"}
        spec_digest = next(m["sha256"] for m in installed_manifest["standards"]["members"] if m["path"] == "SPEC_METHOD.md")
        resolved = [{"uri": program["source_ref"], "sha256": "sha256:" + spec_digest}]
        mapping = {"source_basis": program["source_basis"], "program_uri": program["uri"],
                   "program_sha256": _axiom_digest(program), "resolved_sources": resolved}
        mapping["map_sha256"] = _axiom_digest(mapping)
        report = {"program_uri": program["uri"], "program_sha256": _axiom_digest(program),
                  "status": "valid", "diagnostics": [], "resolved_sources": resolved}
        corpus = {"kind": "stdo-representation.source-corpus", "representation_version": "1.0.0-rc.2",
                  "source_release": {**stdo["freeze"], "cut": "v1.0.0-rc.2", "uri": source_uri,
                                     "qualified_ref": stdo["release_ref"], "project_subtree_root": "specification_methodology",
                                     "standards_members": installed_manifest["standards"]["members"]}}
        for name, payload in [("source-corpus.json", corpus), ("axiomatic-program.json", program),
                              ("logical-constraint-map.json", mapping), ("validation-report.json", report)]:
            path = self.repository / asset_root / name
            write_json(path, payload)
            with (self.repository / "stdo_representation/releases/v1.0.0.md").open("a") as note:
                note.write(path.relative_to(self.repository / "stdo_representation").as_posix() + " " + sha256_bytes(path.read_bytes()) + "\n")
        # Exact Product inventories include the now-constructed release assets.
        for name in self.names:
            base = self.repository / name
            members = [{"type": "file", "path": p.relative_to(base).as_posix(), "sha256": sha256_bytes(p.read_bytes())}
                       for p in sorted(base.rglob("*")) if p.is_file()]
            products[name]["subject"] = {"members": members, "member_count": len(members),
                "member_set_sha256": sha256_bytes("".join(f"{m['sha256']}  file  {m['path']}\n" for m in members).encode())}
        products["stdo_representation"]["dependencies"] = {"axiom_indexer": {
            "version": "1.0.0-rc.2", "product_member_set_sha256": products["axiom_indexer"]["subject"]["member_set_sha256"]}}
        self.cohort = {"kind": "specification-stack.release-matched-cohort", "schema_version": 1,
                       "cohort": {"cut": "v1.0.0-rc.2", "version": "1.0.0-rc.2"}, "products": products,
                       "publication": {"repository_url": "https://github.com/example/stack"},
                       "assets": {"spec_plugin": {"version": "1.0.0-rc.2", "root": "specification_methodology/plugins/spec",
                                                   "manifests": [".claude-plugin/plugin.json", ".codex-plugin/plugin.json"]},
                                  "stdo_semantic_index": {"version": "1.0.0-rc.2", "root": asset_root,
                                      "source_corpus": "source-corpus.json", "program": "axiomatic-program.json",
                                      "map": "logical-constraint-map.json", "validation_report": "validation-report.json",
                                      "release_member_paths": [asset_root.removeprefix("stdo_representation/") + "/" + name
                                                               for name in ["axiomatic-program.json", "logical-constraint-map.json"]]}}}
        write_json(self.repository / "stack_release.json", self.cohort)
        run_git(self.repository, "add", ".")
        run_git(self.repository, "commit", "-qm", "exact companions")
        self.commit = run_git(self.repository, "rev-parse", "HEAD")
        for name in self.names:
            run_git(self.repository, "tag", "-a", name + "/v1.0.0-rc.2", "-m", name)
        self.selection = {"kind": "stdo.cohort-update-selection", "schema_version": 1,
                          "definition_id": self.document["product"]["definition_id"],
                          "cohort": {"repository": str(self.repository),
                                     "ref": "refs/tags/stdo_representation/v1.0.0-rc.2",
                                     "tag_object": run_git(self.repository, "rev-parse", "stdo_representation/v1.0.0-rc.2"),
                                     "path": "stack_release.json"},
                          "companions": [], "derived_context": []}
        for name in self.names:
            self.selection["companions"].append({
                "product": name, "definition_member": "stdo.json", "target_definition_id": "urn:test:" + name,
                "install_root": str(root / "companions" / name / "v1.0.0-rc.2"),
                "product_definition": f"https://raw.githubusercontent.com/example/stack/{self.commit}/{name}/stdo.json",
                "contracts": [f"https://raw.githubusercontent.com/example/stack/{self.commit}/{name}/releases/v1.0.0.md"],
                "links": [{"path": f".products/{name}", "member": "."},
                          {"path": f".agents/skills/{name}", "member": f"skills/{name}"}]})
        self.selection_path = root / "selection.json"
        self.save()

    def save(self):
        write_json(self.definition, self.document)
        write_json(self.selection_path, self.selection)

    def plan(self):
        return cohort_update(self.definition, self.store, self.selection_path, dry_run=True)

    def apply(self, plan):
        return cohort_update(self.definition, self.store, self.selection_path, accepted_plan_sha256=plan["plan_sha256"])

    def add_context(self):
        source = self.consumer / "PRODUCT.md"
        source.write_text("# Accepted source\n\n## Other section\n")
        program = {"kind": "axiom-indexer.axiomatic-program", "schema_version": 1,
                   "uri": "urn:test:program", "calculus_ref": "repo://consumer/PRODUCT.md",
                   "source_basis": "repo://consumer/", "frame_refs": [], "vocabulary_refs": [],
                   "symbols": [], "clauses": [], "residuals": []}
        write_json(self.consumer / "program.json", program)
        mapping = {"kind": "axiom-indexer.logical-constraint-map", "schema_version": 1,
                   "program_sha256": _axiom_digest(program),
                   "resolved_sources": [{"uri": "repo://consumer/PRODUCT.md", "sha256": "sha256:" + sha256_bytes(source.read_bytes())}]}
        mapping["map_sha256"] = _axiom_digest(mapping)
        write_json(self.consumer / "map.json", mapping)
        write_json(self.consumer / "bindings.json", {"kind": "axiom-indexer.binding-set", "schema_version": 1,
                                                    "bindings": [{"uri_prefix": "repo://consumer/", "path": str(self.consumer)}]})
        self.selection["derived_context"] = [{"program": "program.json", "map": "map.json", "bindings": "bindings.json"}]
        self.save()

    def consumer_state(self):
        return {p.relative_to(self.consumer).as_posix(): ("link", os.readlink(p)) if p.is_symlink() else ("file", p.read_bytes())
                for p in self.consumer.rglob("*") if p.is_symlink() or p.is_file()}

    def republish_fixture(self):
        for name in self.names:
            base = self.repository / name
            members = [{"type": "file", "path": p.relative_to(base).as_posix(), "sha256": sha256_bytes(p.read_bytes())}
                       for p in sorted(base.rglob("*")) if p.is_file()]
            self.cohort["products"][name]["subject"] = {"members": members, "member_count": len(members),
                "member_set_sha256": sha256_bytes("".join(f"{m['sha256']}  file  {m['path']}\n" for m in members).encode())}
        write_json(self.repository / "stack_release.json", self.cohort)
        run_git(self.repository, "add", "-A")
        run_git(self.repository, "commit", "-qm", "new explicit test selection")
        commit = run_git(self.repository, "rev-parse", "HEAD")
        for name in self.names:
            run_git(self.repository, "tag", "-fa", name + "/v1.0.0-rc.2", "-m", "new explicit test selection")
        self.selection["cohort"]["tag_object"] = run_git(self.repository, "rev-parse", "stdo_representation/v1.0.0-rc.2")
        for row in self.selection["companions"]:
            row["product_definition"] = row["product_definition"].replace(self.commit, commit)
            row["contracts"] = [value.replace(self.commit, commit) for value in row["contracts"]]
        self.commit = commit
        self.save()


class CohortUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.fixture = CohortFixture(Path(self.temporary.name).resolve())

    def test_basis_status_is_not_complete_cohort_readiness(self):
        f = self.fixture
        self.assertTrue(definition_status(f.definition, f.store, verify=True)["valid"])
        before = f.consumer_state()
        plan = f.plan()
        self.assertEqual(plan["status"], "planned")
        self.assertFalse(plan["complete"])
        self.assertEqual(len(plan["companions"]), 2)
        self.assertEqual(len(plan["bindings"]), 4)
        self.assertEqual(before, f.consumer_state())
        self.assertFalse((f.root / "companions").exists())

    def test_exact_accepted_plan_updates_complete_selected_relation(self):
        f = self.fixture
        f.add_context()
        before = (f.consumer / "map.json").read_bytes()
        result = f.apply(f.plan())
        self.assertTrue(result["complete"])
        updated = json.loads(f.definition.read_text())
        self.assertEqual(updated["unrelated"], f.document["unrelated"])
        self.assertEqual(updated["constitution"]["stdo"]["basis"]["manifest_sha256"], f.digest)
        for row in f.selection["companions"]:
            self.assertEqual((Path(row["install_root"]) / "stdo.json").read_bytes(), (f.repository / row["product"] / "stdo.json").read_bytes())
            self.assertTrue((f.consumer / row["links"][1]["path"] / "SKILL.md").read_text().startswith("# Exact"))
            self.assertTrue((f.root / "historical" / row["product"] / "skills" / row["product"] / "SKILL.md").exists())
        self.assertEqual(before, (f.consumer / "map.json").read_bytes())
        self.assertTrue(definition_status(f.definition, f.store, verify=True)["valid"])

    def test_acceptance_is_required_and_cannot_survive_definition_drift(self):
        f = self.fixture
        before = f.consumer_state()
        with self.assertRaisesRegex(StdoError, "accepted plan"):
            cohort_update(f.definition, f.store, f.selection_path)
        plan = f.plan()
        f.document["unrelated"]["keep"] = "new local work"
        f.save()
        changed = f.consumer_state()
        with self.assertRaisesRegex(StdoError, "accepted plan"):
            f.apply(plan)
        self.assertEqual(changed, f.consumer_state())
        self.assertNotEqual(before, changed)
        self.assertFalse((f.root / "companions").exists())

    def test_changed_selection_or_tag_refuses(self):
        f = self.fixture
        plan = f.plan()
        f.selection["companions"][0]["links"][0]["path"] = ".products/other"
        f.save()
        with self.assertRaisesRegex(StdoError, "accepted plan"):
            f.apply(plan)
        run_git(f.repository, "tag", "-fa", "stdo_representation/v1.0.0-rc.2", "-m", "replacement annotation")
        with self.assertRaisesRegex(StdoError, "tag object changed"):
            f.plan()

    def test_stale_source_holds_before_install_or_consumer_effects(self):
        f = self.fixture
        f.add_context()
        (f.consumer / "PRODUCT.md").write_text("# Changed accepted source\n")
        before = f.consumer_state()
        plan = f.plan()
        self.assertFalse(plan["ready"])
        self.assertIn("Stale derived source digest", plan["holds"][0])
        with self.assertRaisesRegex(StdoError, "held before effects"):
            f.apply(plan)
        self.assertEqual(before, f.consumer_state())
        self.assertFalse((f.root / "companions").exists())
        self.assertFalse((f.store.root / "releases" / "v1.0.0-rc.2").exists())

    def test_missing_map_changed_program_and_broken_map_digest_hold(self):
        f = self.fixture
        for change in ("missing", "program", "map"):
            with self.subTest(change=change):
                f.add_context()
                if change == "missing":
                    (f.consumer / "map.json").unlink()
                elif change == "program":
                    write_json(f.consumer / "program.json", {"uri": "urn:test:changed"})
                else:
                    mapping = json.loads((f.consumer / "map.json").read_text())
                    mapping["resolved_sources"] = []
                    write_json(f.consumer / "map.json", mapping)
                self.assertFalse(f.plan()["ready"])

    def test_source_drift_during_staging_preserves_bindings(self):
        f = self.fixture
        f.add_context()
        plan = f.plan()
        prior_definition = f.definition.read_bytes()
        prior_links = {r["path"]: os.readlink(r["path"]) for r in plan["bindings"]}
        def stage(root, entries):
            _materialize(root, entries)
            (f.consumer / "PRODUCT.md").write_text("# Concurrent author change\n")
        with patch("stdo_toolchain.cohort_update._materialize", side_effect=stage):
            with self.assertRaisesRegex(StdoError, "Derived context changed"):
                f.apply(plan)
        self.assertEqual(prior_definition, f.definition.read_bytes())
        self.assertEqual(prior_links, {p: os.readlink(p) for p in prior_links})

    def test_partial_link_failure_rolls_back_prior_usable_consumer(self):
        f = self.fixture
        plan = f.plan()
        before = f.consumer_state()
        replace = os.replace
        failed_path = str(f.consumer / ".agents/skills/axiom_indexer")
        def fail_second(source, target):
            if str(target) == failed_path:
                raise OSError("injected second-link failure")
            return replace(source, target)
        with patch("stdo_toolchain.cohort_update.os.replace", side_effect=fail_second):
            with self.assertRaisesRegex(StdoError, "injected second-link failure"):
                f.apply(plan)
        self.assertEqual(before, f.consumer_state())

    def test_existing_companion_damage_and_extra_directory_refuse(self):
        f = self.fixture
        f.apply(f.plan())
        root = Path(f.selection["companions"][0]["install_root"])
        (root / "extra").mkdir()
        with self.assertRaisesRegex(StdoError, "Unmanifested companion directory"):
            f.plan()
        (root / "extra").rmdir()
        (root / "stdo.json").chmod(0o644)
        (root / "stdo.json").write_text("{}")
        with self.assertRaisesRegex(StdoError, "Companion entry changed"):
            f.plan()

    def test_omitted_companion_and_unrelated_locator_host_refuse(self):
        f = self.fixture
        original = copy.deepcopy(f.selection)
        f.selection["companions"].pop()
        f.save()
        with self.assertRaisesRegex(StdoError, "population"):
            f.plan()
        f.selection = original
        f.selection["companions"][0]["product_definition"] = f.selection["companions"][0]["product_definition"].replace("raw.githubusercontent.com", "attacker.invalid")
        f.save()
        with self.assertRaisesRegex(StdoError, "immutable member"):
            f.plan()

    def test_regular_file_and_redirected_ancestor_refuse(self):
        f = self.fixture
        path = f.consumer / ".products/axiom_indexer"
        path.unlink()
        path.write_text("unrelated file")
        with self.assertRaisesRegex(StdoError, "non-link"):
            f.plan()
        path.unlink()
        f.selection["companions"][0]["links"][0]["path"] = "redirect/alias"
        (f.consumer / "redirect").symlink_to(f.root / "historical", target_is_directory=True)
        f.save()
        with self.assertRaisesRegex(StdoError, "Redirected"):
            f.plan()

    def test_install_presence_is_not_an_acceptance_change(self):
        f = self.fixture
        plan = f.plan()
        # Failure after immutable staging leaves the original consumer unchanged.
        with patch("stdo_toolchain.cohort_update.atomic_write", side_effect=OSError("definition write failed")):
            with self.assertRaisesRegex(StdoError, "definition write failed"):
                f.apply(plan)
        self.assertEqual(plan["plan_sha256"], f.plan()["plan_sha256"])
        self.assertTrue(f.apply(plan)["complete"])

    def test_real_cli_plans_applies_and_reports_held_context(self):
        f = self.fixture
        command = [sys.executable, "-m", "stdo_toolchain.cli", "--store", str(f.store.root),
                   "cohort-update", "--definition", str(f.definition), "--selection", str(f.selection_path)]
        plan = subprocess.run([*command, "--dry-run"], capture_output=True, text=True, check=True)
        value = json.loads(plan.stdout)
        applied = subprocess.run([*command, "--accept-plan-sha256", value["plan_sha256"]], capture_output=True, text=True, check=True)
        self.assertTrue(json.loads(applied.stdout)["complete"])
        f.document = json.loads(f.definition.read_text())
        f.add_context()
        (f.consumer / "PRODUCT.md").write_text("# Drift\n")
        held = subprocess.run([*command, "--dry-run"], capture_output=True, text=True)
        self.assertEqual(held.returncode, 1, held.stderr)
        self.assertEqual(json.loads(held.stdout)["status"], "held")
        refused = subprocess.run([*command, "--accept-plan-sha256", json.loads(held.stdout)["plan_sha256"]], capture_output=True, text=True)
        self.assertEqual(refused.returncode, 2)
        self.assertIn("held before effects", json.loads(refused.stdout)["error"])

    def test_changed_store_destination_requires_new_acceptance(self):
        f = self.fixture
        plan = f.plan()
        other = Store(f.root / "other-store")
        other.install(str(f.repository), "v1.0.0-rc.1")
        with self.assertRaisesRegex(StdoError, "accepted plan"):
            cohort_update(f.definition, other, f.selection_path, accepted_plan_sha256=plan["plan_sha256"])

    def test_upstream_inventory_mismatch_refuses_before_effects(self):
        f = self.fixture
        f.cohort["products"]["axiom_indexer"]["subject"]["members"][0]["sha256"] = "0" * 64
        write_json(f.repository / "stack_release.json", f.cohort)
        run_git(f.repository, "add", ".")
        run_git(f.repository, "commit", "-qm", "broken exact inventory")
        f.commit = run_git(f.repository, "rev-parse", "HEAD")
        for name in f.names:
            run_git(f.repository, "tag", "-fa", name + "/v1.0.0-rc.2", "-m", "new exact selection")
        f.selection["cohort"]["tag_object"] = run_git(f.repository, "rev-parse", "stdo_representation/v1.0.0-rc.2")
        f.save()
        before = f.consumer_state()
        with self.assertRaisesRegex(StdoError, "Changed Product member"):
            f.plan()
        self.assertEqual(before, f.consumer_state())
        self.assertFalse((f.root / "companions").exists())

    def test_missing_cohort_assets_refuses(self):
        f = self.fixture
        f.cohort.pop("assets")
        f.republish_fixture()
        with self.assertRaisesRegex(StdoError, "assets"):
            f.plan()
        self.assertFalse((f.root / "companions").exists())

    def test_stale_released_source_corpus_refuses(self):
        f = self.fixture
        asset = f.cohort["assets"]["stdo_semantic_index"]
        path = f.repository / asset["root"] / asset["source_corpus"]
        source = json.loads(path.read_text())
        source["source_release"]["installed_manifest_sha256"] = "0" * 64
        write_json(path, source)
        f.republish_fixture()
        before = f.consumer_state()
        with self.assertRaisesRegex(StdoError, "semantic source-corpus installed_manifest_sha256 mismatch"):
            f.plan()
        self.assertEqual(before, f.consumer_state())
        self.assertFalse((f.root / "companions").exists())

    def test_missing_released_source_corpus_refuses(self):
        f = self.fixture
        asset = f.cohort["assets"]["stdo_semantic_index"]
        (f.repository / asset["root"] / asset["source_corpus"]).unlink()
        f.republish_fixture()
        with self.assertRaises(StdoError):
            f.plan()
        self.assertFalse((f.root / "companions").exists())

    def test_removed_stale_source_observation_cannot_be_rehashed_as_ready(self):
        f = self.fixture
        f.add_context()
        source = f.consumer / "SECOND.md"
        source.write_text("# Another accepted source\n")
        program = json.loads((f.consumer / "program.json").read_text())
        program["frame_refs"].append("repo://consumer/SECOND.md")
        write_json(f.consumer / "program.json", program)
        mapping = json.loads((f.consumer / "map.json").read_text())
        mapping["program_sha256"] = _axiom_digest(program)
        mapping["source_routes"] = {"urn:test:source": ["repo://consumer/SECOND.md"]}
        mapping["resolved_sources"].append({"uri": "repo://consumer/SECOND.md", "sha256": "sha256:" + sha256_bytes(source.read_bytes())})
        mapping["map_sha256"] = _axiom_digest({k: v for k, v in mapping.items() if k != "map_sha256"})
        write_json(f.consumer / "map.json", mapping)
        self.assertTrue(f.plan()["ready"])
        source.write_text("# Changed source\n")
        mapping["resolved_sources"] = [r for r in mapping["resolved_sources"] if r["uri"] != "repo://consumer/SECOND.md"]
        mapping["map_sha256"] = _axiom_digest({k: v for k, v in mapping.items() if k != "map_sha256"})
        write_json(f.consumer / "map.json", mapping)
        plan = f.plan()
        self.assertFalse(plan["ready"])
        self.assertIn("Missing declared derived source coverage", plan["holds"][0])
        with self.assertRaisesRegex(StdoError, "held before effects"):
            f.apply(plan)

    def test_absolute_upstream_symlink_refuses_even_under_virtual_prefix(self):
        f = self.fixture
        (f.repository / "axiom_indexer/absolute").symlink_to("/product/outside")
        f.republish_fixture()
        with self.assertRaisesRegex(StdoError, "Absolute upstream Product symlink"):
            f.plan()
        self.assertFalse((f.root / "companions").exists())

    def test_frame_index_sources_cannot_disappear_from_rehashed_evidence(self):
        f = self.fixture
        f.add_context()
        source = f.consumer / "FRAME_INDEX.md"
        source.write_text("# Selected membership\n")
        source_uri = "repo://consumer/FRAME_INDEX.md#selected-membership"
        program = json.loads((f.consumer / "program.json").read_text())
        frame = "repo://consumer/PRODUCT.md#accepted-source"
        program["frame_refs"] = [frame]
        program["residuals"] = [{"uri": "urn:test:residual", "kind": "unresolved",
                                 "subject_refs": [], "detail": "Frame applicability is judged",
                                 "source_refs": [frame], "re_entry_refs": [frame]}]
        program["frame_indexes"] = [{"uri": "urn:test:frame-index", "frame_ref": frame,
                                     "scope": "Selected residual evaluation", "clause_refs": [],
                                     "residual_refs": ["urn:test:residual"], "source_refs": [source_uri]}]
        write_json(f.consumer / "program.json", program)
        mapping = json.loads((f.consumer / "map.json").read_text())
        mapping["program_sha256"] = _axiom_digest(program)
        mapping["source_routes"] = {"urn:test:frame-index": [source_uri]}
        mapping["resolved_sources"].append({"uri": source_uri, "sha256": "sha256:" + sha256_bytes(source.read_bytes())})

        def save_map():
            mapping["map_sha256"] = _axiom_digest({k: v for k, v in mapping.items() if k != "map_sha256"})
            write_json(f.consumer / "map.json", mapping)

        save_map()
        self.assertTrue(f.plan()["ready"])
        source.write_text("# Changed membership\n")
        self.assertIn("Stale derived source digest", f.plan()["holds"][0])
        mapping["source_routes"] = {}
        mapping["resolved_sources"] = [r for r in mapping["resolved_sources"] if r["uri"] != source_uri]
        save_map()
        before = f.consumer_state()
        plan = f.plan()
        self.assertFalse(plan["ready"])
        self.assertIn("Missing declared derived source coverage", plan["holds"][0])
        with self.assertRaisesRegex(StdoError, "held before effects"):
            f.apply(plan)
        self.assertEqual(before, f.consumer_state())
        self.assertFalse((f.root / "companions").exists())

        # Restoring current document evidence does not restore the removed heading.
        mapping["resolved_sources"].append({"uri": source_uri, "sha256": "sha256:" + sha256_bytes(source.read_bytes())})
        save_map()
        self.assertIn("Unresolved derived source fragment", f.plan()["holds"][0])
        source.write_text("# Selected membership\n")
        mapping["resolved_sources"][-1]["sha256"] = "sha256:" + sha256_bytes(source.read_bytes())
        save_map()
        program_before = (f.consumer / "program.json").read_bytes()
        map_before = (f.consumer / "map.json").read_bytes()
        self.assertTrue(f.apply(f.plan())["complete"])
        self.assertEqual(program_before, (f.consumer / "program.json").read_bytes())
        self.assertEqual(map_before, (f.consumer / "map.json").read_bytes())

    def test_document_digest_covers_distinct_reentry_fragment(self):
        f = self.fixture
        f.add_context()
        program = json.loads((f.consumer / "program.json").read_text())
        program["residuals"] = [{"uri": "urn:test:residual", "kind": "unresolved", "subject_refs": [],
                                 "detail": "A retained source-owned residual", "source_refs": ["repo://consumer/PRODUCT.md"],
                                 "re_entry_refs": ["repo://consumer/PRODUCT.md#other-section"]}]
        write_json(f.consumer / "program.json", program)
        mapping = json.loads((f.consumer / "map.json").read_text())
        mapping["program_sha256"] = _axiom_digest(program)
        mapping["map_sha256"] = _axiom_digest({k: v for k, v in mapping.items() if k != "map_sha256"})
        write_json(f.consumer / "map.json", mapping)
        self.assertTrue(f.plan()["ready"])

    def test_absent_fragment_is_not_satisfied_by_document_digest(self):
        f = self.fixture
        f.add_context()
        program = json.loads((f.consumer / "program.json").read_text())
        program["frame_refs"] = ["repo://consumer/PRODUCT.md#missing-heading"]
        write_json(f.consumer / "program.json", program)
        mapping = json.loads((f.consumer / "map.json").read_text())
        mapping["program_sha256"] = _axiom_digest(program)
        mapping["map_sha256"] = _axiom_digest({k: v for k, v in mapping.items() if k != "map_sha256"})
        write_json(f.consumer / "map.json", mapping)
        plan = f.plan()
        self.assertFalse(plan["ready"])
        self.assertIn("Unresolved derived source fragment", plan["holds"][0])


if __name__ == "__main__":
    unittest.main()
