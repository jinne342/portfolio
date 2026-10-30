# backend/auth.py
from fastapi import Depends, HTTPException, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from models import User, User_Role, Role
from typing import Optional, Dict
import uuid
from datetime import datetime, timedelta
import hashlib

# 会话存储（内存）
# 实际生产环境中应该使用Redis或其他持久化存储
active_sessions: Dict[str, Dict] = {}

# 移除会话超时机制
# SESSION_TIMEOUT = 86400  # 已注释掉，不再使用会话超时

security = HTTPBearer(auto_error=False)

def is_session_valid(session_id: str) -> bool:
    """检查会话是否有效（仅检查会话是否存在，不再检查超时）"""
    if session_id not in active_sessions:
        return False
    
    # 不再更新最后活动时间，因为会话不再有超时机制
    return True

def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
) -> User:
    """获取当前登录用户"""
    # 从Bearer token或Header中获取token
    token = None
    if credentials:
        token = credentials.credentials
    elif authorization and authorization.startswith('Bearer '):
        token = authorization.replace('Bearer ', '')
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="未提供认证token"
        )
    
    # 验证会话是否有效
    if not is_session_valid(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="会话无效，请重新登录"
        )
    
    try:
        # 从会话中获取用户ID
        session = active_sessions[token]
        user_id = session['user_id']
        
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            # 用户不存在，删除无效会话
            del active_sessions[token]
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="用户不存在"
            )
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="认证失败"
        )

def get_user_roles(user: User = Depends(get_current_user), db: Session = Depends(get_db)) -> list:
    """获取用户角色列表"""
    user_roles = db.query(User_Role).filter(User_Role.user_id == user.user_id).all()
    role_ids = [ur.role_id for ur in user_roles]
    roles = db.query(Role).filter(Role.role_id.in_(role_ids)).all()
    return [role.role_name for role in roles]

def require_role(allowed_roles: list):
    """角色权限装饰器"""
    def role_checker(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
        user_roles = get_user_roles(user, db)
        # 检查用户是否有允许的角色
        if not any(role in allowed_roles for role in user_roles):
            # 也检查user_type（兼容旧系统）
            # 更新为正确的角色映射（根据数据库表结构）
            user_type_map = {1: '学生', 2: '教师', 3: '竞赛管理员', 0: '超级管理员'}
            user_role_name = user_type_map.get(user.user_type, '')
            if user_role_name not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"需要以下角色之一: {', '.join(allowed_roles)}"
                )
        return user
    return role_checker

def login_user(username: str, password: str, db: Session) -> Optional[dict]:
    """用户登录（实现单点登录功能）"""
    # 查询用户（支持用户名和学号登录）
    user = db.query(User).filter(
        (User.user_name == username) | (User.user_id == username)
    ).first()
    
    if not user:
        return None
    
    # 计算密码的MD5哈希值（数据库存储的是MD5）
    password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    
    # 比较密码：支持MD5哈希和明文（用于测试）
    # 数据库中的密码是MD5哈希值：e10adc3949ba59abbe56e057f20f883e (123456的MD5)
    password_match = (
        user.password.lower() == password_md5.lower() or  # MD5哈希匹配（主要方式，忽略大小写）
        user.password == password or      # 明文匹配（如果数据库存储的是明文）
        password == "testuser123" and user.user_name == "testuser123"  # 测试专用
    )
    
    if password_match:
        # 1. 创建新会话
        session_id = str(uuid.uuid4())
        
        # 2. 清理内存中该用户的旧会话（确保单点登录）
        for sid, session_data in list(active_sessions.items()):
            if session_data['user_id'] == user.user_id:
                del active_sessions[sid]
                break
        
        # 3. 调用数据库存储过程实现单点登录
        try:
            db.execute(
                text("EXEC sp_user_login @user_id = :user_id, @session_id = :session_id, @ip_address = :ip_address, @user_agent = :user_agent"),
                {
                    'user_id': user.user_id,
                    'session_id': session_id,
                    'ip_address': '',  # 可以从请求中获取IP地址
                    'user_agent': ''   # 可以从请求中获取用户代理
                }
            )
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"登录失败：{str(e)}"
            )
        
        # 4. 在内存中保存会话信息（用于快速检查）
        active_sessions[session_id] = {
            'user_id': user.user_id,
            'ip_address': '',
            'user_agent': ''
        }
        
        # 5. 返回用户信息和会话ID（作为token）
        # 更新为正确的角色映射（根据数据库表结构）
        user_type_map = {1: '学生', 2: '教师', 3: '竞赛管理员', 0: '超级管理员'}
        return {
            "user_id": user.user_id,
            "username": user.user_name,
            "role": user_type_map.get(user.user_type, '学生'),
            "user_type": user.user_type,
            "school_id": user.school_id,
            "token": session_id  # 使用UUID作为token
        }
    return None

def logout_user(user_id: str, session_id: str = None, db: Session = None) -> bool:
    """用户登出（实现会话管理功能）"""
    # 1. 从会话存储中删除指定会话
    if session_id and session_id in active_sessions:
        del active_sessions[session_id]
    else:
        # 如果没有指定会话ID，删除用户的所有会话
        for sid, session_data in list(active_sessions.items()):
            if session_data['user_id'] == user_id:
                del active_sessions[sid]
                break
    
    # 2. 如果提供了数据库会话，调用存储过程更新用户状态
    if db:
        try:
            db.execute(
                text("EXEC sp_user_logout @user_id = :user_id"),
                {'user_id': user_id}
            )
            db.commit()
        except Exception as e:
            db.rollback()
            # 非关键错误，不影响登出流程，但记录错误
            print(f"登出数据库操作失败：{str(e)}")
    
    return True

# def clean_expired_sessions():
#     """定期清理过期会话（可以在后台任务中调用）"""
#     current_time = datetime.now()
#     expired_sessions = []
#     
#     for session_id, session_data in active_sessions.items():
#         if current_time - session_data['last_activity'] > timedelta(seconds=SESSION_TIMEOUT):
#             expired_sessions.append(session_id)
#     
#     for session_id in expired_sessions:
#         del active_sessions[session_id]

