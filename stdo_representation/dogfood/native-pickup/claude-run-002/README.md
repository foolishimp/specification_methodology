# Claude Fable 5 Native Pickup Run 002

## Evidence status

This directory retains one fresh Claude native-skill observation over the
repaired STDO Representation skill. Claude acted as a read-only Worker and
answered whether structural validity permits that Worker to publish or accept a
candidate.

The returned verdict is `No`. Publication and acceptance remain on visible
hold pending the separately authorized release relation and Executive or
Product-owner disposition. The Worker closed its activation by returning to the
Executive. No Product or candidate was accepted.

This is invocation evidence, not semantic acceptance, candidate readiness,
publication authority, Product disposition, exact-cut qualification, or an RC
verdict.

## Invocation

- Working directory: `/Users/jim/src/apps/stdo_representation`
- CLI path: `/Users/jim/.local/bin/claude`
- Claude Code version: `2.1.251 (Claude Code)`
- Requested model alias: `fable`
- Requested model family: Claude Fable 5
- Effort: `low`
- Session persistence: disabled with `--no-session-persistence`
- Permission mode: `plan`
- `--allowedTools` value: `Read`
- Prompt transport: exact `request.md` bytes on standard input
- Successful model invocations: `1`
- Exit status: `0`
- Output capture: standard output retained verbatim as `result.md`

The invocation used:

```sh
claude -p \
  --model fable \
  --effort low \
  --no-session-persistence \
  --permission-mode plan \
  --allowedTools Read < dogfood/native-pickup/claude-run-002/request.md
```

The CLI did not provider-attest a resolved backing model revision, so this
record does not infer one. The result self-reports read-only `shasum` and
`git rev-parse` operations. Plain Markdown output does not retain a tool-call
trace; the statement remains part of Claude's verbatim report. Codex
independently recomputed the file and Git identities recorded below after the
invocation.

## Freshness and effect boundary

- The prompt began with `/stdo-representation`.
- The canonical skill was discovered through the repository-native Claude
  symlink.
- Prior dogfood results and expected answers were expressly outside the
  evidence boundary.
- Claude was instructed to apply the repaired exact-input gate before semantic
  map use and to hold rather than guess on unresolved identity.
- The requested subject was hypothetical; no actual repository candidate was
  evaluated.
- Claude reported no edit or external action. The only retained writes are the
  three files in this directory, written by Codex after the invocation.

## Repaired native input identity

| File | Bytes | SHA-256 |
|---|---:|---|
| `skills/stdo-representation/SKILL.md` | 3,316 | `f540971bc895890c182ef5ddbe0478621c418aea430ac7f45a8c3665a45c133c` |
| `skills/stdo-representation/agents/openai.yaml` | 229 | `1a29d7794af568b13c4bce7c68ea7a24e352555cb9d2bccfb4a8221267477f00` |
| `skills/stdo-representation/references/claude.md` | 1,004 | `85ea8f51d91ddec1eafc219b0e143cdc27fd680a63dd568ab10dc29aac4dafb7` |
| `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` | 84,143 | `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95` |

The map declares intrinsic SHA-256
`2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`.
Claude correctly distinguished reading that field from recomputing the
intrinsic canonicalization algorithm.

Exact Axiom Indexer `v0.1.0-rc.1` identities independently observed after the
run:

- annotated tag object: `e7afc8a42a7123aebe91cb7582cb037b1aae612d`;
- peeled commit: `dc3e00998da36dae6ac7b76b340431a85096c83c`;
- tree: `8c9ad5f5e99a60c18fb8c1802471753afb226272`;
- `ac.py` SHA-256:
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`;
- declared member-inventory SHA-256:
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`.

The result retains the member-inventory aggregate as Executive-supplied rather
than falsely claiming it was recomputed. It likewise retains the canonical
edition status of the repaired files as Executive-supplied.

## Map-first selection and role result

Claude reported that semantic selection began from the logical map. Its
smallest selected set covered:

- the derived Worker frame for the bounded construction and return envelope;
- engagement return topology for mandatory return to Executive;
- reference-frame boundedness and authority conservation; and
- immutable-RC publication as a separately owned release relation.

The result visibly supplies purposes and routed Source STDO coordinates. It
also abbreviates the URI column for the Worker frame and several clause/source
rows with an ellipsis or short clause name. The full Worker frame source route
is present, but the abbreviated display is retained as a native-output
precision residual rather than silently repaired in `result.md`.

## Source STDO openings

Claude reported two exact Source STDO file openings, within the request limit
of three:

| Logical source and anchors | Physical installed file | Why re-entered | Bytes | SHA-256 |
|---|---|---|---:|---|
| `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md` — `#derived-worker-frame`, `#complete-engagement-transition` | `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md` | Resolve Worker authority, exclusions, `candidate_ready` versus acceptance, and return topology. | 91,963 | `f6a4e2be637df6c2dd5c69c6da7e77cefd8d8cde93af65ca686608ec43555e3f` |
| `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md` — `#reference-frame-laws` | `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md` | Resolve bounded-frame law and authority conservation against actual installed content. | 46,222 | `90b5ea5e486c1c0e75883db5a15fba3f524cc5d5718c42108a548279e725d51f` |

The routed `REFERENCE_FRAME_METHOD.md#reference-frame-laws` coordinate was not
falsely rejected. Claude found the actual `## Reference Frame Laws` heading at
line 313 and explicitly returned `Not missing, not drifted`.

`RELEASE_METHOD.md#immutable-rc-publication` was not opened. The result makes
full source re-entry there conditional on an Executive need for the exact
publication text.

## Hold, return, and residuals

- Publication and acceptance are visibly held, not implicitly continued.
- Structural validity remains evidence, not semantic truth or action authority.
- The Worker claims no promotion, publication, acceptance, Reviewer
  independence, continuation choice, or external action.
- Disposition returns to the Executive or Product owner with existing
  authority.
- The member-inventory aggregate and canonical-edition status remain supplied
  evidence; the map intrinsic digest is field-matched rather than recomputed.
- No Product acceptance occurred.

## Retained run files

| File | Meaning | Bytes | SHA-256 |
|---|---|---:|---|
| `request.md` | Exact prompt bytes supplied on standard input | 3,068 | `327d981bd903d1726bb855b0c00742a39d7a6fff52258aa5c1f0a0b1ca04a480` |
| `result.md` | Verbatim successful standard output | 5,054 | `4d5d54845ae0d77ea79d2d84478ccbd7b43ce70bb33c12624a5adc4cccb2e06d` |

`README.md` cannot embed its own final digest without changing that digest. Its
final SHA-256 is reported in the delivery handoff after validation.
