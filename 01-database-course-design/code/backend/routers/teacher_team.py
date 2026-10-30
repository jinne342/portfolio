# routers/teacher_team.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from crud import (
    create_teacher_team,
    get_teacher_teams,
    get_teacher_teams_by_user,
    get_teacher_teams_by_team,
    update_teacher_team,
    delete_teacher_team
)
from schemas import TeacherTeamCreate, TeacherTeamUpdate, TeacherTeamOut
from auth import require_role

router = APIRouter(tags=["指导关联管理"])

# 创建指导关联（教师/竞赛管理员）
@router.post("/teacher-teams/", response_model=dict)
def add_teacher_team(teacher_team: TeacherTeamCreate, db: Session = Depends(get_db), _: str = Depends(require_role(['教师', '竞赛管理员']))):
    try:
        result = create_teacher_team(db, teacher_team)
        return {
            "code": 200,
            "message": "指导关联创建成功",
            "data": {
                "user_id": result.user_id,
                "team_id": result.team_id,
                "assign_method": result.assign_method,
                "confirm_status": result.confirm_status,
                "assign_time": result.assign_time.isoformat() if result.assign_time else None
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建指导关联失败：{str(e)}")

# 学生发送指导老师请求
@router.post("/teacher-teams/request/", response_model=dict)
def student_request_teacher(teacher_team: TeacherTeamCreate, db: Session = Depends(get_db), _: str = Depends(require_role(['学生']))):
    try:
        # 学生请求指导老师时，默认设置confirm_status为0（待处理）
        teacher_team.confirm_status = 0
        teacher_team.assign_method = "request"
        
        result = create_teacher_team(db, teacher_team)
        return {
            "code": 200,
            "message": "指导老师请求已发送",
            "data": {
                "user_id": result.user_id,
                "team_id": result.team_id,
                "assign_method": result.assign_method,
                "confirm_status": result.confirm_status,
                "assign_time": result.assign_time.isoformat() if result.assign_time else None
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"发送指导老师请求失败：{str(e)}")

# 获取指导关联列表
@router.get("/teacher-teams/", response_model=dict)
def list_teacher_teams(
    user_id: Optional[str] = Query(None, description="按教师用户ID过滤"),
    team_id: Optional[int] = Query(None, description="按队伍ID过滤"),
    db: Session = Depends(get_db),
    _: str = Depends(require_role(['教师', '竞赛管理员']))
):
    try:
        if user_id:
            teacher_teams = get_teacher_teams_by_user(db, user_id)
        elif team_id:
            teacher_teams = get_teacher_teams_by_team(db, team_id)
        else:
            teacher_teams = get_teacher_teams(db)
        return {
            "code": 200,
            "message": "获取指导关联列表成功",
            "data": teacher_teams
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询指导关联失败：{str(e)}")

# 更新指导关联信息
@router.put("/teacher-teams/{user_id}/{team_id}/", response_model=dict)
def update_teacher_team_info(
    user_id: str,
    team_id: int,
    teacher_team: TeacherTeamUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(require_role(['教师', '竞赛管理员']))
):
    try:
        result = update_teacher_team(db, user_id, team_id, teacher_team)
        if not result:
            raise HTTPException(status_code=404, detail="指导关联不存在")
        return {
            "code": 200,
            "message": "更新指导关联成功",
            "data": {
                "user_id": result.user_id,
                "team_id": result.team_id,
                "assign_method": result.assign_method,
                "confirm_status": result.confirm_status,
                "assign_time": result.assign_time.isoformat() if result.assign_time else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新指导关联失败：{str(e)}")

# 删除指导关联
@router.delete("/teacher-teams/{user_id}/{team_id}/", response_model=dict)
def remove_teacher_team(
    user_id: str,
    team_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(require_role(['教师', '竞赛管理员']))
):
    try:
        result = delete_teacher_team(db, user_id, team_id)
        if not result:
            raise HTTPException(status_code=404, detail="指导关联不存在")
        return {
            "code": 200,
            "message": "删除指导关联成功",
            "data": {
                "user_id": result.user_id,
                "team_id": result.team_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除指导关联失败：{str(e)}")
