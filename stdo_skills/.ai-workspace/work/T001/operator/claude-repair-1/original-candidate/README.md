# Claude STDO Skills — tenant candidate

Repository-local Claude Code skills that help an agent apply the selected STDO
methodology to governed development work in this repository. This is the Claude
realization of the common requirements in `specification/requirements/README.md`.

Status: **candidate construction only** under ticket T-001. Not Product
acceptance, not a release, not host-qualified. Actual-host Q01-Q12 trials and
independent review remain open.

## Skills

| Skill | Covers | Use for |
|---|---|---|
| `stdo-workspace-change` | SK-01, SK-02, SK-03 | Discoverable entry, basis verification, intake, proportional work |
| `stdo-tool-operations` | SK-04, SK-05 | Supported tool operations and bounded context |
| `stdo-delegate-review` | SK-06, SK-07 | Bounded worker handoff and independent review |
| `stdo-continuation` | SK-08, SK-09, SK-12 | Resume/reconcile, truthful status, evidence |
| `stdo-release-install` | SK-10, SK-11 | Release prep, install/update/remove, maintenance |

## Basis

Selected method: `stdo://releases/v3.0.1-rc.1/`, manifest
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8` (static). Host:
Claude Code 2.1.306. Tool transport: the a_c public CLI.

## Layout

- `design/DESIGN.md` — decomposition, trace to SK-01..SK-12 and Q01..Q12, bindings.
- `skills/<name>/SKILL.md` — the five skills.
- `INSTALL.md` — scoped install/update/remove recipe.
- `tests/check_package.py` — read-only package verifier.
- `INVENTORY.md` — exact file inventory with sha256.

Verify with `python3 -I -B build_tenants/claude/tests/check_package.py`.
