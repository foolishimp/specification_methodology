# Validation records
| id | subject | check | basis | result |
|---|---|---|---|---|
| V1 | data/orders.json | conforms to schema | schema/orders.schema.json version 1 | pass (stale: schema/orders.schema.json is now version 2; superseded by V3, not a current pass) |
| V2 | data/customers.json | conforms to schema | schema/customers.schema.json version 1 | pass |
| V3 | data/orders.json | conforms to schema | schema/orders.schema.json version 2 | fail |

Notes (re-observation of current workspace, 2026-10-14):
- V1: the recorded pass was against schema version 1. The current schema is version 2 and adds "currency" to `required`, so V1 no longer describes the current basis. Its original pass is kept for history and is superseded by V3.
- V2: rechecked against schema/customers.schema.json version 1 (unchanged). The data is an array of objects, and every item has "id" and "email". The record remains a current pass.
- V3: data/orders.json item id 1 and item id 2 both lack the required "currency" property, so the data fails version 2 of the schema.
- Method: V2 and V3 were checked by manual inspection of the schema keywords present (type, items.type, items.required). No JSON Schema validator was run.
