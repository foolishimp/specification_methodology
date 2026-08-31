# Candidate Review — STDO Representation 2.5.0

- reviewed_at: `2026-08-31T22:36:39+10:00`
- reviewer: Codex, bounded read-only candidate evaluator
- disposition: `HOLD`
- severity: `P0=0`, `P1=1`, `P2=0`
- publication_authority: none

## Exact subject

This review binds the prepublication candidate at:

- commit: `f9ebf7a1321d206259768b84b4266f0c1199e4ec`;
- repository tree: `447725493cdaaa7a715126729d8c6f4d5979a1a6`;
- `stdo_representation/` subtree: `d8aa5a4c8d30a5005e3ed6211192f64284ca1dfa`;
- release record `releases/v2.5.0.md`: SHA-256
  `5b26158456b535dc1b5c4d67edb011b4165624f926935a023d622478801d38fe`;
- Product Definition Overlay `stdo_representation.json`: SHA-256
  `5e2a9302edcd827278c62393fff4a4fa7bc43d8fffee8bff91c97566dd5cf969`;
- live Product Definition `specification/PRODUCT.md`: SHA-256
  `76c21d20d54d711cd575d2e7f7b4181077c9a793a80a1c811f7d5a8c24426bc7`.

The corrected native runs evaluated the unchanged Product-member bytes at
commit `2849d52fa5fe299d11b96ce28a4e322f23f3cfd9`, repository tree
`3b440d9c014613643a200c7bb749557bd3859ef9`, and Representation subtree
`3769846eb7313ad8a334f5cf694d27f974c34982`. Later commits add or normalize
evidence and release-facing bytes; they do not change the eight Product
members.

This commentary is not part of the reviewed Product or release subject.

## Finding

### P1 — The canonical semantic compression collapses identities that installed STDO requires to remain distinct

The frozen Axiomatic Program contains two material counterexamples:

1. Clause
   `urn:stdo-representation:a-c-text:clause:product-definition-schema-closes-routing-shape`
   states that a Product Definition binds "one Product identity." Exact
   installed `SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence`
   instead defines `product.definition_id` as **Product-Definition Identity**,
   the stable identity of a mutable `WHAT` definition line, and explicitly
   distinguishes it from every immutable released Product and release identity.
2. Symbol
   `urn:stdo-representation:a-c-text:symbol:installed-release` is labeled
   "Immutable installed release" and is used as the subject of clause
   `urn:stdo-representation:a-c-text:clause:release-rc-is-immutable`.
   Installed `SPEC_METHOD.md#recursive-product-taxonomy` and
   `RELEASE_METHOD.md#release-identities` distinguish an immutable RC Release
   Cut, an accepted Product, and an Install. The compression maps the RC-cut
   law through an Install-shaped symbol instead.

These are not missing routes or mechanical-map defects. They are semantic
identity defects in Product member
`build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/axiomatic-program.json`
(file SHA-256
`a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783`,
canonical SHA-256
`e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`).
The deterministic index reproduces them unchanged; structural success cannot
repair their meaning. None of the five declared residuals identifies either
collapse.

The counterexamples falsify `F-MAP-ESSENCE` and
`REQ-P-MAP-002` for the claimed canonical `a_c.STDO` semantic compression.
Release claim `STDO-REP-2.5-C02` is therefore not qualified, so the mandatory
candidate-readiness conjunction cannot return `satisfied` on this frozen
inventory.

## Claim disposition

| Claim | Result | Basis |
|---|---|---|
| `STDO-REP-2.5-C01` | `satisfied` | Representation and represented STDO semantic versions are both `2.5.0`, while Source STDO, Representation, Axiom Indexer, RC, member, and ref identities remain distinct in the live WHAT and release record. |
| `STDO-REP-2.5-C02` | `falsified` | The frozen compression has the Product-Definition/Product and Release-Cut/Install counterexamples above. |
| `STDO-REP-2.5-C03` | `satisfied` at its mechanical boundary | Exact Axiom Indexer reproduced the map byte-for-byte and the map binds the unchanged program URI and canonical digest with total routes over its own items. |
| `STDO-REP-2.5-C04` | `satisfied` | The explicit composition target resolves to `urn:stdo:product-definition:axiom-indexer`; exact immutable Axiom objects, inventory, and `ac.py` were independently verified without substituting mutable sibling source. |
| `STDO-REP-2.5-C05` | `satisfied` only for the observed native tasks | Corrected Codex and Claude run-002 evidence shows canonical-skill discovery, one visible top-level frame, bounded Source STDO re-entry, exact immutable joining, and closed return. It does not cure C02 or generalize beyond the observed tasks. |

## Product, frame, overlay, and dependency identities

The eight-member inventory independently reproduced as SHA-256
`e5155655497ad3021b33fc90a3e105031d5b199be7c3245fd26a9da6a27eb45b`:

