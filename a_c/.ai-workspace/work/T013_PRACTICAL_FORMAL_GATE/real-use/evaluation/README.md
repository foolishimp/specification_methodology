# Withheld evaluation material

This directory is for the independent evaluator after both Worker outputs are
frozen. It is not copied into either task workspace, declared as a Worker source,
or rendered into either Worker Context. The Workers must not access it.

`CASES.json` declares eight discriminator families. Its inputs are authored or
explicitly derived test data, not fresh gate receipts. Run the candidate's public
command on them in a disposable evaluator workspace and retain actual exit,
stdout, stderr and duration. Check raw SHA-256/byte length independently, compare
the complete parsed `reported` value, and assert the listed summary/cost/standing
fields. Malformed-input cases must return exit 2 and empty stdout. Also run the
genuine shared examples and the Worker's tests, but independently inspect the
implementation, documentation and test coverage.

Do not repair either candidate or supply one candidate's output to the other.
Review source-derived expectations without adopting the constructor's self-test
verdict as acceptance. Record additional justified cases and reasons separately.
The evidence supports this task's behavior, not general semantic completeness.
