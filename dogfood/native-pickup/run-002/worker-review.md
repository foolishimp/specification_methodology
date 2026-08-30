# Worker return

**Overall result: `falsified`**

**Release recommendation: HOLD**

The map and imported mechanics substantially match the thin LLM-first design, but the complete frozen Product does not satisfy revision 11. The native skill omits mandatory identity/failure/role instructions, describes the unpublished map as “released,” and no qualifying `K-DOGFOOD` equal-arm comparison exists. This is evidence for Executive disposition only—not Product acceptance, publication authority, or an RC verdict.

## Severity-ranked findings

### High — Native instructions do not implement their accepted contract

- **Violated claims:** `REQ-P-NATIVE-001`, `REQ-P-NATIVE-006`, and `REQ-P-NATIVE-008`; Product native projection items 1, 6, and 7.
- **Candidate evidence:** [SKILL.md](/Users/jim/src/apps/stdo_representation/skills/stdo-representation/SKILL.md:10), SHA-256 `c0585244411ccecdc388625d768595693e559239507129c3e58d6b4839b9bb1d`.
- **Authority:** `repo://stdo-representation/specification/requirements/REQ-P-NATIVE-FRAME-USE.md#requirements` and `repo://stdo-representation/specification/PRODUCT.md#native-agent-projection`.
- **Counterexample:** the complete 36-line skill tells the agent to read a fixed map path and resolve Axiom Indexer `v0.1.0-rc.1`, but never tells it to:
  - verify the map’s file/canonical identity or the dependency’s tag, commit, tree, inventory, or executable identity;
  - return a visible hold/re-entry request on map, dependency, frame, source-route, evidence-boundary, or task failure; or
  - preserve the concrete Worker/Reviewer/Executive prohibitions and closed Executive return.
- **Consequence:** a stale or replaced map/dependency can be consumed under the canonical skill, and correct role behavior depends on externally supplied prompt text rather than the Product’s common semantic instructions. `F-NATIVE-USE` is falsified.

### High — Candidate-native metadata falsely labels the map “released”

- **Violated claim:** the pre-publication/release-status boundary and `REQ-P-NATIVE-007`.
- **Candidate evidence:** [SKILL.md](/Users/jim/src/apps/stdo_representation/skills/stdo-representation/SKILL.md:3) and [openai.yaml](/Users/jim/src/apps/stdo_representation/skills/stdo-representation/agents/openai.yaml:4) both say “released STDO … map.”
- **Authority:** `repo://stdo-representation/specification/PRODUCT.md#current-boundary`, which states that no STDO Representation RC, released `a_c.STDO`, or accepted Product exists.
- **Falsifier:** the exact frozen candidate is pre-publication; `git ls-remote` returned no `v0.1.0*`, `rc/0.1.0`, or `release/0.1.0` refs.
- **Consequence:** the native pickup surface conveys a release status that the exact authority expressly denies.

### High — Required independent dogfood comparison is absent

- **Violated claims:** `REQ-P-DOGFOOD-002`, `008`, and `010`; `F-DOGFOOD-USEFULNESS`/`K-DOGFOOD`.
- **Evidence:** retained smoke, Claude map-first, and Executive-join records exist, but repository search found no frozen direct-prose arm, equal map-first arm, same-task/evidence/model/evaluator record, separated assessor record, or independent usefulness verdict.
- **Authority:** `repo://stdo-representation/specification/REFERENCE_FRAME_BASIS.md#f-dogfood-usefulness` and `#actor-capability-envelopes`.
- **Falsifier:** no exact pair of arm inputs and outputs can be named. Existing map-first records cannot serve as their own comparison verdict.
- **Consequence:** `F-DOGFOOD-USEFULNESS` is `indeterminate`; a GO is prohibited.

### Medium — Retained Claude evidence contains a false source-route residual

- **Affected claim:** accurate bounded source recovery in retained native evidence.
- **Evidence:** [Claude result](/Users/jim/src/apps/stdo_representation/dogfood/native-pickup/claude-run-001/result.md:36) says `#reference-frame-laws` is not an installed heading.
- **Source authority:** `stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws`.
- **Falsifier:** the installed source has `## Reference Frame Laws`, and exact Axiom validation successfully resolves that fragment.
- **Consequence:** the negative result was retained honestly, but it is an actual native source-recovery regression and cannot support a clean usefulness verdict.

## Exact subject and basis verification

No supplied coordinate mismatch was found.

### Frame-basis status

