# Release preparation and scoped deployment

Acquire RELEASE.md and IDENTITY.md from the verified installation and the target Product's release conditions. Bind exact candidate inventory, evidence, acceptance/disposition requirements, destination and publication grant. With a preparation-only grant, assemble a reviewable local artifact and return it; no remote publication follows. Do not invent a second final cut to fix an identity problem. Discover and actually use the release tool contract selected by that Product; unsupported release tooling leaves publication unperformed.

This skill's deployment unit is the entire stdo-work directory. Its repository-local destination is exactly TARGET/.agents/skills/stdo-work. It neither installs the Claude tenant nor modifies host defaults. The tenant README documents the executable package verifier and copy recipe. At deployment time:
1. Freeze the package inventory, verify all ordinary regular files and internal resources, and retain the chosen identity outside the discovery directory.
2. Verify the target grant and every destination ancestor: no symlink, escape or unexpected existing stdo-work. Resolve duplicate skill names deliberately; names are not merged.
3. Install only that directory. Record destination, exact file inventory and old/new package identities in the authorized work surface.
4. Open Codex in that workspace. Exercise ordinary discovery and explicit $stdo-work invocation as separate trials. Confirm acquisition and required tool events. If stale, restart and retain the failed discovery attempt.
5. For update, compare the entire installed file set and hashes to the retained old receipt before replacement. If locally changed or ownership unknown, stop that replacement and report the conflict; do not overwrite it. Retain the old package outside all discovery roots and its identity for deliberate rollback.
6. Remove only the owned selected stdo-work directory after the same receipt check. Preserve .agents/skills, other skills and configuration. Unknown files or hashes block destructive removal. Recheck the remaining unrelated configuration.

These instructions specify a deployable path. Finite package checks do not prove discovery, actual installation, update or removal behavior; Q12 remains open until performed in an authorized disposable host workspace. Installation does not constitute method adoption or Product acceptance.
