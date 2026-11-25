# The method's graph

**Family**: REQ-METHOD-*
**Status**: Active
**Category**: Capability

These requirements cover the graph the product comes with: the method's own
work expressed as a graph.

### REQ-METHOD-001 The product comes with the method's graph

The product comes with one graph for software work under the method. It covers
the method's order: from a ticket, through the intent, the product definition,
the requirements and the design, to tests, code that passes them and the
user's acceptance. The design, the tests and the code are built in a build
tenant, as the definition file declares. Each vector declares the frame of
its working session and, where it has an evaluation, of its evaluating
session (REQ-GRAPH-002).

Acceptance:

- Set-up puts this graph in place for a governed product without the user
  writing a graph.
- Every vector of the graph declares the frame of each of its sessions.

From: product definition, "Product boundary"; intent, purpose.

### REQ-METHOD-002 The first vector for a ticket inducts it

The method's graph declares the first vector for a ticket (REQ-FLOW-004). Its
session inducts the ticket: it adds to the ticket the method's triage of the
change and the term that carries the work out (REQ-METHOD-006). The triage
gives the change's kind, its class, the node at which the work enters, which
is the method's re-entry point and the highest asset the change reaches, the
node at which it ends, and how much of the system it touches. The frame of
the session names the file and the section of the method release that state
the kinds of ticket, the classes of change and the triage.

Acceptance:

- After the first step for a ticket, the ticket holds each of the five and
  the term.
- The file and the section the frame names for the kind, the class and the
  triage are there in the method release the product selects.

From: product definition, the term "Ticket"; intent, purpose, "specification,
ticketing, design and outcome-driven development".

### REQ-METHOD-003 What is wanted is agreed before it is designed

Each graph function that writes the intent, the product definition or the
requirements ends in a decision by the user: once for the three, where one
writes them all, or once for each. No graph function that writes a design runs
before the user has accepted the requirements as they stand.

Acceptance:

- On a built product whose requirements changed after the user accepted
  them, a term that enters at the design or at the tests does not compose,
  and says to enter at the requirements; with no ticket, the requirements are
  asked for again before the design.
- A ticket whose term names the intent, the product definition and the
  requirements one by one waits for the user at each of the three.
- In scenario S1, where no vector fails and the user says yes each time, the
  user is asked three times: to confirm the ticket, to accept the
  specification and to accept the built product.

From: intent, purpose, "what is wanted is written down and agreed before it is
designed, and designed before it is built"; product definition, "Ask".

### REQ-METHOD-004 The author of an asset is never its only judge

The tests are written from the accepted requirements, and exercise the product
from end to end, as a user of it would. The design, the tests and the built
product are each judged against the accepted requirements by an evaluation,
which did not write them. The user accepts the built product against the
requirements. The tests depend on the requirements alone, and the code on the
requirements, the design and the tests (REQ-GRAPH-003). So where the tests are
written by a graph function of their own, it runs before the one that writes
the code, and the tests are evaluated before the code is written. Where one
graph function writes the design, the tests and the code, one evaluation
judges the three (REQ-METHOD-006).

Acceptance:

- In a term that names the tests and the code each on its own, the vector
  that writes the code does not run before the tests exist and have been
  evaluated.
- The vector that writes the tests rests on the requirements alone: neither
  the design nor the code is among what it rests on.
- A run does not end as done before the user's last decision is recorded.

From: product definition, the term "Evaluation"; intent, purpose, "have an LLM
agent build it reliably".

### REQ-METHOD-005 Nothing is orphaned

Every requirement is named in the design, in at least one test and in the code
that carries it out, or is marked as deferred in the requirements the user
accepted. Nothing in the design, the tests or the code names a requirement that
is not there. Checks establish both.

The design, the tests or the code may hold another product's data, such as the
requirements of a sample product that a test builds. The names of that
product's requirements are no part of the tracing. A check that traces names
leaves out every name of a requirement family that the graph declares, for
that check, to be another product's. A check that so declares a family the
requirements have cannot be run.

Acceptance:

