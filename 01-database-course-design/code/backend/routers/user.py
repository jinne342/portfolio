# routers/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from crud import create_user, get_users, get_user, update_user, delete_user
from schemas import UserCreate, UserOut, UserUpdate
from auth import require_role

router = APIRouter(tags=["用户"])

@router.post("", response_model=dict)
def add_user(user: UserCreate, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        result = create_user(db, user)
        return {
            "code": 200,
            "message": "创建用户成功",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建用户失败：{str(e)}")

@router.get("", response_model=dict)
def list_users(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        users = get_users(db)
        return {
            "code": 200,
            "message": "获取用户列表成功",
            "data": users
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取用户列表失败：{str(e)}")

@router.get("/{user_id}/", response_model=dict)
def get_user_detail(user_id: str, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        user = get_user(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="用户不存在")
        return {
            "code": 200,
            "message": "获取用户详情成功",
            "data": user
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取用户详情失败：{str(e)}")

@router.put("/{user_id}/", response_model=dict)
def update_user_info(user_id: str, user: UserUpdate, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        result = update_user(db, user_id, user)
        if not result:
            raise HTTPException(status_code=404, detail="用户不存在")
        return {
            "code": 200,
            "message": "更新用户成功",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新用户失败：{str(e)}")

@router.delete("/{user_id}/", response_model=dict)
def remove_user(user_id: str, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        result = delete_user(db, user_id)
        if not result:
            raise HTTPException(status_code=404, detail="用户不存在")
        return {
            "code": 200,
            "message": "删除用户成功",
            "data": {"user_id": user_id}
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除用户失败：{str(e)}")
