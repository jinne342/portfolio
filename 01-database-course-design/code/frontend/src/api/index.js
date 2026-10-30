import axios from 'axios';
import { showError } from '../utils/notification.js';

// 从环境变量读取后端地址，如果没有则使用默认值
// 开发环境：http://localhost:8000/api
// 生产环境：通过环境变量 VITE_API_BASE_URL 配置
const baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

console.log('API Base URL:', baseURL);

const service = axios.create({
  baseURL,
  timeout: 30000, // 增加超时时间到30秒，避免大数据量查询超时
  // 不设置默认的Content-Type，让浏览器根据数据类型自动设置
  // 对于文件上传，浏览器会自动设置为'multipart/form-data'
  headers: {
    // 'Content-Type' 将根据数据类型自动设置
  }
});

// 请求拦截器
service.interceptors.request.use(
  config => {
    // 添加token
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    } else {
      // 如果没有token，尝试从userInfo中获取
      const userInfo = localStorage.getItem('userInfo');
      if (userInfo) {
        try {
          const user = JSON.parse(userInfo);
          if (user.token) {
            config.headers.Authorization = `Bearer ${user.token}`;
          }
        } catch (e) {
          // 忽略解析错误
        }
      }
    }
    
    // 打印请求信息（开发环境）
    if (import.meta.env.DEV) {
      console.log('请求:', config.method?.toUpperCase(), config.url, config.data || config.params);
    }
    
    return config;
  },
  error => {
    console.error('请求错误:', error);
    return Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use(
  response => {
    // 如果响应数据是对象且包含data字段，直接返回data
    // 否则返回整个response.data
    const data = response.data;
    
    // 打印响应信息（开发环境）
    if (import.meta.env.DEV) {
      console.log('响应:', response.config.url, data);
    }
    
    // 如果后端返回的是 { code, message, data } 格式
    if (data && typeof data === 'object' && 'code' in data) {
      if (data.code === 200 || data.code === 0) {
        // 对于登录和注册接口，返回整个data对象（包含code、message、data）
        // 对于其他接口，返回data字段
        if (response.config.url?.includes('/login') || response.config.url?.includes('/register')) {
          return data;  // 登录和注册接口返回完整对象
        }
        return data.data !== undefined ? data.data : data;
      } else {
        // 业务错误
        showError(data.message || '请求失败');
        return Promise.reject(new Error(data.message || '请求失败'));
      }
    }
    
    // 直接返回data（兼容不同的响应格式）
    return data;
  },
  error => {
    console.error('响应错误:', error);
    
    // 处理HTTP错误
    if (error.response) {
      const { status, data } = error.response;
      
      switch (status) {
        case 401:
          showError('未授权，请重新登录');
          // 清除token并跳转到登录页
          localStorage.removeItem('token');
          if (window.location.pathname !== '/login') {
            window.location.href = '/login';
          }
          break;
        case 403:
          showError('没有权限访问');
          break;
        case 404:
          showError('请求的资源不存在');
          break;
        case 500:
          showError(data?.message || '服务器内部错误');
          break;
        case 503:
          showError('服务暂时不可用，请稍后重试');
          break;
        default:
          showError(data?.message || `请求失败 (${status})`);
      }
    } else if (error.request) {
      // 请求已发出但没有收到响应（超时）
      if (error.code === 'ECONNABORTED' || error.message.includes('timeout')) {
        showError('请求超时，请稍后重试或检查网络连接');
      } else {
        showError('网络错误，请检查网络连接');
      }
    } else {
      // 其他错误
      showError(error.message || '请求失败');
    }
    
    return Promise.reject(error);
  }
);

export default service;
export const request = service;
