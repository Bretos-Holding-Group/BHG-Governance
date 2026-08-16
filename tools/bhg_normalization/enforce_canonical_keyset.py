from pathlib import Path
import yaml

REQUIRED_RELATIONSHIP_KEYS = ["governed_by", "governs", "depends_on", "related_to"]

for path in sorted(Path('.').rglob('*.md')):
    if '.git/' in str(path):
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    if not text.startswith('---\n'):
        continue
    end = text.find('\n---', 4)
    if end < 0:
        continue
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except Exception:
        continue
    body = text[end + 4:].lstrip('\n')
    changed = False
    for key in REQUIRED_RELATIONSHIP_KEYS:
        if key not in data:
            data[key] = []
            changed = True
    if 'extensions' not in data:
        data['extensions'] = {'normalization': {'mode': 'canonical_keyset_enforcement', 'performed': '2026-08-16'}}
        changed = True
    if changed:
        out = '---\n' + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False).strip() + '\n---\n\n' + body
        path.write_text(out, encoding='utf-8')
