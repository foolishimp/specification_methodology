from __future__ import annotations

import subprocess
import tempfile
import unittest
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from stdo_toolchain.product_definition import definition_status, install_bootstrap
from stdo_toolchain.store import Store


def git_repository(project_root: Path) -> Path:
    return Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=project_root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    )


class RepositoryDogfoodTests(unittest.TestCase):
    def test_install_released_stdo_2_4_3_rc1_exactly(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        available = subprocess.run(
            ["git", "cat-file", "-e", "v2.4.3-rc.1^{tag}"],
            cwd=repository,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if available.returncode != 0:
            self.skipTest("repository checkout does not contain v2.4.3-rc.1")
        with tempfile.TemporaryDirectory() as temporary:
            store = Store(Path(temporary) / "store")
            installed = store.install(str(git_repository(repository)), "v2.4.3-rc.1")
            self.assertEqual(
                installed.manifest_sha256,
                "ca6cdcb78166998e96e1efe07128209c15f6277b1c67b3e5760529f70bc538a9",
            )
            self.assertEqual(installed.manifest["standards"]["member_count"], 45)
            self.assertEqual(
                installed.manifest["standards"]["member_set_sha256"],
                "3617ba1b13f134284564621b6e61dbce361d2f6341b768e4d90b5a47554c67cd",
            )
            self.assertEqual(
                installed.manifest["release"]["commit"],
                "7207b43bba9a422c676840567e1566ff3f1558fb",
            )
            self.assertTrue(store.verify("v2.4.3-rc.1")["valid"])
            manifest_schema = json.loads(
                (
                    repository
                    / "specification/standards/schemas/installed-release-manifest.schema.json"
                ).read_text(encoding="utf-8")
            )
            Draft202012Validator.check_schema(manifest_schema)
            errors = list(
                Draft202012Validator(manifest_schema).iter_errors(installed.manifest)
            )
            self.assertEqual(errors, [])

    def test_install_released_stdo_2_5_0_rc1_exactly(self) -> None:
        repository = Path(__file__).resolve().parents[1]
        available = subprocess.run(
            ["git", "cat-file", "-e", "v2.5.0-rc.1^{tag}"],
            cwd=repository,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if available.returncode != 0:
            self.skipTest("repository checkout does not contain v2.5.0-rc.1")
        with tempfile.TemporaryDirectory() as temporary:
            store = Store(Path(temporary) / "store")
            installed = store.install(str(git_repository(repository)), "v2.5.0-rc.1")
            self.assertEqual(
                installed.manifest_sha256,
                "3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338",
            )
            self.assertEqual(installed.manifest["standards"]["member_count"], 51)
            self.assertEqual(
                installed.manifest["standards"]["member_set_sha256"],
                "87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5",
            )
            self.assertEqual(
                installed.manifest["release"]["commit"],
                "ca6694314c4e9a56d3facae3eef06fe2792104c9",
            )
            self.assertTrue(store.verify("v2.5.0-rc.1")["valid"])

    def test_revision_three_product_definition_template_is_structurally_valid(
        self,
    ) -> None:
        repository = Path(__file__).resolve().parents[1]
        schema = json.loads(
            (
                repository
                / "specification/standards/schemas/product-definition.schema.json"
            ).read_text(encoding="utf-8")
        )
        template_text = (
            repository
            / "specification/standards/templates/PRODUCT_DEFINITION_TEMPLATE.json"
        ).read_text(encoding="utf-8")
        template_text = (
            template_text.replace(
                "REPLACE_WITH_IMMUTABLE_CUT",
                "v2.4.3-rc.2",
            )
            .replace(
                "REPLACE_WITH_VERSION_LINE",
                "2.4.3",
            )
            .replace(
                "REPLACE_WITH_64_LOWERCASE_HEX_SHA256",
                "0" * 64,
            )
        )
        template = json.loads(template_text)
        Draft202012Validator.check_schema(schema)
        errors = list(
            Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            ).iter_errors(template)
        )
        self.assertEqual(errors, [])
        template["product"]["source_project"] = "not a uri with spaces"
        format_errors = list(
            Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            ).iter_errors(template)
        )
        self.assertTrue(
            any(error.validator == "format" for error in format_errors),
            format_errors,
        )
        escaping = json.loads(template_text)
        escaping["constitution"]["agent_bootstrap"]["targets"] = ["../../victim.md"]
        target_errors = list(
            Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            ).iter_errors(escaping)
        )
        self.assertTrue(
            any(error.validator == "pattern" for error in target_errors),
            target_errors,
        )

    def test_repository_product_definition_binds_the_rc4_builder_basis(
        self,
    ) -> None:
        repository = Path(__file__).resolve().parents[1]
        definition_path = repository / "stdo_default.json"
        definition = json.loads(definition_path.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temporary:
            store = Store(Path(temporary) / "store")
            installed = store.install(str(git_repository(repository)), "v2.5.0-rc.4")
            self.assertEqual(
                installed.manifest_sha256,
                "4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e",
            )
            self.assertEqual(
                installed.manifest["release"],
                {
                    "cut": "v2.5.0-rc.4",
                    "tag_object": "032dac0c833111547f7dd4b290c5316ed9b70f97",
                    "commit": "7a25668a8fecfd26f895759af3bec4708727964a",
                    "tree": "737af9a7a2779dbf59e7c81232e7efd4dd98692a",
                    "standards_tree": "d6642edac9fb509a68b2ffc81d3404f2360b34e4",
                    "project_release_namespace": "specification_methodology",
                    "qualified_ref": "refs/tags/specification_methodology/v2.5.0-rc.4",
                    "project_subtree_root": "specification_methodology",
                    "project_subtree_tree": "a9565f923213759984f936d087cd7cebd0f44a74",
                },
            )
            self.assertEqual(installed.manifest["standards"]["member_count"], 52)
            self.assertEqual(
                installed.manifest["standards"]["member_set_sha256"],
                "504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656",
            )
            self.assertEqual(
                definition["constitution"]["stdo"]["basis"],
                {
                    "uri": installed.uri,
                    "manifest_sha256": installed.manifest_sha256,
                },
            )
            report = definition_status(definition_path, store, verify=True)
            self.assertTrue(report["valid"], report["failures"])
            self.assertEqual(
                [
                    entrypoint["uri"]
                    for entrypoint in definition["constitution"]["entrypoints"][:4]
                ],
                [
                    "standards/authority_compressions/stdo_bootstrap.md",
                    "standards/SPEC_METHOD.md",
                    "standards/REFERENCE_FRAME_METHOD.md",
                    "standards/STDO_REFERENCE_FRAME_BASELINE.md",
                ],
            )
            for entrypoint in definition["constitution"]["entrypoints"][:4]:
                resolved = store.resolve(installed.uri + entrypoint["uri"])
                self.assertTrue(resolved.is_file(), entrypoint)
            bootstrap = install_bootstrap(definition_path, store, dry_run=True)
            self.assertEqual(
                [target["action"] for target in bootstrap["targets"]],
                ["unchanged", "unchanged"],
            )

        for reference in (
            definition["what"]["intent"],
            definition["what"]["product"],
            *definition["what"]["specification"],
            *definition["how"]["build_tenants"][0]["design"],
            *definition["how"]["build_tenants"][0]["implementation"],
        ):
            self.assertTrue((repository / reference).exists(), reference)


if __name__ == "__main__":
    unittest.main()
