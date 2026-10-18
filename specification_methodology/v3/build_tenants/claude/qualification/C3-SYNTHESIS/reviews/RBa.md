# RBa: Working Review Of B1, B1b And B4

Same-family working check, not acceptance. Reviewer: a fresh Claude context (RBa) that wrote none of the subjects. Authors: Claude Writer activations B1, B1b and B4. Both are Claude contexts, so this is the same-family exception the [ledger](../LEDGER.md) declares (Defaults Taken, item 2); the result counts towards no acceptance.

## Basis

| Coordinate | Binding |
|---|---|
| Repository | `/Users/jim/src/apps/specification_methodology-claude`, paths below relative to `specification_methodology/v3/` |
| Subject commit | `224081c` (B1b), containing B1 `73a0a44` and B4 `2f2338b` |
| Previous | `f7851aa` |
| Subjects | `build_tenants/claude/standards/SPEC_METHOD.md`, `PRODUCT_DEFINITION.md`, `TICKETS.md`; `qualification/C3-SYNTHESIS/returns/B1.md`, `B1b.md`, `B4.md`; `deltas/B1.md`, `deltas/B4.md` |
| Common sources | `specification/PRODUCT.md` Build-Tenant Binding; `specification/requirements/README.md` Build-Tenant Binding, Standalone Successor, Single Ownership, Single Result Algebra; `specification/conformance/README.md` rows 23 to 26 (software, human or mixed realisation; faster plan; two environments; a_c model of a human process) |
| Tenant sources | EXPECTATIONS (E-3-1 to E-3-6, E-1-1 to E-1-7, E-4-1 to E-4-6, E-5-2 to E-5-6, E-7-21 to E-7-25, E-8-6, E-8-7, E-8-11, E-8-13, N-1, N-2, N-6); LEDGER rulings; FOUNDATIONS §3 and §4 Results, Conjunction of results; ACTIVATION §1 Configuration, §3, §4 at `224081c` |
| Predecessor | installed `v2.5.1-rc.2/standards/SPEC_METHOD.md`, `TICKET_METHOD.md`, read-only |

Line references `file:line` are to the subject commit. `SM` is `build_tenants/claude/standards/SPEC_METHOD.md`, `PD` is `PRODUCT_DEFINITION.md`, `TK` is `TICKETS.md`, `FD` is `FOUNDATIONS.md`, `AC` is `ACTIVATION.md`.

## Expectations

Written from the sources above before any subject was opened.

Q1. Build-tenant binding (R Build-Tenant Binding 1 to 6; E-3-1 to E-3-6; E-7-22 to E-7-25).

