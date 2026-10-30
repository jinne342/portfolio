# routers/violation.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Union, Optional
from database import get_db
from crud import create_violation, get_violations, get_violation, update_violation, delete_violation
from schemas import ViolationCreate, ViolationOut, ViolationBase, ViolationUpdate
from auth import require_role

router = APIRouter()

@router.post("/", response_model=dict)
def add_violation(vio: ViolationCreate, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '教师']))):
    try:
        result = create_violation(db, vio)
        return {
            "code": 200,
            "message": "违规记录创建成功",
            "data": {
                "id": result.violation_id,
                "submission_id": result.submission_id,
                "violation_type": result.violation_type
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建违规记录失败：{str(e)}")

@router.get("/{violation_id}/", response_model=dict)
def get_violation_detail(violation_id: int, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        result = get_violation(db, violation_id)
        if not result:
            raise HTTPException(status_code=404, detail="违规记录不存在")
        return {
            "code": 200,
            "message": "查询违规记录成功",
            "data": {
                "violation_id": result.violation_id,
                "submission_id": result.submission_id,
                "team_id": result.team_id,
                "competition_id": result.competition_id,
                "school_id": result.school_id,
                "violation_type": result.violation_type,
                "violation_detail": result.violation_detail,
                "is_approved": result.is_approved,
                "handle_user_id": result.handle_user_id,
                "handle_time": result.handle_time
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询违规记录失败：{str(e)}")

@router.get("/", response_model=dict)
def list_violations(
    user_id: Optional[int] = Query(None, description="按用户ID过滤"),
    db: Session = Depends(get_db),
    _: str = Depends(require_role(['超级管理员']))
):
    try:
        from crud import get_violations_by_user
        if user_id:
            violations = get_violations_by_user(db, user_id)
        else:
            violations = get_violations(db)
        return {
            "code": 200,
            "message": "获取违规记录成功",
            "data": violations
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询违规记录失败：{str(e)}")

@router.put("/{violation_id}/", response_model=dict)
def update_violation_record(violation_id: int, violation: Union[ViolationBase, ViolationUpdate], db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        result = update_violation(db, violation_id, violation)
        if not result:
            raise HTTPException(status_code=404, detail="违规记录不存在")
        return {
            "code": 200,
            "message": "违规记录更新成功",
            "data": {
                "violation_id": result.violation_id,
                "submission_id": result.submission_id,
                "violation_type": result.violation_type,
                "is_approved": result.is_approved
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新违规记录失败：{str(e)}")

@router.delete("/{violation_id}/", response_model=dict)
def delete_violation_record(violation_id: int, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    try:
        result = delete_violation(db, violation_id)
        if not result:
            raise HTTPException(status_code=404, detail="违规记录不存在")
        return {
            "code": 200,
            "message": "违规记录删除成功",
            "data": None
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除违规记录失败：{str(e)}")
