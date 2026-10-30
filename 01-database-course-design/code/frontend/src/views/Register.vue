<template>
  <div class="register-page">
    <div class="register-background">
      <div class="background-pattern"></div>
      <div class="background-overlay"></div>
    </div>
    <div class="register-container">
      <div class="register-box fade-in">
        <div class="register-header">
          <div class="logo-section">
            <h2 class="register-title">创建账户</h2>
            <p class="register-subtitle">加入数学建模竞赛大家庭</p>
          </div>
        </div>
        <form @submit.prevent="handleRegister" class="register-form">
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="form.user_id" 
                type="text" 
                placeholder="用户ID" 
                required 
                autocomplete="off"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="form.username" 
                type="text" 
                placeholder="用户名" 
                required 
                autocomplete="username"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="form.email" 
                type="email" 
                placeholder="邮箱地址（可选）" 
                autocomplete="email"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="form.phone" 
                type="tel" 
                placeholder="手机号码（可选）" 
                autocomplete="tel"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="form.password" 
                type="password" 
                placeholder="密码" 
                required 
                autocomplete="new-password"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input 
                v-model="form.confirmPassword" 
                type="password" 
                placeholder="确认密码" 
                required 
                autocomplete="new-password"
                class="form-input"
              />
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <select 
                v-model="form.user_type" 
                required 
                class="form-input form-select"
              >
                <option value="">选择用户类型</option>
                <option value="1">学生</option>
                <option value="2">教师</option>
                <option value="3">竞赛管理员</option>
              </select>
            </div>
          </div>
          <div class="form-agreement">
            <label class="agreement-checkbox">
              <input type="checkbox" v-model="agreeTerms" required>
              <span>我已阅读并同意 <a href="#" class="terms-link">用户协议</a> 和 <a href="#" class="terms-link">隐私政策</a></span>
            </label>
          </div>
          <button type="submit" class="register-btn" :disabled="loading || !agreeTerms">
            <div class="btn-content">
              <span v-if="loading" class="loading-spinner"></span>
              <span v-if="loading">注册中...</span>
              <span v-else>创建账户</span>
            </div>
          </button>
        </form>

        <div class="login-section">
          <p class="login-text">
            已有账户？
            <router-link to="/login" class="login-link">立即登录</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { showError, showSuccess } from '../utils/notification.js';
import { authApi } from '../api/auth.js';

const router = useRouter();

// 初始化表单数据
const form = reactive({
  user_id: '',
  username: '',
  password: '',
  confirmPassword: '',
  email: '',
  phone: '',
  user_type: ''
});

const agreeTerms = ref(false);
const loading = ref(false);

const handleRegister = async () => {
  // 简化表单验证
  if (!form.username.trim()) {
    showError('请输入用户名');
    return;
  }
  if (!form.password) {
    showError('请输入密码');
    return;
  }
  if (form.password !== form.confirmPassword) {
    showError('两次输入的密码不一致');
    return;
  }
  if (!form.user_type) {
    showError('请选择用户类型');
    return;
  }
  if (!agreeTerms.value) {
    showError('请先同意用户协议和隐私政策');
    return;
  }
  // 邮箱格式验证
  if (form.email.trim()) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(form.email.trim())) {
      showError('请输入有效的邮箱地址（如：example@domain.com）');
      return;
    }
  }
  
  try {
    loading.value = true;
    
    // 调用注册API - 移除邮箱必填检查
    const res = await authApi.register({
      user_id: form.user_id.trim(),
      user_name: form.username.trim(),
      password: form.password,
      email: form.email.trim() || null,  // 允许为空
      phone: form.phone.trim() || null,
      user_type: parseInt(form.user_type)
    });
    
    console.log('注册响应:', res);  
    
    if (res && res.code === 200) {
      showSuccess('注册成功！请登录');
      router.push('/login');
    } else {
      throw new Error(res?.message || '注册失败');
    }
    
  } catch (err) {
    console.error('注册错误:', err);
    showError(err.message || '注册失败，请稍后重试');
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.register-background {
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

.register-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4rem;
  max-width: 1400px;
  width: 100%;
  padding: 2rem;
  position: relative;
  z-index: 10;
}

.register-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 3rem;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
  min-width: 500px;
  max-width: 550px;
  max-height: 90vh;
  overflow-y: auto;
}

.register-header {
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

.register-title {
  font-size: 2rem;
  font-weight: 700;
  color: #2d3748;
  margin: 0;
}

.register-subtitle {
  font-size: 1rem;
  color: #718096;
  margin: 0;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
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
  border-color: #764ba2;
  box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.1);
  background: rgba(255, 255, 255, 0.95);
}

.form-select {
  cursor: pointer;
}

.form-agreement {
  margin: 1rem 0;
}

.agreement-checkbox {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  cursor: pointer;
  color: #4a5568;
  font-size: 0.9rem;
  line-height: 1.5;
}

.agreement-checkbox input[type="checkbox"] {
  accent-color: #764ba2;
  margin-top: 2px;
}

.terms-link {
  color: #764ba2;
  text-decoration: none;
  transition: color 0.2s;
}

.terms-link:hover {
  color: #5a3a82;
}

.register-btn {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1rem;
  box-shadow: 0 4px 15px rgba(118, 75, 162, 0.3);
}

.register-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(118, 75, 162, 0.4);
}

.register-btn:disabled {
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

.login-section {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid #e2e8f0;
}

.login-text {
  color: #718096;
  margin: 0;
  font-size: 0.95rem;
}

.login-link {
  color: #764ba2;
  text-decoration: none;
  font-weight: 600;
  margin-left: 0.5rem;
  transition: color 0.2s;
}

.login-link:hover {
  color: #5a3a82;
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

/* 响应式设计 */
@media (max-width: 1200px) {
  .register-container {
    flex-direction: column;
    gap: 2rem;
  }
  
  .feature-showcase.register-features {
    flex-direction: row;
    max-width: 600px;
  }
  
  .feature-item {
    flex: 1;
  }
}

@media (max-width: 768px) {
  .register-container {
    padding: 1rem;
  }
  
  .register-box {
    padding: 2rem 1.5rem;
    min-width: auto;
    width: 100%;
    max-width: 400px;
    max-height: none;
  }
  
  .register-title {
    font-size: 1.5rem;
  }
  
  .feature-showcase.register-features {
    flex-direction: column;
    max-width: 300px;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .register-box {
    padding: 1.5rem 1rem;
  }
  
  .form-input {
    padding: 0.875rem 0.875rem 0.875rem 2.5rem;
  }
  
  .input-icon {
    left: 0.75rem;
  }
  
  .agreement-checkbox {
    font-size: 0.85rem;
  }
}
</style>