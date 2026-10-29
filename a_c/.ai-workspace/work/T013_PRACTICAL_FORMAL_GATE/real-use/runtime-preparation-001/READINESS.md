# Source-only runtime preparation

The actual a_c Product definition still points to T013 at
`/reference_frame_bases/0/authority/6`. Under the separately recorded Writer
grant, T013 now contains the selected runtime-owner JSON at lines **134–210**.
Its current whole-file SHA-256 is
`fbcf3edf07ae81071ed2d5864bcc7ed7ed946f524edefe17b2ff206252dfa524`.
The original ticket bytes are preserved exactly in
`owner-binding/ticket.before.md`; the append is recorded by
`owner-binding/RECEIPT.json`. Product definition and prior preparation/contract
closures are unchanged. The initial `AUTHORITY_GAP.json` remains historical;
the subsequent exact owner route resolves that gap.

The binding names the same two Workers, task, mechanism, result surface,
invocation limit and selected bounds. It publishes existing owner-approved
operation scope. It grants no assessment, acceptance, new Product feature or
release. No T008 runtime grant is reused.

`prepare_runtime.py` produces packets, standard closed-return contracts/output
schemas, exact source maps, fixed actor_cli plans, guarded policies and public
Context requests. `request_builder.py` constructs each later request from actual
public response references without executing it. `compare_contexts.py` will
compare actual retained Contexts with the complete current pure construction,
the frozen view and all shared source bytes. Its result is not evidence that
the transport has forwarded those bytes; that is checked separately against
helper `context.bin` and the public Attempt delivery observations.

The selected source-only output is **`templates-004/`**. Earlier local drafts
remain preparation history. The selected policies contain a null checker and
pending execution selection and cannot load as runtime policies. Separate
`policy.shape-only.json` files have no executor, no work grants and only public
read/description permission. Their public Runtime/source/schema checks do not
admit execution. Neither arm has a Context, Attempt, gate or actor outcome.

## Finalization after the candidate freeze

The Executive supplies the exact selected checker configuration and an
`a_c.T013.execution-selection/1` record with `state: "selected"`, the reviewed
TASK/PROTOCOL hashes, current ticket hash, exact current `source_pins` shown in
the template manifest, canonical checker-config digest, one invocation per arm,
and `automatic_retry: false`. That supplied record is retained as the external
selection premise. The builder does not authenticate an Executive by parsing
JSON. Any changed owner/admission implementation requires source re-entry.

Select two existing empty, regular task directories outside the protected a_c
source root, under a separate execution-stage filesystem grant. Template mode
creates neither. The finalizer stages the same immutable input bytes into both
and writes only its new runtime directory plus those explicitly supplied fresh
workspaces. It never runs the CLI, gate, public tool, actor or tests.

```sh
python3 -B prepare_runtime.py --out <fresh-directory-under-this-runtime-preparation> \
  --workspace-ungated <fresh-empty-ungated-directory> \
  --workspace-gated <fresh-empty-gated-directory> \
  --checker-config <exact-selected-checker.json> \
  --execution-selection <exact-executive-selection.json>
```

Source-only review of the final plans comes before execution. The exact
`ac_support.py --policy <policy> --policy-sha256 <raw-policy-sha> --principal
executive call --request <request>` path then acquires sources and creates each
actual Context. Compare them before either dispatch. Preflight and dispatch
retain their current checks; the gated arm requires its selected formal proof.
The request builder refuses preparation manifests and refuses a dispatch request
unless the actual public preflight response says admitted. It cannot itself
authenticate a response; the public tool revalidates the actual retained chain.

Both actors receive identical substantive inputs, default native CLI
model/settings, workspace-write and the selected 900-second actor limit.
The outer supervisor is bounded to 1,000 seconds; each output cap is 16 MiB,
stdin cap 2 MiB and termination grace 2 seconds. There is one call per arm,
without automatic retry. Unknown host context remains unknown. Input ceiling
is transport protection, not a qualified model-context-capacity assertion.

The writable territory is the three task deliverables plus `support/` and
`scratch/`. The immutable `inputs/` directory is excluded. The standard Worker
return requires an acquired candidate route: the Worker writes
`support/candidate.json`, listing actual deliverable hashes and byte lengths,
then returns its exact SourceRef and actual test-evidence SourceRefs. These are
transport/provenance requirements applied equally to both arms, not a second
task or an independent acceptance decision.

## Remaining live checks

Before dispatch: candidate/checker and current support selection; reviewed final
runtime records; fresh workspace/input state; actual source acquisition and
source currentness; exact actual Context comparison; actual gate/preflight
results; executable/loader/settings currentness; provider availability and
acceptance of the selected final schema. Template shape success establishes
none of these live outcomes.

After dispatch: exactly one actual attempt per arm; complete raw JSONL and usage;
actual helper/public-delivery byte equality; terminal process/effect standing;
authenticated and bound closed return; exact acquired candidate/test artifacts;
input immutability and access-scope observations; full interval/token/tool/rework
ledger; independent assessment of both frozen outputs. Unreported model, money,
provider retries or hidden context remain unknown. No proof/compiler/model run
has been used to prepare this setup.
