<template>
  <div class="reviewer-review">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>作品评审</h2>
        </div>
        <div class="content-card">
          <el-tabs v-model="activeTab">
            <el-tab-pane label="待评审" name="pending">
              <el-table v-loading="loading" :data="pendingSubmissions" style="width: 100%">
                <el-table-column prop="work_id" label="作品ID" width="100" />
                <el-table-column prop="team_name" label="队伍名称" />
                <el-table-column prop="competition_name" label="竞赛" width="200" />
                <el-table-column prop="problem_name" label="题目" />
                <el-table-column prop="submit_time" label="提交时间" width="200" />
                <el-table-column prop="file_name" label="文件名" width="200" />
                <el-table-column label="操作" width="150" fixed="right">
                  <template #default="scope">
                    <el-button 
                      type="primary" 
                      size="small"
                      @click="handleReview(scope.row)"
                    >
                      开始评审
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="已评审" name="reviewed">
              <el-table v-loading="loading" :data="reviewedSubmissions" style="width: 100%">
                <el-table-column prop="submission_id" label="提交ID" width="100" />
                <el-table-column prop="team_name" label="队伍名称" />
                <el-table-column prop="competition_name" label="竞赛" width="200" />
                <el-table-column prop="problem_name" label="题目" />
                <el-table-column prop="score" label="得分" width="100" />
                <el-table-column prop="review_time" label="评审时间" width="200" />
                <el-table-column prop="reviewer_name" label="评审人" width="120" />
                <el-table-column label="操作" width="150" fixed="right">
                  <template #default="scope">
                    <el-button 
                      type="info" 
                      size="small"
                      @click="handleViewReview(scope.row)"
                    >
                      查看评审
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
          </el-tabs>
        </div>

        <!-- 评审对话框 -->
        <el-dialog
          v-model="reviewDialogVisible"
          title="作品评审"
          width="800px"
        >
          <div v-if="currentSubmission" class="review-form">
            <el-form label-position="top">
              <el-form-item label="队伍名称">
                {{ currentSubmission.team_name }}
              </el-form-item>
              <el-form-item label="竞赛">
                {{ currentSubmission.competition_name }}
              </el-form-item>
              <el-form-item label="题目">
                {{ currentSubmission.problem_name }}
              </el-form-item>
              <el-form-item label="提交文件">
                <el-button 
                  type="link"
                  @click="downloadFile(currentSubmission.submission_id)"
                >
                  {{ currentSubmission.file_name }}
                </el-button>
              </el-form-item>
              <el-form-item label="得分">
                <el-slider
                  v-model="reviewForm.score"
                  :min="0"
                  :max="100"
                  :step="1"
                  show-input
                />
              </el-form-item>
              <el-form-item label="评审意见">
                <el-input
                  v-model="reviewForm.comment"
                  type="textarea"
                  rows="5"
                  placeholder="请输入评审意见"
                />
              </el-form-item>
            </el-form>
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="reviewDialogVisible = false">取消</el-button>
              <el-button type="primary" @click="submitReview">提交评审</el-button>
            </span>
          </template>
        </el-dialog>

        <!-- 评审详情对话框 -->
        <el-dialog
          v-model="reviewDetailDialogVisible"
          title="评审详情"
          width="600px"
          :loading="reviewDetailLoading"
        >
          <div v-if="currentReview" class="review-detail">
            <el-descriptions border :column="1">
              <el-descriptions-item label="评审ID">{{ currentReview.review_id }}</el-descriptions-item>
              <el-descriptions-item label="提交ID">{{ currentReview.submission_id }}</el-descriptions-item>
              <el-descriptions-item label="评审员ID">{{ currentReview.reviewer_id }}</el-descriptions-item>
              <el-descriptions-item label="得分">{{ currentReview.score }}</el-descriptions-item>
              <el-descriptions-item label="评审意见">
                <div class="comment-content">{{ currentReview.comment || '无' }}</div>
              </el-descriptions-item>
              <el-descriptions-item label="评审时间">{{ currentReview.review_time }}</el-descriptions-item>
            </el-descriptions>
          </div>
          <div v-else class="no-data">
            未找到评审详情
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="reviewDetailDialogVisible = false">关闭</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { request } from '../../api';
import { getWorks, getWorkById, reviewWork, downloadWork } from '../../api/work';
import { useUserStore } from '../../store/user';
import { showError, showSuccess, showWarning } from '../../utils/notification.js';

const userStore = useUserStore();
const activeTab = ref('pending');
const loading = ref(false);
const pendingSubmissions = ref([]);
const reviewedSubmissions = ref([]);

// 评审对话框
const reviewDialogVisible = ref(false);
const currentSubmission = ref(null);
const reviewForm = ref({
  score: 0,
  comment: ''
});

// 评审详情对话框
const reviewDetailDialogVisible = ref(false);
const currentReview = ref(null);
const reviewDetailLoading = ref(false);

const fetchSubmissions = async () => {
  loading.value = true;
  try {
    // 获取待评审作品
    const pendingResponse = await getWorks(null, null, null, false);
    pendingSubmissions.value = pendingResponse || [];

    // 获取已评审作品
    const reviewedResponse = await getWorks(null, null, null, true);
    reviewedSubmissions.value = reviewedResponse || [];
  } catch (error) {
    showError('获取作品列表失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    loading.value = false;
  }
};

const handleReview = (row) => {
  currentSubmission.value = row;
  reviewForm.value = {
    score: 0,
    comment: ''
  };
  reviewDialogVisible.value = true;
};

const handleViewReview = async (row) => {
  if (!row.submission_id) return;
  
  reviewDetailLoading.value = true;
  try {
      // 获取该提交的评审详情
      const response = await getReviews({ submission_id: row.submission_id });
      if (response && response.length > 0) {
        // 假设每个提交只有一个评审
        currentReview.value = response[0];
        reviewDetailDialogVisible.value = true;
      } else {
        showWarning('未找到评审信息');
      }
  } catch (error) {
    showError('获取评审详情失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    reviewDetailLoading.value = false;
  }
};

const downloadFile = async (workId) => {
  try {
    const response = await downloadWork(workId);
    const blob = new Blob([response], { type: response.type });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = response.filename || `work_${workId}.pdf`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
    showSuccess('文件下载成功');
  } catch (error) {
    showError('文件下载失败：' + (error.response?.data?.message || error.message || error));
  }
};

const submitReview = async () => {
  if (!currentSubmission.value) return;
  
  try {
    await reviewWork(currentSubmission.value.work_id, {
      review_user_id: userStore.userInfo.user_id,
      score: reviewForm.value.score,
      comment: reviewForm.value.comment
    });
    showSuccess('评审提交成功');
    reviewDialogVisible.value = false;
    // 更新列表
    fetchSubmissions();
  } catch (error) {
    showError('评审提交失败：' + (error.response?.data?.message || error.message || error));
  }
};

onMounted(() => {
  fetchSubmissions();
});
</script>

<style scoped>
.reviewer-review {
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

.review-form {
  max-height: 600px;
  overflow-y: auto;
}

.review-detail {
  padding: 10px 0;
}

.comment-content {
  min-height: 80px;
  white-space: pre-wrap;
  word-break: break-word;
}

.no-data {
  text-align: center;
  color: #909399;
  padding: 20px;
}
</style>

