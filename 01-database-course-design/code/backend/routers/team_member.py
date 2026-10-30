# routers/team_member.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from crud import (
    create_team_member,
    get_team_members,
    get_team_members_by_team,
    get_team_members_by_user,
    delete_team_member
)
from schemas import TeamMemberCreate, TeamMemberOut

router = APIRouter(tags=["队员管理"])

# =================== 创建队伍成员 ===================
@router.post("/", response_model=dict)
def add_team_member(member: TeamMemberCreate, db: Session = Depends(get_db)):
    try:
        result = create_team_member(db, member)
        return {
            "code": 200,
            "message": "添加队员成功",
            "data": {
                "team_id": result.team_id,
                "user_id": result.user_id,
                "join_time": result.join_time.isoformat() if result.join_time else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"添加队员失败：{str(e)}")

# =================== 获取所有队伍成员 ===================
@router.get("/", response_model=dict)
def list_team_members(db: Session = Depends(get_db)):
    try:
        members = get_team_members(db)
        return {
            "code": 200,
            "message": "获取所有队员成功",
            "data": members
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取队员失败：{str(e)}")

# =================== 根据队伍ID获取队员 ===================
@router.get("/team/{team_id}/", response_model=dict)
def list_team_members_by_team(team_id: int, db: Session = Depends(get_db)):
    try:
        members = get_team_members_by_team(db, team_id)
        return {
            "code": 200,
            "message": f"获取队伍{team_id}的队员成功",
            "data": members
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取队员失败：{str(e)}")

# =================== 根据用户ID获取队员 ===================
@router.get("/user/{user_id}/", response_model=dict)
def list_team_members_by_user(user_id: int, db: Session = Depends(get_db)):
    try:
        members = get_team_members_by_user(db, user_id)
        return {
            "code": 200,
            "message": f"获取用户{user_id}的队伍成员信息成功",
            "data": members
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取队员失败：{str(e)}")

# =================== 删除队员 ===================
@router.delete("/", response_model=dict)
def remove_team_member(
    team_id: int = Query(..., description="队伍ID"),
    user_id: int = Query(..., description="用户ID"),
    db: Session = Depends(get_db)
):
    try:
        result = delete_team_member(db, team_id, user_id)
        if not result:
            raise HTTPException(status_code=404, detail="队员不存在")
        return {
            "code": 200,
            "message": "删除队员成功",
            "data": {
                "team_id": result.team_id,
                "user_id": result.user_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除队员失败：{str(e)}")
