# STDO Representation 0.1.0 RC1 Exact-Cut Review

## Verdict

**`satisfied` — GO.**

The public immutable cut `v0.1.0-rc.1` exactly carries the pre-RC candidate
qualified under inventory
`316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`
and release record
`7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876`.
The independently reacquired cut satisfies `F-EXACT-CUT` and the installed
STDO Release Method for the published claims `STDO-REP-0.1-C01` through
`STDO-REP-0.1-C05`.

This GO is qualification evidence. It does not accept the Product, move a ref,
authorize mutation, or choose subsequent work. Exact Product acceptance
remains with `urn:stdo-representation:authority:product-owner`.

## Findings

### P1

None.

### P2

None.

## Activation and independence

- Frame: `F-EXACT-CUT` from accepted project basis
  `urn:stdo-representation:reference-frame-basis:source-project:11`.
- Governing release law: exact installed STDO
  `v2.5.0-rc.1/standards/RELEASE_METHOD.md`, SHA-256
  `c690228adf680dc4ef0a391073a5d60e515fbd4b0150b778b6adb4723e3fa9a0`.
- Assessor: Codex `/root/exact_cut_review`, acting only as the separately
  activated exact-cut assessor. The collaboration runtime does not
  provider-attest its backing model revision.
- Subject acquisition: clean public clone at
  `/tmp/stdo-representation-v0.1.0-rc.1.WHgb17`, detached at the annotated RC
  tag, with `origin` equal to
  `https://github.com/foolishimp/stdo_representation.git`.
- Independence: this assessor did not author, repair, commit, publish, or
  accept the qualifying candidate. Inspection and qualification were
  read-only; the clone remained clean.
- Remote observation time: `2026-08-31T01:47:22+10:00`.

## Public cut identity

Direct `git ls-remote` observation of public `origin` and local Git-object
inspection agreed:

| Coordinate | Verified value |
|---|---|
| immutable RC tag | annotated `v0.1.0-rc.1` |
| RC tag object | `46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f` |
| version-line selector | annotated `v0.1.0` |
| selector tag object | `98ef2a4e54d7b6d8465b71234451e2ccc465f1f8` |
| peeled commit | `b127ee9a0362f85d4875ae59664ecfcd13028d9c` |
| repository tree | `15f9beb360836386ce9607dd31e30d0c8b5cd830` |
| `main` | `b127ee9a0362f85d4875ae59664ecfcd13028d9c` |
| `rc/0.1.0` | `b127ee9a0362f85d4875ae59664ecfcd13028d9c` |
| `release/0.1.0` | `b127ee9a0362f85d4875ae59664ecfcd13028d9c` |

Both annotated tags peel to the same commit. The RC tag message names RC1; the
selector message names `v0.1.0-rc.1` as the latest published RC. Public tag
enumeration found no higher `v0.1.0-rc.*` ordinal. Publication is therefore
complete and the selector, RC branch, release branch, and `main` are aligned.

## Reacquired Product subject

Git tree modes, blob bytes, symlink target strings, per-member SHA-256 values,
and the canonical sorted inventory were reconstructed from the public cut.
The Product contains exactly these eight declared entries:

| Type | Member | Verified SHA-256 |
|---|---|---|
| symlink | `.agents/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| symlink | `.claude/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/axiomatic-program.json` | `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.1/logical-constraint-map.json` | `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95` |
| file | `skills/stdo-representation/SKILL.md` | `f540971bc895890c182ef5ddbe0478621c418aea430ac7f45a8c3665a45c133c` |
| file | `skills/stdo-representation/agents/openai.yaml` | `1a29d7794af568b13c4bce7c68ea7a24e352555cb9d2bccfb4a8221267477f00` |
| file | `skills/stdo-representation/references/claude.md` | `85ea8f51d91ddec1eafc219b0e143cdc27fd680a63dd568ab10dc29aac4dafb7` |
| file | `skills/stdo-representation/references/codex.md` | `add6352200451603da5dda388937c8689300d822ce345413888695c23f4617af` |

Canonical inventory SHA-256:
`316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`.

Release-record SHA-256:
`7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876`.

Candidate and cut bytes agree. No post-publication qualifying-byte repair is
present or needed.

## Exact bases and accepted frame basis

The Product Definition selects exact Source STDO `v2.5.0-rc.1`. `stdo status
--definition stdo_representation.json --verify` and `stdo verify
v2.5.0-rc.1` both returned valid with no failures:

- installed manifest:
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`;
- standards member set:
  `87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5`;
- `AXIOMATIC_CALCULUS.md`:
  `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`.

Exact Axiom Indexer `v0.1.0-rc.1` also matched its public annotated tag and
installed cut:

- tag object: `e7afc8a42a7123aebe91cb7582cb037b1aae612d`;
- peeled commit: `dc3e00998da36dae6ac7b76b340431a85096c83c`;
- tree: `8c9ad5f5e99a60c18fb8c1802471753afb226272`;
- Product inventory:
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`;
- `ac.py`:
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`.

The accepted project frame basis was reacquired at SHA-256
`09db079c16758db8765452bd05f6b5de3ce831974e80fb9ea59ef876fab50ed9`.
Its Product-owner acceptance record matched SHA-256
`371d0d031fa518a7c5a92a97c658e5c1bc5765b13d1c30f0d7938671c054b89e`,
and the bound Product Definition matched SHA-256
`a5bf9dab97d25984a1befed4bcab8dc71938cfdecc975294ba5865f3c0a192b1`.
The basis file's embedded pre-acceptance status remains the exact accepted
subject; the separate decision and overlay carry the acceptance relation.

## Release claims

