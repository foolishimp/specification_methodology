# RT2: round 3 regression pass, tenant contracts and status claims

**Reviewer**: Claude, cross-family Reviewer RT2. Repairs nothing.
**Subject**: frozen `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`. Compared with round 2's `55bbf9e`. The diff was read in context, together with the `AGENTS.md`, `CLAUDE.md` and `build_tenants/README.md` changes that the patch omits.
**Admission evidence after the subject**: main `651581c` (shared input and both admissions) and `HEAD` `e4e72b0`; the Claude tenant ledger at `5ab44d5c` and `81032c4` (Claude-authored).
**Paths**: relative to `specification_methodology/v3/`. "T-00x" means `.ai-workspace/tickets/active/T-00x-*.md`. Line numbers are at `355aa86` unless prefixed with another commit.

## Result

Results use the installed Reference Frame Method family.

| Scope | Result |
|---|---|
| Overall: the conjunction of the scopes below | **falsified** |
| 1. No regressions (round 3 expectation 9) | **falsified**: RT2-03. RT2-04 is a material feasibility gap; the rest are minor |
| 1b. Earlier holds: neutrality (5), a_c boundary (10), writing (12) | **satisfied**, with minor findings |
| 2a. Contract texts `EC-CODEX-I3-02` and `EC-CLAUDE-I3-01` against the specification | **satisfied**. Consistent with territory, input, baselines, limits and reservations; symmetric line by line |
| 2b. Admission of `EC-CLAUDE-I3-01` (interested) | **indeterminate**: RT2-01 and RT2-02 |
| 2c. Admission of `EC-CODEX-I3-02` | **satisfied**, with a minor naming point. T-002-CODEX:114 binds "this Codex session in its coordination frame, under Jim's run-to-completion instruction", which is the session that admitted. The record still says only "the selecting Executive" (see the RT2-01 correction) |
| 3. Status claims | **satisfied**. Nothing is presented as signed off or accepted. "CLOSED FOR CONSTRUCTION" is qualified, but it rests on RT2-03 |

## Findings

