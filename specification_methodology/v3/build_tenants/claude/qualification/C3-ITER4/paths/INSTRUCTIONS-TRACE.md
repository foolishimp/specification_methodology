# Instructions for a desk trace of one deciding path (I4-07)

You are a same-family nonauthor tracer in a fresh context. You trace one
deciding path on three subjects and return the measures the protocol
declares. Read this file, then only what the routes below reach.

## Subjects and entry

| Subject | Where to read it |
|---|---|
| S0, the predecessor | the installed release at `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/` (read the files directly) |
| S1, the preceding candidate | commit `2beed8d`, `specification_methodology/v3/build_tenants/claude/standards/`, read only with `git -C /Users/jim/src/apps/specification_methodology-claude show 2beed8d:<path>` |
| S2, the current candidate | the commit named in the activation, same path, read only with `git show <commit>:<path>` |

Route entry, on every subject: start at the subject's `standards/README.md`
(for S0 the installed one), and from there follow only declared routes: a
link, a named section, or a frame's `Source:` line. Never search the
corpus and never open a file no route named. A deciding locus that no
route reaches is recorded as "unreachable by route": that is an adverse
result, never a skipped step. Frame entry is not traced here.

## The path

The activation names one path id. Its task sentence, situation, clusters,
entry and guard items are in `design/REDUCTION.md` §4.4 at the S2 commit;
read that one table row and nothing else of that file. The task, facts
and grant are the same on all three subjects.

## Measures, per subject

- M1 deciding loci: distinct sections whose own determination you apply
  to reach the result (owner plus each refinement used; pointers not
  counted);
- M2 independent deciders: sections met that state a rival determination
  for the same question;
- M3 reconciliations: pairs of loci, or one label with two meanings, that
  you had to reconcile to decide;
- M4a supplied bytes: the entry file's size;
- M4b cumulative acquired bytes: the sum of every section acquired along
  the route, repeated reads counted again (a section runs from its
  heading to the next heading of equal or higher level);
- M5 hops: distinct sections acquired beyond the entry;
- G: for each guard item of the path, `pass` or `fail` with the sentence
  that decides it.

## Outcome

Against each baseline (S0 and S1) the path is "simpler to determine and
apply" only when G passes, M2 and M3 do not increase, at least one of
them decreases, and every increase in M4 or M5 is explained by a declared
tradeoff (TO1, TO2, TO3 in §4.3) or a preserved distinction. Otherwise
"not established". Under the ratified standing: "simpler" is
`satisfied`; "not established" is `indeterminate` when the measures
cannot decide the required improvement and `falsified` when a
counterexample defeats it (G fails, or M2 or M3 increases).

## Return

Write one Markdown file at the path the activation names, with: the
route taken on each subject (entry, each hop with its section and bytes,
the determinations applied with a quote of at most 20 words each, rivals
met, reconciliations made); the measures table (M1 to M5 and G per
subject); the verdict against S0 and against S1 in the ratified value;
and any finding (a determination reached only outside the route, a label
with two meanings, a guard failure), each with its locus. Then print the
two verdicts. Do not repair anything.
