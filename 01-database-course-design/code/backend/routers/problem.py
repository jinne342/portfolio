# routers/problem.py
from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from database import get_db
from crud import (
    create_problem, get_problems, get_problem,
    update_problem, delete_problem, get_problems_by_competition,
    create_team_problem, get_team_problems, get_team_selected_problem
)
from schemas import ProblemCreate, ProblemUpdate
from utils.file_handler import file_handler

router = APIRouter()

@router.post("", response_model=dict)
def add_problem(
    problem_data: ProblemCreate,
    db: Session = Depends(get_db)
):
    try:
        # 从problem_data中获取数据，不处理文件上传（暂时移除文件上传功能）
        problem_data_dict = {
            "title": problem_data.title,
            "description": problem_data.description,
            "competition_id": problem_data.competition_id,
            "file_url": None,  # 暂时不支持文件上传
            "max_teams": problem_data.max_teams
        }
        
        result = create_problem(db, problem_data)
        return {
            "code": 200,
            "message": "题目创建成功",
            "data": {
                "problem_id": result.problem_id,
                "title": result.title,
                "description": result.description,
                "competition_id": result.competition_id,
                "file_url": result.file_url,
                "max_teams": result.max_teams
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建题目失败：{str(e)}")

@router.get("", response_model=dict)
def list_problems(
    competition_id: Optional[int] = Query(None, description="按竞赛ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if competition_id:
            problems = get_problems_by_competition(db, competition_id)
        else:
            problems = get_problems(db)
        return {
            "code": 200,
            "message": "获取题目列表成功",
            "data": problems
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询题目失败：{str(e)}")

@router.get("/{problem_id}", response_model=dict)
def get_problem_by_id(problem_id: int, db: Session = Depends(get_db)):
    try:
        problem = get_problem(db, problem_id)
        if not problem:
            raise HTTPException(status_code=404, detail="题目不存在")
        return {
            "code": 200,
            "message": "查询题目成功",
            "data": problem
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询题目失败：{str(e)}")

@router.put("/{problem_id}", response_model=dict)
def update_problem_by_id(problem_id: int, problem_data: ProblemUpdate, db: Session = Depends(get_db)):
    try:
        updated_problem = update_problem(db, problem_id, problem_data)
        if not updated_problem:
            raise HTTPException(status_code=404, detail="题目不存在")
        return {
            "code": 200,
            "message": "更新题目成功",
            "data": {
                "problem_id": updated_problem.problem_id,
                "title": updated_problem.title,
                "description": updated_problem.description,
                "competition_id": updated_problem.competition_id,
                "file_url": updated_problem.file_url,
                "max_teams": updated_problem.max_teams
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新题目失败：{str(e)}")

@router.delete("/{problem_id}", response_model=dict)
def delete_problem_by_id(problem_id: int, db: Session = Depends(get_db)):
    try:
        deleted_problem = delete_problem(db, problem_id)
        if not deleted_problem:
            raise HTTPException(status_code=404, detail="题目不存在")
        return {
            "code": 200,
            "message": "删除题目成功",
            "data": {
                "problem_id": deleted_problem.problem_id,
                "title": deleted_problem.title
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除题目失败：{str(e)}")

# 下载题目文件
@router.get("/{problem_id}/download/")
def download_problem_file(problem_id: int, db: Session = Depends(get_db)):
    try:
        # 获取题目信息
        problem = get_problem(db, problem_id)
        if not problem:
            raise HTTPException(status_code=404, detail="题目不存在")
        
        if not problem.file_url:
            raise HTTPException(status_code=404, detail="题目没有附加文件")
        
        # 获取文件的完整路径
        file_path = file_handler.get_file_path(problem.file_url)
        
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

# 团队选择题目
@router.post("/{problem_id}/select/", response_model=dict)
def select_problem(problem_id: int, request_data: dict, db: Session = Depends(get_db)):
    try:
        team_id = request_data.get("team_id")
        if not team_id:
            raise HTTPException(status_code=400, detail="缺少团队ID")
        
        result = create_team_problem(db, team_id, problem_id)
        return {
            "code": 200,
            "message": "题目选择成功",
            "data": {
                "team_id": result.team_id,
                "problem_id": result.problem_id,
                "competition_id": result.competition_id,
                "selection_time": result.selection_time
            }
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"题目选择失败：{str(e)}")

