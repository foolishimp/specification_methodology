"""Reuse the established public reacquisition recipe on the selected RC2 cohort."""
from pathlib import Path
source = Path(__file__).resolve().parents[1] / '20260915T093130Z_rc7_release/reacquire_public.py'
text = source.read_text().replace('2.5.0-rc.7', '2.5.1-rc.2').replace('"0.1.3"', '"0.1.4"')
text = text.replace('"/representation-index-commands.json"', '"/companion/construction-commands.json"')
text = text.replace('if recipe["label"] == "validate":', 'if not recipe["label"].startswith("project-"):')
text = text.replace('"/representation-projections/" + recipe["label"] + ".json"', '"/companion/projections/" + recipe["label"].removeprefix("project-") + ".json"')
text = text.replace('len(projections) == 10', 'len(projections) == 12')
exec(compile(text, str(source), 'exec'))
