<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/250/1920/1080)',  // 校园教学楼风格背景图
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
          title="学院管理" 
          img="https://picsum.photos/id/250/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="colleges.length > 0">
          <thead>
            <tr>
              <th>学院ID</th>
              <th>学院名称</th>
              <th>所属学校</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="c in colleges" :key="c.college_id">
              <td>{{ c.college_id || '-' }}</td>
              <td>{{ c.college_name || '-' }}</td>
              <td>{{ c.university_name || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无学院数据</p>
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

const colleges = ref([]);

// 修复接口路径：带/api/college前缀
const fetchColleges = async () => {
  try {
    const res = await request.get('/api/college/colleges/');
    colleges.value = res.data || [];
  } catch (err) {
    console.error('学院数据加载失败：', err);
    showError(`获取学院数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchColleges);
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