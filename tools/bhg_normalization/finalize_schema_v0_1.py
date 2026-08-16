#!/usr/bin/env python3
from pathlib import Path
import yaml, json

EXCLUDED={'.git','.github','normalization-output','artifacts','graph-evidence','post-remediation-evidence'}
REL={'governed_by','governs','depends_on','related_to'}
REQ=['title','document_id','document_type','version','status','governance_level','owner','approval_authority','created','last_updated','classification','language','repository']
changed=[]
for p in sorted(Path('.').rglob('*.md')):
    if any(x in EXCLUDED for x in p.parts): continue
    text=p.read_text(encoding='utf-8',errors='replace')
    if not text.startswith('---\n'): continue
    e=text.find('\n---',4)
    if e<0: continue
    try: fm=yaml.safe_load(text[4:e]) or {}
    except Exception: continue
    body=text[e+4:].lstrip('\n')
    ext=fm.get('extensions') if isinstance(fm.get('extensions'),dict) else {}
    norm=ext.get('normalization') if isinstance(ext.get('normalization'),dict) else {}
    for k in ('normalization_state','normalization_baseline','normalization_date'):
        if k in fm:
            norm[k.replace('normalization_','')]=fm.pop(k)
    if norm: ext['normalization']=norm
    fm['extensions']=ext
    # Ensure all canonical relationship keys exist so the top-level contract is stable.
    for k in REL:
        if k not in fm: fm[k]=[]
    # Preserve required metadata keys; do not invent semantic values here.
    for k in REQ:
        if k not in fm: fm[k]=None
    out='---\n'+yaml.safe_dump(fm,sort_keys=False,allow_unicode=True).strip()+'\n---\n\n'+body
    if out!=text:
        p.write_text(out,encoding='utf-8'); changed.append(str(p))
Path('normalization-output').mkdir(exist_ok=True)
Path('normalization-output/schema-finalization-register.json').write_text(json.dumps({'modified_count':len(changed),'files':changed},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'modified_count':len(changed)},indent=2))
