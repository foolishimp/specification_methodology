I'll start with the basis and predecessor sources only.

EXPECTATIONS (written from basis and predecessor source only, before opening any candidate, account, conservation, evidence or prior-review material)

Sources read in full: basis/INTENT.md, basis/PRODUCT.md, basis/requirements/README.md, basis/conformance/README.md, basis/requirements/ASSURANCE.md, basis/requirements/A_C_DEPENDENCY.md. Predecessor sections read: REFERENCE_FRAME_METHOD.md §Engagement through §Material Composition (575–709) and §Frame Qualification/Method Self-Qualification (1132–1200). I listed the SPEC_METHOD headings but have not read its body yet. PRINCIPLES, CAPABILITIES, PREDECESSOR_CLAIMS and GOALS are unread so far.

**E1 Generic assessment (changed scope).** I expect the candidate's generic assessment owner (Foundations or Spec Method) to:
- (a) bind every assessment to its producer, subject, governing basis and evidence before it counts toward a required assessment. A judgment returned by a planned assessment but bound to a different subject cannot satisfy that assessment (README "assessment result is bound…"; conformance rows 37–38).
- (b) state applicability as three-valued. A true premise requires the evaluation. A false premise excludes only that obligation, with its cited authority. A missing or ambiguous premise leaves applicability unresolved, not false. A frame name or available tool does not trigger activation (pred. RF Applicability).
- (c) use one conjunction over the core algebra. Missing, stale, wrong-subject, conflicted or indeterminate mandatory results withhold the claim. A failure found by one contributor survives agreement among the others (pred. Result Conjunction; README SRA 6).
- (d) keep not-performed distinct from indeterminate, and keep assessment distinct from the authority to act on it.
- (e) hold for any executor. A human reviewer working from current records and direct observation must be able to conform without code, event streams or replay of complete history (binding req. 2; conformance row 56).
- (f) keep independence conditions: no self-authorship, and a fresh context alone is insufficient.
- (g) keep retained evidence under ASSURANCE change impact. A changed hash alone neither invalidates nor establishes equivalence.

**E2 The five conditional procedure dependencies.** Generic procedures may cite optional profiles (ODD typed-graph, Traversal Occurrence, UX, World Model, Design Module realisation, or operational frame catalogues). I expect each such citation to be conditional ("when selected"). The generic obligation must be obtainable without adopting the profile (SO 8; conformance row 24). The profile owns only its additions, with their selection boundary kept. The trigger, modal force, exceptions and adoption conditions must survive, and no circular referral may occur (Reduction 3; conformance row 23). Provenance links (citing where something came from) must stay distinguishable from operative dependencies (needed for use). A provenance link supplies no conservation. An operative dependency on the predecessor breaks standalone use.

**E3 Optionality.** Preferences stay preferences and "not required" stays not-required. Any change is a fidelity defect without an accepted replacement (row 32). Software execution must not become mandatory.

**E4 Interpretation, compressions, frames and entries.** I expect:
- the a_c interpretation to bind the exact candidate source and its calculus basis (the 2.5.1-rc.2 AXIOMATIC_CALCULUS pin);
- premises, consequences, policies, observations and unresolved claims to stay distinguishable;
- every material owned determination in the changed scope to be represented with its conditions and exceptions;
- compressions and frames to be exact copies that name their owner, or derived views that preserve permitted work;
- every frame that returns a result to carry the core algebra or its mapping;
- an unresolved premise never to be rendered as freedom (row 30).

**E5 Ordinary entry and qualification coordinates (README Standalone; CSR 6; row 33).** I expect:
- root entries and plugin carriers to name the current candidate and its governing input;
- the current interpretation to be distinguished from historical ones;
- the manifest target version to be distinguished from acceptance or publication;
- no "released" standing for the rc preparation, the review archive or a tag;
- qualification routes to point to current evidence and to keep historical returns historical;
- the plugin to supply no successor content from the predecessor during use.

