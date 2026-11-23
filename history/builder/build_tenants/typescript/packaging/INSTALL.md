# Installing STDO Builder

This folder is one release of STDO Builder, `stdo-builder-<version>`. Its
release note, `RELEASE_NOTE.md`, gives the version and what it ships.

To install it you need Node.js 24 or later on your PATH. To use it you also
need git 2.31 or later (2.38 or later for a product inside a larger git
repository), the method's release manager `stdo`, and an LLM agent that runs
from the command line, as `INSTRUCTIONS.md` says.

Install it into a folder of your choice, from this folder:

```
sh install.sh <folder>
```

Name a folder outside this one: a folder inside the release is a file of it
that its manifest does not name, so the release would not install again.

The install first checks every file of this release against its manifest,
`manifest.json`, which gives each file's path, size in bytes and sha256. Where
a file is missing or differs, or the release holds a file the manifest does not
name, it says which and installs nothing: it does not even make `<folder>`.

Otherwise it puts the product in `<folder>/lib/stdo-builder/stdo-builder-<version>`
and the command in `<folder>/bin/stdo-builder`, and writes nothing else.
Installing the same release again replaces what it put there. Put the
command's folder on your PATH, so that you can type `stdo-builder` alone:

```
export PATH="<folder>/bin:$PATH"
```

Then go on with `INSTRUCTIONS.md`, at "Set up a product". If you have not
used the product before, read the getting-started guide, `GETTING_STARTED.md`,
in this folder, first: it takes one small product from nothing to a change.

The install exits with 0 once it has installed; 2 where no folder is named; 3
where Node.js 24 or later is not on your PATH; 5 where the release is not as
its manifest says.
