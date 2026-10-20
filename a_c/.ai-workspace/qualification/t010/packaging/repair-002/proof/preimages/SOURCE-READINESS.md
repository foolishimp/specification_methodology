# Common V3 represented-source readiness

The complete common candidate is frozen for a separate a_c representation.
This is a source-custody result. The method remains an unaccepted, unpublished
candidate; its source-release record says `freeze_readiness: not_ready`.

## Exact subject and basis roles

| Coordinate | Value |
|---|---|
| Represented subject | `repo://stdo-v3-common/35fb4824a064a84df5af214a0d0e2da597c18ac6` |
| Repository | `https://github.com/foolishimp/specification_methodology.git` |
| Source checkpoint | `35fb4824a064a84df5af214a0d0e2da597c18ac6` |
| Payload commit | `7d0516f37716298f038548c4152a1a697ce70f95` |
| Package path | `specification_methodology/v3/build_tenants/common` |
| Package tree | `7f2070b61c848b42b4dfb3af1e0ce53869de1aa1` |
| Complete payload | 81 files, 3,298,515 bytes |
| Construction inventory SHA256 | `187908fed6acee3570f472ee15c11e3116537155a8c5cc14cad8d096dc8381cd` |
| a_c construction basis | `stdo://releases/v2.5.1-rc.2/` |
| Installed basis manifest SHA256 | `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` |
| Installed calculus SHA256 | `cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d` |

The common package is the represented subject, not a newly adopted builder or
runtime method profile. The a_c Product Definition, installed basis and empty
Product composition are unchanged. The application uses the existing Graphify
tenant's source-to-model HOW. It adds no common method rule or F_D runtime
profile.

Jim's latest instruction authorizes construction and release preparation of
the representation. The working scope is the separate representation package
while clarification of the release subject is pending. It authorizes no
publication, consumer adoption or inferred method acceptance. The earlier
T-003 exclusion of in-package representation delivery is preserved: this
application sits outside the common package and edits none of its bytes.

## Corpus selection and custody

All 81 immutable Git blobs are preserved under [source/](source/), with their
original package-relative paths. [package-custody.json](package-custody.json)
records every path, byte count, SHA256, Git blob and Git mode.
[source-classification.json](source-classification.json) accounts for the full
package and retains the exact inherited frame-owner routes.

| Class | Files | Bytes | Use |
|---|---:|---:|---|
| Primary semantic source | 58 | 2,000,888 | All standards except `standards/frames/**`, plus plugin Markdown. This includes the 23 root standards, 2 schemas, 24 templates and 9 plugin workflow/reference documents. |
| Derived frames | 13 | 1,270,927 | Twelve verbatim acquisition frames and `FRAME_INPUTS.json`. Their 223 inherited bindings route to the frozen local owners; they create no independent law. |
| Host/legal/release metadata | 10 | 26,700 | Two licences, two plugin manifests, five host-interface YAML files and the release note. |

[source-manifest.json](source-manifest.json) is the explicit 58-file manifest
for ordinary `ac_generate.py prepare`, using `source/` as the corpus directory.
The YAML invocation prompts and implicit-invocation flags retain host meaning;
classifying them as metadata does not declare them semantically empty. Optional
profiles stay optional, guides and indexes stay non-deciding, and starter
templates do not become a consumer's live constitution through inclusion.

Construction and review records, predecessor accounts, existing native a_c
programs, interpretation outputs and old representation artifacts are excluded
from semantic input. The source-selection manifest is a custody contract, not
an assertion that every proposition has already been interpreted.

The inventory digest is SHA256 over the Git-ordered array of
`{path,bytes,sha256}`, serialized as UTF-8 JSON with sorted object keys, no
whitespace and unescaped Unicode:

- Complete package: `740a3d1066a2b685c3985cf366f29dcb582c38e8ed98ddf5ee3a7576b993126d`.
- Primary semantic source: `7605efc789326de5f2d8568571a65113097cde54947743f622321193480af12f`.