**E6 Inverse consumer metadata.** I expect the consumer relations to be the actual inverse of the stated owner→consumer uses. An empty consumer field is not a defect in itself (instructed). A positive relation that does not match its inverse is a coverage gap, and it stays unresolved rather than satisfied.

**E7 Standing limits.** Mechanical generation or checks support only structural claims. Criterion 4 actual use cannot be satisfied here (the shared trial has not been performed). Criteria 1–3 and 6 depend on predecessor-row and owner-decision evidence that this review touches only for the changed scope.

Now opening the candidate.

Next step: read the SPEC_METHOD construction-assessment owner in the candidate source and compare it with the predecessor's UP-020 text.

Now checking the author's build summary to locate the five carrier dependencies. I'm using it only for navigation; the source text decides.

The five carrier dependencies are plugin skill calls to `PRODUCT_BASIS.md` and `REFRESH.md`. Reading the raw plugin sources next.

Checking the release-preparation return so I can separate preparation from release acceptance, then the account rows for the changed owner.

Locating the account-by-owner material that carries the consumer fields.

Checking the FRAMES.md acquisition unit for stdo-help, to see whether PRODUCT_BASIS is routed.

Now the compressions: checking how they project the changed assessment owner.

The SPEC_METHOD compression may present the disposition values as assessment outcomes. Checking whether prior closed reviews already covered this.

The rc1 overlay rebinds the conservation rows; the I5 record keeps its historical pin by design. Checking the overlay row for the changed owner.

# FINAL REVIEW: Codex STDO v3 candidate `ea27616b93c80b13ee15a9931cd9114275e5de13` (common input `4c340f7a…`, predecessor v2.5.1-rc.2)

## Judgment

**Not ready for selection in the scoped areas. No overall acceptance is supported.**
- **One confirmed medium-severity fidelity defect:** the SPEC_METHOD compression contradicts the changed source on what an assessment returns.
- **Two confirmed low-severity defects:** two views missing from the refresh registry, and an unspecific package entry.
- **The changed owner itself:** the source repair and its exact copies in the frames are faithful.
- **Still unresolved:**
  - whether the changed row is conserved or superseded;
  - how the five new carrier calls are acquired in the generated interpretation;
  - the eleven unmatched positive consumer relations;
  - all actual-use evidence.

None of this establishes a winner, acceptance, release or universal proof. The release preparation and review archive are packaging work: they are not a selected, tagged or released cut.

## Confirmed defects

**D1. Medium: the SPEC_METHOD compression turns dispositions into assessment outcomes.**
- **Where:** `candidate/standards/authority_compressions/spec_method.compressed.md:388–393`, "Assess a bounded candidate as `accept`, `local_repair`, `re_enter`, or `reject`."
- **What the source says:** the owner (`SPEC_METHOD.md:1926–1959`) evaluates a cone-preservation predicate in the core result algebra. The assessment returns evidence and a proposed disposition, and only the existing decision authority applies it ("an assessment verdict is not acceptance authority"). The source table maps each disposition to a core verdict:
  - `local_repair` for inadequate proof → `indeterminate`;
  - `re_enter` for an unusable basis → `invalid_basis`;
  - the remaining cases → `satisfied` or `falsified`.
- **Trigger:** this asset targets the `evaluate_review_grade` prompt family (lines 7–10). A reviewer prompted from it would report a disposition as its verdict.
- **Consequence:**
  - review and decision authority are conflated, which the source forbids;
  - the compression implicitly defines a result set outside the core algebra;
  - the indeterminate and invalid-basis distinctions are lost (single result algebra items 2, 3 and 5; conformance rows 32 and 61).
  - The header's general deferral to its owners (lines 30–34) does not repair a line that states the opposite.
