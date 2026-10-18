# Review: the first common build, against the baseline and as standalone work

Author: the Claude tenant session. It wrote the baseline (Claude RC9) and
most of the register's agreed forms. Under T-003 step 6 this is a
supplementary port and readback review. It is not the covering independent
review, whose assignment (`COVERING_REVIEW_ASSIGNMENT`) is still open. Much
of the standalone residue reported below is text this session wrote, and
the post says so where it applies. This post is commentary. It accepts,
merges or releases nothing.

The owner asked: "review against baseline and as its own standalone work".
The plan and its expectations were recorded before the candidate was
opened ([plan](20261018T161846Z_PLAN_REVIEW_COMMON_FIRST_BUILD.md),
`c4f59356`). The severity scale used here is the plan's.

## Answer

No. The first common build is not freezable as it stands.

Three groups of text defects block freeze. None needs a meaning decision.

1. Two members contradict RELEASE on release identity (B1).
2. Seven section pointers lead to appendices the build removed (B2).
3. Passages still depend on the source project or on its construction
   history (B3). Most of these came from the baseline, and the build did
   not remove them.

Freeze also needs owner decisions. Codex's list carries A1's reach, Q13/Q14,
rows 93–96, the ten disputed rows, P1's class and the covering review. Four
of Codex's standalone adaptations change meaning or need acceptance, and the
handoff's decision list omits them: SC2, SC3 and SC5 (D1–D3), and SC4 (D4).
SC2 and SC5 carry row-level `STANDALONE:` decisions in the conservation
record; SC3 and SC4 carry none. Freeze needs both: the blockers fixed and
those decisions closed.

Every mechanical claim Codex made reproduced. The two gaps I report in its
records tooling go beyond what it claimed. They are not reproduction
failures.

## Subject

- Package: `build_tenants/common/` on `tenant/common/standalone-v3`, tree
  `082df4ea2b7b3658aab528bbfbcfe81234ccc810`, 81 files. The tree is the
  same at `49445152` and `d60dead4`, and the branch has not moved since.
- Construction record: T-003 and `.ai-workspace/common-build/` at
  `d60dead4`.
- Baseline B: `build_tenants/claude/` at `3a209713`.
- `main` gained four commits during the review: `1a37ee9f`, `79fa6edb`
  and `d35b55aa` (the v2 installer work under T-034), and `c2f67fec` (a_c
  tooling requirements). None touches the package tree, and I did not
  review them.
- One of them replaced the installed `stdo` toolchain with 0.1.5 at 16:42Z,
  during this review. I re-ran the installed verifier under 0.1.5 and got
  the same result.

## Mechanical claims: all reproduced

| Claim | My reproduction | Result |
|---|---|---|
| Package checker passes the candidate | pinned launcher, pristine copy | valid; 81 members; 0 failures; 9 advisory signals |
| G1 member identity | one byte appended; an undeclared file added | both fail: changed member, extra member |
| G2 metadata | a stale `Status: under construction` header, re-frozen | fails |
| G3 JSON and references | duplicate key; broken link; file symlink | fail, fail, refused |
| G4 checker authentication | tampered checker under the original pin | refused before execution |
| G5 advisories visible, not failing | pristine report | 9 "complete Product view" signals, valid |
| Prior-version route control | a `stdo://releases/v2.5.1-rc.2/` link added | fails |
| Records rebuild | `build_records.py` from frozen sources, `GIT_DIR` read-only | all four artifacts equal the persisted ones; 16 controls pass; 705 identities (636 shared, 14 tenant, 55 nonbody) |
| G6 compression scope | a compression proposed `intentionally_removed`, then `conserved` | both rejected |
| G7 relation evidence | a row's evidence removed; a disputed row's `CONFIRM-ROW` decision removed; a not-applicable reason replaced by a successor claim; an effective disposition invented | all rejected |
| Installed verification | my own materialisation of all 81 files; the canonical member-set digest recomputed | `[]`. It catches one-byte changes to a standards member, a plugin member and the release note, and an altered set digest |
| Tooling unit tests | `unittest discover` | 29 of 29 pass |
| Frames | owner and section digests recomputed; excerpts compared | 12 frames bind current owners; 195 section digests match; excerpts exact; largest 141,858 B, under the 160,000 B cap |
| Frame regeneration | all 12 frames deleted from a scratch copy; Codex's `generate_frames.py` rerun | byte-identical package: all 81 files, including the frames and `FRAME_INPUTS.json` |
| Links | every Markdown link and anchor | 0 broken; B had 13. Two notation false positives (`F_K[v](X_v)`) |

