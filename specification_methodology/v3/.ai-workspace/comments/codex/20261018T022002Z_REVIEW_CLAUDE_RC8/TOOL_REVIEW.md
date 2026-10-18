# Claude RC8 tooling and local package review

**Overall result: satisfied for the selected tooling and local package-identity
expectations. No new finding in those repairs.** This closes the bounded
enumeration, freeze-order and manifest-identity readback, not C3 acceptance,
semantic qualification, native installation or publication.

Source A is `9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e`; records B are
`1db13bfeb0675fc95de04aceccb214f5b76873fc`. The baseline is candidate 5 A
`4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec` / B
`a85f9ec98e43b942048a6c151aafd9662d2def90`. Source references below are
relative to `specification_methodology/v3/build_tenants/claude/` at A.
The fixed builder v2.5.1-rc.2 verified with no failures at manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

[TOOL_EXPECTATIONS.md](TOOL_EXPECTATIONS.md) was written before candidate
bodies or diffs. The reviewing actor did not author Claude's repaired tools.
Codex's competing-line authorship and prior defect reporting remain disclosed
by the parent activation. Three previous reviewer harnesses were inspected
for their mechanism and limits; their old results were not carried forward as
RC8 evidence. The narrowed probes below execute frozen scripts in new scratch
copies. The author's package was read for coordinates and navigation after
independent expectations and source inspection.

## Executed boundary evidence

[probe.py](tool-evidence/probe.py) and its
[receipt](tool-evidence/probe-receipt.json) retain commands, exits, expected
outcomes and observations. Full stdout/stderr are beside the receipt.

| Case | Independently observed result |
|---|---|
| Complete positive freeze with an actual consumers-output change | Exit 0; 10 projections; seven required controls hold; all 16 README pins match final bytes. The consumers digest changes from `a5ab74aa…` to `b7bac097…`, and the final README pin equals the latter. |
| Enumeration process fails, exit 37 | Real validation succeeds; wrapper exits 1; no project command or projection file follows. |
| Enumeration emits a usable index then fails, exit 37 | Wrapper exits 1 and performs no projection; partial stdout does not erase failure. |
| Enumeration succeeds with empty stdout | Wrapper exits 1 and performs no projection. |
| Enumeration fails inside complete freeze | Complete wrapper exits 1 before copying tenant artifacts; stale scratch projection is removed; none of the observed tenant artifacts changes. |
| A required control is forced to fail inside complete freeze | Complete wrapper exits 1; only `identity-positive` is recorded false. Consumers and README refresh are not reached. Earlier artifact copies and the failing control report remain. |

The source explains these observations: `run_ac.sh:8–9` captures enumeration
status separately and refuses failed or empty output before its projection
loop. The prior validate/project failure accumulator remains intact at lines
5 and 14. `freeze_ac.sh:5` preserves pipeline failure, while lines 14–25 run
controls, regenerate consumers and only then refresh artifact pins. The
[exact diff](tool-evidence/tool-diff.patch) shows those changes against
candidate 5.

The consumers-order probe uses the supported optional `consumer_readings.json`
input for a real frozen consumer link, retaining `support=cites` and changing
only the emitted basis text. This is an ordering probe; it supplies no semantic
judgment. The initial harness incorrectly assumed that optional file existed
and stopped before any candidate command. The
[setup correction](tool-evidence/harness-correction.json) records that
harness-only error.

The failed-control path is sequential, not transactional. Source lines 10–13
copy validation, map, projections and command log before controls run. In the
probe, validation-report bytes replace a sentinel, checker-commands.log changes,
and `ac_controls.json` records failure; consumers and README bytes remain
unchanged. Map and projection bytes already match the regenerated versions,
so unchanged hashes do not establish that no copy occurred. Exit 1 withholds
successful freeze completion. No all-or-nothing filesystem claim is made.

## Frozen identity and digests

[package_probe.py](tool-evidence/package_probe.py) independently recomputes the
manifest membership and hashes before executing the candidate manifest builder.
Its [receipt](tool-evidence/package-receipt.json) establishes:

- B's manifest SHA-256 is
  `2f3b79e0c7015887c471747b9d9ea6e298f66b5d2290124a09243e77018c2d7c`.
  The current `build_manifest.py` reproduces those bytes exactly.
- All 62 standards and 17 plugin members match source A, without missing or
  duplicate entries; license and release-note digests also match. The standards
  aggregate is `dd1871e87f548dcd955468a7711c47b5d15f931ddbb0dcaff958bb760e3b5211`.
- The local qualified ref names annotated tag object
  `08555a3b6f09df0a0297e59932dc7b6a967582bd`, which peels to A. B is A's direct
  child. Repository tree, tenant subtree, standards tree and namespace fields
  agree with the named objects; both plugin manifests identify `3.0.0-rc.8`.
- A and B have identical standards, plugins, a_c, license, release-note and
  manifest-builder bytes. B changes only the recorded package/handoff surfaces
  listed in the receipt. Manifest shape validates against its admitted schema.

The only manifest-builder diff against candidate 5 changes the cut and
qualified-ref labels to RC8; the current labels and generated coordinates were
checked independently. The [original pin probe](tool-evidence/pin_probe.py) and
[receipt](tool-evidence/pin-receipt.json) additionally verify all 16 README
artifact pins directly from A, before any scratch regeneration.

## Limits and containment

All executions used absolute `/private/tmp/` scratch paths. The unchanged
`verify_ai.sh:3–8` changes directory to the Claude checkout for read-only Git
acquisition and then writes through `$AI`, which is derived from `$SP`. An
absolute `$SP` keeps materialization in scratch. A relative `$SP` would resolve
the later writes under that hardcoded checkout. That existing path dependency
was not exercised against the live peer, is not an RC8 regression, and is not
qualified by this result. The candidate scripts themselves were not patched.

The local tag's identity was checked; remote presence or absence was not.
The source's statement that the tag is unpushed is therefore an author record,
not an independently verified remote-publication result. No native installer,
activated consumer, broader unchanged author suite or external paid call ran.
Manifest membership and hashes do not establish source fidelity or satisfy
C3's six member criteria. Generated frame-content comparisons and semantic
consumer/owner judgments belong to the parent and semantic reviews.

[Measurements](tool-evidence/measurements.json) record 154,977 emitted source
bytes (151.3 KiB, including repeated reads and the inspected prior harnesses),
within the 384 KiB envelope. Some tool outputs were truncated; the emission
count conservatively bounds source presented and is not a retained-context
measurement. The package probe mechanically acquired 3,555,476 blob bytes;
that is separate from model-presented source. Initial host context, metadata
listings and total runtime I/O are not fully metered, so no context-fit claim
follows. The measurement was taken 484.3 seconds after the expectations file
was created; the 20-minute checkpoint was not reached. External paid calls:
zero. Candidate, common and Git-ref effects: none performed.
