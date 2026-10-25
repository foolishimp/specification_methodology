---
name: stdo-workspace-change
description: Use for governed STDO / specification-methodology development work in this repository — intake and re-entry, verifying the pinned Product Definition and installed method, and making spec, design, or code changes under the selected STDO 3.0.1 method. Routes to the other stdo-* skills. Do not use for unrelated or general factual questions.
---

# STDO workspace change — entry, basis, intake

This skill is the entry point when someone asks you to do governed
specification-methodology work in this repository: change a requirement, design,
or code owner; re-enter at the right layer; or set up and verify the method.

## When this applies

Apply when the request concerns a workspace that selects an STDO Product
Definition (for example `stdo_skills.json`) and asks you to change, review, or
set up governed artifacts under that method. Automatic selection comes from this
skill's `description`; a user may also invoke it explicitly with
`/stdo-workspace-change`.

## When this does not apply (SK-01 discriminator, Q02)

If the request is an unrelated factual question or a non-governed task, do not
force an STDO setup, do not create a work carrier, and do not run any tool
sequence. Answer the actual question or hand off. Presence of this skill is not a
reason to STDO-ify unrelated work.

## Verify the basis first (SK-02, Q03)

Before relying on any method contract, resolve and verify the exact basis:

1. Identify the selected Product Definition in the workspace (e.g.
   `stdo_skills.json`) and the installed method it pins.
2. Verify the installed cut with the manager, for example:
   `stdo status --definition stdo_skills.json --verify`.
3. Confirm the resolved manifest equals the one the Product Definition pins
   (for STDO Skills: `stdo://releases/v3.0.1-rc.1/`, manifest
   `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`).

If the basis is ambiguous, missing, or altered — the install is absent, a member
is modified, or Product selection is ambiguous — **withhold the dependent work
and report the specific cause**. Do not substitute the latest discovered cut or a
sibling source checkout for the pin. Setup may install or pin only within an
explicit grant; ordinary execution never adopts a newer cut implicitly.

## Intake triage (SK-03)

Name three things before acting: the required outcome, the owner that must
change (goal, intent, product, requirement, design, or realization), and the
existing work basis you can reuse. Choose the smallest lawful re-entry point for
that owner. No bug, feature, or request skips triage straight to code.

## Proportional work (SK-03 discriminator, Q04)

Do the smallest sufficient authorized work.

- A small, already-authorized one-file change with a sufficient existing
  requirement/design proceeds directly as a Writer: make the change and record
  focused evidence. Do **not** invent a mandatory ticket, a coordinating actor,
  or an independent review that the conditions do not require, and do not write
  outside the authorized scope.
- Activate material coordination or independent review only when the actual
  conditions require them (material context, capability, or independence
  boundary) — then route to [stdo-delegate-review](../stdo-delegate-review/SKILL.md).
- Reuse existing sufficient authorization without repeating a permission
  ceremony; keep any genuinely missing authority explicit.

## Routing

- Tool calls, context acquisition, or a failing tool: [stdo-tool-operations](../stdo-tool-operations/SKILL.md).
- Delegation or required review: [stdo-delegate-review](../stdo-delegate-review/SKILL.md).
- Resume, interruption, status, or evidence: [stdo-continuation](../stdo-continuation/SKILL.md).
- Release preparation or install/update/remove: [stdo-release-install](../stdo-release-install/SKILL.md).

## Method sources (cited, not reproduced)

Within the installed cut `stdo://releases/v3.0.1-rc.1/standards/`:
`PRODUCT_DEFINITION.md` (sections 2, 4, 7, 9, 12) for exact Product and installed
basis; `ACTIVATION.md` section 1 for intake, operation scope, admission, and
applicability; `ACTIVATION.md` section 6 for cost and proportionality. The owner
index is `specification/SOURCE_OWNERS.md`.

## Scope and limits

This skill does not itself qualify host behavior or claim acceptance. Discovery
is tested separately from whether a loaded skill completes the task; report host
limits and observed failures instead of claiming guaranteed model compliance.

[required resource](references/../../stdo-tool-operations/SKILL.md)
