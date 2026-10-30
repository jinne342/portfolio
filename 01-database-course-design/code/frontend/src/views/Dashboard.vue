<template>
  <div class="page">
    <Header />
    <div class="layout">
      <Sidebar />
      <main class="content">
        <div class="hero-section">
          <div class="hero-content">
            <h1 class="hero-title">数学建模竞赛管理中心</h1>
            <p class="hero-subtitle">实时数据统计与分析平台</p>
            <div class="hero-decoration"></div>
          </div>
        </div>
        
        <div class="dashboard-stats">
          <div class="stat-card teams-card">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" class="icon-svg">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-number">{{ totalTeams }}</div>
              <div class="stat-label">参赛队伍</div>
            </div>
          </div>
          <div class="stat-card problems-card">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" class="icon-svg">
                <path d="M9 11H5a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h4l3 3V8l-3 3z"></path>
                <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-number">{{ totalProblems }}</div>
              <div class="stat-label">竞赛题目</div>
            </div>
          </div>
          <div class="stat-card submissions-card">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" class="icon-svg">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14,2 14,8 20,8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10,9 9,9 8,9"></polyline>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-number">{{ totalSubmissions }}</div>
              <div class="stat-label">论文提交</div>
            </div>
          </div>
          <div class="stat-card competitions-card">
            <div class="stat-icon">
              <svg viewBox="0 0 24 24" class="icon-svg">
                <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"></polygon>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-number">{{ activeCompetitions }}</div>
              <div class="stat-label">进行竞赛</div>
            </div>
          </div>
        </div>

        <div class="chart-container">
          <ChartCard title="各学院队伍分布" type="bar" :data="teamDistribution" />
          <ChartCard title="题目选择热度" type="pie" :data="problemDistribution" />
          <ChartCard title="题目选择趋势" type="line" :data="problemTrend" />
          <ChartCard title="提交分布" type="pie" :data="submissionDistribution" />
        </div>

        <div class="data-table-container">
          <div class="table-header">
            <h3 class="table-title">数据详情</h3>
            <div class="table-subtitle">查看具体数据明细</div>
          </div>
          <div class="table-tabs">
            <button 
              :class="['tab-button', { active: activeTab === 'teams' }]" 
              @click="activeTab = 'teams'"
            >
              参赛队伍
            </button>
            <button 
              :class="['tab-button', { active: activeTab === 'problems' }]" 
              @click="activeTab = 'problems'"
            >
              题目信息
            </button>
            <button 
              :class="['tab-button', { active: activeTab === 'submissions' }]" 
              @click="activeTab = 'submissions'"
            >
              论文提交
            </button>
          </div>
          
          <div v-if="activeTab === 'teams'" class="data-table">
            <table>
              <thead>
                <tr>
                  <th>队伍名称</th>
                  <th>所属学校</th>
                  <th>队长</th>
                  <th>创建时间</th>
                  <th>状态</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in teamsData" :key="team.id">
                  <td>{{ team.name }}</td>
                  <td>{{ team.school }}</td>
                  <td>{{ team.captain }}</td>
                  <td>{{ formatDate(team.createTime) }}</td>
                  <td><span class="status-badge" :class="team.status">{{ team.statusText }}</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div v-if="activeTab === 'problems'" class="data-table">
            <table>
              <thead>
                <tr>
                  <th>题目编号</th>
                  <th>题目标题</th>
                  <th>选择次数</th>
                  <th>最大得分</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="problem in problemsData" :key="problem.id">
                  <td>{{ problem.title.split('：')[0] }}</td>
                  <td>{{ problem.title.split('：')[1] || problem.title }}</td>
                  <td>{{ problem.selections }}</td>
                  <td>{{ problem.maxScore }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div v-if="activeTab === 'submissions'" class="data-table">
            <table>
              <thead>
                <tr>
                  <th>队伍</th>
                  <th>题目</th>
                  <th>提交时间</th>
                  <th>得分</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="submission in submissionsData" :key="submission.id">
                  <td>{{ submission.teamName }}</td>
                  <td>{{ submission.problemTitle }}</td>
                  <td>{{ formatDate(submission.submitTime) }}</td>
                  <td><span class="score-badge">{{ submission.score }}</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../components/Header.vue';
import Sidebar from '../components/Sidebar.vue';
import Footer from '../components/Footer.vue';
import ChartCard from '../components/ChartCard.vue';
import request from '../api/index.js';
import { showError } from '../utils/notification.js';

// 响应式数据
const teamDistribution = ref([]);
const problemDistribution = ref([]);
const problemTrend = ref([]);
const submissionDistribution = ref([]);

// 统计数据
const totalTeams = ref(0);
const totalProblems = ref(0);
const totalSubmissions = ref(0);
const activeCompetitions = ref(0);

// 表格数据
const teamsData = ref([]);
const problemsData = ref([]);
const submissionsData = ref([]);
const activeTab = ref('teams');

// 格式化日期
const formatDate = (dateString) => {
  if (!dateString) return '-';
  try {
    const date = new Date(dateString);
    if (isNaN(date.getTime())) return '-';
    return date.toLocaleDateString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit'
    });
  } catch (error) {
    return '-';
  }
};

