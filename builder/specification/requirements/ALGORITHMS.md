# The product's functions, as algorithms

**Family**: REQ-ALG-*
**Status**: Active
**Category**: Capability

Each requirement here is one function of the product, stated as an algorithm:
named inputs, and the output they determine. Three laws hold for every one:

- The same inputs give the same output.
- It calls no language model.
- It reads nothing but its inputs. "Workspace" as an input means the
  workspace's folder as it is now, on the ticket's branch for work on a
  ticket (REQ-FLOW-001). Main and a branch, as inputs, are their files under
  the workspace's folder, read from git by the commit each is on and the
  path, never from a folder; which branch is main, REQ-FLOW-001 says. A
  commit of main that changes only files outside the folder changes no
  input. Only `stands` reads the event log.

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
  absent. A resolution of the user also counts as absent where main, taken
  into the ticket's branch after the commit it names, changed a file of the
  node it is recorded at from the last commit of main that the named commit
  holds, whatever the file then holds on the branch.
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
- The user says yes at a node. Main, taken into the ticket's branch, then
  changes a file of that node, and a session writes the file back as it was
  at the yes: the yes counts as absent. Where main changed no file of the
  node, the yes stands.

From: product definition, the terms "Check", "Evaluation" and "Ticket", and
"The framework's own work for a step is small and does not grow with the
history of the work"; intent, guard rail 3; the user, in ticket
261124-091541-a64b.

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
- On a ticket's branch just made from main, every vector closed on main is
  closed.

From: product definition, "A vector is closed when the checks of the assets it
writes pass against the workspace as it is now" and "Change"; intent, guard
rail 3; the user, in ticket 261124-091541-a64b.

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
  it is judged as the ticket's work. Where the user's change by hand was
  committed on the ticket's branch (REQ-FLOW-003, step 1), it also names
  each commit that holds one, and says that the lines it changed are the
  user's and not the ticket's work. The work is the gap between the asset
  as it stands and what is required of it, against what it rests on as it now
  is: with nothing there, all of it; after a no, what was found; after a change
  to what an accepted asset rests on, what the change requires, which may be
  nothing. The places of the assets needed or judged against and, for a
  working session, where what the checks last found is kept. For inducting a ticket, each entry of the registry its term may name,
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
  session its asset and the workspace's own `.gitignore`, and the first
  vector's session also the triage and the term in the branch's ticket; an
  evaluating session its findings and its verdict, and nothing else. That
  anything else in the workspace that differs when the session is over is
  named to the user, who rules on it before
  anything of the step is judged or committed, and that an evaluating
  session's verdict is then not read (REQ-ALG-008). For a working session, that
  the framework commits every file git does not ignore, so what a build
  leaves that is no part of the product is listed in that `.gitignore`. For
  an evaluating session, that it may run commands, and that what a run leaves
  that git does not ignore counts as a change. For each session, that files
  git ignores in the folder may be the user's own, and that it removes of
  them only what its own work or its build made. For each session in a
  workspace inside a larger repository, in one sentence: that the folder
  lies inside a larger git repository, that the files outside the folder are
  the user's and no part of the step, and that a git command given without a
  path acts on the whole repository. Whether the user decides on the asset.
- **The exclusions.** The session reads nothing of the framework: its
  installation, the graph, the registry, the settings and the event log. Of
  the method it reads only the sections the brief names; where the brief
  names none, nothing. The event log is no evidence. For an evaluating
  session, the evidence is the assets its vector names and the assets they
  were made from; what a working session printed, the working packets and
  what the checks found are named, by their places, as not to be read.
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
  A line the user changed by hand on main is not among those lines. A line
  the user changed by hand in the folder while the ticket is active is in a
  commit the brief names as the user's.
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
- Every evaluating brief names as its evidence the assets its vector names
  and those they were made from, and names what a working session printed,
  the working packets and what the checks found, each by its place, as not
  to be read.
- Every brief says what its session may write, and that anything else that
  differs when the session is over is named to the user before anything of
  the step is judged or committed.
- Inside a larger repository, a working brief and an evaluating brief each
  hold the sentence on the larger repository that the authority and the
  territory give. At the top of a repository, neither holds it.

From: product definition, "Change" and the term "Ticket"; intent, guard rails
5 and 7; the method's REFERENCE_FRAME standard, section 11; the user, in
tickets 261123-100659-a0d5, 261124-001024-40f8, 261124-091541-a64b,
261124-220448-c7ab and 261125-043021-2fed.

### REQ-ALG-008 `trespass : {what the step writes, the identities taken at the session's start, the workspace as it is, main} → files, each added, changed or removed, those changed on main apart, and whether the identities were missing`

What a step writes is what its session's packet names it may write
(REQ-ALG-007): for a working session, the assets of its vector and the
workspace's own `.gitignore`, and for the first vector's session the part of
the branch's ticket that session writes; for an evaluating session, its
findings and its verdict, and nothing else.

