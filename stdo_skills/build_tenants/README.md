# Skill build tenants

| Tenant | Target execution environment | Owned realization |
|---|---|---|
| `codex` | Declared Codex host/version and model/settings | Codex design, skill decomposition, prompts, supporting resources, installation and qualification |
| `claude` | Declared Claude host/version and model/settings | Claude design, skill decomposition, prompts, supporting resources, installation and qualification |

Both implement [the same requirements](../specification/requirements/README.md)
under the Product's pinned STDO 3.0.1 basis. Each design must show its calculus
binding from requirements to operations and its execution binding to the actual
host, including material effects, failure behavior and resource assumptions.

Tenant differences require a supported host or behavioral reason. Shared contract
meaning is not copied and independently changed in prompt text. Skill names,
counts and wording may differ; qualification compares outcomes and required paths.
Existing STDO plugin skills may be selected as exact donors, then revised as the
requirements demand. No donor inherits acceptance into this Product.

The public surface for each tenant includes its install/discovery route, explicit
invocation, ordinary task behavior, supported tools and removal/update behavior.
Keep host mechanics in tenant HOW and tool algorithms with their existing owner.
Do not invent a shared skill runtime to make the directories symmetrical.

Construction remains isolated to the tenant's granted territory. Shared WHAT
changes return to Root. A review identifies its exact candidate and exposure;
one tenant's success supplies no qualification for the other host.
