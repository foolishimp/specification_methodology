# Specification Methodology Repository Bootstrap

This repository contains six peer source projects:
`specification_methodology/v2`, `specification_methodology/v3`, `axiom_indexer`,
`stdo_representation`, `a_c` and `stdo_skills`. The root is coordination only and
is not a Product.

`a_c/` independently realizes the axiomatic calculus, with Graphify as a build
tenant. Use its local Product Definition and bootstrap. It participates in the explicitly selected 3.0.5 cohort; the declared relation preserves its own Product ownership.

`stdo_skills/` owns shared skill requirements and independent Codex and Claude
skill build tenants. Select `stdo_skills/stdo_skills.json` and its local bootstrap
for the selected installed STDO 3.0.4 construction basis. It participates in the explicitly selected 3.0.5 cohort while retaining separate Product ownership.

The Git checkout is `specification_methodology`. The STDO Specification
Methodology product has two version lines side by side: STDO 2.* authoring
belongs in `./specification_methodology/v2/`; v3 development belongs in
`./specification_methodology/v3/`. That child now pins the released STDO 3.0.4
builder and native tools; use its local bootstrap and
[versioned guide](specification_methodology/v3/development/STDO_3_0_4.md). Each has its own Product Definition.

Select the applicable child, load its local instructions and Product
Definition, and preserve its exact authority and dependency boundaries.
Directory proximity creates no inheritance or composition. Never substitute a
mutable sibling checkout for an immutable Product or Install selected by the
child.

For complex work, keep the Executive context small: lock outcome and basis,
select the smallest dependency-ready reference-frame set, delegate bounded
evaluations, consume closed results, and choose only an already-authorized next
action. Do not combine all specialist frames into one prompt.

Native skills:

- `/axiomatize-corpus` for LLM-authored `a_c` compression and mechanical checks;
- `/stdo-representation` for the released source-linked `a_c.STDO` map and
  Source STDO re-entry.

These skills route attention and grant no authority.

Read [the required 3.0.5 candidate membership](RELEASE_PRODUCTS.md),
[the complete release procedure](STACK_RELEASE.md) and `stack_release.json`.
An owner release request selects all five Products and every required current
component through installed qualification, atomic publication and public
readback. Historical graphs, reports and source-only archives do not satisfy
current-candidate membership. All owned components use the exact cohort
version; third-party dependencies retain their independent exact pins.
Published cuts remain immutable. The 3.0.4 builder adoption does not change.

Use `scripts/check_stack_release.py` at ready, content, local-ref, published
and public gates. Missing, extra, stale, mismatched or tampered subjects and
unproven required claims stop promotion. The Executive coordinates; a
separately bound Writer performs file/Git effects, and required independent
review assesses the exact subject without repairing it.
