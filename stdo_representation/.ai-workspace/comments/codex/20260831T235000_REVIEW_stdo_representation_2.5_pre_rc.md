# STDO Representation 2.5.0 Pre-RC Readiness Review

- reviewed_at: `2026-08-31T23:50:00+10:00`
- reviewer: Codex, independent bounded pre-publication evaluator
- verdict: `GO`
- severity: `P0=0`, `P1=0`, `P2=0`
- publication_authority: none

## Exact subject

This review binds the clean pre-publication candidate at:

- commit: `fb0c696b3cca9cf66a58d301d37b73ef9ec4862e`;
- repository tree: `1430f70652a58d8f1b5cfb48561e5571902eaef5`;
- `stdo_representation/` subtree: `b69d725726b9d44de63ab55ec436719b13eae6c6`;
- release record `releases/v2.5.0.md` SHA-256:
  `079f1af9f05031524ec3fe003b7bf8cfea6238eacc8ac36dae0802cc3bd03557`;
- Product Definition Overlay `stdo_representation.json` SHA-256:
  `5e2a9302edcd827278c62393fff4a4fa7bc43d8fffee8bff91c97566dd5cf969`;
- eight-member Product inventory SHA-256:
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`.

This commentary is outside the reviewed Product and release subject.

## Prior blocker closure

The prior sole P1 is closed. Exact installed STDO `v2.5.0-rc.1`
`RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015`, SHA-256
`c690228adf680dc4ef0a391073a5d60e515fbd4b0150b778b6adb4723e3fa9a0`,
admits `conserved`, `superseded`, `intentionally removed`, and bounded
`not applicable` as predecessor-claim dispositions.

The repaired release record now gives exactly one admitted disposition to every
accepted predecessor claim:

- `STDO-REP-0.1-C01`: `superseded` by current C02 and C03. Those claims replace
  the predecessor's combined authoring-program/map relation with the explicit
  canonical-compression/deterministic-index relation without dropping either
  side of the behavior;
- `STDO-REP-0.1-C02`: `conserved` by current C03 and the unchanged residual,
  total source-route, and structural-only validation boundary;
- `STDO-REP-0.1-C03`: `conserved` by the same canonical skill and repository
  native Codex/Claude discovery relation;
- `STDO-REP-0.1-C04`: `conserved` by LLM-owned selection, labels, text and
  ordering, immutable Axiom joining, and the zero-local-engine boundary; and
- `STDO-REP-0.1-C05`: `conserved` by the current exact Codex run 004 and Claude
  run 003 native evidence.

The predecessor subject remains immutable and reacquirable: annotated tag
object `46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`, peeled commit
`b127ee9a0362f85d4875ae59664ecfcd13028d9c`, tree
`15f9beb360836386ce9607dd31e30d0c8b5cd830`, eight-member inventory
`316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`,
and release-record SHA-256
`7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876`.
Its Product-owner acceptance record binds the same objects, inventory, release
record, exact-cut review, and accepted C01-C05. No predecessor object, claim, or
acceptance is retargeted.

## Product and release subject

The declared inventory was independently recomputed from exact file bytes and
the two symlink target strings, in canonical path order:

| Type | Member | SHA-256 |
|---|---|---|
| symlink | `.agents/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| symlink | `.claude/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/axiomatic-program.json` | `5e6b6250492f4322f52248f4d889310ae29ff4dfa5578e0126b0a9e8d7ff6d63` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` | `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd` |
| file | `skills/stdo-representation/SKILL.md` | `905313e0784ed15c717d04e432385f68e399e7155a59c31809475d291f4e28c6` |
| file | `skills/stdo-representation/agents/openai.yaml` | `31367869c7bf984c4b50c4fe36d32d1ef6f47a2d2b96adb87fbd6c2082381228` |
| file | `skills/stdo-representation/references/claude.md` | `d104e9d3d6c7bf8c6cc86cd72cec25e6126012dfab648aaf7a58e1a94e2eb164` |
| file | `skills/stdo-representation/references/codex.md` | `fa89365507d72e2a6bdccbb1d81d9ae573e85d69c4f4f7e0b32bff121fcef27a` |

The aggregate reproduced
`08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`.
Git modes are `120000` for the two symlinks and `100644` for the six files.
There are no additional entries in either selected Product directory. All eight
Product members are byte-identical to the checkpoint qualified by the current
native runs; the later commits changed only evidence, release-facing, checker,
and test bytes outside the Product.

The release record accurately keeps the subject a frozen-member candidate,
names the Product-local shared-source ref profile, records the exact inventory,
dependencies, C01-C05, evidence and exclusions, and does not claim publication
or acceptance.

## Closed claim results

- `STDO-REP-2.5-C01` — `satisfied`: Representation semantic version `2.5.0`
  equals the represented STDO semantic version while the Source STDO Product,
  Representation Product, Axiom Indexer Product, RC ordinals, members, refs and
  acceptance identities remain distinct.
- `STDO-REP-2.5-C02` — `satisfied`: the Product carries one canonical
  source-linked `a_c.STDO` compression for exact installed STDO
  `v2.5.0-rc.1`.
- `STDO-REP-2.5-C03` — `satisfied`: the index binds the unchanged program URI
  and canonical SHA-256, retains 15 symbols, 51 clauses and five residuals, and
  exposes total source re-entry. Reproduction was byte-identical.
- `STDO-REP-2.5-C04` — `satisfied`: the explicit composition relation resolves
  `urn:stdo:product-definition:axiom-indexer` and binds immutable Axiom Indexer
  `v0.1.0-rc.1`; no mutable sibling supplied mechanics or authority.
- `STDO-REP-2.5-C05` — `satisfied`: the canonical skill and target references
  direct both native agents to map-first use, visible frame selection, bounded
  source re-entry, exact joining and closed return without promoting the map to
  truth or authority; the current Codex and Claude observations demonstrate it.

The repaired identity semantics are congruent with installed Source STDO: the
program separately represents a continuing mutable Product-Definition identity,
an immutable annotated Release Cut, and a manifest-identified Install, and
explicitly refuses to treat Product Definition as immutable Product identity.
Product acceptance remains a separate human verdict over the immutable cut.

## Bases, map and native evidence

- Installed Source STDO `v2.5.0-rc.1` verified with no failures at manifest
  SHA-256 `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`
  and 51-member standards identity
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`.
- Project frame basis revision 13 SHA-256
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`
  is accepted by separate Product-owner decision SHA-256
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`
  and bound by the overlay. The declaration's embedded pre-acceptance status is
  conserved; the external decision carries acceptance.
