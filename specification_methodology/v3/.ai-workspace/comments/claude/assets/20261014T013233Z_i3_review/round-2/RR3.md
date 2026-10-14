# RR3: Round 2 regression pass

Subject: frozen `55bbf9e`, `specification_methodology/v3/specification/` and `.ai-workspace/tickets/active/`. Diff: `diff_r1_r2.patch` (round 1 `afb6ad6` to `55bbf9e`).

Reviewer: a Claude context, reviewing cross-family. The common pen is Codex. This pass repairs nothing.

Line references are to the frozen subject files:
- `PRODUCT` = `specification/PRODUCT.md`
- `README` = `specification/requirements/README.md`
- `BASIS` = `specification/REFERENCE_FRAME_BASIS.md`
- `CONF` = `specification/conformance/README.md`
- `A_C` = `specification/requirements/A_C_DEPENDENCY.md`
- `PC` = `specification/requirements/PREDECESSOR_CLAIMS.md`
- `WL` = `tickets/active/T-002-iteration-3-work.md`
- `T2C` = `tickets/active/T-002-CODEX-c3-successor-construction.md`

Installed predecessor standards are cited by file name under `v2.5.1-rc.2/standards/`.

Every finding cites at least one line that the patch adds. Defects that live only in unchanged text are listed under "Pre-existing" at the end.

## Findings

Counts: blocking 0, material 7, minor 13. No finding prevents every conforming member from reaching `accept`.