- **Prior coverage:** the I5 derived review only covered changed compression bodies ("does not re-review every unchanged compression paragraph"). This paragraph is unchanged from the predecessor (`predecessor/…/spec_method.compressed.md:367`), so it has never been checked against the revised source.
- **Smallest repair:**
  - In that compression, restate the paragraph: assessment returns the core verdict on the exact predicate plus a *proposed* disposition, with the four-way map; only the bound decision authority applies it.
  - Refresh that compression's pin and its reconciliation record.
  - Related, lower risk: `stdo_compressed.md:815` ("Disposition bounded candidates as …") keeps the decision wording but omits the core-verdict map. Repair it in the same pass.

**D2. Low: the refresh registry omits two of the seven views.**
- **Where:** `plugins/spec/references/REFRESH.md:40–46` lists five views ("The five views project…"). `frames/TRIAGE_CARRIER.md` and `frames/MEMBER_CONSTRUCTION_ASSESSMENT.md` exist, and `standards/README.md:36–43` routes to both.
- **Trigger:** `/spec:refresh --doc` for either view.
- **Consequence:** step 2 refuses it as an unknown name. Ordinary acquisition still works through direct resolution (`stdo-help:25–26`, `stdo-work:20–41`), so this is an incomplete route, not lost content.
- **Smallest repair:** add `triage-carrier-view` and `member-construction-assessment-view` rows, change the text to "seven views", then regenerate the REFRESH row and its pin.

**D3. Low: the package entry does not state its standing against the manifest version.**
- **Where:**
  - both `plugin.json` files carry `"version": "3.0.0-rc.1"`;
  - `candidate/README.md` names neither the candidate identity nor its governing input;
  - nothing in the entry says that version is a target rather than an issued cut.
- **Partial mitigation:** `standards/README.md:100–106` and `README.md:23–24` say distribution presence and source assessment confer no release.
- **Requirement:** the Standalone requirement asks that "a target version in a manifest is distinguished from acceptance or publication at the package entry".
- **Smallest repair:** add one sentence to `candidate/README.md` stating that `3.0.0-rc.1` is the target label, with no cut, acceptance or publication. This could be judged satisfied by the general clauses; I record it as low severity, not as a blocker.

## Disputed or unresolved claims (not defects)

