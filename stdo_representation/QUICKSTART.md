# STDO Representation Quickstart

This guide exercises the STDO 2.5.0 compression-and-index source candidate
against exact Source STDO `v2.5.0-rc.2`. It is not constitutional authority.
Project frame basis revision 14 must be accepted and bound before this workflow
is treated as governed Product use.

## 1. Verify the dependencies

Verify Source STDO:

```sh
stdo verify v2.5.0-rc.2
```

The result must identify manifest SHA-256
`313e23116623a3bfbe96d279e089489aac466584982e1c34171ef244f0ec680a`
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

## 2. Validate the compression and index

Set the verified dependency root for this shell:

```sh
AXIOM_INDEXER_ROOT="/path/to/Axiom Indexer/releases/v0.1.0-rc.1"
```

Validate the selected `a_c.STDO` compression using invocation-local bindings:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" validate \
  --program \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/axiomatic-program.json \
  --bindings \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/bindings.json \
  --emit-map /tmp/stdo-representation-map.json
```

Compare the emitted logical constraint index with:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/
  logical-constraint-map.json
```

Identical compression, bindings, and dependency bytes must reproduce the same index.
The dogfood binding file contains installation-local physical paths and is not a
portable Product member.

## 3. Use the native skill

The native skill in this source candidate is repriced to the exact RC2
compression and index and passes the project checker. Published STDO
Representation `2.5.0` RC1 remains the accepted Product; repository discovery
of these newer bytes is a source-project convenience, not another released RC.
Native discovery remains:

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

1. load the logical constraint index and verify it binds the exact compression;
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
    "label": "Role and outcome",
    "text": "<acting role and intended result>"
  },
  {
    "label": "Reference frame and exact subject",
    "text": "<frame URI, purpose, source route, subject, and evidence boundary>"
  },
  {
    "label": "Hard constraints",
    "text": "<only material governing and forbidden relations>"
  },
  {
    "label": "Index context and evidence routes",
    "text": "<selected clauses, residuals, evidence, and source routes>"
  },
  {
    "label": "Open solution space",
    "text": "<choices left to the acting model unless prohibited>"
  },
  {
    "label": "Return and stop contract",
    "text": "<result, evidence, residual, and stop requirements>"
  },
  {
    "label": "ACTION",
    "text": "<bounded requested action>"
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
or decide authority. The seven rows are caller guidance, not a prompt schema or
engine; include only material constraints and leave unowned realization choices
open.

## 5. Check the accepted basis

```sh
stdo verify v2.5.0-rc.2
python3 -m json.tool stdo_representation.json >/dev/null
```

Revision 14 of the project frame basis is accepted at SHA-256
`6cc05636ea00797e44f6ebb661d342d5b8cfb59cbde2a81059062dddf6eb106f`.
Product-owner decision SHA-256
`68394d5118a6250972aa06db995a5d020c2f09996c90b0dfe70d4d8e908e8eba`
binds those exact bytes. `stdo_representation.json` names that decision in its
`reference_frame_bases` relation; it does not infer activation from this guide
or reuse revision 13. Verify the binding with:

```sh
stdo status --definition stdo_representation.json --verify
```

This acceptance governs the continuing RC2-basis source candidate. It does not
publish or accept another immutable STDO Representation RC.

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

They remain retained prior-WHAT history and evidence. The active Product
contains no local engine and makes no GTL or deterministic-orchestration claim.
