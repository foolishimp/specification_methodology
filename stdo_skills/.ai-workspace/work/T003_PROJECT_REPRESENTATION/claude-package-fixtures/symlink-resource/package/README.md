# Claude STDO Skills — tenant candidate

Repository-local Claude Code skills that help an agent apply the selected STDO
methodology to governed development work and build representations of a user's
nominated project. This is the Claude
realization of the common requirements in `specification/requirements/README.md`.

Status: **candidate construction only** under T-001 with the selected T-002
composition and T-003 representation increments. Not Product
acceptance, not a release, not host-qualified. Actual-host qualification of this increment is unperformed; earlier Q01-Q12
evidence and limits retain their original subjects.

## Skills

| Skill | Covers | Use for |
|---|---|---|
| `stdo-workspace-change` | SK-01, SK-02, SK-03 | Discoverable entry, basis verification, intake, proportional work |
| `stdo-tool-operations` | SK-04, SK-05, SK-13, SK-14 | Supported tool operations, bounded context and nominated-project representation builds |
| `stdo-delegate-review` | SK-06, SK-07 | Bounded worker handoff and independent review |
| `stdo-continuation` | SK-08, SK-09, SK-12 | Resume/reconcile, truthful status, evidence |
| `stdo-release-install` | SK-10, SK-11 | Release prep, install/update/remove, maintenance |

## Basis

Selected method: `stdo://releases/v3.0.1-rc.1/`, manifest
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8` (static). Host:
Claude Code 2.1.306. Tool transport: the a_c public CLI.

## Build a project representation

Ask Claude to “build a representation of my project at …”, or invoke
`/stdo-tool-operations` with that request. Workspace-change routes the natural
request to tool-operations and its packaged
[representation procedure](skills/stdo-tool-operations/references/representation.md).
Supply or resolve the nominated project's exact definition, permitted sources,
fresh output directory and selected provider path. The operator's
`AC_PROJECT_TOOL` may identify `ac_project.py`; the skill bundle does not install
that provider.

Claude runs prepare, authors each frozen-source task in its current session,
submits the actual JSON, builds, verifies current status, and returns actual
model, carrier, coverage and offline explorer links. Direct mode needs no
upstream Graphify; selected `graphify-ac` requires its pinned upstream. The target
method, fixed Skills builder and provider builder remain distinct. Selected
composition restrictions still apply, and incomplete/stale runs withhold a
completed-build claim. This package addition does not close the earlier Claude
Q05 handoff qualification or establish semantic acceptance.

## Layout

- `design/DESIGN.md` — decomposition, trace to SK-01..SK-14 and Q01..Q12, bindings.
- `skills/<name>/SKILL.md` — the five skills installed together as one bundle.
- The tool skill carries conditional composition and representation references.
- The release skill carries `references/maintenance.md` and `scripts/manage_install.py`.
- `INSTALL.md` — owned install/update/remove commands, receipt selection and refusal behavior.
- `tests/check_package.py` — read-only package verifier.
- `INVENTORY.md` — exact file inventory with sha256.

Verify with `python3 -I -B build_tenants/claude/tests/check_package.py`.
