# Converter design

Product duration conversion is realized by DurationMilliseconds -> declared division by 1000 -> DurationSeconds. Unknown or unsupported units return explicit unresolved/unsupported handling. Field shape does not establish domain compatibility. This local design does not impose a vendor namespace or amend Product meaning. Focused checks and affected integration proof remain required.
