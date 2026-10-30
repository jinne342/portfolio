import { createApp } from 'vue';
import { createPinia } from 'pinia';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import App from './App.vue';
import router from './router/index.js';
import { useUserStore } from './store/user.js';

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(ElementPlus);

// 初始化用户状态
const userStore = useUserStore();
userStore.initUser();

// 全局错误处理
app.config.errorHandler = (err, vm, info) => {
  console.error('全局错误:', err);
  console.error('组件:', vm);
  console.error('错误信息:', info);
};

app.mount('#app');