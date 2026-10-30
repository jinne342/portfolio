<template>
  <div class="student-competition">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>竞赛报名</h2>
          <p>查看和报名可参与的竞赛</p>
        </div>
        
        <div class="content-card">
          <h3>竞赛列表</h3>
          <div v-if="!hasAvailableCompetitions && competitions.length > 0" class="no-available-competitions">
            <div class="empty-state">
              <el-icon class="empty-icon"><Warning /></el-icon>
              <h4>当前不存在可报名竞赛</h4>
              <p>请等待新的竞赛发布或检查您的报名状态</p>
              <p class="test-hint">若需要进行测试，请创建处于报名时间范围内且状态为启用的竞赛</p>
            </div>
          </div>
          <div class="competition-list">
            <div class="competition-item" v-for="competition in competitions" :key="competition.competition_id">
              <div class="competition-info">
                <h4>{{ competition.competition_name }}</h4>
                <p class="competition-session">第{{ competition.session_no }}届</p>
                <div class="competition-time">
                  <span class="label">报名时间:</span>
                  <span class="time-range">{{ formatDate(competition.sign_start) }} 至 {{ formatDate(competition.sign_end) }}</span>
                </div>
                <div class="competition-status">
                  <span :class="['status-badge', getStatusClass(competition.competition_id)]">
                    {{ getRegistrationStatus(competition.competition_id) }}
                  </span>
                </div>
              </div>
              <div class="competition-actions">
                <button 
                  v-if="!isRegistered(competition.competition_id) && canRegister(competition)"
                  @click="handleRegistration(competition.competition_id)"
                  class="btn btn-primary"
                >
                  立即报名
                </button>
                <button 
                  v-else-if="isRegistered(competition.competition_id)"
                  class="btn btn-secondary"
                  disabled
                >
                  已报名
                </button>
                <button 
                  v-else
                  class="btn btn-secondary"
                  disabled
                >
                  {{ getRegistrationButtonText(competition) }}
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 团队选择对话框 -->
        <el-dialog
          v-model="teamDialogVisible"
          title="选择团队"
          width="500px"
        >
          <div class="team-selection">
            <div class="form-item">
              <label>选择团队</label>
              <el-select v-model="selectedTeamId" placeholder="请选择您的团队">
                <el-option
                  v-for="team in teams"
                  :key="team.team_id"
                  :label="team.team_name"
                  :value="team.team_id"
                >
                  {{ team.team_name }} (队长: {{ team.captain_name || '未知' }})
                </el-option>
              </el-select>
            </div>
            
            <div class="dialog-actions">
              <el-button @click="cancelRegistration">取消</el-button>
              <el-button type="primary" @click="confirmRegistration">确认报名</el-button>
            </div>
          </div>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '../../store/user.js';
import { showSuccess, showError } from '../../utils/notification.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getCompetitions } from '../../api/contest.js';
import { getRegistrationsByUser } from '../../api/registration.js';
import { getTeams } from '../../api/team.js';
import { ElDialog, ElSelect, ElOption, ElInput, ElButton } from 'element-plus';
import { Warning } from '@element-plus/icons-vue';
import 'element-plus/dist/index.css';

const userStore = useUserStore();
const router = useRouter();
const competitions = ref([]);
const registrations = ref([]);

// 团队相关
const teams = ref([]);
const selectedTeamId = ref(null);
const currentCompetitionId = ref(null);
const teamDialogVisible = ref(false);

// 格式化日期
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('zh-CN', { 
    year: 'numeric', 
    month: '2-digit', 
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  });
};

// 获取报名状态
const getRegistrationStatus = (competitionId) => {
  // 基于用户所在团队判断报名状态
  const teamCount = teamCounts.value[competitionId] || 0;
  if (teamCount > 0) {
    return '已报名';
  }
  return '未报名';
};

// 获取状态样式类
const getStatusClass = (competitionId) => {
  // 基于用户所在团队判断状态样式
  const teamCount = teamCounts.value[competitionId] || 0;
  if (teamCount > 0) {
    return 'status-approved';
  }
  return 'status-not-registered';
};

// 检查是否已报名
const isRegistered = (competitionId) => {
  // 如果用户在该竞赛下有团队，说明已报名
  return teamCounts.value[competitionId] > 0;
};

// 检查是否可以报名
const canRegister = (competition) => {
  // 仅检查竞赛状态为0（可报名）
  return competition.status === 0;
};

// 保存用户在各竞赛下的团队数量
const teamCounts = ref({});

// 获取用户在特定竞赛下的团队数量
const getUserTeamCountForCompetition = async (competitionId) => {
  // 如果已经缓存了该竞赛的团队数量，直接返回
  if (teamCounts.value[competitionId] !== undefined) {
    return teamCounts.value[competitionId];
  }
  
  try {
    const userId = userStore.userInfo?.user_id;
    if (!userId) {
      return 0;
    }
    
    const response = await getTeams(competitionId, userId);
    const count = response?.length || 0;
    teamCounts.value[competitionId] = count;
    return count;
  } catch (error) {
    console.error('获取团队数量失败：', error);
    return 0;
  }
};

// 获取报名按钮文本
const getRegistrationButtonText = (competition) => {
  // 检查竞赛状态
  if (competition.status !== 0) {
    return '竞赛已关闭';
  }
  
  // 使用缓存的团队数量（已在fetchCompetitions中预加载）
  const teamCount = teamCounts.value[competition.competition_id] || 0;
  if (teamCount > 0) {
    return '已报名';
  }
  
  return '立即报名';
};

