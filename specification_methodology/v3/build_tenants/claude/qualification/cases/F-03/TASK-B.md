# TASK B: publish a repaired cut and dispose its predecessor

## Subject

Repository `acme-tools`: one Git repository that releases command-line
tools. The facts below are the whole subject; the record is invented for
this task and is evidence about no real product.

Authorities: Lena is the release authority and the human acceptance
authority for both projects. Priya maintains `ledger_cli`.

Until 2026-10-01 the repository released one project, and its release
record declared the unqualified ref profile. Existing refs: annotated tags
`v1.4.0-rc.1` and `v1.4.0-rc.2`, and an annotated selector tag `v1.4.0`
peeling to the `v1.4.0-rc.2` commit. On 2026-10-05 Lena's release record
assigned the namespaces `ledger_cli` (source root `tools/ledger`) and
`ledger_docs` (source root `docs`). Neither project has published since.

Review of `v1.4.0-rc.2` found a rounding defect. After intake triage
(ticket `T-55`) Priya committed a bounded fix on branch
`rc/ledger_cli/1.4.0`. She proposes, in this order:

1. Option P1: move tag `v1.4.0-rc.2` to the fix commit, because rc.2 was
   never accepted.
2. Option P2, if P1 is refused: create `ledger_cli/v1.4.0-rc.3` and
   `ledger_cli/v1.4.0` over the fix commit, and force-move `v1.4.0` to the
   same commit "so old links get the fix".
3. Her publication record lists: the tag name, the peeled commit, and a
   member inventory digest `sha256:77…e1`.

After publication, reviewer Tom reports one wrong sentence in the release
note, a release-facing asset. Lena writes: "Accept rc.3; Priya will fix the
note and tag the result `v1.4.0-final`."

Consumer `billing-svc` has a product definition whose basis is the exact
cut `v1.4.0-rc.1` with installed-manifest digest `sha256:12…9c`. Its CI job
runs one command, `adopt --latest --yes`, that computes an adoption plan
and applies it in the same invocation. A billing engineer writes: "The
selector now points at rc.3, so billing-svc already runs rc.3."

The 1.4.0 line names `v1.3.2-rc.1` (accepted) as its predecessor. Claims
of that cut, with what Priya recorded for each:
- C1 "CSV export preserves column order": the export module was rewritten
  in 1.4.0 and the 1.3.2 patch is absent; a 1.4.0 test checks column
  order and passes. Recorded: nothing.
- C2 "runs on Python 3.9": 1.4.0 requires 3.11. Recorded: "dropped,
  nobody uses it". No Product decision exists.
- C3 "the `--legacy` flag keeps the old output": 1.4.0 has a function
  `legacy_flag()`. Recorded: "conserved (same name)". No test exists.
- C4: branch `support/1.3.x` received a timezone fix on 2026-10-08. The
  release basis names no watched source for it.

## Instruction

1. For Option P1 and Option P2 separately, say whether it is lawful and
   name each release identity it touches, in the method's terms. Then give
   the exact refs a lawful publication of the fix creates or moves, and
   name what the publication record must bind that Priya's record lacks.
2. Say what Lena's message does and does not achieve, and what the method
   requires instead.
3. State `billing-svc`'s operative basis now, whether the engineer's
   sentence holds, and what a lawful adoption of the fix requires,
   including whether the CI job's single invocation is lawful.
4. Give each of C1 to C4 a disposition, or say it is unresolved and what
   that blocks.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
