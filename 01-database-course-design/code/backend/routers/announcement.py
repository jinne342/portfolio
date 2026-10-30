# routers/announcement.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from crud import create_announcement, get_announcements
from schemas import AnnouncementCreate, AnnouncementOut
from datetime import datetime

# 去掉prefix，由main.py统一挂载/api/announcement
router = APIRouter(tags=["公告"])

@router.post("/announcements/", response_model=AnnouncementOut)
def add_announcement(announcement: AnnouncementCreate, db: Session = Depends(get_db)):
    return create_announcement(db, announcement)

@router.get("/announcements/", response_model=List[dict])
def list_announcements(db: Session = Depends(get_db)):
    try:
        # 适配前端字段：create_time → post_time；添加id映射
        announcements = get_announcements(db)
        return [
            {
                "id": ann.get("id", 0),  # 从字典中获取id
                "title": ann.get("title", ""),
                "content": ann.get("content", ""),
                "post_time": ann.get("post_time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            }
            for ann in announcements
        ]
    except Exception as e:
        # 如果get_announcements返回的是模型对象，直接查询数据库
        from models import Announcement
        try:
            announcements = db.query(Announcement).all()
            return [
                {
                    "id": a.announcement_id,
                    "title": a.title,
                    "content": a.content,
                    "post_time": a.create_time.strftime("%Y-%m-%d %H:%M:%S") if a.create_time else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                for a in announcements
            ]
        except Exception as e2:
            raise HTTPException(status_code=500, detail=f"查询公告失败：{str(e2)}")