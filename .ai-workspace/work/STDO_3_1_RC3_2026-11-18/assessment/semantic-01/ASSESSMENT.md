# STDO 3.1.0-rc.3 independent semantic assessment (stdo-review)

**Result: satisfied for all seven exact-query subjects and the bounded visual. No findings against the claim.** There are three low-severity side observations (A1–A3 below); none changes what any of the seven delivered contexts select. I made no edits and no repairs.

## Subject, basis and claim
- **Native cut:** v3.1.0-rc.3. Native commit `b2e21ad0…`, tree `1432a308…`, tag object `61344ea9…`, manifest `2b3a7391…6c7a9a`, installed root `native-store/releases/v3.1.0-rc.3`, as given in `NATIVE_BINDING.json`. It is local and unpublished; I make no claim about publication.
- **Claim:** the RC3 Python v2 and SDLC v1 indexes, as delivered for the seven `SUBJECTS.json` queries, keep the governing method constraints of the selected native source. The profile query is the declared hypothetical ODD/UX case. The other boundary queries are declared qualification scenarios. Separately, the 24 regenerated visual annotations are still valid against the RC3 sources.
- **Out of scope:** task admission, code correctness, Product conformance, whole-method qualification, human acceptance and publication.

## Obligations I derived from the source before opening any candidate
I read, in this order: `ACTIVATION.md`, the installed 3.0.4 `stdo-review` skill, Purpose Context PRODUCT, requirements PC-R01–R16, then the RC3 native owners.

1. **ODD §11.5D**
   - Tracking and reconciliation are required: obligations, decisions, progress and unresolved matters stay available, and are reconciled to the authoritative workspace before a material decision.
   - The account is never a second truth surface.
   - A register is optional; an LLM or other mechanism counts if it does the same job.
   - Facts a later step needs and cannot re-acquire must be recorded, including judgments, residuals and authority decisions. Sources that can be re-acquired stay sources.
   - Records keep subject, basis, scope, evidence and authority, and corrections keep enough identity to tell prior from current.
   - There is no mandatory replay log, ledger or closure-decision enum.
   - Each evaluation carries its own predicate and core result.
   - An F_P worker must not be given an F_D-authored semantic recipe when the edge needs F_P judgment.
2. **ODD §11.5B (authority audit)**
   - When: before activation and closure.
   - Triggers: changes to traversal control, delegation (including worker transport and process supervision), admission, evidence evaluation, closure, assurance, retry or continuation.
   - Method: examine actual call paths and outputs, and show no rival controller.
   - Consequence: missing or conflicting authority blocks the affected activation and closure.
3. **ODD §5, §10, §11.5, §11.5A, §11.5C and §11.7A**
   - Workspace truth; projections stay coherent with their sources.
   - The runtime owns continuation; the Product owns concrete mechanisms.
   - F_P and F_H add no authority.
   - The walkthrough plus admission gate is conformance evidence, not ratification.
4. **SPEC_METHOD §2–§4**
   - Product defines the intended end state, including capabilities still to be built. Goals are the current epics.
   - `product_reprice` now covers the "adopted Product definition or intended end state".
   - Outcome conservation is unchanged.
5. **UX §8:** the Msg-replay proof is its own, separately retained contract.
6. **ACTIVATION §5:** reconcile the actor's account to current evidence; no complete-history replay is required.

## What I read and the limits of that reading
- The final INDEX, SOURCE-DELTA, CATALOG and the `3.1.0-rc.3` authoring target, including every amended rule's text and grounds and the W35 selector change.
- Every SUBJECTS query, and each delivered `CONTEXT.md` in full (Python and profile) or at least its rule-by-rule applicability (boundaries).
- The fixture's requirements, design, work contract, `stdo_trial.json`, `PROFILE_SCENARIO.md` and `BOUNDARY_SCENARIOS.md`.
- I compared the RC2→RC3 ACTIVATION delta using heading alignment plus targeted greps, not a full byte diff. The changes I found are confined to anchor renames (lines 110 and 878) and the consumer list (line 1448).
- I did not recompute any hashes: I have no hashing tool. The JSON digests below are the SUBJECTS bindings, which I transcribed. I checked consistency only: the catalog index digest equals the SUBJECTS `raw_index_sha256`.
- The observed use was reading and making declared judgments. I invented no task execution and did no host discovery.

