from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import csv, hashlib, json, os
import yaml

ROOT = Path('docs')
OUT = Path('authority-dependency-evidence')
RELATIONS = {
    'governed_by','governs','depends_on','related_to','references',
    'supersedes','superseded_by','replaces','replaced_by',
    'implements','implemented_by'
}
RELATION_LIKE_ALIASES = {
    'governed','governs_document','depends','dependency','requires',
    'parent','child','authority','derived_from'
}

def parse_frontmatter(path):
    text = path.read_text(encoding='utf-8', errors='replace')
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---', 4)
    if end < 0:
        return {'__parse_error__': 'unterminated frontmatter'}
    try:
        value = yaml.safe_load(text[4:end]) or {}
    except Exception as exc:
        return {'__parse_error__': str(exc)}
    return value if isinstance(value, dict) else {'__parse_error__': 'frontmatter root is not a mapping'}

def values(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]

docs = []
by_id = defaultdict(list)
frontmatter_cache = {}
for path in sorted(ROOT.rglob('*.md')):
    fm = parse_frontmatter(path)
    frontmatter_cache[str(path)] = fm
    row = {
        'path': str(path),
        'document_id': '',
        'status': 'MISSING_FRONTMATTER' if fm is None else '',
        'document_type': '',
        'governance_level': '',
        'owner': '',
        'approval_authority': '',
        'parse_error': ''
    }
    if isinstance(fm, dict):
        if '__parse_error__' in fm:
            row['parse_error'] = fm['__parse_error__']
        else:
            for k in ['document_id','status','document_type','governance_level','owner','approval_authority']:
                row[k] = str(fm.get(k, '') or '')
            if row['document_id']:
                by_id[row['document_id']].append(str(path))
    docs.append(row)

def resolve(target):
    target = str(target).strip()
    if target in by_id and len(by_id[target]) == 1:
        return target, 'document_id'
    candidates = []
    for did, paths in by_id.items():
        if len(paths) != 1:
            continue
        p = Path(paths[0])
        if target in {p.name, p.stem, str(p), str(p).lstrip('./')}:
            candidates.append(did)
    if len(candidates) == 1:
        return candidates[0], 'filename-derived-non-authoritative'
    return '', ''

matrix = []
findings = []
edges = []
for path in sorted(ROOT.rglob('*.md')):
    fm = frontmatter_cache[str(path)]
    if not isinstance(fm, dict) or '__parse_error__' in fm:
        continue
    source = str(fm.get('document_id', '') or '')
    if not source:
        continue
    for relation in sorted(RELATIONS):
        for raw in values(fm.get(relation)):
            target = str(raw).strip()
            target_id, resolution = resolve(target)
            target_path = by_id[target_id][0] if target_id else ''
            target_fm = frontmatter_cache.get(target_path) or {}
            target_status = str(target_fm.get('status', '') or '') if isinstance(target_fm, dict) else ''
            result = 'VALID' if target_id else 'MISSING_EVIDENCE'
            reason = 'Canonical target resolved.' if target_id else 'Target does not resolve to a unique canonical document_id.'
            if relation == 'governed_by' and target_id == source:
                result = 'CONTRADICTION'; reason = 'Self-governing authority edge.'
            row = {
                'source_id': source, 'source_path': str(path),
                'source_status': str(fm.get('status', '') or ''),
                'relationship': relation, 'target_raw': target,
                'target_id': target_id, 'target_path': target_path,
                'target_status': target_status, 'resolution': resolution,
                'result': result, 'reason': reason
            }
            matrix.append(row)
            if result != 'VALID':
                findings.append(row)
            if target_id:
                edges.append((source, relation, target_id))

for did, paths in sorted(by_id.items()):
    if len(paths) > 1:
        findings.append({
            'source_id': did, 'source_path': ';'.join(paths), 'source_status': '',
            'relationship': 'identity', 'target_raw': ';'.join(paths),
            'target_id': did, 'target_path': '', 'target_status': '',
            'resolution': '', 'result': 'CONTRADICTION',
            'reason': 'Duplicate canonical document_id prevents deterministic resolution.'
        })

for path in sorted(ROOT.rglob('*.md')):
    fm = frontmatter_cache[str(path)]
    if not isinstance(fm, dict) or '__parse_error__' in fm:
        continue
    for key in fm:
        if key in RELATION_LIKE_ALIASES:
            findings.append({
                'source_id': str(fm.get('document_id', '') or ''), 'source_path': str(path),
                'source_status': str(fm.get('status', '') or ''), 'relationship': key,
                'target_raw': json.dumps(fm[key], ensure_ascii=False, sort_keys=True),
                'target_id': '', 'target_path': '', 'target_status': '', 'resolution': '',
                'result': 'INVALID', 'reason': 'Non-canonical relationship-like field.'
            })

auth = defaultdict(list)
for source, relation, target in edges:
    if relation == 'governed_by':
        auth[source].append(target)
color = {}
cycle_nodes = set()
def visit(node, stack):
    color[node] = 1; stack.append(node)
    for nxt in auth.get(node, []):
        if color.get(nxt, 0) == 0:
            visit(nxt, stack)
        elif color.get(nxt) == 1:
            cycle_nodes.update(stack[stack.index(nxt):])
    stack.pop(); color[node] = 2
for node in list(auth):
    if color.get(node, 0) == 0:
        visit(node, [])
for node in sorted(cycle_nodes):
    findings.append({
        'source_id': node, 'source_path': by_id[node][0] if node in by_id else '',
        'source_status': '', 'relationship': 'governed_by', 'target_raw': 'cycle',
        'target_id': '', 'target_path': '', 'target_status': '', 'resolution': '',
        'result': 'CONTRADICTION', 'reason': 'governed_by authority cycle detected.'
    })

OUT.mkdir(exist_ok=True)
fields = ['source_id','source_path','source_status','relationship','target_raw','target_id','target_path','target_status','resolution','result','reason']
with (OUT/'authority-dependency-matrix.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(matrix)
with (OUT/'reconciliation-findings.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(findings)
with (OUT/'document-authority-inventory.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(docs[0].keys())); w.writeheader(); w.writerows(docs)
summary = {
    'repository': 'Bretos-Holding-Group/BHG-Governance',
    'scope': 'docs/**/*.md',
    'document_count': len(docs),
    'documents_with_document_id': sum(bool(x['document_id']) for x in docs),
    'duplicate_document_id_count': sum(1 for x in by_id.values() if len(x) > 1),
    'relationship_edge_count': len(matrix),
    'relationship_result_counts': dict(sorted(Counter(x['result'] for x in matrix).items())),
    'finding_result_counts': dict(sorted(Counter(x['result'] for x in findings).items())),
    'authority_cycle_nodes': sorted(cycle_nodes),
    'non_authoritative': True
}
(OUT/'reconciliation-summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n', encoding='utf-8')
manifest = {
    'repository': summary['repository'], 'scope': summary['scope'],
    'commit_sha': os.environ.get('GITHUB_SHA', ''),
    'workflow_run_id': os.environ.get('GITHUB_RUN_ID', ''),
    'generated_at': datetime.now(timezone.utc).isoformat(),
    'evidence_files': sorted(p.name for p in OUT.iterdir()),
    'non_authoritative_statement': 'Evidence and reconciliation only; no approval, canonicalization, activation, or authority creation.'
}
(OUT/'reconciliation-manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(summary, indent=2, sort_keys=True))
