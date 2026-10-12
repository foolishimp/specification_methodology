"""Reproduce the bounded RC6 source note and inventory from exact local bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[5]
PROJECT = ROOT / "specification_methodology"
OUT = Path(__file__).resolve().parent
SOURCE = "508ca2d2280870c198e58ca513fb8edd8bf72d39"
PREDECESSOR = "refs/tags/specification_methodology/v2.5.0-rc.5"
PREDECESSOR_TAG = "d4b7c7724944e02ce25c6e6ce69722491c349924"
PREDECESSOR_COMMIT = "c7888bb2dc9aee1f5a217985f6d1547cfe6465f0"
PREDECESSOR_MANIFEST = "3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f"


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
require(all(r["sha256"] == digest(git("show", f"{SOURCE}:specification_methodology/specification/standards/{r['path']}"))
            for r in standards), "standards differ from reviewed source commit")
require({r["path"] for r in plugin if r["disposition"] == "changed"} == {
    ".claude-plugin/plugin.json", ".codex-plugin/plugin.json", "references/GETTING_STARTED.md"},
    "unexpected plugin delta")
require(all(r["disposition"] == "conserved" for r in manager), "manager source changed")
for manifest in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
    require(json.loads((PROJECT / "plugins/spec" / manifest).read_text())["version"] == "2.5.0-rc.6",
            "plugin version mismatch")
conserved = {}
for path in ("pyproject.toml", "LICENSE", "stdo_default.json", "specification/INTENT.md",
             "specification/PRODUCT.md", "specification/SCENARIOS.md", "specification/REFERENCE_FRAME_BASIS.md"):
    value = digest((PROJECT / path).read_bytes())
    require(value == digest(git("show", f"{PREDECESSOR}:specification_methodology/{path}")),
            f"unexpected source binding change: {path}")
    conserved[path] = value

note = f"""# STDO 2.5.0 RC6

This note declares the sixth immutable candidate on the STDO `2.5.0` line.
The product-local cut name is `v2.5.0-rc.6`; the qualified immutable ref is
`refs/tags/specification_methodology/v2.5.0-rc.6` and the public basis is
`stdo://releases/v2.5.0-rc.6/`. The namespace and subtree are both
`specification_methodology`. Publication, exact-cut Product acceptance and
consumer adoption remain distinct; this subject declaration supplies none of
those results by itself.

## Predecessor And Selected Delta

The exact published predecessor is `specification_methodology/v2.5.0-rc.5`,
tag object `{PREDECESSOR_TAG}`, commit
`{PREDECESSOR_COMMIT}`, repository tree
`cb87e3e0bfaf033ee3cfa6b260d0d9ead0312b08`, Project Subtree tree
`40dc632ee5185b2b29cfce43ef8b06f223ea27ea`, standards tree
`b04dee86bd8d4f272d215801257ddd7ae5d5d782`, installed manifest
`{PREDECESSOR_MANIFEST}`.
Its release note, prior claim dispositions and all immutable predecessor
subjects remain at their original tags.

The bounded semantic delta is the optional engagement baseline's
`STDO_REFERENCE_FRAME_BASELINE.md#steel-thread-delivery`, committed in
`{SOURCE}`. Executive establishes or extends
the smallest real runnable Product path early, selects increments by material
uncertainty, dependency/interface reach and failure impact, and uses early
integration evidence to prune incompatible choices. Focused deterministic
checks and judgment probes guide construction; substantial UAT qualifies a
bounded capability or release. Distinct testing claims, unexercised-path
obligations, independence, required repetitions, material invalidation and
existing operation grants remain with their owners.

The aggregate compression projects that guidance; the bootstrap changes only
its source digest. Exactly three standards members change and 49 remain
byte-conserved. The plugin's two version manifests and packaged installation
selectors advance to RC6; its five workflow skills and host metadata remain
byte-conserved. Manager `stdo-toolchain 0.1.3`, all 11 implementation files,
package configuration and license remain byte-conserved from RC5.

