# Independent visual source-fidelity assessment: native A-bound STDO 3.1 visual

## 0. Assessor and limits

- **Who did this.** I am a Claude-family model. Host metadata reports `claude-opus-5-5`, and that metadata, not this text, binds my identity. I authored nothing in this subject. Per `SOURCE_BINDING.author`, the candidate Writer was Codex-family.
- **Tools.** I used none and wrote nothing. The host exposes an "advisor" tool that would forward this whole transcript to another model. I did not call it, because that would make this a joint judgment. That tool's presence means the "no tools" premise is not literally true of this host, and I make no claim of total-context isolation.
- **Selection dependency.** Codex chose and projected what I received, so this assessment is only as complete as that selection.
- **Supplied facts I could not recompute.** The digests in file headers, the manifest `ddbd3910…`, A's commit and tag, the model digests (canonical `10f810f0…`, file `bf696c10…`) and every Writer pass count are taken as supplied. I did not independently revalidate the omitted owner/context/kind scaffolding.
- **What I did check myself:**
  - I enumerated the headings of all three members and compared them with the 93 navigation records.
  - I counted SDLC_DEFAULTS lines to spot-check the grounding coordinates.
  - I checked the record arithmetic: 3 + 93 + 8 = 104 concepts, 93 + 6 = 99 relations, 93 + 1 = 94 residuals, 8 + 6 + 8 + 1 + 1 = 24 annotations, and 142,205 + 11,713 + 101,437 = 255,355 bytes.
  - I counted the 67 unselected standards members.
  - I compared each of the 24 annotations, field by field, with its cited quote and with the full member text.

## 1. Material findings

Severity is qualitative. The 1–5 scale is unconfirmed (G-08 from my expectations).

**F1 (moderate; record 8ac7ef58, the reuse/independence constraint).**
- **Trigger.** The record's `exceptions` field reads "A new role or conversation alone does not invalidate otherwise applicable work." That sentence is true and is inside the grounding quote (TICKETS ~1173–1188). But it is a separate reuse rule, not a case where the independence constraint stops applying. The source states no such exception.
- **Harm.** README says "Source-specific conditions and exceptions are explicit record fields", and the browser checks treat these fields as exceptions. If a reader takes an exception as a defeater, a fresh role or conversation appears to relax the independence requirement. That is the inference SDLC_DEFAULTS ("another actor name or a fresh context does not establish it") and TICKETS ("reusing the author's J cannot satisfy that condition") forbid. The statement text itself is correct.
- **Falsifier.** Either (a) the a_c `model/1` profile defines `exceptions` as free-form limits or nonclaims, which would make this a placement issue only, or (b) some source text makes a new role or conversation an exception to required independence. I found none.
- **Repair.** Move the sentence to the non-invalidation constraint a66cf400, where it already appears, or state it as a nonclaim.

**F2 (low–moderate; field-semantics pattern, an author claim).**
- Several qualifier fields hold nonclaims or obligations rather than source conditions or exceptions:
  - The exceptions on relations f7933543, e1ef9d99 and 178e4545 are "creates no …" nonclaims.
  - The `condition` on constraint b2725b81 ("Preserve selected gates and mandatory conditions") is an obligation, not an applicability trigger.
  - The `exceptions` on constraint c8e46679 are added rules.
- In most of these cases the meaning is still recoverable. The README's characterization overstates the fields' precision.

**F3 (low; record c8e46679, causal triage).**
- **Trigger.** The exception reads "insufficient observation keeps indeterminate and withholds the dependent claim". The source (SDLC_DEFAULTS lines 114–119) gives two lawful actions: acquire the missing admissible observation through its authorized route, *or* retain `indeterminate`.
- **Harm.** The primary corrective route is lost.
- **Falsifier.** The record shows the acquisition route.

**F4 (low; grounding/entailment gaps).**
- **Record 0e726b79.** Its clause "a summary or index supplies no work-state authority, governing meaning or current material evidence" comes from SDLC_DEFAULTS lines 73–74. That lies outside both cited grounds (lines 76–85 and TICKETS 731–744). By my line count the cited quotes do not contain it.
- **Record b7e39de5.**
  - Its condition ("reconcile effects needed by the next dependent action") is not in its only ground (TICKETS 731–744). It comes from SDLC lines 98–105 and ACTIVATION §5, and it drops "uncertain" and "before any repetition".
  - Its exception drops "the carrier" from the source's "cannot replace the carrier, governing sources or current evidence", and adds "summary".
- The meaning is faithful to the same members. But the Writer check "every declared source quote resolves" cannot detect statements the cited quote does not support.

**F5 (low; record 74980192, ticket creation).**
- "Required surviving state and ticket-state authority govern creation/update" weakens the source's necessary condition: "created or updated **only when** the table requires surviving state **and** the actor holds ticket-state authority."
- It also omits the rule that a generic request or model-widened scope cannot supply one-run authority.

