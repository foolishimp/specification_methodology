# Map-first comparison arm 001

This directory freezes one fresh map-first Worker arm. It records no cross-arm
comparison verdict, Product disposition, repair, publication, or acceptance.

## Exact subject

- Shared task and full prompt: `request.md`
- Prompt SHA-256: `362c65f2e83e1eeb7a5b42b79347e48d1a0d92234ec8eb30d8ff87b0df444537`
- Prompt size: 322 bytes
- Canonical skill SHA-256: `f540971bc895890c182ef5ddbe0478621c418aea430ac7f45a8c3665a45c133c`
- OpenAI metadata SHA-256: `1a29d7794af568b13c4bce7c68ea7a24e352555cb9d2bccfb4a8221267477f00`
- Rebuilt eight-member Product inventory SHA-256: `316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`
- Release record SHA-256: `7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876`
- Logical-map file SHA-256: `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`
- Logical-map intrinsic SHA-256: `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`
- Accepted frame: `urn:stdo-representation:reference-frame-basis:source-project:11`
- Frame-basis SHA-256: `09db079c16758db8765452bd05f6b5de3ce831974e80fb9ea59ef876fab50ed9`
- Acceptance-decision SHA-256: `371d0d031fa518a7c5a92a97c658e5c1bc5765b13d1c30f0d7938671c054b89e`
- Bound-overlay SHA-256: `a5bf9dab97d25984a1befed4bcab8dc71938cfdecc975294ba5865f3c0a192b1`

## Invocation

Exactly one invocation ran and exited 0:

```sh
codex exec --ephemeral --sandbox read-only --model gpt-5.6-sol \
  -c "model_reasoning_effort='high'" \
  --output-last-message dogfood/native-pickup/comparison-001/map-first/result.md \
  - < dogfood/native-pickup/comparison-001/map-first/request.md
```

Observed CLI header:

- Codex: `0.150.1`
- provider: `openai`
- model: `gpt-5.6-sol`
- reasoning effort: `high`
- reasoning summaries: `none`
- approval: `never`
- session: `01a05340-1c06-73f0-aff0-2d0ac4ffee9b`
- requested sandbox: `read-only`
- observed effective sandbox: `danger-full-access`

The observed sandbox did not match the requested sandbox. The Worker issued
read-only inspections; the invocation wrapper alone retained `result.md`.
This records the CLI-reported configuration, not a provider attestation.

## Result

- Output: `result.md`
- Output SHA-256: `91f49da14e343f423a79ea20157bdc7026e322039f21602dc39d94a165e7d9af`
- Output size: 3,534 bytes
- Output lines: 31
- Worker verdict: `No`
- Selected frame: `stdo://releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame`

This is the map-first arm result only. It is not the required independent
comparison verdict.

## Source openings

The invocation opened these material content surfaces:

- `skills/stdo-representation/SKILL.md` — native map-first and role procedure.
- `skills/stdo-representation/references/codex.md` — Codex presentation rules.
- `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` — first semantic constraint surface.
- `stdo_representation.json` and `AGENTS.md` — unique Product Definition, exact STDO basis, frame binding, and bootstrap.
- `specification/REFERENCE_FRAME_BASIS.md` — project publication and acceptance boundary.
- `specification/requirements/REQ-P-NATIVE-FRAME-USE.md` — native role and authority constraints.
- `.ai-workspace/decisions/20260831T005313_frame_basis_rev11_acceptance.json` — accepted revision-11 frame evidence.
- `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/manifest.json` — exact installed 51-member basis verification.
- `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/authority_compressions/stdo_bootstrap.md` — exact-basis routing.
- `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/STDO_REFERENCE_FRAME_BASELINE.md` — Worker authority, stop, and Executive-return law.
- `/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.1/standards/AXIOMATIC_CALCULUS.md` — structural/semantic separation.
- `/Users/jim/src/apps/axiom_indexer/releases/v0.1.0.md` and `/Users/jim/src/apps/axiom_indexer/README.md` at exact tag coordinates — Axiom Product identity verification.
- Repository `README.md` and `build_tenants/axiom_indexer/README.md` — local dependency routing.

One non-material web-tool event targeted `https://example.com`; it supplied no
evidence and was not cited in the result. No prior comparison-arm result was
opened or used.
