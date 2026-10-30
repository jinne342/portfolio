<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/237/1920/1080)',  // 证书/荣誉风格背景图
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
          title="证书管理" 
          img="https://picsum.photos/id/237/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="certificates.length > 0">
          <thead>
            <tr>
              <th>证书ID</th>
              <th>用户ID</th>
              <th>证书名称</th>
              <th>证书编号</th>
              <th>颁发日期</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="c in certificates" :key="c.certificate_id">
              <td>{{ c.certificate_id || '-' }}</td>
              <td>{{ c.user_id || '-' }}</td>
              <td>{{ c.certificate_name || '-' }}</td>
              <td>{{ c.certificate_no || '-' }}</td>
              <td>{{ c.issue_date || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无证书数据</p>
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

const certificates = ref([]);

const fetchCertificates = async () => {
  try {
    const res = await request.get('/api/certificate/certificates/');
    certificates.value = res.data || [];
  } catch (err) {
    console.error('证书数据加载失败：', err);
    showError(`获取证书数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchCertificates);
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