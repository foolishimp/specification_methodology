# Final Candidate Review — STDO Representation 2.5.0

- reviewed_at: `2026-08-31T23:20:00+10:00`
- reviewer: Codex, independent bounded pre-publication evaluator
- disposition: `HOLD`
- severity: `P0=0`, `P1=1`, `P2=0`
- publication_authority: none

## Exact subject

This review binds the pre-publication candidate at:

- commit: `26a920224cec9cf188a77c7c6da6893bf945e638`;
- repository tree: `f3d2bc47eb197a6dacbbd22cedfd687f09692e6b`;
- `stdo_representation/` subtree: `9aec2601b5f3b866f28c1e8e34840c69ae715ad4`;
- release record `releases/v2.5.0.md`: SHA-256
  `aee34a1adb2877203fa9ff9920ee82f89be78e69697c0ce80e2eaf3a022bdd99`;
- Product Definition Overlay `stdo_representation.json`: SHA-256
  `5e2a9302edcd827278c62393fff4a4fa7bc43d8fffee8bff91c97566dd5cf969`;
- eight-member Product inventory SHA-256:
  `08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`.

This commentary is outside the reviewed Product and release subject.

## Finding

### P1 — The predecessor claim relation uses a disposition not admitted by the exact Release Method

Exact installed STDO `v2.5.0-rc.1`
`RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015` requires every
predecessor claim capable of affecting the successor to receive exactly one of
these semantic dispositions:

- `conserved`;
- `superseded`;
- `intentionally removed`; or
- `not applicable` with a bounded reason.

It states that an unresolved disposition blocks qualification of the affected
claim.

The candidate release record says predecessor claims
`STDO-REP-0.1-C01` and `STDO-REP-0.1-C02` are **refined** by the
compression/index split. `refined` is not one of the four admitted
dispositions. The same sentence explicitly marks C03 through C05 as
`conserved`, demonstrating that the record is attempting claim-by-claim
successor disposition but leaves C01 and C02 outside the installed result
algebra.

The successor does semantically retain the substance of both claims across
current C02 and C03. That evidence does not choose the missing Release Method
disposition on behalf of Product authority. The exact release-facing bytes
therefore do not yet establish the complete successor relation required for
pre-publication candidate readiness.

Result: `F-CANDIDATE-READINESS` is `falsified` for this exact release record.
Publication is held until Product authority records an admitted disposition
for predecessor C01 and C02 and a new exact candidate is independently
reviewed.

## Product inventory

The declared and independently recomputed inventory contains exactly eight
members:

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

The canonical sorted-row inventory reproduced
`08a13f8c160ec70e724d414260324923eba4187d9474aa434342098d9c45002a`.
File modes and both symlink target strings agree with the release record.

## Closed non-findings

No P0 or P2 issue was found. The following requested boundaries are satisfied
for the exact subject:

- **Identity semantics:** the repaired compression distinguishes the stable
  mutable Product-Definition Identity from immutable Product identity. It also
  carries separate `release-cut` and `install` symbols, binds immutable RC
  publication to Release Cut, and binds the installed-release manifest to
  Install. Product, Release Cut, Install, source project, and definition line
  are not collapsed.
- **Program and index:** the Axiomatic Program is the Product-selected semantic
  compression. The Logical Constraint Map binds its unchanged URI and canonical
  SHA-256 `8910927be67b1d2cac988797a826c3be459512011e82a29bbbe8374614c3f11c`,
  retains the repaired 15-symbol, 51-clause, five-residual populations, and has
  total source routes. Its intrinsic SHA-256 is
  `e3ec18cc61cc297e1fbee96e65bc125de2da08eb3d4e6ddd4f4c354c1073cd93`.
  Exact immutable Axiom Indexer validation reproduced byte-identical map file
  SHA-256 `e00a7ccdecbfb6fae1bd1c99e023ff8bede5508e679562b29f4a054907d9a4dd`.
