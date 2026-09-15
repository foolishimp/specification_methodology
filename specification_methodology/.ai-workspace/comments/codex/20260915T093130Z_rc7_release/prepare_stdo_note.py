"""RC7 adaptation of the RC6 source-note/inventory helper; output stays in this evidence directory."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[5]
PROJECT = ROOT / "specification_methodology"
OUT = Path(__file__).resolve().parent
SOURCE = "0a0cd85229ed5290b14459d727121ba3c987861f"
PREDECESSOR = "refs/tags/specification_methodology/v2.5.0-rc.6"
PREDECESSOR_TAG = "27c11b4e6673b123b4117dea4e200f01fed2f947"
PREDECESSOR_COMMIT = "842d05daf0be1215e99e640396e670cde4c03d31"
PREDECESSOR_MANIFEST = "bed7535a5feddc5e874993ff96d1f5f27e2a0fff63f366fc3b1fec3e301dd9e0"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def inventory(relative):
    base = PROJECT / relative
    rows = [{"path": p.relative_to(base).as_posix(), "sha256": digest(p.read_bytes())}
            for p in sorted(base.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts]
    prefix = "specification_methodology/" + relative + "/"
    old_paths = git("ls-tree", "-r", "--name-only", PREDECESSOR, "--", prefix).decode().splitlines()
    old = {p[len(prefix):]: digest(git("show", f"{PREDECESSOR}:{p}")) for p in old_paths}
    require(set(old) == {r["path"] for r in rows}, f"unexpected member-set change: {relative}")
    for row in rows:
        row["predecessor_sha256"] = old[row["path"]]
        row["disposition"] = "conserved" if old[row["path"]] == row["sha256"] else "changed"
    return rows


def aggregate(rows, prefix):
    return digest("".join(f"{r['sha256']}  {prefix}{r['path']}\n" for r in rows).encode())


def table(rows, prefix):
    return "\n".join(["| Disposition | Member | SHA-256 |", "|---|---|---|"] +
                     [f"| {r['disposition']} | `{prefix}{r['path']}` | `{r['sha256']}` |" for r in rows])


require(git("rev-parse", PREDECESSOR).decode().strip() == PREDECESSOR_TAG, "predecessor tag drift")
require(git("rev-parse", PREDECESSOR + "^{commit}").decode().strip() == PREDECESSOR_COMMIT,
        "predecessor commit drift")
standards = inventory("specification/standards")
plugin = inventory("plugins/spec")
manager = inventory("src/stdo_toolchain")
require((len(standards), len(plugin), len(manager)) == (52, 17, 11), "unexpected inventory counts")
require({r["path"] for r in standards if r["disposition"] == "changed"} == {
    "STDO_REFERENCE_FRAME_BASELINE.md", "authority_compressions/stdo_bootstrap.md",
    "authority_compressions/stdo_compressed.md"}, "unexpected standards delta")
reviewed = {
    "STDO_REFERENCE_FRAME_BASELINE.md": "234172dd0d403d28a3fdee9dfe740ba35b1c7656e92c249aa6f70af67c408ee1",
    "authority_compressions/stdo_bootstrap.md": "9542d4c95dba044a08e2f17b84a3b6ab513fac6d96b7600a32baa45646c8d410",
    "authority_compressions/stdo_compressed.md": "8d30240a4d1323d838aad19051326ec6126040313f580c5a7ebeb8c146d56fcf",
}
require(all(r["sha256"] == reviewed.get(r["path"], r["predecessor_sha256"])
            for r in standards), "standards differ from admitted exact source subjects")
accepted_records = {
    ".ai-workspace/comments/codex/20260915_EXECUTIVE_EVENT_DRIVEN_POSTURE.md":
        "18cb383a9811b4fc6479f082c30e9f805a13c9999504014ae1d52a14cb97ba8b",
    ".ai-workspace/comments/codex/20260915_STDO_RELEASE_REQUEST_SCOPE.md":
        "58daf1b8df2921de01ad0b5b7035b0eff00adda5362e9ba356a594faad806828",
    "tests/test_reference_frame_boundaries.py":
        "857ac6e4a07a9f21543ebd8c196f24323e5c0df9529da781e860f093ff2c6bd5",
}
for path, expected in accepted_records.items():
    require(digest((PROJECT / path).read_bytes()) == expected, f"admitted member changed: {path}")
require({r["path"] for r in plugin if r["disposition"] == "changed"} == {
    ".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "references/GETTING_STARTED.md"},
    "unexpected plugin delta")
require(all(r["disposition"] == "conserved" for r in manager), "manager source changed")
for manifest in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
    require(json.loads((PROJECT / "plugins/spec" / manifest).read_text())["version"] == "2.5.0-rc.7",
            "plugin version mismatch")
conserved = {}
for path in ("pyproject.toml", "LICENSE", "stdo_default.json", "specification/INTENT.md",
             "specification/PRODUCT.md", "specification/SCENARIOS.md", "specification/REFERENCE_FRAME_BASIS.md"):
    value = digest((PROJECT / path).read_bytes())
    require(value == digest(git("show", f"{PREDECESSOR}:specification_methodology/{path}")),
            f"unexpected source binding change: {path}")
    conserved[path] = value

note = f"""# STDO 2.5.0 RC7

