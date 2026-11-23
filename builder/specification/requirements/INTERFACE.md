# The interfaces

**Family**: REQ-INTERFACE-*
**Status**: Active
**Category**: Capability

These requirements cover how the user reaches the product and its workspace.

### REQ-INTERFACE-001 One library, instanced in four ways

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

From: product definition, "The product is one library, and it can be instanced
in four ways"; intent, outcome 5.

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
product. They say where a product may be set up, and what the framework does
in a larger git repository that the workspace lies inside (REQ-FLOW-001). They
say where the user reads a question: in the run's ending, and in what `show`
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
run of the product, which it names by its release and its date, and it states
no figure that run did not give. It says in one sentence what the costs
depend on: the agent and the size of the product. For every detail it points
to the instructions instead of restating them.

Acceptance:

- A person who has only the instructions installs the product and completes
  scenario S1.
- The installation page and the instructions each name the getting-started
  guide.
- The guide names the release and the date of the run it is written from, and
  each figure it states is one that run gave, as the user records it in ticket
  261123-054924-2092.
- A person who has never used the product reads the guide in ten minutes. It
  takes the parts above in their order, gives each command and what the
  product printed, and leaves every detail to the instructions.

From: goals, "First build"; intent, outcome 5; the user, in tickets
261123-001543-eae1, 261123-021212-4e94 and 261123-054924-2092.

### REQ-INTERFACE-004 The product is released as its sibling products are

A release of the product has the form stated here. The reason for this form
is that the product's sibling products in the method's repository are released
in it, each under a profile of its own, and so a release of the product can
join a release of the method as one more product. Nothing else is defined for
it: no other kind of manifest, no registry of releases, no form of address and
no new term.

The person who cuts a release gives its version to the release command. The
release command cuts no release without one, and the release carries the
version given.

The release command writes a public manifest. It names its profile as
`stdo-builder.release-package/1`, the product, the version, the entry points
(the library and each program the release holds) and the version of the
runtime the product needs. It gives every file of the release but the manifest
itself as `path`, `bytes` and `sha256`: the file's path in the release, its
size in bytes and the sha256 of its content.

A release holds an installation page, a getting-started guide
(REQ-INTERFACE-003), a release note, and the licence of each thing the product
depends on that it ships. Apart from these, the instructions REQ-INTERFACE-003
asks for, the manifest and the command that installs it, a release holds only
what is needed to run the product. Of what the product depends on, it holds no
map from built code to its source, no declaration of types and no source that
code was built from.

The one command that installs the product (REQ-INTERFACE-003) checks every
file of the release against the manifest before it installs anything. Where a
file the manifest names is missing or differs from it in size or sha256, or the
release holds a file other than the manifest that the manifest does not name,
it installs nothing.

Acceptance:

- A release cut with the version given as V carries V in its manifest. The
  release command given no version cuts no release.
- The manifest names its profile as `stdo-builder.release-package/1`, the
  product, the version, the entry points and the version of the runtime
  needed, and gives every file of the release but the manifest itself as
  `path`, `bytes` and `sha256`. The release holds no file other than the
  manifest that the manifest does not name.
- The release holds an installation page, a getting-started guide, a release
  note and the licence of each thing it ships that the product depends on.
- Of what the product depends on, the release holds no map from built code to
  its source, no declaration of types and no source that code was built from.
- Where one file of a release is changed, removed or added after the release
  is cut, the install refuses and writes nothing where it would install.

From: the user, in tickets 261122-210140-bf19 and 261123-054924-2092; product
definition, "The library is published with the product"; intent, outcome 5.

### REQ-INTERFACE-005 A release holds the product's own licence

**Status**: Deferred. It is built once the user names the product's licence.

A release holds the product's own licence beside those of what it ships.

Acceptance:

- The release holds the licence the user named for the product.

From: the user, in ticket 261122-210140-bf19, "the licences of what it ships".
