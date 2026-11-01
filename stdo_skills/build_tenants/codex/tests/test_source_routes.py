"""Current provider-source checks, separate from portable package custody."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import verify_package as package


TENANT = Path(__file__).resolve().parents[1]


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def seal(root):
    inventory = json.loads((root / "inventory.json").read_text())
    inventory["files"] = [{"path": name, **value} for name, value in package.regulars(root).items()
                          if name != "inventory.json"]
    write_json(root / "inventory.json", inventory)


class CurrentSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="stdo-skills-route-control-")
        self.addCleanup(self.temp.cleanup)
        self.scratch = Path(self.temp.name).resolve()
        self.repo = self.scratch / "repo"
        self.repo.mkdir()
        (self.repo / ".git").mkdir()
        self.tenant = self.repo / "stdo_skills/build_tenants/codex"
        shutil.copytree(TENANT, self.tenant, ignore=shutil.ignore_patterns("__pycache__"))
        self.route_file = self.tenant / "skills/stdo-work/source-routes.json"
        self.routes = json.loads(self.route_file.read_text())
        self.selected = self.routes["representation_provider"]["selection"]
        self.current = [row for row in self.routes["sources"] if row.get("selection") == self.selected]
        self.targets = {}
        for row in self.current:
            path = self.repo / ("stdo_skills" if row["root"] == "product" else "a_c") / row["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            raw = ("Controlled current source " + row["root"] + ":" + row["path"] + "\n").encode()
            path.write_bytes(raw)
            row["sha256"] = hashlib.sha256(raw).hexdigest()
            self.targets[row["root"], row["path"]] = path
        provider = self.routes["representation_provider"]
        provider["sha256"] = next(row["sha256"] for row in self.current
                                  if (row["root"], row["path"]) == (provider["root"], provider["path"]))
        write_json(self.route_file, self.routes)
        seal(self.tenant)

    def test_repository_checks_current_routes_and_preserves_absent_historical_sources(self):
        # Historical references are deliberately neither acquired nor refreshed.
        historical = [row for row in self.routes["sources"] if "selection" not in row]
        self.assertTrue(historical)
        result = package.check(self.tenant)
        self.assertEqual(result["current_sources"]["status"], "checked")
        self.assertEqual(result["current_sources"]["files"], len(self.targets))

    def test_changed_product_and_tool_source_refuse_even_after_package_reseal(self):
        for key in (("product", "specification/composition/REPRESENTATION_MANIFEST.json"),
                    ("tool", "build_tenants/graphify/design/project-build.md")):
            path = self.targets[key]
            before = path.read_bytes()
            path.write_bytes(before + b"changed provider\n")
            seal(self.tenant)
            with self.subTest(root=key[0]), self.assertRaisesRegex(ValueError, "current source digest mismatch"):
                package.check(self.tenant)
            path.write_bytes(before)

    def test_stale_route_pin_refuses_with_fresh_package_inventory(self):
        changed = copy.deepcopy(self.routes)
        changed["representation_provider"]["sha256"] = "0" * 64
        for row in changed["sources"]:
            if row.get("selection") == self.selected and row["path"] == changed["representation_provider"]["path"]:
                row["sha256"] = "0" * 64
        write_json(self.route_file, changed)
        seal(self.tenant)
        with self.assertRaisesRegex(ValueError, "current source digest mismatch"):
            package.check(self.tenant)

    def test_portable_custody_discloses_unchecked_sources_and_explicit_repo_checks_them(self):
        portable = self.scratch / "portable"
        shutil.copytree(self.tenant, portable)
        installed = self.scratch / "installed-skill"
        shutil.copytree(portable / "skills/stdo-work", installed)
        result = package.check(portable, installed=installed)
        self.assertTrue(result["installed_checked"])
        self.assertEqual(result["current_sources"]["status"], "not_performed")
        checked = package.check(portable, repository=self.repo)
        self.assertEqual(checked["current_sources"]["status"], "checked")
        target = self.targets["tool", "build_tenants/graphify/design/project-build.md"]
        target.write_text("changed\n")
        with self.assertRaisesRegex(ValueError, "current source digest mismatch"):
            package.check(portable, repository=self.repo)

    def test_conflicting_provider_duplicate_refuses_without_external_roots(self):
        self.routes["representation_provider"]["sha256"] = "0" * 64
        write_json(self.route_file, self.routes)
        seal(self.tenant)
        portable = self.scratch / "portable"
        shutil.copytree(self.tenant, portable)
        with self.assertRaisesRegex(ValueError, "contradicts its selected source route"):
            package.check(portable)

    def test_current_route_cannot_escape_its_product_root(self):
        self.current[0]["path"] = "../outside.md"
        write_json(self.route_file, self.routes)
        seal(self.tenant)
        with self.assertRaisesRegex(ValueError, "unsafe current source path"):
            package.check(self.tenant)


if __name__ == "__main__":
    unittest.main()
