import request from './index';

export function getWorks(teamId = null, problemId = null, userId = null, reviewed = null) {
  const params = {};
  if (teamId) params.team_id = teamId;
  if (problemId) params.problem_id = problemId;
  if (userId) params.user_id = userId;
  if (reviewed !== null) params.reviewed = reviewed;
  return request.get('/works/', { params });
}

export function getWorkById(id) {
  return request.get(`/works/${id}/`);
}

export function createWork(data) {
  return request.post('/works/', data);
}

export function updateWork(id, data) {
  return request.put(`/works/${id}/`, data);
}

export function deleteWork(id) {
  return request.delete(`/works/${id}/`);
}

export function reviewWork(id, data) {
  return request.post(`/works/${id}/review/`, data);
}

export function downloadWork(id) {
  return request.get(`/works/${id}/download/`, { responseType: 'blob' });
}
