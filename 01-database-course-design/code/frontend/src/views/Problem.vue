<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/160/1920/1080)',  // 题目/文档风格背景图
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
          title="题目管理" 
          img="https://picsum.photos/id/160/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="problems.length > 0">
          <thead>
            <tr>
              <th>题目ID</th>
              <th>题目名称</th>
              <th>题目描述</th>
              <th>最大队伍数</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in problems" :key="p.problem_id">
              <td>{{ p.problem_id || '-' }}</td>
              <td>{{ p.title || '-' }}</td>
              <td class="desc-cell">{{ p.description || '-' }}</td>
              <td>{{ p.max_teams || 0 }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无题目数据</p>
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

const problems = ref([]);

const fetchProblems = async () => {
  try {
    const res = await request.get('/api/problem/problems/');
    problems.value = res.data || [];
  } catch (err) {
    console.error('题目数据加载失败：', err);
    showError(`获取题目数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchProblems);
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
.desc-cell {
  max-width: 400px;
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