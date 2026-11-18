# Assessment: STDO 3.1.0-rc.3 native candidate and its predecessor dispositions

**Verdict: `falsified`.** The native source changes match the owner's rulings and leave no stale consumer references. The disposition record falls short in four places (F1–F4), two of which (F2 and F3) are guards dropped from the source without any record. Nothing outside those findings changes this result.

## Subject and basis

| Item | Value |
|---|---|
| Native candidate | `specification_methodology/v3/build_tenants/common`, 95 members selected by `method/NATIVE_READY_INVENTORY.json` (inventory SHA-256 `e6d80a24…5e34`, from `freeze.stdout` and `PACKAGE_CHECK.json`) |
| Approved source candidate | `c11c7617…9c57` |
| Disposition record | `.ai-workspace/work/STDO_3_1_RC3_2026-11-18/PREDECESSOR_DISPOSITIONS.json`. It sits in the workspace and is not one of the 95 members. |
| Predecessor | RC2 native `21a9d4b9…`, read as `method/PREDECESSOR_ODD.md` |
| Construction basis | installed `stdo://releases/v3.0.4/` |
| Review law | RELEASE §9, EVALUATION §3–§5, ACTIVATION §5 and §7 |
| Severity scale | 1 highest to 5 lowest. The intake names no scale, so I used the one the earlier reviews in this run used. |

**Claims assessed:**
- **C1:** the bounded native changes put the owner's rulings into effect without unauthorised loss, broken consumer references, or false release or acquisition claims.
- **C2:** every predecessor claim that can affect the successor has an adequate disposition under RELEASE §9.

**Excluded:** future assets, the tag, index and package qualification, whole-method qualification, and human acceptance.

## Obligations I wrote down before opening the candidate

- **O1 (RELEASE §9):** each claim gets one disposition. The comparison covers the same case: what must happen, what may happen, what is prohibited, and what follows when a trigger is absent. It covers the owning text and its consumer bindings. A `conserved` claim keeps its modal force and its exceptions. A statement that a whole package is equivalent establishes nothing for any claim.
- **O2 (owner rulings in the intake and `SOURCE_CONTRACT.md`):**
  - Tracking, keeping needed step-produced facts, and reconciling to the authoritative mutable workspace stay required.
  - The register is optional, and equivalent mechanisms are allowed.
  - The ledger, every-input capture, the event log, the fixed evaluator API, universal replay and downstream runtime design may be removed.
- **O3:** consumers of removed constructs must be updated.
- **O4:** the method is self-contained.
- **O5:** Product defines the intended end state; Goals hold the current epics.
- **O6:** no regression in release acquisition and no false claims.

## What I read

**Predecessor:** all of `PREDECESSOR_ODD.md` §10–§11.5D, including the object and function tables, A0–A16 (with A1a, A1b, A4a, A13a), the constitutional equation, and §15–§20. I checked every `predecessor_start_line` in the record against this file, and all 21 match.

**Candidate:**
- ODD §1–§5, §9–§20 in full, including §11.5–§11.5D.
- SPEC_METHOD §1 (boundary), §2 (chain, goals and product paragraphs, Manifesto), §3, and the change-class table.
- `GOALS_TEMPLATE`, `PRODUCT_TEMPLATE`, `GENERIC_REGISTER.md`, GLOSSARY §14, and the ACTIVATION §5 consumer rows.
- The release note, `documentation/README.md`, and GETTING_STARTED (header, New Project bootstrap, documentation section).

**Searches across the whole package, frames included:**
- The removed vocabulary (`evaluate_next`, `EdgeFulfillmentLedger`, ABG, GTL, A0–A16, `replay-visible`, the old anchors): no hits.
- Ledger and replay mentions (each one classified).
- `liveness`, `recipe`, `before activation`, and external product names.

**Supporting material:** `SOURCE_CONTRACT.md` and the candidate-03 source review, read only after my own derivation.

## Native changes (C1): no defects outside F2 and F3

