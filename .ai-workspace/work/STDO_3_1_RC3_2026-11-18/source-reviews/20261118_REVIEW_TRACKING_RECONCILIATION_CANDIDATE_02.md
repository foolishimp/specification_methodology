# Independent review: STDO source repair, candidate-02 (18 Nov 2026)

**Verdict: `falsified`.** The candidate applies the owner's rulings in ODD itself, but it does not yet do so coherently across ODD's consumers. I found one severity-3 finding and one severity-5 finding.

This is an independent assessment. It is not owner acceptance and it is not a release.

## Subject and basis

- **Product:** `urn:stdo:product-definition:stdo-3`, selected by `stdo_3.json`.
- **Installed basis:** `stdo://releases/v3.0.4/`, manifest SHA-256 `102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b`. I relied on the Writer's `read_basis.py check` receipt and did not recompute it.
- **Candidate:** `.ai-workspace/work/STDO_REVIEW_REPAIR_2026-11-18/candidate-02/`, `CANDIDATE.json` SHA-256 `40bf5567…988f50`, 95 files. I relied on the supplied hash and did not recompute it. The preimage is `before/`, and `SOURCE.patch` covers 33 affected files.
- **Claim:** the candidate implements the owner's rulings coherently and closes the returned findings within the selected scope.
- **Review time:** 2026-11-18.

## Actor and independence limits

- **Reviewer:** Claude, model `claude-opus-5-5` (Opus 5.5) from host metadata. Fresh session with Read, Glob and Grep only, read-only, nothing delegated.
- **Author:** Codex (`REVIEW_HOST.json`). I authored no part of the candidate.
- **Limit (EVALUATION §3):** the architectural direction the candidate adopts was first recommended in an earlier Claude-family review (`review-working-amendment.md`, "bring §11.5D back inside P4b"). The owner's ruling came after it. The basis states no policy on whether two activations of one model family are independent, and the default is that they are not. So my judgment of *that adopted direction* is not established as independent of its contributor's family. This limit does not affect the two findings below.

## Method and evidence read

I recorded my expectations before opening the candidate. They came from:
- the owner statements in the intake;
- the installed EVALUATION §§3–4 and `stdo-review` SKILL;
- current FOUNDATIONS P4b and the step-produced-fact definition (`before/`);
- ACTIVATION §5, "The workspace and an actor's account" (`before/`).

The expectations were:
- ODD requires tracking, reconciliation, recording of facts that cannot be re-acquired (P4b), evidence by reference and authority separation;
- ODD prescribes no ledger, event log, replay, fixed evaluation loop or carrier API;
- the register is an optional example and never outranks the workspace;
- Product means the intended end state and Goals means the current epics, in SPEC_METHOD and its copies;
- no downstream names remain;
- historical custody is stated honestly;
- no consumer reference dangles or drifts;
- the UX Msg-replay profile is untouched.

I then read:
- **Candidate ODD:** lines 1–230 and 370–1110 in full (F18 table, consumers, §§5–20).
- **Candidate files:** `examples/GENERIC_REGISTER.md`, SPEC_METHOD §2 (lines 50–70, 210–295), the templates README, the Product and Goals templates, and `requirements/README.md` lines 1–84.
- **Preimage ODD (`before/`):** §11.5B and A2–A4, A9–A16.
- **`SOURCE.patch`:** the non-ODD hunks and the Goals and requirements hunks.
- **Writer records:** `CHECKS.json`, `HISTORICAL_INPUTS.json`, `CONTRACT.md`, the link-check logic in `freeze_candidate.py`, and both earlier reviews.
- **Searches across the whole candidate:**
  - downstream names, `.genesis` and `worksite`;
  - the old §11.5D anchor and the removed closure-decision values;
  - the old evaluator, carrier and type names;
  - ledger, event-log and replay wording;
  - every `ODD.md#…` link and every "ODD family table … whose row" description, checked against the new F18 table.

## What holds

