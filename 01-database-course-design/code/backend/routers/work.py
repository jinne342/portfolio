# routers/work.py
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from database import get_db
from crud import (
    create_work,
    get_work,
    get_works,
    get_works_by_team,
    get_works_by_problem,
    get_works_by_user,
    update_work,
    delete_work,
    review_work
)
from schemas import WorkCreate, WorkUpdate
from utils.file_handler import file_handler
from auth import require_role

router = APIRouter(tags=["作品管理"])

# 创建作品 - 支持文件上传
@router.post("/", response_model=dict)
def add_work(
    team_id: int,
    problem_id: int,
    file: UploadFile = File(...),
    teacher_user_id: Optional[str] = Query(None, description="指导教师用户ID"),
    db: Session = Depends(get_db)
):
    try:
        # 保存文件到本地存储
        file_path = file_handler.save_file(file, "work")
        
        # 创建作品记录
        work_data = WorkCreate(
            team_id=team_id,
            problem_id=problem_id,
            teacher_user_id=teacher_user_id,
            file_url=file_path,
            version=1,
            score=None,
            review_user_id=None,
            review_comment=None,
            is_reviewed=0
        )
        
        result = create_work(db, work_data)
        
        return {
            "code": 200,
            "message": "作品提交成功",
            "data": {
                "work_id": result.work_id,
                "team_id": result.team_id,
                "problem_id": result.problem_id,
                "competition_id": result.competition_id,
                "teacher_user_id": result.teacher_user_id,
                "file_url": result.file_url,
                "version": result.version,
                "score": result.score,
                "submit_time": result.submit_time.isoformat() if result.submit_time else None,
                "review_user_id": result.review_user_id,
                "review_comment": result.review_comment,
                "review_time": result.review_time.isoformat() if result.review_time else None,
                "is_reviewed": result.is_reviewed == 1
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"作品提交失败：{str(e)}")

# 获取所有作品
@router.get("/", response_model=dict)
def list_works(
    user_id: Optional[str] = Query(None, description="按用户ID过滤"),
    team_id: Optional[int] = Query(None, description="按队伍ID过滤"),
    problem_id: Optional[int] = Query(None, description="按题目ID过滤"),
    reviewed: Optional[bool] = Query(None, description="按是否已评审过滤"),
    db: Session = Depends(get_db)
):
    try:
        from models import Teacher_Team
        
        if user_id:
            # 检查该用户是否是教师（通过Teacher_Team表）
            teacher_teams = db.query(Teacher_Team).filter(Teacher_Team.user_id == user_id).all()
            
            if teacher_teams:
                # 是教师：获取该教师关联的所有队伍ID
                team_ids = [tt.team_id for tt in teacher_teams]
                # 使用get_works函数过滤这些队伍的作品
                works = get_works(db, team_id__in=team_ids, problem_id=problem_id, reviewed=reviewed)
            else:
                # 不是教师（是学生）：获取该用户所在团队的所有作品
                works = get_works_by_user(db, user_id)
                
                # 如果同时提供了team_id或problem_id，进行进一步过滤
                if team_id:
                    works = [w for w in works if w['team_id'] == team_id]
                if problem_id:
                    works = [w for w in works if w['problem_id'] == problem_id]
                if reviewed is not None:
                    if reviewed:
                        works = [w for w in works if w['is_reviewed']]
                    else:
                        works = [w for w in works if not w['is_reviewed']]
        else:
            # 原来的查询逻辑
            works = get_works(db, team_id=team_id, problem_id=problem_id, reviewed=reviewed)
            
        return {
            "code": 200,
            "message": "获取作品列表成功",
            "data": works
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询作品失败：{str(e)}")

# 获取单个作品详情
@router.get("/{work_id}/", response_model=dict)
def get_work_detail(work_id: int, db: Session = Depends(get_db)):
    try:
        work = get_work(db, work_id)
        if not work:
            raise HTTPException(status_code=404, detail="作品不存在")
        return {
            "code": 200,
            "message": "获取作品详情成功",
            "data": work
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取作品详情失败：{str(e)}")

# 更新作品信息
@router.put("/{work_id}/", response_model=dict)
def update_work_info(work_id: int, work: WorkUpdate, db: Session = Depends(get_db)):
    try:
        result = update_work(db, work_id, work)
        if not result:
            raise HTTPException(status_code=404, detail="作品不存在")
        return {
            "code": 200,
            "message": "更新作品成功",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新作品失败：{str(e)}")

# 删除作品
@router.delete("/{work_id}/", response_model=dict)
def remove_work(work_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_work(db, work_id)
        if not result:
            raise HTTPException(status_code=404, detail="作品不存在")
        return {
            "code": 200,
            "message": "删除作品成功",
            "data": {
                "work_id": result.work_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除作品失败：{str(e)}")

# 评审作品
@router.post("/{work_id}/review/", response_model=dict)
def review_work_detail(
    work_id: int,
    review_user_id: str,
    score: float,
    comment: str,
    db: Session = Depends(get_db),
    _: str = Depends(require_role(['教师']))
):
    try:
        result = review_work(db, work_id, review_user_id, score, comment)
        return {
            "code": 200,
            "message": "评审成功",
            "data": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"评审失败：{str(e)}")

# 下载作品文件
@router.get("/{work_id}/download/")
def download_work_file(work_id: int, db: Session = Depends(get_db)):
    try:
        # 获取作品信息
        work = get_work(db, work_id)
        if not work:
            raise HTTPException(status_code=404, detail="作品不存在")
        
        # 获取文件的完整路径
        file_path = file_handler.get_file_path(work['file_url'])
        
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="文件不存在")
        
        # 提取文件名
        file_name = os.path.basename(file_path)
        
        # 返回文件下载响应
        return FileResponse(
            path=file_path,
            filename=file_name,
            media_type='application/octet-stream'
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"文件下载失败：{str(e)}")
