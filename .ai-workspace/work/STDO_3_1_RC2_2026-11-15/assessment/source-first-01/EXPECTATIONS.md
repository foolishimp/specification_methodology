# Source-first expectation report: STDO 3.1.0-rc.2 W35 successor-conservation repair

## 0. Standing of this report

- **What this is:** expectations written before seeing any candidate. It contains no verdict on any candidate, no repair proposal and no publication authority.
- **What I read:** only the supplied packet. I compared the supplied texts by reading them. The only hash comparisons I rely on are the ones the operator computed.
- **Tool use:** none. I made no tool calls, including the advisor tool, because the instruction said not to use tools. I read no files and ran no commands.
- **Host context:** the host injected an account-identity reminder and environment metadata. I did not use either. All other hidden host or system context is unmeasured.
- **Who I am:** a Claude-family actor. I authored neither the candidate nor any governing source. Native CLI metadata, not this text, is authoritative for my session identity.
- **Main limit:** I could not see W35's rule text, the index, the query or fact schema, or the meaning of the boundary values. Every expectation below that depends on them is conditional, and §5 lists them as gaps.

## 1. Expected behaviour by boundary

A "fact" here is a value the query declares, such as which boundary is being decided or whether the subject is a successor.

| Query case | What W35 should do | Depends on | Must not be transferred in |
|---|---|---|---|
| **A. Product acceptance of a successor subject** | W35 is present, with its full meaning (§2). RC1 shows the defect as absent; RC2 must show it present. | Acceptance relies on qualified claims: an unresolved disposition blocks qualification "and so cannot be accepted" (EVALUATION §5 ¶2). Any rule W35 declares as a dependency (for example evidence reuse or result conjunction) must also be selected. | Release-only conditions: atomic 25-ref push, per-ref leases, remote-absence checks, selector advancement, cohort suffix equality, GitHub release, public readback. Also, RELEASE §8's acceptance criteria for an immutable cut must not be presented as the generic Product acceptance law. Acceptance authority stays with the decision owner. |
| **B. Product acceptance, subject not a successor** | The "where the subject is a successor" condition (EVALUATION §5) stays visible. No disposition record is demanded as if the condition held. | The successor trigger itself. | An unconditional "acceptance requires a disposition record" for a subject with no predecessor. |
| **C. Product acceptance, successor status unknown, null or ill-typed** | The condition stays open. If selection is gated on a fact, the result is incomplete or a material gap, never coverage (PC-R03, PC-S05). | — | Treating unknown as "not a successor". |
| **D. Qualification** | W35 present before and after; no regression. RELEASE §3 binds "the complete successor relation"; §9 says an unresolved disposition blocks qualification of the affected claim. | Exact-cut binding. | The human acceptance criterion and any claim of acceptance authority. |
| **E. Release** | W35 present before and after. RELEASE §8 requires the "successor relation stable" and the mandatory gates. | Qualification (D) and the §8 gates. | — (release conditions belong here) |
| **F. Ordinary work, incremental QA, landing, no boundary** | W35 not selected. No acceptance gate is implied. | EVALUATION §5 "Landing, closure and release"; PC-S02 (incremental QA cannot imply acceptance). | The acceptance-blocking predicate. Recording dispositions during construction or integration (RELEASE row 11 and the support-line paragraph) is a separate obligation, unchanged by this repair. |
| **G. Boundary fact unknown, null or ill-typed** | Incomplete, not covered. It must not default to ordinary work (which would drop W35) or to acceptance (which would assert false applicability). | PC-R03, PC-S05. | — |

**Constraint on how the repair is realised.** Two forms are admissible:
- W35 is selected at product acceptance and carries its source-owned successor condition inside the rule; or
- selection is gated on an existing declared fact, with unknown handled as in row C.

If the repair introduces a new purpose fact or changes what an existing fact means, that is a semantic change to the purpose (PC-S06, SDLC-WORKFLOW "existing purpose and fact meanings are preserved"). It would go beyond the activation's description of "a bounded realization/selection repair, not a change to the governing obligation", and it must be declared explicitly. Extra boolean facts must not make the obligation optional.

## 2. Obligations W35 must carry at successor acceptance

