# The product's functions, as algorithms

**Family**: REQ-ALG-*
**Status**: Active
**Category**: Capability

Each requirement here is one function of the product, stated as an algorithm:
named inputs, and the output they determine. Three laws hold for every one:

- The same inputs give the same output.
- It calls no language model.
- It reads nothing but its inputs. "Workspace" as an input means the workspace
  as it is now: for work on a ticket, the workspace as the ticket's checkout
  holds it (REQ-FLOW-004). Main and a branch, as inputs, are their files under
  the workspace's folder, so main that has moved only outside the folder is
  the same input (REQ-FLOW-001). Only `stands` reads the event log.

A person working by hand from the same inputs reaches the same output. That is
the test of each (REQ-VERIFY-004). The [flows](FLOWS.md) say when each is used.

### REQ-ALG-001 `identity : {asset, workspace} → content identity`

The identity git gives to the asset's content: of a file, or of a folder and
all it holds. Files that git is set to ignore are no part of an asset. Only
files under the workspace's folder are part of one, each at its place from
that folder, as the graph and the definition file name places (REQ-FLOW-001).

Laws:

- Two contents have the same identity only when they are the same.
- An identity is used to notice a change and for nothing else. No copy of the
  content is kept to compute or compare it.

Acceptance:

- A file changed by one byte has another identity. Changed back, it has the
  first again.
- Inside a larger repository, files outside the workspace's folder are
  changed, among them one at an asset's place from the repository's top: no
  asset's identity changes.

From: product definition, the term "Content identity"; intent, guard rail 5;
the user, in ticket 261123-001543-eae1.

### REQ-ALG-002 `well_formed : {graph, registry} → yes, or the reasons`

Yes when all of these hold: every node a node depends on is declared, and no
node depends on itself, directly or through other nodes (REQ-GRAPH-003);
every vector carries out an entry of the registry and writes the nodes that
entry writes; the first vector writes none, and every other writes at least
one and no given one; a vector declares an evaluation, or a decision, only
where a node it writes is accepted by one, and a vector of the governing graph
declares each that a node it writes is accepted by (REQ-GRAPH-003); the
vectors of an inner workflow compose from what the vector holding it rests on
and write exactly what it writes; no two nodes, no two vectors and no two
checks of the graph, inner workflows included, have the same name; no asset's place lies inside
another's (REQ-GRAPH-003); every check says what runs it; every graph
function named is in the registry, each entry writes nodes of the graph, and
the definition of each entry no vector carries out names only entries of the
registry, composes from what the entry rests on and writes exactly what it
writes (REQ-GRAPH-005); every term is one the graph language has
(REQ-GRAPH-001); the registry's default term, or where it declares none the
vectors of the graph but the first, each after those that write what it
rests on, denotes vectors of the graph and composes (REQ-METHOD-006); and at
most one vector is the first vector for a ticket.

Laws:

- A graph that is not well formed is never traversed.

Acceptance:

- A graph that fails any one of these is refused, with the reason, before a
  step runs.

From: intent, guard rail 1.

### REQ-ALG-004 `passes : {vector, workspace} → yes, no, or cannot be run; with what was found`

Runs the checks of the nodes the vector writes on the workspace, or for the
first vector the ticket's. Yes only when every one passes, the
records at the nodes it writes stand, each node it writes is
there and each node it rests on is accepted. A verdict that says the
evaluation cannot judge gives cannot in the step that read it, and is no
resolution (REQ-FLOW-005).

A node is accepted where it is there, its records stand, its checks say yes,
and every node it depends on is accepted. Its records are the last resolution
at it of an evaluation, where an evaluation accepts it, and of the user, where
the user's yes does (REQ-GRAPH-003); each must say yes. The resolutions of a
vector are at each node it writes that they accept; so, for a vector of the
governing graph, yes means that every node it writes is accepted. The last
resolution of each kind at a node is read from the branch's ticket; where it
holds none of that kind there, from the done ticket merged last that holds
one.

Laws:

- No session's own report is a check.
- A check may read a resolution of an evaluation, or of the user. Each stands
  only for the content identities it was given on, which git gives under the
  commit it names: those of the node it is recorded at, of what that node
  declares (REQ-GRAPH-003) and of the nodes it depends on and, at the node a
  ticket enters at, of the branch's ticket without its term and without the
  framework's part, so neither a new term nor a line the framework adds
  reopens it. The user's confirmation of the induction stands for the ticket
  without the framework's part, and for what the first vector declares of it.
  On changed content, or where git does not hold the commit, it counts as
  absent.
