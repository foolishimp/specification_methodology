# STDO Skills

Two independently designed skill tenants apply the same shared STDO requirements:

| Tenant | Entry | Installation and verification |
|---|---|---|
| Codex | One progressive [`stdo-work`](build_tenants/codex/skills/stdo-work/SKILL.md) skill | [Codex package guide](build_tenants/codex/README.md) |
| Claude | Five cooperating skills, starting at [`stdo-workspace-change`](build_tenants/claude/skills/stdo-workspace-change/SKILL.md) | [Claude bundle installation](build_tenants/claude/INSTALL.md) |

Both initial dogfood packages are built and have actual-host task evidence.
Codex's finite nested handoff is independently supported. Claude's mandatory
handoff qualification on its declared CLI path remains open, so this is not a
fully qualified or accepted delivery. The [delivery report](.ai-workspace/work/T001/DELIVERY.md)
shows the supported outcomes, retained failures and next needed qualification.

The static methodology is the proper published immutable **STDO 3.0.1 RC1**
release, selected in [stdo_skills.json](stdo_skills.json), manifest
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
The discovery selector does not change that operative basis.

```sh
stdo status --definition stdo_skills.json --verify
```

Construction used current tools: the STDO manager verified the installed basis;
[a_c's native 3.0.1 binding](../a_c/build_tenants/graphify/design/fd-support-stdo-3.0.1.md)
provided exact acquisition, observations, contexts, preflight, dispatch, scoped
writes and return/evidence operations. Native `results.conjoin` remains explicitly
unsupported. The two tenants consume the same contracts with different host designs.

Read [Product](specification/PRODUCT.md), [requirements](specification/requirements/README.md)
and [current work](.ai-workspace/tickets/active/T-001-skills-dogfood.md) for scope.
Use the package guides for a deliberately selected workspace-local installation.
This Product's delivery, acceptance and release are separate from the already
released methodology; no global skill deployment or efficiency claim is made.
