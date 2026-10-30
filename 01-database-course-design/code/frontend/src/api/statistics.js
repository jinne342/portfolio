import request from './index';

// 匹配后端统计接口
export function getUserCount() {
  return request.get('/statistics/user_count');
}

export function getTeamCount() {
  return request.get('/statistics/team_count');
}

export function getActiveCompetitionCount() {
  return request.get('/statistics/active_competition_count');
}

export function getPendingRegistrationCount() {
  return request.get('/statistics/pending_registration_count');
}

export function getTeamCountByCollege() {
  return request.get('/statistics/team_by_college');
}

export function getProblemSelectionCount() {
  return request.get('/statistics/problem_selection');
}