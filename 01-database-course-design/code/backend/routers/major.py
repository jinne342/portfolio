# routers/major.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from crud import create_major, get_major, get_majors, update_major, delete_major
from schemas import MajorCreate, MajorUpdate, MajorOut

router = APIRouter()

@router.post("/majors/", response_model=dict)
def add_major(major: MajorCreate, db: Session = Depends(get_db)):
    try:
        result = create_major(db, major)
        return {
            "code": 200,
            "message": "专业创建成功",
            "data": {
                "major_id": result.major_id,
                "major_name": result.major_name,
                "college_id": result.college_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建专业失败：{str(e)}")

@router.get("/majors/", response_model=List[dict])
def list_majors(college_id: Optional[int] = Query(None, description="学院ID"), db: Session = Depends(get_db)):
    try:
        majors = get_majors(db, college_id)
        return majors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询专业失败：{str(e)}")

@router.get("/majors/{major_id}/", response_model=dict)
def get_major_by_id(major_id: int, db: Session = Depends(get_db)):
    try:
        major = get_major(db, major_id)
        if not major:
            raise HTTPException(status_code=404, detail="专业不存在")
        return {
            "major_id": major.major_id,
            "major_name": major.major_name,
            "college_id": major.college_id
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询专业失败：{str(e)}")

@router.put("/majors/{major_id}/", response_model=dict)
def update_major_info(major_id: int, major: MajorUpdate, db: Session = Depends(get_db)):
    try:
        result = update_major(db, major_id, major)
        if not result:
            raise HTTPException(status_code=404, detail="专业不存在")
        return {
            "code": 200,
            "message": "专业更新成功",
            "data": {
                "major_id": result.major_id,
                "major_name": result.major_name,
                "college_id": result.college_id
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新专业失败：{str(e)}")

@router.delete("/majors/{major_id}/", response_model=dict)
def delete_major_info(major_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_major(db, major_id)
        if not result:
            raise HTTPException(status_code=404, detail="专业不存在")
        return {
            "code": 200,
            "message": "专业删除成功"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除专业失败：{str(e)}")
