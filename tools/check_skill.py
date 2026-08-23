from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
base = root / "skill" / "web-product-vibe"
required = [
    "SKILL.md",
    "references/RESEARCH_METHOD.md",
    "templates/PRODUCT_BRIEF.md",
    "templates/SOLUTION_PROPOSAL.md",
    "templates/USER_JOURNEY.md",
    "templates/UX_SPEC.md",
    "templates/PROJECT_PLAN.md",
    "templates/PRODUCT_SKELETON.md",
    "templates/SCOPE.md",
    "templates/TECH_PLAN.md",
    "templates/IMPLEMENTATION_SLICE.md",
    "templates/ACCEPTANCE_REPORT.md",
]
root_required = [
    "README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
    "install.ps1", "install.sh", "VERSION", "docs/QUICK_START.md", "docs/WORKFLOW.md",
    "docs/DESIGN_PRINCIPLES.md", "platforms/CODEX.md", "platforms/CLAUDE_CODE.md",
    "platforms/DEEPSEEK_HARNESS.md",
]
errors = []

for rel in required:
    if not (base / rel).exists():
        errors.append(f"missing skill file: skill/web-product-vibe/{rel}")

for rel in root_required:
    if not (root / rel).exists():
        errors.append(f"missing project file: {rel}")

skill = base / "SKILL.md"
if skill.exists():
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md missing YAML frontmatter")
    if "name: web-product-vibe" not in text:
        errors.append("SKILL.md has invalid name")
    if "description:" not in text:
        errors.append("SKILL.md missing description")
    for mode in ["DISCOVER", "SYNTHESIZE", "DESIGN", "PLAN", "BUILD", "ACCEPT", "CHANGE", "AUDIT"]:
        if mode not in text:
            errors.append(f"SKILL.md missing mode: {mode}")
    lower = text.lower()
    required_phrases = {
        "real-browser": "real-browser acceptance rule",
        "product skeleton": "Product Skeleton rule",
        "no backend-first completion": "backend-first prevention rule",
        "continuous execution contract": "continuous execution contract",
        "comprehensive project plan": "comprehensive project-plan rule",
        "confirmed fact": "fact/interpretation/assumption separation",
    }
    for phrase, label in required_phrases.items():
        if phrase not in lower:
            errors.append(f"SKILL.md missing {label}")
    for label in ["Backend PASS", "Frontend PASS", "Slice DONE", "Project DONE"]:
        if label not in text:
            errors.append(f"SKILL.md missing completion label: {label}")

project_plan = base / "templates" / "PROJECT_PLAN.md"
if project_plan.exists():
    plan_text = project_plan.read_text(encoding="utf-8").lower()
    for section in [
        "frontend plan", "backend plan", "data and source-of-truth plan", "security, privacy, and permissions",
        "testing strategy", "deployment and release", "product skeleton", "vertical implementation slices",
        "front/back sync contract", "readiness / freeze checklist"
    ]:
        if section not in plan_text:
            errors.append(f"PROJECT_PLAN.md missing section: {section}")

version = (root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").exists() else ""
for readme in ["README.md", "README.zh-CN.md"]:
    p = root / readme
    if p.exists() and version and version not in p.read_text(encoding="utf-8"):
        errors.append(f"{readme} does not mention current version {version}")

if (root / ".deepcode").exists():
    errors.append("obsolete .deepcode adapter still present")

if errors:
    print("FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("PASS: canonical skill package is valid for Codex + Claude Code + DeepSeek Harness installation")