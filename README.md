# Institutional Trading Academy

English-first, dual-language-ready trading and market-intelligence education platform.

## Current build candidate

- Version: **0.8.0** candidate on `agent/ita-v0.8.0-master-build` (baseline v0.7.0 verified on `main`; latest published release remains v0.6.0)
- Canonical language: **English (`en-US`)**
- Arabic: **architecture and RTL scaffolding only; content deferred until English lock**
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

## Build the handbook

```bash
python scripts/build_handbook.py
```

## Package locally

```bash
python scripts/package_release.py
```

## Push the v0.8.0 candidate from Windows

Double-click `PUSH_v0.8.0.cmd`, or run:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\push_v0.8_candidate.ps1
```

This candidate-specific script verifies the exact v0.7.0 base, applies only the release manifest, validates and packages the build, pushes an isolated branch, and opens a draft pull request. See [`docs/26_RELEASE_HANDOFF_v0.8.md`](docs/26_RELEASE_HANDOFF_v0.8.md) for the recorded handoff and remaining release gates.

## Educational safeguards

This project is educational. It is not a signal service, does not promise returns, and must keep risk management ahead of leverage and execution. Order-flow displays are data-source dependent and must not be presented as proof of participant identity, intent, or future direction.
