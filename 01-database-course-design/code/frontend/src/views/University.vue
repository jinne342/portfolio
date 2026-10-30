<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/175/1920/1080)',  // 校园建筑风格背景图
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
          title="学校管理" 
          img="https://picsum.photos/id/175/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="universities.length > 0">
          <thead>
            <tr>
              <th>学校ID</th>
              <th>学校名称</th>
              <th>省份</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="u in universities" :key="u.university_id">
              <td>{{ u.university_id || '-' }}</td>
              <td>{{ u.university_name || '-' }}</td>
              <td>{{ u.province || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无学校数据</p>
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

const universities = ref([]);

// 修复接口路径：带/api/university前缀
const fetchUniversities = async () => {
  try {
    const res = await request.get('/api/university/universities/');
    universities.value = res.data || [];
  } catch (err) {
    console.error('学校数据加载失败：', err);
    showError(`获取学校数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchUniversities);
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