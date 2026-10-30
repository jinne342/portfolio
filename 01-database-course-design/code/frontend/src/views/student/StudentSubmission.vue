<template>
  <div class="student-submission">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>作品提交</h2>
          <button class="primary-btn" @click="showCreateDialog = true">提交作品</button>
        </div>
        
        <!-- 提交列表 -->
        <div class="content-card">
          <h3>我的作品记录</h3>
          <el-table v-if="submissions.length > 0" :data="submissions" stripe style="width: 100%">
            <el-table-column prop="work_id" label="作品ID" width="120" />
            <el-table-column prop="team_id" label="队伍ID" width="100" />
            <el-table-column prop="problem_id" label="题目ID" width="100" />
            <el-table-column prop="file_url" label="文件路径" min-width="200">
              <template #default="scope">
                <el-button type="text" @click="downloadFile(scope.row.work_id, scope.row.file_url)">
                  {{ scope.row.file_url }}
                </el-button>
              </template>
            </el-table-column>
            <el-table-column prop="version" label="版本" width="80" />
            <el-table-column prop="score" label="评分" width="80">
              <template #default="scope">
                {{ scope.row.score || '未评分' }}
              </template>
            </el-table-column>
            <el-table-column prop="submit_time" label="提交时间" width="180" />
            <el-table-column label="操作" width="150" fixed="right">
              <template #default="scope">
                <el-button size="small" type="primary" @click="showUpdateDialog(scope.row)">更新</el-button>
                <el-button size="small" type="danger" @click="handleDeleteSubmission(scope.row.work_id)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-else class="empty-state">
            <el-empty description="暂无作品记录，点击'提交作品'开始提交吧！" />
          </div>
        </div>
        
        <!-- 提交作品对话框 -->
        <el-dialog v-model="showCreateDialog" title="提交作品" width="500px">
          <el-form :model="submissionForm" :rules="submissionRules" ref="submissionFormRef" label-width="100px">
            <el-form-item label="队伍ID" prop="team_id">
              <el-input v-model.number="submissionForm.team_id" placeholder="请输入队伍ID" />
            </el-form-item>
            <el-form-item label="题目ID" prop="problem_id">
              <el-input v-model.number="submissionForm.problem_id" placeholder="请输入题目ID" />
            </el-form-item>
            <el-form-item label="上传文件" prop="file">
              <el-upload
                ref="fileUploadRef"
                :auto-upload="false"
                :file-list="submissionForm.fileList"
                :on-change="handleFileChange"
                accept=".pdf,.docx,.doc,.txt"
                class="upload-demo"
              >
                <el-button type="primary">点击上传</el-button>
                <template #tip>
                  <div class="el-upload__tip">
                    仅支持 PDF、DOCX、DOC、TXT 格式文件
                  </div>
                </template>
              </el-upload>
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showCreateDialog = false">取消</el-button>
              <el-button type="primary" @click="handleCreateSubmission">提交</el-button>
            </span>
          </template>
        </el-dialog>
        
        <!-- 更新提交对话框 -->
        <el-dialog v-model="showUpdateDialogVisible" title="更新提交" width="500px">
          <el-form :model="updateForm" :rules="submissionRules" ref="updateFormRef" label-width="100px">
            <el-form-item label="队伍ID" prop="team_id">
              <el-input v-model.number="updateForm.team_id" placeholder="请输入队伍ID" />
            </el-form-item>
            <el-form-item label="题目ID" prop="problem_id">
              <el-input v-model.number="updateForm.problem_id" placeholder="请输入题目ID" />
            </el-form-item>
            <el-form-item label="上传文件" prop="file">
              <el-upload
                ref="updateFileUploadRef"
                :auto-upload="false"
                :file-list="updateForm.fileList"
                :on-change="handleUpdateFileChange"
                accept=".pdf,.docx,.doc,.txt"
                class="upload-demo"
              >
                <el-button type="primary">点击上传</el-button>
                <template #tip>
                  <div class="el-upload__tip">
                    仅支持 PDF、DOCX、DOC、TXT 格式文件
                  </div>
                </template>
              </el-upload>
            </el-form-item>
            <el-form-item label="版本" prop="version">
              <el-input v-model.number="updateForm.version" placeholder="请输入版本号" />
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="showUpdateDialogVisible = false">取消</el-button>
              <el-button type="primary" @click="handleUpdateSubmission">更新</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getWorks, createWork, updateWork, deleteWork } from '../../api/work.js';
import { useUserStore } from '../../store/user.js';
import { showError, showSuccess, showWarning, showConfirm } from '../../utils/notification.js';

const submissions = ref([]);
const showCreateDialog = ref(false);
const showUpdateDialogVisible = ref(false);
const submissionFormRef = ref(null);
const updateFormRef = ref(null);
const currentWorkId = ref(null);

// 用户状态管理
const userStore = useUserStore();

