<template>
  <div class="login-page">
    <div class="login-background">
      <div class="background-pattern"></div>
      <div class="background-overlay"></div>
    </div>
    <div class="login-container">
      <div class="login-box fade-in">
        <div class="login-header">
          <div class="logo-section">
            <h2 class="login-title">竞赛管理系统</h2>
            <p class="login-subtitle">专业的数学建模竞赛平台</p>
          </div>
        </div>
        <form @submit.prevent="handleLogin" class="login-form">
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="username" 
                type="text" 
                placeholder="请输入用户名" 
                required 
                autocomplete="username"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="password" 
                type="password" 
                placeholder="请输入密码" 
                required 
                autocomplete="current-password"
                class="form-input"
              />
            </div>
          </div>
          <div class="form-options">
            <label class="remember-me">
              <input type="checkbox" v-model="rememberMe">
              <span>记住我</span>
            </label>
            <a href="#" class="forgot-password">忘记密码？</a>
          </div>
          <button type="submit" class="login-btn" :disabled="loading">
            <div class="btn-content">
              <span v-if="loading" class="loading-spinner"></span>
              <span v-if="loading">登录中...</span>
              <span v-else>立即登录</span>
            </div>
          </button>
        </form>
        
        <div class="register-section">
          <p class="register-text">
            还没有账号？
            <router-link to="/register" class="register-link">立即注册</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { authApi } from '../api/auth.js';
import { useRouter } from 'vue-router';
import { useUserStore } from '../store/user.js';
import { showError, showSuccess } from '../utils/notification.js';

const router = useRouter();
const store = useUserStore();

// 初始化表单数据
const username = ref('');
const password = ref('');
const rememberMe = ref(false);
const loading = ref(false);

const handleLogin = async () => {
  // 表单验证
  if (!username.value.trim()) {
    showError('请输入用户名');
    return;
  }
  if (!password.value.trim()) {
    showError('请输入密码');
    return;
  }
  
  try {
    loading.value = true;
    
    // 调用登录API
    const res = await authApi.login(username.value.trim(), password.value.trim());
    
    console.log('登录响应:', res);  // 调试用
    
    // 处理响应数据（后端返回格式：{ code: 200, message: "...", data: {...} }）
    // API拦截器对登录接口返回整个data对象，包含code、message、data字段
    let userData = null;
    if (res && res.code === 200 && res.data && res.data.user_id) {
      // 标准格式：{ code: 200, data: {...user_data...} }
      userData = res.data;
    } else if (res && res.user_id) {
      // 直接返回用户数据（兼容）
      userData = res;
    } else if (res && res.data && typeof res.data === 'object') {
      // 其他格式，直接使用res.data
      userData = res.data;
    }
    
    console.log('提取的用户数据:', userData);  // 调试用
    
    if (userData && userData.user_id) {
      // 保存用户信息
      store.setUser(userData);
      
      // 根据角色跳转到对应页面
      const role = userData.role || (userData.user_type === 1 ? '学生' : userData.user_type === 2 ? '竞赛管理员' : userData.user_type === 3 ? '教师' : userData.user_type === 0 ? '超级管理员' : '');
      if (role === '学生' || userData.user_type === 1) {
        router.push('/student/dashboard');
      } else if (role === '教师' || userData.user_type === 3) {
        router.push('/teacher/dashboard');
      } else if (role === '竞赛管理员' || userData.user_type === 2) {
        router.push('/competition-admin/dashboard');
      } else if (role === '管理员' || role === '超级管理员' || userData.user_type === 0) {
        router.push('/super-admin/dashboard');
      } else {
        router.push('/dashboard');
      }
      
      showSuccess('登录成功');
    } else {
      console.error('登录响应数据格式错误:', res);
      const errorMsg = '登录响应数据格式错误，请检查后端返回';
      showError(errorMsg);
      throw new Error(errorMsg);
    }
  } catch (err) {
    console.error('登录失败：', err);
    const errorMsg = err.response?.data?.detail || err.response?.data?.message || err.message || '登录失败，请检查用户名和密码';
    showError(errorMsg);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.login-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
}

.background-pattern {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 1;
}

.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(224, 234, 252, 0.95) 0%, rgba(207, 222, 243, 0.95) 100%);
  backdrop-filter: blur(2px);
}

.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4rem;
  max-width: 1200px;
  width: 100%;
  padding: 2rem;
  position: relative;
  z-index: 10;
}

.login-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 3rem;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
  min-width: 400px;
  max-width: 450px;
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.logo-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  font-size: 3rem;
  animation: float 3s ease-in-out infinite;
}

.login-title {
  font-size: 2rem;
  font-weight: 700;
  color: #2d3748;
  margin: 0;
}

