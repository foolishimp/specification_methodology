# Retained prior composition verification probe

Producer: `/root/composition_tool_probe`, independently run before this proposal.
Original root: `/var/folders/rz/r6wxvr0n15d906k2s0jw8j2h0000gn/T/stdo-composition-probe-wx4e8fnm`.
The [results](results.json), [tool/source pins](pins.json) and
[fixture hashes](fixture-file-hashes.json) are byte-exact copies. The
[command index](commands.json) groups the original parsed command records by case.
[original-probe.zip](original-probe.zip) preserves all original fixture and run
files byte-exact, including stdout, stderr, commands and independent audits.

Fixtures are archived because `stdo fleet` discovers `stdo_*.json` inside
`.ai-workspace` too. Keeping those synthetic definitions loose here would introduce
extra Products and repeated identities into this workspace. The archive creates
no live Product definitions.

This is retained evidence, not a new run. The original commands and output contain
the original absolute paths. Extraction into a different location requires an
explicitly adapted replay; it is not a bit-for-bit rerun of the old command. Do
not extract into a live discovery root. The source-selected future manager repair
must produce its own post-repair evidence.

All five prior cases returned exit 0 and valid definitions. The valid control's
references resolve; each adverse fixture independently establishes one defect.
The four broken-edge passes demonstrate the missing `fleet verify` checks, not
satisfaction of the proposed required behavior.
