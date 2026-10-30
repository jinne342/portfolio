# backend/routers/registration.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import RegistrationCreate, RegistrationUpdate, RegistrationOut
from auth import require_role
from crud import (
    create_registration,
    get_registrations,
    get_registration,
    get_registrations_by_user,
    get_registrations_by_competition,
    update_registration,
    delete_registration
)

router = APIRouter()

# 创建报名
@router.post("/registrations/", response_model=dict)
def add_registration(registration: RegistrationCreate, db: Session = Depends(get_db)):
    try:
        result = create_registration(db, registration)
        return {
            "code": 200,
            "message": "报名成功",
            "data": {
                "id": result.reg_id,
                "user_id": result.user_id,
                "competition_id": result.competition_id,
                "team_id": result.team_id,
                "registration_time": result.registration_time,
                "fee_status": result.fee_status,
                "audit_status": result.audit_status
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建报名失败：{str(e)}")

# 获取所有报名
@router.get("/registrations/", response_model=dict)
def list_registrations(db: Session = Depends(get_db)):
    try:
        registrations = get_registrations(db)
        return {
            "code": 200,
            "message": "获取所有报名成功",
            "data": registrations
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取报名失败：{str(e)}")

# 获取单个报名详情
@router.get("/registrations/{reg_id}/", response_model=dict)
def get_registration_detail(reg_id: int, db: Session = Depends(get_db)):
    try:
        registration = get_registration(db, reg_id)
        if not registration:
            raise HTTPException(status_code=404, detail="报名不存在")
        return {
            "code": 200,
            "message": "获取报名详情成功",
            "data": {
                "id": registration.reg_id,
                "user_id": registration.user_id,
                "competition_id": registration.competition_id,
                "team_id": registration.team_id,
                "registration_time": registration.registration_time,
                "fee_status": registration.fee_status,
                "payment_method": registration.payment_method,
                "payment_time": registration.payment_time,
                "audit_status": registration.audit_status,
                "audit_remark": registration.audit_remark
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取报名详情失败：{str(e)}")

# 获取用户的所有报名
@router.get("/registrations/user/{user_id}/", response_model=dict)
def list_user_registrations(user_id: int, db: Session = Depends(get_db)):
    try:
        registrations = get_registrations_by_user(db, user_id)
        return {
            "code": 200,
            "message": "获取用户报名成功",
            "data": registrations
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取用户报名失败：{str(e)}")

# 获取竞赛的所有报名
@router.get("/registrations/competition/{competition_id}/", response_model=dict)
def list_competition_registrations(competition_id: int, db: Session = Depends(get_db)):
    try:
        registrations = get_registrations_by_competition(db, competition_id)
        return {
            "code": 200,
            "message": "获取竞赛报名成功",
            "data": registrations
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取竞赛报名失败：{str(e)}")

# 更新报名信息（审核接口）
@router.put("/registrations/{reg_id}/", response_model=dict)
def update_registration_info(reg_id: int, registration: RegistrationUpdate, db: Session = Depends(get_db), _: dict = Depends(require_role(['竞赛管理员', '超级管理员']))):
    try:
        result = update_registration(db, reg_id, registration)
        if not result:
            raise HTTPException(status_code=404, detail="报名不存在")
        return {
            "code": 200,
            "message": "更新报名成功",
            "data": {
                "id": result.reg_id,
                "user_id": result.user_id,
                "competition_id": result.competition_id,
                "team_id": result.team_id,
                "registration_time": result.registration_time,
                "fee_status": result.fee_status,
                "payment_method": result.payment_method,
                "payment_time": result.payment_time,
                "audit_status": result.audit_status,
                "audit_remark": result.audit_remark
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新报名失败：{str(e)}")

# 删除报名
@router.delete("/registrations/{reg_id}/", response_model=dict)
def remove_registration(reg_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_registration(db, reg_id)
        if not result:
            raise HTTPException(status_code=404, detail="报名不存在")
        return {
            "code": 200,
            "message": "删除报名成功",
            "data": {
                "id": result.reg_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除报名失败：{str(e)}")
