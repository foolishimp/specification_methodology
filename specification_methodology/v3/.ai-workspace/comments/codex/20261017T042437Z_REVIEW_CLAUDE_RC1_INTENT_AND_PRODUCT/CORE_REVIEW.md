# Independent core content review — Claude candidate

Closed source-first assessment, 2026-10-17. This is the return for partition A; it is evidence for the parent's review and confers no acceptance.

## Judgment

The inspected core substantially implements the intended method in operative rules. It connects current state and selected destination to construction, evaluates preservation separately from progress, retains missing work and uncertain effects, diagnoses implementation/specification/model/observation discrepancies, and supports recovery and targeted evidence reuse. These conclusions come from following concrete cases through the deciding source, not from headings, trace tables or the author's tests.

It does **not** completely preserve the common assurance requirement through its consumers. One confirmed medium defect makes a predicate-sufficient observation inconclusive merely because it does not distinguish every subject. The foundation states the correct relation; an ordinary assurance consumer strengthens it incorrectly. This is a present-law defect, independent of deferred formal coverage and actual-use work.

Source inspection alone does not establish that this method delivers ordinary tasks reliably, reduces reasoning cost relative to rc.2, fits an actor's active context, or meets all Product qualification conditions. No empirical or release acceptance is inferred here.

## Basis, independence and limits

- Common WHAT: `4c340f7adec9f3c893e3e267b23e4cadeb357854:specification_methodology/v3/specification/`.
- Candidate: `af3b8b7107c92a216cc53d629ddeefecd7f77fca:specification_methodology/v3/build_tenants/claude/`.
- In the references below, **common** paths are relative to the first subtree; **candidate** paths are relative to its `standards/` directory. A path and line range always refer to the pinned Git object, never the live Claude worktree.
- Expectations in [CORE_EXPECTATIONS.md](CORE_EXPECTATIONS.md) were written after the complete common Intent, Product, requirements README, ASSURANCE and PRINCIPLES, before acquiring candidate prose. I did not author the common source or the candidate. The parent disclosed authorship of common material and a competing candidate.
- The parent supplied source questions during review and later corroborated the observation-sufficiency issue after my independent detection. Its finite parity example sharpens the counterexample below. This coordination is disclosed; it is not additional independent-assurance credit.
- Applicable apps/repository/v3 `AGENTS.md` and the review activation were read. Installed builder v2.5.1-rc.2 verification is reused from the parent's current-turn verification, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- The recorded owner scope at `c5209f00` defers complete a_c coverage, remaining actual-use sets and authority compressions/projections. I do not classify those omissions as new baseline defects.
- Candidate/common acquisition used exact `git show` objects only. No Claude live-worktree content, authored tests, grading, frontier judgments, review returns or earlier reviews supplied conclusions. Normative references to their existence inside standards were read as source text, not as evidence that their claims were met.
- No candidate, common-law, ticket, Git, network or paid external effect was performed. No broad suite or new test machinery was used. Only the two granted review artifacts were written.

## Confirmed finding

### CORE-F1 — P2 / medium: assurance acquisition demands subject separation instead of predicate separation

**Owning defect:** candidate `ASSURANCE.md:681–686`, in §11 Assurance subject acquisition and evaluation.

The operative instruction is: “Where the acquired observation cannot separate two admissible subjects, the frame returns further evidence, a justified narrower scope or `indeterminate`”. Neither that sentence nor its local context qualifies the two subjects by different truth values of the evaluated predicate. The surrounding acquisition law at `ASSURANCE.md:672–702` concerns actual owner-issued subjects, independently derived oracles and supported observation bindings; it supplies no definition under which “two admissible subjects” means only subjects with opposite predicate truth.

**Governing requirement:** common `requirements/ASSURANCE.md:49–56` requires:

```text
π(s) = π(s′) implies q_t(s) = q_t(s′).
```

