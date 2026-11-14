# Bounded independent recheck of visual findings F1–F9 on model `784aa60f…`

**Verdict: supported.** F1–F7 are repaired in all 12 changed records. None of those records gained a material defect. F8 is still open but now honestly disclosed as a low limitation. F9 is closed: the browser run is tied by digest to the explorer, though I could not check that digest against the manifest bytes myself. The new RELEASE.md wording settles the earlier G-01 ambiguity in its text.

## 0. Who did this, and the limits

- **Who.** I am a Claude-family model. Host metadata reports `claude-opus-5-5`, and that metadata, not this text, binds my identity. I authored nothing in this subject. Per SOURCE_BINDING, the Writer was Codex-family.
- **Tools.** I used none and wrote nothing. The host still exposes the "advisor" tool. As you instructed, I did not call it, so this is my judgment alone. Because the tool exists, I make no claim of total-context isolation.
- **Facts taken as supplied, not recomputed:**
  - all digests;
  - the 306/12/294 record-equality comparison;
  - "native source and provider runtime unchanged";
  - FINAL-HASHES `browser_bound_to_manifest: true`;
  - the Writer and browser pass results.
- **Not seen:**
  - the manifest `d8a46da4…` itself;
  - the changed top-level `id` and `interpretation` values;
  - native RELEASE §7/§8 text;
  - screenshots.
- **Not mine:** release, publication and owner-acceptance decisions.
- **What I checked myself:**
  - I compared each changed record, field by field, against its cited quotes and the full member text.
  - I checked every new quote word for word against the members. All match exactly.
  - I checked the new line ranges by counting lines relative to anchors I had already spot-checked:
    - SDLC 68–74 sits under the heading at line 66.
    - SDLC 112 is the fourth line after the "Causal triage" heading at 107, and the table starts at 114.
    - ACTIVATION 1381–1388, 1460–1469 and 1485–1492 are consistent with one another. I did not fix their absolute position in the file.
    - ACTIVATION 1707–1716 matches only the quote's own length (10 lines).
  - I confirmed that the 12 keys in ANNOTATION-DELTA match the 12 record IDs in AFFECTED-RECORD-DELTA.
  - In every changed record, `id`, `applies_to`, `source`/`target`, `kind`, `owner`, `scope`, `basis` and `context` are unchanged.

## 1. Disposition of the original findings

**F1 (record 8ac7ef58): repaired.**
- The exceptions field is now `[]`. The remaining condition, "Independent assessment is required by the actual governing boundary", is a real applicability trigger from TICKETS ("Required independent assessment…").
- The non-invalidation rule survives only in the separate record a66cf400. The browser run also observed this.
- No reading of the record can now let a new role or conversation relax required independence.

**F2 (qualifier fields holding non-qualifiers): repaired for all five records named.**
- f7933543 and e1ef9d99: the bindings and the "creates no additional carrier requirement / confers no ticket-state authority" nonclaims now sit in `meaning`. Conditions and exceptions are `[]`.
- 178e4545: "recording creates no new grant" moved into `meaning`. What remains in the qualifier fields is genuine:
  - the condition is the source's "while it applies";
  - the exception is the source's defeater, "new ambiguity or a materially changed decision returns only the affected question".
- b2725b81: the obligation "Preserve selected gates…" moved into the statement.
- c8e46679: everything moved into the statement.
- COVERAGE's sentence "Source-specific conditions and exceptions are explicit record fields" is now accurate for these records.

**F3 (record c8e46679, causal triage): repaired.**
- The statement now gives both lawful routes: acquire the missing admissible observation through its authorized route, *or* retain `indeterminate` and withhold the dependent claim. It also keeps "Repetition of the same uninformative check…".
- The new ground (SDLC line 112) supports the evidence-distinguishing sentence.
- Paraphrasing "inadequate governing requirement or design" as "inadequate governing law" was already there and is acceptable.

**F4 (grounding and entailment gaps): repaired.**
- 0e726b79: a third ground (SDLC 68–74) now contains "a context summary or index supplies none of them by itself", so the cited quotes now entail the clause.
- b7e39de5:
  - Its new ground (ACTIVATION 1381–1388) supports "recover applicable progress, re-check … invalidators, reopen only affected support, reconcile uncertain external effects sufficiently for the next dependent action before any repetition or dependent action" and "resumption does not imply idempotence". "Uncertain" and "before any repetition" are restored.
  - The account clause now reads "cannot replace the carrier, governing sources or current evidence". That matches TICKETS, and the added "summary" is gone.

