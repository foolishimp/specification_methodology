You are an independent source-first reader. Two successor texts, Line A and Line B, each restate the same predecessor method (rc.2). They record different dispositions for some predecessor claims. Your job is to judge, claim by claim, what each line's text actually does with the claim. You do not repair anything and you do not decide which line is better overall.

## Packet (read only these locations)

`/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/0818967d-061f-47a6-9924-2d7ac25b59f8/scratchpad/loan/packets/rA/`

- `INDEX.md`: all 97 rows with each line's recorded disposition.
- `rows/NN.md`: one file per row. Each holds the predecessor section verbatim, then each line's record (disposition, note, and for some rows a "changed meaning" statement), then each line's successor loci as line ranges in the full member copies.
- `A/standards/…` and `B/standards/…`: full copies of each line's members. Tenant names are scrubbed to `[tenant]`.
- `rc2/standards/…`: the full predecessor members.
- `common/PRODUCT.md`, `common/README.md` (the requirements README) and `common/ASSURANCE.md`: the common specification that both lines must satisfy.

And one supplement: `/private/tmp/claude-501/-Users-jim-src-apps-specification-methodology/0818967d-061f-47a6-9924-2d7ac25b59f8/scratchpad/loan/packets/rA2_supplement/CHILD_ROWS.md`. It gives three of Line B's sentence-level child rows (for rows 50, 53 and 54), so that a note's reference to "the child row below" can be checked.

Rules:
- Read nothing outside these two locations. Do not use git, the network or any other directory. Do not write or modify any file.
- Use Read with offset/limit, or `sed -n 'a,bp'`, `grep -n` and `wc` through Bash, all inside the packet.
- Quote at most 25 words at a time, always with file and line numbers.
- Budget: up to 200 tool calls. If you run short, finish the rows you have started and list the rest as not read. Never guess a grade.

## Your rows

These 33 rows, each one judged in full: 07 08 10 13 14 15 16 18 26 30 31 32 33 34 35 37 38 39 41 43 44 45 48 49 50 51 52 53 54 58 61 63 73.

In every one of them, Line A records `superseded` and Line B records `conserved`. Ignore all other rows; other readers have them.

## The meaning test (apply it exactly)

A successor changes a claim's meaning when it changes any of:
1. an obligation;
2. its modal force (must, should, may, must not);
3. an exception;
4. its scope or applicability;
5. which owner holds the claim exclusively.

Moving a rule to another place, restating it in other words, or deriving it from a more general rule, without changing any of the five, preserves meaning. A record's own label ("conserved", "superseded", a "changed meaning" statement) is a claim to check, not evidence.

Conventions, so that your judgments are comparable with the other readers':
- Relocating a determination to another owner preserves meaning (`common/README.md` 67).
- Apply element 5 only where the claim's own text names who holds an authority.
- A descriptive change of standing ("derived" to "selected") is not a meaning change.
- An additive mapping into the core results that leaves the predecessor's conditions and values intact is not a change. A mapping that fixes a determination the predecessor left to a declared rule, or that alters a value's standing, is a change.

Judge against the predecessor section in the row file. The inventory's granularity rule is that a row covers its heading's text up to the next heading of any level; a parent row does not cover its children.

## For each row, report these fields

- **Claim**: one line naming what the predecessor section obliges, permits or forbids.
- **A**: `unchanged`, `changed (elements …)`, `absent` or `cannot decide`, with the deciding line citations in A's member copies.
- **B**: the same.
- **Same change?** If both are `changed`, is it the same change? yes / no / partly.
- **Only in A / Only in B**: any obligation, condition, exception or distinction relevant to this claim that one line's successor text carries and the other's does not, with citations; or "none".
- **Common input**: is each line's change required, permitted, or in conflict with the common specification? Cite `common/` lines where it matters; say "not material" where it does not.
- **Records accurate?** For each line, does its recorded disposition match what its text does? A `conserved` record over a meaning change is inaccurate, unless the line's record discloses the change in a child row that is itself `superseded`. A `superseded` record over unchanged meaning is inaccurate.
- **Worth carrying across?** If one line's text has a determination the other lacks ("Only in …" non-empty), say whether it fills a real gap in the other line: one the common specification requires, one a reader of the other line would act wrongly without, or neither. Cite the reason.
- **Note**: at most two sentences.

## Report format

Return the whole report as your final message, in Markdown:

1. `## Rows`: one compact block per row, in row order, with the fields above.
2. `## Tallies`: counts for your rows of A unchanged/changed/absent/cannot decide, the same for B, "Only in A" non-empty, "Only in B" non-empty, "Worth carrying across" per direction, and inaccurate records per line.
3. `## Limits`: tool calls used, rows not read or read only by sampling, any departures from these rules, and anything in the packet that seemed malformed.

Be exact. Where the text does not settle a question, say `cannot decide` and say what would settle it.