The candidate correctly carries this at `FOUNDATIONS.md:1285–1300`, explicitly limiting the obstacle to “same observation but opposite truth values”. It requires the predicate to be constant on each observation class, not the observation to be injective over subjects. Material sufficiency and irrelevance exclusion in candidate `REFERENCE_FRAME.md:301–316`, and compression at `448–458`, reinforce this distinction.

**Decisive normal case, fixed without any candidate test:**

Take the admitted domain Ω = {1, 2, 3, 4}, required predicate `q(n) = n is even`, and actual owner-issued observation `π(n) = n mod 2`. The observation's binding to the exact subject and basis, its provenance and its fidelity are independently justified; they are not replaced by a harness-created subject. Those separate obligations remain satisfied.

| Admissible subject | Owner observation π | Required q | Correct bounded judgment |
|---|---:|---|---|
| 1 | 1 | false | falsified |
| 2 | 0 | true | satisfied |
| 3 | 1 | false | falsified |
| 4 | 0 | true | satisfied |

The observation is sufficient to decide q soundly and completely over Ω. It does not distinguish 1 from 3, or 2 from 4. The foundation therefore permits the displayed judgments, while the literal consumer requires more evidence, narrower scope or indeterminate for precisely this ordinary sufficient projection.

**Adverse control:** keep Ω and q, but let π be constant. Then 1 and 2 have equal observations and opposite truth values. Further evidence, a justified restriction, or indeterminate is warranted. The common law and candidate foundation distinguish this adverse case from the preceding normal case; §11's unqualified sentence does not.

**Impact:** a lawful bounded evaluation can be forced to acquire irrelevant detail, narrow a supported claim unnecessarily, or return false inconclusiveness. For any large or infinite subject space, the rule can make an otherwise sufficient small observation appear unusable. This undermines bounded attention and proportional acquisition at an ordinary assurance entry point. It is not a demonstrated unsafe acceptance or an observed production failure.

**Counterreading considered:** the explicit link to the correct foundation makes an intended claim-relative reading plausible. It does not remove the direct stronger instruction in the consumer. The method requires a consumer to apply, rather than silently strengthen, the shared relation. A reader should not have to discard a consumer's operative condition to obtain the foundation's lawful decision.

**Smallest owner fix:** qualify the §11 separation condition by differing truth values of the declared predicate, or consume the owning observation-sufficiency condition without restating a stronger one. Keep exact subject/basis authentication, real owner acquisition and oracle independence intact. No new carrier, framework or assurance calculus is needed.

## Independent cases and what the laws actually decide

These are source-level desk cases, not executed-product qualification. The cases were recorded before candidate acquisition except the additional positive observation case that exposed CORE-F1.

