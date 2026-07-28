# Institutional Trading Academy

English-first, dual-language-ready trading and market-intelligence education platform.

## Current release candidate

- Version: **0.8.0** merged and validated on `main` (release-ready but unpublished; latest published release remains v0.6.0)
- Canonical language: **English (`en-US`)**
- Arabic: **architecture and RTL scaffolding only; content deferred until English v1.0.0 lock**
- Authored missions: **70**
- Handbook: English Missions 01-70 source package; prior PDF/DOCX handbook assets remain historical
- Prototype: browser dashboard in `prototype/` (prototype content refresh is outside this release scope)

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
