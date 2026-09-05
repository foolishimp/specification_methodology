# Final Vanilla RC2 Self-Review Receipt

## Outcome

One fresh vanilla Codex Reviewer evaluated the exact frozen Specification
Methodology STDO 2.5.0 RC2 candidate. The Reviewer returned one closed
`falsified` Reference Frame Method result with two findings:

1. S2: the `out_of_frame` projection collapses general claim-material missing
   scope into the narrower outside-claim observation case.
2. S1: the focused tests are structural text/table checks and do not establish
   the claimed semantic, negative-authority, consumption, or refusal behavior.

This receipt records the run only. No comparison with another review was
performed here.

## Exact Subject

- commit: `cfd1e3332cafadea6e2522fe7aaa0918163e5eca`
- repository tree: `f9d45347022989d476027630bb9d78498888e508`
- Specification Methodology subtree:
  `240e2ca6654db1f3e0a5acb08faaeb170944b610`
- standards tree: `002e9a81745412560a4c0300c6cbd5293f7a65d3`
- standards population: 52 members
- standards aggregate SHA-256:
  `01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b`
- extraction: `git archive` of the exact commit into
  `/tmp/stdo-final-vanilla-snapshot.WXa4xq/snapshot`
- snapshot state during review: read-only

All six supplied evidence hashes were reproduced before evaluation and again
after completion. T-022 content was admitted only for lines 1-64. The raw event
stream shows the Reviewer read only those lines from T-022.

## Isolation And Invocation

- invocation count: exactly one; no retry or resume
- thread: `01a05940-e718-7471-8c47-281eeaf1a5c8`
- CLI: `codex-cli 0.150.1`
- model: `gpt-5.6-sol`
- reasoning effort: `xhigh`
- working directory:
  `/tmp/stdo-final-vanilla-snapshot.WXa4xq/reviewer-empty`
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
CODEX_HOME=/tmp/stdo-final-vanilla-snapshot.WXa4xq/codex-home \
codex exec \
  --cd /tmp/stdo-final-vanilla-snapshot.WXa4xq/reviewer-empty \
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

- raw-event file creation: `2026-08-31T19:17:00Z`
- result and terminal-event finalization: `2026-08-31T19:28:10Z`
- observed artifact window: 670 seconds, at filesystem one-second resolution
- terminal event: one `turn.completed`
- completed command executions: 33, all exit code 0
- Codex stderr: empty
- model usage:
  - input tokens: 367,899
  - cached input tokens: 310,784
  - cache-write input tokens: 0
  - output tokens: 18,097
  - reasoning output tokens: 12,713

The Codex run completed and wrote both its final result and terminal event. The
outer zsh receipt wrapper then failed after completion on `status=$?` because
`status` is a reserved read-only zsh variable. The wrapper therefore exited 1
and did not retain the Codex subprocess exit integer. There was no rerun. The
successful terminal event, complete result file, 33 completed zero-exit command
events, and empty Codex stderr are the retained completion evidence.

## Artifacts

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `request.txt` | 6,802 | 133 | `203a0ede3a969d12edef94b0dddead951dbcb299ec99d03cca6cd9502fabd65e` |
| `raw-events.jsonl` | 376,853 | 73 | `987d38f65363e0cd31bdb389204a6c429a93c1d87472c47f9ef62d118f1c102a` |
| `result.txt` | 11,958 | 98 | `85cd9fcc169c30f905afc16df5347e5a91272c52214c29e6e939b8cf1838eb14` |
| `stderr.txt` | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## Invalidation

This review receipt is exact only for the named subject, six admitted byte
sequences, evidence scope, request, model/configuration, and single activation.
Any change to those coordinates requires a new activation; this run must not be
silently reused as review of later bytes.
