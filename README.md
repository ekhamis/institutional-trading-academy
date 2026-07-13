# Institutional Trading Academy

English-first, dual-language-ready trading and market-intelligence education platform.

## Current verified build

- Version: **0.5.0**
- Canonical language: **English (`en-US`)**
- Arabic: **architecture and RTL scaffolding only; content deferred until English lock**
- Authored missions: **40**
- Handbook: English Missions 01-40 source package and prior PDF/DOCX handbook assets
- Prototype: browser dashboard in `prototype/`

## Repository structure

- `content/en-US/` — canonical English missions
- `content/ar/` — deferred Arabic content structure
- `data/` — curriculum, missions, sources, skills, faculty, localization status
- `assets/illustrations/` — instructional diagrams
- `handbooks/` — generated English handbook outputs
- `prototype/` — clickable dashboard prototype
- `docs/` — product, curriculum, AI, UX, assessment, and roadmap specifications
- `schemas/` — structured content schemas
- `scripts/` — validation, packaging, and publishing utilities
- `.github/workflows/` — automated validation, packaging, and releases

## Validate locally

```bash
python scripts/validate_project.py
```

## Package locally

```bash
python scripts/package_release.py
```

## Publish to GitHub from Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\publish_to_github.ps1
```

See [`docs/15_GITHUB_AUTOMATION.md`](docs/15_GITHUB_AUTOMATION.md) for the full workflow.

## Educational safeguards

This project is educational. It is not a signal service, does not promise returns, and must keep risk management ahead of leverage and execution.