| ID | Sev | Claim | Evidence | Smallest correction |
|---|---|---|---|---|
| RR3-01 | material | Member acceptance now has two records, and one of them is written by the author. The new Frontier text and the predecessor-claims header place acceptance standing in the tenant's own frontier. That frontier sits in tenant territory, which only the tenant writes. Unchanged law says the ticket, written by the pen, is the only record of a disposition. | PRODUCT:332 "Each tenant's current dispositions and member acceptances are recorded in its own frontier". PC:673 "Current dispositions and acceptance standing are supplied by each tenant's frozen frontier". Against this: PRODUCT:204 (the pen records each decision in the ticket); PRODUCT:249–250 "The ticket is the only record that can authorise an action … no disposition exists until the pen has recorded it"; BASIS:26. | State that member acceptance is the Executive disposition the ticket records. A tenant frontier may cite that entry but does not supply acceptance standing. |
| RR3-02 | material | Three new conformance rows are process or closure cases, placed in a table that CONF:3 defines as criterion 5, a per-member check that separates a correct candidate from a defective one. Row 60 asks criterion 5 to judge a conjunction that includes criterion 5, and refers to "the installed builder's conjunction". PRODUCT:330 now separates the builder's results from the successor's results, so no candidate text can pass or fail row 60. Row 12, applied per member, lets one reviewer return `indeterminate` until the integrated assessment exists, while another marks it inapplicable. The two then reach different member decisions. | CONF:3 "These discriminators are acceptance criterion 5". New rows: CONF:12 "Candidate closure requires the integrated reduction assessment"; CONF:59; CONF:60 "The installed builder's conjunction withholds member acceptance". PRODUCT:330 "Its results and process govern this construction; the candidate's single result algebra governs the successor". | Move rows 12, 59 and 60 into a labelled subsection of construction and closure checks, evaluated at the Executive's conjunction and the integrated assessment. Alternatively, state that they are not applicable to member criterion 5. |
| RR3-03 | material | Criterion 4's limit test cannot be decided the same way twice. The repair adds acquisition through declared routes, but the Limits paragraph still speaks only of context "measured before reading". Nothing says whether material acquired through those routes counts against the declared context limit. Example: a 30 KB frame that acquires 200 KB under a 40 KB limit either fits or does not. | PRODUCT:395 "a frame that fits the declared limits … uses that frame, its subject and declared acquisition routes and tools". PRODUCT:348 "Supplied context is measured in bytes before acquisition; further material acquired … is recorded". BASIS:29. Unchanged PRODUCT:401 "context in bytes … reports the context measured before reading". | Add one sentence to Limits saying whether the context limit bounds supplied context only, or supplied plus acquired material. |
| RR3-04 | material | The shape of the Reviewer's return and the conjunction rule do not match the installed builder, which governs wherever the two differ (PRODUCT:321). The installed Reviewer returns one closed evaluation carrying one result. PRODUCT asks for "the six" criterion results; BASIS says "applicable" ones. Neither says what the evaluation's own result is. The installed Result Conjunction requires the rule to state which results are mandatory, but "applicable mandatory" names none. The installed result family has no value for an inapplicable criterion, and no actor is named to decide applicability. (interested: this wording answers round-1 M5) | PRODUCT:200 "one closed evaluation containing the six acceptance-criterion results … Every applicable mandatory criterion". BASIS:28 "applicable criterion results". STDO_REFERENCE_FRAME_BASELINE.md:1373–1379, which lists one "Reference Frame Method result". REFERENCE_FRAME_METHOD.md:678 "which results are mandatory". REFERENCE_FRAME_METHOD.md:589–600, where applicability is decided before any result is returned. | Name all six criteria as mandatory when applicable. Say who decides applicability and how an excluded criterion is recorded, citing its basis. State that the evaluation's own result is the conjunction of the criterion results. |
| RR3-05 | material | The round-2 record of changed accepted items, which round-1 M4 asked for, omits several changes that this same round made: <br>• criterion 1 now requires "all successor loci" and drops "that resolves"; <br>• the reviewer and merge-variance bullets of Development Isolation, which README:12 lists as a local axiom of the Product Definition; <br>• packaging closure moved from the release-candidate cut to C3 closure; <br>• the identity decision moved earlier; <br>• single-ownership items 2 and 4, a law the owner selected (GOALS:50); <br>• guides and packaging reclassified as supporting rather than tiers; <br>• fresh-actor isolation relaxed. <br>The disposition post gives reasons for some of these. The specification record does not. | GOALS:42 lists only "replacement-meaning authority, the criterion conjunction, whole-candidate reduction, interpretation coverage/fidelity and independence … ordinary acquisition … builder's results". Omitted changes: PRODUCT:392, 212–217, 264–266, 342, 410, 68/344; README:117, 119; BASIS:29; PC:687. | Add the omitted items to GOALS:42, each with a one-clause reason, and mark the local-axiom change as such. This is the M4 class again, not a new class. |
| RR3-06 | material | The admitted contract was edited in place. The admission line still says the block is the current contract under digest `fc6ed…`, but the bytes above it now hash to `bf1557…`. The installed ticket method makes the digest the evidence of admission, so the ticket now shows a drafted revision under the admitted identity. The re-hashed block also carries the "where applicable" comparison escape, which README:59 removes. Effect is limited: no execution follows until the next input names its contract (T2C:75). | Edited lines T2C:63–64. New paragraph T2C:75 "hashes to `bf1557…` … does not hash this revision". Unchanged admission line T2C:73 "ADMITTED, contract SHA-256 `fc6ed…` … This is the current contract". T2C:67 "compare decisions and acquisition with iteration 2 and rc.2 where applicable". TICKET_METHOD.md:675–678. | Restore the admitted bytes. Carry the routing revision as a separately identified draft, and remove "where applicable" from that draft. |
| RR3-07 | material | The new closure rule makes the first-listed item primary, but the new H-M rows give a different primary for findings already routed above. TC-03 is therefore not closed, although T-001:37 records it as repaired. Conflicting primaries: <br>• CR2-04 and CR2-09: I3-03 (:135) and I3-02 (:157); <br>• CR2-21: I3-02 (:136) and I3-01 (:163); <br>• CR4-F3: I3-06 (:143) and I3-08 (:158); <br>• CR5-04: I3-14 (:146) and I3-10 (:160); <br>• CR5-06: I3-11 (:148) and I3-10 (:160). <br>In addition, WL:168 says "I3-05 and I3-12 can close" CR3-F6/F9. | WL:122–124 "its first-listed work item owns the finding's closure". WL:157–163 (H-M rows). T-001:37 "makes the first-listed work item primary". | State that an H-M row's primary owns only the aggregate H finding, and that each constituent CR finding keeps the primary of its own row. Alternatively, reconcile the rows. |
| RR3-08 | minor | Replacement acceptance cannot be checked against a stated record. "or requirements" reads two ways, as predecessor requirements or as common requirements. "Through the owning re-entry" is undefined. No record is named for the owner's acceptance, yet criterion 3 requires that acceptance to be verified. README:29 says "to its owner", while README:109 defines owner as a place in the text. (interested: this wording answers round-1 B1) | PRODUCT:202, PRODUCT:394, README:29 | Write "the product owner accepts any replacement that changes predecessor meaning, recorded in the ticket before the dependent `accept`". |
| RR3-09 | minor | A tenant's own construction binding is restated with a shorter content list than the requirement, and the requirement is not referred to as the owner. Two builders can diverge: one declares only actors, tools and assumptions; the other declares a calculus with its composition laws and resource measures. | New PRODUCT:173 "identify its actors, tools and material operational assumptions". README:96–98, where item 3 lists "operations, composition laws, effects, resource measures". | Replace the list with a reference to the binding requirement and state the scope the requirement applies at. |
| RR3-10 | minor | Fresh-actor isolation was relaxed and is now ambiguous. "Outside any repository" became "outside repository instruction loading". "A trial of standalone successor use" is undefined, so it is unclear whether criterion 4 trials may follow links into the installed predecessor. The change is not recorded (RR3-05). | BASIS:29, PRODUCT:356 | Keep the "outside any repository" condition, or state the permitted locations. Say whether criterion 4 trials are standalone-use trials. |
| RR3-11 | minor | The a_c concerns were split four ways (theory, interpretation, carrier, checker). The categorical standard still groups tools with carriers, against that split. | A_C:5–10. Unchanged README:162 "its carriers (the files and tools that hold it)". | Change README:162 to "carriers and checkers". |
| RR3-12 | minor | The new Fixed Theory paragraph binds the required interpretation's encoding basis to the predecessor's calculus file by digest. It is not scoped to construction, so it is in tension with standalone completeness and with the open decision on identifiers. | A_C:43 "This is the calculus basis used to encode the required interpretation". PRODUCT:13 "complete without the previous release in force". PRODUCT:410. | Scope the paragraph to construction and checking under this builder. Leave the release's encoding basis to the identity decision. |
| RR3-13 | minor | "Normative tiers" is undefined. Guides now count as supporting, not normative, yet they still own conventions that an actor must apply. README:14 calls such a convention a determination. README still says "owning tier" and "tier obligations" for guides and packaging, while PRODUCT calls the same table the "C3 responsibility table". | PRODUCT:68, 344. README:112–117. PRODUCT:334 "Tier obligations". | Define "normative". State that guide-owned conventions bind within their scope. Use one name for the table. |
| RR3-14 | minor | The loci rule assumes every claim has a shared owner, which pushes builders to invent sharing for claims that only one domain profile owns. Criterion 1 also drops "that resolves". | PRODUCT:392 "its shared owner and necessary domain or consumer bindings". PC:686. | Write "its owning locus and any necessary bindings, each resolving". |
| RR3-15 | minor | The new outcome-driven development row and the new I3-05 exit text can be read in two ways: <br>• generic transition contracts govern all construction; <br>• the optional outcome-driven development profile must govern construction. <br>The second reading conflicts with that profile's optional status. | CONF:15, WL:100. PRODUCT:85. README:123. WL:99 "optional ODD". | Write "the generic outcome-driven transition contracts, wherever owned, govern …". |
| RR3-16 | minor | The reduction comparison fails a candidate only when the comparison is missing. The text does not state what comparison result against the preceding candidate falsifies reduction: for example, a regression against the preceding candidate that is still an improvement on the predecessor. The author chooses "measures appropriate to the claim". This bears on the closure of round-1 M2. | README:59–64 | Name the comparison outcomes that prevent a satisfied conclusion, for example an unjustified increase in acquisition or in reconciliations relative to either comparator. |
| RR3-17 | minor | The triage records a Product re-entry, but the repair edits Intent, which sits upstream of that re-entry point. | T-001:9–10 (`product_reprice`, re-entry PRODUCT.md) and T-001:25. INTENT:13 changed. | Record the Intent edit as a wording alignment with its reason, or raise the re-entry point to Intent. |
| RR3-18 | minor | A stale present-tense statement contradicts the revised routing. | Unchanged WL:27 "The successor common input is recorded in T-002's snapshot". New T-002:30 and WL:95: the next input "is selected and recorded explicitly". | Mark WL:27 as historical. |
| RR3-19 | minor | Writing: <br>• INTENT:13 introduces four pillar names with no context, and its names differ from the Product pillar names ("objects and their boundaries", "axiomatic representation"). <br>• Indicative verbs stand where obligations are meant: PRODUCT:23 "those claims meet", README:154 "establishes", which loses the earlier "only". <br>• "Construction-authorised amendments" (GOALS:17), "Required unresolved coverage" (PRODUCT:403) and "peer-review mutation" (PRODUCT:216) are compressed or undefined. <br>• PC:666 "Current member acceptances are reopened as recorded in GOALS" reads as covering both tenant lines, and cites GOALS, which only reports standing, as its source. <br>• One gate has three names: whole-interpretation acceptance (README:72, CONF:23), candidate acceptance (README:75) and C3 closure (PRODUCT:403). <br>• GOALS:42 adds a model-family name ("Claude's round-1 review") in the same round that removed one from PRODUCT:179. | As cited | Make the matching wording edits. Use "the cross-family round-1 review". |
| RR3-20 | minor (interested) | "A material contribution to … the repair under review" does not say whether a reviewer's own proposed correction, once the pen adopts it, counts as authorship when the same reviewer assesses the repair. This affects every repeat review round, including this one. | PRODUCT:399 | Say whether findings and suggested corrections count as authorship of the repaired text. |

