I'll start by reading only the basis material and predecessor sources, then write expectations before I open any candidate material.

## EXPECTATIONS (stated before I open any candidate, account, conservation, evidence or prior-review material)

**What I read first:** basis/INTENT.md, basis/PRODUCT.md, basis/requirements/README.md, basis/conformance/README.md and the first 60 lines of PREDECESSOR_CLAIMS. From the predecessor I read UX_METHOD (all of it), README, WRITING_GUIDE, POSTING_GUIDE and GLOSSARY_GUIDE (all of them), the TOP sections Position/Scope/Imported Boundary (L1–100), Authority And Adoption (L1042–1071) and Exclusions/Conformance (L1190–1241), ODD §1–3 (L1–125), and BASELINE Status/Applicability/Empirical Revision (L72–181). I also have the heading lists of ODD, WM, TOP and BASELINE. Not yet read: the rest of the predecessor bodies, the templates and schemas, ASSURANCE, A_C_DEPENDENCY, PRINCIPLES and CAPABILITIES.

**What I expect the candidate's primary members to do:**

1. **E1 – Optional profiles stay optional.** TOP, ODD (the typed-graph form), UX, WM and the BASELINE frame catalogue/Executive must each keep a selection boundary. Availability is not adoption. An absent or incomplete adoption leaves the profile inactive (TOP L1062, BASELINE L111–115). Generic law must not live only in an optional profile (README req. 8; discriminators L20 and L24). This applies especially to the generic outcome-driven transition law (construction, evaluation, continuation, recovery, termination) and to the result algebra and frame law. Those belong to Foundations or the Spec Method, not to ODD or BASELINE.
2. **E2 – No executor is assumed.** ODD's ABG/GTL roles and UX's TEA must not become method machinery. Human or mixed realisation is allowed (binding req. 2, discriminator L56). The direct single-Worker route must survive with no required Executive (BASELINE L121–137, discriminator L45).
3. **E3 – Results are stated in the one algebra.** Every domain outcome set must refine the core result algebra with a mapping, a predicate and an original-domain value, and never raise standing. This covers the UX sprint classes `accepted/local_paydown/design_reframe/requirement_reprice/product_reprice/remove`, the TOP judgment/stop/residual kinds, the BASELINE work result (`candidate_ready/refused/incomplete/re_entry_requested`), triage, severity/priority/boundary effect, failure classification, and the WM assurance and evidence hierarchy. Conjunction is defined once, in Foundations.
4. **E4 – The UX conflict stays open.** The three predecessor compliance tests disagree: §12 says "§4–§10 hold and §14 absent", §18 says "§4–§10 and §14", and §8A/§11/§13A add closure duties. Which determination replaces them is an open owner decision (PRODUCT L433). The candidate must not silently pick one. It must keep the fail-closed ambiguity rule (UX §1A) in force, and the affected rows must be pending, not conserved or superseded.
5. **E5 – Ownership is single.** The GLOSSARY successor stays a non-deciding index whose rows resolve to existing successor owners, with no definitions and no stale predecessor anchors. WRITING and POSTING keep their conventions. POSTING keeps the commentary-versus-authority distinction, the Draft/Open/Closed mutability rule, carrier binding and the UP-012 authority-causality chain, or dispositions for each.
6. **E6 – The standards README conserves its content.** That means the member set, the optional TOP adoption, the non-deciding index, the logical URIs/no-local-paths rule and the authority sources. Ordinary entry must not mark a target version as released (standalone req. L56).
7. **E7 – Templates and schemas carry their own claims.** Templates must not encode a fixed role inventory or a software-only layout as required. Schemas must not require ABG, a code carrier or an event stream.
8. **E8 – WM keeps the Markov distinction.** An ordinary bounded object is not a Markov object without evidence. The epistemic overlay and the source-sovereignty laws are conserved or disposed.
9. **E9 – Changed scope (the generic assessment, five carrier dependencies and inverse consumer metadata).** Inverse consumer metadata must not claim consumer relations the source lacks. A positive relation recorded in one direction must have its inverse. A blank field must not stand as coverage (standalone req. 1). The eleven unmatched positive relations must stay explicitly unresolved, not be reported as satisfied.
10. **E10 – Criterion 4 stays unresolved.** No actual-use trial was performed, so frame-use and context-fit judgments must remain unresolved.

Now opening the candidate.

I've checked the UX member against its source. Now I'm looking at the author's UX conservation claims for the changed Cmd/outcome determinations.

