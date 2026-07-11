# GitHub Automation

## Purpose
GitHub becomes the persistent source of truth for the Institutional Trading Academy. The repository preserves version history and automatically validates and packages each build.

## Automated workflows

### Validate and package
Runs on every push to `main`, every pull request, and manual dispatch.

It:
1. Parses every JSON file.
2. Checks mission IDs and prerequisites.
3. Checks illustration and source references.
4. Checks English-first localization rules.
5. Rejects Windows-incompatible filenames.
6. Produces a downloadable versioned ZIP artifact.

### Publish release
Runs when a semantic-version tag such as `v0.3.0` is pushed, or manually from GitHub Actions.

It validates the repository, creates a clean ZIP, and publishes a GitHub Release.

## One-command publishing from Windows
Run PowerShell from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\publish_to_github.ps1
```

The script defaults to:

- Owner: `ekhamis`
- Repository: `institutional-trading-academy`
- Visibility: `private`

Override the values when needed:

```powershell
.\scripts\publish_to_github.ps1 -Owner "ekhamis" -Repository "institutional-trading-academy" -Visibility private
```

The script uses GitHub CLI browser authentication and does not ask you to paste a personal access token into the project.

## Creating a release

```bash
git tag v0.3.0
git push origin v0.3.0
```

GitHub Actions will validate the repository and attach a clean ZIP to the release.

## Important limitation
The included automation validates, versions, packages, and releases content. It does not autonomously write new trading lessons. New content must be created in a controlled build run, reviewed, committed, and then GitHub automates validation and release.
