# Specification Stack

This repository co-locates three peer source projects:

| Project | Purpose |
|---|---|
| [`specification_methodology/`](specification_methodology/) | Specification Methodology and the STDO toolchain manager |
| [`axiom_indexer/`](axiom_indexer/) | LLM-first `a_c` authoring, mechanical validation, logical-map projection, and ordered joining |
| [`stdo_representation/`](stdo_representation/) | Source-linked `a_c.STDO` map and native Codex and Claude use instructions |

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
  -> Axiom Indexer optional a_c compression and mechanical checks
  -> STDO Representation reusable a_c.STDO map and native skill
  -> project-owned Executive frame selection, evaluation, and action
```

`a_c` and STDO Representation are attention and consistency tools. They do not
replace Source STDO or perform downstream semantic interpretation.

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
Future monorepo release naming is intentionally blocked until the Release
Method defines project-qualified tags and project-subtree identity.
