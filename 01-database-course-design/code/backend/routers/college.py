# routers/college.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from crud import create_college, get_college, get_colleges, update_college, delete_college
from schemas import CollegeCreate, CollegeUpdate, CollegeOut

router = APIRouter()

@router.post("/colleges/", response_model=dict)
def add_college(college: CollegeCreate, db: Session = Depends(get_db)):
    try:
        result = create_college(db, college, college.school_id)
        return {
            "code": 200,
            "message": "学院创建成功",
            "data": {
                "college_id": result.college_id,
                "college_name": result.college_name,
                "school_id": result.school_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建学院失败：{str(e)}")

@router.get("/colleges/", response_model=List[dict])
def list_colleges(school_id: Optional[int] = Query(None, description="学校ID"), db: Session = Depends(get_db)):
    try:
        colleges = get_colleges(db, school_id)
        return colleges
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询学院失败：{str(e)}")

@router.get("/colleges/{college_id}/", response_model=dict)
def get_college_by_id(college_id: int, db: Session = Depends(get_db)):
    try:
        college = get_college(db, college_id)
        if not college:
            raise HTTPException(status_code=404, detail="学院不存在")
        return {
            "college_id": college.college_id,
            "college_name": college.college_name,
            "school_id": college.school_id
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询学院失败：{str(e)}")

@router.put("/colleges/{college_id}/", response_model=dict)
def update_college_info(college_id: int, college: CollegeUpdate, db: Session = Depends(get_db)):
    try:
        result = update_college(db, college_id, college)
        if not result:
            raise HTTPException(status_code=404, detail="学院不存在")
        return {
            "code": 200,
            "message": "学院更新成功",
            "data": {
                "college_id": result.college_id,
                "college_name": result.college_name,
                "school_id": result.school_id
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新学院失败：{str(e)}")

@router.delete("/colleges/{college_id}/", response_model=dict)
def delete_college_info(college_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_college(db, college_id)
        if not result:
            raise HTTPException(status_code=404, detail="学院不存在")
        return {
            "code": 200,
            "message": "学院删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除学院失败：{str(e)}")
