You are an independent source-first reader. The product owner has chosen line R as the baseline of a specification methodology, because its structure suits future expansion, and will borrow elements from line D. Your job is to find which of D's routing, frame and member elements R should borrow, and which it should not. You do not repair anything.

## Packet (read only this directory)

`/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/0818967d-061f-47a6-9924-2d7ac25b59f8/scratchpad/loan/packets/rB/`

- `R/standards/…`: the receiving line's members, its entry `README.md`, its 12 frames under `frames/` with `FRAME_INPUTS.json`.
- `D/standards/…`: the donor line's members, its entry `README.md`, its 7 frames under `frames/` with `FRAME_INPUTS.json`, `authority_compressions/` and `verification_material/DERIVATION_SOURCES.json`.
- `common/PRODUCT.md`, `common/README.md` (requirements README), `common/ASSURANCE.md`, `common/REFERENCE_FRAME_BASIS.md`: the common specification both lines must satisfy.
- `rc9/SCENARIOS.md` and `rc9/EXPECTED.md`: ten task scenarios (S1–S10) and their expected distinctions.
- `rc9/READ2A_REPORT.md` and `rc9/READ2B_REPORT.md`: two earlier desk traces of those scenarios through both lines. In them, candidate A is R and candidate B is D (a header says so); their line numbers match the files here.
- `R_FRAME_QUOTES.txt`: R's frame sizes against the 160,000-byte frame capacity, and which R frames copy each owner section. A change to an owner section grows every frame that copies it.

Tenant names are scrubbed to `[tenant]`.

Rules:
- Read nothing outside the packet. No git, network or other directories. Do not write or modify any file.
- Use Read with offset/limit, or `sed -n`, `grep -n` and `wc` through Bash, inside the packet.
- Quote at most 25 words at a time, always with file and line numbers.
- Budget: up to 200 tool calls. If you run short, finish what you started and list the rest as not examined.

## Constraints on any loan

- R keeps its structure: its family tables, its "Foundation to law" tables and its consumers paragraphs stay. A loan may add or change routing, add a section or frame, or restate D's content in R's form. It may not remove R's tables or create a second owner for a determination.
- R's frames are generated from R's owner sections by R's own generator; a frame loan is a new or changed frame definition (task, scope, owner sections), not a copy of D's frame file.
- The owner has put a_c (the formal interpretation), the authority compressions and complete interpretation coverage after the baseline.

## What to examine

1. **Entry and task routing.** Compare `R/standards/README.md` with `D/standards/README.md`. The earlier traces found these problems in R. For each, find whether a D element would fix it:
   - (i) no route or frame for evaluating and reusing results after a change (S5);
   - (ii) R's frame table omits two existing frames, `acceptance-release` and `member-build-assess` (S10);
   - (iii) route labels that land one hop short ("prove a realisation" lands in EVALUATION while the deciding sentence is in ACTIVATION §1, S3);
   - (iv) routes that name whole sections through derivation tables and consumer lists without saying where to stop (EVALUATION §1–2, FOUNDATIONS Results; S8, S9);
   - (v) S1: a procedure line that invites classifying a report as a lawful change before diagnosis.

   Also say what D's routing does worse, so that a loan does not import it (the traces name D's missing task rows for build-tenant binding, test-case authority and ambiguity governance, and its undefined intake shorthand).
2. **Frames.** Compare D's 7 frames with R's 12, by task and scope (read headers, task statements and `Source:` lines; you need not read whole frame bodies). Identify any task D's frames cover that R's do not, and whether R should add a frame or route for it. Use `R_FRAME_QUOTES.txt` for headroom.
3. **TRANSFORMATION_LIBRARY.** Say what `D/standards/TRANSFORMATION_LIBRARY.md` holds, where R carries the same determinations (name R's owners), and whether anything in it is absent from R or better placed for R's consumers.
4. **FOUNDATIONS.** Compare `D/standards/FOUNDATIONS.md` (85 KB) with `R/standards/FOUNDATIONS.md` (146 KB). Identify D sections that state a determination R states less precisely or not at all. Separately, identify where D's compact prose could serve as the deciding paragraph at the head of an R section while R's tables remain below it, and estimate what that would save an actor on the S8 and S9 routes.
5. **Verification material.** Say what `D/standards/verification_material/DERIVATION_SOURCES.json` does, what it depends on, and whether R needs an equivalent for the baseline or only after it.

## For each proposed loan, give

- **Element**: D file and line range.
- **Receiving owner in R**: file and section.
- **Adaptation**: what changes to fit R.
- **What it fixes**: the trace finding, common requirement (cite `common/` lines) or gap, with citations in R.
- **Meaning**: does adopting it change the meaning of any rule R now states (an obligation, modal force, exception, scope, or exclusive owner)? If yes, it needs the owner's replacement decision.
- **Frame impact**: which R frames copy the receiving section and roughly how many bytes they would gain; flag any frame that would pass 160,000.
- **Evidence to check again** after adoption.
- **Class**: `baseline loan`, `owner decision` (changes meaning or adds a member), `after-baseline loan`, `do not loan` (give the cited reason: a lost clause, a conflict with the common specification, a second owner, or a measured cost), or `R-only repair` (a gap in R that no D element fills).

Where D shows an advantage but fit with R is uncertain, class it `baseline loan` and record the uncertainty under evidence to check again.

## Report format

Return the whole report as your final message, in Markdown:

1. `## Loans`: one block per element, most valuable first.
2. `## Not to borrow`: D elements considered and rejected, with reasons.
3. `## R-only repairs`: R gaps no D element fills.
4. `## Answers to the five areas`: two to five sentences each.
5. `## Limits`: tool calls used, what you did not examine, any departures.
