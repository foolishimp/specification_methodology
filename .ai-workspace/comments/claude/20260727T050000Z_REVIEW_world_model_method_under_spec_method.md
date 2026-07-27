# Review: `WORLD_MODEL_METHOD.md` Under `SPEC_METHOD.md`

> **Status: intake evidence for T-004. Not a candidate review.**
> This review binds the **predecessor** member at `v2.2.1`
> (SHA-256 `9108ef2d…`), not the 2.2.2 candidate. It is retained as the
> motivating observation that opened T-004 and carries no promotion or
> closure authority over the successor.
>
> Disposition of its findings under 2.2.2: **F1 (promotion-gate status)
> discharged** — all sites now state one truth. **F2 (unpinned mutable
> citation) discharged** — the companion surface is bound by commit and
> document digest. **F3 (cited experiment range) and F4 (refinement drift)
> remain open** and are not carried by T-004.

- reviewer: claude (independent)
- date: 2026-07-27T05:00Z
- subject: `specification/standards/WORLD_MODEL_METHOD.md`, 1,203 lines,
  SHA-256 `9108ef2d…` — byte-identical in the authoring checkout, the
  2.0-incremental clone, and the ABIogenesis `.genesis` projection
- governing basis: `SPEC_METHOD.md` at the current authoring head
- last substantive change: **2026-04-30** (v1.5.0 standards compression)

## Verdict

**One material finding: the document's declared epistemic status now
misstates the evidence it cites.** The standard says its promotion gate
remains *open*; the companion program it cites reports that gate was
**tested and failed**, twice. Everything else is minor or good.

The error direction is conservative — the construct is already treated as
candidate either way, so no downstream over-claim follows. But "not yet
tested" and "tested and failed" are different epistemic positions, and the
difference is decision-relevant.

## Two Impressions I Checked And Discarded

Recording these because they would have been plausible-sounding findings:

- **No `STDO-UP-*` clause identifiers.** Not a defect — `UX_METHOD.md` also
  has zero. Clause IDs are not universal across members.
- **A "Manifesto" section inside a normative standard.** Not a defect —
  `SPEC_METHOD.md` itself has one at line 134.

## F1 (P1) — The Promotion-Gate Status Contradicts Its Own Cited Source

The standard states, in two places:

> "Until such a test runs and succeeds at a meaningful threshold, published
> cuts that invoke this method should be read as candidate cuts…" (§Epistemic
> Status)

> "…leaving the formal conditional-independence promotion gate **open**."
> (§Companion Surfaces, line 1202)

Both phrasings present the gate as **not yet run**. The cited companion
program, at its current head (`2da7871`, 2026-07-13), states:

> "That promotion gate has now been **tested and fails**: single-chart
> subtraction fails in exp 20, and multi-layer…"

> "**Direction-native conditional independence (exp 20)**: the formal
> promotion gate **fails at both layer 8 and layer 2**."

> "The direction-native conditional-independence test and its multi-layer
> successor have **both failed**, so read the alignment below as *consistent
> with*, not *validation of*."

> "**Do not move the promotion gate.** Exp 20 failed at layers 8 and 2."

Under `SPEC_METHOD` `STDO-UP-001`, a load-bearing claim must identify "the
relation between witness and claim… and falsification condition." This
document does state its falsification condition — commendably — but the
condition has since been tested and not met, and the document still describes
it as outstanding. That is the "read the data under the label" failure at
constitutional altitude: the label says *open*, the data says *failed*.

**Why it matters despite the conservative direction.** The two readings give
opposite guidance to anyone deciding where to spend effort. "Gate not yet
attempted" invites an attempt. "Gate attempted twice, failed, and the
companion explicitly says do not move it" is a settled negative result that
should be inherited, not rediscovered. A reader of the standard alone would
reach the wrong conclusion about the state of the program.

**Repair:** restate the epistemic status as *tested and not met* rather than
*open*, carry the companion's "do not move the promotion gate" instruction,
and keep the candidate classification — which remains correct and is now
better supported, not worse.

## F2 (P2) — Two Unpinned Mutable External Citations

