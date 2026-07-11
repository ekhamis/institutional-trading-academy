param(
    [string]$Owner = "ekhamis",
    [string]$Repository = "institutional-trading-academy",
    [ValidateSet("private", "public", "internal")]
    [string]$Visibility = "private"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Publisher = Join-Path $ProjectRoot "scripts\publish_to_github.ps1"

if (-not (Test-Path $Publisher)) {
    throw "Publishing script not found at: $Publisher"
}

& powershell -ExecutionPolicy Bypass -File $Publisher `
    -Owner $Owner `
    -Repository $Repository `
    -Visibility $Visibility

exit $LASTEXITCODE
