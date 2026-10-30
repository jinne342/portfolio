# routers/certificate.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from fastapi.responses import FileResponse
from database import get_db
from crud import (
    create_certificate,
    get_certificate,
    get_certificates,
    get_certificates_by_user,
    update_certificate,
    delete_certificate
)
from schemas import CertificateCreate, CertificateUpdate, CertificateOut
from utils.file_handler import file_handler

router = APIRouter(tags=["证书管理"])

# 创建证书
@router.post("", response_model=dict)
def add_certificate(cert: CertificateCreate, db: Session = Depends(get_db)):
    try:
        result = create_certificate(db, cert)
        return {
            "code": 200,
            "message": "证书创建成功",
            "data": {
                "certificate_id": result.certificate_id,
                "user_id": result.user_id,
                "school_id": result.school_id,
                "certificate_name": result.certificate_name,
                "competition_name": result.competition_name,
                "award_level": result.award_level,
                "award_year": result.award_year,
                "certificate_url": result.certificate_url,
                "upload_time": result.upload_time.isoformat() if result.upload_time else None,
                "issue_date": result.issue_date.isoformat() if result.issue_date else None,
                "certificate_no": result.certificate_no
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"创建证书失败：{str(e)}")

# 获取所有证书
@router.get("", response_model=dict)
def list_certificates(
    user_id: Optional[str] = Query(None, description="按用户ID过滤"),
    db: Session = Depends(get_db)
):
    try:
        if user_id:
            certificates = get_certificates_by_user(db, user_id)
        else:
            certificates = get_certificates(db)
        return {
            "code": 200,
            "message": "获取证书列表成功",
            "data": certificates
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询证书失败：{str(e)}")

# 获取单个证书
@router.get("/{certificate_id}/", response_model=dict)
def get_certificate_detail(certificate_id: int, db: Session = Depends(get_db)):
    try:
        certificate = get_certificate(db, certificate_id)
        if not certificate:
            raise HTTPException(status_code=404, detail="证书不存在")
        return {
            "code": 200,
            "message": "获取证书详情成功",
            "data": {
                "certificate_id": certificate.certificate_id,
                "user_id": certificate.user_id,
                "school_id": certificate.school_id,
                "certificate_name": certificate.certificate_name,
                "competition_name": certificate.competition_name,
                "award_level": certificate.award_level,
                "award_year": certificate.award_year,
                "certificate_url": certificate.certificate_url,
                "upload_time": certificate.upload_time.isoformat() if certificate.upload_time else None,
                "issue_date": certificate.issue_date.isoformat() if certificate.issue_date else None,
                "certificate_no": certificate.certificate_no
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取证书详情失败：{str(e)}")

# 更新证书
@router.put("/{certificate_id}/", response_model=dict)
def update_certificate_info(certificate_id: int, cert: CertificateUpdate, db: Session = Depends(get_db)):
    try:
        result = update_certificate(db, certificate_id, cert)
        if not result:
            raise HTTPException(status_code=404, detail="证书不存在")
        return {
            "code": 200,
            "message": "更新证书成功",
            "data": {
                "certificate_id": result.certificate_id,
                "user_id": result.user_id,
                "school_id": result.school_id,
                "certificate_name": result.certificate_name,
                "competition_name": result.competition_name,
                "award_level": result.award_level,
                "award_year": result.award_year,
                "certificate_url": result.certificate_url,
                "upload_time": result.upload_time.isoformat() if result.upload_time else None,
                "issue_date": result.issue_date.isoformat() if result.issue_date else None,
                "certificate_no": result.certificate_no
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"更新证书失败：{str(e)}")

# 删除证书
@router.delete("/{certificate_id}/", response_model=dict)
def remove_certificate(certificate_id: int, db: Session = Depends(get_db)):
    try:
        result = delete_certificate(db, certificate_id)
        if not result:
            raise HTTPException(status_code=404, detail="证书不存在")
        return {
            "code": 200,
            "message": "删除证书成功",
            "data": {
                "certificate_id": result.certificate_id
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"删除证书失败：{str(e)}")

# 下载证书文件
@router.get("/{certificate_id}/download/")
def download_certificate_file(certificate_id: int, db: Session = Depends(get_db)):
    try:
        # 获取证书信息
        certificate = get_certificate(db, certificate_id)
        if not certificate:
            raise HTTPException(status_code=404, detail="证书不存在")
        
        # 获取文件的完整路径
        file_path = file_handler.get_file_path(certificate.certificate_url)
        
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
