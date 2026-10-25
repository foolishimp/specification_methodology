# Specification Methodology Repository Bootstrap

This repository contains six peer source projects:
`specification_methodology/v2`, `specification_methodology/v3`, `axiom_indexer`,
`stdo_representation`, `a_c` and `stdo_skills`. The root is coordination only and
is not a Product.

`a_c/` independently realizes the axiomatic calculus, with Graphify as a build
tenant. Use its local Product Definition and bootstrap. It adds no dependency
to v3 or membership in the existing release-matched cohort.

`stdo_skills/` owns shared skill requirements and independent Codex and Claude
skill build tenants. Select `stdo_skills/stdo_skills.json` and its local bootstrap
for the static installed STDO 3.0.1 basis. Its lifecycle is separate from the
release-matched cohort.

The Git checkout is `specification_methodology`. The STDO Specification
Methodology product has two version lines side by side: STDO 2.* authoring
belongs in `./specification_methodology/v2/`; v3.0.0 construction belongs in
`./specification_methodology/v3/`. Each has its own Product Definition.

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

Interpret an owner's STDO release request through
[`Meaning Of A Release Request`](STACK_RELEASE.md#meaning-of-a-release-request).

For an explicitly selected coordinated STDO stack release, read
`STACK_RELEASE.md` and `stack_release.json`. The exact normalized cohort version
must match the STDO corpus, plugin, Axiom Indexer, STDO Representation, and
generated `a_c.STDO` program/map. Run `scripts/check_stack_release.py` at the
content, local-ref-graph, and remote gates. Any missing, stale, differently
versioned, digest-incongruent, or partially published member stops release.
