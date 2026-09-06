"""Construct the selected RC5 cohort carrier and exact child release records."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
PROOF = Path(__file__).resolve().parent
VERSION = "2.5.0-rc.5"
CUT = "v" + VERSION
URL = "https://github.com/foolishimp/specification_methodology.git"
spec = importlib.util.spec_from_file_location("rc5_shared_checker", ROOT / "scripts/check_stack_release.py")
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def put(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def inventory(product, skill, artifacts):
    base = ROOT / product
    paths = [f".agents/skills/{skill}", f".claude/skills/{skill}", *artifacts]
    paths += [p.relative_to(base).as_posix() for p in sorted((base / "skills" / skill).rglob("*")) if p.is_file()]
    result = []
    for name in sorted(set(paths)):
        path = base / name
        row = {"type": "symlink" if path.is_symlink() else "file", "path": name}
        if path.is_symlink():
            row["target"] = os.readlink(path)
            row["sha256"] = hashlib.sha256(row["target"].encode()).hexdigest()
        else:
            row["sha256"] = sha(path)
        result.append(row)
    return {"member_count": len(result), "member_set_sha256": check.product_member_stream(result), "members": result}


def member_table(subject):
    rows = ["| Type | Member | SHA-256 |", "|---|---|---|"]
    for member in subject["members"]:
        name = f"`{member['path']}`"
        if member["type"] == "symlink":
            name += f" -> `{member['target']}`"
        rows.append(f"| {member['type']} | {name} | `{member['sha256']}` |")
    return "\n".join(rows)


payload = json.loads(subprocess.check_output(["git", "show", "a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2:stack_release.json"], cwd=ROOT))
payload["cohort"].update(version=VERSION, cut=CUT, status="candidate")
for name, product in payload["products"].items():
    product["version"] = VERSION
    product["release_ref"] = f"refs/tags/{name}/{CUT}"
    product["release_note_markers"] = [x.replace("2.5.0-rc.4", VERSION) for x in product["release_note_markers"]]

installed = json.loads((PROOF / "stdo-install.json").read_text())
source_inventory = json.loads((PROOF / "source-inventory.json").read_text())
freeze = {k: installed["release"][k] for k in ("tag_object", "commit", "tree", "project_subtree_tree", "standards_tree")}
freeze.update(installed_manifest_sha256=installed["manifest_sha256"], standards_member_count=52,
    standards_member_set_sha256=installed["standards"]["member_set_sha256"], plugin_member_count=17,
    plugin_member_set_sha256=source_inventory["plugin_member_set_sha256"])
payload["products"]["specification_methodology"]["freeze"] = freeze
axiom = payload["products"]["axiom_indexer"]
rep = payload["products"]["stdo_representation"]
artifact_root = f"build_tenants/axiom_indexer/representation/stdo-{CUT}"
axiom["subject"] = inventory("axiom_indexer", "axiomatize-corpus", ["build_tenants/core/code/ac.py"])
rep["subject"] = inventory("stdo_representation", "stdo-representation", [f"{artifact_root}/axiomatic-program.json", f"{artifact_root}/logical-constraint-map.json"])
assert axiom["subject"]["member_count"] == 7
assert rep["subject"]["member_count"] == 9
payload["assets"]["spec_plugin"]["version"] = VERSION
asset = payload["assets"]["stdo_semantic_index"]
asset.update(version=VERSION, root=f"stdo_representation/{artifact_root}", release_member_paths=[f"{artifact_root}/axiomatic-program.json", f"{artifact_root}/logical-constraint-map.json"])


def header(name, title):
    product = payload["products"][name]
    extra = "| matched Source STDO cut |" if name == "axiom_indexer" else "| matched Source STDO ref |"
    return f"""# {title} 2.5.0 RC5

This record declares the exact coordinated candidate. It does not assert
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
{extra} `refs/tags/specification_methodology/{CUT}` |
| public Source STDO basis | `stdo://releases/{CUT}/` |

## Exact Source STDO

The matched source is commit `{freeze['commit']}`, annotated tag object
`{freeze['tag_object']}`, repository tree `{freeze['tree']}`, STDO subtree tree
`{freeze['project_subtree_tree']}`, standards tree `{freeze['standards_tree']}`.
Its installed manifest is `{freeze['installed_manifest_sha256']}`;
{freeze['standards_member_count']} standards members have aggregate
`{freeze['standards_member_set_sha256']}`. The child tag object, carrier commit
and subtree identity are frozen externally by the release qualification;
this note cannot self-embed those future identities.

