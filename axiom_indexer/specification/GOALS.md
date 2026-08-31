# Axiom Indexer Goals

## GOAL-001 — Dogfood the smallest useful Axiom Indexer

Status: completed

Build one LLM-first loop:

```text
exact a_c URI + source URIs + frame URIs + tight skill instructions
  -> LLM-authored axiomatic program
  -> URI resolution and basic validation
  -> diagnostics
  -> LLM repair or use
  -> Executive-selected labeled sections -> exact string join
```

`a_c` compresses the operative meaning of documents into a logical constraint
map. The map may be larger than its prose source. Its value is explicit,
reusable logic, not byte reduction.

### Completion

- One portable native skill tells an LLM how to author and use the program.
- One small tool resolves symbolic URIs, instantiates the map, and returns
  structured diagnostics.
- The same tool joins an LLM-supplied ordered list of labels and text without
  selecting, rewriting, or interpreting its content.
- The validator checks identity, reference, source binding, clause shape, and
  residual closure without authoring semantic content.
- The Tool's own Goals, Intent, Product, and requirements are represented by a
  valid program.
- A fresh agent uses that program, without the complete source corpus in its
  initial context, to perform one useful Product task.
- The observed result drives at least one retained improvement to the skill,
  program, validator, or Product.
- Acting as Executive, an LLM uses the map and selected reference frames to
  build one request whose frame URIs, purposes, and source routes remain
  visible for debugging.

### Disposition

GTL carrier composition, automatic frame selection, fixed multi-model prompt
systems, semantic approval, and carrier admission remain later Product work.
The retained self and ABIogenesis dogfood evidence establishes sufficient
usefulness to select a bounded first publication wave.

## GOAL-002 — Publish Axiom Indexer 0.1.0

Status: completed

Publish the current repository-carried MVP without expanding its Product
meaning.

### Completion

- The exact Product member set, release claims, dependencies, exclusions, and
  first-release successor disposition are declared in `releases/v0.1.0.md`.
- One concise project frame set covers semantic compression, symbolic
  integrity, validation boundaries, dogfood usefulness, and exact release
  identity under the installed STDO basis.
- The Product owner accepts the exact frame-set bytes and the Product
  Definition names that acceptance without relying on ambient conversation.
- Pre-RC qualification passes against one frozen candidate carrier.
- An annotated immutable `v0.1.0-rc.<n>` cut and annotated `v0.1.0` selector
  are published over the same commit and verified remotely.
- Independent exact-cut review and Product-owner acceptance bind the immutable
  RC tag object, peeled commit, tree, member set, and claim bytes.

### Release disposition

- immutable Product tag: `v0.1.0-rc.1`;
- tag object: `e7afc8a42a7123aebe91cb7582cb037b1aae612d`;
- peeled commit: `dc3e00998da36dae6ac7b76b340431a85096c83c`;
- repository tree: `8c9ad5f5e99a60c18fb8c1802471753afb226272`;
- Product member-set SHA-256:
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`;
- remote: `https://github.com/foolishimp/axiom_indexer`; and
- acceptance:
  `../.ai-workspace/decisions/20260831T001139_v0.1.0_rc1_acceptance.json`.

### Boundary

This goal authorizes release authority, qualification, carrier publication,
and exact-cut acceptance for the declared MVP only. It does not authorize GTL,
semantic acceptance, carrier admission, automatic frame selection, a prompt
engine, or changes to the core implementation and native skill merely to add
release ceremony.

## GOAL-003 — Enter the Specification Stack monorepo

Status: active

Move the unchanged Axiom Indexer source project and complete history under the
coordination-only Specification Stack root. Preserve the accepted Product,
Product Definition, release objects, relative tool and skill topology, and
independent authority. Co-location creates no composition and does not replace
the exact released dependency selected by another Product.
