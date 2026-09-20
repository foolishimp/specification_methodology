# STDO Representation 2.5.1 RC1

Status: locally prepared coordinated candidate. Publication, Product acceptance
and external consumer adoption remain separate. T-288 and ABI delivery are
outside this candidate's qualification scope.

| Coordinate | Value |
|---|---|
| release version | `2.5.1-rc.1` |
| product-local cut | `v2.5.1-rc.1` |
| Project Release Namespace | `stdo_representation` |
| Project Subtree root | `stdo_representation` |
| qualified immutable tag ref | `refs/tags/stdo_representation/v2.5.1-rc.1` |
| qualified version-line selector | `refs/tags/stdo_representation/v2.5.1` |
| qualified RC branch | `refs/heads/rc/stdo_representation/2.5.1` |
| qualified release branch | `refs/heads/release/stdo_representation/2.5.1` |
| matched Source STDO ref | `refs/tags/specification_methodology/v2.5.1-rc.1` |
| public Source STDO basis | `stdo://releases/v2.5.1-rc.1/` |

## Exact Source STDO

The source is commit `dc4742d08af0a1c42c437a4ce645ea7ca55f3a3a`, annotated tag object
`b80e82e123f7f88eb0dffd9339f8ead9c733d153`, repository tree `eaf8358b09d3defcc5c85dd812961849480ab0c7`,
STDO subtree tree `00d7144449ca85af8746bbc7912e344dce55f80e` and standards tree
`5d16a82623e9e9450585d877e3d9ed49f132d250`. Its installed manifest is
`5d306da13994e69aa9f215d4c1cd2d0be96283c1e33a652b58e6e9262d036b64`. The complete
52-member standards aggregate is
`c6a3189ef79aeb4e3f75eb8fd8fba2f1126ea450df3ec59087273c56c03e3795`. The source release note and inventory
disposition every member against RC7. Manager 0.1.4 carries the existing install
closure repair; Axiom mechanics remain separate and unchanged.
Child tag and commit-B identities are bound externally by qualification.

## Exact Product Inventory

Exactly 9 entries; file digests cover bytes,
symlink digests their UTF-8 targets without a terminal newline. The sorted stream
contains SHA-256, two spaces, type, two spaces, path and newline:
`d5446c814234265ae4a3885462d2b2aa04e0ee27393e97e693c6e0440bb253c1`.

| Type | Member | SHA-256 |
|---|---|---|
| symlink | `.agents/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| symlink | `.claude/skills/stdo-representation` -> `../../skills/stdo-representation` | `92c6b8eb455f6bd656501d9496179af39f331ebf5df7114ee5e53825d91a6ddb` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1/axiomatic-program.json` | `f45bac9323a3058625325e6791ef8355f45c1bf8a3f8018203f3daf14db4e612` |
| file | `build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1/logical-constraint-map.json` | `a0c68f7a4cebf8166c7e436737d8fe5de68ac8f871dcd6a29196d719af89f9b1` |
| file | `skills/stdo-representation/SKILL.md` | `60d29af40c5820b081c8e0f39f3f637bf51dbc596d5aac5885a9d65854e8aae2` |
| file | `skills/stdo-representation/agents/openai.yaml` | `872aabc6e15b66dfcfe0f2d8c674a9d25511a94d74be781711304bc581619f5a` |
| file | `skills/stdo-representation/references/claude.md` | `584189012cb0c414392e381969a9b02eda2c3cae826cd310218d92a1a3212c20` |
| file | `skills/stdo-representation/references/codex.md` | `4ddbe37bda55a3c8f9e8545f391a906754067ffc49d2d6f0299eae2d41559497` |
| file | `skills/stdo-representation/references/frame-index-use.md` | `0bab598e78b637e29e4ac816f33965f8baef78c44d858adc7f5d2cdc8fbeae85` |

Authority, Definitions/frame configuration, release notes and evidence remain
external to this Product member set. Exact records accompany the install
closure. Co-location does not create Product membership or acceptance.