- A check gives the same result on the same content. Its result may be used
  again for exactly the content it reads, and for no other.
- Who or what wrote an asset makes no difference: a resolution at a node
  accepts it, whichever vector or ticket wrote it.
- A node's checks are run only where their answer can change what the
  framework does next: where the node is there, its records stand or the step
  is on a vector that writes it, and every node it depends on is accepted or
  written by that vector. The ticket's are run where the user's confirmation
  stands or the step is on the first vector. A check not run says neither yes
  nor no.

Acceptance:

- A session that reports success without producing the asset: no.
- An asset the user wrote by hand is judged as one a session wrote.
- The user says no to the intent, and no content changes: no vector that
  writes a node depending on the intent passes.
- After a ticket is done, a new ticket that changes the code alone finds the
  intent, the product definition, the requirements, the design and the tests
  accepted by the resolutions of the done tickets.
- The user says yes to the requirements in one ticket, and no to the same
  content in the next: the requirements are not accepted.
- A resolution whose commit git no longer holds counts as absent, and the
  user is asked again.

From: product definition, the terms "Check", "Evaluation" and "Ticket", and
"The framework's own work for a step is small and does not grow with the
history of the work"; intent, guard rail 3.

### REQ-ALG-005 `open : {vector, workspace} → yes or no`

A vector is open when `passes` does not say yes for it on the workspace as it
is now. Otherwise it is closed.

`changed` is the set of nodes the vector rests on, with the branch's ticket
without its term and without the framework's part at the node the ticket
enters at, whose content identity differs from the one under the commit of
the last resolution of the vector's evaluation at a node it is recorded at,
or of the user's where the vector declares no evaluation. Where it has
neither yet, `changed` is empty.

Laws:

- No record makes a vector closed. Only the checks of the assets it writes do.
  The ticket's checklist plays no part.
- A changed asset opens the vector: its resolutions no longer stand
  (REQ-ALG-004).
- The event log plays no part. A ticket that is done plays a part only by the
  resolutions it holds.

Acceptance:

- After a requirement of a built product is changed, the vectors that depend
  on it are open, without the framework being told what changed.
- In a checkout just opened from main, every vector closed on main is closed.

From: product definition, "A vector is closed when the checks of the assets it
writes pass against the workspace as it is now" and "Change"; intent, guard
rail 3.

### REQ-ALG-006 `next : {graph, workspace} → one vector, or none`

The vectors that take part in the work on a ticket are the first vector for a
ticket and the vectors the term in force names: the ticket's term, or, where
there is none to read, for the simplest ticket and on main, the method's
default term (REQ-METHOD-006).

`next` is the first of the vectors that take part, in the order of the term
in force, that is open; within an inner workflow, in an order in which each
vector comes after those that write what it rests on.

The first vector for a ticket (REQ-FLOW-004) writes no node: it adds to the
branch's ticket what the graph declares. While it is
open it is `next`, before any other vector. It takes no part for the simplest
ticket.

Laws:

- No session chooses the next vector.
- The framework takes no step the graph does not allow.

Acceptance:

- For a ticket confirmed at the code with the code alone as its term, on a
  built product, `next` never returns a vector that writes the intent, the
  product definition, the requirements or the design.
- For a ticket confirmed at the design with the design and then the code as
  its term, on a built product, `next` never returns a vector that writes the
  intent, the product definition, the requirements or the tests.

From: intent, guard rail 1 and outcome 2; intent, model, "The graph fixes where
the agent can be in the work and where it can go next."

### REQ-ALG-007 `brief : {vector, kind of session, workspace, method release} → references`

What a session is given for a step: the activation packet of the reference
frame the vector declares for that kind of session (REQ-GRAPH-002). It holds
the minimum that section 11 of the method's REFERENCE_FRAME standard sets. The
method release is given by the exact identity the definition file selects,
and, where the frame names terms of the method, by the path where the method
keeps it installed. The brief is sufficient: a session needs to read nothing
of the framework, of the graph or of the method outside the sections it names
to do its work. It holds:

