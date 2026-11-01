# Invoice export

Export rows as CSV with columns id, amount, currency in that order.
Preserve every supplied decimal digit in amount; binary floating-point conversion is forbidden.
For zero rows, emit the header alone.

## Unresolved rounding policy

Rounding is not yet specified. Retain this as unresolved; do not invent a rounding rule.
