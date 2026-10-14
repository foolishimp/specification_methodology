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
  FOUNDATIONS.md: 33c6892d36ca8bc1b977d872a33932b5b687a487f9ec7b89292660618e59f216
  TRANSFORMATION_LIBRARY.md: 958ad140727a27a5c47e210a7d71bd779c8e5aa3a13a21375271eeb487aff68a
  SPEC_METHOD.md: 55e6d4f63003ab9dfedaa61163b8ee1836441e22c451c3e5b275b9c5ac67b6e9
  REFERENCE_FRAME_METHOD.md: 5cc32146b4a574f9fd8937a5123816682751a2741c5def42d952ed57f625196e
  STDO_REFERENCE_FRAME_BASELINE.md: 2acdb2d3a7b51484181e201354f3bda8537d489dcf04386426ed6574fb2388a3
  RELEASE_METHOD.md: 66d76a3dbfb93f29c5c8981f495ff6e19815307972ea6ae5ad646d2a004e5fe3
  schemas/product-definition.schema.json: e0a3b544dae6c83bf941096b440700d02fa988fd2767f3b4ab297a1a03f67abf
compression_profile: discovery_bootstrap_v1
target_prompt_families:
  - bootstrap
stale_if_source_digest_changes: true
---

# STDO Discovery Bootstrap

The [core result contract](../FOUNDATIONS.md#result-algebra) owns outcomes and
[result conjunction](../FOUNDATIONS.md#result-conjunction) owns their conjunctive
combination. Domain labels below are refinements on their exact predicates,
retaining original outcomes, performance and effect observations.
[Current workspace acquisition](../FOUNDATIONS.md#workspace-and-context)
governs context reconstruction and conditional reuse.


The [Foundations](../FOUNDATIONS.md) and [Transformation Library](../TRANSFORMATION_LIBRARY.md)
own shared result, context, configuration and conditional transformation
contracts. Detailed owners retain
their exact applicability, result refinements and operation grants. Use a sufficient
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
