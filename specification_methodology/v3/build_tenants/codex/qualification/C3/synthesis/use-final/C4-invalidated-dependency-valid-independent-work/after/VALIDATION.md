# Validation records
| id | subject | check | basis | result |
|---|---|---|---|---|
| V1 | data/orders.json | conforms to schema | schema/orders.schema.json version 1 | pass (stale: schema/orders.schema.json is now version 2; superseded by V3, not a current pass) |
| V2 | data/customers.json | conforms to schema | schema/customers.schema.json version 1 | pass (re-checked against current workspace 2026-10-14; schema still version 1) |
| V3 | data/orders.json | conforms to schema | schema/orders.schema.json version 2 | fail: items id=1 and id=2 lack required property "currency" |

Notes (2026-10-14):
- V2 and V3 were checked by manual inspection of the current workspace files against each schema's `type` and `required` constraints. No schema validator was executed.
- V1 is kept as a historical result on its version 1 basis. It is not overwritten, and it is not a current pass.
- Resolving V3 needs either an orders data change or an orders schema decision by its owner. Neither is made here.
