# Converter design

Product output is seconds. The producer provides metres as scalar float.
The consumer accepts seconds as scalar float. Equal field shapes establish compatible composition.
Unknown source units are coerced to zero. A successful typecheck proves Product adequacy.
This helper also requires that all applications use the implementation vendor namespace.
