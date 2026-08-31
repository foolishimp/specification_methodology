# T-003 - Enter The Specification Stack Monorepo

- id: T-003
- title: Enter the Specification Stack monorepo
- status: completed
- review_status: go
- change_class: realization_refactor
- re_entry_point: build_tenants/core/design/README.md
- owner: axiom_indexer
- work_authorization: direct_human_authorization_2026-08-31

## Outcome

- the exact source tree at `1fe3ef2af41b6df76d34d1a2fd1145d71e84a639`
  enters `axiom_indexer/` without squashing or rewriting history;
- the accepted `v0.1.0-rc.1` Product and tag object remain unchanged and
  reachable through a project-qualified archival ref;
- project-local native skill links and all relative Product paths still work;
- a root native skill link may expose the same unchanged canonical skill; and
- Product meaning, validation behavior, join behavior, and release claims do
  not change.

## Refusal

Refuse any implicit composition, mutable-sibling dependency substitution,
copied Product member, rewritten history, changed release object, root Product
authority, or unqualified future tag collision.

## Closure Evidence

- Import commit `4c835cd971c1b641ae2f20fc09565b6546c77e9d`
  contains subtree tree
  `ae10199814a5a61ea93fc0adfac986c29273c5dd`, equal to the frozen source
  tree.
- Source commit `1fe3ef2af41b6df76d34d1a2fd1145d71e84a639` remains an ancestor.
- Accepted annotated tag object
  `e7afc8a42a7123aebe91cb7582cb037b1aae612d` remains reachable at
  `refs/tags/legacy/axiom_indexer/v0.1.0-rc.1` and peels to the unchanged
  release commit.
- Project-local and root skill discovery links resolve to the same canonical
  skill.
- The complete MVP suite passes normally and under optimized Python; lint,
  formatting, JSON, and skill checks pass.
- Fleet verification reports the Axiom Indexer Product Definition valid and
  independent.