One control passed when a defect was planted: the sentence "law carried
from the common binding requirement of the source project" added as prose.
The checker's declared scope excludes it: "Prose and generated-project
paths require review." That is a scope limit, not a defect. It is also why
the residue in B3 survived the mechanical gates.

Two gaps in the records tooling:

- `validate()` accepts a `superseded` or `conserved` row with no receiving
  locus. One row already does this. `plugins/spec/LICENSE` is proposed
  `conserved` with no receiving locus, although the package holds that
  file.
- `build()` counts unresolved receiving loci but does not refuse them. The
  count is currently 0 of 814. `VALIDATION.json` writes the constant result
  `mechanical_properties_pass` whatever the count.

## Against the baseline

### The register, forward

All 28 items are at their owners in the agreed form, with these states:

- A1's four complete-Product-view passages are unchanged, pending the
  owner's reach decision.
- R1–R4 and R6 are not landed (Q13/Q14 gate them).
- M6 is not a donor transplant.

These sections and items are as expected:

- ACTIVATION §3 and FOUNDATIONS §4 Results differ from B only by
  provenance strips, renamed CONFORMANCE routes and the phrase "installed
  builder's", which became "core". The five-value result algebra is
  unchanged.
- No item on T-003's exclusion list is present.
- In the executive profile, the ledger change [78] is A1. Items 9 and 11 of
  §21 (and the RF-005 pointers) are P1 and M3. Item 10 of §21 is P2, at a
  locus P2 lists in `REGISTER.json`.

### Every changed paragraph, converse

The forward check cannot find a meaning change nobody registered, so I ran
the converse:

- I diffed the 29 changed members paragraph by paragraph, after stripping
  the citation pattern. Frames are excluded because they are regenerated.
- I set aside 286 pure history strips and 9 removed disposition tables or
  appendices.
- I mapped each remaining change by heading to the loci of a register item
  or of an SC adaptation. SC1–SC7 are the seven standalone adaptations in
  `returns/root-construction.json`.
- 63 changes matched no locus. I read each one. They are history strips the
  pattern missed, removed appendix pointers, SC3's rewording outside its §5
  locus, the Q10 wording, and renamed examples.

I found no meaning change outside the register and SC1–SC7. Limit: a
heading match shows where a change is, not that it stays inside its item's
scope. I read the hunks of the items that carry findings below (P1, P2, M3,
A1).

The dismissed set could hide a lost obligation, so I searched it for modal
force (must, never, only, requires, cannot, may not):

- 23 deleted tables:
  - 21 are Source dispositions tables. The conservation record accounts for
    each of their rows among its 705 identities.
  - One is CONFORMANCE §5's old table, now SC3's full distinctions.
  - One is the README frames table, which was rewritten.
- 35 deleted blocks: appendix text, release-note history, or law that is
  still present or re-expressed by a registered item. ACTIVATION §1's
  delegated-worker paragraph is still present. TICKETS' repricing paragraph
  is M6, AXIOMATIC_CALCULUS §8 is SC2, and the recoverability benchmark is
  SC4.
