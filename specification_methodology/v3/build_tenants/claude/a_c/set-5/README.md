# a_c interpretation of the twenty-three-member set (Claude tenant, set-5)

Status: the successor of [set-4/](../set-4/README.md), derived over the
standards at commit `3824752` on `tenant/claude/c3-v3` by the W22 Writer
activation. It is a partial encoding. It adds what nine F-03 task frames
and one candidate bootstrap frame need from TICKETS, RELEASE, IDENTITY,
DESIGN_MODULE, ODD, TRAVERSAL_OCCURRENCE, UX, WORLD_MODEL, GLOSSARY and
PRODUCT_DEFINITION, rewrites two set-4 rows and one symbol label whose
source text the sweep restated, and disposes one set-4 residual that the
sweep discharged. The program validates with zero diagnostics against the
byte-verified pinned Axiom Indexer subject. Ten frames are projected, each
under the Executive's 100,000-byte limit. No author-independent fidelity
judgment of this program exists, nothing here is accepted, and set-4/ is
frozen history that this derivation did not edit.

## Frozen subject

The twenty-three Markdown members under `standards/` at `3824752`,
identified by digest. `git status --porcelain -- standards/` was empty at
derivation time, and the working-tree bytes equal the commit's.

<!-- subject -->
| File | SHA-256 |
|---|---|
| `standards/ACTIVATION.md` | `0f54587b2f1e1d483dd95a0d0144ebeee1196953830684ceb499b52a7ef085d8` |
| `standards/ASSURANCE.md` | `6821ef04c1584dcdeb1bbe4dc62b07eb35807b856ced9c26f730ced27aed85e8` |
| `standards/AXIOMATIC_CALCULUS.md` | `5daa991d3fa18498bf93e495b1d8e45c2157ae762efa05cfe4473adecc66c763` |
| `standards/CONFORMANCE.md` | `be1b88f98e24f3d9c655948191f5cd87d28e7941f0a4bb8028010004eef1dd05` |
| `standards/DESIGN_MODULE.md` | `660d108a5cd15582c75df66a664d34cf4a2286ee5bb78fef1304f3d7005a61f0` |
| `standards/EVALUATION.md` | `bea4a6372ebc7cf2ba7b6dcf42396d0a8f521a8abf48e8fc239dccfb32632375` |
| `standards/EXECUTIVE_BASELINE.md` | `478acc9c681b339384d7ae411190cea928fb323246f9eba590cf99893a344476` |
| `standards/FOUNDATIONS.md` | `f8873279f0bd15645e24e5d83e64eec4994ee42167deeb03594d8fdadfd09f66` |
| `standards/GLOSSARY.md` | `d75740a492756535851b99e8e2b1b269e733ef6fc8336128fa1160c2d8b00e44` |
| `standards/IDENTITY.md` | `03150e390768bf92d7bc66068ffad9ecfb3acce69e5188552316d2e049027f53` |
| `standards/ODD.md` | `5e40d354ed3631a08e6d71dba28d45df45a64cc156a67222b1f2d37690756a44` |
| `standards/POSTING_GUIDE.md` | `e784c72ab18d3386d4aa28f9eed43aef675d01f1a03ec8ec2bcc440f33edfb86` |
| `standards/PRODUCT_DEFINITION.md` | `87ea972972051f0e2694010e257635faf9bf0210f990fc96c5e45e573e18ae5f` |
| `standards/PROFILES.md` | `3b01313b54fb27d4ac4530636ed285e86afa7d6b53eae5b5f166fc920214323b` |
| `standards/README.md` | `79cb0f1c9ab9c54edcfb5e7bc344ca9af6507b412274e39f1879258b6b9fa6a4` |
| `standards/REFERENCE_FRAME.md` | `ef9a6a62d2b949a448d8c6bdd0c28bae7c33548fa2febf12e50f39cbb99f9495` |
| `standards/RELEASE.md` | `3d442f9eaffb4019447892ff9e46862eb63ebd312da2e4baa26e42a5fba8a886` |
| `standards/SPEC_METHOD.md` | `a4a90622a23d325985b0d9a2dca2e97681cb2ce0ea936a45fd1a1cb1ab4a6946` |
| `standards/TICKETS.md` | `adf2044f52ba26f6cfe44f3bc785657ed414c1b99e3d8b9185f9c9bb3dd0b4ec` |
| `standards/TRAVERSAL_OCCURRENCE.md` | `b37b7828709f614d155803cce560183e25e6225c204a129e6b704c373c20f616` |
| `standards/UX.md` | `0adbf491693217466252176c87f4e454fc2617080d8e27136e1f0859a5347d55` |
| `standards/WORLD_MODEL.md` | `0d7400f26134371da6cc51642f01074775ada6bb1a01e057d95aff43b7f9327b` |
| `standards/WRITING_GUIDE.md` | `d4c647a8d7ce59521069d1d311f2fa59f86cdc79bb01dd919a8f9bf57aba6106` |
<!-- /subject -->

