<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/1058/1920/1080)',  // 首页/科技风格背景图
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
          title="系统首页" 
          img="https://picsum.photos/id/1058/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <div class="dashboard-cards">
          <div class="card">
            <h3>总队伍数</h3>
            <p>{{ teamCount || 0 }}</p>
          </div>
          <div class="card">
            <h3>总学校数</h3>
            <p>{{ universityCount || 0 }}</p>
          </div>
          <div class="card">
            <h3>总题目数</h3>
            <p>{{ problemCount || 0 }}</p>
          </div>
          <div class="card">
            <h3>总提交数</h3>
            <p>{{ submissionCount || 0 }}</p>
          </div>
        </div>
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

const teamCount = ref(0);
const universityCount = ref(0);
const problemCount = ref(0);
const submissionCount = ref(0);

const fetchDashboardData = async () => {
  try {
    // 总队伍数
    const res1 = await request.get('/api/statistics/team_count');
    teamCount.value = res1.data.total_teams || 0;

    // 总学校数
    const res2 = await request.get('/api/university/universities/');
    universityCount.value = res2.data.length || 0;

    // 总题目数
    const res3 = await request.get('/api/problem/problems/');
    problemCount.value = res3.data.length || 0;

    // 总提交数
    const res4 = await request.get('/api/submission/submissions/');
    submissionCount.value = res4.data.length || 0;
  } catch (err) {
    console.error('首页数据加载失败：', err);
  }
};

onMounted(fetchDashboardData);
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
.dashboard-cards {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-top: 20px;
}
.card {
  flex: 1 1 200px;
  background: rgba(255,255,255,0.9);
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}
.card h3 {
  margin: 0 0 10px 0;
  color: #333;
}
.card p {
  font-size: 24px;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
}
</style>