## Assessment against the obligations
- **Profile (ODD/UX hypothetical):** every obligation above is present.
  - O02 covers the audit's timing, triggers, consequence, call-path evidence and rival-controller exclusion.
  - O03 keeps authorities separate and says F_P/F_H add no authority.
  - O05 covers tracking, reconciliation, the optional register or equivalent, needed transient facts, correction identity, and the restored F_P semantic-judgment guard.
  - O06 covers predicate-specific results, with no ledger fold and no closure enum.
  - O04 and O07–O10 cover the outcome boundary, continuation, projection coherence and the walkthrough.
  - O02, O03 and O05–O08 explicitly deny a named runtime, mandatory ledger, evaluator API, universal replay and closure enum.
  - U05 and U09 retain UX's own Msg-replay duty separately.
  - D39 and C19 stop a helper from gaining traversal control.
  - The amended texts match the RC3 clauses they cite. I checked the ground line ranges against the actual RC3 section boundaries (ODD 587–782 and 955–970).
- **Python:** O and U rules are correctly absent because `profile_odd` and `profile_ux` are false. C19 keeps the conditional pointer.
  - The family guard does not require the profiles to be false (PC-R12).
  - The exception premise conjunctions in D05, D06 and D08 are preserved, and a false request grants nothing (PC-R13).
  - C01 keeps coverage separate from task admission and verification (PC-R11).
  - S01 carries the Product/Goals amendment.
  - C20's "exact replay" is ACTIVATION §4's admission-proof replay (RC3 lines 1327 and 1358), not the removed ODD replay.
- **SDLC (work, sdlc, acceptance, qualification, release):**
  - W35 now selects `product_acceptance` as well, grounded in EVALUATION §5 and RELEASE §9. Its dependencies, exceptions and unknown handling are preserved.
  - W26 applies only to release.
  - W14–W16 apply only when review is in scope.
  - W27–W31 apply only when evidence reuse or a source change is involved.
  - W39 and W40 keep needed step-produced facts and resumption without a registry or complete replay.
  - The RC3 change to ACTIVATION §5 (line 1448) touches only the consumer list. W40's meaning is unaffected.
- **PC-R15/R16:** the indexes are bound to the actual cut manifest. Provenance reads `covered:false` and `unassessed`. No predecessor judgment is transferred.

## Source-ground amendment function
`apply_source_amendment` (`purpose_context/scripts/rebuild_release_indexes.py:43`):
- It requires the predecessor rule text to equal the declared preimage.
- It requires each ground's actual RC3 bytes to match the declared sha256, and requires at least one ground.
- It replaces only `text` and `source_refs`.
- It writes no assessment or coverage standing.
- The SDLC field amendment also checks the preimage and section hashes.
- I found no way it bypasses source or preimage validity or fabricates an assessment. One latent gap is A3 below.

## Visual (24 annotations: 8 concepts, 6 relations, 8 constraints, 1 latitude, 1 residual)
- **Unchanged owners:** TICKETS and SDLC_DEFAULTS are byte-equal between RC2 and RC3.
- **ACTIVATION:** every quote resolves at RC3 (lines 695, 1381, 1460–1492, 1683 and 1707). The ACTIVATION changes are cross-reference anchors and consumer lists. They don't change the meaning of any selected annotation, including the reconciliation and step-produced-fact meanings, which agree with the new ODD §11.5D.
- **AXIOMATIC_CALCULUS:** changed, but AC-003 and AC-011 still exist (lines 500 and 670). The residual explicitly leaves it unmodelled.
- **Receipts:**
  - The browser run had 12 checks passed, 0 HTTP requests, 0 page errors, and the artifact digest was stable throughout.
  - The Writer checks resolved 317 grounding occurrences and gave 93 sections a residual.
  - A stale copied source was refused (exit 2).
- **Limits:** navigation plus selected relations only. These are Writer and browser observations, not semantic proof. The meaning judgment above is mine.

## Side observations (separate from the claim; severity 4 = low)
- **A1 – W11 lost the class names.** The RC3 W11 text no longer names the class identifiers (`goal_reprice` … `realization_refactor`). The unchanged SPEC_METHOD §4 and TICKETS §4 still declare and record those names. The layer meaning survives, and W11 isn't selected in any of the seven contexts. It would affect future queries with a finding present. My recommendation is to restore the identifiers alongside the new layer wording.
- **A2 – The scenario document is stale.** `BOUNDARY_SCENARIOS.md` is the grant for four queries, but it still describes an RC2 basis and an RC1 predecessor. The four query IDs also read `stdo-31-rc2-successor-*`. The query facts and `stdo_trial.json` correctly bind RC3, so context coverage isn't affected. The file must not be used as RC3 predecessor evidence.
- **A3 – The amendment function doesn't cross-check `path` against `source_id`.** It hashes the bytes at `ground.path` but records `ground.source_id`. All entries in this target are consistent, so nothing is exploited here; it's a hardening gap.

