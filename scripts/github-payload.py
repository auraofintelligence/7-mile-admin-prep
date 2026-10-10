from pathlib import Path
import json,base64,sys
r=Path(__file__).resolve().parents[1]
files=[]
for f in sorted(r.rglob('*')):
 if not f.is_file() or any(p in {'.git','.openai','__pycache__','.private'} for p in f.relative_to(r).parts):continue
 if f.suffix in {'.tar','.gz','.zip'}:continue
 x={'path':str(f.relative_to(r)),'mode':'100644','type':'blob'}
 try:x['content']=f.read_text()
 except UnicodeDecodeError:
  if '--binary' not in sys.argv:continue
  x['base64']=base64.b64encode(f.read_bytes()).decode()
 files.append(x)
print(json.dumps(files))
