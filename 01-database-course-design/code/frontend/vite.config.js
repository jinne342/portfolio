// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  plugins: [vue()],
  // CSS配置
  css: {
    postcss: false,  // 禁用PostCSS，绕过Tailwind报错
    devSourcemap: true  // 开发环境启用sourcemap
  },
  server: {
    // 前端服务端口（固定为5173）
    port: 5173,
    host: '0.0.0.0',  // 允许外部访问
    strictPort: true,  // 严格使用指定端口，如果被占用则报错
    // 代理配置：将 /api 请求代理到后端
    proxy: {
      '/api': {
        target: process.env.VITE_API_BASE_URL || 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path,  // 不重写路径
        configure: (proxy, options) => {
          proxy.on('error', (err, req, res) => {
            console.log('代理错误:', err);
          });
        }
      }
    },
    // 自动打开浏览器
    open: false,
    // 热更新配置
    hmr: {
      overlay: true,  // 显示错误覆盖层
      protocol: 'ws',  // WebSocket协议
      host: 'localhost'
    },
    // CORS配置
    cors: true
  },
  // 构建配置
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,  // 生产环境不生成sourcemap
    // 压缩配置
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,  // 移除console
        drop_debugger: true  // 移除debugger
      }
    },
    // 分块配置
    rollupOptions: {
      output: {
        manualChunks: {
          'vue-vendor': ['vue', 'vue-router', 'pinia'],
          'chart-vendor': ['echarts', 'vue-echarts']
        }
      }
    },
    // 构建大小警告阈值（KB）
    chunkSizeWarningLimit: 1000
  },
  // 环境变量前缀
  envPrefix: 'VITE_',
  // 优化配置
  optimizeDeps: {
    include: ['vue', 'vue-router', 'pinia', 'axios', 'echarts']
  }
});