# Using STDO

This guide is the practical entrypoint for a person or LLM entering an
STDO-governed project. It answers four questions:

1. How do I get ready to work?
2. How do I iterate requirements?
3. What authorizes code development and testing?
4. How do I monitor progress and help triage?

This guide and its companion skills are non-deciding interaction projections.
The project's exact installed STDO cut and Product-owned authority remain the
governing sources.

## Contents

- [Get Ready To Work](#1-get-ready-to-work)
- [Iterate Requirements](#2-iterate-requirements)
- [Start Code Development And Testing](#3-start-code-development-and-testing)
- [Monitor And Help Triage](#4-monitor-and-help-triage)
- [Common Stops](#common-stops)
- [Owning References](#owning-references)

## The Operating Loop

Keep these distinct:

- an immutable STDO cut defines the selected method;
- `stdo_<label>.json` selects that cut and locates the Product's actual
  authority, realization, and work carriers;
- the project owns its Goals, Intent, Product, requirements, design, code,
  tickets, decisions, and evidence; and
- skills route common requests without becoming another method, workflow
  engine, prompt engine, or source of truth.

```text
request
  -> verify the exact basis and current outcome
  -> triage, select the smallest work carrier, and admit a run contract
  -> re-enter at the first changed layer
  -> update constitutional truth and accepted design when required
  -> construct code and tests when authorized
  -> return an exact candidate
  -> independently review when required
  -> Product-owned disposition and checkpoint
  -> status, evidence, and the next authorized action
```

STDO constrains governed relations. It does not prescribe an actor count,
repository layout, prompt construction engine, internal decomposition, search
procedure, or tool sequence where those choices cannot change a governed
semantic, authority, evidence, safety, or release property.

## 1. Get Ready To Work

### Existing STDO-Governed Project

Locate the one Product Definition that applies to the requested Product scope.
Directory nesting does not imply governance. Require exactly one applicable
`stdo_<label>.json`.

Start read-only:

```sh
stdo status --definition <path-to-definition> --verify
```

If the selected cut is absent and installation is authorized, synchronize that
exact pinned basis and verify it again:

```sh
stdo sync --definition <path-to-definition>
stdo status --definition <path-to-definition> --verify
```

`sync` may install bytes. It never follows the moving selector or edits the
Product Definition. The shell command `stdo status` reports basis and install
health; it is not a Product-delivery status report.

Before acting, resolve:

1. the Product Definition bootstrap entrypoint;
2. the Product-owned accepted Project Reference-Frame Basis;
3. current Goals;
4. Intent and Product;
5. only the affected requirements and accepted design;
6. the admitted ticket, sprint entry, or equivalent work carrier; and
7. only the exact owning standard needed for the action.

Do not bulk-load the standards corpus. A new LLM should be able to state this
compact basis before it changes anything:

```text
Product definition: <identity and path>
STDO basis: <immutable cut and manifest digest>
Current outcome: <Goal or Product outcome>
Work authority: <carrier and re-entry point>
Role and grant: <actor, operation, subject, write territory>
Proof boundary: <claim and required evidence>
Stop/re-entry conditions: <conditions>
ACTION: <one bounded requested action>
```

The action comes last. The preceding context qualifies the work without
prescribing irrelevant internal procedure.

### New Project

Select one immutable product-local cut and its qualified repository ref. For
the published STDO 2.5.0 RC3 distribution:

```sh
STDO_CUT='v2.5.0-rc.3'
STDO_REF='specification_methodology/v2.5.0-rc.3'
STDO_TOOLCHAIN_MIN='0.1.2'
STDO_TOOLCHAIN_SPEC='git+https://github.com/foolishimp/specification_methodology.git@specification_methodology/v2.5.0-rc.3#subdirectory=specification_methodology'

stdo_version_at_least() {
  python3 - "$1" "$2" <<'PY'
import re
import sys

def version(value):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)(?:[.+-].*)?", value)
    if match is None:
        raise SystemExit(f"invalid stdo-toolchain version: {value}")
    return tuple(map(int, match.groups()))

raise SystemExit(0 if version(sys.argv[1]) >= version(sys.argv[2]) else 1)
PY
}

if ! command -v stdo >/dev/null 2>&1; then
  pipx install "$STDO_TOOLCHAIN_SPEC"
elif ! stdo_version_at_least \
  "$(stdo --version | awk '{print $NF}')" "$STDO_TOOLCHAIN_MIN"; then
  pipx install --force "$STDO_TOOLCHAIN_SPEC"
fi

stdo --version
stdo_version_at_least \
  "$(stdo --version | awk '{print $NF}')" "$STDO_TOOLCHAIN_MIN" || {
    echo "stdo-toolchain ${STDO_TOOLCHAIN_MIN} or newer is required" >&2
    exit 1
  }

stdo install "$STDO_CUT"
stdo verify "$STDO_CUT"
```

The exact qualified RC3 install is the missing-tool path. The explicit
`pipx install --force` branch upgrades an older installation. Do not continue
to `stdo install` unless the final version check accepts `stdo-toolchain
0.1.2` or newer.

Resolve and copy the Product Definition and Project Reference-Frame Basis
templates from that same installed cut:

```sh
STDO_TEMPLATE_PATH="$(
  stdo resolve \
    "stdo://releases/${STDO_CUT}/standards/templates/PRODUCT_DEFINITION_TEMPLATE.json" |
    python3 -c 'import json, sys; print(json.load(sys.stdin)["path"])'
)"
STDO_FRAME_TEMPLATE_PATH="$(
  stdo resolve \
    "stdo://releases/${STDO_CUT}/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md" |
    python3 -c 'import json, sys; print(json.load(sys.stdin)["path"])'
)"

python3 - \
  "$STDO_TEMPLATE_PATH" ./stdo_default.json \
  "$STDO_FRAME_TEMPLATE_PATH" ./specification/REFERENCE_FRAME_BASIS.md <<'PY'
import os
import pathlib
import sys
import tempfile

arguments = sys.argv[1:]
if not arguments or len(arguments) % 2:
    raise SystemExit("expected one or more source/target pairs")

pairs = [
    (pathlib.Path(source_name), pathlib.Path(target_name))
    for source_name, target_name in zip(
        arguments[::2], arguments[1::2], strict=True
    )
]
if len({target.absolute() for _, target in pairs}) != len(pairs):
    raise SystemExit("refusing duplicate STDO setup targets")

# Preflight every source and target before creating a directory or file.
prepared = []
for source, target in pairs:
    if not source.is_file():
        raise SystemExit(f"missing STDO setup source: {source}")
    payload = source.read_bytes()
    if target.exists() or target.is_symlink():
        raise SystemExit(
            f"refusing to overwrite existing STDO setup file: {target}"
        )

    ancestor = target.parent
    while not ancestor.exists() and not ancestor.is_symlink():
        ancestor = ancestor.parent
    if not ancestor.is_dir():
        raise SystemExit(f"STDO setup target parent is not a directory: {ancestor}")
    prepared.append((target, payload, source.stat().st_mode & 0o777))

created_directories = []
staged = []
owned_outputs = {}


def create_parents(parent):
    missing = []
    cursor = parent
    while not cursor.exists():
        missing.append(cursor)
        cursor = cursor.parent
    for directory in reversed(missing):
        try:
            directory.mkdir()
        except FileExistsError:
            if not directory.is_dir():
                raise
        else:
            created_directories.append(directory)


def remember_owned(path, identity=None):
    if identity is None:
        stat = path.stat()
        identity = (stat.st_dev, stat.st_ino)
    owned_outputs.setdefault(path, set()).add(identity)


def remove_if_owned(path):
    identities = owned_outputs.get(path, set())
    try:
        stat = path.stat()
    except FileNotFoundError:
        return
    if (stat.st_dev, stat.st_ino) in identities:
        path.unlink()

try:
    for target, payload, mode in prepared:
        create_parents(target.parent)
        descriptor, stage_name = tempfile.mkstemp(
            dir=target.parent,
            prefix=f".{target.name}.stdo-stage-",
        )
        stage = pathlib.Path(stage_name)
        staged.append(stage)
        os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "wb") as output:
            output.write(payload)
            output.flush()
            os.fsync(output.fileno())

    # Reserve every final name without overwriting a racing existing file.
    for target, _, _ in prepared:
        descriptor = os.open(
            target,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
        os.close(descriptor)
        remember_owned(target)

    # Each replacement is an atomic rename into a name reserved by this run.
    for stage, (target, _, _) in zip(staged.copy(), prepared, strict=True):
        stat = stage.stat()
        remember_owned(target, (stat.st_dev, stat.st_ino))
        os.replace(stage, target)
        staged.remove(stage)
except BaseException:
    for target in reversed(list(owned_outputs)):
        remove_if_owned(target)
    for stage in staged:
        stage.unlink(missing_ok=True)
    for directory in reversed(created_directories):
        try:
            directory.rmdir()
        except OSError:
            pass
    raise
PY
```

Use the installed cut's `templates/README.md` to fill the definition over the
existing layout. Bind a real Product-owned reference-frame basis, `WHAT`,
`HOW`, work carriers, and every known Product composition edge. Replace every
placeholder. A delegated agent may draft a complete provisional basis, but it
must return that exact draft and stop for Product-owner ratification. The
Product owner records and admits acceptance; the drafting agent cannot record,
admit, or infer that acceptance itself. A copied or completed template is not
accepted merely because it exists.

Then preview and install only the marker-owned agent bootstrap:

```sh
stdo sync --definition stdo_default.json
stdo status --definition stdo_default.json --verify
stdo bootstrap --definition stdo_default.json --dry-run
stdo bootstrap --definition stdo_default.json
```

A repository checkout also contains `QUICKSTART.md` with the expanded
field-by-field walkthrough. The plugin does not depend on that repository-root
file; this packaged guide remains sufficient after installation.

### Install The Shared Skills

The `spec` plugin version and immutable repository cut are aligned at
`2.5.0-rc.3`. RC2 retains its earlier Claude-only refresh payload and never
moves. The Specification Stack marketplace name is `specification_stack`.

Claude Code:

```sh
SPEC_PLUGIN_REF='specification_methodology/v2.5.0-rc.3'
claude plugin marketplace add \
  "foolishimp/specification_methodology@${SPEC_PLUGIN_REF}"
claude plugin install spec@specification_stack
```

Codex:

```sh
SPEC_PLUGIN_REF='specification_methodology/v2.5.0-rc.3'
codex plugin marketplace add foolishimp/specification_methodology \
  --ref "$SPEC_PLUGIN_REF"
codex plugin add spec@specification_stack
```

Both hosts consume the same workflow skill bytes. Use this conversational
convention:

| Say | Portable skill | Claude | Codex |
|---|---|---|---|
| `stdo help` | `stdo-help` | `/spec:stdo-help` | `$spec:stdo-help` |
| `stdo ticket` | `stdo-ticket` | `/spec:stdo-ticket` | `$spec:stdo-ticket` |
| `stdo work` | `stdo-work` | `/spec:stdo-work` | `$spec:stdo-work` |
| `stdo review` | `stdo-review` | `/spec:stdo-review` | `$spec:stdo-review` |
| `stdo status` | `stdo-status` | `/spec:stdo-status` | `$spec:stdo-status` |

Natural-language invocation remains valid. In chat, `stdo status` requests
Product/work status through the skill. In a shell, `stdo status --definition
...` remains the toolchain command for installed-basis health.

## 2. Iterate Requirements

Every feature, bug, failed test, operator finding, scenario failure, or release
concern begins with intake triage. The intake label does not decide where work
starts.

### Find The First Changed Layer

| First changed layer | Change class | Re-entry point |
|---|---|---|
| current work-wave focus | `goal_reprice` | Goals |
| purpose or scope | `intent_reprice` | Intent |
| Product shape, terms, or boundary | `product_reprice` | Product |
| invariant truth | `requirement_reprice` | Requirements |
| realization structure | `design_reframe` | Design |
| code or configuration only | `realization_refactor` | realized surface |

Before substantive execution, establish applicable upstream work authority,
then derive and admit one run-scoped execution contract from the first matching
row. A ticket cannot substitute for missing upstream authority. For work inside
an admitted sprint, the local carrier boundary is that sprint; otherwise it is
the current run.

| Situation | Smallest carrier | New durable ticket? |
|---|---|---|
| no applicable upstream work authority exists | none | no substitute ticket; stop or re-enter |
| an admitted ticket already covers the exact work | derive the run contract from it | no; reuse it |
| no exact admitted ticket covers the work and independent state is needed beyond the local carrier boundary | durable ticket plus run contract | yes, under ticket-state authority |
| no exact admitted ticket covers work that ends inside its admitted sprint | manifest-local iteration entry | no |
| no exact admitted ticket or sprint covers authorized work that ends in this run | intake-drafted run contract | no |

`Ticket-shaped` describes required execution-contract fields; it does not mean
“create a ticket.” Drafting, admission, and execution may occur in the same
invocation. A drafted or rejected contract stops before construction, while an
admitted one does not require another ticket, turn, or approval ceremony.
The admitted result names the Product-bound mechanism and authority, exact
contract identity or digest, decision, and evidence; the drafting model cannot
supply those coordinates by assertion. The contract also names an authorized
Product-bound durable result/evidence surface. Every result, withheld closure,
and residual is recorded there before return; a conversation return alone is
not durable evidence.
If the run discovers an obligation that needs state beyond the local carrier
boundary, persist it only when the current exact grant already includes the
required ticket-state mutation. Otherwise retain it in the contract's named
durable result/evidence surface or an already-authorized enclosing carrier,
mark closure withheld, and return the re-entry pressure plus an explicit `stdo
ticket` route without invoking it.

The base ticket fields are exactly `id`, `title`, `type`, `ticket_category`,
`status`, `goal`, `change_intent`, `change_class`, `re_entry_point`,
`triaged_at`, `created_at`, and `updated_at`. Execution admission additionally
binds `target_truth`, relevant `superseded_truth`, `closure_law`,
`evaluation_criteria`, `non_closure_conditions`, and `proof_surface`. Record
dependencies where applicable. The Product Definition locates the actual
lanes; `.ai-workspace/tickets/` is only the default.

### Change Requirement Truth

For `requirement_reprice`:

1. confirm that Goals, Intent, and Product still support the requirement;
2. establish the new present-tense requirement version as the sole operative
   truth; supersede or withdraw a published live domain artifact instead of
   silently correcting it in place;
3. give each requirement family `Family`, lifecycle `Status`, and `Category`;
4. state stable obligations and explicit acceptance criteria;
5. provide written testcase or other proof authority;
6. expose lifecycle gaps rather than letting design or code decide them;
7. leave incidental realization choice in design; and
8. re-derive affected design, scenarios, code, and proof.

If the requirement already exists but its structural realization is missing,
re-enter design. If requirements and design are current and code deviated, use
`realization_refactor`. Current code is evidence, not authority.

## 3. Start Code Development And Testing

Raw prompt wording does not authorize implementation. Code work begins when an
admitted work carrier supplies a reconstructable basis:

- selected Product outcome;
- lawful re-entry point and target truth;
- governing requirement and accepted design where required;
- smallest coherent affected relation set;
- exact operation grant, mutation subject, and write territory;
- closure law, evaluation criteria, and non-closure conditions; and
- proof, review, stop, and upstream re-entry conditions.

When the Product adopts the optional STDO engagement profile, the practical
split is:

| Frame | Owns | Does not gain automatically |
|---|---|---|
| Executive | bounded attention, activation, result consumption, Product-owned priority and boundary effect, disposition, checkpoint, next already-authorized action | implementation, publication, or new decision authority |
| Worker | bounded construction, tests, and self-review under the exact operation grant | acceptance, independent review, or continuation |
| Reviewer | independent evaluation and evidence-bound technical triage for one exact claim | repair, Product priority, disposition, or next activation |

The frame label grants nothing. The Project Reference-Frame Basis binds the
actors, capabilities, authorities, results, scales, cutoff, hard stops, and
invalidation law. One person or agent may occupy different frames across
different claims only when every grant and any claimed independence remain
valid.

### Derive Tests From Authority

```text
work carrier -> intake triage -> re-entry point
             -> requirement/design/module/closure law -> expected result
```

Use proof breadth that matches the claim:

- unit tests prove module-owned law;
- integration tests prove participating boundaries together;
- harnessed sandbox UAT proves a composed Product path deterministically;
- live sandbox UAT crosses the real external worker or service when the claim
  depends on that live boundary; and
- installed-development proof exercises the built or installed Product through
  its declared public path.

Start with the cheapest focused falsifier adequate for the active relation.
Run broader qualification at the candidate boundary or earlier when risk
requires it. Green evidence does not close a claim when it exercised the wrong
subject, fixture, route, authority, or external-boundary substitute.

Worker returns one exact candidate and evidence, then stops. Product-owned
authority decides whether independent review is required. Reviewer returns one
closed result. Executive, when adopted and authorized, applies priority and
disposition. Repair creates a new candidate and invalidates affected results.

## 4. Monitor And Help Triage

Monitoring is read-only unless the user separately authorizes a state change.
Read in this order:

1. verify the selected STDO basis;
2. read current Goals;
3. read authoritative active, backlog, and completed work state;
4. identify the accepted checkpoint and current workspace delta;
5. inspect observed tests, installed/runtime evidence, and exact reviews; and
6. compare claims only when they share the same subject and basis.

Default commands apply only when the Product Definition binds the default
layout:

```sh
stdo status --definition stdo_default.json --verify
rg --files .ai-workspace/tickets/active .ai-workspace/tickets/backlog
git status --short --branch
```

A useful status report leads with the Product outcome and includes:

- basis health;
- accepted Product movement since the comparison point;
- active work and dependencies;
- exact proof and review state;
- blockers, residuals, drift, and uncertainty;
- proposed triage or decisions needed; and
- the next already-authorized action.

Do not use prose volume, commit count, test count, or review count as Product
progress by itself.

Reviewer technical triage and Executive delivery priority are distinct. Under
the STDO engagement profile, Reviewer may return technical severity, impact,
confidence, blast radius, workaround, repair complexity, regression risk, and
uncertainty. Executive combines that evidence with the complete Product view
and current release or MVP mandate to assign Product-owned priority,
promotion-boundary effect, disposition, and action. The Project Reference-
Frame Basis owns the concrete scales, cutoff, and non-waivable hard stops. STDO
does not impose a universal P2 release cutoff.

Status may propose a likely change class and re-entry point. It does not
silently create a ticket, widen a release boundary, reprioritize the Product,
or apply disposition.

## Common Stops

| Condition | Response |
|---|---|
| zero or several Product Definitions apply | stop and disambiguate Product scope |
| installed cut or manifest does not verify | stop; never substitute mutable source |
| reference-frame basis is missing or a placeholder | return the missing Product-owned acceptance basis |
| no admitted run-scoped execution contract exists | select the smallest carrier, draft and validate the contract, then continue in the same invocation only if admitted |
| requirement truth is missing | re-enter requirements, not code |
| structural decision is missing | re-enter design |
| code and test disagree | reconcile through governing authority |
| independent review is required | stabilize one exact review subject and activate Reviewer; freeze before material reference exposure where generic-method qualification requires it |
| a finding is adjacent to the current claim | return it as triage input; do not automatically block |
| requested effect exceeds the grant | refuse and return to Product-owned decision authority |

## Owning References

Resolve these from the exact installed basis selected by the Product
Definition:

- `SPEC_METHOD.md` — constitutional chain, triage, requirements,
  construction, testing, and proportional delivery;
- `TICKET_METHOD.md` — work carriers, fields, states, execution contract, test
  authority, and projection;
- `RELEASE_METHOD.md` — immutable cuts, qualified transport refs, publication,
  successor identity, and release evidence;
- `REFERENCE_FRAME_METHOD.md` — bounded evaluation and result law; and
- `STDO_REFERENCE_FRAME_BASELINE.md` — optional Executive, Worker, Reviewer,
  testing, technical-triage, and disposition profile.

Claude retains the legacy manual-only `refresh` loader for a full exact owning
document. Codex should resolve and read that exact installed member directly;
the five daily workflow skills remain byte-shared. Daily work should read the
smallest relevant source surface.
