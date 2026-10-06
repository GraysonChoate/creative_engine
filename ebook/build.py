# Build Directing-the-Engine.html from content.json (edit the JSON, then run: python3 build.py)
import json,pathlib
d=pathlib.Path(__file__).parent
data=json.dumps(json.loads((d/"content.json").read_text()),ensure_ascii=False).replace("</","<\\/")
(d/"Directing-the-Engine.html").write_text((d/"template.html").read_text().replace("__DATA__",data))
