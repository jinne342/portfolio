import service from './index.js';

export const authApi = {
  // 登录（使用JSON格式）
  login(username, password) {
    return service.post('/auth/login', {
      username: username,
      password: password
    });
  },
  
  // 注册新用户
  register(userData) {
    return service.post('/auth/register', userData);
  },
  
  // 获取当前用户信息
  getCurrentUser() {
    return service.get('/auth/me');
  },
  
  // 登出
  logout() {
    return service.post('/auth/logout');
  },
  
  // 检查用户是否在线
  checkOnlineStatus() {
    return service.get('/auth/online-status');
  },
  
  // 更新会话活动时间
  updateSessionActivity() {
    return service.post('/auth/update-session');
  }
};