// 获取仪表盘数据
const fetchDashboardData = async () => {
  try {
    console.log('开始获取仪表盘数据...');
    
    // 1. 获取各学院队伍分布
    const teamRes = await request.get('/api/statistics/team_by_college');
    console.log('队伍分布数据:', teamRes.data);
    teamDistribution.value = teamRes.data.map(item => ({
      name: item.college,
      value: item.count
    }));
    totalTeams.value = teamRes.data.reduce((sum, item) => sum + item.count, 0);

    // 2. 获取题目选择统计
    const problemRes = await request.get('/api/statistics/problem_selection');
    console.log('题目选择数据:', problemRes.data);
    problemDistribution.value = problemRes.data.map(item => ({
      name: item.problem.split('：')[0], // 只取题目编号
      value: item.count
    }));
    
    // 转换为趋势数据（按题目编号排序）
    problemTrend.value = problemRes.data.map((item, index) => ({
      name: `第${index + 1}次提交`,
      value: item.count
    }));
    
    totalProblems.value = problemRes.data.length;

    // 3. 获取总队伍数（如果需要更准确的数据）
    const countRes = await request.get('/api/statistics/team_count');
    console.log('队伍总数:', countRes.data);
    // 如果API返回的总数与分布之和不一致，使用API返回的总数
    if (countRes.data.total_teams !== totalTeams.value) {
      totalTeams.value = countRes.data.total_teams;
    }

    // 6. 模拟生成提交分布数据
    totalSubmissions.value = problemRes.data.reduce((sum, item) => sum + item.count, 0);
    submissionDistribution.value = [
      { name: '已评分', value: Math.floor(totalSubmissions.value * 0.8) },
      { name: '待评分', value: Math.floor(totalSubmissions.value * 0.2) }
    ];

    // 7. 模拟竞赛数据
    activeCompetitions.value = 2; // 根据插入的数据

    // 8. 清空模拟数据（使用真实数据）
    teamsData.value = [];
    problemsData.value = [];
    submissionsData.value = [];
    
    console.log('仪表盘数据加载完成');
    
  } catch (err) {
    console.error('仪表盘数据加载失败：', err);
    showError('仪表盘数据加载失败，请稍后重试');
    // 使用默认数据
    teamDistribution.value = [{ name: '暂无数据', value: 0 }];
    problemDistribution.value = [{ name: '暂无数据', value: 0 }];
    problemTrend.value = [{ name: '暂无数据', value: 0 }];
    submissionDistribution.value = [{ name: '暂无数据', value: 0 }];
  }
};



onMounted(() => {
  fetchDashboardData();
  
  // 设置定时刷新（每30秒）
  setInterval(() => {
    fetchDashboardData();
  }, 30000);
});
</script>

<style scoped>
.page {
  width: 100%;
  min-height: 100vh;
  padding: 0;
  margin: 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.content { 
  padding: 30px; 
  background: rgba(255,255,255,0.95);
  margin: 20px;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.1);
  backdrop-filter: blur(10px);
}

/* Hero 区域 */
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  padding: 40px;
  margin-bottom: 30px;
  position: relative;
  overflow: hidden;
  color: white;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
  animation: heroGlow 6s ease-in-out infinite;
}

@keyframes heroGlow {
  0%, 100% { transform: scale(1) rotate(0deg); opacity: 0.5; }
  50% { transform: scale(1.1) rotate(180deg); opacity: 0.8; }
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 10px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.hero-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
  font-weight: 300;
}

.hero-decoration {
  width: 60px;
  height: 4px;
  background: linear-gradient(90deg, #fff, #ff6b6b);
  border-radius: 2px;
  margin-top: 20px;
  animation: decorationGlow 3s ease-in-out infinite;
}

@keyframes decorationGlow {
  0%, 100% { opacity: 0.8; transform: scaleX(1); }
  50% { opacity: 1; transform: scaleX(1.2); }
}

/* 统计数据卡片 */
.dashboard-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  margin-bottom: 35px;
}

.stat-card {
  color: white;
  padding: 30px;
  border-radius: 16px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.12);
  display: flex;
  align-items: center;
  gap: 20px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.stat-card:hover::before {
  opacity: 1;
}

.stat-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

/* 不同卡片颜色主题 */
.teams-card {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.problems-card {
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
}

.submissions-card {
  background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
}

.competitions-card {
  background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
}

.stat-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  background: rgba(255,255,255,0.2);
  border-radius: 12px;
  position: relative;
  z-index: 2;
}

.icon-svg {
  width: 32px;
  height: 32px;
  fill: white;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
}

.stat-content {
  flex: 1;
  position: relative;
  z-index: 2;
}

