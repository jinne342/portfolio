<template>
  <div class="admin-violation">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>违规管理</h2>
        </div>
        
        <!-- 操作区域 -->
        <div class="action-area">
          <h3>违规信息登记</h3>
          <el-button type="success" size="small" @click="addViolation">
            添加违规记录
          </el-button>
        </div>
        
        <!-- 违规列表 -->
        <div class="content-card">
          <el-table v-loading="loading" :data="violations" style="width: 100%">
            <el-table-column type="selection" width="55" />
            <el-table-column prop="violation_id" label="违规编号" width="120" />
            <el-table-column prop="team_name" label="队伍名称" width="180" />
            <el-table-column prop="competition_name" label="竞赛名称" width="200" />
            <el-table-column prop="violation_type" label="违规类型" width="150" />
            <el-table-column prop="violation_detail" label="违规内容" width="200" />
            <el-table-column prop="handle_time" label="违规日期" width="150">
              <template #default="scope">
                {{ formatDateTime(scope.row.handle_time) }}
              </template>
            </el-table-column>
            <el-table-column prop="is_approved" label="处理状态" width="120">
              <template #default="scope">
                <el-tag :type="getStatusTagType(scope.row.is_approved)">
                  {{ getApprovalStatus(scope.row.is_approved) }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column label="操作" width="200" fixed="right">
              <template #default="scope">
                <el-button type="primary" size="small" @click="handleViolation(scope.row)">
                  查看
                </el-button>
                <el-button type="warning" size="small" @click="editViolation(scope.row)">
                  编辑
                </el-button>
              </template>
            </el-table-column>
          </el-table>

          <!-- 处理违规对话框 -->
          <el-dialog v-model="dialogVisible" title="处理违规" width="500px">
            <el-form :model="handleForm" label-width="100px">
              <el-form-item label="违规ID">
                {{ selectedViolation?.violation_id }}
              </el-form-item>
              <el-form-item label="违规类型">
                {{ selectedViolation?.violation_type }}
              </el-form-item>
              <el-form-item label="违规内容">
                {{ selectedViolation?.violation_detail }}
              </el-form-item>
              <el-form-item label="处理结果" required>
                <el-select v-model="handleForm.is_approved" placeholder="请选择处理结果">
                  <el-option label="通过" :value="1" />
                  <el-option label="不通过" :value="0" />
                </el-select>
              </el-form-item>
            </el-form>
            <template #footer>
              <span class="dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="submitHandle">确定</el-button>
              </span>
            </template>
          </el-dialog>
          
          <!-- 添加/编辑违规对话框 -->
          <el-dialog v-model="addEditDialogVisible" :title="isEdit ? '编辑违规记录' : '添加违规记录'" width="600px">
            <el-form :model="addEditForm" label-width="120px" :rules="addEditRules" ref="addEditFormRef">
              <el-form-item label="队伍名称" prop="team_name" required>
                <el-input v-model="addEditForm.team_name" placeholder="请输入队伍名称" />
              </el-form-item>
              <el-form-item label="竞赛名称" prop="competition_name" required>
                <el-input v-model="addEditForm.competition_name" placeholder="请输入竞赛名称" />
              </el-form-item>
              <el-form-item label="违规类型" prop="violation_type" required>
                <el-select v-model="addEditForm.violation_type" placeholder="请选择违规类型">
                  <el-option label="逾期未提交" value="逾期未提交" />
                  <el-option label="违反竞赛规则" value="违反竞赛规则" />
                  <el-option label="材料造假" value="材料造假" />
                  <el-option label="其他" value="其他" />
                </el-select>
              </el-form-item>
              <el-form-item label="违规日期" prop="violation_date" required>
                <el-date-picker v-model="addEditForm.violation_date" type="datetime" placeholder="请选择违规日期" style="width: 100%" />
              </el-form-item>
              <el-form-item label="违规内容" prop="violation_detail">
                <el-input v-model="addEditForm.violation_detail" type="textarea" rows="4" placeholder="请输入违规内容" />
              </el-form-item>
              <el-form-item label="处理状态" prop="handle_status">
                <el-select v-model="addEditForm.handle_status" placeholder="请选择处理状态">
                  <el-option label="未处理" value="未处理" />
                  <el-option label="处理中" value="处理中" />
                  <el-option label="已处理" value="已处理" />
                </el-select>
              </el-form-item>
            </el-form>
            <template #footer>
              <span class="dialog-footer">
                <el-button @click="addEditDialogVisible = false">取消</el-button>
                <el-button type="primary" @click="submitAddEdit">确定</el-button>
              </span>
            </template>
          </el-dialog>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getViolationList, updateViolation, createViolation } from '../../api/violation';
