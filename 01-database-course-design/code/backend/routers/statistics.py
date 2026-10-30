from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
from auth import require_role

router = APIRouter(tags=["数据统计"])

@router.get("/user_count")
def api_user_count(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    """获取总用户数量"""
    try:
        total_users = crud.get_user_count(db)
        return {"total_users": total_users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")

@router.get("/team_count")
def api_team_count(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    """获取总队伍数量"""
    try:
        total_teams = crud.get_team_count(db)
        return {"total_teams": total_teams}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")

@router.get("/active_competition_count")
def api_active_competition_count(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    """获取进行中竞赛数量"""
    try:
        active_competitions = crud.get_active_competition_count(db)
        return {"active_competitions": active_competitions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")

@router.get("/pending_registration_count")
def api_pending_registration_count(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员', '竞赛管理员']))):
    """获取待处理报名审核数量"""
    try:
        pending_registrations = crud.get_pending_registration_count(db)
        return {"pending_registrations": pending_registrations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")

@router.get("/team_by_college")
def api_team_by_college(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    """获取各学院队伍数量"""
    try:
        data = crud.get_team_count_by_college(db)
        return [{"college": name, "count": count} for name, count in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")

@router.get("/problem_selection")
def api_problem_selection(db: Session = Depends(get_db), _: str = Depends(require_role(['超级管理员']))):
    """获取各题目被选择次数"""
    try:
        data = crud.get_problem_selection_count(db)
        return [{"problem": title, "count": count} for title, count in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")

@router.get("/teacher")
def api_teacher_statistics(db: Session = Depends(get_db), current_user_id: str = Depends(require_role(['教师']))):
    """获取教师统计数据"""
    try:
        from models import Team, Work
        
        # 获取教师指导的队伍
        teams = db.query(Team).filter(Team.teacher_user_id == current_user_id).all()
        team_count = len(teams)
        
        # 统计已确认指导和待确认指导的队伍
        confirmed_teams = len([t for t in teams if t.status == 1])
        pending_teams = len([t for t in teams if t.status == 0])
        
        # 获取教师评审的作品
        works = db.query(Work).filter(Work.review_user_id == current_user_id).all()
        total_reviews = len(works)
        
        # 统计已完成评审和待评审的作品
        completed_reviews = len([w for w in works if w.is_reviewed == 1])
        pending_reviews = len([w for w in works if w.is_reviewed == 0])
        
        # 计算平均得分
        average_score = 0
        if completed_reviews > 0:
            reviewed_works = [w for w in works if w.is_reviewed == 1]
            total_score = sum(float(w.score) if w.score else 0 for w in reviewed_works)
            average_score = total_score / completed_reviews
        
        # 计算得分分布
        score_distribution = [0, 0, 0, 0, 0]
        for work in works:
            if work.score:
                score = float(work.score)
                if score < 20:
                    score_distribution[0] += 1
                elif score < 40:
                    score_distribution[1] += 1
                elif score < 60:
                    score_distribution[2] += 1
                elif score < 80:
                    score_distribution[3] += 1
                else:
                    score_distribution[4] += 1
        
        return {
            "teamCount": team_count,
            "confirmedTeams": confirmed_teams,
            "pendingTeams": pending_teams,
            "totalReviews": total_reviews,
            "completedReviews": completed_reviews,
            "pendingReviews": pending_reviews,
            "averageScore": average_score,
            "scoreDistribution": score_distribution
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")