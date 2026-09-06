// Read public bibliographic pages as HTML data; no browser interaction or logins.
const fs=require('node:fs'),{execFileSync}=require('node:child_process'),{JSDOM,VirtualConsole}=require('jsdom');
const papers=JSON.parse(fs.readFileSync('_data/publications.json','utf8'));
const norm=s=>s.toLowerCase().replace(/[^a-z0-9]/g,'');
function page(url){const raw=execFileSync('curl',['-L','-sS','--max-time','25',url],{encoding:'utf8',maxBuffer:4000000});return new JSDOM(raw,{virtualConsole:new VirtualConsole()}).window.document;}
const author=page('https://aclanthology.org/people/d/da-ju/');
for(const paper of papers){
  const anchor=[...author.querySelectorAll('a[href]')].find(a=>norm(a.textContent)===norm(paper.title));
  if(!anchor){console.log(JSON.stringify({id:paper.id,acl:null}));continue;}
  const url=new URL(anchor.getAttribute('href'),'https://aclanthology.org').href;
  const d=page(url);const links=[...d.querySelectorAll('a[href]')].map(a=>({text:a.textContent.trim(),url:new URL(a.getAttribute('href'),url).href})).filter(a=>/video|present|slides|poster|youtube|vimeo|slideslive|virtual|talk/i.test(a.text+' '+a.url));
  const embeds=[...d.querySelectorAll('iframe')].map(n=>n.getAttribute('src')||n.getAttribute('data-src'));
  console.log(JSON.stringify({id:paper.id,acl:url,title:d.title,links,embeds}));
}
