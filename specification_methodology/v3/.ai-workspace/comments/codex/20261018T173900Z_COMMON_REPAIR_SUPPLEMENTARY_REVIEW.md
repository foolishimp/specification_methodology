# Supplementary review of the first common repair

The bounded repair predicate is satisfied. I found no remaining blocker in the B1–B3 corrections or the two records-mechanism repairs reviewed here. This is a review of those corrections, not a whole-candidate acceptance or release-freeze verdict. The candidate is still not freezable: pending owner and covering-review decisions and their implementation follow-through remain.

## Role, subject and expectations

Reviewer: `/root/common_repair_review`, a fresh actor that authored none of the reviewed package, mechanism or decision edits. Root and two delegated Writers authored them. I share the root author's model family and received its review task and inherited context; I also read the writers' returns. This is a declared supplementary review, not cross-family evidence, a cold-reader trial or the covering independent review. I do not assign P1's class or accept D1–D4. The covering review remains unassigned.

The delegated predicate, fixed before candidate inspection, was: restore the existing RC-only rule; correct all seven orphaned appendix pointers; remove source-construction residue without losing local obligations; preserve current owner-derived frame content; require valid receiving loci for carried claims; and expose D1–D4 without accepting them. I used the pinned Claude review as finding input and checked the actual source and preimage diff, rather than accepting the writers' conclusions.

- Reviewed checkpoint: `7d0516f37716298f038548c4152a1a697ce70f95`.
- Package tree: `7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`.
- Preimage: `d60dead410b1d7e19d88ed80037d8a22708d8cc4`, package tree `082df4ea2b7b3658aab528bbfbcfe81234ccc810`.
- Package inventory: `package-inventory.json`, SHA-256 `187908fed6acee3570f472ee15c11e3116537155a8c5cc14cad8d096dc8381cd`; exactly 81 members. Before and after reading, every current member's bytes and digest matched the inventory, with no extra or missing file. At the end, each also matched the checkpoint's Git bytes.
- Review input: `inputs/claude-review.md`, SHA-256 `52022b61f5c3572cd674002bf761005117d72f36f533a8bc837ea44fb85031ff`, bound by `inputs/PINS.json` to corrected review `94ac5d3e8b977d28f668a5988327fdd5b340f0bd`.
- Builder basis selected by `stdo_3.json`: `v2.5.1-rc.2`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. Root's fresh verification is shared mechanical evidence; I did not independently rerun installed-basis verification.

The only file I write is this report. No package repair, generated-output rewrite, Git effect, owner decision or installed state change was performed by this Reviewer.

## Findings in the repaired scope

No blocking or material defect found within the bounded correction predicate.

| Area | Source-first result |
|---|---|
| B1, release identity | AXIOMATIC_CALCULUS §8 and TRAVERSAL_OCCURRENCE Closed profile signature now require the immutable RC URI and route acceptance to RELEASE. RELEASE's cut-name, mutable-selector and no-second-final-cut law is unchanged. Its only repair edits remove an orphaned appendix reference and construction provenance. The same-package derivation proposal remains pending D1. |
| B2, seven pointers | ASSURANCE's §17, IDENTITY's §13, PRODUCT_DEFINITION's §13 and RELEASE's §11 sentences are removed. ODD's §21 reference becomes the live RELEASE §9 successor-disposition route, retaining its distinction from ACTIVATION dispositions. WORLD_MODEL's two §15 routes and bare builder anchor are removed while the units and stages remain. |
| B3, source-history residue | The changed paragraphs now state local law directly. Accounts remain three distinct non-tier, non-commitment accounts. FOUNDATIONS already owned accounts and imports in its lead; its added-choice standing remains. Imports retain owner-qualified identity, direction, zero loss and no grant of semantic, evaluation, operation or decision authority. All ten pillar contributions remain in order; their trace still creates no premise, standing or choice. |
| B3, assurance and porting | Ported authorship now routes to EVALUATION §3, which already retains a contribution's author and excludes that author's independent acceptance. Shared dependencies and the limits of repeated or same-family evidence remain in FOUNDATIONS. No new review authority is introduced by localising the route. |
| B3, formal representation | AXIOMATIC_CALCULUS §6 and Constraint surfaces supply the local fidelity owner. The five support kinds, external-predicate provenance, positive/negative/unresolved cases, finite-proof limits and separate semantic/fidelity/use evidence remain. The text no longer asserts a delivered candidate interpretation or depends on an external six-criterion construction scheme. Its generic interpretation obligations remain conditional on the selected surface, consistent with CONFORMANCE's applicability paragraph. |
| Smaller routes | EVALUATION identifies RELEASE as F15; the frame-basis template uses ACTIVATION's local disposition owner; GETTING_STARTED uses packaged templates rather than unavailable QUICKSTART; historical glossary/schema comparisons are removed. |
| Decision readback | REGISTER and DECISIONS explicitly list D1–D4 as pending. D2 is honestly represented outside the inherited population because CONFORMANCE has no inherited identity. D4's existing row now has its standalone-adaptation flag and a pending STANDALONE decision while preserving CONFIRM-ROW-20. |