| ID | Severity | Claim | Evidence | Smallest correction | Interested |
|---|---|---|---|---|---|
| RT2-01 | material | The actor that admitted `EC-CLAUDE-I3-01` is not shown to be selected for that line. The record calls it only "the selecting Executive". By the T-001 record, it is the common-repair Executive role of the Codex common-pen parent activation. That is not the Executive the contract binds, and no owner selection of it as the Claude line's C3 Executive is recorded. The authority coordinate the project defines, "this ticket and the contract" (T-002:100), is present; the defect is in actor selection. | `651581c:T-002-CLAUDE:43`: "the selecting Executive admits `EC-CLAUDE-I3-01`" (no actor named). `651581c:T-001:47`: "Executive disposition: … admit the separately identified EC-CODEX-I3-02 and EC-CLAUDE-I3-01". T-001:43: "The parent acts next as the Git Writer … Executive then selects". The contract, T-002-CLAUDE:34: "the Claude tenant session acts as Executive for its line". `REFERENCE_FRAME_BASIS.md:25`: the C3 Executive is "The product owner, or one activation the product owner selects". `REFERENCE_FRAME_BASIS.md:24`: the common-definition subject is "shared purpose, boundary, checkpoints and affected clauses", which does not include tenant admissions. `PRODUCT.md:237–239`: "The pen drafts the contract on the Executive's selection … records the Executive's decision to run it". T-002-CLAUDE:56: whether the 2026-10-12 Executive binding carries forward "is Jim's decision". T-002:126: M1 is "OPEN; Jim names the Executive and Reviewer per tenant". If the owner's words are instead read as an override, installed TICKET_METHOD:669–670 requires "explicit human override of the exact contract". "do that close the round 2 findings" predates the contract and does not name it. | Name the admitting actor and the source of its selection. Then either the owner selects that actor as admitting authority for the Claude line, or the Claude line's bound Executive (or the owner) admits the exact digest `3c9288…`. Apply the same naming to `EC-CODEX-I3-02`. | yes |
| RT2-02 | material; does not block specification sign-off | **The owner's verbatim words do not decide whether the Claude line starts before sign-off on B or after sign-off.**<br>The authority to admit before sign-off rests on the pen's paraphrase.<br>The owner's verbatim words select a Claude-line iteration 3, and they say to wait for round 3 before sign-off. Neither forbids starting on B.<br>The pen reads them as permitting a start before sign-off on B. The Claude Executive reads them as a start after sign-off on the signed-off commit. Both are inferences.<br>The Claude Executive's reading is a tenant-territory record, which cannot authorise (`PRODUCT.md:251`).<br>The owner's 14:42Z question refers to "Codex's round 3 repairs" as pending, although `355aa86` was frozen and admitted by 07:36Z. The owner may have answered without the admission in view.<br>The owner's answers are not in any ticket. | **Pen records:**<ul><li>T-001:23 holds the only verbatim words, "do that close the round 2 findings". It paraphrases the accepted proposal as "prepare both tenant execution contracts".</li><li>T-001:51 records that the owner "asks whether both tenant implementations can then start". That question becomes "asking to start both" in `GOALS.md:40` and "The owner requests both successive implementations" in T-002:44.</li><li>T-001:41 is the pen's own rule: input "may be selected and admitted for draft implementation before final common acceptance".</li></ul>**Claude ledger (Claude-authored):**<ul><li>`5ab44d5c:…/C3-SYNTHESIS/LEDGER.md:360`: the owner chose "Repair now, then iteration 3 (Recommended)".</li><li>`:382–388`: the owner asked "how can you do I3 without i3.specificaiton completeing…". The Claude Executive recorded a hold that "waits until the common pen freezes … and the product owner signs it off".</li><li>`81032c4:…/LEDGER.md:404–406`, at 14:42Z, after the 07:36Z admission: the owner answered "Wait for round 3 (Recommended)" to the sign-off question and "Claude line" to "Which line should start iteration 3?".</li><li>`:408–413`: the Executive's inference, "starts only after … signs off".</li><li>`:3`: the pen is to transcribe these into T-002-CLAUDE. T-002-CLAUDE has no such entry at `355aa86`, `651581c` or `HEAD`.</li></ul>**Rules and current ticket state:**<ul><li>Installed TICKET_METHOD:758: a human ruling "receives durable disposition before the next affected acceptance boundary. Its source wording remains distinct from agent interpretation."</li><li>`651581c:T-002-CLAUDE:26`: "The separate tenant session can begin".</li></ul> | Quote verbatim, in T-001, the proposal that "do that" accepted. Transcribe the owner's verbatim answers from the Claude ledger into T-002-CLAUDE. The owner then states whether `EC-CLAUDE-I3-01` on B stands or is superseded by a contract on the signed-off commit. | yes |
| RT2-03 | material | **Regression of round-1 M7 point 4, which round 2 recorded as closed: I3-00 no longer closes on the owner's sign-off.**<br>The I3-00 exit proof dropped "owner sign-off separately recorded".<br>The C1-era gate sentence was rewritten in place, on the strength of the pen's own claim of owner authority.<br>`651581c` then labels I3-00 "CLOSED FOR CONSTRUCTION". | Diff line 255, the old I3-00 exit: "…independently reviewed; owner sign-off separately recorded". Diff line 256, the new exit: "Final common acceptance remains a separate owner decision". Round 1 M7: "Make the owner's sign-off the closure condition of I3-00". Round 2 marked M7 "Closed". T-001:162 rewrites the sentence "The next C3 snapshot is recorded in T-002 after common sign-off" as "The then-planned … is historical". `651581c:T-002-iteration-3-work:98`: "ROUND-2 REPAIR CLOSED FOR CONSTRUCTION … Common repair, source review and input preparation are complete". The disposition record's RR2-01 entry does not record removing sign-off from I3-00's exit. | Restore "owner sign-off separately recorded" as I3-00's exit. Alternatively, split I3-00 into a construction-input item that a working review can close and a sign-off item that stays open. Record the change of closure condition with its reason. | no |
| RT2-04 | material (feasibility) | **Harness-based fresh-actor runs cannot establish criterion 4 fit, and no route to a fully measured run is named.**<br>The new Limits text denominates context in bytes and bars an unmeasured platform portion from establishing fit. A reviewer can decide this: an unmeasured host portion means fit is not established.<br>Both contracts concede that platform context is uninstrumented, so runs through a harness that adds its own context cannot establish fit. Runs through direct calls with recorded input can.<br>Neither the specification nor the contracts name that route. | `PRODUCT.md:403`: "context in bytes … Unmeasured platform context or unsupported truncation cannot establish fit". `PRODUCT.md:397`, criterion 4: "has a frame that fits the declared limits". T-002-CLAUDE:39 and T-002-CODEX:39: "identify unknown platform portions and make no unsupported fit claim". T-002-CODEX:90: "Parent platform context and reasoning tokens are not fully instrumented". `REFERENCE_FRAME_BASIS.md:29`. | State how fit is established when a host adds context. Either require fresh-actor runs whose whole input is recorded, or permit a declared, separately measured host allowance. State the result an unmeasured portion yields. | no |
| RT2-05 | minor | Conformance treats a criterion as possibly inapplicable; Product makes all six mandatory. | `conformance/README.md:74`: "Five applicable member criteria are satisfied". `PRODUCT.md:200`: "All six member acceptance criteria are mandatory". | "Five member criteria are satisfied and the sixth is missing…" | no |
| RT2-06 | minor | Term drift after the tier rename. | `requirements/README.md:121`: "deriving method determinations from their normative owners". `PRODUCT.md:68` now reads "three tiers of method law", and `PRODUCT.md:346` reads "method-law owners", with guide and packaging conventions binding. | Use "method-law owners" at README:121. | no |
| RT2-07 | minor | Dangling antecedent. | `PRODUCT.md:165`: "Their separate construction and integrated-closure section checks those decisions." | "…checks the Executive's acceptance decisions and C3 closure." | no |
| RT2-08 | minor | Intent asserts as fact a relationship that Product treats as established only on demonstration. | `INTENT.md:13`: "Category theory expresses these relationships with explicit preservation obligations." `PRODUCT.md:23`: "established only when its claim meets the categorical demonstration standard". | "The method uses category theory to state these relationships; each categorical claim holds only when demonstrated." | no |
| RT2-09 | minor | The reduction pre-declaration names no record, so "before" cannot be checked. Neither contract declares the dimensions. | `requirements/README.md:63`: "Declare the measured dimensions and any proposed tradeoff before the comparison". The contracts (T-002-CLAUDE:33, T-002-CODEX:33) fix the subjects only. | Name the record whose commit must precede the comparison, for example the activation record or frozen expectations. | no |
| RT2-10 | minor | An unlabelled stale Actors table contradicts the current contract. | T-002-CLAUDE:63: Executive "Claude, the session holding the pen … bound". T-002-CLAUDE:66: "Ledger Writer: the common pen (Claude)". Against these, T-002-CLAUDE:34: "the common pen records admissions". T-002-CLAUDE:56: the later-phase Executive is open. | Label the table historical, or update it. | yes |
| RT2-11 | minor | The milestone state is inconsistent after admission. | T-002:126: M1 "OPEN; Jim names the Executive and Reviewer per tenant". T-002:32: "Current actor assignments are those in the admitted tenant contracts". | Record the owner's naming, or state that the contract actor bindings await it (see RT2-01). | yes |
| RT2-12 | minor | The C3 row in GOALS is stale. | `GOALS.md:19`: "the Codex line is authorised … The peer line retains its own activation record". This is unchanged at `651581c`, whose `GOALS.md:26` records both admissions. | Update the C3 row. | yes |
| RT2-13 | minor | "Cross-tenant review" is undefined relative to cross-family review. | Both contracts at line 34: "cross-tenant reviews retain the owner's separate authorisation". `PRODUCT.md:401`: a different family is the default Reviewer. `build_tenants/README.md:39`: "An actual Claude review runs as Claude". It is undecided whether a tenant Executive may invoke the peer's model family without owner authorisation. | Define the term, or state the rule. | yes |
| RT2-14 | minor | The identical Resources clause has asymmetric starting effect. The Claude line has no recorded spend allowance; Codex carries USD 12. | T-002-CLAUDE:39 and T-002-CODEX:39: "Any paid actor trial must bind a separately recorded applicable allowance". T-002-CODEX:90: "initial USD 12 aggregate operating allowance". There is no allowance in T-002-CLAUDE or the Claude ledger. This is lawful, because `PRODUCT.md:403` lets the Executive select limits. | No text change. The Claude line records an allowance before its first paid trial. | yes |
| RT2-15 | minor (pre-existing, not a regression) | The Executive "records" limits, but it holds no write grant. | `PRODUCT.md:403`: "The Executive selects and records the limits". `PRODUCT.md:390`: "holds no write grant". | "selects the limits; the pen records them". | no |
| RT2-16 | minor | Product's dependency summary is wider than its owner. | `PRODUCT.md:163`: the dependency contract "fixes the exact a_c theory". `requirements/A_C_DEPENDENCY.md:43`: "encoding basis for construction and checking"; the released basis follows an open owner decision. | "…fixes the exact a_c theory used for construction and checking…" | no |