- Frame set: `urn:stdo-representation:reference-frame-basis:source-project:11`
- Basis file: `specification/REFERENCE_FRAME_BASIS.md`
- Basis SHA-256: `09db079c16758db8765452bd05f6b5de3ce831974e80fb9ea59ef876fab50ed9`
- Decision: `.ai-workspace/decisions/20260831T005313_frame_basis_rev11_acceptance.json`
- Decision SHA-256: `371d0d031fa518a7c5a92a97c658e5c1bc5765b13d1c30f0d7938671c054b89e`
- Actor: `https://github.com/foolishimp`
- Authority: `urn:stdo-representation:authority:product-owner`
- Scope: exact revision-11 thin-0.1.0 qualification/publication basis only; no Product expansion or not-yet-published RC acceptance.
- Product authority: `specification/PRODUCT.md#product-disposition-authority`
- Product SHA-256: `f0c47af3c167b977e0c0aec11a4a7388ccb29b24cf35204b80ccc341a879a6ff`
- Overlay: `stdo_representation.json`
- Overlay SHA-256: `a5bf9dab97d25984a1befed4bcab8dc71938cfdecc975294ba5865f3c0a192b1`
- Binding: exact revision-11 basis plus Product authority and exact decision, applying to `urn:stdo:product-definition:stdo-representation`.

`stdo status --verify` reported no failures. The basis file’s self-description as pending is not drift: its acceptance gate deliberately requires the external exact-digest decision, which exists and matches. This is frame-basis acceptance only—not Product acceptance, RC acceptance, publication, or GTL direction.

### Frozen eight-member subject

| Member | Verified SHA-256 |
|---|---|
| `axiomatic-program.json` | `a561853b324e6464324238ee3cdb505edff20e78a8b5b83ff8bc202a1d261783` |
| `logical-constraint-map.json` | `8161a99e0cd80170882e2019f72f419dd773683c0731ad9b3a0d1d31a5905a95` |
| `SKILL.md` | `c0585244411ccecdc388625d768595693e559239507129c3e58d6b4839b9bb1d` |
| `agents/openai.yaml` | `9f35206d89079a1467f567f9d35e60a09daadca8a6279c046fafd748b6919916` |
| `references/claude.md` | `85ea8f51d91ddec1eafc219b0e143cdc27fd680a63dd568ab10dc29aac4dafb7` |
| `references/codex.md` | `add6352200451603da5dda388937c8689300d822ce345413888695c23f4617af` |
| `.agents/skills/stdo-representation` target string | `../../skills/stdo-representation`, digest `92c6b8…6ddb` |
| `.claude/skills/stdo-representation` target string | `../../skills/stdo-representation`, digest `92c6b8…6ddb` |

Independently rebuilt canonical inventory:

`71059615dde0f9c4e94e34f6517ef6f363858be462613fe3e1c31195786ce779`

Release record:

`47c9a2893f61d1dce72103d9c837f12ed5fa9fe6ae65719c07c693e5e100b857`

Genesis disposition is explicit and non-contradictory: `v0.1.0-rc.1` is the genesis cut, has no predecessor immutable RC, and successor-baseline conservation is inapplicable to that first cut.

### Program, map, and dependencies

- Program URI: `urn:stdo-representation:program:a-c-text:stdo-v2.5.0-rc.1:run-001`
- Program canonical SHA-256: `e325e4399560b0be5562d345005818e4f925f72ecbfd9a234207f8c77b095cc5`
- Map canonical preimage: `2df34cb85bf6fbad2436e468e14cb5c26ff8d0aa721f8de10bb7e948b0d21b78`
- Population: 14 symbols, 51 clauses, five residuals.
- Source STDO manifest: `3cd24c…d338`, valid with no failures.
- Source member aggregate: `87dca9…e1e5`, 51 members.
- Axiom Indexer: tag `e7afc8…612d`, commit `dc3e00…f3c`, tree `8c9ad5…272`.
- Axiom Product inventory: `7df380…f7e6`.
- Exact executable SHA-256: `dfb4d7…b672`.
- All 51 installed Source STDO members are grounded by program item source routes; missing `[]`, extra `[]`.

## Ordered frame results

| Frame | Result | Closed subject and evidence |
|---|---|---|
| `F-PRODUCT-BOUNDARY` | `satisfied` | Exact inventory `710596…e779`. Eight members only; no local executable, semantic compiler, GTL, ABG, renderer, tokenizer, or hidden heavy-prototype dependency. |
| `F-MECHANICAL-BOUNDARY` | `satisfied` | Program `e325e4…5cc5`, binding-set file `dd6d19…e1d4`, exact Axiom executable `dfb4d7…b672`. Validation returned `valid`, zero diagnostics; in-memory instantiation reproduced map bytes `8161a9…a95`. Join input `d67c42…a564` reproduced request `43cad2…ad9e`. |
| `F-MAP-ESSENCE` | `satisfied` | Consumed the closed mechanical result above and exact map `8161a9…a95`/preimage `2df34c…21b78`. The adversarial sample recovered governing layer, authority, frame, release, compression, and overlay constraints without a material map contradiction. All five residuals are useful and source-routed. |
| `F-NATIVE-USE` | `falsified` | Consumed the same closed mechanical/map subjects. Discovery symlinks and presentation-only references work, but the exact canonical skill fails accepted identity-verification, failure-return, and role-return instruction requirements and misstates release status. |
| `F-DOGFOOD-USEFULNESS` | `indeterminate` | No lawful equal-arm `K-DOGFOOD` subject exists. The frame was not manufactured from unpaired retained outputs. |
| `F-CANDIDATE-READINESS` | `falsified` | Subject is inventory `710596…e779`, release record `47c9a2…b857`, exact dependencies, and explicit genesis disposition. It cannot close because Native is falsified and Dogfood is indeterminate. The publication plan exists in T-004, but no publication grant follows and remote target refs are absent. |

