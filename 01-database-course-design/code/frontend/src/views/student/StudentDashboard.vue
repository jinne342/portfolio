<template>
  <div class="student-dashboard">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>学生工作台</h2>
          <p>欢迎回来，{{ userStore.userInfo.username }}！</p>
        </div>
        
        <div class="stats-grid">
          <router-link to="/student/team" class="stat-card-link">
            <div class="stat-card">
              <div class="stat-icon">👥</div>
              <div class="stat-info">
                <h3>我的队伍</h3>
                <p class="stat-value">{{ teamCount }}</p>
              </div>
            </div>
          </router-link>
          <router-link to="/student/submission" class="stat-card-link">
            <div class="stat-card">
              <div class="stat-icon">📤</div>
              <div class="stat-info">
                <h3>已提交作品</h3>
                <p class="stat-value">{{ submissionCount }}</p>
              </div>
            </div>
          </router-link>
          <router-link to="/student/certificate" class="stat-card-link">
            <div class="stat-card">
              <div class="stat-icon">🏆</div>
              <div class="stat-info">
                <h3>获得证书</h3>
                <p class="stat-value">{{ certificateCount }}</p>
              </div>
            </div>
          </router-link>
          <router-link to="/student/message" class="stat-card-link">
            <div class="stat-card">
              <div class="stat-icon">💬</div>
              <div class="stat-info">
                <h3>未读消息</h3>
                <p class="stat-value">{{ messageCount }}</p>
              </div>
            </div>
          </router-link>
        </div>

        <div class="content-grid">
          <div class="content-card">
            <h3>最近活动</h3>
            <div class="activity-list">
              <div class="activity-item" v-for="i in 5" :key="i">
                <span class="activity-time">2025-01-{{ 10 + i }}</span>
                <span class="activity-text">提交了作品 #{{ i }}</span>
              </div>
            </div>
          </div>
          <div class="content-card">
            <h3>快速操作</h3>
            <div class="quick-actions">
              <router-link to="/student/team" class="action-btn">
                <span class="icon">👥</span>
                <span>查看队伍</span>
              </router-link>
              <router-link to="/student/submission" class="action-btn">
                <span class="icon">📤</span>
                <span>提交作品</span>
              </router-link>
              <router-link to="/student/certificate" class="action-btn">
                <span class="icon">🏆</span>
                <span>我的证书</span>
              </router-link>
              <router-link to="/student/message" class="action-btn">
                <span class="icon">💬</span>
                <span>消息中心</span>
              </router-link>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '../../store/user.js';
import { getTeams } from '../../api/team.js';
import { getWorks } from '../../api/work.js';
import { getCertificates } from '../../api/certificate.js';
import { getMessages } from '../../api/message.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { showError } from '../../utils/notification.js';

const userStore = useUserStore();
const teamCount = ref(0);
const submissionCount = ref(0);
const certificateCount = ref(0);
const messageCount = ref(0);

onMounted(async () => {
  const userId = userStore.userInfo?.user_id;
  if (userId) {
    try {
      // 获取用户的队伍数量
      const teamsResponse = await getTeams(null, userId);
      teamCount.value = teamsResponse?.length || 0;
      
      // 获取用户的提交作品数量
      const worksResponse = await getWorks(null, null, userId);
      submissionCount.value = worksResponse?.length || 0;
      
      // 获取用户的证书数量
      const certificatesResponse = await getCertificates({ user_id: userId });
      certificateCount.value = certificatesResponse?.length || 0;
      
      // 获取用户的未读消息数量
      const messagesResponse = await getMessages({ user_id: userId, is_read: false });
      messageCount.value = messagesResponse?.length || 0;
    } catch (error) {
      showError('获取数据失败：' + (error.response?.data?.message || error.message || error));
    }
  }
});
</script>

<style scoped>
.student-dashboard {
  min-height: 100vh;
  background: #f5f7fa;
}

.main-layout {
  display: flex;
}

.main-content {
  flex: 1;
  padding: 30px;
  min-height: calc(100vh - 70px);
}

.page-header {
  margin-bottom: 30px;
}

.page-header h2 {
  font-size: 28px;
  color: #2d3748;
  margin-bottom: 8px;
}

.page-header p {
  color: #718096;
  font-size: 16px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}

.stat-card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.stat-icon {
  font-size: 48px;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
}

.stat-info h3 {
  font-size: 14px;
  color: #718096;
  margin: 0 0 8px 0;
  font-weight: 500;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  color: #2d3748;
  margin: 0;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.content-card h3 {
  font-size: 18px;
  color: #2d3748;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid #e2e8f0;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.activity-item {
  display: flex;
  justify-content: space-between;
  padding: 12px;
  background: #f7fafc;
  border-radius: 8px;
}

.activity-time {
  color: #718096;
  font-size: 14px;
}

.activity-text {
  color: #2d3748;
  font-size: 14px;
}

.quick-actions {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s;
  font-weight: 500;
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.action-btn .icon {
  font-size: 20px;
}
</style>