- **The frame and its closed result.** The frame's name and revision. For a
  working session: the asset to produce, and that the checks judge what it
  leaves there. For an evaluating session: the asset to judge, the assets to
  judge it against, where its findings are written, the exact content of its
  verdict, and what each verdict means. Yes: the asset is what the graph
  declares it must be. No: the asset is written again, with the findings as
  the reason. Cannot: the session could not judge, the findings say why, and
  the run stops for the user. For both, but for inducting the ticket, whose
  session chooses the work: that the asset holds what the ticket's work needs
  and no part the ticket does not ask for, and that such a part is a ground
  for no; for the working session, also that every line the ticket's work and
  the findings do not require is left as it stands, and that where its work
  removes or renames a file, a command, a record or a term, no file it may
  write still mentions it as it was, and what it prints names each file of an
  asset it may not write that does, which is left for that asset's step; for
  the evaluating session, also that a line changed since the content last
  accepted, as main holds it (below), that the ticket's work and the findings do not require is
  a ground for no, and that the findings name each such line by its path and
  line and copy none of it.
- **The subject and the basis.** The asset's place; the branch's ticket, as
  the context the session starts from, and that the rulings in it bind the
  session; the definition file and the method release. For each term of the method that
  the frame names, the file and the section of the release that state it.
  Where the frame names terms and the release is not found on this machine,
  the brief says so, names it by its identity alone, and says that the session
  judges by the brief alone.
- **The attention surface.** What the graph declares must be true of the
  asset, and the asset as it stands: for each node the session writes or
  judges, whether it is there; what the last resolutions at it of the
  evaluation and of the user said (REQ-ALG-004), the ticket that holds each
  and the commit it names, with where the findings of a no are kept and, for
  the user's no, that its reason is in that ticket; and each identity under
  that commit that differs now, with the command that reads git's content
  under the old one. For an evaluating session, also, at each node it
  judges, the content last accepted as main holds it, with what the user
  changed there by hand, and the command that gives the lines the branch
  changed from it; or, where main holds none of the node, that every line of
  it is judged as the ticket's work. The work is the gap between the asset
  as it stands and what is required of it, against what it rests on as it now
  is: with nothing there, all of it; after a no, what was found; after a change
  to what an accepted asset rests on, what the change requires, which may be
  nothing. The places of the assets needed or judged against, and where what
  the checks last found is kept. For inducting a ticket, each entry of the registry its term may name,
  the induction's own among them, with the nodes it writes, what it rests on
  and its purpose; and where the run has reached an induction entry, its stretch,
  that the term written is the confirmed one with that entry alone replaced,
  and the commit that holds the ticket as the user confirmed it. For an asset that collided (REQ-ALG-013): the commit that holds main's
  content of it, the commit that holds the branch's, and the tickets on each
  side.
- **The checks, each in its exact form:** those of the assets the vector
  writes, and those of other assets that run or read them. For `command`, the
  command line as it is run, and the folder it is run in. For
  `ticket_field`, the field, that it is read from a line `- field: value`, and
  the value it must have or must not have, where the graph gives one. For
  `ticket_kept`, what is compared. For `traced`, the pattern, the places it
  reads from and into, the word that marks a requirement as deferred, and the
  families of another product. For the first vector's working session, also
  that the ticket's term composes (REQ-METHOD-006).
- **The authority and the territory.** What the session may write: a working
  session its asset and the workspace's own `.gitignore`. The protected
  files and the protected part of the ticket, which it must not change
  (REQ-ALG-008). For a working session, that
  the framework commits every file git does not ignore, so what a build
  leaves that is no part of the product is listed in that `.gitignore`. For
  an evaluating session, that it may run commands, and that what a run leaves
  that git does not ignore counts as a change. Whether the user decides on
  the asset.
- **The exclusions.** The session reads nothing of the framework: its
  installation, the graph, the registry, the settings and the event log. Of
  the method it reads only the sections the brief names; where the brief
  names none, nothing. The event log is no evidence.
- **The stop conditions.** The attempts and the time the graph allows, and
  the limits the settings set on a run. A working session whose work needs a
  change it may not make says in what it prints what change and why, and
  stops without writing its asset. An evaluating session that cannot judge
  says so in its verdict.

Laws:

- Everything is given by name, by path or by the identity git holds it under.
  A brief holds no line of an asset. What it takes from the graph, such as a
  check's form, is the graph's and not an asset's.
- Of tickets, it names only the branch's own, a done ticket that holds a
  resolution it names, and those of a collision.
- It names the ticket and its rulings, and copies no line of either.
- A brief says nothing on how the session is to do its work.
- Its size is bounded (REQ-PARAM-001), whatever the size of the assets, the
  length of the ticket or of the event log, or the number of earlier steps.

Acceptance:

- Every brief of scenario S1 after the induction, for a working and for an
  evaluating session, says the asset holds what the ticket's work needs and
  no part the ticket does not ask for, and that such a part is a ground for
  no. The brief for inducting the ticket does not: its session chooses the
  work.