| Case | Deciding candidate source | Source-derived outcome |
|---|---|---|
| C-A: lawful invariant-preserving no-op repeated until the budget ends | `ACTIVATION.md:117–196,198–352,1413–1433,1664–1679`; `SPEC_METHOD.md:668–755` | Lawfulness and preservation do not establish accepted movement toward Z. Strategy claims need their destination and conditions; exhaustion retains an unresolved stop. Counts of commits, proofs or iterations do not establish progress. No false completion permission found. |
| C-B: sorted arbitrary integers supplied to a nonnegative-only consumer | `FOUNDATIONS.md:477–493,1177–1228`; `ACTIVATION.md:1212–1236` | Local success is insufficient. The postcondition-to-precondition relation must be established, with material seams and outer obligations retained. A declared adapter is itself governed. No composition waiver found. |
| C-C: submitted transfer times out and retry may duplicate it | `ACTIVATION.md:1122–1170,1388–1395,1467–1514`; `SPEC_METHOD.md:986–991` | Lost response or absent context trace does not establish absence of effect. Completion remains unknown until evidence suffices for the next dependent action; no blind repetition is licensed. A counterexample to an interval-bound outcome can coexist with an effect whose end is still unknown. |
| C-D: one mandatory counterexample plus another required evaluation never performed | `FOUNDATIONS.md:840–847,1008–1129`; `REFERENCE_FRAME.md:574–609,625–632,750–782`; `TICKETS.md:1174–1208` | The known counterexample and missing coverage both survive. The conjunction cannot report satisfied; nonperformance is not fabricated as an evaluation result. A stale held result becomes a coverage gap, whereas an evaluation establishing invalid basis remains an invalid-basis result. No aggregate-green escape found. |
| C-E: the requested artifact exists but its contents violate the requirement | `FOUNDATIONS.md:790–939,1080–1109`; `ACTIVATION.md:943–971,1008–1083` | Availability can be satisfied for “a candidate is available”. That predicate cannot count toward fitness or acceptance. The decision owner disposes the assessed candidate; the assessor's recommendation is not acceptance. |
| C-F: “every eligible item exactly once” tested only by “some notification exists” | `FOUNDATIONS.md:1230–1283`; `ASSURANCE.md:236–251,639–668,688–702`; `TICKETS.md:1210–1255` | A necessary/local assertion does not establish the full requirement. Assertion provenance, intended-domain interpretation and any conjunction's sufficiency remain claims needing support. Implementation agreement cannot authorise changing the test's expected semantics. |
| C-G: equal return codes/logs hide once versus duplicate external delivery | `FOUNDATIONS.md:1285–1300`; `ASSURANCE.md:672–702` | Correctly requires further evidence, justified narrower scope or indeterminate for the adverse case. CORE-F1 is the distinct failure to permit noninjective observations that are sufficient for q. |
| C-H: implementation and checker share a mistaken exclusion | `FOUNDATIONS.md:1302–1407`; `EVALUATION.md:178–240`; `ASSURANCE.md:236–251,688–702` | Agreement is not source fidelity. Assertion provenance and execution provenance stay separate; diverse actor/model labels alone establish no claim-relative independence. Numeric assurance needs supported conditional/joint error assumptions. |
| C-I: artifact unchanged, external policy or evidence dependency changed; other evidence unaffected | `FOUNDATIONS.md:1409–1492`; `ACTIVATION.md:1692–1758`; `REFERENCE_FRAME.md:910–963`; `TICKETS.md:1103–1130,1198–1208` | The affected validity dependencies reopen even without changed subject bytes. An unrelated role/conversation change does not invalidate results. Old evidence keeps its original subject and may support the new subject only through an explicit applicability relation. A required independent judgment cannot be replaced by reuse of the author's judgment. |
| C-J: prediction wrong but requirement met; separately, requirement no longer serves intended outcome | `ACTIVATION.md:278–317`; `SPEC_METHOD.md:815–864,967–975` | Four-cause diagnosis distinguishes implementation, requirement/design, model and observation. A model error is not automatically a product failure; adequate existing law permits local repair. A changed governing outcome re-enters its owner and does not establish the prior Z. |
| C-K: adequate human-only document process with no code or event stream | `SPEC_METHOD.md:229–251,1772–1840,1846–1896`; `ACTIVATION.md:510–706,1377–1386`; `REFERENCE_FRAME.md:355–374,441–446` | Generic operations, roles, carriers and configuration remain available without the Executive/ODD/design profile. Direct operations and adequate current records are allowed; no universal hierarchy, software runtime or complete-history replay is imposed by these laws. This is source-level permission, not actual-use proof. |
| C-L: two approximations each have a local tolerance, no final bound | `FOUNDATIONS.md:1177–1228`; `ACTIVATION.md:1260–1289` | Local tolerances alone cannot establish whole-composite adequacy. The approximate composite needs its own justified end-to-end bound; the exact induction is not applied to it. |

The positive conclusions are supported by bodies that decide cases, not only by the foundation-to-law indexes. In particular, the core result predicates travel through admission, construction availability, ambiguity, effects, disposition, frame conjunction, coverage and ticket closure. The A-to-Z model reaches the strategy, feedback, stop, progress and recovery consumers. These connections are meaningful implementation of the common Intent and Product.

## Suspected tensions not promoted to findings

