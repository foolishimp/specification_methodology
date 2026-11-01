# T-019 code representation delivery

The bounded code-overlay implementation, public workflow, offline reader,
ABIogenesis application and both Skills consumer routes are complete and
independently reviewed. The [final review](review/INDEPENDENT_REVIEW.md),
SHA-256 `7d188c64d2769cc560038702052f4d3d3cbded49d60121817515bddbf0adc634`,
reports no open actionable S0–S4 finding. This handoff records the reviewed
worktree increment based on `c034593eea08`; Git checkpoint effects are separately
owned. It issues no owner acceptance or release.

## Use it

Open the [ABIogenesis code explorer](../../../applications/abiogenesis-code-explorer/index.html)
and follow its [quickstart](../../../applications/abiogenesis-code-explorer/README.md):
canonicalization requirement → proposed implementation → relevant test-source
assertions. Files, source quotations, Back and 3D/2D/Layered modes retain the
selected information. Reading needs no service, extractor or LLM.

For another subject, use the [public commands](../../../build_tenants/graphify/README.md#follow-requirements-into-code-and-test-sources):
`prepare` selects an exact generated base and local code/tests; `task` supplies
the endpoint IDs and mapping schema; the current F_P host authors a mapping
outside the run; `build` emits the overlay and reader; `status` and a repeated
build check currentness and reuse. Both Skills tenants route explicit code
requests through this same provider. The selected parser dependencies and pinned
Graphify checkout are needed for extraction. The observed scratch parser target
is not a delivered installation or fresh-machine qualification.

## What was established

- [CR-01–CR-07](../../../specification/requirements/code-realization.md) and the
  [tenant contract](../../../build_tenants/graphify/design/code-realization.md)
  distinguish fallible structural observations from caller-attributed trace
  proposals. Unknown endpoints, extraction diagnostics and unselected source
  boundaries remain visible. Overlay edges do not enter native governing closure.
- The [actual application](abiogenesis-01/README.md) completed
  prepare/task/build/status/reuse over three implementation files and one test
  file. Its 48 raw observations and 127 edges survive normalization, with 11
  unresolved endpoints. Five partial mappings connect canonical ordering,
  serialization, digest construction and test assertions; three unresolved
  mapping statements retain the broader obligations. Original model, carrier,
  native view and 86 source files remain unchanged.
- The independent reviewer ran the 23-test backend suite on the
  acquisition-repaired predecessor `60b115…`, then the three affected tests on
  the terminal-line-ending successor `1c9a9b14…`. These are not one fresh
  26-test suite. Actual ambient-configuration, metadata, failure restoration,
  parser-diagnostic and exact-newline controls support the declared boundary.
- All seven corrected reader checks passed on the actual ABI HTML, together
  with a separate exact record-ID/source/Back journey. The reader and layered
  adapter execute; force rendering is stubbed. Both final Skills package checks
  pass, including the provider/current-source pins. No new host trial follows
  from those package checks.

The [successor source freeze](implementation/repair-terminal-lf-001/SOURCE_FREEZE.json)
and final review bind the exact implementation, reader and provider cut. The
application [VIEW record](../../../applications/abiogenesis-code-explorer/VIEW.json)
remains the frozen construction record; subsequent review standing is recorded
here. Earlier failed attempts and predecessor evidence remain intact.

## Retained boundaries

This is a four-file demonstration, not whole-ABI coverage or full LAWS-021/022
satisfaction. No ABIogenesis code/test execution, overlay Lean check, runtime
correctness, semantic acceptance or measured benefit is asserted. Actual
browser/WebGL/camera behaviour, fresh Codex/Claude host operation, installed
delivery and release retain their own obligations. The source-only extractor
adapter is a cooperative synchronous Python boundary, not host isolation.

The cross-Product relation is the existing Skills consumption of a_c plus this
explicit ABIogenesis application and the separate STDO documentation distribution.
It migrates no authority or method: a_c remains on installed 2.5.1 RC2, Skills on
3.0.1 RC1, and the represented ABIogenesis basis remains its exact 3.0.2 selection.
T-019 does not itself alter or release the STDO 3.0.3 package.
