from pathlib import Path
import hashlib
import re
import subprocess
import yaml

BASELINE = "8685abae60b176dcb3042400ebacc01b7dea97a5"
ROOT = Path(".")
CANONICAL_KEYS = {
    "title", "document_id", "document_type", "version", "status",
    "governance_level", "owner", "approval_authority", "created",
    "last_updated", "effective_date", "classification", "language",
    "repository", "governed_by", "governs", "depends_on", "related_to",
    "extensions",
}
ALIASES = {
    "document-id": "document_id", "documentId": "document_id", "id": "document_id",
    "document-type": "document_type", "documentType": "document_type",
    "governance-level": "governance_level", "governanceLevel": "governance_level",
    "approval-authority": "approval_authority", "approvalAuthority": "approval_authority",
    "effective-date": "effective_date", "effectiveDate": "effective_date",
    "last-updated": "last_updated", "lastUpdated": "last_updated", "updated": "last_updated",
    "created-date": "created", "created_at": "created", "created-at": "created",
    "approved-by": "approved_by", "approvedBy": "approved_by",
    "review-authority": "review_authority", "reviewAuthority": "review_authority",
    "governing-authority": "governing_authority",
    "related-to": "related_to", "depends-on": "depends_on", "governed-by": "governed_by",
    "superseded-by": "superseded_by", "supersedes": "supersedes",
}
STATUS_MAP = {
    "draft": "Draft", "review": "Review", "approved": "Approved", "active": "Active",
    "effective": "Effective", "deprecated": "Deprecated", "archived": "Archived",
    "concept": "Concept", "official": "Review",
}
DUPLICATE_OWNERS = {
    "BHG-POL-001": "docs/01-POLICIES/POLICY_HIERARCHY.md",
    "GEN-BHG-ENG-013": "docs/04-AI/GENESIS/GENESIS_PROVIDER_ABSTRACTION.md",
}

def git_date(path, latest=False):
    args = ["git", "log", "--follow", "--format=%cs", "--", str(path)]
    if latest:
        args = ["git", "log", "-1", "--format=%cs", "--", str(path)]
    try:
        out = subprocess.check_output(args, text=True, stderr=subprocess.DEVNULL).splitlines()
        if out:
            return out[0] if latest else out[-1]
    except Exception:
        pass
    return "2026-08-16"

def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end < 0:
        return None, text
    block = text[4:end]
    try:
        data = yaml.safe_load(block) or {}
    except Exception:
        data = {}
    body = text[end + 4:]
    return data, body.lstrip("\n")

def title_from(path, body):
    match = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    return match.group(1).strip() if match else path.stem.replace("_", " ").replace("-", " ").title()

def infer_type(path):
    p = str(path)
    if "docs/01-POLICIES/" in p: return "Policy"
    if "docs/02-STANDARDS/" in p: return "Standard"
    if "docs/03-ENGINEERING/" in p: return "Engineering Standard"
    if "docs/04-AI/" in p: return "AI Document"
    if "docs/05-AUTOMATION/" in p: return "Automation Document"
    if "docs/06-AUDIT/" in p: return "Audit Record"
    if "docs/99-HISTORY/" in p: return "Historical Record"
    if "docs/00-GOVERNANCE/" in p: return "Governance Document"
    if "docs/00-FOUNDATION/" in p: return "Governance Model"
    return "Repository Record"

def infer_level(path):
    p = str(path)
    for token, level in [
        ("01-POLICIES", "Policy"), ("02-STANDARDS", "Standard"),
        ("03-ENGINEERING", "Engineering"), ("04-AI", "AI"),
        ("05-AUTOMATION", "Automation"), ("06-AUDIT", "Audit"),
        ("99-HISTORY", "History"),
    ]:
        if token in p: return level
    if "00-FOUNDATION" in p or "00-GOVERNANCE" in p: return "Enterprise"
    return "Repository"

def make_id(path):
    return "BHG-MIG-" + hashlib.sha256((BASELINE + "|" + str(path)).encode()).hexdigest()[:12].upper()

def normalize_key(key):
    return ALIASES.get(str(key), str(key))

changed = []
registry = []

