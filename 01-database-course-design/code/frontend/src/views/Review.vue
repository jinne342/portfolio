<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/48/1920/1080)',  // 文档评审风格背景图
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
          title="评审管理" 
          img="https://picsum.photos/id/48/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="reviews.length > 0">
          <thead>
            <tr>
              <th>评审ID</th>
              <th>提交ID</th>
              <th>评审人ID</th>
              <th>评分</th>
              <th>评审内容</th>
              <th>评审时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in reviews" :key="r.id">
              <td>{{ r.id || '-' }}</td>
              <td>{{ r.submission_id || '-' }}</td>
              <td>{{ r.reviewer_id || '-' }}</td>
              <td>{{ r.score || '无评分' }}</td>
              <td class="content-cell">{{ r.comments || '-' }}</td>
              <td>{{ r.review_time || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无评审数据</p>
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
import request from '../api/index.js';
import { showError } from '../utils/notification.js';

const reviews = ref([]);

const fetchReviews = async () => {
  try {
    const res = await request.get('/api/review/reviews/');
    reviews.value = res.data || [];
  } catch (err) {
    console.error('评审数据加载失败：', err);
    showError(`获取评审数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchReviews);
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
.content-cell {
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