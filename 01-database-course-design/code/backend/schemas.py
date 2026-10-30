# backend/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, Union
from datetime import datetime



# =================== College ===================
class CollegeBase(BaseModel):
    college_name: str
    school_id: int

class CollegeCreate(CollegeBase):
    pass

class CollegeUpdate(BaseModel):
    college_name: Optional[str] = None
    school_id: Optional[int] = None

class CollegeOut(CollegeBase):
    college_id: int
    class Config:
        orm_mode = True

# =================== Role ===================
class RoleBase(BaseModel):
    role_name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    role_name: Optional[str] = None
    description: Optional[str] = None

class RoleOut(RoleBase):
    role_id: int
    class Config:
        orm_mode = True

# =================== Permission ===================
class PermissionBase(BaseModel):
    perm_name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class PermissionUpdate(BaseModel):
    perm_name: Optional[str] = None
    description: Optional[str] = None

class PermissionOut(PermissionBase):
    perm_id: int
    class Config:
        orm_mode = True

# =================== User_Role ===================
class UserRoleBase(BaseModel):
    user_id: str
    role_id: int

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleOut(UserRoleBase):
    class Config:
        orm_mode = True

# =================== Role_Permission ===================
class RolePermissionBase(BaseModel):
    role_id: int
    perm_id: int

class RolePermissionCreate(RolePermissionBase):
    pass

class RolePermissionOut(RolePermissionBase):
    class Config:
        orm_mode = True

# =================== User ===================
class UserBase(BaseModel):
    user_id: str  # 添加user_id字段作为主键
    user_name: str
    email: Optional[EmailStr] = None

class UserCreate(UserBase):
    password: str
    phone: Optional[str] = None
    school_id: Optional[int] = None
    college_id: Optional[int] = None
    major_id: Optional[int] = None
    grade: Optional[str] = None
    user_type: int = 1  # 默认学生

class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    school_id: Optional[int] = None
    college_id: Optional[int] = None
    major_id: Optional[int] = None
    grade: Optional[str] = None
    user_type: Optional[int] = None
    status: Optional[int] = None

class UserOut(UserBase):
    user_id: str
    phone: Optional[str] = None
    school_id: Optional[int] = None
    college_id: Optional[int] = None
    major_id: Optional[int] = None
    grade: Optional[str] = None
    user_type: int
    status: int
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    class Config:
        orm_mode = True
        from_attributes = True  # 兼容Pydantic v2

# =================== Team ===================
class TeamBase(BaseModel):
    team_name: str
    competition_id: int
    school_id: int
    captain_id: str  # 11位字符串user_id
    status: Optional[int] = 0

class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    team_name: Optional[str] = None
    competition_id: Optional[int] = None
    school_id: Optional[int] = None
    captain_id: Optional[str] = None  # 11位字符串user_id
    status: Optional[Union[str, int]] = None

class TeamOut(TeamBase):
    team_id: int
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Team_Member ===================
class TeamMemberBase(BaseModel):
    team_id: int
    user_id: str

class TeamMemberCreate(TeamMemberBase):
    pass

class TeamMemberOut(TeamMemberBase):
    join_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Team_Invite ===================
class TeamInviteBase(BaseModel):
    team_id: int
    to_user_id: str

class TeamInviteCreate(TeamInviteBase):
    pass

class TeamInviteUpdate(BaseModel):
    status: int

class TeamInviteOut(TeamInviteBase):
    invite_id: int
    status: int
    create_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Problem ===================
class ProblemBase(BaseModel):
    title: str
    description: Optional[str] = None
    file_url: Optional[str] = None
    max_teams: Optional[int] = 0

class ProblemCreate(ProblemBase):
    competition_id: int

class ProblemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    file_url: Optional[str] = None
    max_teams: Optional[int] = None

class ProblemOut(ProblemBase):
    problem_id: int
    competition_id: int
    class Config:
        orm_mode = True

