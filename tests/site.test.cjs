const {JSDOM,VirtualConsole}=require('jsdom');
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),source=fs.readFileSync(path.join(root,'assets/js/personal.js'),'utf8');
const papers=JSON.parse(fs.readFileSync(path.join(root,'_data/publications.json'),'utf8'));
function setup(file='index.html'){
  const errors=[],vc=new VirtualConsole();vc.on('jsdomError',e=>{if(e.type!=='css parsing')errors.push(e.message)});
  const html=fs.readFileSync(path.join(root,file),'utf8').replace('<script src="/assets/js/personal.js" defer></script>','').replace('</body>','<script>'+source+'</script></body>');
  const dom=new JSDOM(html,{url:'https://dexterju.me/'+(file==='index.html'?'':file),runScripts:'dangerously',virtualConsole:vc,beforeParse(w){w.IntersectionObserver=class{observe(){}disconnect(){}};}});
  assert.deepEqual(errors,[]);return {dom,w:dom.window,d:dom.window.document};
}
async function main(){
const {dom,w,d}=setup();const visible=()=>[...d.querySelectorAll('.paper')].filter(p=>!p.hidden);
assert.equal(papers.length,22);assert.equal(d.querySelectorAll('.paper').length,22);assert.equal(d.querySelectorAll('.feature-card').length,4);assert.equal(visible().length,22);
assert.equal(new Set(papers.map(p=>p.id)).size,22);assert.equal(papers.filter(p=>p.id==='blenderbot-3').length,1);
for(const id of ['mai-thinking-1','llama-4','open-domain-progress','growing-up-together'])assert.ok(d.getElementById('paper-'+id));
for(const p of papers)assert.ok(p.url.startsWith('https://'));
const search=d.getElementById('paper-search'),year=d.getElementById('paper-year');
search.value='MAI-Thinking';search.dispatchEvent(new w.Event('input'));assert.equal(visible().length,1);assert.equal(visible()[0].id,'paper-mai-thinking-1');
search.value='Ullrich';search.dispatchEvent(new w.Event('input'));assert.equal(visible().length,1);
search.value='missing-paper-xyz';search.dispatchEvent(new w.Event('input'));assert.equal(visible().length,0);assert.equal(d.getElementById('paper-empty').hidden,false);
d.getElementById('reset-papers').click();assert.equal(visible().length,22);
d.querySelector('[data-topic="safety"]').click();assert.ok(visible().length>1);assert.ok(visible().every(p=>p.dataset.topics.split(' ').includes('safety')));
year.value='2026';year.dispatchEvent(new w.Event('change'));assert.equal(visible().length,1);assert.ok(d.getElementById('paper-status').textContent.startsWith('1 work '));
d.getElementById('clear-papers').click();assert.equal(visible().length,22);
assert.equal(d.querySelectorAll('.paper-team').length,2);assert.equal(d.querySelector('link[rel="canonical"]').href,'https://dexterju.me/');
assert.ok(d.querySelector('meta[name="description"]').content.length>50);assert.ok(d.querySelector('img').alt.includes('Dexter'));
assert.ok(!d.querySelector('img').src.includes('profil-photo.jpg'));assert.ok(fs.statSync(path.join(root,'assets/images/dexter-portrait-960.webp')).size<200000);
assert.ok(d.querySelector('a[href="/nyc/"]'));assert.ok(d.querySelector('a[href="/bachelor-thesis.pdf"]'));
const allIds=[...d.querySelectorAll('[id]')].map(n=>n.id);assert.equal(new Set(allIds).size,allIds.length);
for(const a of d.querySelectorAll('a[target="_blank"]')){assert.ok(a.rel.includes('noopener'));assert.ok(a.rel.includes('noreferrer'));}
for(const a of d.querySelectorAll('a[href^="#"]'))assert.ok(d.querySelector(a.getAttribute('href')),a.href);
for(const a of d.querySelectorAll('a[href^="/#"]'))assert.ok(d.querySelector(a.hash),a.href);
for(const a of d.querySelectorAll('[src^="/assets"],[href^="/assets"]'))assert.ok(fs.existsSync(path.join(root,a.getAttribute('src')||a.getAttribute('href'))));
const contact=setup('contact.html');
for(const page of ['index.html','contact.html','contact/index.html']){
  const html=fs.readFileSync(path.join(root,page),'utf8');
  assert.ok(!/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(html),'No email address in public HTML');
  assert.ok(!/mailto:|data-copy-email/.test(html),'No hidden email link or copy data');
}
assert.ok(contact.d.querySelector('a[href^="https://www.linkedin.com/"]'));
const nojs=new JSDOM(fs.readFileSync(path.join(root,'index.html'),'utf8'));assert.equal(nojs.window.document.querySelectorAll('.paper:not([hidden])').length,22);assert.equal(nojs.window.document.querySelector('.publication-tools').hidden,true);
for(const x of [dom,contact.dom,nojs])x.window.close();
console.log('PASS: publications, filters, SEO, assets, safe links, no-JS content, contact profiles, and no email exposure in public pages');
}
main().catch(e=>{console.error(e);process.exitCode=1});
