param(
    [ValidateSet("pull-request", "direct")]
    [string]$Mode = "pull-request"
)

$ErrorActionPreference = "Stop"

$Owner = "ekhamis"
$Repo = "institutional-trading-academy"
$FullName = "$Owner/$Repo"
$WorkRoot = Join-Path $env:USERPROFILE "Documents\Codex\ITA_GitHub_App_Work"
$RepoPath = Join-Path $WorkRoot $Repo
$TokenScript = Join-Path $PSScriptRoot "app_token_v2.py"

function Find-Python {
    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) { return @("py", "-3") }

    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) { return @("python") }

    throw "Python 3 was not found. Install Python 3, then run this publisher again."
}

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$GitArgs
    )
    & git @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($GitArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
}

function Copy-DirectoryContents {
    param(
        [string]$Source,
        [string]$Destination
    )

    Get-ChildItem -LiteralPath $Destination -Force |
        Where-Object { $_.Name -ne ".git" } |
        ForEach-Object {
            if ($_.PSIsContainer) {
                Remove-Item -LiteralPath $_.FullName -Recurse -Force
            } else {
                Remove-Item -LiteralPath $_.FullName -Force
            }
        }

    Get-ChildItem -LiteralPath $Source -Force |
        ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
        }
}

function Resolve-PackageRoot {
    param([string]$ExtractedRoot)

    $children = Get-ChildItem -LiteralPath $ExtractedRoot -Force
    $directories = @($children | Where-Object { $_.PSIsContainer })
    $files = @($children | Where-Object { -not $_.PSIsContainer })

    if ($directories.Count -eq 1 -and $files.Count -eq 0) {
        return $directories[0].FullName
    }

    return $ExtractedRoot
}

function New-GitHubPullRequest {
    param(
        [string]$Token,
        [string]$Owner,
        [string]$Repo,
        [string]$Head,
        [string]$Base,
        [string]$Title,
        [string]$Body
    )

    $headers = @{
        "Accept" = "application/vnd.github+json"
        "X-GitHub-Api-Version" = "2022-11-28"
        "Authorization" = "Bearer $Token"
        "User-Agent" = "ita-github-app-publisher-v2"
    }

    $payload = @{
        title = $Title
        head = $Head
        base = $Base
        body = $Body
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Method Post -Uri "https://api.github.com/repos/$Owner/$Repo/pulls" -Headers $headers -Body $payload -ContentType "application/json"
        Write-Host "Pull request created: $($response.html_url)"
    }
    catch {
        $message = $_.Exception.Message
        Write-Host "Pull request creation did not complete automatically: $message"
        Write-Host "The branch was pushed. Open a PR manually from branch: $Head"
    }
}

function Backup-And-Reclone {
    param(
        [string]$RepoPath,
        [string]$WorkRoot,
        [string]$AuthRemote
    )

    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backup = Join-Path $WorkRoot ("institutional-trading-academy.backup-" + $stamp)
    Write-Host "Existing automation work copy has uncommitted changes."
    Write-Host "Renaming it to: $backup"
    Set-Location $WorkRoot
    Move-Item -LiteralPath $RepoPath -Destination $backup
    Write-Host "Cloning a fresh work copy..."
    Invoke-Git @("clone", $AuthRemote, $RepoPath)
}

Write-Host "ITA GitHub App Publisher v2"
Write-Host "Repository: $FullName"
Write-Host "Mode: $Mode"
Write-Host ""

$Package = Read-Host "Full path to the verified academy release ZIP"
$Version = Read-Host "Version string, for example v0.4.0"

if (-not (Test-Path -LiteralPath $Package)) {
    throw "Package not found: $Package"
}

if ($Version -notmatch '^v\d+\.\d+\.\d+$') {
    throw "Version must look like v0.4.0"
}

$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) { throw "Git was not found. Install Git for Windows first." }

$PythonCmd = Find-Python
$PythonExe = $PythonCmd[0]
$PythonArgs = @()
if ($PythonCmd.Length -gt 1) {
    $PythonArgs = $PythonCmd[1..($PythonCmd.Length - 1)]
}