for path in sorted(ROOT.rglob("*.md")):
    if ".git/" in str(path):
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    data, body = parse_frontmatter(text)
    original = dict(data or {})
    had_frontmatter = data is not None
    data = data or {}
    canonical = {}
    legacy = {}

    for key, value in data.items():
        normalized = normalize_key(key)
        if normalized in CANONICAL_KEYS and normalized not in canonical:
            canonical[normalized] = value
        else:
            legacy[str(key)] = value

    canonical["title"] = canonical.get("title") or title_from(path, body)

    if not canonical.get("document_id"):
        canonical["document_id"] = make_id(path)
        registry.append((str(path), canonical["document_id"], "generated_missing_identity"))

    if canonical["document_id"] in DUPLICATE_OWNERS and str(path) != DUPLICATE_OWNERS[canonical["document_id"]]:
        old = canonical["document_id"]
        canonical["document_id"] = make_id(path)
        registry.append((str(path), canonical["document_id"], f"duplicate_identity_reassigned_from_{old}"))

    canonical["document_type"] = canonical.get("document_type") or infer_type(path)
    canonical["version"] = canonical.get("version") or "0.1.0"

    raw_status = str(canonical.get("status", "")).strip()
    canonical["status"] = STATUS_MAP.get(raw_status.lower(), "Draft")
    if raw_status and raw_status.lower() == "official":
        legacy["legacy_status"] = raw_status

    canonical["governance_level"] = canonical.get("governance_level") or infer_level(path)
    canonical["owner"] = canonical.get("owner") or "BHG Governance Council"
    canonical["approval_authority"] = canonical.get("approval_authority") or "BHG Governance Council"
    canonical["created"] = canonical.get("created") or git_date(path)
    canonical["last_updated"] = canonical.get("last_updated") or git_date(path, latest=True)
    canonical["effective_date"] = canonical.get("effective_date", None)
    canonical["classification"] = canonical.get("classification") or "Internal"
    canonical["language"] = canonical.get("language") or "en"
    canonical["repository"] = canonical.get("repository") or "BHG-GOVERNANCE"

    if "document_type" in original and original.get("document_type") != canonical["document_type"]:
        legacy["legacy_document_type"] = original.get("document_type")

    if legacy:
        canonical["extensions"] = {
            "legacy_metadata": legacy,
            "normalization": {
                "baseline": BASELINE,
                "performed": "2026-08-16",
                "mode": "controlled_reconciliation",
            },
        }
    else:
        canonical["extensions"] = canonical.get("extensions") or {
            "normalization": {
                "baseline": BASELINE,
                "performed": "2026-08-16",
                "mode": "controlled_reconciliation",
            }
        }

    output = "---\n" + yaml.safe_dump(
        canonical, sort_keys=False, allow_unicode=True, default_flow_style=False
    ).strip() + "\n---\n\n" + body

    if output != text:
        path.write_text(output, encoding="utf-8")
        changed.append(str(path))

register = ROOT / "docs/00-GOVERNANCE/BHG_DOCUMENT_ID_MIGRATION_REGISTER_V0_1.md"
lines = [
    "---", "document_id: BHG-GOV-DIMR-001", "title: BHG Document ID Migration Register",
    "document_type: Governance Reconciliation Matrix", "version: 0.1.0", "status: Review",
    "governance_level: Enterprise", "owner: BHG Governance Council",
    "approval_authority: BHG Governance Council", "created: 2026-08-16",
    "last_updated: 2026-08-16", "effective_date: null", "classification: Internal",
    "language: en", "repository: BHG-GOVERNANCE", "governed_by:",
    "  - BHG_CONSTITUTION", "  - DOCUMENT_METADATA_STANDARD", "  - DOCUMENT_IDENTIFIER_STANDARD",
    "---", "", "# BHG Document ID Migration Register v0.1", "",
    "This register records deterministic identity assignments and duplicate-ID remediation performed against the N3-N5 remediation baseline. Generated IDs are permanent assignments from this migration event and are not recomputed from filenames after assignment.",
    "", "| Path | Assigned ID | Reason |", "|---|---|---|",
]
for path, doc_id, reason in registry:
    lines.append(f"| `{path}` | `{doc_id}` | `{reason}` |")
register.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"changed={len(changed)} generated_or_reassigned_ids={len(registry)}")