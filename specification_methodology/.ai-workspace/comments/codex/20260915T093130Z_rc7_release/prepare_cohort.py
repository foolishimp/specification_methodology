"""Prepare RC7 cohort records from held child bytes and frozen remote expectations."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
VERSION = "2.5.0-rc.7"
CUT = "v" + VERSION
OLD_B = "adb25a35acad363823b4c0d05fecbf9a2f20d25d"
ARTIFACT_ROOT = f"build_tenants/axiom_indexer/representation/stdo-{CUT}"
spec = importlib.util.spec_from_file_location("rc7_cohort_checker", ROOT / "scripts/check_stack_release.py")
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)
view = check.View(ROOT)
old_view = check.View(ROOT, OLD_B)


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def sha(relative):
    return check.sha256(view.read_bytes(relative))


def put(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


held = {
    f"stdo_representation/{ARTIFACT_ROOT}/axiomatic-program.json": "d1bd16268cf434db984c9e6c3ebfd119110f9de211dbe69b952794cf9f13dc68",
    f"stdo_representation/{ARTIFACT_ROOT}/logical-constraint-map.json": "d0685a7548812610cda9aa9369f423e2d9944f194a5cd5c5b61e92c374b675af",
    f"stdo_representation/{ARTIFACT_ROOT}/source-corpus.json": "97ec14964df30f3d9203a052aa03170c65ce599d0dd6a0ed110dcd6282b28582",
    f"stdo_representation/{ARTIFACT_ROOT}/validation-report.json": "8330717085c0a4072aed5f0c26978691b16f6ea65d6da633b7fdd20863ee74cf",
    "stdo_representation/skills/stdo-representation/SKILL.md": "d58d79380411f5c9980bc369e4bbe6255b72af7a908832a27b0bafae67f8c49d",
    "stdo_representation/skills/stdo-representation/references/frame-index-use.md": "3e7274395b1ea085e0397ab684f6ce7caba5524e39bb8c4a234dcc0272ade3ed",
}
for path, expected in held.items():
    require(sha(path) == expected, "held child source drift: " + path)
payload = old_view.read_json("stack_release.json")
prior = old_view.read_json("stack_release.json")
payload["cohort"].update(version=VERSION, cut=CUT, status="candidate")
for name, product in payload["products"].items():
    product.update(version=VERSION, release_ref=f"refs/tags/{name}/{CUT}")
    product["release_note_markers"] = [m.replace("2.5.0-rc.6", VERSION) for m in product["release_note_markers"]]
installed = json.loads((OUT / "stdo-install.json").read_text())
verified = json.loads((OUT / "stdo-verify.json").read_text())
require(verified["valid"] and not verified["failures"], "RC7 Install is not verified")
require(installed["manifest_sha256"] == verified["manifest_sha256"] ==
        "1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae", "Install identity drift")
source_inventory = json.loads((OUT / "source-inventory.json").read_text())
freeze = {key: installed["release"][key] for key in
          ("tag_object", "commit", "tree", "project_subtree_tree", "standards_tree")}
require(check.local_tag_identity(ROOT, payload["products"]["specification_methodology"]["release_ref"],
                                 "specification_methodology") == freeze, "local source tag drift")
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
prior_axiom = {m['path']: m for m in prior['products']['axiom_indexer']['subject']['members']}
changed_axiom = [m for m in axiom['subject']['members'] if m != prior_axiom[m['path']]]
require(len(changed_axiom) == 1 and changed_axiom[0]['path'] == 'build_tenants/core/code/ac.py' and
        changed_axiom[0]['sha256'] == '5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8',
        'Axiom change exceeds the bounded loop/output-preservation repair')
require(rep["subject"]["member_count"] == 9, "Representation member boundary drift")
for row in rep["subject"]["members"]:
    full = "stdo_representation/" + row["path"]
    if full not in held:
        require(check.sha256(old_view.read_member_bytes(full, row["type"])) == row["sha256"],
                "unselected native member change: " + full)
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
    return f"""# {title} 2.5.0 RC7

This record declares the exact coordinated candidate. It does not supply
publication, Product acceptance or consumer adoption by its own existence.

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

