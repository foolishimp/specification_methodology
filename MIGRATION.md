# Monorepo Migration Evidence

This is coordination evidence, not Product or release authority.

## Frozen Source Inputs

| Project | Commit | Tree |
|---|---|---|
| Specification Methodology | `4f2a5ddcd7a021bf663a6e0714fe688f654882e2` | `7eebeddcd448fc31041040f2b4637e7535f1cc1f` |
| Axiom Indexer | `1fe3ef2af41b6df76d34d1a2fd1145d71e84a639` | `ae10199814a5a61ea93fc0adfac986c29273c5dd` |
| STDO Representation | `9eface352e78ce76b437025e82eb84ab41bbfa89` | `81789b7cc3c61f26dfd5397d5cbeda383ccac84c` |

Specification Methodology was moved without byte changes in commit
`0750ede`. Axiom Indexer was imported without squashing in `4c835cd`. STDO
Representation was imported without squashing in `e89a62d`.

## Preserved Release Objects

- STDO `v2.5.0-rc.1`: tag object
  `42f59b6cd24071d9c445a29ae2a691cf0828211e`, peeled commit
  `ca6694314c4e9a56d3facae3eef06fe2792104c9`;
- Axiom Indexer `v0.1.0-rc.1`: tag object
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
  `dc3e00998da36dae6ac7b76b340431a85096c83c`;
- STDO Representation `v0.1.0-rc.1`: tag object
  `46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`, peeled commit
  `b127ee9a0362f85d4875ae59664ecfcd13028d9c`.

Existing STDO tag refs remain unchanged. Colliding Axiom Indexer and STDO
Representation tag objects are retained under
`refs/tags/legacy/<project>/...`; their branches are retained under
`refs/heads/archive/<project>/...`.

The predecessor GitHub repositories remain authoritative for their published
release URLs until an independently verified remote cutover. They are not
deleted or archived by this migration.

## Boundary

The root contains no Product Definition, `PRODUCT.md`, or licence. Each child
retains its own Product and licence disposition. Future releases are blocked
until project-qualified tag refs and project-subtree identity are ratified.

## Verification

- The three import-commit subtree trees equal the frozen source trees.
- The three frozen source commits remain ancestors of the integrated branch.
- Original annotated release tag objects and peels reproduce exactly.
- Specification Methodology passes 78/78 tests normally and under optimized
  Python from its nested root.
- Axiom Indexer and STDO Representation pass their complete project checks
  from their nested roots.
- `stdo fleet status --root .` and `stdo fleet verify --root .` find exactly
  three valid, independently governed Product Definitions.
- Root and child native skill links resolve without copying Product members.
- JSON, formatting, lint, diff, and Git object-integrity checks pass.

No remote was changed by the local migration. A remote cutover requires a
separate exact-tree review and explicit publication authorization.
