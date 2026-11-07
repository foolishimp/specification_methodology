# STDO Representation 3.0.5 Quickstart

Use the exact subject and same-version Axiom dependency bound by
[the release record](releases/v3.0.5.md) and final cohort binding. The caller's
own Product Definition, accepted frame and work grant remain operative.

## Verify current identity

Check `VERSION`, the exact release inventory, source freeze, current model
binding and conversion receipt before use. The canonical source snapshot is
`build_tenants/a_c/representation/stdo-v3.0.5/source/`; it contains 68 frozen
members. `current-binding.json` names its source identity and exact model.
Final installed native manifest identity belongs to the external cohort binding.

In an explicitly selected source candidate, the supplied invocation-local
Binding Set routes `stdo://releases/v3.0.5/` to that exact snapshot. For an
installed native release, bind the same URI to the verified Install root
containing `standards/` and `plugins/`. Do not substitute a mutable neighboring
checkout. Binding Sets are access coordinates, not authority or acceptance.

## Validate and select a bounded view

From the Representation Product root, use the verified Axiom Product:

```sh
python3 <axiom-product-root>/build_tenants/core/code/ac.py validate --program build_tenants/axiom_indexer/representation/stdo-v3.0.5/axiomatic-program.json --bindings build_tenants/axiom_indexer/representation/stdo-v3.0.5/bindings.json
```

The map names five explicit indexes. For the current native work/control cone:

```sh
python3 <axiom-product-root>/build_tenants/core/code/ac.py project --program build_tenants/axiom_indexer/representation/stdo-v3.0.5/axiomatic-program.json --map build_tenants/axiom_indexer/representation/stdo-v3.0.5/logical-constraint-map.json --bindings build_tenants/axiom_indexer/representation/stdo-v3.0.5/bindings.json --frame-index urn:stdo-representation:frame-index:v3.0.5:native-work --mode reference-only
```

Use `materialized` for unchanged authored rows of the same closure. Omitted
`--output` writes stdout; `--output -` names a literal file. File outputs need
an existing grant and must be separate from inputs and source. The native work
selection contains 21 records, including its real nested control/issuer/host
dependencies and unresolved actual-host evidence limit. It does not authorize
work or certify isolation.

## Source re-entry and native use

Load the canonical `skills/stdo-representation/SKILL.md` through the host's
actual supported skill mechanism. Workspace Codex/Claude discovery links point
to that same bundle; distributed inventories contain regular files.
Read [frame-index use](skills/stdo-representation/references/frame-index-use.md)
for refusal, source-currentness and role boundaries.

Bring actual task facts, semantic judgments and owner rulings separately.
Re-enter the exact owner for ambiguity, unsupported applicability, missing
dependencies or changed normative premises. A historical judgment survives
only its declared invalidators; equal source text alone is insufficient.

For a requested handoff, author an ordered array of `{label,text}` strings and
use Axiom's pure `join --input <sections.json>` command. It selects no frames,
rewrites no grants and invokes no model. A sufficient direct task needs no
new ticket, coordination or approval merely to use this representation.

Model/carrier preservation, source fidelity review, real Lean checking,
native usability, publication and consumer adoption are distinct evidence.
Historical 2.x artifacts remain historical; they do not substitute for this
current model or its exact release dependencies.