I searched all packaged Markdown, including frames, for the reported residue forms: `carried from`, `common requirement`, unqualified `is new`/`are new`/`also new`, `records dispositions`, `Product that owns this/the corpus`, `Cross-Synthesis`, `seventh criterion`, `revision-2`, `earlier label`, `a_c/i3`, `common frame basis`, `constraint-surface fidelity rule` and `candidate's a_c`. There were no matches. A broader scan of construction, owning-Product, candidate and predecessor language found generic method/scenario uses, not an additional demonstrated source-history dependency. This lexical search is discovery support, not proof that all prose is standalone.

## Mechanical readback performed here

The current records generator's `--check` passed: 705 identities, 636 shared body plus 14 tenant children plus 55 nonbody records, 19 truncated-disposition repairs, zero unresolved selected loci and 20 passing controls. I read the parser, resolver, build ordering, validator and output path.

The repaired parser selects `plugins/spec/LICENSE` from the frozen receiving column; it does not substitute the root LICENSE mentioned in the historical note. The persisted receiving locus resolves to the actual plugin file and its seed-identical SHA-256. The validator now requires a nonempty locus collection for `conserved` and `superseded` proposals and refuses every unresolved selected locus, including on unresolved proposals. `build()` calls validation before producing its proof; `main()` receives a completed build before writing outputs.

I also exercised four independent in-memory mutations against the integrated subject. These were not package edits:

| Control | Observation |
|---|---|
| Empty receiving loci on a conserved claim | Refused: `carried claim has no receiving locus: README.md#standards-library`. |
| Empty receiving loci on a superseded claim | Refused: `carried claim has no receiving locus: AXIOMATIC_CALCULUS.md#derivation-provenance`. |
| Full build whose reader returns no plugin LICENSE bytes | Refused at validation: `plugins/spec/LICENSE (missing_candidate_member)`. |
| Full build whose README reader omits the selected heading | Refused at validation: `standards/README.md#library-and-installed-basis (missing_candidate_anchor)`. |

The last two injected bytes through the reader in memory and bypassed only the stable-file re-read for that simulation, so they reached the missing-locus validation being tested. They demonstrate refusal before `build()` returns; they are not filesystem deletion or crash-atomicity tests. Existing persisted outputs were not rewritten. I did not extend these bounded checks into an audit of every possible parser input.

Compared with the preimage projection, all 705 identity keys, raw seed dispositions, proposed dispositions and pre-existing pending-decision objects are preserved. Every effective disposition remains unresolved and every acceptance pending. The only added row-level decision is `STANDALONE:REFERENCE_FRAME_METHOD.md#method-self-qualification`. LICENSE gains its receiving route; changed member/section digests correctly bind the new bytes.