When a session starts, the framework takes the content identity of every file
of the workspace that git does not ignore, as the workspace's folder holds
it, with what is not committed there. When the session is over
(REQ-FLOW-005), however it ended, `trespass` takes them again and compares
the two, path by path. It returns each file whose identity differs, outside
what the step writes, by its path in the workspace: added where it was not
there at the start, removed where it is not there now, and changed where it
is there both times. Of the branch's ticket it compares each part apart. What
the framework itself writes is not returned, a ticket the user writes with
the product's command among it.

It also returns, apart, each file of the workspace's folder that differs
between the commit main was on at the session's start and the commit main is
on now, by its path in the workspace: added where main holds it now and did
not then, removed where main held it then and does not now, and changed where
main holds it both times and not as it was. Main is the branch the ticket
left (REQ-FLOW-001). Git gives what differs from the two commits and the
paths, and no content is read. None of these counts as what the step writes,
whatever the file: the step's own work, committed on main, is returned too.

The framework keeps the identities taken at a session's start, with the name
of the commit the folder was on then and the name of the commit main was on
then, as the record of that start among its own files, in git's own
directory for the workspace's folder (REQ-FLOW-001),
as identities and never as content, from the session's
start until the result of its step is committed (REQ-FLOW-003, step 1, and
REQ-FLOW-005, step 7), or the next session of that step takes its own. Where
they are missing, cannot be read, name a step the graph does not hold or name
what git no longer holds, the identities of the commit the session started
from stand in their place, with nothing counted as what the step writes, and
are kept as that session's: so each file of the folder that differs from that
commit when the comparison is made, committed since or not committed, is
returned, and `trespass` says that the identities were missing. The run that
started the session knows that commit: it is the one it names in the event
`session started` (REQ-FLOW-007). A later run, or an answer, reads it from the
record kept at the session's start, where that record reads and git holds the
commit it names. Where neither holds, which is a later run or an answer where
that record is gone, cannot be read or names a commit git does not hold, the
identities of the commit the folder is on stand in, in the same way, and each
file not committed is returned: what a session committed of its own is then
not returned. That is an accepted limit. Where the
identities of a commit stand in, in either way, or the record names no commit
of main, as a record an earlier build wrote names none, the commit where the
ticket's branch and main last met stands in for the commit main was on at the
session's start: each file of the folder that main holds otherwise than that
commit is returned, apart. A yes of the user
on what changed (REQ-FLOW-006) counts for a file only where the ticket holds
the line of that ruling, naming the file with the identity it has now, and
the framework's own record agrees; for a file changed on main, the line names
it apart from a file of the folder (REQ-FLOW-004), with the identity main
gives it now.

Laws:

- It reads the workspace and main as they are now. The identities kept from
  a session's start say only what they were then. Where they are missing,
  the framework cannot tell what the session changed, so it asks: it never
  goes on without the user's ruling (REQ-FLOW-005).
- Only what differs when the session is over counts. What a session does and
  undoes inside its time, with git or without, is its own affair, and so are
  its own commits of its step's work on the ticket's branch. A commit on main
  is not: each file of the folder it changes is returned (above).
- The framework cannot tell who changed a file. A change the user makes while
  a session works, in the folder or by a commit on main, is returned as well,
  and named as REQ-FLOW-006 says.
- It freezes nothing and puts nothing back: the user may work in the folder
  while a session works.
- A file git ignores is not compared, the framework's own files among them.
  Nothing outside the repository is seen, and whether a session read a file
  cannot be known. It is a check on an agent that strays and on a run the
  user interrupts; the framework is not hardened against an agent that sets
  out to get round it.

Acceptance:

- Scenario S7 ends as it should.
- A working session on a vector that writes three nodes changes each of
  them: nothing is returned. A working session on a vector that writes one of
  them and changes another: that one is returned, as changed.
- The first vector's session changes the triage and the term: nothing is
  returned. It changes a resolution: the ticket is returned.
- A session adds a file in a place that neither the graph nor the definition
  file names, and removes another: the one is returned as added, the other as
  removed.
- While a session works, the user changes a file the step does not write: it
  is returned, by its path in the workspace, as changed.
- A session changes a file outside what its step writes and changes it back,
  or commits its own asset on the ticket's branch: nothing is returned.
- While a session works, the user writes a ticket with the product's command:
  it is not returned.
- The user says yes to what changed, and then takes the line of that ruling
  out of the ticket by hand: the yes does not count, and the file is returned
  again.
- A working session gives `git clean -fdx` in the workspace's folder as its
  first act, then sets the command of a check in the graph to `true`, adds a
  line to `AGENTS.md` and writes a file of its own outside every asset, and
  returns. The run asks for a ruling that names those three files and none of
  what the step writes, and commits nothing.
- The same, with `git clean -fdX` as the session's last act; and again with
  `git stash --all` as its first act, the stash never taken back.