The validation report records 210 resolved sources over 22 files: 209
tenant sources over 21 members, each carrying one of the digests above,
and one rc.2 source, the calculus. POSTING_GUIDE and WRITING_GUIDE are cited by no record.

## Mechanical subject

Unchanged from set-4: tag `refs/tags/axiom_indexer/v2.5.1-rc.2` (tag
object `9bff233c…`, commit `9a9c4797…`). `build_tenants/core/code/ac.py`
was read from that tag with `git show`; its SHA-256,
`5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8`, matches
the value set-4 recorded against the release record. It was invoked from a
scratch copy with `python3 -I`. `calculus_ref` stays
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; moving it is
not this Writer's decision.

## Artifacts

<!-- artifacts -->
| File | SHA-256 | Role |
|---|---|---|
| `axiomatic-program.json` | `b66563e4402f33f44278641fc50a78251b5cba4d647c42c9def1b78cb4655602` | the authored a_c.text program `urn:stdo-3:claude:program:a-c-text:set-5`; canonical program digest `sha256:b12b31216456f375c2a2e24aefbd16c897d92c1a7b469b50c52ee89b450e4a42` |
| `logical-constraint-map.json` | `278d7c2dee4ebb4a9e75de347365ed2f17118dbdaea8767567ac83fa14566762` | deterministic index over the program; intrinsic digest `sha256:64e1240a662f7da6f2ed42b1a9897fd628a4086809e58c8751f6c11512459f9f` |
| `validation-report.json` | `a34f6dfa8f16a2beb750420c6dcd7496f5bb209e9e96f75eb9f6f4836ffa746e` | status `valid`, zero diagnostics; 301 symbols, 417 clauses, 6 residuals; 210 resolved sources |
| `projection-carrier-retention-materialized.json` | `16bc90d75e969e44e238f1dc13059c7b3aabbe5247ae3e442e8da0f00e78c4eb` | frame `carrier-retention`, materialized; projection digest `sha256:1bd16441891284ce6c8f27613e71805a3584ee41de7b16c1f20d9f61b366381c` |
| `projection-carrier-retention-reference-only.json` | `f13a6a88c6f87a7906431ca6eadd081a0e03ba3425498258862f24750eab148e` | the same frame, reference-only; `sha256:76898aa7b75af32e67a61b44f75003404f2e8150b6291273a8dbd0a1d47c056a` |
| `projection-release-and-successor-materialized.json` | `42a33da6a01e9c8740fcc420cb75cda2875a4706ce304037ce97507cad9acbf4` | frame `release-and-successor`, materialized; projection digest `sha256:84135246bb4af996928c42c2a8082ec94f283548b4bc7c712557592891df36ab` |
| `projection-release-and-successor-reference-only.json` | `9990d6f0598867eaa060e82a211666f55733c257d9073ba1326742276ab2c625` | the same frame, reference-only; `sha256:5c2c2bde0d00fb7306b0961106066e5cbf971cd00a6e61b66b1a358fa2b57bc6` |
| `projection-identity-scoped-materialized.json` | `2148de3efe8ab0f838faf8e53df05b25f43949078e47d3bec4a2552fa61077c1` | frame `identity-scoped`, materialized; projection digest `sha256:327f3ef86669bd9b8969ebe2ca9262aff5ef3d5dec19f954683c877a9965e1b5` |
| `projection-identity-scoped-reference-only.json` | `d6bb0ea5ee9dfb1d9b78f40310d8dfd7a63366185170cf3e5ac331d43df02bc7` | the same frame, reference-only; `sha256:7bde224263f623c5f56a3d3d6d0619bb1e07dbda15e0b87fd7844bfa43ee6573` |
| `projection-design-gate-materialized.json` | `82bbd09ca1b4922f543d4328c4c33fdeafc03dd0b643494c0c21d4317251c663` | frame `design-gate`, materialized; projection digest `sha256:0a5902493c1470bedb9145cc8dfddbd75632a48b730f2e94bc0f26fb53e7bc91` |
| `projection-design-gate-reference-only.json` | `8eeec347eb7e90115dbd4834e1b51feab05d2ae151fd3ce06a209510b9bb2ef5` | the same frame, reference-only; `sha256:2f75e28b16bfeb7529d1707aa08a5eeb9294e00560c6f6eb2fc117486e13f7de` |
| `projection-odd-closure-materialized.json` | `ec44026052563a4ce951051048cec44ecf35af8908b13e0e999f07089e5e2ea2` | frame `odd-closure`, materialized; projection digest `sha256:bb274399a1d1eeb3724d96817e20ff82ac7ca24168314e3897857c5ffaffb5ea` |
| `projection-odd-closure-reference-only.json` | `0b6eafbdd63b814e1198a0fd95198de90c6a220210d53923c1098b323e9c5196` | the same frame, reference-only; `sha256:03ed095dc51e05a00f8eecb3c8c89e100a92fdcc9260a48db9db6d532e83020c` |
| `projection-traversal-lineage-materialized.json` | `6c017de3956ed9ff2bd9ff1a82dfe872ebe656f3ceb9665ad9bd5345164d788a` | frame `traversal-lineage`, materialized; projection digest `sha256:673bf3a01d907e688921720d4223a762df5ca34788c73bdaef21acd2cd0b0e98` |
| `projection-traversal-lineage-reference-only.json` | `0d2b2cb36f89c233f6956d08b53c1b9529f032ef7d10bceabe92f5af8de1086b` | the same frame, reference-only; `sha256:a3041ab3df0f85485e17a1d97757159516b79c4d9b920084c4a13133bdf7220e` |
| `projection-ux-replay-materialized.json` | `c923a607c7faea6bbfeb993270a7524988ef83d8e9abd8167c0d639b0730f69f` | frame `ux-replay`, materialized; projection digest `sha256:121172474f7f0e0388dd1a1c936e428fe097eecf71cbaa3d5ab8a32bf12324cd` |
| `projection-ux-replay-reference-only.json` | `34c050228b7f9b5b51bdb9e6913535b1f7e52a644f6e4432db9547d298b0f3e9` | the same frame, reference-only; `sha256:05795790d329e9927dae10bc6ad39811b97887c4ef7a1d36b03cad38690ab510` |
| `projection-world-model-cut-materialized.json` | `b85f70562d366be3eaed846d21b49ee30751f3c085497ba96e7a956df674d9e7` | frame `world-model-cut`, materialized; projection digest `sha256:be03b85c618c13d1da1d95026493a01ef37049dac3fbc513cce90daccbfdbfa7` |
| `projection-world-model-cut-reference-only.json` | `adb401d0727862cd941703dd718b79b42752ceb4baeed138439e6162878af847` | the same frame, reference-only; `sha256:0468393a9ed1eca168324d62dacd490c28e2f9292d77b56c3a63b3310eb164b7` |
| `projection-bind-and-resolve-materialized.json` | `871c6d663f666cdf5ba2a6114ac815bbc4ac24b3ea985caf4203892aedc9ffda` | frame `bind-and-resolve`, materialized; projection digest `sha256:2c4c7cf436a66047978b741fa39af1a62259c321776c57fdaf8d5c17bcd2fe11` |
| `projection-bind-and-resolve-reference-only.json` | `983c8d98a2858186f39304ad27d86a76704aff330d3058188df8fd5f13022d28` | the same frame, reference-only; `sha256:d460d6f4290ba9fc92a083613908273688469cac479d0ccf571cb2bf92bb17ff` |
| `projection-bootstrap-materialized.json` | `d69e175d44ccb9bc1111d4472de4ecd92f32d85a5854547a289543a8c702a1aa` | frame `bootstrap`, materialized; projection digest `sha256:ca4a63515f96d3f18c723451155087df10fb86a4629be8466b9ef59f12594055` |
| `projection-bootstrap-reference-only.json` | `5d395703e033f92d673f579b8e948712cb045a4493c5a1670d786176bc06fcb4` | the same frame, reference-only; `sha256:d95f27ce5412fcb8d78cb9509be7c6ca27782af55de385cb97ee0a00ca89091b` |
| `bindings.json` | `816d211c2a92c3e3d2e8adc13d07fb1ae5ecc9fb8b8b4ba593b6f7f6009e201f` | byte-identical to set-4's |
<!-- /artifacts -->

