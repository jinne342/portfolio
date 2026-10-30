# routers/role.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from crud import (
    create_role, get_role, get_roles,
    update_role, delete_role,
    create_user_role, get_user_roles, get_user_roles_by_user, get_user_roles_by_role,
    delete_user_role
)
from schemas import RoleCreate, RoleUpdate, RoleOut, UserRoleCreate, UserRoleOut

router = APIRouter()

@router.post("/roles/", response_model=dict)
def add_role(role: RoleCreate, db: Session = Depends(get_db)):
    try:
        result = create_role(db, role)
        return {
            "code": 200,
            "message": "角色创建成功",
            "data": {
                "role_id": result.role_id,
                "role_name": result.role_name,
                "description": result.description
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建角色失败：{str(e)}")

@router.get("/roles/", response_model=List[dict])
def list_roles(
    role_id: Optional[int] = Query(None, description="按角色ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if role_id:
            role = get_role(db, role_id)
            if not role:
                return []
            return [{
                "role_id": role.role_id,
                "role_name": role.role_name,
                "description": role.description
            }]
        else:
            return get_roles(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询角色失败：{str(e)}")

@router.get("/roles/{role_id}/", response_model=dict)
def get_role_by_id(role_id: int, db: Session = Depends(get_db)):
    try:
        role = get_role(db, role_id)
        if not role:
            raise HTTPException(status_code=404, detail="角色不存在")
        return {
            "role_id": role.role_id,
            "role_name": role.role_name,
            "description": role.description
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询角色失败：{str(e)}")

@router.put("/roles/{role_id}/", response_model=dict)
def update_role_info(role_id: int, role: RoleUpdate, db: Session = Depends(get_db)):
    try:
        result = update_role(db, role_id, role)
        if not result:
            raise HTTPException(status_code=404, detail="角色不存在")
        return {
            "code": 200,
            "message": "角色更新成功",
            "data": {
                "role_id": result.role_id,
                "role_name": result.role_name,
                "description": result.description
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新角色失败：{str(e)}")

@router.delete("/roles/{role_id}/", response_model=dict)
def delete_role_info(role_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_role(db, role_id)
        if not result:
            raise HTTPException(status_code=404, detail="角色不存在")
        return {
            "code": 200,
            "message": "角色删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除角色失败：{str(e)}")

# =================== User Role ===================
@router.post("/user-roles/", response_model=dict)
def add_user_role(user_role: UserRoleCreate, db: Session = Depends(get_db)):
    try:
        result = create_user_role(db, user_role)
        return {
            "code": 200,
            "message": "用户角色关联创建成功",
            "data": {
                "user_id": result.user_id,
                "role_id": result.role_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建用户角色关联失败：{str(e)}")

@router.get("/user-roles/", response_model=List[dict])
def list_user_roles(
    user_id: Optional[int] = Query(None, description="按用户ID过滤"),
    role_id: Optional[int] = Query(None, description="按角色ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if user_id:
            return get_user_roles_by_user(db, user_id)
        elif role_id:
            return get_user_roles_by_role(db, role_id)
        else:
            return get_user_roles(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询用户角色关联失败：{str(e)}")

@router.delete("/user-roles/{user_id}/{role_id}/", response_model=dict)
def remove_user_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_user_role(db, user_id, role_id)
        if not result:
            raise HTTPException(status_code=404, detail="用户角色关联不存在")
        return {
            "code": 200,
            "message": "用户角色关联删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除用户角色关联失败：{str(e)}")
