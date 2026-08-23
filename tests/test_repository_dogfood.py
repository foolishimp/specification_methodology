from __future__ import annotations

import subprocess
import tempfile
import unittest
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from stdo_toolchain.product_definition import definition_status
from stdo_toolchain.store import Store


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
            installed = store.install(str(repository), "v2.4.3-rc.1")
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

    def test_repository_product_definition_binds_the_rc2_builder_basis(
        self,
    ) -> None:
        repository = Path(__file__).resolve().parents[1]
        definition_path = repository / "stdo_default.json"
        definition = json.loads(definition_path.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temporary:
            store = Store(Path(temporary) / "store")
            installed = store.install(str(repository), "v2.4.3-rc.2")
            self.assertEqual(
                definition["constitution"]["stdo"]["basis"],
                {
                    "uri": installed.uri,
                    "manifest_sha256": installed.manifest_sha256,
                },
            )
            report = definition_status(definition_path, store, verify=True)
            self.assertTrue(report["valid"], report["failures"])
            for entrypoint in definition["constitution"]["entrypoints"][:2]:
                resolved = store.resolve(installed.uri + entrypoint["uri"])
                self.assertTrue(resolved.is_file(), entrypoint)

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