## Frames

Each frame was projected from its own frame index and measured with the
file size after projection, before any actor read it. The limit is
100,000 bytes materialized. All ten frames are under it, met by selecting
clauses, never by truncating them. Each frame's clause list is the
projection's `closure.clauses`: the index roots plus what their support
references pull in transitively.

| Frame | Task | Materialized bytes | SHA-256 (materialized file) | Reference-only bytes | Closure (symbols, clauses, residuals) | Under limit |
|---|---|---|---|---|---|---|
| `carrier-retention` | A | 55,905 | `16bc90d75e96…` | 29,890 | 14, 17, 0 | yes |
| `release-and-successor` | B | 62,813 | `42a33da6a01e…` | 33,862 | 14, 12, 0 | yes |
| `identity-scoped` | C | 37,612 | `2148de3efe8a…` | 20,684 | 11, 11, 0 | yes |
| `design-gate` | D | 83,252 | `82bbd09ca1b4…` | 43,284 | 24, 19, 2 | yes |
| `odd-closure` | E | 47,936 | `ec4402605256…` | 24,800 | 18, 11, 0 | yes |
| `traversal-lineage` | F | 62,598 | `6c017de3956e…` | 33,417 | 21, 15, 0 | yes |
| `ux-replay` | G | 46,256 | `c923a607c7fa…` | 24,994 | 12, 11, 0 | yes |
| `world-model-cut` | H | 38,558 | `b85f70562d36…` | 21,184 | 10, 10, 0 | yes |
| `bind-and-resolve` | I | 53,088 | `871c6d663f66…` | 28,458 | 10, 11, 0 | yes |
| `bootstrap` | none (candidate) | 9,571 | `d69e175d44cc…` | 6,073 | 1, 3, 0 | yes |

