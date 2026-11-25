# The interfaces

**Family**: REQ-INTERFACE-*
**Status**: Active
**Category**: Capability

These requirements cover how the user reaches the product and its workspace.

### REQ-INTERFACE-001 One library, instanced in four ways

**Status**: Active for the library, the command-line program and an
application of the user's own. The program that serves the commands as tools
over the Model Context Protocol and the service with an API are Deferred: the
user put them off on 23 November 2026, in ticket 261124-055459-1851.

The product's commands are functions of one library: to set a product up, start
a run, give an answer, show where the work stands, list the registry and
record the release that builds a product (REQ-FLOW-010). The library can be
instanced in four ways:

- within a command-line program;
- within a program that serves the commands as tools an agent calls over the
  Model Context Protocol;
- as a service with an API;
- built directly into an application of the user's own.

The product comes with the first three: the command-line program first, and
the other two after the first build (goals, "First build"). All four give the same commands, take
the same inputs and return the same results. None holds a rule of the product:
each passes the command to the library and gives back what it returns. The
library is published with the product and documented for use.

A command given from inside a session the framework started, on the workspace
that session works for or on a folder inside it, is refused by the library,
says why and changes nothing.

A command that works in a workspace reads git's version before anything else.
Where it reads as older than the version REQ-PARAM-001 gives, the command is
refused, changes nothing, and names in one sentence the version found and the
version needed.

A command that is not known, or is not given what it needs, such as an answer
that is neither yes nor no or a ticket with no words, prints the usage and
ends with the code the instructions give for a command not given what it
needs.

Acceptance:

- For the first build: scenario S1 ends as it should driven from the command
  line, and the command-line program's code holds nothing but the passing of
  commands to the library.
- Each command, given in each way the product then offers on the same
  workspace, gives the same result.
- Adding the second and the third way changes no line of the library.
- The code of the first three holds no check, no decision and no step of a run.
- A small application that holds the library and nothing else of the product
  sets a product up and starts a run.
- A session the framework started gives each command on the workspace it
  works for and on a folder inside it: each is refused, says why and changes
  nothing.
- The product's own tests, which start the product on workspaces of their
  own, pass when they are run from inside a session that builds this product.
- A script named `git`, first on the PATH, answers `--version` with a version
  older than REQ-PARAM-001 gives and passes every other command on to git:
  each command that works in a workspace is refused, names in one sentence
  the version found and the version needed, and changes nothing.
- A command that is not known, an answer that is neither yes nor no and a
  ticket with no words each print the usage and end with the code the
  instructions give for a command not given what it needs.

From: product definition, "The product is one library, and it can be instanced
in four ways"; intent, guard rail 1 and outcome 5; the user, in tickets
261123-185201-a149, 261124-091541-a64b and 261124-220448-c7ab.

### REQ-INTERFACE-002 A workspace is named by a URI

**Status**: Active for a workspace on a mounted file system. A workspace
reached through a service is Deferred: it is built after the first build, as a
ticket.

The framework reaches the workspace only by the URI the user named, to read
and write files and to use git. The workspace may be on a mounted file system,
or reached through a service that gives access to one, and the framework
treats the two alike.

Acceptance:

- Scenario S1 ends as it should on a workspace on a mounted file system.

From: product definition, "Its workspace is named by a URI"; intent, guard
rails 2 and 5.

### REQ-INTERFACE-003 The product is installed from a release, with instructions and a getting-started guide for users