## Exact Product Inventory

Exactly {product['subject']['member_count']} entries. File digests cover bytes;
symlink digests cover their UTF-8 targets without a terminal newline. The
aggregate sorts paths and emits SHA-256, two spaces, type, two spaces, path,
newline: `{product['subject']['member_set_sha256']}`.

{member_table(product['subject'])}

Authority documents, release metadata, bindings and proof remain external to
this Product member set. Installation retains the exact external dependency
and cohort records needed to verify these members; it does not copy a mutable
checkout as Product truth.
"""


axiom_note = header("axiom_indexer", "Axiom Indexer") + """
## Selected Claims And Predecessor Dispositions

The immediate published predecessor is `axiom_indexer/v2.5.0-rc.4`, tag
`4750e09639c118f1097d4ea046fe23d26713f96b`, commit
`a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2`. Its exact record remains at that tag;
the accepted v0.1.0 RC1 baseline and its acceptance remain unchanged history.

- `AXIOM-2.5-RC5-C01`: explicitly authored frame indexes select declared
  dependency closure; both views preserve identities, qualifications,
  residual uncertainty and source routes, with unchanged materialized content.
- `AXIOM-2.5-RC5-C02`: missing, stale, ambiguous or aliased inputs produce
  deterministic diagnostics without unsafe output effects.
- `AXIOM-2.5-RC5-C03`: original resolution, validation and exact text joining
  remain available; no semantic inference, applicability decision or executor
  is introduced.
- `AXIOM-2.5-RC5-C04`: exact RC5 mechanics and native authoring contracts form
  the separately owned dependency consumed by STDO Representation RC5.

RC4 C01 and C05 are **conserved**, with the successor's exact suffix. C02's
seven-member byte-conservation claim is **superseded** by the selected new
projection capability and the inventory above. C03/C04 retain their bounded
original behavior and are **superseded** only for the explicitly added optional
frame-index authoring/projection interface. RC1's earlier functional claims,
pure-join law and exclusions remain **conserved** through those relations.

The exact mechanics passed 31 normal and 31 optimized regression cases and
independent assessment in `dogfood/t009-frame-projection/run-002/`. Release
qualification rechecks member conservation and the installed consumer path;
test counts supply no semantic qualification. No complete admitted M_b, GTL,
automatic frame selection, semantic acceptance, prompt orchestration or runtime
is claimed. No new open-source licence is selected by this release.

Publication follows the exact shared cohort content/ref/remote gates.
Product acceptance remains a separate exact-cut owner judgment.
"""
(ROOT / axiom["release_note"]).write_text(axiom_note)
mechanics = [{"role": role, "path": path, "sha256": sha(ROOT / "axiom_indexer" / path)} for role, path in [
    ("executable", "build_tenants/core/code/ac.py"), ("output_contract", "skills/axiomatize-corpus/references/output-contract.md"), ("schema", "skills/axiomatize-corpus/references/program.schema.json")]]
dependency = {"version": VERSION, "release_ref": axiom["release_ref"], "product_member_count": axiom["subject"]["member_count"], "product_member_set_sha256": axiom["subject"]["member_set_sha256"],
    "release_record": {"path": axiom["release_note"], "sha256": sha(ROOT / axiom["release_note"])}, "mechanics": mechanics}
rep["dependencies"]["axiom_indexer"] = dependency
aux = "\n".join(f"| `{artifact_root}/{name}` | `{sha(ROOT / 'stdo_representation' / artifact_root / name)}` |" for name in ["source-corpus.json", "axiomatic-program.json", "logical-constraint-map.json", "validation-report.json"])
mech_rows = "\n".join(f"| {r['role']} | `{r['path']}` | `{r['sha256']}` |" for r in mechanics)
rep_note = header("stdo_representation", "STDO Representation") + f"""
## Exact Dependency And Generated Assets

| exact Axiom dependency | `{axiom['release_ref']}` |

Axiom version `{VERSION}`, {dependency['product_member_count']} members,
aggregate `{dependency['product_member_set_sha256']}`. Its exact external
release record `{dependency['release_record']['path']}` has SHA-256
`{dependency['release_record']['sha256']}`.