`F-EXACT-CUT` was not selected, activated, or assessed. No immutable STDO Representation RC subject exists.

## Dogfood comparison record

- **Direct-prose arm:** absent.
- **Equal map-first arm:** absent.
- **Available unpaired map-first records:**
  - Codex smoke: `gpt-5.6-sol`, low effort; pickup only.
  - Claude smoke: `claude-fable-5` alias, low effort; pickup only.
  - Claude bounded task: request `bdbb49…3fb`, result `1d4264…14a6`, Claude Code `2.1.251`, alias `fable`, low effort, plan mode, `Read` only.
  - Executive join: sections `d67c42…a564`, request `43cad2…ad9e`.
- **Task/evidence/model/evaluator equality:** not established.
- **Assessor separation:** not established for a paired comparison.
- **Direct-arm source openings:** absent.
- **Regressions:** false Claude `#reference-frame-laws` residual.
- **Negative comparison results:** none retained because no comparison occurred.
- **REQ-P-DOGFOOD-008 verdict:** not produced; `indeterminate`.

This Worker began map-first and inspected retained outputs. It therefore cannot retroactively act as an uncontaminated equal-initial-context direct-prose arm.

## Release claims

| Claim | Result |
|---|---|
| `STDO-REP-0.1-C01` | `satisfied` — source-linked program and exact deterministic map reproduced. |
| `STDO-REP-0.1-C02` | `satisfied` — five explicit residuals, resolving source routes, and honest mechanical limits. |
| `STDO-REP-0.1-C03` | `satisfied` — one canonical skill resolves through both exact relative symlinks. |
| `STDO-REP-0.1-C04` | `satisfied` at its narrow claim — LLM owns frame/row choices; external Axiom owns pure joining; no local engine. |
| `STDO-REP-0.1-C05` | `satisfied` at its literal bounded scope — retained evidence demonstrates pickup, visible frame details, bounded re-entry, and reproducible joining. It does not establish comparative usefulness or readiness. |

The release claims do not exhaust the accepted requirements; their narrow satisfaction does not cure the Native and Dogfood frame failures.

## Semantic recovery

Recovered without material contradiction:

- `a_c`, `a_c.X`, and `a_c.X.C` are distinct; this is only an `a_c.text` working surface.
- Mechanical structural success is not semantic fidelity or acceptance.
- WHAT governs HOW through the specification chain.
- Frames require exact subject/basis, finite evidence, authority conservation, closed results, invalidation, and re-entry.
- Worker and Reviewer results return to Executive without self-promotion, repair, disposition, or continuation authority.
- Candidate construction, publication, exact-cut qualification, acceptance, and consumer adoption are distinct.
- The genesis disposition is project-specific and explicit.
- Compressions and maps are read models; exact raw owners remain deciding.
- Overlay/schema validity is structural and does not create semantic decisions or authority.
- Dogfood comparison requires genuine independence and arm equality.

Useful residuals: all five. No material semantic omission was found in the bounded map sample; detailed release sequencing, project genesis, native law, and dogfood equality correctly required bounded re-entry into their owners.

False confidence observed: zero-diagnostic validation did not expose the native-instruction omissions, release-status wording, false Claude route residual, or missing dogfood comparison.

## Source re-entry log

