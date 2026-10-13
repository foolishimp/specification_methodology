"""Bind current documentary pins to a working snapshot or a frozen source tree.

Inventory and source conservation locations remain author records. This command
does not change dispositions or convert old reviews into current acceptance.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("--source-commit")
args = parser.parse_args()
base = Path(__file__).resolve().parents[3]
root = base / "successor"
support = base / "qualification/C3"
inventory_path = support / "CANDIDATE.json"
inventory = json.loads(inventory_path.read_text())
old = {row["path"]: row for row in inventory["members"]}
rows = []
repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                  cwd=base, text=True).strip())
if args.source_commit:
    args.source_commit = subprocess.check_output(
        ["git", "rev-parse", args.source_commit + "^{commit}"], cwd=repo, text=True).strip()
for path in sorted(root.rglob("*")):
    if not path.is_file():
        continue
    relative = str(path.relative_to(root))
    body = path.read_bytes()
    if args.source_commit:
        frozen = subprocess.check_output(["git", "show", args.source_commit + ":" + str(path.relative_to(repo))], cwd=repo)
        if frozen != body:
            raise SystemExit("Package differs from selected source commit: " + relative)
    row = dict(old.get(relative, {"path": relative, "role": "Product member",
                                 "expected_installed_path": relative}))
    row.update(sha256=hashlib.sha256(body).hexdigest(), bytes=len(body))
    rows.append(row)
inventory.update(members=rows, source_input_commit="31f28f90c4a9b15243d84630fc4799024a9cd7ac",
                 inventory_input_commit=args.source_commit,
                 candidate_body_input_commit=args.source_commit,
                 standing="Author round-1 successor candidate under the unchanged common contract. Prior reviews retain their own cuts; whole-member acceptance and release remain open.",
                 snapshot_order="Package bytes verified from inventory_input_commit; external inventory is recorded in a descendant commit." if args.source_commit else
                                "Author working-tree snapshot; immutable source freeze remains pending.")
inventory_path.write_text(json.dumps(inventory, indent=2) + "\n")
path = support / "CONSERVATION.json"
mapping = json.loads(path.read_text())
for name, pin in mapping["successor_member_pins"].items():
    body = (root / name).read_bytes()
    pin.update(sha256=hashlib.sha256(body).hexdigest(), bytes=len(body))
for row in mapping["rows"]:
    if row.get("successor_sha256"):
        name = row["successor_locus"].split("#", 1)[0]
        row["successor_sha256"] = hashlib.sha256((root / name).read_bytes()).hexdigest()
mapping["candidate_source_commit"] = args.source_commit
mapping["round_1"] = {"source_commit": args.source_commit,
                       "meaning": "Author loci and pins refreshed; dispositions and historical judgment subjects unchanged.",
                       "independent_changed_cone_acceptance": "pending"}
path.write_text(json.dumps(mapping, indent=2) + "\n")
print(json.dumps({"package_members": len(rows), "source_commit": args.source_commit,
                  "author_frontier_rows": len(mapping["rows"])}))
