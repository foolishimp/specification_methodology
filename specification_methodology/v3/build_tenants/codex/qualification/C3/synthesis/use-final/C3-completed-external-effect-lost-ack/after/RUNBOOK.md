# Runbook
Deploy requests are not idempotent: every line appended to outbox/requests.jsonl starts a new rollout.
external/deploy_registry.json is mirrored read-only from the deploy service and is its authoritative record of rollouts.
