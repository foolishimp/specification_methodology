You are an independent source-first reader. Two successor texts, Line A and Line B, each restate the same predecessor method (rc.2). They record different dispositions for some predecessor claims. Your job is to judge, claim by claim, what each line's text actually does with the claim. You do not repair anything and you do not decide which line is better overall.

## Packet (read only this directory)

`/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/0818967d-061f-47a6-9924-2d7ac25b59f8/scratchpad/loan/packets/rA/`

- `INDEX.md`: all 97 rows with each line's recorded disposition and any shared-cause tag.
- `CAUSES.md`: three shared causes that Line A's record tags on many rows.
- `rows/NN.md`: one file per row. Each holds the predecessor section verbatim, then each line's record (disposition, note, and for some rows a "changed meaning" statement), then each line's successor loci as line ranges in the full member copies.
- `A/standards/…` and `B/standards/…`: full copies of each line's members. Tenant names are scrubbed to `[tenant]`.
- `rc2/standards/…`: the full predecessor members.
- `common/PRODUCT.md`, `common/README.md` (the requirements README) and `common/ASSURANCE.md`: the common specification that both lines must satisfy.

Rules:
- Read nothing outside the packet. Do not use git, the network or any other directory. Do not write or modify any file.
- Use Read with offset/limit, or `sed -n 'a,bp'`, `grep -n` and `wc` through Bash, all inside the packet.
- Quote at most 25 words at a time, always with file and line numbers.
- Budget: up to 220 tool calls. If you run short, finish the rows you have started and list the rest as not read. Never guess a grade.

## Your rows

1. The three causes in `CAUSES.md`. Judge each once (see below).
2. The 40 tagged rows among 01–73: 01 02 03 04 05 06 09 11 12 17 19 20 21 22 23 24 25 27 28 29 36 40 42 46 47 55 56 57 59 60 62 64 65 66 67 68 69 70 71 72. For each, first apply your cause judgments, then check the row for anything that goes beyond its causes.
3. Rows 74–97: 24 rows where the recorded dispositions differ in other ways (one line records `conserved` or `superseded` where the other records `not applicable`, or one records `superseded` where the other records `conserved`). Judge each in full.

Ignore the other 33 rows; another reader has them.

## The meaning test (apply it exactly)

A successor changes a claim's meaning when it changes any of:
1. an obligation;
2. its modal force (must, should, may, must not);
3. an exception;
4. its scope or applicability;
5. which owner holds the claim exclusively.

Moving a rule to another place, restating it in other words, or deriving it from a more general rule, without changing any of the five, preserves meaning. A record's own label ("conserved", "superseded", a "changed meaning" statement) is a claim to check, not evidence.

Judge against the predecessor section in the row file. The inventory's granularity rule is that a row covers its heading's text up to the next heading of any level; a parent row does not cover its children.

## For each cause

- State in two or three lines what the cause changes relative to the predecessor result, judgment or conjunction text it replaces. Read the cause's predecessor rows (02 for AC-014 judgment separation; find the rows for RF-012 closed results and Result Conjunction in INDEX.md if present, otherwise use `rc2/standards/REFERENCE_FRAME_METHOD.md` and `rc2/standards/AXIOMATIC_CALCULUS.md` directly).
- Under the meaning test, does the cause change meaning? Which of the five elements, with citations?
- Does each line's text make that change? Cite the owning sections (for example each line's FOUNDATIONS result sections).
- Is the change required by the common specification? Cite `common/` lines (look for the single result algebra in `common/PRODUCT.md` "Result Algebra" and the requirements README).

## For each row, report these fields

- **Claim**: one line naming what the predecessor section obliges, permits or forbids.
- **A**: `unchanged`, `changed (elements …)`, `absent` or `cannot decide`, with the deciding line citations in A's member copies.
- **B**: the same.
- **Same change?** If both are `changed`, is it the same change? yes / no / partly.
- **Only in A / Only in B**: any obligation, condition, exception or distinction relevant to this claim that one line's successor text carries and the other's does not, with citations; or "none".
- **Common input**: is each line's change required, permitted, or in conflict with the common specification? Cite `common/` lines where it matters; say "not material" where it does not.
- **Records accurate?** For each line, does its recorded disposition match what its text does? A `conserved` record over a meaning change is inaccurate. A `superseded` record over unchanged meaning is inaccurate. For a `not applicable` record, decide whether the claim applies to the successor product, and why.
- **Note**: at most two sentences.

## Report format

Return the whole report as your final message, in Markdown:

1. `## Causes`: one subsection per cause.
2. `## Rows`: one compact block per row, in row order, with the fields above.
3. `## Tallies`: counts for your rows of A unchanged/changed/absent/cannot decide, the same for B, "Only in A" non-empty, "Only in B" non-empty, and inaccurate records per line.
4. `## Limits`: tool calls used, rows not read, any departures from these rules, and anything in the packet that seemed malformed.

Be exact. Where the text does not settle a question, say `cannot decide` and say what would settle it.