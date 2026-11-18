## Result: **falsified.** One finding, on the new `triage` subject. The other seven subjects are supported.

I did not edit, repair or publish anything, and I make no claim about any actor picking this up. I did not compute any hashes. The digests in the JSON are copied from `assessment/semantic-02/SUBJECTS.json` as bindings only.

### What I checked
- **Native cut:** v3.1.0-rc.3 (commit `b2e21ad0…`, manifest `2b3a7391…6c7a9a`), local and unpublished, per `NATIVE_BINDING.json`.
- **Claim:** the eight delivered contexts keep the governing method constraints after the bounded A1–A3 repairs.
- **Out of scope:** task admission, Product conformance, whole-method qualification, human acceptance and publication.

### Obligations I took from the source, before opening the candidates
- **`SPEC_METHOD` §4 Change classes (lines 872–905):**
  - Six named classes, each with its own re-entry point.
  - Goals means the current work-wave focus; Product means the adopted definition or intended end state.
  - `realization_refactor` *"must prove no upstream drift"*.
  - A smaller change re-enters below Goals only if it explicitly asserts that nothing upstream changes.
  - A declared class is never a result: "realization_refactor cannot stand in for a satisfied result that no upstream drift occurred".
- **`SPEC_METHOD` §4 intake and computed classification:**
  - A diagnosis grants no repair.
  - Unknown stays unknown.
  - Classification facts are not evaluation results.
- **`PRODUCT_DEFINITION` §3:** a complete constitutional set. Entry points and indexes cannot narrow it.
- **`ACTIVATION.md`:**
  - Product is the intended end state; Goals are the current epics.
  - Tracking and reconciliation are required.
  - A register is optional and an equivalent mechanism is allowed.
  - No mandatory ledger, event log, evaluator API or replay.

### Finding F1: the triage context drops W11's no-drift proof obligation (severity 3 on the 1-highest/5-lowest scale)
- **What's wrong:** RC2 W11 said "realization_refactor … with no-upstream-drift proof". The repaired W11 (`purpose_context/authoring/release-targets/3.1.0-rc.3.json:569`, delivered at `codex-triage-boundary/CONTEXT.md:90`) says "realization_refactor for local realization change with no upstream drift re-enters only that surface". The proof obligation has become a description of the class.
- **Nothing else in the triage context restores it.** It never says a class label is not a satisfied no-drift result. W05 only states the general rule that only `satisfied` establishes a predicate.
- **Why it matters:** this is the property the new grant itself requires. `BOUNDARY_SCENARIOS.md:13-14` says the context must keep the named classes "rather than accepting a class label as a successful no-drift result".
- **How it could go wrong:** an agent triaging a planned repair picks `realization_refactor`. It then treats "no upstream drift" as established by the label and skips the proof. Upstream drift could then land without its class or re-entry.
- **Where it started:** the packages-01 W11 had already lost the proof wording. The A1 repair restored only the identifiers. Semantic-01's "layer meaning survives" did not catch this, and I do not reuse that judgment.
- **Blast radius:** only SDLC-index contexts with `repair_planned=true`, since only W11 is affected and no rule depends on W11. Of the eight subjects, that is just `triage`. The Python index S rule still keeps "must prove no upstream drift" and "A class label is not a successful no-drift evaluation".
- **Workaround:** W11 cites `SPEC_METHOD:872-905`, so a reader who acquires the cited source gets the full rule.
- **Repair:** low complexity. Restore "with no-upstream-drift proof" in the replacement text, optionally adding the class-label sentence. Then rebuild and re-assess `triage` exactly; the other seven need only an index-binding recheck. Regression risk is low.
- **Confidence:** high. This goes to the Purpose Context owner; priority belongs to the decision owner.

### A1–A3 disposition
- **A1 (W11 class names): partly repaired.**
  - All six identifiers are back, alongside "current epics/work-wave focus" and "adopted Product definition or intended end state".
  - The triage query selects W11.
  - The triage query is hypothetical (`finding_present` and `repair_planned` both true) and claims no diagnosis or effect grant. W09/W10 require classification before diagnosis or repair. W10 and W02 deny repair authority.
  - But the repair carries the F1 omission, so A1 is not closed.
