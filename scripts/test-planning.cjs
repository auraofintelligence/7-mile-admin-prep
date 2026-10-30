const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const data=JSON.parse(fs.readFileSync(path.join(root,'plan.json'),'utf8'));
const code=fs.readFileSync(path.join(root,'app.js'),'utf8').split('if(docid){')[0];
function render(call,search=''){
 const elements=new Map();
 function node(key){if(!elements.has(key))elements.set(key,{innerHTML:'',value:'',textContent:'',addEventListener(){},querySelectorAll(){return []},scrollIntoView(){}});return elements.get(key)}
 const document={body:{dataset:{page:'index.html'}},querySelector:node,getElementById:node};
 const context={window:{PLAN:data},document,location:{pathname:'/',search},localStorage:{getItem(){return null}},URLSearchParams};
 vm.runInNewContext(code+'\n'+call,context);
 return {main:node('#content').innerHTML,results:node('#results').innerHTML,detail:node('#checklist-detail').innerHTML};
}
for(const call of ['overview();','originalPlan();','sitemap();','documents();','decisions();','references();','agencies();','tasks();','checklists();']){
 const out=render(call);assert.ok(out.main.length>200,call);
 for(const markup of Object.values(out))for(const match of markup.matchAll(/(?:href|src)="([^"]+)"/g)){
  const url=match[1];if(!/^(https?:|#|data:)/.test(url))assert.ok(fs.existsSync(path.join(root,url.split(/[?#]/)[0])),call+' missing '+url);
 }
}
for(const d of data.docs){const out=render('documentDetail(P.docs.find(d=>d.id==='+JSON.stringify(d.id)+'));');assert.ok(out.main.includes(d.title),d.id);assert.ok(out.main.includes('REFERENCE LINKS:'),d.id+' prompt links')}
for(const theme of data.themes){
 const out=render('tasks();','?theme='+theme.id);
 const ids=[...out.results.matchAll(/data-status="(T\d+)"/g)].map(m=>m[1]);
 assert.deepEqual(ids,theme.tasks.filter(id=>data.tasks.find(t=>t.id===id)).sort((a,b)=>data.tasks.findIndex(t=>t.id===a)-data.tasks.findIndex(t=>t.id===b)),theme.id+' exact tasks');
}
for(const c of data.checklists){const out=render('checklists();','?list='+c.id);assert.equal([...out.detail.matchAll(/data-status="/g)].length,c.tasks.length,c.id)}
assert.deepEqual([...render('tasks();','?task=T53').results.matchAll(/data-status="(T\d+)"/g)].map(m=>m[1]),['T53']);
assert.ok(render('overview();').main.includes('permanent residents'));
assert.ok(render('originalPlan();').main.includes('54259 m2'));
const roof=20*74+20*37+30*15+350;
assert.equal(roof,3020);
assert.equal(40*65+15*90+10*125,5200);
assert.equal(8000+18000+6000+8159+1000,41159);
assert.equal(4700+5200+3200+41159,54259);
console.log('Passed rendered-page links, all document prompts, theme filters, checklist selection and source arithmetic checks.');
