param(
    [string]$Owner = "ekhamis",
    [string]$Repository = "institutional-trading-academy",
    [ValidateSet("private", "public", "internal")]
    [string]$Visibility = "private"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or is not available in PATH."
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI is required. Install it with: winget install --id GitHub.cli"
}
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python is required and is not available in PATH."
}

gh auth status 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "GitHub authentication is required. A browser sign-in will open." -ForegroundColor Yellow
    gh auth login --web --git-protocol https
    if ($LASTEXITCODE -ne 0) { throw "GitHub authentication failed." }
}

python scripts/validate_project.py
if ($LASTEXITCODE -ne 0) { throw "Project validation failed." }

if (-not (Test-Path ".git")) {
    git init -b main
    git config user.name "Eyad Khamis"
    git config user.email "ekhamis@gmail.com"
}

git add .
$changes = git status --porcelain
if ($changes) {
    $Version = (Get-Content VERSION -Raw).Trim()
    git commit -m "chore: establish ITA English-first academy repository v$Version"
    if ($LASTEXITCODE -ne 0) { throw "Git commit failed." }
}

$FullName = "$Owner/$Repository"
gh repo view $FullName 2>$null | Out-Null
$RepoExists = ($LASTEXITCODE -eq 0)

if (-not $RepoExists) {
    $VisibilityFlag = switch ($Visibility) {
        "private"  { "--private" }
        "public"   { "--public" }
        "internal" { "--internal" }
    }
    & gh repo create $FullName $VisibilityFlag --source . --remote origin --push --description "English-first, dual-language-ready Institutional Trading Academy"
    if ($LASTEXITCODE -ne 0) { throw "Repository creation or initial push failed." }
} else {
    git remote get-url origin 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        git remote add origin "https://github.com/$FullName.git"
    }
    git push -u origin main
    if ($LASTEXITCODE -ne 0) { throw "Git push failed." }
}

Write-Host "Published: https://github.com/$FullName" -ForegroundColor Green
