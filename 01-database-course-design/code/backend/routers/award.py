# routers/award.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from crud import (
    create_award,
    get_award,
    get_awards,
    get_awards_by_team,
    get_awards_by_competition,
    update_award,
    delete_award
)
from schemas import AwardCreate, AwardUpdate, AwardOut

router = APIRouter(tags=["奖项管理"])

# 创建奖项
@router.post("/awards/", response_model=dict)
def add_award(award: AwardCreate, db: Session = Depends(get_db)):
    try:
        result = create_award(db, award)
        return {
            "code": 200,
            "message": "奖项创建成功",
            "data": {
                "award_id": result.award_id,
                "team_id": result.team_id,
                "competition_id": result.competition_id,
                "school_id": result.school_id,
                "award_name": result.award_name,
                "award_rank": result.award_rank
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建奖项失败：{str(e)}")

# 获取奖项列表
@router.get("/awards/", response_model=dict)
def list_awards(
    team_id: Optional[int] = Query(None, description="按队伍ID过滤"),
    competition_id: Optional[int] = Query(None, description="按竞赛ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if team_id:
            awards = get_awards_by_team(db, team_id)
        elif competition_id:
            awards = get_awards_by_competition(db, competition_id)
        else:
            awards = get_awards(db)
        return {
            "code": 200,
            "message": "获取奖项列表成功",
            "data": awards
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询奖项失败：{str(e)}")

# 获取单个奖项详情
@router.get("/awards/{award_id}/", response_model=dict)
def get_award_detail(award_id: int, db: Session = Depends(get_db)):
    try:
        award = get_award(db, award_id)
        if not award:
            raise HTTPException(status_code=404, detail="奖项不存在")
        return {
            "code": 200,
            "message": "获取奖项详情成功",
            "data": {
                "award_id": award.award_id,
                "team_id": award.team_id,
                "competition_id": award.competition_id,
                "school_id": award.school_id,
                "award_name": award.award_name,
                "award_rank": award.award_rank
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取奖项详情失败：{str(e)}")

# 更新奖项信息
@router.put("/awards/{award_id}/", response_model=dict)
def update_award_info(award_id: int, award: AwardUpdate, db: Session = Depends(get_db)):
    try:
        result = update_award(db, award_id, award)
        if not result:
            raise HTTPException(status_code=404, detail="奖项不存在")
        return {
            "code": 200,
            "message": "更新奖项成功",
            "data": {
                "award_id": result.award_id,
                "team_id": result.team_id,
                "competition_id": result.competition_id,
                "school_id": result.school_id,
                "award_name": result.award_name,
                "award_rank": result.award_rank
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新奖项失败：{str(e)}")

# 删除奖项
@router.delete("/awards/{award_id}/", response_model=dict)
def remove_award(award_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_award(db, award_id)
        if not result:
            raise HTTPException(status_code=404, detail="奖项不存在")
        return {
            "code": 200,
            "message": "删除奖项成功",
            "data": {
                "award_id": result.award_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除奖项失败：{str(e)}")
