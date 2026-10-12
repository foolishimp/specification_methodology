"""Reproduce RC5 release inventories from the selected source bytes."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[5]
PROJECT = ROOT / "specification_methodology"
OUT = Path(__file__).resolve().parent
PREDECESSOR = "refs/tags/specification_methodology/v2.5.0-rc.4"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inventory(relative):
    base = PROJECT / relative
    return [{"path": p.relative_to(base).as_posix(), "sha256": digest(p.read_bytes())}
            for p in sorted(base.rglob("*")) if p.is_file() and "__pycache__" not in p.parts]


def aggregate(rows, prefix):
    return digest("".join(f"{r['sha256']}  {prefix}{r['path']}\n" for r in rows).encode())


standards = inventory("specification/standards")
plugin = inventory("plugins/spec")
manager = inventory("src/stdo_toolchain")
snapshot = ROOT / "stdo_representation/dogfood/t009-frame-projection/run-001/source/standards"
assert all(digest((snapshot / r["path"]).read_bytes()) == r["sha256"] for r in standards)
assert len(standards) == len([p for p in snapshot.rglob("*") if p.is_file()]) == 52

def table(rows, prefix="", compare=False):
    lines = ["| Disposition | Member | SHA-256 |", "|---|---|---|"]
    for r in rows:
        disposition = "included"
        if compare:
            old = subprocess.run(["git", "show", f"{PREDECESSOR}:specification_methodology/{prefix}{r['path']}"], cwd=ROOT, capture_output=True)
            disposition = "added" if old.returncode else "conserved" if digest(old.stdout) == r["sha256"] else "changed"
        lines.append(f"| {disposition} | `{prefix}{r['path']}` | `{r['sha256']}` |")
    return "\n".join(lines)


note = f"""# STDO 2.5.0 RC5

This note declares the fifth immutable candidate on the STDO `2.5.0` line.
The product-local cut name is `v2.5.0-rc.5`; the qualified immutable ref is
`refs/tags/specification_methodology/v2.5.0-rc.5` and the public basis is
`stdo://releases/v2.5.0-rc.5/`. The namespace and subtree are both
`specification_methodology`. Publication, exact-cut Product acceptance and
consumer adoption remain distinct. This note does not assert an unobserved
test result or an acceptance of its own subject.

## Predecessor And Selected Delta

The exact published predecessor is `specification_methodology/v2.5.0-rc.4`,
tag object `032dac0c833111547f7dd4b290c5316ed9b70f97`, commit
`7a25668a8fecfd26f895759af3bec4708727964a`, installed manifest
`4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`.
Its release note and every earlier immutable cut remain at their original tags.
The accepted RC1 semantic baseline and its subsequent explicit dispositions
remain recorded by the predecessor; publication does not retrospectively
accept any predecessor.

T030 supplies proportionate classification and treatment, condition-based
closure, valid judgment/ruling reuse, conditional frame applicability and
bounded shared native guidance. Generic meaning remains in its owning
standard. SCENARIOS is the source Product-use model, outside the released
normative member set. There is no token accounting or universal cost gate.

T029 supplies the shared `cohort-update` operation in `stdo-toolchain 0.1.3`:
an explicitly selected whole context is prepared and bound to an exact accepted
plan, stale source/companion and preimage drift refuse, caught failures restore
the declared rollback territory. It does not claim crash-atomic filesystem
transactions or infer semantic sufficiency. The original narrower adoption
operation remains available under its original contract.

The coordinated successor includes Axiom's explicit dependency projections and
Representation's authored STDO chains/index and native use through T009.
Those remain separately owned child Products. The complete cohort uses suffix
`2.5.0-rc.5`, exact source digests and one guarded atomic ref transaction.

## Claims And Successor Dispositions

- `STDO-2.5-RC5-C01`: the owning source methods express the selected logical
  use model without mandatory process for an otherwise sufficient local fix.
- `STDO-2.5-RC5-C02`: the five shared native entrypoints project those methods
  while preserving unknowns, conditional independence and effect grants.
- `STDO-2.5-RC5-C03`: the shared complete updater checks the exact selected
  context and source relations before admitted effects and final verification.
- `STDO-2.5-RC5-C04`: the complete coordinated package binds the same RC5
  corpus, plugin, Axiom dependency and Representation program/map, with the
  exact installed path independently qualified before publication.

RC4 C01-C03 are **conserved**, with the exact suffix advanced by this successor.
RC4 C04's frozen plugin-byte claim is **superseded** by RC5 C02 and the inventory
below; native entrypoint roles and the shared dual-host distribution persist.
Earlier manager-byte conservation is **superseded** by RC5 C03. RC2 and RC3
functional claims, and the RC1 calculus, occurrence-profile and exclusions,
are **conserved** subject to those explicit successor relations. No native
observation establishes universal model reliability or unobserved host paths.

## Normative Standards Subject

Exactly {len(standards)} standards members; aggregate (SHA-256, two spaces,
`specification/standards/` plus member path and newline):
`{aggregate(standards, 'specification/standards/')}`.

{table(standards, 'specification/standards/', True)}

## Subordinate Native Plugin

Exactly {len(plugin)} plugin members, version `2.5.0-rc.5`; aggregate with
`./`-prefixed member names: `{aggregate(plugin, './')}`.

{table(plugin, 'plugins/spec/', True)}

## Manager Package Inputs

The Python package is installed from this exact qualified Git cut and the
`specification_methodology` subtree. It is subordinate tooling, not a new
normative standards member. Its selected source files are:

{table(manager, 'src/stdo_toolchain/', True)}

`pyproject.toml` SHA-256: `{digest((PROJECT / 'pyproject.toml').read_bytes())}`.

## Qualification And Publication

Source/model comparison, actual native attempts (including failures), fixture
oracles, exact-source mechanical checks and installed-path observations remain
in their owning T030/T009 proof records. This note defines the subject and
claims; the final closed verdict binds their exact evidence and limitations.
Qualification does not turn an absent observation into a passed condition.

The release carrier follows `STACK_RELEASE.md`: freeze STDO commit A and its
local annotated tag, verify the exact Install, construct and qualify child
commit B, and publish only the checked full-object refspec vector with exact
remote leases in one atomic transaction. The three qualified version-line
selectors, RC branches and release branches identify their corresponding cuts.
Post-publication checks reacquire those exact objects and installed bytes.
Later bookkeeping cannot change a tag. ABIogenesis and fleet adoption are
outside this release grant.
"""
(PROJECT / "releases/v2.5.0.md").write_text(note)
(OUT / "source-inventory.json").write_text(json.dumps({"standards": standards, "standards_member_set_sha256": aggregate(standards, "specification/standards/"), "plugin": plugin, "plugin_member_set_sha256": aggregate(plugin, "./"), "manager": manager, "working_source_snapshot_conserved": True}, indent=2) + "\n")
print(json.dumps({"standards": len(standards), "plugin": len(plugin), "manager": len(manager), "source_snapshot_conserved": True}))
