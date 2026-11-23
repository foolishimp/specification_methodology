# Builder installs the way STDO does

- kind: feature
- from: the product owner, 20 November 2026: "eventually build should follow
  the install pattern of stdo"

Builder is released and installed by the pattern STDO uses for its own
releases, in place of the folder and `install.sh` of the first build
(design decision D63).

Not for now. It is taken up when the product owner says.

## To settle when it is taken up

- Which parts of STDO's pattern are meant: the release address
  (`stdo://releases/<version>/`), the channel a product selects, the manifest
  and its hash, the command that installs and verifies, and where an installed
  release is kept.
- Whether Builder's releases are managed by STDO's own tool or by one of its
  own that follows the same pattern.