This note declares the seventh immutable candidate on the STDO `2.5.0` line.
The product-local cut name is `v2.5.0-rc.7`; the qualified immutable ref is
`refs/tags/specification_methodology/v2.5.0-rc.7` and the public basis is
`stdo://releases/v2.5.0-rc.7/`. The namespace and subtree are both
`specification_methodology`. Publication, exact-cut Product acceptance and
consumer adoption remain distinct; this subject declaration supplies none of
those results by itself. Public installation references apply after the
complete coordinated publication, not merely after local source freeze.

## Predecessor And Selected Delta

The exact published predecessor is `specification_methodology/v2.5.0-rc.6`,
tag object `{PREDECESSOR_TAG}`, commit
`{PREDECESSOR_COMMIT}`, repository tree
`b0bedab11282019e86603c1561187918ee8b9957`, Project Subtree tree
`9896c966e6b5f42d2d7498831a6b28ffa03b6efd`, standards tree
`a9616a8cc8a6ae9e5591f7938a9b7b3796ef3f7f`, installed manifest
`{PREDECESSOR_MANIFEST}`.
Its release note, claim dispositions and all immutable predecessor subjects
remain at their original tags.

The bounded semantic delta is the optional engagement baseline's
`STDO_REFERENCE_FRAME_BASELINE.md#event-driven-executive-attention`.
Executive attention is event-driven by default: decision-relevant closed
returns, material exceptions or changed basis, owner requests and declared
deadlines/checkpoints trigger attention. While Workers carry out their grants
and no other authorized decision is ready, Executive waits rather than
re-inspecting unfinished work or replaying unchanged judgments. Bounded
fallback observation supports unreliable notification or actual supervision;
silence is neither progress nor failure. Genuine blockers, material risk and
repeated no-progress require the owning bounded investigation or decision.
Current-workspace/evidence validity, drift locks, required independence,
capability, closed returns and all authority and closure duties survive.

The aggregate compression projects the rule; bootstrap adds its default and
a route to the single owner, with both source digests refreshed. Exactly three
standards members change and 49 remain byte-conserved from RC6. The plugin's
two version manifests and packaged installation references advance to RC7;
its five workflow skills and host metadata remain byte-conserved. Manager
`stdo-toolchain 0.1.3`, all 11 implementation files, package configuration and
license remain byte-conserved from RC6.

The complete successor uses suffix `2.5.0-rc.7`. Axiom Indexer and
Representation retain separate ownership. The affected Executive semantic
compression requires re-authoring, source-digest rebinding, map/projection
regeneration and affected semantic/native qualification against exact RC7;
RC6 derived assets cannot stand in for the changed source. No Axiom engine
change follows from this norm. The repository's accepted release-request
instructions select all dependency phases as part of one release mandate,
without changing generic release law, Product ownership or operation grants.
Source Product/Intent/model/frame declarations and the operative RC4 Definition
remain unchanged. Completed delivery tickets are not reopened.

## Claims And Successor Dispositions

