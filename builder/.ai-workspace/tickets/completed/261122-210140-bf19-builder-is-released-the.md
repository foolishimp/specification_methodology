Builder is released the way its sibling products in the method's repository are released, so that it can join a release of the method as one more product. Nothing new is defined for this: no new kind of manifest beyond a profile of Builder's own as each sibling has, no registry, no address form, no new term. The person who cuts a release gives its version to the release command; the version is no longer 0.0.0 with a commit. The release command writes a public manifest that names the product, the version, the entry points and the Node version needed, and gives the path, the size and the sha256 of every file of the release. A release holds an installation page, a release note, and the licences of what it ships. It holds only what is needed to run: no source maps, type declaration files or TypeScript sources of what it depends on. install.sh stays, and checks every file against the manifest before it installs anything. How a governed product records which Builder release builds it is not part of this ticket.

## Triage

- kind: feature
- class: requirement_reprice
- enters: requirements
- ends: code
- scope: Builder's release and its install only. It touches REQ-INTERFACE-003, or a requirement beside it in INTERFACE.md; design D63, and D190 for the entry points; scripts/release.mjs, packaging/install.sh and packaging/INSTRUCTIONS.md; tests/release.test.ts and the install path of S1's test. It does not touch the library's commands, the method's graph or any other requirement family. Publishing the release (still not built, D63), the method's own release taking Builder in, and any change to the method's repository are outside it, as is how a governed product records its Builder release.
- term: {"term": "sequence", "terms": [{"term": "reference", "name": "write-requirements"}, {"term": "reference", "name": "write-build"}]}
- triaged: 2026-11-22

Why it enters at the requirements: REQ-INTERFACE-003 asks only for a release installed by one command, holding the instructions for users. No accepted requirement asks for a version given by whoever cuts the release, a public manifest with the size and sha256 of every file, a release note, the licences of what is shipped, a release that holds only what runs, or an install that checks every file before it writes. D63 leaves the version as package.json's 0.0.0 with the commit, for the product owner. This is new behaviour, so it is stated first in the requirements, for the user's decision. The design, tests and code then follow in one session, judged together, since a person judges the release command and its install as a whole. The intent and the product definition do not change: the user's words add no term and no new kind of thing, and the product definition says nothing of a release's form. The ticket builds the release command and cuts no release, so the basis having no frame yet for release and qualification does not hold it up. The work stays within the current release scope.

Open for the requirements session:

- The form Builder's release follows is that of its sibling products in the method's repository, a profile of Builder's own. This session did not read it, because its packet admits only named sections of the method. The requirements session needs that form within what it may read.
- Builder has no licence file of its own and package.json names none. The release carries the licences of what it ships, and the user decides Builder's own.
- The rule against type declarations names only those of what Builder depends on. The library is published for use (REQ-INTERFACE-001), so whether Builder's own declarations ship is to be decided.
