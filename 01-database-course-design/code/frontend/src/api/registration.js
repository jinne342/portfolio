import request from './index';

// 竞赛报名相关API
export function getRegistrations() {
  return request.get('/registrations/');
}

export function getRegistrationsByUser(userId) {
  return request.get(`/registrations/user/${userId}/`);
}

export function createRegistration(data) {
  return request.post('/registrations/', data);
}

export function getRegistrationById(id) {
  return request.get(`/registrations/${id}/`);
}

export function updateRegistration(id, data) {
  return request.put(`/registrations/${id}/`, data);
}

export function deleteRegistration(id) {
  return request.delete(`/registrations/${id}/`);
}
