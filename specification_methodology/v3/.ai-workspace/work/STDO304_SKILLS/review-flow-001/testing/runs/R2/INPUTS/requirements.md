# Export requirements

R-ARITH: Each invoice's net amount is quantity multiplied by unit_price. Tax is net multiplied by tax_rate; every amount in this fixture is exactly representable to two decimal places. Gross is net plus tax. Monetary values are decimal major currency units. Currency is AUD.

R-DATE: invoice_date is the calendar issue date rendered as YYYY-MM-DD, irrespective of the operator's locale. Source issue dates use that format.

R-IDENTITY: Every source invoice_id appears exactly once in the export, with its source quantity, unit_price, tax_rate and currency.
