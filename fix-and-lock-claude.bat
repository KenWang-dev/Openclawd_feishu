@echo off
echo ============================================
echo  Step 1: Disable Claude Code auto-update
echo ============================================
setx DISABLE_AUTOUPDATER 1
if %errorlevel%==0 (
    echo [OK] Auto-update disabled.
) else (
    echo [FAIL] Could not set env var. Try running as Administrator.
)

echo.
echo ============================================
echo  Step 2: Downgrade Claude Code to 2.1.263
echo ============================================
call npm install -g @anthropic-ai/claude-code@2.1.263
echo.

echo ============================================
echo  Step 3: Verify version
echo ============================================
call claude --version
echo.
echo ============================================
echo  ALL DONE!
echo  1. Close ALL windows
echo  2. Open a NEW window, start Claude Code
echo  3. Version must show 2.1.263
echo ============================================
pause
