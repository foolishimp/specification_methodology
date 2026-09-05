# Vanilla RC2 Semantic-Slice Review Run 002

## Purpose

This is the vanilla comparison run for the STDO 2.5.0 RC2 self-review
experiment. It used no a_c index, no STDO Representation skill, no prior review
or dogfood result, and no repository or user prompt rules. The Reviewer received
only the six absolute evidence paths and constraints in `request.txt`.

## Invocation receipt

- invoked once: yes
- started: 2026-09-01T04:49:55+1000
- completed: 2026-09-01T04:59:08+1000
- exit status: 0
- model: `gpt-5.6-sol`
- reasoning effort: `xhigh`
- persistence: `--ephemeral`
- sandbox: `read-only`
- isolated cwd: `/tmp/stdo-vanilla-rc2-002.rUDmgL`
- Git repository check: skipped for the empty temporary cwd
- user config: ignored
- repository rules: ignored
- event format: JSONL
- thread id: `01a05928-1d1b-78b0-a793-d9cc7a10ba14`
- input tokens: 682271
- cached input tokens: 616192
- output tokens: 14578
- reasoning output tokens: 9544

Invocation shape:

```text
codex exec --model gpt-5.6-sol \
  --config 'model_reasoning_effort="xhigh"' \
  --ephemeral --ignore-user-config --ignore-rules \
  --sandbox read-only \
  --cd /tmp/stdo-vanilla-rc2-002.rUDmgL \
  --skip-git-repo-check --json \
  --output-last-message reviewer-result.md -
```

The wrapper recomputed the standards aggregate and verified all six file
digests immediately before starting Codex. The Reviewer independently verified
the same six digests as its first evidence command before semantic inspection.

## Frozen subject

- standards aggregate:
  `483542072037d644f4026c13ce744597a7433f7bb05ae8992f7a81afef4c7a89`
- `REFERENCE_FRAME_METHOD.md`:
  `c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8`
- `STDO_REFERENCE_FRAME_BASELINE.md`:
  `0f7257f8c2adf4341f1eb8075f822984a88cfcb9930e11440fa74defceea4f4c`
- `stdo_compressed.md`:
  `e40efa944f61fb6aac73d568046c8635df28666f4f36d5a4ffd3a22ed9891f4a`
- `PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md`:
  `33770a4f0b5d7ad61db09e3b1079633c110df44f69d595379cf10fa76e0d1b21`
- `test_reference_frame_boundaries.py`:
  `570d9e04b85f3a0115d3c9be378deb29a35fe2c7c96a5ee521244292c8802b89`
- active T-022:
  `023ed7f3b9f352354691cbc596987edf45c49ddd6cbc32f0c59a2806807f63fd`

## Result

- Reference Frame Method verdict: `satisfied`
- material findings: none
- technical triage: `not_applicable` for the selected no-finding branch
- focused proof: substantively establishes the claimed prose-standard relation
  for the admitted slice; it does not claim runtime or repository-wide proof

The Reviewer assigned no priority, boundary effect, disposition, release
status, repair direction, continuation, or subsequent activation.

## Concurrent source drift

The shared live tree changed after invocation and digest verification but before
the run completed. At 2026-09-01T04:54:12+1000, the admitted
`stdo_compressed.md` moved from the frozen digest above to
`47addcb1dab04b0de0a686355fe23fe7839d76c20ace17437bf1003f18142e81` as
source-digest metadata was regenerated. The live standards aggregate after the
run was
`01238f901426807b5350e1013c85b8e5f4ebe29cf89c62a858707dd705d6415b`.
The other five admitted file digests remained equal to the frozen subject.

The Reviewer trace records its exact pre-drift digest verification and its
inspection of the frozen compression relation. Nevertheless, the closed result
is evidence only for the frozen `483542...` subject. Its own invalidation clause
means it is not a current-tree verdict after the digest change. No retry was
made.

## Artifact digests

- `request.txt`:
  `0b40eafbdc53533c3219fc4b5f570a3f575a15aefceb9eba62fc843344f8321e`
- `events.jsonl`:
  `f9f903054dcb2d1bcf3997fc3459b19e73fafeb2d317e3b2c5745ef50073c859`
- `reviewer-result.md`:
  `8d6ccf3b5d5015e247fc9382792cd693e5f913ec5f16b0ff8dce83f3ff095ea6`

`events.jsonl` is the exact structured stdout trace. `reviewer-result.md` is the
exact final model response. Neither was edited after the invocation.