- **O2:** ODD §11.5D lines 715–752 make tracking and reconciliation required functions. The register is "one tool", equivalence is defined functionally, and P4b recording of facts that cannot be re-acquired is kept. §20 agrees.
- **O3:** no removed construct survives in any member or frame. ACTIVATION §5 Row 1 (line 1448) now cites ODD's conservation row. The remaining "ledger" hits belong to other owners: the WORLD_MODEL attribute ledger, the REFERENCE_FRAME coverage ledger, the EXECUTIVE_BASELINE closed-result ledger, the TICKETS item ledger, and the UX Msg-replay proof. These are separate, optional or profile-owned mechanisms that the owner's ruling does not touch.
- **O4:** ODD §1 (lines 50–68) and §10 Runtime (552–567) define the roles inside the method. The only external names are the repository and install coordinates in plugin metadata and the bootstrap, which is acceptable.
- **O5:** SPEC_METHOD lines 55–59, 215–219, 249–258 and 282–283, the `product_reprice` row (line 881), the templates, the GETTING_STARTED change-class row (line 647) and TICKETS are consistent.
- **Outcome termination** (the old §11.5D preamble) is kept by SPEC_METHOD §3 lines 690–707.
- **O6:** the release note, the documentation README and GETTING_STARTED all use RC3 coordinates and a six-asset population, and verify by the fixed tag's digest. I found no false claim.

## Findings

### F1 — severity 3: the blanket "Remaining … conserved" entry has no valid basis

**Where:** `PREDECESSOR_DISPOSITIONS.json`, the final entry.

**Why it fails:**
- RELEASE §9 says a statement that a whole package is equivalent establishes nothing for any claim.
- The approved-source review it relies on explicitly performed "no new assessment of ODD" and "no whole-method … assessment", and left these dispositions open.

**Counterexample:** predecessor §11.5 (line 689) says "Visible current state is a projection and does not replace runtime truth." Successor §11.5 (lines 652–656) makes the workspace the truth surface and says runtime records "do not form a second truth surface." That reverses the claim, so it is superseded, not conserved.

**Other changed clauses that have no disposition of their own:**
- §1 bullets
- §10 ABG ownership list
- §11.2A "lineage ledger declarations"
- §11.4 named boundary surfaces
- §11.5A prohibitions, such as multi-step controller memory and inferring later steps locally
- §11.5C rule that runtime views derive from events and replay
- §11.5D preamble: object and function tables, and "the word evaluator is not sufficient"
- §16 items 11–15
- §17 steps 10–13
- §19 questions 6 and 8–11
- §20

**Consequence:** these dispositions are unresolved, which blocks qualification of the affected claims (RELEASE §9, EVALUATION §5). In substance most of them look supportable by the owner's rulings plus the core owners. For example, ODD §11.5A, §11.7B and §16 cover hidden controllers, and SPEC_METHOD §3 covers termination. The repair is therefore to the record.

**Repair:** give each of the clauses above its own disposition. Limit any remaining `conserved` entry to owning text and consumer bindings that are byte-unchanged, and name the comparison evidence.

### F2 — severity 3 (medium confidence): the §11.5B disposition does not record two narrowings the owner did not authorise

**Where:** predecessor §11.5B lines 717–721 and 758, against successor ODD lines 683–688.

**What was dropped:**
1. **Timing.** The audit was required "before activation and closure". The successor states no timing, and no other member supplies one (searched).
2. **Triggers and consequence.** The triggers were closure, assurance, retry, worker transport and process supervision, and "Any of these conditions prevents closure" was explicit. The successor's triggers are "traversal control, delegation, admission or continuation" only. The closure consequence now exists only implicitly, through §11's "every clause holds" and §16.

The owner's rulings remove runtime design, the ledger, the event log and replay. They do not address when an authority audit must happen.

**Consequence:** a change to runtime control can be activated before its audit, and a change only to closure semantics may escape the audit altogether. The blast radius is every ODD consumer's authority-audit gate. This is contained in part because the conformance consequence in §11 and §16 still applies.

**Repair (the owner chooses):** either restore "before activation and closure" and the closure/assurance trigger in §11.5B, or record both narrowings as `intentionally_removed` with the owner's decision.

### F3 — severity 4: the A5 disposition omits a dropped prohibition

**Where:** predecessor lines 1099–1101: "An F_P worker must not be given an F_D-authored semantic extraction recipe when the edge requires F_P judgment."

**What happened:** no successor locus contains this. A search for "recipe" finds nothing, and the closest text, ODD §5 lines 267–271 and 332–334, does not prohibit it. The A5 entry lists what was kept and what was removed, but not this.

**Repair:** restore the sentence in ODD §5 or §11.5D, or record it as `intentionally_removed` with owner authority.

### F4 — severity 5: imprecise loci and identification in the record

