import { request } from './index';

// 获取违规记录列表
export function getViolationList(params = {}) {
  return request.get('/violations/', { params });
}

// 创建违规记录
export function createViolation(data) {
  return request.post('/violations/', data);
}

// 获取违规记录详情
export function getViolationDetail(id) {
  return request.get(`/violations/${id}/`);
}

// 更新违规记录
export function updateViolation(id, data) {
  return request.put(`/violations/${id}/`, data);
}

// 删除违规记录
export function deleteViolation(id) {
  return request.delete(`/violations/${id}/`);
}
