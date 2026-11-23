# Reference-frame basis

Identity: `urn:stdo-builder:frame-basis:1`.
Scope: all work on the product whose definition is
`urn:stdo:product-definition:stdo-builder`.

## Method

Work follows the method release selected in the
[definition file](../stdo_builder.json). The method's default flow for software
work (`standards/SDLC_DEFAULTS.md`) is selected. The method's optional
arrangement of an Executive with workers and reviewers is not adopted: there is
no coordinating agent and no standing arrangement of workers and reviewers.

## How the product is specified and built

The requirements state the product's functions as algorithms and process
flows. Its scale, costs and limits are stated apart, as parameters.

The design chooses, for each algorithm and flow, a computational algorithm
from a prescribed set, and says why that choice meets the parameters. It
invents none where the set has one that fits.

The technology stack is bound last, in the build tenant's design. No
specification page names one.

A build is correct when it returns what each algorithm returns.

## Roles

| Role | Does | Does not |
|---|---|---|
| Product owner | Writes or approves every sentence of the intent and the product definition. Accepts requirements and designs. Decides each loan. Makes the human decisions a step calls for. | |
| Executive | Coordinates the work and answers to the product owner for its compliance: with the requirements, with the prescribed set of computational algorithms and with the layers of the design. Has a reviewer check compliance at the end of each phase, and takes back a verdict and the exceptions only. | Write or review the work itself. Accept on the product owner's behalf. |
| Writer | One at a time. Writes within the territory a task names, inside `builder/` only. | Change the intent or the product definition. Accept its own work. |
| Reviewer | Reads a finished piece of work that it did not write, at the end of a phase. States what it tested the meaning against. | Repair what it reviews. Stand in for the product owner's acceptance. |

## Review findings

A reviewer works as quality assurance under the method's review rules. For
each review that has findings it writes one bug report, in the commentary
folder, with one entry for each finding: an identity, a severity, the exact
thing reviewed, the claim it breaks, where, and evidence a reader can follow
to it. A review with no findings writes no report.

Severity is the reviewer's grade of the consequence, on the method's scale of
1, the highest, to 5:

| Severity | Consequence |
|---|---|
| 1 | Critical loss of the outcome, or of safety, authority or integrity |
| 2 | Major failure of essential behaviour, with no adequate way round it |
| 3 | Material but bounded. The reviewer states what depends on it |
| 4 | Limited and local, with a practical way round it |
| 5 | Minor |

The Executive then triages each finding: its priority, its owner and what is
done with it. It writes that into the ticket whose work was reviewed, as a
table of bug items. A finding of severity 1 or 2 thereby becomes part of that
ticket's delivery: the ticket is not done until the item is verified. The
reviewer's severity is never changed. An item is open,
then fixed, with the commit and a test that failed before the repair and
passes after it, then verified.

A fresh reviewer checks a repair again only where the repair touches a guard
rail, has no such test, or the first review left part of its subject
unread. Otherwise the test verifies it.

This is a rule against churn. The Executive keeps the steel thread moving:
the thinnest build that carries scenario S1 from end to end, and then each
scenario after it. A finding stops that work only where it is a hard stop, is
of severity 1 or 2, or breaks the steel thread. Every other finding goes into
the same table and is repaired in a batch at the end of the phase, or put off
with a reason. A finding of severity 3 to 5 opens no new round of review.

A break of one of the intent's guard rails is a hard stop: no priority waives
it. A phase does not close with an item of severity 1 or 2 open.

The reviewer hands back to the Executive its verdict, the count of findings at
each severity, and the entries of severity 1 and 2. The rest is in the report.

## Acceptance

A specification page is accepted only by the product owner's own statement. A
review is advice to the product owner. A check of form is reported as a check
of form.

A request to plan or to close work gives no licence to change the goals, the
intent or the product definition. A writer who finds that a task needs such a
change says so first and stops.

## Progress and weight

Progress is stated as what a user can now do with the installed product, by
scenario. A count of tests, tickets, commits or reviews is not progress.

One ticket is in work at a time, on one line of the repository.

A rule, a role or a record is added to this page only with what it protects and
what it costs. One that no longer protects anything is removed.

Nothing from a scenario's sample product enters the intent, the product
definition or the requirements.

## Work records

Tickets are kept under `.ai-workspace/tickets/` and commentary under
`.ai-workspace/comments/<author>/`. Commentary is not law.

## Not yet covered

Release, installation and qualification of the product have no frame yet. They
are added when the first build is done.

## What makes this page stale

A change to the intent, to the product definition or to the selected method
release. The page is then read again against them before further work.
