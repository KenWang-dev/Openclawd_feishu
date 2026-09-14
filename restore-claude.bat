@echo off
chcp 65001 >nul
echo ============================================
echo  还原设置：删除 CLAUDE_CODE_DISABLE_ARTIFACT
echo  （等官方修复后，用这个脚本复原即可）
echo ============================================
echo.
reg delete "HKCU\Environment" /v CLAUDE_CODE_DISABLE_ARTIFACT /f >nul 2>&1
if %errorlevel%==0 (
    echo [OK] 环境变量已删除，恢复默认状态
) else (
    echo [提示] 该环境变量本来就不存在，无需还原
)
echo.
echo ============================================
echo  完成！关闭所有窗口后重新打开 Claude Code
echo ============================================
pause
