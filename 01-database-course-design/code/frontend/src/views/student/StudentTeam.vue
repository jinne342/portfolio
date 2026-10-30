<template>
  <div class="student-team">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>我的队伍</h2>
          <button class="primary-btn" @click="openCreateTeamDialog">创建队伍</button>
        </div>
        
        <!-- 标签页 -->
        <el-tabs v-model="activeTab" type="border-card">
          <!-- 我的队伍列表 -->
          <el-tab-pane label="我的队伍" name="my-teams">
            <div class="content-card">
              <h3>我的队伍</h3>
          <el-table v-if="teams.length > 0" :data="teams" stripe style="width: 100%">
            <el-table-column prop="team_name" label="队伍名称" width="200" />
            <el-table-column prop="competition_id" label="竞赛ID" width="120" />
            <el-table-column prop="captain_id" label="队长ID" width="120" />
            <el-table-column prop="guide_teacher" label="指导教师" width="150">
              <template #default="scope">
                {{ scope.row.guide_teacher }}
              </template>
            </el-table-column>
            <el-table-column prop="status" label="状态" width="120">
              <template #default="scope">
                <el-tag :type="scope.row.status === 1 ? 'success' : 'danger'">
                  {{ scope.row.status === 1 ? '活跃' : '停用' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="create_time" label="创建时间" width="180" />
            <el-table-column label="操作" width="300" fixed="right">
              <template #default="scope">
                <el-button size="small" type="primary" @click="viewTeamMembers(scope.row.team_id)">查看成员</el-button>
                <el-button size="small" type="warning" @click="viewTeamDetails(scope.row)">详情</el-button>
                <el-button size="small" type="info" @click="openRequestTeacherDialog(scope.row.team_id)">请求指导老师</el-button>
                <el-button v-if="scope.row.status === 'pending'" size="small" type="danger" @click="handleDeleteTeam(scope.row.team_id)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-else class="empty-state">
            <el-empty description="暂无队伍，点击'创建队伍'开始组建队伍吧！" />
          </div>
        </div>
      </el-tab-pane>
      
      <!-- 我的邀请列表 -->
      <el-tab-pane label="我的邀请" name="my-invites">
        <div class="content-card">
          <h3>我的邀请</h3>
          <el-table v-if="teamInvites.length > 0" :data="teamInvites" stripe style="width: 100%">
            <el-table-column prop="team_id" label="队伍ID" width="120" />
            <el-table-column prop="from_user_id" label="邀请人" width="120" />
            <el-table-column prop="status" label="状态" width="120">
              <template #default="scope">
                <el-tag :type="scope.row.status === 0 ? 'warning' : scope.row.status === 1 ? 'success' : 'danger'">
                  {{ scope.row.status === 0 ? '待处理' : scope.row.status === 1 ? '已接受' : '已拒绝' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="create_time" label="创建时间" width="180" />
            <el-table-column label="操作" width="200" fixed="right">
              <template #default="scope">
                <el-button v-if="scope.row.status === 0" size="small" type="success" @click="acceptInvite(scope.row)">接受</el-button>
                <el-button v-if="scope.row.status === 0" size="small" type="danger" @click="rejectInvite(scope.row)">拒绝</el-button>
                <el-button size="small" type="primary" @click="viewInviteDetails(scope.row)">详情</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-else class="empty-state">
            <el-empty description="暂无邀请" />
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
    
    <!-- 创建队伍对话框 -->
    <el-dialog v-model="showCreateTeamDialog" title="创建队伍" width="500px">
          <el-form :model="newTeamForm" :rules="createTeamRules" ref="createTeamFormRef" label-width="100px">
            <el-form-item label="队伍名称" prop="team_name">
              <el-input v-model="newTeamForm.team_name" placeholder="请输入队伍名称" />
            </el-form-item>
            <el-form-item label="竞赛名称" prop="competition_id">
              <el-select v-model.number="newTeamForm.competition_id" placeholder="请选择竞赛">
                <el-option v-for="competition in competitions" :key="competition.competition_id" 
                  :label="competition.competition_name" :value="competition.competition_id" />
              </el-select>
            </el-form-item>
            <!-- 自动填充并隐藏的字段 -->
            <el-form-item prop="school_id" v-show="false">
              <el-input v-model.number="newTeamForm.school_id" />
            </el-form-item>
            <el-form-item prop="captain_id" v-show="false">
              <el-input v-model="newTeamForm.captain_id" />
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showCreateTeamDialog = false">取消</el-button>
              <el-button type="primary" @click="handleCreateTeam">创建</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 队伍详情对话框 -->
        <el-dialog v-model="showTeamDetailsDialog" :title="'队伍详情 - ' + currentTeam.team_name" width="600px">
          <div class="team-details" v-if="currentTeam.team_id">
            <el-descriptions :column="1" border>
              <el-descriptions-item label="队伍ID">{{ currentTeam.team_id }}</el-descriptions-item>
              <el-descriptions-item label="队伍名称">{{ currentTeam.team_name }}</el-descriptions-item>
              <el-descriptions-item label="竞赛ID">{{ currentTeam.competition_id }}</el-descriptions-item>
              <el-descriptions-item label="学校ID">{{ currentTeam.school_id }}</el-descriptions-item>
              <el-descriptions-item label="队长ID">{{ currentTeam.captain_id }}</el-descriptions-item>
              <el-descriptions-item label="状态">
                <el-tag :type="currentTeam.status === 1 ? 'success' : 'danger'">
                  {{ currentTeam.status === 1 ? '活跃' : '停用' }}
                </el-tag>
              </el-descriptions-item>
              <el-descriptions-item label="创建时间">{{ currentTeam.create_time }}</el-descriptions-item>
            </el-descriptions>
          </div>
          <div v-else class="loading-state">
            <el-skeleton :rows="6" animated />
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showTeamDetailsDialog = false">关闭</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 队伍成员对话框 -->
        <el-dialog v-model="showTeamMembersDialog" title="队伍成员" width="500px">
          <div v-if="currentTeamMembers.length > 0">
            <el-table :data="currentTeamMembers" stripe style="width: 100%">
              <el-table-column prop="user_id" label="用户ID" width="120" />
              <el-table-column prop="join_time" label="加入时间" width="180" />
              <el-table-column label="操作" width="100" fixed="right">
                <template #default="scope">
                  <el-button size="small" type="danger" @click="removeMember(scope.row.user_id)">移除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div v-else class="empty-state">
            <el-empty description="暂无成员" />
          </div>
          
          <!-- 邀请成员 -->
          <div class="invite-member">
            <h4>邀请成员</h4>
            <el-form :model="inviteMemberForm" :rules="inviteMemberRules" ref="inviteMemberFormRef" label-width="80px">
              <el-form-item label="用户ID" prop="user_id">
                <el-input v-model.number="inviteMemberForm.user_id" placeholder="请输入要邀请的用户ID" />
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="handleInviteMember">发送邀请</el-button>
              </el-form-item>
            </el-form>
          </div>
          
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showTeamMembersDialog = false">关闭</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 邀请详情对话框 -->
        <el-dialog v-model="showInviteDetailsDialog" title="邀请详情" width="500px">
          <div class="invite-details" v-if="currentInvite.invite_id">
            <el-descriptions :column="1" border>
              <el-descriptions-item label="邀请ID">{{ currentInvite.invite_id }}</el-descriptions-item>
              <el-descriptions-item label="队伍ID">{{ currentInvite.team_id }}</el-descriptions-item>
              <el-descriptions-item label="邀请人">{{ currentInvite.from_user_id }}</el-descriptions-item>
              <el-descriptions-item label="状态">
                <el-tag :type="currentInvite.status === 0 ? 'warning' : currentInvite.status === 1 ? 'success' : 'danger'">
                  {{ currentInvite.status === 0 ? '待处理' : currentInvite.status === 1 ? '已接受' : '已拒绝' }}
                </el-tag>
              </el-descriptions-item>
              <el-descriptions-item label="创建时间">{{ currentInvite.create_time }}</el-descriptions-item>
            </el-descriptions>
            
            <div class="invite-actions" v-if="currentInvite.status === 0">
              <el-button type="success" @click="acceptInvite(currentInvite)">接受邀请</el-button>
              <el-button type="danger" @click="rejectInvite(currentInvite)">拒绝邀请</el-button>
            </div>
          </div>
          <div v-else class="loading-state">
            <el-skeleton :rows="6" animated />
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showInviteDetailsDialog = false">关闭</el-button>
            </span>
          </template>
        </el-dialog>

        <!-- 请求指导老师对话框 -->
        <el-dialog v-model="showRequestTeacherDialog" title="请求指导老师" width="500px">
          <el-form :model="requestTeacherForm" :rules="requestTeacherRules" ref="requestTeacherFormRef" label-width="100px">
            <el-form-item label="教师用户ID" prop="teacher_user_id">
              <el-input v-model="requestTeacherForm.teacher_user_id" placeholder="请输入指导老师的用户ID" />
            </el-form-item>
            <el-form-item label="队伍ID" prop="team_id">
              <el-input v-model.number="requestTeacherForm.team_id" disabled />
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showRequestTeacherDialog = false">取消</el-button>
              <el-button type="primary" @click="handleRequestTeacher">发送请求</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, nextTick, watch } from 'vue';
import { useRoute } from 'vue-router';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getTeams, getTeamById, createTeam, deleteTeam, getTeamMembers, addTeamMember, removeTeamMember, createTeamInvite, getTeamInvitesByUser, handleTeamInvite } from '../../api/team.js';
import { createTeacherTeam, getTeacherTeamsByTeam, studentRequestTeacherTeam } from '../../api/teacherTeam.js';
import { getCompetitions } from '../../api/contest.js';
import { useUserStore } from '../../store/user.js';
import { showError, showSuccess, showWarning, showConfirm, showInfo } from '../../utils/notification.js';

const teams = ref([]);
const competitions = ref([]);
const activeTab = ref('my-teams');
const showCreateTeamDialog = ref(false);
const showTeamMembersDialog = ref(false);
const showTeamDetailsDialog = ref(false);
const currentTeamId = ref(null);
const currentTeamMembers = ref([]);
const currentTeam = ref({});
const createTeamFormRef = ref(null);
const inviteMemberFormRef = ref(null);
// 邀请列表相关
const teamInvites = ref([]);
const showInviteDetailsDialog = ref(false);
const currentInvite = ref({});

// 获取用户信息
const userStore = useUserStore();
// 获取路由信息
const route = useRoute();

// 创建队伍表单
const newTeamForm = reactive({
  team_name: '',
  competition_id: null,
  school_id: null,
  captain_id: null
});

// 创建队伍表单验证规则
const createTeamRules = reactive({
  team_name: [
    { required: true, message: '请输入队伍名称', trigger: 'blur' },
    { min: 2, max: 50, message: '队伍名称长度在 2 到 50 个字符', trigger: 'blur' }
  ],
  competition_id: [
    { required: true, message: '请选择竞赛', trigger: 'blur' },
    { type: 'number', message: '竞赛ID必须是数字', trigger: 'blur' }
  ],
  // 队长ID和学校ID将自动填充，不需要验证
  school_id: [
    { required: false }
  ],
  captain_id: [
    { required: false }
  ]
});

// 邀请成员表单
const inviteMemberForm = reactive({
  user_id: null
});

// 邀请成员表单验证规则
const inviteMemberRules = reactive({
  user_id: [
    { required: true, message: '请输入用户ID', trigger: 'blur' },
    { type: 'number', message: '用户ID必须是数字', trigger: 'blur' }
  ]
});

// 请求指导老师对话框相关
const showRequestTeacherDialog = ref(false);
const requestTeacherFormRef = ref(null);
const requestTeacherForm = reactive({
  teacher_user_id: '',
  team_id: null
});

// 请求指导老师表单验证规则
const requestTeacherRules = reactive({
  teacher_user_id: [
    { required: true, message: '请输入教师用户ID', trigger: 'blur' }
  ],
  team_id: [
    { required: true, message: '队伍ID不能为空', trigger: 'blur' },
    { type: 'number', message: '队伍ID必须是数字', trigger: 'blur' }
  ]
});

// 处理从URL参数传递的竞赛ID
const handleCompetitionIdParam = async () => {
  const competitionId = route.query.competitionId;
  if (competitionId) {
    // 确保竞赛列表已加载
    if (competitions.value.length === 0) {
      await fetchCompetitions();
    }
    
    // 检查该竞赛是否存在且状态为0（可报名）
    const competition = competitions.value.find(c => c.competition_id === Number(competitionId));
    if (competition) {
      // 打开创建队伍对话框并自动选择该竞赛
      await openCreateTeamDialog();
      newTeamForm.competition_id = Number(competitionId);
    } else {
      showError('指定的竞赛不存在或不可报名');
    }
  }
};

// 监听URL参数变化
watch(() => route.query.competitionId, async (newCompetitionId) => {
  if (newCompetitionId) {
    await handleCompetitionIdParam();
  }
});

// 页面加载时获取队伍列表
onMounted(async () => {
  fetchTeams();
  await fetchCompetitions();
  fetchTeamInvites();
  
  // 检查URL参数中是否有competitionId
  await handleCompetitionIdParam();
});

// 获取用户的邀请列表
const fetchTeamInvites = async () => {
  try {
    const response = await getTeamInvitesByUser();
    teamInvites.value = response || [];
  } catch (error) {
    showError('获取邀请列表失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 接受邀请
const acceptInvite = async (invite) => {
  try {
    await showConfirm('提示', '确定要接受该邀请吗？');
    
    await handleTeamInvite(invite.invite_id, { status: 1 });
    showSuccess('邀请已接受！');
    // 重新获取邀请列表和队伍列表
    fetchTeamInvites();
    fetchTeams();
  } catch (error) {
    if (error !== 'cancel') {
      showError('接受邀请失败：' + (error.response?.data?.detail || error.response?.data?.message || error.message || error));
    }
  }
};

// 拒绝邀请
const rejectInvite = async (invite) => {
  try {
    await showConfirm('提示', '确定要拒绝该邀请吗？');
    
    await handleTeamInvite(invite.invite_id, { status: 2 });
    showSuccess('邀请已拒绝！');
    // 重新获取邀请列表
    fetchTeamInvites();
  } catch (error) {
    if (error !== 'cancel') {
      showError('拒绝邀请失败：' + (error.response?.data?.detail || error.response?.data?.message || error.message || error));
    }
  }
};

// 查看邀请详情
const viewInviteDetails = (invite) => {
  currentInvite.value = invite;
  showInviteDetailsDialog.value = true;
};

// 打开创建队伍对话框
const openCreateTeamDialog = () => {
  newTeamForm.captain_id = String(userStore.userInfo.user_id || '');
  newTeamForm.school_id = Number(userStore.userInfo.school_id || 0);
  showCreateTeamDialog.value = true;
};

// 获取队伍列表
const fetchTeams = async () => {
  try {
    // 获取当前用户的user_id
    const userId = userStore.userInfo?.user_id;
    console.log('当前用户ID:', userId);
    if (!userId) {
      showWarning('用户未登录，无法获取队伍信息');
      return;
    }
    
    // 传递user_id参数，只获取当前用户所在的队伍
    console.log('调用getTeams API，参数:', { userId });
    const response = await getTeams(null, userId);
    console.log('getTeams API响应:', response);
    teams.value = response || [];
    console.log('更新后的teams.value:', teams.value);
    
    // 为每个队伍获取指导教师信息
    for (const team of teams.value) {
      try {
        const teacherAssociations = await getTeacherTeamsByTeam(team.team_id);
        console.log(`队伍 ${team.team_id} 的教师关联信息:`, teacherAssociations);
        
        // 找到已确认的指导教师
        const confirmedTeacher = teacherAssociations.find(ta => ta.confirm_status === 'confirmed');
        if (confirmedTeacher) {
          team.guide_teacher = confirmedTeacher.teacher_name || '未知教师';
        } else {
          team.guide_teacher = '未确认';
        }
      } catch (error) {
        console.error(`获取队伍 ${team.team_id} 的指导教师信息失败:`, error);
        team.guide_teacher = '获取失败';
      }
    }
  } catch (error) {
    console.error('获取队伍列表失败:', error);
    showError('获取队伍列表失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 获取竞赛列表
const fetchCompetitions = async () => {
  try {
    const response = await getCompetitions();
    // 只显示状态为0（可报名）的竞赛
    competitions.value = (response || []).filter(competition => competition.status === 0);
  } catch (error) {
    showError('获取竞赛列表失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 创建队伍
const handleCreateTeam = async () => {
  if (!createTeamFormRef.value) return;
  
  await createTeamFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        console.log('创建队伍表单数据:', JSON.stringify(newTeamForm, null, 2));
        console.log('captain_id类型:', typeof newTeamForm.captain_id);
        console.log('school_id类型:', typeof newTeamForm.school_id);
        console.log('competition_id类型:', typeof newTeamForm.competition_id);
        
        // 验证当前用户是否已在该竞赛中加入其他队伍
        const hasTeamInCompetition = teams.value.some(team => 
          team.competition_id === newTeamForm.competition_id && team.team_id !== newTeamForm.team_id
        );
        
        if (hasTeamInCompetition) {
          showWarning('您已在该竞赛中加入了其他队伍，同一竞赛只能加入一个队伍');
          return;
        }
        
        await createTeam(newTeamForm);
        showSuccess('队伍创建成功！');
        showCreateTeamDialog.value = false;
        // 重置表单
        Object.assign(newTeamForm, {
          team_name: '',
          competition_id: null,
          school_id: null,
          captain_id: null
        });
        // 重新获取队伍列表
        fetchTeams();
      } catch (error) {
        console.error('创建队伍失败，错误详情:', error);
        showError('创建队伍失败：' + (error.response?.data?.detail || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 删除队伍
const handleDeleteTeam = async (teamId) => {
  try {
    await showConfirm('警告', '确定要删除该队伍吗？删除后无法恢复');
    
    await deleteTeam(teamId);
    showSuccess('队伍删除成功！');
    fetchTeams();
  } catch (error) {
    if (error !== 'cancel') {
      showError('删除队伍失败：' + (error.response?.data?.message || error.message || error));
    }
  }
};

// 查看队伍成员
const viewTeamMembers = async (teamId) => {
  console.log('viewTeamMembers 被调用，teamId:', teamId);
  currentTeamId.value = teamId;
  console.log('currentTeamId.value 已设置:', currentTeamId.value);
  
  // 先获取成员数据
  await fetchTeamMembers(teamId);
  
  console.log('viewTeamMembers - 获取数据后 currentTeamMembers:', currentTeamMembers.value);
  console.log('viewTeamMembers - currentTeamMembers长度:', currentTeamMembers.value.length);
  
  // 使用nextTick确保数据更新后再显示对话框
  await nextTick();
  console.log('viewTeamMembers - nextTick 完成');
  
  // 显示对话框
  showTeamMembersDialog.value = true;
  console.log('viewTeamMembers - showTeamMembersDialog.value 已设置:', showTeamMembersDialog.value);
  
  // 再次检查数据
  await nextTick();
  console.log('viewTeamMembers - 对话框显示后 currentTeamMembers:', currentTeamMembers.value);
};

// 获取队伍成员
const fetchTeamMembers = async (teamId) => {
  try {
    console.log('fetchTeamMembers 被调用，teamId:', teamId);
    const response = await getTeamMembers(teamId);
    console.log('获取队伍成员API响应:', response);
    console.log('响应类型:', typeof response);
    console.log('响应是否为数组:', Array.isArray(response));
    currentTeamMembers.value = response || [];
    console.log('currentTeamMembers.value 已设置:', currentTeamMembers.value);
    console.log('currentTeamMembers长度:', currentTeamMembers.value.length);
  } catch (error) {
    console.error('获取队伍成员错误:', error);
    console.error('错误响应:', error.response);
    showError('获取队伍成员失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 邀请成员
const handleInviteMember = async () => {
  if (!inviteMemberFormRef.value) return;
  
  await inviteMemberFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // 获取当前竞赛ID
        const currentTeamInfo = teams.value.find(team => team.team_id === currentTeamId.value);
        if (!currentTeamInfo) {
          showError('获取队伍信息失败');
          return;
        }
        
        // 调用创建邀请API
        await createTeamInvite({
          team_id: currentTeamId.value,
          to_user_id: inviteMemberForm.user_id.toString()
        });
        showSuccess('邀请发送成功！');
        // 重置表单
        inviteMemberForm.user_id = null;
        // 重新获取队伍成员
        fetchTeamMembers(currentTeamId.value);
      } catch (error) {
        showError('邀请失败：' + (error.response?.data?.detail || error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请输入用户ID');
      return false;
    }
  });
};

// 移除成员
const removeMember = async (userId) => {
  try {
    await showConfirm('警告', '确定要移除该成员吗？');
    
    await removeTeamMember(currentTeamId.value, userId);
    showSuccess('成员移除成功！');
    fetchTeamMembers(currentTeamId.value);
  } catch (error) {
    if (error !== 'cancel') {
      showError('移除成员失败：' + (error.response?.data?.message || error.message || error));
    }
  }
};

// 查看队伍详情
const viewTeamDetails = async (team) => {
  currentTeam.value = team;
  showTeamDetailsDialog.value = true;
  
  try {
    // 获取完整的队伍详情
    const response = await getTeamById(team.team_id);
    currentTeam.value = response || team;
  } catch (error) {
    showError('获取队伍详情失败：' + (error.response?.data?.message || error.message || error));
    // 保持显示基本信息
  }
};

// 打开请求指导老师对话框
const openRequestTeacherDialog = (teamId) => {
  requestTeacherForm.team_id = teamId;
  requestTeacherForm.teacher_user_id = '';
  showRequestTeacherDialog.value = true;
};

// 处理发送指导老师请求
const handleRequestTeacher = async () => {
  if (!requestTeacherFormRef.value) return;
  
  await requestTeacherFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // 检查队伍是否已经有指导老师
        const existingTeacherTeams = await getTeacherTeamsByTeam(requestTeacherForm.team_id);
        if (existingTeacherTeams && existingTeacherTeams.length > 0) {
          const activeTeacherTeam = existingTeacherTeams.find(item => item.confirm_status !== 'rejected');
          if (activeTeacherTeam) {
            showWarning('该队伍已经有指导老师，无法重复请求');
            return;
          }
        }
        
        // 发送请求
        await studentRequestTeacherTeam({
          user_id: requestTeacherForm.teacher_user_id,
          team_id: requestTeacherForm.team_id
        });
        
        showSuccess('指导老师请求已发送！');
        showRequestTeacherDialog.value = false;
      } catch (error) {
        showError('发送请求失败：' + (error.response?.data?.detail || error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};
</script>

<style scoped>
.student-team {
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

.invite-member {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #e2e8f0;
}

.invite-member h4 {
  font-size: 16px;
  color: #2d3748;
  margin-bottom: 12px;
}

.invite-details {
  margin-bottom: 20px;
}

.invite-actions {
  margin-top: 20px;
  display: flex;
  gap: 10px;
  justify-content: center;
}

.loading-state {
  padding: 20px 0;
}
</style>