// 获取用户团队
const fetchUserTeams = async (competitionId) => {
  const userId = userStore.userInfo?.user_id;
  if (!userId) return;
  
  try {
    const response = await getTeams(competitionId, userId);
    teams.value = response || [];
  } catch (error) {
    showError('获取团队列表失败：' + (error.response?.data?.message || error.message));
  }
};

// 处理报名
const handleRegistration = async (competitionId) => {
  const userId = userStore.userInfo?.user_id;
  if (!userId) {
    showError('请先登录');
    return;
  }
  
  // 直接跳转到创建队伍页面，并传递当前竞赛ID
  router.push({
    path: '/student/team',
    query: { competitionId: competitionId }
  });
};

// 确认报名
const confirmRegistration = async () => {
  if (!selectedTeamId.value) {
    showError('请选择团队');
    return;
  }
  
  const userId = userStore.userInfo?.user_id;
  if (!userId || !currentCompetitionId.value) return;
  
  try {
    await createRegistration({
      user_id: userId,
      competition_id: currentCompetitionId.value,
      team_id: selectedTeamId.value
    });
    
    showSuccess('报名成功，请等待审核');
    // 关闭对话框
    teamDialogVisible.value = false;
    // 清空选择
    selectedTeamId.value = null;
    // 重新获取报名状态
    fetchUserRegistrations();
  } catch (error) {
    showError('报名失败：' + (error.response?.data?.detail || error.message));
  }
};

// 取消报名
const cancelRegistration = () => {
  teamDialogVisible.value = false;
  selectedTeamId.value = null;
  currentCompetitionId.value = null;
};

// 获取竞赛列表
const fetchCompetitions = async () => {
  try {
    const response = await getCompetitions();
    competitions.value = response || [];
    
    // 预获取所有竞赛的团队数量（无论是否可报名）
    const userId = userStore.userInfo?.user_id;
    if (userId) {
      for (const competition of competitions.value) {
        await getUserTeamCountForCompetition(competition.competition_id);
      }
    }
  } catch (error) {
    showError('获取竞赛列表失败：' + (error.response?.data?.message || error.message));
  }
};

// 获取用户报名记录
const fetchUserRegistrations = async () => {
  const userId = userStore.userInfo?.user_id;
  if (!userId) return;
  
  try {
    const response = await getRegistrationsByUser(userId);
    registrations.value = response.data || [];
  } catch (error) {
    showError('获取报名记录失败：' + (error.response?.data?.message || error.message));
  }
};

// 判断是否有可报名的竞赛
const hasAvailableCompetitions = computed(() => {
  return competitions.value.some(competition => {
    if (isRegistered(competition.competition_id)) {
      return false;
    }
    if (!canRegister(competition)) {
      return false;
    }
    // 检查用户是否有该竞赛的团队
    return teamCounts.value[competition.competition_id] > 0;
  });
});

onMounted(() => {
  fetchCompetitions();
  fetchUserRegistrations();
});
</script>

<style scoped>
.student-competition {
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

.competition-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.competition-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background: #f7fafc;
  border-radius: 8px;
  transition: all 0.2s;
}

.competition-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.competition-info {
  flex: 1;
}

.competition-info h4 {
  margin: 0 0 8px 0;
  font-size: 18px;
  color: #2d3748;
}

.competition-session {
  margin: 0 0 12px 0;
  font-size: 14px;
  color: #718096;
}

.competition-time {
  margin-bottom: 8px;
  font-size: 14px;
}

.competition-time .label {
  color: #718096;
  margin-right: 5px;
}

.competition-time .time-range {
  color: #2d3748;
  font-weight: 500;
}

.competition-status {
  margin-top: 8px;
}

.status-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 500;
  }

  /* 团队选择对话框样式 */
  .team-selection {
    padding: 20px 0;
  }

  .form-item {
    margin-bottom: 20px;
  }

  .form-item label {
    display: block;
    margin-bottom: 8px;
    font-weight: 500;
    color: #2d3748;
  }

  .dialog-actions {
    margin-top: 30px;
    text-align: right;
  }

  .dialog-actions .el-button {
    margin-left: 10px;
  }

.status-badge.status-pending {
  background-color: #fef5e7;
  color: #d68910;
}

.status-badge.status-approved {
  background-color: #e8f5e9;
  color: #27ae60;
}

.status-badge.status-rejected {
  background-color: #fee;
  color: #c0392b;
}

.status-badge.status-not-registered {
  background-color: #e8eaf6;
  color: #3f51b5;
}

.competition-actions {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background-color: #e2e8f0;
  color: #718096;
}

/* 无可用竞赛状态样式 */
.no-available-competitions {
  margin-bottom: 20px;
}

.empty-state {
  text-align: center;
  padding: 40px 20px;
  background-color: #fff3cd;
  border: 1px solid #ffeaa7;
  border-radius: 8px;
  margin-bottom: 20px;
}

.empty-icon {
  font-size: 48px;
  color: #fdcb6e;
  margin-bottom: 16px;
}

.empty-state h4 {
  margin: 0 0 8px 0;
  color: #d68910;
  font-size: 18px;
}

.empty-state p {
  margin: 0 0 8px 0;
  color: #856404;
  font-size: 14px;
}

.test-hint {
  font-style: italic;
  color: #725b2b !important;
  font-size: 13px !important;
}
</style>