- A requirement with no test leaves the vector that writes the tests open.
- Code that names a requirement which does not exist leaves the vector that
  writes the code open.
- The tests name requirements of another product, of a family that the check
  of the tests declares to be another product's. Those names do not make that
  check say no. Without the declaration, they leave the vector that writes
  the tests open.
- A check that declares a family the requirements have to be another
  product's cannot be run.

From: product definition, "Build", "until the two agree"; the method's rule
that requirements are traced into the design, the tests and the code.

### REQ-METHOD-006 Induction chooses the graph functions

Induction is the first step for a ticket (REQ-METHOD-002). From its triage it
chooses the graph functions of the registry that carry the work out, in
proportion to the work, and writes them on the ticket as one term
(REQ-GRAPH-001): a reference to an entry of the registry, or a sequence of
such references, in the order the work is done. The registry gives, for each
entry, the nodes it writes and when it fits (REQ-GRAPH-005).

Beside the six graph functions that each write one asset, the method's
registry holds two that each write three:

1. **The specification.** It writes the intent, the product definition and
   the requirements, and rests on the ticket alone: one working session
   writes all three. The user's one decision follows (REQ-METHOD-003). There
   is no evaluation.
2. **The build.** It writes the design, the tests and the code, and rests on
   the requirements: one working session writes all three. The checks of all
   three run on what it leaves. One evaluating session, which did not write them,
   judges the three against the requirements, with one verdict. The user's
   decision on the built product follows.

When each fits is stated here once, and each entry's purpose in the registry
says it. The two fit work whose whole specification, and whose whole build, a
person accepts at once: a new product of a few commands is the specification
and then the build, and a change to one that enters at the requirements is the
requirements and then the build. The six fit work too large for one decision,
and a change to one asset alone, such as a fault in the code, which is the
code alone. An induction entry fits a later stretch whose right grain cannot
be judged until the assets before it are accepted. Small work never needs one.

Each name of a term is in the registry and is carried out by one vector of the
governing graph, or names a term that is. A name of the first vector's own
graph function is an induction entry: it names its stretch, the node it enters
at and the node it ends at, and writes the work of that stretch, which is
smaller than the work it lies in. It is never a term's first entry. No other
name names a stretch.

The work from one node to another is the two nodes and every node that
depends on the first and on which the second depends (REQ-GRAPH-003). The
work of a ticket runs from the node at which it enters to the node at which
it ends. Entries compose by the nodes they write and rest on (REQ-GRAPH-005).
A sequence of entries composes exactly when each node an entry rests on is
written by an entry before it, or else is accepted on the workspace as it is
(REQ-ALG-004) and written by no entry of the sequence, and no node is written
twice. The empty term composes, and writes nothing. A ticket's term is well
formed exactly when:

1. it composes;
2. it writes exactly the work of the ticket;
3. the vector of its first entry declares an evaluation or a decision
   (REQ-FLOW-004).

Where every node the set rests on and none of it writes is accepted, of the
orders of one set of entries exactly those compose in which each entry comes
after the entries that write what it rests on. Proportion is a choice among
terms that write the same work: of those, the one in proportion to the work
is chosen. Fine and coarse entries may be mixed, as the requirements and then
the build. The framework reads the term through the graph language's
constructors and checks it, beside the first vector's own checks. A term that
is not well formed is a no, with what was found: an entry and a node it rests
on that is neither accepted nor written before it; a node written twice; a
node of the work no entry writes; or a node an entry writes outside the work.
Where the node is not accepted, the finding names the first node, through
those it depends on, that is not accepted, and where to enter: the nearest
node on which both that node and the work depend, at which a term can begin,
or, where there is none, that a run with no ticket accepts that node first.

A run carries out the term in force: the vectors it names take part, in its
order, and no other (REQ-ALG-006). The term in force is the confirmed term. A
ticket that carries none that reads, the simplest ticket and main take the
method's default term, which the registry declares (REQ-GRAPH-005): the six
graph functions that each write one asset, each after those that write what
it rests on. The simplest ticket is not inducted.

