# Direct-Source STDO comparison arm

## Evidence status

This directory retains one fresh direct-Source-STDO Worker observation for
comparison task `comparison-001`. It is invocation evidence only. It does not
compare or score the paired arm, repair the candidate, authorize publication,
or accept a Product.

## Exact artifacts

- `request.md`: 2,228 bytes; SHA-256
  `8e1bf4566abc0f12d6ba3fe0d5f6be7c91a72d8e400574da0bc3e06146357f4e`.
- `result.md`: 2,967 bytes; SHA-256
  `880f75d13a6417e30ed3ead94e6e7d53f340ad13b5c6ba85c4245aca13efd76a`.
- The final `agent_message` from the JSONL event stream is retained verbatim in
  `result.md`; no output repair or editorial qualification was added.

## Single invocation

- Working directory: `/Users/jim/src/apps/stdo_representation`
- CLI: `codex-cli 0.150.1`
- Requested model: `gpt-5.6-sol`
- Requested reasoning effort: `high`
- Role: Worker
- Session persistence: disabled with `--ephemeral`
- Requested sandbox: `read-only`
- Approval policy reported by the actor: `never`
- Effective sandbox reported by the actor: unrestricted
  `danger-full-access`; this differs from the requested sandbox
- Prompt transport: exact `request.md` bytes on standard input
- Event transport: JSONL on standard output
- Exit status: `0`
- Thread ID: `01a05340-08f7-75d3-a96c-99387e5c52a4`
- Usage reported by the CLI: 1,226,333 input tokens; 1,091,840 cached input
  tokens; 11,322 output tokens; 6,483 reasoning output tokens

The exact invocation was:

```sh
codex exec \
  -m gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' \
  --ephemeral \
  -s read-only \
  --json \
  -C /Users/jim/src/apps/stdo_representation \
  - < dogfood/native-pickup/comparison-001/direct-prose/request.md
```

The CLI attests the requested model/configuration in the local invocation; it
does not expose a provider-attested backing revision. All recorded commands
were non-mutating reads. The actor did not test sandbox enforcement by
attempting a write.

## Substantive source openings

The event trace recorded these raw Source STDO owners:

| Source | SHA-256 from the verified installed manifest | Use |
|---|---|---|
| `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md` | `f6a4e2be637df6c2dd5c69c6da7e77cefd8d8cde93af65ca686608ec43555e3f` | Worker authority, closed result, stop, and Worker-to-Executive return |
| `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md` | `90b5ea5e486c1c0e75883db5a15fba3f524cc5d5718c42108a548279e725d51f` | authority conservation and distinct authority relations |
| `stdo://releases/v2.5.0-rc.1/standards/SPEC_METHOD.md` | `4c4158b0b2a888277802237d467c7ea0b7e8e5993f5976f5b929e63a6ed0a85b` | project frame binding and `STDO-UP-020` delegation/disposition law |
| `stdo://releases/v2.5.0-rc.1/standards/RELEASE_METHOD.md` | `c690228adf680dc4ef0a391073a5d60e515fbd4b0150b778b6adb4723e3fa9a0` | publication phase and exact-cut human acceptance law |

The exact installed basis was resolved and verified through `stdo status`,
`stdo verify`, and `stdo resolve`:

- release: `stdo://releases/v2.5.0-rc.1/`;
- installed manifest SHA-256:
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`;
- standards member-set SHA-256:
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`;
- verification failures: none.

The event trace recorded these current project authority openings:

| Project source | SHA-256 | Use |
|---|---|---|
| `stdo_representation.json` | `a5bf9dab97d25984a1befed4bcab8dc71938cfdecc975294ba5865f3c0a192b1` | sole Product Definition, immutable STDO basis, and frame-basis binding |
| `specification/REFERENCE_FRAME_BASIS.md` | `09db079c16758db8765452bd05f6b5de3ce831974e80fb9ea59ef876fab50ed9` | revision-11 Worker and candidate-readiness authority boundary |
| `.ai-workspace/decisions/20260831T005313_frame_basis_rev11_acceptance.json` | `371d0d031fa518a7c5a92a97c658e5c1bc5765b13d1c30f0d7938671c054b89e` | exact Product-owner acceptance of frame basis revision 11 |
| `specification/PRODUCT.md` | `f0c47af3c167b977e0c0aec11a4a7388ccb29b24cf35204b80ccc341a879a6ff` | Product disposition and external-authority boundary |
| `specification/requirements/REQ-P-CANDIDATE-VALIDATION.md` | `485f2f381a4e6652e120f089203502de05ea88398e313c510364ab76185e51e0` | structural-validation limit |
| `specification/requirements/REQ-P-NATIVE-FRAME-USE.md` | `d7ff8d930c74698c329b3dff35a356fa3f746f25453e3a5bca5b5cb96ec96faa` | role labels grant no publication or acceptance authority |
| `.ai-workspace/tickets/active/T-004-publish-stdo-representation-0.1.0.md` | `9ec42992e70393f97b1b2dbfc21e664031be9b0120c186c8f606c6647f5371b8` | current publication/acceptance outcome and non-closure law |
| `releases/v0.1.0.md` | `7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876` | supplied exact candidate record and inventory law |

Directory-wide `rg` filename and coordinate searches also occurred. They were
discovery operations, not additional semantic authorities. The invocation did
not open the logical constraint map, Axiomatic Program, native skill, metadata,
target references, or paired-arm material as guidance. Candidate-member access
was limited to filesystem identity and SHA-256 computation.

The current release-publication grant under `.ai-workspace/decisions/` was not
opened by this invocation. This record preserves that source-opening boundary
as observed; it does not repair or reinterpret the returned result.

## Subject hash checks

The successful checks matched the supplied coordinates:

| Subject | Observed SHA-256 |
|---|---|
| `skills/stdo-representation/SKILL.md` | `f540971bc895890c182ef5ddbe0478621c418aea430ac7f45a8c3665a45c133c` |
| `skills/stdo-representation/agents/openai.yaml` | `1a29d7794af568b13c4bce7c68ea7a24e352555cb9d2bccfb4a8221267477f00` |
| `releases/v0.1.0.md` | `7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876` |
| `specification/REFERENCE_FRAME_BASIS.md` | `09db079c16758db8765452bd05f6b5de3ce831974e80fb9ea59ef876fab50ed9` |
| canonical eight-member inventory | `316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091` |

The inventory check succeeded on its third read-only construction. The first
attempt shadowed the shell `PATH` variable and could not invoke its hashing
tools; the second included a newline in each symlink-target preimage and
therefore produced non-authoritative digest
`b65243f6f282eeecb0439bec80b28f92696269bbadbd05751f68ab99e8fad6f6`.
The final check used the required symlink target string without a terminal
newline and matched `316121da…091`.
