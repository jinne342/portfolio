<template>
  <div class="reviewer-dashboard">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>评审工作台</h2>
          <p>欢迎，{{ userStore.userInfo.username }}评审专家！</p>
        </div>
        
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">📝</div>
            <div class="stat-info">
              <h3>待评审作品</h3>
              <p class="stat-value">{{ pendingCount }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">✅</div>
            <div class="stat-info">
              <h3>已评审</h3>
              <p class="stat-value">{{ reviewedCount }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📊</div>
            <div class="stat-info">
              <h3>平均分</h3>
              <p class="stat-value">{{ avgScore }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">⏱️</div>
            <div class="stat-info">
              <h3>今日完成</h3>
              <p class="stat-value">{{ todayCount }}</p>
            </div>
          </div>
        </div>

        <div class="content-card">
          <h3>待评审作品列表</h3>
          <div class="review-list">
            <div class="review-item" v-for="work in pendingWorks" :key="work.work_id">
              <div class="review-info">
                <span class="review-title">作品 #{{ work.work_id }}</span>
                <span class="review-team">队伍：{{ work.team_name }}</span>
                <span class="review-time">提交时间：{{ work.submit_time }}</span>
              </div>
              <button class="review-btn" @click="$router.push('/reviewer/review')">开始评审</button>
            </div>
            <div v-if="pendingWorks.length === 0" class="empty-state">
              暂无待评审作品
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
import { getWorks } from '../../api/work.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { showError } from '../../utils/notification.js';

const userStore = useUserStore();
const pendingCount = ref(0);
const reviewedCount = ref(0);
const avgScore = ref('0.0');
const todayCount = ref(0);
const pendingWorks = ref([]);

onMounted(async () => {
  try {
    const userId = userStore.userInfo?.user_id;
    if (userId) {
      const works = await getWorks(null, null, userId);
      
      pendingWorks.value = works.filter(work => !work.is_reviewed);
      const reviewedWorks = works.filter(work => work.is_reviewed);
      
      pendingCount.value = pendingWorks.value.length;
      reviewedCount.value = reviewedWorks.length;
      
      if (reviewedWorks.length > 0) {
        const totalScore = reviewedWorks.reduce((sum, work) => {
          return sum + (parseFloat(work.score) || 0);
        }, 0);
        avgScore.value = (totalScore / reviewedWorks.length).toFixed(1);
      } else {
        avgScore.value = '0.0';
      }
      
      const today = new Date().toISOString().split('T')[0];
      todayCount.value = reviewedWorks.filter(work => {
        if (work.review_time) {
          return work.review_time.startsWith(today);
        }
        return false;
      }).length;
    }
  } catch (error) {
    showError('获取数据失败：' + (error.response?.data?.message || error.message || error));
  }
});
</script>

<style scoped>
.reviewer-dashboard {
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

.stat-icon {
  font-size: 48px;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
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

.review-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.review-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background: #f7fafc;
  border-radius: 8px;
  border-left: 4px solid #fa709a;
}

.review-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}

.review-title {
  font-size: 16px;
  font-weight: 600;
  color: #2d3748;
}

.review-team {
  font-size: 14px;
  color: #718096;
}

.review-time {
  font-size: 12px;
  color: #a0aec0;
}

.review-btn {
  padding: 10px 20px;
  background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s;
}

.review-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(250, 112, 154, 0.4);
}

.empty-state {
  padding: 40px;
  text-align: center;
  color: #a0aec0;
  font-size: 16px;
}
</style>

