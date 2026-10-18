## Standard applied

Judged against the predecessor section in each row file. An added sentence that binds the section to a shared owner counts as a change only where it adds an obligation or condition on a case the predecessor already decided, or widens scope; pure pointers, derivation notes and additive core-result mappings that leave the predecessor's conditions intact do not (per the packet conventions). Relocation to another owner is conservation (`common/README.md` 67). All line numbers refer to `A/standards/…`, `B/standards/…`, `rc2/standards/…` or `common/…` inside the packet.

## Rows

**07 `DESIGN_MODULE_METHOD.md#14-design-review-questions`**
- Claim: when reviewing code, ask the 56 listed questions; if they cannot be answered cleanly the realization is too coupled or too imperative.
- A: changed (1, 4). The 56 questions become nine owner-mapped families (A DESIGN_MODULE_METHOD.md 2385-2395) entered via "Review the exact adopted boundary and claim by applying Contract application" (2379-2380); the conclusion becomes "A missing answer on a required relation prevents the corresponding design-conformance claim; use the owner to determine whether the defect is coupling, imperative meaning, incompleteness..." (2398-2401); results go "through the shared result contract" (2397-2398).
- B: unchanged. All 56 questions (B DESIGN_MODULE.md 2098-2239); conclusion kept at 2241-2242.
- Same change? n/a.
- Only in A: owner-routed diagnosis, the "missing answer prevents the claim" consequence, result through the shared result contract. Only in B: the explicit question list.
- Common input: A permitted (README 63 contraction into owners; README 110 diagnosis routed to its owner; README 162 judgments in the core). B permitted (README 54 unchanged text).
- Records accurate? A yes; B yes.
- Worth carrying across? A→B, modest: B's reviewer who cannot answer e.g. question 50 (a missing discovery record) must conclude "too coupled or too imperative" (B 2241-2242), which README 110 ("routes each supported repair to its affected owner rather than inferring a repair from the intake label") disfavours. B→A: the list is acquisition convenience, not a gap.
- Note: A trades a checklist for owner references; whether that costs acquisition is a criterion-4 question, not a meaning one.

**08 `DESIGN_MODULE_METHOD.md#6b-module-derived-unit-test-rule`**
- Claim: unit tests are module-owned proof lanes, derive from module ownership evidence (five sources), not primarily from code shape (five sources); helper tests allowed but never the canonical proof surface; no module-derived lane means not closure-ready; DMM owns the concept, not UAT meaning.
- A: changed (1). Inserted A DESIGN_MODULE_METHOD.md 1877-1884: apply Parallel assurance and provenance; "A test discovered from implementation is re-expressed and justified against that module obligation before it supplies module closure." Rest verbatim 1865-1925.
- B: unchanged. B ASSURANCE.md 1037-1072; ownership kept with the design profile (1037-1043); indicative wording for "must" (1045-1046, README 34); closure-ready rule 1069-1071.
- Only in A: the re-expression condition and provenance binding. Only in B: pointer to the unit frame (1071-1072), not material.
- Common input: ASSURANCE.md 64 is common law both carry at their assurance owners; A's consumer binding is permitted, not required at this locus.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither: B already excludes implementation-shaped tests as canonical proof (1057-1064); A's clause is a conditioned permission, not a missing obligation.
- Note: B relocates the owning locus to ASSURANCE §15 while naming the design profile as the authority source, which the conventions treat as conservation.

**10 `DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019`**
- Claim: component role sets (technology confers no authority; three cases, two require re-entry); the design must project domain design into its computational realization; producer-to-consumer path identification using the UP-021 validity/reuse relation; operational assumptions declared with cost separation; projection subordinate; two-part disposition; four falsifiers.
- A: changed (1, 4). Inserted A DESIGN_MODULE_METHOD.md 1632-1644: the projection "applies the build-tenant binding"; "A machine stack, a human procedure and a mixed process each state their operations, composition, effect locations, authority and material resource measures" with units and observation boundaries; validity relation re-owned to FOUNDATIONS workspace-and-context (1648-1651). Rest verbatim.
- B: unchanged. B DESIGN_MODULE.md 1623-1714; cost separation relocated to ACTIVATION §6 (1665-1667; carried at B ACTIVATION.md 1596 "one cannot conceal another"); validity relation to ACTIVATION §4/§7 (1655-1657); falsifiers 1708-1714.
- Only in A: human/mixed binding obligations stated at UP-019. Only in B: none material (B binds build tenancy at DESIGN_MODULE.md 171 and SPEC_METHOD §11).
- Common input: README 122-126 require the Spec Method to state and apply the binding; A does it here, B at SPEC_METHOD.md 1782-1976 (1803, 1813-1815, 1868). A's consumer restatement permitted, not required here.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: B's "Three cases are distinguished" for "must be distinguished" is indicative law (README 34).

**13 `ODD_METHOD.md#19-ramp-up-checklist`**
- Claim: an LLM ramping into an ODD product should quickly answer 14 questions; if not, the product is not yet sufficiently ODD-shaped.
- A: changed (1, 4). Prose compression of the questions (A ODD_METHOD.md 1827-1831; question 7, the projection/query lane, is not explicit); new condition "The entry is sufficient only when that material lets the actor determine..." (1833-1836); "Apply Contract application to this acquisition claim" (1837-1838); diagnosis narrowed to "not yet sufficiently specified for that ODD entry" (1838-1839).
- B: unchanged. Fourteen questions B ODD.md 1756-1777; conclusion 1779-1780.
- Only in A: sufficiency condition, Contract application, entry-scoped diagnosis. Only in B: explicit questions including q7.
- Common input: not material; A permitted (README 67, 110).
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: A restores "should" (1827) as its record says.

