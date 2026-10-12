"""Freeze RC1 source inventory and release note from independently reviewed bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
PROJECT = ROOT / "specification_methodology"
PREDECESSOR = "refs/tags/specification_methodology/v2.5.0-rc.7"
PREDECESSOR_TAG = "ac0e72b49814c30caf373fe87cedce585bdd36b8"
PREDECESSOR_COMMIT = "ddeb971da89ee47065359c99897a825b803eedd4"
START = "3251990630aced3be29c128e8d0fe17bb6df0b92"


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
                "2.5.1-rc.1", "plugin version mismatch")
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
note = f"""# STDO 2.5.1 RC1

This declaration identifies the first candidate on the STDO `2.5.1` line.
The product-local cut name is `v2.5.1-rc.1`; the qualified immutable ref is
`refs/tags/specification_methodology/v2.5.1-rc.1` and the public basis is
`stdo://releases/v2.5.1-rc.1/`. The moving selector is
`refs/tags/specification_methodology/v2.5.1`; RC and release branches are
`refs/heads/rc/specification_methodology/2.5.1` and
`refs/heads/release/specification_methodology/2.5.1`.

Status: local candidate preparation. This note does not claim publication,
public reacquisition, Product acceptance or external consumer adoption. Source
authoring remains on its separately accepted RC4 basis. STDO 2.5.1 qualification
is independent of T-288 and ABI delivery; postmortem cases test these amendments.

## Predecessor And Scope

The immutable published predecessor is `{PREDECESSOR}`, annotated tag object
`{PREDECESSOR_TAG}`, commit `{PREDECESSOR_COMMIT}`, installed manifest
`1f56029380604b0879fe322047fa8b38060297ba86b54bc8db8450d01ec034ae`.
All prior cuts and their bounded evidence remain immutable.

The amendments make applicability and invalidation govern fact/result reuse;
evaluate complete computational paths and material operational assumptions;
bind findings and retained predicates to supported obligations and threats;
preserve permissions and exclusions through compression; put the burden on
retaining superseded production responsibility; and conserve obligations,
evidence and usable work through repricing. Existing owning clauses absorb the
relations. A Product owns its concrete workload, bounds and runtime policy.

Accepted T-031 adds the derived end-to-end interface integration frame. Its
contract-sufficiency, boundary-congruence, path-realization and ordinary-user
usability claims remain distinct, with evidence appropriate to each claim.

## Claims And Dispositions

| RC1 claim | Scope and predecessor disposition |
|---|---|
| `STDO-2.5.1-RC1-C01` | RC7 C01 is refined by validity-preserving reuse, complete-path evaluation, applicable operational/threat assumptions, retention burden and continuity. Capability, independent assessment, Executive mutation lock, closure and existing frame conditions remain. No per-function proof ceremony, per-status Writer activation, universal cost quota or new fact registry is introduced. |
| `STDO-2.5.1-RC1-C02` | RC7 C02's five portable plugin entrypoints are conserved. Affected guidance and exact distribution identities are updated. T-031's frame becomes available in the matched Representation; native usability needs the separate bounded observations. |
| `STDO-2.5.1-RC1-C03` | RC7 C03 is refined by the already committed manager 0.1.4 repair: choose the declared companion install closure before validating it. Unsafe, missing, escaping or cyclic links within that closure still refuse. Unselected historical fixtures do not block the install. Existing transaction limitations remain. |
| `STDO-2.5.1-RC1-C04` | RC7 C04's exact cohort identity is superseded by this matched source/plugin/Axiom/Representation candidate. Complete inventories, exact source routes and independently qualified changed meaning remain required. Preparing local refs does not publish them. |

R7/R8 reuse existing law where sufficient. No ABI runtime guard, event model,
cache, C2 policy, ticket closure or downstream method adoption is part of this
release. No native LLM decision qualifies a mechanical property. Qualification
does not claim general host reliability or universal operational improvement.

## Normative Standards Subject

Exactly {len(standards)} standards members; {len(changed)} change from RC7.
The aggregate hashes the sorted SHA-256, two spaces, `specification/standards/`
plus member path and newline: `{aggregate(standards, 'specification/standards/')}`.

{table(standards, 'specification/standards/')}

## Subordinate Native Plugin

Exactly {len(plugin)} members, version `2.5.1-rc.1`; aggregate with `./`-prefixed
member paths: `{aggregate(plugin, './')}`.

{table(plugin, 'plugins/spec/')}

## Manager Package Inputs

Manager `0.1.4` is subordinate tooling. Its repair is existing commit
`b2bcdfeb8c56c140e94b4867f1151542192ec0e0`, versioned by
`3251990630aced3be29c128e8d0fe17bb6df0b92`. This preparation conserves those
mechanics; their changed install behavior is included in package qualification.

{table(manager, 'src/stdo_toolchain/')}

`pyproject.toml` SHA-256: `{package_sha}`.
`LICENSE` SHA-256: `{conserved['LICENSE']}`.

## Qualification And Construction

The [RC1 preparation record](../.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md)
binds the independent source review, exact inventories, mechanical results,
matched semantic projections, native task outcomes and local cohort checks.
The [RC7 record](../.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
and T-031 evidence apply only to conserved subjects and their original limits.

Local construction follows [the coordinated procedure](../../STACK_RELEASE.md#coordinated-construction):
freeze source commit A and its annotated tag, install/verify exact source,
construct and qualify companions at commit B, and check the local ref graph
and remote expectations. Publication and fresh public reacquisition are separate
effects. Later bookkeeping cannot move immutable tags.
"""
record = {
    "kind": "stdo.251-rc1-source-inventory", "starting_commit": START,
    "predecessor": {"ref": PREDECESSOR, "tag_object": PREDECESSOR_TAG, "commit": PREDECESSOR_COMMIT},
    "standards": standards, "standards_member_set_sha256": aggregate(standards, "specification/standards/"),
    "plugin": plugin, "plugin_member_set_sha256": aggregate(plugin, "./"),
    "manager": manager, "manager_member_set_sha256": aggregate(manager, "src/stdo_toolchain/"),
    "conserved_source_bindings": conserved, "package_configuration_sha256": package_sha,
    "source_review_sha256": sha((OUT / "source-review.json").read_bytes()),
    "release_note_sha256": sha(note.encode()), "added_members": [], "removed_members": [],
}
(OUT / "release-note.candidate.md").write_text(note)
(PROJECT / "releases/v2.5.1.md").write_text(note)
(OUT / "source-inventory.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"standards": len(standards), "changed_standards": changed,
                  "plugin": len(plugin), "manager": len(manager),
                  "release_note_sha256": record["release_note_sha256"]}))
