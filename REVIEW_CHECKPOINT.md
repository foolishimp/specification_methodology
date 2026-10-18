# Full repository review checkpoint

This branch collects the current work for Jim's review on another machine. It contains the latest a_c implementation and evidence, the V3 common candidate, the Claude and Codex RC9 tenant trees, the V3-capable installer, and the existing peer source projects.

The branch is `review/2026-10-19-full-tree`. Existing source branches remain available separately. This publication is a checkpoint of work in progress; it grants no Product acceptance or release qualification.

## Open the checkpoint

For an existing clone:

```sh
git fetch origin
git switch --track origin/review/2026-10-19-full-tree
```

For a new clone:

```sh
git clone --branch review/2026-10-19-full-tree https://github.com/foolishimp/specification_methodology.git
```

## Review entrypoints

| Subject | Start here |
|---|---|
| a_c current implementation | [Graphify tenant](a_c/build_tenants/graphify/README.md), [F_D design](a_c/build_tenants/graphify/design/fd-support.md), [T-008](a_c/.ai-workspace/tickets/active/T-008-fd-tenant-implementation.md) |
| a_c qualification and review evidence | [T-008 evidence tree](a_c/.ai-workspace/qualification/t008/), [review record](a_c/.ai-workspace/comments/codex/20261019_AC_FD_TENANT_REVIEW.md) |
| V3 common candidate | [Method entry](specification_methodology/v3/build_tenants/common/standards/README.md) |
| Common construction status and owner choices | [Construction return](specification_methodology/v3/.ai-workspace/common-build/BUILD.md), [D1–D4](specification_methodology/v3/.ai-workspace/common-build/repair-1/DECISIONS.md), [28-item register](specification_methodology/v3/.ai-workspace/common-build/REGISTER.json) |
| Frozen comparison candidates | [Claude tenant](specification_methodology/v3/build_tenants/claude/), [Codex tenant](specification_methodology/v3/build_tenants/codex/) |
| Installer changes and proof | [V3 installer result](specification_methodology/v2/.ai-workspace/comments/codex/20261019T034_v3_installer/RESULT.md) |

[REVIEW_CHECKPOINT.json](REVIEW_CHECKPOINT.json) records the source commits and exact subtree identities. Each assembled a_c, installer, Claude, Codex, common and common-records subtree is byte-identical to its selected source tree. The only merge conflict was T-003's progress prose; the resolution preserves both the historical first-build record and the current construction return.

Main's a_c checkpoint is `bfe228511415d346459523cec44e7e8157e2991a`: 11,538 added or changed files, including implementation, design, tests and qualification evidence. Raw evidence is retained as recorded. Some test fixtures and historical receipts contain machine-local paths or symlinks; their presence is evidence custody, not a promise that old runs replay without their declared environment.

Existing Git ignores still exclude local virtual environments, caches and generated output directories. No implementation is changed or newly qualified by this repository assembly. V3 common's pending owner decisions and covering review remain open.
