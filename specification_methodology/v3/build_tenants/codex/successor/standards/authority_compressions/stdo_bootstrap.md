---
kind: authority_compression_asset
asset_ref: authority-compression://stdo/bootstrap/v1
source_refs:
  - ../FOUNDATIONS.md
  - ../TRANSFORMATION_LIBRARY.md
  - ../SPEC_METHOD.md
  - ../REFERENCE_FRAME_METHOD.md
  - ../STDO_REFERENCE_FRAME_BASELINE.md
  - ../RELEASE_METHOD.md
  - ../schemas/product-definition.schema.json
source_digests:
  FOUNDATIONS.md: e6990f703e2906c99ac822d5e9cceff489e43645a4c1ce472f924e7bae0f6632
  TRANSFORMATION_LIBRARY.md: 53a7ca66b0adfb6ebf49e99e602caa90e11b575edb82efe3e9639a415a0aa783
  SPEC_METHOD.md: 76897691b91a05c4a3756d8c6d0bae336684c09096daa67166e0b4e785f0626d
  REFERENCE_FRAME_METHOD.md: 44bb25eacd05550240d31ef318dc2c23db2b8a147ba1b8daa342f688d343e488
  STDO_REFERENCE_FRAME_BASELINE.md: ca38b577b2cb5ffddbcc7692857cfaaad2e9f686a3fdf2bf534c7c008de2633b
  RELEASE_METHOD.md: 26f48744f6344f11237f78ddc8a7012f0d85abf20043fcf1a8b84942bfb19373
  schemas/product-definition.schema.json: e0a3b544dae6c83bf941096b440700d02fa988fd2767f3b4ab297a1a03f67abf
compression_profile: discovery_bootstrap_v1
target_prompt_families:
  - bootstrap
generated_by: codex
generated_at: 2026-10-12
stale_if_source_digest_changes: true
---

# STDO Discovery Bootstrap

The [Foundations](../FOUNDATIONS.md) and [Transformation Library](../TRANSFORMATION_LIBRARY.md)
organise shared premises and transformation families. Detailed owners retain
their exact applicability, result domains and operation grants. Use a sufficient
reference frame for the selected claim; these names supply no compulsory
stages, new record schema or automatic authority.

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
6. Resolve the applicable accepted Project Reference-Frame Basis or its
   declared composition. Bind the exact outcome, basis and existing work grant.
   Use direct Writer entry when that configuration permits it and one capable
   context is sufficient. For material coordination, use its Executive frame
   or declared project equivalent and activate only the smallest dependency-ready
   frontier. Determine required evaluations from their owning applicability
   conditions; unknown applicability remains unresolved. A role name grants no
   effects and Executive performs no file or Git mutation.
   Executive attention is event-driven by default; supervision exceptions and
   conserved assurance remain owned by
   `STDO_REFERENCE_FRAME_BASELINE.md#event-driven-executive-attention`.
7. Load the Product Definition's bound `WHAT`, local constitutional relations,
   `HOW`, work carriers, composition contracts, and exact source material only
   as required by that activation and governed scope. A prompt, summary,
   symbolic map, or prior result may route attention but cannot replace current
   source authority or a closed frame result.
   When the selected evaluation needs the cross-interface refinement, acquire
   `STDO_REFERENCE_FRAME_BASELINE.md#derived-end-to-end-interface-integration-frame`;
   it separates design, actual-boundary, runnable-path and user-usability claims.
   Its computational whole-path refinement covers material composition and
   recurrence; inspect the causal cone within access authority even when the
   mutation grant names narrower write territory.
8. Reuse applicable computed facts, recorded judgments and original owner
   rulings through their exact source/evidence routes. Refresh affected support
   on a material invalidator; do not reclassify merely because a session or role
   changed. Closure requires satisfied applicable conditions, not a review
   event. The raw owning standards decide sufficiency and reserved authority.

Derived guidance preserves source permissions and conditions as well as
prohibitions. A digest does not establish that fidelity. Complete enclosing
admission permits applicable established facts; a function or role boundary
alone does not require repeating their derivation. Material invalidation and
required independent judgment retain their own checks. Bind findings and test
predicates to the supported operating/threat model. Retirement is the default
for superseded responsibility; source law places the burden on retention.

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
