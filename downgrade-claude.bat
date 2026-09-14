@echo off
echo ============================================
echo  Downgrade Claude Code to 2.1.263 (stable)
echo ============================================
echo.
call npm install -g @anthropic-ai/claude-code@2.1.263
echo.
echo ============================================
echo  Verify version:
call claude --version
echo.
echo  Done! Close ALL windows, open a new one,
echo  then start Claude Code and test again.
echo ============================================
pause
