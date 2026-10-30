<template>
  <header class="header">
    <div class="header-content">
      <div class="logo-section">
        <h1 class="logo">数学建模竞赛平台</h1>
      </div>
      <div class="user-info">
        <div class="user-avatar">
          <span>{{ userStore.userInfo.username?.charAt(0) || 'U' }}</span>
        </div>
        <div class="user-details">
          <span class="username">{{ userStore.userInfo.username || '用户' }}</span>
          <span class="user-role">{{ getRoleName() }}</span>
        </div>
        <button class="logout-btn" @click="logout">
          <span>退出</span>
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useUserStore } from '../store/user.js';
import { useRouter } from 'vue-router';
import { showConfirm } from '../utils/notification.js';

const userStore = useUserStore();
const router = useRouter();

const getRoleName = () => {
  if (userStore.isSuperAdmin) return '超级管理员';
  if (userStore.isCompetitionAdmin) return '竞赛管理员';
  if (userStore.isTeacher) return '教师';
  if (userStore.isStudent) return '学生';
  return userStore.userInfo.role || '用户';
};

const logout = async () => {
  try {
    await showConfirm('提示', '确定要退出登录吗？', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    });
    await userStore.logout();
    router.push('/login');
  } catch {
    // 用户取消
  }
};
</script>

<style scoped>
.header {
  width: 100%;
  height: 70px;
  background: #1e293b;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 0 30px;
  max-width: 100%;
}

.logo-section {
  display: flex;
  align-items: center;
}

.logo {
  margin: 0;
  font-size: 22px;
  font-weight: 600;
  color: white;
  letter-spacing: 0.5px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #60a5fa;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 16px;
  border: none;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.user-details {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.username {
  color: white;
  font-weight: 600;
  font-size: 15px;
}

.user-role {
  color: rgba(255,255,255,0.8);
  font-size: 12px;
  margin-top: 2px;
}

.logout-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px 16px;
  background: transparent;
  color: white;
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
  font-weight: 500;
}

.logout-btn:hover {
  background: rgba(255,255,255,0.1);
  border-color: rgba(255,255,255,0.5);
}
</style>