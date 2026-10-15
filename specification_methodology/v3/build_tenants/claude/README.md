# Claude Build Tenant

Identity: urn:stdo-3:build-tenant:claude

This tenant realises the shared [Intent](../../specification/INTENT.md) and [Product](../../specification/PRODUCT.md) as an independent document HOW, under [Development Isolation](../../specification/PRODUCT.md#development-isolation) on the branch `tenant/claude/c3-synthesis`. Do not read the peer tenant's realisation except under an authorised review at a named frozen commit.

## Current state

Iteration 4 of the C3 construction, on the ratified common input C3-I4-03 (`3c4c503`). The work record is the [ledger](qualification/C3-SYNTHESIS/LEDGER.md), section "Iteration 4"; the plan and returns are under [qualification/C3-ITER4/](qualification/C3-ITER4/PLAN.md), and the handoff for the frozen candidate is written there at the freeze. The candidate's law is [standards/](standards/README.md), whose README routes each task to its deciding sections; its frames are [standards/frames/](standards/frames/FRAME_INPUTS.json); its current formal interpretation is [a_c/i3/](a_c/i3/README.md); its design is [design/](design/README.md); its frontier record is [frontier/PREDECESSOR_CLAIMS.md](frontier/PREDECESSOR_CLAIMS.md) with the review record `frontier/REVIEW.json`. Nothing in this tenant is accepted; acceptance standing comes only from the common tickets.

## History

The earlier states are recorded, not current: C1 (the initial principles, [design/PRINCIPLES.md](design/PRINCIPLES.md); the historical Codex review `qualification/C1_REVIEW.md` predates the isolation rule); the threads T1 to T4 and their cases under [qualification/cases/](qualification/cases/) with the historical programs under [a_c/](a_c/README.md); the first C3 pass, merged to `main` at `d276de2` for visibility and found to route to rc.2 instead of restating it; the C3 synthesis and iteration 3 under [qualification/C3-SYNTHESIS/](qualification/C3-SYNTHESIS/LEDGER.md) and [qualification/C3-ITER3/](qualification/C3-ITER3/HANDOFF.md), whose frozen candidate `2beed8d` is this iteration's preceding candidate. [qualification/RETURNS.md](qualification/RETURNS.md) and [qualification/REVIEW_HANDOFF.md](qualification/REVIEW_HANDOFF.md) are the historical return and review routes of those states.
