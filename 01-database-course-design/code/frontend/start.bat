@echo off
chcp 65001 >nul
echo ============================================
echo 数学建模平台 - 前端服务启动脚本
echo ============================================
echo.

REM 检查Node.js是否安装
node --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Node.js，请先安装Node.js 16+
    pause
    exit /b 1
)

echo [信息] 检测到Node.js环境
node --version
npm --version

echo.
echo [信息] 检查依赖包...
if not exist "node_modules" (
    echo [警告] 未检测到依赖包，正在安装...
    call npm install
    if errorlevel 1 (
        echo [错误] 依赖包安装失败
        pause
        exit /b 1
    )
)

echo.
echo [信息] 启动前端服务...
echo [信息] 服务地址: http://localhost:5173
echo [信息] 请确保后端服务已启动在 http://127.0.0.1:8000
echo.
echo 按 Ctrl+C 停止服务
echo.

REM 启动服务
call npm run dev

pause
