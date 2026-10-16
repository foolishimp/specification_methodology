# REVIEW: v3 common specification consistency across iterations 1–5

Frozen subject: `a3c43335e6d50bb7d6dd247c90de99e7404e1d1a`, carrying I5 source `bc8662a90323d38166164afac03468942667cf7a` (C3-I5-05). Review requested by the product owner on 2026-10-16. The installed builder is STDO 2.5.1-rc.2, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Summary

**The common specification is coherent across the five iterations within the reviewed scope. No blocking or material contradiction was established. Two Low corrections are recommended: one stale work-entry projection and one ambiguity in failure-handling wording.**

The assurance addition governs the transformation process. Its preservation conditions apply to composition, its assertion and observation conditions apply to evaluation, and its validity conditions apply to change, recovery and closure. Foundations, Spec Method, reference frames, the six member criteria, integrated demonstrations and the I5 work map all consume those relationships. I found no assurance duty left as an isolated explanatory paragraph or omitted because it has no predecessor claim row.

The earlier contributions remain: independent WHAT/HOW realisations; one semantic owner and one result algebra; the three algorithmic, informational and computational accounts; human and mixed execution; finite context and attention; configurations derived from the task; current-workspace recovery; foundational reduction; complete interpretation fidelity; and exact-input comparison with separate owner acceptance.

This establishes source consistency and required follow-through. It does not establish that either tenant already implements I5, that actual use has qualified the method, or that the common model necessarily captures the desired real-world outcome. I5 ratification and admissions remain pending. Existing I4 candidates retain their admitted requirements.

## Findings

### FC-01 — Low: a current work-entry page presents obsolete authority state and a broken route

The [work-surface README](../../README.md), lines 8–9, says the Executive is unbound and no tenant execution contract is admitted. It links Codex to `tickets/backlog/T-002-CODEX-c3-successor-construction.md`, which is absent from the frozen tree. The [active Codex ticket](../../tickets/active/T-002-CODEX-c3-successor-construction.md), lines 24–28, records the admitted I4 contract. Current T-002 and the shared tenant entry reach that active record correctly.

A fresh reader using the work-surface entry encounters a failed link and an incorrect current-state assertion. The authoritative contract remains available elsewhere, so this causes discovery failure or an unnecessary stop rather than granting unapproved work. It is not a loss of I5 meaning.

Correction belongs to the common pen's shared work-entry projection: repair the link and route current standing to its owning ticket, distinguishing admitted I4 work from pending I5. Check that entry and its target afterward. No tenant rebuild, new requirement or broad qualification run follows from this repair. This is the history review's H-L1, reproduced by the link checker.

### FC-02 — Low: failure-handling wording can suggest repair before diagnostic execution

[ASSURANCE](../../../specification/requirements/ASSURANCE.md), line 121, ends:

> Failures feed causal diagnosis and repair before another selected run.

The whole contract permits further observation or a justified retry when a repair is not yet supported: Product line 76; the construction requirement at requirements/README lines 110–112; ASSURANCE line 115; and the diagnosis conformance case at line 76. Those clauses retain unresolved causes and permit a bounded hypothesis test. They do not require speculative changes merely to unlock another run.

The local sentence can nevertheless be read as an unconditional sequence of diagnosis, repair, then execution. Consider a genuine failed observation whose cause could be the implementation or the observation environment. An authorised, safe diagnostic run is needed to distinguish them. No repair is yet justified. A repair-first consumer would block that observation or pressure an unsupported mutation. A transient external failure followed by observed recovery supplies a second case where an authorised retry need not involve a source repair.

Two fresh reviewers assessed this case separately. Both agree on the permitted behavior and reject a universal completed-repair gate. The assurance reviewer treats the exact verb “feed” and explicit owner alternatives as sufficient, reporting a clarity concern only. The process reviewer records a Low ambiguity because a consuming procedure could still encode the restrictive reading. The coordinated review retains the Low clarity finding; it does not claim that the full specification forbids diagnosis or that a tenant has implemented the defect.

