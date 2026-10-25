# Claude tenant design — STDO Skills (successor-1 candidate)

Identity: `urn:stdo-skills:T001:claude:candidate`.
Frame: Worker `skills.worker/1` (revision 3). Consumer: root-executive.
Status: **candidate construction only**. This is not Product acceptance, not a
release, and not host qualification. Actual-host Q01-Q12 trials and independent
review remain open obligations (see sections 4 and 7).

## 1. Scope and selected basis

- Common WHAT realized here: `specification/requirements/README.md`
  (SK-01..SK-12) and the oracle `specification/requirements/SCENARIOS.md`
  (Q01..Q12). Product boundary: `specification/PRODUCT.md`;
  intent: `specification/INTENT.md`.
- Selected method (static, pinned, no channel adoption):
  `stdo://releases/v3.0.1-rc.1/`, manifest
  `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
  Deciding method owners are indexed in `specification/SOURCE_OWNERS.md`;
  skills cite those files by installed path and do not reproduce their clauses.
- Host: Claude Code (verified local version 2.1.306). Repository skills live at
  `<workspace>/.claude/skills/<name>/SKILL.md`; the `description` field drives
  automatic selection and `/<name>` invokes explicitly. `disable-model-invocation`
  is not set, so both lanes stay open. Newer documented host behavior is not
  assumed on 2.1.306.
- Tool transport: the a_c public CLI
  (`a_c/build_tenants/graphify/code/ac_support.py ... call --request -` on stdin),
  method/tool profile `urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1`.
  Native `results.conjoin` is unsupported (reported by `tools.describe`).

## 2. Decomposition and rationale

Five repository-local Claude skills. Each is self-contained: it cites method
sources by installed path and does not depend on another skill's files or on the
Codex tenant, so every reference still resolves after a skill directory is copied
to `<workspace>/.claude/skills/<name>/` (SK-11).

| Skill | SK coverage | Purpose |
|---|---|---|
| `stdo-workspace-change` | SK-01, SK-02, SK-03 | Discoverable entry; verify the pinned basis; lawful intake and proportional work |
| `stdo-tool-operations` | SK-04, SK-05 | Supported tool binding and bounded context acquisition |
| `stdo-delegate-review` | SK-06, SK-07 | Bounded worker handoff and independent review |
| `stdo-continuation` | SK-08, SK-09, SK-12 | Continuation/recovery, truthful status, evidence capture |
| `stdo-release-install` | SK-10, SK-11 | Release preparation, scoped install/update/removal, maintenance |

Rationale: one broadly-described entry skill gives SK-01 discovery without a
remembered name; the specialized skills carry the heavier flows and are reached
by their own descriptions, by explicit `/<name>`, or by routing from the entry
skill. Self-containment is chosen over a shared reference directory because the
install unit is the individual skill directory.

## 3. Requirement to skill to section trace

| Req | Skill / section |
|---|---|
| SK-01 Discoverable task entry | `stdo-workspace-change`: When this applies / When this does not apply |
| SK-02 Static basis and scope | `stdo-workspace-change`: Verify the basis first |
| SK-03 Lawful intake and proportional work | `stdo-workspace-change`: Intake triage, Proportional work |
| SK-04 Supported tool use | `stdo-tool-operations`: Transport and operations, When a tool fails |
| SK-05 Adequate bounded context | `stdo-tool-operations`: Acquire only the deciding context |
| SK-06 Construction and delegated return | `stdo-delegate-review`: Delegating a bounded worker |
| SK-07 Independent review | `stdo-delegate-review`: Independent review |
| SK-08 Continuation and recovery | `stdo-continuation`: Resume and reconcile |
| SK-09 Truthful status and closure | `stdo-continuation`: Status and closure |
| SK-10 Release and installation | `stdo-release-install`: Prepare a release, Install / update / remove |
| SK-11 Independent realization and maintenance | `stdo-release-install`: Maintenance and bindings |
| SK-12 Evidence and benefit | `stdo-continuation`: Capture evidence |

## 4. Scenario coverage (every case OPEN on the actual host)

The skills describe the intended path and the falsifier for each case; this
candidate asserts no host compliance. Q01..Q12 qualification requires the frozen
oracle protocol in `SCENARIOS.md` on the real host and is **not performed** here.

| Case | Addressed by | Status |
|---|---|---|
| Q01 discover + explicit invocation | `stdo-workspace-change` | OPEN |
| Q02 unrelated task not forced into STDO | `stdo-workspace-change` (When this does not apply) | OPEN |
| Q03 valid/invalid pinned basis | `stdo-workspace-change` (Verify the basis first) | OPEN |
| Q04 one-file authorized change, no invented ceremony | `stdo-workspace-change` (Proportional work) | OPEN |
| Q05 bounded worker + independent review | `stdo-delegate-review` | OPEN |
| Q06 unsupported method / execution error retained | `stdo-tool-operations` (When a tool fails) | OPEN |
| Q07 equal bytes, divergent retained obligation | `stdo-continuation` (Resume and reconcile) | OPEN |
| Q08 interrupted effect, reconcile before retry | `stdo-continuation` (Resume and reconcile) | OPEN |
| Q09 stale review invalidated by change | `stdo-continuation` (Status and closure) | OPEN |
| Q10 candidate / indeterminate / not-performed distinct | `stdo-continuation` (Status and closure) | OPEN |
| Q11 release prep without publication grant | `stdo-release-install` (Prepare a release) | OPEN |
| Q12 install / invoke / remove / update in disposable host | `stdo-release-install` (Install / update / remove) | OPEN |

## 5. Requirements-to-algorithm and algorithm-to-host bindings (SK-11)

- Basis verification -> `stdo status --definition stdo_skills.json --verify`
  (manager at `/Users/jim/.local/bin/stdo`), cross-checked against the manifest
  pinned in `PRODUCT.md`. Ambiguous, missing, or altered basis -> withhold the
  dependent work and report the cause.
- Tool operation -> a_c public CLI envelope on stdin; each operation uses its
  `tools.describe` contract; a failure retains partial evidence and withholds the
  dependent claim.
- Context acquisition -> `source.read` over the declared source routes; retain
  evidence ids.
- Effect write -> `work.write` with the activation grant, the exact target
  preimage, and the actor's own `workspace.observe`.
- Host binding -> Bash + Read + the CLI; discovery via
  `<workspace>/.claude/skills/<name>/`.
- Failure behavior and qualification scope are stated per skill; unknown measures
  stay unknown rather than being invented.

## 6. Supported versions and material coordinates

- Claude Code 2.1.306 (observed local). Behavior requiring later versions is not claimed.
- Method manifest `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`.
- Tool/method profile `urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1`,
  sha256 `a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7`.
- The worker policy path, principal, and grant id are activation-scoped inputs;
  they are deliberately **not** embedded in any skill, so a skill is not single-use.

## 7. Unsupported and explicitly out of scope

- Native `results.conjoin`; other method cuts; MCP server/discovery; semantic
  sufficiency certification; benefit or acceptance claims (per `tools.describe`
  `unsupported`).
- This candidate performs no host install, no Q01..Q12 qualification, no
  independent review, and no release publication. Those remain later obligations.

## 8. Package layout and integrity

- `design/DESIGN.md` (this file), `skills/<name>/SKILL.md` (5), `INSTALL.md`,
  `README.md`, `tests/check_package.py`, `INVENTORY.md`.
- `INVENTORY.md` lists every package regular file with its sha256, excluding
  itself. `tests/check_package.py` is a read-only verifier that checks
  frontmatter, name/dir agreement, absence of symlinks, references resolving
  inside each skill directory, absence of any other-tenant or personal-config
  path, and inventory agreement with the files on disk. Running the verifier is
  the proof; the presence of the file is not.
