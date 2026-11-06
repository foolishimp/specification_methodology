"""Read-only containment against an existing filesystem object.

Path.resolve() preserves case spellings on some case-insensitive filesystems.
Compare filesystem identities instead; never infer identity by case folding.
These cooperative checks do not protect against concurrent path replacement.
"""
from pathlib import Path


def overlaps_existing(candidate: Path, protected: Path) -> bool:
    """Return whether either path contains the other, including physical aliases.

    The protected object must exist. A future candidate is checked through its
    existing ancestors. Only absence is ignored; inaccessible or malformed
    paths raise rather than being treated as disjoint. No filesystem effects
    or directory probes are performed.
    """
    protected = Path(protected).resolve(strict=True)
    protected_stat = protected.stat()
    protected_identity = (protected_stat.st_dev, protected_stat.st_ino)
    candidate = Path(candidate).resolve(strict=False)
    candidate_identity: tuple[int, int] | None = None
    for ancestor in (candidate, *candidate.parents):
        try:
            observed = ancestor.stat()
        except FileNotFoundError:
            continue
        identity = (observed.st_dev, observed.st_ino)
        if ancestor == candidate:
            candidate_identity = identity
        if identity == protected_identity:
            return True
    if candidate_identity is not None:
        for ancestor in protected.parents:
            observed = ancestor.stat()
            if (observed.st_dev, observed.st_ino) == candidate_identity:
                return True
    return False

# changed dependency