Next I'm reading the profile-binding headers of TOP, ODD and WM, plus the start of BASELINE.

I'm reading the shared Foundations result algebra/conjunction and bounded construction sections, plus the candidate glossary and posting guide.

I'm checking the changed-scope receipt to see what changed in my members (two BASELINE rows).

I'm checking how ODD's closure decision sum type (A8) maps into the core result.

Posting/Writing conservation looks questionable. I'm checking whether the prior closed reviews already covered these rows.

## FINAL REVIEW: Codex STDO v3 candidate `ea27616b`, source/domain partition

**Bottom line:** the members in this partition are **not ready for acceptance**. I found two confirmed defects, both medium. Several required judgments are also still pending, and the shared actual-use trial was not run, so criterion 4 can't be satisfied. Nothing here amounts to acceptance, release, a winner or proof for the whole candidate.

**Ordering:** I read basis/INTENT, PRODUCT, requirements/README and conformance/README first, then the predecessor sources, and posted EXPECTATIONS (E1–E10) before opening any candidate, account, conservation, evidence or prior-review file.

### Confirmed defects

**D1 (medium): three UX compliance tests disagree, and the open owner decision is not recorded anywhere in the candidate.**
- **Where:** `candidate/standards/UX_METHOD.md:172` and `:186` (§4A: a realisation is compliant if it preserves §4–§8). `:416` (§12: §4–§10 hold and the §14 failure patterns are absent). `:623` (§18: §4–§10 plus §14). `:537` and `:300` (closure also requires the §8A replay proof and §11 accessibility).
- **What's missing:** the Governing Relations table (`:31–39`) never mentions the conflict. The account marks the 4A, 12 and 18 rows `conserved` (conservation-by-source/UX L321, L942, L1396) and never cites `basis/PRODUCT.md:433`, which says the replacement for these tests is still an open owner decision. A grep found no candidate or account text acknowledging the conflict.
- **Trigger:** a surface that preserves §4–§8 but skips runtime validation at an untrusted seam. §4A calls it compliant; §12 and §14 item 14 call it a violation. A second case: a surface where §4–§10 hold but there is no §8A replay proof. §12 calls it compliant; §13B (`:537`) withholds closure.
- **Consequence:** three places in one candidate decide "method-compliant" differently, which is a counterexample under single-ownership req. 7 and discriminator L60. Copying the predecessor text word for word, with the §1A fail-closed rule still in force, is lawful conservation. What is missing is any record of the conflict. Without that, consumers and a_c projections can pick one test without anyone noticing.
- **Smallest repair (UX owner):** add one clause to UX Governing Relations. It should name the three tests and the pending PRODUCT decision, and state that §1A fail-closed governs until a replacement is accepted. Carry that clause as an interpretation residual, and cite the decision in the 4A, 12 and 18 rows.

**D2 (medium): `POSTING_GUIDE#boundary` is labelled `conserved`, but its required work changed.**
- **Where:** `candidate/standards/POSTING_GUIDE.md:21–27` adds a duty before publishing any review or handoff: apply Workspace and context, and report any judgment as a complete core result record (predicate, subject, basis, verdict, performance, outcome, evidence, unresolved items and effects).
- **Account:** the row (conservation-by-source/POSTING L3–15) is `conserved` and lists only `POSTING_GUIDE.md#boundary`. It omits `FOUNDATIONS#result-algebra` and `#workspace-and-context`, so the criterion 1 locus list is incomplete.
- **Trigger:** a REVIEW post whose analysis says, in prose, that a design is unsafe. That conforms to the predecessor and does not conform to the successor.
- **Consequence:** under the disposition requirement, a changed obligation needs a named replacement relation and an owner decision. A general common requirement does not accept specific changed meanings (PRODUCT L224).
- **Smallest repair (choose one):** limit the clause to judgments a post offers as assessment results. Or mark the row `superseded`, pending, tied to the shared result-algebra replacement, and add the two Foundations loci.
- **Same pattern, low severity:** `WRITING_GUIDE.md:106–108`, where a writing review must use the core result.

### Disputed (not counted as defects)
- **Glossary wording tension:** `GLOSSARY_GUIDE.md:7–8` says the file declares no "disambiguation", but `:44–70` is a table separating the senses of one label. Its own text says it adds no definition or precedence, so this is low severity.
- **Writing qualifier:** `WRITING_GUIDE.md:116,127` adds "within the owning authority" to the delete/supersede instruction. I read this as making explicit an authority that already applied, which is conservation, so I didn't count it.
- **Common-inventory gap (for the common pen, not a candidate defect):** PREDECESSOR_CLAIMS has no row for the POSTING_GUIDE H1 body (predecessor L3–15). The candidate does carry that text word for word (`:5–15`).

