# STDO Skills

STDO Skills makes the selected STDO method usable in ordinary agent work through
tool-backed skills. One shared specification has two independent build tenants:
Codex and Claude. Each tenant may choose different skill boundaries, instructions,
context mechanisms and host integration while preserving the same requirements.

This is a construction candidate. The current work is [T-001](.ai-workspace/tickets/active/T-001-skills-dogfood.md).
Read [Intent](specification/INTENT.md), [Product](specification/PRODUCT.md),
[Goals](specification/GOALS.md), [requirements](specification/requirements/README.md)
and the [frame basis](specification/REFERENCE_FRAME_BASIS.md).

The static methodology is **STDO 3.0.1 RC1**, selected by
[stdo_skills.json](stdo_skills.json). Its manifest is
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
The discovery selector never substitutes for that operative basis.

```sh
stdo status --definition stdo_skills.json --verify
```

STDO owns methodology; a_c owns computational support tools; this Product owns
the agent-facing application of those contracts. Their release and adoption
decisions remain separate. Existing installed STDO skills are donor material,
not the new tenants' accepted implementation.

Current a_c lifecycle tooling has a Claude RC9 method binding. Its support for
3.0.1 must be established per operation. An honest legacy mechanical acquisition
can supply source bytes; it does not establish 3.0.1 lifecycle admission,
conjunction or semantic qualification. See the
[tool-binding requirement](specification/requirements/README.md#sk-04-supported-tool-use).

The initial proof is a matched finite set of realistic tasks on both hosts,
including automatic discovery, explicit invocation, tool failures and recovery.
Passing metadata checks alone does not show that agents use the tooling.
