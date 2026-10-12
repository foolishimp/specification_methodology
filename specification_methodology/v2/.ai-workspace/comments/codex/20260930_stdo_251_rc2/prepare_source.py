"""Freeze RC1 source inventory and release note from independently reviewed bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
PROJECT = ROOT / "specification_methodology"
PREDECESSOR = "refs/tags/specification_methodology/v2.5.1-rc.1"
PREDECESSOR_TAG = "b80e82e123f7f88eb0dffd9339f8ead9c733d153"
PREDECESSOR_COMMIT = "dc4742d08af0a1c42c437a4ce645ea7ca55f3a3a"
START = "b445265"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def inventory(relative):
    base = PROJECT / relative
    rows = [{"path": p.relative_to(base).as_posix(), "sha256": sha(p.read_bytes())}
            for p in sorted(base.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts]
    prefix = "specification_methodology/" + relative + "/"
    paths = git("ls-tree", "-r", "--name-only", PREDECESSOR, "--", prefix).decode().splitlines()
    old = {p[len(prefix):]: sha(git("show", f"{PREDECESSOR}:{p}")) for p in paths}
    require(set(old) == {r["path"] for r in rows}, f"unselected member-set change: {relative}")
    for row in rows:
        row["predecessor_sha256"] = old[row["path"]]
        row["disposition"] = "conserved" if old[row["path"]] == row["sha256"] else "changed"
    return rows


def aggregate(rows, prefix):
    return sha("".join(f"{r['sha256']}  {prefix}{r['path']}\n" for r in rows).encode())


def table(rows, prefix):
    return "\n".join(["| Disposition | Member | SHA-256 |", "|---|---|---|"] +
                     [f"| {r['disposition']} | `{prefix}{r['path']}` | `{r['sha256']}` |" for r in rows])


require(git("rev-parse", PREDECESSOR).decode().strip() == PREDECESSOR_TAG, "predecessor tag drift")
require(git("rev-parse", PREDECESSOR + "^{commit}").decode().strip() == PREDECESSOR_COMMIT,
        "predecessor commit drift")
review = json.loads((OUT / "source-review.json").read_text())
require(review["status"] == "satisfied", "independent source assessment is not satisfied")
for relative, digest in review["files"].items():
    require(sha((ROOT / relative).read_bytes()) == digest, f"reviewed subject drift: {relative}")
standards, plugin, manager = (inventory(p) for p in
                            ("specification/standards", "plugins/spec", "src/stdo_toolchain"))
require((len(standards), len(plugin), len(manager)) == (52, 17, 11), "unselected member count")
for row in standards:
    if row["disposition"] == "changed":
        relative = "specification_methodology/specification/standards/" + row["path"]
        require(review["files"].get(relative) == row["sha256"], "unreviewed source delta: " + relative)
for row in plugin:
    if row["disposition"] == "changed" and row["path"].startswith("skills/"):
        relative = "specification_methodology/plugins/spec/" + row["path"]
        require(review["files"].get(relative) == row["sha256"], "unreviewed skill delta: " + relative)
    if row["path"].endswith("plugin.json"):
        require(json.loads((PROJECT / "plugins/spec" / row["path"]).read_text())["version"] ==
                "2.5.1-rc.2", "plugin version mismatch")
for row in manager:
    relative = "specification_methodology/src/stdo_toolchain/" + row["path"]
    require(row["sha256"] == sha(git("show", f"{START}:{relative}")), "manager changed during preparation")
conserved = {}
for path in ("LICENSE", "stdo_default.json", "specification/INTENT.md",
             "specification/PRODUCT.md", "specification/SCENARIOS.md", "specification/REFERENCE_FRAME_BASIS.md"):
    value = sha((PROJECT / path).read_bytes())
    require(value == sha(git("show", f"{PREDECESSOR}:specification_methodology/{path}")),
            f"source binding changed: {path}")
    conserved[path] = value
package_sha = sha((PROJECT / "pyproject.toml").read_bytes())
require(package_sha == sha(git("show", f"{START}:specification_methodology/pyproject.toml")),
        "package configuration changed during preparation")
changed = [r["path"] for r in standards if r["disposition"] == "changed"]
note = f"""# STDO 2.5.1 RC2

The product-local cut name is `v2.5.1-rc.2`; its immutable ref is
`refs/tags/specification_methodology/v2.5.1-rc.2` and public basis is
`stdo://releases/v2.5.1-rc.2/`. The version-line selector is
`refs/tags/specification_methodology/v2.5.1`.

Status: reviewed source candidate; publication is recorded separately in the
[RC2 release record](../.ai-workspace/comments/codex/20260930_stdo_251_rc2/README.md).
The immutable predecessor is `{PREDECESSOR}`, tag `{PREDECESSOR_TAG}`,
commit `{PREDECESSOR_COMMIT}`. All prior immutable cuts remain preserved.

## Change and qualification

Universal Intake Triage explains triangulation: applicable reference frames
constrain candidate diagnoses through distinct material variables, relations and
evidence over one subject and basis. Combined results preserve uncertainty and
identify the smallest sufficient lawful repair. Repeating analysis supplies no
additional evidence. No mandatory reviewer count, new review round, automatic
constitutional repricing or extra mutation authority is introduced.

Four standards members change: SPEC_METHOD and its three affected compressions.
The bootstrap compression changes only its source binding and generation date.
Independent source/invariant review binds every changed member. The matched
Representation authors the focused semantic delta, rebinds all source members,
and mechanically regenerates the map/projections from this exact Install.
Its separate release note records native-use evidence and limitations.

RC1 claims C01-C03 and their unchanged evidence remain valid within their prior
scope; this paragraph clarifies C01. C04's exact cohort identity advances to RC2.
Plugin workflow bytes and manager 0.1.4 remain unchanged; only plugin version
metadata advances. The source project's authoring basis remains RC4. External
consumer adoption, ABG delivery and repeated-judgment reliability are unclaimed.

## Standards inventory

52 members; aggregate `{aggregate(standards, '')}`.

{table(standards, '')}

## Plugin inventory

17 members; aggregate `{aggregate(plugin, '')}`.

{table(plugin, '')}

## Manager inventory

11 byte-conserved members; aggregate `{aggregate(manager, '')}`.

{table(manager, '')}
"""
(PROJECT / "releases/v2.5.1.md").write_text(note)
record = {"standards": standards, "plugin": plugin, "manager": manager,
          "standards_member_set_sha256": aggregate(standards, ""),
          "plugin_member_set_sha256": aggregate(plugin, ""), "conserved": conserved,
          "changed_standards": changed, "source_review_sha256": sha((OUT / "source-review.json").read_bytes())}
(OUT / "source-inventory.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"changed_standards": changed, "standards":len(standards), "plugin":len(plugin), "manager":len(manager)}))
