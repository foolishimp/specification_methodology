# Optional required formal verification gate

T-012 refines this tenant's realization of [FR-008–FR-014](../../../specification/requirements/formalisation.md).
The Lean tenant owns the checked adapter contracts, source interpretation,
proofs and portable evidence format. This adapter owns the actual generation
and Worker delivery boundary. Formal verification does not grant work authority,
prove prose fidelity, discharge semantic acceptance or establish the whole calculus.

## Trusted selection

The operator selects an exact Lean tenant and Python executable once:

```sh
python3 a_c/build_tenants/graphify/code/ac_formal_gate.py \
  --lean-root /absolute/path/to/a_c/build_tenants/lean \
  --output /absolute/new/checker.json
```

The command prints the configuration's SHA-256. `checker.json` is a trusted
startup input, not a model-supplied command. It contains the fixed checker root,
Python executable digest, Graphify adapter digest, fixed entry digest, complete deciding runtime identity
and outer timeout. Generation selection and trusted support startup reject a
changed Graphify adapter. The selected Lean identity includes every deciding Python helper,
profile, core proof source, toolchain/Mathlib lock and the exact proof-support
manifest. Selection must be repeated explicitly after changing that basis.

Before executing checker code the parent independently hashes the selected
runtime pins, checks their aggregate identity and rejects changed or additional
Python/profile members. Source paths cannot escape the selected root or traverse
symlinks. Python environment overrides and user site packages are disabled;
source imports bypass bytecode caches. The pinned checker checks the support
manifest's compiler, imported proof objects and library members before use and
before returning success. Checking the child-reported identity supplements these
parent checks; it cannot replace them.

The adapter invokes only the fixed `scripts/formal_gate.py` CLI. The request
cannot supply commands, compiler options, implementation paths or schema changes.
Each outer invocation has its own process group. At timeout a bounded OS
PID/PPID/PGID census identifies its private descendant groups, excluding caller
and ancestor groups; a second bounded census before KILL covers children spawned
during TERM grace. TERM/KILL cleanup targets those positively observed groups
and the checker group, with bounded pipe draining and reaping. This also covers
the checker's nested proof groups when its parent stalls. An incomplete result
retains attribution and cleanup limits; it does not infer that escaped or
already reparented descendants ended.

## Ordinary generation

Select the required gate at `ac_generate prepare`, or at the first `assemble`
or `run`, using both startup coordinates:

```sh
python3 a_c/build_tenants/graphify/code/ac_generate.py prepare \
  --corpus /absolute/source --manifest /absolute/manifest.json \
  --output /absolute/new/run --mode direct \
  --formal-checker /absolute/checker.json --formal-checker-sha256 EXACT_SHA256
```

The plan and retained `formal-selection.json` bind that selection. Later commands
inherit it; a changed override or missing prepared selection refuses. The shared
`check_formal_proposal` helper is used by ordinary, grounded and repaired assembly,
including partial proposal variants. Those paths cannot bypass a selected gate.
`ac_generate run` uses the same helper when it reaches assembly.

The helper checks the exact generated `model.json` and actual `carrier.json` in
separate linked invocations. Both have `selections: []` and null supplied views:
this is model/carrier verification without a projection claim. The immutable
proposal retains both invocation results and their portable evidence bundles.
Verified formal structure still has proposal status and unassessed semantic
acceptance. A gate refusal, unsupported profile or operational failure leaves an
`unverified_proposal` and its corresponding `refused`, `unsupported` or
`incomplete` gate status. CLI exits are respectively 2, 3 and 4. A selected `run`
that does not reach assembly reports an incomplete gate. Existing calls with no
selection preserve their prior behavior and require no Lean installation.

## Context, admission and actual delivery

The trusted support policy optionally contains `formal_gate`, with `checker`
holding the complete selected configuration and `required_targets` listing
registered target principal IDs. Selecting no targets performs no verification.
This policy is itself digest-bound by the existing public CLI/server startup.
An untrusted request cannot add, remove or replace the target requirement.

`context.assemble` remains pure with respect to effect execution. For a required
target it retains the policy-derived pending formal condition, exact ordered
selections, actual computed views and the context rendering. That pending state
describes assembly; portable proof evidence is retained beside the Context after
the effect runs, so it cannot change the bytes it claims to cover. No compiler
is launched by the core or its `EffectPlan` preparation.

The preflight effect reacquires every model through the existing authorized
SourceRef engine, scope and digest checks. It snapshots those acquired bytes,
never accepts a Context-supplied filesystem path, and supplies the exact ordered
views, record budgets, rendering SHA-256 and activation identity to the selected
verifier. Empty selections verify their model only; required contexts with no
model subject refuse. Record budgets and the existing context byte capacity
remain separate constraints.

The effect stores an existing `raw` artifact carrying the checked bindings,
fixed invocation origin and hashes of the complete portable result bytes. The
preflight receipt references this evidence. Support envelopes remain integer-only;
the complete checker JSON, including fractional timings, stays in the hash-bound
sidecar. A supported formal refusal rejects the admission condition. Unsupported
capability and incomplete observation use the existing method result mapping.
All ordinary role, operation, composition, Grant, predicate and fit checks still
apply independently, including when the proof succeeds.

The effect reacquires material currentness after the potentially long proof call
as well as before it. Dispatch and supervisor do the same immediately after their
fresh replay, before reserving or launching the actual use.

Dispatch compares the current policy requirement, reconstructed rendering,
acquired model bytes, selections, views and activation against the receipt.
It checks the protected result bytes and invokes `check-evidence` for a fresh
proof replay. The supervisor repeats this check at the actual launch boundary
before sending the sealed rendering to Worker stdin. Neither a saved `verified`
field nor caller-supplied JSON can substitute for these executions. Existing
attempt reservation, uncertain-effect and retry/reconciliation behavior remains
in charge; the gate adds evidence to those boundaries rather than a second
orchestration lifecycle.

## Qualification and limits

`test_env/test_ac_formal_gate.py` contains narrow positive/adverse controls,
including changed helper code that tries to report the old identity, changed
support manifests, escaped model source paths, dropped policy requirements,
forged success, distinct failure statuses across all three producer paths, and
an actual timeout/descendant cleanup probe. Explicit doubles in these tests are
unit controls, not formal qualification evidence.

`test_env/qualify_formal_gate.py` runs two fresh subjects through ordinary public
generation, exercises grounded and repaired producers, and drives actual public
Context → preflight → dispatch → supervisor → controlled Worker stdin. It retains
the CLI inputs/outputs, process identities, exact received hash, tamper/refusal
cases and a successful proof with missing authority. Author answers are explicitly
test-authored/replayed; no paid LLM invocation or semantic quality claim is needed
to qualify these mechanics. Independent assessment remains separate.

The trusted Python parser/importer/generator, explicit schema-role interpretation,
compiler/runtime serialization and selected support-manifest establishment remain
the Lean tenant's declared trust boundary. This integration is a cooperative local
POSIX boundary, not isolation from an administrator rewriting the trusted startup
policy or protected evidence store. Large inputs can be incomplete under the
selected resource bounds; no truncation, weaker schema or fabricated proof fills
that gap.