`carrier-retention` (frame ref TICKETS `#execution-contract-admission`;
F-03 task A, re-running the gap of F-02 task C). 17 clauses. Roots: the
set-4 TICKETS §5 rows carrier-selection-takes-the-first-matching-row,
ticket-shaped-creates-no-ticket,
absence-of-a-ticket-neither-requires-nor-authorises-one,
carrier-assertion-is-not-admission-evidence,
surviving-obligation-is-carried-when-admission-fails (the
obligation-retention order: sprint-local entry; otherwise a durable ticket
only under ticket-state authority; where that authority is absent, the
contract's named durable result and evidence surface or an
already-authorised enclosing carrier, closure marked withheld, re-entry
returned), carrier-is-an-admission-candidate-never-truth,
admission-never-admits-a-growth-basis,
execution-contract-is-the-run-scoped-admitted-surface,
execution-contract-loop-admits-before-execution; the ACTIVATION §1
Admission rows drafting-and-admission-are-distinct (rewritten),
drafting-actor-never-infers-admission,
execution-begins-only-after-admission,
admitted-result-identifies-mechanism-contract-decision-and-evidence,
admitted-contract-names-a-durable-result-surface; the SPEC_METHOD §3 row
authority-for-growth-derives-from-outcome; and one new TICKETS §1 row,
goals-are-not-the-durable-unit-of-execution-tracking. Pulled in by
support: authority-is-never-minted. Compared with set-4's
`carrier-and-admission`, this frame drops
carrier-is-selected-by-proportionality (SPEC_METHOD Carriers), whose
support closure pulled in the proportionality clauses and two residuals,
and it no longer carries the conflict residual, which is disposed. The
F-02 C-001 actor asked whether a goals outcome is upstream work authority
and whether it may write a record before admission; the frame now carries
the goals row and the growth-authority row for the first question, and
the second is answered only as far as the retention order states it.

