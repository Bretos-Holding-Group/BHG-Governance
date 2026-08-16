#!/usr/bin/env python3
"""Read-only corpus scorer for BHG Canonical Core Discovery R00.

Scores documentary centrality across the four BHG repositories without editing
source documents. Output is intended as an auditable candidate-ranking aid,
not as normative authority.
"""
from __future__ import annotations
import json, re, subprocess
from collections import Counter, defaultdict
from pathlib import Path

# This file lives at <repo>/tools/. parents[1] is therefore the repository root.
ROOT=Path(__file__).resolve().parents[1]
REPOS={
 'BHG-Governance': ROOT,
 'BHG-Ecosystem-Foundation': ROOT/'_corpus'/'BHG-Ecosystem-Foundation',
 'bhg-knowledge': ROOT/'_corpus'/'bhg-knowledge',
 'ZivaLatam': ROOT/'_corpus'/'ZivaLatam',
}
OUT=ROOT/'artifacts'
OUT.mkdir(exist_ok=True)

def clone_missing():
    base='https://github.com/Bretos-Holding-Group/{}.git'
    for name,path in REPOS.items():
        if name=='BHG-Governance': continue
        path.parent.mkdir(parents=True,exist_ok=True)
        if not path.exists():
            subprocess.run(['git','clone','--depth','1',base.format(name),str(path)],check=True,stdout=subprocess.DEVNULL)

def fm(text):
    if not text.startswith('---'): return {}
    m=re.match(r'^---\s*\n(.*?)\n---\s*\n',text,re.S)
    if not m:return {}
    d={}
    for line in m.group(1).splitlines():
        if ':' in line:
            k,v=line.split(':',1); d[k.strip()]=v.strip().strip('"\'')
    return d

def norm(v): return str(v or '').lower()

def score(doc, inbound, outbound, xrefs, conflicts, cycles):
    fm0=doc['fm']; path=doc['path']; text=doc['text']; typ=norm(fm0.get('document_type')); lvl=norm(fm0.get('governance_level'))
    s=0; reasons=[]
    if 'constitution' in typ or lvl=='supreme': s+=40; reasons.append('constitutional/supreme')
    if lvl in {'foundational','foundation','enterprise'}: s+=15; reasons.append('foundational governance level')
    if any(x in typ for x in ['standard','model','matrix','architecture','policy','protocol','repository']): s+=10; reasons.append('shared contract/model type')
    if any(x in path.lower() for x in ['00-foundation','foundation']): s+=8; reasons.append('foundation location')
    if any(x in norm(text) for x in ['governed_by','approval_authority','document_id','canonical','normative authority']): s+=5; reasons.append('governance-contract indicators')
    if 'zivalatam' in doc['repo'].lower() and ('charter' in path.lower() or 'governance' in typ): s+=8; reasons.append('domain governance bridge candidate')
    s += min(inbound*2,30) + min(outbound,15) + min(xrefs*3,18)
    if inbound: reasons.append(f'inbound centrality={inbound}')
    if xrefs: reasons.append(f'cross-repo references={xrefs}')
    if conflicts: s+=3; reasons.append('conflict evidence present')
    if cycles: s-=8; reasons.append('authority-cycle participation; unresolved')
    if norm(fm0.get('status')) in {'deprecated','superseded'}: s-=25; reasons.append('deprecated/superseded')
    return max(s,0),reasons

def main():
    clone_missing(); docs=[]; idmap={}; refs=defaultdict(list); xref=Counter(); conflicts=Counter(); cycles=set()
    for repo,root in REPOS.items():
        for p in root.rglob('*.md'):
            if '.git' in p.parts: continue
            text=p.read_text(errors='ignore'); f=fm(text); did=f.get('document_id') or p.stem
            d={'repo':repo,'path':str(p.relative_to(root)),'document_id':did,'fm':f,'text':text}
            docs.append(d); idmap.setdefault(did,[]).append(d)
    all_ids=set(idmap)
    for d in docs:
        for rid in re.findall(r'\b[A-Z][A-Z0-9_-]{2,}(?:-[A-Z0-9]+)+\b',d['text']):
            if rid in all_ids and rid!=d['document_id']:
                refs[rid].append(d['document_id'])
                target=idmap[rid][0]
                if target['repo']!=d['repo']: xref[rid]+=1
        if 'NORMATIVE_CONFLICT_REGISTER' in d['path'] or 'conflict' in norm(d['fm'].get('document_type')): conflicts[d['document_id']]+=1
        if any(x in d['text'] for x in ['BHG-MIG-304657D4691E','BHG-MIG-38F961165834','BHG-MIG-4EF6926C68EA','BHG-MIG-71A9F2A90F32','BHG-MIG-83A30C7D861D','BHG-MIG-AB1A5B8A9156','BHG-MIG-D13DBA24B680','BHG-MIG-D140A7A5674C']): cycles.add(d['document_id'])
    rows=[]
    for d in docs:
        inbound=len(refs.get(d['document_id'],[])); outbound=sum(1 for r in all_ids if re.search(r'\b'+re.escape(r)+r'\b',d['text']) and r!=d['document_id']); xr=xref[d['document_id']]
        s,why=score(d,inbound,outbound,xr,conflicts[d['document_id']],d['document_id'] in cycles)
        rows.append({'document_id':d['document_id'],'repository':d['repo'],'path':d['path'],'status':d['fm'].get('status'),'document_type':d['fm'].get('document_type'),'governance_level':d['fm'].get('governance_level'),'inbound_references':inbound,'outbound_references':outbound,'cross_repository_references':xr,'conflict_evidence':conflicts[d['document_id']],'authority_cycle_participation':d['document_id'] in cycles,'score':s,'reasons':why})
    rows.sort(key=lambda x:(-x['score'],x['repository'],x['path']))
    top=rows[:60]
    payload={'phase':'Canonical Core Discovery R00 scoring','authority_effect':'NONE','source_modification':False,'corpus_documents':len(docs),'candidate_target':'40-60','top_candidate_count':len(top),'rows':rows,'top_candidates':top}
    (OUT/'canonical-core-score-r00.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
    lines=['# BHG Canonical Core Score R00','',f'- Corpus documents: **{len(docs)}**',f'- Ranked candidates: **{len(top)}**', '- Authority effect: **NONE**','- Source normative documents modified: **NO**','', '| Rank | Score | Document ID | Repository | Status | Type | Layer evidence |','|---:|---:|---|---|---|---|---|']
    for i,r in enumerate(top,1): lines.append(f"| {i} | {r['score']} | `{r['document_id']}` | {r['repository']} | {r['status'] or '-'} | {r['document_type'] or '-'} | {'; '.join(r['reasons'][:3])} |")
    lines += ['', '## Interpretation', 'This is a discovery ranking only. Scores do not create canonical status or normative authority. Cycles and unresolved authority conflicts remain preserved for semantic review.', '']
    (OUT/'canonical-core-score-r00.md').write_text('\n'.join(lines))

if __name__=='__main__': main()
