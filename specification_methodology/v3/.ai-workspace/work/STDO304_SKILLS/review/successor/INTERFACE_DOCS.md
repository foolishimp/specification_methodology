# Current external interface check

Retrieved 2026-11-03 Australia/Sydney from the primary Claude Code hook reference:
https://code.claude.com/docs/en/hooks#command-hook-fields and https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails .

The documented command hook accepts separate executable `command` and `args`, which invoke without a shell. `onFailure: "block"` is documented from Claude Code 2.1.295 onward for command/HTTP hooks; startup, timeout, abnormal exit and invalid JSON failures block the guarded action. This supports the revision-2 HOST_BINDING template's interface shape on its named 2.1.306 host. Documentation does not establish that a particular native run installed or honored the hook; that remains an actual trace question.

The CommonMark 0.31.2 fenced-code rule at https://spec.commonmark.org/0.31.2/#fenced-code-blocks was independently used for OP-02. No third-party search result supplies the finding's technical oracle.
