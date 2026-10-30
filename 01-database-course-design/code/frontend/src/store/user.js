import { defineStore } from 'pinia';
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { authApi } from '../api/auth.js';
import { showError } from '../utils/notification.js';

export const useUserStore = defineStore('user', () => {
  const userInfo = ref({
    user_id: null,
    username: '',
    role: '',
    user_type: null,
    token: '',
    roles: [],
    session_id: '',
    is_online: false,
    school_id: null
  });

  // 计算属性：判断用户角色
  const isStudent = computed(() => userInfo.value.user_type === 1 || userInfo.value.role === '学生');
  const isTeacher = computed(() => userInfo.value.user_type === 2 || userInfo.value.role === '教师');
  const isCompetitionAdmin = computed(() => userInfo.value.user_type === 3 || userInfo.value.role === '竞赛管理员');
  const isSuperAdmin = computed(() => userInfo.value.user_type === 0 || userInfo.value.role === '超级管理员' || userInfo.value.role === '管理员');
  // 移除评审员角色，已合并到教师角色
  const isReviewer = computed(() => false);

  // 保存用户信息
  const setUser = (data) => {
    userInfo.value = {
      user_id: data.user_id || data.id,
      username: data.username || data.user_name,
      role: data.role || '',
      user_type: data.user_type || null,
      token: data.token || '',
      roles: data.roles || [],
      session_id: data.session_id || '',
      is_online: data.is_online || false,
      school_id: data.school_id || null
    };
    // 保存到localStorage
    if (data.token) {
      localStorage.setItem('token', data.token);
    }
    localStorage.setItem('userInfo', JSON.stringify(userInfo.value));
  };

  // 清除用户信息
  const clearUser = () => {
    userInfo.value = { 
      user_id: null,
      username: '', 
      role: '', 
      user_type: null,
      token: '',
      roles: [],
      session_id: '',
      is_online: false,
      school_id: null
    };
    localStorage.removeItem('token');
    localStorage.removeItem('userInfo');
  };

  // 初始化用户信息
  const initUser = () => {
    const token = localStorage.getItem('token');
    const savedUserInfo = localStorage.getItem('userInfo');
    if (token && savedUserInfo) {
      try {
        userInfo.value = JSON.parse(savedUserInfo);
        // 验证token是否有效
        authApi.getCurrentUser().then(res => {
          if (res && res.data) {
            setUser(res.data);
          }
        }).catch(() => {
          clearUser();
        });
      } catch (e) {
        clearUser();
      }
    }
  };
  
  // 登出功能
  const logout = async () => {
    try {
      await authApi.logout();
    } catch (error) {
      console.error('登出API调用失败:', error);
    } finally {
      clearUser();
    }
  };

  // 检查权限
  const hasRole = (role) => {
    if (isSuperAdmin.value) return true;
    return userInfo.value.roles.includes(role) || userInfo.value.role === role;
  };
  
  // 组件挂载时初始化用户信息
  onMounted(() => {
    initUser();
  });

  return { 
    userInfo, 
    setUser, 
    clearUser, 
    initUser,
    logout,
    isStudent,
    isTeacher,
    isCompetitionAdmin,
    isSuperAdmin,
    isReviewer,
    hasRole
  };
});