# =================== Submission ===================
class WorkBase(BaseModel):
    team_id: int
    problem_id: int
    teacher_user_id: Optional[str] = None
    file_url: Optional[str]
    version: Optional[int] = 1
    score: Optional[float] = None
    review_user_id: Optional[str] = None
    review_comment: Optional[str] = None
    is_reviewed: Optional[int] = 0

class WorkCreate(WorkBase):
    pass

class WorkUpdate(BaseModel):
    teacher_user_id: Optional[str] = None
    file_url: Optional[str] = None
    version: Optional[int] = None
    score: Optional[float] = None
    review_user_id: Optional[str] = None
    review_comment: Optional[str] = None
    review_time: Optional[datetime] = None
    is_reviewed: Optional[int] = None

class WorkOut(WorkBase):
    work_id: int
    competition_id: int
    submit_time: Optional[datetime] = None
    review_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Message ===================
class MessageBase(BaseModel):
    sender_id: Optional[str] = None
    receiver_id: str
    content: str
    send_time: Optional[datetime] = None

class MessageCreate(MessageBase):
    pass

class MessageUpdate(BaseModel):
    sender_id: Optional[int] = None
    receiver_id: Optional[int] = None
    content: Optional[str] = None
    status: Optional[Union[str, int]] = None

class MessageOut(MessageBase):
    message_id: int
    class Config:
        orm_mode = True

# =================== Announcement ===================
class AnnouncementBase(BaseModel):
    title: str
    content: str
    post_time: Optional[datetime] = None

class AnnouncementCreate(AnnouncementBase):
    pass

class AnnouncementUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class AnnouncementOut(AnnouncementBase):
    announcement_id: int
    class Config:
        orm_mode = True

# =================== Violation_Record ===================
class ViolationBase(BaseModel):
    team_id: int
    work_id: int
    competition_id: int
    school_id: int
    violation_type: str
    violation_detail: str
    is_approved: Optional[int] = 0

class ViolationCreate(ViolationBase):
    pass

class ViolationOut(ViolationBase):
    violation_id: int
    handle_time: Optional[datetime] = None
    class Config:
        orm_mode = True

class ViolationUpdate(BaseModel):
    violation_type: Optional[str] = None
    violation_detail: Optional[str] = None
    is_approved: Optional[int] = None
    handle_time: Optional[datetime] = None

# =================== Award ===================
class AwardBase(BaseModel):
    team_id: int
    competition_id: int
    school_id: int
    award_name: str
    award_rank: Optional[int] = None

class AwardCreate(AwardBase):
    pass

class AwardUpdate(BaseModel):
    team_id: Optional[int] = None
    competition_id: Optional[int] = None
    school_id: Optional[int] = None
    award_name: Optional[str] = None
    award_rank: Optional[int] = None

class AwardOut(AwardBase):
    award_id: int
    class Config:
        orm_mode = True

# =================== Certificate_Info ===================
class CertificateBase(BaseModel):
    user_id: str
    school_id: int
    certificate_name: str
    competition_name: Optional[str] = None
    award_level: Optional[str] = None
    award_year: Optional[int] = None
    certificate_url: Optional[str] = None
    issue_date: Optional[datetime] = None
    certificate_no: Optional[str] = None

class CertificateCreate(CertificateBase):
    pass

class CertificateUpdate(BaseModel):
    school_id: Optional[int] = None
    certificate_name: Optional[str] = None
    competition_name: Optional[str] = None
    award_level: Optional[str] = None
    award_year: Optional[int] = None
    certificate_url: Optional[str] = None
    issue_date: Optional[datetime] = None
    certificate_no: Optional[str] = None

class CertificateOut(CertificateBase):
    certificate_id: int
    upload_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Competition ===================
class CompetitionBase(BaseModel):
    competition_name: str
    session_no: str
    school_id: Optional[int] = None
    sign_start: datetime
    sign_end: datetime
    competition_start: Optional[datetime] = None
    competition_end: Optional[datetime] = None
    fee_amount: Optional[float] = 0.0
    reward_rule: Optional[str] = None
    status: Optional[int] = 1