// 文件上传引用
const fileUploadRef = ref(null);
const updateFileUploadRef = ref(null);

// 提交表单
const submissionForm = reactive({
  team_id: null,
  problem_id: null,
  file: null,
  fileList: []
});

// 更新表单
const updateForm = reactive({
  team_id: null,
  problem_id: null,
  file: null,
  fileList: [],
  version: 1
});

// 表单验证规则
const submissionRules = reactive({
  team_id: [
    { required: true, message: '请输入队伍ID', trigger: 'blur' },
    { type: 'number', message: '队伍ID必须是数字', trigger: 'blur' }
  ],
  problem_id: [
    { required: true, message: '请输入题目ID', trigger: 'blur' },
    { type: 'number', message: '题目ID必须是数字', trigger: 'blur' }
  ],
  file: [
    { required: true, message: '请选择要上传的文件', trigger: 'change' }
  ]
});

// 处理文件选择
const handleFileChange = (file, fileList) => {
  submissionForm.file = file.raw;
  submissionForm.fileList = fileList;
};

// 处理更新表单的文件选择
const handleUpdateFileChange = (file, fileList) => {
  updateForm.file = file.raw;
  updateForm.fileList = fileList;
};

// 页面加载时获取提交列表
onMounted(() => {
  fetchSubmissions();
});

// 获取提交列表
const fetchSubmissions = async () => {
  try {
    // 获取当前用户ID
    const userId = userStore.userInfo?.user_id;
    if (!userId) {
      showWarning('用户未登录或登录状态异常');
      submissions.value = [];
      return;
    }
    
    // 根据用户ID获取作品记录
    const response = await getWorks(null, null, userId);
    submissions.value = response || [];
  } catch (error) {
    showError('获取作品列表失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 下载文件
const downloadFile = (workId, fileUrl) => {
  if (!workId || !fileUrl) {
    showWarning('文件信息不完整');
    return;
  }
  
  try {
    // 创建下载链接，使用后端下载API端点
    const link = document.createElement('a');
    link.href = `${import.meta.env.VITE_API_BASE_URL || ''}/works/${workId}/download/`;
    
    // 从fileUrl中提取文件名
    const fileName = fileUrl.split('/').pop() || 'downloaded_file';
    link.download = fileName;
    
    // 触发下载
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    showSuccess('文件下载已开始');
  } catch (error) {
    showError('文件下载失败：' + (error.message || error));
  }
};

// 创建提交
const handleCreateSubmission = async () => {
  if (!submissionFormRef.value) return;
  
  await submissionFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // 创建FormData对象处理文件上传
        const formData = new FormData();
        formData.append('team_id', submissionForm.team_id);
        formData.append('problem_id', submissionForm.problem_id);
        formData.append('file', submissionForm.file);
        
        await createWork(formData);
        showSuccess('作品提交成功！');
        showCreateDialog.value = false;
        // 重置表单
        Object.assign(submissionForm, {
          team_id: null,
          problem_id: null,
          file: null,
          fileList: []
        });
        // 重新获取提交列表
        fetchSubmissions();
      } catch (error) {
        showError('提交失败：' + (error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 显示更新对话框
const showUpdateDialog = (work) => {
  currentWorkId.value = work.work_id;
  Object.assign(updateForm, {
    team_id: work.team_id,
    problem_id: work.problem_id,
    file: null,
    fileList: [],
    version: work.version || 1
  });
  showUpdateDialogVisible.value = true;
};

// 更新提交
const handleUpdateSubmission = async () => {
  if (!updateFormRef.value) return;
  
  await updateFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // 创建FormData对象处理文件上传
        const formData = new FormData();
        formData.append('team_id', updateForm.team_id);
        formData.append('problem_id', updateForm.problem_id);
        formData.append('version', updateForm.version);
        if (updateForm.file) {
          formData.append('file', updateForm.file);
        }
        
        await updateWork(currentWorkId.value, formData);
        showSuccess('作品更新成功！');
        showUpdateDialogVisible.value = false;
        // 重置表单
        Object.assign(updateForm, {
          team_id: null,
          problem_id: null,
          file: null,
          fileList: [],
          version: 1
        });
        // 重新获取提交列表
        fetchSubmissions();
      } catch (error) {
        showError('更新失败：' + (error.response?.data?.message || error.message || error));
      }
    } else {
      showWarning('请完整填写表单信息');
      return false;
    }
  });
};

// 删除提交
const handleDeleteSubmission = async (workId) => {
  try {
    await showConfirm('确定要删除该作品吗？删除后无法恢复', '警告');
    
    await deleteWork(workId);
    showSuccess('作品删除成功！');
    fetchSubmissions();
  } catch (error) {
    if (error !== 'cancel') {
      showError('删除失败：' + (error.response?.data?.message || error.message || error));
    }
  }
};
</script>

<style scoped>
.student-submission {
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
</style>

