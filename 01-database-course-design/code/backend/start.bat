@echo off
chcp 65001 >nul
echo ============================================
echo 数学建模平台 - 后端服务启动脚本
echo ============================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

echo [信息] 检测到Python环境
python --version

echo.
echo [信息] 检查依赖包...
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo [警告] 未检测到依赖包，正在安装...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [错误] 依赖包安装失败
        pause
        exit /b 1
    )
)

echo.
echo [信息] 启动后端服务...
echo [信息] 服务地址: http://127.0.0.1:8000
echo [信息] API文档: http://127.0.0.1:8000/docs
echo [信息] 健康检查: http://127.0.0.1:8000/health
echo.
echo 按 Ctrl+C 停止服务
echo.

REM 启动服务
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

pause
