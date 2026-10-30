# 数学建模竞赛平台 · 数据库课程设计

## 背景
为高校数学建模竞赛设计一套完整的业务数据库与管理系统，覆盖**学校、教师、队伍、赛题、报名、作品提交、评审、证书、违规处理**等核心流程。

## 我的工作
- 需求分析与 E-R 建模，设计 20+ 张关系表，完成关系模式与范式检查
- 编写 SQL Server 建库脚本：建表、主外键、约束、索引、视图、存储过程
- 使用 FastAPI + SQLAlchemy 实现后端 API（认证、报名、作品、评审等）
- 使用 Vue 3 + Element Plus + ECharts 实现前端页面与统计图表
- 撰写课程设计报告并完成答辩

## 目录
```
code/backend/   FastAPI 后端（路由、模型、CRUD、认证）
code/frontend/  Vue 3 前端（页面、API 封装、图表）
sql/schema.sql  SQL Server 建库脚本（UTF-8）
slides.pptx     答辩演示文稿
```

## 技术栈
Python · FastAPI · SQLAlchemy · SQL Server · Vue 3 · Element Plus · ECharts · Vite

## 运行
1. 在 SQL Server 中执行 `sql/schema.sql`
2. 后端：`pip install -r code/backend/requirements.txt`，运行 `uvicorn main:app --reload`
3. 前端：`cd code/frontend && npm install && npm run dev`

> 完整课程报告含个人信息，未公开；可联系索取。
