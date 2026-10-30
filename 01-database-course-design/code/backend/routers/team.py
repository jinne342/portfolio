# backend/routers/team.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from schemas import TeamCreate, TeamUpdate, TeamOut
from crud import (
    create_team,
    get_team,
    get_teams,
    get_teams_by_user,
    update_team,
    delete_team,
    get_team_selected_problem
)
from auth import require_role

router = APIRouter(tags=["队伍"])  # 移除prefix，由main.py统一配置

# 创建队伍
@router.post("", response_model=dict)
def add_team(team: TeamCreate, db: Session = Depends(get_db)):
    try:
        result = create_team(db, team)
        return {
            "code": 200,
            "message": "创建队伍成功",
            "data": {
                "team_id": result.team_id,
                "team_name": result.team_name,
                "competition_id": result.competition_id,
                "school_id": result.school_id,
                "captain_id": result.captain_id,
                "status": result.status,
                "create_time": result.create_time.isoformat() if result.create_time else None,
                "update_time": result.update_time.isoformat() if result.update_time else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建队伍失败：{str(e)}")

# 获取所有队伍（支持按竞赛ID和用户ID过滤）
@router.get("", response_model=dict)
def list_teams(
    competition_id: Optional[int] = Query(None, description="按竞赛ID过滤"),
    user_id: Optional[str] = Query(None, description="按用户ID过滤，获取该用户所在的队伍"),
    db: Session = Depends(get_db)
):
    try:
        if user_id:
            # 如果提供了用户ID，获取该用户所在的所有队伍
            teams = get_teams_by_user(db, user_id)
            # 可选：进一步按竞赛ID过滤
            if competition_id:
                teams = [team for team in teams if team['competition_id'] == competition_id]
        else:
            # 否则按竞赛ID过滤获取所有队伍
            teams = get_teams(db, competition_id)
        
        return {
            "code": 200,
            "message": "获取队伍成功",
            "data": teams
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询队伍失败：{str(e)}")

# 获取单个队伍
@router.get("/{team_id}", response_model=dict)
def get_team_detail(team_id: int, db: Session = Depends(get_db)):
    try:
        team = get_team(db, team_id)
        if not team:
            raise HTTPException(status_code=404, detail="队伍不存在")
        return {
            "code": 200,
            "message": "获取队伍详情成功",
            "data": {
                "team_id": team.team_id,
                "team_name": team.team_name,
                "competition_id": team.competition_id,
                "school_id": team.school_id,
                "captain_id": team.captain_id,
                "status": team.status,
                "create_time": team.create_time.isoformat() if team.create_time else None,
                "update_time": team.update_time.isoformat() if team.update_time else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取队伍详情失败：{str(e)}")

# 更新队伍信息
@router.put("/{team_id}", response_model=dict)
def update_team_info(team_id: int, team: TeamUpdate, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    try:
        result = update_team(db, team_id, team)
        if not result:
            raise HTTPException(status_code=404, detail="队伍不存在")
        return {
            "code": 200,
            "message": "更新队伍成功",
            "data": {
                "team_id": result.team_id,
                "team_name": result.team_name,
                "competition_id": result.competition_id,
                "school_id": result.school_id,
                "captain_id": result.captain_id,
                "status": result.status,
                "create_time": result.create_time.isoformat() if result.create_time else None,
                "update_time": result.update_time.isoformat() if result.update_time else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新队伍失败：{str(e)}")

# 删除队伍
@router.delete("/{team_id}", response_model=dict)
def remove_team(team_id: int, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    try:
        result = delete_team(db, team_id)
        if not result:
            raise HTTPException(status_code=404, detail="队伍不存在")
        return {
            "code": 200,
            "message": "删除队伍成功",
            "data": {
                "team_id": result.team_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除队伍失败：{str(e)}")

# 获取团队已选择的题目
@router.get("/{team_id}/selected-problem/", response_model=dict)
def get_team_selected_problem_endpoint(team_id: int, db: Session = Depends(get_db)):
    try:
        problem = get_team_selected_problem(db, team_id)
        if not problem:
            return {
                "code": 200,
                "message": "团队尚未选择题目",
                "data": None
            }
        return {
            "code": 200,
            "message": "获取团队已选择题目成功",
            "data": {
                "problem_id": problem.problem_id,
                "title": problem.title,
                "description": problem.description,
                "file_url": problem.file_url
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取团队已选择题目失败：{str(e)}")