- Every working brief of scenario S1 after the induction says that every line
  the ticket's work and the findings do not require is left as it stands, and
  what must hold where the work removes or renames a file, a command, a
  record or a term.
- In scenario S1, the evaluating brief on the code says that main holds none
  of the code. After S1, under a ticket that changes the code, it gives the
  command that shows the lines the branch changed in the code from main, and
  says that a line changed that the ticket's work and the findings do not
  require is a ground for no, which the findings name by its path and line.
  A line the user changed by hand on main is not among those lines.
- The brief for the code step of scenario S1 holds no line of any asset. After
  ten more tickets are done, the brief for the same step is no longer.
- Every brief of scenario S1 holds each part listed above. Every working
  brief holds each check of the assets its vector writes in its exact form.
- The brief for inducting a ticket names, for the ticket's kind, its class and
  the triage, the file and the section of the method release that state them.
  It lists each entry of the registry the term may name, with the nodes it
  writes, what it rests on and when it fits, and gives the check of the term
  in its form, with the nodes each node depends on. Where the run has reached
  an induction entry, it names the stretch.
- The brief is sufficient. After the evaluation of the code says no, the
  brief for the code names where its findings are. The brief for the tests
  gives the command the code's check runs them by, and the folder it is run
  in.
- Every brief states its gap in one form. On an empty workspace, a working
  brief says its asset is not there and nothing is recorded at it, and an
  evaluating brief that nothing is recorded at it; after a no, a brief names
  where the findings or the reason are kept.
- After the accepted product definition of a built product is changed by
  hand, the working brief for the requirements says the user accepted them
  and names the identity the product definition had then, with a command that
  reads it. Where that session leaves the requirements as they were, no
  session is started on the design, the tests or the code. After the
  requirements are reworded, the evaluating brief for the design names what
  they were in the same way.
- Every brief names the branch's ticket as the context its session starts
  from. After the user gives a ruling with an answer, every later brief on
  the ticket says that the rulings in the ticket bind its session.

From: product definition, "Change" and the term "Ticket"; intent, guard rails
5 and 7; the method's REFERENCE_FRAME standard, section 11; the user, in
ticket 261123-100659-a0d5.

### REQ-ALG-008 `trespass : {vector, kind of session, graph, workspace at the start, workspace at the return} → files`

The protected files for a working session are: the files of every asset the
vector does not write; every ticket that was
there at the start, but for the first vector's session the branch's ticket,
of which only the framework's part is protected; the definition file, the
settings file, the governing graph, the registry, every verdict, and the
framework's own files (REQ-FLOW-001). For an evaluating session the asset it judges is
protected too, and the places for its findings and verdict are not. `trespass`
returns the protected files whose identity differs between the start and the
return, and the branch's ticket where its protected part differs.

Laws:

- A file in a place that neither the graph nor the definition file names is
  never returned.
- What a session does with git is its own affair. Only the content of the
  protected files at its return counts.
- A change made by hand during the session is returned as well: the framework
  cannot tell who made it.
- `trespass` reads the files of the workspace at the return, and nothing of
  git's own. It is a check on an agent that strays, and the framework is not
  hardened against an agent that sets out to get round it. It puts nothing
  right. The next session works in its checkout as it finds it and carries on
  with its task.

Acceptance:

- Scenario S7 ends as it should.
- A working session on a vector that writes three nodes changes each of
  them: nothing is returned. A working session on a vector that writes one of
  them and changes another: that one is returned.
- The first vector's session changes the triage and the term: nothing is
  returned. It changes a resolution: the ticket is returned.

From: product definition, "neither writes the other's"; intent, guard rail 7
and outcome 2.

### REQ-ALG-009 `progress : {what the checks found after the last working session of the attempt, what they find after this one} → yes or no`

Yes when fewer checks fail now than failed before. The first working session
of an attempt counts as progress.

Acceptance:

- Three checks failed, then two: yes. The same two again: no.
- The first working session after an evaluation says no: yes.

From: product definition, the term "Step"; intent, guard rail 1; the user, in
ticket 261123-100659-a0d5.

### REQ-ALG-010 `take_up : {board, tickets a run holds, the ticket the user names, graph, main} → a ticket, the simplest ticket, or none`

The board is the three ticket lanes as main has them: backlog, active and
done. In order:

1. an active ticket that no run holds, the first by name;
2. where fewer tickets are active than the limit the user set
   (REQ-PARAM-001), the first ticket in the backlog by name;
3. where no ticket is active and `done` says no on main, the simplest ticket:
   build the workspace to the specification as it stands;
