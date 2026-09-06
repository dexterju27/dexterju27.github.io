#!/usr/bin/env python3
"""Small static homepage builder. Never touches the independently published /nyc/."""
from pathlib import Path
from string import Template
from html import escape
from urllib.parse import urlsplit
import argparse,json,re
ROOT=Path(__file__).resolve().parents[1]
TOPICS={'safety':'Safety & alignment','planning':'Reasoning & planning','dialogue':'Dialogue','evaluation':'Evaluation','architectures':'Architectures'}
DESCRIPTION='Da (Dexter) Ju works on AI safety and reasoning at Microsoft AI. Previously Meta Superintelligence Labs (MSL) and FAIR. Research, publications, and personal projects.'


def external(url,text,cls='',label=''):
    if not url.startswith(('https://','http://')):raise ValueError('Unsafe external link')
    return '<a href="%s" target="_blank" rel="noopener noreferrer"%s%s>%s</a>'%(escape(url,quote=True),' class="'+cls+'"' if cls else '', ' aria-label="'+escape(label,quote=True)+'"' if label else '',text)


def graphic(topic):
    motifs={
      'planning':'<path d="M12 54 31 37 43 43 69 13"/><circle cx="12" cy="54" r="4"/><circle cx="31" cy="37" r="4"/><circle cx="43" cy="43" r="4"/><circle cx="69" cy="13" r="4"/>',
      'dialogue':'<path d="M10 14h44v29H29L18 54V43h-8z"/><path d="M35 49h18l10 10V48h8V28H60"/><path d="M20 24h23m-23 9h15"/>',
      'multimodal':'<rect x="27" y="8" width="43" height="35" rx="3"/><path d="m30 36 12-12 9 8 6-6 10 10"/><circle cx="59" cy="18" r="3"/><path d="M48 48v16H11V32h11m-2 15h18m-18 8h12"/>',
      'architectures':'<path d="M10 61h60M14 53V40h13V27h13V14h14V4"/><path d="M22 61V48h13V35h13V22h14V12"/><path d="M43 60V47h13V34h14"/>',
      'safety':'<path d="M40 7 66 17v20c0 17-26 28-26 28S14 54 14 37V17z"/><path d="m27 35 9 9 19-21"/>'}
    return '<svg viewBox="0 0 80 74" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+motifs.get(topic,motifs['planning'])+'</svg>'


def validate(papers):
    ids=set();titles=set()
    for p in papers:
        title=re.sub(r'\W','',p['title'].lower())
        if p['id'] in ids or title in titles:raise ValueError('Duplicate paper')
        ids.add(p['id']);titles.add(title)
        if not p['url'].startswith('https://'):raise ValueError('Missing secure paper URL: '+p['id'])
        if not 2010<=p['year']<=2030:raise ValueError('Invalid year')
        if not set(p['topics'])<=set(TOPICS):raise ValueError('Invalid topic')
        if p.get('kind')!='team' and 'Da Ju' not in p['authors']:raise ValueError('Author missing: '+p['id'])