| Claim | Result | Reacquired qualification |
|---|---|---|
| `STDO-REP-0.1-C01` | `satisfied` | The public eight-member subject contains one exact source-linked `a_c.text` program and its logical map. Fresh exact Axiom validation produced report `66ffd50f30801fd6b9c0b29e94839dadf09f9ae8f901239e81c224733b2aed4f` and reproduced the Product map byte-for-byte at `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95`. |
| `STDO-REP-0.1-C02` | `satisfied` | The program has 14 symbols, 51 clauses, and five explicit source-routed residuals. Map source routes are total over program items. The Product, release record, skill, and retained validation evidence consistently limit validation to structure and resolution. |
| `STDO-REP-0.1-C03` | `satisfied` | Both repository-native symlinks have the exact declared target and resolve to the same four-file canonical skill. Retained fresh Codex and Claude smoke evidence identifies the exact Product program URI. |
| `STDO-REP-0.1-C04` | `satisfied` | The canonical skill assigns every frame, label, text value, and ordering choice to the LLM and delegates only the pure join relation to exact Axiom Indexer. The Product member set contains no local engine. Fresh joins reproduced run-001 request SHA-256 `0b94d157012b7c118e6150309fba8a3aba6e2af26aa3f2659d8bc0dd98ab0051` and run-002 request SHA-256 `43cad2ada2ca54a0b8fe7a5bc0ba424cd0556eaa8e18a8e0c5bcfd88af9aad9e`. |
| `STDO-REP-0.1-C05` | `satisfied` | The public cut retains native pickup, visible Executive frame details and source routes, bounded source re-entry, equal-task direct-prose/map-first comparison, Claude corroboration, and exact join inputs and outputs. The closed pre-RC review bounds the claim to observed tasks and reports the retained negative and residual evidence. |

No claim is widened into semantic completeness, automatic frame selection,
GTL, ABG, provider attestation, runtime authority, publication authority, or
Product acceptance.

## Genesis and retained candidate result

The release record declares `v0.1.0-rc.1` as a genesis cut with no predecessor
immutable STDO Representation RC. Public enumeration confirms there is no lower
or higher RC on the `0.1.0` line. Successor-baseline conservation is therefore
not applicable to this first cut.

The public cut retains the closed pre-RC result at
`.ai-workspace/comments/codex/20260831T012000_REVIEW_stdo_representation_0.1.0_pre_rc.md`,
file SHA-256
`31e16e0ec53ea7d22c9f14341b86ddf4ca1c8296def3b22c2b2ae73cb30c9a06`.
It returns `satisfied` and GO over the same inventory and release-record bytes,
and it retains rather than erases the earlier different-subject HOLD,
sandbox-enforcement limitation, Claude display-precision residual, comparison
evidence, and five semantic-map residuals. The exact publication grant is also
retained at SHA-256
`176a5b886bef76ef762ba2f31d50149dfc02961f8a5d5116407e06d3a3022863`.

## Checks

- Public `git ls-remote` for all three branches, both annotated tags, peeled
  refs, and all `v0.1.0-rc.*` tags: exact alignment; no higher ordinal.
- Tag-object, commit, tree, Git mode, blob, symlink, inventory, and release-
  record reconstruction: exact match.
- `git fsck --strict`, `git diff --check`, and detached-clone cleanliness:
  passed.
- `stdo status --definition stdo_representation.json --verify`: valid, no
  failures, accepted-and-bound revision-11 frame basis.
- `stdo verify v2.5.0-rc.1`: valid, no failures.
- `python3 scripts/check_constitution.py`: `valid: true`, failures `[]`, eight
  members, exact program/map identities.
- `python3 -m unittest scripts.test_check_constitution -v`: 6/6 passed.
- Exact installed Axiom Indexer unit and falsifier suite: 15/15 passed.
- Fresh exact map reproduction in temporary output space: validation report
  SHA-256 `66ffd50f...ed4f`; map SHA-256 `8161a99e...5a95`; byte comparison
  matched the public Product map.
- Fresh exact request joining for retained run 001 and run 002: both expected
  SHA-256 values reproduced.

These checks establish only their named identity, transport, structural,
mechanical, source-recovery, and observed-use properties. Claim disposition is
the bounded semantic judgment above.

## Residuals

- The five published map residuals remain active: semantic acceptance is not
  supplied; a complete admitted `M_b` is not constructed; compression overlap
  may require source re-entry; frame references do not establish adoption; and
  template placeholders are not decisions.
- Semantic fidelity and native usefulness beyond the observed Codex and Claude
  tasks remain probabilistic and are not generalized by this GO.
- Provider backing revisions remain unattested. The retained dogfood evidence
  does not claim exact provider-invocation provenance.
- The retained requested-versus-effective sandbox mismatch limits sandbox-
  enforcement assurance but does not affect the published behavioral claims.
  The retained Claude URI-display abbreviation does not affect the exact source
  route or successful source re-entry.
- `main`, the RC branch, the release branch, and the version-line selector are
  mutable discovery carriers. This verdict binds their observed alignment at
  the time above and the immutable RC object; later mutable-ref drift requires
  a new observation, not reinterpretation of this result.

## Invalidation

This result is invalid for another RC, tag object, peeled commit, tree, Product
inventory, release-record bytes, claim set, dependency cut, frame-basis
acceptance relation, predecessor/genesis disposition, or retained candidate
result. Any qualifying-byte repair requires a higher immutable RC.

## Closed return

Frame result: **`satisfied`**.

Exact-cut recommendation: **GO** for annotated
`v0.1.0-rc.1` tag object
`46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`, peeled commit
`b127ee9a0362f85d4875ae59664ecfcd13028d9c`, and tree
`15f9beb360836386ce9607dd31e30d0c8b5cd830`.

Return consumer: Executive/root agent and Product owner. No repair,
publication, ref mutation, acceptance, Product disposition, or continuation
selection was performed.
