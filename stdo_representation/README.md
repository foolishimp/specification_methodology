# STDO Representation

STDO Representation `2.5.0-rc.4` is the coordinated candidate canonical
`a_c.STDO` semantic compression of exact STDO `v2.5.0-rc.4`, a deterministic
logical constraint index over that compression, and a concise native skill for
using both. An LLM authors and reviews meaning. The exact same-version Axiom
Indexer candidate supplies URI resolution, basic validation, index
instantiation, and exact ordered string joining.

```text
Source STDO v2.5.0-rc.4
  -> LLM-authored a_c.STDO 2.5.0-rc.4 compression
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
  `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/`;
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

- Source STDO: `v2.5.0-rc.4`, installed-manifest SHA-256
  `4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`;
  standards member aggregate
  `504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656`.
- Axiom Indexer: exact `v2.5.0-rc.4` candidate at intended ref
  `refs/tags/axiom_indexer/v2.5.0-rc.4`, seven-member inventory SHA-256
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
  and executable SHA-256
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.

The Axiom tag object and commit-B coordinates do not exist until coordinated
child-tag creation. Candidate mechanics are construction evidence until that
exact immutable cut is created and qualified.

The bootstrap STDO Representation Product remains the accepted immutable
[`v0.1.0-rc.1`](https://github.com/foolishimp/stdo_representation/releases/tag/v0.1.0-rc.1).
Its annotated tag object is
`46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`; it peels to commit
`b127ee9a0362f85d4875ae59664ecfcd13028d9c` and tree
`15f9beb360836386ce9607dd31e30d0c8b5cd830`. The annotated `v0.1.0` tag is
the mutable highest-published-RC selector, not the immutable Product identity.
The active source candidate is STDO Representation `2.5.0-rc.4`, exactly
matching the represented STDO suffix while retaining its own Product and RC
identity.

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

`stdo_representation.json` selects the exact locally tagged and verified Source
STDO `v2.5.0-rc.4` cut frozen by coordinated commit A. Project frame basis
revision 15 is accepted at SHA-256
`e55baf9e244be377140374636b2ec8bde361aec38ee27f260daba02baef2342e`.
Product-owner decision SHA-256
`ecad96e450c97bc3ad276bf1d541bda7fae860a88363451e851be689f6b57a92`
accepts those exact bytes, and the overlay binds that decision and basis.

Accepted revision 13 and its decision remain exact historical authority for
the published STDO Representation `2.5.0` RC1 subject. Revision 15 separately
governs the continuing RC4-cohort source candidate; it neither changes RC1 nor
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
stdo verify v2.5.0-rc.4 \
  --manifest-sha256 4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e
python3 -m json.tool stdo_representation.json >/dev/null
```

The JSON parse establishes syntax only. Product Definition status verifies the
accepted basis relation; project-local checks establish only the additional
properties they report.
