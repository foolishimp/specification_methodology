# Declared test interventions

The original expectation freeze remains unchanged at SHA-256
`b50b63d4c1fc917747e9123fad131f845ab0208ba277a41f1776774faff25250`.
The candidate source freeze remains unchanged at SHA-256
`6d10acddf9821764b29a8d3f95441be4fe6a5e7aa60915b3d7eefd4ca8703782`.

1. The first isolated-store copy omitted the store registry and real manager
   verification refused. The preparation script now also copies the retained
   relative-path registry. The completed isolated-store verification was real
   manager verification, not a stub. This happened before model invocation.
2. The initial Codex process supplied an approval flag that the configured
   launcher also supplied. The CLI rejected it before model execution. Its
   output is preserved in `runs/direct-launch-error/`. Root authorized one
   transport-only replacement; the redundant flag was removed, leaving
   configured authorization unchanged.
3. Initial native sessions are preserved in `runs/direct/` and `runs/issuer/`,
   with raw fixture state under `fixtures/initial/`. The direct session refused
   because the login shell reset PATH, bypassing the isolated-store launcher.
   The fixture's real isolated store was valid, but the actor used the shared
   store, where 3.0.3 is not installed. This is a harness availability failure.
4. The original relay used `direct-relay.md` and `worker-relay.md` rather than
   the contract-named result files. This is a harness result-routing defect,
   independently reported by the reviewer. New runs relay only to the exact
   named surface, preserving an existing actor-written result and recording
   the relay receipt. The original direct run remains an unfulfilled durable
   result relation; it is not retroactively repaired.
5. A new fixture suite explicitly binds `/Users/jim/.local/bin/stdo --store
   <isolated-store>` in AGENTS/CLAUDE entry metadata. It does not depend on PATH.
   The excluded-parent wording explicitly distinguishes directory listings
   from the already-admitted exact method-manager/store/skill routes. These
   are fixture binding corrections, not candidate changes.
6. The first Claude issuer request named help/ticket/work/status as relevant.
   It loaded all four exact candidate bodies, made 43 tool calls and acquired
   191,713 bytes of tool-result strings before the 180-second deadline. It
   produced no final packet. It also read outside its own permitted input set;
   later success cannot turn that run into a compliant issuer witness. The
   revised issuer request names only stdo-work and the exact issuer/worker
   contracts, the ordinary documented invocation. It contains no oracle,
   expected verdict, suspected defect or new forbidden-read reminder.
7. Root explicitly authorized four further actual sessions, for at most six
   actual model sessions total plus the one pre-model CLI failure: direct
   retry <=180s; focused issuer <=300s; fresh receiver of that actual packet
   <=240s; negative/review <=180s. The new fixture contracts and runner bind
   those limits. Receiving is dependent on an actual returned issuer packet;
   an owner-authored substitute will not be invented if issuing fails.

The revised runs are new subjects with changed fixture/host bindings and, for
the issuer, a narrower request and changed time envelope. They are not an
unchanged rerun or independent proof of a candidate repair. Provider system
and configured user instructions remain not fully exposed; the sessions are
fresh with respect to fixture conversation, not certified free of all host
context. Actual model selection is left at each host's configured default.

8. The corrected direct run timed out after recognizing valid direct authority, without editing the label. The runner had selected its last progress message as a final result. This extraction defect is explicitly withdrawn in `runs/direct-rebound/EXTRACTION_CORRECTION.json`; original bytes remain. Future extraction requires a no-timeout terminal completion event. No extra session is authorized or started for this repair.

The initial Claude issuer did verify its selected store successfully; the Codex login-shell store failure does not explain the Claude timeout. They remain separate observations.