**14 `POSTING_GUIDE.md#boundary`**
- Claim: use a post for provisional, investigative, comparative, argumentative or not-yet-ratified content; never for live requirements, live design decisions or active process law, which belong in bound WHAT or ratified design.
- A: changed (1). Inserted A POSTING_GUIDE.md 23-27: "Before publishing a review or handoff, apply Workspace and context ... and report any judgment through the complete core result"; lists verbatim 30-44.
- B: unchanged. B POSTING_GUIDE.md 35-40.
- Only in A: pre-publication acquisition and core-result reporting; "commentary cannot supply an absent decision" (27).
- Common input: README 162/174 put review judgments in the core; B carries this globally at B FOUNDATIONS.md 865 ("No outcome exists outside the core") and its posting guide has no result clause (grep empty). A's binding permitted; not required at a guide (README 143-144).
- Records accurate? A yes; B yes.
- Worth carrying across? Neither: a B reviewer's judgment is bound by FOUNDATIONS 865 wherever posted.
- Note: none.

**15 `REFERENCE_FRAME_METHOD.md#evaluation`**
- Claim: an evaluation is a declared question whose admissible result family, evidence basis, decision authority and (for material action) operation authority are known; it may ask for eight kinds of answer; a family shares manifold, authority basis and result algebra; similar wording proves nothing.
- A: changed (1). "whose predicate, admissible evidence..."; "Its results use the core result algebra directly or a declared reason-sensitive refinement under RF-012" (A REFERENCE_FRAME_METHOD.md 123-126); family shares a "result binding or refinement of that one algebra" (130-131).
- B: unchanged. Table rows B FOUNDATIONS.md 112-113 verbatim.
- Only in A: the single-algebra binding at the definition.
- Common input: README 162-163 and PRODUCT 138 require one algebra; A's change is required in substance; B satisfies it at FOUNDATIONS §4 Results (790; 865). Locus is a tenant choice.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: B's "admissible result family" is constrained by its §4 owner, so no parallel algebra is permitted by the definition.

**16 `REFERENCE_FRAME_METHOD.md#evidence`**
- Claim: evidence is the exact observation or artifact admitted for an evaluation; carries provenance, subject identity, basis, scope; becomes neither truth nor authority by being in a frame.
- A: changed (1). Added reliance contract A REFERENCE_FRAME_METHOD.md 205-210: bind Construction assurance; "A sufficiently small frame or an authenticated observation alone does not establish a sound, complete decision".
- B: unchanged. B FOUNDATIONS.md 66 (table row; "admitted to evaluate a claim on a basis" is restatement).
- Only in A: the reliance contract.
- Common input: ASSURANCE.md 47, 62 are common law; B carries them at FOUNDATIONS §4 (1230, 1302). Consumer binding here permitted, not required.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: B's cited locus is a 327-line range; the deciding text is one table row.

**18 `REFERENCE_FRAME_METHOD.md#independently-activated-co-evaluation`**
- Claim: several frames may evaluate one subject through separate activations returning closed results; overlap allowed; neither consumes the other's unclosed working result.
- A: changed (1). Added A REFERENCE_FRAME_METHOD.md 785-789: for a mutual-assurance claim apply Parallel assurance and provenance; separate activations "do not by themselves establish statistical independence".
- B: unchanged. B REFERENCE_FRAME.md 618-623.
- Only in A: the mutual-assurance obligation at this locus.
- Common input: ASSURANCE.md 66; B carries it at B FOUNDATIONS.md 1341 ("model families or codebases do not establish statistical independence").
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**26 `REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates`**
- Claim: every result binds exact subject, basis, coordinates, evidence scope; a stale, advanced, ambiguous or mismatched basis returns `invalid_basis` or requires reactivation; apparent equality is not coordinate equality.
- A: changed (1, 4). `invalid_basis` only where the governing basis "cannot support interpretation of its bound predicate" (A REFERENCE_FRAME_METHOD.md 411-413); stale supporting evidence → `indeterminate` under RF-012 (413-416); "A basis advance ... does not by itself invalidate a historical result" (416-417); reuse via Change impact (409-411).
- B: unchanged. B REFERENCE_FRAME.md 320-324 verbatim ("never substitutes").
- Only in A: governing-basis vs supporting-evidence split; advance does not auto-invalidate; applicability relation for new reliance.
- Common input: ASSURANCE.md 115 ("A changed hash alone establishes neither invalidity nor equivalence") and README 97 (reuse of closed results follows change impact): A's change is aligned and required in substance. B's literal RF-005 (321-322) and B FOUNDATIONS.md 1455-1456 (the same ASSURANCE 115 law) decide the same question differently (README 150).
- Records accurate? A yes; B yes (text conserved).
- Worth carrying across? A→B yes: a B reader of RF-005 alone treats any basis advance as `invalid_basis`/re-run, against ASSURANCE 115 and B's own FOUNDATIONS 1455.
- Note: B's result tables also return `invalid_basis` on "advanced" (B REFERENCE_FRAME.md 579, 588), so the tension is carried into consumers.

