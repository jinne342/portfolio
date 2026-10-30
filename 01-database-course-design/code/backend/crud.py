# backend/crud.py
from sqlalchemy.orm import Session
from sqlalchemy import func
import datetime as dt
from models import (
    College, School, Major, User, Team, Team_Member, Team_Invite,
    Problem, Work, Message, Announcement,
    Competition, Registration, Award, Teacher_Team, Teacher,
    User_Import_Log, Role, Permission, User_Role, Role_Permission,
    Violation_Record, Certificate_Info, Team_Problem
)
from schemas import (
    CollegeCreate, CollegeUpdate, 
    SchoolCreate, SchoolUpdate, MajorCreate, MajorUpdate, UserCreate, UserUpdate,
    TeamCreate, TeamUpdate, TeamMemberCreate, ProblemCreate, ProblemUpdate,
    WorkCreate, WorkUpdate,
    MessageCreate, MessageUpdate, AnnouncementCreate, AnnouncementUpdate,
    CompetitionCreate, CompetitionUpdate,
    RegistrationCreate, RegistrationUpdate, AwardCreate, AwardUpdate,
    TeacherCreate, TeacherUpdate, TeacherTeamCreate, TeacherTeamUpdate, RoleCreate, RoleUpdate, PermissionCreate, PermissionUpdate,
    UserRoleCreate, RolePermissionCreate, UserImportLogCreate, UserImportLogUpdate,
    ViolationCreate, ViolationBase, ViolationUpdate, CertificateCreate, CertificateUpdate
)
from typing import List, Optional, Union



# =================== School ===================
def create_school(db: Session, school: SchoolCreate):
    db_school = School(
        school_code=school.school_code,
        school_name=school.school_name,
        status=school.status
    )
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def get_schools(db: Session):
    schools = db.query(School).all()
    return schools

def get_school(db: Session, school_id: int):
    return db.query(School).filter(School.school_id == school_id).first()

def get_schools_by_name(db: Session, school_name: str):
    schools = db.query(School).filter(School.school_name.like(f"%{school_name}%")).all()
    return schools

def update_school(db: Session, school_id: int, school: SchoolUpdate):
    db_school = db.query(School).filter(School.school_id == school_id).first()
    if db_school:
        if school.school_code is not None:
            db_school.school_code = school.school_code
        if school.school_name is not None:
            db_school.school_name = school.school_name
        if school.status is not None:
            db_school.status = school.status
        db.commit()
        db.refresh(db_school)
    return db_school

def delete_school(db: Session, school_id: int):
    db_school = db.query(School).filter(School.school_id == school_id).first()
    if db_school:
        db.delete(db_school)
        db.commit()
    return db_school

# =================== College ===================
def create_college(db: Session, college: CollegeCreate):
    db_college = College(
        college_name=college.college_name,
        school_id=college.school_id
    )
    db.add(db_college)
    db.commit()
    db.refresh(db_college)
    return db_college

def get_colleges(db: Session):
    colleges = db.query(College).all()
    return [
        {
            "college_id": c.college_id,
            "college_name": c.college_name,
            "school_id": c.school_id
        }
        for c in colleges
    ]

def get_college(db: Session, college_id: int):
    return db.query(College).filter(College.college_id == college_id).first()

def get_colleges_by_school(db: Session, school_id: int):
    colleges = db.query(College).filter(College.school_id == school_id).all()
    return [
        {
            "college_id": c.college_id,
            "college_name": c.college_name,
            "school_id": c.school_id
        }
        for c in colleges
    ]

def update_college(db: Session, college_id: int, college: CollegeUpdate):
    db_college = db.query(College).filter(College.college_id == college_id).first()
    if db_college:
        if college.college_name is not None:
            db_college.college_name = college.college_name
        if college.school_id is not None:
            db_college.school_id = college.school_id
        db.commit()
        db.refresh(db_college)
    return db_college

def delete_college(db: Session, college_id: int):
    db_college = db.query(College).filter(College.college_id == college_id).first()
    if db_college:
        db.delete(db_college)
        db.commit()
    return db_college

# =================== Major ===================
def create_major(db: Session, major: MajorCreate):
    db_major = Major(
        major_name=major.major_name,
        college_id=major.college_id
    )
    db.add(db_major)
    db.commit()
    db.refresh(db_major)
    return db_major

def get_majors(db: Session):
    majors = db.query(Major).all()
    return [
        {
            "major_id": m.major_id,
            "major_name": m.major_name,
            "college_id": m.college_id
        }
        for m in majors
    ]

def get_major(db: Session, major_id: int):
    return db.query(Major).filter(Major.major_id == major_id).first()

def get_majors_by_college(db: Session, college_id: int):
    majors = db.query(Major).filter(Major.college_id == college_id).all()
    return [
        {
            "major_id": m.major_id,
            "major_name": m.major_name,
            "college_id": m.college_id
        }
        for m in majors
    ]

def update_major(db: Session, major_id: int, major: MajorUpdate):
    db_major = db.query(Major).filter(Major.major_id == major_id).first()
    if db_major:
        if major.major_name is not None:
            db_major.major_name = major.major_name
        if major.college_id is not None:
            db_major.college_id = major.college_id
        db.commit()
        db.refresh(db_major)
    return db_major

def delete_major(db: Session, major_id: int):
    db_major = db.query(Major).filter(Major.major_id == major_id).first()
    if db_major:
        db.delete(db_major)
        db.commit()
    return db_major