class CompetitionCreate(CompetitionBase):
    pass

class CompetitionUpdate(BaseModel):
    competition_name: Optional[str] = None
    session_no: Optional[str] = None
    school_id: Optional[int] = None
    sign_start: Optional[datetime] = None
    sign_end: Optional[datetime] = None
    competition_start: Optional[datetime] = None
    competition_end: Optional[datetime] = None
    fee_amount: Optional[float] = None
    reward_rule: Optional[str] = None
    status: Optional[Union[str, int]] = None

class CompetitionOut(CompetitionBase):
    competition_id: int
    create_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Registration ===================
class RegistrationBase(BaseModel):
    user_id: str
    competition_id: int
    team_id: Optional[int]
    fee_status: Optional[int] = 0  # 0: 未缴费, 1: 已缴费
    payment_method: Optional[str] = None
    payment_time: Optional[datetime] = None
    audit_status: Optional[int] = 0  # 0: 待审核, 1: 通过, 2: 驳回

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    fee_status: Optional[int] = None
    payment_method: Optional[str] = None
    payment_time: Optional[datetime] = None
    audit_status: Optional[int] = None
    audit_remark: Optional[str] = None

class RegistrationOut(RegistrationBase):
    reg_id: int
    registration_time: Optional[datetime] = None
    audit_remark: Optional[str] = None
    class Config:
        orm_mode = True

# =================== Teacher ===================
class TeacherBase(BaseModel):
    teacher_no: str
    teacher_name: str
    school_id: int
    college_id: int
    research_field: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    max_guide_teams: Optional[int] = 3
    current_guide_teams: Optional[int] = 0
    status: Optional[int] = 1

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(BaseModel):
    teacher_name: Optional[str] = None
    school_id: Optional[int] = None
    college_id: Optional[int] = None
    research_field: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    max_guide_teams: Optional[int] = None
    current_guide_teams: Optional[int] = None
    status: Optional[int] = None

class TeacherOut(TeacherBase):
    teacher_id: int
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Teacher_Team ===================
class TeacherTeamBase(BaseModel):
    user_id: str
    team_id: int
    assign_method: Optional[str] = None
    confirm_status: Optional[int] = 0

class TeacherTeamCreate(TeacherTeamBase):
    pass

class TeacherTeamUpdate(BaseModel):
    assign_method: Optional[str] = None
    confirm_status: Optional[Union[str, int]] = None

class TeacherTeamOut(TeacherTeamBase):
    assign_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== School ===================
class SchoolBase(BaseModel):
    school_code: str
    school_name: str
    status: Optional[int] = 1

class SchoolCreate(SchoolBase):
    pass

class SchoolUpdate(BaseModel):
    school_code: Optional[str] = None
    school_name: Optional[str] = None
    status: Optional[int] = None

class SchoolOut(SchoolBase):
    school_id: int
    create_time: Optional[datetime] = None
    class Config:
        orm_mode = True

# =================== Major ===================
class MajorBase(BaseModel):
    major_name: str
    college_id: int

class MajorCreate(MajorBase):
    pass

class MajorUpdate(BaseModel):
    major_name: Optional[str] = None
    college_id: Optional[int] = None

class MajorOut(MajorBase):
    major_id: int
    class Config:
        orm_mode = True

# =================== User_Import_Log ===================
class UserImportLogBase(BaseModel):
    operator_id: str
    file_name: str
    success_count: Optional[int] = 0
    fail_count: Optional[int] = 0

class UserImportLogCreate(UserImportLogBase):
    pass

class UserImportLogUpdate(BaseModel):
    operator_id: Optional[int] = None
    file_name: Optional[str] = None
    success_count: Optional[int] = None
    fail_count: Optional[int] = None

class UserImportLogOut(UserImportLogBase):
    import_id: int
    import_time: Optional[datetime] = None
    class Config:
        orm_mode = True
