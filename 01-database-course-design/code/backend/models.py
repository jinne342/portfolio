# backend/models.py
from sqlalchemy import (Column, Integer, String, ForeignKey, DateTime,
    DECIMAL, Text, SmallInteger, UniqueConstraint, CheckConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime as dt
import os

# SQLite兼容性配置
DB_TYPE = os.getenv("DB_TYPE", "sqlite").lower()

Base = declarative_base()

# 1. User表（完全匹配数据库结构）
class User(Base):
    __tablename__ = "User"
    user_id = Column(String(11), primary_key=True, index=True)
    user_name = Column(String(50), nullable=False)  # 对应数据库user_name
    password = Column(String(255), nullable=False)  # 匹配SQL中的NVARCHAR(255)
    phone = Column(String(20), nullable=True)
    email = Column(String(50), unique=True, nullable=True)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=True)
    college_id = Column(Integer, ForeignKey("College.college_id", ondelete="NO ACTION"), nullable=True)
    major_id = Column(Integer, ForeignKey("Major.major_id", ondelete="NO ACTION"), nullable=True)
    grade = Column(String(20), nullable=True)
    user_type = Column(SmallInteger, default=1, nullable=False)  # 对应TINYINT
    status = Column(SmallInteger, default=1, nullable=False)
    create_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    update_time = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)


# 2. Role表
class Role(Base):
    __tablename__ = "Role"
    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200), nullable=True)


# 3. Permission表
class Permission(Base):
    __tablename__ = "Permission"
    perm_id = Column(Integer, primary_key=True, index=True)
    perm_name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200), nullable=True)


# 4. User_Role表
class User_Role(Base):
    __tablename__ = "User_Role"
    user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), primary_key=True)
    role_id = Column(Integer, ForeignKey("Role.role_id", ondelete="NO ACTION"), primary_key=True)


# 5. Role_Permission表
class Role_Permission(Base):
    __tablename__ = "Role_Permission"
    role_id = Column(Integer, ForeignKey("Role.role_id", ondelete="NO ACTION"), primary_key=True)
    perm_id = Column(Integer, ForeignKey("Permission.perm_id", ondelete="NO ACTION"), primary_key=True)


# 6. School表（匹配SQL文件）
class School(Base):
    __tablename__ = "School"
    school_id = Column(Integer, primary_key=True, index=True)
    school_code = Column(String(30), unique=True, nullable=False)
    school_name = Column(String(100), unique=True, nullable=False)
    status = Column(SmallInteger, default=1)
    create_time = Column(DateTime, default=dt.datetime.now)



# 8. College表（匹配SQL文件，有school_id字段）
class College(Base):
    __tablename__ = "College"
    college_id = Column(Integer, primary_key=True, index=True)
    college_name = Column(String(100), nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=False)
    __table_args__ = (UniqueConstraint('college_name', 'school_id', name='uq_college_name_school'),)


# 9. Major表（匹配SQL文件）
class Major(Base):
    __tablename__ = "Major"
    major_id = Column(Integer, primary_key=True, index=True)
    major_name = Column(String(100), nullable=False)
    college_id = Column(Integer, ForeignKey("College.college_id", ondelete="NO ACTION"), nullable=False)
    __table_args__ = (UniqueConstraint('major_name', 'college_id', name='uq_major_name_college'),)


# 10. Competition表（匹配SQL文件，添加school_id）
class Competition(Base):
    __tablename__ = "Competition"
    competition_id = Column(Integer, primary_key=True, index=True)
    competition_name = Column(String(100), nullable=False)
    session_no = Column(String(20), unique=True, nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=True)
    sign_start = Column(DateTime, nullable=False)
    sign_end = Column(DateTime, nullable=False)
    competition_start = Column(DateTime, nullable=True)
    competition_end = Column(DateTime, nullable=True)
    fee_amount = Column(DECIMAL(10, 2), default=0)
    reward_rule = Column(String(500), nullable=True)
    status = Column(SmallInteger, default=1, nullable=False)
    create_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 10. Registration表
class Registration(Base):
    __tablename__ = "Registration"
    reg_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), nullable=False)
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), nullable=True)
    registration_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    fee_status = Column(SmallInteger, default=0)
    payment_method = Column(String(50), nullable=True)
    payment_time = Column(DateTime, nullable=True)
    audit_status = Column(SmallInteger, default=0)
    audit_remark = Column(String(500), nullable=True)
    __table_args__ = (UniqueConstraint('user_id', 'competition_id', name='uq_registration_user_competition'),)


# 13. Team表（匹配SQL文件，添加school_id，status改为TINYINT，添加teacher_user_id）
class Team(Base):
    __tablename__ = "Team"
    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String(100), unique=True, nullable=False)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=False)
    captain_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    teacher_user_id = Column(String(20), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=True)
    create_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    update_time = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)
    status = Column(SmallInteger, default=0)  # 匹配SQL中的TINYINT DEFAULT 0


# 12. Team_Member表
class Team_Member(Base):
    __tablename__ = "Team_Member"
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), primary_key=True)
    user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), primary_key=True)
    join_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 15. Team_Invite表（队伍邀请表）
class Team_Invite(Base):
    __tablename__ = "Team_Invite"
    invite_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), nullable=False)
    from_user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    to_user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    status = Column(SmallInteger, default=0, nullable=False)  # 0: 待处理, 1: 已接受, 2: 已拒绝
    create_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    __table_args__ = (UniqueConstraint('team_id', 'to_user_id', name='uq_team_invite_to_user'),)


