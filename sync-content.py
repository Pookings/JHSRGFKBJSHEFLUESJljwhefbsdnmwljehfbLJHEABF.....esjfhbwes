"""Synchronize editable content.json into the browser content script."""
from pathlib import Path
import json
root = Path(__file__).resolve().parent
content = json.loads((root / 'content.json').read_text())
script = root / 'content.js'
marker = '\nwindow.shiruhValidateContent='
original = script.read_text()
if marker not in original:
    raise SystemExit('Missing content validator; content.js was not changed.')
output = 'window.SHIRUH_CONTENT=' + json.dumps(content, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c') + ';' + marker + original.split(marker, 1)[1]
script.write_text(output)
print(f'Synchronized {len(content["units"])} topics and {len(content["questions"])} questions.')
