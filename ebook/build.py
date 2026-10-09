# Build the ebook HTML from a content JSON.
#   python3 build.py                 -> Directing-the-Engine.html   (agent edition, from content.json)
#   python3 build.py me              -> Directing-the-Engine-Me.html (personal edition, from content-me.json)
import json,pathlib,sys
d=pathlib.Path(__file__).parent
ed=sys.argv[1] if len(sys.argv)>1 else "agent"
cfg={"agent":("content.json","Directing-the-Engine.html","Directing the Engine","How to tell Claude and Higgsfield what you see in your head. Pick a tab, copy a phrase, use it."),
     "me":("content-me.json","Directing-the-Engine-Me.html","Directing the Engine: My Manual","Your seat in the Creative Engine. What you do, what to look for, what to say. Pick a tab.")}[ed]
data=json.dumps(json.loads((d/cfg[0]).read_text()),ensure_ascii=False).replace("</","<\\/")
html=(d/"template.html").read_text().replace("__TITLE__",cfg[2]).replace("__SUB__",cfg[3]).replace("__DATA__",data)
(d/cfg[1]).write_text(html)
print("wrote",cfg[1],len(html))