## Reproduce the custody checks

From this application directory:

```sh
python3 -B freeze_sources.py --check
python3 -B freeze_sources.py --check --git-repository /Users/jim/src/apps/specification_methodology
```

Both commands read only. The second re-enters the fixed source and payload
commits, checks the package tree, and compares every frozen file with its
immutable Git blob. Neither command can replace source, refresh a hash, choose
another version or repin a study. The local check also verifies the explicit
selection, all three class populations, the inherited frame manifest, and
frame/owner file identities. It does not independently prove the semantic
sufficiency of those frames or every section digest.

## Current method-release standing

The exact source checkpoint's construction record is outside the semantic
corpus. Relevant records at that commit are:

- `specification_methodology/v3/.ai-workspace/common-build/BUILD.md`;
- `common-build/repair-1/CHECKPOINT.json`, `AUTHOR_RETURN.json` and `DECISIONS.json`
  under that same `.ai-workspace/` root; and
- `common-build/repair-1/SUPPLEMENTARY_REVIEW.md` and the canonical review it
  names.

They report owner acceptance `not_given`, covering independent review
`unassigned`, and actual-use qualification unperformed on the repaired subject.
The bounded same-family nonauthor supplementary review closes the B1–B3 text
and two records-mechanism repairs only. Its author-task exposure and inherited
context are disclosed. It is not the covering review or a cold-reader trial.

Concrete source-release gates still recorded as open are:

- A1 reach, Q13 frame-excerpt policy, Q14 entry routing, Q2/Q6 rows 93–96,
  the exact predecessor replacements, ten disputed changed-but-conserved rows,
  and assignment of the covering review.
- D1's calculus derivation basis, complete clause-address grammar and
  digest-field encoding/comparison. These remain incomplete before a runnable
  method identity-record claim.
- D2's CONFORMANCE scope and independent expected distinctions, with consistent
  README and EVALUATION consumers.
- D3's proposed World Model application-evidence duty, preserving the Markov
  construct's candidate standing.
- D4's recoverability benchmark and whether comparative baseline evidence is
  required. The recommendation is not an owner decision.
- P1's stale-basis wording conflict and its classification by the covering
  reviewer; Q10's unresolved UX interpretation.
- Current semantic and actual-use evidence, independent assessment over the
  material contribution set, owner replacement decisions and exact-cut release
  acceptance. All 705 effective predecessor dispositions remain unresolved
  and their acceptances pending in the current construction record.

The recorded package controls establish their declared mechanical properties
on the unchanged payload: 81 files, 5,860 local references, 29 package-tool
controls, 20 conservation controls, 815 receiving loci and 12 frame outputs.
These observations are carried from their exact recorded subject; this source
freeze does not rerun them or turn them into semantic qualification.

The materialization using `v3.0.0-rc.9999` and an all-zero absent-tag sentinel
is verification-only. Its manifest is not a publishable release manifest. The
separate real-Git installer replay covered the older first-build payload, not
fresh installation of this repaired candidate or its method acceptance.

## Representation handoff and remaining claims

Source custody and explicit selection are ready for separately activated
ordinary Graphify/F_P authoring. The source's open choices and inconsistent or
incomplete rules must remain inspectable; authoring must not silently decide
them or assert qualification that the source does not claim.

No F_P generation, interpretation fidelity assessment, carrier admission,
whole-calculus conformance, efficiency comparison, accepted model or release
package is established by this source freeze. Those results and the final
representation release disposition remain downstream. The source's own release
gates do not prevent an honestly labeled proposal representation, and the
representation cannot close those gates on the method's behalf.

The Writer activation, basis/source preimages, initial dirty-worktree summary
and guard evidence are under
[the source proof](../../.ai-workspace/qualification/t010/source/).
[T-010](../../.ai-workspace/tickets/active/T-010-common-representation-release-preparation.md)
records the application scope. No Git checkpoint or publication is performed
by this Writer activation.
