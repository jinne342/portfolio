<template>
  <div class="admin-dashboard">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>竞赛管理系统</h2>
          <p>管理竞赛信息</p>
        </div>
        
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-info">
              <p class="stat-label">总用户数</p>
              <p class="stat-value">{{ userCount }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-info">
              <p class="stat-label">总队伍数</p>
              <p class="stat-value">{{ teamCount }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-info">
              <p class="stat-label">进行中竞赛</p>
              <p class="stat-value">{{ competitionCount }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-info">
              <p class="stat-label">待处理报名审核</p>
              <p class="stat-value">{{ pendingRegistrationCount }}</p>
            </div>
          </div>
        </div>

        <div class="content-grid">
          <div class="content-card">
            <h3>系统概览</h3>
            <div class="overview-list">
              <div class="overview-item">
                <span class="label">今日新增用户</span>
                <span class="value">12</span>
              </div>
              <div class="overview-item">
                <span class="label">今日新增队伍</span>
                <span class="value">8</span>
              </div>
              <div class="overview-item">
                <span class="label">今日提交作品</span>
                <span class="value">25</span>
              </div>
              <div class="overview-item">
                <span class="label">系统运行时间</span>
                <span class="value">365天</span>
              </div>
            </div>
          </div>
          <div class="content-card">
            <h3>管理功能</h3>
            <div class="quick-actions">
              <router-link v-if="userStore.isSuperAdmin" to="/super-admin/user" class="action-btn">
                <span>用户管理</span>
              </router-link>
              <router-link v-if="userStore.isSuperAdmin || userStore.isCompetitionAdmin" to="/team" class="action-btn">
                <span>队伍管理</span>
              </router-link>
              <router-link v-if="userStore.isSuperAdmin || userStore.isCompetitionAdmin" to="/competition" class="action-btn">
                <span>竞赛管理</span>
              </router-link>
              <router-link v-if="userStore.isSuperAdmin" to="/super-admin/violation" class="action-btn">
                <span>违规管理</span>
              </router-link>
              <router-link v-if="userStore.isSuperAdmin" to="/super-admin/statistics" class="action-btn">
                <span>数据统计</span>
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
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getUserCount, getTeamCount, getActiveCompetitionCount, getPendingRegistrationCount } from '../../api/statistics.js';

const userStore = useUserStore();
const userCount = ref(0);
const teamCount = ref(0);
const competitionCount = ref(0);
const pendingRegistrationCount = ref(0);

// 在组件挂载时获取真实数据
onMounted(async () => {
  try {
    // 获取总用户数
    const userData = await getUserCount();
    userCount.value = userData.total_users;
    
    // 获取总队伍数
    const teamData = await getTeamCount();
    teamCount.value = teamData.total_teams;
    
    // 获取进行中竞赛数
    const competitionData = await getActiveCompetitionCount();
    competitionCount.value = competitionData.active_competitions;
    
    // 获取待处理报名审核数
    const registrationData = await getPendingRegistrationCount();
    pendingRegistrationCount.value = registrationData.pending_registrations;
  } catch (error) {
    console.error('获取统计数据失败:', error);
  }
});
</script>

<style scoped>
.admin-dashboard {
  min-height: 100vh;
  background: #f1f5f9;
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
  font-size: 24px;
  color: #1e293b;
  margin-bottom: 8px;
  font-weight: 600;
}

.page-header p {
  color: #64748b;
  font-size: 14px;
  margin: 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.2s;
  color: white;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.stat-info {
  text-align: center;
}

.stat-label {
  font-size: 14px;
  opacity: 0.9;
  margin: 0 0 8px 0;
  font-weight: 500;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  margin: 0;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.content-card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.content-card h3 {
  font-size: 18px;
  color: #1e293b;
  margin-bottom: 20px;
  font-weight: 600;
}

.overview-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.overview-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #f8fafc;
  border-radius: 6px;
}

.overview-item .label {
  color: #64748b;
  font-size: 14px;
}

.overview-item .value {
  color: #1e293b;
  font-size: 16px;
  font-weight: 600;
}

.quick-actions {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  background: #667eea;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.3s;
  font-weight: 500;
  border: none;
  cursor: pointer;
  font-size: 14px;
}

.action-btn:hover {
  background: #5b21b6;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}
</style>

