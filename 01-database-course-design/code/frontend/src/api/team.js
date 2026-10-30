import request from './index';

export function getTeams(competitionId = null, userId = null) {
  const params = {};
  if (competitionId) params.competition_id = competitionId;
  if (userId) params.user_id = userId;
  return request.get('/teams/', { params });
}

export function getTeamById(id) {
  return request.get(`/teams/${id}/`);
}

export function createTeam(data) {
  return request.post('/teams/', data);
}

export function updateTeam(id, data) {
  return request.put(`/teams/${id}/`, data);
}

export function deleteTeam(id) {
  return request.delete(`/teams/${id}/`);
}

// 队伍成员管理
export function getTeamMembers(teamId) {
  return request.get(`/team-members/team/${teamId}/`);
}

export function addTeamMember(data) {
  return request.post('/team-members/', data);
}

export function removeTeamMember(teamId, userId) {
  return request.delete(`/team-members/?team_id=${teamId}&user_id=${userId}`);
}

// 队伍邀请管理
export function createTeamInvite(data) {
  return request.post('/team_invites/', data);
}

export function getTeamInvitesByUser(status = null) {
  const params = {};
  if (status !== null) params.status = status;
  return request.get('/team_invites/user/', { params });
}

export function handleTeamInvite(inviteId, data) {
  return request.put(`/team_invites/${inviteId}/`, data);
}

// 根据用户ID获取团队列表
export function getTeamsByUser(userId) {
  return getTeams(null, userId);
}