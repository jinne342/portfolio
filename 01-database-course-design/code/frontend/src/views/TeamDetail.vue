<template>
  <div class="page" :style="{ 
    backgroundImage: 'url(https://picsum.photos/id/429/1920/1080)',  // 团队详情风格背景图
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
          title="队伍详情" 
          img="https://picsum.photos/id/429/1200/300"
          :style="{ backgroundSize: 'cover', backgroundPosition: 'center' }"
        />
        
        <div class="detail-card" v-if="team">
          <h3>队伍基本信息</h3>
          <div class="detail-item">
            <label>队伍ID：</label>
            <span>{{ team.team_id || '-' }}</span>
          </div>
          <div class="detail-item">
            <label>队伍名称：</label>
            <span>{{ team.team_name || '-' }}</span>
          </div>
          <div class="detail-item">
            <label>所属学院：</label>
            <span>{{ team.college_name || '-' }}</span>
          </div>
          <div class="detail-item">
            <label>状态：</label>
            <span>{{ team.status || '未审核' }}</span>
          </div>
          <div class="detail-item">
            <label>成员列表：</label>
            <div class="member-list">
              <span v-for="(member, idx) in team.members" :key="idx">{{ member.user_name }}（ID:{{ member.user_id }}）</span>
            </div>
          </div>
        </div>
        <p v-else class="empty-tip">暂无队伍详情数据</p>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import Header from '../components/Header.vue';
import Sidebar from '../components/Sidebar.vue';
import Footer from '../components/Footer.vue';
import PageBanner from '../components/PageBanner.vue';
import request from '../api/index.js';
import { showError } from '../utils/notification.js';

const route = useRoute();
const team = ref(null);

const fetchTeamDetail = async () => {
  try {
    const teamId = route.params.id;
    const res = await request.get(`/api/team/teams/${teamId}/`);
    team.value = res.data || null;
  } catch (err) {
    console.error('队伍详情加载失败：', err);
    showError(`获取队伍详情失败：${err.message || '接口异常'}`);
  }
};

onMounted(fetchTeamDetail);
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
.detail-card {
  background: rgba(255,255,255,0.9);
  padding: 20px;
  border-radius: 8px;
}
.detail-card h3 {
  margin: 0 0 20px 0;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 10px;
}
.detail-item {
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}
.detail-item label {
  font-weight: 600;
  width: 120px;
}
.member-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.member-list span {
  background: #f5f7fa;
  padding: 5px 10px;
  border-radius: 4px;
}
.empty-tip {
  text-align: center;
  padding: 40px;
  color: #666;
}
</style>