- **A10 (`conserved`):** the success direction is kept by line 755. The failure direction ("cannot by itself declare semantic failure") rests on FOUNDATIONS §4 (line 740: `falsified` requires a declared counterexample) and on ACTIVATION §5's interruption rule. The entry cites only §11.5D.
- **Missing fields:** the last four entries have no predecessor hash, line or authority.
- **Product/Goals entry:** it does not list the predecessor clauses it supersedes: SPEC_METHOD §1 boundary, the §2 chain and surface paragraphs, the Manifesto, the `product_reprice` trigger, and the templates.

**Repair:** add the missing loci and identifiers.

## Adequacy of each predecessor disposition

| Claim | Recorded | My assessment |
|---|---|---|
| A0 | superseded | Adequate. Successor loci: ODD lines 672–675, 685–687 and 931–932, plus §16. |
| A1 | superseded | Adequate. Successor loci: lines 658–667. |
| A1a | superseded | Adequate. Lines 715–752; the owner ruled on the ledger and append-only correction. |
| A1b | intentionally_removed | Adequate. The owner ruled on ledger-only and every-input capture. Summaries still cannot overrule current evidence (ACTIVATION §5, ODD §11.7A). |
| A2 | conserved | Adequate. Line 733 plus ACTIVATION §1 Intake; "Evidence for one predicate cannot satisfy another" (line 765). The binding schema is a carrier, and removing it is consistent. |
| A3 | superseded | Adequate. Covered by §11.2, §11.7 and lines 733–735. |
| A4 | intentionally_removed | Adequate. The owner ruled on the fixed API. Re-pricing and termination are kept by SPEC_METHOD §3–§4. |
| A4a | superseded | Adequate. Covered by lines 695–696 and 557. |
| **A5** | superseded | **Inadequate (F3).** |
| A6, A7 | superseded / intentionally_removed | Adequate. Covered by lines 754–756 and 719–721. |
| A8 | intentionally_removed | Adequate. Covered by lines 761–768. |
| A9 | superseded | Adequate, resting on the core distinction between `indeterminate` and `falsified`. |
| A10 | conserved | Adequate in substance; the locus is incomplete (F4). |
| A11, A12 | superseded | Adequate. Covered by lines 677–679, 578–579 and 708–711. |
| A13, A13a | intentionally_removed / superseded | Adequate. The owner ruled on universal replay; Products may still require replay (lines 749–752). |
| A14, A15, A16 | superseded | Adequate. Covered by lines 773–776, §11.9, §10 Runtime and lines 664–666. |
| **11.5B five-row audit** | superseded | **Inadequate (F2).** |
| Product/Goals | superseded | Adequate in substance; identification is imprecise (F4). |
| Downstream dependency | superseded | Adequate. |
| **Remaining … conserved** | conserved | **No valid basis (F1).** |

## Results

| Claim | Result | Reason |
|---|---|---|
| C2, disposition adequacy | `falsified` | F1–F4 |
| C1, native changes | `satisfied` for the owner's rulings, consumer coherence, self-containment, Product/Goals, and the release note and Getting Started; `falsified` for the two unrecorded narrowings in F2 and F3 | Fixing F2 and F3 either way (restoring the text or recording the removal) clears C1. |
| Overall | `falsified` | |

Technical severity only. Priority and whether any finding blocks promotion belong to the owner, under EVALUATION §5.

## Independence and limits

- **Reviewer:** Claude (claude-opus-5-5), read-only. I wrote none of the construction and made no repairs.
- **Not independent of the direction:** the original architectural recommendations were also Claude-family, so this review is independent of the Codex construction but not of that direction. Earlier Claude reviews were read after my own derivation and used only for their exact claims.
- **Subject binding is not recomputed.** I had no hashing ability, so I read the working-tree files and relied on the freeze, package-check (`valid: true`) and frame-test (exit 0) receipts. I also relied on `PREDECESSOR_ODD.md` being the exact RC2 bytes, and did not verify the predecessor SHA-256 values.
- **No acquisition comparison with RC2.** The RC2 native GETTING_STARTED was outside the host's allowed paths, so that byte comparison was not performed. I assessed only the internal consistency of the RC3 acquisition text.
- **Release-note claims not checked.** The note says release evidence and indexes "bind" or "are refreshed". That depends on the later qualification, which is outside this review.
- **Not read in full:** frames, and members other than those named above.

## Invalidation and re-entry

This result is void if any of the following changes: an inventory member, the disposition record, the owner's rulings, or the selected basis.

The repairs go to the Writer: the disposition record for F1 and F4, and, by the owner's choice, either ODD §11.5B and §5 or the record for F2 and F3. This result returns to the Product-owned decision authority. The native tag, index and package qualification remain a separate step.