The product is installed from a release, by one command. The release holds the
product's instructions for users: how to install it, set up a governed
product, write a ticket, start a run, give an answer, with the reason of a no
and a ruling, see where the work stands and record the release that builds a
product. The installation page and the instructions each name, in one place,
what the product needs: git of the version REQ-PARAM-001 gives, for every
product, and `ps`, with the package that brings it on Debian and Ubuntu.
They say where a product may be set up, and what the framework does
in a larger git repository that the workspace lies inside (REQ-FLOW-001).
Where they say what a run notes while a session works, and where they speak
of a larger repository, they say that a session's git commands act on the
whole repository, so that a session which commits with `git add -A` commits
what the user has not committed outside the folder; that the run names what
was committed outside the folder while a session worked; and that a ticket's
merge names what it took in there (REQ-FLOW-008).
Where they speak of the one merge a run completes, they say that a file the
user has staged elsewhere in the repository then is in it (REQ-FLOW-008), and
that the user commits that merge first, or unstages what is not to go with
it. They
say what a run commits as the user's own change; that what changed while a
session worked, outside what its step writes, is named to the user, and the
run waits for the user's ruling before it judges or commits anything of the
step; what a yes and a no then mean (REQ-FLOW-006); and when a run stops.
Where they say what changed while a session worked, and what a run notes
among the branches, they say that each file of the folder that main, the
branch the ticket left, gained while a session's identities were kept is put
to the user, named apart as changed on main; that nothing of main is taken
into the ticket's branch before the user's yes; what a yes and a no mean for
those files (REQ-FLOW-006); that inside a larger repository a file outside
the folder committed on main while a session worked is named, and nothing is
asked on it; and that what main gains while no session's identities are kept
is taken in with no question (REQ-FLOW-008). Nothing else they say
contradicts this. Where they say which files the comparison reads, they
say, as its limits, the three cases it does not reach: a folder in the workspace that is
a git repository of its own, as `git clone` or `git init` there leaves, none
of whose files is compared or asked about, and for which the framework
commits a pointer to its commit that a clone of the product cannot follow; a
file that a session takes out of git's index and has git ignore, which is
removed from the ticket's branch, and so from main, with no question, and
stays in the folder; and a change of a file's mode alone, which is committed
with no question. Where they say that what changed while a session worked,
outside what its step writes, does not stop a run, they say the case that
does: a symbolic link to a folder, or one whose target is not there, that
appears while a session works stops the run with git's own words, and each
run and answer after is refused until the user removes the link or has git
ignore it.
They say what stands in for the identities kept from a session's start where
those cannot serve: the commit the session started from, so that every file
that differs from it is asked about; and, in the same place, the accepted
limit: where the record of that start is gone, cannot be read or names a
commit git does not hold, the commit the folder is on stands in, and what a
session committed of its own is not asked about (REQ-ALG-008). They
say, in plain words, that a ticket is built in the workspace's own folder on
a branch of its own, and what that costs the user, as REQ-FLOW-001 states it:
what is committed in the folder while a ticket is active, two products in one
repository, the files git ignores in the folder, and the refusal while the
folder is on another branch. They say
how the user removes, with git's own commands, a checkout an earlier release
left and a done ticket's branch, and that a job of the user's own may be
named as a process the framework cannot place, and which processes of a
session it does not find, wherever they work, with what still holds of what
they write (REQ-FLOW-001). Where they speak of a new release, they say to
finish or put back every active ticket with the release that pulled it
before the new release is installed and recorded, and why, in one sentence:
a release does not read the hold or the identities that an earlier release
kept in another place, so a ruling awaited across the change is not asked
again, and the next run commits what is not committed as the user's change
by hand. They say that a
command given from inside a session the framework started, on its workspace,
is refused (REQ-INTERFACE-001). They say where the user reads a
question: in the run's ending, and in what `show`
gives. They say what the ticket holds as the work goes on, and which part of
it is the framework's (REQ-FLOW-004). They assume no knowledge of the
framework's source.

The release also carries a getting-started guide: a page of its own at the
top of the release, beside the installation page and the instructions, and
named by both. It is for a person who has never used the product, and it is
one page that person reads in ten minutes. It walks one small product from
nothing to a change, in the order a person meets things, in the parts the
user gives in ticket 261123-054924-2092: installing the product; setting the
product up in a folder inside a larger git repository; a first ticket in the
user's words, through each question a run ends at, with a ruling given with
the first answer; what the ticket then holds; a change by a second ticket; a
change by hand with no ticket; a run with nothing changed, which is refused;
what `show` gives; and the three places what happened is read from. It gives
the exact commands and what the product printed. It is written from one real
run of the product, which it names by its date, and it states no figure that
run did not give. As the product's words it gives only lines that the release
it ships in prints, and wherever it names a version of the product it names
that release's own. The release command runs the guide's commands on the
release it has just installed (REQ-INTERFACE-004), with the stand-in agent
where a session is needed, and fails, naming the line, where a line the guide
gives as printed is not printed. It says in one sentence what the costs
depend on: the agent and the size of the product. For every detail it points
to the instructions instead of restating them.

Acceptance:

- A person who has only the instructions installs the product and completes
  scenario S1.
- The installation page and the instructions each name the getting-started
  guide.
- The guide names the date of the run it is written from, and each figure it
  states is one that run gave, as the user records it in ticket
  261123-054924-2092. Wherever it names a version of the product, it names
  the release it ships in.
- A person who has never used the product reads the guide in ten minutes. It
  takes the parts above in their order, gives each command and what the
  product printed, and leaves every detail to the instructions.
- Each line the guide gives as printed is printed when its commands are run
  on the installed release. A guide that gives a line the release does not
  print, such as a version in another form than the release prints, fails the
  cut, which names the line.

From: goals, "First build"; intent, outcome 5; the user, in tickets
261123-001543-eae1, 261123-021212-4e94, 261123-054924-2092,
261123-185201-a149, 261124-001024-40f8, 261124-055459-1851,
261124-091541-a64b, 261124-220448-c7ab, 261125-014851-46cb,
261125-043021-2fed and 261125-083337-0fdf.

### REQ-INTERFACE-004 The product is released as its sibling products are

A release of the product has the form stated here. The reason for this form
is that the product's sibling products in the method's repository are released
in it, each under a profile of its own, and so a release of the product can
join a release of the method as one more product. Nothing else is defined for
it: no other kind of manifest, no registry of releases, no form of address and
no new term.

A release is cut by one command of the product's own, the release command,
which is under version control with the product's source. No part of what it
cuts is made by a script outside version control, or by hand, apart from the
words the person who cuts gives it for that one cut as a file under version
control (below). The person who
cuts a release gives
its version to the release command. The release command cuts no release
without one, and the release carries the version given. The cut publishes
nothing: it pushes nothing and uploads nothing.

The release command cuts the whole release, in this order:

1. the release of the product;
2. the bundle, which holds the release of the product and, beside it, the
   release of the method's standards that set-up installs where the user
   names none (REQ-FLOW-002);
3. the download: one compressed file of the bundle;
4. an install from the download, unpacked with every member kept as a file,
   which ends with the installed product giving its version.

Where a step fails, the cut fails, names the step and leaves no download.

For the release of the product, the release command writes a public
manifest. It names its profile as
`stdo-builder.release-package/1`, the product, the version, the entry points
(the library and each program the release holds) and the version of the
runtime the product needs. It gives every file of the release but the manifest
itself as `path`, `bytes` and `sha256`: the file's path in the release, its
size in bytes and the sha256 of its content.

A release holds an installation page, a getting-started guide
(REQ-INTERFACE-003), a release note, the product's own licence
(REQ-INTERFACE-005), and the licence of each thing the product depends on that
it ships. Apart from these, the instructions REQ-INTERFACE-003
asks for, the manifest and the command that installs it, a release holds only
what is needed to run the product. Of what the product depends on, it holds no
map from built code to its source, no declaration of types and no source that
code was built from.

The one command that installs the product (REQ-INTERFACE-003) checks every
file of the release against the manifest before it installs anything. Where a
file the manifest names is missing or differs from it in size or sha256, or the
release holds a file other than the manifest that the manifest does not name,
it installs nothing.

The bundle's manifest is of the kind the release's is. It names a profile of
its own, the product, the version, and every file of the bundle but the
manifest itself as `path`, `bytes` and `sha256`. Beside these it names the
release of each part of the bundle with the sha256 of that part's own
manifest. The bundle holds an installation page, a release note, the
product's own licence (REQ-INTERFACE-005), the manifest and the command that
installs it, and a history page only where the person who cuts gives one for
that cut.

The product states once the release of the method's standards that set-up
installs where the user names none. The release command takes that release
from where the method keeps its releases, verified by the method's own
command, and never from a folder a person names. The bundle's note names it.

The bundle's install command checks that the runtime the product needs is
there, and of the version it needs, before it makes or copies anything. It
checks every file of the bundle against the bundle's manifest, as the
release's install does. It ends with the codes its installation page lists
and no other, and where it fails it leaves nothing it made. Where the folder
it is to install in cannot be made, it says so in one sentence and ends with
the code its page lists for a folder that cannot be used.

The download holds the files the bundle's manifest names and the manifest,
each as a plain file, and nothing else: no file that holds another file's
attributes, and no name of the person who cut it. The release command reads
the download back member by member to establish this, and does not rest on
the tool that wrote it.

