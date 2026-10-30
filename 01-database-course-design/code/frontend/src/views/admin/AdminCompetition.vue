<template>
  <div class="admin-competition">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>竞赛管理</h2>
          <button class="primary-btn" @click="showCreateDialog = true">创建竞赛</button>
        </div>
        
        <!-- 竞赛列表 -->
        <div class="content-card">
          <h3>竞赛列表</h3>
          <el-table v-if="competitions.length > 0" :data="competitions" stripe style="width: 100%">
            <el-table-column prop="competition_id" label="竞赛ID" width="100" />
            <el-table-column prop="competition_name" label="竞赛名称" min-width="200" />
            <el-table-column prop="session_no" label="届数" width="80" />
            <el-table-column prop="status" label="状态" width="120">
              <template #default="scope">
                <el-tag :type="scope.row.status === 'active' ? 'success' : scope.row.status === 'pending' ? 'warning' : 'danger'">
                  {{ scope.row.status === 'active' ? '进行中' : scope.row.status === 'pending' ? '未开始' : '已结束' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="sign_start" label="报名开始" width="180" />
            <el-table-column prop="sign_end" label="报名结束" width="180" />
            <el-table-column prop="competition_start" label="竞赛开始" width="180" />
            <el-table-column prop="competition_end" label="竞赛结束" width="180" />
            <el-table-column label="操作" width="200" fixed="right">
              <template #default="scope">
                <el-button 
                  size="small" 
                  type="primary" 
                  @click="showUpdateDialog(scope.row)"
                >编辑</el-button>
                <el-button size="small" type="success" @click="manageProblems(scope.row)">管理赛题</el-button>
                <el-button size="small" type="danger" @click="handleDeleteCompetition(scope.row.competition_id)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-else class="empty-state">
            <el-empty description="暂无竞赛数据，点击'创建竞赛'开始添加吧！" />
          </div>
        </div>
        
        <!-- 创建竞赛对话框 -->
        <el-dialog v-model="showCreateDialog" title="创建竞赛" width="600px">
          <el-form :model="competitionForm" :rules="competitionRules" ref="competitionFormRef" label-width="120px">
            <el-form-item label="竞赛名称" prop="competition_name">
              <el-input v-model="competitionForm.competition_name" placeholder="请输入竞赛名称" />
            </el-form-item>
            <el-form-item label="届数" prop="session_no">
              <el-input v-model="competitionForm.session_no" placeholder="请输入届数" />
            </el-form-item>
            <el-form-item label="学校ID" prop="school_id">
              <el-input v-model.number="competitionForm.school_id" placeholder="请输入学校ID" />
            </el-form-item>
            <el-form-item label="报名开始时间" prop="sign_start">
              <el-date-picker
                v-model="competitionForm.sign_start"
                type="datetime"
                placeholder="选择报名开始时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="报名结束时间" prop="sign_end">
              <el-date-picker
                v-model="competitionForm.sign_end"
                type="datetime"
                placeholder="选择报名结束时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="竞赛开始时间" prop="competition_start">
              <el-date-picker
                v-model="competitionForm.competition_start"
                type="datetime"
                placeholder="选择竞赛开始时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="竞赛结束时间" prop="competition_end">
              <el-date-picker
                v-model="competitionForm.competition_end"
                type="datetime"
                placeholder="选择竞赛结束时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="报名费" prop="fee_amount">
              <el-input v-model.number="competitionForm.fee_amount" placeholder="请输入报名费" />
            </el-form-item>
            <el-form-item label="奖励规则" prop="reward_rule">
              <el-input v-model="competitionForm.reward_rule" type="textarea" placeholder="请输入奖励规则" :rows="3" />
            </el-form-item>
            <el-form-item label="状态" prop="status">
              <el-select v-model="competitionForm.status" placeholder="请选择状态">
                <el-option label="未开始" value="pending" />
                <el-option label="进行中" value="active" />
                <el-option label="已结束" value="ended" />
              </el-select>
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showCreateDialog = false">取消</el-button>
              <el-button type="primary" @click="handleCreateCompetition">创建</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 更新竞赛对话框 -->
        <el-dialog v-model="showUpdateDialogVisible" title="编辑竞赛" width="600px">
          <el-form :model="updateForm" :rules="competitionRules" ref="updateFormRef" label-width="120px">
            <el-form-item label="竞赛名称" prop="competition_name">
              <el-input v-model="updateForm.competition_name" placeholder="请输入竞赛名称" />
            </el-form-item>
            <el-form-item label="届数" prop="session_no">
              <el-input v-model="updateForm.session_no" placeholder="请输入届数" />
            </el-form-item>
            <el-form-item label="学校ID" prop="school_id">
              <el-input v-model.number="updateForm.school_id" placeholder="请输入学校ID" />
            </el-form-item>
            <el-form-item label="报名开始时间" prop="sign_start">
              <el-date-picker
                v-model="updateForm.sign_start"
                type="datetime"
                placeholder="选择报名开始时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="报名结束时间" prop="sign_end">
              <el-date-picker
                v-model="updateForm.sign_end"
                type="datetime"
                placeholder="选择报名结束时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="竞赛开始时间" prop="competition_start">
              <el-date-picker
                v-model="updateForm.competition_start"
                type="datetime"
                placeholder="选择竞赛开始时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="竞赛结束时间" prop="competition_end">
              <el-date-picker
                v-model="updateForm.competition_end"
                type="datetime"
                placeholder="选择竞赛结束时间"
                style="width: 100%"
              />
            </el-form-item>
            <el-form-item label="报名费" prop="fee_amount">
              <el-input v-model.number="updateForm.fee_amount" placeholder="请输入报名费" />
            </el-form-item>
            <el-form-item label="奖励规则" prop="reward_rule">
              <el-input v-model="updateForm.reward_rule" type="textarea" placeholder="请输入奖励规则" :rows="3" />
            </el-form-item>
            <el-form-item label="状态" prop="status">
              <el-select v-model="updateForm.status" placeholder="请选择状态">
                <el-option label="未开始" value="pending" />
                <el-option label="进行中" value="active" />
                <el-option label="已结束" value="ended" />
              </el-select>
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showUpdateDialogVisible = false">取消</el-button>
              <el-button type="primary" @click="handleUpdateCompetition">保存</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 赛题列表对话框 -->
        <el-dialog v-model="showProblemDialog" title="赛题管理" width="800px">
          <div class="dialog-header">
            <h3>{{ currentCompetition?.competition_name }} - 赛题列表</h3>
            <el-button type="primary" @click="handleShowCreateProblemDialog">创建赛题</el-button>
          </div>
          <div class="content-card">
            <el-table v-if="problems.length > 0" :data="problems" stripe style="width: 100%">
              <el-table-column prop="problem_id" label="赛题ID" width="100" />
              <el-table-column prop="title" label="赛题标题" min-width="200" />
              <el-table-column prop="max_teams" label="最大参赛队伍数" width="150" />
              <el-table-column label="操作" width="180" fixed="right">
                <template #default="scope">
                  <el-button size="small" type="primary" @click="handleShowUpdateProblemDialog(scope.row)">编辑</el-button>
                  <el-button size="small" type="danger" @click="handleDeleteProblem(scope.row.problem_id)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
            <div v-else class="empty-state">
              <el-empty description="暂无赛题数据，点击'创建赛题'开始添加吧！" />
            </div>
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showProblemDialog = false">关闭</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 创建赛题对话框 -->
        <el-dialog v-model="showCreateProblemDialog" title="创建赛题" width="600px">
          <el-form :model="createProblemForm" :rules="problemRules" ref="createProblemFormRef" label-width="120px">
            <el-form-item label="赛题标题" prop="title">
              <el-input v-model="createProblemForm.title" placeholder="请输入赛题标题" />
            </el-form-item>
            <el-form-item label="赛题描述" prop="description">
              <el-input v-model="createProblemForm.description" type="textarea" placeholder="请输入赛题描述" :rows="4" />
            </el-form-item>
            <el-form-item label="最大参赛队伍数" prop="max_teams">
              <el-input v-model.number="createProblemForm.max_teams" placeholder="请输入最大参赛队伍数" />
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showCreateProblemDialog = false">取消</el-button>
              <el-button type="primary" @click="handleCreateProblem">创建</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 更新赛题对话框 -->
        <el-dialog v-model="showUpdateProblemDialog" title="编辑赛题" width="600px">
          <el-form :model="updateProblemForm" :rules="problemRules" ref="updateProblemFormRef" label-width="120px">
            <el-form-item label="赛题标题" prop="title">
              <el-input v-model="updateProblemForm.title" placeholder="请输入赛题标题" />
            </el-form-item>
            <el-form-item label="赛题描述" prop="description">
              <el-input v-model="updateProblemForm.description" type="textarea" placeholder="请输入赛题描述" :rows="4" />
            </el-form-item>
            <el-form-item label="最大参赛队伍数" prop="max_teams">
              <el-input v-model.number="updateProblemForm.max_teams" placeholder="请输入最大参赛队伍数" />
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showUpdateProblemDialog = false">取消</el-button>
              <el-button type="primary" @click="handleUpdateProblem">保存</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import { showError, showSuccess, showWarning, showConfirm } from '../../utils/notification.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getCompetitions, createCompetition, updateCompetition, deleteCompetition } from '../../api/contest.js';
import { getProblemsByCompetition, createProblem, updateProblem, deleteProblem as deleteProblemApi } from '../../api/problem.js';

const competitions = ref([]);
const showCreateDialog = ref(false);
const showUpdateDialogVisible = ref(false);
const competitionFormRef = ref(null);
const updateFormRef = ref(null);
const currentCompetitionId = ref(null);

// 赛题管理相关
const showProblemDialog = ref(false);
const showCreateProblemDialog = ref(false);
const showUpdateProblemDialog = ref(false);
const currentCompetition = ref(null);
const problems = ref([]);
const createProblemForm = reactive({});
const updateProblemForm = reactive({});
const currentProblemId = ref(null);
const createProblemFormRef = ref(null);
const updateProblemFormRef = ref(null);

// 赛题表单验证规则
const problemRules = reactive({
  title: [
    { required: true, message: '请输入赛题标题', trigger: 'blur' },
    { min: 2, max: 200, message: '赛题标题长度在 2 到 200 个字符', trigger: 'blur' }
  ],
  max_teams: [
    { type: 'number', min: 0, message: '最大参赛队伍数必须大于等于0', trigger: 'blur' }
  ]
});

// 创建竞赛表单
const competitionForm = reactive({
  competition_name: '',
  session_no: '',
  school_id: null,
  sign_start: '',
  sign_end: '',
  competition_start: '',
  competition_end: '',
  fee_amount: 0,
  reward_rule: '',
  status: 'pending'
});

// 更新竞赛表单
const updateForm = reactive({
  competition_name: '',
  session_no: '',
  school_id: null,
  sign_start: '',
  sign_end: '',
  competition_start: '',
  competition_end: '',
  fee_amount: 0,
  reward_rule: '',
  status: 'pending'
});

// 表单验证规则
const competitionRules = reactive({
  competition_name: [
    { required: true, message: '请输入竞赛名称', trigger: 'blur' },
    { min: 2, max: 100, message: '竞赛名称长度在 2 到 100 个字符', trigger: 'blur' }
  ],
  session_no: [
    { required: true, message: '请输入届数', trigger: 'blur' }
  ],
  school_id: [
    { required: true, message: '请输入学校ID', trigger: 'blur' },
    { type: 'number', message: '学校ID必须是数字', trigger: 'blur' }
  ],
  sign_start: [
    { required: true, message: '请选择报名开始时间', trigger: 'change' }
  ],
  sign_end: [
    { required: true, message: '请选择报名结束时间', trigger: 'change' }
  ],
  competition_start: [
    { required: true, message: '请选择竞赛开始时间', trigger: 'change' }
  ],
  competition_end: [
    { required: true, message: '请选择竞赛结束时间', trigger: 'change' }
  ]
});

// 页面加载时获取竞赛列表
onMounted(() => {
  fetchCompetitions();
});

// 获取竞赛列表
const fetchCompetitions = async () => {
    try {
      const response = await getCompetitions();
      // 状态码映射：0→'pending'（未开始），1→'active'（进行中），2→'ended'（已结束）
      const mappedCompetitions = response.map(competition => ({
        ...competition,
        status: competition.status === 0 ? 'pending' : competition.status === 1 ? 'active' : 'ended'
      }));
      competitions.value = mappedCompetitions || [];
    } catch (error) {
      showError('获取竞赛列表失败：' + (error.response?.data?.message || error.message || error));
    }
  };

// 创建竞赛
const handleCreateCompetition = async () => {
  if (!competitionFormRef.value) return;
  
  await competitionFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        await createCompetition(competitionForm);
        showSuccess('竞赛创建成功！');
        showCreateDialog.value = false;
        // 重置表单
        Object.assign(competitionForm, {
          competition_name: '',
          session_no: '',
          school_id: null,
          sign_start: '',
          sign_end: '',
          competition_start: '',
          competition_end: '',
          fee_amount: 0,
          reward_rule: '',
          status: 'pending'
        });
        // 重新获取竞赛列表
        fetchCompetitions();
      } catch (error) {
        showError('创建失败：' + (error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 显示更新对话框
const showUpdateDialog = (competition) => {
  currentCompetitionId.value = competition.competition_id;
  Object.assign(updateForm, {
    competition_name: competition.competition_name,
    session_no: competition.session_no,
    school_id: competition.school_id,
    sign_start: competition.sign_start,
    sign_end: competition.sign_end,
    competition_start: competition.competition_start,
    competition_end: competition.competition_end,
    fee_amount: competition.fee_amount || 0,
    reward_rule: competition.reward_rule || '',
    status: competition.status
  });
  showUpdateDialogVisible.value = true;
};

// 更新竞赛
const handleUpdateCompetition = async () => {
  if (!updateFormRef.value) return;
  
  await updateFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        await updateCompetition(currentCompetitionId.value, updateForm);
        showSuccess('竞赛更新成功！');
        showUpdateDialogVisible.value = false;
        // 重新获取竞赛列表
        fetchCompetitions();
      } catch (error) {
        showError('更新失败：' + (error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 删除竞赛
const handleDeleteCompetition = async (competitionId) => {
  try {
    await showConfirm('警告', '确定要删除该竞赛吗？删除后无法恢复', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    });
    
    await deleteCompetition(competitionId);
    showSuccess('竞赛删除成功！');
    fetchCompetitions();
  } catch (error) {
    if (error !== 'cancel') {
      showError('删除失败：' + (error.response?.data?.message || error.message || error));
    }
  }
};

// 赛题管理方法

// 管理赛题
const manageProblems = async (competition) => {
  try {
    currentCompetition.value = competition;
    showProblemDialog.value = true;
    await fetchProblems(competition.competition_id);
  } catch (error) {
    showError('获取赛题列表失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 获取赛题列表
const fetchProblems = async (competitionId) => {
  try {
    const response = await getProblemsByCompetition(competitionId);
    problems.value = response || [];
  } catch (error) {
    showError('获取赛题列表失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 显示创建赛题对话框
const handleShowCreateProblemDialog = () => {
  // 重置表单
  Object.assign(createProblemForm, {
    title: '',
    description: '',
    max_teams: 0
  });
  showCreateProblemDialog.value = true;
};

// 创建赛题
const handleCreateProblem = async () => {
  if (!createProblemFormRef.value) return;
  
  await createProblemFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        const problemData = {
          ...createProblemForm,
          competition_id: currentCompetition.value.competition_id
        };
        await createProblem(problemData);
        showSuccess('赛题创建成功！');
        showCreateProblemDialog.value = false;
        // 重新获取赛题列表
        await fetchProblems(currentCompetition.value.competition_id);
      } catch (error) {
        showError('创建失败：' + (error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 显示更新赛题对话框
const handleShowUpdateProblemDialog = (problem) => {
  currentProblemId.value = problem.problem_id;
  Object.assign(updateProblemForm, {
    title: problem.title,
    description: problem.description || '',
    max_teams: problem.max_teams || 0
  });
  showUpdateProblemDialog.value = true;
};

// 更新赛题
const handleUpdateProblem = async () => {
  if (!updateProblemFormRef.value) return;
  
  await updateProblemFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        await updateProblem(currentProblemId.value, updateProblemForm);
        showSuccess('赛题更新成功！');
        showUpdateProblemDialog.value = false;
        // 重新获取赛题列表
        await fetchProblems(currentCompetition.value.competition_id);
      } catch (error) {
        showError('更新失败：' + (error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 删除赛题
const handleDeleteProblem = async (problemId) => {
  try {
    await showConfirm('警告', '确定要删除该赛题吗？删除后无法恢复', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    });
    
    await deleteProblemApi(problemId);
    showSuccess('赛题删除成功！');
    // 重新获取赛题列表
    await fetchProblems(currentCompetition.value.competition_id);
  } catch (error) {
    if (error !== 'cancel') {
      showError('删除失败：' + (error.response?.data?.message || error.message || error));
    }
  }
};
</script>

<style scoped>
.admin-competition {
  min-height: 100vh;
  background: #f5f7fa;
}

.main-layout {
  display: flex;
}

.main-content {
  flex: 1;
  padding: 30px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.page-header h2 {
  font-size: 28px;
  color: #2d3748;
  margin: 0;
}

.primary-btn {
  padding: 8px 16px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s;
}

.primary-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  margin-bottom: 20px;
}

.content-card h3 {
  font-size: 20px;
  color: #2d3748;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid #e2e8f0;
}

.empty-state {
  text-align: center;
  padding: 40px 0;
}

.dialog-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.dialog-header h3 {
  font-size: 18px;
  margin: 0;
  color: #2d3748;
}
</style>

