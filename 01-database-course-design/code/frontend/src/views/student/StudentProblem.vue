<template>
  <div class="student-problem">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>题目选择与下载</h2>
          <p>查看和选择竞赛题目</p>
        </div>
        
        <!-- 竞赛选择 -->
        <div class="content-card">
          <h3>已报名竞赛</h3>
          <div class="competition-selector">
            <select v-model="selectedCompetitionId" @change="handleCompetitionChange" class="select-control">
              <option value="">请选择一个竞赛</option>
              <option v-for="competition in registeredCompetitions" :key="competition.competition_id" :value="competition.competition_id">
                {{ competition.competition_name }} (第{{ competition.session_no }}届)
              </option>
            </select>
          </div>
        </div>
        
        <!-- 团队选择 -->
        <div v-if="selectedCompetitionId && competitionTeams.length > 0" class="content-card">
          <h3>选择团队</h3>
          <div class="team-selector">
            <select v-model="currentTeamId" @change="handleTeamChange" class="select-control">
              <option value="">请选择一个团队</option>
              <option v-for="team in competitionTeams" :key="team.team_id" :value="team.team_id">
                {{ team.team_name }} (队长: {{ team.captain_name || '未知' }})
              </option>
            </select>
          </div>
        </div>
        
        <!-- 题目列表 -->
        <div v-if="selectedCompetitionId" class="content-card">
          <h3>竞赛题目列表</h3>
          
          <div v-if="!currentTeamId" class="warning-state">
            <p>请先选择一个团队</p>
          </div>
          
          <div v-else-if="selectedCompetitionId && problems.length === 0" class="empty-state">
            <p>该竞赛暂无题目</p>
          </div>
          
          <div v-else class="problem-list">
            <div class="problem-item" v-for="problem in problems" :key="problem.problem_id">
              <div class="problem-header">
                <h4>{{ problem.title }}</h4>
                <div class="problem-status">
                  <span v-if="selectedProblemId === problem.problem_id" class="status-badge status-selected">
                    已选择
                  </span>
                </div>
              </div>
              
              <div class="problem-description" v-if="problem.description">
                <p>{{ problem.description }}</p>
              </div>
              
              <div class="problem-details">
                <div v-if="problem.max_teams > 0" class="problem-quota">
                  <span class="label">最大选择团队数:</span>
                  <span class="value">{{ problem.max_teams }}</span>
                </div>
                <div v-if="problem.file_url" class="problem-file">
                  <span class="label">题目文件:</span>
                  <a href="#" @click.prevent="handleFileDownload(problem.problem_id)" class="file-link">
                    <span class="icon">📄</span>
                    <span>下载题目文件</span>
                  </a>
                </div>
              </div>
              
              <div class="problem-actions">
                <button 
                  v-if="selectedProblemId !== problem.problem_id"
                  @click="handleProblemSelect(problem.problem_id)"
                  class="btn btn-primary"
                  :disabled="!canSelectProblem(problem)"
                >
                  {{ getSelectButtonText(problem) }}
                </button>
                <button 
                  v-else
                  class="btn btn-secondary"
                  disabled
                >
                  已选择
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useUserStore } from '../../store/user.js';
import { showSuccess, showError } from '../../utils/notification.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getProblemsByCompetition } from '../../api/problem.js';
import { selectProblem, getSelectedProblem } from '../../api/problem.js';
import { getTeamsByUser } from '../../api/team.js';
import { getCompetitions } from '../../api/contest.js';

const userStore = useUserStore();
const userTeams = ref([]); // 用户所在的所有团队
const allCompetitions = ref([]); // 所有竞赛
const competitionTeams = ref([]); // 当前竞赛的团队列表
const selectedCompetitionId = ref('');
const problems = ref([]);
const selectedProblemId = ref(null);
const currentTeamId = ref(null);

// 计算用户已报名的竞赛（基于团队）
const registeredCompetitions = computed(() => {
  // 获取用户所有团队参与的竞赛ID
  const competitionIds = [...new Set(userTeams.value.map(team => team.competition_id))];
  // 返回这些竞赛的详细信息
  return allCompetitions.value.filter(competition => 
    competitionIds.includes(competition.competition_id)
  );
});

// 获取用户所有团队
const fetchUserTeams = async () => {
  const userId = userStore.userInfo?.user_id;
  if (!userId) return;
  
  try {
    const response = await getTeamsByUser(userId);
    userTeams.value = response || [];
  } catch (error) {
    showError('获取团队列表失败：' + (error.response?.data?.message || error.message));
  }
};

// 获取所有竞赛
const fetchAllCompetitions = async () => {
  try {
    const response = await getCompetitions();
    allCompetitions.value = response || [];
  } catch (error) {
    showError('获取竞赛列表失败：' + (error.response?.data?.message || error.message));
  }
};

