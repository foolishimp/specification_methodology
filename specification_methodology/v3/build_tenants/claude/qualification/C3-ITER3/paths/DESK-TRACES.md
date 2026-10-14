# Desk Traces Of The Declared Sample, Iteration 3

Same-family working evidence (a Claude tracer that authored none of the iteration 3 member text; CONSTRUCTION_BINDING section 1 exception). It is not the independent integrated assessment, and it is not actual use by fresh actors.

## 1. What was done and what was not

- Declared sample, fixed before any trace (systematic, every sixth path): DP-01, DP-07, DP-13, DP-19, DP-25, DP-31, DP-37, DP-43. The paths, dimensions and outcome rule are those of `design/REDUCTION.md` section 4 at S2 (`416bdb5`), read at lines 1382-1550 and the DP rows of the table at lines 1465-1527 and 1639-1644. DP-41 to DP-46 are defined in section 4.7, not in the section 4.4 table.
- Traced in full on S0, S1 and S2 (route entry): **DP-43 only.**
- **Not traced: DP-01, DP-07, DP-13, DP-19, DP-25, DP-31, DP-37.** Reason: this activation's acquisition budget (about 450 KB) was spent before Part 3 began, by Part 1 (three members in full, 281 KB) and Part 2. A verdict against S0 and S1 needs all three subjects traced, and one unfinished subject gives no outcome. I did not trace these seven in part. No result is given for them.
- **The other 38 of the 46 deciding paths were not traced** (DP-02 to DP-06, DP-08 to DP-12, and every path not in the sample, as well as the seven above). Nothing here says anything about them. One path out of 46 supports no whole-candidate reduction claim.
- Frame entry was not traced for DP-43 (the path names no frame; its frame-entry column is "README route").
- Acquisition: this part added about 35 KB to a total of about 510 KB for the activation, against a stated budget of about 450 KB; see `reviews/FINAL.md` section 1.
- Time: start `Wed 14 Oct 2026 18:45:58 UTC` for the whole activation; end is recorded in `reviews/FINAL.md` section 6.
- Acquisition limits of this part. I did not read the S1 or S2 `standards/README.md` in full: I read the route rows that name the task (by line), and take supplied bytes from `wc -c`. M4b is computed from the byte size of each section a tracer would acquire (the named member or section), not from what I read. I opened the S0 owner section only after the route trace, to judge the guard G; it is marked below. I used `design/REDUCTION.md` R32 (the inventory, not a route) to know what the path's guard items are.

## 2. DP-43

- Task kind: review. Situation (REDUCTION.md:1641): "a requirements surface narrates a transition and labels current law with a version line". Task for all three subjects: decide whether such a surface conforms and what repair the method requires. Same facts, same grant.
- Guard items (REDUCTION.md:1641): the owner's modal force kept; only the owner's label uses admitted; one owner for the rule. Deciding locus on S1 and S2: SPEC_METHOD section 2, Specification surface rule (R32 owner). On S0: the predecessor's SPEC_METHOD "Specification Surface Rule" section (SPEC_METHOD.md:2690-2717, 2,540 bytes).
- Measures. M1 deciding loci applied; M2 sections met, besides the owner, that decide the same question in their own words (a rival decider); M3 reconciliations the actor must make; M4a supplied bytes (the entry); M4b cumulative acquired bytes (section sizes, repeats counted); M4c not computed; M5 hops beyond the entry; G per guard item.

### 2.1 S0, installed `v2.5.1-rc.2`

- Entry: `standards/README.md`, 2,330 bytes (M4a). It names `SPEC_METHOD.md` and `WRITING_GUIDE.md` as members in a list of kinds. It has no task routing and names no section.
- Acquired: `WRITING_GUIDE.md` (whole member, 3,092 bytes; the member has no routed sub-section). M5 = 1; M4b = 3,092.
- Determinations applied: `WRITING_GUIDE.md:89` ("state the current live truth, not a narrated transition"), `:112` ("Active specification should describe the current constitutional surface in present tense"), `:131-132` ("Use explicit version labels only for immutable release facts, explicit mutable selector bindings, or clearly historical material").
- Rivals met: none. The owner is not met. `WRITING_GUIDE.md:83` names `SPEC_METHOD.md` as "the constitutional authority" for specification-layer roles and closure, with no section; the README names the member only. The deciding owner section (2,540 bytes inside a 157,952-byte member) is **unreachable by route** at section level. That is an adverse result for S0.
- M1 = 2 (WRITING_GUIDE Specification Artifact Practice; Current-Surface Writing). M2 = 0 (owner unreached). M3 = 0 on the text met.
- What the route yields is the guide's advisory "should" and a label list that omits "superseded" material. The owner (read after the trace, outside the route, to judge G) says "shall be written in present tense", "shall not remain", "shall be deleted, superseded, or moved to commentary", "Do not use version-line branding ... merely to indicate recency", and reserves labels for release facts, selector bindings, or "clearly historical or superseded material". The route actor does not reach the mandatory force or the full list.
- G on S0: not a candidate claim; recorded for the comparison: the owner's modal force is not reached by route; the admitted-label list is reached in its short form (superseded omitted); the rule has two deciders in the predecessor (WRITING_GUIDE and the owner) that the route does not reconcile.

### 2.2 S1, `5ab44d5`

