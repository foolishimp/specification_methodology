# Claude native pickup — release 2.5.0 run 003

Disposition: **PASS**. One fresh Claude Fable 5 invocation used the canonical
native `/stdo-representation` skill against Product-member checkpoint
`95f7bf2061189e27348695df14b8597c4bc9c0bd`. There was no rerun or repair.

## Invocation receipt

- Started: `2026-08-31T22:56:47+1000`
- Completed: `2026-08-31T23:02:57+1000`
- Exit status: `0`
- CLI: Claude Code `2.1.251`
- Model: `claude-fable-5`
- Effort: `high`
- Permission mode: `bypassPermissions`
- Session: `64dfe155-ee70-4282-b6f7-39f83a4e41f3`
- Terminal result: `success`
- Duration: `369277 ms`; 34 turns; no permission denials; no subagents
- Candidate repository tree: `45be515ab8a6989b0366a4c4d4cd3e9d8cf4bfdc`
- Candidate subtree tree: `7a8c7d643434d95a948cc7f26271c1ad3a1409b5`

Exact invocation:

```sh
claude --print --model claude-fable-5 --effort high \
  --output-format stream-json --verbose \
  --dangerously-skip-permissions --no-session-persistence \
  < dogfood/native-pickup/release-2.5.0/claude-run-003/request.md \
  > dogfood/native-pickup/release-2.5.0/claude-run-003/events.jsonl
```

Standard error was empty and was not retained. The native slash expansion
preserved the exact literal `cut -d ' ' -f 1` before any on-disk skill read.

## Qualification result

- Skill file SHA-256:
  `905313e0784ed15c717d04e432385f68e399e7155a59c31809475d291f4e28c6`.
- Claude reference SHA-256:
  `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164`.
- Product inventory SHA-256:
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`.
- Program file / canonical SHA-256:
  `5e6b6250492f4322f52248f4d889310ae29ff4dfa5578e0126b0a9e8d7ff6d63` /
  `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`.
- Index file / intrinsic SHA-256:
  `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd` /
  `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`.
- Project frame basis / decision SHA-256:
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539` /
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`.

The model opened the Logical Constraint Map before the Axiomatic Program and
Source STDO, then verified the map's exact program URI and canonical digest
binding. It selected exactly one actual top-level `frame_refs` member:

`stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`

The frame URI was also its source route. The separately labeled supporting
clause was
`urn:stdo-representation:a-c-text:clause:product-definition-schema-closes-routing-shape`,
routed through `source_routes` to the Product Definition schema. No symbol,
clause, residual, digest, decision, Product Definition, Install, or Release Cut
was called a frame.

Bounded source re-entry used the digest-verified installed STDO
`v2.5.0-rc.1`: the Derived Reviewer Frame, Release Method publication and
acceptance passages, Identity Method core law, Product Definition schema, and
installed-release manifest schema. The result correctly kept the continuing
mutable Product-Definition identity, immutable Release Cut, verified Install,
publication, and Product-owner acceptance distinct. It rejected the supplied
conflation and returned the review closed to Executive without repair or
promotion.

From the child root, the model root-forced the immutable Axiom Indexer archive
and verified tag object `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled
commit `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
`8c9ad5f5e99a60c18fb8c1802471753afb226272`, seven-member inventory
`7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
and `ac.py` SHA-256
`dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
The mutable `../axiom_indexer` sibling was neither read nor used.

The trace discloses one boundary observation: while locating the installed
STDO store, Claude inspected mutable `specification_methodology` toolchain
path-resolution source. Those bytes supplied only the store location; they did
not supply STDO meaning, dependency mechanics, joining, or identity. The
operative Source STDO basis was the exact installed release verified by its
manifest digest. This is not mutable-sibling substitution, and the observation
is retained rather than hidden.

`sections.json` contains the six Claude-layout labels. The extracted immutable
`ac.py` produced `joined-request.txt`; independent receipt validation confirmed
exact `label + newline + text` rows separated by one blank line with no
terminal newline. The raw trace contains one `Write`, targeting only
`sections.json`; the only other model-created repository output was
`joined-request.txt` through the immutable joiner. No prior dogfood result or
review was opened, no candidate member was edited, and a concurrently created
`codex-run-003/` directory was not read.

## Evidence hashes

| File | SHA-256 |
|---|---|
| `request.md` | `cb8d9effff7c4e2bdef0cc87786e73b49f9b978c1dfe5c4a0847ec40c21e60ac` |
| `events.jsonl` | `f6a7ec920fff4f5e9aff576b361f48794432b5a0c7b80ffa9da3e75f990acb0b` |
| `result.md` | `4391927b2fd8e2dc9cbb31ce991f7c2c3d266d5064d14544b080e8e976921f6e` |
| `sections.json` | `e97f5661d9b2d35daa5fc081bf06b1b28ba23cffc6e23d6dc9bca13baacf0b31` |
| `joined-request.txt` | `bffa355be559bfdf70638e8632445c131bf2fa5a610bb7a544bf2ae1cb93a86f` |

`result.md` is the sole terminal result from `events.jsonl` plus one terminal
newline.
