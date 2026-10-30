# routers/permission.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from crud import (
    create_permission, get_permission, get_permissions,
    update_permission, delete_permission,
    create_role_permission, get_role_permissions, get_role_permissions_by_role, get_role_permissions_by_permission,
    delete_role_permission
)
from schemas import PermissionCreate, PermissionUpdate, PermissionOut, RolePermissionCreate, RolePermissionOut

router = APIRouter()

@router.post("/permissions/", response_model=dict)
def add_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    try:
        result = create_permission(db, permission)
        return {
            "code": 200,
            "message": "权限创建成功",
            "data": {
                "perm_id": result.perm_id,
                "perm_name": result.perm_name,
                "description": result.description
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建权限失败：{str(e)}")

@router.get("/permissions/", response_model=List[dict])
def list_permissions(
    perm_id: Optional[int] = Query(None, description="按权限ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if perm_id:
            permission = get_permission(db, perm_id)
            if not permission:
                return []
            return [{
                "perm_id": permission.perm_id,
                "perm_name": permission.perm_name,
                "description": permission.description
            }]
        else:
            return get_permissions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询权限失败：{str(e)}")

@router.get("/permissions/{perm_id}/", response_model=dict)
def get_permission_by_id(perm_id: int, db: Session = Depends(get_db)):
    try:
        permission = get_permission(db, perm_id)
        if not permission:
            raise HTTPException(status_code=404, detail="权限不存在")
        return {
            "perm_id": permission.perm_id,
            "perm_name": permission.perm_name,
            "description": permission.description
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询权限失败：{str(e)}")

@router.put("/permissions/{perm_id}/", response_model=dict)
def update_permission_info(perm_id: int, permission: PermissionUpdate, db: Session = Depends(get_db)):
    try:
        result = update_permission(db, perm_id, permission)
        if not result:
            raise HTTPException(status_code=404, detail="权限不存在")
        return {
            "code": 200,
            "message": "权限更新成功",
            "data": {
                "perm_id": result.perm_id,
                "perm_name": result.perm_name,
                "description": result.description
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新权限失败：{str(e)}")

@router.delete("/permissions/{perm_id}/", response_model=dict)
def delete_permission_info(perm_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_permission(db, perm_id)
        if not result:
            raise HTTPException(status_code=404, detail="权限不存在")
        return {
            "code": 200,
            "message": "权限删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除权限失败：{str(e)}")

# =================== Role Permission ===================
@router.post("/role-permissions/", response_model=dict)
def add_role_permission(role_permission: RolePermissionCreate, db: Session = Depends(get_db)):
    try:
        result = create_role_permission(db, role_permission)
        return {
            "code": 200,
            "message": "角色权限关联创建成功",
            "data": {
                "role_id": result.role_id,
                "perm_id": result.perm_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建角色权限关联失败：{str(e)}")

@router.get("/role-permissions/", response_model=List[dict])
def list_role_permissions(
    role_id: Optional[int] = Query(None, description="按角色ID过滤"),
    perm_id: Optional[int] = Query(None, description="按权限ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if role_id:
            return get_role_permissions_by_role(db, role_id)
        elif perm_id:
            return get_role_permissions_by_permission(db, perm_id)
        else:
            return get_role_permissions(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询角色权限关联失败：{str(e)}")

@router.delete("/role-permissions/{role_id}/{perm_id}/", response_model=dict)
def remove_role_permission(role_id: int, perm_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_role_permission(db, role_id, perm_id)
        if not result:
            raise HTTPException(status_code=404, detail="角色权限关联不存在")
        return {
            "code": 200,
            "message": "角色权限关联删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除角色权限关联失败：{str(e)}")