| Type | Member | SHA-256 |
|---|---|---|
| symlink | `.agents/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| symlink | `.claude/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/axiomatic-program.json` | `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` | `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95` |
| file | `skills/stdo-representation/SKILL.md` | `ba7b83bce4a3a437ec78fcd6a1b5745d080bda23d93236d20067bfa14f1158d0` |
| file | `skills/stdo-representation/agents/openai.yaml` | `31367869c7bf984c4b50c4fe36d32d1ef6f47a2d2b96adb87fbd6c2082381228` |
| file | `skills/stdo-representation/references/claude.md` | `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164` |
| file | `skills/stdo-representation/references/codex.md` | `fa89365507d72e2a6bdccbb1d81d9ae573e85d69c4f4f7e0b32bff121fcef27a` |

Additional bindings:

- logical-map intrinsic SHA-256:
  `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`;
- accepted frame-basis bytes:
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`;
- separate Product-owner frame decision:
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`;
- exact Source STDO installed manifest:
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`;
- Source STDO standards member set:
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`;
- exact Axiom Indexer tag object / peeled commit / tree:
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d` /
  `dc3e00998da36dae6ac7b76b340431a85096c83c` /
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`;
- Axiom Product inventory:
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`;
- exact `ac.py`:
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.

The overlay's composition edge resolves to target definition
`urn:stdo:product-definition:axiom-indexer` at current definition-file SHA-256
`e7bf72bb1c4199867d44e5a43cf352a1226015e22ce080f46bb9211c6bdf0073`
and cites the exact immutable contracts. Its Shared-Source Release Profile is a
Product-local axiom specializing only the installed Release Method's explicit
alternate-spelling permission. No mutable `specification_methodology` source
term is treated as released consumer law. The source-subtree tree is additional
reacquisition evidence, not Product identity.

## Native evidence

- Codex run-002 receipt / raw events / normalized result:
  `5d9eebb16f5cb2aa7f736190719dc2dc41581cd3ca79838ae2d149d96f26b824` /
  `d03799a3bf86012aa0ae9bdd4b0641c0696d09db4a49160544d184055d9d40fd` /
  `6989605681ceccbee080451eab6c6697922f25ff931ae7759ef5962c6cf009c5`;
- Codex sections / joined request:
  `01801684f094d34758bd188c39eaa0b9774ff339a68068f7dbd6f568ab19639b` /
  `97ff403ea6564e9b6139f499b39f4bd11d462a21ffb03ab807767aedaf75ef5e`;
- Claude run-002 receipt / raw events / result:
  `7179cf36a3bad0db19213c5b56b2f742cb6e416ddfa5aa76647d0bbef9d9044b` /
  `706761116c4343879652f6a2c51ba10740b04c11c72bd2b366d63b963fce1ab7` /
  `561caca6a1f96afe65f59b9ecb1e3364df3fec52d126894410656f4d1a2cfa6b`;
- Claude sections / joined request:
  `6eca6271c3bbc9b94450281af6d1a73a1edf9c030cbd10fe7aa89a33a121426c` /
  `bb6d2789af0e0e9f16663beea038230b380b55f83326abad099ce92a078b27c4`.

The Codex readable projection equals the raw final message after only removal
of trailing Markdown line-break spaces and addition of the retained terminal
newline. The Claude result equals the raw terminal result plus one terminal
newline. Both joined requests reproduce the exact released join law and have no
terminal newline.

## Predecessor and namespace

The declared predecessor remains exact and reachable:

- release record SHA-256:
  `7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876`;
- legacy annotated RC tag / peeled commit / repository tree:
  `46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f` /
  `b127ee9a0362f85d4875ae59664ecfcd13028d9c` /
  `15f9beb360836386ce9607dd31e30d0c8b5cd830`;
- predecessor Product inventory:
  `316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`.

At review time, local and `origin` observations were empty for the planned
Representation namespace:

- `refs/heads/rc/stdo_representation/2.5.0`;
- `refs/tags/stdo_representation/v2.5.0-rc.*`;
- `refs/tags/stdo_representation/v2.5.0`; and
- `refs/heads/release/stdo_representation/2.5.0`.

That confirms prepublication state; it grants no publication authority.

## Checks

- `stdo verify v2.5.0-rc.1`: valid, no failures.
- `stdo status --definition stdo_representation.json --verify`: valid, exact
  installed basis and schema.
- `python3 -B scripts/check_constitution.py`: valid, no mechanical failures.
- `python3 -B -m unittest scripts.test_check_constitution -v`: 16/16 passed.
- exact Axiom Indexer `test_ac.py`: 15/15 passed.
- exact Axiom validation report SHA-256:
  `66ffd50f30801fd6b9c0b29e94839dadf09f9ae8f901239e81c224733b2aed4f`.
- emitted map SHA-256:
  `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`;
  byte-identical to the frozen Product map.
- Product inventory, symlink modes and target strings, JSON parsing, Git object
  identities, `git diff --check`, and `git fsck --strict`: passed.

These checks prove their structural, identity, and deterministic boundaries.
They do not decide the P1 semantic counterexamples.

## Closed return

Frame result: `falsified` for `F-MAP-ESSENCE`; candidate readiness is `HOLD`.

No Product member, release record, authority surface, ref, tag, branch, commit,
or remote state was changed. This review does not authorize publication,
Product acceptance, repair, or continuation.
