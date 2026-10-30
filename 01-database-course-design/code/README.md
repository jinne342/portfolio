# 数学建模数据库管理系统

这是一个完整的数学建模竞赛管理平台，包含前端、后端和数据库三个部分。

## 📁 项目结构

```
数据库课设/
├── backend/              # FastAPI 后端服务
│   ├── routers/         # API 路由
│   ├── models.py        # 数据库模型（已匹配SQL结构）
│   ├── schemas.py       # Pydantic 模式
│   ├── crud.py          # CRUD 操作
│   ├── database.py      # 数据库连接（已优化）
│   ├── main.py          # FastAPI 应用入口（已优化）
│   ├── requirements.txt # Python依赖
│   └── start.bat        # 启动脚本
├── frontend/            # Vue 3 前端应用
│   ├── src/            # 源代码
│   ├── vite.config.js  # Vite配置（已优化）
│   ├── package.json    # 依赖配置
│   └── start.bat       # 启动脚本
├── SQL数学建模.sql      # 数据库初始化脚本（中文已修复）
├── 配置说明.md          # 详细配置说明
└── README.md           # 本文件
```

## ⚙️ 环境要求

- **Python**: 3.8+
- **Node.js**: 16+
- **SQL Server**: 2012+ 或 SQL Server Express
- **ODBC Driver**: 17 for SQL Server 或更高版本

## 🚀 快速开始

### 1. 数据库设置

1. 打开 SQL Server Management Studio (SSMS)
2. 执行 `SQL数学建模.sql` 脚本创建数据库和表
3. 确认数据库名称为 `math_modeling_platform`
4. 确认数据库排序规则为 `Chinese_PRC_CI_AS`（脚本已自动设置）

### 2. 后端设置

```bash
# 进入后端目录
cd backend

# 安装 Python 依赖
pip install -r requirements.txt

# 配置数据库连接（可选）
# 编辑 database.py 或创建 .env 文件（参考 .env.example）

# 启动后端服务
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

# 或使用启动脚本（Windows）
start.bat
```

后端服务将在 `http://127.0.0.1:8000` 启动

**验证后端**:
- 健康检查: http://127.0.0.1:8000/health
- API文档: http://127.0.0.1:8000/docs

### 3. 前端设置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 配置API地址（可选）
# 创建 .env 文件，设置 VITE_API_BASE_URL=http://127.0.0.1:8000

# 启动开发服务器
npm run dev

# 或使用启动脚本（Windows）
start.bat
```

前端服务将在 `http://localhost:5173` 启动

## 🔧 配置说明

### 端口配置

- **后端端口**: 默认 `8000`，可通过环境变量 `BACKEND_PORT` 修改
- **前端端口**: 默认 `5173`，可通过环境变量 `PORT` 修改

### 数据库配置

在 `backend/database.py` 中，可以通过环境变量配置数据库连接：

- `DB_SERVER`: SQL Server 服务器和实例名（默认：`localhost\SQLEXPRESS`）
- `DB_NAME`: 数据库名称（默认：`math_modeling_platform`）
- `DB_DRIVER`: ODBC 驱动名称（默认：`ODBC Driver 17 for SQL Server`）
- `USE_TRUSTED_CONNECTION`: 是否使用 Windows 信任连接（默认：`yes`）

### API连接配置

前端通过 `frontend/src/api/index.js` 连接后端，默认地址为 `http://127.0.0.1:8000`。

可以通过创建 `frontend/.env` 文件并设置 `VITE_API_BASE_URL` 来修改。

**详细配置说明请查看 `配置说明.md`**

## 📚 API 文档

启动后端服务后，访问以下地址查看 API 文档：

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## ✨ 主要功能

- ✅ 用户管理（学生、教师、管理员）
- ✅ 学校、学院、专业管理
- ✅ 竞赛管理
- ✅ 队伍管理
- ✅ 题目管理
- ✅ 提交和评审
- ✅ 证书管理
- ✅ 违规记录
- ✅ 消息和公告
- ✅ 数据统计

## 🔍 已修复和优化的内容

### 数据库
- ✅ 修复了 Submission 表的重复字段问题
- ✅ 确保所有中文字段使用 NVARCHAR 类型
- ✅ 设置了正确的排序规则（Chinese_PRC_CI_AS）
- ✅ 添加了编码设置，确保中文正确显示

### 后端
- ✅ 修复了 models.py，完全匹配数据库结构
- ✅ 添加了 School 模型
- ✅ 修复了所有外键关系
- ✅ 优化了数据库连接配置（连接池、超时等）
- ✅ 添加了全局异常处理
- ✅ 优化了端口配置（支持环境变量）
- ✅ 添加了健康检查接口

### 前端
- ✅ 优化了 API 连接配置（支持环境变量）
- ✅ 优化了错误处理
- ✅ 优化了 Vite 配置（代理、构建等）
- ✅ 添加了请求/响应拦截器

### 配置
- ✅ 创建了环境变量示例文件
- ✅ 创建了启动脚本
- ✅ 创建了详细的配置说明文档

## 🐛 常见问题

### 1. 数据库连接失败

**解决方法**:
- 确认 SQL Server 服务正在运行
- 检查 ODBC 驱动是否已安装
- 验证数据库名称和服务器名称是否正确
- 如果使用 Windows 信任连接，确认当前用户有数据库访问权限

### 2. 前端无法连接后端

**解决方法**:
- 确认后端服务已启动（访问 http://127.0.0.1:8000/health）
- 检查 `frontend/src/api/index.js` 中的 baseURL 配置
- 确认 CORS 配置正确（后端已配置常见端口）
- 检查浏览器控制台的错误信息

### 3. 端口冲突

**解决方法**:
- 后端：修改 `backend/main.py` 中的 `BACKEND_PORT` 或设置环境变量
- 前端：修改 `frontend/vite.config.js` 中的 `port` 或设置环境变量 `PORT`

### 4. 中文显示乱码

**解决方法**:
- 在 SSMS 中打开 SQL 文件时，选择 "使用编码打开"，选择 UTF-8 with BOM
- 确认数据库排序规则为 `Chinese_PRC_CI_AS`
- 查看 `SQL文件中文显示说明.md` 获取详细说明

## 📝 技术栈

- **后端**: FastAPI, SQLAlchemy, PyODBC
- **前端**: Vue 3, Vue Router, Pinia, Axios, ECharts
- **数据库**: SQL Server
- **构建工具**: Vite

## 📄 许可证

本项目仅用于学习和教育目的。

## 📞 技术支持

如果遇到问题，请：
1. 查看 `配置说明.md` 获取详细配置信息
2. 查看 `SQL文件中文显示说明.md` 解决中文显示问题
3. 检查所有配置文件是否正确
4. 查看后端和前端控制台的错误信息
