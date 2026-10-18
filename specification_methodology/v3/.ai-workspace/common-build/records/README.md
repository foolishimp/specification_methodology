# Common construction conservation record

This is construction accounting outside the standalone V3 package. It records historical source claims and proposals against the current common member bytes. It does not give the candidate authority, accept a replacement, establish semantic conservation, or qualify a release.

`CONSERVATION.json` covers all 705 source identities: 636 shared body rows, 14 tenant child rows and 55 nonbody rows. The nonbody set is exactly 10 compressions, 2 schemas, 24 templates, 1 licence, 17 plugin files and 1 release note. All ten compression deliveries remain deferred; their semantic disposition is unresolved, never `not_applicable` because of that deferral.

The original files are retained byte for byte under `sources/`, with Git identities and hashes in `SOURCES.json`. The historical predecessor evidence acquired from the selected installed release is separately pinned by `PREDECESSOR_SOURCE.json`. These source records are never rewritten by the generator. `RULES.json` is the declared author transform, including the exact loan-comparison row order, proposed meaning-change rows, ten disputed rows and Q2/Q6 owner choices.

| Artifact | Meaning |
|---|---|
| `CONSERVATION.json` | Every source ID, raw and normalized seed disposition, proposed current relation, receiving loci and their hashes, evidence, dependencies and pending decisions. All effective dispositions and acceptance remain unresolved/pending. |
| `VALIDATION.json` | Mechanical coverage and integrity checks, 16 positive/negative controls, and remaining limits. It does not assess meaning. |
| `LOAN_ROW_INDEX.json` | The 97 comparison row numbers mapped to stable source IDs using the frozen packet builder's `(claude, codex, id)` sort. The raw JSON array order is different and is not used as row numbering. |
| `CLAIM_DIGEST_RECOVERY.json` | New evidence for the 17 missing claim digests, with original null fields retained. Two exact heading-content digests are recovered; 15 synthetic clause extents remain unresolved. |

The generator restores exactly 19 truncated `not` values to `not_applicable`. Each repair retains the original bounded reason and points to its precise machine and prose source. None is a compression row. The source record remains unchanged; normalization occurs only in the construction projection.

One additional source-parser repair restores the successor routes for `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary-ownership`. The frozen prose row at `sources/claude_frontier.md:503` contains pipes quoted inside its disposition. The original parser consequently omitted its two successor loci. The repair quotes that complete row and recovers `FOUNDATIONS.md#results` for the result algebra/conjunction and `ASSURANCE.md#7-product-testing-frame-set` for testing-frame mappings. Its `superseded` proposal and pending acceptance are unchanged; Q17 remains open.

The ten disputed conserved-but-changed rows are 01, 11, 12, 19, 20, 25, 27, 32, 40 and 48. Each has its own `CONFIRM-ROW-nn` decision and an unresolved current proposal. This projection does not confirm them as a group or copy a donor relation. Rows 93–96 retain explicit Q2/Q6 keep-or-withdraw decisions; no withdrawal is performed. M1–M7 and A1 are proposed `superseded` relations requiring exact owner acceptance. A1's additional reach and P1's reviewer classification remain separate pending decisions. All 19 historical question IDs are retained with their source wording and current scope limits; Q10's UX ambiguity remains open.

Every historical review result is preserved as evidence with `current_applicability: not_established`. Matching text is a byte-identity observation, not a substitute for that applicability relation. The receiving-locus collection contains current package dependencies. Old names quoted in historical narrative are preserved separately as historical routes; they do not become missing package dependencies. A release note whose source claim is explicitly not applicable needs no replacement member.

The 17 missing predecessor digests were checked against the exact installed `v2.5.1-rc.2` manifest, SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`, and five member digests authenticated by it. The two UX heading slugs omit a hyphen created by an em dash. A unique normalized heading match recovers their content bytes using the original parser's rule: after the heading, through the next heading of any level. The other 15 IDs are synthetic clause splits. A containing heading is not the exact clause extent, so its digest is retained only as contextual evidence; inventing a clause digest would change the claim's scope. Every unresolved ID and its reason is listed in `CLAIM_DIGEST_RECOVERY.json`.

Run from the repository root:

```sh
python3 specification_methodology/v3/.ai-workspace/common-build/records/build_records.py
python3 specification_methodology/v3/.ai-workspace/common-build/records/build_records.py --check
```

The first command projects the authenticated frozen sources onto current candidate bytes and writes four JSON artifacts in this directory. The second recomputes and checks them without writing. It fails if source bytes, transformation rules, generator bytes or selected receiving member bytes have changed. Rebuild before the next freeze when the candidate changes. The generator rejects duplicate JSON keys, omitted/duplicate identities, malformed non-applicability, compression scope drift, invented acceptance, automatic disposition of disputed rows, proposed meaning changes marked conserved, missing dependencies/owner decisions, historical reviews promoted to current, and routes escaping the candidate.

Current mechanical result: all 705 records covered, all 16 controls pass, and every selected receiving locus resolves. Semantic review, completeness of material dependency sets, exact clause extents for 15 synthetic IDs, current applicability of historical evidence, owner replacement decisions, and release qualification remain open. This Writer authored the transform and provides no independent assessment of it.
