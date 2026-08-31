# Native Skill Smoke

Date: 2026-08-31

Both repository-native discovery surfaces loaded `stdo-representation` from
the repository root and recovered the exact Product program URI without source
mutation.

## Codex

- host: `codex-cli 0.150.1`;
- model: `gpt-5.6-sol`;
- reasoning effort: `low`;
- invocation: `$stdo-representation` under `codex exec --ephemeral`;
- output: `codex.txt`; and
- output SHA-256:
  `117a1ee86faca31048202835c85e5d4da116ce180fb559003afee7f02db81f64`.

## Claude

- host: Claude Code `2.1.251`;
- model: `claude-fable-5` through alias `fable`;
- effort: `low`;
- invocation: `/stdo-representation` with only the `Read` tool;
- output: `claude.txt`; and
- output SHA-256:
  `51b6fb8cba5e4e1841f63032bb35b7e5c7391f4d55734c72d6afd0baddfc9792`.

Both outputs identify:

`urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.1:run-001`.

This proves native discovery and exact map pickup only. It does not prove
semantic fidelity, usefulness, authority, or model equivalence.
