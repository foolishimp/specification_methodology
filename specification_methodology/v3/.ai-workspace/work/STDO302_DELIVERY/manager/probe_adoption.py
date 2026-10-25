"""Exercise explicit legacy-to-stable adoption using an installed wheel."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repository.resolve()
    sys.path[:0] = [str(repo / "specification_methodology/v2/tests"), str(repo / "specification_methodology/v2")]
    import stdo_toolchain
    from stdo_toolchain.errors import StdoError
    from stdo_toolchain.product_definition import adopt_definition, definition_status
    from test_stable_releases import StableReleaseTests, URI
    from test_toolchain import definition_document

    module = Path(stdo_toolchain.__file__).resolve()
    assert "site-packages" in module.parts and "src" not in module.parts
    test = StableReleaseTests()
    test.setUp()
    try:
        legacy = test.store.install(str(test.fixture.repository), "v3.0.0-rc.1")
        document = definition_document(test.fixture.repository, legacy.uri, legacy.manifest_sha256)
        document.pop("unrelated")
        document["$schema"] = legacy.uri + "standards/schemas/product-definition.schema.json"
        # This explicit consumer selection is separate from release publication.
        document["constitution"]["stdo"]["selector"] = "stdo://channels/3.0.2"
        consumer = test.root / "legacy-consumer"
        consumer.mkdir()
        definition = consumer / "stdo_default.json"
        definition.write_text(json.dumps(document, indent=2) + "\n")
        before = definition.read_bytes()
        plan = adopt_definition(definition, test.store, dry_run=True)
        assert plan["changed"] and plan["to"]["basis"] == URI
        assert definition.read_bytes() == before
        assert not test.store.is_installed("v3.0.2")
        try:
            adopt_definition(definition, test.store)
        except StdoError as exc:
            assert "requires --accept-plan-sha256" in str(exc)
            refusal = str(exc)
        else:
            raise AssertionError("Unaccepted adoption unexpectedly performed")
        assert definition.read_bytes() == before
        applied = adopt_definition(definition, test.store, accepted_plan_sha256=plan["plan_sha256"])
        after = json.loads(definition.read_bytes())
        expected = copy.deepcopy(document)
        expected["$schema"] = URI + "standards/schemas/product-definition.schema.json"
        expected["constitution"]["stdo"]["basis"] = {"uri": URI, "manifest_sha256": plan["to"]["manifest_sha256"]}
        assert after == expected
        assert definition_status(definition, test.store, verify=True)["valid"]
        assert test.store.verify("v3.0.0-rc.1", expected_manifest_sha256=legacy.manifest_sha256)["valid"]
        result = {
            "status": "passed explicit cross-version RC-to-stable adoption",
            "imported_manager": str(module), "manager_version": stdo_toolchain.__version__,
            "before_sha256": hashlib.sha256(before).hexdigest(), "plan": plan,
            "unaccepted_refusal": refusal, "applied": applied,
            "after": after, "legacy_install_unchanged": True,
            "limits": "Isolated consumer fixture and actual installed manager; no consumer adoption outside the fixture.",
        }
        args.output.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"status": result["status"], "imported_manager": str(module)}))
    finally:
        test.doCleanups()


if __name__ == "__main__":
    main()
