# backend/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import get_db
from auth import login_user, get_current_user, get_user_roles, logout_user
from models import User
from schemas import UserCreate
from crud import create_user
import hashlib
from datetime import datetime
from typing import Optional

security = HTTPBearer(auto_error=False)

router = APIRouter(tags=["认证"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """用户登录（JSON格式）"""
    if not request.username or not request.password:
        raise HTTPException(status_code=400, detail="用户名和密码不能为空")
    
    user_data = login_user(request.username, request.password, db)
    if not user_data:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return {
        "code": 200,
        "message": "登录成功",
        "data": user_data
    }

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    """用户注册"""
    # 检查用户名是否已存在
    existing_user = db.query(User).filter(User.user_name == user.user_name).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    
    # 检查user_id是否已存在
    existing_user_by_id = db.query(User).filter(User.user_id == user.user_id).first()
    
    if existing_user_by_id:
        raise HTTPException(status_code=400, detail="用户ID已被注册")
    
    try:
        # 创建新用户，使用create_user函数
        # 注意：密码需要先进行MD5加密
        user.password = hashlib.md5(user.password.encode('utf-8')).hexdigest()
        new_user = create_user(db, user)
        
        return {
            "code": 200,
            "message": "注册成功",
            "data": {
                "user_id": new_user.user_id,
                "username": new_user.user_name,
                "email": new_user.email,
                "user_type": new_user.user_type
            }
        }
    except Exception as e:
        db.rollback()
        # 处理数据库唯一性约束异常
        error_msg = str(e)
        if "UNIQUE constraint failed" in error_msg or "unique constraint" in error_msg.lower():
            if "email" in error_msg:
                raise HTTPException(status_code=400, detail="邮箱已被注册")
            elif "user_id" in error_msg:
                raise HTTPException(status_code=400, detail="用户ID已被注册")
            else:
                raise HTTPException(status_code=400, detail="数据已存在")
        elif "CHECK constraint" in error_msg:
            raise HTTPException(status_code=400, detail="输入数据不符合约束条件")
        else:
            raise HTTPException(status_code=500, detail=f"注册失败: {str(e)}")

@router.get("/me")
def get_current_user_info(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取当前用户信息"""
    user_type_map = {1: '学生', 2: '教师', 3: '竞赛管理员', 0: '超级管理员'}
    roles = get_user_roles(user, db)
    return {
        "code": 200,
        "message": "获取成功",
        "data": {
            "user_id": user.user_id,
            "username": user.user_name,
            "email": user.email,
            "role": user_type_map.get(user.user_type, '学生'),
            "user_type": user.user_type,
            "roles": roles,
            "school_id": user.school_id
        }
    }

@router.post("/logout")
def logout(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    authorization: Optional[str] = Header(None)
):
    """用户登出"""
    # 获取当前会话ID
    session_id = None
    if credentials:
        session_id = credentials.credentials
    elif authorization and authorization.startswith('Bearer '):
        session_id = authorization.replace('Bearer ', '')
    
    # 执行登出操作
    success = logout_user(user.user_id, session_id, db)
    
    if success:
        return {
            "code": 200,
            "message": "登出成功"
        }
    else:
        raise HTTPException(status_code=500, detail="登出失败")

