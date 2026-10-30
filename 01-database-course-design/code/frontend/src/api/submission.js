import request from './index';

export function getSubmissions(teamId = null, problemId = null, userId = null, reviewed = null) {
  const params = {};
  if (teamId) params.team_id = teamId;
  if (problemId) params.problem_id = problemId;
  if (userId) params.user_id = userId;
  if (reviewed !== null) params.reviewed = reviewed;
  return request.get('/submissions/', { params });
}

export function getSubmissionById(id) {
  return request.get(`/submissions/${id}/`);
}

export function createSubmission(data) {
  return request.post('/submissions/', data);
}

export function updateSubmission(id, data) {
  return request.put(`/submissions/${id}/`, data);
}

export function deleteSubmission(id) {
  return request.delete(`/submissions/${id}/`);
}

// 下载提交文件
export function downloadSubmission(id) {
  return request.get(`/submissions/${id}/download/`, { responseType: 'blob' });
}
