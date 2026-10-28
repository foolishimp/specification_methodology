"""Review marker: delegate all real behavior to the unchanged flat helper."""
from pathlib import Path
import importlib.util
_marker = Path(__file__).resolve().parents[3] / 'package-executed.txt'
_marker.write_text(str(Path(__file__).resolve()) + '\n')
_original = Path(__file__).resolve().parents[1] / 'import_fixture.py'
_spec = importlib.util.spec_from_file_location('_review_original_import_fixture', _original)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({name: value for name, value in vars(_module).items() if not name.startswith('__')})
