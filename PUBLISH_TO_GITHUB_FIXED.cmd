@echo off
setlocal
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0PUBLISH_TO_GITHUB_FIXED.ps1"
echo.
pause
