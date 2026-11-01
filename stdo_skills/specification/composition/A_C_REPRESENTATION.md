# a_c project representation provider

## Selected representation build

Relation: `urn:stdo-skills:composition:a-c-project-build:1`.
Consumer: `urn:stdo:product-definition:stdo-skills`.
Provider: `urn:stdo:product-definition:a-c-implementations`.
Selection: [T-003](../../.ai-workspace/tickets/active/T-003-project-representation.md).
Exact provider source: [REPRESENTATION_MANIFEST.json](REPRESENTATION_MANIFEST.json).

Both skill tenants consume the provider's
[project-build contract](../../../a_c/build_tenants/graphify/design/project-build.md)
and public `ac_project.py` CLI to build a representation of a nominated project.
The provider reuses its source preparation, F_P author schema/grounding checks,
model adapter, carrier, optional formal gate and offline explorer. Skills owns
recognition of the user's request, host-session authoring and consumption of
actual operation results. It does not copy those algorithms into skill scripts.

Skills remains constructed under released 3.0.1 RC1; a_c remains constructed
under 2.5.1 RC2. A nominated project's exact installed STDO 3.x definition is
subject data for this bounded source operation. This relation does not issue
lifecycle admission under a different profile or migrate either builder.
The existing T-002 native support relation and its frozen sources remain separate.

The user selects the project/source scope and authorized output territory.
Default source is the selected definition's local WHAT, resolved according to
that definition, not all code or neighboring Products. Explicit source paths
are relative to the nominated project. Independent child Products remain out
of scope unless separately nominated. Direct mode and Graphify-assisted mode
are distinct recorded inputs, and no fallback changes a selected treatment.

This provider uses the caller-authorized local filesystem route. It does not
implement the FD support policy's mediated `source.read` boundary. If a consumer
requires that boundary or has no eligible local route, this entry is unsupported
for that activation: retain the refusal before source acquisition. A provider
edge, successful resolver or copied corpus supplies no read/disclosure grant.
Host-session author labels are caller declarations, not isolation, authenticated
identity or measured usage evidence. Existing model and interpretation limits
remain visible in coverage and the return.

Runtime selection names the exact provider path/interpreter and ordinary manager;
optional upstream Graphify and a required formal-checker configuration are
additional declared dependencies. A skill installation alone does not install
these tools. Supplied pins establish byte identity, not semantic acceptance,
complete calculus conformance or authorization to run effects. Missing or changed
dependencies withhold the dependent build claim. Source and artifact currentness
is rechecked through the provider's public resume/readback operation.
