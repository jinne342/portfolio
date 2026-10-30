# routers/team_invite.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from crud import (
    create_team_invite,
    get_team_invites_by_user,
    update_invite_status,
    get_team_invites_by_team
)
from schemas import TeamInviteCreate, TeamInviteUpdate, TeamInviteOut
from auth import get_current_user
from models import User

router = APIRouter(tags=["队伍邀请管理"])

# =================== 创建队伍邀请 ===================
@router.post("/", response_model=dict)
async def send_team_invite(invite: TeamInviteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        # 使用当前登录用户的ID作为from_user_id
        from_user_id = current_user.user_id
        result = create_team_invite(db, invite.team_id, from_user_id, invite.to_user_id)
        return {
            "code": 200,
            "message": "发送邀请成功",
            "data": {
                "invite_id": result.invite_id,
                "team_id": result.team_id,
                "from_user_id": result.from_user_id,
                "to_user_id": result.to_user_id,
                "status": result.status,
                "create_time": result.create_time.isoformat() if result.create_time else None
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"发送邀请失败：{str(e)}")

# =================== 获取用户的邀请列表 ===================
@router.get("/user/", response_model=dict)
async def get_user_invites(
    status: Optional[int] = Query(None, description="邀请状态：0-待处理，1-已接受，2-已拒绝"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        # 使用当前登录用户的ID
        user_id = current_user.user_id
        invites = get_team_invites_by_user(db, user_id, status)
        return {
            "code": 200,
            "message": "获取邀请列表成功",
            "data": invites
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取邀请列表失败：{str(e)}")

# =================== 更新邀请状态 ===================
@router.put("/{invite_id}/", response_model=dict)
async def handle_team_invite(
    invite_id: int,
    update: TeamInviteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        # 使用当前登录用户的ID
        user_id = current_user.user_id
        result = update_invite_status(db, invite_id, update.status, user_id)
        return {
            "code": 200,
            "message": "处理邀请成功",
            "data": {
                "invite_id": result.invite_id,
                "status": result.status,
                "status_text": "待处理" if result.status == 0 else "已接受" if result.status == 1 else "已拒绝"
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"处理邀请失败：{str(e)}")

# =================== 获取队伍的邀请列表 ===================
@router.get("/team/{team_id}/", response_model=dict)
async def get_team_invites(team_id: int, db: Session = Depends(get_db)):
    try:
        invites = get_team_invites_by_team(db, team_id)
        return {
            "code": 200,
            "message": "获取队伍邀请列表成功",
            "data": invites
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取队伍邀请列表失败：{str(e)}")