- 19 word-level deletions: provenance notes. Three of them, in the
  DESIGN_MODULE, UX and WORLD_MODEL leads, also said that "the
  predecessor's 'must' is written in the indicative". SPEC_METHOD §2's
  present-tense rule and RELEASE §9 ("indicative wording can state a binding
  law") carry that reading.

No lost obligation found.

### Records

- 19 truncated `not` values are restored with their reasons. None is a
  compression row.
- All ten compression rows are deferred and unresolved.
- `CONFIRM-ROW` decisions exist for rows 01, 11, 12, 19, 20, 25, 27, 32, 40
  and 48. That is exactly the register's set.
- `KEEP-OR-WITHDRAW` decisions exist for rows 93–96.
- There are `P1-CLASS` decisions (two rows), an `A1` decision and four
  `A1-REACH` decisions.
- Q1–Q19 are carried as historical questions. Q10 is open.
- Separability:
  - M1–M7 and A1 each have their own loci and their own row decision, so the
    owner can decline one alone. Doing so means reverting its loci by hand;
    no per-item patch set exists.
  - P2 (item 10) and M3 (item 11) share EXECUTIVE_BASELINE §21, but on
    separate items.

### Side checks

- File lists: B and common hold the same 81 paths. No file was dropped or
  added.
- `2e7fa0f6` adds 143 files under `comments/codex/`, the ticket and two
  construction files. It edits GOALS, `stdo_3.json` and
  `build_tenants/README.md`, which T-003 line 31 grants.
- Neither `2e7fa0f6` nor `156ac5af` changes any file under
  `comments/claude/`.
- I checked the scope of the 143 review files, not their bytes. I have no
  earlier hash record of my own to compare them with. I did not use Codex's
  `REVIEW_CHECKPOINT.json` instead, because it is the author's own record.

## As standalone work

The build removed most of the history. Matches for my history pattern fell
from 2,308 in B to 713. `rc.2` matches fell from 1,031 to 1, and that one is
an example cut name at RELEASE.md:446. The remaining "Claude" and "Codex"
matches are host-adapter names in the plugin. What remains is below.

### B1. Release identity contradicts RELEASE (blocks)

- TRAVERSAL_OCCURRENCE.md:1587–1590 (Closed profile signature):
  "`publication_basis.release_uri` is one absolute immutable
  `stdo://releases/v<version>/` URI for a release or
  `stdo://releases/v<version>-rc.<positive-ordinal>/` URI for a release
  candidate."
- AXIOMATIC_CALCULUS.md:1195–1196 (§8): "The release may be a candidate or a
  stable release; its coordinate states which".
- RELEASE disagrees with both:
  - RELEASE.md:45–50: "The product-local cut name is always:
    `v<version>-rc.<n>`".
  - RELEASE.md:62–68: `v<version>` "denotes a mutable version-line selector
    … not immutable identity and not sufficient as an exact constitutional,
    dependency, evidence or replay basis".
  - RELEASE.md:253–256: the logical release is
    `stdo://releases/v<version>-rc.<n>/`.
  - RELEASE.md:276–279: acceptance is a verdict over the exact RC, "rather
    than a second carrier".
- The product-definition schema's `stdoReleaseUri` pattern also requires
  the `-rc.<n>` form. I checked this in both packages.

B's TRAVERSAL_OCCURRENCE (line 1580) admitted only the RC form. The stable
form arrived with SC2: both passages sit in rows carrying `STANDALONE:`
decisions.

Repair: restore the RC-only URI in both members, and drop "stable release"
or route release standing to RELEASE §8. This is needed whatever the owner
decides on SC2. The cold reader also reported it as a contradiction between
owners, answering a task that asked whether the owners agree (see below).

### B2. Pointers to removed appendices (blocks)

Each sentence describes an appendix that SC1 removed:

- ASSURANCE.md:109: "§17 records dispositions and decides nothing."
- IDENTITY.md:71: "§13 records where each predecessor claim is carried".
- ODD.md:1192: "The dispositions of §21 are the successor dispositions of
  RELEASE §9".
- PRODUCT_DEFINITION.md:125: "§13 records dispositions".
- RELEASE.md:131: "§11 records dispositions".
- WORLD_MODEL.md:566 and :620: "named in §15". Line 565 also adds a bare
  `#builder-project`, which is not a link.

The build removed the same sentence from EXECUTIVE_BASELINE (§23),
SPEC_METHOD (§12), REFERENCE_FRAME (§15) and EVALUATION (§8). These seven
were missed. The sentences are B's.

### B3. Text that needs the source project or its history (blocks)

Origin: B, unless marked new. The build removed some of each kind, for
example ACTIVATION's "carried from the common construction requirement" and
12 of 27 "is new" sentences.

- "Law carried from the common … requirement":
  - FOUNDATIONS.md:481, :554 and :1061;
  - SPEC_METHOD.md:1791;
  - RELEASE.md:685;
  - frame copies at `binding.md:92`, `member-build-assess.md:229` and
    `:663`, and `acceptance-release.md:644`.
- Construction-candidate text. FOUNDATIONS Formal representation
  (≈1418–1440):
  - "The candidate's a_c interpretation represents …";
  - "The candidate demonstrates the applicable positive, negative and
    unresolved cases";
  - "these obligations create no seventh criterion".

  The passage relies on construction criteria outside the package, and on
  an interpretation delivery that T-003 excludes. EVALUATION.md:120 ("the
  common frame basis") is the same kind.
- "Is new" with no stated comparator: ACTIVATION.md:872, 1052, 1090 and
  1136, and their frame copies (11).
- Owners outside the package. The package names "the Cross-Synthesis rule"
  (FOUNDATIONS.md:1091 and 1264–1265) and "the constraint-surface fidelity
  rule" (1418–1421) "of the Product that owns this corpus", but states
  neither rule. The other "Product that owns this corpus" references
  attribute ownership of content the package states itself. Those are minor.
- New in common: CONFORMANCE.md:182 (row 42), "Common requirements decide
  fitness". The package defines no "common requirements". The phrase
  arrived with SC3.
- Smaller items: GLOSSARY.md:344 ("the earlier label `Evidence Class` is
  superseded") and templates/README.md:21–29 ("retain their revision-2
  meaning"). ACTIVATION §2 says "a `stdo://` route in this section is
  provenance only", but the section now holds no such route.

### Self-application

B2, B3 and the Q10 marker (Minor) break the package's own SPEC_METHOD §2
Specification surface rule: "material that is no longer live is deleted,
superseded or moved to commentary". RELEASE §10 "Open questions" states
current open questions in the present tense, which that rule permits.

### Material defects

- REFERENCE_FRAME.md:159 states the stale-basis rule without its qualifier
  ("A stale, advanced, ambiguous or mismatched basis returns
  `invalid_basis`"). RF-005 in the same member (313–317) now reads "An
  evaluation performed on a stale … basis that cannot support its required
  claim returns `invalid_basis`". The member states two versions of its own
  rule, whatever P1's class turns out to be.
  - On the landed text the qualifier narrows when `invalid_basis` applies.
    I read that as a meaning change. Classing it is the `P1_CLASS` decision.
- The records defects in the mechanical section: the LICENSE row, the
  missing locus control, and unresolved loci that are counted but not
  refused.

### Minor

- Q10 wording, at four places in UX:
  - "the two compliance tests … differ in scope" asserts a reading Q10 has
    not decided;
  - "with the ambiguity retained for the governing authority" is a
    provisional marker in live text.
  - Suggested: "Where the two tests disagree, the stricter applies under §1
    Authority's fail-closed rule." Q10 stays in the record.
- TRAVERSAL_OCCURRENCE.md:1574 has a bare "§8" that names no member. It
  means AXIOMATIC_CALCULUS §8, and it is new with SC2.
- Inherited from B. The reader found these, and I confirmed each by
  counting it in both packages:
  - EVALUATION.md:499 labels RELEASE §9 "family F19". FOUNDATIONS lists
    RELEASE as F15 and gives F19 to traversal occurrence.
  - AXIOMATIC_CALCULUS §8 and TRAVERSAL_OCCURRENCE spell digests
    `sha256:<hex>`, while the schemas and the template use bare hex.
  - `STDO-UP-013` (ODD.md:790) and `STDO-UP-020` (frame-basis template) are
    labels the package never defines.
  - GETTING_STARTED.md:333 points to a `QUICKSTART.md` outside the package.
- The plugin version is `3.0.0-dev.1` (SC7). RELEASE §7 requires the cohort
  suffix at cut (RELEASE.md:508–511). This is acceptable before cut and must
  be stamped then.

## Owner decisions this review adds

Codex's handoff lists A1_REACH, Q13, Q14, rows 93–96, the ten rows, P1's
class and the covering review. These four are missing from it.

- **D1. SC2 beyond M5.** M5 at Derivation provenance is agreed. Beyond it,
  AXIOMATIC_CALCULUS §8 and the two traversal identity rows change.
  - B's law: `derivation_basis` binds "one exact accepted predecessor cut";
    "It cannot depend on the publication carrier or on the calculus-basis
    identity being created"; "Same-release references … are publication or
    cross-context relations, not derivation provenance (P3)".
  - Common's law: principle references resolve "inside the same exact
    immutable package named by `publication_basis`", and the two release
    URIs and manifest digests are equal.
  - T-003 line 42 supports both readings.
    - "All normative dependencies … resolve locally" supports SC2.
    - "Generic method law about revisions, historical evidence, successor
      conservation or provenance remains stated in full" supports B's law.
      That law names no version, and the actual predecessor is bound only in
      the external record.
  - T-003 does not settle it, so it is the owner's decision. The record
    carries it only as row-level `STANDALONE:` decisions. If SC2 stands,
    keep B's rule against depending on the identity being created.
  - I wrote B's law, so I have an interest here.
- **D2. SC3: CONFORMANCE's scope and its oracle.**
  - B: CONFORMANCE owns the cases "this corpus must pass before it is
    qualified". The construction specification owns the expected
    distinctions, outside the package. "No rule an adopting Product applies
    depends on §5", and a case names "the independently specified expected
    distinction".
  - Common: CONFORMANCE "defines conformance cases for the method's shared
    owners and their consumers" and states its own 80 expected
    distinctions. "Independently specified" is gone.
  - That helps adopters. But when the package itself is qualified, its
    author now writes the oracle inside the subject.
  - If SC3 stands, it should say who specifies the expected distinctions
    when the package itself is qualified.
  - CONFORMANCE has no predecessor identity, so no record row or
    `STANDALONE:` decision covers it.
  - The README index row (standards/README.md:55) still describes the old
    scope. That is minor unless the owner wants that scope back.
- **D3. SC5: a new duty for applications.**
  - WORLD_MODEL's four working refinements now say "An application records
    its own evidence for the boundaries and overlays it publishes". B
    grounded the refinements in its research programme and put no evidence
    duty on applications.
  - The family table moves append-only from consequence to choice. The law
    itself stands at WORLD_MODEL.md:641, so the move is a trace
    reclassification.
- **D4. SC4.** It reads as a sound generic re-expression, and I recommend
  acceptance:
  - recoverability is measured on the package's own exact evidence;
  - a comparative claim declares its baseline;
  - no prior release is a runtime dependency.

  Its row (Method self-qualification) is pending as `CONFIRM-ROW-20` but is
  not flagged as a standalone adaptation.

A1's reach still matters to a standalone reader. Until it is decided, the
executive profile asks the Executive to acquire only the material portion of
the frontier at its attention cycle. Elsewhere, at EXECUTIVE_BASELINE.md:370
and 1274 and GETTING_STARTED.md:603, it requires a complete Product view.
These are the nine advisory signals.

## Cold reader

- Reader: one Fable reader at maximum effort, which is the same model family
  as the baseline author.
- Material: an 81-file copy of the package and nothing else. It used no
  repository, no git and no history.
- Tasks, from the README routes: release identity, calculus identity,
  triaging a stale frame, and reviewing a candidate with a mis-resolving
  route.
- Tasks 1, 2 and 4 aimed at defects I had already found. Agreement there
  shows a cold reader can see them; it is not independent discovery. The
  reader's independent value is task 3 and its four lists.

Results:

- Usable standalone: triage, bounded work, review and acceptance. The
  owners agree, the result algebra is one, and every anchor resolves.
  - Task 4 (result value, non-disposition, the two stale-basis cases):
    answered with high confidence.
  - Task 3: answered with medium confidence, because no owner names the
    change class for regenerating a derived surface. The reader chose
    between `realization_refactor` and "not a substantive change".
    SPEC_METHOD §4 could name it.
- Release and calculus identity are where standalone use fails.
  - The reader reported B1 as a contradiction between owners.
  - The reader could not settle how a `principle_refs` entry is formed.
    AXIOMATIC_CALCULUS §8's "semantic-address URI" has no written rule.
    Some derivation items, such as table rows and a paragraph, have no
    heading to address.
- Residue. The reader found every B2 pointer. It also found the B3 kinds my
  own history scan had missed: the construction-candidate text, the "is
  new" sentences and the owners outside the package. That is why B3 is
  longer than my plan expected.
- Reported but not verified by me:
  - the namespace grammar in the installed-release manifest schema is looser
    than RELEASE's;
  - the README route for occurrence histories lands on the adoption clause.

## Next

- Codex: B1–B3 are text repairs. A residue search for "carried from",
  "common requirement", "the candidate", "is new", "records dispositions"
  and "Product that owns this corpus" would catch every B3 kind found here.
- Owner: D1–D4 join the existing list.
- The covering nonauthor review remains unassigned. This review cannot stand
  in for it on B's content or on the register's wording.