- X1. SM states, for any product the method governs, that a build tenant binds the common requirements calculus to a declared computational calculus and binds that calculus to a concrete execution environment, and that these bindings sit in the tenant's existing design and realisation surfaces; no new carrier (R 1; E-3-2).
- X2. The environment may be a stack, a human process or a combination, selected within the common requirements including any required human decision. Author identity, actor identity and operation kind stay distinct; a person performing an operation does not make it human adjudication (R 2; E-3-3).
- X3. The binding names the material operations, composition laws, effects, resource measures and operational assumptions; human effort, elapsed time, communication and machine resources are measured where obligations need them, with units and boundaries (R 3; E-3-4).
- X4. Conformance evidence shows how the bound realisation meets meaning and constraints, including authority, independence, failure and recovery. Convenience never weakens an obligation; merging two required independent assessments or automating a required human decision fails conformance whatever the speed, cost or matching output. A categorical preservation claim meets the demonstration standard (R 4; E-3-5; E-7-23).
- X5. One calculus may serve several tenants and environments wherever the bindings meet its laws; a different language, tool or team does not by itself require a different calculus; the kind of executor neither accepts nor rejects a realisation (R 5; E-3-6; E-7-22; E-7-24).
- X6. a_c representation selects no executor, and structural validation alone establishes no execution conformance (R 6; E-3-6; E-7-25).
- X7. "Applies": SM uses the relation where it governs realisation (design, assurance, acceptance), not only defines it (E-3-2, ambiguity A1 reading (a)). Whether this candidate declares its own calculus and binding (A1 (b)) is recorded, not failed.
- X8. One owner: SM owns the relation; FOUNDATIONS, PD, profiles, guides, packaging and design refer to it (E-3-1; E-4-1).
- X9. The binding states its purpose and material relation (E-8-11; E-7-21) and adds no carrier.
- X10. Old §11 (this source project's development law) leaves method law only if each of its determinations is carried by the owner the subject names (common Product Development Isolation, tenant design), and no live link still targets the removed anchor.

Q2. Results (R Single Result Algebra 1 to 5; E-5-2 to E-5-6; N-2).

- Every value set an actor returns in SM, PD or TK (triage outcomes, consistency gate, ambiguity outcomes, lifecycle sufficiency, disposition, admission of execution contracts, closure classifications, sprint close review, evaluation criteria and non-closure conditions) is stated in the core or as a refinement that names its owner, question and predicate and maps each value to exactly one core value.
- No mapping raises standing; not-performed is no result and never `indeterminate`; an unknown effect never maps to none or completed.
- Availability, assessment and acceptance stay separate; a successful step is never acceptance.
- A refinement already owned elsewhere (ACTIVATION §3 disposition and ambiguity outcome, EVALUATION §4, RELEASE §9) is referred to, not mapped a second time.
- A declared state (ticket status, lifecycle marker, change class, category) is called a state or fact, not a result, and the claim holds: the value records a fact rather than answering a predicate an evaluation decides.

Q3. Family tables F10 to F13 (FD §3 Foundation to law; E-1-1 to E-1-3; N-6).

- Each table sits where FD's index says: F10 at SM §2, F11 at SM §4, F12 at PD §1, F13 at TK §5.
- Each states instance premises labelled as such, then rows in the four columns.
- Each premise carries FD §3's standing: P0 recovered; P1, P2, P3, P4a, P6 independent; P4b derived from P0 and P2 with P0's premise that step-produced facts are not re-acquirable; P5 derived from P0 and P6 with P0's open-world premise. A lead or row that shortens or changes this is a defect.
- Each consequence column names a linked rule; each choice column names an owner or "none"; the table owns no determination and refers to Foundation to law for the standing of consequences.
- Each table accounts for every deciding rule of the sections the index assigns: F10 SM §1 to §3, §6, §9 to §11; F11 SM §4, §5, §7; F12 all of PD and FD §2 Imports except its result grounds; F13 all of TK. SM §8 belongs to F2 and F5.

Q4. Ownership and use (R Standalone 2; R Single Ownership; E-1-4; E-4-1 to E-4-6).

- SM and TK apply FD's frame, result, authority and evidence contracts at the step where an actor uses them, not only in a preamble.
- PD §5 reads its relation kinds in FD §2 Imports terms, names FD as owner, and redefines none of: reference-only, owner-qualified identity, direction, no loss, no authority.
- No second owner of the hard stops (AC §4), the results and conjunction (FD §4; AC §3), configuration (AC §1) or the binding (SM §11); no precedence rule between loci.

Q5. Conservation (R Standalone 3; criterion 2; E-1-5; E-1-7; E-8-7).

- For each changed determination, the predecessor's meaning is in the subject's own text, with no loss of a condition, list member or modal force; a link to `stdo://` alone does not carry it.

Q6. Links and writing.

- Every relative link and anchor resolves at the subject commit. No undefined term, floral wording, history narration in live text, person's name, or change of modal force.

## Results

Convention, as in the ledger's earlier working checks: a question with any finding is `falsified`; severity says whether it blocks. Nothing here is blocking.

| Q | Result | Findings |
|---|---|---|
| 1 Build-tenant binding | `satisfied` | none |
| 2 Results | `falsified` | 2 material (M1, M2), 1 minor |
| 3 Family tables F10 to F13 | `falsified` | 4 minor |
| 4 Ownership and use | `falsified` | 6 minor |
| 5 Conservation | `falsified` | 2 minor |
| 6 Links and writing | `falsified` | 1 minor (links: none broken) |

### Q1. SPEC_METHOD §11 as method law

Result: `satisfied`.

Evidence:

- Scope. §11 applies "to every product built with this method" (SM:1596–1597). It names no tenant of this source project.
- Item 1. Rule 1 (SM:1633–1644) states both bindings, places them in the tenant's existing design and realisation surfaces, and states that "the method requires no further carrier".
- Item 2. Rule 2 (SM:1645–1659) covers a stack, a human process or a mix, chosen within the requirements calculus, and says no choice removes a required human decision or a required independent assessment. Author, actor and operation kind are defined at SM:1621–1629 and kept distinct at SM:1650–1654. A person performing an operation does not thereby adjudicate (SM:1654–1657).
- Item 3. Rule 3 (SM:1660–1683) covers operations, effects and outcome values, each value mapped to one core value; composition laws and transformations; resource measures; and operational assumptions. Each measure states its unit and its boundary, and a resource claim without them supports no conformance claim.
- Item 4. Rule 4 (SM:1684–1706):
  - the obligations decide fitness, and the kind of executor alone neither accepts nor rejects (E-7-22);
  - the evidence covers authority, independence, failure and recovery;
  - conformance is the FD conjunction, with the obligations as required coverage;
  - merging two required independent assessments, or automating a required human decision, is `falsified` for the obligation it weakens, and matching outputs, lower cost or a faster run discharge nothing (E-7-23);
  - a categorical claim meets the FD §4 Formal fragment, which routes preservation and licensing to AC §4 Refinement (FD:618–624). This is the whole demonstration standard (N-1).
- Item 5. Rule 5 (SM:1707–1712). A new language, tool, team or person changes the execution binding, not the calculus (E-7-24).
- Item 6. Rule 6 (SM:1713–1721). An a_c model of a human process neither selects an automated executor nor shows conformance (E-7-25).
- Applied, A1 reading (a). The relation is applied at four points (SM:1723–1732):
  - the Design rule (SM:420–421);
  - §5 narrowing (SM:1051–1053) and its human-adjudication sentences (SM:1081–1087);
  - §4 triage of a binding change, where a weaker obligation is a WHAT change;
  - §8 (SM:1486–1490).
- A1 reading (b) is present. The tenant declares its own calculus, binding and evidence in `design/CONSTRUCTION_BINDING.md` §2 to §5.
- One owner (E-3-1). PD §8 (PD:643–654), FD index F10, AC §6 (AC:1189–1190) and DESIGN_MODULE:158 refer to §11 and do not restate it. The GLOSSARY `Build Tenant` row still routes to PD §8 (GLOSSARY:181). That row is outside this subject and assigned to B10.
- Purpose and material relation are stated (SM:1743–1750). No carrier is added (E-7-21, E-8-11).
- Old §11. Each of the ten determinations in deltas/B1.md:74–83 was checked against its stated locus.
  - Nine are owned by the common PRODUCT Development Isolation (PRODUCT.md:183–247):
    - Tenant branches: the branches, the worktrees and the sparse cones;
    - Snapshot: the binding to an input commit;
    - Review: reviews at named commits;
    - Merge: merge on acceptance;
    - Territory: commits only in the tenant's own territory; a common change is requested and merged inward; no edits to tickets or common files; no edits to the peer.
  - The tenant design binds those nine (CONSTRUCTION_BINDING:99, :117–121, :254–274).
  - The tenth, "local development law, not method law", is carried in generic form at SM:1734–1741.
  - No live standards or design file links the removed anchor; only historical `a_c/` sets and `runs/` inputs do. Nothing is lost.

### Q2. Result references

Result: `falsified`.

Mapped or referred correctly:

- TK §3 close classifications and debt outcomes map once each, for a named predicate (TK:284–318). No non-compliant value maps to `satisfied`. The `closed` state requires an outcome for every item, not a `satisfied` one (TK:313–315). The change-class layer is a declared fact carried as the domain outcome (TK:303–307).
- SM §5 names the four ambiguity outcomes and refers to AC §3 for their values, without mapping them again (SM:1066–1072).
- SM §8 keeps availability, assessment and disposition separate through AC §3 (SM:1480–1486; E-5-6).
- SM §4 triage results join under FD conjunction, and a frame that was not applied leaves its diagnosis open (SM:744–748). The gate is the conjunction (SM:890–897). An unknown effect is `completion_unknown` (SM:862–866).
- The SM §4 walk values are facts, not results (SM:832–841). The SM §2 lifecycle markers are declared states, not results (SM:588–595). Both state their purpose.
- PD §5: an evaluation that depends on unresolved or ambiguous meaning takes the `out_of_frame` ground of FD Results (PD:447–452). Its fixed value narrows the owner; see m4-6.
- No mapping raises standing. Nothing not performed becomes `indeterminate` (N-2).

Findings:

M1 and M2 are in text that B1, B1b and B4 carried forward without change. Each is a gap in the result coverage of the subject members, not a defect these activations introduced.

- **M1 (material; text not changed by these activations).** TK:1078–1085: the repricing dispositions of an obligation (`retained`, `superseded`, `deferred`, `withdrawn`) are authority decisions with no core mapping and no declared-state statement.
  - B4's return reads them as carrier facts (returns/B4.md:31), but no text says so. F13 lists them as a choice (TK:559).
  - A parallel decision, the successor disposition, is evaluated in the core (RELEASE §9, ledger B7). An unmapped outcome set was rated material in RA1 and RA23.
  - Repair: one paragraph at TK:1085. Either map the four values for a named predicate, or declare them states of the obligation that map to no core value, mirroring SM:588–595, with their purpose.
- **M2 (material; text not changed by these activations).** PD §4 operation outcomes have no core mapping and no reference to AC §3 Effects:
  - drift refuses mutation (PD:293–294);
  - the fail-closed list (PD:302–306);
  - "reports completion only after verifying", refusal before consumer effects, and a caught failure that "does not report completion" (PD:383–387);
  - host loss that "requires recovery" (PD:388–391).

  The owner of the obligation is FD §4 Results: "This core is the only one. Results of constraints, judgments, frame evaluations, stops, work steps and effects are stated in it or in a refinement mapped into it" (FD:657–660), with R Single Result Algebra item 1. SM §11 rule 3 (SM:1662–1666) supports it for any operation of a binding. RA1 and RA23 rated an unmapped outcome set as material. Repair: one paragraph after PD:391:
  - completion reported maps to `completed`;
  - a refusal before effects maps to `not_effected`, with its refusal mapped by cause (`invalid_basis` for drift, mismatch or an unverifiable state; `out_of_frame` for missing authorisation);
  - host loss or unavailable rollback maps to `completion_unknown`.
- **m2-1 (minor).** Declared-state coverage is partial. Two value sets are declared non-results; the following carry no such statement:
  - SM: requirement `Status` and `Category` (SM:479–487), the legacy classes (SM:489–497), the four evidence kinds (SM:606–609), the old-path classes (SM:1289–1290), `carry_across`, `redundant` and `rewrite` (SM:1419–1422), and ADR `Status:` (SM:1553);
  - TK: sprint status (TK:211–218), ticket status (TK:507–509), lanes (TK:513–523), and the `migration_strategy` and `library_usage` values (TK:740–742).

  B1b's return leaves "status axis not covered" (returns/B1b.md:7). Repair: one sentence at SM §2 Requirement categories, and one at TK §4 Status covering TK §3 and §6, mirroring SM:588–595.

### Q3. Family tables F10 to F13

Result: `falsified`.

Satisfied parts:

- The tables sit where FD's index puts them: F10 at SM:147, F11 at SM:684, F12 at PD:90 and F13 at TK:534.
- Instance premises are labelled. All rows use the four columns, and every consequence names a linked rule.
- Each table refers to FD §3 for the standing of its consequences (SM:178–179, :713–714; PD:123–124; TK:564–565).
- F12 and F13 copy each standing in full on every row.
- The F10 lead copies FD §3 exactly (SM:158–161).
- F12 accounts for PD §1 to §12 and FD §2 Imports through its sixth row (PD:104–108, :117).
- F13 accounts for TK §1 to §9, section by section (TK:552–562).

Findings:

- **m3-1 (minor).** The F11 lead (SM:696–698) reads "P4b derived from P0, P2 and the step-produced-facts premise; P5 derived from P0, the open-world premise and P6". It makes each premise a separate co-source instead of P0's premise, and it leaves "the step-produced-facts premise" undefined; FD's wording is "that step-produced facts are not re-acquirable". B1b's return calls this "outside" (returns/B1b.md:11), but the text is in SPEC_METHOD, B1b's territory. Repair: copy SM:158–161.
- **m3-2 (minor).** SM:181–184 says SM §8's binding of the step "is accounted for by family F2 at ACTIVATION §1". The F2 lead (AC:48–49) covers only "this section and §4", and no F2 row names SM §8. B1 added three statements to SM §8: results through AC §3, calculus and limits from §11, and the coordinator (SM:1480–1490, :1511–1523). No table traces them. Repair: either a sentence after F2 naming SM §8 (outside this subject), or an F10 row for SM §8's binding sentences with the closing claim corrected.
- **m3-3 (minor).** F10 leaves deciding text in its own sections untraced:
  - §11 "Application in this method" (SM:1723–1732), including "a change that needs a weaker obligation is a change to the WHAT ... never a tenant's choice";
  - in §3, the rule that a regression blocks promotion only on the affected path (SM:671–676);
  - in §3, the added choice that "consumers own deletion, archival, quarantine and salvage mechanics" (SM:666).

  Repair: add "Application in this method" to the rule column of F10 row 11 (SM:175). Add the regression consequence and "deletion, archival, quarantine and salvage mechanics: consumers" to row 6 (SM:170).
- **m3-4 (minor).** The premise column of F10 row 12 (SM:176) is "P6, P4a, P0". The rules it traces cite P0, P2, P5 (rule 3, SM:1683), P1, P4a (rule 5, SM:1712) and P6, P0 (SM:1741). Its consequence, outcome values mapped into the core, rests on P5. Repair: premises "P0 recovered; P1, P2, P4a, P6 independent; P5 derived".

### Q4. Ownership and use

Result: `falsified`.

Satisfied parts:

- Hard stops have one owner, AC §4 (AC:814–826). SM §5 refers to it (SM:1097–1098), F11's choice column names the owner (SM:708), and the deltas record the ruling.
- Results and conjunction are owned by FD §4. SM, TK and PD apply them at each point of use (SM:744, :893, :1068; TK:287–290, :1096–1100; PD:447–452). E-1-4 holds.
- Configuration is owned by AC §1, and SM §8 adds no role inventory (SM:1511–1515).
- The binding is owned by SM §11 (see Q1).
- PD §5 names FD §2 as the owner of import. It applies FD §2's unchanged meaning, direction, loss and lack of authority, and reads translation, equivalence and disambiguation as not imports, in FD's terms (PD:477–503). It reconciles FD's owner-as-place with semantic authority (PD:485–486). Nothing is redefined. FD:963 now names FD §2 as the owner.
- No precedence rule stands in for an owner (E-4-6).

Findings:

- **m4-1 (minor).** SM:1081–1087 governs a person who decides a declared ambiguity, where policy permits, without admission: that person "acts under the policy and recording that govern lawful probabilistic processing". The owner's ground for `resolved` (AC:761) is "a decision ... by lawful probabilistic processing or by human adjudication". The SM text defines lawful probabilistic processing as non-human (SM:1078), so such a decision fits no outcome ground. Repair at the owner: change the AC:761 ground to "under the policy that permits lawful probabilistic processing, or by human adjudication". Alternatively, SM:1087 can state that the decision takes the outcome a lawful probabilistic decision takes under AC §3.
- **m4-2 (minor).** SM:1516–1519 restates the coordinator rule of AC §1 Coordination across tasks (AC:331) in other words, omitting "sufficient bounded view" and "missing information never assumed favourable", and does not name that paragraph. Repair: cite "ACTIVATION §1 Configuration, Coordination across tasks" for the sentence, or reduce it to that reference.
- **m4-3 (minor).** The canonical statement routes the hard-stop exception to "(§5)" (SM:126–127). The owner is AC §4. Repair: "(§5; ACTIVATION §4)".
- **m4-4 (minor).** "This method prescribes none of these mechanics" (SM:1739–1741), with "review points" in the list, sits beside the multi-build-tenant review rule (TK §6, TK:826) and cites only TK §4. Repair: cite "TICKETS §4 and §6 Multi-build-tenant review" for what the method does prescribe.
- **m4-5 (minor; text not changed by these activations).** PD:17–18 names "SPEC_METHOD §2 and §6" for the recursive product taxonomy. The owner is FD §2 Product lineage objects (SM:1113–1117). Repair: name FD §2.
- **m4-6 (minor).** PD:447–452 says the evaluation "returns `out_of_frame`". The owner leaves more open: where a claim depends on an undeclared relation and the admissible evidence also cannot decide it, "`out_of_frame` and `indeterminate` each have a lawful ground; the result names the value it returns and that ground, and this boundary excludes neither" (FD:760–764). Fixing one value narrows the owner. Repair: "returns `out_of_frame`, or `indeterminate` where FOUNDATIONS §4 Results gives that ground too, and names the ground".

### Q5. Conservation

Result: `falsified`.

Twenty-six changed or adjacent determinations were compared with the installed predecessor, weighted to SM §4, §5 and §8 and TK §3. rc.2 lines are in `SPEC_METHOD.md` (S) or `TICKET_METHOD.md` (T).

| # | Determination | rc.2 | Subject | Verdict |
|---|---|---|---|---|
| 1 | triage determines six things | S:1203–1212 | SM:724–730 | conserved |
| 2 | no intake bypasses triage | S:1214–1215 | SM:730–731 | conserved; "may bypass" becomes the prohibition "No ... bypasses" |
| 3 | exposing frame need not contain cause; renamed analysis adds no evidence | S:1221–1227 | SM:735–742 | conserved |
| 4 | smallest sufficient frame configuration; localisation where required | S:1229–1232 | SM:742–750 | conserved |
| 5 | diagnosis grants no repair | S:1233–1235 | SM:751–753 | conserved |
| 6 | re-entry below Goals only by explicit assertion | S:1246–1247 | SM:769–771 | conserved |
| 7 | unknown effect state not treated as no effect | S:1315–1316 | SM:860–866 | conserved. `completion_unknown` names the intended effect; AC §5 reconciles uncertainty over external effects generally, and the observed effect state is kept (SM:861) |
| 8 | no gate closes while inconsistent; three proofs | S:1330–1338 | SM:881–888 | conserved |
| 9 | closure needs every obligation, judgment and ruling | S:1340–1344 | SM:890–897 | conserved. The B1b list "material counterexample to a mandatory constraint" (SM:894) is illustrative; SM:890 still requires every declared obligation satisfied, so nothing is weakened |
| 10 | event, aggregate or status cannot substitute | S:1344–1345 | SM:899–901 | conserved |
| 11 | code and test mismatch: evidence, not authority | S:1346–1350 | SM:903–908 | conserved; "graph" dropped (SM:1765) |
| 12 | bounded context; shorthands stay in their profile | S:1054–1058 | SM:1041–1045 | conserved, generalised; ODD keeps F_D, F_P, F_H (ODD.md:19) |
| 13 | narrowing order, including stack choice | S:1062–1072 | SM:1047–1054 | conserved |
| 14 | major and micro; major always surfaced; four records | S:1074–1090 | SM:1056–1066 | conserved |
| 15 | detection mandatory, blocking policy | S:1092 | SM:1072–1073 | conserved |
| 16 | the two concept definitions with URNs | S:1094–1100 | SM:1075–1081 | conserved |
| 17 | default model; threshold by risk appetite | S:1102–1113 | SM:1087–1095 | conserved |
| 18 | five hard-stop classes | S:1116–1123 | AC:814–826 via SM:1097 | conserved at owner |
| 19 | UP-020 normative relation and non-prescription | S:1505–1522 | SM:1472–1479; AC:36–46 | conserved |
| 20 | tenant split whatever the layout; derivative until ratified | S:985–990 | SM:1633–1637; SM:70–73 | conserved |
| 21 | registry entry records tenant identity and locations | S:2968 | SM:1579–1580 | conserved |
| 22 | build tenant and build tenancy | S:796–802 | SM:1601–1604; PD:656–659 | conserved |
| 23 | Agent Frame Activation does not mutate overlay | S:758 | PD:603 | conserved |
| 24 | Semantic Equivalence | S:662–664 | PD:493 | weakened modal (m5-1) |
| 25 | sprint record, fields, status, admission, escrow, close review, six classes | T:182–338 | TK:181–282 | conserved; "graph functions or AssetSurface" generalised (TK:1361–1362) |
| 26 | condition-based closure | T:871–889 | TK:1089–1116 | conserved; "Executive appointment" becomes "coordinating appointment" |

Findings:

- **m5-1 (minor).** rc.2 reads "Semantic Equivalence **requires** the governing authorities to establish the claimed equality". PD:493 reads "The governing authorities establish the claimed equality", which drops the necessity. Repair: "requires the governing authorities to establish the claimed equality".
- **m5-2 (minor; over-claim, nothing lost).** SM:1750–1755, the §12 row at SM:1800, the new-law note at SM:1871–1872 and deltas/B1.md:12 (row 431) each say that three determinations are conserved from rc.2 `#constitutional-chain`. Only two are in rc.2 (S:985–990). "Conformance ... judged under EVALUATION §6 without identical behaviour outside the contract" appears nowhere in rc.2 SPEC_METHOD or TICKET_METHOD. It is the equivalence ladder of EVALUATION §6 (EVALUATION:259), which that member records as "New law in this member, with no rc.2 clause" (EVALUATION:535). Repair: in those four places, say two determinations are conserved, and state that rule 4 applies EVALUATION §6's new law by reference.

Satisfied parts:

- E-8-6: every delta row carries one disposition, and each conserved locus resolves.
- E-1-5 and E-1-7: no changed determination is carried only by an `stdo://` link.

### Q6. Links and writing

Result: `falsified`.

Links: a script resolved every relative link and anchor at `224081c` in the eight subject files, with no break. The script was checked against a known-absent anchor, `ACTIVATION.md#3-result-algebra`.

Writing: no person's name, no floral wording. The new terms are defined at their first use: requirements calculus, computational calculus, execution environment, calculus binding, execution binding, author identity, actor identity and operation kind (SM:1599–1629). The modal change is m5-1. The undefined term in the F11 lead is m3-1.

Findings:

- **m6-1 (minor).** SM:1751: "stated before in §2" narrates the candidate's own edit history in live text. Repair: delete the phrase; m5-2's repair rewrites the sentence anyway.

## Disclosures

- The subject files were extracted to scratch at `224081c` before the expectations were written, but they were not read until afterwards.
- The F2 table and the AC §1 coordination text are outside the subject. They were read only to test the claims SM makes about them.
