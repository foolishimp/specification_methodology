# C3S-01 Frame usability: REFERENCE_FRAME, tasks A and B

Identity: `urn:stdo-3:claude:case:C3S-01`. This is a case of the Claude tenant's C3 cross-synthesis rebuild. Status: oracle written; no frame and no run exist.

## Claim under test

A fresh actor given only the frame and the task applies the REFERENCE_FRAME member correctly. The actor receives exactly three things: a routing card that carries no method content, one frame as its only method source, and one task. It has no tools, no memory and no repository. It returns what the task asks for, and the determinations it applies are the member's as the frame carries them, with the result values stated in the core result algebra or the frame's mapping into it.

## Frames to be given

There is one frame per task. Each will be generated later from the candidate. Its identity, bytes and SHA-256 are recorded here when it is generated, and before any run.

| Task | Frame | What the task exercises |
|---|---|---|
| A | REFERENCE_FRAME for C3S-01 task A | the minimal frame declaration; activation on an exact subject and basis; the minimal evaluation result with one result value and its inference relation; authority separation for an owner's claim |
| B | REFERENCE_FRAME for C3S-01 task B | the coverage tuple, ledger fields and statuses; the diagnostic order on a missing-frame signal; one revision action and what it reopens |

## Tasks

Each task is copied verbatim from an existing fixture. The copy is byte-identical to its source.

| File | Source path (tenant-relative) | SHA-256 | Bytes |
|---|---|---|---|
| [TASK-A.md](TASK-A.md) | `qualification/cases/F-01/TASK-A.md` | `93b314b26c7691ab996ca8bc0bff6ec66e7d9b0deb135d129ac034f51b7624d5` | 3,136 |
| [TASK-B.md](TASK-B.md) | `qualification/cases/F-01/TASK-B.md` | `48b2ebd6db468597410cf4f72f54c406025256e248938fbf02d5262e266ef41e` | 3,985 |

## Oracle

[EXPECTATIONS.md](EXPECTATIONS.md) was written on 2026-10-14 by oracle activation C3. It was written before any frame or run existed for this case. The writer read no candidate text.

- Read: the F-01 task, case and card files. The installed predecessor release `v2.5.1-rc.2` (REFERENCE_FRAME_METHOD, AXIOMATIC_CALCULUS, TRAVERSAL_OCCURRENCE_PROFILE, and the cited IDENTITY_METHOD and SPEC_METHOD sections). The common `specification/requirements/README.md` and `specification/conformance/README.md`. The rebuild ledger.
- Not read: anything under the tenant's `standards/`, `a_c/`, `frontier/` or `design/`; the fixtures' earlier `EXPECTATIONS.md`; any run output; the C3-SYNTHESIS reviews.

The worktree head at the time of writing was `bafb3f90885525cb3b56c794851e02a92f412337` on `tenant/claude/c3-synthesis`.

## Runs and assessments

| Run | Frame digest | Record | Assessment |
|---|---|---|---|
| none | | | |

An assessor other than the frame's author reads a run record after this oracle exists. It judges each record against the expectations and makes no repair.
