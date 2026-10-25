# Compact author assessment — Claude tenant candidate (successor-1)

Subject: `urn:stdo-skills:T001:claude:candidate`. Producer: Worker
`skills.worker/1` rev 3. Activation `urn:stdo-skills:T001:claude:construction:3`.
These are Worker F_P author assessments, not independent review and not
actual-host qualification.

## Candidate inventory (package regular files, build_tenants/claude)

| path | sha256 |
|---|---|
| design/DESIGN.md | 767f29e03e9edf3bec7673d5bc5461c73d6dbd0d06dff8b0eef816d590c3a95e |
| skills/stdo-workspace-change/SKILL.md | 840bc1eeadcd575b15be7bc426a66f1407624a433ef49edf827671b9c1a6b3d1 |
| skills/stdo-tool-operations/SKILL.md | a850e36e8136b0db0d233d0bdfc4e8c6b4bc88949be5ea08cc7bb9c2ec4b09a0 |
| skills/stdo-delegate-review/SKILL.md | f8bd00924ad601c7e38d9c36eae95364246dab33d3f31fc6c2e8eea076b7b8cf |
| skills/stdo-continuation/SKILL.md | 90f3778a97df92796c8d052e4d46ca01e01b1913d3421fa8f421310d03c3cd61 |
| skills/stdo-release-install/SKILL.md | e29457bf87fd34032e3ad5339549888766b54ebff18cb97051a6293c547127c1 |
| INSTALL.md | 650a83518d996b83546be7b287e77e6aae08e88521831372e4ef66e61e909f60 |
| README.md | 8427582db2e83449700ec600bfb8ab48e922ead27930acde250ac5a5c066a4ce |
| tests/check_package.py | 5d05378a72322ac0d64c383a7b79d5fe9fb7c25378570ec0dc1cdfe65345a70c |
| INVENTORY.md | 63095869d5f4e2a5b85a9bec17598ebf0e683d0ae45bb06f4d1abc85821ba9c7 |

## tenant-instruction-fitness — satisfied (bounded author assessment)

Every SK-01..SK-12 has a coherent instruction path in an actual skill body; no
contradiction or material missing action was found. Required paths and the three
source-derived discriminators, with exact locations:

- SK-01 discovery + exclusion: `stdo-workspace-change` frontmatter `description`
  and "When this does not apply" (Q02: unrelated task is not forced into STDO).
- SK-02 basis: `stdo-workspace-change` "Verify the basis first" binds
  `stdo status --definition stdo_skills.json --verify` and the pinned manifest;
  ambiguous/missing/altered -> withhold (Q03).
- SK-03 / Q04 discriminator: "Proportional work" states a sufficient one-file
  authorized change proceeds directly as Writer with no invented ticket,
  coordinator, or review, and no out-of-scope write.
- SK-04 / Q06 discriminator: `stdo-tool-operations` "When a tool fails" retains
  an unsupported-method or execution error, withholds the dependent claim, names
  the next re-entry, and forbids manufactured success. Native `results.conjoin`
  named unsupported.
- SK-05: "Acquire only the deciding context" (equal bytes do not erase a retained
  obligation).
- SK-06, SK-07: `stdo-delegate-review` preserves basis/grant/territory/return and
  keeps reviewer independent and non-authoring (Q05).
- SK-08 / Q07 and Q08 discriminators: `stdo-continuation` "Resume and reconcile":
  identical candidate bytes with a retained counterexample yield different
  continuations; uncertain effect is reconciled before retry, no duplicate.
- SK-09, SK-12: "Status and closure" and "Capture evidence" keep candidate /
  indeterminate / not-performed distinct and keep unknown measures unknown.
- SK-10, SK-11: `stdo-release-install` prepares a release without inferring
  publication authority (Q11) and gives scoped install/update/remove (Q12).

Actual tool invocations and paths cited: a_c public CLI
`ac_support.py ... call --request -` with activation-sourced policy/principal/
grant (not embedded, so not single-use); `stdo status --definition
stdo_skills.json --verify` (manager present at /Users/jim/.local/bin/stdo);
discovery path `<workspace>/.claude/skills/<name>/SKILL.md`; install/update/
remove via real `mkdir -p`, `cp -R`, `rm -rf`, `sha256sum`. No invented
non-executable command was used.

Limits: this is author self-assessment. It does not claim automatic discovery,
runtime execution, independent review, or actual-host Q01-Q12 qualification.

## tenant-package-integrity — satisfied (observed finite checks)

The read-only verifier `tests/check_package.py` was executed
(`python3 -I -B ...`, rc=0, 35/35 checks) against the exact files on disk. It
confirmed: valid frontmatter and name/directory agreement for all five skills;
no symlinks; no other-tenant or personal-config path (`build_tenants/codex`,
`~/.claude`, `$HOME/.claude`); no markdown reference escaping a skill directory;
and `INVENTORY.md` agreeing with the files on disk (no missing, no extra, digests
match, 9 entries). The design was written first (record
`sha256:dd70edd8913b5f12058b02aff013d45c9052fc9442352816e661fd45a13b5ada`) before
the dependent skills; each artifact has a successful `work.write` record binding
it. Update/removal in INSTALL.md and `stdo-release-install` address only the
selected owned skill directories and preserve unrelated configuration.

Limits: these are finite package facts. Host installation/discovery behavior
(Q12) requires later isolated host proof; the presence of the verifier is
distinguished from its execution (the execution above is the evidence).

## Open residuals (not performed here)

- Actual-host Q01-Q12 qualification on Claude Code 2.1.306.
- Independent (fresh, ideally cross-family) review.
- Release publication and Product acceptance (owner decisions).
