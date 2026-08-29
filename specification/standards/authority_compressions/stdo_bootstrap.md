---
kind: authority_compression_asset
asset_ref: authority-compression://stdo/bootstrap/v1
source_refs:
  - ../SPEC_METHOD.md
  - ../RELEASE_METHOD.md
  - ../schemas/product-definition.schema.json
source_digests:
  SPEC_METHOD.md: 4c4158b0b2a888277802237d467c7ea0b7e8e5993f5976f5b929e63a6ed0a85b
  RELEASE_METHOD.md: c690228adf680dc4ef0a391073a5d60e515fbd4b0150b778b6adb4723e3fa9a0
  schemas/product-definition.schema.json: e0a3b544dae6c83bf941096b440700d02fa988fd2767f3b4ab297a1a03f67abf
compression_profile: discovery_bootstrap_v1
target_prompt_families:
  - bootstrap
generated_by: codex
generated_at: 2026-08-29
stale_if_source_digest_changes: true
---

# STDO Discovery Bootstrap

This is a small routing projection. The exact installed release and its raw
owning standards remain constitutional authority.

1. Discover `stdo_<label>.json` definitions recursively from the requested
   workspace scope. Prune `.git`, `.hg`, `.svn`, `.bzr`, `.venv`, `venv`,
   `node_modules`, `vendor`, `site-packages`, `build`, `dist`, `out`, `target`,
   `.gradle`, `.tox`, `.nox`, `.cache`, `.ruff_cache`, `.mypy_cache`,
   `.pytest_cache`, `__pycache__`, `.genesis`, and `.stdo`; refuse symlinked
   Product Definitions. Directory nesting creates no inheritance or
   composition.
2. Select exactly one definition applicable to the requested Product scope.
   Zero or multiple unresolved definitions fail closed.
3. Read `constitution.stdo.basis`. Its immutable release URI and manifest digest
   are the sole operative STDO selection. The source repository and
   `constitution.stdo.selector` are discovery inputs only.
4. Synchronize and verify that exact basis through the STDO toolchain manager.
   Do not substitute mutable authoring source, another installed cut, a moving
   version alias, a cache record, or a project-local copy selected by proximity.
5. Resolve the Product Definition's declared bootstrap entrypoint against its
   named basis. Load raw owning standards whenever this projection is
   insufficient or its source digests are stale.
6. Load the Product Definition's bound `WHAT`, local constitutional relations,
   collective reference-frame bases, `HOW`, work carriers, and composition only
   as required by the active task and governed scope.

`sync` materializes only the already selected exact basis. `adopt --dry-run`
presents a digest-bound plan to the highest-ordinal published immutable RC and
refuses a lagging selector or same-line downgrade; a later mutating `adopt`
must be given that plan digest and must re-derive it unchanged. Fleet adoption
requires the aggregate plan digest. `adopt` is the sole toolchain operation
that may resolve the mutable version-line selector and atomically change a
Product Definition basis after explicit acceptance. Moving the selector alone
never changes a consumer.

Bootstrap targets are relative to the resolved `product.source_project` and
cannot escape or traverse a redirected component. Fleet bootstrap additionally
confines every source project to its authorized root and preflights all targets
before writing. Only one correctly ordered marker span is manager-owned; all
prefix and suffix bytes remain exact project-owned bytes.
