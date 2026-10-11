# Independent Build Tenants

[Codex](codex/README.md) and [Claude](claude/README.md) implement one common [Product](../specification/PRODUCT.md) as documents. Their designs, prose organisation, optional a_c encodings and proof differ lawfully within shared semantics.

Jim owns common C1/C2 decisions. Codex currently holds the common construction pen. Tenant work follows [Development Isolation](../specification/PRODUCT.md#development-isolation): own branch, own sparse worktree, own territory. A tenant requests shared changes through the pen and never patches common WHAT, tickets or its peer's implementation.

## Initial Principles Task

Each tenant's task is READY / NOT_STARTED. C0 setup readiness is satisfied; activation still selects the shared [C1-inputs-20261011-02 snapshot](../.ai-workspace/tickets/active/T-001-common-definition-and-checkpoints.md#common-c1-input-snapshot). Parent-ticket completion is not a prerequisite. Explicit activation selects its own [backlog ticket](../.ai-workspace/README.md#work-records); this setup correction executes neither attempt.

Deliver one own design/PRINCIPLES.md containing:

- current-clause recovery with exact source routes and the selected interpretation;
- premises and dependency/derivation arguments;
- argued independence claims and unresolved hypotheses;
- contradictions, duplication, gaps and proposed corrections;
- candidate Spec Method mechanisms evaluated through five questions: requiring principle, performed transformation, conserved distinctions, admissible alternative HOW and observable adequacy.

The five questions organise this review; they are not universal mandatory template fields.

Construction territory is the tenant's own `build_tenants/<tenant>/`. Returns are recorded there (for example `qualification/RETURNS.md`) and mirrored to the common ticket by the pen. Reviews between tenants are authorised by Jim one at a time under [Development Isolation](../specification/PRODUCT.md#development-isolation): the reviewer reads the reviewed tenant's branch at a named commit, records source-first expectations before opening the candidate, writes only in its own tenant (for example `reviews/`), makes no repair and does not assess its own authored attempt. An actual Claude review must run as Claude and an actual Codex review as Codex. The C1 reciprocal reviews written before this rule into peer `qualification/C1_REVIEW.md` files and peer tickets are historical records, not a template.

Each activation verifies the current snapshot tuple from its input commit and the immutable builder basis before effects. Stop and rebind for material input changes; explicitly name any additional material source selected. Declared shared inputs outside the tenant's sparse cone are read with `git show <input-commit>:<path>`. Do not consume peer realisation except under an authorised review. Freeze the exact authored subject and retain its pin, basis, residuals and return in the tenant's own return record.

Tenant self-check is not acceptance. One reviewer GO cannot close the peer's task, C1 or C2. Jim resolves conflicts and decides one common principles basis; capability and steel-thread selection follows.

No full standards set, completed a_c program, worked example, trial, receipt hierarchy, universal numeric budget or runtime is required for C1.