## Earlier evidence
None of the RC2, 3.0.5 or 3.0.4 assessments applies: the index, corpus and query identities all changed. I reused only mechanical facts, namely the byte equality of conserved spans and unchanged members, after checking that they applied. Every judgment here is new.

## Independence
I am a Claude-family reviewer, independent of the Codex construction but not of the earlier Claude-family architectural direction, as `ACTIVATION.md` discloses. Same-family independence beyond that is not established. A1 and A2 return to the Product decision owner, and A3 to the Purpose Context owner.

```json
{
  "kind": "stdo.rc3-semantic-assessment/1",
  "result": "satisfied",
  "visual_result": "satisfied",
  "assessments": [
    {"name": "python", "index_sha256": "b449c20fb13e90c42a433caacbe84605a460366e4be36890f752f17f2cb204d8", "corpus_sha256": "b762e5eaa14744b2e8fc5aa44b94c91377c74b98c596e1268df501aa65613c91", "query_sha256": "271933f847f65ba77cf1b7fdb520a6490252db3844be5224896075218c3c2ecd", "status": "supported", "evidence": "Non-ODD/UX pure refactor: S/D/A/E/C rules applicable; O/U correctly excluded with C19 conditional pointer; S01 Product/Goals amendment faithful; exception premise conjunctions and C01 coverage/task separation retained."},
    {"name": "sdlc", "index_sha256": "b8b6073c1c634b2a83323b48dd9e493163334fa196bcf774fd518bdcdd3d0292", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "70d35add8f0558bb9182914d50063a3cf3ab9c05efae68abe8541e369fdbf879", "status": "supported", "evidence": "Ordinary run-carrier work: W01-W08, W12, W23-W24, W33-W34, W36-W40 retain carrier, context, step-fact recording and resumption without registry or replay; finding-gated rules false."},
    {"name": "profile", "index_sha256": "b449c20fb13e90c42a433caacbe84605a460366e4be36890f752f17f2cb204d8", "corpus_sha256": "b762e5eaa14744b2e8fc5aa44b94c91377c74b98c596e1268df501aa65613c91", "query_sha256": "fc37ed7b374d76e2e0ae7f85371f875c2c6377d20ee6e6ee75ebcca765d5ab2a", "status": "supported", "evidence": "Hypothetical ODD/UX: O01-O10 retain graph ownership, 11.5B audit timing/triggers/consequence, separate authority, F_P judgment guard, tracking/reconciliation, optional register, needed facts and predicate-specific evidence; no ledger/evaluator API/replay/enum; U05/U09 keep UX Msg-replay separately."},
    {"name": "acceptance", "index_sha256": "b8b6073c1c634b2a83323b48dd9e493163334fa196bcf774fd518bdcdd3d0292", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "0136d1bffe3e01f468bc952efc6422e350e5d2e0c859482b457541ce1e9a28d1", "status": "supported", "evidence": "product_acceptance selects W25 and amended W35 (EVALUATION 5 / RELEASE 9), review W14-W16, reuse W27-W31; W26 correctly release-only; declared scenario, no verdict."},
    {"name": "qualification", "index_sha256": "b8b6073c1c634b2a83323b48dd9e493163334fa196bcf774fd518bdcdd3d0292", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "e7dcee1d44334b1253747e7f4327c915deb88358f63bfdb1aa587b22dfbfff9c", "status": "supported", "evidence": "W25, W35 successor dispositions, review, reuse and invalidation retained; W26 not applicable outside release; declared scenario."},
    {"name": "release", "index_sha256": "b8b6073c1c634b2a83323b48dd9e493163334fa196bcf774fd518bdcdd3d0292", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "6a0a47a5ced7f0dcfff40cfa0776df62d3efbd425d0ffc91cfc51468b8ac2d3c", "status": "supported", "evidence": "W26 release criteria, W35 conservation, W25 gate, review and reuse rules applicable; no publication or acceptance implied; declared scenario."},
    {"name": "work", "index_sha256": "b8b6073c1c634b2a83323b48dd9e493163334fa196bcf774fd518bdcdd3d0292", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "aa0f9a503a621a833103313e70959521c094cba381dacd9d6bc10b4c4cfed6b6", "status": "supported", "evidence": "Boundary none with reuse and source change: W27-W31 invalidation/staleness, W36-W40 carrier and resumption retained; review rules correctly false. Grant document text is stale (adjacent A2) but does not alter selection."}
  ]
}
```