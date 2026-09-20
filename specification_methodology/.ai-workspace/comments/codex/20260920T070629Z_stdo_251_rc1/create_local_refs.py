"""Create the absent local cohort refs atomically; never push or move a cut."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
parser = argparse.ArgumentParser()
parser.add_argument("--commit", required=True)
args = parser.parse_args()
if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
    raise SystemExit("Require the full frozen commit-B identity")


def git(*argv, text=None):
    return subprocess.check_output(["git", *argv], cwd=ROOT, input=text,
                                   text=True).strip()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


content = json.loads((OUT / "cohort-content-commit-b.json").read_text())
require(content.get("status") == "valid" and not content.get("failures"),
        "Frozen commit-B content gate is not satisfied")
require(content.get("checked_revision") == args.commit, "Content gate covers a different revision")
disposition = json.loads((OUT / "candidate-disposition.json").read_text())
require(disposition.get("status") == "qualified_for_local_freeze",
        "Exact candidate disposition does not select local freeze")
require(git("rev-parse", "refs/heads/main") == args.commit, "main differs from commit B")
cohort_bytes = subprocess.check_output(["git", "show", args.commit + ":stack_release.json"], cwd=ROOT)
cohort = json.loads(cohort_bytes)
require(hashlib.sha256(cohort_bytes).hexdigest() == disposition["cohort_sha256"],
        "Candidate disposition covers different cohort bytes")
disposition_path = str((OUT / "candidate-disposition.json").relative_to(ROOT))
require(subprocess.check_output(["git", "show", args.commit + ":" + disposition_path], cwd=ROOT)
        == (OUT / "candidate-disposition.json").read_bytes(), "Disposition differs from frozen commit B")
require(cohort["cohort"]["version"] == "2.5.1-rc.1", "Unexpected cohort")
source = cohort["products"]["specification_methodology"]
require(git("rev-parse", source["release_ref"]) == source["freeze"]["tag_object"],
        "Source immutable tag changed")
require(git("rev-parse", source["release_ref"] + "^{commit}") == source["freeze"]["commit"],
        "Source immutable commit changed")
targets = []
for name, product in cohort["products"].items():
    commit = source["freeze"]["commit"] if name == "specification_methodology" else args.commit
    if name != "specification_methodology":
        targets.append((product["release_ref"], commit, True))
    targets.append((product["selector_ref"], commit, True))
    targets.extend((product[key], commit, False) for key in ("rc_branch", "release_branch"))
for ref, commit, annotated in targets:
    result = subprocess.run(["git", "show-ref", "--verify", "--quiet", ref], cwd=ROOT)
    require(result.returncode == 1, "Expected absent local ref: " + ref)

tagger = git("var", "GIT_COMMITTER_IDENT")
creates = []
for ref, commit, annotated in targets:
    if annotated:
        tag = ref.removeprefix("refs/tags/")
        body = (f"object {commit}\ntype commit\ntag {tag}\ntagger {tagger}\n\n"
                "STDO 2.5.1 RC1 cohort; owner-selected release with recorded native limitations.\n")
        object_id = git("mktag", text=body)
    else:
        object_id = commit
    creates.append({"ref": ref, "object": object_id, "commit": commit, "annotated": annotated})
transaction = "start\n" + "".join(f"create {r['ref']} {r['object']}\n" for r in creates) + "prepare\ncommit\n"
receipt = git("update-ref", "--stdin", text=transaction)
result = {"commit_b": args.commit, "tree": git("rev-parse", args.commit + "^{tree}"),
          "created": creates, "transaction_receipt": receipt, "published": False,
          "source_cut_preserved": source["release_ref"],
          "claim": "Local ref construction only; the mandatory refs gate follows."}
(OUT / "local-ref-construction.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"commit_b": args.commit, "created_ref_count": len(creates), "published": False}))
