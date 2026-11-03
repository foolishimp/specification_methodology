"""Adjacent whitespace discriminators, fixed without successor exposure."""
import importlib.util
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('raw_probe', HERE / 'probe_cli.py')
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
probe.HERE = HERE / 'adjacent'
probe.HERE.mkdir(exist_ok=True)


def specimens():
    headings = [{'heading': 'One', 'level': 2, 'first_line': 1, 'unique': True},
                {'heading': 'Two', 'level': 2, 'first_line': 5, 'unique': True}]
    first = '## One\nkept\n##\u00a0\nmore kept\n'
    second = '## One\nparagraph\n===\u00a0\nmore kept\n'
    return [
        {'name': 'NBSP-after-empty-ATX-marker', 'text': first + '## Two\nexcluded\n',
         'outcome': 'projection', 'one_text': first, 'one_last_line': 4, 'headings': headings},
        {'name': 'NBSP-after-setext-looking-line', 'text': second + '## Two\nexcluded\n',
         'outcome': 'projection', 'one_text': second, 'one_last_line': 4, 'headings': headings},
        {'name': 'NBSP-nonblank-before-real-setext', 'text': '## One\n\u00a0\n===\n## Two\nexcluded\n',
         'outcome': 'refuse'},
    ]


probe.specimens = specimens
probe.main()