| Exact URI or project route | Purpose and recovered/challenged meaning | Necessary |
|---|---|---|
| `stdo://…/authority_compressions/stdo_bootstrap.md#stdo-discovery-bootstrap` | Unique Product Definition and immutable-basis resolution. | Yes |
| `stdo://…/AXIOMATIC_CALCULUS.md#position`, `#core-signature`, `#ac-018-structural-and-semantic-separation`, `#subject-and-carrier-boundaries`, `#application-boundary` | Layer separation, full-`M_b` boundary, mechanical/semantic separation, downstream authority. | Yes |
| `stdo://…/SPEC_METHOD.md#stdo-product-definition-overlay-and-layout-independence`, `#local-constitutional-binding`, `#collective-reference-frame-basis`, `#constitutional-chain`, `#semantic-evidence-and-projection-separation-stdo-up-008` | Overlay structural limits, authority flow, frame-basis admission, semantic/evidence separation. | Yes |
| `stdo://…/REFERENCE_FRAME_METHOD.md#reference-frame-laws`, `#engagement`, `#using-frames-in-conjunction`, `#minimal-evaluation-result` | Exact frame law, ordered closed results, and conjunction rules. | Yes |
| `stdo://…/STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary`, `#derived-worker-frame`, `#derived-reviewer-frame`, `#complete-engagement-transition`, `#missing-frame-and-re-entry-application`, `#actor-binding-and-independence` | Role, return, no-repair, independence, and re-entry boundaries. | Yes |
| `stdo://…/RELEASE_METHOD.md#immutable-rc-publication`, `#exact-cut-qualification`, `#monotonic-version-line-advancement`, `#product-subject-and-repository-carrier`, `#successor-baseline-conservation-stdo-up-015` | Candidate/publication/exact-cut sequencing and predecessor law. | Yes |
| `stdo://…/README.md#standards-library` | Complete immutable cut as the method basis. | Yes |
| `stdo://…/authority_compressions/README.md#authority-compression-assets` and `stdo_compressed.md#re-entry-compression` | Compression is a read model and raw-source re-entry remains required. | Yes |
| `stdo://…/templates/README.md#product-definition-overlay` | Templates/placeholders and schema validation do not create decisions. | Yes |
| `repo://stdo-representation/specification/REFERENCE_FRAME_BASIS.md` plus exact decision and overlay | Accepted revision-11 activation, ordered frame interactions, and K-DOGFOOD law. | Yes |
| `repo://stdo-representation/specification/PRODUCT.md` and five active requirement files | Thin purpose, native contract, dogfood equality, exclusions, and current unreleased status. | Yes |
| `repo://stdo-representation/releases/v0.1.0.md` | Frozen inventory, claims, genesis disposition, and candidate/publication boundary. | Yes |

The validator mechanically resolved and hashed all 62 declared Source STDO URIs; that was URI/digest verification, not semantic reliance on the full corpus. Semantic reading remained bounded to the routes above.

## Unnecessary expansion

No unrelated Source STDO standard was semantically loaded. One broad text search against the minified map expanded its entire single JSON line in command output; it added no evidence and was not relied upon.

## Checks and exact outputs

- `stdo status --definition stdo_representation.json --verify`: `failures: []`, `valid: true`.
- `stdo verify v2.5.0-rc.1 --manifest-sha256 3cd24…d338`: `failures: []`, `valid: true`.
- Independent SHA-256 verification of all stated authority and candidate files: all matched.
- Independent candidate inventory reconstruction: `710596…e779`.
- Axiom tag/commit/tree and seven-member dependency inventory: all matched.
- Exact validator: `status: valid`, diagnostics `[]`, counts `14/51/5`.
- Exact in-memory instantiation: candidate map byte comparison exit `0`.
- Falsifiers all refused:
  - malformed shape → `missing_field`;
  - duplicate set → `duplicate_ref`/`noncanonical_order`;
  - unsorted set → `noncanonical_order`;
  - dangling ref → `dangling_ref`;
  - unresolved route → `unresolved_fragment`;
  - ungrounded item → `empty_set`;
  - broken residual re-entry → `unresolved_fragment`.
- Exact join reproduction: byte comparison exit `0`; digest `43cad2…ad9e`.
- Reversed rows produced different digest `bdb84c…5c83`.
- Malformed join input exited `2`, `join_error:invalid_sections`.
- Symlink discovery comparisons: both exit `0`.
- Source coverage: manifest `51`, grounded `51`, missing `[]`, extra `[]`.
- Remote observation: no matching `v0.1.0*`, `rc/0.1.0`, or `release/0.1.0` refs returned.

## Remaining uncertainty and invalidation

Activation: Worker, read-only, 2026-08-31T01:10:12+10:00. The exact provider model revision and reasoning configuration were not independently attested. No candidate authorship or repair was performed.

This result is invalidated by any change to the inventory, candidate bytes, authority files, revision-11 decision/overlay, Source STDO or Axiom identities, dogfood arm records, actor separation, or evidence population.

Smallest owning re-entry:

1. the Product/native-instruction authority for the exact `REQ-P-NATIVE-*` mismatch and release-status wording; and
2. a separately activated `K-DOGFOOD` relation with frozen equal arms and an uncontaminated assessor.

## Closed return

**`refused`**

Reason: the frozen candidate has a material native-contract falsifier, and the mandatory dogfood comparison remains indeterminate. The candidate is not `candidate_ready`. No Product acceptance, publication authority, release disposition, or next-work authority is claimed.