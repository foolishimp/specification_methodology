# Native Skill Discovery Smoke

Date: 2026-08-30

Subject:

- canonical skill: `skills/axiomatize-corpus/SKILL.md`;
- canonical skill SHA-256:
  `dcd2294e7de7ae5bfb4a70b3980594a36f9a3b28b42236523a86cbc42aa7babe`;
- Codex discovery path: `.agents/skills/axiomatize-corpus`;
- Claude discovery path: `.claude/skills/axiomatize-corpus`.

Both discovery paths resolve to the canonical directory and expose identical
skill bytes.

## Codex

Host: `codex-cli 0.150.1`

A fresh ephemeral `gpt-5.6-sol` session started at the repository root and
invoked `$axiomatize-corpus`. It returned:

```text
skill=axiomatize-corpus
validate=python3 build_tenants/core/code/ac.py validate
join=python3 build_tenants/core/code/ac.py join
```

## Claude

Host: `Claude Code 2.1.251`

A fresh non-persistent Fable session started at the repository root and invoked
`/axiomatize-corpus`. It returned:

```text
skill=axiomatize-corpus
validate=validate
join=join
```

The smoke sessions were instructed not to edit files or run the Product. This
evidence establishes native discovery and command pickup only; it does not
establish semantic program quality.