| RC7 claim | Bounded claim and RC6 disposition |
|---|---|
| `STDO-2.5-RC7-C01` | RC6 C01 is superseded only by event-driven Executive attention with bounded effective supervision. Steel-thread delivery, proportionate treatment, C/J/O, conditional frames, valid evidence reuse, closure, grants, required capability and independence remain conserved. |
| `STDO-2.5-RC7-C02` | RC6 C02's shared five-entrypoint functional claim is conserved. RC7 package identities and installation references replace RC6 distribution identities; no new workflow or host-reliability claim is added. |
| `STDO-2.5-RC7-C03` | RC6 C03 is conserved with exact manager 0.1.3 bytes: selected complete updates, source/preimage refusal and bounded caught-failure recovery retain their contract and limitations. |
| `STDO-2.5-RC7-C04` | RC6 C04's exact-cohort identity is superseded by the complete RC7 corpus/plugin/Axiom/Representation binding. Complete-cohort, installed-path and guarded atomic publication conditions remain mandatory and require RC7 evidence. |

Earlier claims and exclusions retain their exact RC6 dispositions. There is
no universal cost/accounting gate, lower-assurance or downgraded-capability
path, scheduler or semantic decision engine, crash-atomic filesystem claim,
implicit consumer adoption, or new repeated-J reliability claim. Reused
evidence retains its original exact subjects and finite limitations.

## Normative Standards Subject

Exactly {len(standards)} standards members; aggregate (SHA-256, two spaces,
`specification/standards/` plus member path and newline):
`{aggregate(standards, 'specification/standards/')}`.

{table(standards, 'specification/standards/')}

## Subordinate Native Plugin

Exactly {len(plugin)} plugin members, version `2.5.0-rc.7`; aggregate with
`./`-prefixed member names: `{aggregate(plugin, './')}`.

{table(plugin, 'plugins/spec/')}

## Manager Package Inputs

The manager is subordinate tooling, not a normative standards member. Its
unchanged version is `0.1.3`; an exact RC7 Git installation selects the same
package source and configuration as RC6.

{table(manager, 'src/stdo_toolchain/')}

`pyproject.toml` SHA-256: `{conserved['pyproject.toml']}`.
`LICENSE` SHA-256: `{conserved['LICENSE']}`.

## Qualification And Publication

The [RC7 work and evidence carrier](../.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
binds exact source inventory, conserved independent semantic judgments,
source/package checks and subsequent phase results. [RC6 evidence](../.ai-workspace/comments/codex/20260906T130745Z_rc6_release/README.md)
is reused only for conserved claims on its original subjects and limitations.
Source and mechanical results are not new native qualification.

The release follows the single [root coordination procedure](../../STACK_RELEASE.md#coordinated-construction):
freeze commit A and its local annotated STDO tag, verify that Install,
construct and qualify commit B, qualify the complete local ref graph and
remote leases, publish only the checked full-object argument vector in one
atomic transaction, and freshly reacquire public objects and bytes. This note
does not claim those pending results. Later bookkeeping cannot move immutable
tags. Actual Product acceptance and consumer adoption remain separately owned.
"""
(OUT / "release-note.candidate.md").write_text(note)
record = {
    "kind": "stdo.rc7-source-inventory", "starting_commit": SOURCE,
    "reviewed_standards_sha256": reviewed, "accepted_records": accepted_records,
    "predecessor": {"ref": PREDECESSOR, "tag_object": PREDECESSOR_TAG,
                    "commit": PREDECESSOR_COMMIT, "installed_manifest_sha256": PREDECESSOR_MANIFEST},
    "standards": standards,
    "standards_member_set_sha256": aggregate(standards, "specification/standards/"),
    "plugin": plugin, "plugin_member_set_sha256": aggregate(plugin, "./"),
    "manager": manager, "manager_member_set_sha256": aggregate(manager, "src/stdo_toolchain/"),
    "conserved_source_bindings": conserved, "added_members": [], "removed_members": [],
    "release_note_sha256": digest(note.encode()), "reviewed_standards_source_conserved": True,
}
(OUT / "source-inventory.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"standards": len(standards), "changed_standards": 3,
                  "plugin": len(plugin), "changed_plugin": 3, "manager": len(manager),
                  "changed_manager": 0, "release_note_sha256": record["release_note_sha256"]}))
