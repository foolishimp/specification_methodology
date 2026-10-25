# Manager 0.1.6 delivery return

The selected manager source and reproducible wheel are ready for independent
review and the native 3.0.2 publication checks. This return supersedes the
pending-proof status in the immutable source freeze; it does not replace or
rewrite that freeze.

## Exact subject

| Item | Identity |
|---|---|
| Starting checkpoint | `88305bef5dbd9d56db4668ef85611941f5e67705` |
| Current 22-file freeze | `CANDIDATE-repair1.json` |
| Freeze SHA-256 | `e3c5302012ac9cfdc2413096976a9ba2ae49e408b0d01f47320edd21ae1fd50d` |
| Wheel | `package-03/stdo_toolchain-0.1.6-py3-none-any.whl` |
| Wheel SHA-256 | `ef726f780220a4be93c8ce014e2838d140851ec0e3d47902ea2ddd36a26c3242` |
| Wheel size | 61,549 bytes |
| Package record SHA-256 | `6310139ed937bcc5b6184fc6412134c0df736044f8bf89318acfbd7449ebbe30` |
| Repaired `composition.py` SHA-256 | `f9c15e022627c12a1a9c8b7cbaf642fc396101fd2b0314e14b988456afff76d1` |

The wheel and its adjacent `.sha256` file are separate release assets: the
native methodology tag contains no Python project. No PyPI publication is
required. The runtime modules, both selected common successor schemas, tests,
version and manager documentation are bound by the freeze. Its 22 file hashes
were rechecked unchanged after packaging and the explicit adoption probe.

## Delivered behavior

The selected `stable-v1` profile requires a qualified annotated tag directly
naming a commit, the matching embedded tag name, and exactly one unindented
`STDO-Release-Profile: stable-v1` line. Same-version RC refs and historical bare
aliases refuse stable acquisition. The canonical stable manifest records
`release.profile = "stable-v1"`; stable channel resolution returns that exact
tag with a null ordinal. Historical RC manifest bytes and bare RC-line selector
meaning are preserved. Explicit stable-to-RC regression within one version
refuses; selecting another version remains an explicit consumer operation.

The composition fragment scanner now masks list/quote-contained fenced code
and an unfinished actual HTML comment. It retains the preceding physical-line
heading grammar: container normalization is for literal-block masking, not
new heading recognition. Literal comment openers in code spans, escaped text
or HTML attributes remain observable as text where appropriate. The a_c
Writer copied the exact helper algorithm under separate custody; the manager
has no runtime cross-product import.

## Evidence

| Evidence | Result |
|---|---|
| `focused-03.json` / `.log` | All 11 stable-acquisition tests pass, including marker uniqueness, annotation/embedded-name/direct-commit requirements, namespace collisions, legacy selector refusal, manifest/schema coupling, tamper and downgrade cases. |
| `repair-01/before-public-cli-02.json` | Both reported false anchors reproduced through `fleet verify`; the absent-anchor control refused. |
| `repair-01/after-public-cli.json` | Both counterexamples and the absent-anchor control refuse; genuine post-container and container HTML anchors pass. |
| `package-03/commands.json` | Exact commands, cleared Python import environment, exit codes and hashed logs for the complete package campaign. |
| `package-03/wheel-build-{1,2}.log` / `PACKAGE.json` | Two clean-source builds are byte-identical. Build tool versions and source timestamp are retained. |
| `package-03/wheel-import.log` / `wheel-cli.log` | Fresh isolated wheel installation reports 0.1.6; imports come from its `site-packages`, not the checkout. |
| `package-03/affected-suite.log` | **121 tests pass, zero skips**, 222.534 seconds. Includes toolchain, layout, native V3, cohort, composition, repository dogfood and stable-release tests. Public composition CLI fixtures use the installed wheel. |
| `package-03/legacy-301-manifest.log` | Actual immutable `v3.0.1-rc.1` reproduces canonical digest `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`, without a new profile field. |
| `package-03/stable-adoption.json` | Installed-wheel fixture proves explicit old-RC-to-stable adoption: dry-run is inert, unaccepted mutation refuses, the accepted exact plan changes only basis and schema, and the old installation remains valid. |

