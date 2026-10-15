# Review: C3-I4-01 common specification at `5d2b257`

Verdict: **no blocking defect**. The frozen revision is ratifiable as it
stands. Three findings are each a one-sentence change; the product owner
may take them in a successor freeze before ratification or carry them
into the ticket at admission.

## Subject, baseline, standing

- Subject: `specification_methodology/v3/specification/` at `5d2b257`,
  against the closed I3 input `1fce537`. Recording `51ccfd6`. Also read:
  the T-001 and T-002 changes, `build_tenants/README.md`, `v3/AGENTS.md`,
  `v3/CLAUDE.md`, Codex's expectations post (at `430f0f4`) and its
  divergence classification post (at `5d2b257`), and the handoff.
- Expectations: `20261015T060155Z_EXPECTATIONS_REVIEW_C3_I4_01_5D2B257.md`,
  committed at `dae2ed5` before any of the above was opened.
- Standing: cross-family, nonauthor of the common text, interested party
  twice: I built the competing Claude candidate, and I authored the
  port-review and comparison policy (plan D4, D6, Stage 3) that
  Cross-Synthesis paragraphs 4 and 5 and the Candidate Comparison
  selection paragraph adopt. My reading of those passages is a
  consistency check, not independent acceptance of them. The owner
  ratifies them.
- Budget: the full diff of every changed file, two mechanical checks, no
  subagent, no candidate read.

## Results against the expectations

| Exp. | Result | Evidence |
|---|---|---|
| E1 classification | met | All ten divergences classified in the divergence post with a reason; the classes match mine on every item. Reserved owner decisions are named in Product's Open Owner Decisions, each with its decision point: acceptance-review activations in each ticket; actual-use resources before the comparison, with missing resources leaving the criterion unresolved; the UX conflict under the ambiguity rule until a replacement is accepted; identity and packaging before any dependent acceptance and a release-candidate cut |
| E2 conservation and modal force | met | `requirements/README.md` states one test once: compare the decisions permitted and required on the same case, scope and authority, with triggers, exceptions and absent premises, examining owning text and consumer bindings with counterexamples; changed determination needs a replacement; undecidable stays unresolved; shared arguments may cover equivalent claims with coverage stated. Indicative wording can bind; replacing "must" is neither automatic conservation nor supersession; a package-wide equivalence assertion proves nothing at consumers. The conformance row applies that test and names the owner |
| E3 owed evidence and work items | met | Product's Candidate Comparison names what each return accounts for: six criteria, integrated checks, satisfied/falsified/unresolved, actual use with supported fit, own preceding-candidate reduction and the head-to-head. T-002's nine items name both tenants' work and an observable return each. CX-03 and CX-05 go to I4-02, CX-04 to I4-09, CX-06, CX-08 and CX-09 to I4-08, CX-07 to I4-06; CX-01 and CX-02 are carried through I4-01. The Claude handoff's gaps map to I4-02, I4-04, I4-05, I4-06 and I4-07 |
| E4 port authorship | met, authored policy | Cross-Synthesis: a port enters inside a declared cone with a record of source, owner, adaptation, affected claims and evidence to recheck; the port list is input, not an obligation; porting does not erase authorship; the receiving line's same-family nonauthor supplies the independent assessment, reason and limits recorded; donor reading supplementary; each handoff names which review covers each contribution. A repair produces a successor freeze with its affected owners, bindings, interpretations, frames, dispositions and evidence named; the reviewer checks changed material and dependents and whether reused evidence applies; a changed port gets nonauthor readback. Same meaning as the plan, no new machinery |
| E5 comparison | met | Eligibility requires the six criteria and integrated obligations satisfied on the exact candidate; missing assessment withholds acceptance and "does not invent a failed evaluation"; conformance adds "an unassessed candidate is not evidence that its peer qualifies"; no qualified choice exists; choosing a basis accepts no replacement, merges and publishes nothing |
| E6 agreement | met | GOALS, Product, frame basis, routing files and both tickets say the same thing: Codex prepares, Claude reviews the exact freeze, the owner ratifies at an exact commit recorded in T-001, admission names the ratified commit, donors live in the ticket. The historical `31f28f9` table is out of live law; Porting reads takes the donor from the admitted contract |
| E7 writing | two low findings | F2, F3 below |
| E8 smallest change | met | 35 insertions, 25 deletions in five files. No frame-file count, capacity figure or result representation is imposed; pillars, 52 discriminators and three integrated checks keep their meaning; the only removals are the historical table, the superseded port-list routing and the ported-part owner decision, now answered by Cross-Synthesis under ratification |
| E9 verification | met | All 19 recorded hashes and byte counts reproduce from `5d2b257`. All 16 links in the added specification lines resolve to a file and heading at `5d2b257`. Codex's 273-link pass was not rerun |
| E10 process | substituted, recorded | Plan step 1.2, a full review of `2beed8d` with the 52 discriminators, was executed as a bounded source reading, disclosed as such in the divergence post. The discriminator pass moves to Stage 3 on the I4 successor under I4-09. Step 1.1, my divergence list, was taken from the plan's starting list. Nothing is lost: the classifications are checked here, and the Claude line's repair list is defined by I4-01 to I4-09 |

