# F3 repair return

Worker `/root/repair_skills_pins` returns to Executive `/root` under
[ACTIVATION.md](ACTIVATION.md). F3 is reproduced and repaired. This is author
verification of a bounded implementation repair, not independent assessment,
host qualification, Product acceptance or release.

The original package's current provider-manifest pin and its matching T-003
source entry both named `d3fdbea6…`; the actual manifest was `1801cc3b…`.
The T-003 project-build design pin named `d50294d5…` while the source was
`8df6f695…`. Seven other selected route files matched. The prior verifier only
checked hash spelling, so its package result could not detect this divergence.

## Changed realization

- `build_tenants/codex/tests/verify_package.py` compares the selected current
  Product/tool whole-file routes at the recognized repository tenant location,
  or in an explicitly supplied `--repository`. The provider's top-level pin and
  its matching selected source entry must agree even when external roots are
  absent. Portable package and installed-copy custody still work and report
  external source currentness as `not_performed`.
- `build_tenants/codex/tests/test_source_routes.py` supplies six discriminating
  regression cases using disposable repositories and packages.
- The Codex README and design declare the exact new checking scope. Runtime
  provider selection and permissions remain activation-owned.
- `specification/composition/REPRESENTATION_MANIFEST.json` retains its 22-member
  population and refreshes only the two files returned by the origin repair
  Worker: `ac_project.py` (`8a87775e…`) and `project-build.md` (`fb4655dd…`).
  The Codex source routes refresh the three affected digest occurrences, and
  its inventory is sealed after all package edits.

All 17 untagged historical source entries and the selected method remain
unchanged against HEAD. Frozen T-003 native runs and prior inventories are not
rewritten. No Claude package member carries a copied provider-manifest pin;
its existing 14-file inventory remains current without an edit.

## Verification

The new current-source check rejected the original live routes with
`current source digest mismatch: product:specification/composition/REPRESENTATION_MANIFEST.json`.
The repaired package check passes 14 members, 21 local links and nine distinct
current source files. All 22 provider members match the refreshed manifest.

The six regression cases passed:

1. Matching current routes succeed while absent historical sources are not
   acquired or refreshed.
2. Changed Product and tool files fail even after the package inventory is
   refreshed.
3. Stale current digest declarations fail despite a fresh package inventory.
4. A portable installed-copy custody check succeeds with external currentness
   unperformed; selecting its source repository enables that check and catches
   later tool-source change.
5. Contradictory provider duplicate pins fail without external source roots.
6. A current source path cannot escape its named Product root.

Actual CLI checks also passed for a disposable portable package/installed copy
and for that copy with an explicit repository. [CHECKS.json](CHECKS.json) retains
their observed result scopes. Skill-creator's `quick_validate.py` reports valid;
the unchanged Claude package checker reports no errors. Scoped `git diff --check`
passes.

Exact current identities:

| Subject | SHA-256 |
| --- | --- |
| Representation provider manifest | `52370df979656210e7582b2a740d2d40b6356ed466aa1ab580490892347b624e` |
| Codex package inventory | `803226b6f06b99fd8d2cc1ea16a4e830fb419b9ae78affb1d052c0f24825fb88` |

No host/model invocation, shared installation, Git mutation, commit or push was
performed. The new verifier checks the selected source-route files; it does not
recursively interpret arbitrary external registries or establish their semantics.
Source/provider or package changes invalidate the corresponding current check.
