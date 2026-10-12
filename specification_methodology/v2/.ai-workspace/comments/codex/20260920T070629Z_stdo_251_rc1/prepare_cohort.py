"""Prepare exact local 2.5.1 RC1 cohort; no Git mutation or publication."""
from pathlib import Path
import argparse
import importlib.util
import json
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
parser = argparse.ArgumentParser()
parser.add_argument("--review", type=Path, default=OUT / "companion-review.json")
parser.add_argument("--record-suffix", default="")
args = parser.parse_args()
VERSION = "2.5.1-rc.1"
LINE = "2.5.1"
CUT = "v" + VERSION
OLD_B = "4824d5a05619e6957110b7ac97464b42ac84c096"
ARTIFACT_ROOT = f"build_tenants/axiom_indexer/representation/stdo-{CUT}"
URL = "https://github.com/foolishimp/specification_methodology.git"
spec = importlib.util.spec_from_file_location("rc1_cohort_checker", ROOT / "scripts/check_stack_release.py")
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)
view = check.View(ROOT)
prior = check.View(ROOT, OLD_B).read_json("stack_release.json")
payload = json.loads(json.dumps(prior))


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def sha(relative):
    return check.sha256(view.read_bytes(relative))


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


review = json.loads(args.review.read_text())
require(review["status"] == "satisfied", "companion assessment is not satisfied")
for relative, digest in review["files"].items():
    require(sha(relative) == digest, "reviewed companion changed: " + relative)
payload["cohort"].update(version=VERSION, cut=CUT, status="candidate")
for name, product in payload["products"].items():
    product.update(version=VERSION, release_ref=f"refs/tags/{name}/{CUT}",
                   selector_ref=f"refs/tags/{name}/v{LINE}",
                   rc_branch=f"refs/heads/rc/{name}/{LINE}",
                   release_branch=f"refs/heads/release/{name}/{LINE}",
                   release_note=f"{name}/releases/v{LINE}.md")
    product["release_note_markers"] = [m.replace("2.5.0-rc.7", VERSION)
                                       for m in product["release_note_markers"]]
installed = json.loads((OUT / "stdo-install.json").read_text())
verified = json.loads((OUT / "stdo-verify.json").read_text())
require(verified["valid"] and not verified["failures"], "Source Install is not verified")
require(installed["manifest_sha256"] == verified["manifest_sha256"], "Install identity mismatch")
source_inventory = json.loads((OUT / "source-inventory.json").read_text())
freeze = {key: installed["release"][key] for key in
          ("tag_object", "commit", "tree", "project_subtree_tree", "standards_tree")}
require(check.local_tag_identity(ROOT, payload["products"]["specification_methodology"]["release_ref"],
                                 "specification_methodology") == freeze, "source tag drift")
freeze.update(installed_manifest_sha256=installed["manifest_sha256"],
              standards_member_count=installed["standards"]["member_count"],
              standards_member_set_sha256=installed["standards"]["member_set_sha256"],
              plugin_member_count=len(source_inventory["plugin"]),
              plugin_member_set_sha256=source_inventory["plugin_member_set_sha256"])
payload["products"]["specification_methodology"]["freeze"] = freeze


def inventory(name):
    product = payload["products"][name]
    failures = []
    required = check.required_child_members(view, name, product, failures)
    require(not failures, "; ".join(failures))
    members = []
    for path, kind in sorted(required.items()):
        full = product["subtree"] + "/" + path
        require(view.member_kind(full) == kind, "missing or wrong member kind: " + full)
        content = view.read_member_bytes(full, kind)
        row = {"type": kind, "path": path, "sha256": check.sha256(content)}
        if kind == "symlink":
            row["target"] = content.decode()
        members.append(row)
    return {"member_count": len(members), "member_set_sha256": check.product_member_stream(members),
            "members": members}


axiom = payload["products"]["axiom_indexer"]
rep = payload["products"]["stdo_representation"]
axiom["subject"] = inventory("axiom_indexer")
rep["subject"] = inventory("stdo_representation")
require(axiom["subject"] == prior["products"]["axiom_indexer"]["subject"], "Axiom Product changed")
require(rep["subject"]["member_count"] == 9, "Representation boundary changed")
payload["assets"]["spec_plugin"]["version"] = VERSION
payload["assets"]["stdo_semantic_index"].update(
    version=VERSION, root=f"stdo_representation/{ARTIFACT_ROOT}",
    release_member_paths=[f"{ARTIFACT_ROOT}/axiomatic-program.json", f"{ARTIFACT_ROOT}/logical-constraint-map.json"])


def table(subject):
    result = ["| Type | Member | SHA-256 |", "|---|---|---|"]
    for row in subject["members"]:
        path = f"`{row['path']}`"
        if row["type"] == "symlink":
            path += f" -> `{row['target']}`"
        result.append(f"| {row['type']} | {path} | `{row['sha256']}` |")
    return "\n".join(result)