## Clean: changed passages with no defect found

These passages were checked against the six criteria and no defect was found. Items marked interested judge wording that answers Claude's round-1 corrections.

- **PRODUCT**
  - the pillar table and the paragraph that follows it (PRODUCT:43–52);
  - Construction Authority's de-naming (PRODUCT:179);
  - "the conjunction is not erased" and the withholding causes (PRODUCT:200, interested);
  - the merge variance (PRODUCT:264–266);
  - the Outcome bullets and the separation of builder results from successor results (PRODUCT:326–330);
  - the coverage-input paragraph (PRODUCT:344);
  - Executive loop steps 4–5 (PRODUCT:379–384);
  - criterion 5 apart from RR3-02 (PRODUCT:396);
  - the open owner decisions on review assignment (PRODUCT:407).
- **BASIS**
  - the common-definition result, which maps the round-1 value set into the installed family (BASIS:24);
  - the Writer row (BASIS:27).
- **CONF**
  - the header text and the new reduction, fragment and projection rows (CONF:5, 13, 14, 23, 24).
- **A_C**
  - the four-way split, proof claims and record list (A_C:5–10, 63, 67).
- **README**
  - the definition of a material determination (README:16);
  - the foundation-to-law binding (README:42);
  - constraint-surface items 2, 3 and 6 (README:71–75);
  - the workspace item (README:86);
  - the frame copy and derived view rule (README:119);
  - the result/data paragraph (README:146).
