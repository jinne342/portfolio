<template>
  <div class="admin-registration-audit">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>竞赛报名审核</h2>
        </div>
        
        <!-- 报名列表 -->
        <div class="content-card">
          <h3>待审核报名</h3>
          <el-table v-if="registrations.length > 0" :data="registrations" stripe style="width: 100%">
            <el-table-column prop="reg_id" label="报名ID" width="100" />
            <el-table-column prop="user_id" label="用户ID" width="120" />
            <el-table-column prop="user_name" label="用户名" width="150" />
            <el-table-column prop="competition_id" label="竞赛ID" width="100" />
            <el-table-column prop="competition_name" label="竞赛名称" min-width="200" />
            <el-table-column prop="team_id" label="团队ID" width="100" />
            <el-table-column prop="team_name" label="团队名称" width="150" />
            <el-table-column prop="registration_time" label="报名时间" width="180" />
            <el-table-column prop="audit_status" label="审核状态" width="120">
              <template #default="scope">
                <el-tag :type="scope.row.audit_status === 0 ? 'warning' : scope.row.audit_status === 1 ? 'success' : 'danger'">
                  {{ scope.row.audit_status === 0 ? '待审核' : scope.row.audit_status === 1 ? '已通过' : '已驳回' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column label="操作" width="200" fixed="right">
              <template #default="scope">
                <el-button 
                  v-if="scope.row.audit_status === 0"
                  size="small" 
                  type="success" 
                  @click="handleAuditPass(scope.row)"
                >通过</el-button>
                <el-button 
                  v-if="scope.row.audit_status === 0"
                  size="small" 
                  type="danger" 
                  @click="handleAuditReject(scope.row)"
                >驳回</el-button>
                <el-button 
                  v-if="scope.row.audit_status !== 0"
                  size="small" 
                  type="info" 
                  @click="showAuditDetails(scope.row)"
                >查看详情</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-else class="empty-state">
            <el-empty description="暂无待审核报名" />
          </div>
        </div>
        
        <!-- 审核对话框 -->
        <el-dialog v-model="showAuditDialog" :title="dialogTitle" width="500px">
          <el-form :model="auditForm" label-width="120px">
            <el-form-item label="报名ID">
              <el-input v-model="auditForm.reg_id" disabled />
            </el-form-item>
            <el-form-item label="用户">
              <el-input v-model="auditForm.user_name" disabled />
            </el-form-item>
            <el-form-item label="竞赛">
              <el-input v-model="auditForm.competition_name" disabled />
            </el-form-item>
            <el-form-item label="团队">
              <el-input v-model="auditForm.team_name" disabled />
            </el-form-item>
            <el-form-item label="报名时间">
              <el-input v-model="auditForm.registration_time" disabled />
            </el-form-item>
            <el-form-item label="审核备注" prop="audit_remark">
              <el-input 
                v-model="auditForm.audit_remark" 
                type="textarea" 
                placeholder="请输入审核备注" 
                :rows="3" 
                :disabled="!isAuditing"
              />
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showAuditDialog = false">关闭</el-button>
              <el-button 
                v-if="isAuditing && auditAction === 'pass'" 
                type="success" 
                @click="confirmAuditPass"
              >确认通过</el-button>
              <el-button 
                v-if="isAuditing && auditAction === 'reject'" 
                type="danger" 
                @click="confirmAuditReject"
              >确认驳回</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, computed } from 'vue';
import { showError, showSuccess } from '../../utils/notification.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getRegistrations, updateRegistration } from '../../api/registration.js';

const registrations = ref([]);
const showAuditDialog = ref(false);
const currentRegistration = ref(null);
const auditAction = ref('');

// 审核表单
const auditForm = reactive({
  reg_id: '',
  user_name: '',
  competition_name: '',
  team_name: '',
  registration_time: '',
  audit_remark: ''
});

// 计算属性
const dialogTitle = computed(() => {
  if (auditAction.value === 'pass') return '审核通过';
  if (auditAction.value === 'reject') return '审核驳回';
  return '审核详情';
});

const isAuditing = computed(() => {
  return auditAction.value === 'pass' || auditAction.value === 'reject';
});

// 页面加载时获取报名列表
onMounted(() => {
  fetchRegistrations();
});

// 获取报名列表
const fetchRegistrations = async () => {
  try {
    // 获取所有报名记录，包括待审核和已审核的
    const response = await getRegistrations();
    registrations.value = response || [];
  } catch (error) {
    showError('获取报名列表失败：' + (error.response?.data?.message || error.message));
  }
};

// 处理审核通过
const handleAuditPass = (registration) => {
  currentRegistration.value = registration;
  auditAction.value = 'pass';
  populateAuditForm(registration);
  showAuditDialog.value = true;
};

// 处理审核驳回
const handleAuditReject = (registration) => {
  currentRegistration.value = registration;
  auditAction.value = 'reject';
  populateAuditForm(registration);
  showAuditDialog.value = true;
};

// 查看审核详情
const showAuditDetails = (registration) => {
  currentRegistration.value = registration;
  auditAction.value = 'view';
  populateAuditForm(registration);
  showAuditDialog.value = true;
};

// 填充审核表单
const populateAuditForm = (registration) => {
  Object.assign(auditForm, {
    reg_id: registration.reg_id,
    user_name: registration.user_name || registration.user_id,
    competition_name: registration.competition_name || `竞赛${registration.competition_id}`,
    team_name: registration.team_name || `团队${registration.team_id}`,
    registration_time: registration.registration_time,
    audit_remark: ''
  });
};

// 确认审核通过
const confirmAuditPass = async () => {
  if (!currentRegistration.value) return;
  
  try {
    // 调用审核通过接口
    await updateRegistration(currentRegistration.value.reg_id, {
      audit_status: 1, // 通过
      audit_remark: auditForm.audit_remark
    });
    
    showSuccess('审核通过成功！');
    showAuditDialog.value = false;
    // 重新获取报名列表
    fetchRegistrations();
  } catch (error) {
    showError('审核失败：' + (error.response?.data?.message || error.message));
  }
};

// 确认审核驳回
const confirmAuditReject = async () => {
  if (!currentRegistration.value) return;
  
  try {
    // 调用审核驳回接口
    await updateRegistration(currentRegistration.value.reg_id, {
      audit_status: 2, // 驳回
      audit_remark: auditForm.audit_remark
    });
    
    showSuccess('审核驳回成功！');
    showAuditDialog.value = false;
    // 重新获取报名列表
    fetchRegistrations();
  } catch (error) {
    showError('审核失败：' + (error.response?.data?.message || error.message));
  }
};
</script>

<style scoped>
.admin-registration-audit {
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
  margin-bottom: 20px;
}

.page-header h2 {
  font-size: 28px;
  color: #2d3748;
  margin: 0;
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
</style>