- **Frame basis:** revision 13 SHA-256
  `0e3e0f70e78030a4e1d099be01699823d375293f929e549ef780a3a83c925539`
  is accepted by the separate Product-owner decision SHA-256
  `7866c99d4f40d8625d5ca469730fbfc9412c55a6e693a53079d7085f3c493001`
  and is bound by the overlay. The proposal bytes remain unchanged while the
  external decision supplies acceptance.
- **Release profile and composition:** the Product-local shared-source profile
  uses the installed Release Method's alternate-spelling permission without
  turning the source subtree into Product identity. The explicit composition
  edge resolves target definition
  `urn:stdo:product-definition:axiom-indexer`, cites the exact contracts, and
  does not substitute the mutable sibling.
- **Immutable Axiom dependency:** tag object
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d`, peeled commit
  `dc3e00998da36dae6ac7b76b340431a85096c83c`, tree
  `8c9ad5f5e99a60c18fb8c1802471753afb226272`, seven-member inventory
  `7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6`,
  and `ac.py` SHA-256
  `dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672`
  agree across the release, skill, checker, and installed dependency.
- **Native evidence:** repaired Claude run 003 and Codex run 004 bind the same
  current Product inventory and repaired program/index identities, start
  map-first, select one actual Reviewer frame, keep clauses and residuals
  separate, re-enter exact installed Source STDO, preserve the four identity
  distinctions, and return closed without repair or promotion. Re-executing the
  immutable joiner over each retained `sections.json` reproduced each
  `joined-request.txt` byte-for-byte. Receipt SHA-256 values are
  `08639b2e5cc2cd4656cc1024e1a1ef86bc511b5d4b9b2919043cb5095df6e0ca`
  and
  `183fb2363cae0923079ed07cf1019457061f617c2771aa14879145775a145f42`.
- **Retained capacity HOLD:** Codex run 003 transparently retains the one-shot
  `gpt-5.6-sol` provider-capacity failure, absent sections and join, and its
  unclosed boundary. It changed no Product member and is not used to qualify
  C05. Codex run 004 supplies the successful current Codex observation.
- **Claims C01-C05:** C01 through C05 are satisfied at their declared Product,
  semantic, mechanical, dependency, and observed-native boundaries. Validation
  and native use do not claim completeness, unique truth, acceptance, or
  authority. These claim results do not cure the separate incomplete
  predecessor disposition.
- **Predecessor objects:** the accepted bootstrap predecessor remains exact at
  annotated tag object `46e9cb36ce0056cf75e9c12bcde4e6834a1d3a4f`, peeled
  commit `b127ee9a0362f85d4875ae59664ecfcd13028d9c`, tree
  `15f9beb360836386ce9607dd31e30d0c8b5cd830`, inventory
  `316121da619af277b984a599d290e41e4740ef9f1a2bf3fd8151ac9b1d64e091`,
  and release-record SHA-256
  `7d7e0c78fa5fe893ae530df0069d7f18ecf69144a845f8f782d3c842fe50f876`.
  The P1 concerns only the successor claim-disposition vocabulary.
- **Checks:** normal and optimized constitutional checkers returned `valid`
  with no failures; normal and optimized constitutional tests passed 18/18;
  exact Axiom Indexer tests passed 15/15; Product status and all three fleet
  definitions verified; installed STDO `v2.5.0-rc.1` verified at manifest
  `3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338`;
  Git diff checking and `git fsck --strict` passed.
- **Publication namespace:** `origin` has no matching
  `refs/heads/rc/stdo_representation/2.5.0`,
  `refs/tags/stdo_representation/v2.5.0-rc.*`,
  `refs/tags/stdo_representation/v2.5.0`, or
  `refs/heads/release/stdo_representation/2.5.0`. The candidate remains
  unpublished.

## Closed return

Verdict: **HOLD**. `P0=0`, `P1=1`, `P2=0`.

No Product member, release record, specification, decision, ref, tag, branch,
or remote was changed. This review grants no publication, repair, continuation,
or Product-acceptance authority.
