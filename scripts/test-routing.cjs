const fs=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const prefix=fs.readFileSync(path.join(root,'dist/app.js'),'utf8').split('const docid=')[0];
function resolve(pathname,page){return vm.runInNewContext(prefix+'\nfile;', {window:{PLAN:{}},location:{pathname},document:{body:{dataset:page?{page}:{} }}})}
for(const route of ['plan','tasks','documents','checklists','references','agencies','decisions','sitemap','document-D01']){
 for(const url of ['/'+route,'/'+route+'.html','/'+route+'/','/dist/'+route+'.html'])assert.equal(resolve(url),route+'.html',url);
}
assert.equal(resolve('/'),'index.html');
assert.equal(resolve('/index'),'index.html');
assert.equal(resolve('/tasks','tasks.html'),'tasks.html');
assert.equal(resolve('/hosted-path','document-D01.html'),'document-D01.html');
assert.notEqual(resolve('/tasks'),'index.html');
for(const f of fs.readdirSync(path.join(root,'dist')).filter(f=>f.endsWith('.html'))){
 const markup=fs.readFileSync(path.join(root,'dist',f),'utf8');
 assert.ok(markup.includes('data-page="'+f+'"'),f+' page identity');
}
console.log('Passed URL-form routing checks and explicit page identity checks for all generated pages.');