def header(name, title):
    product = payload["products"][name]
    source_label = "matched Source STDO cut" if name == "axiom_indexer" else "matched Source STDO ref"
    return f"""# {title} 2.5.1 RC1

Status: locally prepared coordinated candidate. Publication, Product acceptance
and external consumer adoption remain separate. T-288 and ABI delivery are
outside this candidate's qualification scope.

| Coordinate | Value |
|---|---|
| release version | `{VERSION}` |
| product-local cut | `{CUT}` |
| Project Release Namespace | `{name}` |
| Project Subtree root | `{name}` |
| qualified immutable tag ref | `{product['release_ref']}` |
| qualified version-line selector | `{product['selector_ref']}` |
| qualified RC branch | `{product['rc_branch']}` |
| qualified release branch | `{product['release_branch']}` |
| {source_label} | `refs/tags/specification_methodology/{CUT}` |
| public Source STDO basis | `stdo://releases/{CUT}/` |

## Exact Source STDO

The source is commit `{freeze['commit']}`, annotated tag object
`{freeze['tag_object']}`, repository tree `{freeze['tree']}`,
STDO subtree tree `{freeze['project_subtree_tree']}` and standards tree
`{freeze['standards_tree']}`. Its installed manifest is
`{freeze['installed_manifest_sha256']}`. The complete
{freeze['standards_member_count']}-member standards aggregate is
`{freeze['standards_member_set_sha256']}`. The source release note and inventory
disposition every member against RC7. Manager 0.1.4 carries the existing install
closure repair; Axiom mechanics remain separate and unchanged.
Child tag and commit-B identities are bound externally by qualification.

## Exact Product Inventory

Exactly {product['subject']['member_count']} entries; file digests cover bytes,
symlink digests their UTF-8 targets without a terminal newline. The sorted stream
contains SHA-256, two spaces, type, two spaces, path and newline:
`{product['subject']['member_set_sha256']}`.

{table(product['subject'])}

Authority, Definitions/frame configuration, release notes and evidence remain
external to this Product member set. Exact records accompany the install
closure. Co-location does not create Product membership or acceptance.
"""


axiom_note = header("axiom_indexer", "Axiom Indexer") + f"""
## Claims And Predecessor Dispositions

The published predecessor is `axiom_indexer/v2.5.0-rc.7`, annotated tag
`95c5c4d268f7a5969a0d79d6384b47044788d346`, commit `{OLD_B}`.
Its seven Product members and aggregate are byte-conserved.

- `AXIOM-2.5.1-RC1-C01` conserves RC7 C01: explicit authored frame-index closure
  and both views preserve identities, qualifications, residuals and source routes.
- `AXIOM-2.5.1-RC1-C02` conserves RC7 C02: declared missing, stale, ambiguous,
  aliased and unresolved-link refusals retain their source/output protection.
- `AXIOM-2.5.1-RC1-C03` conserves RC7 C03: validation, projection and caller-ordered
  joining introduce no semantic inference, applicability decision or executor.
- `AXIOM-2.5.1-RC1-C04` supersedes RC7 C04's exact cohort coordinates with RC1.
  Representation owns its newly authored method clauses and indexes.

Verified unchanged evidence retains its original claims and observed runtime
limits. Reproduction over the new source/program binds the affected relation;
it supplies no semantic or native-use verdict by itself.

The [RC1 preparation record](../../specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md)
binds exact checks and dispositions. Historical cut acceptance is not successor
acceptance. No publication or public reacquisition is claimed here.
"""
mechanics = [{"role": role, "path": path, "sha256": sha("axiom_indexer/" + path)} for role, path in (
    ("executable", "build_tenants/core/code/ac.py"),
    ("output_contract", "skills/axiomatize-corpus/references/output-contract.md"),
    ("schema", "skills/axiomatize-corpus/references/program.schema.json"))]
dependency = {"version": VERSION, "release_ref": axiom["release_ref"],
              "product_member_count": axiom["subject"]["member_count"],
              "product_member_set_sha256": axiom["subject"]["member_set_sha256"],
              "release_record": {"path": axiom["release_note"], "sha256": check.sha256(axiom_note.encode())},
              "mechanics": mechanics}
rep["dependencies"]["axiom_indexer"] = dependency
mechanical_rows = "\n".join(f"| {r['role']} | `{r['path']}` | `{r['sha256']}` |" for r in mechanics)
asset_rows = "\n".join(f"| `{ARTIFACT_ROOT}/{name}` | `{sha('stdo_representation/' + ARTIFACT_ROOT + '/' + name)}` |"
                       for name in ("source-corpus.json", "axiomatic-program.json", "logical-constraint-map.json", "validation-report.json"))
