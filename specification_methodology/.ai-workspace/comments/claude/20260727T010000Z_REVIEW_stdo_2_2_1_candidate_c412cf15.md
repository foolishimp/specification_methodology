# Independent Review: STDO 2.2.1 Candidate `c412cf15`

- reviewer: claude (independent)
- date: 2026-07-27T01:00Z
- subject: commit `c412cf15ae83ef827ca9f059c1dd90168fbe59cb`, local `main` in
  the `specification_methodology` checkout
- predecessor: released `v2.2.0` at `5326562f`

## Verdict

**Mechanically exact and lawfully based. Two findings, neither falsifying the
candidate: one is a supersession-classification judgment for F_H, the other is
this candidate's own new law failing on its own review claim.**

Every declared number reproduces. Ancestry is clean. Root conservation is
intact — the full `STDO-UP-*` clause set is identical to `v2.2.0`, with none
added or lost.

## Ancestry — The Question This Checkout Raised

I checked this first because I have twice flagged this checkout as sitting on
the rejected `c6c085a`, and authoring a successor there would have been a P0.

| Check | Result |
|---|---|
| `v2.2.0` is an ancestor of `c412cf15` | **yes** |
| rejected `c6c085a` (executable-overstep) is an ancestor | **no** |
| `archive/rejected-stdo-2.0-executable-overstep` | not an ancestor |
| `archive/rejected-stdo-2.0-overcorrected-normative-target` | not an ancestor |

The checkout was repointed onto the release lineage. My earlier hygiene
finding is discharged.

**On "behind 5" — this is not missing law, and the report's caution is
slightly over-stated.** `origin/main` sits at `ad7b1d0` and does **not**
descend from `v2.2.0`; it is the abandoned pre-release line. Its 5 commits are
3 review receipts plus two method commits (`b3e5e4a` three-view gate,
`f28e0d8` ontology-before-semantic-design) dated before the 2.0 release. I
verified both laws are present in the candidate — `## 4B. Ontology-First
Design Rule` and 12 three-view references in `DESIGN_MODULE_METHOD.md`. The
content was replayed into the incremental lineage exactly as the 2.0 recovery
M1 required.

So reconciliation is a **ref decision, not a merge of missing law**: publishing
means deciding what `origin/main` should point at, not recovering content. Do
not merge `origin/main` into the release lineage to clear the "behind" — that
would reintroduce the abandoned line.

## Mechanical Verification — All Exact

| Claim | Result |
|---|---|
| Aggregate `485d22a7…72da2` | **exact** |
| 41 members retained | **41**, member path set identical to `v2.2.0` |
| 9 changed / 32 conserved | **9 / 32** — declared set equals actual set |
| All 9 declared member hashes | **9/9 reproduce** |
| 13 compression bindings | **13/13, 0 stale** |
| Normative growth 142 lines / 1.45% | **9,934 vs 9,792 = 142 = 1.45%** |
| Whitespace (trailing / tabs / CRLF / final newline) | 0 / 0 / 0 / 0 |
| `git diff --check` | clean |
| Nothing pushed or tagged | confirmed |
| Six untracked artifacts untouched | confirmed (6 entries) |

**Root conservation:** the `STDO-UP-*` clause set at `c412cf15` is **identical**
to `v2.2.0` — no clause added, none lost. `STDO-UP-003` Recursive Prime And
Root Conservation survives, reworded from "authority-bearing unit" to
"candidate semantic atom," which is exactly consistent with the declared Prime
supersession rather than a silent loss.

## Content — Coherent And Incident-Derived

Four delta families, taxonomised as **one supersession plus three
clarifications**, which is the right shape to justify a patch number:

- **Prime Semantic Atoms** — declared supersession: "supersedes wording that
  defined a realization unit itself as Prime." The removed text
  ("A realization unit is **prime** when it introduces one irreducible new
  semantic or topological boundary…") is exactly what the declaration names.
  Correctly matched.
- **Capability-Aware Proportional Constraint** — "clarifies `STDO-UP-014`."
- **Decision-Complete Symbolic Design** — "clarifies the accepted proportional
  sequencing relation."
- **Semantic Review Reconstruction** — additive.

Two of these are direct answers to findings from my own prior reviews, and
both deserve recording:

1. **My N2b from the RC review is fixed and cited.** The note states the
   ticket-method compression "restores the accepted source qualifier
   `competing or ambiguous authority`, which its `v2.2.0` projection shortened
   to `competing authority`." That is precisely the finding I filed.
2. **`TICKET_METHOD` now makes durable review traceability law:** "A claimed
   independent review may support promotion or closure only when its exact
   subject and verdict are durably traceable through an existing ticket,
   commentary, qualification, or release-evidence carrier. A statement that
   review occurred, an unbound conversation summary, or an unavailable draft is
   not the review verdict."

The "Semantic Review Reconstruction" family also encodes, as law, the two
errors I actually made reviewing S03: "Headings and artifact presence
establish location. Green tests establish only the properties they actually
assert. None supplies a missing semantic relation." That is my failure mode
converted into a constitutional check, which is the right destination for it.

## F1 — One Change Is Classified As Clarification But Reads As Supersession

`SPEC_METHOD.md:1649` replaces the co-evolution admissibility test:

- **was:** "When upstream truth leaves no unresolved material architecture
  decision, design, implementation, and tests may co-evolve."
- **now:** "When `DESIGN_MODULE_METHOD.md` applies and its decision-complete
  network has no unresolved material relation, design, implementation, and
  tests may co-evolve. Otherwise accept the smallest causally closed affected
  design set…"

The note classifies this as a clarification and states it "does not create a
new design obligation." I think that under-describes it in two respects:

1. The admissibility bar moves from "no unresolved material architecture
   decision" to "a decision-complete network with no unresolved material
   relation" — and the note itself defines decision-completeness as a
   satisfiable constraint network over identities, authorities, functions,
   relationships, cardinalities, topology, lifecycle transitions, public
   contracts, admission conditions, failure routes, effect and closure laws,
   projections, module mappings, and material algorithmic obligations. That is
   a materially higher bar than the predecessor text.
2. It gains a scope condition ("when `DESIGN_MODULE_METHOD.md` applies") that
   the predecessor did not have, and the fallback branch changes from "the
   affected design" to "the smallest causally closed affected design set."

A consumer lawfully co-evolving under the old test could be non-conformant
under the new one without changing anything. By the project's own standard
that is a semantic supersession, and qualification condition 2 requires the
delta to identify **every** semantic supersession.

This is a classification judgment, not a defect in the law — the new rule is
better than the one it replaces. But it is F_H's call whether the delta
declares one supersession or two, and it bears on whether `2.2.1` is the right
number. Cheapest resolution: add a "This supersedes…" sentence to the
Decision-Complete section and keep the patch number, or rule explicitly that
tightening a test's precision without changing its intent is a clarification
under this project's law.

## F2 — The Candidate's Own New Law Fails On Its Own Review Claim

The report states "Independent review: no P0/P1/P2 blockers." There is **no
durable record of that review**. At `c412cf15`, `.ai-workspace/comments/`
contains my 2.2.0 RC review, two 2.0-era codex checkpoints, and two human
decisions — nothing reviewing this candidate. Repo-wide, the only file
mentioning `c412cf15` or `485d22a7` is the release note itself.

This candidate adds the rule that such a claim "is not the review verdict."
So by 2.2.1's own law, the review supporting 2.2.1 does not yet support
promotion. That is not a gotcha — it is the new law working correctly on the
first subject it touches, which is the strongest evidence it was worth adding.

This is the **eighth** occurrence of this pattern I have recorded across STDO
and ABG. Making it law is the right fix; the fix now needs to be applied to
this candidate before its own publication.

## Publication Path

The note carries a `## Publication Boundary` section and no status/tag-existence
claims — the status-free pattern established at 2.2.0 is conserved, so a
zero-delta final remains achievable.

`RELEASE_METHOD` is unchanged in this candidate and still states: "If a project
has not ratified a separate patch-release or hotfix method, the default
post-tap path is a new RC cycle." STDO has ratified no patch method, so 2.2.1
should go through `v2.2.1-rc.1` → independent exact-cut review of the RC →
direct human acceptance → final tag, exactly as 2.2.0 did. The patch number
does not shorten the process.

T-003 is well-formed: `change_class: requirement_reprice`, `re_entry_point:
SPEC_METHOD.md`, `triaged_at: 2026-07-26`, `review_status:
candidate_ready_for_review`. Unlike the S05 ticket, the class was declared
before the change, not after.

## Recommendation

Sound work on a clean base. Before an RC:

1. Rule on F1 — declare the sequencing change a second supersession, or record
   the clarification ruling explicitly.
2. Land a durable review record (F2) — required by this candidate's own law.
3. Decide the `origin/main` ref question deliberately; do not merge the
   abandoned line to clear "behind 5."