**U1. Is the changed row conserved?** The predecessor said "exact live code" (`predecessor SPEC_METHOD.md:1558`); the candidate says "exact live realisation under the selected computational binding" (`SPEC_METHOD.md:1889–1890`).
- **What is preserved:** exact subject, authority paths, proof, installed subject, the summary prohibition, independence, and no prescribed actor count.
- **What is open:** the common binding requirement (README items 2 and 125–127; conformance row 56) requires this generality. On the same human-process case, though, the predecessor could not be satisfied without code and the successor can. So it is unclear whether this is relocation-equivalent conservation or a changed determination, which would need a superseded disposition plus an owner decision.
- **Current records:** the rc1 overlay (`CONSERVATION_APPLICABILITY.json:14691–14709`) keeps the row `conserved`, with the standing "affected_scope_requires_current_independent_assessment".
- **My judgment:** `indeterminate` under the disposition requirement. The comparison cannot decide it without an owner-recorded reading.
- **Repair:** record the scope argument (the predecessor's "code" was the software instance of the realisation), or move the row to `superseded`, citing the owner's ratification of the binding requirement.

**U2. Typing of the five new carrier calls.**
- **What I found:** in the shipped account, the calls from help, review, status, ticket and refresh appear only in the untyped `dependencies` list. They have no `dependency_relations` entry (for example `account-by-owner/…refresh__SKILL.md.json:36` versus 38–84). The stdo-work entry is typed.
- **What exists elsewhere:** the patch's quote, modal force and `required_when` evidence stays in `RECIPROCAL_CALL_PATCH.json`. In `program.json` the edge is a `declared-dependency` (for example line 3948) with no acquisition-route record.
- **Assessment:** the conditions are preserved through each row's applicability, and the inverse consumers match (`PRODUCT_BASIS` lists all five skills; `REFRESH` lists the refresh adapter).
- **Open question:** whether the native projection closure follows untyped declared dependencies. I did not run it, so ordinary symbolic acquisition of these calls is unresolved.

**U3. Applicability of the refresh adapter row.** The row says "explicitly selects … or its stated governed-task trigger applies", which is broader than the manual-only source (`disable-model-invocation: true`). The row's obligation, "Invoke only manually", restores the source meaning, so this is a risk rather than a defect.

**U4. Eleven unmatched positive consumer relations.** These remain unresolved as instructed. I did not adjudicate them.

**U5. Release preparation.** The author's return records two gaps:
- the current loader excludes `interpretation/`, although `stdo-work:53–59` and both READMEs route to it;
- the encoding-theory URI fails the cohort's cross-cut check.

Both remain release blockers pending owner decisions. They are not candidate-text defects.

## Coverage

**Read in full:**
- basis: INTENT, PRODUCT, requirements/README, conformance/README, ASSURANCE, A_C_DEPENDENCY;
- predecessor: REFERENCE_FRAME_METHOD:575–709 and 1132–1200, SPEC_METHOD:1503–1637;
- candidate: SPEC_METHOD:1816–2165, FOUNDATIONS:201–232, root README, standards/README, interpretation/README;
- all five plugin skills, both references, both plugin manifests;
- spec_method.compressed:1–43 and 365–418; stdo_compressed:798–819 and 978–991;
- MEMBER_CONSTRUCTION_ASSESSMENT:1–60, 381–414, 600–631 plus its heading list;
- the account rows for the changed owner and its baseline consumer; the account-by-owner rows for the seven plugin carriers;
- one patch excerpt; the program records near the new edges.

**Grep-verified:**
- the frames' copies of the changed paragraph (WORK_RECOVERY:566, TRIAGE_CARRIER:1028, MEMBER_CONSTRUCTION_ASSESSMENT:621);
- no remaining "exact live code" anywhere;
- the conditional profile clauses (`Where DESIGN_MODULE_METHOD.md applies`; "an optional profile adds duties only where adopted").

**Unassessed:**
- PRINCIPLES, CAPABILITIES, PREDECESSOR_CLAIMS and GOALS;
- the other compression paragraphs; the bootstrap compression beyond a grep;
- the bodies of CONSTITUTIONAL_DERIVATION, DOMAIN_BINDING, EVALUATION_CONJUNCTION and RELEASE_ADOPTION, and the unread parts of the other three frames;
- the remaining 706 account rows; GETTING_STARTED; templates and schemas;
- every predecessor row outside the changed owner;
- the native generation and projection closure (not run);
- the eleven unmatched positives.

## Justified reuse

- I used the I5 derived review only for its stated scope: changed compression bodies and the reproduction of all seven views at that freeze. I did not extend it to D1's paragraph.
- I relied on no prior conclusion for the changed owner or the five calls.

## Contributions to the six criteria

| Criterion | Result in this scope |
|---|---|
| 1. Disposition completeness | Indeterminate. Only the changed row was checked, and it has one disposition. |
| 2. Conservation | Indeterminate for the changed row (U1). |
| 3. Accepted replacements | Not assessed. I found no owner decision covering U1. |
| 4. Actual use / context fit | Unresolved. The shared trial has not been performed and context fit is unmeasured. |
| 5. Fidelity / conformance | Falsified for D1's projection. Satisfied for the changed owner, its account predicate and its three frame copies. U2 is unresolved. |
| 6. Governing reduction | Not assessed. The change adds no new mechanism. |

## Resource limits

- **Spend:** about USD 4.3 of 6 when this review was written, by the visible counter; the parent joins the measured value.
- **Elapsed time:** unavailable.
- **Byte acquisition:** not instrumented.
- **Actions:** only Read, Glob and Grep, no external calls; I made no changes.
- **Context fit:** not claimed.