**F5 (record 74980192, ticket creation): repaired.**
- It now states the necessary condition: created or updated "only when the carrier-selection table requires surviving state **and** the actor holds ticket-state authority".
- It also adds the one-run authority rule and the exclusion of a generic request or model-widened scope.
- Writing "Product-authorized" where the source has "product-authorised", and omitting "to create a durable record", do not change the meaning.

**F6: repaired in both parts.**
- 2de0fd46: "disposable" now carries its ground, "because a step records its closed results and step-produced facts before it returns".
- 75d9d582: a third forbidden item now rules out treating a missing trace as evidence that work was not done, that an effect did not occur, or that it ended. It is grounded on ACTIVATION 1485–1492, and the quote matches exactly.

**F7 (record 1c1b407b): repaired.** The definition now includes "The linked sections remain the single deciding owners."

**F8 (empty `re_entry` arrays): retained, low, honestly bounded.** See §3.

**F9 (browser evidence binding): closed, with one limit.** See §4.

## 2. Did the 12 changed records gain new defects?

No material defects were introduced. Relation directions are unchanged, so ACTIVATION still owns the rules TICKETS §5 applies; the prior N-03 judgment still holds. No record reverses a source rule or claims authority.

Non-blocking observations:

- **O1 (178e4545; pre-existing, not introduced).** `meaning` drops the source's "J is not O" (a recorded judgment is not an owner ruling). It keeps "recording a ruling or judgment cannot create … beyond the original grant", so nothing is inverted. Low.
- **O2 (75d9d582; provenance precision).** The new ACTIVATION 1485–1492 ground was attached to `allowed_variation` as well as `forbidden_variation`. It supports only the new forbidden item. This over-attaches provenance but asserts nothing false. Negligible.
- **O3 (a66cf400; outside the batch, unchanged).** Its second exception, "Changed coordinates alone establish neither claim failure nor success", is a nonclaim-like limit on what invalidation implies. My prior assessment did not flag it. It cannot be read as relaxing any rule. I record it for completeness only; it is not a reopened finding.
- **Limit of the Writer checks.** "Every declared source quote resolves" still cannot detect a gap between a statement and its quote. My own comparison above covers that for these 12 records only.

## 3. F8: is it honestly bounded?

- **The fact itself (supplied):** all 94 `re_entry` arrays are empty.
- **The disclosure (current COVERAGE.md):** it states the empty arrays outright. It says re-entry comes only from the textual consequence, the source grounding and SOURCE_BINDING's hashed inventory. It says named cross-owner dependencies have no in-model owner coordinates, and that the visual "supplies no automatic cross-owner context closure".
- **My judgment:** this is an honest, explicit limitation that matches what I found. It stays a low structural finding, not repaired. It is acceptable under the narrowed claim.

## 4. F9: does the explorer digest close the evidence binding?

**What the evidence shows:**
- `browser-final-004/RESULT.json` records the explorer `artifact_sha256` `2ab25f47…` (3,562,244 bytes) and the same value in `artifact_sha256_after`. A dedicated check reports it "unchangedDuringObservation".
- That digest equals `explorer_sha256` in both FINAL-HASHES and INPUT_READBACK.
- The run also reports model `5e1b2b5f…` with canonical digest `784aa60f…`, matching README, GENERATION and FINAL-HASHES.

**Judgment:** this meets the falsifier I set, an observation-time digest equal to the inventoried member. The one remaining link is the manifest itself: that its entry for `explorer.html` is `2ab25f47…` is the operator's statement (`browser_bound_to_manifest: true`), and I did not recompute it from `d8a46da4…`.

**Still open (unchanged):**
- The run used `file://` on the candidate worktree, so packaged, installed and public reruns (R3/R5) are still needed.
- It is a Writer observation on a single host.
- It now adds targeted F1 checks but still samples records rather than reading all 24 annotations in the UI.
- There is still no jsdom harness lane and no screenshots.

## 5. G-01 against the current RELEASE.md wording

**Earlier ambiguity:** the text never said "not a complete §7 stack".