| Role | Axiom member | SHA-256 |
|---|---|---|
{mech_rows}

| Representation artifact / external source evidence | SHA-256 |
|---|---|
{aux}

## Selected Claims And Predecessor Dispositions

The immediate published predecessor is `stdo_representation/v2.5.0-rc.4`,
tag `d85d25482f9d9132147bea189b0fe0aca1929dff`, commit
`a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2`. Its record and the accepted
Representation RC1 baseline remain at their immutable identities.

- `STDO-REP-2.5-RC5-C01`: one LLM-authored source-linked program represents
  the selected RC5 source, preserving uncertainty and exact source re-entry.
- `STDO-REP-2.5-RC5-C02`: the exact Axiom dependency reproduces the map and
  both projection views over two overlapping explicitly authored update frames,
  retaining supporting premises, conditions, exceptions and residuals.
- `STDO-REP-2.5-RC5-C03`: the complete nine-member native package gives Codex
  and Claude the selected skill/host instructions, source and projection routes;
  actual bounded use is judged by retained source-grounded native observations.
- `STDO-REP-2.5-RC5-C04`: the same-version cohort binds every source member,
  Product member and external identity required by the installed native path.

RC4 C01, C03 and C06 are **conserved** for the exact successor. C02's RC4
compression is **superseded** by the RC5-grounded authored program. C04's
historical RC3-to-RC4 delta is **superseded** by the complete RC4-to-RC5 source
inventory and recorded source comparison. C05's native interface persists and
is **superseded** only by the declared frame-index guide and successor routes.
The accepted RC1 claim dispositions and semantic/runtime exclusions remain
**conserved** through those explicit successor relations.

## Qualification Boundary

The 97-statement authored program, 23 supporting links and two frame indexes
were independently compared with all 52 source files through T009. RC5
construction only replaces the source URI prefix and program identity; its
inverse transformation equals the reviewed authored predecessor. Exact-source
validation and all six views reproduce with the unchanged qualified mechanic.

Independent original-source oracles are frozen before the parallel native UAT.
The final result records each exact host, treatment, observed effect and
disposition, including failed predecessors and unavailable preparations.
Historical Claude FP04 overreach and its limited support remain observations;
a newer run never erases them. No universal LLM reliability, token/time budget,
automatic classification, source semantics, owner ruling or executor is claimed
by the indexing mechanics. UAT and installed E2E remain distinct evidence.

The exact candidate verdict and publication records remain outside these
self-reference-sensitive release bytes. Required source, native, installed,
member and remote gates must hold before the selected atomic publication.
Product acceptance and real consumer/fleet adoption remain separate.
"""
(ROOT / rep["release_note"]).write_text(rep_note)

refs = {}
raw = subprocess.check_output(["git", "ls-remote", URL], cwd=ROOT, text=True)
(PROOF / "remote-before-publication.txt").write_text(raw)
for line in raw.splitlines():
    oid, name = line.split("\t", 1)
    refs[name] = oid
destinations = [payload["cohort"]["carrier_ref"]]
for product in payload["products"].values():
    destinations += [product[k] for k in ["release_ref", "selector_ref", "rc_branch", "release_branch"]]
expected = {name: refs.get(name) for name in sorted(destinations)}
lines = {}
for name, product in payload["products"].items():
    rows = []
    for ref, oid in refs.items():
        ordinal = check.rc_ref_ordinal(ref, product["namespace"], "2.5.0", include_unqualified=name == "specification_methodology")
        if ordinal is not None:
            rows.append({"ordinal": ordinal, "ref": ref, "tag_object": oid, "peeled_commit": refs.get(ref + "^{}")})
    lines[name] = sorted(rows, key=lambda row: (row["ordinal"], row["ref"]))
    assert all(row["ordinal"] < 5 and row["peeled_commit"] for row in rows)
payload["publication"] = {"repository_url": URL, "expected_remote": expected, "expected_version_lines": lines,
    "expected_version_lines_sha256": check.canonical_value_sha256({"repository_url": URL, "version_lines": lines})}
put(ROOT / "stack_release.json", payload)
print(json.dumps({"cohort": CUT, "axiom_inventory": axiom["subject"]["member_set_sha256"], "representation_inventory": rep["subject"]["member_set_sha256"], "remote_destinations": len(expected)}))
