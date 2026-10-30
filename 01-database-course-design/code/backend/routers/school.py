# routers/school.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from crud import (
    create_school, get_school, get_schools,
    update_school, delete_school
)
from schemas import SchoolCreate, SchoolUpdate, SchoolOut

router = APIRouter()

@router.post("/schools/", response_model=dict)
def add_school(school: SchoolCreate, db: Session = Depends(get_db)):
    try:
        result = create_school(db, school)
        return {
            "code": 200,
            "message": "学校创建成功",
            "data": {
                "school_id": result.school_id,
                "school_code": result.school_code,
                "school_name": result.school_name,
                "status": result.status
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建学校失败：{str(e)}")

@router.get("/schools/", response_model=List[dict])
def list_schools(db: Session = Depends(get_db)):
    try:
        schools = get_schools(db)
        return schools
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询学校失败：{str(e)}")

@router.get("/schools/{school_id}/", response_model=dict)
def get_school_by_id(school_id: int, db: Session = Depends(get_db)):
    try:
        school = get_school(db, school_id)
        if not school:
            raise HTTPException(status_code=404, detail="学校不存在")
        return {
            "school_id": school.school_id,
            "school_code": school.school_code,
            "school_name": school.school_name,
            "status": school.status,
            "create_time": school.create_time
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询学校失败：{str(e)}")

@router.put("/schools/{school_id}/", response_model=dict)
def update_school_info(school_id: int, school: SchoolUpdate, db: Session = Depends(get_db)):
    try:
        result = update_school(db, school_id, school)
        if not result:
            raise HTTPException(status_code=404, detail="学校不存在")
        return {
            "code": 200,
            "message": "学校更新成功",
            "data": {
                "school_id": result.school_id,
                "school_code": result.school_code,
                "school_name": result.school_name,
                "status": result.status
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新学校失败：{str(e)}")

@router.delete("/schools/{school_id}/", response_model=dict)
def delete_school_info(school_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_school(db, school_id)
        if not result:
            raise HTTPException(status_code=404, detail="学校不存在")
        return {
            "code": 200,
            "message": "学校删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除学校失败：{str(e)}")
