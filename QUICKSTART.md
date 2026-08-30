# STDO Representation Quickstart

This guide exercises the thin map-first Product. It is not constitutional
authority.

## 1. Verify the dependencies

Verify Source STDO:

```sh
stdo verify v2.5.0-rc.1
```

The result must identify manifest SHA-256
`3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`
with no failures.

Resolve an installed Axiom Indexer `v0.1.0-rc.1` checkout and verify:

```sh
git -C "/path/to/Axiom Indexer/releases/v0.1.0-rc.1" \
  rev-parse refs/tags/v0.1.0-rc.1
git -C "/path/to/Axiom Indexer/releases/v0.1.0-rc.1" \
  rev-parse 'refs/tags/v0.1.0-rc.1^{}'
```

Expected tag object:
`e7afc8a42a7123aebe91cb7582cb037b1aae612d`.
Expected peeled commit:
`dc3e00998da36dae6ac7b76b340431a85096c83c`.

Stop on any mismatch. Do not substitute a branch or compatible source tree.

## 2. Validate the selected map

Set the verified dependency root for this shell:

```sh
AXIOM_INDEXER_ROOT="/path/to/Axiom Indexer/releases/v0.1.0-rc.1"
```

Validate the released Product program using invocation-local bindings:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" validate \
  --program \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/axiomatic-program.json \
  --bindings \
    dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/bindings.json \
  --emit-map /tmp/stdo-representation-map.json
```

Compare the emitted map with:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/
  logical-constraint-map.json
```

Identical program, bindings, and dependency bytes must reproduce the same map.
The dogfood binding file contains installation-local physical paths and is not a
portable Product member.

## 3. Use the native skill

Codex discovers:

```text
.agents/skills/stdo-representation
```

Claude discovers:

```text
.claude/skills/stdo-representation
```

Both resolve to the canonical `skills/stdo-representation/` bundle. Ask the
agent to use `stdo-representation` for a bounded task. It should:

1. load the logical map;
2. select material frame URIs;
3. show each frame URI, purpose, and source route;
4. re-enter Source STDO only when required;
5. preserve its Executive, Worker, or Reviewer boundary; and
6. report unresolved residuals.

The agent, not code, owns frame selection.

## 4. Join an Executive request

Write a bare ordered JSON array:

```json
[
  {
    "label": "Reference frames",
    "text": "<frame URI, purpose, and source route>"
  },
  {
    "label": "Task",
    "text": "<bounded task>"
  }
]
```

Then invoke the exact joiner:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" join \
  --input /path/to/ordered-sections.json \
  --output /path/to/request.txt
```

The joiner preserves every supplied label, text value, and row order. It does
not select frames, rewrite instructions, enforce a token budget, invoke a model,
or decide authority.

## 5. Run project checks

```sh
python3 scripts/check_constitution.py
python3 -m unittest scripts.test_check_constitution -v
```

`stdo status --definition stdo_representation.json --verify` must pass against
the exact accepted revision-11 project frame basis. Any failure is a release
hold.

## Historical paths

Do not use these as the current Product:

```text
build_tenants/semantic_compile/
build_tenants/gtl/
build_tenants/json_schema/
scripts/prepare_stdo_gtl_candidate.py
scripts/finalize_stdo_gtl_product.py
scripts/test_frozen_gtl_tenant.py
```

They remain retained prior-WHAT history and evidence. The thin `0.1.0` Product
contains no local engine and makes no GTL or deterministic-orchestration claim.
