<template>
  <header class="new-header">
    <div class="new-header-content">
      <div class="logo-section">
        <h1 class="logo">数学建模竞赛平台</h1>
      </div>
      <nav class="nav-menu">
        <router-link to="/" class="nav-item">首页</router-link>
        <router-link to="/competition-detail" class="nav-item">竞赛详情</router-link>
        <router-link to="/competition-news" class="nav-item">竞赛新闻</router-link>
        <router-link to="/organization-structure" class="nav-item">组织结构</router-link>
        <router-link to="/competition-time" class="nav-item">竞赛时间</router-link>
        <router-link to="/award-query" class="nav-item">获奖查询</router-link>
        <router-link to="/apply-cooperation" class="nav-item">申请协办</router-link>
        <router-link to="/past-reviews" class="nav-item">往届回顾</router-link>
        <router-link to="/feedback" class="nav-item">意见留言</router-link>
      </nav>
      <div class="auth-buttons">
        <router-link to="/register" class="btn-register">注册</router-link>
        <router-link to="/login" class="btn-login">登录</router-link>
      </div>
    </div>
  </header>
</template>

<style scoped>
.new-header {
  background: #1e293b;
  padding: 16px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.new-header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-section {
  display: flex;
  align-items: center;
  color: white;
}

.logo {
  font-size: 20px;
  font-weight: 600;
  margin: 0;
  letter-spacing: 0.5px;
}

.nav-menu {
  display: flex;
  gap: 28px;
  flex: 1;
  justify-content: center;
}

.nav-item {
  color: white;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  padding: 6px 0;
  border-radius: 0;
  transition: all 0.3s;
  position: relative;
}

.nav-item:hover {
  color: #60a5fa;
  transform: translateY(0);
}

.nav-item:hover::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #60a5fa;
  border-radius: 2px;
}

.auth-buttons {
  display: flex;
  gap: 12px;
  align-items: center;
}

.btn-register {
  padding: 8px 20px;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 4px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s;
}

.btn-register:hover {
  background: #2563eb;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
}

.btn-login {
  padding: 8px 20px;
  background: transparent;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s;
}

.btn-login:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.5);
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .nav-menu {
    gap: 20px;
  }
  
  .nav-item {
    font-size: 13px;
  }
}

@media (max-width: 991px) {
  .nav-menu {
    display: none;
  }
  
  .new-header-content {
    justify-content: space-between;
  }
}

@media (max-width: 576px) {
  .logo {
    font-size: 18px;
  }
  
  .btn-login, .btn-register {
    padding: 6px 12px;
    font-size: 13px;
  }
}
</style>