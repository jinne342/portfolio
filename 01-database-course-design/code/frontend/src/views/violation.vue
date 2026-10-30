<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/1025/1920/1080)',  // 违规/警示风格背景图
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    minHeight: '100vh'
  }">
    <Header />
    <div class="layout">
      <Sidebar />
      <main class="content">
        <PageBanner 
          title="违规管理" 
          img="https://picsum.photos/id/1025/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="violations.length > 0">
          <thead>
            <tr>
              <th>违规ID</th>
              <th>用户ID</th>
              <th>违规类型</th>
              <th>违规详情</th>
              <th>处理时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="v in violations" :key="v.violation_id">
              <td>{{ v.violation_id || '-' }}</td>
              <td>{{ v.user_id || '-' }}</td>
              <td>{{ v.violation_type || '-' }}</td>
              <td class="detail-cell">{{ v.violation_detail || '-' }}</td>
              <td>{{ v.handle_time || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无违规数据</p>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../components/Header.vue';
import Sidebar from '../components/Sidebar.vue';
import Footer from '../components/Footer.vue';
import PageBanner from '../components/PageBanner.vue';
import { getViolationList } from '../api/violation.js';
import { useUserStore } from '../store/user.js';
import { showError, showWarning } from '../utils/notification.js';

const userStore = useUserStore();
const violations = ref([]);

const fetchViolations = async () => {
  try {
    const userId = userStore.userInfo?.user_id;
    if (!userId) {
      showWarning('用户未登录或登录状态异常');
      return;
    }
    const response = await getViolationList({ user_id: userId });
    violations.value = response.data || [];
  } catch (err) {
    console.error('违规数据加载失败：', err);
    showError(`获取违规数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchViolations);
</script>

<style scoped>
.page {
  width: 100%;
  min-height: 100vh;
  padding: 0;
  margin: 0;
}
.content { 
  padding: 20px; 
  background: rgba(255,255,255,0.85);
  margin: 20px;
  border-radius: 8px;
}
.content table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 24px;
  background: rgba(255,255,255,0.95);
  border-radius: 8px;
}
th, td {
  border: 1px solid #e0e0e0;
  padding: 12px 8px;
  text-align: left;
}
th { background: #f5f7fa; font-weight: 600; }
.detail-cell {
  max-width: 300px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.empty-tip {
  text-align: center;
  padding: 40px;
  color: #666;
}
</style>