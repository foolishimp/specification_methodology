# STDO Representation Quickstart

This guide exercises the coordinated STDO Representation `2.5.0-rc.4`
compression-and-index candidate against exact Source STDO `v2.5.0-rc.4`. It is
not constitutional authority. Accepted project frame basis revision 15 governs
this workflow.

## 1. Verify the dependencies

Verify Source STDO:

```sh
STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"
stdo --store "$STDO_STORE" verify v2.5.0-rc.4 \
  --manifest-sha256 4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e
```

The result must identify manifest SHA-256
`4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`
with no failures.

During the authorized coordinated prepublication construction, use the exact
same-version sibling candidate and verify its frozen mechanics:

```sh
STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"
AXIOM_INDEXER_ROOT=../axiom_indexer
python3 "$AXIOM_INDEXER_ROOT/scripts/check_constitution.py" \
  --stdo-store "$STDO_STORE"
test "$(shasum -a 256 \
  "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" | cut -d ' ' -f 1)" = \
  dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
```

Require Product inventory SHA-256
`7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
program-schema SHA-256
`61c9d26fabb1d844f643712632f6a6551a1c6f7f8ddfef604673e57b7c6b3b7b`,
and output-contract SHA-256
`fd0996009b890e464399863e1f16bb9b9ca7820cb5aa04e95244618849983694`.

After coordinated child-tag creation, ordinary and release qualification use
only `refs/tags/axiom_indexer/v2.5.0-rc.4` and bind its annotated tag object,
commit-B peel, tree, Project Subtree tree, and the same seven-member inventory.
The mutable sibling is authorized construction evidence only. Stop on any
mismatch or on use outside that boundary before the immutable cut exists.

## 2. Validate the compression and index

Validate the selected `a_c.STDO` compression using invocation-local bindings:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" validate \
  --program \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/axiomatic-program.json \
  --bindings \
    build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/bindings.json \
  --emit-map /tmp/stdo-representation-map.json
```

Compare the emitted logical constraint index with:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/
  logical-constraint-map.json
```

Identical compression, bindings, and dependency bytes must reproduce the same index.
The dogfood binding file contains installation-local physical paths and is not a
portable Product member.

## 3. Use the native skill

The native skill in this source candidate is repriced to the exact RC4
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
STDO_STORE="${STDO_STORE:-$HOME/Library/Application Support/STDO}"
stdo --store "$STDO_STORE" verify v2.5.0-rc.4 \
  --manifest-sha256 4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e
python3 -m json.tool stdo_representation.json >/dev/null
```

Revision 15 of the project frame basis is accepted at SHA-256
`e55baf9e244be377140374636b2ec8bde361aec38ee27f260daba02baef2342e`.
Product-owner decision SHA-256
`ecad96e450c97bc3ad276bf1d541bda7fae860a88363451e851be689f6b57a92`
binds those exact bytes. `stdo_representation.json` names that decision in its
`reference_frame_bases` relation; it does not infer activation from this guide
or reuse revision 13. Verify the binding with:

```sh
stdo --store "$STDO_STORE" status \
  --definition stdo_representation.json --verify
```

This acceptance governs the continuing RC4-cohort source candidate. It does not
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
