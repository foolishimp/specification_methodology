#!/usr/bin/env python3
"""Focused resource and owned-lifecycle falsifiers. Explicit fresh fixture root.

All fixture effects remain under --fixtures. Output is JSON evidence on stdout;
this does not run a model or claim actual-host skill behavior.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

PKG = Path(__file__).resolve().parents[1]
HELPER = Path("skills/stdo-release-install/scripts/manage_install.py")
spec = importlib.util.spec_from_file_location("claude_repair_helper", PKG / HELPER)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
parser = argparse.ArgumentParser()
parser.add_argument("--fixtures", required=True, type=Path)
args = parser.parse_args()
ROOT = args.fixtures.absolute()
if ROOT.exists() or ROOT.is_symlink() or ROOT.is_relative_to(PKG):
    raise SystemExit("Fixture root must be fresh and outside source package")
ROOT.mkdir(parents=True)
results, commands = [], []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(root):
    rows = {}
    for parent, dirs, files in os.walk(root, followlinks=False):
        for name in sorted(dirs + files):
            path = Path(parent) / name
            key = path.relative_to(root).as_posix()
            rows[key] = ("link", os.readlink(path)) if path.is_symlink() else ("dir", None) if path.is_dir() else ("file", sha(path))
    return rows


def inventory(package):
    rows = ["# Fixture inventory", "", "| Path | SHA256 |", "| --- | --- |"]
    for path in sorted(package.rglob("*")):
        if path.is_file() and path.name != "INVENTORY.md":
            rows.append("| " + path.relative_to(package).as_posix() + " | " + sha(path) + " |")
    (package / "INVENTORY.md").write_text("\n".join(rows) + "\n")


def copied(label):
    target = ROOT / label / "package"
    shutil.copytree(PKG, target)
    return target


def command(helper, action, workspace=None, package=None, receipt=None):
    argv = [sys.executable, "-I", "-B", str(helper), action]
    if package is not None:
        argv += ["--package", str(package)]
    if workspace is not None:
        argv += ["--workspace", str(workspace)]
    if receipt is not None:
        argv += ["--receipt-sha256", receipt]
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=30)
    try:
        body = json.loads(completed.stdout)
    except ValueError:
        body = {"invalid_stdout": completed.stdout, "stderr": completed.stderr}
    commands.append({"argv": argv, "exit": completed.returncode, "result": body})
    return completed.returncode, body


def run(name, test):
    try:
        test()
        results.append({"case": name, "passed": True})
    except Exception as exc:
        results.append({"case": name, "passed": False, "detail": type(exc).__name__ + ": " + str(exc)})


def local_reference(label, target, existing_outside=False, expect_ok=False):
    package = copied(label)
    if existing_outside:
        (package / "outside.md").write_text("outside declared bundle\n")
    skill = package / "skills/stdo-workspace-change/SKILL.md"
    skill.write_text(skill.read_text() + "\n[required resource](" + target + ")\n")
    inventory(package)
    errors = module.validate_package(package)
    assert (not errors) == expect_ok, errors
    if not expect_ok:
        assert any("Missing or escaping" in e for e in errors), errors


def symlink_resource():
    package = copied("symlink-resource")
    outside = ROOT / "outside.md"; outside.write_text("external\n")
    ref = package / "skills/stdo-workspace-change/escape.md"; ref.symlink_to(outside)
    inventory(package)
    assert any("Symlink" in e for e in module.validate_package(package))


def install(label):
    workspace = ROOT / label / "workspace"; workspace.mkdir(parents=True)
    unrelated = workspace / ".claude/skills/unrelated"; unrelated.mkdir(parents=True)
    (unrelated / "SKILL.md").write_text("foreign sibling\n")
    (workspace / ".claude/config.txt").write_text("unrelated config\n")
    code, body = command(PKG / HELPER, "install", workspace, PKG)
    assert code == 0 and body["status"] == "ok", body
    return workspace, body["receipt_sha256"]


def clean_lifecycle():
    workspace, previous = install("clean")
    new = copied("new-compatible")
    changed = new / "skills/stdo-release-install/references/maintenance.md"
    changed.write_text(changed.read_text() + "\nFixture compatible successor marker.\n")
    inventory(new)
    code, update = command(new / HELPER, "update", workspace, new, previous)
    assert code == 0 and update["receipt_sha256"] != previous, update
    assert (workspace / ".claude/skills/stdo-release-install/references/maintenance.md").read_bytes() == changed.read_bytes()
    for name in module.NAMES:
        assert module.tree(workspace / ".claude/skills" / name) == module.tree(new / "skills" / name)
    code, result = command(workspace / ".claude" / HELPER, "remove", workspace, receipt=update["receipt_sha256"])
    assert code == 0, result
    assert not (workspace / ".claude" / module.RECEIPT).exists()
    assert all(not (workspace / ".claude/skills" / name).exists() for name in module.NAMES)
    assert (workspace / ".claude/skills/unrelated/SKILL.md").read_text() == "foreign sibling\n"
    assert (workspace / ".claude/config.txt").read_text() == "unrelated config\n"


def refusal(label, mutate, action="remove", wrong_receipt=False):
    workspace, receipt = install(label)
    mutate(workspace)
    before = snapshot(workspace)
    code, body = command(PKG / HELPER, action, workspace, PKG if action == "update" else None, "0"*64 if wrong_receipt else receipt)
    assert code == 1 and body.get("status") == "refused", body
    assert snapshot(workspace) == before, "Refused operation mutated the installation"


def foreign_collision():
    workspace = ROOT / "foreign/workspace"; directory = workspace / ".claude/skills/stdo-workspace-change"
    directory.mkdir(parents=True); (directory / "SKILL.md").write_text("foreign same-name\n")
    before = snapshot(workspace)
    code, body = command(PKG / HELPER, "install", workspace, PKG)
    assert code == 1 and body["status"] == "refused", body
    assert snapshot(workspace) == before


def corrupt_update():
    workspace, receipt = install("corrupt-update")
    package = copied("corrupt-source")
    (package / "skills/stdo-continuation/SKILL.md").write_text("corrupt without new inventory\n")
    before = snapshot(workspace)
    code, body = command(package / HELPER, "update", workspace, package, receipt)
    assert code == 1 and body["status"] == "refused", body
    assert snapshot(workspace) == before


def malformed_receipt():
    workspace, _ = install("malformed-receipt")
    path = workspace / ".claude" / module.RECEIPT
    path.write_text("[]\n")
    before = snapshot(workspace)
    code, body = command(PKG / HELPER, "remove", workspace, receipt=sha(path))
    assert code == 1 and body["status"] == "refused", body
    assert snapshot(workspace) == before


run("unchanged full package", lambda: module.checked_source(PKG))
run("missing local reference with refreshed inventory", lambda: local_reference("missing", "missing.md"))
run("nested traversal to existing outside file", lambda: local_reference("escape", "references/../../../outside.md", True))
run("encoded traversal to existing outside file", lambda: local_reference("encoded", "%2e%2e/%2e%2e/outside.md", True))
run("explicit sibling dependency resolves within declared bundle", lambda: local_reference("sibling", "references/../../stdo-tool-operations/SKILL.md", expect_ok=True))
run("existing escaping symlink with refreshed inventory", symlink_resource)
run("clean install compatible update and installed-helper removal", clean_lifecycle)
run("foreign same-name install is preserved", foreign_collision)
run("hidden local addition preserved on removal", lambda: refusal("extra", lambda w: (w/".claude/skills/stdo-continuation/.local").write_text("mine")))
run("empty local directory preserved on update", lambda: refusal("extra-dir", lambda w: (w/".claude/skills/stdo-continuation/local").mkdir(), "update"))
run("modified installed file preserved on update", lambda: refusal("modified", lambda w: (w/".claude/skills/stdo-continuation/SKILL.md").write_text("mine"), "update"))
run("missing installed file refuses removal", lambda: refusal("missing-installed", lambda w: (w/".claude/skills/stdo-continuation/SKILL.md").unlink()))
run("wrong selected receipt preserves installation", lambda: refusal("wrong-receipt", lambda w: None, wrong_receipt=True))
run("installed symlink preserved by refusal", lambda: refusal("installed-link", lambda w: (w/".claude/skills/stdo-continuation/extra").symlink_to(w/".claude/config.txt")))
run("invalid source refuses update without target mutation", corrupt_update)
run("malformed ownership receipt refused", malformed_receipt)
print(json.dumps({"source_inventory_sha256": sha(PKG/"INVENTORY.md"), "fixtures": str(ROOT), "cases": results, "commands": commands}, indent=2))
raise SystemExit(0 if all(row["passed"] for row in results) else 1)