.stat-number {
  font-size: 2.2rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 8px;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stat-label {
  font-size: 1rem;
  opacity: 0.95;
  font-weight: 500;
  letter-spacing: 0.3px;
}

/* 图表容器 */
.chart-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

/* 数据表格容器 */
.data-table-container {
  background: white;
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
  margin-top: 30px;
  border: 1px solid rgba(255,255,255,0.8);
}

.table-header {
  margin-bottom: 25px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f8f9fa;
}

.table-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 8px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.table-subtitle {
  font-size: 0.95rem;
  color: #6c757d;
  font-weight: 400;
}

/* 标签页 */
.table-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 30px;
  background: #f8f9fa;
  padding: 6px;
  border-radius: 12px;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.06);
}

.tab-button {
  padding: 14px 28px;
  background: transparent;
  border: none;
  font-size: 1rem;
  color: #6c757d;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 8px;
  font-weight: 500;
  position: relative;
  overflow: hidden;
}

.tab-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: -1;
}

.tab-button:hover::before {
  opacity: 0.1;
}

.tab-button.active::before {
  opacity: 1;
}

.tab-button:hover {
  color: #2c3e50;
  transform: translateY(-1px);
}

.tab-button.active {
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* 数据表格 */
.data-table {
  overflow-x: auto;
  border-radius: 12px;
  background: white;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.data-table table {
  width: 100%;
  border-collapse: collapse;
  border-radius: 12px;
  overflow: hidden;
}

.data-table th {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 18px 16px;
  text-align: left;
  font-weight: 600;
  font-size: 0.95rem;
  letter-spacing: 0.3px;
  position: relative;
  text-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.data-table th::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: rgba(255,255,255,0.3);
}

.data-table td {
  padding: 16px;
  border-bottom: 1px solid #f1f3f4;
  color: #2c3e50;
  font-size: 0.9rem;
  transition: background-color 0.2s ease;
}

.data-table tr {
  transition: all 0.2s ease;
}

.data-table tr:hover {
  background: linear-gradient(135deg, #f8f9ff 0%, #f0f2ff 100%);
  transform: scale(1.001);
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.data-table tr:last-child td {
  border-bottom: none;
}

.data-table tr:last-child:hover {
  border-radius: 0 0 12px 12px;
}

/* 状态徽章 */
.status-badge {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: none;
  letter-spacing: 0.3px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.status-badge::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.2;
  transition: opacity 0.3s ease;
}

.status-badge:hover::before {
  opacity: 0.3;
}

.status-badge.active {
  background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
  color: #155724;
  border: 1px solid #c3e6cb;
}

.status-badge.pending {
  background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
  color: #856404;
  border: 1px solid #ffeaa7;
}

.status-badge.inactive {
  background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* 分数徽章 */
.score-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 8px 16px;
  border-radius: 25px;
  font-size: 0.9rem;
  font-weight: 700;
  display: inline-block;
  min-width: 55px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.score-badge::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  transition: left 0.5s ease;
}

.score-badge:hover::before {
  left: 100%;
}

.score-badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(102, 126, 234, 0.4);
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .chart-container {
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  }
}

@media (max-width: 768px) {
  .content {
    margin: 10px;
    padding: 20px;
  }
  
  .hero-section {
    padding: 30px 20px;
    text-align: center;
  }
  
  .hero-title {
    font-size: 2rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
  }
  
  .dashboard-stats {
    grid-template-columns: 1fr;
    gap: 15px;
    margin-bottom: 25px;
  }
  
  .stat-card {
    padding: 20px;
  }
  
  .stat-number {
    font-size: 1.8rem;
  }
  
  .stat-icon {
    width: 50px;
    height: 50px;
  }
  
  .icon-svg {
    width: 28px;
    height: 28px;
  }
  
  .chart-container {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .data-table-container {
    padding: 20px;
    margin-top: 20px;
  }
  
  .table-tabs {
    flex-direction: column;
    gap: 5px;
  }
  
  .tab-button {
    text-align: center;
    padding: 12px 20px;
  }
  
  .table-title {
    font-size: 1.5rem;
  }
  
  .data-table th,
  .data-table td {
    padding: 12px 8px;
    font-size: 0.85rem;
  }
  
  .data-table {
    border-radius: 8px;
  }
}

@media (max-width: 480px) {
  .content {
    margin: 5px;
    padding: 15px;
  }
  
  .hero-section {
    padding: 20px 15px;
  }
  
  .hero-title {
    font-size: 1.8rem;
  }
  
  .stat-card {
    padding: 15px;
    flex-direction: column;
    text-align: center;
    gap: 15px;
  }
  
  .stat-number {
    font-size: 1.6rem;
  }
  
  .data-table-container {
    padding: 15px;
  }
  
  .data-table th,
  .data-table td {
    padding: 12px 8px;
    font-size: 0.85rem;
  }
}
</style>