4. none.

Where the user names a ticket, it is that ticket under the same conditions, or
none.

Laws:

- Work begun is taken up before new work.
- The lane a ticket lies in is never proof of anything about what is built.

Acceptance:

- With the limit at one, a second ticket waits and is built after the first.
- No ticket waits, and a file that is part of no asset is changed by hand so
  that a test fails. The run writes the simplest ticket and works under it.
- Inside a larger repository, no ticket waits and `done` says yes on main. A
  file outside the workspace's folder is changed and committed on main:
  `take_up` gives none.

From: product definition, "Ask" and the term "Ticket"; the user, in ticket
261123-001543-eae1.

### REQ-ALG-011 `done : {graph, workspace} → yes, or the vectors and checks that say no`

Yes when `passes` is yes for every vector that takes part (REQ-ALG-006), on
the workspace as it then is.

Laws:

- A run reports the work done on this and on nothing else.

Acceptance:

- A file that is part of no asset is changed so that a test fails. `done` says
  no.

From: intent, guard rail 3 and outcome 3.

### REQ-ALG-012 `stands : {graph, board, workspace, event log} → where the work stands`

In the graph's own names:

- For each ticket on the board, its lane, and for an active one what it waits
  on, the first of these that holds: the user's answer, and to what; to be
  inducted; held up, with the vector, the checks that said no and where what
  they found is kept; in build, with the vector of the last step; to be
  merged. The first two are read from the ticket: a vector's work that its
  checklist shows delivered for the user's decision, with no answer of the
  user after it, and whether a confirmation in it stands (REQ-ALG-004). The
  rest are read from the event log: how the last run on the ticket ended, and
  its last step. It says which it read each from, with when that was written,
  and that a run reads the workspace again.
- A ticket that has a branch and is not on the board: withdrawn.
- For a ticket, active or done: every asset it changed and how many lines of
  each. For an active ticket that is the difference between main and its
  branch; for a done one, what its merge brought to main.
- From the event log: how the last run on each ticket ended and why, the
  sessions and attempts so far, how long each took, and the cost and the
  calls the agent reported for each, with their sums for the ticket. A cost
  reported as a number, and the ticket's sum of such costs, is given with two
  places after the decimal point, rounded to the nearest, then its unit where
  one is named: `0.65 USD`, or `0.65` where none is. The sum is of the costs as
  reported, not as given. It says that the calls, of each session and their
  sum for the ticket, are the agent's own report.

Laws:

- It starts no session and changes nothing in the workspace.
- It runs no check and keeps nothing. It works out what it gives, when asked,
  from the board, the tickets, git and the event log, and from no other
  record.
- Without an event log it gives what the board, the tickets and git give, and
  says the log was not found. For an active ticket that waits on neither the
  user's answer nor its induction, it then says that a run finds what it
  waits on.

Acceptance:

- A person who has not read the framework's source can say from it what is
  done, what is next and what is asked of them.
- After two tickets are done, it names for each the assets that ticket
  changed, and no others.
- For a ticket whose sessions reported their cost and their calls, it gives
  each session's, and their sums, and says that the calls and their sum are
  the agent's own report.
- A session that reported a cost of `0.6511950000000001` with the unit USD is
  given as `0.65 USD`; one that reported it with no unit, as `0.65`.
- Three sessions that each reported a cost of `0.334` with the unit USD are each
  given as `0.33 USD`, and the ticket's sum as `1.00 USD`.
- A run ends waiting for the user's answer on a vector, and the code in the
  ticket's checkout is then deleted: it still gives that the ticket waits for
  the user's answer on that vector, as the ticket shows, with when the
  question was asked.
- With the event log deleted, it gives what a ticket waiting for the user's
  answer is asked, from the ticket, and says the log was not found.
- Inside a larger repository, a file changed outside the workspace's folder,
  on main or on a ticket's branch, is named for no ticket and adds to no
  count of lines.

From: product definition, "Show" and "What happened is recovered from these
three"; intent, outcome 5; the user, in tickets 261122-232152-1198,
261123-001543-eae1 and 261123-021212-4e94.

### REQ-ALG-013 `collides : {branch, main, graph} → assets`

**Status**: Deferred, with REQ-FLOW-009.

The assets whose content changed on the branch since it last held all of main,
and also changed on main since then. Git gives both sets.

Laws:

- It says nothing on which side is right.

Acceptance:

- Two tickets that changed no asset in common: none.
- Two tickets that each changed the code: the code.

From: product definition, "Several tickets may be active at once".