# =================== User ===================
def create_user(db: Session, user: UserCreate):
    db_user = User(
        user_id=user.user_id,
        user_name=user.user_name,
        email=user.email,
        password=user.password,
        phone=user.phone,
        school_id=user.school_id,
        college_id=user.college_id,
        major_id=user.major_id,
        grade=user.grade,
        user_type=user.user_type
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    users = db.query(User).all()
    return [
        {
            "user_id": u.user_id,
            "user_name": u.user_name,
            "email": u.email,
            "phone": u.phone,
            "school_id": u.school_id,
            "college_id": u.college_id,
            "major_id": u.major_id,
            "grade": u.grade,
            "user_type": u.user_type,
            "status": u.status,
            "create_time": u.create_time.isoformat() if u.create_time else None,
            "update_time": u.update_time.isoformat() if u.update_time else None
        }
        for u in users
    ]

def get_user(db: Session, user_id: str):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        return {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "email": user.email,
            "phone": user.phone,
            "school_id": user.school_id,
            "college_id": user.college_id,
            "major_id": user.major_id,
            "grade": user.grade,
            "user_type": user.user_type,
            "status": user.status,
            "create_time": user.create_time.isoformat() if user.create_time else None,
            "update_time": user.update_time.isoformat() if user.update_time else None
        }
    return None

def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        if user.user_name is not None:
            db_user.user_name = user.user_name
        if user.email is not None:
            db_user.email = user.email
        if user.password is not None:
            db_user.password = user.password
        if user.phone is not None:
            db_user.phone = user.phone
        if user.school_id is not None:
            db_user.school_id = user.school_id
        if user.college_id is not None:
            db_user.college_id = user.college_id
        if user.major_id is not None:
            db_user.major_id = user.major_id
        if user.grade is not None:
            db_user.grade = user.grade
        if user.user_type is not None:
            db_user.user_type = user.user_type
        if user.status is not None:
            db_user.status = user.status
        # 注意：角色通过User_Role表关联，不直接更新
        db.commit()
        db.refresh(db_user)
        # 返回可序列化的字典，与get_user保持一致
        return {
            "user_id": db_user.user_id,
            "user_name": db_user.user_name,
            "email": db_user.email,
            "phone": db_user.phone,
            "school_id": db_user.school_id,
            "college_id": db_user.college_id,
            "major_id": db_user.major_id,
            "grade": db_user.grade,
            "user_type": db_user.user_type,
            "status": db_user.status,
            "create_time": db_user.create_time.isoformat() if db_user.create_time else None,
            "update_time": db_user.update_time.isoformat() if db_user.update_time else None
        }
    return None

def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# =================== Team ===================

def create_team(db: Session, team: TeamCreate):
    # 处理队长ID：如果是字符串，尝试作为user_id查询对应的用户
    captain_id = team.captain_id
    if isinstance(captain_id, str):
        # 按学号查询用户
        captain_user = db.query(User).filter(User.user_id == captain_id).first()
        if not captain_user:
            raise ValueError(f"学号为 {captain_id} 的用户不存在")
        captain_id = captain_user.user_id
    
    # 检查竞赛是否存在且状态为0（未开始，可报名）
    competition = db.query(Competition).filter(Competition.competition_id == team.competition_id).first()
    if not competition:
        raise ValueError(f"竞赛ID {team.competition_id} 不存在")
    if competition.status != 0:
        raise ValueError(f"竞赛ID {team.competition_id} 未处于可报名状态（状态0）")
    
    # 检查用户是否已经在该竞赛中注册了队伍
    existing_registration = db.query(Registration).filter(
        Registration.user_id == captain_id,
        Registration.competition_id == team.competition_id
    ).first()
    
    if existing_registration:
        raise ValueError(f"用户ID {captain_id} 已经在竞赛ID {team.competition_id} 中注册了队伍")
    
    # 创建队伍
    db_team = Team(
        team_name=team.team_name,
        competition_id=team.competition_id,
        school_id=team.school_id,
        captain_id=captain_id,
        status=team.status
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    
    # 将队长自动加入团队成员表
    db_team_member = Team_Member(
        team_id=db_team.team_id,
        user_id=captain_id
    )
    db.add(db_team_member)
    db.commit()
    db.refresh(db_team_member)
    
    # 在Registration表中为队长创建注册记录
    registration = Registration(
        user_id=captain_id,
        competition_id=team.competition_id,
        team_id=db_team.team_id
    )
    db.add(registration)
    db.commit()
    db.refresh(registration)
    
    return db_team


def get_teams(db: Session, competition_id: Optional[int] = None):
    query = db.query(Team)
    
    # 按竞赛ID过滤
    if competition_id:
        query = query.filter(Team.competition_id == competition_id)
    
    teams = query.all()
    return [
        {
            "team_id": t.team_id,
            "team_name": t.team_name,
            "competition_id": t.competition_id,
            "school_id": t.school_id,
            "captain_id": t.captain_id,
            "status": t.status,
            "create_time": t.create_time,
            "update_time": t.update_time
        }
        for t in teams
    ]

def get_teams_by_user(db: Session, user_id: str):
    """根据用户ID获取该用户所在的所有队伍"""
    # 获取用户作为成员的队伍ID
    team_members = db.query(Team_Member).filter(Team_Member.user_id == user_id).all()
    member_team_ids = [tm.team_id for tm in team_members]
    
    # 获取用户作为队长的队伍ID
    captain_teams = db.query(Team).filter(Team.captain_id == user_id).all()
    captain_team_ids = [t.team_id for t in captain_teams]
    
    # 合并所有队伍ID并去重
    all_team_ids = list(set(member_team_ids + captain_team_ids))
    
    # 如果用户没有加入任何队伍，返回空列表
    if not all_team_ids:
        return []
    
    # 查询这些队伍的详细信息
    teams = db.query(Team).filter(Team.team_id.in_(all_team_ids)).all()
    return [
        {
            "team_id": t.team_id,
            "team_name": t.team_name,
            "competition_id": t.competition_id,
            "school_id": t.school_id,
            "captain_id": t.captain_id,
            "status": t.status,
            "create_time": t.create_time,
            "update_time": t.update_time
        }
        for t in teams
    ]

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.team_id == team_id).first()

def update_team(db: Session, team_id: int, team: TeamUpdate):
    db_team = db.query(Team).filter(Team.team_id == team_id).first()
    if db_team:
        if team.team_name is not None:
            db_team.team_name = team.team_name
        if team.competition_id is not None:
            db_team.competition_id = team.competition_id
        if team.school_id is not None:
            db_team.school_id = team.school_id
        if team.captain_id is not None:
            # 处理队长ID：如果是字符串，尝试作为user_id查询对应的用户
            captain_id = team.captain_id
            if isinstance(captain_id, str):
                # 按学号查询用户
                captain_user = db.query(User).filter(User.user_id == captain_id).first()
                if not captain_user:
                    raise ValueError(f"学号为 {captain_id} 的用户不存在")
                captain_id = captain_user.user_id
            db_team.captain_id = captain_id
        if team.status is not None:
            if isinstance(team.status, str):
                if team.status == "inactive":
                    db_team.status = 0
                elif team.status == "active":
                    db_team.status = 1
            else:
                db_team.status = team.status
        db.commit()
        db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    # 获取要删除的队伍信息
    db_team = db.query(Team).filter(Team.team_id == team_id).first()
    if db_team:
        # 获取队伍所属的竞赛ID
        competition_id = db_team.competition_id
        
        # 获取队伍的所有成员
        team_members = db.query(Team_Member).filter(Team_Member.team_id == team_id).all()
        
        # 删除所有队员的Registration记录
        for member in team_members:
            db.query(Registration).filter(
                Registration.user_id == member.user_id,
                Registration.competition_id == competition_id
            ).delete()
        
        # 删除队长的Registration记录
        db.query(Registration).filter(
            Registration.user_id == db_team.captain_id,
            Registration.competition_id == competition_id
        ).delete()
        
        # 删除队伍
        db.delete(db_team)
        db.commit()
    return db_team

# =================== Team_Member ===================
def create_team_member(db: Session, team_member: TeamMemberCreate):
    # 获取要加入的队伍所属的竞赛ID
    team = db.query(Team).filter(Team.team_id == team_member.team_id).first()
    if not team:
        raise ValueError(f"队伍ID {team_member.team_id} 不存在")
    
    # 检查该用户是否已经在该竞赛中注册了队伍
    existing_registration = db.query(Registration).filter(
        Registration.user_id == team_member.user_id,
        Registration.competition_id == team.competition_id
    ).first()
    
    if existing_registration:
        raise ValueError(f"用户ID {team_member.user_id} 已经在竞赛ID {team.competition_id} 中注册了队伍")
    
    # 创建队员记录
    db_team_member = Team_Member(
        team_id=team_member.team_id,
        user_id=team_member.user_id
    )
    db.add(db_team_member)
    db.commit()
    db.refresh(db_team_member)
    
    # 在Registration表中创建记录，触发UNIQUE约束
    registration = Registration(
        user_id=team_member.user_id,
        competition_id=team.competition_id
    )
    db.add(registration)
    db.commit()
    db.refresh(registration)
    
    return db_team_member

def get_team_members(db: Session):
    team_members = db.query(Team_Member).all()
    return [
        {
            "team_id": tm.team_id,
            "user_id": tm.user_id,
            "join_time": tm.join_time.isoformat() if tm.join_time else None
        }
        for tm in team_members
    ]

def get_team_members_by_team(db: Session, team_id: int):
    # 关联查询Team_Member和User表
    team_members = db.query(Team_Member, User).filter(
        Team_Member.team_id == team_id,
        Team_Member.user_id == User.user_id
    ).all()
    return [
        {
            "team_id": tm.team_id,
            "user_id": tm.user_id,
            "username": user.user_name,
            "student_name": user.user_name,
            "school_id": user.school_id,
            "college_id": user.college_id,
            "major_id": user.major_id,
            "join_time": tm.join_time.isoformat() if tm.join_time else None
        }
        for tm, user in team_members
    ]

def get_team_members_by_user(db: Session, user_id: str):
    team_members = db.query(Team_Member).filter(Team_Member.user_id == user_id).all()
    return [
        {
            "team_id": tm.team_id,
            "user_id": tm.user_id,
            "join_time": tm.join_time.isoformat() if tm.join_time else None
        }
        for tm in team_members
    ]

def delete_team_member(db: Session, team_id: int, user_id: str):
    db_team_member = db.query(Team_Member).filter(
        Team_Member.team_id == team_id,
        Team_Member.user_id == user_id
    ).first()
    if db_team_member:
        # 获取队伍所属的竞赛ID
        team = db.query(Team).filter(Team.team_id == team_id).first()
        if team:
            # 删除该队员的Registration记录
            db.query(Registration).filter(
                Registration.user_id == user_id,
                Registration.competition_id == team.competition_id
            ).delete()
        
        db.delete(db_team_member)
        db.commit()
    return db_team_member

# =================== Team_Invite ===================
def create_team_invite(db: Session, team_id: int, from_user_id: str, to_user_id: str):
    """创建队伍邀请"""
    # 检查发送者是否在该队伍中
    sender_in_team = db.query(Team_Member).filter(
        Team_Member.team_id == team_id,
        Team_Member.user_id == from_user_id
    ).first() or db.query(Team).filter(
        Team.team_id == team_id,
        Team.captain_id == from_user_id
    ).first()
    
    if not sender_in_team:
        raise ValueError("只有队伍成员才能发送邀请")
    
    # 检查接收者是否已经在该队伍中
    receiver_in_team = db.query(Team_Member).filter(
        Team_Member.team_id == team_id,
        Team_Member.user_id == to_user_id
    ).first() or db.query(Team).filter(
        Team.team_id == team_id,
        Team.captain_id == to_user_id
    ).first()
    
    if receiver_in_team:
        raise ValueError("该用户已经是队伍成员")
    
    # 检查是否已经存在待处理的邀请
    existing_invite = db.query(Team_Invite).filter(
        Team_Invite.team_id == team_id,
        Team_Invite.to_user_id == to_user_id,
        Team_Invite.status == 0
    ).first()
    
    if existing_invite:
        raise ValueError("该用户已经有一个待处理的邀请")
    
    # 检查接收者是否在该竞赛中已经加入了其他队伍
    team = db.query(Team).filter(Team.team_id == team_id).first()
    if team:
        existing_registration = db.query(Registration).filter(
            Registration.user_id == to_user_id,
            Registration.competition_id == team.competition_id
        ).first()
        
        if existing_registration:
            raise ValueError("该用户已经在该竞赛中加入了其他队伍")
    
    # 创建邀请
    db_invite = Team_Invite(
        team_id=team_id,
        from_user_id=from_user_id,
        to_user_id=to_user_id,
        status=0  # 0: 待处理
    )
    db.add(db_invite)
    db.commit()
    db.refresh(db_invite)
    return db_invite

def get_team_invites_by_user(db: Session, user_id: str, status: Optional[int] = None):
    """获取用户的邀请列表"""
    query = db.query(Team_Invite).filter(Team_Invite.to_user_id == user_id)
    
    if status is not None:
        query = query.filter(Team_Invite.status == status)
    
    invites = query.order_by(Team_Invite.create_time.desc()).all()
    
    # 获取详细信息
    result = []
    for invite in invites:
        # 获取发送者信息
        from_user = db.query(User).filter(User.user_id == invite.from_user_id).first()
        # 获取队伍信息
        team = db.query(Team).filter(Team.team_id == invite.team_id).first()
        # 获取竞赛信息
        competition = db.query(Competition).filter(Competition.competition_id == team.competition_id).first() if team else None
        
        invite_info = {
            "invite_id": invite.invite_id,
            "team_id": invite.team_id,
            "team_name": team.team_name if team else "未知队伍",
            "competition_id": team.competition_id if team else None,
            "competition_name": competition.competition_name if competition else "未知竞赛",
            "from_user_id": invite.from_user_id,
            "from_user_name": from_user.user_name if from_user else "未知用户",
            "to_user_id": invite.to_user_id,
            "status": invite.status,
            "status_text": "待处理" if invite.status == 0 else "已接受" if invite.status == 1 else "已拒绝",
            "create_time": invite.create_time.isoformat() if invite.create_time else None
        }
        result.append(invite_info)
    
    return result

def update_invite_status(db: Session, invite_id: int, status: int, user_id: str):
    """更新邀请状态"""
    # 获取邀请信息
    invite = db.query(Team_Invite).filter(
        Team_Invite.invite_id == invite_id,
        Team_Invite.to_user_id == user_id
    ).first()
    
    if not invite:
        raise ValueError("邀请不存在")
    
    if invite.status != 0:
        raise ValueError("邀请已经处理过")
    
    if status not in [1, 2]:
        raise ValueError("无效的状态值")
    
    # 更新邀请状态
    invite.status = status
    db.commit()
    db.refresh(invite)
    
    # 如果接受邀请，添加到队伍中
    if status == 1:
        team = db.query(Team).filter(Team.team_id == invite.team_id).first()
        if team:
            # 创建队员记录
            team_member = Team_Member(
                team_id=invite.team_id,
                user_id=user_id
            )
            db.add(team_member)
            
            # 在Registration表中创建记录
            registration = Registration(
                user_id=user_id,
                competition_id=team.competition_id
            )
            db.add(registration)
            
            db.commit()
    
    return invite

def get_team_invites_by_team(db: Session, team_id: int):
    """获取队伍的邀请列表"""
    invites = db.query(Team_Invite).filter(Team_Invite.team_id == team_id).all()
    
    # 获取详细信息
    result = []
    for invite in invites:
        # 获取发送者信息
        from_user = db.query(User).filter(User.user_id == invite.from_user_id).first()
        # 获取接收者信息
        to_user = db.query(User).filter(User.user_id == invite.to_user_id).first()
        
        invite_info = {
            "invite_id": invite.invite_id,
            "team_id": invite.team_id,
            "from_user_id": invite.from_user_id,
            "from_user_name": from_user.user_name if from_user else "未知用户",
            "to_user_id": invite.to_user_id,
            "to_user_name": to_user.user_name if to_user else "未知用户",
            "status": invite.status,
            "status_text": "待处理" if invite.status == 0 else "已接受" if invite.status == 1 else "已拒绝",
            "create_time": invite.create_time.isoformat() if invite.create_time else None
        }
        result.append(invite_info)
    
    return result

# =================== Problem ===================
def create_problem(db: Session, problem: ProblemCreate):
    db_problem = Problem(
        title=problem.title,
        description=problem.description,
        file_url=problem.file_url,
        max_teams=problem.max_teams,
        competition_id=problem.competition_id
    )
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_problems(db: Session):
    problems = db.query(Problem).all()
    return [
        {
            "problem_id": p.problem_id,
            "title": p.title,
            "description": p.description,
            "file_url": p.file_url,
            "max_teams": p.max_teams,
            "competition_id": p.competition_id
        }
        for p in problems
    ]

def get_problem(db: Session, problem_id: int):
    return db.query(Problem).filter(Problem.problem_id == problem_id).first()

def get_problems_by_competition(db: Session, competition_id: int):
    problems = db.query(Problem).filter(Problem.competition_id == competition_id).all()
    return [
        {
            "problem_id": p.problem_id,
            "title": p.title,
            "description": p.description,
            "file_url": p.file_url,
            "max_teams": p.max_teams,
            "competition_id": p.competition_id
        }
        for p in problems
    ]

def update_problem(db: Session, problem_id: int, problem: ProblemUpdate):
    db_problem = db.query(Problem).filter(Problem.problem_id == problem_id).first()
    if db_problem:
        if problem.title is not None:
            db_problem.title = problem.title
        if problem.description is not None:
            db_problem.description = problem.description
        if problem.file_url is not None:
            db_problem.file_url = problem.file_url
        if problem.max_teams is not None:
            db_problem.max_teams = problem.max_teams
        db.commit()
        db.refresh(db_problem)
    return db_problem

def delete_problem(db: Session, problem_id: int):
    db_problem = db.query(Problem).filter(Problem.problem_id == problem_id).first()
    if db_problem:
        db.delete(db_problem)
        db.commit()
    return db_problem

# =================== Work ===================
def create_work(db: Session, work_data):
    from models import Problem, Team
    
    # 获取题目信息
    problem = db.query(Problem).filter(Problem.problem_id == work_data.problem_id).first()
    if not problem:
        raise ValueError("题目不存在")
    
    # 获取队伍信息
    team = db.query(Team).filter(Team.team_id == work_data.team_id).first()
    if not team:
        raise ValueError("队伍不存在")
    
    # 创建作品
    db_work = Work(
        team_id=work_data.team_id,
        problem_id=work_data.problem_id,
        competition_id=problem.competition_id,
        teacher_user_id=work_data.teacher_user_id,
        file_url=work_data.file_url,
        version=work_data.version,
        score=work_data.score,
        review_user_id=work_data.review_user_id,
        review_comment=work_data.review_comment,
        is_reviewed=work_data.is_reviewed
    )
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work

def get_works(db: Session, team_id: Optional[int] = None, team_id__in: Optional[List[int]] = None, problem_id: Optional[int] = None, reviewed: Optional[bool] = None):
    from models import Team, Problem, Competition
    
    # 连接查询获取完整信息
    query = db.query(Work, Team, Problem, Competition).outerjoin(
        Team, Work.team_id == Team.team_id
    ).outerjoin(
        Problem, Work.problem_id == Problem.problem_id
    ).outerjoin(
        Competition, Problem.competition_id == Competition.competition_id
    )
    
    # 按队伍ID过滤
    if team_id:
        query = query.filter(Work.team_id == team_id)
    
    # 按队伍ID列表过滤
    if team_id__in and len(team_id__in) > 0:
        query = query.filter(Work.team_id.in_(team_id__in))
    
    # 按题目ID过滤
    if problem_id:
        query = query.filter(Work.problem_id == problem_id)
    
    # 按是否已评审过滤
    if reviewed is not None:
        if reviewed:
            # 已评审：is_reviewed=1
            query = query.filter(Work.is_reviewed == 1)
        else:
            # 未评审：is_reviewed=0
            query = query.filter(Work.is_reviewed == 0)
    
    results = query.all()
    
    return [
        {
            "work_id": w.work_id,
            "team_id": w.team_id,
            "team_name": t.team_name if t else "",
            "school_id": t.school_id if t else None,
            "problem_id": w.problem_id,
            "problem_name": p.title if p else "",
            "competition_id": w.competition_id,
            "competition_name": c.competition_name if c else "",
            "teacher_user_id": w.teacher_user_id,
            "file_url": w.file_url,
            "file_name": w.file_url.split('/')[-1] if w.file_url else '',
            "version": w.version,
            "score": w.score,
            "submit_time": w.submit_time.isoformat() if w.submit_time else None,
            "review_user_id": w.review_user_id,
            "review_comment": w.review_comment,
            "review_time": w.review_time.isoformat() if w.review_time else None,
            "is_reviewed": w.is_reviewed == 1
        }
        for w, t, p, c in results
    ]

def get_work(db: Session, work_id: int):
    return db.query(Work).filter(Work.work_id == work_id).first()

def get_works_by_team(db: Session, team_id: int):
    works = db.query(Work).filter(Work.team_id == team_id).all()
    return [
        {
            "work_id": w.work_id,
            "team_id": w.team_id,
            "problem_id": w.problem_id,
            "competition_id": w.competition_id,
            "teacher_user_id": w.teacher_user_id,
            "file_url": w.file_url,
            "version": w.version,
            "score": w.score,
            "submit_time": w.submit_time.isoformat() if w.submit_time else None,
            "review_user_id": w.review_user_id,
            "review_comment": w.review_comment,
            "review_time": w.review_time.isoformat() if w.review_time else None,
            "is_reviewed": w.is_reviewed == 1
        }
        for w in works
    ]

def get_works_by_problem(db: Session, problem_id: int):
    works = db.query(Work).filter(Work.problem_id == problem_id).all()
    return [
        {
            "work_id": w.work_id,
            "team_id": w.team_id,
            "problem_id": w.problem_id,
            "competition_id": w.competition_id,
            "teacher_user_id": w.teacher_user_id,
            "file_url": w.file_url,
            "version": w.version,
            "score": w.score,
            "submit_time": w.submit_time,
            "review_user_id": w.review_user_id,
            "review_comment": w.review_comment,
            "review_time": w.review_time,
            "is_reviewed": w.is_reviewed == 1
        }
        for w in works
    ]

def get_works_by_user(db: Session, user_id: str):
    """根据用户ID获取该用户所在团队的所有作品"""
    from models import Team, Problem, Competition
    
    # 通过Team_Member表关联查询用户所在的队伍
    team_members = db.query(Team_Member).filter(Team_Member.user_id == user_id).all()
    team_ids = [tm.team_id for tm in team_members]
    
    # 如果用户没有加入任何队伍，返回空列表
    if not team_ids:
        return []
    
    # 连接查询获取完整信息
    query = db.query(Work, Team, Problem, Competition).join(
        Team, Work.team_id == Team.team_id
    ).join(
        Problem, Work.problem_id == Problem.problem_id
    ).join(
        Competition, Problem.competition_id == Competition.competition_id
    ).filter(Work.team_id.in_(team_ids))
    
    results = query.all()
    
    return [
        {
            "work_id": w.work_id,
            "team_id": w.team_id,
            "team_name": t.team_name,
            "problem_id": w.problem_id,
            "problem_name": p.title,
            "competition_id": w.competition_id,
            "competition_name": c.competition_name,
            "teacher_user_id": w.teacher_user_id,
            "file_url": w.file_url,
            "file_name": w.file_url.split('/')[-1] if w.file_url else '',
            "version": w.version,
            "score": w.score,
            "submit_time": w.submit_time.isoformat() if w.submit_time else None,
            "review_user_id": w.review_user_id,
            "review_comment": w.review_comment,
            "review_time": w.review_time.isoformat() if w.review_time else None,
            "is_reviewed": w.is_reviewed == 1
        }
        for w, t, p, c in results
    ]

def update_work(db: Session, work_id: int, work_data):
    db_work = db.query(Work).filter(Work.work_id == work_id).first()
    if db_work:
        if work_data.file_url is not None:
            db_work.file_url = work_data.file_url
        if work_data.version is not None:
            db_work.version = work_data.version
        if work_data.score is not None:
            db_work.score = work_data.score
        if work_data.review_user_id is not None:
            db_work.review_user_id = work_data.review_user_id
        if work_data.review_comment is not None:
            db_work.review_comment = work_data.review_comment
        if work_data.review_time is not None:
            db_work.review_time = work_data.review_time
        if work_data.is_reviewed is not None:
            db_work.is_reviewed = work_data.is_reviewed
        if work_data.teacher_user_id is not None:
            db_work.teacher_user_id = work_data.teacher_user_id
        db.commit()
        db.refresh(db_work)
    return db_work

def delete_work(db: Session, work_id: int):
    db_work = db.query(Work).filter(Work.work_id == work_id).first()
    if db_work:
        db.delete(db_work)
        db.commit()
    return db_work

def review_work(db: Session, work_id: int, review_user_id: str, score: float, comment: str):
    """评审作品"""
    from models import Team
    
    db_work = db.query(Work).filter(Work.work_id == work_id).first()
    if not db_work:
        raise ValueError("作品不存在")
    
    team_id = db_work.team_id
    
    # 查询该队伍的指导教师
    guiding_teachers = db.query(Teacher_Team).filter(Teacher_Team.team_id == team_id).all()
    guiding_teacher_ids = [t.user_id for t in guiding_teachers]
    
    # 检查评审员是否是该队伍的指导教师
    if review_user_id in guiding_teacher_ids:
        raise ValueError("不能评审自己指导的队伍")
    
    # 更新作品评审信息
    db_work.score = score
    db_work.review_user_id = review_user_id
    db_work.review_comment = comment
    db_work.review_time = dt.datetime.now()
    db_work.is_reviewed = 1
    
    db.commit()
    db.refresh(db_work)
    
    return {
        "work_id": db_work.work_id,
        "team_id": db_work.team_id,
        "problem_id": db_work.problem_id,
        "score": db_work.score,
        "review_user_id": db_work.review_user_id,
        "review_comment": db_work.review_comment,
        "review_time": db_work.review_time.isoformat() if db_work.review_time else None,
        "is_reviewed": db_work.is_reviewed == 1
    }

# =================== Message ===================
def create_message(db: Session, message: MessageCreate):
    db_message = Message(
        sender_id=message.sender_id,
        receiver_id=message.receiver_id,
        content=message.content,
        status=0  # 默认未读
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, user_id: Optional[str] = None, is_read: Optional[bool] = None):
    query = db.query(Message)
    
    # 按用户ID过滤（接收者）
    if user_id:
        query = query.filter(Message.receiver_id == user_id)
    
    # 按是否已读过滤
    if is_read is not None:
        # 假设status=0表示未读，1表示已读
        status_value = 1 if is_read else 0
        query = query.filter(Message.status == status_value)
    
    messages = query.all()
    return [
        {
            "message_id": m.message_id,
            "sender_id": m.sender_id,
            "receiver_id": m.receiver_id,
            "content": m.content,
            "status": "read" if m.status == 1 else "unread",
            "send_time": m.send_time.isoformat() if m.send_time else None
        }
        for m in messages
    ]

def get_message(db: Session, message_id: int):
    return db.query(Message).filter(Message.message_id == message_id).first()

def get_messages_by_sender(db: Session, sender_id: int):
    messages = db.query(Message).filter(Message.sender_id == sender_id).all()
    return [
        {
            "message_id": m.message_id,
            "sender_id": m.sender_id,
            "receiver_id": m.receiver_id,
            "content": m.content,
            "status": "read" if m.status == 1 else "unread",
            "send_time": m.send_time.isoformat() if m.send_time else None
        }
        for m in messages
    ]

def get_messages_by_receiver(db: Session, receiver_id: str):
    messages = db.query(Message).filter(Message.receiver_id == receiver_id).all()
    return [
        {
            "message_id": m.message_id,
            "sender_id": m.sender_id,
            "receiver_id": m.receiver_id,
            "content": m.content,
            "status": "read" if m.status == 1 else "unread",
            "send_time": m.send_time.isoformat() if m.send_time else None
        }
        for m in messages
    ]

def update_message(db: Session, message_id: int, message: MessageUpdate):
    db_message = db.query(Message).filter(Message.message_id == message_id).first()
    if db_message:
        if message.status is not None:
            # 将前端传来的字符串状态转换为后端的数字状态
            if isinstance(message.status, str):
                db_message.status = 1 if message.status == "read" else 0
            else:
                db_message.status = message.status
        db.commit()
        db.refresh(db_message)
    return db_message

def delete_message(db: Session, message_id: int):
    db_message = db.query(Message).filter(Message.message_id == message_id).first()
    if db_message:
        db.delete(db_message)
        db.commit()
    return db_message

# =================== Announcement ===================
def create_announcement(db: Session, announcement: AnnouncementCreate):
    db_announcement = Announcement(
        title=announcement.title,
        content=announcement.content,
        author_id=announcement.author_id
    )
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement

def get_announcements(db: Session):
    announcements = db.query(Announcement).all()
    return [
        {
            "announcement_id": a.announcement_id,
            "title": a.title,
            "content": a.content,
            "author_id": a.author_id,
            "create_time": a.create_time
        }
        for a in announcements
    ]

def get_announcement(db: Session, announcement_id: int):
    return db.query(Announcement).filter(Announcement.announcement_id == announcement_id).first()

def update_announcement(db: Session, announcement_id: int, announcement: AnnouncementUpdate):
    db_announcement = db.query(Announcement).filter(Announcement.announcement_id == announcement_id).first()
    if db_announcement:
        if announcement.title is not None:
            db_announcement.title = announcement.title
        if announcement.content is not None:
            db_announcement.content = announcement.content
        db.commit()
        db.refresh(db_announcement)
    return db_announcement

def delete_announcement(db: Session, announcement_id: int):
    db_announcement = db.query(Announcement).filter(Announcement.announcement_id == announcement_id).first()
    if db_announcement:
        db.delete(db_announcement)
        db.commit()
    return db_announcement







# =================== Competition ===================
def create_competition(db: Session, competition: CompetitionCreate):
    db_competition = Competition(
        competition_name=competition.competition_name,
        session_no=competition.session_no,
        school_id=competition.school_id,
        sign_start=competition.sign_start,
        sign_end=competition.sign_end,
        competition_start=competition.competition_start,
        competition_end=competition.competition_end,
        fee_amount=competition.fee_amount,
        reward_rule=competition.reward_rule,
        status=competition.status
    )
    db.add(db_competition)
    db.commit()
    db.refresh(db_competition)
    return db_competition

def get_competitions(db: Session):
    competitions = db.query(Competition).all()
    return [
        {
            "competition_id": c.competition_id,
            "competition_name": c.competition_name,
            "session_no": c.session_no,
            "school_id": c.school_id,
            "sign_start": c.sign_start,
            "sign_end": c.sign_end,
            "competition_start": c.competition_start,
            "competition_end": c.competition_end,
            "fee_amount": c.fee_amount,
            "reward_rule": c.reward_rule,
            "status": c.status,
            "create_time": c.create_time
        }
        for c in competitions
    ]

def get_competition(db: Session, competition_id: int):
    return db.query(Competition).filter(Competition.competition_id == competition_id).first()

def update_competition(db: Session, competition_id: int, competition: CompetitionUpdate):
    db_competition = db.query(Competition).filter(Competition.competition_id == competition_id).first()
    if db_competition:
        if competition.competition_name is not None:
            db_competition.competition_name = competition.competition_name
        if competition.session_no is not None:
            db_competition.session_no = competition.session_no
        if competition.school_id is not None:
            db_competition.school_id = competition.school_id
        if competition.sign_start is not None:
            db_competition.sign_start = competition.sign_start
        if competition.sign_end is not None:
            db_competition.sign_end = competition.sign_end
        if competition.competition_start is not None:
            db_competition.competition_start = competition.competition_start
        if competition.competition_end is not None:
            db_competition.competition_end = competition.competition_end
        if competition.fee_amount is not None:
            db_competition.fee_amount = competition.fee_amount
        if competition.reward_rule is not None:
            db_competition.reward_rule = competition.reward_rule
        if competition.status is not None:
            if isinstance(competition.status, str):
                if competition.status == "pending":
                    db_competition.status = 0
                elif competition.status == "active":
                    db_competition.status = 1
                elif competition.status == "ended":
                    db_competition.status = 2
            else:
                db_competition.status = competition.status
        db.commit()
        db.refresh(db_competition)
    return db_competition

def delete_competition(db: Session, competition_id: int):
    db_competition = db.query(Competition).filter(Competition.competition_id == competition_id).first()
    if db_competition:
        db.delete(db_competition)
        db.commit()
    return db_competition

# =================== Registration ===================
def create_registration(db: Session, registration: RegistrationCreate):
    # 检查竞赛是否存在
    competition = db.query(Competition).filter(Competition.competition_id == registration.competition_id).first()
    if not competition:
        raise ValueError("竞赛不存在")
    
    # 检查竞赛状态是否为可报名（状态0）
    if competition.status != 0:
        raise ValueError("该竞赛当前不可报名")
    
    # 检查团队是否存在
    team = db.query(Team).filter(Team.team_id == registration.team_id).first()
    if not team:
        raise ValueError("团队不存在")
    
    # 检查团队是否属于该竞赛
    if team.competition_id != registration.competition_id:
        raise ValueError("该团队不属于此竞赛")
    
    # 检查用户是否为团队成员
    is_team_member = db.query(Team_Member).filter(
        Team_Member.team_id == registration.team_id,
        Team_Member.user_id == registration.user_id
    ).first()
    if not is_team_member:
        # 检查用户是否为队长
        if team.captain_id != registration.user_id:
            raise ValueError("您不是该团队的成员")
    
    # 检查是否已经报名
    existing_registration = db.query(Registration).filter(
        Registration.user_id == registration.user_id,
        Registration.competition_id == registration.competition_id
    ).first()
    if existing_registration:
        raise ValueError("您已经报名该竞赛")
    
    # 创建报名记录
    db_registration = Registration(
        user_id=registration.user_id,
        competition_id=registration.competition_id,
        team_id=registration.team_id,
        registration_time=current_time,
        fee_status=registration.fee_status or 0,
        audit_status=registration.audit_status or 0
    )
    
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration

def get_registrations(db: Session):
    registrations = db.query(Registration).all()
    return [
        {
            "reg_id": r.reg_id,
            "user_id": r.user_id,
            "competition_id": r.competition_id,
            "team_id": r.team_id,
            "registration_time": r.registration_time,
            "fee_status": r.fee_status,
            "payment_method": r.payment_method,
            "payment_time": r.payment_time,
            "audit_status": r.audit_status,
            "audit_remark": r.audit_remark
        }
        for r in registrations
    ]

def get_registration(db: Session, registration_id: int):
    return db.query(Registration).filter(Registration.reg_id == registration_id).first()

def get_registrations_by_user(db: Session, user_id: int):
    registrations = db.query(Registration).filter(Registration.user_id == user_id).all()
    return [
        {
            "reg_id": r.reg_id,
            "user_id": r.user_id,
            "competition_id": r.competition_id,
            "team_id": r.team_id,
            "registration_time": r.registration_time,
            "fee_status": r.fee_status,
            "payment_method": r.payment_method,
            "payment_time": r.payment_time,
            "audit_status": r.audit_status,
            "audit_remark": r.audit_remark
        }
        for r in registrations
    ]

def get_registrations_by_competition(db: Session, competition_id: int):
    registrations = db.query(Registration).filter(Registration.competition_id == competition_id).all()
    return [
        {
            "reg_id": r.reg_id,
            "user_id": r.user_id,
            "competition_id": r.competition_id,
            "team_id": r.team_id,
            "registration_time": r.registration_time,
            "fee_status": r.fee_status,
            "payment_method": r.payment_method,
            "payment_time": r.payment_time,
            "audit_status": r.audit_status,
            "audit_remark": r.audit_remark
        }
        for r in registrations
    ]

def update_registration(db: Session, registration_id: int, registration: RegistrationUpdate):
    db_registration = db.query(Registration).filter(Registration.reg_id == registration_id).first()
    if db_registration:
        if registration.fee_status is not None:
            db_registration.fee_status = registration.fee_status
        if registration.payment_method is not None:
            db_registration.payment_method = registration.payment_method
        if registration.payment_time is not None:
            db_registration.payment_time = registration.payment_time
        if registration.audit_status is not None:
            db_registration.audit_status = registration.audit_status
            # 审核通过时，自动将团队状态设置为活跃(1)
            if registration.audit_status == 1 and db_registration.team_id:
                db_team = db.query(Team).filter(Team.team_id == db_registration.team_id).first()
                if db_team:
                    db_team.status = 1
        if registration.audit_remark is not None:
            db_registration.audit_remark = registration.audit_remark
        db.commit()
        db.refresh(db_registration)
    return db_registration

def delete_registration(db: Session, registration_id: int):
    db_registration = db.query(Registration).filter(Registration.reg_id == registration_id).first()
    if db_registration:
        db.delete(db_registration)
        db.commit()
    return db_registration

# =================== Award ===================
def create_award(db: Session, award: AwardCreate):
    db_award = Award(
        team_id=award.team_id,
        competition_id=award.competition_id,
        school_id=award.school_id,
        award_name=award.award_name,
        award_rank=award.award_rank
    )
    db.add(db_award)
    db.commit()
    db.refresh(db_award)
    return db_award

def get_awards(db: Session):
    awards = db.query(Award).all()
    return [
        {
            "award_id": a.award_id,
            "team_id": a.team_id,
            "competition_id": a.competition_id,
            "school_id": a.school_id,
            "award_name": a.award_name,
            "award_rank": a.award_rank
        }
        for a in awards
    ]

def get_award(db: Session, award_id: int):
    return db.query(Award).filter(Award.award_id == award_id).first()

def update_award(db: Session, award_id: int, award: AwardUpdate):
    db_award = db.query(Award).filter(Award.award_id == award_id).first()
    if db_award:
        if award.team_id is not None:
            db_award.team_id = award.team_id
        if award.competition_id is not None:
            db_award.competition_id = award.competition_id
        if award.school_id is not None:
            db_award.school_id = award.school_id
        if award.award_name is not None:
            db_award.award_name = award.award_name
        if award.award_rank is not None:
            db_award.award_rank = award.award_rank
        db.commit()
        db.refresh(db_award)
    return db_award

def delete_award(db: Session, award_id: int):
    db_award = db.query(Award).filter(Award.award_id == award_id).first()
    if db_award:
        db.delete(db_award)
        db.commit()
    return db_award

def get_awards_by_team(db: Session, team_id: int):
    awards = db.query(Award).filter(Award.team_id == team_id).all()
    return [
        {
            "award_id": a.award_id,
            "team_id": a.team_id,
            "competition_id": a.competition_id,
            "school_id": a.school_id,
            "award_name": a.award_name,
            "award_rank": a.award_rank
        }
        for a in awards
    ]

def get_awards_by_competition(db: Session, competition_id: int):
    awards = db.query(Award).filter(Award.competition_id == competition_id).all()
    return [
        {
            "award_id": a.award_id,
            "team_id": a.team_id,
            "competition_id": a.competition_id,
            "school_id": a.school_id,
            "award_name": a.award_name,
            "award_rank": a.award_rank
        }
        for a in awards
    ]

# =================== Teacher_Team ===================
def create_teacher_team(db: Session, teacher_team: TeacherTeamCreate):
    # 检查用户是否为教师
    teacher_user = db.query(User).filter(
        User.user_id == teacher_team.user_id,
        User.user_type == 2  # 2表示教师用户类型
    ).first()
    
    if not teacher_user:
        raise ValueError(f"用户ID {teacher_team.user_id} 不是有效的教师用户")
    
    # 检查队伍是否存在
    team = db.query(Team).filter(Team.team_id == teacher_team.team_id).first()
    if not team:
        raise ValueError(f"队伍ID {teacher_team.team_id} 不存在")
    
    # 检查队伍是否已经有指导老师
    existing_teacher_team = db.query(Teacher_Team).filter(
        Teacher_Team.team_id == teacher_team.team_id,
        Teacher_Team.confirm_status == 1  # 1表示已同意
    ).first()
    
    if existing_teacher_team:
        raise ValueError(f"队伍ID {teacher_team.team_id} 已经有指导老师")
    
    # 创建指导关联
    db_teacher_team = Teacher_Team(
        user_id=teacher_team.user_id,
        team_id=teacher_team.team_id,
        assign_method=teacher_team.assign_method or "student_request",
        confirm_status=teacher_team.confirm_status or 0  # 0表示待处理
    )
    
    db.add(db_teacher_team)
    db.commit()
    db.refresh(db_teacher_team)
    return db_teacher_team

def get_teacher_teams(db: Session):
    teacher_teams = db.query(Teacher_Team).all()
    return [
        {
            "user_id": tt.user_id,
            "team_id": tt.team_id
        }
        for tt in teacher_teams
    ]

def get_teacher_teams_by_user(db: Session, user_id: str):
    teacher_teams = db.query(Teacher_Team).filter(Teacher_Team.user_id == user_id).all()
    return [
        {
            "user_id": tt.user_id,
            "team_id": tt.team_id,
            "assign_method": tt.assign_method,
            "confirm_status": "confirmed" if tt.confirm_status == 1 else "rejected" if tt.confirm_status == 2 else "pending",
            "assign_time": tt.assign_time.isoformat() if tt.assign_time else None
        }
        for tt in teacher_teams
    ]

def get_teacher_teams_by_team(db: Session, team_id: int):
    teacher_teams = db.query(Teacher_Team, User).join(User, Teacher_Team.user_id == User.user_id).filter(Teacher_Team.team_id == team_id).all()
    return [
        {
            "user_id": tt.user_id,
            "team_id": tt.team_id,
            "assign_method": tt.assign_method,
            "confirm_status": "confirmed" if tt.confirm_status == 1 else "rejected" if tt.confirm_status == 2 else "pending",
            "assign_time": tt.assign_time.isoformat() if tt.assign_time else None,
            "teacher_name": user.user_name
        }
        for tt, user in teacher_teams
    ]

def delete_teacher_team(db: Session, user_id: str, team_id: int):
    db_teacher_team = db.query(Teacher_Team).filter(
        Teacher_Team.user_id == user_id,
        Teacher_Team.team_id == team_id
    ).first()
    if db_teacher_team:
        db.delete(db_teacher_team)
        db.commit()
    return db_teacher_team

def update_teacher_team(db: Session, user_id: str, team_id: int, teacher_team: TeacherTeamUpdate):
    db_teacher_team = db.query(Teacher_Team).filter(
        Teacher_Team.user_id == user_id,
        Teacher_Team.team_id == team_id
    ).first()
    if db_teacher_team:
        if teacher_team.assign_method is not None:
            db_teacher_team.assign_method = teacher_team.assign_method
        if teacher_team.confirm_status is not None:
            if isinstance(teacher_team.confirm_status, str):
                if teacher_team.confirm_status == "confirmed":
                    db_teacher_team.confirm_status = 1
                elif teacher_team.confirm_status == "rejected":
                    db_teacher_team.confirm_status = 2
                elif teacher_team.confirm_status == "pending":
                    db_teacher_team.confirm_status = 0
            else:
                db_teacher_team.confirm_status = teacher_team.confirm_status
        db.commit()
        db.refresh(db_teacher_team)
    return db_teacher_team

# =================== Teacher ===================
def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(
        teacher_no=teacher.teacher_no,
        teacher_name=teacher.teacher_name,
        school_id=teacher.school_id,
        college_id=teacher.college_id,
        research_field=teacher.research_field,
        phone=teacher.phone,
        email=teacher.email,
        max_guide_teams=teacher.max_guide_teams,
        current_guide_teams=teacher.current_guide_teams,
        status=teacher.status
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teachers(db: Session):
    teachers = db.query(Teacher).all()
    return [
        {
            "teacher_id": t.teacher_id,
            "teacher_no": t.teacher_no,
            "teacher_name": t.teacher_name,
            "school_id": t.school_id,
            "college_id": t.college_id,
            "research_field": t.research_field,
            "phone": t.phone,
            "email": t.email,
            "max_guide_teams": t.max_guide_teams,
            "current_guide_teams": t.current_guide_teams,
            "status": t.status,
            "create_time": t.create_time,
            "update_time": t.update_time
        }
        for t in teachers
    ]

def get_teacher(db: Session, teacher_id: int):
    teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if teacher:
        return {
            "teacher_id": teacher.teacher_id,
            "teacher_no": teacher.teacher_no,
            "teacher_name": teacher.teacher_name,
            "school_id": teacher.school_id,
            "college_id": teacher.college_id,
            "research_field": teacher.research_field,
            "phone": teacher.phone,
            "email": teacher.email,
            "max_guide_teams": teacher.max_guide_teams,
            "current_guide_teams": teacher.current_guide_teams,
            "status": teacher.status,
            "create_time": teacher.create_time,
            "update_time": teacher.update_time
        }
    return None

def get_teachers_by_school(db: Session, school_id: int):
    teachers = db.query(Teacher).filter(Teacher.school_id == school_id).all()
    return [
        {
            "teacher_id": t.teacher_id,
            "teacher_no": t.teacher_no,
            "teacher_name": t.teacher_name,
            "school_id": t.school_id,
            "college_id": t.college_id,
            "research_field": t.research_field,
            "phone": t.phone,
            "email": t.email,
            "max_guide_teams": t.max_guide_teams,
            "current_guide_teams": t.current_guide_teams,
            "status": t.status,
            "create_time": t.create_time,
            "update_time": t.update_time
        }
        for t in teachers
    ]

def get_teachers_by_college(db: Session, college_id: int):
    teachers = db.query(Teacher).filter(Teacher.college_id == college_id).all()
    return [
        {
            "teacher_id": t.teacher_id,
            "teacher_no": t.teacher_no,
            "teacher_name": t.teacher_name,
            "school_id": t.school_id,
            "college_id": t.college_id,
            "research_field": t.research_field,
            "phone": t.phone,
            "email": t.email,
            "max_guide_teams": t.max_guide_teams,
            "current_guide_teams": t.current_guide_teams,
            "status": t.status,
            "create_time": t.create_time,
            "update_time": t.update_time
        }
        for t in teachers
    ]

def update_teacher(db: Session, teacher_id: int, teacher: TeacherUpdate):
    db_teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if db_teacher:
        if teacher.teacher_name is not None:
            db_teacher.teacher_name = teacher.teacher_name
        if teacher.school_id is not None:
            db_teacher.school_id = teacher.school_id
        if teacher.college_id is not None:
            db_teacher.college_id = teacher.college_id
        if teacher.research_field is not None:
            db_teacher.research_field = teacher.research_field
        if teacher.phone is not None:
            db_teacher.phone = teacher.phone
        if teacher.email is not None:
            db_teacher.email = teacher.email
        if teacher.max_guide_teams is not None:
            db_teacher.max_guide_teams = teacher.max_guide_teams
        if teacher.current_guide_teams is not None:
            db_teacher.current_guide_teams = teacher.current_guide_teams
        if teacher.status is not None:
            db_teacher.status = teacher.status
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return db_teacher

# =================== Role ===================
def create_role(db: Session, role: RoleCreate):
    db_role = Role(
        role_name=role.role_name,
        description=role.description
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    role = db.query(Role).filter(Role.role_id == role_id).first()
    if role:
        return {
            "role_id": role.role_id,
            "role_name": role.role_name,
            "description": role.description
        }
    return None

def get_roles(db: Session):
    roles = db.query(Role).all()
    return [
        {
            "role_id": role.role_id,
            "role_name": role.role_name,
            "description": role.description
        }
        for role in roles
    ]

def update_role(db: Session, role_id: int, role: RoleUpdate):
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role:
        if role.role_name is not None:
            db_role.role_name = role.role_name
        if role.description is not None:
            db_role.description = role.description
        db.commit()
        db.refresh(db_role)
        return {
            "role_id": db_role.role_id,
            "role_name": db_role.role_name,
            "description": db_role.description
        }
    return None

def delete_role(db: Session, role_id: int):
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()
        return {
            "role_id": db_role.role_id,
            "role_name": db_role.role_name,
            "description": db_role.description
        }
    return None

# =================== Permission ===================
def create_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(
        perm_name=permission.perm_name,
        description=permission.description
    )
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def get_permission(db: Session, perm_id: int):
    permission = db.query(Permission).filter(Permission.perm_id == perm_id).first()
    if permission:
        return {
            "perm_id": permission.perm_id,
            "perm_name": permission.perm_name,
            "description": permission.description
        }
    return None

def get_permissions(db: Session):
    permissions = db.query(Permission).all()
    return [
        {
            "perm_id": perm.perm_id,
            "perm_name": perm.perm_name,
            "description": perm.description
        }
        for perm in permissions
    ]

def update_permission(db: Session, perm_id: int, permission: PermissionUpdate):
    db_permission = db.query(Permission).filter(Permission.perm_id == perm_id).first()
    if db_permission:
        if permission.perm_name is not None:
            db_permission.perm_name = permission.perm_name
        if permission.description is not None:
            db_permission.description = permission.description
        db.commit()
        db.refresh(db_permission)
        return {
            "perm_id": db_permission.perm_id,
            "perm_name": db_permission.perm_name,
            "description": db_permission.description
        }
    return None

def delete_permission(db: Session, perm_id: int):
    db_permission = db.query(Permission).filter(Permission.perm_id == perm_id).first()
    if db_permission:
        db.delete(db_permission)
        db.commit()
        return {
            "perm_id": db_permission.perm_id,
            "perm_name": db_permission.perm_name,
            "description": db_permission.description
        }
    return None

# =================== User_Role ===================
def create_user_role(db: Session, user_role: UserRoleCreate):
    db_user_role = User_Role(
        user_id=user_role.user_id,
        role_id=user_role.role_id
    )
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return db_user_role

def get_user_roles(db: Session):
    user_roles = db.query(User_Role).all()
    return [
        {
            "user_id": ur.user_id,
            "role_id": ur.role_id
        }
        for ur in user_roles
    ]

def get_user_roles_by_user(db: Session, user_id: int):
    user_roles = db.query(User_Role).filter(User_Role.user_id == user_id).all()
    return [
        {
            "user_id": ur.user_id,
            "role_id": ur.role_id
        }
        for ur in user_roles
    ]

def get_user_roles_by_role(db: Session, role_id: int):
    user_roles = db.query(User_Role).filter(User_Role.role_id == role_id).all()
    return [
        {
            "user_id": ur.user_id,
            "role_id": ur.role_id
        }
        for ur in user_roles
    ]

def delete_user_role(db: Session, user_id: int, role_id: int):
    db_user_role = db.query(User_Role).filter(
        User_Role.user_id == user_id,
        User_Role.role_id == role_id
    ).first()
    if db_user_role:
        db.delete(db_user_role)
        db.commit()
    return db_user_role

# =================== Role_Permission ===================
def create_role_permission(db: Session, role_perm: RolePermissionCreate):
    db_role_perm = Role_Permission(
        role_id=role_perm.role_id,
        perm_id=role_perm.perm_id
    )
    db.add(db_role_perm)
    db.commit()
    db.refresh(db_role_perm)
    return db_role_perm

def get_role_permissions(db: Session):
    role_permissions = db.query(Role_Permission).all()
    return [
        {
            "role_id": rp.role_id,
            "perm_id": rp.perm_id
        }
        for rp in role_permissions
    ]

def get_role_permissions_by_role(db: Session, role_id: int):
    role_permissions = db.query(Role_Permission).filter(Role_Permission.role_id == role_id).all()
    return [
        {
            "role_id": rp.role_id,
            "perm_id": rp.perm_id
        }
        for rp in role_permissions
    ]

def get_role_permissions_by_permission(db: Session, perm_id: int):
    role_permissions = db.query(Role_Permission).filter(Role_Permission.perm_id == perm_id).all()
    return [
        {
            "role_id": rp.role_id,
            "perm_id": rp.perm_id
        }
        for rp in role_permissions
    ]

def update_role_permission(db: Session, role_id: int, old_perm_id: int, new_perm_id: int):
    # 先删除旧的权限关联
    db.query(Role_Permission).filter(
        Role_Permission.role_id == role_id,
        Role_Permission.perm_id == old_perm_id
    ).delete()
    
    # 添加新的权限关联
    db_role_perm = Role_Permission(
        role_id=role_id,
        perm_id=new_perm_id
    )
    db.add(db_role_perm)
    db.commit()
    return db_role_perm

def delete_role_permission(db: Session, role_id: int, perm_id: int):
    result = db.query(Role_Permission).filter(
        Role_Permission.role_id == role_id,
        Role_Permission.perm_id == perm_id
    ).delete()
    db.commit()
    return result > 0

def batch_assign_permissions(db: Session, role_id: int, perm_ids: List[int]):
    # 删除该角色的所有现有权限
    db.query(Role_Permission).filter(Role_Permission.role_id == role_id).delete()
    
    # 批量添加新的权限关联
    role_permissions = [
        Role_Permission(role_id=role_id, perm_id=perm_id)
        for perm_id in perm_ids
    ]
    db.add_all(role_permissions)
    db.commit()
    return role_permissions


# =================== User_Import_Log ===================
def create_user_import_log(db: Session, user_import_log: UserImportLogCreate):
    db_user_import_log = User_Import_Log(
        operator_id=user_import_log.operator_id,
        file_name=user_import_log.file_name,
        success_count=user_import_log.success_count,
        fail_count=user_import_log.fail_count
    )
    db.add(db_user_import_log)
    db.commit()
    db.refresh(db_user_import_log)
    return db_user_import_log

def get_user_import_logs(db: Session):
    user_import_logs = db.query(User_Import_Log).all()
    return [
        {
            "import_id": uil.import_id,
            "operator_id": uil.operator_id,
            "import_time": uil.import_time,
            "file_name": uil.file_name,
            "success_count": uil.success_count,
            "fail_count": uil.fail_count
        }
        for uil in user_import_logs
    ]

def get_user_import_log(db: Session, import_id: int):
    user_import_log = db.query(User_Import_Log).filter(User_Import_Log.import_id == import_id).first()
    if user_import_log:
        return {
            "import_id": user_import_log.import_id,
            "operator_id": user_import_log.operator_id,
            "import_time": user_import_log.import_time,
            "file_name": user_import_log.file_name,
            "success_count": user_import_log.success_count,
            "fail_count": user_import_log.fail_count
        }
    return None

def update_user_import_log(db: Session, import_id: int, user_import_log: UserImportLogUpdate):
    db_user_import_log = db.query(User_Import_Log).filter(User_Import_Log.import_id == import_id).first()
    if db_user_import_log:
        if user_import_log.operator_id is not None:
            db_user_import_log.operator_id = user_import_log.operator_id
        if user_import_log.file_name is not None:
            db_user_import_log.file_name = user_import_log.file_name
        if user_import_log.success_count is not None:
            db_user_import_log.success_count = user_import_log.success_count
        if user_import_log.fail_count is not None:
            db_user_import_log.fail_count = user_import_log.fail_count
        db.commit()
        db.refresh(db_user_import_log)
    return db_user_import_log

def delete_user_import_log(db: Session, import_id: int):
    db_user_import_log = db.query(User_Import_Log).filter(User_Import_Log.import_id == import_id).first()
    if db_user_import_log:
        db.delete(db_user_import_log)
        db.commit()
    return db_user_import_log


# =================== Violation_Record ===================


def create_violation(db: Session, violation: ViolationCreate):
    db_violation = Violation_Record(
        team_id=violation.team_id,
        work_id=violation.work_id,
        competition_id=violation.competition_id,
        school_id=violation.school_id,
        violation_type=violation.violation_type,
        violation_detail=violation.violation_detail,
        is_approved=violation.is_approved,
        handle_time=dt.datetime.now()
    )
    db.add(db_violation)
    db.commit()
    db.refresh(db_violation)
    return db_violation

def get_violations(db: Session):
    violations = db.query(Violation_Record).all()
    return [
        {
            "violation_id": v.violation_id,
            "team_id": v.team_id,
            "team_name": v.team.team_name if v.team else None,
            "competition_id": v.competition_id,
            "competition_name": v.competition.competition_name if v.competition else None,
            "school_id": v.school_id,
            "violation_type": v.violation_type,
            "violation_detail": v.violation_detail,
            "is_approved": v.is_approved,
            "handle_user_id": v.handle_user_id,
            "handle_time": v.handle_time
        }
        for v in violations
    ]

def get_violation(db: Session, violation_id: int):
    return db.query(Violation_Record).filter(Violation_Record.violation_id == violation_id).first()

def get_violations_by_user(db: Session, user_id: int):
    violations = db.query(Violation_Record).join(Team_Member, Violation_Record.team_id == Team_Member.team_id).filter(Team_Member.user_id == user_id).all()
    return [
        {
            "violation_id": v.violation_id,
            "team_id": v.team_id,
            "team_name": v.team.team_name if v.team else None,
            "competition_id": v.competition_id,
            "competition_name": v.competition.competition_name if v.competition else None,
            "school_id": v.school_id,
            "violation_type": v.violation_type,
            "violation_detail": v.violation_detail,
            "is_approved": v.is_approved,
            "handle_user_id": v.handle_user_id,
            "handle_time": v.handle_time
        }
        for v in violations
    ]

def update_violation(db: Session, violation_id: int, violation: Union[ViolationBase, ViolationUpdate]):
    db_violation = db.query(Violation_Record).filter(Violation_Record.violation_id == violation_id).first()
    if db_violation:
        if hasattr(violation, 'violation_type') and violation.violation_type is not None:
            db_violation.violation_type = violation.violation_type
        if hasattr(violation, 'violation_detail') and violation.violation_detail is not None:
            db_violation.violation_detail = violation.violation_detail
        if hasattr(violation, 'handle_time') and violation.handle_time is not None:
            db_violation.handle_time = violation.handle_time
        if hasattr(violation, 'is_approved') and violation.is_approved is not None:
            old_is_approved = db_violation.is_approved
            db_violation.is_approved = violation.is_approved
            
            # 当违规记录被批准（is_approved=1），将该作品的分数和评审分数设为0
            if old_is_approved != violation.is_approved and violation.is_approved == 1:
                # 查询该作品记录
                if db_violation.work_id:
                    # 获取作品记录
                    work = db.query(Work).filter(
                        Work.work_id == db_violation.work_id
                    ).first()
                    
                    # 将作品的分数设为0
                    if work:
                        work.score = 0
                        db.add(work)
        
        db.commit()
        db.refresh(db_violation)
    return db_violation

def delete_violation(db: Session, violation_id: int):
    db_violation = db.query(Violation_Record).filter(Violation_Record.violation_id == violation_id).first()
    if db_violation:
        db.delete(db_violation)
        db.commit()
    return db_violation

# =================== Certificate_Info ===================
def create_certificate(db: Session, certificate: CertificateCreate):
    db_certificate = Certificate_Info(
        user_id=certificate.user_id,
        school_id=certificate.school_id,
        certificate_name=certificate.certificate_name,
        competition_name=certificate.competition_name,
        award_level=certificate.award_level,
        award_year=certificate.award_year,
        certificate_url=certificate.certificate_url,
        issue_date=certificate.issue_date or dt.datetime.now(),
        certificate_no=certificate.certificate_no
    )
    db.add(db_certificate)
    db.commit()
    db.refresh(db_certificate)
    return db_certificate

def get_certificates(db: Session):
    certificates = db.query(Certificate_Info).all()
    return [
        {
            "certificate_id": c.certificate_id,
            "user_id": c.user_id,
            "school_id": c.school_id,
            "certificate_name": c.certificate_name,
            "competition_name": c.competition_name,
            "award_level": c.award_level,
            "award_year": c.award_year,
            "certificate_url": c.certificate_url,
            "upload_time": c.upload_time,
            "issue_date": c.issue_date,
            "certificate_no": c.certificate_no
        }
        for c in certificates
    ]

def get_certificate(db: Session, certificate_id: int):
    return db.query(Certificate_Info).filter(Certificate_Info.certificate_id == certificate_id).first()

def get_certificates_by_user(db: Session, user_id: str):
    certificates = db.query(Certificate_Info).filter(Certificate_Info.user_id == user_id).all()
    return [
        {
            "certificate_id": c.certificate_id,
            "user_id": c.user_id,
            "school_id": c.school_id,
            "certificate_name": c.certificate_name,
            "competition_name": c.competition_name,
            "award_level": c.award_level,
            "award_year": c.award_year,
            "certificate_url": c.certificate_url,
            "upload_time": c.upload_time,
            "issue_date": c.issue_date,
            "certificate_no": c.certificate_no
        }
        for c in certificates
    ]

def update_certificate(db: Session, certificate_id: int, certificate: CertificateUpdate):
    db_certificate = db.query(Certificate_Info).filter(Certificate_Info.certificate_id == certificate_id).first()
    if db_certificate:
        if certificate.school_id is not None:
            db_certificate.school_id = certificate.school_id
        if certificate.certificate_name is not None:
            db_certificate.certificate_name = certificate.certificate_name
        if certificate.competition_name is not None:
            db_certificate.competition_name = certificate.competition_name
        if certificate.award_level is not None:
            db_certificate.award_level = certificate.award_level
        if certificate.award_year is not None:
            db_certificate.award_year = certificate.award_year
        if certificate.certificate_url is not None:
            db_certificate.certificate_url = certificate.certificate_url
        if certificate.issue_date is not None:
            db_certificate.issue_date = certificate.issue_date
        if certificate.certificate_no is not None:
            db_certificate.certificate_no = certificate.certificate_no
        db.commit()
        db.refresh(db_certificate)
    return db_certificate

def delete_certificate(db: Session, certificate_id: int):
    db_certificate = db.query(Certificate_Info).filter(Certificate_Info.certificate_id == certificate_id).first()
    if db_certificate:
        db.delete(db_certificate)
        db.commit()
    return db_certificate

# =================== Statistics ===================
def get_user_count(db: Session):
    """获取总用户数量"""
    return db.query(User).count()

def get_team_count(db: Session):
    """获取总队伍数量"""
    return db.query(Team).count()

def get_active_competition_count(db: Session):
    """获取进行中竞赛数量"""
    return db.query(Competition).filter(Competition.status == 1).count()

def get_pending_registration_count(db: Session):
    """获取待处理报名审核数量"""
    return db.query(Registration).filter(Registration.audit_status == 0).count()

def get_team_count_by_college(db: Session):
    """获取各学院队伍数量"""
    # 通过关联查询获取每个学院的队伍数量
    result = db.query(
        College.college_name,
        func.count(Team.team_id).label('team_count')
    ).join(
        User, User.college_id == College.college_id
    ).join(
        Team, Team.captain_id == User.user_id
    ).group_by(
        College.college_name
    ).all()
    
    return [(row.college_name, row.team_count) for row in result]

def get_problem_selection_count(db: Session):
    """获取各题目被选择次数"""
    # 查询每个题目的选择次数
    result = db.query(
        Problem.title,
        func.count(Work.work_id).label('selection_count')
    ).join(
        Work, Work.problem_id == Problem.problem_id
    ).group_by(
        Problem.title
    ).all()
    
    return [(row.title, row.selection_count) for row in result]

# =================== Team Problem ===================
def create_team_problem(db: Session, team_id: int, problem_id: int):
    """创建团队题目关联"""
    # 检查团队是否存在
    team = db.query(Team).filter(Team.team_id == team_id).first()
    if not team:
        raise ValueError("团队不存在")
    
    # 检查题目是否存在
    problem = db.query(Problem).filter(Problem.problem_id == problem_id).first()
    if not problem:
        raise ValueError("题目不存在")
    
    # 检查团队和题目是否属于同一竞赛
    if team.competition_id != problem.competition_id:
        raise ValueError("团队和题目不属于同一竞赛")
    
    # 检查是否已经选择了该题目
    existing = db.query(Team_Problem).filter(
        Team_Problem.team_id == team_id,
        Team_Problem.problem_id == problem_id,
        Team_Problem.competition_id == team.competition_id
    ).first()
    if existing:
        raise ValueError("团队已经选择了该题目")
    
    # 检查题目是否达到最多选择团队数
    if problem.max_teams > 0:
        current_team_count = db.query(Team_Problem).filter(
            Team_Problem.problem_id == problem_id,
            Team_Problem.competition_id == problem.competition_id
        ).count()
        if current_team_count >= problem.max_teams:
            raise ValueError("该题目已达到最多选择团队数")
    
    # 创建关联
    team_problem = Team_Problem(
        team_id=team_id,
        problem_id=problem_id,
        competition_id=team.competition_id,
        selection_time=dt.datetime.now()
    )
    
    db.add(team_problem)
    db.commit()
    db.refresh(team_problem)
    return team_problem

def get_team_problems(db: Session, team_id: Optional[int] = None, problem_id: Optional[int] = None, competition_id: Optional[int] = None):
    """获取团队题目关联"""
    query = db.query(Team_Problem)
    
    if team_id:
        query = query.filter(Team_Problem.team_id == team_id)
    if problem_id:
        query = query.filter(Team_Problem.problem_id == problem_id)
    if competition_id:
        query = query.filter(Team_Problem.competition_id == competition_id)
    
    return query.all()

def get_team_selected_problem(db: Session, team_id: int):
    """获取团队已选择的题目"""
    # 获取团队信息以获取competition_id
    team = db.query(Team).filter(Team.team_id == team_id).first()
    if not team:
        return None
    
    team_problem = db.query(Team_Problem).filter(
        Team_Problem.team_id == team_id,
        Team_Problem.competition_id == team.competition_id
    ).first()
    if not team_problem:
        return None
    
    # 获取完整的题目信息
    problem = db.query(Problem).filter(Problem.problem_id == team_problem.problem_id).first()
    return problem