# backend/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ========== 数据库配置（使用SQL Server） ==========
# 检查环境变量决定使用哪种数据库
DB_TYPE = os.getenv("DB_TYPE", "sqlserver").lower()  # 默认使用sqlserver

if DB_TYPE == "sqlite":
    # 使用SQLite进行演示（无需外部依赖）
    DB_PATH = os.getenv("DB_PATH", "math_modeling_platform.db")
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"
    print(f"✅ 使用SQLite数据库: {DB_PATH}")
else:
    # SQL Server配置（使用用户提供的信息）
    DB_SERVER = os.getenv("DB_SERVER", "ZJW2580\\MSSQLSERVER02")
    DB_NAME = os.getenv("DB_NAME", "math_modeling_platform")
    DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    USE_TRUSTED_CONNECTION = os.getenv("USE_TRUSTED_CONNECTION", "yes")
    
    # 构建连接字符串（使用Windows身份验证）
    if USE_TRUSTED_CONNECTION.lower() == "yes":
        SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER.replace(' ', '+')}&trusted_connection=yes&TrustServerCertificate=yes&Encrypt=yes"
    else:
        DB_USER = os.getenv("DB_USER", "sa")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "")
        SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DB_DRIVER.replace(' ', '+')}&TrustServerCertificate=yes&Encrypt=yes"
    print(f"✅ 使用SQL Server数据库: {DB_SERVER}/{DB_NAME}")

# 创建数据库引擎
# echo=False 生产环境关闭SQL日志，开发环境可通过环境变量控制
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

# SQLite配置
if DB_TYPE == "sqlite":
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=DEBUG_MODE,
        connect_args={"check_same_thread": False}  # SQLite多线程支持
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=DEBUG_MODE,          # 开发环境打印SQL日志
        pool_pre_ping=True,        # 自动检测连接有效性
        pool_size=5,              # 连接池大小
        max_overflow=10,          # 最大溢出连接数
        pool_recycle=3600         # 连接回收时间（秒）
    )

# 创建数据库会话工厂
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 基础模型类
if DB_TYPE == "sqlite":
    # SQLite模式使用简化模型
    from models_sqlite import Base
else:
    # SQL Server模式使用完整模型
    from models import Base

# 数据库依赖函数（供路由使用）
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# 验证数据库连接（运行该文件即可测试）
if __name__ == "__main__":
    try:
        with engine.connect():
            print("✅ 数据库连接成功！")
    except Exception as e:
        print(f"❌ 数据库连接失败：{str(e)}")