**Current wording:** RELEASE.md now says that "under RELEASE §8, visual qualification is expressly narrowed to the selected ACTIVATION, SDLC_DEFAULTS and TICKETS documentation". It also says the successor "does not claim the complete whole-method semantic stack described by the historical five-Product RELEASE §7 profile", while keeping §7's dependency, complete-ref and atomic-publication duties.

**Judgment:** that removes the ambiguity in wording, and the narrowed claim matches this subject's declared scope.

**Still not assessed:**
- whether native RELEASE §8 permits this narrowing, and under what owner authority (the member is unselected and its text was not supplied);
- the cohort record.

Those decisions belong to the owner and the release record.

## 6. Prior judgments reused, and under what conditions

These prior judgments apply to model `784aa60f…` because they concern record values the operator reports as byte-equal, plus unchanged sources:

- Navigation and residual coverage: 93 out of 93 headings (29 ACTIVATION, 6 SDLC_DEFAULTS, 58 TICKETS); fenced pseudo-headings correctly excluded; all 93 residual dispositions present.
- Record arithmetic and byte totals: unchanged per GENERATION and COVERAGE.
- Fidelity of the 12 unchanged annotations, including record a66cf400.
- Direction of all six authored relations, re-confirmed from unchanged `source`/`target` on the four that changed.
- Scope honesty, historical non-rebinding, separation of the calculus coordinate, and the 67-member unselected list. I re-read the current README, COVERAGE and SOURCE_BINDING; they are consistent with these.

**Not carried forward:** the prior "supported" verdict was bound to model `10f810f0…` / `bf696c10…` and stays as history. The verdict here is new, for `784aa60f…` / `5c1ef148…`, and is built from those reused judgments plus my fresh judgment on the 12 changed records.

