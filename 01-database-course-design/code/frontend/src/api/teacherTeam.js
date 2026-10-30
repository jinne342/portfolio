import request from './index';

// 获取教师指导的队伍列表
export function getTeacherTeams(teacherId) {
  return request.get('/teacher-teams/', {
    params: { user_id: teacherId }
  });
}

// 获取所有教师团队关联
export function getAllTeacherTeams() {
  return request.get('/teacher-teams/');
}

// 获取特定队伍的教师指导信息
export function getTeacherTeamsByTeam(teamId) {
  return request.get('/teacher-teams/', {
    params: { team_id: teamId }
  });
}

// 创建教师团队关联
export function createTeacherTeam(data) {
  return request.post('/teacher-teams/', data);
}

// 更新教师团队关联信息
export function updateTeacherTeam(userId, teamId, data) {
  return request.put(`/teacher-teams/${userId}/${teamId}/`, data);
}

// 删除教师团队关联
export function deleteTeacherTeam(userId, teamId) {
  return request.delete(`/teacher-teams/${userId}/${teamId}/`);
}

// 学生发送指导老师请求
export function studentRequestTeacherTeam(data) {
  return request.post('/teacher-teams/request/', data);
}

// 确认指导请求
export function confirmTeacherTeam(userId, teamId) {
  return updateTeacherTeam(userId, teamId, {
    confirm_status: 'confirmed'
  });
}

// 拒绝指导请求
export function rejectTeacherTeam(userId, teamId) {
  return updateTeacherTeam(userId, teamId, {
    confirm_status: 'rejected'
  });
}
