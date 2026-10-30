<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/342/1920/1080)',  // 消息/通讯风格背景图
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
          title="消息管理" 
          img="https://picsum.photos/id/342/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <table v-if="messages.length > 0">
          <thead>
            <tr>
              <th>消息ID</th>
              <th>发送者ID</th>
              <th>接收者ID</th>
              <th>消息内容</th>
              <th>发送时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="m in messages" :key="m.message_id">
              <td>{{ m.message_id || '-' }}</td>
              <td>{{ m.sender_id || '-' }}</td>
              <td>{{ m.receiver_id || '-' }}</td>
              <td class="content-cell">{{ m.content || '-' }}</td>
              <td>{{ formatTime(m.send_time) }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else class="empty-tip">暂无消息数据</p>
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

const messages = ref([]);

// 时间格式化函数
const formatTime = (timeString) => {
  if (!timeString) return '-';
  
  try {
    // 尝试解析时间字符串
    const date = new Date(timeString);
    
    // 检查是否是有效日期
    if (isNaN(date.getTime())) {
      return '-';
    }
    
    // 格式化为YYYY-MM-DD HH:mm:ss
    return date.toISOString().slice(0, 19).replace('T', ' ');
  } catch (e) {
    console.error('时间格式化失败:', e);
    return '-';
  }
};

const fetchMessages = async () => {
  try {
    const res = await request.get('/messages/');
    messages.value = res || [];
  } catch (err) {
    console.error('消息数据加载失败：', err);
    showError(`获取消息数据失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchMessages);
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