# Installing STDO Builder 3.2.1 with the method's standards

This bundle holds release 3.2.1 of STDO Builder, in `builder/`, and release v3.1.0-rc.3 of the
method's standards, `stdo://releases/v3.1.0-rc.3/`, in `standards/`. Its release note is `RELEASE_NOTE.md`.

To install it you need Node.js 24 or later on your PATH. To use STDO Builder you also need
what `builder/INSTALL.md` names.

From this folder:

```
sh install.sh <folder>
```

It first checks that node is on your PATH and of the version STDO Builder needs, then every file of this
bundle against `manifest.json`. Only then does it install STDO Builder into `<folder>`, by `builder/install.sh`,
as `builder/INSTALL.md` says. Where it fails, it takes away what it made.

The standards in `standards/` are for reading, and are not installed. STDO Builder does not read this copy: it
finds the method's standards through the method's release manager, `stdo`, and set-up installs there the
release it names, which is stdo://releases/v3.1.0-rc.3/ where you name none.

Once installed, `stdo-builder --version` prints `stdo-builder v3.2.1`. Go on with `builder/GETTING_STARTED.md`
and `builder/INSTRUCTIONS.md`.

The install exits with:

- 0: STDO Builder is installed
- 2: no folder is named, or the folder named cannot be used
- 3: node is not on your PATH, or is older than STDO Builder needs
- 5: the bundle is not as its manifest says
- 6: the install could not finish