def build(check=False):
    papers=json.loads((ROOT/'_data/publications.json').read_text());validate(papers)
    resources=json.loads((ROOT/'_data/publication-resources.json').read_text())['works']
    if set(resources)!={p['id'] for p in papers}:raise ValueError('Resource audit must account for each publication')
    papers=sorted(papers,key=lambda p:-p['year'])
    featured=[];rows=[]
    for p in papers:
        title=escape(p['title']);year=str(p['year']);venue=escape(p['venue']);team=p.get('kind')=='team'
        if p.get('featured'):
            credit=p.get('feature_credit') or ('Team-authored report' if team else p.get('note') or 'Research paper')
            featured.append('<article class="feature-card" data-feature-id="%s"><div><p class="feature-meta">%s / %s</p><h3>%s</h3><p>%s</p><p class="feature-credit">%s · %s</p></div><div class="feature-graphic">%s</div></article>'%(
                p['id'],year,venue,external(p['url'],escape(p.get('short_title') or p['title'])),escape(p['summary']),escape(credit),escape(p['feature_label']),graphic(p.get('motif') or p['topics'][0])))
        authors=escape(p['authors']).replace('Da Ju','<strong>Da Ju</strong>')
        foot=[]
        if team:foot.append('<span class="paper-team">Team-authored report</span>')
        if p.get('note'):foot.append('<span class="paper-note">'+escape(p['note'])+'</span>')
        host=urlsplit(p['url']).hostname
        primary_label='ACL Anthology' if host=='aclanthology.org' else 'Meta AI blog' if host=='ai.meta.com' and '/blog/' in p['url'] else 'OpenReview' if host=='openreview.net' else 'Report' if team else 'Paper'
        links=[{'label':primary_label,'url':p['url']}]
        if p.get('extra_url'):links.append({'label':p['extra_label'],'url':p['extra_url']})
        links+=resources[p['id']]['links']
        if p.get('scholar_id'):
            url='https://scholar.google.com/citations?view_op=view_citation&hl=en&user=YW5jp5QAAAAJ&citation_for_view=YW5jp5QAAAAJ:'+p['scholar_id']
            links.append({'label':'Scholar record','url':url})
        seen=set()
        for resource in links:
            canonical=resource['url'].rstrip('/')
            if canonical in seen:continue
            seen.add(canonical)
            foot.append(external(resource['url'],escape(resource['label'])+' ↗','paper-resource',resource['label']+' — '+p['title']))
        search=' '.join([p['title'],p['authors'],p['venue'],p['summary'],year]+[TOPICS[t] for t in p['topics']])
        rows.append('<article class="paper" id="paper-%s" data-year="%s" data-topics="%s" data-search="%s"><div class="paper-meta"><span class="paper-year">%s</span><span class="paper-venue">%s</span></div><div class="paper-main"><h3>%s</h3><p class="paper-authors">%s</p>%s</div></article>'%(
            p['id'],year,' '.join(p['topics']),escape(search,quote=True),year,venue,external(p['url'],title),authors,
            '<div class="paper-foot">'+''.join(foot)+'</div>' if foot else ''))
    topics='<button type="button" data-topic="" aria-pressed="true">All work</button>'+''.join('<button type="button" data-topic="%s" aria-pressed="false">%s</button>'%(key,label) for key,label in TOPICS.items())
    years=''.join('<option value="%s">%s</option>'%(y,y) for y in sorted({p['year'] for p in papers},reverse=True))
    home=Template((ROOT/'tools/templates/home.html').read_text()).substitute(featured=''.join(featured),featured_layout='featured-grid--odd' if len(featured)%2 else '',publications=''.join(rows),work_count=len(papers),topic_filters=topics,year_options=years)
    contact=(ROOT/'tools/templates/contact.html').read_text()
    person={'@context':'https://schema.org','@type':'Person','name':'Da (Dexter) Ju','alternateName':['Dexter Ju','Da Ju'],'url':'https://dexterju.me/','image':'https://dexterju.me/assets/images/dexter-portrait.jpg','jobTitle':'Member of Technical Staff','worksFor':{'@type':'Organization','name':'Microsoft AI'},'sameAs':['https://github.com/dexterju27','https://scholar.google.com/citations?user=YW5jp5QAAAAJ','https://www.linkedin.com/in/dexter-da-j-37101976/']}
    layout=Template((ROOT/'tools/templates/layout.html').read_text())
    outputs={}
    for path,body,title,url in [('index.html',home,'Da (Dexter) Ju — AI Safety & Reasoning','https://dexterju.me/'),('contact.html',contact,'Contact — Dexter Ju','https://dexterju.me/contact/'),('contact/index.html',contact,'Contact — Dexter Ju','https://dexterju.me/contact/')]:
        outputs[path]=layout.substitute(body=body,page_title=escape(title),canonical=url,description=escape(DESCRIPTION),person_json=json.dumps(person,ensure_ascii=False).replace('<','\\u003c'))
    outputs['sitemap.xml']='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://dexterju.me/</loc></url><url><loc>https://dexterju.me/contact/</loc></url><url><loc>https://dexterju.me/nyc/</loc></url></urlset>\n'
    for name,text in outputs.items():
        path=ROOT/name
        if check:
            if not path.exists() or path.read_text()!=text:raise SystemExit('Generated file needs rebuild: '+name)
        else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    print(('Checked' if check else 'Built')+' personal site: '+str(len(papers))+' unique works; NYC files untouched.')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();build(a.check)
