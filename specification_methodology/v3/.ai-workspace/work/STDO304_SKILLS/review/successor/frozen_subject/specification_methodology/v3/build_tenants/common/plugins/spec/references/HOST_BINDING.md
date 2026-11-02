# Bind The Actual Host

The Product supplies the actor's required context/acquisition boundary and
operation grant. Bind the actual session to it before dependent work. These
adapters project an already-authorized policy; they create no admission and
are optional when a Product already selects sufficient tools. Use those
declared tools rather than installing a competing mechanism.

## Claude: Explicit Session Tool Policy

Claude's documented `PreToolUse` event can deny a tool call before it runs.
The bundled [claude_tool_gate.py](../scripts/claude_tool_gate.py) consumes a
Product-owned, digest-pinned policy of this form:

```json
{
  "kind": "stdo.claude-tool-policy",
  "schema_version": 1,
  "policy_id": "<exact policy identity>",
  "authority_ref": "<existing grant identity and source route>",
  "cwd": "<canonical absolute worksite>",
  "read_paths": ["<canonical absolute permitted control file>"],
  "bash_commands": ["<complete exact permitted command string>"],
  "skills": ["spec:stdo-work"]
}
```

The operation owner supplies the approved reads/commands and checks their
outputs against the actor's acquisition boundary. The adapter does not parse
shell syntax or infer what a command may do. No wildcards apply. A changed
command, unlisted path/skill, redirected path, changed cwd, unknown tool/event,
unsupported parameters, changed policy digest or failed check is denied.
Read ranges may narrow an approved file. Skill calls accept the selected name
without added arguments. Background execution and permission overrides are
unsupported. A trusted allowed command's internal reads, effects and outputs
remain that command's contract; exact string equality does not prove them.

Select the policy and optional audit path through an authorized session
binding. Do not edit global host settings. A session settings fragment is:

```json
{
  "autoMemoryEnabled": false,
  "hooks": {
    "PreToolUse": [{
      "matcher": ".*",
      "hooks": [{
        "type": "command",
        "command": "<absolute Python executable>",
        "args": ["<absolute plugin>/scripts/claude_tool_gate.py", "--policy", "<absolute policy>", "--policy-sha256", "<policy sha256>", "--audit", "<authorized JSONL result path>"],
        "timeout": 10,
        "onFailure": "block"
      }]
    }]
  }
}
```

The audit option is an explicit append effect; omit it without that grant.
It records decision, policy identity, tool identity and event digest, without
copying tool output. Failure to append when selected denies the tool call.
Keep the policy, adapter and any command implementation outside the actor's
write grant. Register the hook for every tool, with failure blocking selected;
otherwise a crash, timeout or unmatched tool could bypass the intended gate.

Bind the available tool roster to `Read,Skill,Bash` for the supported policy
surface, the explicit plugin root, selected worksite and exact session settings.
The observed CLI supports session `--plugin-dir`, `--tools`, `--settings`,
`--restricted`, `--strict-mcp-config` and `--no-session-persistence`; verify
those capabilities on the selected host before depending on them. Use the
already-selected actor/model. An allow list plus `dontAsk` alone does not
confine built-in read-only shell commands, so it is not this gate's substitute.

This covers the hooked tool calls. It does **not** control existing context,
system/managed instructions, native file mentions expanded before a tool call,
or a permitted program's internal acquisition. The run binding must account
for these routes; in a tool-confined trial, supply no unselected file mentions
and admit the actual plugin/control inputs. If the required claim excludes
unmeasured host context, that claim is unsupported by this adapter. A failed
or denied attempt is not a successful acquisition or completed work result.

Documented interface: [Claude hook reference](https://code.claude.com/docs/en/hooks),
[CLI reference](https://code.claude.com/docs/en/cli-reference) and
[memory controls](https://code.claude.com/docs/en/memory). Session controls were
inspected on Claude Code 2.1.306; actual qualification binds its exact retained run.

## Codex: Declare The Remaining Boundary

Codex 0.164.0 exposes the session override `--disable memories`; its effective
feature state was locally checked. It removes that enabled feature for the
invocation without editing global configuration. It does not establish that
all ambient instructions are absent or that shell reads match the contract.

No exact-file/command acquisition gate for Codex's general shell is established
by this delivery. A grant requiring that capability cannot be discharged by a
fresh context, `read-only`/`workspace-write` names, or the memory flag. Use an
already-declared compatible mechanism, or return the unsupported capability
before dependent work. Direct tasks whose admitted envelope permits the actual
host can still use the normal skill. Report the observed context/tool limits;
do not relabel instruction-following as enforced isolation.
