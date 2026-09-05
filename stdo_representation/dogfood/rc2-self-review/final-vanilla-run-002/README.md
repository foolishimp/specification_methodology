# Final Repaired Vanilla RC2 Check Receipt

## Outcome

One fresh vanilla Codex Reviewer evaluated the exact repaired Specification
Methodology STDO 2.5.0 RC2 candidate. The Reviewer returned one closed
`falsified` Reference Frame Method result with two S2 findings:

1. An adjacent observation outside the evaluated claim is incorrectly made an
   `out_of_frame` cause even when the exact claim itself remains decidable.
2. The executable checks reject some structural defects but do not establish
   semantic exclusivity or raw/compression/template congruence; the Reviewer
   supplied a passing in-memory counterexample population.

This receipt records this run only. No earlier review or comparison was
supplied to the Reviewer or used here.

## Exact Subject

- commit: `1126d21e23e8907ac0f6258450ef930f5560aa11`
- repository tree: `851241a6e00873ef437048d0d177eca5a6f4553a`
- Specification Methodology subtree:
  `9c99497a8e69b5533a9df85b3b3ca9c05aac4cdf`
- standards tree: `9421d06ee9a206db5cb15eee3cb4328cef486acb`
- standards population: 52 members
- standards aggregate SHA-256:
  `787b49219db716e9a7acd60b780889365a78751ed604e610348734dc2ef71f4a`
- extraction: `git archive` of the exact commit into
  `/tmp/stdo-final-vanilla2-snapshot.38WiTz/snapshot`
- snapshot state during review: read-only

All six supplied evidence hashes were reproduced before evaluation and again
after completion. T-022 content was admitted only for lines 1-64. The raw event
stream shows the Reviewer read only those lines from T-022.

## Isolation And Invocation

- invocation count: exactly one; no retry or resume
- thread: `01a0595d-90b1-76a2-a8f5-03d526f8bb52`
- CLI: `codex-cli 0.150.1`
- model: `gpt-5.6-sol`
- reasoning effort: `xhigh`
- working directory:
  `/tmp/stdo-final-vanilla2-snapshot.38WiTz/reviewer-empty`
- working-directory state before and after: empty
- sandbox: `read-only`
- session persistence: `--ephemeral`
- repository discovery: `--skip-git-repo-check`
- user configuration: excluded with `--ignore-user-config`
- user and project rules: excluded with `--ignore-rules`
- native/user skill discovery: excluded by using an isolated `CODEX_HOME`
  containing only the copied authentication file; that temporary credential
  copy was removed immediately after completion
- project bootstrap: absent because the Reviewer started in the empty
  non-repository directory
- request transport: stdin from `request.txt`
- event transport: JSONL stdout to `raw-events.jsonl`
- final-result transport: `--output-last-message result.txt`

The invocation was:

```text
CODEX_HOME=/tmp/stdo-final-vanilla2-snapshot.38WiTz/codex-home \
codex exec \
  --cd /tmp/stdo-final-vanilla2-snapshot.38WiTz/reviewer-empty \
  --skip-git-repo-check \
  --ephemeral \
  --ignore-user-config \
  --ignore-rules \
  --model gpt-5.6-sol \
  --config model_reasoning_effort="xhigh" \
  --sandbox read-only \
  --json \
  --color never \
  --output-last-message result.txt \
  -
```

## Completion And Timing

- started: `2026-08-31T19:48:18Z`
- completed: `2026-08-31T20:00:55Z`
- elapsed: 757 seconds
- Codex process exit status: 0
- terminal event: one `turn.completed`
- completed command executions: 15, all exit code 0
- Codex stderr: empty
- model usage:
  - input tokens: 744,877
  - cached input tokens: 647,424
  - cache-write input tokens: 0
  - output tokens: 20,191
  - reasoning output tokens: 13,753

## Artifacts

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `request.txt` | 7,146 | 137 | `9591b5ceec70dd67d2e66a97b41b8a04f89664d9cce877b77dc101dd0ceb78e8` |
| `raw-events.jsonl` | 413,092 | 37 | `4afc7dafa5065df25a248ff4b6389d0605cfa332a07827a0f561c27db5554cfb` |
| `result.txt` | 12,059 | 93 | `fa293ea22e19c060e19c5d58ba27b0d271cd978f8b9ef0bcfed900296255122e` |
| `stderr.txt` | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## Invalidation

This review receipt is exact only for the named subject, six admitted byte
sequences, evidence scope, request, model/configuration, and single activation.
Any change to those coordinates requires a new activation; this run must not be
silently reused as review of later bytes.
