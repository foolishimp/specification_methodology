# Axiom Indexer Goals

## Current Goal

Status: exact RC4 mechanics baseline supplies T-009 M02's selected dependencies;
no generic mechanics defect demonstrated and no Product code change required

Supply the smallest sufficient generic mechanics for faithful, reproducible
axiomatic indexing and native STDO use. Existing resolution, validation,
diagnostics, map generation and exact joining are the starting point. A useful
contribution may be validated reuse; a new capability requires a demonstrated
mechanical gap and its own exact Product/requirement/design authority.

The [overall STDO delivery goal](../../specification_methodology/specification/GOALS.md#goal)
owns the shared outcome. The existing combined
[Representation T-009](../../stdo_representation/.ai-workspace/tickets/active/T-009-deliver-qualified-native-stdo-use-with-axiom-indexer.md#delivery-timeline)
owns delivery tracking for this provider/consumer relation: M01 identifies
actual gaps, M02 supplies the selected mechanics, and M03/M04 consume their
exact results for regeneration and native qualification. This creates no
duplicate Indexer ticket or independent milestone ledger. The owner's direct
implementation grant and bounded Writer activation are recorded in
[T-009](../../stdo_representation/.ai-workspace/tickets/active/T-009-deliver-qualified-native-stdo-use-with-axiom-indexer.md#implementation-admission-and-writer-activation).

The Executive keeps mechanical facts distinct from semantic judgments and
owner rulings. STDO-specific authoring and frame use stay with Representation;
worksite classification producers remain with their declared owners. No
semantic acceptance, automatic frame selection, context-budget engine or
runtime is selected. Qualification and any release identity stay Product-local;
published RC4 mechanics and their valid evidence remain available throughout.

The [actual T-009 baseline](../../stdo_representation/dogfood/t009-m01/run-001/README.md)
reproduced the exact Representation index, passed all 15 existing mechanical
tests under normal and optimized Python, and refused eight malformed actual-
program variants with stale maps removed. Representation consumes these exact
results for M03. Its instruction repair remains at that Product; this Goal
does not close native qualification, accept a Product or publish a successor.

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

Status: completed

Move the unchanged Axiom Indexer source project and complete history under the
coordination-only Specification Stack root. Preserve the accepted Product,
Product Definition, release objects, relative tool and skill topology, and
independent authority. Co-location creates no composition and does not replace
the exact released dependency selected by another Product.

### Completion

- The exact source history entered `axiom_indexer/` without rewriting.
- The accepted release objects remain reachable under project-qualified
  archival refs.
- Project-local and root native skill discovery resolve to the unchanged
  canonical skill.
- The full MVP suite passes normally and under optimized Python from the
  nested child root.
- Fleet verification preserves the independent Product Definition.

## GOAL-004 — Cut the release-coupled Axiom mechanics for STDO RC4

Status: completed

Reprice the continuing Axiom Indexer mechanics as a release-coupled asset for
exact Source STDO `v2.5.0-rc.4`. Preserve the accepted `v0.1.0-rc.1` Product
and its evidence as immutable history. Do not absorb the sibling
`a_c.STDO` semantic program or logical map into this Product.

### Completion

- The Product Definition selects and verifies immutable
  `stdo://releases/v2.5.0-rc.4/` with installed-manifest SHA-256
  `4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e`.
  Mutable source bytes or a provisional digest shall not substitute for that
  basis.
- Live Product and requirement law makes the Axiom product-local cut suffix
  equal the exact selected STDO cut suffix while preserving distinct Product,
  namespace, member, and acceptance identities.
- `releases/v2.5.0.md` declares the exact coordinated candidate, its conserved
  seven-member mechanics inventory, predecessor dispositions, dependency
  basis, exclusions, and project-qualified future refs.
- A deterministic project checker verifies the exact basis, coupled cut
  identity, seven Product members, inventory digest, release claims, and
  exclusion of sibling semantic program and map bytes.
- The unchanged implementation passes its complete unit and falsifier suite
  normally and under optimized Python from the nested child root.
- STDO Representation separately re-authors affected RC4 semantic compression
  entries, regenerates its deterministic map with this exact Axiom mechanics,
  and binds the released Axiom cut as an explicit dependency.

### Release boundary

The qualified immutable ref is
`refs/tags/axiom_indexer/v2.5.0-rc.4`. This goal constructed and qualified that
candidate but granted no tag, branch, selector, remote, or Product-acceptance
effect. The later direct coordinated-release grant published the exact cut in
one atomic Specification Stack transaction. Publication does not accept
Product meaning. After immutable publication, any Axiom qualifying-byte repair
requires another coordinated Source STDO and Axiom cut rather than an
independently numbered Axiom RC.

The verified RC3 Product Definition adoption is retained only as the completed
construction transition from the accepted RC1 basis. It is not the release
basis and no Axiom RC3 cut will be published.

### Completion evidence

- immutable tag: `refs/tags/axiom_indexer/v2.5.0-rc.4`;
- tag object: `4750e09639c118f1097d4ea046fe23d26713f96b`;
- peeled commit: `a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2`;
- repository tree: `093302db57bfb2e7beeed7f02dfc6d7090921a15`;
- Axiom subtree: `3f71c3c2df99008b9521e338a7837c553f87173a`;
- seven-member Product inventory SHA-256:
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`;
- matched Source STDO tag:
  `refs/tags/specification_methodology/v2.5.0-rc.4`; and
- the root published-cohort gate returned valid with zero failures after the
  atomic 13-ref transaction.
