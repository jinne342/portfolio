<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/180/1920/1080)',  // 数据图表风格背景图
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
          title="数据统计" 
          img="https://picsum.photos/id/180/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <!-- 队伍总数 -->
        <div class="stat-card">
          <h3>总队伍数量</h3>
          <p class="stat-value">{{ teamCount || 0 }}</p>
        </div>

        <!-- 各学院队伍数量 -->
        <div class="stat-card" v-if="teamByCollege.length > 0">
          <h3>各学院队伍数量</h3>
          <table>
            <thead>
              <tr>
                <th>学院</th>
                <th>队伍数</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in teamByCollege" :key="item.college">
                <td>{{ item.college }}</td>
                <td>{{ item.count }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 各题目选择次数 -->
        <div class="stat-card" v-if="problemSelection.length > 0">
          <h3>各题目被选择次数</h3>
          <table>
            <thead>
              <tr>
                <th>题目</th>
                <th>选择次数</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in problemSelection" :key="item.problem">
                <td>{{ item.problem }}</td>
                <td>{{ item.count }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p v-if="!teamCount && !teamByCollege.length && !problemSelection.length" class="empty-tip">暂无统计数据</p>
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

const teamCount = ref(0);
const teamByCollege = ref([]);
const problemSelection = ref([]);

// 加载所有统计数据
const fetchStatistics = async () => {
  try {
    // 总队伍数
    const res1 = await request.get('/api/statistics/team_count');
    teamCount.value = res1.data.total_teams || 0;

    // 各学院队伍数
    const res2 = await request.get('/api/statistics/team_by_college');
    teamByCollege.value = res2.data || [];

    // 各题目选择次数
    const res3 = await request.get('/api/statistics/problem_selection');
    problemSelection.value = res3.data || [];
  } catch (err) {
    console.error('统计数据加载失败：', err);
    showError(`获取统计数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchStatistics);
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
.stat-card {
  margin-bottom: 30px;
  padding: 15px;
  background: rgba(255,255,255,0.9);
  border-radius: 8px;
}
.stat-card h3 {
  margin: 0 0 15px 0;
  color: #333;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 8px;
}
.stat-value {
  font-size: 24px;
  font-weight: 600;
  color: #2c3e50;
  margin: 10px 0;
}
.stat-card table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #e0e0e0;
  padding: 10px 8px;
  text-align: left;
}
th { background: #f5f7fa; font-weight: 600; }
.empty-tip {
  text-align: center;
  padding: 40px;
  color: #666;
}
</style>