from pathlib import Path
from html.parser import HTMLParser
import json,re
R=Path(__file__).resolve().parents[1];D=R/'dist';p=json.loads((D/'plan.json').read_text())
for name in ('docs','tasks','refs'):
 ids=[x['id'] for x in p[name]];assert len(ids)==len(set(ids)),name
ids={x['id'] for x in p['docs']};tids={x['id'] for x in p['tasks']};rids={x['id'] for x in p['refs']}
for d in p['docs']:
 assert set(d['depends'])<=ids and set(d['sources'])<=rids
 assert 'C-Hours have no financial aspect' in d['prompt']
 assert (D/('document-'+d['id']+'.html')).exists()
 assert (D/('prompts-'+d['id']+'.txt')).read_text()==d['prompt']
for t in p['tasks']:assert t['document'] in ids and set(t['depends'])<=tids
seen=set();active=set()
def walk(id):
 assert id not in active,'Dependency cycle '+id
 if id in seen:return
 active.add(id)
 for v in next(x for x in p['tasks'] if x['id']==id)['depends']:walk(v)
 active.remove(id);seen.add(id)
for t in p['tasks']:walk(t['id'])
for c in p['checklists']:assert set(c['tasks'])<=tids
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('href','src') and v and not v.startswith(('http:','https:','#','mailto:','data:')):
    v=v.split('?')[0].split('#')[0]
    assert (D/v).is_file(),str(self.file)+' missing '+v
for f in D.glob('*.html'):
 l=Links();l.file=f;l.feed(f.read_text())
 assert 'route-nav' in f.read_text() and 'top-button' in f.read_text()
 assert 'AI-generated concept art' in f.read_text()
print(f"Validated {len(list(D.glob('*.html')))} pages, {len(p['docs'])} prompts, task dependency DAG, identifiers and local asset links.")