The original `CANDIDATE.json` and `package-01` / `package-02` runs remain
historical evidence. The first package attempt failed a proof-path comparison
(`/var` versus `/private/var`); the second passed 99 tests but had one test-module
loader error. Those were harness failures, not passing full campaigns. The
newly reported scanner repair then required a successor source freeze and
wheel. The package-03 campaign above is the final affected run.

## Reproduction and publication handoff

From the repository root, reproduce the package into a new evidence directory:

```sh
python3 -I -B specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/manager/build_wheel.py \
  --repository /Users/jim/src/apps/specification_methodology \
  --source-freeze /Users/jim/src/apps/specification_methodology/specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/manager/CANDIDATE-repair1.json \
  --output /Users/jim/src/apps/specification_methodology/specification_methodology/v3/.ai-workspace/work/STDO302_DELIVERY/manager/package-reproduction
```

Build script SHA-256:
`77057f12fee7929648ef9e845bd1b40e2eb789dbf2b99012e5661ef619bef38e`.
It obtains pinned build tools, checks every selected source hash before and
after, builds twice, installs into a fresh runtime venv and runs the affected
suite against that wheel. The probe script `probe_adoption.py` has SHA-256
`053f55b34acdf5144810728967ee19f6bd044ba56e89a69f823ddb1659942b7c`.

The existing proven runtime is retained for the Git Writer:

```sh
STDO302_PYTHON='/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/stdo302-manager-2ystgd7a/runtime-venv/bin/python'
STDO302_CLI='/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/stdo302-manager-2ystgd7a/runtime-venv/bin/stdo'
env -u PYTHONPATH -u PYTHONHOME "$STDO302_PYTHON" -I -B "$STDO302_CLI" --version
```

After the authorized native tag exists, use the same runtime against the
selected local repository, then repeat against the public repository after
publication. Bind the manifest digest from the reviewed native release record
rather than accepting an unexamined computed digest:

```sh
STDO302_REPOSITORY='https://github.com/foolishimp/specification_methodology.git'
STDO302_STORE='<new disposable test store>'
STDO302_MANIFEST='<reviewed native 3.0.2 manifest SHA-256>'
env -u PYTHONPATH -u PYTHONHOME "$STDO302_PYTHON" -I -B "$STDO302_CLI" \
  manifest v3.0.2 --repository "$STDO302_REPOSITORY"
env -u PYTHONPATH -u PYTHONHOME "$STDO302_PYTHON" -I -B "$STDO302_CLI" \
  --store "$STDO302_STORE" install v3.0.2 --repository "$STDO302_REPOSITORY" \
  --manifest-sha256 "$STDO302_MANIFEST"
env -u PYTHONPATH -u PYTHONHOME "$STDO302_PYTHON" -I -B "$STDO302_CLI" \
  --store "$STDO302_STORE" verify v3.0.2 --manifest-sha256 "$STDO302_MANIFEST"
env -u PYTHONPATH -u PYTHONHOME "$STDO302_PYTHON" -I -B "$STDO302_CLI" \
  --store "$STDO302_STORE" resolve stdo://releases/v3.0.2/standards/frames/bootstrap.md
```

For fresh acquisition, download the published wheel and checksum, compare
them to the wheel identity above, create a new venv and install that local
verified wheel. Retain its `site-packages` import path, distribution version
and downloaded wheel digest in the publication evidence; do not inject
checkout `PYTHONPATH` into these checks.

## Remaining ownership

Independent review, actual 3.0.2 native-tag acquisition, public reacquisition,
publication and release acceptance remain with the Executive and Git Writer.
This worker made no Git index/ref/commit changes, no push, no global manager
replacement and no consumer adoption outside disposable fixtures. No claim of
full Markdown-renderer coverage or semantic adequacy is made by fragment
resolution. The old matched-cohort updater contract remains unchanged.
