<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/301/1920/1080)',  // 归档/文档风格背景图
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
          title="归档管理" 
          img="https://picsum.photos/id/301/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="archives.length > 0">
          <thead>
            <tr>
              <th>归档ID</th>
              <th>归档名称</th>
              <th>归档内容</th>
              <th>归档时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="a in archives" :key="a.archive_id">
              <td>{{ a.archive_id || '-' }}</td>
              <td>{{ a.archive_name || '-' }}</td>
              <td class="content-cell">{{ a.archive_content || '-' }}</td>
              <td>{{ a.archive_time || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无归档数据</p>
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

const archives = ref([]);

const fetchArchives = async () => {
  try {
    const res = await request.get('/api/archive/archives/');
    archives.value = res.data || [];
  } catch (err) {
    console.error('归档数据加载失败：', err);
    showError(`获取归档数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchArchives);
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