## Exact Dependency And Generated Assets

| exact Axiom dependency | `refs/tags/axiom_indexer/v2.5.1-rc.1` |

Axiom version `2.5.1-rc.1` has 7 members and
aggregate `55a2061bd55ca29e349318a2869bc13518374ef2fa764a73b1688e76d35a63c1`. Its external release
record `axiom_indexer/releases/v2.5.1.md` has digest
`d7075ec17d1a5c62cae4665abb80a44fc4661378b067daa77afbc77c2a57f654`.

| Role | Axiom member | SHA-256 |
|---|---|---|
| executable | `build_tenants/core/code/ac.py` | `5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8` |
| output_contract | `skills/axiomatize-corpus/references/output-contract.md` | `c124264d1fc564a8a054bba46b5c188c4e770da51862b4c2122e3c616efb1b6b` |
| schema | `skills/axiomatize-corpus/references/program.schema.json` | `43326dbab520bd2d56fbdf605211f66499de1969b13e2e0226868bd6af9777a7` |

| Representation artifact / external source evidence | SHA-256 |
|---|---|
| `build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1/source-corpus.json` | `2fe2f40dda56983e6617785f6cdda906dd5c5400e566346cdbdc3b6730a090e6` |
| `build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1/axiomatic-program.json` | `f45bac9323a3058625325e6791ef8355f45c1bf8a3f8018203f3daf14db4e612` |
| `build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1/logical-constraint-map.json` | `a0c68f7a4cebf8166c7e436737d8fe5de68ac8f871dcd6a29196d719af89f9b1` |
| `build_tenants/axiom_indexer/representation/stdo-v2.5.1-rc.1/validation-report.json` | `602d511f2d8b03663235ab7dc8e867e34b7b9c6f0b0dc28b4affb87fdf4371c8` |

## Claims And Predecessor Dispositions

The published predecessor is `stdo_representation/v2.5.0-rc.7`, annotated tag
`a010992bd0b403c032f68df9496386bb06bbfa65`, commit `4824d5a05619e6957110b7ac97464b42ac84c096`, aggregate
`cd42f90929ebaf6b4f7d8d983bffcb729ee38f173ca5cfb0d74a9be4f08feb26`.

- `STDO-REP-2.5.1-RC1-C01` refines RC7 C01 with source-grounded reuse/invalidators,
  computational-path evaluation, supported operational and threat assumptions,
  retention burden, compression fidelity and work continuity. Changed meanings
  are authored; digest rebinding alone supplies no semantic qualification.
- `STDO-REP-2.5.1-RC1-C02` refines RC7 C02 with accepted T-031's interface frame
  and affected explicit frame membership/support. Its four claim classes and
  conditional applicability remain distinct. Axiom's generic mechanics are
  unchanged and reproduce both views of the authored indexes.
- `STDO-REP-2.5.1-RC1-C03` conserves RC7 C03's native interface, updating exact
  routes and qualifying the changed guidance in fresh Codex/Claude source/map
  contexts. Native decisions qualify observed use only, never fixture counts,
  effects or refusal behavior owned by executable checks.
- `STDO-REP-2.5.1-RC1-C04` supersedes RC7 C04's cohort identity with RC1. Exact
  source/dependency closure and separately owned acceptance remain mandatory.

The candidate contains 115 clauses and
6 explicit frame indexes. Its source record
binds the complete 52-member exact Install.
The [RC1 preparation record](../../specification_methodology/.ai-workspace/comments/codex/20260920T070629Z_stdo_251_rc1/README.md)
retains conservation/semantic assessment, mechanical reproduction and negatives,
actual native results and limitations, internal configuration and cohort checks.
Their claims remain distinct; source or map presence closes none by itself.

No automatic frame selection, semantic grader, universal operational bound,
general native reliability or ABI delivery outcome is claimed. Immutable
predecessor results remain bounded by their original subjects. This candidate
record does not publish or accept a Product or adopt it in external consumers.