- **GOALS**
  - GOALS:11, the new checkpoint row at :18, the projection role at :24, and :32.
- **Tickets**
  - T-002:30–32;
  - the T-001 review-repair section (T-001:21–37) apart from RR3-07 and RR3-17;
  - the work list I3-00, I3-02, I3-08, I3-09, I3-14 and I3-16 rows, the decision dependencies, and the reported peer findings, which are scoped and unassigned (interested).

## Round-1 "holds" results

- **5, neutrality: holds.** No new requirement can be met by only one tenant's present design. Both exact copies and derived projections are permitted (README:119). "Grouping and encoding remain the tenant's choices" (README:72). The evidence-binding paragraph disclaims any prescribed protocol (README:90). RR3-15 is an ambiguity that applies to both tenants equally.
- **10, a_c dependency boundary: holds and is strengthened.** A_C:5–10 separates theory, interpretation, carrier and checker. "Separately selecting a mechanical check does not make semantic fidelity optional" (README:75), and checker selection stays separate (A_C:43). RR3-11 and RR3-12 are minor drift, not a reopening.
- **12, writing: holds, with minor findings.** No personal names were added to specification surfaces, and no new product naming by acronym or version appears in added prose. RR3-19 lists the minor drift.

## Pre-existing (unchanged text, not counted)

- PC:668 still opens "STDO 3 is the successor", naming the product by acronym and version. The line was touched in round 2 but this wording was not changed.
- PRODUCT:407 and PRODUCT:408 give two deadlines for the ported-part decision.
- T2C:70 "no uncalibrated hard context-size threshold", against PRODUCT:401.

## Limits

- **Tenant interest.** I am a Claude context, a tenant governed by this specification. Verdicts on PRODUCT:200, PRODUCT:202, PRODUCT:212–217, I3-00 and the reported peer-findings section judge wording that answers Claude's round-1 smallest corrections or concerns the Claude line. Under the new PRODUCT:399 these verdicts are interested, and they are marked so above.
- **Material not read.** I read the round-1 disposition post only to check whether the change reasons exist (RR3-05). I did not read either candidate.
- **Coverage of the claims inventory.** I checked only the changed header and rules lines of `PREDECESSOR_CLAIMS.md`, plus a grep of its packaging rows.
