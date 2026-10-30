<template>
  <div class="teacher-review">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>评审管理</h2>
        </div>
        <div class="content-card">
          <el-tabs v-model="activeTab">
            <el-tab-pane label="待评审" name="pending">
              <el-table v-loading="loading" :data="pendingSubmissions" style="width: 100%">
                <el-table-column prop="submission_id" label="提交ID" width="100" />
                <el-table-column prop="team_name" label="队伍名称" />
                <el-table-column prop="competition_name" label="竞赛" width="200" />
                <el-table-column prop="problem_name" label="题目" />
                <el-table-column prop="submit_time" label="提交时间" width="200" />
                <el-table-column prop="file_name" label="文件名" width="200" />
                <el-table-column label="操作" width="250" fixed="right">
                  <template #default="scope">
                    <el-button 
                      type="primary" 
                      size="small"
                      @click="handleReview(scope.row)"
                    >
                      开始评审
                    </el-button>
                    <el-button 
                      type="success" 
                      size="small"
                      @click="downloadFile(scope.row.submission_id)"
                    >
                      下载作品
                    </el-button>
                    <el-button 
                      type="warning" 
                      size="small"
                      @click="handleViolation(scope.row)"
                    >
                      判定违规
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="已评审" name="reviewed">
              <el-table v-loading="loading" :data="reviewedSubmissions" style="width: 100%">
                <el-table-column prop="work_id" label="作品ID" width="100" />
                <el-table-column prop="team_name" label="队伍名称" />
                <el-table-column prop="competition_name" label="竞赛" width="200" />
                <el-table-column prop="problem_name" label="题目" />
                <el-table-column prop="score" label="得分" width="100" />
                <el-table-column prop="review_time" label="评审时间" width="200" />
                <el-table-column prop="reviewer_name" label="评审人" width="120" />
                <el-table-column label="操作" width="320" fixed="right">
                  <template #default="scope">
                    <el-button 
                      type="info" 
                      size="small"
                      @click="handleViewReview(scope.row)"
                    >
                      查看评审
                    </el-button>
                    <el-button 
                      type="primary" 
                      size="small"
                      @click="handleEditReview(scope.row)"
                    >
                      修改评审
                    </el-button>
                    <el-button 
                      type="success" 
                      size="small"
                      @click="downloadFile(scope.row.work_id)"
                    >
                      下载作品
                    </el-button>
                    <el-button 
                      type="warning" 
                      size="small"
                      @click="handleViolation(scope.row)"
                    >
                      判定违规
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
              <el-descriptions-item label="评审员ID">{{ currentReview.user_id }}</el-descriptions-item>
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

        <!-- 违规判定对话框 -->
        <el-dialog
          v-model="violationDialogVisible"
          title="判定作品违规"
          width="600px"
        >
          <div v-if="currentSubmissionForViolation" class="violation-form">
            <el-form label-position="top">
              <el-form-item label="队伍名称">
                {{ currentSubmissionForViolation.team_name }}
              </el-form-item>
              <el-form-item label="竞赛">
                {{ currentSubmissionForViolation.competition_name }}
              </el-form-item>
              <el-form-item label="题目">
                {{ currentSubmissionForViolation.problem_name }}
              </el-form-item>
              <el-form-item label="提交文件">
                {{ currentSubmissionForViolation.file_name }}
              </el-form-item>
              <el-form-item label="违规类型" required>
                <el-select v-model="violationForm.violationType" placeholder="请选择违规类型" style="width: 100%;">
                  <el-option label="抄袭" value="plagiarism" />
                  <el-option label="作弊" value="cheating" />
                  <el-option label="内容违规" value="content_violation" />
                  <el-option label="格式不符合要求" value="format_violation" />
                  <el-option label="其他违规" value="other" />
                </el-select>
              </el-form-item>
              <el-form-item label="违规详情" required>
                <el-input
                  v-model="violationForm.violationDetail"
                  type="textarea"
                  rows="5"
                  placeholder="请详细描述违规情况"
                />
              </el-form-item>
            </el-form>
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="violationDialogVisible = false">取消</el-button>
              <el-button type="primary" @click="submitViolation">提交违规判定</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { ElLoading } from 'element-plus';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { request } from '../../api';
import { getWorks, getWorkById, reviewWork, downloadWork } from '../../api/work';
import { createViolation } from '../../api/violation';
import { showError, showSuccess, showWarning } from '../../utils/notification.js';

const activeTab = ref('pending');
const loading = ref(false);
const pendingSubmissions = ref([]);
const reviewedSubmissions = ref([]);

// 评审对话框
const reviewDialogVisible = ref(false);
const currentSubmission = ref(null);
const reviewForm = ref({
  review_id: null,
  score: 0,
  comment: ''
});

// 违规判定对话框
const violationDialogVisible = ref(false);
const currentSubmissionForViolation = ref(null);
const violationForm = ref({
  violationType: '',
  violationDetail: ''
});

