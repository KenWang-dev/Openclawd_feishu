@echo off
chcp 65001 >nul
echo ============================================
echo  修复 Claude Code 接入 GLM 报 400 [1210] 错误
echo  原理：禁用 Artifacts 功能（2.1.265+ 的 bug）
echo ============================================
echo.

setx CLAUDE_CODE_DISABLE_ARTIFACT "1" >nul
if %errorlevel%==0 (
    echo [OK] 环境变量 CLAUDE_CODE_DISABLE_ARTIFACT=1 已永久设置
) else (
    echo [失败] 环境变量设置出错，请以管理员身份重试
    pause
    exit /b 1
)

echo.
echo ============================================
echo  完成！接下来请手动做两步：
echo   1. 关闭所有 PowerShell / CMD / Claude Code 窗口
echo   2. 重新打开一个新窗口，再启动 Claude Code 测试
echo  （环境变量只对新开的窗口生效）
echo ============================================
echo.
echo 如果重启后仍然报 1210，运行同目录下的
echo downgrade-claude.bat 降级回 2.1.264 临时使用
echo.
pause