1. **“Failure to derive” as an upper-layer defect.** `EVALUATION.md:428–459` and `SPEC_METHOD.md:335–375` use broad wording. Their sufficiency test assumes a competent actor in the declared configuration, and `EVALUATION.md:449–459` rejects indictment outside that envelope. The operative feedback and triage clauses explicitly admit model, observation and implementation defects and correction under sufficient existing law. I found no consumer that necessarily routes one unsuccessful bounded attempt to constitutional repair. This is not a confirmed defect in this review.
2. **Build-tenant outcomes versus plain output data.** `SPEC_METHOD.md:1846–1850` lists outputs separately from outcome values. `SPEC_METHOD.md:890–899,956–965` distinguishes recorded states/computed facts from evaluated results, and `FOUNDATIONS.md:811–816,862–879` binds a refinement to its predicate and original domain outcome. A transform may return numeric data as its output and a predicate-bound completion/refusal outcome. I found no necessary coercion of arbitrary numeric data into the five core values.
3. **Module-unit obligations outside the optional profile.** `ASSURANCE.md:495–496` says every coded module needs the module-derived lane, but frame selection at `341–354`, its design-profile ownership, and the explicit scope of §15 at `1034–1061` prevent a sound finding that every generic human or non-design-profile activity must adopt that lane. Full profile evaluation belongs to the other review partition.
4. **Different-basis evidence exclusion versus reuse.** `EVALUATION.md:173–176` does not license silently rebinding old evidence. The explicit original-subject plus new-applicability relation at `FOUNDATIONS.md:1440–1460` and `ACTIVATION.md:1712–1720` provides the permitted route. No actual prohibition of that route was established.
5. **Known failure combined with missing assessment.** The conjunction includes required coverage and unperformed work, preserves failure information, prohibits raising to satisfied, and separates stale evidence from a current invalid-basis evaluation. The existence of domain-owned ordering among remaining nonsatisfied values is not itself a defect.

## Empirical and scope residuals

The following remain unestablished by this partition, rather than being silently counted as passed:

- Actual ordinary-use success, recovery between real activations, frame attention adequacy and actor usability. `EVALUATION.md:580–601,605–702` states relevant qualification obligations; written obligations do not discharge them.
- Comparative reduction in effective reasoning complexity, startup/acquisition cost or total task cost. The proportionality relation at `ACTIVATION.md:1528–1602` is substantive, but neither its existence nor reduced word count measures realized benefit.
- Complete a_c semantic coverage, cross-corpus preservation and all actual-use sets. The selected baseline defers identified parts; nothing in this review grants full Product qualification.
- Complete profile/runtime/package/release conformance. I followed material core consumers and did not inspect all optional profile bodies or packaging sources.
- A global no-defects claim. The finite coverage below supports a bounded content judgment. It does not establish the absence of unknown material relations, nor statistical defect confidence.

## Exact coverage and measurement

All body ranges below were presented completely from their pinned objects. Two initially oversized presentations were truncated by tool output: `FOUNDATIONS.md:781–1060` and `EVALUATION.md:1–280`. The omitted spans, respectively `972–989` and `98–116`, were reacquired in complete smaller slices before relying on full-file coverage. Repeated acquisition is counted conservatively below; no missing text is counted merely because the shell requested it.

| Source | Body coverage | Raw unique body bytes |
|---|---:|---:|
| common `INTENT.md` | 1–53, full | 10,378 |
| common `PRODUCT.md` | 1–437, full | 67,479 |
| common `requirements/README.md` | 1–195, full | 40,116 |
| common `requirements/ASSURANCE.md` | 1–131, full | 17,842 |
| common `requirements/PRINCIPLES.md` | 1–130, full | 14,917 |
| candidate `FOUNDATIONS.md` | 1–1614, full | 146,087 |
| candidate `EVALUATION.md` | 1–761, full | 93,992 |
| candidate `ASSURANCE.md` | 1–1184, full | 96,205 |
| candidate `SPEC_METHOD.md` | 1–2097, full | 164,288 |
| candidate `ACTIVATION.md` | 1–1838, full material consumer | 156,093 |
| candidate `REFERENCE_FRAME.md` | 276–964 | 37,329 |
| candidate `TICKETS.md` | 1103–1256 | 8,760 |

