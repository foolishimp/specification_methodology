# STDO Representation 2.5.0 RC1 Exact-Cut Review

- reviewed_at: `2026-09-01T00:10:00+10:00`
- reviewer: Codex, independent bounded post-publication evaluator
- verdict: `GO`
- severity: `P0=0`, `P1=0`, `P2=0`
- acceptance_authority: none

## Exact immutable subject

This review reacquired the public repository from
`https://github.com/foolishimp/specification_methodology.git` into a fresh
temporary clone and detached at the qualified annotated RC. The reacquired
identity is:

- immutable RC ref: `refs/tags/stdo_representation/v2.5.0-rc.1`;
- immutable RC tag object: `1eb81f90bcb2348027682b7d4d7e75285d7d917b`;
- version-line selector ref: `refs/tags/stdo_representation/v2.5.0`;
- selector tag object: `5f3abae64770bf19185d9ab8a76b7bdf14785761`;
- peeled commit: `5767f40a4d363067b2dbe8f47f6e288e3e5e9cd7`;
- repository tree: `66ff1f256dd96e2fba84a009a1f83a1c969a3c2b`;
- `stdo_representation/` subtree:
  `c1a8221b525a292322d80543d7d4d3491c4fe5e0`;
- eight-member Product inventory SHA-256:
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`;
- release record `releases/v2.5.0.md` SHA-256:
  `079f1af9f05031524ec3fe003b7bf8cfea6238eacc8ac36dae0802cc3bd03557`.

Both tags are annotated tags and peel to the same commit. A live public
`git ls-remote` showed `main`, `rc/stdo_representation/2.5.0`, and
`release/stdo_representation/2.5.0` at that commit. The only public immutable RC
on the Representation `2.5.0` line is RC1, so RC1 is the highest positive RC
ordinal and the selector is aligned. No mutable local checkout supplied the
review subject.

## Governing release basis and immutable reacquisition

The Product Definition selects exact installed Source STDO
`stdo://releases/v2.5.0-rc.1/` with manifest SHA-256
`3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`.
A new temporary toolchain store independently installed, synchronized, and
verified that cut with no failures:

- STDO tag object: `42f59b6cd24071d9c445a29ae2a691cf0828211e`;
- peeled commit: `ca6694314c4e9a56d3facae3eef06fe2792104c9`;
- repository tree: `f0fac91f195b1f1506423060556bd36b3256d835`;
- standards tree: `48a3e52b0aaf24b6d1d38ff551349e19b9b3c208`;
- standards members: `51`;
- standards member-set SHA-256:
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`;
- installed `RELEASE_METHOD.md` SHA-256:
  `c690228adf680dc4ef0a391073a5d60e515fbd4b0150b778b6adb4723e3fa9a0`.

The installed Release Method governs this evaluation. Its exact-cut identity,
highest-RC selector, complete-successor-disposition, qualifying-byte, and
separate human-acceptance laws are satisfied for the subject above.

## Product members and release claims

The declared inventory was recomputed from exact file bytes and the UTF-8
symlink target strings, in canonical path order:

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

The two symlink modes are `120000`; the six file modes are `100644`. The
canonical row aggregate is exactly
`08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`.

The five release claims close at their declared boundaries:

- `STDO-REP-2.5-C01` — `satisfied`: Representation version `2.5.0` equals the
  represented STDO semantic version while Product, release, RC ordinal, member,
  dependency, and acceptance identities remain distinct.
- `STDO-REP-2.5-C02` — `satisfied`: the Product carries one canonical,
  source-linked `a_c.STDO` compression for exact STDO `v2.5.0-rc.1`.
- `STDO-REP-2.5-C03` — `satisfied`: the deterministic index binds the unchanged
  compression URI and canonical digest, preserves 15 symbols, 51 clauses, five
  residuals, and has one source-route entry for every one of those 71 items.
- `STDO-REP-2.5-C04` — `satisfied`: the explicit Product Definition composition
  resolves `urn:stdo:product-definition:axiom-indexer` and imports only the
  exact immutable Axiom Indexer mechanics; mutable sibling source was not used.
- `STDO-REP-2.5-C05` — `satisfied`: the canonical skill and target references
  preserve map-first use, visible frame selection, bounded Source STDO re-entry,
  exact joining, role closure, and the non-authority boundary for both retained
  native observations.

The accepted bootstrap predecessor remains immutable at tag object
`46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`, peeled commit
`b127ee9a0362f85d4875ae59664ecfcd13028d9c`, tree
`15f9beb360836386ce9607dd31e30d0c8b5cd830`, and inventory
`316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`.
Every predecessor claim has exactly one Release-Method disposition:

- `STDO-REP-0.1-C01`: `superseded` by current C02 and C03;
- `STDO-REP-0.1-C02`: `conserved` by current C03;
- `STDO-REP-0.1-C03`: `conserved` by the canonical skill and discovery members;
- `STDO-REP-0.1-C04`: `conserved` by LLM-owned selection/order, immutable
  joining, and the zero-local-engine boundary; and
- `STDO-REP-0.1-C05`: `conserved` within the exact current native-evidence
  boundary.

## Accepted frame basis and Product Definition

Project frame-basis revision 13 recomputes to SHA-256
`0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`.
The separate Product-owner acceptance decision recomputes to SHA-256
`7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`.
The Product Definition Overlay recomputes to SHA-256
`5e2a9302edcd827278c62393fff4a4fa7bc43d8fffee8bff91c97566dd5cf969`
and binds that exact declaration and decision. The declaration's embedded
pre-acceptance status remains historical text; the external decision supplies
the acceptance relation. Overlay schema validation and verified status both
pass against the exact installed STDO basis.

## Immutable Axiom dependency and reproductions

A separate fresh public clone of `https://github.com/foolishimp/axiom_indexer.git`
was detached at exact `v0.1.0-rc.1`. It independently reproduced:

