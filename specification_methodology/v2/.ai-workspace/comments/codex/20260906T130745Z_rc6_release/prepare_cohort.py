"""Prepare RC6 cohort records from held child bytes and frozen remote expectations."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
VERSION = "2.5.0-rc.6"
CUT = "v" + VERSION
OLD_B = "4560b4ec1ac18f7ff3dab09c5ca4e7629d467a94"
ARTIFACT_ROOT = f"build_tenants/axiom_indexer/representation/stdo-{CUT}"
spec = importlib.util.spec_from_file_location("rc6_cohort_checker", ROOT / "scripts/check_stack_release.py")
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
    f"stdo_representation/{ARTIFACT_ROOT}/axiomatic-program.json": "ea68d04a125e7a7035759b69dba063cd86dd72c0438254c7fabfee8134f0fc9e",
    f"stdo_representation/{ARTIFACT_ROOT}/logical-constraint-map.json": "7c2369251fbb6a480b25bafa8a2042c95114ac9df673364f5841c2c55f37137e",
    f"stdo_representation/{ARTIFACT_ROOT}/source-corpus.json": "d79c4d97336c062ad58a677b3c304acfc218b30d5040ee723170243ca9ef2efb",
    f"stdo_representation/{ARTIFACT_ROOT}/validation-report.json": "d83573388b24d0cdd5c2ac7ccd61610c64c4693cbd45b69fb04a08ccdb26245a",
    "stdo_representation/skills/stdo-representation/SKILL.md": "424785112fb70e9f0c0c484a2a074d6ecfd8f9478f33a6960b7ca86968c3828d",
    "stdo_representation/skills/stdo-representation/references/frame-index-use.md": "0e5ed60300e4355856df04b46760944827b77329f80d40600a4ebf014dc950c0",
}
for path, expected in held.items():
    require(sha(path) == expected, "held child source drift: " + path)
payload = old_view.read_json("stack_release.json")
prior = old_view.read_json("stack_release.json")
payload["cohort"].update(version=VERSION, cut=CUT, status="candidate")
for name, product in payload["products"].items():
    product.update(version=VERSION, release_ref=f"refs/tags/{name}/{CUT}")
    product["release_note_markers"] = [m.replace("2.5.0-rc.5", VERSION) for m in product["release_note_markers"]]
installed = json.loads((OUT / "stdo-install.json").read_text())
verified = json.loads((OUT / "stdo-verify.json").read_text())
require(verified["valid"] and not verified["failures"], "RC6 Install is not verified")
require(installed["manifest_sha256"] == verified["manifest_sha256"] ==
        "bed7535a5feddc5e874993ff96d1f5f27e2a0fff63f366fc3b1fec3e301dd9e0", "Install identity drift")
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
require(axiom["subject"] == prior["products"]["axiom_indexer"]["subject"], "Axiom member drift")
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
    return f"""# {title} 2.5.0 RC6

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
change from RC5; the remaining 49 and manager 0.1.3 are byte-conserved.
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

The exact published predecessor is `axiom_indexer/v2.5.0-rc.5`, annotated tag
`7813c9555ddde8f649d70870dc6ab9dabdd1d80c`, commit
`4560b4ec1ac18f7ff3dab09c5ca4e7629d467a94`. Its seven Product members are
byte-conserved, aggregate
`41350ccf7b10173f36cab011cb85e9c0b552c9af6d6efe2f2f2782125df00c19`.

- `AXIOM-2.5-RC6-C01`: RC5 C01 is conserved: explicit authored frame-index
  dependency closure and both views preserve identity, qualifications,
  residuals, source routes and unchanged materialized content.
- `AXIOM-2.5-RC6-C02`: RC5 C02 is conserved: declared missing, stale, ambiguous
  and aliased input refusals retain the exact source-protection contract.
- `AXIOM-2.5-RC6-C03`: RC5 C03 is conserved: resolution, validation and pure
  caller-ordered joining introduce no semantic inference, frame selection or
  executor.
- `AXIOM-2.5-RC6-C04`: RC5 C04's exact dependency-cut identity is superseded
  by RC6; the mechanics remain separately owned and byte-identical while
  Representation consumes them for the matched RC6 source.

Prior claim and acceptance dispositions remain at their immutable subjects.
The new Executive clause/index is Representation's authored input, not new
Axiom behavior. Historical 31 normal/optimized mechanical cases and source
protection review retain their original scope; final RC6 checks and installed
use are bound by the shared release evidence. No mechanical count supplies
semantic or native qualification. No new licence, automatic judgment, prompt
orchestration, complete admitted M_b, GTL or runtime is selected.

