# STDO Representation

STDO Representation 2.5.0 is the canonical `a_c.STDO` semantic compression of
STDO 2.5.0, a deterministic logical constraint index over that compression,
and a concise native skill for using both. An LLM authors and reviews meaning.
Accepted Axiom Indexer `v0.1.0-rc.1` supplies URI resolution, basic validation,
index instantiation, and exact ordered string joining.

```text
Source STDO 2.5.0 (exact cut v2.5.0-rc.1)
  -> LLM-authored a_c.STDO 2.5.0 compression
  -> validated logical constraint index over the compression
  -> LLM-selected visible reference frames
  -> exact ordered join
  -> native Codex or Claude work with source re-entry
```

The compression or index may be larger than prose. Their value is explicit
reusable constraints and stable source routes, not fewer bytes. Source STDO
remains semantic authority.

## MVP

The selected Product members are:

- the STDO Axiomatic Program compression and logical constraint index under
  `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/`;
- one canonical skill under `skills/stdo-representation/`;
- concise Codex and Claude instruction references in that skill; and
- native discovery symlinks under `.agents/skills/` and `.claude/skills/`.

The Product contains no local engine code. The LLM selects every frame, label,
text value, and ordering choice. The Axiom Indexer joiner only concatenates
those exact strings.

## Use

Start with the [Quickstart](QUICKSTART.md). The normal agent loop is:

1. discover the `stdo-representation` native skill;
2. load the logical constraint index over the exact compression before loading
   broad Source STDO prose;
3. select material frame URIs for the task;
4. show each frame's purpose and Source STDO route;
5. re-enter source when a residual, disagreement, or task requires it;
6. write the ordered labeled context; and
7. invoke the exact Axiom Indexer joiner.

Executive, Worker, and Reviewer are instruction-level context roles imported
from Source STDO. A role label or prompt grants no external authority.

## Exact bases

- Source STDO: `v2.5.0-rc.1`, installed-manifest SHA-256
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`.
- Axiom Indexer: annotated `v0.1.0-rc.1` tag object
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
  `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`.

The bootstrap STDO Representation Product remains the accepted immutable
[`v0.1.0-rc.1`](https://github.com/foolishimp/stdo_representation/releases/tag/v0.1.0-rc.1).
Its annotated tag object is
`46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`; it peels to commit
`b127ee9a0362f85d4875ae59664ecfcd13028d9c` and tree
`15f9beb360836386ce9607dd31e30d0c8b5cd830`. The annotated `v0.1.0` tag is
the mutable highest-published-RC selector, not the immutable Product identity.
The active source candidate is STDO Representation `2.5.0`, matching the
represented STDO line while retaining its own RC and Product identities.

## Evidence and boundary

The initial map-authoring evidence is under
`dogfood/axiom-indexer-v0.1.0-rc.1/stdo-v2.5.0-rc.1/run-001/`. Runtime bindings
and reports are evidence, not portable Product members.

Validation proves declared mechanical structure and resolution only. This
release does not claim:

- a complete admitted `a_c` model;
- semantic truth, completeness, fidelity, or unique interpretation;
- automatic frame selection;
- GTL, GraphFunctions, deterministic prompt packets, rendering, or ABG; or
- authority obtained from a map, skill, validation result, or prompt.

The retained semantic-compiler, GTL, JSON Schema, and historical carrier paths
remain source history and evidence. They are not current Product members or
dependencies.

## Product Definition

The Product owner accepted project frame basis revision 13 at SHA-256
`0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`.
The external decision SHA-256 is
`7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`.
`stdo_representation.json` binds those exact bytes and the decision.

## Authority order

1. [`specification/GOALS.md`](specification/GOALS.md)
2. [`specification/INTENT.md`](specification/INTENT.md)
3. [`specification/PRODUCT.md`](specification/PRODUCT.md)
4. [`specification/requirements/`](specification/requirements/)
5. [`specification/REFERENCE_FRAME_BASIS.md`](specification/REFERENCE_FRAME_BASIS.md)
6. current build-tenant instructions and exact artifacts
7. retained evidence and history

## Focused checks

```sh
stdo verify v2.5.0-rc.1
python3 scripts/check_constitution.py
python3 -m unittest scripts.test_check_constitution -v
```

Project-local checks establish only the properties they report.
