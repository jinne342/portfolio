import request from './index';

// 竞赛管理
export function getCompetitions() {
  return request.get('/competitions/');
}

export function getCompetitionById(id) {
  return request.get(`/competitions/${id}/`);
}

export function createCompetition(data) {
  return request.post('/competitions/', data);
}

export function updateCompetition(id, data) {
  return request.put(`/competitions/${id}/`, data);
}

export function deleteCompetition(id) {
  return request.delete(`/competitions/${id}/`);
}

// 赛题管理
export function getProblems(competitionId = null) {
  const params = competitionId ? { competition_id: competitionId } : {};
  return request.get('/problems/', { params });
}

export function getProblemById(id) {
  return request.get(`/problems/${id}/`);
}

export function createProblem(data) {
  return request.post('/problems/', data);
}

export function updateProblem(id, data) {
  return request.put(`/problems/${id}/`, data);
}

export function deleteProblem(id) {
  return request.delete(`/problems/${id}/`);
}