- **ODD no longer mandates the old runtime design.**
  - §11.5, §11.5A–D, §16, §17 and §20 make the mutable workspace the only truth surface.
  - They state that an observation need not be copied into a ledger, and they disclaim any immutable replay log, closure-decision enum, fixed loop or command API.
  - None of the removed carrier, evaluator or closure-enum names remain anywhere in the candidate.
- **Required functions are kept.**
  - §11.5D requires tracking and reconciliation before a material decision, P4b recording, and records that carry subject, basis, scope, evidence references and authority.
  - It also requires invalidation on change, supersession identity, one predicate per result with visible gaps, worker reports that cannot close work, and the same rules for inner steps.
  - The authority content of the old A2, A3, A10, A12, A14, A15 and A16 is carried by §11.5B, §11.5D, §10 and §11.7B.
- **The register is an optional example.** `GENERIC_REGISTER.md` says it is illustrative, that an equivalent LLM mechanism is allowed, that unavailable private state does not qualify, and that the register is not a truth surface. The same rule appears in ODD §11.5D, ODD §20 and `requirements/README.md:68-74`.
- **The UX Msg-replay profile is untouched.** UX.md is unchanged, and ODD consumer 6 adds no replay requirement.
- **Product and Goals.**
  - SPEC_METHOD:215-219, 254-258, 881 and 1112, the GETTING_STARTED row, and the templates README, Product template and Goals template now state the rulings: Product is the intended end state including capabilities still to be built; Goals are the current epics.
- **Earlier findings 1, 2, 4, 5 and 6 are closed.**
  - My own search finds 0 downstream names, `.genesis` or `worksite` in `build_tenants/`.
  - "Mutable workspace" is restored in I2.
  - "Truth" is now limited to the workspace.
  - The requirement is declarative and sourced from Product.
- **Historical custody is stated honestly.** The Goals page marks one source verified and one unresolved, which matches `HISTORICAL_INPUTS.json`. I relied on the Writer's `git show` receipts.
- **Most F18 consumer descriptions match the new table.** That covers PRODUCT_DEFINITION, REFERENCE_FRAME, TICKETS, RELEASE, SPEC_METHOD and AXIOMATIC_CALCULUS. One exception is in F1.

## Findings

| # | Sev | Where | Finding |
|---|---|---|---|
| F1 | 3 | `ACTIVATION.md:1448` (and its copy at `frames/stale-summary.md:660`); `standards/README.md:70`; `DESIGN_MODULE.md:242` | Three consumer descriptions still describe the old ODD architecture, contradicting the amended ODD they link to. |
| F2 | 5 | `SPEC_METHOD.md:55-59`, `249-250`, `282` | Three nearby sentences in the owning section keep the older Product and Goals framing. |

**F1 detail**
- **What the stale text says:**
  - ACTIVATION §5 consumers, row 1: "the ODD family table, whose rows for the immutable ledger and for yield import F4 for a replay-visible work state." The new F18 table has neither row; its F4 import is the P4b row, which says "no mandatory ledger or event-log design."
  - The standards README index entry for ODD still lists "the constructive evaluation and yield loop (A0 to A16)."
  - DESIGN_MODULE row 10 says ODD §11.5B makes "the runtime's admission authority" a specialisation of admission completeness. The new §11.5B instead leaves admission with ACTIVATION §4 and binds runtime control separately.
- **Violated property:** consumer descriptions match their owner (FOUNDATIONS §3 Consumers). The contract also required "consumer descriptions" to be updated.
- **Causal path:** none of these three files' stale lines are in the patch. The link checker only tests anchors, so it cannot see stale prose.
- **Affected boundary:** shipped core and index text plus a generated frame. The `stale-summary` frame covers exactly the resume-and-reconcile task, so it would tell an actor that ODD requires an immutable ledger and replay-visible state, which is the design the owner rejected.
- **Blast radius:** 3 source members and 1 frame, all shipped. No rule actually decides on these lines, because consumer lists and indexes are non-deciding and the linked ODD text governs. But they are what the owner's "Not complete" return was about.
- **Confidence:** high. The text was read directly and compared with the F18 rows.
- **Containment:** a careful actor who follows the link reaches the correct ODD text. Nothing else contains it.
- **Repair scope:** three sentences in source, then regenerate the frame.
- **Regression risk:** low.
- **Uncertainty:** whether other prose descriptions (not links) of ODD in unread parts of members are stale. Every "ODD family table … whose row" phrase in the candidate was checked.