- Entry: `standards/README.md`, 27,011 bytes. Route row, README line 40: "write or revise a specification artifact | WRITING_GUIDE, then SPEC_METHOD section 2 for the layer a sentence belongs to".
- Acquired: `WRITING_GUIDE.md` (5,906 bytes); `SPEC_METHOD.md#2-the-chain` (SPEC_METHOD.md:145-616, 35,002 bytes; the Specification surface rule subsection is lines 377-415, 2,498 bytes). M5 = 2. M4b = 40,908 with section 2 whole; 8,404 if only the subsection is acquired.
- Determinations applied: `SPEC_METHOD.md:399-407` (present tense; no dead law; labels reserved for release facts, selector bindings, historical or superseded material); `WRITING_GUIDE.md:94` area (state live truth, not a narrated transition; remove stale law).
- Rivals met (M2 = 2): `WRITING_GUIDE.md:114-126` restates the rule ("should describe ... in present tense", labels "only for an immutable release fact, an explicit mutable selector binding or clearly historical material", and says SPEC_METHOD section 6 "states the same boundary"); `SPEC_METHOD.md:168` (F10 consequence in the same section 2: "a version label names an immutable release fact, not recency", one use where the owner allows three).
- Reconciliations (M3 = 3, plus one pointer error): force ("should" against "is written"); label list (guide omits superseded material); label uses (F10 row names one of three). The guide's pointer to section 6 as the owner of the boundary is wrong (the owner is section 2).
- M1 = 2. G on S1: owner force and the owner's label list are present at the owner; "one owner for the rule" fails (two deciders and an F10 single-use statement coexist).

### 2.3 S2, `416bdb5`

- Entry: `standards/README.md`, 28,087 bytes; the same route row (README line 40).
- Acquired: `WRITING_GUIDE.md` (5,870 bytes); `SPEC_METHOD.md#2-the-chain` (SPEC_METHOD.md:147-636, 38,554 bytes; the Specification surface rule is lines 376-415, 2,498 bytes). M5 = 2. M4b = 44,424 with section 2 whole; 8,368 for the subsection.
- Determinations applied: `SPEC_METHOD.md:398-406`; `WRITING_GUIDE.md:86-94` (state live truth, not a narrated transition; "remove stale law, as section 9 states") and `:114-122` (refers to the owner "with its force" and adds only the writing practice).
- Rivals met: none that decide. `WRITING_GUIDE.md:114-122` refers to the owner. `SPEC_METHOD.md:170` (F10 consequence) now lists the owner's three label uses ("an immutable release fact, a selector binding, or clearly historical or superseded material, never recency") and sits in a family table that FOUNDATIONS.md:572-574 defines as a trace that states no determination. M2 = 0. M3 = 0. M1 = 2 (owner; the guide's own practice, which R32 retains as the guide's subject).
- G on S2:
  - only the owner's label uses admitted: pass (WRITING_GUIDE:114-122 and SPEC_METHOD:170 carry the owner's three uses).
  - one owner for the rule: pass on the route (WRITING_GUIDE refers; the F10 row is a trace).
  - the owner's modal force kept: **contested, not passed.** The owner text at S1 and S2 reads "is written in the present tense", "does not remain", "is deleted, superseded or moved to commentary", "is not used merely to indicate recency". The predecessor reads "shall be written", "shall not remain", "shall be deleted, superseded, or moved", "Do not use". The candidate applies a declared convention that the predecessor's "must" is written in the indicative (IDENTITY.md:407 states it for that member). The S2 SPEC_METHOD does not mark this row as a proposed replacement, and no ticket decision is cited in what I read. The change is identical at S1 and S2.

### 2.4 Measures

| Measure | S0 | S1 | S2 |
|---|---|---|---|
| Entry, M4a (bytes) | 2,330 | 27,011 | 28,087 |
| M1 deciding loci | 2 | 2 | 2 |
| M2 rival deciders | 0 (owner unreachable by route) | 2 | 0 |
| M3 reconciliations | 0 (on text met) | 3 (+ 1 pointer error) | 0 |
| M4b, section 2 whole (bytes) | 3,092 | 40,908 | 44,424 |
| M4b, owner subsection only (bytes) | 3,092 | 8,404 | 8,368 |
| M5 hops | 1 | 2 | 2 |
| G: one owner | not reached | fail | pass |
| G: label uses | short form | pass at owner | pass |
| G: owner's modal force | not reached | contested | contested |

M4c and M4 as a whole are partly estimated: M4b is from section sizes, not from my reading; M4c was not computed.

### 2.5 Outcome rule

- Against S0 (route entry): **not established.** On the route S0 meets one decider and never reaches the owner, so M2 and M3 are 0 and cannot decrease; M4a, M4b and M5 increase (README +25,757 bytes, M4b +41,332 or +5,276, M5 +1). The M5 increase is the declared tradeoff TO2 (REDUCTION.md:1648-1651 lists DP-43 M5 against S0 as expected adverse). S0's route also fails to reach its own owner section ("unreachable by route"). Elimination witness: S2 removes the predecessor's rival decider (WRITING_GUIDE:112 and :131 against the owner), the force mismatch and the label-list mismatch, so a witness is present in the structure, but it needs G to pass and the modal-force item is contested. I therefore do not claim a supported witness.
- Against S1 (route entry): M2 falls 2 to 0 and M3 falls 3 to 0; nothing in M2 or M3 increases; M5 is unchanged; M4b rises 3,516 bytes with section 2 whole (the section grew), and is unchanged for the subsection, and the rise is not tied to this path's rule. G's modal-force item is contested but identical at S1 and S2. Result: **simpler to determine and apply against S1, on condition that the modal-force item is accepted as conserved**; if the item is judged a change of force, the verdict is "not established". I do not treat the contested item as a pass.
- This is one path. It does not establish a reduction for the candidate.

## 3. Findings from the trace

- The owner text of the Specification surface rule changed from "shall" and "Do not use" to the indicative at S1 and kept so at S2. Whether this is conserved force or a change of force is not settled by the text I read. See FINAL.md, FR-08.
