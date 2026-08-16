from pathlib import Path
import yaml

REL_KEYS = ["governed_by", "governs", "depends_on", "related_to"]
BASELINE = "8685abae60b176dcb3042400ebacc01b7dea97a5"

def parse(path):
    text=path.read_text(encoding='utf-8',errors='replace')
    if not text.startswith('---\n'): return None,text
    end=text.find('\n---',4)
    if end<0:return None,text
    try:data=yaml.safe_load(text[4:end]) or {}
    except Exception:return None,text
    return data,text[end+4:].lstrip('\n')

docs=sorted(Path('.').rglob('*.md'))
docs=[p for p in docs if '.git/' not in str(p)]
by_id={}; aliases={}
for p in docs:
    fm,body=parse(p)
    if not fm: continue
    did=str(fm.get('document_id',''))
    if not did: continue
    by_id[did]=str(p)
    aliases[p.name]=did
    aliases[p.stem]=did
    aliases[str(p)]=did
    aliases[str(p).lstrip('./')]=did

changed=0; migrated=[]; unresolved=[]
def resolve(target):
    t=str(target).strip()
    if t in by_id:return t
    if t in aliases:return aliases[t]
    if t.startswith('./') and t[2:] in aliases:return aliases[t[2:]]
    # case-insensitive filename/stem match
    low=t.lower()
    for k,v in aliases.items():
        if k.lower()==low:return v
    return None

def classify_external(t):
    s=str(t)
    if '*' in s:return 'external_scope'
    if s.endswith('.md') or '/' in s:return 'missing_document_target'
    if s.isupper() and ('_' in s or '-' in s):return 'missing_document_or_external_identifier'
    return 'external_scope'

for p in docs:
    fm,body=parse(p)
    if not fm: continue
    ext=fm.get('extensions') or {}
    legacy=list(ext.get('legacy_relationships') or [])
    local_changed=False
    for key in REL_KEYS:
        vals=fm.get(key)
        if vals is None: vals=[]
        if not isinstance(vals,list): vals=[vals]
        new=[]
        for target in vals:
            r=resolve(target)
            if r:
                new.append(r)
                if str(target)!=r:
                    migrated.append({'source':str(p),'relationship':key,'from':str(target),'to':r,'kind':'canonicalized_target'})
                    local_changed=True
            else:
                cls=classify_external(target)
                legacy.append({'relationship':key,'target':str(target),'classification':cls,'baseline':BASELINE})
                unresolved.append({'source':str(p),'relationship':key,'target':str(target),'classification':cls})
                local_changed=True
        fm[key]=new
    if legacy:
        ext['legacy_relationships']=legacy
    ext['normalization']={**(ext.get('normalization') or {}),'relationship_target_reconciliation':{'baseline':BASELINE,'performed':'2026-08-16','mode':'canonicalize_or_classify_external'}}
    fm['extensions']=ext
    if local_changed:
        out='---\n'+yaml.safe_dump(fm,sort_keys=False,allow_unicode=True,default_flow_style=False).strip()+'\n---\n\n'+body
        p.write_text(out,encoding='utf-8'); changed+=1

report=Path('docs/00-GOVERNANCE/BHG_RELATIONSHIP_TARGET_RECONCILIATION_V0_1.md')
lines=['---','document_id: BHG-GOV-RTRR-001','title: BHG Relationship Target Reconciliation Register','document_type: Governance Reconciliation Matrix','version: 0.1.0','status: Review','governance_level: Enterprise','owner: BHG Governance Council','approval_authority: BHG Governance Council','created: 2026-08-16','last_updated: 2026-08-16','effective_date: null','classification: Internal','language: en','repository: BHG-GOVERNANCE','governed_by:','- BHG_CONSTITUTION','---','','# BHG Relationship Target Reconciliation Register v0.1','',f'- Documents changed: **{changed}**',f'- Targets canonicalized: **{len(migrated)}**',f'- Targets classified as external/missing: **{len(unresolved)}**','']
lines += ['## External / non-document targets preserved as legacy evidence','']
for x in unresolved: lines.append(f"- `{x['source']}` — `{x['relationship']}` → `{x['target']}` — `{x['classification']}`")
report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'changed={changed} canonicalized={len(migrated)} unresolved_or_external={len(unresolved)}')