- Immutable Axiom Indexer verified at annotated tag object
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
  `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`, independently recomputed
  seven-member inventory
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
  and `ac.py` SHA-256
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.
- The exact validator reproduced program canonical SHA-256
  `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`,
  map intrinsic SHA-256
  `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`,
  and byte-identical map file SHA-256
  `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd`.
- Codex run 004 receipt SHA-256 is
  `183fb2363cae0923079ed07cf1019457061f617c2771aa14879145775a145f42`;
  its retained sections reproduced joined output SHA-256
  `123be210a03d6f0af78c87f75910252c75d6396554fc0d485305f973488cce36`.
- Claude run 003 receipt SHA-256 is
  `08639b2e5cc2cd4656cc1024e1a1ef86bc511b5d4b9b2919043cb5095df6e0ca`;
  its retained sections reproduced joined output SHA-256
  `bffa355be559bfdf70638e8632445c131bf2fa5a610bb7a544bf2ae1cb93a86f`.
  Both joined outputs match the immutable join law byte-for-byte and have no
  terminal newline.
- Codex run 003 remains a transparent provider-capacity HOLD with no sections,
  join or qualifying effect. Run 004 supplies the current successful Codex
  observation; no native model dogfood was rerun for this review.

## Exact checks

- `python3 -B scripts/check_constitution.py`: `valid`, failures `[]`;
- `python3 -B -O scripts/check_constitution.py`: `valid`, failures `[]`;
- normal constitutional tests: 19/19 passed;
- optimized constitutional tests: 19/19 passed;
- immutable Axiom Indexer tests: 15/15 passed;
- exact map reproduction: byte-identical;
- Codex run 004 join reproduction: byte-identical;
- Claude run 003 join reproduction: byte-identical;
- `stdo verify v2.5.0-rc.1`: valid, failures `[]`;
- `stdo status --definition stdo_representation.json --verify`: valid, installed,
  failures `[]`;
- `stdo fleet status --root ..` and `stdo fleet verify --root ..`: exactly three
  Product Definitions discovered and all valid; and
- `git diff --check` and `git fsck --strict`: passed.

The worktree was clean at requested HEAD immediately before this authorized
carrier was written. After writing it, this carrier is the sole worktree change.

## Publication namespace and residuals

A read-only `git ls-remote` successfully observed public `origin` main at
`41cb31318c945c7e529fe17e8b74d134c1409a98`. The same live query returned no
matching remote ref for:

- `refs/heads/rc/stdo_representation/2.5.0`;
- `refs/tags/stdo_representation/v2.5.0-rc.*`;
- `refs/tags/stdo_representation/v2.5.0` or its peeled form; or
- `refs/heads/release/stdo_representation/2.5.0`.

The matching local planned namespace is also absent. This is a qualified,
time-bound namespace observation, not proof of a future state and not a
publication act.

Residual uncertainty is non-blocking and unchanged: the five program residuals
remain active; semantic fidelity and usefulness beyond the observed tasks and
model families remain probabilistic; provider backing revisions are not
attested; and post-publication `F-EXACT-CUT` review, remote reacquisition and
human Product-owner acceptance remain future, separately authorized relations.

## Closed return

Verdict: **GO** for immutable RC publication readiness. `P0=0`, `P1=0`,
`P2=0`.

`F-CANDIDATE-READINESS` is `satisfied` for the exact subject bound above. This
review does not publish, tag, push, mutate a ref, accept a Product, or grant any
such authority. Any qualifying-byte change invalidates this verdict and requires
a new candidate review.
