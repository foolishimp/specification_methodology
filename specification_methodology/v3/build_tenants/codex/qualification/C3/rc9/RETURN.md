# Codex RC9 evaluation handoff

The Codex build is frozen as `3.0.0-rc.9` at
`5592168e26759f37e730aed12c030a6061709ec4`, ready for the product owner's
evaluation alongside the Claude build. The common specification remains
C3-I5-06 at `4c340f7adec9f3c893e3e267b23e4cadeb357854`.

Start with the [method entry](../../../successor/README.md) and
[standards library](../../../successor/standards/README.md). The
[interpretation](../../../successor/interpretation/README.md) provides the
source-bound logical account. [Coordinates](COORDINATES.json) identify the
package, documentary source, review evidence and retained qualification.

## Change and review applicability

RC9 preserves the reviewed final-repair package
`5a5b5ad80f0ba4b56b83aadd42ac130de53ba803`. Only five package files change:
the README and two plugin manifests receive the RC9 label; the mapping and
documentary inventory bind the new source freeze. Every other package byte
is identical. In particular, the standards, frames, compression bodies,
semantic account, native program, native map and consumer entry are unchanged.

The final same-family readback and Claude's cross-family readback at
`5f72d36a02abb84b41b96abb11f520bd19c28b0b` therefore retain their applicability
to the unchanged repaired content. They close the final repair findings;
they do not establish whole-method acceptance. No semantic review or actor
trial was repeated for the label change.

## Current checks

[CHECKS.json](CHECKS.json) proves the five-file boundary and rejects any
other package change. [ARTIFACT_CHECK.json](ARTIFACT_CHECK.json) records:

- 90 package members, 38,958,677 bytes;
- seven reproduced responsibility frames;
- 2,250 resolving local links and 32 matching compression pins;
- successful cold identity with 19 negative controls;
- zero artifact failures.

[INTERPRETATION_IDENTITY.json](INTERPRETATION_IDENTITY.json) records a successful
invocation of the unchanged consumer entry against the RC9 source inventory
and exact installed encoding theory. The native program and map retain their
earlier validation evidence through byte identity. The current check is not
a new claim of semantic fidelity, context sufficiency or actual use.

## Decisions still reserved

The [conservation account](../rc5/integration/CONSERVATION.json) and
[replacement questions](../rc5/integration/REPLACEMENT_QUESTIONS.json) retain
their original source and review subjects: 595 conserved proposals, 95
proposed replacements and one not-applicable row, with 36 replacement
questions. No disposition, question or acceptance standing changes in RC9.
The full qualified-choice criteria, outstanding member decisions, broader
foundation-to-law and interpretation assessment, reduction and actual-use
evidence retain their existing limits. The owner's evaluation selects neither
a release nor acceptance automatically.

The candidate is on `tenant/codex/c3-iteration-5` in the Codex worktree.
Historical candidates and evidence remain intact. No peer implementation,
common requirement, release tag, installation, outward merge or remote was
changed.

## Reproduction

`package.py` uses the existing pinned documentary inventory and package checker.
Run it with the installed toolchain Python in a disposable checkout, because
verification writes its RC9 receipts:

```sh
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  qualification/C3/rc9/package.py verify \
  --source-commit bb04f40fa559bf56b10e548b8d35cc2b13f989e4 \
  --package-commit 5592168e26759f37e730aed12c030a6061709ec4
```

To reproduce the two metadata outputs, begin at the documentary source commit
`bb04f40f` and use `bind --source-commit` with its full coordinate above.
Compare the resulting package with `5592168e` before verification. The bind
operation requires the source preimage, not the already rebound package.
