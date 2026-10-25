# Specification Methodology Repository

The Git repository is `foolishimp/specification_methodology`. In this workspace,
the checkout directory is `specification_methodology`. The STDO Specification
Methodology product has two source projects side by side under its
`specification_methodology/` child: `v2/` owns the current STDO 2.* source and
the toolchain manager; `v3/` owns STDO 3 source and standalone native releases
of the same product. Select a child Product before working on its source.

## STDO 3.0.2 release

**STDO 3.0.2 is published as a normal standalone release and GitHub Latest**,
without an RC suffix: [download the release](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology%2Fv3.0.2),
immutable tag `specification_methodology/v3.0.2`. The
[installation instructions](specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md#new-project)
acquire the distributed manager wheel and native manifest. All six assets were
downloaded and verified, followed by a fresh isolated public installation and
portable supplement verification. The [release record](specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/RELEASED.md)
binds the exact identities, evidence and retained qualification limits.

This standalone payload is the methodology and its `spec` plugin, with a separate
bounded representation supplement. It does not select the older v2 matched cohort
or migrate Skills from its installed 3.0.1 basis. Installing a release and adopting
it for a Product remain separate operations.

This repository co-locates six peer source projects:

| Project | Purpose |
|---|---|
| [`specification_methodology/v2/`](specification_methodology/v2/) | Specification Methodology 2.* source and the STDO toolchain manager |
| [`specification_methodology/v3/`](specification_methodology/v3/) | STDO 3 methodology source and standalone native releases; the common payload retains independent tenant construction history |
| [`axiom_indexer/`](axiom_indexer/) | LLM-first `a_c` authoring, mechanical validation, logical-map projection, and ordered joining |
| [`stdo_representation/`](stdo_representation/) | Release-matched `a_c.STDO` compression, constraint index, and native Codex and Claude instructions |
| [`a_c/`](a_c/) | Independent axiomatic-calculus implementations, with Graphify as the first build tenant |
| [`stdo_skills/`](stdo_skills/) | Shared agent-skill requirements with independent Codex and Claude skill build tenants, using static released STDO 3.0.1 |

Both STDO source projects share one release namespace, `specification_methodology`,
and one Product identity. Release tags and rc/release branches keep that
namespace; only the source paths carry the version line.

The repository root is coordination only. It is not a Product, has no
Product Definition, and grants no constitutional, composition, execution, or
release authority. Each child retains its own WHAT, HOW, Product identity,
release records, licence boundary, tickets, and accepted dependencies.

Co-location does not allow mutable sibling source to replace an immutable
Product or Install selected by another child. Use the sibling only when an
exact work relation authorizes source-level development across both projects.

## Development Flow

```text
Specification Methodology prose and reference-frame law
  -> STDO Representation release-matched a_c.STDO compression
  -> Axiom Indexer mechanical validation and constraint index
  -> STDO Representation native skill
  -> project-owned Executive frame selection, evaluation, and action
```

Axiom Indexer and STDO Representation are attention and consistency tools.
`a_c` is the calculus they apply. None replaces Source STDO or performs
downstream semantic interpretation.

The independent [`a_c/`](a_c/) source project realizes the selected published
axiomatic calculus through its own build tenants. Its Graphify tenant does not
depend on v3, Axiom Indexer or STDO Representation and is outside the existing
release-matched cohort. This adds no dependency or member to those Products.

The independent [`stdo_skills/`](stdo_skills/) Product applies the static installed
STDO 3.0.1 basis selected in its [Product Definition](stdo_skills/stdo_skills.json).
Its two skill tenants share requirements while owning their host-specific designs
and tuning. It has a separate lifecycle from the release-matched cohort; its
[local bootstrap](stdo_skills/AGENTS.md) routes construction and tool use.

Work from the applicable child root. From this root, inspect all Product
Definitions without changing them:

```sh
stdo fleet status --root .
stdo fleet verify --root .
```

Install the current source toolchain for development with:

```sh
pipx install --force ./specification_methodology/v2
```

Each child owns its release profile, qualification, and publication decision.
Published cuts retain their immutable refs and release records. A consumer's
Product Definition selects its exact governing cut.

## Coordinated Release-Matched Cohort

This older cohort relation is not selected for the standalone 3.0.2 release above.
For the default scope of an owner instruction to release STDO, follow
[`Meaning Of A Release Request`](STACK_RELEASE.md#meaning-of-a-release-request).

The [RC7 release work](specification_methodology/v2/.ai-workspace/comments/codex/20260915T093130Z_rc7_release/README.md)
records the published and publicly reacquired complete RC7 cohort. STDO,
Axiom Indexer and STDO Representation retain distinct immutable RC7 cuts;
RC6 remains their immutable predecessor.

The [2.5.1 RC1 release](specification_methodology/v2/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/RELEASED.md)
records the published matched cohort, verified public installation and retained
Representation native qualification limits. T-288 and ABI delivery supply no
release dependency. External consumer adoption remains unselected.

The Product owners have declared one explicit release relation for STDO and its
indexes. When that relation is selected, the exact normalized cohort version
must match all five required assets:

1. Specification Methodology/STDO standards corpus;
2. distributed Claude and Codex `spec` plugin;
3. Axiom Indexer mechanics Product;
4. STDO Representation Product; and
5. released `a_c.STDO` program and logical constraint map with complete exact
   source-member and digest closure.

[`stack_release.json`](stack_release.json) records the selected cohort version,
exact Product refs, member inventories, source digests, and index locations.
It links each Product's release record for qualification, publication evidence,
and release history. Publication, Product acceptance, and consumer adoption
remain separate.

This relation does not make the root a Product or merge the three child
Products. It makes publication incomplete if one required asset is stale,
missing, differently versioned, or derived from another STDO cut. Follow
[`STACK_RELEASE.md`](STACK_RELEASE.md) for the release procedure and use
`scripts/check_stack_release.py` to validate the selected cohort.