`release-and-successor` (frame ref RELEASE `#3-phases`; task B). 12 new
clauses: release-identities-are-distinct,
release-refs-are-project-qualified, release-cut-binds-its-project-subtree,
release-historical-refs-and-public-uris-are-conserved,
release-has-three-phases-and-no-second-final-cut,
release-mutable-candidate-is-non-operative,
release-rc-publication-creates-one-immutable-subject,
release-exact-cut-qualification-binds-the-cut,
release-selector-advances-strictly-monotonically,
release-selector-never-selects-a-consumer-basis,
release-adoption-presents-a-plan-before-mutation,
release-successor-disposes-every-predecessor-claim. No support
references: §3 and §9 cite EVALUATION §1 and FOUNDATIONS §1 as the generic
or applying law, which the qualification literals name.

`identity-scoped` (frame ref IDENTITY `#scoped-identity`; task C). 9 new
clauses: identity-is-authority-kind-value,
identity-is-unique-within-its-lawful-scope,
identity-kinds-are-not-collapsed, identity-change-is-an-explicit-relation,
engine-and-domain-own-different-identities,
authority-is-an-identity-bearing-relation,
carriers-never-widen-authority,
proxy-identity-stays-distinct-from-human-authority,
recorded-decision-preserves-its-coordinates. Pulled in by support (the
source cites FOUNDATIONS §2 Object and Authority):
identity-survives-admissible-change, authority-is-never-minted.

`design-gate` (frame ref DESIGN_MODULE
`#7-ontology-and-three-view-design-gate`; task D). 12 new clauses:
design-decision-complete-is-the-gate-criterion,
design-projections-do-not-establish-decision-completeness,
design-sequencing-follows-decision-completeness,
design-sequencing-mode-is-selected-by-proportionality,
design-implementation-is-evidence-not-semantic-authority,
design-hidden-ambiguity-switches-to-gated-sequencing,
design-substrate-must-natively-construct-the-design (UP-002),
design-prime-contracts-the-whole-family-and-conserves-the-root (UP-003),
design-gate-carries-ontology-and-three-view-asset,
design-gate-verdicts-accepted-before-promotion,
design-unchanged-refactor-gate-reuses-the-verdict,
design-pre-gate-implementation-is-provisional. Pulled in by support
(ACTIVATION §6, SPEC_METHOD §4, FOUNDATIONS §4 and ACTIVATION §7 are cited
by the source): proportionality-definition, change-classes-and-re-entry-points,
transformation-records-accounting,
closed-result-reused-after-applicability-check,
obligation-without-route-is-unjustified, p2-statement,
substantive-change-starts-with-triage. The proportionality symbols carry
in the residuals derivation-chain-cost-per-boundary and
independence-arguments-are-one-sentence.

`odd-closure` (frame ref ODD `#115d-constructive-evaluation-and-yield-loop`;
task E). 6 new clauses: odd-closure-decision-is-a-closed-sum-type (A8,
A11), odd-closure-decisions-map-to-core (the seven-row A8 table with the
cause read from the reason refs), odd-yield-is-lawful-iterate-not-failure
(A9, A10), odd-cumulative-environment-law (11.8),
odd-negative-proof-exercises-the-real-authority-path and
odd-supported-path-has-no-rival-controller (11.7B, STDO-UP-010). Pulled in
by support (ACTIVATION §3, §3 Disposition and §4):
construction-availability-maps-to-core,
disposition-consumes-a-core-result, reconfiguration-follows-the-cause,
refinements-map-totally-to-core, diagnostic-order-is-eight-questions-in-order.

`traversal-lineage` (frame ref TRAVERSAL_OCCURRENCE
`#causality-and-typed-lineage`; task F). 13 new clauses:
causal-families-stay-distinct-and-cause-is-admitted,
typed-lineage-cycle-is-judged-per-causal-subgraph,
lineage-relation-kinds-are-typed (the seven lineage rows only),
op-001-seed-acyclicity to op-007-scope-conservation,
traversal-stop-kinds-and-constraint-results,
traversal-stops-and-decisions-map-to-core,
structural-refusal-and-partial-effect-losses. Pulled in by support:
construction-availability-maps-to-core, refinements-map-totally-to-core.
profile-binding-is-declared (PROFILES §1) was left out as a support
because it would carry the residual rc2-routes-are-outside-program-basis.