### Supported within what I read
- **TOP stays optional:** an absent adoption leaves it inactive (`TRAVERSAL_OCCURRENCE_PROFILE.md:6,36,63–71`).
- **Generic outcome-driven law sits in Foundations, not ODD:** `FOUNDATIONS.md:907–996`, plus the optional Executive at `:1016`. This holds for discriminators L20 and L24.
- **Changed generic assessment is executor-neutral, with direct Writer entry kept:** `SPEC_METHOD.md:1886–1922` (L45, L56). The author's case set includes a human procedure.
- **Domain outcomes map into the core with reasons, and none raises standing:** BASELINE work result (`:555–596`) and boundary effect (`:544–553`), ODD A8/A9 (`:1197–1235`), UX §8A replay (`:324–339`), WM eligibility versus decision (`:44–60`), TOP judgments (`:754–806`).
- **Foundations result algebra and conjunction:** read in full (`:322–579`); consistent with the requirement.
- **UX §5, §6 and §8A replacements:** honestly recorded as `proposed_pending_owner_decision` with `owner_decision: null`.

### Changed scope and the eleven unmatched relations
- I sampled one of the eleven unmatched positives: FOUNDATIONS.construction-assurance listing BASELINE.assurance-subject-acquisition-and-evaluation as a consumer. The BASELINE source (`:1244`, `:1256`) does cite the subsections `#assertions-and-observations` and `#parallel-assurance-and-provenance`. So the relation is real at subsection level, not stale; the reciprocal just belongs at the subsection rows. It stays open for the owner.
- I did not assess the other ten, the 100 inverse projections or the five carrier calls.

### Coverage
- **Read in full, both sides:** UX, POSTING, standards README; predecessor WRITING and GLOSSARY.
- **Partly read:**
  - WRITING candidate: 60–146 only (rows Core Rule through Good Prose unassessed).
  - GLOSSARY candidate: 1–80, plus an anchor check.
  - TOP: 1–80 and 752–806.
  - ODD: 1–110 and 1180–1250.
  - WM: 1–64.
  - BASELINE: 1–80, 500–600, 790–860 and 1222–1262.
  - FOUNDATIONS: 322–579 and 907–1022.
  - SPEC: 1886–1960.
- **Templates and schemas:** grep only. That supports E7 for the frame-basis template, which keeps its optional Executive. Nothing else there was assessed.
- **Predecessor rows actually assessed:**
  - UX: all 24 by text comparison, but dispositions checked for only 4A, 5, 6, 8A, 12 and 18. Note: 13B moves classification to Ticket; I didn't check that row's disposition.
  - POSTING: all 9. Eight are word-for-word and supported; one has D2.
  - WRITING: 5 of 9.
  - README: 1.
  - GLOSSARY: 2 of 14.
- **Unassessed:** every other ODD, WM, TOP and BASELINE row, every template and schema row, and the `TICKET#sprint-close-review` binding.
- **Reuse:** none. The prior closed reviews don't cover these rows. The BASELINE amendments they judge (R007, R009) were neither checked nor relied on here.

### Six criteria (this partition only)

| # | Criterion | Judgment and why |
|---|---|---|
| 1 | Disposition completeness | Rows I checked each have one disposition. The POSTING#boundary locus list is incomplete (D2). |
| 2 | Conservation | Supported for 8 POSTING rows and the word-for-word UX rows. D2 is a counterexample. |
| 3 | Accepted replacements | Not satisfied: UX §5, §6 and §8A are still pending owner decisions. |
| 4 | Actual use / context fit | Indeterminate: no trial was run and context fit was not measured. |
| 5 | Fidelity / conformance | D1 is a counterexample for UX. The other discriminators I checked are supported within my reading. |
| 6 | Governing reduction | Not established: no deciding-path comparison was done, and D1 is a counterexample for UX. |

### Resources
- **Spend:** about $3.5 of the $6 allowance, by the running meter.
- **Elapsed time and context:** not available to me; the parent has the measured values.
- **Stopped early:** I stopped short of full coverage to stay within budget. Everything listed as unassessed above remains open; I have not marked any of it satisfied.