| # | Obligation | Source |
|---|---|---|
| O1 | Acceptance evidence for a successor includes the successor disposition record. | EVALUATION §5 ¶2 |
| O2 | The record names the exact predecessor immutable cut, and that origin stays immutable for the candidate. | RELEASE §9 ¶1 |
| O3 | Every predecessor claim capable of affecting the successor receives exactly one disposition: conserved, superseded (an accepted successor relation replaces it), intentionally removed (current Product authority removes it) or not applicable (with a bounded reason). | RELEASE §9 ¶1 |
| O4 | A claim with an unresolved disposition cannot be qualified, and so cannot be accepted. In conjunction it is a gap, a planned assessment without a closed result. It is not a falsified result. | EVALUATION §5; RELEASE §9; FOUNDATIONS Conjunction "Gaps" |
| O5 | "Conserved" is a semantic test made on the same material case, scope and authority. It covers what must happen, what may happen, what is prohibited, and what follows when a trigger, exception or premise is absent. It applies in the owning text and in the consumer bindings, with counterexamples. Obligation strength, preferences, exceptions and scope conditions must all survive. Naming, code similarity, patch absence or a whole-package equivalence statement prove nothing. | RELEASE §9 ¶3 |
| O6 | A "conserved" disposition recorded before this test applied is unresolved until re-evaluated. | RELEASE §9 ¶3 |
| O7 | A conserved reading made on an earlier successor text carries over only if the owning text and consumer bindings are unchanged, or the change is shown not to affect the claim (`retain_applicable`). | RELEASE §9 ¶2; FOUNDATIONS Change impact and evidence reuse |
| O8 | A disposition is a claim, not a result. Qualification records a core result for it. It is distinct from the decision owner's disposition of an assessed candidate (ACTIVATION §3). | RELEASE §9 ¶4 |
| O9 | "Intentionally removed" is a decision of the current Product authority, and the record is that decision. | EVALUATION §5 |
| O10 | Acceptance is the decision owner's act over an unchanged subject. A reviewer result is input, never closure. Green labels and counts are not acceptance. Index coverage grants no acceptance. | EVALUATION §5 ¶1; Purpose Context PRODUCT "makes no release decision" |

**Behaviour when a trigger, exception or premise is missing:**

| Situation | Expected outcome |
|---|---|
| Successor trigger absent | O1–O9 are not asserted. The general acceptance law still applies. |
| Trigger present, predecessor not named | O2 is unmet, so the claim cannot be qualified or accepted. |
| "Not applicable" without a bounded reason | Unresolved. |
| "Removed" without an authority decision | Unresolved. |
| Evidence binds an earlier text and no applicability is shown | Excluded by basis (EVALUATION §2). |

Deterministic-kind migration applies only if a successor adopts the total deterministic kind. I do not expect it at this boundary unless W35's source closure already includes it.

**Finite counterexamples W35 must expose.** Each is a falsifier for the RC2 product-acceptance context:

| ID | Scenario | Expected handling |
|---|---|---|
| K1 | Successor acceptance with no disposition record | W35 shows the block |
| K2 | Record says "conserved" on the strength of whole-package wording equivalence | Unresolved |
| K3 | Pre-test "conserved" disposition | Unresolved |
| K4 | "Removed" without a Product-authority decision | Unresolved |
| K5 | All dispositions resolved | Rendering must not imply acceptance follows |
| K6 | Rendering conflates disposition (claim) with acceptance disposition (result) | Conflation is a falsifier |
| K7 | RC1 conserved evidence reused after the bindings changed | Not retained without applicability |

## 3. Verification matrix (proportionate)

| Dimension | Kind of claim | Expected evidence | Not established by |
|---|---|---|---|
| **Before/after** | Behaviour | Before the repair: on RC1's exact published package (index ID, manifest `ddbd…7faa`, query bytes, output), rows A, D and E reproduce "absent / present / present", and that failed expectation is retained. After: RC2 on rows A–G as in §1, with the before and after outputs kept as distinct subjects. | A label change, or a digest update alone (PC-S06) |
| **Structural content** | Structure | The RC2 indexes bind the actual RC2 native cut A, its tag object and the manager-produced manifest, not 3.0.4 or a predicted value. Source membership, order and bytes are bound. RC1, 3.0.4, 3.0.5 and development entries are byte-identical. The 39 unaffected rules are text-stable. Catalog, public-manifest and Skills pins are reconciled. No manifest contains its own hash. Six-Product version suffixes equal `3.1.0-rc.2`. | Semantic adequacy |
| **Semantic coverage** | Independent judgment | A new assessment of the RC2 index, corpus and query for the repaired acceptance context, including rows B–G, qualification, release and dependency guards. Codex authored the candidate and a Claude-family assessor is declared, so this is cross-family; same-family Codex checks count as mechanical only. Contexts never assessed stay `covered: false` or unknown. | Tests, checksums, author self-review, RC1 verdicts |
| **Actor and host behaviour** | Operational | Both installed host adapters resolve the same checked runtime (PC-R09). Explicit invocation, installed-layout behaviour and automatic discovery are reported as separate claims, and only observed modes are qualified. | Source success standing in for installed behaviour (RELEASE §3) |
| **Predecessor conservation** | Claim-level | RC1 → RC2 dispositions per affected Product claim. W35 gets an explicit entry (changed selection, unchanged obligation). Native selected owners are compared RC1 vs RC2 byte by byte; any changed owner (for example release-facing metadata) gets a claim-level reading. The earlier repairs (two stale-guide findings, missing-helper frame failure) are re-verified, including all 52 frame tests. Visual rebinding carries the predecessor/current identity and the source delta of its selected members. | A version-string change alone (PC-R16) |
| **Release identity** | Exact cut | Commit A, its local annotated tag and a private verified install; commit B; Product subtree roots and trees; member inventories. Remote absence of every RC2 immutable ref and no higher ordinal. Exact expected object IDs for mutable refs. One atomic transaction for 25 refs with no fallback. RC1 refs unmoved. A normal GitHub release. Downloaded assets match advertised and expected hashes. A fresh isolated-store install of the manager and native cut, with membership and context results verified. | Publication standing in for acceptance |
| **Exact-cut acceptance** | Human decision | Outside the publication evidence. Recorded as open until the human authority accepts the exact cut identity. | Publication, qualification, review results |

