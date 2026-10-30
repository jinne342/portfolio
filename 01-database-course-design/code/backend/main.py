from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from database import Base, engine
import os
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 导入所有路由
from routers import (
    college, school, major, user, team, team_member, team_invite, problem, work,
    message, announcement, violation, certificate, statistics, auth, competition, registration, award, teacher_team,
    role, permission
)

# 注意：数据库表应该通过执行 SQL数学建模.sql 脚本创建（SQL Server）
# 对于SQLite，这里自动创建表用于演示
import os
DB_TYPE = os.getenv("DB_TYPE", "sqlserver").lower()

if DB_TYPE == "sqlite":
    # SQLite模式下自动创建表
    print("🔧 SQLite模式：自动创建数据库表...")
    Base.metadata.create_all(bind=engine)
    print("✅ 数据库表创建完成")
else:
    print("🔧 SQL Server模式：使用现有数据库表...")
    # SQL Server模式下不自动创建表，避免与现有数据库结构冲突

# 从环境变量读取配置，默认值
# 注意：端口配置优先级：环境变量 > 默认值(8000)
BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8000"))
BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost")

# 验证端口范围
if not (1024 <= BACKEND_PORT <= 65535):
    logger.warning(f"端口 {BACKEND_PORT} 不在有效范围内(1024-65535)，使用默认端口 8000")
    BACKEND_PORT = 8000

app = FastAPI(
    title="数学建模平台后端",
    description="数学建模平台 RESTful API 服务",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 跨域配置（兼容所有前端端口，不报错）
# 支持开发和生产环境
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

# 允许从环境变量添加额外的源
extra_origins = os.getenv("CORS_ORIGINS", "").split(",")
origins.extend([origin.strip() for origin in extra_origins if origin.strip()])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# 全局异常处理
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"未处理的异常: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "code": 500,
            "message": "服务器内部错误",
            "detail": str(exc) if os.getenv("DEBUG", "False").lower() == "true" else "请联系管理员"
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"请求验证失败: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "code": 422,
            "message": "请求参数验证失败",
            "detail": exc.errors()
        }
    )

# 挂载所有路由（路径正确，无冲突）
app.include_router(auth.router, prefix="/api/auth", tags=["认证"])

app.include_router(school.router, prefix="/api/schools", tags=["学校"])
app.include_router(college.router, prefix="/api/colleges", tags=["学院"])
app.include_router(major.router, prefix="/api/majors", tags=["专业"])
app.include_router(user.router, prefix="/api/users", tags=["用户"])
app.include_router(role.router, prefix="/api/roles", tags=["角色"])
app.include_router(permission.router, prefix="/api/permissions", tags=["权限"])
app.include_router(competition.router, prefix="/api/competitions", tags=["竞赛"])
app.include_router(registration.router, prefix="/api", tags=["报名"])
app.include_router(team.router, prefix="/api/teams", tags=["队伍"])
app.include_router(team_member.router, prefix="/api/team-members", tags=["队伍成员"])
app.include_router(team_invite.router, prefix="/api/team_invites", tags=["队伍邀请"])
app.include_router(problem.router, prefix="/api/problems", tags=["题目"])
app.include_router(work.router, prefix="/api/works", tags=["作品"])
app.include_router(message.router, prefix="/api/messages", tags=["消息"])
app.include_router(announcement.router, prefix="/api/announcements", tags=["公告"])
app.include_router(violation.router, prefix="/api/violations", tags=["违规记录"])
app.include_router(certificate.router, prefix="/api/certificates", tags=["证书"])
app.include_router(award.router, prefix="/api/awards", tags=["奖项"])
app.include_router(teacher_team.router, prefix="/api", tags=["指导关联"])
app.include_router(statistics.router, prefix="/api/statistics", tags=["数据统计"])

# 健康检查接口
@app.get("/health")
async def health_check():
    """健康检查接口，用于检查服务是否正常运行"""
    try:
        # 测试数据库连接
        from sqlalchemy import text
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "message": "服务运行正常",
            "database": "connected"
        }
    except Exception as e:
        logger.error(f"数据库连接失败: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "unhealthy",
                "message": "数据库连接失败",
                "database": "disconnected",
                "error": str(e)  # 临时显示完整错误信息
            }
        )

# 修复前端可能请求的archive接口404
@app.get("/api/archive/")
def empty_archive():
    return []

@app.get("/")
def read_root():
    return {
        "message": "数学建模平台后端服务已启动！",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

# 启动信息
if __name__ == "__main__":
    import uvicorn
    logger.info(f"启动后端服务: http://{BACKEND_HOST}:{BACKEND_PORT}")
    uvicorn.run(
        "main:app",
        host=BACKEND_HOST,
        port=BACKEND_PORT,
        reload=True,
        log_level="info"
    )