# Closed review: construction and assurance consistency

Result: `satisfied` within the assigned common-source scope. No material contradiction, vacuous acceptance route or underconstrained deciding obligation was found. Findings: none. Finding triage, severity, priority and repair owner: `not_applicable`.

This is a source-first consistency judgment on the consolidated specification. It is not mathematical proof of the whole methodology, tenant implementation qualification, C3 acceptance, common ratification or a release decision.

## Activation, subject and governing basis

- Activation: `/root/v3_consistency_construction_assurance`, delegated by the coordinator for the full common-specification consistency review.
- Reviewer: fresh nonauthor Codex context. Same model family as the coordinator; this is the declared bounded working-review exception, not cross-family acceptance. No prior turn history or other current review report was loaded. Source work records contain summaries of earlier reviews; those summaries were treated as status records, not evidence for this judgment.
- Subject: `a3c43335e6d50bb7d6dd247c90de99e7404e1d1a`. Its parent is `bc8662a90323d38166164afac03468942667cf7a`, the C3-I5-05 source. The reviewed constitutional files are byte-identical between those commits; the recording commit changes Goals and work/review records.
- Governing Product: `urn:stdo:product-definition:stdo-3`, resolved from the frozen `specification_methodology/v3/stdo_3.json`.
- Builder: installed `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. `stdo verify v2.5.1-rc.2 --manifest-sha256 <digest>` returned `valid: true`, no failures, at `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2`. The initial URI-form invocation was rejected by the CLI before verification; the cut-name invocation above succeeded.
- Frame: the frozen `specification/REFERENCE_FRAME_BASIS.md` common-definition row at line 24, with the installed Reference Frame Method's closed-result, applicability, independence and conjunction rules. The installed bootstrap, RF laws, result-consumption sections, and Reviewer return/independence portions of the baseline were acquired directly.
- Prior expectations: `assurance-expectations.md` was written before acquiring the frozen subject bodies. The review-only Writer grant covers these two artifacts and nothing else. No source, ticket, Git, tenant, installed-release or external-service effects were performed.

All subject citations below are relative to `specification_methodology/v3/` at the frozen commit, not the current working tree.

## Coverage and closed judgments

| Relation reviewed | Result and exact source route |
|---|---|
| A, Z, lawful work, strategy and completion | `satisfied`. Intent 5–13 and 21–23; Product 66–82; requirements/README 103–118; conformance/README 68–82. Z is a normative predicate, observation describes current reality, and a predictive model supports intervention selection. Lawful activity, preservation, useful discovery, termination and delivered outcome remain distinct. |
| Algebraic, informational and computational accounts | `satisfied`. Product 17–23, 41–50 and 107–113; PRINCIPLES 98–104; requirements/README 120–131; ASSURANCE 11–23. Operations and composition, retained meaning, and concrete execution have separate claims. Human and mixed bindings remain available; they must establish the same material authority, effects, failure and recovery conditions. |
| Refinement, exact preservation and approximation | `satisfied`. Product 101; requirements/README 109, 127 and 182–195; ASSURANCE 9–23 and 60–64. The preservation object is declared; implication of retained obligations does not demand equality of every permitted implementation. Approximation needs its own end-to-end adequacy bound, and categorical assertions need their additional laws. The detailed nondeterminism case below distinguishes refinement from a changed source representation. |
| Assertion meaning and observation sufficiency | `satisfied`. ASSURANCE 25–56; requirements/README 118; conformance/README 90–94; Product 419–420. A necessary predicate cannot close its stronger source obligation. Interpretation fidelity, observational soundness, observation acquisition and actual-checker conformance are separate obligations. Indeterminate, not-performed and unknown-effect standing survive. |
| Parallel derivation, provenance and mutual assurance | `satisfied`. Intent 11; ASSURANCE 58–70; Product 305–313 and 419–423; conformance/README 93–96 and 116. Expected answers require source justification, while runs require execution provenance. Port authorship and shared specifications, fixtures, tools and observations remain visible. Agreement is not promoted to independent confirmation or validation of the governing model. |
| Risk and finite resources | `satisfied`. requirements/README 108 and 112–114; ASSURANCE 72–95 and 119–121; CAPABILITIES 12–19; conformance/README 79–81, 96–97 and 101. Work authority selects the risk policy within existing obligations. Numeric claims need their probabilistic model; cost selection cannot waive authority, safety, acceptance or separately mandatory gates. |
| Change impact, incremental assurance and recovery | `satisfied`. Intent 51; requirements/README 97, 111 and 118; ASSURANCE 97–121; REFERENCE_FRAME_BASIS 47–64; conformance/README 98–101 and 117; Product 309, 419 and 427. Assertion provenance and evidence-validity dependencies are different relations. Absence of an influence edge cannot justify omission. Original evidence keeps its subject; explicit applicability permits reuse on a successor. |
| Deciding consumers and closure | `satisfied`. Product 80, 185, 220–226, 362–368, 419–427; requirements/README 49–50, 73, 83–87, 114 and 118; conformance/README 103–121; REFERENCE_FRAME_BASIS 47 and 51. Assurance is consumed at composition, evaluation, change, recovery and closure, including actual-use and integrated evidence. All six criteria remain mandatory; missing required evidence withholds acceptance while retaining supported local findings. |

The assigned Intent, requirements index, ASSURANCE, CAPABILITIES, PRINCIPLES, conformance and Reference Frame basis were read in full. Product was read at lines 1–229 and 299–437: the assigned opening sections and C3 contract, plus the authority, cross-synthesis and comparison consumers necessary to assess them. Development Isolation, lines 230–298, was outside this bounded semantic scope. The a_c dependency contract was also read in full to check that the new formal obligations do not silently acquire a mechanical proof claim.

The current source consolidates the five iterations. This review checks that combined source, including earlier foundational, ownership, representation, domain and construction commitments; it does not reassess each historical snapshot's original acceptance.

## Counterexamples and why they do not defeat this source

### 1. Ordinary nondeterminism-reducing refinement

Let the governing outcome be `Q(y) := y ∈ {0,1}`. A refinement chooses the deterministic implementation `y = 0`. Its behaviour set is smaller than the set permitted by Q; it is not equivalent to a system required to realise every permitted alternative.

The source admits this refinement without treating it as quantitative approximation. `requirements/README.md:109` expressly permits added detail within permitted variation, and `PRODUCT.md:101` requires preservation of upstream obligations. `ASSURANCE.md:11–19` asks for retained or established properties and a one-way preservation implication, not equality of all behaviour sets. Choosing 0 retains Q exactly. The new deterministic choice is a design obligation under `ASSURANCE.md:60`, and line 64 explicitly allows distinct conforming implementations to produce different outputs.

`requirements/README.md:185` makes the layer state what it preserves; line 187 separates conformance, equivalence and functorial preservation. Thus an exact claim about Q does not entail a claim of full behavioural equivalence. No metric, error tolerance or probabilistic approximation is required for this case.

Conversely, changing the *representation of the common obligation* so that it says 1 is prohibited would alter permitted work. `requirements/README.md:83–85` rejects that as a fidelity defect unless an authorised successor changes the determination. The distinction is between choosing within the permitted constraint surface and changing that surface. No finding is filed for this join.

### 2. Vacuous preservation without a delivered outcome

Choose `P_i = false`, or an empty transition relation, or a loop that preserves `P` indefinitely. The isolated implication is vacuously true in the first two cases, and invariance can hold in the third without useful progress.

`ASSURANCE.md:19` separately requires the initial condition, join premises and final connection to Z. It explicitly denies that preservation establishes progress, termination or a suitable next step. `requirements/README.md:112–113` and `conformance/README.md:80–81` require a supported purpose for continuation and sufficient evidence for completion. An empty relation also supplies no actual execution conformance under `ASSURANCE.md:17`. These examples therefore cannot earn delivery or C3 closure merely through a true formula.

### 3. Locally acceptable errors with an unacceptable composition

Suppose a first approximation introduces an error of 0.1 and the next operation multiplies its input by 100. A local 0.1 tolerance cannot be carried unchanged to the final output. Similarly, two local checks may each pass although the first postcondition fails to establish the second precondition.

`ASSURANCE.md:19–21` and `requirements/README.md:185` require the actual joins and complete-composition bound; they expressly reject automatic addition or retention of local tolerances. `conformance/README.md:90` makes the unsupported outer conclusion fail while preserving the supported local results. The requirements do not prescribe a universal metric because each domain supplies its claimed adequacy relation and bound.

### 4. Strong claim from a weak or observationally ambiguous test

Take two histograms with identical keys but different counts. A key-only observer maps them to the same observation. If the full obligation demands correct counts, a key assertion can pass for a defective histogram.

`ASSURANCE.md:27–37` binds the assertion to its actual predicate and distinguishes necessary from sufficient conditions. Lines 39–56 require sound conclusions over all admitted cases and state the observation-sufficiency condition. The two-histogram example violates that condition for the count predicate. Lines 47 and 56 require the result to remain an observation, narrow the claim lawfully, acquire distinguishing evidence or return indeterminate. `conformance/README.md:91–93` directly exercises the failure.

The sufficiency statement is mathematically bounded correctly: constancy of `q_t` on every fibre of π permits a well-defined predicate on the image of π in the declared classical set model. It does not provide an effective algorithm or a resource bound; `ASSURANCE.md:56` says so. A relation T can admit a sound satisfied result and an indeterminate result on the same observation without requiring deterministic conclusion or completeness. Every admitted satisfied/falsified result remains constrained by lines 42–47.

### 5. Agreement and multiplied miss rates despite a shared error

Two implementations use the same mistaken interpretation. Their matching outputs cannot establish the intended requirement. Likewise, let two checks miss exactly the same faults with conditional probability 0.2. The joint miss rate is 0.2, not `0.2 × 0.2 = 0.04`.

`ASSURANCE.md:62–68` requires assertion provenance and shared-cause accounting, and separates agreement with a model from validation against the desired outcome. The Bayesian expression at lines 76–84 is the usual conditional total-probability expansion with a nonzero denominator; it does not manufacture a prior or likelihood. The factorisation at lines 86–93 uses conditional probabilities, and replacement by the unconditional-on-prior-misses factors requires conditional independence. Defined-conditioning and calibration limits are explicit. `conformance/README.md:95–96` and `PRODUCT.md:313` carry these distinctions into review and candidate comparison.

### 6. Targeted testing misses an execution dependency

A requirements-to-test graph is unchanged, but a shared parser, measurement instrument or external assumption changes. A selector based only on requirement links skips the affected check and reuses its old pass.

`ASSURANCE.md:99–107` expressly distinguishes justification from validity dependencies, includes execution and environment dependencies, and rejects missing edges as evidence of non-influence. Unknown impact widens reassessment or leaves assurance unresolved. Lines 109–119 require separate execution evidence, supported retention, new-obligation assessment and mandatory gates. The old result retains its original subject and known failures remain visible. `conformance/README.md:99` and 117 require this missed-dependency case in the consuming assessment.

The converse also holds: a justified local change does not force every unrelated check to rerun. `ASSURANCE.md:115–119` permits a supported preservation relation for retained evidence. That permission does not satisfy an uncovered current obligation or replace an independently required judgment.

## Integration into successor work

The new assurance text is not isolated explanatory material. The formal owner is `requirements/ASSURANCE.md:5`; its placement and consuming operations are specified by `PRODUCT.md:80` and `requirements/README.md:118`. Foundation and Spec Method duties are allocated at `PRODUCT.md:362–368`. Frame admission acquires the source obligation, predicate, observations and validity dependencies at `REFERENCE_FRAME_BASIS.md:51`.

At member acceptance, criterion 4 consumes assertion provenance and reuse conditions (`PRODUCT.md:419`); criterion 5 consumes the assurance discriminators and prevents a stated formula from standing in for its argument (`PRODUCT.md:420`). The actual-operation joins occur at the integrated boundary (`conformance/README.md:105–117`), with missing required assessment preventing C3 closure (`PRODUCT.md:427`). This avoids treating an unbuilt implementation as a source defect while retaining the implementation and evidence obligations.

The frozen T-002 work map also provides concrete follow-through: `.ai-workspace/tickets/active/T-002-c3-successor-construction.md:61–67` assigns preservation, assertions/observations, formal fidelity, mutual assurance, risk, impact/reuse and the complete assurance account to I5-01, I5-02, I5-05, I5-06, I5-07 and I5-09, with the affected consumers named. These assignments are future work obligations; their presence proves neither implementation nor qualification. Lines 32–36 and 75–77 retain ratification, admission, shared-protocol and resource boundaries.

## Source defects versus outstanding evidence

No owning correction is required by this bounded review. The following remain work or evidence obligations, not contradictions in the reviewed source:

- Tenant-specific preservation relations, domain binding and actual-checker conformance must still be instantiated and supported for their claims.
- Complete a_c coverage, semantic fidelity, current publication routes and independent practical evidence remain required; the structural checker does not discharge them (`A_C_DEPENDENCY.md:61–93`).
- Actual-use evidence must still establish its subject, expectations, actor conditions and context fit. This review supplies none of criterion 4's execution evidence.
- Integrated demonstrations must exercise the assertion/observation/provenance join and both valid retention and invalidation after change. The source's instruction to perform them is not their successful result.
- Common-model fitness against intended real-world outcomes, numerical assurance, categorical equivalence, stronger Markov properties and useful cost reductions require their separately supported claims. No universal solver, termination, optimality or automatic independent-error claim is established here.
- I5 ratification and tenant admissions remain pending in this frozen source. Prior I4 evidence retains its own subject; the new requirements do not silently rebind it.

## Acquisition, limits and invalidation

Primary source acquisition used `git show a3c43335e6d50bb7d6dd247c90de99e7404e1d1a:<path>`. Long outputs that were truncated were reacquired in bounded slices for every assigned constitutional body. Tree enumeration was used only to discover names; its truncated output was not treated as coverage. Ticket sections were selectively read to resolve the current grant, status and assurance work consumers, not audited in full. No historical review report body or tenant candidate body was acquired, and no author witness program was run.

| Primary file | UTF-8 bytes in complete file | SHA-256 |
|---|---:|---|
| specification/INTENT.md | 10199 | `8bf8f448b027ad8925b22619e145efa4634c594171b23cac0df14129d042a498` |
| specification/PRODUCT.md | 66579 | `71f963c36705e5491e050e213dd361affc64a5274a9db2769bf2d81759062059` |
| specification/requirements/README.md | 39787 | `ecb7db6b86f69cde8ac71b0926277a7504e08a3aad59bdc2df3ca461ae42c3c0` |
| specification/requirements/ASSURANCE.md | 17584 | `38f1a3e8bb5207e16156e349f1fbd5ae5caa19bf120c450cc3cff01d3149cd14` |
| specification/requirements/CAPABILITIES.md | 5299 | `024affc0ed27ff886f8171f545217d58b6d0cae18643e0e2732506f1e20e528c` |
| specification/requirements/PRINCIPLES.md | 14917 | `9004a5f109552bebde017396040ee645f39dfeae71a1901632e3b479173bb5cc` |
| specification/conformance/README.md | 26404 | `c1cced11624037060fa85ce749c0fb9fbb9865b87d32b6fa945124bfd5e53d4b` |
| specification/REFERENCE_FRAME_BASIS.md | 9109 | `f18f73ebea127b8933e71765485a070813ad0d50eadea7734918d8d741308f4a` |
| specification/requirements/A_C_DEPENDENCY.md | 8074 | `1095e3c5e63c25b12736de05121ae84cbee3095776cf924f90e4768d8d65c8b8` |

These complete-file identities total 197,952 bytes; that is an inventory subtotal, not cumulative actor acquisition or active context. Product coverage is the stated line subset. Repeated reads, system instructions and tool output add acquisition beyond this subtotal. Total cumulative acquisition, host-supplied active context and native spend were not instrumented; no context-fit, efficiency or cost claim is made. The measured interval from prior-expectations creation at 09:21:33.855 UTC to the initial final artifact check at 09:29:48 UTC was 494 seconds; earlier instruction acquisition and this timing annotation are outside that interval, so it is not total activation cost. No external paid call, live tenant trial, proof assistant or statistical experiment was selected. The mathematical checks above are direct reasoning and bounded counterexamples, not externally sourced research or a proof of all possible claims.

The read-only scope included repository status and worktree checks. Unrelated dirty root files and pre-existing untracked commentary were preserved. Only the two assigned commentary artifacts were written.

This judgment is invalidated for affected claims by a change to the bound source, builder basis, claimed scope, assurance policy or material dependency, by a supported contrary interpretation or counterexample, or by a material authorship/independence fact not disclosed here. A future changed source requires applicability review; an unchanged source can reuse this bounded result without relabelling it tenant acceptance.
