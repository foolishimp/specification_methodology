# Bounded host-capability findings

Research only. No model/actor session was launched, no credentials were read,
and no global settings, installation or original campaign evidence changed.

## Codex 0.164.0

`codex --disable memories ...` is a supported session override. The local
`features list` declares `memories` stable; the session override actually changes
its effective state from true to false without editing the global configuration.
`CODEX_FEATURES.json` retains the command and observation. This is preferable to
inventing a configuration key or turning off all user configuration.

`codex debug prompt-input` renders the model-visible input list without a model
task. Two render-only calls succeeded in the corrected fixture, with and without
the flag; the available native stdo-work skill and fixture instructions remained
present. Neither render included the memory-path/summary markers tested, even
without the flag. Thus the render does not by itself demonstrate that every
runtime memory/context path is suppressed. Only safe marker/size/digest summaries
were retained, not the rendered private instructions.

Current nonsecret configuration selects `gpt-6-astra` and `max` reasoning effort.
The original stream did not expose its effective model, so this current setting
does not retroactively replace that limitation. Preserve the existing model
configuration in a later probe; the memory flag needs no model change.

Native local `.agents/skills` discovery and exact source acquisition have already
been observed. The inspected CLI help exposes no session-only plugin-directory
flag, so this remains a local-skill route rather than a plugin-install trial.
No verified per-command or exact-file read boundary was established for Codex's
general shell. `read-only` and `workspace-write` sandbox names do not establish
the packet's acquisition boundary. Memory suppression is not a substitute for
that distinction or for observing subsequent tool reads.

## Claude Code 2.1.306

Local help supports session-only `--plugin-dir`, `--tools`, `--settings`,
`--restricted`, `--strict-mcp-config` and `--no-session-persistence`.
`--tools` can remove Glob, Grep, Edit, Write and Agent from an issuer's tool
surface. `--restricted` ignores user/project/local settings and confines file
tools to working directories; managed settings still apply. The observed
`claude-fable-5-1` can be bound explicitly if ignoring settings would otherwise
change model selection. This is a supported host configuration proposal, not a
tested successor run. [Official CLI reference](https://code.claude.com/docs/en/cli-reference)

Session `--settings` can carry `autoMemoryEnabled: false` and
`claudeMdExcludes` patterns for unselected instruction paths. Exclusions cannot
suppress managed instructions. Selected fixture AGENTS/CLAUDE instructions and
the explicit plugin should remain admitted. The current local `--bare` help
says it changes authentication to API-key/helper routes and skips keychain/OAuth;
the successful trial exposed `apiKeySource: none`. Bare-mode compatibility is
therefore unestablished and should not be assumed.
[Official memory documentation](https://code.claude.com/docs/en/memory)

**An allow list in `--allowedTools` plus `dontAsk` is not a strict command
allowlist.** Built-in read-only Bash commands, including directory listings,
remain automatically allowed. File reads inside working directories also need
no approval. Exact allow rules cannot carve exceptions out of broader deny/ask
rules. Keeping Bash available therefore needs an additional control if arbitrary
directory discovery must be prevented. These native permission settings do not
establish the desired boundary by themselves.
[Official permission documentation](https://code.claude.com/docs/en/permissions)

The documented `PreToolUse` hook can inspect tool input before execution and
return a deny decision. A fixture-only session hook could reject every Read
whose exact resolved path is not admitted and every Bash call except full exact
real-manager, admission and verified-section-reader commands. It should return
no additional instructional context, log actual decisions, and be tested before
any behavioral claim. This would be an explicit host binding with its own
qualification scope, not proof that skill prose enforces isolation. No hook was
implemented or installed during this research.
[Official hook documentation](https://code.claude.com/docs/en/hooks)

## Bounded recommendation

For the next separately authorized trial, retain the frozen original failures;
use the native candidate skill; disable Codex memories only for that invocation;
and, for a Claude issuer, select a small declared tool surface plus a supported
session control if exact read/command restrictions are required. Bind absolute
real-manager/store routes and the exact result relay. Do not grant broader
inputs merely because the host asks for them. Unmeasured managed/system context
and unsupported confinement remain explicit. A successor result should be
claimed only for the exact observed host binding and task.