.login-subtitle {
  font-size: 1rem;
  color: #718096;
  margin: 0;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.input-group {
  margin: 0;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.form-input {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1rem;
  background: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
  outline: none;
}

.form-input:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  background: rgba(255, 255, 255, 0.95);
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0.5rem 0;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  color: #4a5568;
  font-size: 0.9rem;
}

.remember-me input[type="checkbox"] {
  accent-color: #667eea;
}

.forgot-password {
  color: #667eea;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.2s;
}

.forgot-password:hover {
  color: #5a67d8;
}

.login-btn {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1rem;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.loading-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.error-message {
  background: rgba(254, 226, 226, 0.9);
  border: 1px solid #feb2b2;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  margin-top: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #c53030;
  font-size: 0.9rem;
}

.register-section {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e2e8f0;
}

.register-text {
  color: #718096;
  margin: 0;
  font-size: 0.95rem;
}

.register-link {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  margin-left: 0.5rem;
  transition: color 0.2s;
}

.register-link:hover {
  color: #5a67d8;
}

.feature-showcase {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  color: white;
  max-width: 300px;
}

.feature-item {
  text-align: center;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: transform 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.feature-item h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: white;
}

.feature-item p {
  font-size: 0.9rem;
  opacity: 0.9;
  margin: 0;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in {
  animation: fadeIn 0.6s ease-out;
}

/* 响应式设计 - 统一断点设置 */
/* 大屏幕 (1200px及以上) */
@media (min-width: 1200px) {
  .login-container {
    gap: 6rem;
    max-width: 1400px;
  }
  
  .login-box {
    padding: 3.5rem;
    min-width: 450px;
    max-width: 500px;
  }
  
  .feature-showcase {
    max-width: 400px;
  }
  
  .feature-item {
    padding: 2rem;
  }
}

/* 平板横屏 (992px-1199px) */
@media (max-width: 1199px) and (min-width: 992px) {
  .login-container {
    gap: 3rem;
  }
  
  .login-box {
    padding: 2.8rem;
    min-width: 420px;
  }
  
  .feature-showcase {
    max-width: 350px;
  }
  
  .feature-item {
    padding: 1.8rem;
  }
}

/* 平板 (768px-991px) */
@media (max-width: 991px) and (min-width: 768px) {
  .login-container {
    flex-direction: column;
    gap: 2.5rem;
    padding: 1.5rem;
  }
  
  .feature-showcase {
    flex-direction: row;
    max-width: 700px;
  }
  
  .feature-item {
    flex: 1;
    padding: 1.5rem;
  }
  
  .login-box {
    padding: 2.5rem;
    min-width: 380px;
  }
  
  .login-title {
    font-size: 1.8rem;
  }
}

/* 手机横屏 (576px-767px) */
@media (max-width: 767px) and (min-width: 576px) {
  .login-container {
    flex-direction: column;
    gap: 2rem;
    padding: 1rem;
  }
  
  .feature-showcase {
    flex-direction: row;
    max-width: 500px;
    gap: 1.5rem;
  }
  
  .feature-item {
    flex: 1;
    padding: 1.2rem;
  }
  
  .login-box {
    padding: 2rem;
    min-width: auto;
    width: 100%;
    max-width: 450px;
  }
  
  .login-title {
    font-size: 1.6rem;
  }
  
  .form-input {
    padding: 0.9rem 0.9rem 0.9rem 2.8rem;
    font-size: 0.95rem;
  }
  
  .login-btn {
    padding: 0.9rem;
    font-size: 1rem;
  }
}

/* 手机竖屏 (575px及以下) */
@media (max-width: 575px) {
  .login-container {
    padding: 0.8rem;
    gap: 1.5rem;
  }
  
  .login-box {
    padding: 1.8rem 1.5rem;
    min-width: auto;
    width: 100%;
    max-width: 400px;
    border-radius: 16px;
  }
  
  .login-title {
    font-size: 1.5rem;
  }
  
  .login-subtitle {
    font-size: 0.9rem;
  }
  
  .logo-icon {
    font-size: 2.5rem;
  }
  
  .form-input {
    padding: 0.8rem 0.8rem 0.8rem 2.5rem;
    font-size: 0.9rem;
  }
  
  .input-icon {
    left: 0.8rem;
    font-size: 1.1rem;
  }
  
  .remember-me {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .remember-me span {
    font-size: 0.85rem;
  }
  
  .forgot-password {
    font-size: 0.85rem;
  }
  
  .login-btn {
    padding: 0.85rem;
    font-size: 0.95rem;
  }
  
  .feature-showcase {
    max-width: 320px;
    gap: 1rem;
  }
  
  .feature-item {
    padding: 1rem;
  }
  
  .feature-icon {
    font-size: 2rem;
    margin-bottom: 0.8rem;
  }
  
  .feature-item h3 {
    font-size: 1rem;
    margin-bottom: 0.4rem;
  }
  
  .feature-item p {
    font-size: 0.8rem;
  }
}

/* 超小屏幕优化 (400px及以下) */
@media (max-width: 400px) {
  .login-container {
    padding: 0.5rem;
  }
  
  .login-box {
    padding: 1.5rem 1.2rem;
    border-radius: 12px;
  }
  
  .login-title {
    font-size: 1.3rem;
  }
  
  .logo-icon {
    font-size: 2.2rem;
  }
  
  .form-input {
    padding: 0.75rem 0.75rem 0.75rem 2.3rem;
    font-size: 0.85rem;
  }
  
  .login-btn {
    padding: 0.8rem;
    font-size: 0.9rem;
  }
  
  .feature-item {
    padding: 0.8rem;
  }
}

@media (max-width: 768px) {
  .login-container {
    padding: 1rem;
  }
  
  .login-box {
    padding: 2rem 1.5rem;
    min-width: auto;
    width: 100%;
    max-width: 400px;
  }
  
  .login-title {
    font-size: 1.5rem;
  }
  
  .feature-showcase {
    flex-direction: column;
    max-width: 300px;
  }
  
  .form-options {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .login-box {
    padding: 1.5rem 1rem;
  }
  
  .form-input {
    padding: 0.875rem 0.875rem 0.875rem 2.5rem;
  }
  
  .input-icon {
    left: 0.75rem;
  }
}
</style>