- annotated tag object: `e7afc8a42a7123aebe91cb7582cb037b1aae612d`;
- peeled commit: `dc3e00998da36dae6ac7b76b340431a85096c83c`;
- repository tree: `8c9ad5f5e99a60c18fb8c1802471753afb226272`;
- seven-member Product inventory SHA-256:
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`;
- `ac.py` SHA-256:
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.

That immutable validator, using the independently installed STDO basis,
returned `valid`, zero diagnostics, canonical program SHA-256
`8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`,
and intrinsic map SHA-256
`e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`.
The emitted map was byte-identical to the Product member at file SHA-256
`e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd`.

No model dogfood was rerun. The retained fresh receipts and their exact joining
were instead reverified:

- Codex run 004 receipt SHA-256:
  `183fb2363cae0923079ed07cf1019457061f617c2771aa14879145775a145f42`;
  immutable join reproduction matched its retained 6,033-byte output at
  SHA-256 `123be210a03d6f0af78c87f75910252c75d6396554fc0d485305f973488cce36`.
- Claude run 003 receipt SHA-256:
  `08639b2e5cc2cd4656cc1024e1a1ef86bc511b5d4b9b2919043cb5095df6e0ca`;
  immutable join reproduction matched its retained 5,670-byte output at
  SHA-256 `bffa355be559bfdf70638e8632445c131bf2fa5a610bb7a544bf2ae1cb93a86f`.

Both outputs match the exact caller-order join law and have no terminal
newline. Both receipts bind the current Product inventory, accepted frame
basis, exact STDO Install, immutable Axiom dependency, visible top-level
Reviewer frame, bounded source re-entry, and distinct Product Definition,
Release Cut, Product, and Install relations.

## No qualifying-byte delta

The pre-RC review qualified commit
`fb0c696b3cca9cf66a58d301d37b73ef9ec4862e`, repository tree
`1430f70652a58d8f1b5cfb48561e5571902eaef5`, and Representation subtree
`b69d725726b9d44de63ab55ec436719b13eae6c6`.

The complete Git delta from that subject to the public RC adds only:

- `.ai-workspace/comments/codex/20260831T235000_REVIEW_stdo_representation_2.5_pre_rc.md`; and
- `.ai-workspace/decisions/20260901T000051_v2.5.0_rc1_publication_grant.json`.

No Product member, release record, release claim, predecessor disposition,
Product Definition, frame basis, frame-basis decision, requirement, or
dependency byte changed. The exact Product inventory and release-record hashes
therefore equal the pre-RC reviewed subject. The qualifying-byte delta is zero;
the changed subtree identity reflects only retained qualification and
publication evidence outside the Product and release subject.

## Checks

- normal constitutional checker: `valid`, failures `[]`;
- optimized constitutional checker: `valid`, failures `[]`;
- normal constitutional tests: `19/19` passed;
- optimized constitutional tests: `19/19` passed;
- immutable Axiom Indexer tests: `15/15` passed;
- map reproduction: byte-identical;
- Codex run 004 join reproduction: byte-identical;
- Claude run 003 join reproduction: byte-identical;
- `stdo verify v2.5.0-rc.1`: valid, failures `[]`;
- Product Definition sync/status with verification: valid and installed;
- fleet sync/status/verify: exactly three Product Definitions, all valid;
- `git diff --check`: passed; and
- `git fsck --strict`: passed.

The detached review clone remained clean. The current Product bytes were not
edited.

## Findings, residuals, and closed return

Findings: none. `P0=0`, `P1=0`, `P2=0`.

The five declared program residuals remain explicit and non-blocking for the
bounded release claims:

- `compression-overlap-needs-source-reentry`;
- `frame-adoption-not-claimed`;
- `full-m-b-not-constructed`;
- `semantic-acceptance-not-supplied`; and
- `template-placeholders-are-not-decisions`.

Semantic fidelity and usefulness beyond the retained tasks and model families
remain probabilistic. Provider backing revisions are not attested. Structural
validation, publication, and successful native observations still do not
establish complete semantic truth, runtime authority, or Product acceptance.

Verdict: **GO** for exact-cut qualification of public STDO Representation
`2.5.0-rc.1`. `F-EXACT-CUT` is `satisfied` for the exact subject above. The RC
is eligible for a separate human Product-owner acceptance decision.

This review is a continuing-main commentary carrier outside the immutable RC,
Product member set, and release-scoped claim bytes. It does not accept the
Product, move a ref, mutate a tag, publish anything, change a ticket or Goal, or
grant continuation authority.