**30 `SPEC_METHOD.md#agentic-construction-execution-stdo-up-020`**
- Claim: when construction is delegated to a probabilistic/agentic worker the method governs the execution relation without prescribing model, prompt, tools, search, topology, layout or runtime; the nine-step normative relation.
- A: changed (4). New framing A SPEC_METHOD.md 1826-1841, including "A human, machine or mixed binding remains subject to the same affected obligations; an optional profile adds duties only where adopted" (1840-1841); predecessor text verbatim 1843-1860.
- B: unchanged. Non-prescription and all nine steps in prose, B ACTIVATION.md 39-49, relocated to ACTIVATION §1.
- Only in A: scope extension to human/mixed bindings; F1–F6 derivation. Only in B: none at this claim.
- Common input: README 125 (generic procedure scope independent of execution environment) supports A's extension; B's step is generic already (B ACTIVATION.md 32-37).
- Records accurate? A yes (its listed duties sit mostly in subsections, but the parent's scope sentence is itself a change); B yes.
- Worth carrying across? Neither.
- Note: none.

**31 `SPEC_METHOD.md#canonical-compression`**
- Claim: the one-paragraph compression (spec as constitutional source; WHAT/HOW; the `stdo_<label>.json` definition as routing overlay; bounded-context resolution; mandatory ambiguity detection; "Code realizes decisions"; derivability of design and code; "Events, projection, and delta reveal drift"; supersession; gap analysis; sprints).
- A: changed (4). "Realization, including code in a software binding, implements decisions" (A SPEC_METHOD.md 85-86); "realization must be derivable" (88); "Observations and their selected projections reveal drift; events are one durable observation carrier" (90-91).
- B: unchanged. B SPEC_METHOD.md 107-145 ("Code realises decisions" 132-133; "Events, projection and delta reveal drift" 135-136); file name delegated to PRODUCT_DEFINITION §1 (111-117), a packaging format (README 145).
- Only in A: realisation/observation generalisation.
- Common input: README 125 makes code and event streams conditional; A aligned; B carries that qualifier at B SPEC_METHOD.md 1813-1815.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: "graph functions" → "functions" (B 129) is a term generalisation, not an obligation change.

**32 `SPEC_METHOD.md#construction-assessment-and-delegation`**
- Claim: constructor owns bounded implementation and self-review; where independent assessment supports promotion the assessor evaluates exact live code, authority paths, proof and installed subject, not the constructor's summary; no actor count; one actor may hold different roles across claims; proxy powers and limits; no human ceremony where basis, cone, envelope and re-entry are accepted; direct entry as constructor/Writer without an Executive activation; one grant may span construction/status/checkpoint; material change needs the binding resolved; Executive mutation restrictions remain.
- A: changed (4). "the exact live realisation under the selected computational binding" (A SPEC_METHOD.md 1898-1900); "Apply Independent assessment" (1896-1897); the explicit one-actor-several-roles sentence is replaced by "The selected configuration binds actors to that claim under the shared independence conditions" (1902-1903); A FOUNDATIONS.md 276-303 gives claim-relative authorship but not that explicit permission. Rest verbatim 1905-1931.
- B: changed (4), marginal. "the assessor evaluates the exact live subject, its authority paths, proof and installed state" (B ACTIVATION.md 642-644); proxy limit relocated to B FOUNDATIONS.md 174-176 with "the governing outcome's meaning" for "Product meaning"; "No coordinating activation" for "No Executive activation" (664-665); mutation restriction generalised to any coordinating role (701-706). Explicit one-actor-several-roles kept (645-647). New "Recording a result without review" (675-694).
- Same change? Partly: both widen the assessment object beyond code; A names the computational binding, B generalises the coordinator and proxy object.
- Only in A: "under the selected computational binding"; Independent-assessment owner binding. Only in B: the explicit one-actor-several-roles permission (645-647); recording-without-review conditions ("states only conditions that were evaluated", 681-682; insufficiency "withholds the dependent effect", 687-688); a named decision owner (640-641).
- Common input: README 125 (human/mixed environments) supports both widenings; README 96 (no prescribed role inventory) supports B's generalisation.
- Records accurate? A yes. B: `conserved` over the same code→subject widening that A's own record calls a meaning change; inaccurate on a strict reading, marginal and contestable (rc.2's "installed subject" already covered non-code subjects partly). What would settle it: whether rc.2 admitted non-software build tenants, which the packet does not show.
- Worth carrying across? B→A: the explicit one-actor-several-roles sentence; A's owner implies it ("prescribes no actor count", 1903; "not an author of the reviewed subject", FOUNDATIONS 280-281) so no reader acts wrongly without it. A→B: none.
- Note: B's recording-without-review paragraph is an elaboration of "condition-based result recording" consistent with README 167.

**33 `SPEC_METHOD.md#manifesto`**
- Claim: thirteen commitments; "If these claims do not hold, the work is not genuinely spec-driven."
- A: changed (1, 4). Code → realisation (A SPEC_METHOD.md 268, 270, 279); evidence "through the observations and proof surfaces appropriate to their declared realization, including scenarios and tests" (274-275), dropping events/projection/delta as named carriers.
- B: unchanged. B SPEC_METHOD.md 283-306 ("code" 291, 300; "scenarios, tests, events, projection and delta" 295-296; indicative "the specification changes" 297).
- Only in A: realisation generalisation; evidence carriers by declared realisation.
- Common input: README 125; B qualifies at SPEC_METHOD.md 1813-1815.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**34 `SPEC_METHOD.md#position`**
- Claim: specification is constitutional source; the point is to make software re-derivable, auditable and correctable under explicit authority; declarative bias; the system should declare truths and let lawful processing derive work; imperative procedure subordinate.
- A: changed (4). "make governed work re-derivable..."; "Software, human processes and mixed processes realise the same declared obligations through separately bound build tenants" (A SPEC_METHOD.md 108-110).
- B: unchanged. B SPEC_METHOD.md 30-38 ("make software re-derivable" 31-32). B 40-45 adds an unrelated examples claim outside this row.
- Only in A: human/mixed scope.
- Common input: README 125; B carries it at SPEC_METHOD.md 459, 1803, 1842.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: B drops "In the age of LLMs", a framing cut.

