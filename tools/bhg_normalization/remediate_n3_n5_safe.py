#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
from datetime import date
import hashlib, re, yaml, json

ROOT=Path('.')
EXCLUDED={'.git','.github','normalization-output'}
REQ=['title','document_id','document_type','version','status','governance_level','owner','approval_authority','created','last_updated','classification','language','repository']
ALIASES={'document-id':'document_id','documentId':'document_id','doc_id':'document_id','document-type':'document_type','documentType':'document_type','governance-level':'governance_level','governanceLevel':'governance_level','approval-authority':'approval_authority','approvalAuthority':'approval_authority','last-updated':'last_updated','lastUpdated':'last_updated','created-date':'created','created_at':'created','createdAt':'created','repo':'repository','repository-name':'repository','depends-on':'depends_on','governed-by':'governed_by','related-to':'related_to'}
DUP_OWNERS={'BHG-POL-001':'docs/01-POLICIES/POLICY_HIERARCHY.md','GEN-BHG-ENG-013':'docs/04-AI/GENESIS/GENESIS_PROVIDER_ABSTRACTION.md'}

def parse(text):
    if not text.startswith('---\n'): return None,text
    e=text.find('\n---',4)
    if e<0:return None,text
    try:d=yaml.safe_load(text[4:e]) or {}
    except Exception:d={}
    return d,text[e+4:].lstrip('\n')

def title(path,body):
    m=re.search(r'^#\s+(.+?)\s*$',body,re.M)
    return m.group(1).strip() if m else path.stem.replace('_',' ').replace('-',' ')

def typ(path):
    s=str(path)
    for token,val in [('01-POLICIES','policy'),('02-STANDARDS','standard'),('03-ENGINEERING','engineering_document'),('04-AI','ai_document'),('05-AUTOMATION','automation_document'),('06-AUDIT','audit_record'),('99-HISTORY','historical_record'),('00-GOVERNANCE','governance_document'),('00-FOUNDATION','foundation_document')]:
        if token in s:return val
    return 'unclassified'

def level(path):
    s=str(path)
    for token,val in [('01-POLICIES','Policy'),('02-STANDARDS','Standard'),('03-ENGINEERING','Engineering'),('04-AI','AI'),('05-AUTOMATION','Automation'),('06-AUDIT','Audit'),('99-HISTORY','History')]:
        if token in s:return val
    return 'Enterprise' if ('00-' in s) else 'Unclassified'

def lang(body):
    ws=re.findall(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+',body.lower())
    es=sum(w in {'el','la','los','las','de','del','que','para','una','un','y','en','con','por','como'} for w in ws)
    en=sum(w in {'the','of','and','to','for','a','an','is','with','by','as','this'} for w in ws)
    return 'es' if es>en else 'en'

def pid(path,body):return 'BHG-MIG-'+hashlib.sha256((str(path)+'|'+body[:2000]).encode()).hexdigest()[:12].upper()

files=[p for p in sorted(ROOT.rglob('*.md')) if not any(x in EXCLUDED for x in p.parts)]
original={p:(p.read_text(encoding='utf-8',errors='replace')) for p in files}
parsed={p:parse(t) for p,t in original.items()}
ids=defaultdict(list)
for p,(fm,body) in parsed.items():
    if fm and fm.get('document_id'):ids[str(fm['document_id'])].append(p)
records=[]
for p,(fm,body) in parsed.items():
    fm=dict(fm or {}); provisional=[]
    canon={}
    for k,v in fm.items():
        nk=ALIASES.get(str(k),str(k))
        if nk in canon and canon[nk]!=v:
            provisional.append('metadata_collision'); canon.setdefault('extensions',{})
        else:canon[nk]=v
    if not canon.get('title'):canon['title']=title(p,body);provisional.append('title_derived')
    did=canon.get('document_id')
    if not did:canon['document_id']=pid(p,body);provisional.append('identity_generated')
    elif str(did) in DUP_OWNERS and str(p)!=DUP_OWNERS[str(did)]:
        old=str(did);canon['document_id']=pid(p,body);canon['identity_previous_document_id']=old;provisional.append('duplicate_identity_reassigned')
    defaults={'document_type':typ(p),'version':'0.0.0','status':'Draft','governance_level':level(p),'owner':'PENDING-OWNER-ASSIGNMENT','approval_authority':'PENDING-AUTHORITY-ASSIGNMENT','created':'PENDING-DATE-VERIFICATION','last_updated':'PENDING-DATE-VERIFICATION','classification':'PENDING-CLASSIFICATION','language':lang(body),'repository':'BHG-GOVERNANCE'}
    for k,v in defaults.items():
        if k not in canon or canon[k] in (None,''):canon[k]=v;provisional.append(k)
    canon['normalization_state']='provisional_metadata' if provisional else canon.get('normalization_state','normalized')
    canon['normalization_baseline']='8685abae60b176dcb3042400ebacc01b7dea97a5'
    canon['normalization_date']=str(date.today())
    out='---\n'+yaml.safe_dump(canon,sort_keys=False,allow_unicode=True).strip()+'\n---\n\n'+body
    if out!=original[p]:
        p.write_text(out,encoding='utf-8');records.append({'path':str(p),'provisional':sorted(set(provisional)),'document_id':canon['document_id']})
out=Path('normalization-output');out.mkdir(exist_ok=True)
(out/'n3-n5-remediation-register.json').write_text(json.dumps({'mode':'loss_minimizing_structural_remediation','modified_count':len(records),'records':records},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'modified_count':len(records),'duplicate_reassignments':sum('duplicate_identity_reassigned' in r['provisional'] for r in records),'provisional_documents':sum(bool(r['provisional']) for r in records)},indent=2))
