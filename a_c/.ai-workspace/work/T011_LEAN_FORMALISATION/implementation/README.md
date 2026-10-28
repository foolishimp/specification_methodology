# Lean tenant construction return

Status: bounded implementation and author-produced mechanical verification are
complete. Independent review and owner disposition remain separate. No Product
acceptance, release, installation of the tenant, or full-calculus claim is made.

Root activated this Worker for `a_c/build_tenants/lean/**` and this work item's
`implementation/**` / `runtime/**`. The common contract Writer separately owned
Product/requirement/ticket changes, then received the bounded adapter grant
recorded in [adapter/CLOSED.json](adapter/CLOSED.json). No Worker Git commit,
index mutation, global toolchain installation, installed-method modification,
mutable v3/Graphify dependency or paid model campaign was performed.

The [tenant README](../../../../build_tenants/lean/README.md) is the runnable
entry. The [design](../../../../build_tenants/lean/design/README.md),
[source correspondence](../../../../build_tenants/lean/design/SOURCE_CORRESPONDENCE.md)
and [boundary ledger](../../../../build_tenants/lean/design/BOUNDARIES.md) identify
the exact claims, assumptions and unsupported work.

The final [check-002 report](../runtime/check-002/report.json) binds source
hashes and toolchain versions. It records:

- Lean 4.35.0, compiler commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`,
  and Mathlib commit `56a005855ea17e0b0958f73ec801ae140b0a1679` with exact
  transitive Lake manifest pins.
- Exact copied primary fixture bytes; canonical model
  `b3f97a2667c277c21417230421aca02c26b3a7b19baa598197e94f67c5439151`;
  both actual carrier paths independently recover the complete 32-record,
  246-reference, 47-required-edge model.
- A separate exact 14-record, 124-reference, 29-required-edge toy fixture with
  all eight families populated, including inert traversal/transformation/judgment
  records and discriminating direction/cycle/non-governing cases.
- 32 passing adapter tests; all 46 singleton selectors carry kernel-checked
  certificate, exact result set, reachability, executable success and one-short
  budget-refusal theorems.
- Fixed expected proposition contracts and 204 deciding axiom reports. The only
  dependencies reported are the declared standard `propext`, `Classical.choice`
  and `Quot.sound`; no added axiom, admission or native proof evaluation.
- Fresh `leanchecker --fresh AC` replay of the project and selected imports
  passed in 71.08 seconds. Cached Mathlib proof objects are therefore not merely
  accepted because `lake build` found them.
- 46 actual Lean output projections exactly match independently recovered source
  payloads, parent coordinates, included/excluded sets, external/ordinary
  references and retained/excluded residual boundaries. All 46 one-record-short
  operations return refusal. A deliberately false truncated real-fixture
  certificate claim fails kernel proof checking.

[check-001](../runtime/check-001/) retains an intermediate integration attempt:
core proofs/axiom audit/fresh kernel replay passed, then actual execution exposed
missing interpreter IR for a module import. Explicit `meta import` declarations
in `AC.Run` supply runtime IR under Lean 4.35's module system. The subsequent
check-002 repeats the complete path and passes. No failure is reclassified as a
successful runtime check.

The full [frozen source manifest](SOURCE_MANIFEST.json) identifies all tenant
source files and the [Worker return](CLOSED.json) binds that manifest and final
report. Toolchain, downloaded Mathlib caches and generated local run caches are
excluded from source via the tenant-local `.gitignore`; pinned lockfiles,
fixtures, source, proof, commands and logs remain reviewable.
