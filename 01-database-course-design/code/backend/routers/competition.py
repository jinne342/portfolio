# backend/routers/competition.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import (
    create_competition, get_competitions, get_competition,
    update_competition, delete_competition
)
from schemas import CompetitionCreate, CompetitionUpdate, CompetitionOut
from auth import require_role

router = APIRouter()

# =================== 创建竞赛 ===================
@router.post("", response_model=dict)
def add_competition(competition: CompetitionCreate, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    try:
        result = create_competition(db, competition)
        return {
            "code": 200,
            "message": "竞赛创建成功",
            "data": {
                "competition_id": result.competition_id,
                "competition_name": result.competition_name,
                "session_no": result.session_no,
                "status": result.status
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建竞赛失败：{str(e)}")

# =================== 获取所有竞赛 ===================
@router.get("", response_model=dict)
def list_competitions(db: Session = Depends(get_db)):
    try:
        competitions = get_competitions(db)
        return {
            "code": 200,
            "message": "获取竞赛列表成功",
            "data": competitions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询竞赛失败：{str(e)}")

# =================== 获取单个竞赛 ===================
@router.get("/{competition_id}", response_model=dict)
def get_competition_detail(competition_id: int, db: Session = Depends(get_db)):
    try:
        competition = get_competition(db, competition_id)
        if not competition:
            raise HTTPException(status_code=404, detail="竞赛不存在")
        return {
            "competition_id": competition.competition_id,
            "competition_name": competition.competition_name,
            "session_no": competition.session_no,
            "school_id": competition.school_id,
            "sign_start": competition.sign_start.isoformat() if competition.sign_start else None,
            "sign_end": competition.sign_end.isoformat() if competition.sign_end else None,
            "competition_start": competition.competition_start.isoformat() if competition.competition_start else None,
            "competition_end": competition.competition_end.isoformat() if competition.competition_end else None,
            "fee_amount": float(competition.fee_amount) if competition.fee_amount else 0.0,
            "reward_rule": competition.reward_rule,
            "status": competition.status,
            "create_time": competition.create_time.isoformat() if competition.create_time else None
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询竞赛失败：{str(e)}")

# =================== 更新竞赛 ===================
@router.put("/{competition_id}", response_model=dict)
def update_competition_detail(competition_id: int, competition: CompetitionUpdate, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    try:
        result = update_competition(db, competition_id, competition)
        if not result:
            raise HTTPException(status_code=404, detail="竞赛不存在")
        return {
            "code": 200,
            "message": "竞赛更新成功",
            "data": {
                "competition_id": result.competition_id,
                "competition_name": result.competition_name,
                "session_no": result.session_no,
                "status": result.status
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新竞赛失败：{str(e)}")

# =================== 删除竞赛 ===================
@router.delete("/{competition_id}", response_model=dict)
def delete_competition_detail(competition_id: int, db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    try:
        result = delete_competition(db, competition_id)
        if not result:
            raise HTTPException(status_code=404, detail="竞赛不存在")
        return {
            "code": 200,
            "message": "竞赛删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除竞赛失败：{str(e)}")
