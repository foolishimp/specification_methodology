"""Execute the existing guarded release sequence after the recorded disposition."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--revision", required=True)
parser.add_argument("--review", type=Path, required=True)
parser.add_argument("--review-sha256", required=True)
args = parser.parse_args()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + "\n")


commands = []


def run(name, argv):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    (OUT / (name + ".stdout.txt")).write_bytes(result.stdout)
    (OUT / (name + ".stderr.txt")).write_bytes(result.stderr)
    commands.append({"name": name, "argv": argv, "started_at": started,
                     "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     "exit_code": result.returncode, "stdout_sha256": sha(result.stdout),
                     "stderr_sha256": sha(result.stderr)})
    save("publication-commands.json", commands)
    require(result.returncode == 0, name + " failed; no fallback or automatic retry")
    return result.stdout


def git(*argv):
    return subprocess.check_output(["git", *argv], cwd=ROOT, text=True).strip()


def direct(ref):
    result = subprocess.run(["git", "rev-parse", "--verify", ref], cwd=ROOT,
                            capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


revision = git("rev-parse", args.revision + "^{commit}")
require(git("rev-parse", "HEAD") == revision, "HEAD must remain exact commit B")
require(sha(args.review.read_bytes()) == args.review_sha256, "consumed review bytes differ")
require(not (OUT / "publication-commands.json").exists(), "retain and assess the existing attempt before any retry")
manifest = json.loads(git("show", revision + ":stack_release.json"))
require(manifest["cohort"]["cut"] == "v2.5.0-rc.6", "wrong selected release")
require((ROOT / "scripts/check_stack_release.py").read_bytes()
        == subprocess.check_output(["git", "show", revision + ":scripts/check_stack_release.py"], cwd=ROOT),
        "shared checker differs from B")
products = manifest["products"]
freeze = products["specification_methodology"]["freeze"]
expected = manifest["publication"]["expected_remote"]
require(direct(products["specification_methodology"]["release_ref"]) == freeze["tag_object"],
        "source A immutable tag differs")
for name, product in products.items():
    if name != "specification_methodology":
        require(direct(product["release_ref"]) is None, "immutable child cut already exists")
    for field in ("selector_ref", "rc_branch", "release_branch"):
        require(direct(product[field]) == expected[product[field]], "local predecessor differs: " + product[field])

save("publication-disposition-binding.json", {
    "kind": "rc6.publication-writer-disposition-binding", "writer": "/root/t030_m01_writer",
    "commit_b": revision, "review": str(args.review), "review_sha256": args.review_sha256,
    "authority": "Direct owner RC6 release instruction and coordinator consumption of the exact independent native/final result before this execution.",
    "mechanism": "Existing STACK_RELEASE local refs, shared refs gate, exact emitted atomic push argv, published gate; no alternative transport."})

local = []
for name, product in products.items():
    target = freeze["commit"] if name == "specification_methodology" else revision
    if name != "specification_methodology":
        run("local-cut-" + name, ["git", "tag", "-a", product["release_ref"].removeprefix("refs/tags/"),
            target, "-m", name + " v2.5.0-rc.6 qualified coordinated release"])
    run("local-selector-" + name, ["git", "tag", "-f", "-a",
        product["selector_ref"].removeprefix("refs/tags/"), target,
        "-m", name + " v2.5.0 selects qualified v2.5.0-rc.6"])
    for field in ("rc_branch", "release_branch"):
        run("local-" + field + "-" + name,
            ["git", "update-ref", product[field], target, expected[product[field]]])
    local.append({"product": name, "release_ref": product["release_ref"],
                  "tag_object": direct(product["release_ref"]), "commit": target,
                  "repository_tree": git("rev-parse", target + "^{tree}"),
                  "product_subtree": git("rev-parse", target + ":" + product["subtree"]),
                  "selector_ref": product["selector_ref"],
                  "selector_preimage": expected[product["selector_ref"]],
                  "selector_object": direct(product["selector_ref"])})
save("local-refs.json", {"kind": "rc6.local-ref-construction", "commit_b": revision,
                         "products": local, "remote_effects": False})

checker = [sys.executable, "scripts/check_stack_release.py", "--revision", revision, "--remote", "origin"]
ref_bytes = run("cohort-refs-final", [*checker, "--phase", "refs"])
(OUT / "cohort-refs-final.json").write_bytes(ref_bytes)
qualification = json.loads(ref_bytes)
require(qualification["status"] == "valid" and not qualification["failures"], "ref gate refused")
run("atomic-publication", qualification["push_argv"])
save("atomic-publication.json", {"kind": "rc6.atomic-publication-observation",
    "actor": "/root/t030_m01_writer", "commit_b": revision,
    "refs_gate_sha256": sha(ref_bytes), "qualified_push_sha256": qualification["qualified_push_sha256"],
    **commands[-1]})
published_bytes = run("cohort-published", [*checker, "--phase", "published"])
(OUT / "cohort-published.json").write_bytes(published_bytes)
published = json.loads(published_bytes)
require(published["status"] == "valid" and not published["failures"], "published verification refused")
print(json.dumps({"status": "valid", "commit_b": revision,
                  "published_gate": "cohort-published.json", "fresh_public_reacquisition": "pending"}))
