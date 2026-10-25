# Install, update, and remove — Claude STDO Skills package

This package is a set of repository-local Claude Code skills. The install unit is
an individual skill directory under `skills/`. Claude Code discovers repository
skills at `<workspace>/.claude/skills/<name>/SKILL.md`.

These instructions describe the scoped recipe; this candidate does not execute
them. Actual-host install/invoke/remove qualification (Q12) is a later obligation.

## Package contents

- `skills/stdo-workspace-change/SKILL.md`
- `skills/stdo-tool-operations/SKILL.md`
- `skills/stdo-delegate-review/SKILL.md`
- `skills/stdo-continuation/SKILL.md`
- `skills/stdo-release-install/SKILL.md`
- `design/DESIGN.md`, `README.md`, `tests/check_package.py`, `INVENTORY.md`

Each skill directory is self-contained: it references only files inside itself and
cites method sources by installed path. No skill depends on another skill or on
the Codex tenant.

## Verify the package before installing

```
python3 -I -B build_tenants/claude/tests/check_package.py
```

The verifier checks frontmatter, name/directory agreement, absence of symlinks,
that references resolve inside each skill directory, that no other-tenant or
personal-config path is referenced, and that `INVENTORY.md` matches the files on
disk. A passing run of this verifier is the integrity evidence; the presence of
the file is not.

## Install (into a disposable workspace)

```
mkdir -p <workspace>/.claude/skills
for s in stdo-workspace-change stdo-tool-operations stdo-delegate-review \
         stdo-continuation stdo-release-install; do
  cp -R build_tenants/claude/skills/$s <workspace>/.claude/skills/
done
```

Then confirm discovery: each `<workspace>/.claude/skills/<name>/SKILL.md` exists,
and invoking `/stdo-workspace-change` selects the exact package.

## Update

Record the installed identity, then replace the directory in place:

```
sha256sum <workspace>/.claude/skills/<name>/SKILL.md   # compare to INVENTORY.md
rm -rf <workspace>/.claude/skills/<name>
cp -R build_tenants/claude/skills/<name> <workspace>/.claude/skills/
```

## Remove (scoped)

```
for s in stdo-workspace-change stdo-tool-operations stdo-delegate-review \
         stdo-continuation stdo-release-install; do
  rm -rf <workspace>/.claude/skills/$s
done
```

Install, update, and remove touch only this tenant's named directories in the
selected workspace. They do not enable the Codex tenant, do not modify the user's
personal configuration, and leave unrelated configuration intact.
