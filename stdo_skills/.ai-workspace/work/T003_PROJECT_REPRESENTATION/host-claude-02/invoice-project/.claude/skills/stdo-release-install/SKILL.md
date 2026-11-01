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

Install the complete five-skill bundle, including every resource below its five
directories. The entry and delegation paths require sibling skills. Claude Code
discovers these directories under `<workspace>/.claude/skills/`; a single directory
is not a supported independent installation.

Use the delivered [installation helper](scripts/manage_install.py) with an exact
source package and a selected existing workspace. For initial install:

```
python3 -I -B <this-skill-directory>/scripts/manage_install.py install --package <selected-package> --workspace <workspace>
```

The helper validates the source package and refuses any ownership receipt or
same-name directory collision. Retain the returned receipt SHA256 and verify
actual host discovery/invocation separately. The receipt records the source
inventory and exact installed file/directory population and contents.

For update/removal, select the previously recorded receipt SHA256:

```
python3 -I -B <this-skill-directory>/scripts/manage_install.py update --package <new-package> --workspace <workspace> --receipt-sha256 <previous-receipt-sha256>
python3 -I -B <this-skill-directory>/scripts/manage_install.py remove --workspace <workspace> --receipt-sha256 <current-receipt-sha256>
```

The receipt must identify this bundle; every owned installed file and directory
must still match. Local additions, modified/missing files, foreign same-name
installations and symlinks cause refusal before mutation. Preserve them and
reconcile ownership; do not refresh a hash or delete a directory to bypass the
refusal. Unrelated siblings/configuration remain untouched. Update validates the
entire new bundle first and returns a successor receipt. There is no force or
individual-skill update.

Use exclusive workspace access. A filesystem error may leave partial effects;
retain the current tree/receipt and reconcile before retry. The helper reports
`effect_uncertain` rather than claiming rollback. Use disposable workspaces for
trials; package verification is distinct from host qualification and acceptance.

## Maintenance and bindings (SK-11)

Read the delivered [maintenance coordinates](references/maintenance.md) for the
selected method/tool/host basis and algorithm bindings. a_c contracts are consumed,
not reimplemented. When host behavior, tool contracts, method adoption or package
bytes change, identify affected tests and claims; do not reset unrelated valid
evidence. Required delivered links are checked against the complete bundle;
method and engagement Product sources remain explicit external dependencies.

## Method sources (cited, not reproduced)

Within `stdo://releases/v3.0.1-rc.1/standards/`: `RELEASE.md` and `IDENTITY.md`
for release identity and consumer adoption; `PRODUCT_DEFINITION.md` sections 2, 4,
7, 9, 12 for installed basis; `SPEC_METHOD.md` sections 2, 10, 11 and
`DESIGN_MODULE.md` for realization binding.

## Scope and limits

Preparing a release is not publishing one, and installing into a disposable
workspace is not Product acceptance. This candidate performs neither publication
nor acceptance.
