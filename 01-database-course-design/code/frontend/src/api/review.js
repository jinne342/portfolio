import request from './index';

// 创建评审
export function createReview(data) {
  return request.post('/reviews/', data);
}

// 获取评审列表
export function getReviews(params = {}) {
  return request.get('/reviews/', { params });
}

// 获取评审详情
export function getReviewDetail(reviewId) {
  return request.get(`/reviews/${reviewId}/`);
}

// 更新评审
export function updateReview(reviewId, data) {
  return request.put(`/reviews/${reviewId}/`, data);
}

// 删除评审
export function deleteReview(reviewId) {
  return request.delete(`/reviews/${reviewId}/`);
}

// 获取评审员的评审列表
export function getReviewerReviews(reviewerId) {
  return request.get('/reviews/', { params: { reviewer_id: reviewerId } });
}

// 获取提交的评审列表
export function getSubmissionReviews(submissionId) {
  return request.get('/reviews/', { params: { submission_id: submissionId } });
}
