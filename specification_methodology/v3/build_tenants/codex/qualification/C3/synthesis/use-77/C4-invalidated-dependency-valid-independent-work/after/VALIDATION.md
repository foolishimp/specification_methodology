# Validation records
| id | subject | check | basis | result |
|---|---|---|---|---|
| V1 | data/orders.json | conforms to schema | schema/orders.schema.json version 1 | pass (stale: basis superseded by schema/orders.schema.json version 2; replaced by V3) |
| V2 | data/customers.json | conforms to schema | schema/customers.schema.json version 1 | pass |
| V3 | data/orders.json | conforms to schema | schema/orders.schema.json version 2 | fail: items id 1 and id 2 lack required property "currency" |

Re-checked 2026-10-14 against the current workspace by manual inspection of file contents. No schema validator was executed. V2 holds: the basis is still version 1, and both items have "id" and "email". V3 fails.