**F6 (low; records 2de0fd46 and 75d9d582).**
- The concept 2de0fd46 states "disposable" without its source ground: the step records closed results and facts before returning. The recording constraint d7916c0e attaches to closed_result, not to actor_account.
- The latitude 75d9d582 forbids treating unresolved completion as *completed*. It does not forbid the reverse error, treating a missing trace as evidence of *no effect* (ACTIVATION §3 Effects; §5 "missing trace … is no evidence"). Its first forbidden item (no retry before reconciliation) mitigates this, and ACTIVATION §3 Effects is left as a residual.

**F7 (low; concept 1c1b407b, SDLC guidance).**
- The definition omits "the linked sections remain the single deciding owners", which is the guidance's standing.
- The rest of the definition ("projection of existing method law", "creates no … permission") and residual 30ac9621 ("not … a substitute constitution") largely carry it.

**F8 (low; structural).**
- All 94 residuals have an empty `re_entry` array.
- Re-entry is only textual, or carried through the section grounding and SOURCE_BINDING's hashed unselected list.
- For the cross-owner residual 30ac9621, the named owners (FOUNDATIONS, REFERENCE_FRAME, EVALUATION, SPEC_METHOD) have no in-model coordinates.

**F9 (evidence binding).**
- `browser-final-003/RESULT.json` binds the explorer by *path* only, with no `explorer.html` digest.
- `final-checks-001` binds the model file but not the HTML.
- So the browser observation is not tied by digest to the explorer bytes inventoried in STDO Representation manifest `f1e13206…`.
- **Falsifier.** A record of the explorer digest at observation time that equals the manifest member.

**Observations (not defects):**
- Containment edges are flat (member → section). Nesting is preserved only in labels and section URNs.
- The 24 annotations reach their source sections through grounding URNs, not through graph edges.
- The compact latitude label is a known UX limitation that loses no meaning, since the full payload is readable in the record.

## 2. Verdicts on the bounded claims

**Navigation and residual coverage: supported.**
- The navigation records cover every heading: ACTIVATION 29 (one h1, seven h2, 21 h3), SDLC_DEFAULTS 6 and TICKETS 58, for 93 in total.
- Headings inside fenced code in TICKETS §6 and §8 (for example "# SPRINT-…" and "## Migration Checklist") are correctly not treated as sections.
- All 93 sections carry `residual` with an honest "not comprehensively represented" consequence.
- The SDLC line coordinates I spot-checked match: 1, 3–7, 9, 11–17, 28, 36–43, 66, 76–85, 87–96, 98–105, 107, 114–119.

**Annotation source fidelity: supported for the declared bounded scope, with findings.**
- Every statement and definition is materially faithful.
- Direction is correct on all six authored relations:
  - frame basis → guidance;
  - carrier → context, work state and closed result, so ACTIVATION stays the owner (TICKETS §5 is an application, matching N-03);
  - current state → corrects the account;
  - owner ruling → bounds continuation.
- No record reverses a source rule or claims authority.
- Defects are confined to qualifier fields and grounding provenance (F1–F7). None of them needs a whole-claim falsification, provided F1 is repaired or its field semantics are disclosed. If the a_c profile gives `exceptions` defeater semantics, F1 becomes a fidelity defect in one record.

**Scope honesty and nonclaims: supported.**
- README, COVERAGE, SOURCE_BINDING limits, GENERATION standing, RELEASE.md and MIGRATION.md consistently disclaim:
  - whole-method semantics;
  - purpose-index role;
  - execution or authority, Lean/formal and Graphify execution;
  - independent acceptance.
- They keep the 3.0.5 model as history and keep the v2.5.1-rc.2 calculus coordinate separate from the represented 3.1 calculus.
- The 67 unselected members are listed with hashes.

## 3. V-04 and G-01 within the bounded visual claim

- **Satisfied as a declared-scope, source-matched model of A.**
  - It is freshly authored and binds A's commit, tag object, manifest, trees and the three member digests.
  - The member digest `a04335fe…` equals the previously assessed default projection.
  - It is not a rebinding of 3.0.5. The predecessor's nine top-level files are byte-conserved; subdirectories are not covered by that record.
  - This assessment supplies the required independent fidelity standing.
- **Unknown at the cohort level.** I cannot tell whether release §7's "release-matched STDO stack" accepts a three-member coverage declaration, or instead needs an explicit §8 narrowing in the release or cohort record. RELEASE.md narrows the claim in prose but never says "not a complete §7 stack". The cohort record was not supplied. That decision belongs to the owner and release record, not to this subject.

## 4. Mechanical and browser evidence: applicability and limits

**Applies, as computed facts I may consume (EVALUATION §3):**
- Model-file and canonical identities agree across README, GENERATION, RESULT, the projection and final-checks.
- The STDO Representation manifest `f1e13206…` agrees between RESULT and FINAL-INVENTORY.
- The stale-source refusal check restored the SDLC member to `a04335fe…`.
- Axiom convert/restore exact equality.
- Offline Chrome 157 run: 9 checks, 0 HTTP requests, 0 page errors.

