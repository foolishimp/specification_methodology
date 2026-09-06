# STDO Representation Quickstart

Use the RC5 program, map, complete native bundle and exact Axiom dependency
bound by [the release record](releases/v2.5.0.md). The instructions below assume
those exact Products have been provisioned through the selected cohort. A
source checkout is a construction subject until its exact release is verified.
External callers retain their own Product Definition and accepted work/frame
configuration; a represented rule does not silently replace that basis.

## 1. Verify the dependencies

From the coordinated Git source, the shared release checker verifies exact
content, full member inventories and source closure:

```sh
python3 scripts/check_stack_release.py --phase content \
  --revision refs/tags/stdo_representation/v2.5.0-rc.5
```

Run that command at the repository root with the exact annotated cohort tags
available. Bind their acquired identities to the retained publication receipt.
The `published` phase verifies the immediate publication snapshot, including
`main == commit B`. A permitted later bookkeeping commit changes that snapshot
without invalidating the immutable releases. Prepublication construction uses
the content and local-ref phases under its explicit grant.

The shared manager verifies the exact Source STDO Install:

```sh
stdo verify v2.5.0-rc.5 \
  --manifest-sha256 3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f
```

Use the Axiom Product root selected by the caller's dependency record, verify
its seven-member inventory and executable/schema/contract digests against the
release record, and set `AXIOM_INDEXER_ROOT` to that exact installation. Use
`REPRESENTATION_ROOT` for the corresponding nine-member Representation Install.
Source archives contain additional authority and evidence; only the declared
members constitute each Product. Mutable sibling code does not substitute for
the selected dependency.

## 2. Validate the compression and index

Prepare an invocation-local Binding Set in an authorized work directory:

```json
{
  "kind": "axiom-indexer.binding-set",
  "schema_version": 1,
  "bindings": [{
    "uri_prefix": "stdo://releases/v2.5.0-rc.5/",
    "path": "/absolute/path/to/the/verified/RC5/Install"
  }]
}
```

The path is the Install root containing `standards/`. Set `STDO_BINDINGS` to
that file. From the selected Representation Product root, validate to stdout:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" validate \
  --program build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.5/axiomatic-program.json \
  --bindings "$STDO_BINDINGS"
```

To reproduce the map, add `--emit-map` with an explicitly writable destination
and compare its bytes with the released `logical-constraint-map.json` beside
the program. Binding Sets are local evidence, not portable Product members.

## 3. Use the native skill

Codex discovers `.agents/skills/stdo-representation`; Claude discovers
`.claude/skills/stdo-representation`. Both resolve the same canonical bundle.
Ask the agent to use `stdo-representation` for the bounded task. It verifies
identities, reads the map, selects visible source-grounded frames, recovers
sufficient task facts and valid judgments/rulings, re-enters source as needed,
and returns the warranted result under the existing grant.

Direct sufficient work does not require an Executive appointment, new ticket
or review round. Required independent assessment and reserved owner decisions
remain conditions when their actual reference frames apply.

## 4. Join an Executive request

For an actual bounded handoff, write an ordered array of caller-authored
`{"label": "...", "text": "..."}` rows in an authorized work directory:

```sh
python3 "$AXIOM_INDEXER_ROOT/build_tenants/core/code/ac.py" join \
  --input /authorized/path/ordered-sections.json
```

The pure joiner returns the exact labeled text to stdout. It selects no
frames, rewrites no content and invokes no model. File output requires the
applicable grant; omit `--output` for read-only use.

## 5. Check the accepted basis

For this source project:

```sh
stdo status --definition stdo_representation.json --verify
```

Follow that Definition's exact frame declaration and digest-bound decision.
For an external project use its own Definition. Frame acceptance, exact-cut
Product acceptance, publication and consumer adoption are separate relations;
this guide does not create any of them.

## 6. Use explicitly selected frame indexes

The [frame-index guide](skills/stdo-representation/references/frame-index-use.md)
provides the released RC5 commands. Select the complete-update Worker or
Reviewer index only when its declared question and scope apply. Ordinary tasks
use relevant actual source frames and map entries. Both views preserve the
same selected supporting closure and uncertainty; the materialized view
resolves unchanged authored content.

Supply actual task facts, residual judgments and owner rulings separately.
A plan digest does not grant operation acceptance; stale source evidence does
not complete an update. Unknown effects require permitted observation before
dependent completion or unsafe retry, without inventing a new failure or
revoking still-applicable original authority.

## Historical paths

Earlier RC4 cuts and `dogfood/t009-frame-projection/run-001` through `run-004`
remain exact historical evidence. The semantic_compile, GTL, JSON Schema and
prior carrier tools remain outside the current Product and installed path.
