# STDO Representation

STDO Representation 2.5.0 is the canonical `a_c.STDO` semantic compression of
STDO 2.5.0, a deterministic logical constraint index over that compression,
and a concise native skill for using both. An LLM authors and reviews meaning.
Accepted Axiom Indexer `v0.1.0-rc.1` supplies URI resolution, basic validation,
index instantiation, and exact ordered string joining.

```text
Source STDO 2.5.0 (exact cut v2.5.0-rc.2)
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
  `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.2/`;
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

- Source STDO: `v2.5.0-rc.2`, installed-manifest SHA-256
  `313e23116623a3bfbe96d279e089489aac466584982e1c34171ef244f0ec680a`;
  standards member aggregate
  `a5910bc56b491b5c520910e7bdad0949c1283e8b71951f1079e1fd86f59d20e7`.
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

`stdo_representation.json` selects exact published Source STDO
`v2.5.0-rc.2`. Project frame basis revision 14 is accepted at SHA-256
`6cc05636ea00797e44f6ebb661d342d5b8cfb59cbde2a81059062dddf6eb106f`.
Product-owner decision SHA-256
`68394d5118a6250972aa06db995a5d020c2f09996c90b0dfe70d4d8e908e8eba`
accepts those exact bytes, and the overlay binds that decision and basis.

Accepted revision 13 and its decision remain exact historical authority for
the published STDO Representation `2.5.0` RC1 subject. Revision 14 separately
governs the continuing RC2-basis source candidate; it neither changes RC1 nor
publishes or accepts another immutable Representation RC.

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
stdo verify v2.5.0-rc.2
python3 -m json.tool stdo_representation.json >/dev/null
```

The JSON parse establishes syntax only. Product Definition status verifies the
accepted basis relation; project-local checks establish only the additional
properties they report.
