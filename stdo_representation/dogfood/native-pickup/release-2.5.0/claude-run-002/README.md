# Claude native pickup — release 2.5.0 run 002

Disposition: **PASS**. One fresh Claude Fable 5 invocation used the native
`/stdo-representation` skill against frozen candidate
`2849d52fa5fe299d11b96ce28a4e322f23f3cfd9`. There was no rerun or repair.

## Invocation receipt

- Started: `2026-08-31T21:54:45+1000`
- Completed: `2026-08-31T22:00:31+1000`
- Exit status: `0`
- CLI: Claude Code `2.1.251`
- Model: `claude-fable-5`
- Effort: `high`
- Permission mode: `bypassPermissions`
- Session: `31d3ba0c-05f3-498a-9f3c-e436f1410435`
- Terminal result: `success`, `completed`, `end_turn`
- Duration: `346024 ms`; 34 turns; no permission denials; no subagents
- Candidate repository tree: `3b440d9c014613643a200c7bb749557bd3859ef9`
- Candidate subtree tree: `3769846eb7313ad8a334f5cf694d27f974c34982`

Exact invocation:

```sh
claude --print --model claude-fable-5 --effort high \
  --output-format stream-json --verbose \
  --dangerously-skip-permissions --no-session-persistence \
  < dogfood/native-pickup/release-2.5.0/claude-run-002/request.md \
  > dogfood/native-pickup/release-2.5.0/claude-run-002/events.jsonl \
  2> dogfood/native-pickup/release-2.5.0/claude-run-002/stderr.log
```

The native slash expansion supplied the skill before any on-disk skill read and
preserved the corrected literal fragment `cut -d ' ' -f 1` exactly.

## Qualification result

- Skill: `ba7b83bce4a3a437ec78fcd6a1b5745d080bda23d93236d20067bfa14f1158d0`
- Claude reference: `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164`
- Product inventory: `e5155655497ad3021b33fc90a3e105031d5b199be7c3245fd26a9da6a27eb45b`
- Project frame basis: `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`
- Acceptance decision: `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`
- Axiom tag/commit/tree: `e7afc8a42a7123aebe91cb7582cb037b1aae612d` /
  `dc3e00998da36dae6ac7b76b340431a85096c83c` /
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`
- Axiom inventory: `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`
- Axiom `ac.py`: `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`

The model opened the constraint map before the program and Source STDO. It
verified the map's program URI and canonical digest, then selected exactly this
actual top-level `frame_refs` member:

`stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`

The same URI was used as the frame source route. The separately labeled
supporting residual was
`urn:stdo-representation:a-c-text:residual:semantic-acceptance-not-supplied`,
routed through `source_routes` to AC-018. No clause, residual, digest, or
decision was called a frame.

Bounded Source STDO re-entry opened only the installed manifest, the Derived
Reviewer Frame section, and AC-018/AC-019. Candidate reads were the release
record, map, program, overlay, and Claude layout; basis, decision, and Product
members were hash-only inputs. The immutable Axiom archive supplied its release
record, member hashes, and joiner. The mutable `../axiom_indexer` sibling was
not read or used.

`sections.json` contains the six ordered Claude-layout labels. The extracted
immutable `ac.py` produced `joined-request.txt`; independent receipt validation
confirmed exact `label + newline + text` rows separated by one blank line, with
no terminal newline. Mechanical validation, publication, and semantic
acceptance remained distinct. The bounded claim was rejected and returned
closed to the Executive.

The raw trace contains one `Write` call, targeting `sections.json`; the only
other repository output made by Claude was `joined-request.txt` through the
immutable joiner. Its temporary archive and inventory file were removed after
the run. No candidate byte was edited. A concurrently produced untracked
`codex-run-002/` directory was not read and is outside this receipt.

## Evidence hashes

| File | SHA-256 |
|---|---|
| `request.md` | `7e063d7106d9b9d393c6db95ac6af9ba71302ee2db9a092a8951c7c05887b3c3` |
| `events.jsonl` | `706761116c4343879652f6a2c51ba10740b04c11c72bd2b366d63b963fce1ab7` |
| `stderr.log` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `result.md` | `561caca6a1f96afe65f59b9ecb1e3364df3fec52d126894410656f4d1a2cfa6b` |
| `sections.json` | `6eca6271c3bbc9b94450281af6d1a73a1edf9c030cbd10fe7aa89a33a121426c` |
| `joined-request.txt` | `bb6d2789af0e0e9f16663beea038230b380b55f83326abad099ce92a078b27c4` |

`result.md` is the terminal result from `events.jsonl` plus one terminal
newline. `stderr.log` is empty.
