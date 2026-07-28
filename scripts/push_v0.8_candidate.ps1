param(
    [string]$Owner = "ekhamis",
    [string]$Repository = "institutional-trading-academy",
    [string]$Branch = "agent/ita-v0.8.0-master-build",
    [string]$BaseSha = "9b06d41a018248a0b4664449bb958f793cceebbc",
    [string]$DestinationPath = ""
)

$ErrorActionPreference = "Stop"
$SourceRoot = Split-Path -Parent $PSScriptRoot
$ManifestPath = Join-Path $SourceRoot "release/v0.8.0/update_manifest.txt"
$FullName = "$Owner/$Repository"

if (-not $DestinationPath) {
    $DestinationPath = Join-Path (Split-Path -Parent $SourceRoot) "ITA_v0.8.0_push"
}

foreach ($Command in @("git", "gh")) {
    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        throw "$Command is required and is not available in PATH."
    }
}

if (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonExe = "py"
    $PythonPrefix = @("-3")
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonExe = "python"
    $PythonPrefix = @()
} else {
    throw "Python 3 is required and is not available in PATH."
}

if (-not (Test-Path $ManifestPath)) {
    throw "Update manifest not found: $ManifestPath"
}

$ManifestEntries = Get-Content $ManifestPath | ForEach-Object { $_.Trim() } | Where-Object { $_ -and -not $_.StartsWith("#") }
if (-not $ManifestEntries) {
    throw "The v0.8.0 update manifest is empty."
}

$Missing = @($ManifestEntries | Where-Object { -not (Test-Path (Join-Path $SourceRoot $_)) })
if ($Missing.Count -gt 0) {
    throw "Candidate package is incomplete. Missing: $($Missing -join ', ')"
}

& gh auth status 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "GitHub authentication is required. A browser sign-in will open." -ForegroundColor Yellow
    & gh auth login --web --git-protocol https
    if ($LASTEXITCODE -ne 0) { throw "GitHub authentication failed." }
}
& gh auth setup-git
if ($LASTEXITCODE -ne 0) { throw "GitHub could not configure Git authentication." }

if (Test-Path $DestinationPath) {
    $Existing = @(Get-ChildItem -Force $DestinationPath -ErrorAction SilentlyContinue)
    if ($Existing.Count -gt 0) {
        throw "Destination is not empty: $DestinationPath. Choose a new -DestinationPath."
    }
} else {
    New-Item -ItemType Directory -Path $DestinationPath | Out-Null
}

$CloneParent = Split-Path -Parent $DestinationPath
$CloneName = Split-Path -Leaf $DestinationPath
Set-Location $CloneParent
& git clone "https://github.com/$FullName.git" $CloneName
if ($LASTEXITCODE -ne 0) { throw "Repository clone failed." }
Set-Location $DestinationPath

& git checkout main
& git pull --ff-only origin main
$CurrentSha = (& git rev-parse HEAD).Trim()
if ($CurrentSha -ne $BaseSha) {
    throw "Safety stop: main is $CurrentSha, but this candidate was built from $BaseSha. Review and rebase before applying it."
}

& git ls-remote --exit-code --heads origin $Branch 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    throw "Remote branch already exists: $Branch. Review it before running this script again."
}

& git checkout -b $Branch
if ($LASTEXITCODE -ne 0) { throw "Could not create build branch $Branch." }

foreach ($RelativePath in $ManifestEntries) {
    $Source = Join-Path $SourceRoot $RelativePath
    $Target = Join-Path $DestinationPath $RelativePath
    $TargetDirectory = Split-Path -Parent $Target
    if (-not (Test-Path $TargetDirectory)) {
        New-Item -ItemType Directory -Force -Path $TargetDirectory | Out-Null
    }
    Copy-Item -LiteralPath $Source -Destination $Target -Force
}

& $PythonExe @PythonPrefix scripts/build_handbook.py
if ($LASTEXITCODE -ne 0) { throw "Handbook build failed." }
& $PythonExe @PythonPrefix scripts/validate_project.py
if ($LASTEXITCODE -ne 0) { throw "Project validation failed." }
& $PythonExe @PythonPrefix scripts/package_release.py
if ($LASTEXITCODE -ne 0) { throw "Release packaging failed." }

if (-not (& git config user.name)) { & git config user.name "Eyad Khamis" }
if (-not (& git config user.email)) { & git config user.email "ekhamis@gmail.com" }

& git add -- $ManifestEntries
if ($LASTEXITCODE -ne 0) { throw "Staging failed." }
& git diff --cached --quiet
if ($LASTEXITCODE -eq 0) { throw "No candidate changes were staged." }

& git commit -m "build: add v0.8.0 liquidity and order flow candidate"
if ($LASTEXITCODE -ne 0) { throw "Commit failed." }
& git push -u origin $Branch
if ($LASTEXITCODE -ne 0) { throw "Branch push failed." }

$PrBody = @"
## Summary
- expands the canonical English curriculum from 60 to 70 missions
- begins Level 4 with liquidity and order-flow data literacy
- adds ten numbered instructional illustrations and the cumulative English handbook
- makes handbook generation and validation mission-count aware

## Validation
- 70 canonical English missions
- 0 errors
- 0 warnings
- local v0.8.0 ZIP generated

## Release discipline
This is a draft build candidate. Do not tag or publish v0.8.0 until branch validation passes, the candidate is merged to main with authorization, and main validation passes.
"@
$PrBodyPath = Join-Path $env:TEMP "ita-v0.8.0-pr-body.md"
Set-Content -Path $PrBodyPath -Value $PrBody -Encoding UTF8

$PrUrl = & gh pr create --repo $FullName --draft --base main --head $Branch --title "build: add v0.8.0 liquidity and order flow candidate" --body-file $PrBodyPath
if ($LASTEXITCODE -ne 0) { throw "Draft pull request creation failed." }

Write-Host "Validated candidate branch pushed: $Branch" -ForegroundColor Green
Write-Host "Draft pull request: $PrUrl" -ForegroundColor Green
Write-Host "Local package: $(Join-Path $DestinationPath 'dist/institutional-trading-academy-v0.8.0.zip')" -ForegroundColor Green