## Findings

**F1, Medium.** Candidate Comparison: "Before the comparison, a nonauthor
records the tasks, supplied facts, grants, expected distinctions,
ordinary entry routes, tools and resource envelopes in the existing
qualification record." It does not say whose record. Each tenant has a
qualification record in its own territory, which the other tenant may not
read except under an authorised review. If each line records its own
protocol, the tasks are not shared and the comparison fails its own
matching condition. Smallest repair: "…in one record in the common work
carrier, or a record it names, identical for both candidates." The ticket
can name the record at admission without a specification change, but the
sentence is the law the ticket would be interpreting.

**F2, Low.** "Comparable coverage" is used twice in Product and once in
conformance without definition. Smallest repair: one clause at first use
in Candidate Comparison, for example "the same obligations assessed on
both candidates".

**F3, Low.** GOALS.md and `build_tenants/README.md` name the person
("Jim selects", "his choice", "Jim ratifies") where their surrounding text
and Product use the role. Smallest repair: "the product owner" in the six
new sentences. `AGENTS.md` and `CLAUDE.md` already use the name throughout
and are not changed by this revision.

## Observations for the ticket, no specification change

- **Replacement decisions are the schedule risk.** The law is right: an
  unresolved replacement blocks dependent acceptance, and the comparison
  needs both candidates eligible. That means every proposed relation on
  both lines, 68 on Codex and 15 on Claude at I3, must be decided by the
  product owner before Stage 3 closes, or no candidate is eligible and the
  return is no qualified choice. I4-04 should name that decision point and
  produce one consolidated list for the owner, by question rather than by
  tenant, since several relations overlap.
- **Port lists are now input, not obligation.** I4-03 says "evaluate
  C1–C6" and "evaluate X1–X9", with reasoned exclusions. That differs from
  plan D3, which fixed the lists. The specification's reading governs; the
  owner should know a tenant may decline a port with a reason recorded.
- **D6 in the ticket, Product's wording.** Product compares non-blocking
  findings over comparable coverage "with their impact stated". The
  ticket's "prefer fewer" should say the count is read with impact, so a
  smaller count of heavier findings is not a win.
- **Criterion 4 for the Claude line.** The frame basis defines a fresh
  actor as any family starting without prior private context or
  unselected repository instructions. A subagent in a clean context meets
  that. D5 option A therefore costs session tokens, not external spend.
- **One Claude handoff gap is implicit.** The frames' missing family rows
  and result maps (tradeoff TO1, the F5 kind label) are not named in the
  Claude column of I4-06; the tenant ledger carries them as HOW.

## Not done here

No candidate was read. The 52 discriminators were not executed on either
candidate; that is Stage 3 work. Codex's own link pass and Product
Definition verification were not rerun. This review accepts nothing;
ratification is the product owner's act.