```json
{
  "subject": {
    "native_A_commit": "c1e0faaa8437c169031a476343c764614135cd93",
    "native_tag_object": "fca8d5e97cf2e945196aecdc33908bb190efdca5",
    "installed_manifest_sha256": "ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa",
    "model_identity": "urn:a-c:generation:c8b565861ea509feddf2ebd4:model:5e1b2b5f8f9ed32537efefe0",
    "model_canonical_sha256": "784aa60f81eb2e9c4612ce0062a1e34c459088615692d672a0834021edfacde3",
    "model_file_sha256": "5c1ef1485ec7f470c42dada810f15fe4d66200a7140a14eb1d185c0fd8bb51cb",
    "stdo_representation_public_manifest_sha256": "d8a46da4e3fcce75ef9e761fe172d3e8ba583d2fd973c447a9fb324388b950f7",
    "explorer_sha256": "2ab25f47a5f99575c7c93bfff3a57a3241d22925dbfb69068fdf1c9b453007e5",
    "recheck_population": "12 changed records (0e726b79, 74980192, 8ac7ef58, b2725b81, c8e46679, 75d9d582, 1c1b407b, 2de0fd46, f7933543, b7e39de5, e1ef9d99, 178e4545) plus F8/F9 evidence and the RELEASE.md section-8 narrowing wording",
    "predecessor_subject_history": "model 10f810f0.../bf696c10..., manifest f1e13206...; prior verdict retained as history, not relabelled",
    "assessor": "Claude-family (host metadata claude-opus-5-5 authoritative); single author; no tools used; advisor tool exposed but not called per instruction; no total-context isolation claimed"
  },
  "status": "supported",
  "finding_dispositions": {
    "F1": {"disposition": "repaired", "basis": "8ac7ef58 exceptions emptied; remaining condition is a source applicability trigger; non-invalidation rule only in separate a66cf400"},
    "F2": {"disposition": "repaired", "basis": "nonclaims/obligations moved from qualifier fields to meaning/statement in f7933543, e1ef9d99, 178e4545, b2725b81, c8e46679; remaining qualifiers on 178e4545 and 8ac7ef58 are genuine source conditions/defeaters"},
    "F3": {"disposition": "repaired", "basis": "c8e46679 now states acquire-observation OR retain indeterminate, grounded on SDLC 114-119 plus line 112"},
    "F4": {"disposition": "repaired", "basis": "0e726b79 gains SDLC 68-74 ground entailing summary/index clause; b7e39de5 gains ACTIVATION 1381-1388 ground, restores 'uncertain', 'before any repetition' and 'the carrier', drops added 'summary'"},
    "F5": {"disposition": "repaired", "basis": "74980192 states 'only when ... and' necessary condition and the generic-request/model-widened-scope exclusion"},
    "F6": {"disposition": "repaired", "basis": "2de0fd46 states disposability ground; 75d9d582 forbids missing-trace-as-no-effect/not-done/ended, grounded on ACTIVATION 1485-1492"},
    "F7": {"disposition": "repaired", "basis": "1c1b407b definition includes 'linked sections remain the single deciding owners'"},
    "F8": {"disposition": "retained_disclosed", "severity": "low", "basis": "94 empty re_entry arrays explicitly declared in COVERAGE.md with textual/grounding/SOURCE_BINDING re-entry route and no automatic cross-owner closure claim"},
    "F9": {"disposition": "closed_with_limit", "basis": "browser-final-004 records explorer sha256 2ab25f47... before and after observation, equal to FINAL-HASHES and INPUT_READBACK explorer digest, with model 784aa60f...; manifest d8a46da4 membership of that digest is operator-asserted, not recomputed"}
  },
  "remaining_findings": [
    {"id": "F8", "severity": "low", "status": "open_disclosed", "issue": "structured re_entry arrays empty; cross-owner residual 30ac9621 lacks in-model owner coordinates"},
    {"id": "O1", "severity": "observation", "record": "178e4545", "issue": "meaning omits source 'J is not O'; pre-existing, not introduced; no inversion"},
    {"id": "O2", "severity": "observation", "record": "75d9d582", "issue": "ACTIVATION 1485-1492 ground also attached to allowed_variation, which it does not support; provenance over-attachment only"},
    {"id": "O3", "severity": "observation", "record": "a66cf400 (unchanged, outside batch)", "issue": "second exception is a nonclaim-like limit; cannot be read to relax any rule; not a reopened finding"}
  ],
  "reused_prior_claims": [
    {"claim": "93/93 heading navigation coverage (29/6/58) with residual dispositions; fenced pseudo-headings excluded", "applicability": "operator-reported byte equality of 294 unchanged records and unchanged native members"},
    {"claim": "fidelity of the 12 unchanged annotations including a66cf400", "applicability": "operator-reported byte equality"},
    {"claim": "direction of all 6 authored relations; TICKETS section 5 as application of ACTIVATION owners (N-03)", "applicability": "source/target/kind unchanged in delta for the 4 changed relations; others byte-equal"},
    {"claim": "scope honesty, nonclaims, historical non-rebinding, calculus-coordinate separation, 67 unselected members listed", "applicability": "re-read in current README, COVERAGE, SOURCE_BINDING, GENERATION"}
  ],
  "g01_assessment": {
    "prior": "unknown at cohort level (no explicit section-8 narrowing wording)",
    "current": "wording ambiguity resolved: RELEASE.md explicitly narrows visual qualification under section 8 to the three selected members and disclaims the historical section-7 whole-method stack while retaining section-7 dependency/ref/atomic-publication duties",
    "not_assessed": "lawfulness and authority of the narrowing under native RELEASE section 8 (member text not supplied); cohort record"
  },
  "limits": [
    "digests, 306/12/294 equality, native/provider unchanged and manifest membership of the explorer digest are operator/Writer-supplied, not recomputed",
    "changed top-level model 'id' and 'interpretation' values not supplied or assessed",
    "new line coordinates checked by relative counting only (SDLC 68-74 and 112 against prior anchors; ACTIVATION 1381-1388, 1460-1469 and 1485-1492 mutually consistent; 1707-1716 by quote length only); absolute ACTIVATION offsets not independently anchored",
    "browser evidence is a Writer observation over file:// on the candidate worktree on one host; packaged/installed/public reruns (R3/R5), jsdom lane and screenshots not performed or seen",
    "native RELEASE section 7/8 text, cohort record and manifest d8a46da4 not supplied",
    "no general UX, non-STDO visual, Graphify, formal/Lean, whole-method or host-pickup predicates assessed",
    "release, owner acceptance, publication and B exact-ref closure remain later and are not decided here",
    "single-author assessment over a Codex-selected packet"
  ]
}
```
