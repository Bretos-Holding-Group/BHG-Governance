#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import json, hashlib, re
import yaml

ROOT = Path('.')
OUT = Path('normalization-output/core-n3-n5-evidence')
EXCLUDED = {'.git', '.github', 'normalization-output'}
REL_KEYS = ('governed_by', 'depends_on', 'related_to', 'governs')


def parse(text):
    if not text.startswith('---\n'):
        return {}, False
    end = text.find('\n---', 4)
    if end < 0:
        return {}, False
    try:
        value = yaml.safe_load(text[4:end]) or {}
        return value if isinstance(value, dict) else {}, True
    except Exception:
        return {}, False


def values(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(x).strip() for x in value if str(x).strip()]
    return [str(value).strip()] if str(value).strip() else []


files = [p for p in sorted(ROOT.rglob('*.md')) if not any(part in EXCLUDED for part in p.parts)]
records = []
id_index = defaultdict(list)
relationships = []
for path in files:
    text = path.read_text(encoding='utf-8', errors='replace')
    fm, valid = parse(text)
    did = str(fm.get('document_id', '')).strip()
    if did:
        id_index[did].append(str(path))
    record = {
        'path': str(path),
        'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
        'frontmatter_valid': valid,
        'document_id': did or None,
        'status': fm.get('status'),
        'version': fm.get('version'),
        'governance_level': fm.get('governance_level'),
        'owner': fm.get('owner'),
        'approval_authority': fm.get('approval_authority'),
    }
    missing = [k for k in ('document_id','version','status','governance_level','owner','approval_authority') if not fm.get(k)]
    record['required_identity_metadata_missing'] = missing
    records.append(record)
    if did:
        for key in REL_KEYS:
            for target in values(fm.get(key)):
                relationships.append({'source': did, 'path': str(path), 'type': key, 'target': target})

# N3: permanent identity integrity
n3 = {
    'documents_scanned': len(records),
    'missing_document_id': sum(r['document_id'] is None for r in records),
    'duplicate_document_ids': {k:v for k,v in id_index.items() if len(v) > 1},
    'duplicate_id_count': sum(1 for v in id_index.values() if len(v) > 1),
}

# N4: relationship target resolution and inverse observations
known = set(id_index)
unresolved = [r for r in relationships if r['target'] not in known]
n4 = {
    'relationship_declarations': len(relationships),
    'known_document_ids': len(known),
    'unresolved_targets': unresolved,
    'unresolved_target_count': len(unresolved),
}

# N5: authority graph. governed_by means source -> authority target.
graph = defaultdict(set)
for r in relationships:
    if r['type'] == 'governed_by' and r['target'] in known and r['source'] in known:
        graph[r['source']].add(r['target'])

state = {}
cycles = []
stack = []

def dfs(node):
    state[node] = 1
    stack.append(node)
    for nxt in graph.get(node, set()):
        if state.get(nxt, 0) == 0:
            dfs(nxt)
        elif state.get(nxt) == 1:
            try:
                i = stack.index(nxt)
                cycles.append(stack[i:] + [nxt])
            except ValueError:
                cycles.append([nxt, node, nxt])
    stack.pop()
    state[node] = 2

for node in known:
    if state.get(node, 0) == 0:
        dfs(node)

self_authority = sorted({r['source'] for r in relationships if r['type'] == 'governed_by' and r['source'] == r['target']})
n5 = {
    'authority_edges': sum(len(v) for v in graph.values()),
    'authority_cycles': cycles,
    'authority_cycle_count': len(cycles),
    'self_authority_edges': self_authority,
}

OUT.mkdir(parents=True, exist_ok=True)
result = {'scope': 'BHG-Governance', 'mode': 'read_only', 'n3_identity': n3, 'n4_relationships': n4, 'n5_authority': n5, 'document_records': records}
(OUT / 'evidence.json').write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
summary = [
    '# Core N3-N5 Evidence Audit', '',
    '**Mode:** read-only / non-authoritative', '',
    '## N3 Identity',
    f"- Documents scanned: **{n3['documents_scanned']}**",
    f"- Missing document IDs: **{n3['missing_document_id']}**",
    f"- Duplicate document IDs: **{n3['duplicate_id_count']}**", '',
    '## N4 Relationships',
    f"- Relationship declarations: **{n4['relationship_declarations']}**",
    f"- Unresolved targets: **{n4['unresolved_target_count']}**", '',
    '## N5 Authority',
    f"- Authority edges: **{n5['authority_edges']}**",
    f"- Authority cycles: **{n5['authority_cycle_count']}**",
    f"- Self-authority edges: **{len(n5['self_authority_edges'])}**", '',
    '## Gate',
    'This evidence does not approve, promote, rename, delete, or otherwise modify normative documents.',
]
(OUT / 'summary.md').write_text('\n'.join(summary) + '\n', encoding='utf-8')
print(json.dumps({'N3': n3, 'N4': {'relationships': n4['relationship_declarations'], 'unresolved': n4['unresolved_target_count']}, 'N5': {'edges': n5['authority_edges'], 'cycles': n5['authority_cycle_count'], 'self_authority': len(n5['self_authority_edges'])}}, indent=2))