- **A2 (stale scenario document and labels): repaired.**
  - `final-use-02/fixture/BOUNDARY_SCENARIOS.md` binds RC3 and names RC2 as the immutable predecessor.
  - The query IDs now read `stdo-31-rc3-*`.
  - The fixture's Product, work contract and `stdo_trial.json` bind v3.1.0-rc.3.
- **A3 (source id/path mismatch): repaired.**
  - In `rebuild_release_indexes.py:43-58`, the preimage check, the new id/path refusal (line 50) and the ground-hash check (line 53) run before any write.
  - At least one ground is required, and only `text` and `source_refs` change.
  - The SDLC field-amendment path builds its path from the source id, so it cannot diverge.
  - `SOURCE_AMENDMENT_CONTROLS.json` lists refusals for all three cases. I treat those counts as observations, not semantic support, and I did not confirm the generator digest.

### Reuse scope and limits
- **What changed since semantic-01:**
  - The Python index is unchanged: its `SUBJECTS` digests match semantic-01.
  - In the SDLC index, by the author's per-rule digests in `SOURCE-DELTA`, only W11 differs between packages-01 and packages-02. I read the W11 text in both.
  - For the seven earlier queries, the facts differ only in `id` and the `grant` path.
  - `PROFILE_SCENARIO.md` reads identically in both runs.
  - Each delivered context has the same number of rule entries as its trial-hosts-01 counterpart.
- **What I reused, and on what grounds:**
  - For `python`, `profile`, `sdlc`, `work`, `acceptance`, `qualification` and `release`, I reuse semantic-01's judgments only on that basis.
  - The boundary contexts were not diffed line by line; my check there is the matching counts plus guard analysis showing W11 cannot be selected when `repair_planned=false`.
  - My own current judgment covers W11, the triage context, the A2 grant text and the A3 code.
- **Profile, checked against the current context:**
  - O05 keeps tracking and reconciliation, the optional register or equivalent mechanism, needed transient facts, correction identity and the F_P guard.
  - O02 keeps the §11.5B audit.
  - O02, O03 and O05–O08 deny any mandatory ledger, evaluator API, replay or closure enum.
  - U05 and U09 keep UX's Msg replay as a separate scope.
- **Native and visual:** source native bytes and the visual model are unchanged, so semantic-01's source-first reasoning on them carries over with its stated limits (heading alignment and targeted greps, plus Writer and browser observations that are not semantic proof).
- **Independence:** I am a Claude-family reviewer, independent of the Codex construction but not of the earlier Claude-family direction. Independence beyond that is not established.

