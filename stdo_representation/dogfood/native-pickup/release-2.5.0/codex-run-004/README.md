# Codex native pickup run 004

Disposition: `PASS`. This is one fresh, non-mutating Codex qualification of
checkpoint `95f7bf2061189e27348695df14b8597c4bc9c0bd`, not a repair or retry
of an earlier run. It qualifies map-first native request construction only; it
does not publish or accept STDO Representation 2.5.0.

## Invocation

- Codex CLI: `0.150.1`;
- model: `gpt-5.6-terra`;
- reasoning effort: `xhigh`;
- requested sandbox: `workspace-write`;
- session: `--ephemeral`;
- thread: `01a057f2-54b2-7df0-af64-eee2aa7aaf10`;
- invocation count: one;
- reruns or repairs: none;
- process exit: `0`.

```sh
codex exec --ephemeral --sandbox workspace-write --model gpt-5.6-terra \
  -c 'model_reasoning_effort="xhigh"' --json \
  --output-last-message dogfood/native-pickup/release-2.5.0/codex-run-004/result.md \
  - < dogfood/native-pickup/release-2.5.0/codex-run-004/request.md \
  > dogfood/native-pickup/release-2.5.0/codex-run-004/events.jsonl
```

The raw event stream has one started thread, one completed turn, and no
terminal error or failure. The model excluded `dogfood/**` and prior review or
commentary paths from its repository inspection. It neither opened nor used the
mutable Axiom Indexer sibling.

## Observed qualification

The native skill resolved through `.agents/skills/stdo-representation` to the
canonical `skills/stdo-representation/` surface. The model verified:

- skill SHA-256 `905313e0784ed15c717d04e432385f68e399e7155a59c31809475d291f4e28c6`;
- eight-member Product inventory SHA-256
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`;
- program file/canonical SHA-256
  `5e6b6250492f4322f52248f4d889310ae29ff4dfa5578e0126b0a9e8d7ff6d63` /
  `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`;
- index file/intrinsic SHA-256
  `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd` /
  `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`;
- frame-basis revision 13 / separate acceptance-decision SHA-256
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539` /
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`; and
- root-forced immutable Axiom Indexer tag object, commit, tree, inventory, and
  `ac.py` SHA-256 `e7afc8a42a7123aebe91cb7582cb037b1aae612d` /
  `dc3e00998da36dae6ac7b76b340431a85096c83c` /
  `8c9ad5f5e99a60c18fb8c1802471753afb226272` /
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6` /
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.

It started with the logical map, verified its exact program binding, selected
exactly one real top-level Reviewer frame, performed bounded installed-Source
STDO re-entry, and kept clauses and residuals distinct from that frame. It
authored the six lean Codex-layout sections and used only extracted immutable
`ac.py join` to write the joined request. The exact-byte check passed with no
terminal newline. The unexecuted Reviewer return is explicitly closed back to
Executive.

The observed boundary remains: validation and joining are mechanical;
publication requires the immutable RC process; Product-owner acceptance is a
separate judgment over that exact cut. No authority follows from the joined
request or its successful construction.

## Retained evidence

| File | SHA-256 |
|---|---|
| `request.md` | `770ec2da5158aeece6f87bf3e7436fe2d18f35b4e933246dbdd461981da3f88a` |
| `events.jsonl` | `232f37371ce8d108a7a8181e3d1e73531b3d73d26944ce1a4fcc99f00494af09` |
| `result.md` | `d0fb4a49a537d3b98bc05261ea1185edef3ff25d45be983e3f92dde4bcd3c059` |
| `sections.json` | `67c21a6f5b88b019462a6f81e218c624443cdd23e59d9f3215e2852ae4389122` |
| `joined-request.txt` | `123be210a03d6f0af78c87f75910252c75d6396554fc0d485305f973488cce36` |

No existing file or Product member was modified. This README is the sixth and
final retained evidence artifact for run 004.
