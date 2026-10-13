"""Run bounded checks on exact frozen package bytes and bind their receipts.

This is a qualification Writer. It does not issue a cut or accept a member.
The package, checker programs and original a_c fixture must match the named
source commit before execution. Receipts are recorded in a descendant commit.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--source-commit", required=True)
args = parser.parse_args()
base = Path(__file__).resolve().parents[3]
support = base / "qualification/C3"
root = base / "successor"
repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=base, text=True).strip())
source_commit = subprocess.check_output(["git", "rev-parse", args.source_commit + "^{commit}"], cwd=repo, text=True).strip()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def frozen(path):
    relative = str(path.relative_to(repo))
    raw = path.read_bytes()
    old = subprocess.check_output(["git", "show", source_commit + ":" + relative], cwd=repo)
    if raw != old:
        raise ValueError("Changed frozen input: " + relative)
    return {"path": relative, "sha256": sha(raw)}


tree_names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", source_commit, "--",
                                     str(root.relative_to(repo))], cwd=repo, text=True).splitlines()
current_names = sorted(str(p.relative_to(repo)) for p in root.rglob("*") if p.is_file())
if sorted(tree_names) != current_names:
    raise ValueError("Package membership differs from the frozen source")
package = [{"path": str((repo / name).relative_to(root)), "sha256": frozen(repo / name)["sha256"]}
           for name in current_names]
package_digest = sha(json.dumps(package, sort_keys=True, separators=(",", ":")).encode())
subject = {"kind": "frozen_codex_package", "source_commit": source_commit,
           "package_member_count": len(package), "package_content_sha256": package_digest,
           "digest_recipe": "SHA-256 of sorted path/sha256 descriptors as compact sorted-key JSON"}
programs = [support / "check_candidate.py", support / "check_distribution.py",
            support / "refresh_views.py", support / "round-1/check_acquisition.py",
            support / "round-1/derivation_material.py"]
program_pins = [frozen(p) for p in programs]
for p in [support / "FRAME_INPUTS.json", support / "a_c/program.json", support / "a_c/bindings.json",
          support / "a_c/SOURCE.md"]:
    frozen(p)

commands = [
    ("ARTIFACT_CHECK.json", [sys.executable, "-B", str(support / "check_candidate.py")]),
    ("../DISTRIBUTION_CHECK.json", [sys.executable, "-B", str(support / "check_distribution.py")]),
    ("ACQUISITION_CHECK.json", [sys.executable, "-B", str(support / "round-1/check_acquisition.py")]),
    ("IDENTITY_CHECK.json", [sys.executable, "-B", str(support / "round-1/derivation_material.py"), "--test"]),
]
for name, command in commands:
    result = subprocess.run(command, cwd=repo, capture_output=True, text=True, check=True)
    target = Path(__file__).parent / name
    if name == "ARTIFACT_CHECK.json":
        receipt = json.loads(result.stdout)
    else:
        receipt = json.loads(target.read_text())
    if not receipt.get("valid"):
        raise ValueError("Check failed: " + name)
    receipt["subject"] = subject
    receipt["checker_source_pins"] = program_pins
    if name == "IDENTITY_CHECK.json":
        receipt["positive_basis_scope"] = "Hypothetical v0.0.0-rc.1 fixture identities, not issued identities"
    target.write_text(json.dumps(receipt, indent=2) + "\n")
    print(name + ": valid; frozen source " + source_commit[:7])

tool_receipt = json.loads((support / "a_c/INSTALL_VERIFICATION.json").read_text())
tool_root = base / "a_c/install/axiom_indexer-v2.5.1-rc.2"
for member in tool_receipt["members"]:
    path = tool_root / member["path"]
    raw = os.readlink(path).encode() if member["type"] == "symlink" else path.read_bytes()
    if sha(raw) != member["sha256"]:
        raise ValueError("Changed installed a_c tool member: " + member["path"])
subprocess.run([sys.executable, "-B", str(tool_root / "build_tenants/core/code/ac.py"), "validate",
                "--program", str(support / "a_c/program.json"),
                "--bindings", str(support / "a_c/bindings.json"),
                "--output", str(Path(__file__).with_name("AC_VALIDATION.json")),
                "--emit-map", str(Path(__file__).with_name("AC_MAP.json"))], cwd=repo, check=True)
ac_path = Path(__file__).with_name("AC_VALIDATION.json")
ac_receipt = json.loads(ac_path.read_text())
if ac_receipt.get("status") != "valid" or ac_receipt.get("diagnostics"):
    raise ValueError("a_c validation failed")
ac_receipt["subject"] = subject
ac_receipt["installed_tool_members_verified"] = len(tool_receipt["members"])
ac_receipt["limits"] = ["Existing six-clause program; no whole-method or new identity-contract acceptance"]
ac_path.write_text(json.dumps(ac_receipt, indent=2) + "\n")

# The acquisition check calls refresh. Recheck frozen bytes after every run so
# a mutated subject cannot receive the original commit's evidence binding.
for name in current_names:
    frozen(repo / name)
frozen(support / "FRAME_INPUTS.json")
summary = {"subject": subject, "checker_source_pins": program_pins,
           "checked_reports": [name for name, _ in commands] + ["AC_VALIDATION.json"], "valid": True,
           "limits": ["Bounded documentary and byte verification, not semantic or release acceptance",
                      "The checking Writer and its code are recorded in the descendant checkpoint"]}
Path(__file__).with_name("FROZEN_CHECK.json").write_text(json.dumps(summary, indent=2) + "\n")