`WORLD_MODEL_METHOD.md` is the **only** STDO member containing external URLs.
Both point at
`github.com/foolishimp/constraint_emergence_ontology/blob/**main**/…` — a
mutable branch ref with no commit pin, tag, or digest.

This sits oddly inside a methodology whose entire discipline is exact
immutable identity: 41-member aggregates, per-member digests,
`stale_if_source_digest_changes`, exact candidate qualification, zero-byte
final deltas. Every internal reference in STDO is pinned or conserved; the one
external load-bearing reference is not.

It is not hypothetical drift: the companion last changed **2026-07-13**, the
standard **2026-04-30**, and nothing detects the gap — which is precisely how
F1 arose. The citation happens to still resolve (§15 and §15.1 exist), which
is luck rather than law.

**Repair:** pin to a commit SHA plus a content digest, on the pattern the
authority compressions already use for their sources, or vendor the alignment
table into the standard so the load-bearing claim is conserved with the member
set.

## F3 (P3) — The Cited Experiment Range Excludes The Decisive Experiment

The Companion Surfaces entry cites "Experiments 08–18." The companion now runs
through experiment 25 (§12.1, "Follow-up wave — experiments 19–25"), and the
experiment that settles the promotion gate is **exp 20** — outside the cited
range. The citation therefore points away from the result that most changes
the standard's own claim.

## F4 (P3) — The Four Working Refinements Have Drifted From Their Source

The standard's four refinements and the companion's current §15.2 four
overlap but are no longer the same list in wording or order:

| Standard | Companion §15.2 |
|---|---|
| 1. Identity is a translation, not a variance axis | 4. Identity is a DC shift, not a principal-variance axis |
| 2. Attribute schemas sense and fragment | 2. Attribute schemas sense and fragment; they do not isolate |
| 3. Core identity, not core size, is diagnostic | 3. Core identity, not core size, is the discriminator |
| 4. Boundary is interventional, not structural | 1. Effective blanket is geometric, not set-theoretic |

The substance survives; the standard presents them as "Four Working
Refinements Indicated By The Empirical Program," which reads as a faithful
projection of a source that has since been re-cut. Same class as F2 — no pin,
so no detection.

## What Is Genuinely Good Here

This should not be lost in the findings, because it is the best instance of
its kind in the member set:

- **It is the only STDO member that declares its own central construct
  candidate and names the experiment that would promote it.** Under
  `STDO-UP-001`'s proof-target discipline and 2.2.1's semantic-review law
  ("green tests establish only the properties they actually assert"), that is
  exemplary rather than merely adequate.
- **The candidate status is made downstream-safe by default:** "Tooling that
  materializes Markov-object cuts under this method should default to a
  candidate-class publication kind and reserve any formally-closed publication
  kind for cuts backed by a real promotion-gate result." That is the correct
  fail-closed direction, and F1 does not weaken it.
- **It subordinates itself correctly.** §Relation To Design Module Method
  states "This document does not make the empirical Markov-object program a
  prerequisite for all design work," and assigns the general engineering law
  to `DESIGN_MODULE_METHOD.md`. A theoretical framing that declines to become
  a gate on unrelated work is the right altitude.

## Consumption And Blast Radius

`WORLD_MODEL_METHOD.md` is referenced by `UX_METHOD.md`,
`DESIGN_MODULE_METHOD.md`, `ODD_METHOD.md`, the standards `README.md`, and
both agent templates — but it carries **no entry in
`stdo_compressed.md`**, so it does not reach agents through the authority
compression. Combined with its self-subordinating stance, the practical blast
radius of F1 is low: it misinforms a reader of this document, not the
operative law of a consuming Product.

That is also why none of these findings block anything. They are corrections
to a conserved member that has ridden unchanged through v1.6 → v2.2.1-rc.2.

## Recommendation

Handle as one bounded `requirement_reprice` on this member when a successor
line is next opened — not as a hotfix, and not inside the 2.2.1 RC, whose
zero-byte final delta should not be disturbed. F1 is the substantive item;
F2 is the structural fix that prevents F1 recurring.