// 评审详情对话框
const reviewDetailDialogVisible = ref(false);
const currentReview = ref(null);
const reviewDetailLoading = ref(false);

const fetchSubmissions = async () => {
  loading.value = true;
  try {
    // 获取当前登录用户信息
    const userInfo = JSON.parse(localStorage.getItem('userInfo'));
    const userId = userInfo?.user_id;
    
    // 获取待评审作品
    const pendingResponse = await getWorks(null, null, userId, false);
    pendingSubmissions.value = pendingResponse || [];

    // 获取已评审作品
    const reviewedResponse = await getWorks(null, null, userId, true);
    reviewedSubmissions.value = reviewedResponse || [];
  } catch (error) {
    showError('获取作品列表失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    loading.value = false;
  }
};

const handleReview = (row, reviewData = null) => {
  currentSubmission.value = row;
  if (reviewData) {
    // 如果有评审数据，填充到表单中（用于编辑）
    reviewForm.value = {
      review_id: reviewData.review_id,
      score: reviewData.score || 0,
      comment: reviewData.comment || ''
    };
  } else {
    // 新评审
    reviewForm.value = {
      review_id: null,
      score: 0,
      comment: ''
    };
  }
  reviewDialogVisible.value = true;
};

// 处理违规判定
const handleViolation = (row) => {
  currentSubmissionForViolation.value = row;
  violationForm.value = {
    violationType: '',
    violationDetail: ''
  };
  violationDialogVisible.value = true;
};

const handleEditReview = async (row) => {
  if (!row.submission_id) return;
  
  try {
    // 获取该提交的评审列表
    const reviewsResponse = await getReviews({ submission_id: row.submission_id });
    if (reviewsResponse && reviewsResponse.length > 0) {
      // 获取第一个评审的详情
      const reviewId = reviewsResponse[0].review_id;
      const reviewDetail = await getReviewDetail(reviewId);
      if (reviewDetail) {
        // 调用handleReview函数，并传入评审数据
        handleReview(row, reviewDetail);
      } else {
        showWarning('未找到评审信息');
      }
    } else {
      showWarning('未找到评审信息');
    }
  } catch (error) {
    showError('获取评审详情失败：' + (error.response?.data?.message || error.message || error));
  }
};

const handleViewReview = async (row) => {
  if (!row.work_id) return;
  
  reviewDetailLoading.value = true;
  try {
    // 获取该作品的详情
    const workDetail = await getWorkById(row.work_id);
    if (workDetail) {
      // 显示作品评审信息
      currentReview.value = {
        review_id: workDetail.work_id,
        submission_id: workDetail.work_id,
        user_id: workDetail.review_user_id,
        reviewer_id: workDetail.review_user_id,
        score: workDetail.score,
        comment: workDetail.review_comment,
        review_time: workDetail.review_time
      };
      reviewDetailDialogVisible.value = true;
    } else {
      showWarning('未找到作品信息');
    }
  } catch (error) {
    showError('获取作品详情失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    reviewDetailLoading.value = false;
  }
};

const downloadFile = async (submissionId) => {
  try {
    const response = await downloadSubmission(submissionId);
    const blob = new Blob([response], { type: response.type });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = response.filename || `submission_${submissionId}.pdf`;
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
    // 准备评审数据
    const reviewData = {
      review_user_id: userStore.userInfo?.user_id,
      score: reviewForm.value.score,
      comment: reviewForm.value.comment
    };
    
    // 调用评审接口
    await reviewWork(currentSubmission.value.work_id, reviewData);
    
    showSuccess('评审提交成功');
    reviewDialogVisible.value = false;
    // 更新列表
    fetchSubmissions();
  } catch (error) {
    showError('评审提交失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 提交违规判定
const submitViolation = async () => {
  if (!currentSubmissionForViolation.value) return;
  
  // 检查违规判定的必填项
  if (!violationForm.value.violationType) {
    showWarning('请选择违规类型');
    return;
  }
  if (!violationForm.value.violationDetail) {
    showWarning('请填写违规详情');
    return;
  }
  
  try {
      // 创建违规记录
      await createViolation({
        team_id: currentSubmissionForViolation.value.team_id,
        work_id: currentSubmissionForViolation.value.work_id,
        competition_id: currentSubmissionForViolation.value.competition_id,
        school_id: currentSubmissionForViolation.value.school_id,
        violation_type: violationForm.value.violationType,
        violation_detail: violationForm.value.violationDetail
      });
    
    showSuccess('违规判定提交成功');
    violationDialogVisible.value = false;
    // 更新列表
    fetchSubmissions();
  } catch (error) {
    showError('违规判定提交失败：' + (error.response?.data?.message || error.message || error));
  }
};

onMounted(() => {
  fetchSubmissions();
});
</script>

<style scoped>
.teacher-review {
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