program = view.read_json(f"stdo_representation/{ARTIFACT_ROOT}/axiomatic-program.json")
rep_note = header("stdo_representation", "STDO Representation") + f"""
## Exact Dependency And Generated Assets

| exact Axiom dependency | `{axiom['release_ref']}` |

Axiom version `{VERSION}` has {dependency['product_member_count']} members and
aggregate `{dependency['product_member_set_sha256']}`. Its external release
record `{dependency['release_record']['path']}` has digest
`{dependency['release_record']['sha256']}`.

| Role | Axiom member | SHA-256 |
|---|---|---|
{mechanical_rows}

| Representation artifact / external source evidence | SHA-256 |
|---|---|
{asset_rows}

## Claims And Predecessor Dispositions

The published predecessor is `stdo_representation/v2.5.0-rc.7`, annotated tag
`a010992bd0b403c032f68df9496386bb06bbfa65`, commit `{OLD_B}`, aggregate
`cd42f90929ebaf6b4f7d8d983bffcb729ee38f173ca5cfb0d74a9be4f08feb26`.

- `STDO-REP-2.5.1-RC1-C01` refines RC7 C01 with source-grounded reuse/invalidators,
  computational-path evaluation, supported operational and threat assumptions,
  retention burden, compression fidelity and work continuity. Changed meanings
  are authored; digest rebinding alone supplies no semantic qualification.
- `STDO-REP-2.5.1-RC1-C02` refines RC7 C02 with accepted T-031's interface frame
  and affected explicit frame membership/support. Its four claim classes and
  conditional applicability remain distinct. Axiom's generic mechanics are
  unchanged and reproduce both views of the authored indexes.
- `STDO-REP-2.5.1-RC1-C03` conserves RC7 C03's native interface, updating exact
  routes and qualifying the changed guidance in fresh Codex/Claude source/map
  contexts. Native decisions qualify observed use only, never fixture counts,
  effects or refusal behavior owned by executable checks.
- `STDO-REP-2.5.1-RC1-C04` supersedes RC7 C04's cohort identity with RC1. Exact
  source/dependency closure and separately owned acceptance remain mandatory.

The candidate contains {len(program['clauses'])} clauses and
{len(program.get('frame_indexes', []))} explicit frame indexes. Its source record
binds the complete {freeze['standards_member_count']}-member exact Install.
The [RC1 preparation record](../../specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md)
retains conservation/semantic assessment, mechanical reproduction and negatives,
actual native results and limitations, internal configuration and cohort checks.
Their claims remain distinct; source or map presence closes none by itself.

No automatic frame selection, semantic grader, universal operational bound,
general native reliability or ABI delivery outcome is claimed. Immutable
predecessor results remain bounded by their original subjects. This candidate
record does not publish or accept a Product or adopt it in external consumers.
"""

# Pin the literal endpoint and read every destination/version-line ref at once.
for endpoint_args in (("remote", "get-url", "origin"), ("remote", "get-url", "--push", "origin")):
    actual = subprocess.check_output(["git", *endpoint_args], cwd=ROOT, text=True).strip()
    require(actual == URL, "configured repository endpoint mismatch")
raw = subprocess.check_output(["git", "ls-remote", URL], cwd=ROOT, text=True)
remote = {line.split("\t")[1]: line.split("\t")[0] for line in raw.splitlines()}
destinations = {"refs/heads/main"}
for product in payload["products"].values():
    destinations.update(product[k] for k in ("release_ref", "selector_ref", "rc_branch", "release_branch"))
require(remote.get("refs/heads/main"), "remote main is absent")
require(all(remote.get(ref) is None for ref in destinations - {"refs/heads/main"}),
        "a selected first-line destination already exists; preserve and reprice")
for name in payload["products"]:
    require(not any(ref.startswith(f"refs/tags/{name}/v{LINE}-rc.") for ref in remote),
            "same-line immutable cut exists: " + name)
require(not any(ref.startswith(f"refs/tags/v{LINE}-rc.") for ref in remote),
        "historical unqualified same-line cut exists")
histories = {name: [] for name in payload["products"]}
publication = {"repository_url": URL,
               "expected_remote": {ref: remote.get(ref) for ref in sorted(destinations)},
               "expected_version_lines": histories,
               "expected_version_lines_sha256": check.canonical_value_sha256({"repository_url": URL, "version_lines": histories})}
payload["publication"] = publication
def record(name):
    path = Path(name)
    return OUT / (path.stem + args.record_suffix + path.suffix)


put(record("remote-expectations.json"), {"status": "satisfied", "failures": [], **publication})
for relative, candidate, content in (
    (axiom["release_note"], "axiom-release-note.candidate.md", axiom_note),
    (rep["release_note"], "representation-release-note.candidate.md", rep_note)):
    record(candidate).write_text(content)
    (ROOT / relative).write_text(content)
put(record("stack-release.candidate.json"), payload)
put(ROOT / "stack_release.json", payload)
put(record("cohort-subject.json"), {"status": "candidate", "source_freeze": freeze,
    "axiom_subject": axiom["subject"], "representation_subject": rep["subject"],
    "companion_review_sha256": check.sha256(args.review.read_bytes()),
    "outputs": {p: sha(p) for p in ("stack_release.json", axiom["release_note"], rep["release_note"])},
    "limits": "Prepared content only. Content/ref results and publication remain separately recorded."})
print(json.dumps({"status": "candidate", "source_manifest": installed["manifest_sha256"],
                  "axiom_members": axiom["subject"]["member_count"],
                  "representation_members": rep["subject"]["member_count"]}))
