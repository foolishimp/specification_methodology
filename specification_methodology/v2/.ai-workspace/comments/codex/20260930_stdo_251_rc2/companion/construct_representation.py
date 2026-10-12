"""Reuse the prior qualified construction recipe with explicit RC2 coordinates.
Only this release input binding changes; no new Product mechanics are added.
"""
from pathlib import Path
source = Path(__file__).resolve().parents[2] / "20260920T070629Z_stdo_251_rc1/companion/construct_representation.py"
text = source.read_text().replace("2.5.1-rc.1", "2.5.1-rc.2").replace("2.5.0-rc.7", "2.5.1-rc.1").replace("RC1", "RC2").replace("rc1-", "rc2-")
exec(compile(text, str(source), "exec"))