Write-Host "Generating short-lived GitHub App token..."
$TokenOutput = & $PythonExe @($PythonArgs + @($TokenScript)) 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host $TokenOutput
    throw "Failed to generate GitHub App token."
}
$Token = ($TokenOutput | Select-Object -Last 1).Trim()
if (-not $Token) { throw "Token generation returned empty output." }

$AuthRemote = "https://x-access-token:$Token@github.com/$FullName.git"
$CleanRemote = "https://github.com/$FullName.git"

New-Item -ItemType Directory -Force -Path $WorkRoot | Out-Null

if (-not (Test-Path -LiteralPath (Join-Path $RepoPath ".git"))) {
    Write-Host "Cloning repository into $RepoPath..."
    Invoke-Git @("clone", $AuthRemote, $RepoPath)
}

Set-Location $RepoPath
Invoke-Git @("remote", "set-url", "origin", $AuthRemote)
Invoke-Git @("fetch", "origin")
Invoke-Git @("checkout", "main")
Invoke-Git @("pull", "--ff-only", "origin", "main")

$status = git status --porcelain
if ($status) {
    git remote set-url origin $CleanRemote 2>$null | Out-Null
    Backup-And-Reclone -RepoPath $RepoPath -WorkRoot $WorkRoot -AuthRemote $AuthRemote
    Set-Location $RepoPath
    Invoke-Git @("remote", "set-url", "origin", $AuthRemote)
    Invoke-Git @("fetch", "origin")
    Invoke-Git @("checkout", "main")
    Invoke-Git @("pull", "--ff-only", "origin", "main")
}

$Branch = "release/$Version"
if ($Mode -eq "pull-request") {
    Invoke-Git @("checkout", "-B", $Branch, "origin/main")
} else {
    Invoke-Git @("checkout", "main")
}

$TempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("ita_release_" + [Guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force -Path $TempRoot | Out-Null

try {
    Write-Host "Extracting package..."
    Expand-Archive -LiteralPath $Package -DestinationPath $TempRoot -Force
    $PackageRoot = Resolve-PackageRoot -ExtractedRoot $TempRoot

    if (-not (Test-Path -LiteralPath (Join-Path $PackageRoot "README.md"))) {
        Write-Host "Warning: README.md was not found at package root. Continuing, but verify this is the intended release package."
    }

    Write-Host "Applying package snapshot to repository work copy..."
    Copy-DirectoryContents -Source $PackageRoot -Destination $RepoPath

    Invoke-Git @("add", "-A")
    $changes = git status --porcelain
    if (-not $changes) {
        Write-Host "No file changes detected. Nothing to publish."
        Invoke-Git @("remote", "set-url", "origin", $CleanRemote)
        exit 0
    }

    Invoke-Git @("config", "user.name", "ita-academy-builder-ek[bot]")
    Invoke-Git @("config", "user.email", "ita-academy-builder-ek[bot]@users.noreply.github.com")

    Invoke-Git @("commit", "-m", "Release $Version")

    if ($Mode -eq "pull-request") {
        Write-Host "Pushing release branch..."
        Invoke-Git @("push", "-u", "origin", $Branch, "--force-with-lease")

        $body = "Automated academy release $Version prepared by the ITA GitHub App publisher."
        New-GitHubPullRequest -Token $Token -Owner $Owner -Repo $Repo -Head $Branch -Base "main" -Title "Release $Version" -Body $body
    } else {
        Write-Host "Pushing main and tag..."
        Invoke-Git @("tag", "-f", $Version)
        Invoke-Git @("push", "origin", "main")
        Invoke-Git @("push", "origin", $Version, "--force")
    }

    Invoke-Git @("remote", "set-url", "origin", $CleanRemote)

    Write-Host ""
    Write-Host "Publish completed successfully."
    Write-Host "Repository: https://github.com/$FullName"
    Write-Host "Version: $Version"
    if ($Mode -eq "pull-request") {
        Write-Host "Branch: $Branch"
    }
}
finally {
    if (Test-Path -LiteralPath $TempRoot) {
        Remove-Item -LiteralPath $TempRoot -Recurse -Force
    }
    if (Test-Path -LiteralPath (Join-Path $RepoPath ".git")) {
        Set-Location $RepoPath
        git remote set-url origin $CleanRemote 2>$null | Out-Null
    }
}
