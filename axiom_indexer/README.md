# Axiom Indexer

Axiom Indexer is an LLM-first semantic-compression tool. An LLM turns exact
documents into a source-linked axiomatic program. A small resolver/validator
checks URI, shape, reference, grounding, and residual closure, then
instantiates the unchanged program as a logical constraint map.

The map may be larger than the prose. Its value is explicit reusable logic:
an LLM can traverse constraints consistently and re-enter exact sources without
reconstructing the whole corpus from textual similarity.

```text
exact a_c URI + source URIs + frame URIs + native skill
  -> LLM-authored axiomatic program
  -> validate -> diagnostics -> LLM repair
  -> logical constraint map
  -> Executive-selected labeled sections -> exact string join
  -> LLM use with source re-entry when required
```

Code does not author, repair, select, or accept meaning. It performs symbolic
late binding and declared mechanical checks. Logical identity uses URIs;
physical paths, line numbers, and member counts do not become semantic
identity.

## MVP

- [`skills/axiomatize-corpus/`](skills/axiomatize-corpus/) is the native LLM
  instruction surface.
- [`build_tenants/core/code/ac.py`](build_tenants/core/code/ac.py) resolves,
  validates, instantiates, and joins LLM-supplied labeled text.
- [`dogfood/self/`](dogfood/self/) contains the Product's first self-program,
  validation report, and logical map.
- [`dogfood/abg/`](dogfood/abg/) contains the first external map and an
  Executive-authored request that visibly names its reference frames.

Validate the self-program:

```sh
python3 build_tenants/core/code/ac.py validate \
  --program dogfood/self/axiomatic-program.json \
  --bindings dogfood/self/bindings.json \
  --output dogfood/self/validation-report.json \
  --emit-map dogfood/self/logical-constraint-map.json

python3 build_tenants/core/code/ac.py join \
  --input dogfood/abg/executive-sections.json \
  --output dogfood/abg/executive-request.txt
```

Run the focused tests:

```sh
python3 -m unittest discover -s build_tenants/core/code -p 'test_*.py' -v
```

The same canonical skill is discoverable by Codex through `.agents/skills/`
and by Claude through `.claude/skills/`.

## Release

The accepted first Product remains immutable `v0.1.0-rc.1`. Its exact subject,
claims, dependencies, exclusions, and qualification boundary are declared in
[`releases/v0.1.0.md`](releases/v0.1.0.md).

The immutable Product identity is annotated tag `v0.1.0-rc.1`, tag object
`e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeling to commit
`dc3e00998da36dae6ac7b76b340431a85096c83c`. The unqualified `v0.1.0` tag is
only the mutable highest-published-RC selector.

The selected coordinated successor is `axiom_indexer/v2.5.0-rc.5`.
[Its release record](releases/v2.5.0.md) and [cohort carrier](../stack_release.json)
bind the exact seven-member mechanics, matched Source STDO and qualification
claims. RC5 adds explicit authored frame-index dependency closure and
reference-only/unchanged-content materialized projections. Original validation,
resolution and pure joining remain available. RC4's exact bytes and observations
remain at its immutable tag.

The caller's Product Definition identifies its own operative basis. For this
source project, use the shared manager:

```sh
stdo status --definition stdo_default.json --verify
```

From the coordinated repository root, use the shared release checker against
the exact RC5 carrier for content/ref/publication integrity. The retained
`check_constitution.py` is an explicitly historical RC4 audit, not the RC5
qualification command. Publication does not by itself accept Product meaning.

## Boundary

Validation proves declared structure and resolution, not semantic truth,
completeness, fidelity, or usefulness. The source remains authority. The LLM
reviews meaning and revises candidates.

The working artifact is the `a_c.text` authoring surface. Mapping it to a
complete admitted `a_c` model `M_b` remains an explicit residual, not an MVP
claim.

GTL composition, automatic frame selection, fixed prompt-template systems,
semantic acceptance, and carrier admission remain deferred. The MVP joiner
only concatenates the exact labels and text supplied by the LLM.

Release publication is a separate lifecycle over this bounded Product; it does
not become another Product capability. The source-project frame basis and exact decision are bound by
`stdo_default.json`; this README does not separately maintain their identities.
Frame acceptance does not establish Product acceptance or publication.

## Authority order

1. [`specification/GOALS.md`](specification/GOALS.md)
2. [`specification/INTENT.md`](specification/INTENT.md)
3. [`specification/PRODUCT.md`](specification/PRODUCT.md)
4. [`specification/requirements/`](specification/requirements/)
5. [`specification/REFERENCE_FRAME_BASIS.md`](specification/REFERENCE_FRAME_BASIS.md)

The layout-neutral Product Definition is
[`stdo_default.json`](stdo_default.json).
