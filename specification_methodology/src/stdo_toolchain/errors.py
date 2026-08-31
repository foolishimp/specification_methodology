"""Typed failures surfaced by the STDO command-line interface."""


class StdoError(RuntimeError):
    """A deterministic STDO operation refusal."""