The smallest correction is at the final sentence of ASSURANCE line 121: make it explicit that failure informs causal diagnosis and selection of the next authorised response, with repair when supported. Reuse the construction owner's existing alternatives. Preserve failed observations, uncertain effects, authority, risk limits and mandatory gates. No new retry policy, result value, actor role or work carrier is needed. A changed-clause readback and assessment of any consumer that actually adopted the restrictive reading would be sufficient.

## Iteration retention

Iteration numbers describe successive construction inputs, not product releases or the C0–C3 checkpoint numbers. The historical review binds the full coordinates and changed obligations in its [retention matrix](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/history-review.md#iteration-to-current-owner-and-consumer-matrix).

| Iteration | Contribution checked | Current deciding owners and follow-through |
|---|---|---|
| I1, selected C3 contract at `c9924e1` | Standalone successor; complete predecessor accounting; six criteria; bounded frames; independent review; separate construction and acceptance authority | Successor requirements, Product's construction authority and C3 contract, predecessor inventory, criteria 1–6 and integrated acceptance. Historical C1 tenant principle decisions retain their own subjects. |
| I2, rebuild input `9810215` following `bb76b1d` | One owner and result algebra; categorical demonstration; human/mixed execution; bounded A→Z work; persistent workspace and disposable context; independent tenant lines with permitted ports | Frame, ownership, result, execution-binding and categorical requirements; Product's context/configuration and Cross-Synthesis clauses; corresponding conformance cases. |
| I3, closed source `dc5dc27`, recorded at `1fce537` | Pillar-driven reconstruction and demonstrated reduction; complete a_c coverage/fidelity; owners and actual consumers; exact conjunction, context fit and replacement authority | Reduction and constraint-surface requirements, criteria 3–6, complete interpretation and integrated closure. Unchanged prose remains permitted when it carries the required relationships. |
| I4, ratified source `3c4c503` | Common ratification before admission; each tenant's own line and exact donor; nonauthor assessment of ports; semantic/modal conservation; shared comparison and no-qualified-choice outcome | Cross-Synthesis and Candidate Comparison, disposition requirements, admission records and the explicit I4-to-I5 work mapping. Ordinary discovery and supplied-frame trials remain separate claims. |
| I5, proposed source `bc8662a` | Universal construction, strategy and feedback; bugs as feature/change work; formal preservation; assertion and execution provenance; mutual assurance; risk; targeted reassessment and reuse | Construction and ASSURANCE owners, frame bindings, criteria 4/5, integrated demonstrations and seven assigned assurance duties. These extend the earlier process without silently rebinding I4. |

No mandatory I1–I4 obligation was found silently removed or weakened by I5. Historical changes to the criteria and construction contract are recorded as changes; the original C1/C2 closure dates do not accept those later bytes. Proposed and accepted predecessor replacements remain distinct.

## Assurance through the construction process

The relevant path is current state and required outcome → bounded construction → observation and judgment → authorised disposition → continuation, correction, recovery or closure. Assurance attaches to each relation, including the joins between steps.

| Process boundary | Assurance required there | Binding and deciding consumer |
|---|---|---|
| Define A and Z | Separate material state, observations, normative conditions and predictive models. Establish the selected basis and material assumptions. | Product 66–82; construction requirement 107; ASSURANCE 9; frame requirement 97. |
| Refine or transform | State the retained/established property; support the initial condition, each step, compatible joins and final connection to Z. Approximation needs its complete-composition bound. | ASSURANCE 11–23; construction requirement 109/118; categorical standard; conformance 90. |
| Acquire context and execute | Bind task, subject, authority, material inputs and observations. A small or faithful rule packet alone does not provide the facts needed for its decision. | Frame requirement 93–101; constraint-surface requirement; frame basis 47–51; criterion 4. |
| Evaluate a result | Identify the source obligation and interpreted predicate, whether the assertion is necessary or sufficient, the observation binding and supported conclusion. | ASSURANCE 27–56/62; criteria 4/5; conformance 91–94/116. |
| Compare independent paths | Account for shared specifications, interpretations, tools, fixtures, ports and observations. Agreement does not prove independent errors or validate a wrong common model. | ASSURANCE 60–95; Product 305–317; port-review independence and conformance 95–96. |
| Combine results and decide | Keep failure, missing coverage, undecidability, non-performance and uncertain effects distinct. Producing a candidate cannot imply fitness or acceptance. | Single result algebra; Product 220–226; criterion conjunction; conformance 37–38/61–64/113. |
| Diagnose and change | Distinguish realisation, requirement/design, prediction and observation defects. Change expected answers only through the owning authority and preserve the original counterexample. | Construction requirement 110–112; ASSURANCE 68/115–121; triage and re-entry consumers. FC-02 concerns only local wording of the next-run relation. |
| Select targeted reassessment | Follow assertion and execution-validity dependencies, including environments and assumptions. Unknown influence widens reassessment or leaves the dependent claim unresolved; new obligations create work. | ASSURANCE 99–109; frame basis 51; conformance 98–101/117. |
| Recover and reuse | Reacquire current reality, resolve material effect uncertainty, retain valid work, and establish applicability of earlier evidence to the new subject. Original evidence retains its original subject. | Frame requirement 97; construction requirement 111; ASSURANCE 115–119; repair readback and criterion 4. |
| Accept or release | Conjoin the required evidence on the exact subject and basis. Retained and new evidence may combine; missing mandatory coverage cannot become green. Approval and release retain their authority. | Product 222/309/419–427; integrated conformance 105–117; I5-A7 and existing release requirements. |

The [seven I5 assurance duties](../../tickets/active/T-002-c3-successor-construction.md#assurance-work-and-proof) each have one primary work owner and named consumers. They cover preservation; assertions/observations; formal interpretation; mutual assurance/actual use; risk and resources; impact/reuse; and the complete evidence account.

New obligations are not excluded by a predecessor-only frontier. Product line 356 defines unresolved work as the claims **and every required evaluation not closed on the current basis**. The criteria and integrated checks apply to the new owned determinations. Disposing every predecessor row while omitting I5 assurance still leaves required work open and prevents closure.

## Counterexamples checked

These are source-level discriminator traces, not claims that a tenant has executed or passed them. Exact clause pairs and reasoning are in the [construction/assurance review](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/assurance-review.md) and [process/recovery review](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/process-review.md).

- A specification permits output 0 or 1 and a design chooses 0. This can preserve the obligation exactly while adding detail; it need not claim behavioral equivalence or become a quantitative approximation. Changing the common requirement to prohibit 1 is a different, authority-bearing change.
- An empty transition relation makes an isolated implication vacuously true, or a loop preserves an invariant forever. Neither establishes the initial execution, compatible joins, progress, termination or Z.
- Each local check passes but one postcondition fails the next precondition. The outer conclusion remains unsupported; valid local results survive.
- Histogram keys match while counts are wrong, or two cases with different truth values have identical observations. A weak or ambiguous observation cannot establish the full obligation.
- Two constructions agree through the same wrong oracle. Neither actor diversity nor repeated agreement establishes independent assurance. Multiplying miss rates needs the stated conditional-independence model.
- A shared parser or external assumption changes while requirement-to-test links stay unchanged. Validity dependencies still invalidate affected evidence. Conversely, a supported isolated change need not rerun every unrelated check.
- A context restart occurs after a request whose external effect is uncertain. It cannot establish absence of the effect, reset the workspace or invent completed assessment.
- One required judgment fails and another is absent, while work reports `candidate_ready`. The result and authority contracts prevent promotion to acceptance.
- A human process uses current records and direct observation without code or complete-history replay. That remains permitted where its binding satisfies the common obligations; required human authority or independence cannot be traded away for speed.
- A C3 Writer returns `refused`, `incomplete` or `re_entry_requested`. The local loop imports the installed complete transition, which supplies those branches. A pre-activation `activation_refusal` remains distinct from a Worker result. No missing-branch defect was established.
- A trial supplies a curated frame but claims ordinary discovery. The comparison and publication contracts keep those claims separate; supplied-frame evidence cannot replace the missing entry-path evidence.
- A failure requires a diagnostic execution before the cause is known. The full construction owner permits it with authority and effect safety; FC-02 records the local wording risk. Both [assurance readback](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/assurance-readback.md) and [process readback](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/process-readback.md) are preserved, including their different finding classifications.

## Verification and review limits

The review inspected all current common normative sections, the governing construction/acceptance and routing surfaces, and the historical evolution of their obligations. Its [subject manifest](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/subject.json) binds nineteen files totalling 691,502 bytes: the original eighteen-file common/work scope plus the discovered work-entry README. That is an inventory size, not measured actor context.

Mechanical results:

- The installed 2.5.1-rc.2 basis and current Product Definition verify with no failures.
- All forty C3-I5-05 input pins reproduce from `bc8662a`.
- The historical reviewer verified 357 snapshot member occurrences across fifteen snapshots, all 71 predecessor member identities, and preservation of the 635 original section-row identities. The current inventory has one explicitly split child, giving 636 body rows plus 55 other member rows: 691 claims. This checks inventory retention, not the semantic conservation of every tenant implementation.
- Of 427 checked local and installed-source links, 426 resolve. FC-01 is the sole missing target. Four historical links into the separate ABG repository were excluded from this frozen-repository link check and are disclosed in the results.
- No trailing whitespace was found in the nineteen subject files.

The [mechanical results](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/mechanical-results.json) and [replay script](20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/verify_subject.py) are retained. From the repository root:

```sh
python3 specification_methodology/v3/.ai-workspace/comments/codex/20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS/verify_subject.py --repo . --assets specification_methodology/v3/.ai-workspace/comments/codex/20261016T091908Z_V3_FULL_CONSISTENCY_ASSETS
```

On the reviewed subject this command exits nonzero because it reproduces FC-01. A green identity/link check would still not establish semantic consistency.

The coordinator authored prior common changes and supplies no independent acceptance of them. Three fresh same-family nonauthor activations fixed expectations before acquiring their assigned bodies and returned closed source judgments. The reason for this working-review arrangement was to obtain bounded nonauthor scrutiny through the available native reviewer mechanism, without selecting an external paid trial. It is not cross-family acceptance or evidence of statistically independent errors. The coordinator then checked the joins and requested the additional diagnostic-run case. The reviewers' original returns and supplements remain separate; the narrow process supplement qualifies its earlier no-finding result for that sentence.

This was not a semantic requalification of all 691 predecessor claims, a review of every tenant member, a fresh-actor task trial, or an independent proof of every mathematical proposition. Historical review verdicts and witness passes supplied no automatic current qualification. Complete host context, cumulative acquisition and native spend were not instrumented, so no context-fit or efficiency claim is made. The review establishes no universal Markov property, termination, optimality, numerical correctness probability or fitness of the common model against every intended use.

## Recommended action

Make the two bounded corrections at their existing owners, retaining the current construction and assurance meanings. Recheck the changed clause, the work-entry route and affected consumers. This review supplies no reason to introduce another conceptual layer, a seventh criterion, a parallel evidence ledger or a new iteration of the architecture.

After exact common ratification and the existing admissions, both tenants should implement I5 through the assigned owner-to-consumer work. Their next reviews must follow actual source → interpretation → acquired frame → execution/observation → judgment → authorised disposition, including valid reuse and invalidation after change. A requirement to perform that chain is not evidence that it already works.

The common specification, tickets, tenant codebases, branch, index and installed products were left unchanged. Only this review and its supporting commentary artifacts were written. No ratification, repair, commit, push, candidate acceptance or release was performed.