# 13. Problem表
class Problem(Base):
    __tablename__ = "Problem"
    problem_id = Column(Integer, primary_key=True, index=True)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    file_url = Column(String(500), nullable=True)
    max_teams = Column(Integer, default=0)


# 14. Team_Problem表
class Team_Problem(Base):
    __tablename__ = "Team_Problem"
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), primary_key=True)
    problem_id = Column(Integer, ForeignKey("Problem.problem_id", ondelete="NO ACTION"), primary_key=True)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), primary_key=True)
    selection_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 15. Work表（合并Submission和Review表）
class Work(Base):
    __tablename__ = "Work"
    work_id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), nullable=False)
    problem_id = Column(Integer, ForeignKey("Problem.problem_id", ondelete="NO ACTION"), nullable=False)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), nullable=False)
    teacher_user_id = Column(String(20), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=True)
    file_url = Column(String(500), nullable=False)
    submit_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    version = Column(Integer, default=1, nullable=False)
    score = Column(DECIMAL(5, 2), nullable=True)
    review_user_id = Column(String(20), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=True)
    review_comment = Column(Text, nullable=True)
    review_time = Column(DateTime, nullable=True)
    is_reviewed = Column(SmallInteger, default=0, nullable=False)
    __table_args__ = (
        CheckConstraint('score BETWEEN 0 AND 100'),
    )


# 17. Award表（匹配SQL文件，添加school_id和唯一约束）
class Award(Base):
    __tablename__ = "Award"
    award_id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), nullable=False)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=False)
    award_name = Column(String(50), nullable=False)
    award_rank = Column(Integer, nullable=True)
    __table_args__ = (UniqueConstraint('team_id', 'competition_id', name='uq_award_team_competition'),)


# 18. Teacher表（匹配SQL文件，添加school_id和college_id）
class Teacher(Base):
    __tablename__ = "Teacher"
    teacher_id = Column(Integer, primary_key=True, index=True)
    teacher_no = Column(String(20), unique=True, nullable=False)
    teacher_name = Column(String(50), nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=False)
    college_id = Column(Integer, ForeignKey("College.college_id", ondelete="NO ACTION"), nullable=False)
    research_field = Column(String(200), nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(50), nullable=True)
    max_guide_teams = Column(Integer, default=3)
    current_guide_teams = Column(Integer, default=0)
    status = Column(SmallInteger, default=1)
    create_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    update_time = Column(DateTime, default=dt.datetime.now, onupdate=dt.datetime.now, nullable=False)


# 19. Teacher_Team表
class Teacher_Team(Base):
    __tablename__ = "Teacher_Team"
    user_id = Column(String(20), ForeignKey("User.user_id", ondelete="NO ACTION"), primary_key=True)
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), primary_key=True)
    assign_method = Column(String(50), nullable=True)
    confirm_status = Column(SmallInteger, default=0)
    assign_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 20. Announcement表
class Announcement(Base):
    __tablename__ = "Announcement"
    announcement_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    create_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 21. Message表
class Message(Base):
    __tablename__ = "Message"
    message_id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=True)
    receiver_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(SmallInteger, default=0)
    send_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 22. File_Resource表
class File_Resource(Base):
    __tablename__ = "File_Resource"
    file_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    category = Column(String(50), nullable=True)
    sub_category = Column(String(50), nullable=True)
    file_url = Column(String(500), nullable=False)
    view_count = Column(Integer, default=0)
    upload_time = Column(DateTime, default=dt.datetime.now, nullable=False)


# 23. User_Import_Log表
class User_Import_Log(Base):
    __tablename__ = "User_Import_Log"
    import_id = Column(Integer, primary_key=True, index=True)
    operator_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    import_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    file_name = Column(String(200), nullable=False)
    success_count = Column(Integer, default=0)
    fail_count = Column(Integer, default=0)


# 24. Violation_Record表（匹配SQL文件，添加school_id和handle_user_id，submission_id改为work_id）
class Violation_Record(Base):
    __tablename__ = "Violation_Record"
    violation_id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("Team.team_id", ondelete="NO ACTION"), nullable=False)
    work_id = Column(Integer, ForeignKey("Work.work_id", ondelete="NO ACTION"), nullable=False)
    competition_id = Column(Integer, ForeignKey("Competition.competition_id", ondelete="NO ACTION"), nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=False)
    violation_type = Column(String(50), nullable=False)
    violation_detail = Column(Text, nullable=False)
    is_approved = Column(SmallInteger, default=0, nullable=False)
    handle_user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=True)
    handle_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    
    team = relationship("Team", backref="violations")
    competition = relationship("Competition", backref="violations")


# 25. Certificate_Info表（匹配SQL文件，添加school_id）
class Certificate_Info(Base):
    __tablename__ = "Certificate_Info"
    certificate_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(11), ForeignKey("User.user_id", ondelete="NO ACTION"), nullable=False)
    school_id = Column(Integer, ForeignKey("School.school_id", ondelete="NO ACTION"), nullable=False)
    certificate_name = Column(String(200), nullable=False)
    competition_name = Column(String(100), nullable=True)
    award_level = Column(String(50), nullable=True)
    award_year = Column(Integer, nullable=True)
    certificate_url = Column(String(500), nullable=True)
    upload_time = Column(DateTime, default=dt.datetime.now, nullable=False)
    issue_date = Column(DateTime, default=dt.datetime.now, nullable=False)
    certificate_no = Column(String(50), nullable=True)
    __table_args__ = (
        # 匹配数据库中的CHECK约束
        CheckConstraint('award_year > 2000'),
    )