## Clean passages

- **RR3-06 restoration.** The `EC-CODEX-I3-01` block at `355aa86` is 4,459 bytes, SHA-256 `fc6ed417…`, byte-identical to `dad25ef`. The rejected revision is recorded as history (T-002-CODEX).
- **Successor digests.**
  - `EC-CLAUDE-I3-01` is 5,163 bytes, `3c928885…`, and reproduces at `355aa86`, `651581c` and `HEAD`.
  - `EC-CODEX-I3-02` is 5,089 bytes, `b1a8ab97…`, and reproduces at the same three commits.
  - Neither block has been edited since admission, although 21 later commits change T-002-CODEX.
- **Shared input.** All 24 member hashes and sizes in `651581c` T-002 "C3 I3 round-2 shared input snapshot" reproduce from B `355aa86`.
- **Preimage claims.**
  - The Claude tree at `5ab44d5c` is `b75d6aa6…`.
  - The Codex tree at `d832a51` and at `de8232a` is `dd222838…`.
- **Contract symmetry.** The two blocks are identical line by line except for these lines:
  - the heading;
  - the preimage;
  - the comparison subject;
  - the tenant name in Actors;
  - the territory path;
  - Required work.

  Required work is symmetric in kind: each line rechecks the findings against its own candidate, F1–F5 for Claude and I3-01–14 for Codex, without the common index asserting their current state.
