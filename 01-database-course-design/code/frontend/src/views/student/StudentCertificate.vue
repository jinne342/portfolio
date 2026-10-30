<template>
  <div class="student-certificate">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>我的证书</h2>
        </div>
        <div class="content-card">
          <el-table v-loading="loading" :data="certificates" style="width: 100%">
            <el-table-column prop="certificate_name" label="证书名称" />
            <el-table-column prop="competition_name" label="竞赛" width="200" />
            <el-table-column prop="award_level" label="获奖等级" width="120" />
            <el-table-column prop="award_year" label="获奖年份" width="100" />
            <el-table-column prop="issue_date" label="颁发日期" width="150" />
            <el-table-column prop="certificate_no" label="证书编号" width="150" />
            <el-table-column label="操作" width="120" fixed="right">
              <template #default="scope">
                <el-button 
                  type="primary" 
                  size="small"
                  @click="handleDownloadCertificate(scope.row.certificate_id)"
                >
                  下载证书
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getCertificates, downloadCertificate } from '../../api/certificate';
import { useUserStore } from '../../store/user';
import { showError, showSuccess } from '../../utils/notification.js';

const userStore = useUserStore();
const loading = ref(false);
const certificates = ref([]);

const fetchCertificates = async () => {
  loading.value = true;
  try {
    // 获取当前用户的证书列表
    const response = await getCertificates({ user_id: userStore.userInfo.user_id });
    certificates.value = response || [];
  } catch (error) {
    showError('获取证书列表失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    loading.value = false;
  }
};

const handleDownloadCertificate = async (certificateId) => {
  try {
    const response = await downloadCertificate(certificateId);
    const blob = new Blob([response], { type: response.type });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = response.filename || `certificate_${certificateId}.pdf`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
    showSuccess('证书下载成功');
  } catch (error) {
    showError('证书下载失败：' + (error.response?.data?.message || error.message || error));
  }
};

onMounted(() => {
  fetchCertificates();
});
</script>

<style scoped>
.student-certificate {
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