The [RC6 release carrier](../../specification_methodology/.ai-workspace/comments/codex/20260906T130745Z_rc6_release/README.md)
owns the exact affected results. Publication follows the complete content,
local-ref and remote gates; exact-cut Product acceptance remains separate.
"""
(ROOT / axiom["release_note"]).write_text(axiom_note)
mechanics = [{"role": role, "path": path, "sha256": sha("axiom_indexer/" + path)} for role, path in (
    ("executable", "build_tenants/core/code/ac.py"),
    ("output_contract", "skills/axiomatize-corpus/references/output-contract.md"),
    ("schema", "skills/axiomatize-corpus/references/program.schema.json"))]
dependency = {"version": VERSION, "release_ref": axiom["release_ref"],
              "product_member_count": axiom["subject"]["member_count"],
              "product_member_set_sha256": axiom["subject"]["member_set_sha256"],
              "release_record": {"path": axiom["release_note"], "sha256": sha(axiom["release_note"])},
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

The exact published predecessor is `stdo_representation/v2.5.0-rc.5`,
annotated tag `5edeb22233fb9625fbf3b386a2fb1e2f8f88fead`, commit
`4560b4ec1ac18f7ff3dab09c5ca4e7629d467a94`, nine-member aggregate
`5a73c04c7f704d3ce9dc051ba1214bf4a177305daf59eb4800b51429853ac1e2`.

- `STDO-REP-2.5-RC6-C01`: RC5 C01 is superseded only by exact RC6 source
  rebinding and one authored Executive steel-thread constraint. The prior 97
  clauses, supporting relations and explicit residuals are conserved modulo
  that source URI/program-identity translation.
- `STDO-REP-2.5-RC6-C02`: RC5 C02 is conserved and extended by one explicit
  Executive index. The original two update indexes are conserved; the same
  Axiom mechanics reproduce the map and both views of the three indexes.
- `STDO-REP-2.5-RC6-C03`: RC5 C03's native interface is conserved, with
  selection routes rebound to the exact RC6 package. The new Executive path
  requires its own bounded fresh source/map qualification on Codex and Claude;
  prior native observations do not supply that result.
- `STDO-REP-2.5-RC6-C04`: RC5 C04's exact cohort identity is superseded by
  RC6. Complete source/member/dependency closure and installed-path requirements
  are conserved and checked against the successor.

Earlier predecessor claim and acceptance dispositions remain unchanged history.
The changed member bytes are the program, map and two native selection-route
files. The remaining five members are byte-conserved. Source-project
continuation bindings are separately owned and are not new Product members.

## Qualification Boundary

The candidate has 98 clauses and three explicit frame indexes. Source
conservation compares the prior 97 clauses and two indexes by inverse source
rebinding, and separately evaluates the new Executive clause/index against its
exact source owner. Mechanical regeneration retains both views of every index.
The source-corpus record binds all 52 installed RC6 standards members.

The [RC6 release carrier](../../specification_methodology/.ai-workspace/comments/codex/20260906T130745Z_rc6_release/README.md)
binds the exact semantic review, mechanical checks, four fresh source/map
native contexts and subsequent installed/cohort results. Those results remain
outside these self-reference-sensitive note bytes. Source, mechanical, native,
installed and publication evidence retain their distinct claims.

Conserved RC5 evidence remains bounded by its original inputs and observed
tasks. Failed attempts, blocked 10A/B preparations, unnecessary index use and
historical Claude FP04 prospective overreach remain visible. No repeated-J or
universal LLM reliability, minimal interaction/cost advantage, new accounting
rule, automatic frame selection, semantic decision or executor is claimed.
Publication requires the exact content/ref/remote gates and the affected
qualified outcomes; Product acceptance and real consumer adoption are separate.
"""
(ROOT / rep["release_note"]).write_text(rep_note)
remote = json.loads((OUT / "remote-expectations.json").read_text())
require(remote["status"] == "satisfied" and not remote["failures"], "remote snapshot is not qualified")
payload["publication"] = {key: remote[key] for key in
                          ("repository_url", "expected_remote", "expected_version_lines", "expected_version_lines_sha256")}
put(ROOT / "stack_release.json", payload)
result = {"kind": "stdo.rc6-cohort-preparation", "status": "candidate_ready",
          "source_freeze": freeze, "axiom_subject": axiom["subject"], "representation_subject": rep["subject"],
          "held_child_inputs": held, "remote_expectations_sha256": check.sha256((OUT / "remote-expectations.json").read_bytes()),
          "outputs": [{"path": p, "sha256": sha(p)} for p in
                      ("stack_release.json", axiom["release_note"], rep["release_note"])],
          "qualification": "Prepared content only; independent/native/installed/ref/publication results remain separate."}
put(OUT / "cohort-subject.json", result)
print(json.dumps({"status": "candidate_ready", "axiom_members": 7, "representation_members": 9,
                  "axiom_aggregate": axiom["subject"]["member_set_sha256"],
                  "representation_aggregate": rep["subject"]["member_set_sha256"],
                  "outputs": result["outputs"]}))
