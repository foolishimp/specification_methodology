STDO 3.0.5 delivers one coordinated release of five Products: Specification Methodology v3, STDO Representation, a_c Implementations (Graphify and Lean), Axiom Indexer, and STDO Skills for Codex and Claude.

The installed release includes the native workflow, current source-linked model and constraint map, 3D/2D/layered explorer with source and file navigation, executable Graphify and Lean tools, current proof evidence and reader, and both host skill packages. The external `stack-release-v3.0.5.json` asset records their exact membership, dependencies, qualification evidence and limits.

The manager runtime ZIP contains the installation README, exact dependency wheels and hash-locked requirements for the qualified macOS arm64 / CPython 3.13 environment. The separate constraints file records the selected dependency versions. After installing the manager, select the immutable native cut explicitly:

```sh
stdo install v3.0.5 \
  --repository https://github.com/foolishimp/specification_methodology.git \
  --manifest-sha256 998852a22578a798abceb821fa654d5287c0b1fb908734afa3ee9403738596cd
```

Use the installed `standards/documentation/index.html` for the current explorer and proof reader, and `standards/tooling/README.md` for component and host setup. The proof materializer preserves the original evidence and prepares a local request for a new installed verification.

The current STDO model contains 1,885 records. Its formal results have the exact obligations and bounds stated in the retained evidence; the independent semantic review has its separately stated scope. The ABI code explorer is an explicitly labelled frozen example from the published 3.0.4 cut.