import { showError, showSuccess } from '../../utils/notification.js';

// 格式化日期时间
const formatDateTime = (dateTime) => {
  if (!dateTime) return '-';
  try {
    const date = new Date(dateTime);
    if (isNaN(date.getTime())) return '-';
    return date.toLocaleString('zh-CN');
  } catch (error) {
    return '-';
  }
};

// 获取状态标签类型
const getStatusTagType = (status) => {
  switch (status) {
    case 1:
    case '已处理':
      return 'success';
    case '处理中':
      return 'warning';
    case 0:
    case '未处理':
      return 'info';
    default:
      return 'info';
  }
};

// 获取审批状态文本
const getApprovalStatus = (isApproved) => {
  if (isApproved === 1) return '已通过';
  if (isApproved === 0) return '未通过';
  return '未处理';
};

const violations = ref([]);
const loading = ref(false);
const dialogVisible = ref(false);
const selectedViolation = ref(null);
const handleForm = ref({
  is_approved: 0
});

// 新增数据结构
const addEditDialogVisible = ref(false);
const isEdit = ref(false);
const addEditForm = ref({
  team_name: '',
  competition_name: '',
  violation_type: '',
  violation_date: '',
  violation_detail: '',
  handle_status: '未处理'
});
const addEditFormRef = ref(null);
const addEditRules = ref({
  team_name: [
    { required: true, message: '请输入队伍名称', trigger: 'blur' }
  ],
  competition_name: [
    { required: true, message: '请输入竞赛名称', trigger: 'blur' }
  ],
  violation_type: [
    { required: true, message: '请选择违规类型', trigger: 'change' }
  ],
  violation_date: [
    { required: true, message: '请选择违规日期', trigger: 'change' }
  ]
});

const fetchViolations = async () => {
  loading.value = true;
  try {
    const response = await getViolationList();
    violations.value = response || [];
  } catch (error) {
    showError('获取违规记录失败');
  } finally {
    loading.value = false;
  }
};

const handleViolation = (row) => {
  selectedViolation.value = row;
  handleForm.value.is_approved = row.is_approved || 0;
  dialogVisible.value = true;
};

const submitHandle = async () => {
  try {
    await updateViolation(selectedViolation.value.violation_id, {
      is_approved: handleForm.value.is_approved
    });
    showSuccess('处理成功');
    dialogVisible.value = false;
    fetchViolations();
  } catch (error) {
    showError('处理失败：' + (error.response?.data?.detail || '未知错误'));
  }
};

// 新增方法
const addViolation = () => {
  isEdit.value = false;
  addEditForm.value = {
    team_name: '',
    competition_name: '',
    violation_type: '',
    violation_date: '',
    violation_detail: '',
    handle_status: '未处理'
  };
  addEditDialogVisible.value = true;
};

const editViolation = (row) => {
  isEdit.value = true;
  addEditForm.value = {
    team_name: row.team_name || '',
    competition_name: row.competition_name || '',
    violation_type: row.violation_type || '',
    violation_date: row.violation_date || '',
    violation_detail: row.violation_detail || '',
    handle_status: row.handle_status || '未处理'
  };
  selectedViolation.value = row;
  addEditDialogVisible.value = true;
};

const submitAddEdit = async () => {
  try {
    if (isEdit.value) {
      // 编辑现有记录
      await updateViolation(selectedViolation.value.violation_id, addEditForm.value);
      showSuccess('编辑成功');
    } else {
      // 添加新记录
      await createViolation(addEditForm.value);
      showSuccess('添加成功');
    }
    addEditDialogVisible.value = false;
    fetchViolations();
  } catch (error) {
    showError((isEdit.value ? '编辑' : '添加') + '失败：' + (error.response?.data?.detail || '未知错误'));
  }
};

onMounted(() => {
  fetchViolations();
});
</script>

<style scoped>
.admin-violation {
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

.content-card h3 {
  font-size: 18px;
  color: #2d3748;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid #e2e8f0;
}

.action-area {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.action-area h3 {
  font-size: 18px;
  color: #2d3748;
  margin: 0;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
}
</style>

