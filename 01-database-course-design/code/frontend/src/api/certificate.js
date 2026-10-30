import request from './index';

// 获取证书列表
export function getCertificates(params = {}) {
  return request.get('/certificates/', { params });
}

// 获取证书详情
export function getCertificateDetail(certificateId) {
  return request.get(`/certificates/${certificateId}/`);
}

// 下载证书文件
export function downloadCertificate(certificateId) {
  return request.get(`/certificates/${certificateId}/download/`, { responseType: 'blob' });
}
