# Use-trial findings and disposition

These findings concern the recorded experiments. They do not accept a method
member or a release. Original actor returns and failed checks remain unchanged.
The Executive's dispositions distinguish a source defect, a trial defect and
an actor error; a green host check establishes none of those distinctions alone.

## Repaired source defect: undertaking versus conclusion

The original C6 actor at `a746559` reported an actual, inconclusive load test as
`not_performed`. The source then carried that error after an earlier review
prescription conflated evaluating with reaching a conclusion. The fixed oracle
required `performed` and an unresolved verdict. The host detected the discrepancy.

The source repair at `79e53e3` separates evidence that the evaluation occurred,
its extent and its conclusion. Fresh C6 actors at `9982ab8` and `77f2efb` retain
P1's actual undertaking and distinguish the absent P2 return. Both later host
checks pass; both final graders support the latter distinction. This closes
that demonstrated source contradiction, not every possible performance error.

## Final matched grading

Two fresh graders received identical 79,796-byte evidence packets for the ten
`77f2efb` actor returns. Their [first](runs/use-77-grade-1/RESULT.md) and
[second](runs/use-77-grade-2/RESULT.md) judgments are retained separately.
Neither grader changed source, proposals, host evidence or oracle.

| Subject | Observations and disagreement | Executive disposition |
|---|---|---|
| C1 stale summary | Both support source-led correction; real tests expose the stale expectation before and pass after. | Bounded behavior supported. |
| C2 cold continuation | Both support retaining completed work and the open review slot. One result uses `not applicable` for effects. | Continuation supported; non-enumerated vocabulary is not accepted as a core value. |
| C3 completed remote effect | Both support not repeating the request. Graders disagree whether proposed record edits were `not_started` or `unknown`. | No duplicate request in the fixture. Later host observation supersedes the proposal-time account; the observation boundaries must not be collapsed. |
| C3b unknown effect | Both support stopping and identifying the needed owning observation. They disagree on performance for the completion predicate. | Safe stop supported. Inspection of available evidence was performed; fresh remote observation was not. The return does not bind those procedures precisely enough to accept the coordinate without qualification. |
| C4 changed dependency | Both support retaining independent V2, exposing stale V1 and new failing V3. | Bounded dependency handling supported; historical `pass` text is not current green evidence. |
| C5 failed A plus uncovered B | Both support conserved failure/citations and uncovered coverage. The actor also uses free prose for an effect value. | Conjunction supported. Prose is not automatically an authenticated refinement into the core effect domain. |
| C6 absent versus undecidable | Both support the corrected distinction. Graders disagree about the proposed STATUS write's observation boundary. | Original source defect repaired; proposed and applied effects remain separate observations. |
| C7 available but unfit | Both support separate availability, failed fitness, acceptance and publication. | Bounded behavior supported. |
| C8 direct repair | Both support simple work and host behavior. They disagree about proposal-time effects. Negative-total behavior changed outside declared examples. | Required examples supported; broader behavior and coordinate fidelity remain unaccepted. |
| D1 dependent rename | Both retain the old-name oracle failure. Grader 1 also gives a guard/consumer counterexample. | Separate trial-contract defect and actual implementation defect; see below. |

The first grader's later-host-state argument does not retroactively falsify an
earlier, explicitly bounded observation. Conversely, a proposal-time state
cannot be reused as current after host application. The proposals and host
executions establish those boundaries; they do not justify silently normalising
every raw actor result into a conforming core record. Result-field fidelity
remains a qualification limit, especially where an actor does not state the
procedure or observation boundary precisely.

Graders read selected source excerpts. Narrative reports for C4–C7 and some
cited clauses were omitted from their bounded packets; complete records remain
beside the runs. Grading does not assess omitted prose, all citations, the
complete corpus, or real remote systems.

## D1: trial contract and genuine bug

The original task says to rename the declaration and keep dependents working.
Its hidden oracle additionally requires every exact occurrence of the old name
to disappear. The [task/oracle assessment](runs/d1-oracle-validity/RESULT.md)
finds that hard-cut policy is not entailed. The host's exact-byte-replacement
check is also stronger than the ban on unrelated changes. The original two
unmet checks remain recorded. They do not alone prove a method defect.

That assessment's broader reassurance about the fallback does not dispose of
the separate guard/consumer bug. With `APP_API_TOKEN` empty and `APP_TOKEN=x`,
the proposed shell guard returns `ok` while Python obtains an empty token.
Both outcomes were reproduced in [GUARD_COUNTEREXAMPLE.json](use-d1-hard-cut/GUARD_COUNTEREXAMPLE.json).
This is a real divergence introduced by the actor's speculative fallback,
regardless of the unsupported hard-cut oracle. It exposes a limitation in the
actor's dependency analysis and the original positive examples.

A labelled successor fixes the task contract before executing a new actor:
remove the old exact name from all files, including aliases and historical
notes, and retain `APP_TOKEN_TTL`. The original workspace, oracle checks and
forbidden conditions remain. Its [oracle](use-d1-hard-cut/ORACLE.json) records
the original oracle digest and the correction.

The new actor used source `9bc8962`, proposed exactly four replacements, and
made no claim to have executed them. The host applied those proposals without
repair. [Eleven checks and six executions pass](use-d1-hard-cut/APPLICATION_REPORT.json).
The extra counterexample now fails the shell guard as required. The actor took
28.119 seconds and provider-reported USD 0.2048708. This successful successor
neither erases the failed original experiment nor proves that another actor
will never introduce a speculative fallback.

## Evidence applicability and unresolved work

The ten `77f2efb` returns retain that source. Later changes update compact
acquisition, clarify unrequested possible effects observed absent, admit
contrary currentness observations through ODD's owning path, and replace a
duplicated part-classification rule with its owner reference. These fixtures
do not execute those new deciding branches. Their host observations remain
applicable to the same fixture predicates, but are not ten new runs against
`9bc8962`. The final effect-owner review and bounded a_c checks assess their
own selected later-source conditions separately.

The ordinary-entry experiment remains separately bounded:
[source entry with rc.2 assistance](entry/bound/RETURN.md). It demonstrates
actual continuation over partial files, but the fixture selects installed rc.2.
It cannot establish ordinary installed-v3 use, or better performance than rc.2.

Further qualification should test precise result records, discovery and cold
continuation through a truthfully selected immutable v3 installation. It must
use the unchanged installed candidate, not relabel these source experiments.
No additional rule, compulsory role arrangement or compulsory event replay
follows from the actor mistakes found here.
