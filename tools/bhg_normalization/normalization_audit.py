#!/usr/bin/env python3
"""Read-only BHG governance-core normalization audit.

This tool inventories Markdown artifacts, extracts frontmatter/relationship
signals, and produces evidence for N1-N7. It never modifies source documents.
"""
from __future__ import annotations
import json, re, hashlib
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path('.')
EXCLUDED = {'.git', '.github'}
SCOPES = [Path('docs'), Path('README.md'), Path('CHANGELOG.md'), Path('ARCHITECTURE_MAP.md'), Path('GENESIS_BOOTSTRAP_REPORT_20260711.md')]
RELATIONS = {'governed_by','governs','depends_on','related_to','references','supersedes','superseded_by','replaces','replaced_by','implements','implemented_by'}
REQUIRED = {'title','document_id','document_type','version','status','governance_level','owner','approval_authority','created','last_updated','classification','language','repository'}
CANONICAL_CONTRACTS = {
 'CANONICAL_AUTHORITY_MODEL.md': 'draft',
 'DOCUMENT_STANDARD.md': 'draft',
 'DOCUMENT_METADATA_STANDARD.md': 'draft',
 'DOCUMENT_IDENTIFIER_STANDARD.md': 'draft',
 'DOCUMENT_SCHEMA_STANDARD.md': 'draft',
 'DOCUMENT_RELATIONSHIP_STANDARD.md': 'draft',
}

def sha256(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        return {}, False
    end = text.find('\n---', 4)
    if end < 0:
        return {}, False
    block = text[4:end]
    fields = {}
    current = None
    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue
        m = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', raw)
        if m:
            key, val = m.groups(); key = key.strip(); val = val.strip()
            if val in ('null','~'): val = None
            elif val.startswith('[') and val.endswith(']'):
                val = [x.strip().strip("'\"") for x in val[1:-1].split(',') if x.strip()]
            fields[key] = val; current = key
            continue
        m = re.match(r'^\s+-\s+(.*)$', raw)
        if m and current:
            if not isinstance(fields.get(current), list): fields[current] = []
            fields[current].append(m.group(1).strip().strip("'\""))
    return fields, True

def files():
    out=[]
    for p in ROOT.rglob('*.md'):
        if any(part in EXCLUDED for part in p.parts): continue
        out.append(p)
    return sorted(out)

def main():
    records=[]
    for p in files():
        text=p.read_text(encoding='utf-8', errors='replace')
        fm, valid = parse_frontmatter(text)
        lower=text.lower()
        rels={r: (r in fm or re.search(rf'\b{re.escape(r)}\b', lower) is not None) for r in RELATIONS}
        fields=set(fm)
        missing=sorted(REQUIRED-fields)
        records.append({
            'path': str(p), 'sha256': sha256(p), 'bytes': p.stat().st_size,
            'frontmatter_present': valid, 'frontmatter_keys': sorted(fields),
            'missing_required_metadata': missing,
            'document_id': fm.get('document_id'), 'title': fm.get('title'),
            'document_type': fm.get('document_type'), 'version': fm.get('version'),
            'status': fm.get('status'), 'canonical': fm.get('canonical'), 'effective': fm.get('effective'),
            'governance_level': fm.get('governance_level'), 'owner': fm.get('owner'),
            'approval_authority': fm.get('approval_authority'), 'relationships_declared': sorted(k for k,v in rels.items() if v),
        })
    ids=Counter(r['document_id'] for r in records if r['document_id'])
    keysets=Counter(tuple(r['frontmatter_keys']) for r in records if r['frontmatter_present'])
    statuses=Counter(str(r['status']) for r in records if r['status'] is not None)
    types=Counter(str(r['document_type']) for r in records if r['document_type'] is not None)
    report={
        'phase':'N1', 'mode':'read_only_content_extraction', 'source_modification':False,
        'artifact_count':len(records), 'frontmatter_count':sum(r['frontmatter_present'] for r in records),
        'frontmatter_missing_count':sum(not r['frontmatter_present'] for r in records),
        'required_metadata_gap_count':sum(bool(r['missing_required_metadata']) for r in records),
        'duplicate_document_ids':sorted(k for k,v in ids.items() if v>1),
        'frontmatter_keyset_count':len(keysets), 'status_distribution':dict(statuses),
        'document_type_distribution':dict(types), 'artifacts':records,
        'contract_dependency_cluster':CANONICAL_CONTRACTS,
    }
    Path('normalization-output').mkdir(exist_ok=True)
    Path('normalization-output/n1-inventory.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    md=['# BHG Governance Core — N1 Content Inventory','',f"- Artifacts: **{len(records)}**",f"- Frontmatter present: **{report['frontmatter_count']}**",f"- Frontmatter missing: **{report['frontmatter_missing_count']}**",f"- Required-metadata gaps: **{report['required_metadata_gap_count']}**",f"- Frontmatter keysets: **{len(keysets)}**",'']
    md += ['## Duplicate document IDs',''] + [f'- `{x}`' for x in report['duplicate_document_ids']] if report['duplicate_document_ids'] else ['## Duplicate document IDs','', '- None detected by exact metadata value.']
    md += ['', '## Status distribution',''] + [f'- `{k}`: {v}' for k,v in sorted(statuses.items())]
    md += ['', '## N1 interpretation','', '- This is evidence, not approval.', '- Missing metadata is recorded, not inferred.', '- Relationships are observed before canonical mapping.', '- No source document is modified by this audit.']
    Path('normalization-output/N1_CONTENT_INVENTORY.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['artifact_count','frontmatter_count','frontmatter_missing_count','required_metadata_gap_count','frontmatter_keyset_count','duplicate_document_ids']},indent=2))

if __name__=='__main__': main()