The frame generator's `--check --root build_tenants/common` passed without writes. Separately, using a heading parser and SHA-256 calculation that did not import the frame generator, I recomputed all 223 owner/section bindings across all 12 frames, including the bounded assurance spans. Each matched FRAME_INPUTS. Every frame's byte count and digest matched; the largest is 141,785 bytes under the declared 160,000-byte cap. The generator's exact-output comparison covers excerpt rebasing; my independent calculation covers owner and section identities. Neither is evidence of actual actor context fit or semantic sufficiency.

## Remaining findings and decisions outside this repair closure

These are unresolved current conditions, not newly repaired or accepted matters. They continue to prevent a whole-candidate freeze claim.

1. **Material: P1's inconsistent stale-basis wording remains.** REFERENCE_FRAME's family-table sentence at line 159 is unqualified; RF-005 at lines 313–317 qualifies the case by inability to support the required claim. I confirm the mismatch, without classifying P1 or selecting either rule. DECISIONS.md exposes it and leaves classification to the covering reviewer.
2. **Material before a runnable identity-record claim: D1 follow-through remains incomplete.** AXIOMATIC_CALCULUS §8 calls for absolute semantic addresses to the actual premise clauses, including table terms and paragraphs in §1's derivation population; TRAVERSAL_OCCURRENCE requires each fragment to resolve one heading under a publication rule that is not completed here. The digest scalar fields in both identity records use `sha256:<hex>`, while the packaged schemas use bare 64-character hex. The profile also relates those fields to manifest digests. A declared encoding/comparison rule and complete clause-address rule are still needed; the legitimate `:sha256:` component in identity URNs is a different matter. DECISIONS.json carries these as follow-through. This review does not invent their grammar or choose the derivation basis, and no a_c implementation is required to observe these textual gaps.
3. **Material owner choice: D2 remains open.** CONFORMANCE currently publishes its own expected distinctions; EVALUATION's family table still names independently specified expectations, and the README index retains qualification-only wording. The proposed independent-qualification preamble is present only in DECISIONS.json, not applied. The chosen scope and independence relation still need consistent consumers.
4. **Minor, already exposed: Q10's provisional interpretation remains in UX.** The stricter-test/scope reading and the marker retaining ambiguity are unchanged. This review supplies no decision or copy-editing override of Q10.

D3's added World Model application-evidence duty and D4's recoverability adaptation remain visible proposals. The pre-existing A1 reach, Q13/Q14, rows 93–96, exact replacements, disputed changed-but-conserved rows, P1 class and covering-review assignment retain their owners. No decision count or whole-candidate acceptance is inferred from these repairs.

## Evidence pins and limits

| Reviewed support | SHA-256 |
|---|---|
| DECISIONS.json | `749efedd867c6267da6f9ad00bf6bdf0a19244f8e8e0450b911f0f195f641c2a` |
| DECISIONS.md | `be5fa2b83463d08c5fff07bf7691417d8a9fd6e963a78f24d04d7907f6efc543` |
| records/build_records.py | `23e44744cea801b8c76890359171eb641421c1665b1a773beecec680ede3664c` |
| records/RULES.json | `e51932643c71d2aece45155c182c07512f67c63c6e4597d63ad36af522dbdab0` |
| records/CONSERVATION.json | `5ed8f330900b31b5a8a48a825f5a87ed41bc280ac8a2e0aeec457cf7adaa79a7` |
| records/VALIDATION.json | `0c1ddd7a3f5243a91adf6f00d155d186e40b0401a12d7f896bd6ba0c3aafea37` |
| frame-tools/generate_frames.py | `d114f3352063cbfbbe179aa5a395a745b03c3319173b8d63b55935ef04b1fc48` |

This review covers the correction delta and the named local owners, not a fresh obligation-by-obligation review of the whole method. It does not qualify the materialised install, source/installed equality, release package, real-interpreter behavior, actual-use scenarios, independence policy or all 705 semantic conservation claims. Root's separate installed-verifier proof and existing author tests are not my semantic verdict. Historical qualifications remain bound to their old subjects. Host context, spend and actor-capacity fit were not measured. No acceptance, merge, publication, release or consumer adoption is granted.