The matched source is commit `{freeze['commit']}`, annotated tag object
`{freeze['tag_object']}`, repository tree `{freeze['tree']}`,
STDO subtree tree `{freeze['project_subtree_tree']}` and standards tree
`{freeze['standards_tree']}`. Its installed manifest is
`{freeze['installed_manifest_sha256']}`. Exactly
{freeze['standards_member_count']} standards members have aggregate
`{freeze['standards_member_set_sha256']}`. Three reviewed standards/projections
change from RC6; the remaining 49 and manager 0.1.3 are byte-conserved.
The future child tag, carrier and subtree identities are bound externally by
qualification; this note cannot embed its own future identity.

## Exact Product Inventory

Exactly {product['subject']['member_count']} entries. File digests cover bytes;
symlink digests cover UTF-8 targets without a terminal newline. The aggregate
sorts paths and emits SHA-256, two spaces, type, two spaces, path and newline:
`{product['subject']['member_set_sha256']}`.

{table(product['subject'])}

Authority documents, release records, source-project Definitions/frame
configuration and proof remain external to this Product member set. Their
exact dependency and cohort records remain available for installation checks;
co-location does not make a mutable checkout Product truth.
"""


axiom_note = header("axiom_indexer", "Axiom Indexer") + """
## Selected Claims And Predecessor Dispositions

The exact published predecessor is `axiom_indexer/v2.5.0-rc.6`, annotated tag
`b75e25b4f1d34e405dbfb240ef8a148530bdecb4`, commit
`adb25a35acad363823b4c0d05fecbf9a2f20d25d`. Its seven-member aggregate is
`41350ccf7b10173f36cab011cb85e9c0b552c9af6d6efe2f2f2782125df00c19`.

- `AXIOM-2.5-RC7-C01`: RC6 C01 is conserved: explicit authored frame-index
  dependency closure and both views preserve identity, qualifications,
  residuals, source routes and unchanged materialized content.
- `AXIOM-2.5-RC7-C02`: RC6 C02 is conserved: declared missing, stale, ambiguous
  and aliased input refusals retain the exact source-protection contract.
  A bounded executable correction restores unresolved-symlink-loop output
  preservation on observed Python 3.13.7 as well as Python 3.12.8; six Product
  members remain byte-conserved and the test carrier adds both-view checks.
- `AXIOM-2.5-RC7-C03`: RC6 C03 is conserved: resolution, validation and pure
  caller-ordered joining introduce no semantic inference, frame selection or
  executor.
- `AXIOM-2.5-RC7-C04`: RC6 C04's exact dependency-cut identity is superseded
  by RC7; the mechanics remain separately owned with only that bounded repair while
  Representation consumes them for the matched RC7 source.

Prior claim and acceptance dispositions remain at their immutable subjects.
The event-driven Executive clauses/index are Representation's authored input,
not an Axiom semantic feature. Historical 31 normal/optimized mechanical cases
and source-protection review retain their original scope; the newly observed
Python 3.13.7 output-deletion failure and its repair remain in the RC7 evidence.
Normal and optimized checks on Python 3.12.8 and 3.13.7, final RC7 checks and installed
use are bound by the shared release evidence. No mechanical count supplies
semantic or native qualification. No new licence, automatic judgment, prompt
orchestration, complete admitted M_b, GTL or runtime is selected.

