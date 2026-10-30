import request from './index';

// 题目相关API
export function getProblems() {
  return request.get('/problems/');
}

export function getProblemsByCompetition(competitionId) {
  return request.get(`/problems/?competition_id=${competitionId}`);
}

export function getProblemById(id) {
  return request.get(`/problems/${id}/`);
}

// 创建赛题
export function createProblem(data) {
  return request.post('/problems/', data);
}

// 更新赛题
export function updateProblem(problemId, data) {
  return request.put(`/problems/${problemId}/`, data);
}

// 删除赛题
export function deleteProblem(problemId) {
  return request.delete(`/problems/${problemId}/`);
}

export function selectProblem(problemId, teamId) {
  return request.post(`/problems/${problemId}/select/`, { team_id: teamId });
}

export function getSelectedProblem(teamId) {
  return request.get(`/teams/${teamId}/selected-problem/`);
}
