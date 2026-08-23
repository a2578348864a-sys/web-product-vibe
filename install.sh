#!/usr/bin/env bash
set -euo pipefail

HOST_TYPE="${1:-all}"
PROJECT_ROOT="${2:-$PWD}"
PACKAGE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"

install_skill() {
  local source="$1"
  local destination="$2"
  mkdir -p "$(dirname "$destination")"
  if [[ -e "$destination" ]]; then
    mv "$destination" "${destination}.backup-${TIMESTAMP}"
    echo "Backed up: ${destination}.backup-${TIMESTAMP}"
  fi
  cp -R "$source" "$destination"
  echo "Installed: $destination"
}

case "$HOST_TYPE" in
  codex|dsh)
    install_skill "$PACKAGE_ROOT/skill/web-product-vibe" "$PROJECT_ROOT/.agents/skills/web-product-vibe"
    ;;
  claude)
    install_skill "$PACKAGE_ROOT/skill/web-product-vibe" "$PROJECT_ROOT/.claude/skills/web-product-vibe"
    ;;
  all)
    install_skill "$PACKAGE_ROOT/skill/web-product-vibe" "$PROJECT_ROOT/.agents/skills/web-product-vibe"
    install_skill "$PACKAGE_ROOT/skill/web-product-vibe" "$PROJECT_ROOT/.claude/skills/web-product-vibe"
    ;;
  *)
    echo "Usage: ./install.sh [codex|claude|dsh|all] [project-root]" >&2
    exit 2
    ;;
esac
