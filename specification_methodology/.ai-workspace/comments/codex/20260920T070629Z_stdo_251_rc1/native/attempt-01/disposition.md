# Pre-exposure harness failure

All four contexts are retained without provider exposure. The `--contexts`
argument was relative, and the confinement probe passed its sibling sentinel
as `attempt-01/withheld.txt` into a subprocess rooted at the worksite. That path
did not exist there, producing ENOENT instead of the required access denial.

Every other probe succeeded: task/source readability, oracle denial, permitted
runtime writes, denied worksite writes, native versions, fixture execution,
pure joining and both map projections. Worksite snapshots remain unchanged.
The failure is in harness path resolution, not the candidate task or Product.

Resolve the selection path before constructing control paths. Prepare fresh
attempt-02 contexts and repeat their no-provider checks. No native semantic
result exists, no evidence is overwritten, and no provider retry is involved.
