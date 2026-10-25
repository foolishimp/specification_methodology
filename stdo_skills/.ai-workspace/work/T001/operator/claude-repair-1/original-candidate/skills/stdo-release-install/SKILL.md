---
name: stdo-release-install
description: Use when governed STDO work in this repository needs release preparation or installation lifecycle management — binding an exact candidate to release conditions without inferring publication authority, and installing, updating, or removing a skill package in a disposable host workspace. Covers tenant realization and maintenance. Not for unrelated tasks.
---

# STDO release preparation, install, update, remove

Use this skill to prepare a reviewable release and to manage the installation
lifecycle of this skill package in a host workspace.

## Prepare a release (SK-10, Q11)

Bind the exact selected candidate, the release conditions, the publication grant,
and the destination, using the supported release tools. You can prepare a
reviewable release **without** inferring publication authority:

- If a local artifact grant is present but no remote publication grant is, prepare
  the exact reviewable candidate and name the destination; do **not** publish and
  do **not** invent a second final cut.
- Preserve the method's immutable-cut semantics; an implementation defect does not
  authorize editing a selected methodology.

## Install / update / remove (SK-10, SK-11, Q12)

The install unit is a single skill directory. Claude Code discovers repository
skills under `<workspace>/.claude/skills/<name>/SKILL.md`. Use a disposable host
workspace for trials.

Install (copy each skill directory into the project-local skills root):

```
mkdir -p <workspace>/.claude/skills
cp -R build_tenants/claude/skills/stdo-workspace-change <workspace>/.claude/skills/
cp -R build_tenants/claude/skills/stdo-tool-operations   <workspace>/.claude/skills/
cp -R build_tenants/claude/skills/stdo-delegate-review   <workspace>/.claude/skills/
cp -R build_tenants/claude/skills/stdo-continuation      <workspace>/.claude/skills/
cp -R build_tenants/claude/skills/stdo-release-install    <workspace>/.claude/skills/
```

Verify discovery: confirm each `<workspace>/.claude/skills/<name>/SKILL.md`
resolves and that referenced files inside each directory are present. Then invoke
one skill (for example `/stdo-workspace-change`) to confirm the host selected the
exact package.

Update (record identity, then replace in place):

```
# record the currently installed identity before replacing
sha256sum <workspace>/.claude/skills/stdo-workspace-change/SKILL.md
# compare against build_tenants/claude/INVENTORY.md, then replace the directory
rm -rf <workspace>/.claude/skills/stdo-workspace-change
cp -R build_tenants/claude/skills/stdo-workspace-change <workspace>/.claude/skills/
```

The previous package stays identifiable (its recorded inventory sha) and the
replacement is deliberate.

Remove (scoped to the named directories only):

```
rm -rf <workspace>/.claude/skills/stdo-workspace-change
rm -rf <workspace>/.claude/skills/stdo-tool-operations
rm -rf <workspace>/.claude/skills/stdo-delegate-review
rm -rf <workspace>/.claude/skills/stdo-continuation
rm -rf <workspace>/.claude/skills/stdo-release-install
```

Installation, update, and removal touch only this tenant's named directories in
the selected workspace. They must not enable the Codex tenant, must not touch the
user's personal configuration, and must leave unrelated configuration intact.

## Maintenance and bindings (SK-11)

This tenant declares its requirements-to-algorithms and algorithms-to-host
bindings, supported versions, and failure behavior in `design/DESIGN.md`
(sections 5 and 6). Shared mechanics (the a_c tool contracts) are consumed, not
reimplemented. Tuning is driven by observed task behavior. A host change, a
tool-contract change, or a method adoption identifies the affected tests and
claims without resetting unrelated valid evidence. Skill and source references
stay resolvable in the delivered form (each skill directory is self-contained).

## Method sources (cited, not reproduced)

Within `stdo://releases/v3.0.1-rc.1/standards/`: `RELEASE.md` and `IDENTITY.md`
for release identity and consumer adoption; `PRODUCT_DEFINITION.md` sections 2, 4,
7, 9, 12 for installed basis; `SPEC_METHOD.md` sections 2, 10, 11 and
`DESIGN_MODULE.md` for realization binding.

## Scope and limits

Preparing a release is not publishing one, and installing into a disposable
workspace is not Product acceptance. This candidate performs neither publication
nor acceptance.
