# Specification Methodology

This source project constructs the next major release of Specification Methodology. One common specification governs the independent Codex and Claude realisations under `build_tenants/`. The installed STDO 2.5.1 RC2 release governs construction; the existing 2.* source and released products remain separate.

## Start

1. Resolve [stdo_3.json](stdo_3.json), verify its exact installed basis and load its declared bootstrap entrypoint.
2. Read [Intent](specification/INTENT.md), [Product](specification/PRODUCT.md) and the current selection in [Goals](specification/GOALS.md).
3. Bind the applicable [reference frame](specification/REFERENCE_FRAME_BASIS.md) and work grant: [T-001](.ai-workspace/tickets/active/T-001-common-definition-and-checkpoints.md) for the common definition, or [T-002](.ai-workspace/tickets/active/T-002-c3-successor-construction.md) and its tenant ticket for construction.
4. For tenant work, follow the [tenant entry contract](build_tenants/README.md), including its selected input snapshot, isolation and admission requirements.

Codex holds the common pen. Common acceptance and release selection remain the product owner's decisions. Current checkpoint and review state are recorded in Goals; neither this entry route nor a checkpoint commit starts tenant work.

## Historical Inputs

The [bootstrap review](.ai-workspace/comments/codex/20261011T041334Z_REVIEW_STDO_3_BOOTSTRAP.md) records the setup review. The [working principles and C1 disposition](specification/requirements/PRINCIPLES.md) retain the principles review and each tenant's accepted C1 basis.

The [6 October documented-coverage matrix](../v2/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md) and the [Product-direction draft](../v2/.ai-workspace/comments/codex/20261006T010215Z_STRATEGY_STDO_3_0_WORKING_PRODUCT_DEFINITION.md), [Claude plan](../v2/.ai-workspace/comments/claude/20261011T033759Z_STRATEGY_stdo_3_0_steel_thread_implementation_plan.md) and [Codex plan](../v2/.ai-workspace/comments/codex/20261011T033457Z_STRATEGY_STDO_3_0_FOUNDATIONS_STRUCTURE_AND_PLAN.md) are preserved construction inputs. Their historical snapshots bind their original activations; current work uses the input contract selected in its work grant.
