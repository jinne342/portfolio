<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/1048/1920/1080)',  // 替换为在线背景图（科技感/办公风，适配公告页）
    backgroundSize: 'cover',       // 图片自适应铺满容器，不拉伸
    backgroundRepeat: 'no-repeat', // 禁止图片重复
    backgroundPosition: 'center',  // 图片居中显示
    minHeight: '100vh'             // 背景至少铺满整个屏幕高度
  }">
    <Header />
    <div class="layout">
      <Sidebar />
      <main class="content">
        <!-- 修复PageBanner的图片链接，改用在线图 -->
        <PageBanner 
          title="公告管理" 
          img="https://picsum.photos/id/1048/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="announcements.length > 0">
          <thead>
            <tr>
              <th>公告ID</th>
              <th>标题</th>
              <th>内容</th>
              <th>发布时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="a in announcements" :key="a.id">
              <td>{{ a.id || '-' }}</td>
              <td>{{ a.title || '-' }}</td>
              <td class="content-cell">{{ a.content || '-' }}</td>
              <td>{{ formatTime(a.post_time) || '-' }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无公告数据</p>
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

const announcements = ref([]);

const formatTime = (timeStr) => {
  if (!timeStr) return '';
  try {
    return new Date(timeStr).toLocaleString('zh-CN');
  } catch (err) {
    return timeStr;
  }
};

// 匹配后端完整接口路径：/api/announcement/announcements/
const fetchAnnouncements = async () => {
  try {
    // 前端请求需带/api前缀（后端main.py挂载的prefix）
    const res = await request.get('/api/announcement/announcements/');
    announcements.value = res.data || [];
  } catch (err) {
    console.error('公告数据加载失败：', err);
    showError(`获取公告数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchAnnouncements);
</script>

<style scoped>
/* 新增page样式，保证背景铺满+布局正常 */
.page {
  width: 100%;
  min-height: 100vh;
  padding: 0;
  margin: 0;
}
/* 优化content样式，增加半透明背景，避免文字被背景遮挡 */
.content { 
  padding: 20px; 
  background: rgba(255,255,255,0.85); /* 白色半透明，兼顾美观和可读性 */
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