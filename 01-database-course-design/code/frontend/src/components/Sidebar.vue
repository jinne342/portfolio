<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <h3>导航菜单</h3>
    </div>
    <nav class="sidebar-nav">
      <!-- 学生菜单 -->
      <template v-if="userStore.isStudent">
        <router-link to="/student/dashboard" class="nav-item" active-class="active">
          <span>我的首页</span>
        </router-link>
        <router-link to="/student/team" class="nav-item" active-class="active">
          <span>我的队伍</span>
        </router-link>
        <router-link to="/student/submission" class="nav-item" active-class="active">
          <span>作品提交</span>
        </router-link>
        <router-link to="/student/competition" class="nav-item" active-class="active">
          <span>竞赛报名</span>
        </router-link>
        <router-link to="/student/problem" class="nav-item" active-class="active">
          <span>题目选择</span>
        </router-link>
        <router-link to="/student/certificate" class="nav-item" active-class="active">
          <span>我的证书</span>
        </router-link>
        <router-link to="/student/message" class="nav-item" active-class="active">
          <span>消息中心</span>
        </router-link>
      </template>

      <!-- 教师菜单 -->
      <template v-else-if="userStore.isTeacher">
        <router-link to="/teacher/dashboard" class="nav-item" active-class="active">
          <span>工作台</span>
        </router-link>
        <router-link to="/teacher/team" class="nav-item" active-class="active">
          <span>指导队伍</span>
        </router-link>
        <router-link to="/teacher/review" class="nav-item" active-class="active">
          <span>评审管理</span>
        </router-link>
        <router-link to="/teacher/statistics" class="nav-item" active-class="active">
          <span>数据统计</span>
        </router-link>
        <router-link to="/teacher/message" class="nav-item" active-class="active">
          <span>消息中心</span>
        </router-link>
      </template>

      <!-- 超级管理员菜单 -->
      <template v-else-if="userStore.isSuperAdmin">
        <router-link to="/super-admin/dashboard" class="nav-item" active-class="active">
          <span>管理首页</span>
        </router-link>
        
        <router-link to="/super-admin/user" class="nav-item" active-class="active">
          <span>用户管理</span>
        </router-link>
        
        <router-link to="/super-admin/team" class="nav-item" active-class="active">
          <span>队伍管理</span>
        </router-link>
        <router-link to="/super-admin/competition" class="nav-item" active-class="active">
          <span>竞赛管理</span>
        </router-link>
        
        <router-link to="/super-admin/violation" class="nav-item" active-class="active">
          <span>违规管理</span>
        </router-link>
        <router-link to="/super-admin/statistics" class="nav-item" active-class="active">
          <span>数据统计</span>
        </router-link>
        
        <router-link to="/super-admin/message" class="nav-item" active-class="active">
          <span>消息中心</span>
        </router-link>
      </template>
      
      <!-- 竞赛管理员菜单 -->
      <template v-else-if="userStore.isCompetitionAdmin">
        <router-link to="/competition-admin/dashboard" class="nav-item" active-class="active">
          <span>管理首页</span>
        </router-link>
        
        <router-link to="/competition-admin/team" class="nav-item" active-class="active">
          <span>队伍管理</span>
        </router-link>
        <router-link to="/competition-admin/competition" class="nav-item" active-class="active">
          <span>竞赛管理</span>
        </router-link>
        
        <router-link to="/competition-admin/registration-audit" class="nav-item" active-class="active">
          <span>报名审核</span>
        </router-link>
        
        <router-link to="/competition-admin/message" class="nav-item" active-class="active">
          <span>消息中心</span>
        </router-link>
      </template>

      <!-- 评审菜单 -->
      <template v-else-if="userStore.isReviewer">
        <router-link to="/reviewer/dashboard" class="nav-item" active-class="active">
          <span>评审工作台</span>
        </router-link>
        <router-link to="/reviewer/review" class="nav-item" active-class="active">
          <span>作品评审</span>
        </router-link>
        <router-link to="/reviewer/message" class="nav-item" active-class="active">
          <span>消息中心</span>
        </router-link>
      </template>

      <!-- 默认菜单（未识别角色） -->
      <template v-else>
        <router-link to="/dashboard" class="nav-item" active-class="active">
          <span>首页</span>
        </router-link>
        <router-link to="/team" class="nav-item" active-class="active">
          <span>队伍</span>
        </router-link>
        <router-link to="/submission" class="nav-item" active-class="active">
          <span>提交</span>
        </router-link>
      </template>
    </nav>
  </aside>
</template>

<script setup>
import { useUserStore } from '../store/user.js';

const userStore = useUserStore();
</script>

<style scoped>
.sidebar {
  width: 220px;
  background: #475569;
  min-height: calc(100vh - 70px);
  box-shadow: 2px 0 8px rgba(0,0,0,0.1);
  position: sticky;
  top: 70px;
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.sidebar-header h3 {
  color: white;
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.sidebar-nav {
  padding: 16px 0;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 12px 24px;
  color: rgba(255,255,255,0.9);
  text-decoration: none;
  transition: all 0.3s;
  border-left: 3px solid transparent;
  font-size: 14px;
  font-weight: 500;
}

.nav-item:hover {
  background: rgba(255,255,255,0.08);
  color: white;
}

.nav-item.active {
  background: rgba(96, 165, 250, 0.15);
  border-left-color: #60a5fa;
  color: white;
}
</style>
