#!/usr/bin/env bash
set -euo pipefail
OWNER="${1:-ekhamis}"
REPOSITORY="${2:-institutional-trading-academy}"
VISIBILITY="${3:-private}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

command -v git >/dev/null || { echo "git is required" >&2; exit 1; }
command -v gh >/dev/null || { echo "GitHub CLI is required: https://cli.github.com" >&2; exit 1; }
gh auth status >/dev/null 2>&1 || gh auth login --web --git-protocol https
python3 scripts/validate_project.py

if [[ ! -d .git ]]; then
  git init -b main
  git config user.name "Eyad Khamis"
  git config user.email "ekhamis@gmail.com"
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "chore: establish ITA English-first academy repository v$(cat VERSION)"
fi

FULL_NAME="$OWNER/$REPOSITORY"
if gh repo view "$FULL_NAME" >/dev/null 2>&1; then
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$FULL_NAME.git"
  git push -u origin main
else
  gh repo create "$FULL_NAME" --"$VISIBILITY" --source . --remote origin --push \
    --description "English-first, dual-language-ready Institutional Trading Academy"
fi
printf 'Published: https://github.com/%s\n' "$FULL_NAME"