`ux-replay` (frame ref UX `#8-continuation-and-replay`; task G). 10 new
clauses: ux-process-model-is-the-elm-architecture,
ux-stack-is-free-and-the-model-is-not, ux-effects-only-at-the-membrane,
ux-membrane-interprets-one-declared-cmd,
ux-view-does-not-own-continuation, ux-msg-replay-proof-before-closure,
ux-adoption-declares-the-surface-contract,
ux-surface-is-governed-by-default,
ux-scaffold-exemption-is-recorded-and-bounded,
ux-profile-verdicts-map-to-core (all seven §15 rows). Pulled in by
support: refinements-map-totally-to-core. The stack-free clause carries
both compliance readings the source states, since UX §15 leaves the
stricter one to a pending ruling.

`world-model-cut` (frame ref WORLD_MODEL `#9-entity-cut-construction`;
task H). 9 new clauses: entity-cuts-are-recovered-not-invented,
entity-cut-admissibility-test, explicit-admits-three-lawful-surface-values,
sparse-first-publication-is-lawful,
entity-cut-carries-its-own-discrimination,
published-cut-is-traceable-and-immutable,
attribute-ledger-is-the-immediate-source-of-a-cut,
saturation-forbids-silent-unsupported-attributes (§11 Saturation law,
added because the §14 saturated row depends on it),
world-model-verdicts-map-to-core (all eleven §14 rows). Pulled in by
support: refinements-map-totally-to-core.

`bind-and-resolve` (frame ref PRODUCT_DEFINITION
`#5-bounded-context-semantic-resolution`; task I). 11 new clauses:
product-definition-carries-the-required-relations,
product-definition-locates-and-never-restates-source-truth,
product-definition-bounded-context-is-enclosing-not-a-registry,
term-context-and-concept-reference-are-distinct,
bounded-context-exists-only-by-owner-declaration,
term-occurrence-resolves-under-its-semantic-address (the five ordered
steps), zero-or-several-concepts-fail-closed,
glossary-locates-and-never-decides,
cross-context-relation-is-explicit-and-owner-authorised,
four-cross-context-relation-kinds-are-distinct,
semantic-resolution-minimum-conformance-cases. No support references:
the source cites AC-012, which no set encodes.

## Candidate bootstrap frame

`bootstrap` (frame ref PRODUCT_DEFINITION `#12-bootstrap`) is not a task
frame. It is the smallest frame found that routes a fresh agent from a
product definition to its exact basis and the members it must load first:
9,571 bytes materialized (6,073 reference-only), one symbol and three
clauses, no residuals. A four-clause version with a separate
never-override clause and a second symbol measured 13,422 and then 10,902
bytes; the limit was met by merging the never-override sentence into the
routes clause, shortening the URIs and using one symbol. Clauses:
bootstrap-routes (PRODUCT_DEFINITION §4 "routes ... can neither restate
nor override them", and the README Routes order for binding a project,
doing bounded work and resolving a term), bootstrap-discovery
(PRODUCT_DEFINITION §4 pruning law and §9 recursive discovery without
nesting inheritance), bootstrap-basis (PRODUCT_DEFINITION §4 and §12: the
exact basis URI and manifest digest as the sole authored selection, sync
versus adopt, no proximity selection).

Coverage of rc.2 `standards/authority_compressions/stdo_bootstrap.md`
(5.8 KB), claim by claim:

| rc.2 bootstrap claim | In the candidate frame |
|---|---|
| 1. discover `stdo_<label>.json` recursively; the prune list; refuse symlinked definitions; nesting creates no inheritance or composition | carried, except the prune list itself, which is named by reference to PRODUCT_DEFINITION §4 |
| 2. select exactly one applicable definition; zero or several fail closed | not carried; no tenant locus was found for the selection rule (PRODUCT_DEFINITION §9 fails closed on an identity mismatch, not on plural definitions) |
| 3. the basis URI and manifest digest are the sole operative selection; source and selector are discovery inputs | carried |
| 4. sync and verify through the toolchain manager; no mutable source, other cut, alias, cache or proximity copy | carried in part: sync, adopt and proximity; the other named substitutes are not listed |
| 5. resolve the declared bootstrap entrypoint; load raw standards when the projection is insufficient or stale | carried in part: route-not-override; the entrypoint resolution and the stale-digest rule are not |
| 6. reference-frame basis, direct versus Executive entry, smallest frontier, unknown applicability unresolved, role grants no effects, Executive performs no mutation, event-driven attention | not carried; the routes clause sends bounded work to ACTIVATION §1-3 and REFERENCE_FRAME §11 only |
| 7. load WHAT, HOW, carriers only as required; a summary or prior result routes but never replaces source authority; the end-to-end interface frame | carried in part: route-not-override; the rest is not |
| 8. reuse computed facts, judgments and rulings by route; refresh on invalidation; closure by condition | not carried |
| derived guidance preserves permissions; retirement default | not carried |
| sync, adopt dry-run, plan digest, selector alone never changes a consumer | carried in part: sync never consults the selector; adopt only with the exact plan digest |
| bootstrap targets relative to the source project; fleet confinement; marker spans | not carried |