- **Comparison baselines.** Both baselines are fixed before each line's iteration 3 work.
  - Codex uses `3ad1fca`, named earlier in `EC-CODEX-I3-01`.
  - Claude uses `5ab44d5c`, which is pre-iteration 3 because I3-1 stopped before writing (Claude ledger `5ab44d5c:…/LEDGER.md:386–388`).

  Both are lawful under `requirements/README.md:61`. They differ in kind: Codex's repairs to its iteration 3 are counted against its iteration-2 cut, whereas Claude's revision-2b repairs fall before its baseline (interested).
- **Territory and reservations.** These match Development Isolation (`PRODUCT.md:210–278`) and Open Owner Decisions (`PRODUCT.md:409–410`). The Claude worktree, which is this reviewer's own line, is sparse to `specification/`, `.ai-workspace/` and `build_tenants/claude`.
- **One acceptance record.** The tenant frontier records proposals and the ticket records acceptance. This is consistent across:
  - `PRODUCT.md:334`;
  - `PREDECESSOR_CLAIMS.md:3, 5, 8, 18`;
  - `requirements/README.md:31`;
  - criterion 3;
  - `conformance/README.md:73`.
- **New definitions.** "Consumer" and "contracting" are defined at `requirements/README.md:16`, and the constraint-surface purpose is stated.
- **Independence clause.** The new clause at `PRODUCT.md:401` separates reporting a defect from authoring a repair. It is neutral.
- **Status claims.** No ticket or GOALS line presents common sign-off, member acceptance or C3 closure as given. `GOALS.md:18` and `651581c:GOALS.md:18` both keep "Final common sign-off remains open".

## Earlier "holds"

- **Neutrality (5): holds.**
  - The new rules apply to both lines alike: standalone criterion-4 use without a mandated directory (`PRODUCT.md:358`), generic outcome-driven contracts without the optional profile (`conformance/README.md:18`), and the limits rule.
  - The contract texts are symmetric.
  - RT2-14 is an asymmetry of starting state, not of rule.
- **a_c boundary (10): holds and is strengthened.**
  - Categorical item 5 now keeps theory, interpretation, carrier and checker separate (`requirements/README.md:166`), closing the round-2 drift.
  - Mechanical results are retained only "where that evaluation is selected" (`A_C_DEPENDENCY.md:71`).
  - RT2-16 is minor.
- **Writing (12): holds, with RT2-06 to RT2-08.**
  - No personal names are added to specification surfaces. Existing Codex and Claude mentions are unchanged.
  - The `PREDECESSOR_CLAIMS.md` header drops "STDO 3".
  - The new Intent summary defines a_c, A, Z and reference frames at first use.

## Corrections to this review's own record

- The round 3 expectations say "After `355aa86`, `main` changes only GOALS status lines up to `65c0210`". That is wrong:
  - `651581c` adds the T-002 shared-input snapshot, both admissions, the T-001 closure disposition, the work-list status and two Codex reviews;
  - `8a0cab4` to `65c0210` record Codex construction in T-002-CODEX and the work list.
- Expectation 2 assumed `EC-CLAUDE-I3-01` was admitted at `355aa86`. It was a draft there (T-002-CLAUDE:43, "Admission record: pending") and was admitted at `651581c`. Its digest check is reported above.

## Independence and limits

- **Interested.** Claude is the tenant that `EC-CLAUDE-I3-01` governs. Every Claude-line judgment is marked. The evidence for RT2-02 includes Claude-authored ledger entries, which are cited as the Claude Executive's records, not as tickets.
- **Authorship.** Several repairs adopt round-2 wording from this reviewer line, for example:
  - the RR3-01 split between frontier and ticket;
  - RR3-04's single overall result;
  - RR3-06's restore-and-successor remedy.

  Under `PRODUCT.md:401`, this report supplies no independent acceptance evidence for those passages.
- **Peer worktree.** The Codex worktree's branch and sparse list were seen as metadata only. Nothing above relies on them. Codex evidence comes from committed branch or main objects.
- **Not read.** Neither candidate body, and the two Codex working reviews that support the admission. Those reviews were read only as recorded in T-001.
- **Sampling.** `PREDECESSOR_CLAIMS.md` was checked through its diff: header lines only, with rows unchanged.
- **Overlap.** The closure of round-2 items (RR3-01 to RR3-07, M1, M4, RR1-N2) belongs to a separate reviewer's scope. It is touched here only where it bears on regressions.