My own consistency arithmetic gives 25 refs as 6 Products × 4 (RC tag, selector, RC branch, release branch) + 1 carrier. That is my inference only; no source supplied says so.

## 4. Evidence reuse rules and what I will need later

**Reuse rules:**
- RC1 evidence keeps its original subject. It can be used for RC2 only under `retain_applicable`: the claim and scope still apply, the assertion and observation basis is still justified, and the dependencies are unchanged or covered by a preservation relation.
- RC1 exact-query assessments are never relabelled as RC2 results (PC-S09, PC-R16). They may be cited as prior evidence.
- Mechanical evidence may be shared; judgments may not (EVALUATION §3).
- The W35 counterexample is later counterevidence. Any RC1 verdict that depended on acceptance coverage for the affected query is invalidated for that claim, and the record must say so rather than delete it (EVALUATION §1).
- Mandatory gates (RELEASE §8) stay in force even where evidence is reused.

**Bytes, queries and evidence I will need:**
1. The RC1 and RC2 W35 rule objects: text, conditions, exceptions, dependencies and grounds.
2. The full rule-set diff, which should show only the W35 selection change.
3. The SDLC purpose definition and its fact schema, including the boundary values and their meanings.
4. The exact queries for rows A–G, with outputs from RC1 and RC2.
5. RC2 native A: commit, tag object and manifest. The selected-owner byte comparison RC1 vs RC2.
6. The catalog, public manifest, coverage-standing records and Skills dependency pins.
7. The disposition and impact record.
8. Outputs of the 52 frame tests and the current-state checks.
9. Both host-adapter observations.
10. Commit B, the cohort record, the ref graph with remote expected and absent states, the GitHub asset hashes and the fresh-install readback.
11. The Python RC2 entry's binding and its coverage-standing record.

## 5. Gaps, ambiguities and limits

**Missing sources and the predicates they leave unresolved:**
- **What "product_acceptance" means:** this is owned by the Purpose Context SDLC purpose (`skills/stdo-context/references/sdlc-workflow.md` and the authoring inputs for the RC1 SDLC entry). Without it, I cannot decide whether this boundary includes acceptance of an immutable release cut, which would bring in RELEASE §8. Rows A, B and C stay conditional.
- **Parts of the method not supplied:** TICKETS, SPEC_METHOD, EXECUTIVE_BASELINE, ACTIVATION §1–§5, `method-targets.md`, the Skills and visual Product documents, the RC1 cohort record and the RC2 root RELEASE record. These own boundary policy, the independence boundaries (UP-007) and the visual and Skills claims. I made no expectations that depend on them.

**Reading observations (by eye, not by byte diff):**
- Native RC1 RELEASE and installed 3.0.4 RELEASE differ in §7: RC1 adds "Source freeze and stable cohort construction" and rewrites the lead-in to the two-commit paragraph. The texts of §3, §8 and §9 look identical.
- EVALUATION is byte-equal between the two, per the operator's hash.
- This supports "native law is already correct" for W35's owning sections, but only as a reading.

**Adjacent observation, not part of this repair:** if the preserved development SDLC entry shares W35's selection, it carries the same historical defect. It stays immutable and goes back to its owner with no repair here.

**Not done:** I examined no candidate, executed nothing, verified no hashes, and claim no whole-method or universal context-fit result. I use no numeric severity scale; materiality is stated as the affected predicate (product-acceptance coverage, qualification and release regression, false applicability, unknown handling).