**35 `SPEC_METHOD.md#process-constitution`**
- Claim: the method is the process constitution; four meta-constitutional roles; bootstrap from scratch; the boundary list (including the definition binding authority locations and `how.build_tenants`); strict WHAT/HOW split; default scaffold, requirements at any bound URI; declarative bias; recovery via method plus domain specification.
- A: changed (4), minimal: "design, realisation, evidence" for "design, code, evidence" (A SPEC_METHOD.md 321); rest verbatim 317-357.
- B: unchanged. B SPEC_METHOD.md 49-87 ("code" 52; definition binding relocated to PRODUCT_DEFINITION §1/§8 at 67-73; "any location the product definition binds" 81-82).
- Only in A: "realisation" in the relation list.
- Common input: not material.
- Records accurate? A yes (small but real); B yes.
- Worth carrying across? Neither.
- Note: none.

**37 `SPEC_METHOD.md#reconstruction-litmus`**
- Claim: five ordered derivations ending in conformant Code; derivation not unique; five upstream-defect diagnoses; ADRs load-bearing; hidden ambiguity defeats sufficiency; reuse of an accepted relation after applicability check; route not execution; no restart authority; span by claim; DMM owns the design-view gate.
- A: changed (4, 3). "conformant Realization in its selected execution environment" (A SPEC_METHOD.md 2897); "different software, human or mixed realizations" (2900-2901); "Where DESIGN_MODULE_METHOD.md applies, it owns..." makes the gate ownership conditional (2924-2927).
- B: unchanged. B SPEC_METHOD.md 341-379 (code kept 352, 364-365); generic law at B EVALUATION.md 428-443, which carries "grants no restart authority and does not excuse stale success" (440-441), span and counterexamples (441-443); gate unconditional (376-379).
- Only in A: realisation scope; conditional DMM applicability.
- Common input: README 125; B qualifies elsewhere (SPEC_METHOD.md 1813-1815).
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**38 `SPEC_METHOD.md#testing-strategy-taxonomy`**
- Claim: ownership of the product-assurance context and Product-level taxonomy; every executable proof surface must declare its authority source; ticket as proof authority; two authorities with sources and questions; sandbox-only UAT; sandbox tests exercise the runnable product form from requirement-sourced scenarios; harnessed vs live modes; necessary-not-sufficient; terminology; local lanes map back before closure.
- A: changed (1). Inserted A SPEC_METHOD.md 2657-2663 and 2670-2678: "For each claimed lane, apply Parallel assurance and provenance"; "An implementation-derived regression check retains its supported local scope without being promoted to upstream acceptance."
- B: unchanged. B ASSURANCE.md 143-221, owner relocated to the ASSURANCE member; every determination present (150, 154-155, 161-162, 181-189, 191-207, 209-218, 220-221).
- Only in A: per-lane provenance binding; regression-check standing.
- Common input: ASSURANCE.md 62-64; B carries them at FOUNDATIONS §4 (1302 ff.).
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**39 `SPEC_METHOD.md#transition-evidence-and-proof-cadence`**
- Claim: a reviewable transition identifies the listed items and the assessor disposition; consumers choose representation; transition evidence is a read model; construction uses the cheapest focused proof capable of falsifying the active relation; whole-candidate qualification at a declared boundary unless risk requires it earlier; same-process proof cannot establish durable authority.
- A: changed (1, 3). Selection rule replaced by Change impact plus Risk and assurance selection, binding "supported exclusions, newly uncovered cases and applicable mandatory gates" (A SPEC_METHOD.md 1995-1999); "cheap falsification of a weaker condition cannot close the stronger claim" (2002); earlier whole-candidate qualification "where affected risk, uncertain impact or a mandatory gate requires it" (2005-2006); "the assessor's proposed disposition and any separately applied decision" (1989-1990).
- B: unchanged. B ACTIVATION.md 1762-1780; cheapest-focused-proof rule verbatim 1773-1776; "where an assessor was activated, the assessor's recommended disposition, with the decision owner's disposition beside it" (1765-1767).
- Only in A: risk/impact-qualified selection; mandatory-gate and uncertain-impact triggers; weaker-condition rule; retention with applicability.
- Common input: ASSURANCE.md 74, 107, 119, 121 are common law; B carries mandatory gates at B FOUNDATIONS.md 1159 and 1478; A applies them at the consumer.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**41 `SPEC_METHOD.md#what-how-and-work-carriers`**
- Claim: ownership of the build-tenancy context; one WHAT realized by one or more independent HOW tenants; tenant, tenancy, singleton, multi-tenancy; `what.*` locate WHAT; Tenant Registry as canonical `how.build_tenants`; Common Build-Tenant Surface; `TENANT_REGISTRY.md` companion only; `ticketing.*` bindings; goals own the wave, ticket state is ticket authority, comments non-authoritative.
- A: changed (1, 4). Inserted binding law A SPEC_METHOD.md 912-942: "The binding may use software, hardware, people, organisations or a mixture" (917-918); design-admission obligations (929-933); resource units (934-936); "A tenant cannot repair an inconvenient requirement by silently changing the common WHAT" (941-942).
- B: unchanged. B PRODUCT_DEFINITION.md 742-784 (owner relocated; singleton/multi 755-758; registry 765-773; ticketing 775-782); tenant and relation at B SPEC_METHOD.md 1791, 1829.
- Only in A: the binding law inlined here. Only in B: none (B's SPEC_METHOD §11, 1782-1976, carries the equivalent: 1803, 1813-1815, 1842-1844, 1868).
- Common input: README 122-129; both carry it.
- Records accurate? A yes (its note's "work-carrier selection follows obligation lifetime" is not visible in 902-965, but the inserted binding law supports `superseded`); B yes.
- Worth carrying across? Neither.
- Note: none.

**43 `STDO_REFERENCE_FRAME_BASELINE.md#7-executive-disposes-and-checkpoints`**
- Claim: the Executive verifies bound results, revalidates the complete Product view and current mandate, applies declared conjunction, assigns priority, records boundary effect, acts on exactly one UP-020 disposition; UP-020 owns dispositions; repair → new candidate, review reactivated; acceptance widens nothing; severity/priority/hard-stop rules; blocking determined from claim, mandate, hard stops and Product-owned cutoff; unsupported assessment returned via a new activation.
- A: changed (1). "revalidates the sufficient bounded delivery view" for "complete Product view" (A STDO_REFERENCE_FRAME_BASELINE.md 1605); rest verbatim 1604-1624.
- B: unchanged. B EXECUTIVE_BASELINE.md 1271-1295 ("complete Product view" 1272); blocking determinants relocated to B EVALUATION.md 366 ("the applicable hard stops and the Product-owned cutoff policy"); 1281-1283 adds the README 170 mapping (disposition is the acceptance result), additive.
- Only in A: the bounded view. Only in B: the explicit "neither candidate_ready nor a satisfied review result is acceptance" (1282-1283), derived.
- Common input: PRODUCT 201 ("uses a sufficient bounded view of worker results") and README 94 favour A; B permitted as conserved.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither: when the complete view exceeds an envelope, B's RF-014 (B REFERENCE_FRAME.md 172) supplies the lawful responses.
- Note: A's wording is the one the common construction itself uses for its Executive.

**44 `STDO_REFERENCE_FRAME_BASELINE.md#anti-patterns`**
- Claim: 32 misapplication patterns.
- A: changed (3). Item 10 reframed as authorship while claiming nonauthor assessment, with "reporting defects and rechecking them follows Independent assessment" (A STDO_REFERENCE_FRAME_BASELINE.md 2029-2032); item 11 becomes "inherits the predecessor verdict without established applicability" (2033-2035). Others verbatim.
- B: unchanged. B EXECUTIVE_BASELINE.md 1723-1788; item 11 verbatim "a changed candidate or basis reuses the predecessor verdict" (1742); item 14 names successor owners (1746-1748); item 5 "core result" (1731).
- Only in A: item 11's applicability exception; item 10's recheck carve-out.
- Common input: ASSURANCE.md 115 and README 97 require reuse via an applicability relation; A aligned. B's item 11 is an unqualified prohibition while B FOUNDATIONS.md 1455 carries the common law, so two B loci decide the same question (README 63, 150). PRODUCT 423 supports A's item 10; B's item 10 does not contradict it.
- Records accurate? A yes; B yes (predecessor text).
- Worth carrying across? A→B yes (item 11): a B reader of the anti-patterns treats any post-change reuse as misapplication, against ASSURANCE 115 and B's own FOUNDATIONS 1455.
- Note: none.

**45 `STDO_REFERENCE_FRAME_BASELINE.md#assurance-subject-acquisition-and-evaluation`**
- Claim: acquisition and evaluation are distinct; owner-issued truth is acquired through the exact owner surface; harness, fixture, builder, script, evaluator or Reviewer never reconstructs a parallel owner state; an independent oracle evaluates; generic mechanics cannot mint carriers or interpret meaning; the implementation need not be the oracle; a missing projection stays a named gap.
- A: changed (1). Bindings to Acquire/Evaluate/Faithful projection (A STDO_REFERENCE_FRAME_BASELINE.md 1236-1243); new obligations 1256-1264: state the assertion's predicate and scope; "select the required acceptable relation rather than assuming all valid outputs must be equal"; support checker conformance; 1266-1272 provenance and the implementation-derived-check limit. Exclusion list kept (1245-1248).
- B: unchanged. B ASSURANCE.md 682-713 verbatim ("assessor" for "Reviewer", 688); 691-697 adds the observation-sufficiency return (further evidence, narrower scope or `indeterminate`), an additive core mapping from ASSURANCE 56 that leaves the predecessor's conditions intact.
- Only in A: assertion scope, acceptable relation, checker conformance, provenance. Only in B: observation-sufficiency return (691-697).
- Common input: ASSURANCE.md 47, 56, 62-64; B carries "equality of outputs is not always the oracle" at B FOUNDATIONS.md 1332.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**48 `STDO_REFERENCE_FRAME_BASELINE.md#combinatorial-coverage-and-testing-value-index`**
- Claim: testing value indexed by discriminated material combinations, not counts; eight dimensions; no universal scalar, a project may define one only through authority and must retain coordinates; unit and integration altitudes; material factors; the frame declares the finite population; covering-array reduction only with justification; visitation metrics prove no semantic coverage.
- A: changed (1). Added A STDO_REFERENCE_FRAME_BASELINE.md 1144-1151: risk-qualified selection; cost boundary; "A numeric confidence claim uses that owner's probability, dependence and calibration conditions"; 1118-1119 clarification.
- B: changed (1), minor. Added condition on the scalar permission: "A project-defined scalar is a quantified claim under FOUNDATIONS §4 Quantified assurance and keeps its model and limits explicit" (B ASSURANCE.md 554-556). Rest verbatim 536-594.
- Same change? Partly: both bind numeric claims to the quantified-assurance owner; A adds selection and cost obligations B lacks.
- Only in A: risk-qualified selection, cost boundary, estimates kept apart from measurements. Only in B: none beyond the shared scalar condition.
- Common input: ASSURANCE.md 74-95; B's condition is ASSURANCE 76 applied; both permitted.
- Records accurate? A yes. B: `conserved` over an added condition on a predecessor permission, inaccurate on a strict reading, minor.
- Worth carrying across? Neither.
- Note: a project that defines a scalar without a stated model was permitted under rc.2 and is not under B; that is the change.

**49 `STDO_REFERENCE_FRAME_BASELINE.md#derived-executive-frame`**
- Claim: the eleven-element Executive frame; no `authorize`/`no_action`; activation is the RFM function; dispositions exactly the four; priority and boundary effect are decision projections; unreliable severity is reactivated or retained, never rewritten.
- A: changed (1). Invalidation row bound to Change impact: "historical result identity and any new reliance follow that shared owner" (A STDO_REFERENCE_FRAME_BASELINE.md 681-684); authority row drops "no operation authority ... arises from the Executive label" (693), carried at A 46-47 "No frame gains admission, publication, mutation, or other operation authority from its label."
- B: unchanged. B EXECUTIVE_BASELINE.md 848-869; label clause kept (855); invariants relocated (854); result in the core (859).
- Only in A: invalidation → applicability assessment. Only in B: the label clause in the row itself.
- Common input: ASSURANCE.md 115 aligns with A; B's invalidation row is the predecessor's, and B binds frame invalidation rows to ACTIVATION §7 at B ASSURANCE.md 359-362.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**50 `STDO_REFERENCE_FRAME_BASELINE.md#derived-generic-specialist-frame-set`**
- Claim: twelve archetypes; labels resolve in the frame-evaluation context; non-hierarchical; every family dispositioned as instantiated, non-material, or explicit residual (uncovered, conditional, conflicted or `out_of_frame`); absence of an artifact proves nothing; no twelve-component rule; refinement records; coverage is the union; a composite is `satisfied` only through a declared conjunction in which every seam preserves identity, coordinate and basis, value or evidence, lifecycle scope, authority and provenance; a missing or non-commuting seam returns the applicable non-satisfied value; no dominant frame; no imported consumer frames.
- A: changed (1). Residual option excludes `out_of_frame` as an inventory treatment (A STDO_REFERENCE_FRAME_BASELINE.md 883-885); the accounting predicate is mapped to core values and "Accounting for a residual does not establish adequate coverage" (887-898); the seam rule becomes a reference to Result Conjunction (912-917). The explicit seam-preservation list and "missing or non-commuting seam returns..." are not in A's section, not at A REFERENCE_FRAME_METHOD.md 791-807 or 773-841, and a phrase search of A's RFM, FOUNDATIONS and baseline finds no "lifecycle scope" or "carried value or evidence".
- B: changed (1), disclosed by its child row. Seam-case table B EXECUTIVE_BASELINE.md 1078-1085: an unaddressed seam is "uncovered coverage, a gap with no value of its own"; a failing seam is `falsified`; undeclared translation `out_of_frame`. Seam list kept 1071-1074; dispositions kept 1039-1054 including the `out_of_frame` residual (1048).
- Same change? Partly: both route the composite through the core conjunction; A re-maps the accounting predicate, B turns unaddressed seams into gaps rather than values.
- Only in A: the accounting-predicate result mapping (887-898). Only in B: the explicit seam-preservation list (1071-1074) and the seam-case table (1078-1085).
- Common input: README 162-163, 171 (conjunction defined once) satisfied by both; README 101 ("A failure and its citations remain visible when separate required coverage is missing") matches B's gap treatment.
- Records accurate? A: `superseded` is right, but the seam-list drop is undisclosed. B: parent `conserved` plus child `superseded` (supplement row 50), accurate.
- Worth carrying across? B→A, conditionally: A's reader has no stated list of what a seam must preserve at this locus or its cited conjunction owners. Cannot decide whether row 17's A locus (`#evidence-or-coordinate-translation`, another reader) carries it in other words; that read would settle it.
- Note: none.

**51 `STDO_REFERENCE_FRAME_BASELINE.md#derived-product-testing-frame-set`**
- Claim: when the profile supports promotion, closure or release assurance, testing is a claim-relative frame set; the runner never selects the frame; where the generic set is adopted, testing frames feed Proof evaluations; Proof is no hierarchy; four frames; overlap allowed; labels carry no assurance value without a declaration.
- A: changed (1). "Apply Construction assurance to each selected testing claim" with requirement source, predicate, observation basis and required assurance (A STDO_REFERENCE_FRAME_BASELINE.md 964-968); derivation 928-935.
- B: unchanged. Trigger restated as selection by configuration or work authority for such a claim (B ASSURANCE.md 351-358), four frames 363-374, overlap/labels 400-403; Proof relation at B EXECUTIVE_BASELINE.md 1101-1105. Additive: fan-out topology 376-398; invalidation-row binding 359-363; "it adopts nothing" (354-356).
- Only in A: the per-claim Construction-assurance binding. Only in B: the fan-out topology and the applicability clause.
- Common input: README 151 (generic determination available without an optional profile) supports B's relocation to ASSURANCE; ASSURANCE 60-62 carried by B at FOUNDATIONS §4.
- Records accurate? A yes; B yes (the restated trigger decides the same case the same way).
- Worth carrying across? Neither.
- Note: none.

**52 `STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`**
- Claim: the eleven-element Reviewer frame; UP-007 decides when review is required, UP-022 the assurance boundary; no universal review round; UP-020 owns assessment and disposition, the Executive applying it as authorized assessor or proxy; no second verdict; repair-risk assessment without ownership; uncertainty recorded; tests inside the manifold; findings bind property, entry, threat model and causal path; retention rules; a suggested repair binds only through its owner.
- A: changed (1). Invalidation row adds "apply Change impact and evidence retention to affected reliance" (A STDO_REFERENCE_FRAME_BASELINE.md 795); 804-808 has the Executive apply the disposition "through Dispose" and states "The Reviewer assessment remains distinct from that decision", dropping the "authorized assessor" label; the actor applying the disposition is unchanged.
- B: unchanged. B EXECUTIVE_BASELINE.md 950-997; invariants relocated (956); result in the core (961); invalidation verbatim (962); "the Executive as the authorised assessor or proxy that applies the one existing disposition" (975-976).
- Only in A: invalidation binding; assessment/decision wording.
- Common input: README 174 (assessing and acting distinct) favours A's wording; B's wording does not merge the results (B 1282-1283).
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**53 `STDO_REFERENCE_FRAME_BASELINE.md#derived-worker-frame`**
- Claim: the eleven-element Worker frame with result "one RFM result plus exactly one candidate_ready/refused/incomplete/re_entry_requested variant"; `candidate_ready` is not `accept`; green tests prove only exercised relations; the label grants no mutation authority; mutate only the granted subject and territory; read scope follows the cone; out-of-territory repair returns to its owner.
- A: changed (1). Invalidation row adds the Change-impact binding (A STDO_REFERENCE_FRAME_BASELINE.md 761); "Apply Judgment and authority to the Worker activation" replaces "The Worker label grants no mutation authority" (767-771), carried at A 46-47 and anti-pattern 7 (2023-2024).
- B: changed (1), disclosed by its child row. Result row: "exactly one work-result value, which carries the one core value ACTIVATION §3 maps it to for 'a candidate is available'" (B EXECUTIVE_BASELINE.md 926). Rest verbatim 929-944; label sentence kept (934).
- Same change? No: A changes invalidation semantics, B the result structure.
- Only in A: invalidation applicability binding. Only in B: the availability mapping; the explicit label sentence at this locus.
- Common input: README 170 and 172 require B's kind of mapping in substance; A's "one RFM result plus variant" is also in A's core (RF-012 replaced under I3-R2-R012, CAUSES.md 11-15). ASSURANCE 115 for A's change.
- Records accurate? A yes; B yes (supplement row 53 child `superseded`).
- Worth carrying across? Neither.
- Note: the child's `incomplete` → `falsified` for the availability predicate lowers standing, as README 164-168 permits.

**54 `STDO_REFERENCE_FRAME_BASELINE.md#executive`**
- Claim: Executive is the label for the frame that selects or confirms the configuration and consumes closed results under existing decision authority; it holds the complete Product view and current mandate needed to prioritise, dispose and select the next action; occupied by human authority or an admitted bounded proxy; not a universal owner, controller, service or observer.
- A: changed (1). "maintains a sufficient bounded delivery view..."; "the Executive need not load the whole Product, every historical result or every worker's context" (A STDO_REFERENCE_FRAME_BASELINE.md 296-301).
- B: unchanged. "It holds the complete Product view" (B EXECUTIVE_BASELINE.md 379-381); proxy admission relocated (384-386).
- Only in A: bounded view; workspace carries the frontier.
- Common input: PRODUCT 201, 356 and README 94 favour A; B permitted as conserved.
- Records accurate? A yes; B yes. The supplement's row 54 child (`#executive-drift-locks-stale-held-result`) concerns the drift-locks clause of rc.2's attention section (row 55, another reader), not this parent's text (rc2 246-260); it does not bear on this row.
- Worth carrying across? Neither (as row 43).
- Note: none.

**58 `STDO_REFERENCE_FRAME_BASELINE.md#testing-evidence-composition`**
- Claim: one execution may yield several bound results combined only through declared RFM relations; four default proof responsibilities; UA-alone and E2E-alone limits; integration and unit cannot substitute; when all are required, a conflict or missing result stays visible to Executive disposition and is not hidden by aggregate green.
- A: changed (1). Added A STDO_REFERENCE_FRAME_BASELINE.md 1225-1232: apply Parallel assurance and provenance; "overlapping claims from one run do not create independent observations"; conjunction preserving failed and missing claims.
- B: unchanged. B ASSURANCE.md 649-678; relations relocated to REFERENCE_FRAME §6/FOUNDATIONS §4 (653-655); "visible to the decision owner's disposition" generalises the profile's Executive to the generic owner (675-676); 657-661 adds the README 169/ASSURANCE 37 clause (each result states its predicate), additive.
- Only in A: dependence accounting for mutual assurance. Only in B: the necessary-condition/sufficiency clause (657-661).
- Common input: ASSURANCE.md 37, 66; both carry them at their owners.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**61 `TICKET_METHOD.md#execution-contracts`**
- Claim: tickets are durable work authority; execution contracts are run-scoped admitted surfaces from ticket, sprint or intake; three lifetimes; not a rival backlog; five purposes including "log the admitted execution basis into runtime/event truth"; the seven-step loop.
- A: changed (1). "record the admitted execution basis on the selected durable work surface" (A TICKET_METHOD.md 140) for the runtime/event-truth log; rest verbatim 122-152.
- B: unchanged. B TICKETS.md 82-103; "log the admitted execution basis into runtime and event truth" (93-94).
- Only in A: recording on the durable work surface; no universal event-truth log.
- Common input: README 125 ("Code, an event stream or reconstruction from complete history is required only when the governing obligations or selected execution binding require it"): A aligned. B's TICKETS states the log unconditionally while B SPEC_METHOD.md 1813-1815 states README 125's conditional, a rival determination at the consumer (README 63).
- Records accurate? A yes; B yes.
- Worth carrying across? A→B yes: a B reader of TICKETS alone requires an event/runtime log for every run, against README 125 and B's own SPEC_METHOD 1813-1815.
- Note: none.

**63 `TICKET_METHOD.md#test-case-authority`**
- Claim: tests are proof projections from admitted work authority along the stated chain; no authority from implementation; acceptance predicates need a supported entry and a threat-model obligation; existing tests authorise no excluded threat; implementation is evidence, not arbiter; the five-step reconciliation order; code cannot authorise changing an expectation; code-driven test changes are defects; repricing must be named before updating tests; stale tickets re-enter triage; a pass is closure evidence only when traceable.
- A: changed (1). Added A TICKET_METHOD.md 1083-1089: apply Parallel assurance and provenance to the expectation path and the executed check; execution provenance names subject, checker, environment, observations, result; no per-test ticket.
- B: unchanged. B TICKETS.md 1216-1259; "graph" → "published function" (1222, 1243) generalises a profile term; pointer to ASSURANCE §3 (1258-1259).
- Only in A: the provenance binding.
- Common input: ASSURANCE.md 62; B carries it at FOUNDATIONS §4.
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

**73 `WRITING_GUIDE.md#practical-layer-checks`**
- Claim: when writing or revising a specification artifact, ask three questions; if any answer is wrong, rewrite or delete.
- A: changed (1, 3). Added acquisition before revising and "A writing review uses the core result on the preservation or style predicate actually checked; shorter text alone establishes neither" (A WRITING_GUIDE.md 102-108); "rewrite or delete within the owning authority. A predecessor determination retains its recorded UP-015 disposition" (116-119).
- B: unchanged. B WRITING_GUIDE.md 103-110.
- Only in A: acquisition; core-result review; owning-authority and UP-015 conditions on rewrite/delete.
- Common input: README 23-28 and PRODUCT 224 own dispositions regardless of a guide; README 162 for judgments. A's conditions are consumer bindings, permitted, not required at a guide (README 144).
- Records accurate? A yes; B yes.
- Worth carrying across? Neither.
- Note: none.

## Tallies

- A: unchanged 0; changed 33; absent 0; cannot decide 0.
- B: unchanged 29; changed 4 (rows 32, 48, 50, 53; 50 and 53 disclosed by `superseded` child rows); absent 0; cannot decide 0.
- "Only in A" non-empty: 33 of 33.
- "Only in B" non-empty (material): 10 (rows 07, 13, 32, 43, 45, 49, 50, 51, 53, 58).
- Worth carrying across, A→B: 4 (rows 26, 44, 61 required by the common ASSURANCE 115 / README 97 / README 125; row 07 a modest second-kind gap). B→A: 1, conditional (row 50 seam-preservation list; settled by reading row 17's A locus).
- Inaccurate records: A 0 (row 50's `superseded` is right but under-discloses the seam-list drop); B 2 (row 32 marginal, row 48 minor), both `conserved` over small undisclosed changes.

## Limits

- Tool calls used: 54 of 200.
- Every one of the 33 predecessor sections and both lines' primary successor loci were read in full. A's long secondary loci (FOUNDATIONS, TRANSFORMATION_LIBRARY, whole frame files, compressions) were read only where a question required it (FOUNDATIONS 276-303; grep of FOUNDATIONS 230-275; RFM 791-807 and grep of 773-841). B's long secondary loci were read by targeted grep (ACTIVATION §6 and whole file; SPEC_METHOD §11; EVALUATION §5-§6; FOUNDATIONS §4; POSTING_GUIDE). Row 32's whole-file A loci (frames, 941-1586 lines each) were not read.
- No departures: no git, network or writes; nothing read outside the two packet locations; quotes kept to 25 words or fewer.
- Packet observations: the supplement's row 54 child concerns `#executive-drift-locks`, whose predecessor clause is not inside row 54's text (rc2 STDO_REFERENCE_FRAME_BASELINE.md 246-260). Row 16's B locus is a 327-line range for a single table row (B FOUNDATIONS.md 66). Row 41's A note mentions carrier selection by obligation lifetime, which does not appear in the cited A locus (902-965). Row 30's A "changed meaning" statement describes duties that live in the subsections (A SPEC_METHOD.md 1862-2051), outside the parent row's granularity.