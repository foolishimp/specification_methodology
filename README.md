# Specification Methodology Repository

The Git repository is `foolishimp/specification_methodology`. In this workspace,
the checkout directory is `specification_methodology`; the STDO source project
is its `specification_methodology/` child. Select a child Product before working
on its source.

This repository co-locates three peer source projects:

| Project | Purpose |
|---|---|
| [`specification_methodology/`](specification_methodology/) | Specification Methodology and the STDO toolchain manager |
| [`axiom_indexer/`](axiom_indexer/) | LLM-first `a_c` authoring, mechanical validation, logical-map projection, and ordered joining |
| [`stdo_representation/`](stdo_representation/) | Release-matched `a_c.STDO` compression, constraint index, and native Codex and Claude instructions |

The repository root is coordination only. It is not a fourth Product, has no
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

Work from the applicable child root. From this root, inspect all Product
Definitions without changing them:

```sh
stdo fleet status --root .
stdo fleet verify --root .
```

Install the current source toolchain for development with:

```sh
pipx install --force ./specification_methodology
```

Existing immutable releases remain at their original repositories and refs.
Mutable Specification Methodology source defines a successor shared-source ref
and subtree-evidence law, but that source is not publication authority for a
consumer until released and adopted. A child using the currently installed
method must define any alternate Git spelling as its own Product-local release
profile. Each child still requires its own frozen candidate, authority,
qualification, and publication decision.

## Coordinated Release-Matched Cohort

The Product owners have declared one explicit release relation for STDO and its
indexes. When that relation is selected, the exact normalized cohort version
must match all five required assets:

1. Specification Methodology/STDO standards corpus;
2. distributed Claude and Codex `spec` plugin;
3. Axiom Indexer mechanics Product;
4. STDO Representation Product; and
5. released `a_c.STDO` program and logical constraint map with complete exact
   source-member and digest closure.

The first complete cohort is publicly frozen at `2.5.0-rc.4`. Source STDO and
the `spec` plugin are identified by
`specification_methodology/v2.5.0-rc.4` at commit
`7a25668a8fecfd26f895759af3bec4708727964a`; Axiom Indexer, STDO
Representation, and the released `a_c.STDO` program/map are identified by their
project-qualified RC4 tags at coordinated commit
`a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2`. The exact commit-B published gate
verified the complete atomic 13-ref transaction.

RC5 remains the exact published predecessor. The selected RC6 successor
contains the reviewed Executive steel-thread guidance and its matched source,
plugin and child indexes. Its bounded work and qualification are retained in
the [RC6 release carrier](specification_methodology/.ai-workspace/comments/codex/20260906T130745Z_rc6_release/README.md).
Current selection does not assert publication, Product acceptance or adoption.

This relation does not make the root a Product or merge the three child
Products. It makes publication incomplete if one required asset is stale,
missing, differently versioned, or derived from another STDO cut. Read
[`STACK_RELEASE.md`](STACK_RELEASE.md) and qualify the active
[`stack_release.json`](stack_release.json) with
`scripts/check_stack_release.py`.