Common unique body acquisition is **150,732 bytes**. The four primary candidate members total **500,572 bytes**. Full body acquisition including consumers totals **853,486 bytes**. Additional heading-index lines in REFERENCE_FRAME, TICKETS and DESIGN_MODULE add **5,824 unique bytes**; DESIGN_MODULE's body was not read and no body coverage is claimed for it. Total tracked unique pinned-source bytes are **859,310**. Cumulative requested pinned-source bytes, including index overlaps and repeat reads, are **881,154**, with a conservative **21,844-byte repeat/reacquisition overhead**. The latter includes the truncation recoveries and therefore overstates actual repeated presentation where the first display omitted text.

The grant was extended from 512 KiB to **1.25 MiB (1,310,720 bytes)** for cumulative new source. The reported tracked pinned source remains within it. Administrative instruction acquisition, the narrow memory lookup, tool wrappers, metadata and these authored review artifacts are outside the pinned-source accounting boundary; they are not claimed as zero. The four current administrative source files inventory at 22,721 bytes, but their earlier presentation and the amended activation were not instrumented as immutable source acquisitions.

These quantities measure raw UTF-8 source presented or requested, not tokenizer usage or simultaneous active-context occupancy. The initial host/system context, retained context after compaction, attention adequacy and native model cost are unmeasured. No active-context-fit, attention-quality or total-cost claim follows. No network/paid external calls or suite executions occurred.

The review began after the activation at approximately 04:24 UTC and reached the closed source judgment before 04:45 UTC on 2026-10-17, within the 30-minute progress and 60-minute return bounds. Exact native model effort and dollar cost were not exposed.

### Content identities

| Source | SHA-256 of complete pinned file |
|---|---|
| common INTENT | `fb5529c530d48cf45fc8f60ba97fe4885726680fbec9ff2641a26a4a4ca151fb` |
| common PRODUCT | `4d6a43c25c58e76ea1283b1e2cacae5d40e3fba939681f188d99378bfadcc1d5` |
| common requirements/README | `ad0b7eca928ed184d845e45781344cbc47934f73a4293411c2f0a25ed72b532d` |
| common requirements/ASSURANCE | `ef6dbee500c42289cf710fae81bc6c79af67f3c6b9f94a11b48be48ccf643ef5` |
| common requirements/PRINCIPLES | `9004a5f109552bebde017396040ee645f39dfeae71a1901632e3b479173bb5cc` |
| candidate FOUNDATIONS | `740847e4c66b692959fd4a2f1f328ab9cfcd0df5c9ac38af10227f0cc590951a` |
| candidate EVALUATION | `14f8816b1eb9cd146dd58a29bac35ea47a62e4e4b093b20f9892330e44922991` |
| candidate ASSURANCE | `ca4b49d6252f6f071de37b0fdfdff2fb8f01974cb4c0747d4dfed1e2c8e2c56b` |
| candidate SPEC_METHOD | `8044f968eaecfba67d98bf1847e73401f29b6a8500bd6115db3a23c44abccca9` |
| candidate ACTIVATION | `c2009a691e33a374ea221e8ece7202d9086dfb2fe83f326d70232a039a191fc3` |
| candidate REFERENCE_FRAME | `d64ee5c05aaefac346116c2e43eabf193dd84123f1d461070ecd378ce5e9b551` |
| candidate TICKETS | `d858ac526b3956432e75c0dee32e5672a4679badab19b7f26ca5de613c4cd453` |
| candidate DESIGN_MODULE, headings only | `cbe1f91e698725e1a3347d7aee097f9a25c89ba519b7e6b1e02eea2e1f580d6b` |