The complete coordinated successor uses suffix `2.5.0-rc.6`. Its Axiom and
Representation Products retain separate ownership. Their same-version
program/map and complete source-corpus bindings must be regenerated and
qualified from the exact RC6 Install; RC5 derived assets cannot stand in for
the changed source. Source Product/Intent/model/frame declarations and the
source project's operative RC4 Definition are excluded from the released
normative inventory and remain unchanged. Completed T030/T029 are not reopened.

## Claims And Successor Dispositions

| RC6 claim | Bounded claim and RC5 disposition |
|---|---|
| `STDO-2.5-RC6-C01` | RC5 C01 is superseded only by the explicit steel-thread sequencing extension above. Existing proportionate treatment, C/J/O, conditional frames, design coverage, closure, grant and independence meanings are conserved. |
| `STDO-2.5-RC6-C02` | RC5 C02's shared five-entrypoint functional claim is conserved. RC6 package identities and installation selectors replace the RC5 distribution identities; no new workflow or host-reliability claim is added. |
| `STDO-2.5-RC6-C03` | RC5 C03 is conserved with exact manager 0.1.3 bytes: selected complete updates, source/preimage refusal and bounded caught-failure recovery retain their prior contract and limitations. |
| `STDO-2.5-RC6-C04` | RC5 C04's exact-cohort identity is superseded by the complete RC6 corpus/plugin/Axiom/Representation binding. The complete-cohort, installed-path and guarded atomic publication requirements are conserved and require RC6 evidence. |

Earlier claims and exclusions retain their explicit RC5 dispositions. There
is no universal cost gate, automatic frame or semantic decision engine,
crash-atomic filesystem claim, implicit consumer adoption, or new repeated-J
reliability claim. Reused evidence preserves its exact earlier subjects and
limitations, including the historical unqualified FP04 prospective advice.

## Normative Standards Subject

Exactly {len(standards)} standards members; aggregate (SHA-256, two spaces,
`specification/standards/` plus member path and newline):
`{aggregate(standards, 'specification/standards/')}`.

{table(standards, 'specification/standards/')}

## Subordinate Native Plugin

Exactly {len(plugin)} plugin members, version `2.5.0-rc.6`; aggregate with
`./`-prefixed member names: `{aggregate(plugin, './')}`.

{table(plugin, 'plugins/spec/')}

## Manager Package Inputs

The manager is subordinate tooling, not a normative standards member. Its
unchanged version is `0.1.3`; an exact RC6 Git installation selects the same
package source and configuration as RC5.

{table(manager, 'src/stdo_toolchain/')}

`pyproject.toml` SHA-256: `{conserved['pyproject.toml']}`.
`LICENSE` SHA-256: `{conserved['LICENSE']}`.

## Qualification And Publication

The [RC6 work and evidence carrier](../.ai-workspace/comments/codex/20260906T130745Z_rc6_release/README.md)
binds source inventory, affected semantic/package qualification and subsequent
exact-cut results. [RC5 evidence](../.ai-workspace/comments/codex/20260906T083553Z_rc5_release/README.md)
is reused only for conserved claims with its original finite observations and
limitations; no source or mechanical result becomes new native evidence.

The release follows the explicit root `STACK_RELEASE.md` relation: freeze
commit A and its local annotated STDO tag, verify the exact Install, construct
and qualify commit B, qualify the complete local ref graph and frozen remote
leases, publish only the checked full-object argument vector in one atomic
transaction, and reacquire the public objects and bytes. This note does not
claim those pending results. Later bookkeeping cannot change immutable tags.
Actual Product acceptance and consumer adoption remain separately authorized.
"""
(PROJECT / "releases/v2.5.0.md").write_text(note)
record = {
    "kind": "stdo.rc6-source-inventory", "source_commit": SOURCE,
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