Acceptance is of a node, whoever wrote it (REQ-ALG-004): a product built by
the specification and then the build is done on main under the six, and one
built by the six is done under the two.

What the build gives up: the session that writes the code also writes the
tests, so the tests are not judged before the code is written against them.
The one evaluation therefore judges, among its grounds, whether the tests
exercise the product as a user would and were not bent to fit the code.

The run reaches an induction entry where the user's confirmation of the term
stands and the vector of every entry before it passes. The first vector then
runs again, bound to the stretch: its one session writes, in the entry's
place, a term for the work from the node the stretch enters at to the node it
ends at. That term writes what the entry writes, so the ticket's term still
composes. The session changes nothing else of the ticket. The framework
checks that the ticket's term is the confirmed term with that entry alone
replaced, that every other line but the framework's part is as the user
confirmed it, and that the term in its place is well formed as the work of
the stretch; the session's packet and each finding name the ticket as the
user confirmed it, by the commit the user's confirmation names. By the same
rule, that term may hold an induction entry only over a stretch strictly
smaller than the one it fills. The user confirms the new term as they confirm
the induction, by a resolution in the ticket (REQ-FLOW-004), and it is then
the term in force. What a confirmation stands for is in REQ-ALG-004.

A term that turns out wrong goes back when the user says no to the induction,
or edits the ticket: the ticket is then inducted again (REQ-FLOW-004). The
user's change, an edit of the term alone included, binds no stretch. A no to
the term written in an induction entry's place inducts the whole ticket again.

Acceptance:

- In scenario S1, where no vector fails and the user says yes each time, the
  term is the specification and then the build, and four sessions are
  started: the induction, the specification, the build and its evaluation.
  Every check of the design, the tests and the code passes, and a run started
  after the merge is refused, with nothing to build.
- A term of the six, one by one, starts one session on each and none on the
  specification or the build.
- A term that ends at the specification starts no session after it. The
  ticket is done, and the next run builds what is missing.
- The evaluation of the build says no: the next working session on the build
  is told where the findings are.
- A term of the design and then the code, entering at the design, starts no
  session on the specification or the tests.
- The user edits the ticket's term: the next run asks the user to confirm the
  induction again, and the run after it works by the new term.
- A term that does not write the node at which the work enters is not well
  formed: the induction does not close, and the run stops on it, saying why.
- A term with a gap, as the requirements and then the code, one against the
  edges, as the code and then the tests, and one that writes past where the
  work ends, as the specification and the build ending at the design, are not
  well formed, and each finding names the entry and the node.
- A term of the specification alone whose session leaves no requirements
  does not close, and the ticket is not merged.
- Both packets of the build name the design, the tests and the code and every
  check of them. The working one lets its session write all three,
  and the evaluating one names, among the results, the ground on the tests
  above.
- A term of the intent and the product definition one by one, and then an
  induction entry from the requirements to the code, is built to the merge.
  When the run reaches the entry, its session chooses the requirements and
  then the build, the user confirms the term with the entry so replaced, and
  seven sessions are started: the induction, the two, the induction on the
  stretch, the requirements, the build and its evaluation.
- In an induction entry's place, a term that is not well formed as the work
  of the stretch, one that changes anything else of the confirmed term, and
  one that holds an induction entry over the same or a larger stretch are
  each a no, with what was found; so is a session that changes any other line
  of the ticket. The induction does not close, and the user is not asked.
- An induction entry that names no stretch, one over the whole work, one that
  is the term's first entry, and a stretch named on any other entry are not
  well formed.
- While the run waits at an induction entry, before or after its session,
  the user edits the ticket's term: the next run holds the edit as the
  user's, binds no stretch, and asks the user to confirm the induction of the
  whole ticket again, with no session where the term is well formed. Where it
  is not, the induction runs again on the whole ticket, and the question says
  so.
- A product built by the specification and then the build is done on main
  under the six, and one built by the six is done under the two.

From: product definition, "Ask", "at which node it enters the graph", and the
terms "Step" and "Registry"; the method's REFERENCE_FRAME standard, RF-017.
