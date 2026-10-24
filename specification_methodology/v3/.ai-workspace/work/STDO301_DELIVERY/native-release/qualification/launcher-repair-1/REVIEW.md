# Installed-task launcher review and disposition

This is Root Writer's transcription of two closed returns by the nonauthor
`/root/stdo301_application_review`. It is a same-family mechanics review,
selected because the subject is a bounded invocation wrapper rather than
source semantics. The reviewer performed no edits, installations, Git effects
or model invocations.

## Initial return: falsified

S2: the initial launcher handled timeout only. Its child starts a new process
session, so a launcher KeyboardInterrupt or termination could leave the actor
running without its 900-second supervision and without completion evidence.
An in-memory execution of the exact handler AST confirmed that interruption
escaped, issued no cleanup signal and did not reach the completion record.
Review stopped at this supported blocker. Original launcher SHA256:
`23b0f0eeb4e80e1b75629e000dcad9382760b686d096365fa0216be277549e2d`.
Original launch note SHA256:
`5d873f3f5b093d95298a0cc037f73915c43bde9f3aa1c92c49170a6abb8e81f1`.
Both preimages are preserved beside this record.

Root selected interruption handling, bounded whole-process-group cleanup and
truthful interrupted completion as the exact repair. No native/source/model
work was performed by this repair.

## Focused readback: satisfied for launcher mechanics

The prior S2 is discharged. Interruption is recorded before the child-assignment
boundary as well as during communication. Cleanup tests group absence separately
from direct exit, escalates TERM to KILL, and bounds both waits. Completion is
retained. Interruptions, timeouts, errors and unconfirmed cleanup cannot return
success. No new supported blocker was found in the affected cone.

The reviewer independently executed the exact functions in memory for eight
cases: ordinary exit, KeyboardInterrupt, pre-assignment SIGTERM, timeout, exited
parent with living group, TERM resistance, unconfirmed group and cleanup error.
All produced the expected retained completion and status. No reviewer subprocess
or actor was started. Source was inspected before author outcomes. The review
also checked the current hash against the four author subprocess controls; it
did not rerun them.

Reviewed pins:

- `../run_actor.py`: `fd2a8d60582d2b323083575d11dd06e5a80cf00b8a4ad9b0d72af071a1ed88d9`.
- `../LAUNCH.md`: `191bb446544d015a3495b2fc93897d0ad9c46d31c69fed20d2d887ee81dd95e0`.
- `lifecycle-probes.json`: `0096d7ff63855cf66769838e2fa5f0ac7a1c4721506e413610e1eee0dcbf0cbb`.

## Limits and Executive disposition

The CLI help supports the declared safe/restricted modes, read-tool inventory,
empty strict MCP configuration and disabled persistence. Actual runtime
initialization, resolved model/tools, source access, terminal result/usage and
unchanged installed bytes remain Root checks at each invocation. Native identity
is a Root-supplied prerequisite; the launcher only checks the installed entry
exists. Prompt pinning, exclusive output creation and absence of automatic
retry/resume are supported; transport success is not semantic assessment.

Uncatchable SIGKILL, host failure or another missing handoff requires external
reconciliation. The process-group observation is not a claim about arbitrarily
detached processes. The qualified actor has only confined read tools and no
shell or MCP capability.

Executive disposition: admit the repaired launcher for the four already
selected installed-route tasks once the native source readback, sealing and
installation prerequisites close. No task was invoked by preparation or review.