**Limits:**
- These are Writer observations, not semantic verdicts.
- The browser checks sample one record per family (one relation, one constraint, one residual), not all 24.
- The run used `file://` on the candidate worktree, not packaged, installed or public bytes, so R3/R5 reruns remain needed.
- The browser result is not digest-bound to the explorer (F9).
- The jsdom DOM-harness lane was not performed.
- I did not see any screenshots.
- Pass counts (138/44, 34, 15/1) are not my judgment.

```json
{
  "subject": {
    "native_A_commit": "c1e0faaa8437c169031a476343c764614135cd93",
    "native_tag_object": "fca8d5e97cf2e945196aecdc33908bb190efdca5",
    "installed_manifest_sha256": "ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa",
    "model_canonical_sha256": "10f810f04d4fcf99424ea99631f461e108ee8030ce8145915eb5b9dbe8d14851",
    "model_file_sha256": "bf696c10177ffc393a3ae0279b3717fccb42d06d6092afd626d8efa245bc022f",
    "stdo_representation_public_manifest_sha256": "f1e132063af09d266c9aef908ea778253d22ede665c1bcf6762d33b4d8e124e8",
    "population": "24 authored annotations + 93 navigation/residual sections over ACTIVATION (56109ffa), SDLC_DEFAULTS (a04335fe), TICKETS (2e601f70)",
    "assessor": "Claude-family (host metadata authoritative); single author; advisor tool exposed but not called; no total-context isolation claimed"
  },
  "status": "supported",
  "findings": [
    {"id": "F1", "severity": "moderate", "record": "8ac7ef58 (reuse_preserves_independence)", "issue": "exceptions field holds an adjacent non-invalidation rule, not a source exception; defeater reading would relax independence contrary to SDLC_DEFAULTS and TICKETS", "falsifier": "a_c profile defines exceptions as free-form limits, or source text making a new role or conversation an exception to required independence (none found)"},
    {"id": "F2", "severity": "low-moderate", "records": "f7933543, e1ef9d99, 178e4545, b2725b81, c8e46679", "issue": "qualifier fields hold nonclaims or obligations; README overstates them as source-specific conditions and exceptions"},
    {"id": "F3", "severity": "low-moderate", "record": "c8e46679", "issue": "drops 'acquire the missing admissible observation' alternative; keeps only retain-indeterminate"},
    {"id": "F4", "severity": "low", "records": "0e726b79, b7e39de5", "issue": "clauses not supported by their cited quotes (sourced from SDLC 73-74 and 98-105); b7e39de5 exception drops 'the carrier'"},
    {"id": "F5", "severity": "low", "record": "74980192", "issue": "'govern' weakens 'only when ... and' necessary condition; omits generic-request and model-widened-scope exclusion"},
    {"id": "F6", "severity": "low", "records": "2de0fd46, 75d9d582", "issue": "'disposable' stated without its recording-before-return ground; latitude forbids only the unresolved-to-completed error, not missing-trace-as-no-effect"},
    {"id": "F7", "severity": "low", "record": "1c1b407b", "issue": "omits 'linked sections remain the single deciding owners'"},
    {"id": "F8", "severity": "low", "records": "all 94 residuals", "issue": "re_entry arrays empty; cross-owner residual 30ac9621 lacks structured owner coordinates in-model"},
    {"id": "F9", "severity": "low", "subject": "browser-final-003", "issue": "browser observation bound to explorer by path, not digest", "falsifier": "observation-time explorer.html digest equal to the STDO Representation manifest member"}
  ],
  "supported_claims": [
    "93/93 source headings (29/6/58) represented as navigation sections with residual dispositions; fenced-code pseudo-headings correctly excluded",
    "record arithmetic and selected byte total consistent",
    "all 24 annotation statements and definitions materially faithful; all 6 authored relation directions correct; no authority or execution claim",
    "TICKETS §5 represented as an application of ACTIVATION §2/§5/§7 with no added carrier requirement",
    "scope, nonclaims, historical non-rebinding and calculus-coordinate separation honestly declared",
    "V-04 / G-01 satisfied as a declared-scope fresh A-bound model, with this assessment as the independent fidelity standing"
  ],
  "unperformed_or_excluded": [
    "a_c model/1 profile field semantics for conditions and exceptions (decides F1 severity)",
    "whether release §7 accepts three-member coverage without explicit §8 cohort narrowing (cohort record not supplied)",
    "independent revalidation of omitted owner/context/kind scaffolding",
    "manifest-membership recomputation of the three member digests against A",
    "screenshots, packaged/installed/public explorer reading, jsdom harness lane",
    "non-STDO visual path, Graphify, whole-method, formal and host-pickup claims (excluded by source)",
    "release, owner acceptance and publication verdicts"
  ],
  "evidence_limits": [
    "digests and pass counts are operator/Writer-supplied; not recomputed",
    "line coordinates spot-checked on SDLC_DEFAULTS only",
    "browser checks were Writer observations on the candidate worktree over file:// on one host, sampling one record per family",
    "predecessor conservation covers nine top-level files only",
    "single-author assessment over a Codex-selected packet"
  ]
}
```
