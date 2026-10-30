# routers/message.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from crud import create_message, get_messages, get_message, get_messages_by_receiver, update_message, delete_message
from schemas import MessageCreate, MessageOut, MessageUpdate

router = APIRouter()

@router.post("", response_model=dict)
def send_message(message: MessageCreate, db: Session = Depends(get_db)):
    try:
        result = create_message(db, message)
        return {
            "code": 200,
            "message": "消息发送成功",
            "data": {
                "id": result.message_id,
                "sender_id": result.sender_id,
                "receiver_id": result.receiver_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"发送消息失败：{str(e)}")

@router.get("", response_model=List[dict])
def list_messages(user_id: Optional[str] = Query(None, description="按用户ID过滤"),
                  is_read: Optional[bool] = Query(None, description="按是否已读过滤"),
                  db: Session = Depends(get_db)):
    try:
        messages = get_messages(db, user_id=user_id, is_read=is_read)
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询消息失败：{str(e)}")

@router.get("/{message_id}/", response_model=dict)
def get_message_detail(message_id: int, db: Session = Depends(get_db)):
    try:
        message = get_message(db, message_id)
        if not message:
            raise HTTPException(status_code=404, detail="消息不存在")
        return {
            "message_id": message.message_id,
            "sender_id": message.sender_id,
            "receiver_id": message.receiver_id,
            "content": message.content,
            "status": message.status,
            "created_at": message.created_at
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询消息失败：{str(e)}")

@router.get("/user/{user_id}/", response_model=List[dict])
def get_user_messages(user_id: str, db: Session = Depends(get_db)):
    try:
        messages = get_messages_by_receiver(db, user_id)
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询用户消息失败：{str(e)}")

@router.put("/{message_id}/", response_model=dict)
def update_message_status(message_id: int, message: MessageUpdate, db: Session = Depends(get_db)):
    try:
        updated_message = update_message(db, message_id, message)
        if not updated_message:
            raise HTTPException(status_code=404, detail="消息不存在")
        return {
            "code": 200,
            "message": "消息状态更新成功",
            "data": {
                "message_id": updated_message.message_id,
                "status": updated_message.status
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新消息状态失败：{str(e)}")

@router.delete("/{message_id}/", response_model=dict)
def delete_message_endpoint(message_id: int, db: Session = Depends(get_db)):
    try:
        deleted_message = delete_message(db, message_id)
        if not deleted_message:
            raise HTTPException(status_code=404, detail="消息不存在")
        return {
            "code": 200,
            "message": "消息删除成功"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除消息失败：{str(e)}")
