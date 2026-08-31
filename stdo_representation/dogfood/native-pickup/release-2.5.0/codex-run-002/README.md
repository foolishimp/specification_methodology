# Codex native pickup — corrected Representation 2.5.0 candidate

Disposition: `PASS`. One Codex invocation evaluated frozen candidate
`2849d52fa5fe299d11b96ce28a4e322f23f3cfd9`; no repair or rerun occurred.
This is candidate qualification evidence, not publication or Product
acceptance.

## Invocation

- Codex CLI: `0.150.1`;
- model: `gpt-5.6-sol`;
- reasoning effort: `high`;
- requested sandbox: `workspace-write`;
- actor-reported effective sandbox: unrestricted filesystem, network enabled,
  approvals `never`;
- thread: `01a057ab-958c-78a1-99ab-629c7f838623`;
- start: `2026-08-31T11:54:05Z`;
- completion: `2026-08-31T22:09:38+10:00`;
- exit: `0`;
- invocation count: one.

```sh
codex exec --ephemeral --sandbox workspace-write --model gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' \
  --json \
  --output-last-message \
    dogfood/native-pickup/release-2.5.0/codex-run-002/result.md \
  - < dogfood/native-pickup/release-2.5.0/codex-run-002/request.md \
  > dogfood/native-pickup/release-2.5.0/codex-run-002/events.jsonl
```

## Frozen subject

- repository tree: `3b440d9c014613643a200c7bb749557bd3859ef9`;
- Representation subtree: `3769846eb7313ad8a334f5cf694d27f974c34982`;
- Product inventory:
  `e5155655497ad3021b33fc90a3e105031d5b199be7c3245fd26a9da6a27eb45b`;
- skill: `ba7b83bce4a3a437ec78fcd6a1b5745d080bda23d93236d20067bfa14f1158d0`;
- Codex reference:
  `fa89365507d72e2a6bdccbb1d81d9ae573e85d69c4f4f7e0b32bff121fcef27a`;
- project frame basis:
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`;
- frame-basis decision:
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`.

## Observed result

The actor used the root-forced immutable Axiom acquisition and verified tag
object `e7afc8a…`, commit `dc3e009…`, tree `8c9ad5…`, seven-member inventory
`7df380d5…`, and `ac.py` `dfb4d7f1…`. It did not open or execute the mutable
Axiom sibling.

The actor opened the logical map before Source STDO, reproduced the
map-to-program binding, and selected exactly one actual top-level frame:

```text
stdo://releases/v2.5.0-rc.1/standards/
STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame
```

It kept the supporting release clause and semantic-acceptance residual
separate from the frame and correctly labeled the project frame-basis and
decision digests. Bounded source re-entry covered the Reviewer frame, Release
Method publication law, and AC-018 structural/semantic separation. The
immutable join reproduced the authored section bytes exactly. The resulting
Reviewer request was not executed and returned closed to Executive.

## Retained evidence

| File | Bytes | SHA-256 |
|---|---:|---|
| `request.md` | 5705 | `00c4c69e98b075bb0edcb9d2b9059bb3cbd081bd5700cdaba30397c0c96b88f6` |
| `events.jsonl` | 246803 | `d03799a3bf86012aa0ae9bdd4b0641c0696d09db4a49160544d184055d9d40fd` |
| `result.md` | 4932 | `1e6f614e55042b37f312d91edfb528d46451f64aed9aa6a37875bec15e1bd5b7` |
| `sections.json` | 7439 | `01801684f094d34758bd188c39eaa0b9774ff339a68068f7dbd6f568ab19639b` |
| `joined-request.txt` | 7188 | `97ff403ea6564e9b6139f499b39f4bd11d462a21ffb03ab807767aedaf75ef5e` |

`events.jsonl` is the raw event stream. `result.md` is the CLI-emitted final
message. The run changed no existing Product or source member.