// 获取当前竞赛下的用户团队
const fetchCompetitionTeams = async (competitionId) => {
  if (!competitionId) {
    competitionTeams.value = [];
    currentTeamId.value = null;
    return;
  }
  
  // 从用户团队中筛选出参加当前竞赛的团队
  competitionTeams.value = userTeams.value.filter(team => team.competition_id === competitionId);
  
  // 如果用户在该竞赛下只有一个团队，默认选择它
  if (competitionTeams.value.length === 1) {
    currentTeamId.value = competitionTeams.value[0].team_id;
  } else {
    currentTeamId.value = null;
  }
};

// 获取竞赛题目列表
const fetchCompetitionProblems = async (competitionId) => {
  if (!competitionId) return;
  
  try {
    const response = await getProblemsByCompetition(competitionId);
    problems.value = response || [];
    // 获取当前队伍已选择的题目
    fetchSelectedProblem();
  } catch (error) {
    showError('获取题目列表失败：' + (error.response?.data?.message || error.message));
  }
};

// 获取已选择的题目
const fetchSelectedProblem = async () => {
  if (!currentTeamId.value) {
    selectedProblemId.value = null;
    return;
  }
  
  try {
    const response = await getSelectedProblem(currentTeamId.value);
    if (response?.problem_id) {
      selectedProblemId.value = response.problem_id;
    } else {
      selectedProblemId.value = null;
    }
  } catch (error) {
    console.error('获取已选择题目失败:', error);
    selectedProblemId.value = null;
  }
};

// 处理竞赛选择变化
const handleCompetitionChange = () => {
  problems.value = [];
  selectedProblemId.value = null;
  if (selectedCompetitionId.value) {
    fetchCompetitionTeams(selectedCompetitionId.value);
    fetchCompetitionProblems(selectedCompetitionId.value);
  } else {
    competitionTeams.value = [];
    currentTeamId.value = null;
  }
};

// 处理团队选择变化
const handleTeamChange = () => {
  fetchSelectedProblem();
};

// 检查是否可以选择题目
const canSelectProblem = (problem) => {
  if (!currentTeamId.value) return false;
  // 题目已达到最大选择团队数
  if (problem.max_teams > 0) {
    // 这里应该从后端获取当前选择该题目的团队数，但暂时简单处理
    return true;
  }
  return true;
};

// 获取选择按钮文本
const getSelectButtonText = (problem) => {
  if (!currentTeamId.value) return '请先选择团队';
  if (!canSelectProblem(problem)) return '无法选择';
  return '选择该题目';
};

// 处理题目选择
const handleProblemSelect = async (problemId) => {
  if (!currentTeamId.value) {
    showError('请先选择一个团队');
    return;
  }
  
  try {
    await selectProblem(problemId, currentTeamId.value);
    showSuccess('题目选择成功');
    selectedProblemId.value = problemId;
  } catch (error) {
    showError('题目选择失败：' + (error.response?.data?.detail || error.message));
  }
};

// 处理文件下载
const handleFileDownload = async (problemId) => {
  try {
    // 构建下载URL
    const downloadUrl = `${import.meta.env.VITE_API_BASE_URL}/api/problems/${problemId}/download/`;
    
    // 使用隐藏的iframe或新窗口下载文件
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.setAttribute('download', '');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  } catch (error) {
    showError('文件下载失败：' + (error.response?.data?.detail || error.message));
  }
};

onMounted(async () => {
  await fetchUserTeams();
  await fetchAllCompetitions();
});
</script>

<style scoped>
.student-problem {
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
  margin-bottom: 20px;
}

.content-card h3 {
  font-size: 18px;
  color: #2d3748;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid #e2e8f0;
}

.competition-selector {
  max-width: 400px;
}

.select-control {
  width: 100%;
  padding: 10px 15px;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 14px;
  background-color: white;
  cursor: pointer;
  transition: all 0.2s;
}

.select-control:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.empty-state {
  text-align: center;
  padding: 40px 0;
  color: #718096;
}

.problem-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.problem-item {
  background: #f7fafc;
  border-radius: 8px;
  padding: 20px;
  transition: all 0.2s;
}

.problem-item:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.problem-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.problem-header h4 {
  margin: 0;
  font-size: 18px;
  color: #2d3748;
}

.problem-description {
  margin-bottom: 16px;
  padding: 12px;
  background: white;
  border-radius: 6px;
}

.problem-description p {
  margin: 0;
  color: #4a5568;
  font-size: 14px;
  line-height: 1.5;
}

.problem-details {
  margin-bottom: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.problem-details .label {
  color: #718096;
  margin-right: 5px;
  font-size: 14px;
}

.problem-details .value {
  color: #2d3748;
  font-weight: 500;
  font-size: 14px;
}

.problem-file .file-link {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  color: #667eea;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s;
}

.problem-file .file-link:hover {
  color: #5a67d8;
  text-decoration: underline;
}

.problem-actions {
  display: flex;
  justify-content: flex-end;
}

.status-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge.status-selected {
  background-color: #e8f5e9;
  color: #27ae60;
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
</style>