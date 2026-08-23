from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
base = root / "skill" / "web-product-vibe"
required = [
    "SKILL.md",
    "references/RESEARCH_METHOD.md",
    "references/INSPIRATION.md",
    "templates/PRODUCT_BRIEF.md",
    "templates/USER_JOURNEY.md",
    "templates/UX_SPEC.md",
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
    for mode in ["DISCOVER", "DESIGN", "PLAN", "BUILD", "ACCEPT", "CHANGE", "AUDIT"]:
        if mode not in text:
            errors.append(f"SKILL.md missing mode: {mode}")
    lower = text.lower()
    if "real-browser" not in lower:
        errors.append("SKILL.md missing real-browser acceptance rule")
    if "product skeleton" not in lower:
        errors.append("SKILL.md missing Product Skeleton rule")
    if "no backend-first completion" not in lower:
        errors.append("SKILL.md missing backend-first prevention rule")
    if "continuous execution contract" not in lower:
        errors.append("SKILL.md missing continuous execution contract")
    for label in ["Backend PASS", "Frontend PASS", "Slice DONE"]:
        if label not in text:
            errors.append(f"SKILL.md missing completion label: {label}")

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
