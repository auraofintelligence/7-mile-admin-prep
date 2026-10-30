from pathlib import Path
from html.parser import HTMLParser
import json,re
R=Path(__file__).resolve().parents[1];D=R;p=json.loads((D/'plan.json').read_text())
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
for t in p['themes']:
 assert set(t['documents'])<=ids and set(t['tasks'])<=tids
 assert t['checklist'] in {c['id'] for c in p['checklists']}
 assert t['source'].startswith(p['provenance']['original'])
for e in p['estimates']:assert e['document'] in ids
assert (D/'plan.html').exists()
assert len(p['themes'])==13
assert all('permanent residents' in d['prompt'] and '7-Mile is on a native title claim' in d['prompt'] for d in p['docs'])
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('href','src') and v and not v.startswith(('http:','https:','#','mailto:','data:')):
    v=v.split('?')[0].split('#')[0]
    assert (D/v).is_file(),str(self.file)+' missing '+v
for f in D.glob('*.html'):
 l=Links();l.file=f;l.feed(f.read_text())
 assert 'route-nav' in f.read_text() and 'top-button' in f.read_text()
 assert 'data-page="'+f.name+'"' in f.read_text()
 assert 'class="concept"' not in f.read_text()
 canonical='https://auraofintelligence.github.io/7-mile-admin-prep/'+('' if f.name=='index.html' else f.name)
 assert '<link rel="canonical" href="'+canonical+'">' in f.read_text()
 assert 'chatgpt.site' not in f.read_text()
 assert 'location.search+location.hash' in (D/'dist'/f.name).read_text()
assert 'chatgpt.site' not in (R/'README.md').read_text()
assert 'Sitemap: https://auraofintelligence.github.io/7-mile-admin-prep/sitemap.xml' in (D/'robots.txt').read_text()
import xml.etree.ElementTree as ET
urls=ET.parse(D/'sitemap.xml').getroot()
assert len(urls)==len(list(D.glob('*.html')))
print(f"Validated {len(list(D.glob('*.html')))} pages, {len(p['docs'])} prompts, task dependency DAG, identifiers and local asset links.")