**F2 detail**
- **What the old framing says:**
  - Line 58 says Product "names the current product definition of the mutable source project," the wording that caused the earlier misreading.
  - Line 250 says Goals hold "overriding concerns for the **next** body of work," while line 215 says the work wave is currently pursued.
  - Line 282, in the Manifesto, says "current product definition in explicit present-tense terms."
- **Causal path:** the patch edited only lines 215–219 and 254–258.
- **Affected boundary:** SPEC_METHOD only. None of these lines is copied into a frame.
- **Confidence:** medium-high.
- **Containment:** the paragraphs at 215 and 254 now define "current" as the adopted definition, so a reader of the whole section gets the right meaning.
- **Repair scope:** three phrases.
- **Regression risk:** negligible.

## Residuals

- **Successor dispositions are not yet recorded.** `requirements/README.md:33-44` (STDO-UP-015, RELEASE §9) needs dispositions for the removed ODD claims (A0–A16, the closure enum, the §11.5B inventory table) before any successor that carries this source is accepted. The intake excludes this from this review's premise, so it remains open for release time.
- **The independence limit above applies** to the adopted architectural direction.

## Adjacent observations

Triage is `not_applicable` to the claim for all of these.

- **`CHECKS.json` labelling.**
  - `preexisting_broken_links` lists `GENERIC_REGISTER.md`'s §11.5D anchor. The file is new, and the anchor exists in the candidate. `links(prior=True)` reads new files against the `before/` targets.
  - It also lists the two Goals links that the candidate removed.
  - `remaining_broken_links` is correctly empty, so the candidate is unaffected; only the evidence label is wrong.
- **Not indexed.** `GENERIC_REGISTER.md` is not in the standards README documents table, though DETERMINISTIC_CONTRACTS is. The PRODUCT_COMPOSITION example is not indexed either, so this predates the candidate.
- **Goals page.** `specification/GOALS.md` still names the downstream product and gives a machine-local absolute repository path. This is the Product's own non-normative page, so the self-contained requirement does not apply. Whether to keep it is the owner's choice.
- **Unchanged earlier-review items.** The earlier review flagged downstream short names in `requirements/PRINCIPLES.md` and `STDO_3_0_1.md`. Neither file is in the candidate, and I did not assess them.
- **Removed yield semantics.** The old A9 "yield" (return control from long-running work without classifying it as failure) is now left entirely to the runtime Product. That fits the ruling; noted only so the decision is visible.

## Scope and coverage limits

- **ODD lines 230–370 not read.** These cover §5 Nodes, Vectors, Probabilistic compute and Graph functions. The patch shows no hunks there.
- **Not read:** the old ODD §11.5D lines 924–1000 and 1103–1250 (A0, A1–A1b, A4a–A8 bodies), the old ODD lines 1285–1343 beyond A13's start, and unchanged members other than the sections cited above.
- **Not re-run or recomputed:** frame drift and frame selections (`CHECKS.json` receipt relied on), SHA-256 hashes, Git custody.
- **Not performed:** installed or runtime behaviour, which is a source-only claim.

## Invalidation and re-entry

This result is void if:
- any candidate byte or `CANDIDATE.json` changes;
- an owner ruling quoted in the intake changes;
- the selected basis or its manifest changes;
- the severity scale changes.

The result goes to the Product-owned decision authority. Both findings are bounded source repairs under unchanged law, re-entering ACTIVATION §5, the standards README, DESIGN_MODULE §2 consumers and SPEC_METHOD §2, then regenerating the affected frame. Repair, priority and acceptance are not mine to decide.
