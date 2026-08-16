from pathlib import Path
from collections import Counter
import json, re, sys

SCORE_PATH = Path('artifacts/canonical-core-score-r00.json')
OUT_MD = Path('audit/canonical-core-qualification-matrix-r00.md')
OUT_JSON = Path('artifacts/canonical-core-qualification-r00.json')

CYCLE_IDS = {
    'BHG-MIG-304657D4691E','BHG-MIG-38F961165834','BHG-MIG-4EF6926C68EA',
    'BHG-MIG-71A9F2A90F32','BHG-MIG-83A30C7D861D','BHG-MIG-AB1A5B8A9156',
    'BHG-MIG-D13DBA24B680','BHG-MIG-D140A7A5674C'
}

ALLOWED_STATUS = {'Concept','Draft','Review','Proposed','Pre-Verified','Independently Reviewed','Approved','Canonical','Active','Effective','Enforced','Retired','Deprecated','Archived'}


def frontmatter(text):
    if not text.startswith('---\n'):
        return {}
    end = text.find('\n---', 4)
    if end < 0:
        return {}
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("'\"")
    return fm


def main():
    if not SCORE_PATH.exists():
        raise SystemExit(f'missing discovery score: {SCORE_PATH}')
    data = json.loads(SCORE_PATH.read_text(encoding='utf-8'))
    rows = data.get('rows', [])[:60]
    if len(rows) != 60:
        raise SystemExit(f'expected 60 discovery candidates, found {len(rows)}')

    qualified = []
    counts = Counter()
    for rank, row in enumerate(rows, 1):
        path = Path(row['path'])
        text = path.read_text(encoding='utf-8', errors='replace') if path.exists() else ''
        fm = frontmatter(text)
        status = str(fm.get('status') or row.get('status') or '')
        doc_type = str(fm.get('document_type') or row.get('document_type') or '')
        level = str(fm.get('governance_level') or row.get('governance_level') or '')
        owner = str(fm.get('owner') or '')
        approval = str(fm.get('approval_authority') or '')
        cycle = bool(row.get('authority_cycle_participation')) or row['document_id'] in CYCLE_IDS
        conflict = int(row.get('conflict_evidence', 0) or 0) > 0
        exists = path.exists()
        metadata_complete = all(k in fm for k in ('title','document_id','document_type','version','status','governance_level','owner','approval_authority')) if exists else False
        authority_signal = any(x in level.lower() for x in ('supreme','foundation','foundational','enterprise')) and bool(approval)
        contractuality = any(x in doc_type.lower() for x in ('standard','policy','model','constitution','governance','process','matrix')) or any('contract' in r.lower() for r in row.get('reasons', []))
        foundationality = any(x in level.lower() for x in ('supreme','foundation','foundational')) or 'foundation location' in ' '.join(row.get('reasons', [])).lower()

        if not exists or not metadata_complete:
            decision = 'HOLD'
        elif cycle or conflict:
            decision = 'HOLD'
        elif status in {'Draft','Review','Concept','Proposed','Pre-Verified'}:
            decision = 'HOLD'
        elif authority_signal and contractuality and foundationality:
            decision = 'CORE-CANDIDATE'
        elif contractuality or foundationality:
            decision = 'SUPPORTING-CANDIDATE'
        else:
            decision = 'EXCLUDE-FROM-CORE'
        counts[decision] += 1
        qualified.append({
            'rank': rank, 'document_id': row['document_id'], 'repository': row.get('repository'), 'path': row['path'],
            'score': row.get('score'), 'status': status, 'document_type': doc_type, 'governance_level': level,
            'owner': owner, 'approval_authority': approval, 'authority_signal': authority_signal,
            'contractuality': contractuality, 'foundationality': foundationality, 'ownership_evidence': bool(owner),
            'metadata_complete': metadata_complete, 'path_exists': exists, 'conflict': conflict, 'cycle': cycle,
            'decision': decision, 'discovery_reasons': row.get('reasons', [])
        })

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps({'phase':'Canonical Core Qualification R00','input_documents':data.get('corpus_documents'),'discovery_candidates':60,'counts':dict(counts),'rows':qualified}, indent=2, ensure_ascii=False), encoding='utf-8')

    lines = [
        '# Canonical Core Qualification Matrix R00','',
        'Status: CANDIDATE / NON-NORMATIVE','',
        f"Input corpus: **{data.get('corpus_documents')}** documents. Discovery candidates: **60**.",
        '',
        '## Decision rules',
        '- Centrality never creates authority.',
        '- Draft/Review/Concept/Proposed/Pre-Verified remain HOLD.',
        '- Any protected authority cycle remains HOLD.',
        '- Any conflict evidence remains HOLD.',
        '- Missing source path or required metadata remains HOLD.',
        '- Approved/Active/Effective status is evidence of lifecycle state, not a grant of new authority.',
        '',
        '## Results',
        f"- CORE-CANDIDATE: **{counts['CORE-CANDIDATE']}**",
        f"- SUPPORTING-CANDIDATE: **{counts['SUPPORTING-CANDIDATE']}**",
        f"- HOLD: **{counts['HOLD']}**",
        f"- EXCLUDE-FROM-CORE: **{counts['EXCLUDE-FROM-CORE']}**",
        '',
        '## Matrix',
        '| Rank | Document ID | Score | Status | Level | Contractuality | Foundationality | Conflict | Cycle | Evidence | Decision |',
        '|---:|---|---:|---|---|:---:|:---:|:---:|:---:|---|---|'
    ]
    for r in qualified:
        evidence = 'path+metadata' if r['path_exists'] and r['metadata_complete'] else 'incomplete'
        lines.append(f"| {r['rank']} | `{r['document_id']}` | {r['score']} | {r['status']} | {r['governance_level']} | {'Y' if r['contractuality'] else 'N'} | {'Y' if r['foundationality'] else 'N'} | {'Y' if r['conflict'] else 'N'} | {'Y' if r['cycle'] else 'N'} | {evidence} | **{r['decision']}** |")
    lines += ['', '## Gate interpretation', 'The output is a qualification candidate register, not normative approval. Final Canonical Core admission requires the applicable governance approval and independent verification.']
    OUT_MD.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(json.dumps({'counts':dict(counts),'rows':60}, indent=2))

if __name__ == '__main__':
    main()
