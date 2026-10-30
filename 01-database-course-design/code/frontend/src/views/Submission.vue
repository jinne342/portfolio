<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/287/1920/1080)',  // 提交/文档风格背景图
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
          title="提交管理" 
          img="https://picsum.photos/id/287/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="submissions.length > 0">
          <thead>
            <tr>
              <th>提交ID</th>
              <th>队伍ID</th>
              <th>题目ID</th>
              <th>提交文件</th>
              <th>提交时间</th>
              <th>评分</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="s in submissions" :key="s.submission_id">
              <td>{{ s.submission_id || '-' }}</td>
              <td>{{ s.team_id || '-' }}</td>
              <td>{{ s.problem_id || '-' }}</td>
              <td><a :href="s.file_url" target="_blank">{{ s.file_url ? '查看文件' : '无文件' }}</a></td>
              <td>{{ s.submit_time || '-' }}</td>
              <td>{{ s.score || '未评分' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无提交数据</p>
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

const submissions = ref([]);

const fetchSubmissions = async () => {
  try {
    const res = await request.get('/api/submission/submissions/');
    submissions.value = res.data || [];
  } catch (err) {
    console.error('提交数据加载失败：', err);
    showError(`获取提交数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchSubmissions);
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
.empty-tip {
  text-align: center;
  padding: 40px;
  color: #666;
}
</style>