Apart from the words of the person who cuts (below), each statement of fact
in the bundle's installation page and release note, such as a version, the
release of the standards, a licence, what is put off and what a command
prints, is written by the cut from what it has just read or checked. What is
put off is read from the requirement files. No such statement
is written into the release command as a sentence about one release.

The release note also holds the words of the person who cuts about that one
release: what changed since the last release, and what is known and left.
The person gives them to the release command as a file under version
control, for that cut. The note holds them as given, beside the statements of
fact the cut writes. No such words are written into the release command, and
none carry over from one cut to the next. A cut given none holds a note of
the statements of fact alone.

Acceptance:

- A release cut with the version given as V carries V in its manifest. The
  release command given no version cuts no release.
- The manifest names its profile as `stdo-builder.release-package/1`, the
  product, the version, the entry points and the version of the runtime
  needed, and gives every file of the release but the manifest itself as
  `path`, `bytes` and `sha256`. The release holds no file other than the
  manifest that the manifest does not name.
- The release holds an installation page, a getting-started guide, a release
  note, the product's own licence and the licence of each thing it ships that
  the product depends on.
- Of what the product depends on, the release holds no map from built code to
  its source, no declaration of types and no source that code was built from.
- Where one file of a release is changed, removed or added after the release
  is cut, the install refuses and writes nothing where it would install.
- A cut ends with an install from its own download, unpacked with every
  member kept as a file, and the installed product gives the version V.
- A cut in which any one step is made to fail fails, names that step and
  leaves no download.
- A file of the bundle that carries attributes of the file system it was cut
  on adds no member to the download. No member of the download names the
  person who cut it. Read back member by member, the download holds exactly
  the files the bundle's manifest names and the manifest.
- The bundle's manifest names a profile of its own, the product, the version,
  every file of the bundle but itself as `path`, `bytes` and `sha256`, and the
  release of each part with the sha256 of that part's own manifest.
- The bundle's install, where the runtime is missing or older than the
  product needs, makes and copies nothing. Given a bundle with one file
  changed, added or removed, it installs nothing. Each of its failures leaves
  nothing it made and ends with a code its installation page lists.
- Given a folder that cannot be made, the bundle's install says in one
  sentence that the folder cannot be made, ends with the code its page lists
  for a folder that cannot be used, and leaves nothing it made.
- A bundle cut with no history page given holds none.
- The bundle's note names exactly the requirements that the requirement files
  mark as put off.
- Where what the requirement files mark as put off, or the release of the
  standards that set-up installs where the user names none, changes, the
  note of the next cut names what is then put off and the release of the
  standards its bundle then holds, with no change to the release command.
- The bundle holds the release of the method's standards that set-up installs
  where the user names none, and its note names that release.
- That release is stated in one place in the product. Changed there and
  nowhere else, it is the release set-up then installs where the user names
  none and the release the next cut's bundle holds.
- The release command takes the standards only from where the method keeps
  its releases, once the method's own command has verified them; no input of
  the release command names a folder they are taken from. Where that
  verification fails, the cut fails, names the bundle's step and leaves no
  download.
- A cut given a file of the words of the person who cuts holds those words in
  its note as given, beside the statements of fact. A cut given none holds a
  note of the statements of fact alone, with none of the words given to an
  earlier cut. The release command holds no such words.
- The cut pushes nothing and uploads nothing.

From: the user, in tickets 261122-210140-bf19, 261123-054924-2092,
261124-055459-1851 and 261124-220448-c7ab; product definition, "The library is published with the
product"; intent, guard rail 4 and outcome 5.

### REQ-INTERFACE-005 A release holds the product's own licence

The product's licence is the Apache License 2.0, the licence of the method's
standards, since the two are one bundle (REQ-INTERFACE-004). The product's
source, each release and each bundle hold it. Each release note says what is
under that licence, and that each library a release ships keeps its own
licence, which the release holds beside it.

Acceptance:

- The product's source, each release and each bundle hold the Apache License
  2.0.
- Each release note names what is under the Apache License 2.0 and says that
  each library the release ships keeps its own licence. The release holds
  each of those licences.

From: the user, in ticket 261122-210140-bf19, "the licences of what it ships";
the user, on 23 November 2026, in ticket 261124-055459-1851.