The [RC7 release carrier](../../specification_methodology/.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
owns the exact affected results. Publication follows the complete content,
local-ref and remote gates; exact-cut Product acceptance remains separate.
"""
(OUT / "axiom-release-note.candidate.md").write_text(axiom_note)
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
rep_note = header("stdo_representation", "STDO Representation") + f"""
## Exact Dependency And Generated Assets

| exact Axiom dependency | `{axiom['release_ref']}` |

Axiom version `{VERSION}` has {dependency['product_member_count']} members,
aggregate `{dependency['product_member_set_sha256']}`. Its external release
record `{dependency['release_record']['path']}` has SHA-256
`{dependency['release_record']['sha256']}`.

| Role | Axiom member | SHA-256 |
|---|---|---|
{mechanical_rows}

| Representation artifact / external source evidence | SHA-256 |
|---|---|
{asset_rows}

## Selected Claims And Predecessor Dispositions

The exact published predecessor is `stdo_representation/v2.5.0-rc.6`,
annotated tag `9dffb7161e97d040b83ec4863826d3c32cf12ddd`, commit
`adb25a35acad363823b4c0d05fecbf9a2f20d25d`, nine-member aggregate
`9cb7a9b8901f303ce69011c4f7ba551e101712c2a8e03010eac2aa1dbf9ceb8b`.

- `STDO-REP-2.5-RC7-C01`: RC6 C01 is superseded only by exact RC7 source
  rebinding and three authored event-driven Executive constraints. The 98 prior
  statements and all residuals are conserved; only the steel-thread clause's
  supporting closure gains the attention rule. The other 97 complete clauses
  are conserved modulo source URI/program-identity translation.
- `STDO-REP-2.5-RC7-C02`: RC6 C02 is conserved and extended by one explicit
  event-driven Executive index. All three preceding index declarations are
  conserved; the steel-thread view gains its declared attention support. The
  exact repaired Axiom mechanics reproduce the unchanged map and both views of
  all four indexes; only the demonstrated loop/refusal path changes.
- `STDO-REP-2.5-RC7-C03`: RC6 C03's native interface is conserved, with
  selection routes rebound to the exact RC7 package. The new Executive path
  requires its own bounded fresh source/map qualification on Codex and Claude;
  prior native observations do not supply that result.
- `STDO-REP-2.5-RC7-C04`: RC6 C04's exact cohort identity is superseded by
  RC7. Complete source/member/dependency closure and installed-path requirements
  are conserved and checked against the successor.

Earlier predecessor claim and acceptance dispositions remain unchanged history.
The changed member bytes are the program, map and two native selection-route
files. The remaining five members are byte-conserved. Source-project
continuation bindings are separately owned and are not new Product members.

## Qualification Boundary

The candidate has 101 clauses and four explicit frame indexes. Source
conservation compares 97 whole prior clauses, all 98 prior statements and all
three preceding indexes by inverse source rebinding, then separately evaluates
the three attention rules, their condition/exception/support closure and the
steel-thread support bridge against the exact RC7 owner. Mechanical regeneration
retains both views of every index and the overlapping update pair.
The source-corpus record binds all 52 installed RC7 standards members.

The [RC7 release carrier](../../specification_methodology/.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
binds the exact semantic review, mechanical checks, four fresh source/map
native contexts and subsequent installed/cohort results. Those results remain
outside these self-reference-sensitive note bytes. Source, mechanical, native,
installed and publication evidence retain their distinct claims.

Conserved RC6 evidence remains bounded by its original inputs and observed
tasks. Failed attempts, blocked 10A/B preparations, unnecessary index use and
historical Claude FP04 prospective overreach remain visible. No repeated-J or
universal LLM reliability, minimal interaction/cost advantage, new accounting
rule, automatic frame selection, semantic decision or executor is claimed.
Publication requires the exact content/ref/remote gates and the affected
qualified outcomes; Product acceptance and real consumer adoption are separate.
"""
(OUT / "representation-release-note.candidate.md").write_text(rep_note)
remote = json.loads((OUT / "remote-expectations.json").read_text())
require(remote["status"] == "satisfied" and not remote["failures"], "remote snapshot is not qualified")
payload["publication"] = {key: remote[key] for key in
                          ("repository_url", "expected_remote", "expected_version_lines", "expected_version_lines_sha256")}
put(OUT / "stack-release.candidate.json", payload)
result = {"kind": "stdo.rc7-cohort-preparation", "status": "candidate_ready",
          "source_freeze": freeze, "axiom_subject": axiom["subject"], "representation_subject": rep["subject"],
          "held_child_inputs": held, "remote_expectations_sha256": check.sha256((OUT / "remote-expectations.json").read_bytes()),
          "outputs": [{"path": path, "candidate": candidate, "sha256": check.sha256((OUT / candidate).read_bytes())}
                      for path, candidate in (("stack_release.json", "stack-release.candidate.json"),
                      (axiom["release_note"], "axiom-release-note.candidate.md"),
                      (rep["release_note"], "representation-release-note.candidate.md"))],
          "qualification": "Prepared content only; independent/native/installed/ref/publication results remain separate."}
put(OUT / "cohort-subject.json", result)
print(json.dumps({"status": "candidate_ready", "axiom_members": 7, "representation_members": 9,
                  "axiom_aggregate": axiom["subject"]["member_set_sha256"],
                  "representation_aggregate": rep["subject"]["member_set_sha256"],
                  "outputs": result["outputs"]}))