- The same as the session that gives `git clean -fdx` as its first act, where
  the product is one folder of a larger repository and the cleaning is given
  at the repository's top.
- While a session works, the identities kept from its start are removed from
  where they lie, and the session returns. The run says that they are
  missing, puts every file not committed to the user and commits nothing.
  After the user's yes, they are committed with the step and the work goes
  on.
- An evaluating session changes a file its step does not write, commits what
  it changed in the workspace's folder, and gives `git gc --prune=now`. The
  run asks for a ruling that names the file, reads no verdict and commits
  nothing of the step.
- The same, with `git prune --expire=now` in place of the gc.
- The same, where the run is killed while that session works, after the
  session has committed and pruned: the next run asks, naming the file.
- A working session commits a file its step does not write, and the record
  of its start is then removed from git's own directory: the run that started
  it still asks, naming the file.
- A working session sets the command of a check in the graph to `true`, adds
  a line to `AGENTS.md` and writes a file of its own, commits the three on
  main, puts the folder back on the ticket's branch and returns. The run ends
  waiting for the user's ruling and names the three as changed on main. The
  ticket's branch holds none of them, and no commit the framework made holds
  them. After the user's yes, the next run takes main in; the ticket holds
  one ruling on what changed, which names the three; and what rests on them
  is judged or asked again.

From: product definition, "neither writes the other's"; intent, guard rails
1, 2, 3, 5 and 7 and outcome 2; the user, in tickets 261124-001024-40f8,
261124-091541-a64b, 261124-190535-753f, 261125-014851-46cb and
261125-083337-0fdf.

### REQ-ALG-009 `progress : {what the checks found after the last working session of the attempt, what they find after this one} → yes or no`

Yes when fewer checks fail now than failed before. The first working session
of an attempt counts as progress.

Acceptance:

- Three checks failed, then two: yes. The same two again: no.
- The first working session after an evaluation says no: yes.

From: product definition, the term "Step"; intent, guard rail 1; the user, in
ticket 261123-100659-a0d5.

### REQ-ALG-010 `take_up : {board, tickets a run holds, the ticket the user names, graph, main} → a ticket, the simplest ticket, or none`

The board is the three ticket lanes as main has them (REQ-FLOW-001):
backlog, active and done. In order:

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

From: product definition, "Ask" and the term "Ticket"; the user, in tickets
261123-001543-eae1 and 261124-091541-a64b.

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
  on, the first of these that holds: the user's ruling on what changed while
  a session worked, with the question again (REQ-FLOW-006); the user's
  answer, and to what; to be
  inducted; held up, with the vector, the checks that said no and where what
  they found is kept; in build, with the vector of the last step; to be
  merged. The first is read, where no run holds the ticket, from the
  identities kept from the session's start and the workspace and main as
  they are (REQ-ALG-008), with the files changed on main named apart. The
  next two are read from the ticket: a vector's work that its
  checklist shows delivered for the user's decision, with no answer of the
  user after it, and whether a confirmation in it stands (REQ-ALG-004). The
  rest are read from the event log: how the last run on the ticket ended, and
  its last step. It says which it read each from, with when that was written,
  and that a run reads the workspace again.
- A ticket that has a branch and is not on the board: withdrawn.
- While a ticket is active and the folder is not on its branch: that the
  folder is on another branch, naming both, and that a run and an answer are
  refused until the folder is put back on the ticket's branch (REQ-FLOW-001).
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
- It runs no check, keeps nothing and writes nothing: no file, and nothing
  into git's index or git's store. It works out what it gives, when asked,
  from the board, the tickets, git, the identities kept from a session's
  start and the event log, and from no other record.
- Without an event log it gives what the board, the tickets and git give, and
  says the log was not found. For an active ticket that waits on neither the
  user's ruling, the user's answer nor its induction, it then says that a run
  finds what it waits on.

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
- A run ends waiting for the user's answer on a vector, and the code is then
  deleted from the folder: it still gives that the ticket waits for
  the user's answer on that vector, as the ticket shows, with when the
  question was asked.
- With the event log deleted, it gives what a ticket waiting for the user's
  answer is asked, from the ticket, and says the log was not found.
- Inside a larger repository, a file changed outside the workspace's folder,
  on main or on a ticket's branch, is named for no ticket and adds to no
  count of lines.
- A run ends waiting for the user's ruling on what changed while a session
  worked: it gives that the ticket waits on that ruling, and the same
  question, file by file, the files changed on main named apart as the
  question names them.
- After it answers, every file of the workspace, git's index and git's store
  are as they were before it was asked.
- A ticket is active and the folder is on another branch: it answers, names
  both branches, and says that a run and an answer are refused until the
  folder is put back.

From: product definition, "Show" and "What happened is recovered from these
three"; intent, outcome 5; the user, in tickets 261122-232152-1198,
261123-001543-eae1, 261123-021212-4e94, 261124-001024-40f8,
261124-091541-a64b and 261125-083337-0fdf.

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