The frame carries the discovery and selection spine (claims 1, 3 and
part of 4) and a member route, and leaves the coordination, reuse and
fleet claims to the members the route names. Whether a bootstrap frame
of this size is wanted, and what it must carry, is Jim's pending ruling.

## Changes between set-4 and set-5

Counts: symbols 236 to 301 (65 added, one label rewritten), clauses 331
to 417 (86 added, two rewritten in place), residuals 7 to 6 (one
disposed, none added), frame indexes 11 to 21, frame refs 11 to 21.
Nothing else was retired.

### Sweep check

Validating set-4's program unchanged against `3824752` gave zero
diagnostics: no anchor moved, so no row needed re-anchoring. Validation
does not show whether the text under an anchor changed, so the diff from
`978d324` to `3824752` was mapped to headings. 193 set-4 records (clauses
and symbols) anchor at a heading whose span holds a changed line:
FOUNDATIONS 85, ACTIVATION 42, EVALUATION 22, SPEC_METHOD 17, PROFILES
15, REFERENCE_FRAME 7, README 6, EXECUTIVE_BASELINE 1. Broad headings
such as FOUNDATIONS `#2-ontology` count every row under them. Of these,
the rows that land in a set-5 frame closure were read against the
current text: the five ACTIVATION §1 Admission rows, authority-is-never-minted,
identity-survives-admissible-change, obligation-without-route-is-unjustified,
p2-statement, proportionality-definition, reconfiguration-follows-the-cause,
substantive-change-starts-with-triage. One of them was stale and is
rewritten; the others still state the current text. The remaining set-4
records under changed headings were not re-derived, and their fidelity to
the swept text is unknown.

### Rewritten in place

- `clause:drafting-and-admission-are-distinct` (ACTIVATION `#admission`):
  the swept ACTIVATION §1 states that a contract "carries at minimum the
  states drafted, admitted, rejected and superseded" and cites TICKETS §5.
  The literal, statement and qualification now say so, and the clause
  cites TICKETS `#execution-contract-admission` as well.
- `symbol:contract-state`: label "at minimum drafted, admitted, rejected
  and superseded", with the same added source.
- `clause:faithful-refinement-definition` (ACTIVATION
  `#4-totality-and-refinement`): the sweep restated refinement over the
  cumulative input (the outer input retained for every step, with the
  earlier outputs retained up to that step; the chained reading is the
  special case). The literal and statement now carry that reading. The
  clause is in no set-5 frame.

### Disposed

- `residual:contract-state-set-closed-or-minimum` (kind `conflict`) is
  removed. Its conflict was ACTIVATION §1's closed set of four contract
  states against TICKETS §5's minimum; the swept ACTIVATION §1 states the
  minimum and cites TICKETS §5, so the two members no longer disagree.
  This record is its disposition.

### Added

65 symbols and 86 clauses, listed by frame above, plus ten frame indexes
and ten frame refs. Each new clause cites the section it encodes and names
its principles or UP tags in a qualification literal. A new clause carries
a support reference only where its source cites the supported law and an
encoded clause states it. The core-mapping clauses
(odd-closure-decisions-map-to-core, traversal-stops-and-decisions-map-to-core,
ux-profile-verdicts-map-to-core, world-model-verdicts-map-to-core) use the
`maps-to` operator with the core result members as targets.

## What is and is not encoded

