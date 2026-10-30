import request from './index';

export function getUsers() {
  return request.get('/users/');
}

export function getUserById(id) {
  return request.get(`/users/${id}/`);
}

export function updateUser(id, data) {
  return request.put(`/users/${id}/`, data);
}

export function deleteUser(id) {
  return request.delete(`/users/${id}/`);
}
