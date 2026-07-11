param(
    [string]$Owner = "ekhamis",
    [string]$Repository = "institutional-trading-academy",
    [ValidateSet("private", "public")]
    [string]$Visibility = "private"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Prevent expected non-zero native exit codes from becoming terminating
# PowerShell errors while we perform existence checks.
if (Test-Path variable:PSNativeCommandUseErrorActionPreference) {
    $PSNativeCommandUseErrorActionPreference = $false
}

function Require-Command {
    param([Parameter(Mandatory = $true)][string]$Name)

    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

function Run-Checked {
    param(
        [Parameter(Mandatory = $true)][string]$Command,
        [Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments
    )

    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "'$Command $($Arguments -join ' ')' failed with exit code $LASTEXITCODE."
    }
}

Require-Command git
Require-Command gh

# The script may be placed either in the repository root or in its scripts folder.
$CandidateRoot = $PSScriptRoot
if ((Split-Path $PSScriptRoot -Leaf) -eq "scripts") {
    $CandidateRoot = Split-Path $PSScriptRoot -Parent
}

Set-Location $CandidateRoot
$RepoRoot = (Get-Location).Path
$FullName = "$Owner/$Repository"
$ExpectedRemote = "https://github.com/$FullName.git"

Write-Host ""
Write-Host "Repository folder: $RepoRoot" -ForegroundColor Cyan
Write-Host "GitHub repository: $FullName" -ForegroundColor Cyan
Write-Host ""

# Authenticate if needed.
$OldPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
& gh auth status *> $null
$Authenticated = ($LASTEXITCODE -eq 0)
$ErrorActionPreference = $OldPreference

if (-not $Authenticated) {
    Write-Host "GitHub authentication is required. Opening browser login..." -ForegroundColor Yellow
    Run-Checked gh auth login --hostname github.com --git-protocol https --web
}

$Login = (& gh api user --jq ".login").Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($Login)) {
    throw "Could not determine the authenticated GitHub account."
}

if ($Login -ne $Owner) {
    throw "GitHub CLI is authenticated as '$Login', but the requested owner is '$Owner'. Run 'gh auth switch' or rerun this script with -Owner '$Login'."
}

# Initialize Git if the extracted package has no .git directory.
if (-not (Test-Path ".git")) {
    Write-Host "Initializing local Git repository..." -ForegroundColor Yellow
    Run-Checked git init
}

Run-Checked git branch -M main

# Ensure there is at least one commit.
Run-Checked git add --all

$OldPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
& git diff --cached --quiet
$HasStagedChanges = ($LASTEXITCODE -ne 0)
$ErrorActionPreference = $OldPreference

if ($HasStagedChanges) {
    $OldPreference = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"
    & git config user.name *> $null
    $HasUserName = ($LASTEXITCODE -eq 0)
    & git config user.email *> $null
    $HasUserEmail = ($LASTEXITCODE -eq 0)
    $ErrorActionPreference = $OldPreference

    if (-not $HasUserName) {
        Run-Checked git config user.name "Eyad Khamis"
    }
    if (-not $HasUserEmail) {
        Run-Checked git config user.email "ekhamis@gmail.com"
    }

    Run-Checked git commit -m "Initial Institutional Trading Academy import"
}
else {
    Write-Host "No uncommitted file changes detected." -ForegroundColor DarkGray
}

# Check whether the GitHub repository exists.
# A missing repository is expected on the first run and must not terminate the script.
$OldPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
& gh repo view $FullName --json name *> $null
$RepoExists = ($LASTEXITCODE -eq 0)
$ErrorActionPreference = $OldPreference

if (-not $RepoExists) {
    Write-Host "Creating $Visibility GitHub repository '$FullName'..." -ForegroundColor Yellow

    if ($Visibility -eq "public") {
        Run-Checked gh repo create $FullName --public --source "." --remote "origin"
    }
    else {
        Run-Checked gh repo create $FullName --private --source "." --remote "origin"
    }
}
else {
    Write-Host "GitHub repository already exists." -ForegroundColor Green

    $OldPreference = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"
    $CurrentRemote = (& git remote get-url origin 2>$null)
    $OriginExists = ($LASTEXITCODE -eq 0)
    $ErrorActionPreference = $OldPreference

    if (-not $OriginExists) {
        Run-Checked git remote add origin $ExpectedRemote
    }
    elseif ($CurrentRemote.Trim() -ne $ExpectedRemote) {
        Write-Host "Correcting the origin remote..." -ForegroundColor Yellow
        Run-Checked git remote set-url origin $ExpectedRemote
    }
}

Write-Host "Pushing the main branch..." -ForegroundColor Yellow
Run-Checked git push --set-upstream origin main

Write-Host ""
Write-Host "Published successfully:" -ForegroundColor Green
Write-Host "https://github.com/$FullName" -ForegroundColor Cyan
