@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\push_v0.8_candidate.ps1"
set EXITCODE=%ERRORLEVEL%
echo.
if not "%EXITCODE%"=="0" (
  echo ITA v0.8.0 candidate push stopped with exit code %EXITCODE%.
) else (
  echo ITA v0.8.0 candidate push completed.
)
pause
exit /b %EXITCODE%
