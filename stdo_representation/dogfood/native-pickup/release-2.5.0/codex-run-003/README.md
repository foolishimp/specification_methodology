# Codex native pickup run 003

## Subject and invocation

- source checkpoint: `95f7bf2061189e27348695df14b8597c4bc9c0bd`;
- requested model: `gpt-5.6-sol`;
- reasoning effort: `high`;
- Codex CLI: `0.150.1`;
- thread: `01a057e3-662a-7ff1-88cc-c6be89d86f07`;
- invocation count: one;
- reruns or repairs: none;
- sandbox: `workspace-write`;
- session persistence: `--ephemeral`;
- process exit: `1`.

The exact invocation was:

```sh
codex exec --ephemeral --sandbox workspace-write \
  --model gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' \
  --json \
  --output-last-message \
  dogfood/native-pickup/release-2.5.0/codex-run-003/result.md \
  - < dogfood/native-pickup/release-2.5.0/codex-run-003/request.md
```

Standard output was captured verbatim in `events.jsonl`. Standard error was
empty. The CLI did not create the requested last-message file because the turn
failed before a final model message. `result.md` is therefore explicitly marked
as an orchestration projection of the raw terminal event.

## Verdict

`HOLD` for native Codex qualification.

The terminal event is:

```text
Selected model is at capacity. Please try a different model.
```

The same error appears as both an event-stream `error` and `turn.failed`. The
one-shot rule prohibits retrying this run.

## Completed observations before interruption

The raw events record successful exact checks for:

- checkpoint `95f7bf2061189e27348695df14b8597c4bc9c0bd`;
- canonical skill SHA-256
  `905313e0784ed15c717d04e432385f68e399e7155a59c31809475d291f4e28c6`;
- eight-member Product inventory SHA-256
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`;
- program file and canonical SHA-256 values
  `5e6b6250492f4322f52248f4d889310ae29ff4dfa5578e0126b0a9e8d7ff6d63`
  and
  `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`;
- index file and intrinsic SHA-256 values
  `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd`
  and
  `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`;
- accepted frame-basis revision 13 SHA-256
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`
  and acceptance-decision SHA-256
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`;
- immutable Axiom Indexer tag object
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
  `dc3e00998da36dae6ac7b76b340431a85096c83c`, repository tree
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`, seven-member inventory
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
  and joiner SHA-256
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`;
- map-to-program binding and candidate status boundary; and
- selection of exactly one real top-level frame:
  `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`.

The model used the root-forced archived Axiom release. Its commands excluded
`dogfood/**` and `.ai-workspace/comments/**`; no command read the mutable
`axiom_indexer/` sibling.

## Unclosed observations

The provider failure occurred before bounded Source STDO re-entry, an explicit
final statement of the Product-Definition/Release-Cut/Product/Install
distinctions, construction of `sections.json`, execution and byte verification
of the pure join, creation of `joined-request.txt`, or closed return to the
Executive. Those artifacts are intentionally absent rather than fabricated.

No existing repository file or Product member was modified by this run.

## Retained file identities

| File | SHA-256 |
|---|---|
| `request.md` | `151cca732565ff3fdc2462f8d87685135cb27f9be73b8f7ab76d9a8b89a592cd` |
| `events.jsonl` | `81ecf7ef6e5988e1191dd8d1aef15e42f894d9fb4e0d49a1e81c69410da68aa9` |
| `result.md` | `51c69645da59b92727c9e7923e9d1a3a91ead34bfc6e0f25b55baefa43fceeef` |
