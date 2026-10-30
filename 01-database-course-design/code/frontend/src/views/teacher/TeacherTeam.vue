<template>
  <div class="teacher-team">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>指导队伍</h2>
        </div>
        <div class="content-card">
          <el-table v-loading="loading" :data="teams" style="width: 100%">
            <el-table-column prop="team_id" label="队伍ID" width="100" />
            <el-table-column prop="team_name" label="队伍名称" />
            <el-table-column prop="members" label="队员" width="300">
              <template #default="scope">
                <div v-if="scope.row.members && scope.row.members.length">
                  <div v-for="(member, index) in scope.row.members" :key="member.user_id">
                    {{ member.username }}
                    <span v-if="index < scope.row.members.length - 1">, </span>
                  </div>
                </div>
                <span v-else>无</span>
              </template>
            </el-table-column>
            <el-table-column prop="assign_method" label="分配方式" width="150">
              <template #default="scope">
                <span v-if="scope.row.assign_method === 'system'">系统分配</span>
                <span v-else-if="scope.row.assign_method === 'manual'">手动分配</span>
                <span v-else-if="scope.row.assign_method === 'request'">学生申请</span>
                <span v-else>{{ scope.row.assign_method }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="confirm_status" label="确认状态" width="150">
              <template #default="scope">
                <el-tag v-if="scope.row.confirm_status === 'confirmed'" type="success">已确认</el-tag>
                <el-tag v-else-if="scope.row.confirm_status === 'pending'" type="warning">待确认</el-tag>
                <el-tag v-else-if="scope.row.confirm_status === 'rejected'" type="danger">已拒绝</el-tag>
                <el-tag v-else>{{ scope.row.confirm_status }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="assign_time" label="分配时间" width="200" />
            <el-table-column label="操作" width="250" fixed="right">
              <template #default="scope">
                <el-button 
                  type="primary" 
                  size="small"
                  @click="handleConfirm(scope.row)"
                  v-if="scope.row.confirm_status === 'pending'"
                >
                  确认指导
                </el-button>
                <el-button 
                  type="danger" 
                  size="small"
                  @click="handleReject(scope.row)"
                  v-if="scope.row.confirm_status === 'pending'"
                >
                  拒绝指导
                </el-button>
                <el-button 
                  type="info" 
                  size="small"
                  @click="handleViewDetails(scope.row)"
                >
                  查看详情
                </el-button>
                <el-button 
                  type="warning" 
                  size="small"
                  @click="handleDelete(scope.row)"
                  v-if="scope.row.confirm_status !== 'pending'"
                >
                  解除关联
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </main>
    </div>
    
    <!-- 队伍详情对话框 -->
    <el-dialog v-model="showDetailDialog" :title="'队伍详情 - ' + currentTeam.team_name" width="700px">
      <div class="team-details" v-if="currentTeam.team_id">
        <el-descriptions :column="1" border>
          <el-descriptions-item label="队伍基本信息">
            <el-row :gutter="20">
              <el-col :span="12">
                <div class="detail-item">
                  <strong>队伍ID：</strong>{{ currentTeam.team_id }}
                </div>
              </el-col>
              <el-col :span="12">
                <div class="detail-item">
                  <strong>队伍名称：</strong>{{ currentTeam.team_name }}
                </div>
              </el-col>
              <el-col :span="12">
                <div class="detail-item">
                  <strong>分配方式：</strong>
                  <span v-if="currentTeam.assign_method === 'system'">系统分配</span>
                  <span v-else-if="currentTeam.assign_method === 'manual'">手动分配</span>
                  <span v-else-if="currentTeam.assign_method === 'request'">学生申请</span>
                  <span v-else>{{ currentTeam.assign_method }}</span>
                </div>
              </el-col>
              <el-col :span="12">
                <div class="detail-item">
                  <strong>确认状态：</strong>
                  <el-tag v-if="currentTeam.confirm_status === 'confirmed'" type="success">已确认</el-tag>
                  <el-tag v-else-if="currentTeam.confirm_status === 'pending'" type="warning">待确认</el-tag>
                  <el-tag v-else-if="currentTeam.confirm_status === 'rejected'" type="danger">已拒绝</el-tag>
                  <el-tag v-else>{{ currentTeam.confirm_status }}</el-tag>
                </div>
              </el-col>
              <el-col :span="12">
                <div class="detail-item">
                  <strong>分配时间：</strong>{{ currentTeam.assign_time }}
                </div>
              </el-col>
              <el-col :span="12">
                <div class="detail-item">
                  <strong>队长ID：</strong>{{ currentTeam.captain_id || '未知' }}
                </div>
              </el-col>
            </el-row>
          </el-descriptions-item>
          
          <el-descriptions-item label="队员信息">
            <div v-if="currentTeam.members && currentTeam.members.length">
              <el-table :data="currentTeam.members" size="small" style="width: 100%">
                <el-table-column prop="user_id" label="用户ID" width="100" />
                <el-table-column prop="username" label="姓名" />
                <el-table-column prop="college" label="学院" />
                <el-table-column prop="major" label="专业" />
              </el-table>
            </div>
            <span v-else class="empty-text">暂无队员</span>
          </el-descriptions-item>
          
          <el-descriptions-item label="竞赛信息">
            <div class="detail-item">
              <strong>竞赛ID：</strong>{{ currentTeam.competition_id || '未知' }}
            </div>
          </el-descriptions-item>
        </el-descriptions>
      </div>
      <div v-else class="loading-state">
        <el-skeleton :rows="8" animated />
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="showDetailDialog = false">关闭</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { request } from '../../api';
import { getTeacherTeams, confirmTeacherTeam, rejectTeacherTeam, deleteTeacherTeam } from '../../api/teacherTeam';
import { useUserStore } from '../../store/user';
import { showError, showSuccess, showConfirm } from '../../utils/notification.js';

const userStore = useUserStore();
const teams = ref([]);
const loading = ref(false);

// 详情对话框相关
const showDetailDialog = ref(false);
const currentTeam = ref({
  team_id: null,
  team_name: '',
  members: [],
  assign_method: '',
  confirm_status: '',
  assign_time: '',
  user_id: null,
  captain_id: null,
  competition_id: null
});

// 获取队伍详情
const getTeamDetails = async (teamId) => {
  try {
    // 假设后端提供了获取队伍详情的API
    const response = await request.get(`/teams/${teamId}/`);
    return response || {};
  } catch (error) {
    console.error('获取队伍详情失败:', error);
    return {};
  }
};

// 获取队伍成员信息
const getTeamMembers = async (teamId) => {
  try {
    // 假设后端提供了获取队伍成员的API
    const response = await request.get(`/team-members/team/${teamId}/`);
    return response || [];
  } catch (error) {
    console.error('获取队伍成员失败:', error);
    return [];
  }
};

// 合并队伍信息
const mergeTeamInfo = async (teacherTeam) => {
  try {
    // 获取队伍基本信息
    const teamDetails = await getTeamDetails(teacherTeam.team_id);
    // 获取队伍成员信息
    const teamMembers = await getTeamMembers(teacherTeam.team_id);
    
    // 合并信息
    return {
      ...teacherTeam,
      team_name: teamDetails.team_name || '未知队伍',
      captain_id: teamDetails.captain_id,
      competition_id: teamDetails.competition_id,
      members: teamMembers.map(member => ({
        user_id: member.user_id,
        username: member.username || member.student_name
      }))
    };
  } catch (error) {
    console.error('合并队伍信息失败:', error);
    return teacherTeam;
  }
};

const fetchTeams = async () => {
  loading.value = true;
  try {
    console.log('当前用户ID:', userStore.userInfo.user_id);
    console.log('完整用户信息:', userStore.userInfo);
    // 确保用户ID存在
    if (!userStore.userInfo.user_id) {
      console.error('用户ID不存在');
      showError('用户未登录或登录信息不完整');
      loading.value = false;
      return;
    }
    
    const response = await getTeacherTeams(userStore.userInfo.user_id);
    console.log('API响应:', response);
    
    // 检查响应数据格式
    if (!response || typeof response !== 'object') {
      console.error('响应数据格式不正确:', response);
      showError('获取队伍列表失败：响应数据格式不正确');
      loading.value = false;
      return;
    }
    
    // 处理每个队伍，获取详细信息
    const teamList = response || [];
    console.log('处理前的队伍列表:', teamList);
    
    const teamPromises = teamList.map(mergeTeamInfo);
    const mergedTeams = await Promise.all(teamPromises);
    
    console.log('合并后的队伍列表:', mergedTeams);
    teams.value = mergedTeams;
  } catch (error) {
    console.error('获取队伍列表错误:', error);
    console.error('错误详情:', error.response);
    showError('获取队伍列表失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    loading.value = false;
  }
};

const handleConfirm = async (row) => {
  try {
    await confirmTeacherTeam(row.user_id, row.team_id);
    showSuccess('确认指导成功');
    row.confirm_status = 'confirmed';
  } catch (error) {
    showError('确认指导失败：' + (error.response?.data?.message || error.message || error));
  }
};

const handleReject = async (row) => {
  try {
    await rejectTeacherTeam(row.user_id, row.team_id);
    showSuccess('拒绝指导成功');
    row.confirm_status = 'rejected';
  } catch (error) {
    showError('拒绝指导失败：' + (error.response?.data?.message || error.message || error));
  }
};

const handleDelete = async (row) => {
  try {
    await showConfirm('提示', '确定要解除与该队伍的指导关联吗？', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    });
    
    await deleteTeacherTeam(row.user_id, row.team_id);
    showSuccess('解除关联成功');
    // 从列表中移除该关联
    const index = teams.value.findIndex(item => item.user_id === row.user_id && item.team_id === row.team_id);
    if (index !== -1) {
      teams.value.splice(index, 1);
    }
  } catch (error) {
    if (error !== 'cancel') {
      showError('解除关联失败：' + (error.response?.data?.message || error.message || error));
    }
  }
};

const handleViewDetails = async (row) => {
  // 查看队伍详情
  try {
    const teamDetails = await mergeTeamInfo(row);
    currentTeam.value = teamDetails;
    showDetailDialog.value = true;
  } catch (error) {
    console.error('查看队伍详情失败:', error);
    showError('查看队伍详情失败');
  }
};

onMounted(() => {
  fetchTeams();
});
</script>

<style scoped>
.teacher-team {
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

.page-header h2 {
  font-size: 28px;
  color: #2d3748;
  margin-bottom: 20px;
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
</style>

