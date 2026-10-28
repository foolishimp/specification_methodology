# T-011 Lean formalisation tenant

Status: bounded implementation and independent final review complete; no
findings or required repairs remain for FR-001–FR-007. Owner: Jim. Coordinating
Executive: `/root`. This record remains in `active/`; no ticket move is selected.
Work is uncommitted and unpushed on `main`; no owner acceptance or release is
issued.
Change class: `product_reprice`; re-entry: Product, then requirements and tenant
design. Initial observed checkpoint:
`298593398c51e1c33c8ff9662da9a0aa18749194` on clean `main`.

## Owner instruction

Jim selected “yes it would be a new build tenant for formalisation” and then
instructed “i want you to work on this - define the build tenant and do the work”.
This authorizes definition, implementation and local verification of the new
Lean/Mathlib tenant within the existing `a_c` Product. It supplies no semantic
acceptance of an interpretation, whole-calculus validity, Product acceptance,
release, publication, commit or push decision.

## Selected outcome and basis

Implement the common [formalisation requirements](../../../specification/requirements/formalisation.md)
as tenant `urn:a-c-implementations:build-tenant:lean` under `build_tenants/lean/`.
The first delivery constructs a source-linked formal model with all eight
record-family tags and generic checked proofs of exact declared dependency
closure, retained-record projection preservation and budget refusal. The
execution path applies that model to the frozen published STDO 3.0.2 composition
supplement and exposes exact successful and refused results.

The unchanged installed builder is `stdo://releases/v2.5.1-rc.2/`, manifest
SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The owning `standards/AXIOMATIC_CALCULUS.md` has SHA-256
`cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.
The Executive verified this installed basis; the Writer re-entered its bootstrap,
record definitions, AC-001..011 and interpretation/valid-model clauses.

The subject fixture is the exact existing
`specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/native-release/release-run-01/supplement-bundle/MODEL.json`,
relative to the checkout root: raw SHA-256
`fc3114dd666218c387a64846b755a14979182f488de64ffff6a6d305a9698793`,
canonical model identity
`b3f97a2667c277c21417230421aca02c26b3a7b19baa598197e94f67c5439151`.
It has 32 local records, with explicit empty traversal, transformation and
judgment populations. The tenant retains its own exact fixture copy and source
mapping. This is subject data, not an operative builder, adopted methodology,
composed Product or runtime dependency on mutable v3. Existing Graphify output
may supply an explicit import adapter; the formal tenant is independently usable.

## Activations recorded before common-source effects

Executive `/root` selects the bounded work and consumes closed results. It does
not mutate candidate or Product bytes. Writer `/root/ac_lean_contract_writer`
is delegated the operation to define the shared formalisation contract and bind
the new tenant, with this exact write territory:

- `a_c/README.md` and `a_c/stdo_a_c.json`;
- `a_c/specification/GOALS.md`, `PRODUCT.md`, `INTENT.md`,
  `REFERENCE_FRAME_BASIS.md`, `requirements/README.md` and new
  `requirements/formalisation.md`;
- `a_c/build_tenants/README.md`;
- this ticket and `a_c/.ai-workspace/work/T011_LEAN_FORMALISATION/contract/`.

The disjoint formal Worker `/root/ac_lean_worker` receives its tenant design,
code, proof, executable, local tooling and evidence grant separately from the
Executive. A nonauthor Reviewer receives read-only source/candidate/evidence
access and records a bounded assessment separately. Construction does not supply
its own independent judgment or admission. The owner instruction and delegated
operation authorize these effects; this record is not a generated admission
receipt. No receipt is fabricated for an unperformed evaluation.

Existing Graphify implementation, shared methodology, frozen studies and Git
effects are outside this Writer grant. Preimage identities and the closed
contract return are retained under `contract/`. Each actor stops at its closed
return; further mutations need a supported, separately bounded activation.

## Completion conditions

- Common requirements bind the source/proof interpretation, exact import and
  trust boundaries, selected executable fragment and reserved claims.
- The independent tenant provides pinned reproducible Lean/Mathlib setup,
  executable positive/refusal examples and source-linked generic kernel-checked
  closure, preservation and refusal proofs.
- The frozen 32-record fixture is imported without silent record loss or
  authority/basis/residual changes, and an actual end-to-end run exercises it.
- Independent assessment inspects the exact source/model/proof boundary and
  meaningful negative controls; supported findings receive bounded repairs.
- The final handoff names source identities, performed checks, proof assumptions
  and trust dependencies, unproven claims and unresolved evidence.

Passing a theorem about declared data establishes only its stated proposition
under its premises. Prose fidelity, semantic selection of dependencies,
interpretation/admission authority, arbitrary constraint evaluation, AC-013
transformation execution, full calculus validity, efficiency and Product release
remain outside this increment unless separately evidenced and selected.

## Completed delivery and independent assessment

The [delivery handoff](../../work/T011_LEAN_FORMALISATION/DELIVERY.md) provides
the runnable entry, exact source identities and retained evidence. The
[29-file tenant freeze](../../work/T011_LEAN_FORMALISATION/implementation/SOURCE_MANIFEST.json)
contains the complete independent Lean/Mathlib realization, both copied fixture
models, generic and concrete proofs, source adapter and public check path.

The [independent final review](../../work/T011_LEAN_FORMALISATION/review/20261027_FINAL_REVIEW.md)
is satisfied for the selected FR-001–FR-007 first fragment, with no findings or
required repairs. The reviewer executed the documented public path: 46 concrete
selectors, 46 actual projection outputs, 46 insufficient-budget refusals, 204
deciding theorem axiom reports and fresh kernel replay passed. Independent
controls rejected source/projection tampering and a disconnected closed cycle
that was not reachable from the seeds. Executive `/root` consumed this closed
assessment and selected the bounded implementation increment as complete.

The 32-record published composition supplement remains represented subject
data. The 14-record application-neutral fixture exercises all eight populated
families, parallel/self relations and repeated references. The builder,
requirements, Product, Intent, registry, Product Definition and frame basis
remain unchanged from the reviewed cut. Lean source and proof files were not
changed during status finalization, and no new test or review campaign ran.

Before these factual status updates, the Writer preserved and verified all
eleven original common-contract subjects in an
[exact historical snapshot](../../work/T011_LEAN_FORMALISATION/final-status/PRESERVED_REVIEWED_SOURCE.json).
Prior closed returns retain their original bytes and identify those historical
reviewed subjects. This status record does not retroactively rewrite them or
claim that the old hashes describe the updated status files.

The Lean kernel and standard `propext`, `Classical.choice` and `Quot.sound`
axioms remain trusted. Python parsing/hash/schema mapping/generation and
compiler/runtime/serialization remain tested or trusted boundaries. F_P source
fidelity, dependency sufficiency and authority legitimacy remain external
judgments. Whole-calculus validity, arbitrary predicate or transformation
execution, efficiency, semantic/carrier admission, Product acceptance and
release are outside this completed increment.