| Member | Encoded in set-5 (added) | Not encoded |
|---|---|---|
| TICKETS | §1 Goals; the §5 carrier and retention rows carried from set-4 | §1 ticket records, sprints, comments, milestones; §2; §3; §4 beyond set-4; §5 evaluation criteria and term binding; §6 to §10 |
| ACTIVATION | §1 Admission state set and §4 refinement rewritten | the other swept text, as in set-4 |
| RELEASE | §2 identities, project-qualified refs, subtree identity, historical ref conservation; §3 all four phases; §4; §9 (STDO-UP-015) | §1, §5 to §8, §10, §11 |
| IDENTITY | §2 scoped identity, uniqueness, type, stability; §5; §6 (STDO-UP-004) | §1, §3, §4, §7 to §13 |
| DESIGN_MODULE | §5 Proportional design sequencing, Decision-complete symbolic design, Native constructability (UP-002), Recursive Prime and root conservation (UP-003); §7 lead and Gate and retrospective work | §1 to §4; the rest of §5 and §7 (Ontology evidence, three views, cross-view axioms, UP-018, UP-019); §6; §8 to §13 |
| ODD | 11.5D A8 to A11; 11.7B (STDO-UP-010); 11.8 | §1 to §10; 11.1 to 11.5C; 11.5D A1 to A7, A12, A13; 11.6, 11.7, 11.7A, 11.9; §12 to §21 |
| TRAVERSAL_OCCURRENCE | causality and typed lineage; OP-001 to OP-007; the stop kinds, the stop and decision mapping to the core; the lineage rows of the relation families | semantic-object sorts and reference domain; event-kind population; other relation rows; judgment kinds; occurrence identity beyond OP-001; effect relation beyond OP-005 and OP-006; frontier and projection; authority and adoption; profile signature; exclusions; conformance obligations |
| UX | §4 with stack mandate and realisation discretion; §6; §8 with the Msg-replay proof; §12 adoption list and Scaffold and exemption; §15 | §1 to §3, §5, §7, §9 to §11, §12 sprint escrow, §13, §14, §16 |
| WORLD_MODEL | §8 Attribute ledger law; §9 all four parts; §11 Saturation law; §14 | §1 to §7; §8 other laws; §10 (only its mapping rows); §11 composition and projection; §12, §13, §15 |
| GLOSSARY | §1 Index contract; §2 Locator law | the index tables §3 to §15; §16 |
| PRODUCT_DEFINITION | §2; §4 basis selection, pruning and the bootstrap-route sentence; §5; §6 disambiguation binding; §9 discovery; §10; §12 basis and proximity sentences | §1; §3; §4 manager functions, plans and hashing beyond the above; §7; §8; §9 composition entry fields; §11; §12 scaffold and sequence; §13 |
| README | Routes (bootstrap only) | the rest |

ASSURANCE §14 to §16, EXECUTIVE_BASELINE, AXIOMATIC_CALCULUS, PROFILES
§6, POSTING_GUIDE and WRITING_GUIDE gained nothing in set-5. As before,
the source-dispositions tables of every member are not encoded.

## What validation proves

Validation proves structure, URI resolution, reference closure, the
grounding of every anchor in a heading of the resolved file, and the
canonical digest. It does not prove that the clauses are faithful to the
documents, complete or uniquely interpreted; that judgment is
author-independent and source-first, and none has been made. The program
increment, the frames and the F-03 fixture under
[qualification/cases/F-03/](../../qualification/cases/F-03/CASE.md) were
authored by one Writer activation and its forks.

## Reproduction

```sh
AC=<scratch copy of axiom_indexer/build_tenants/core/code/ac.py at 9a9c4797>
python3 -I $AC validate --program axiomatic-program.json --bindings bindings.json \
  --output validation-report.json --emit-map logical-constraint-map.json
for FI in carrier-retention release-and-successor identity-scoped design-gate \
    odd-closure traversal-lineage ux-replay world-model-cut bind-and-resolve bootstrap; do
  for M in materialized reference-only; do
    python3 -I $AC project --program axiomatic-program.json --map logical-constraint-map.json \
      --bindings bindings.json --frame-index urn:stdo-3:claude:a-c-text:frame-index:$FI \
      --mode $M --output projection-$FI-$M.json
  done
done
```

The derivation from set-4's program was performed by a scratch script that
is not committed, as with the earlier sets: it applied the rewrites and the
disposal above, then merged ten fragments, one per frame, each authored and
validated separately. The program is the artefact, and this file records
every class of change.
