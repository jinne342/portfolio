<template>
  <div class="teacher-dashboard">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>教师工作台</h2>
          <p>欢迎，{{ userStore.userInfo.username }}老师！</p>
        </div>
        
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">👥</div>
            <div class="stat-info">
              <h3>指导队伍</h3>
              <p class="stat-value">{{ teamCount }}</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📝</div>
            <div class="stat-info">
              <h3>待评审</h3>
              <p class="stat-value">{{ pendingReview }}</p>
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
        </div>

        <div class="content-grid">
          <div class="content-card">
            <h3>待处理事项</h3>
            <div class="task-list">
              <div class="task-item" v-for="task in pendingTasks" :key="task.id">
                <span class="task-priority">{{ task.priority }}</span>
                <span class="task-text">{{ task.text }}</span>
                <button class="task-btn">处理</button>
              </div>
              <div v-if="pendingTasks.length === 0" class="no-tasks">
                <p>暂无待处理事项</p>
              </div>
            </div>
          </div>
          <div class="content-card">
            <h3>快速操作</h3>
            <div class="quick-actions">
              <router-link to="/teacher/team" class="action-btn">
                <span class="icon">👥</span>
                <span>队伍管理</span>
              </router-link>
              <router-link to="/teacher/review" class="action-btn">
                <span class="icon">📝</span>
                <span>开始评审</span>
              </router-link>
              <router-link to="/teacher/statistics" class="action-btn">
                <span class="icon">📊</span>
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
import { getTeacherTeams } from '../../api/teacherTeam.js';
import { getWorks } from '../../api/work.js';

const userStore = useUserStore();
const teamCount = ref(0);
const pendingReview = ref(0);
const reviewedCount = ref(0);
const avgScore = ref('0.0');
const pendingTasks = ref([]);

// 获取教师指导的队伍数量
const fetchTeacherTeams = async () => {
  try {
    const userId = userStore.userInfo.user_id;
    const teams = await getTeacherTeams(userId);
    teamCount.value = teams.length;
  } catch (error) {
    console.error('获取教师队伍失败:', error);
  }
};

// 获取教师的评审任务
const fetchReviewTasks = async () => {
  try {
    const userId = userStore.userInfo.user_id;
    
    // 获取待评审的作品
    const pendingWorks = await getWorks(null, null, userId);
    const filteredPending = pendingWorks.filter(work => !work.is_reviewed);
    pendingReview.value = filteredPending.length;
    
    // 获取已评审的作品
    const filteredReviewed = pendingWorks.filter(work => work.is_reviewed);
    reviewedCount.value = filteredReviewed.length;
    
    // 计算平均分
    if (filteredReviewed.length > 0) {
      const totalScore = filteredReviewed.reduce((sum, work) => {
        return sum + (parseFloat(work.score) || 0);
      }, 0);
      avgScore.value = (totalScore / filteredReviewed.length).toFixed(1);
    } else {
      avgScore.value = '0.0';
    }
    
    // 设置待处理事项（最多显示3个）
    pendingTasks.value = filteredPending.slice(0, 3).map((work, index) => ({
      id: work.work_id,
      text: `评审队伍 ${work.team_name} 的作品`,
      priority: '高'
    }));
  } catch (error) {
    console.error('获取评审任务失败:', error);
  }
};

// 在组件挂载时获取数据
onMounted(() => {
  fetchTeacherTeams();
  fetchReviewTasks();
});
</script>

<style scoped>
.teacher-dashboard {
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
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
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

.task-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: #f7fafc;
  border-radius: 8px;
}

.task-priority {
  padding: 4px 8px;
  background: #fc8181;
  color: white;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
}

.task-text {
  flex: 1;
  color: #2d3748;
  font-size: 14px;
}

.task-btn {
  padding: 6px 16px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}

.task-btn:hover {
  background: #5568d3;
}

.no-tasks {
  text-align: center;
  padding: 20px;
  color: #718096;
  font-size: 14px;
  background: #f7fafc;
  border-radius: 8px;
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
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s;
  font-weight: 500;
}

.action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(245, 87, 108, 0.4);
}

.action-btn .icon {
  font-size: 20px;
}
</style>