```json
{
  "kind": "stdo.rc3-semantic-assessment/1",
  "result": "falsified",
  "visual_result": "satisfied",
  "visual_evidence": "Unchanged exact visual model and source native bytes; semantic-01 visual judgment reused with its stated limits (navigation plus selected relations; Writer/browser receipts are not semantic proof). No new visual assessment performed.",
  "findings": [
    {"id": "F1", "subject": "triage", "severity": 3, "confidence": "high", "property": "SPEC_METHOD 4 Change classes: realization_refactor must prove no upstream drift; a declared class is not a satisfied no-drift result", "evidence": "release-targets/3.1.0-rc.3.json:569 W11 replacement drops RC2 'with no-upstream-drift proof'; delivered codex-triage-boundary/CONTEXT.md:90 states the class as a description; no selected rule restores it; BOUNDARY_SCENARIOS.md:13-14 requires it", "blast_radius": "SDLC-index contexts with repair_planned=true; no rule depends on W11", "workaround": "acquire cited SPEC_METHOD:872-905", "re_entry": "Purpose Context owner: restore proof wording in W11 replacement_text, rebuild, exact triage reassessment"}
  ],
  "a1_a3": {"A1": "partially_repaired_identifiers_restored_proof_obligation_missing_F1", "A2": "repaired", "A3": "repaired"},
  "assessments": [
    {"name": "python", "index_sha256": "b449c20fb13e90c42a433caacbe84605a460366e4be36890f752f17f2cb204d8", "corpus_sha256": "b762e5eaa14744b2e8fc5aa44b94c91377c74b98c596e1268df501aa65613c91", "query_sha256": "6d3de8871e9768e78af2ae130f4b7a7b7ee6e452e3fe44ce5d70a66b568678cb", "status": "supported", "evidence": "Index identity unchanged from semantic-01; query differs only by grant path to an equivalent RC3 work contract; same rule count; semantic-01 judgment reused after this applicability check. Python S rule retains no-drift proof and class-label-not-result."},
    {"name": "sdlc", "index_sha256": "89830711e9596c395dcd0ba8751f8b6f5474138977f1c4b1c46d37afa670b05e", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "023f7a92026fd8a9dfd5deb10469e49f584c7951466def1e4e42e5765e4a9330", "status": "supported", "evidence": "Only W11 changed (author per-rule digests plus my text read); repair_planned=false so W11 is not selected and has no dependents; facts unchanged apart from grant path; same rule count; semantic-01 judgment reused."},
    {"name": "profile", "index_sha256": "b449c20fb13e90c42a433caacbe84605a460366e4be36890f752f17f2cb204d8", "corpus_sha256": "b762e5eaa14744b2e8fc5aa44b94c91377c74b98c596e1268df501aa65613c91", "query_sha256": "3b9eeecea33fd2509101c39209110c1c25b9fc3054b0cba558f97902b80954f4", "status": "supported", "evidence": "Index unchanged; PROFILE_SCENARIO reads identically; current context O02/O05-O08 retain audit, tracking/reconciliation, optional register or equivalent, needed transient facts, predicate-specific results; no mandatory ledger/evaluator API/replay/enum; U05/U09 keep UX Msg replay separate."},
    {"name": "acceptance", "index_sha256": "89830711e9596c395dcd0ba8751f8b6f5474138977f1c4b1c46d37afa670b05e", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "c4fcab963e40633990fb59dc78c41760b0db36cc1ea769a682d4ebd84ec5c0fa", "status": "supported", "evidence": "W11 not selected (repair_planned=false); id now rc3 and grant is the corrected RC3/RC2-predecessor scenario; same rule count; semantic-01 judgment reused."},
    {"name": "qualification", "index_sha256": "89830711e9596c395dcd0ba8751f8b6f5474138977f1c4b1c46d37afa670b05e", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "037cccee9b71610bf010350ede664fbdea73be0a553a4ce1e35070abcbc3558c", "status": "supported", "evidence": "W11 not selected; label/grant corrected (A2); same rule count; semantic-01 judgment reused."},
    {"name": "release", "index_sha256": "89830711e9596c395dcd0ba8751f8b6f5474138977f1c4b1c46d37afa670b05e", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "7e5bc5f229bc52669b58e159dca7aa51394c768e0e124c1435028cac6b865126", "status": "supported", "evidence": "W11 not selected; label/grant corrected (A2); same rule count; semantic-01 judgment reused; no publication implied."},
    {"name": "work", "index_sha256": "89830711e9596c395dcd0ba8751f8b6f5474138977f1c4b1c46d37afa670b05e", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "cd57990a1dc3efbc835c160db3c4260a1eb176c15509746328837ba41c9b1927", "status": "supported", "evidence": "W11 not selected; stale-grant observation from semantic-01 resolved by A2; same rule count; semantic-01 judgment reused."},
    {"name": "triage", "index_sha256": "89830711e9596c395dcd0ba8751f8b6f5474138977f1c4b1c46d37afa670b05e", "corpus_sha256": "25ac95be8936a9fd0d8e1556af02803f14c6fa885935431ccdb0094d0a5806f6", "query_sha256": "b39217d1c0b0b5b1833ca5b74c18eb864bdd6e144a55a41d0bdfe941f8d02d74", "status": "falsified", "reason": "F1: W11 selected with six identifiers and Product/Goals wording, classify-before-diagnose ordering and no repair authority retained, but the realization_refactor no-upstream-drift proof obligation required by SPEC_METHOD 4 and the scenario grant is absent from the delivered context."}
  ]
}
```