@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0PUBLISH_ITA_WITH_GITHUB_APP.ps1" -Mode direct
echo.
pause

