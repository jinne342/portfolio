<template>
  <div class="home-page">
    <div class="home-background">
      <div class="background-overlay"></div>
    </div>
    <Header />
    <main class="home-main">
      <div class="hero-content">
        <div class="hero-icon">🏆</div>
        <h1 class="hero-title">欢迎来到数学建模竞赛管理平台</h1>
        <p class="hero-subtitle">专业的数学建模竞赛管理与评审平台</p>
        <div class="hero-actions">
          <router-link to="/login" class="btn-primary">立即登录</router-link>
          <router-link to="/register" class="btn-secondary">免费注册</router-link>
        </div>
        <div class="feature-cards">
          <div class="feature-card">
            <div class="feature-icon">👥</div>
            <h3>团队协作</h3>
            <p>支持多人组队，协同完成数学建模竞赛</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>数据管理</h3>
            <p>智能的数据统计与可视化分析</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">🏅</div>
            <h3>专业评审</h3>
            <p>权威专家在线评审，公平公正</p>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';
</script>

<style scoped>
.home-page {
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
}

.home-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  background-image: url('https://picsum.photos/id/1011/1920/1080');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(102, 126, 234, 0.8);
  backdrop-filter: blur(1px);
}

.home-main {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 10;
  padding: 2rem;
}

.hero-content {
  text-align: center;
  color: white;
  max-width: 1200px;
  width: 100%;
}

.hero-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  animation: bounce 2s infinite;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  animation: fadeInUp 1s ease-out;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  animation: fadeInUp 1s ease-out 0.2s both;
}

.hero-actions {
  margin-bottom: 3rem;
  animation: fadeInUp 1s ease-out 0.4s both;
}

.btn-primary, .btn-secondary {
  display: inline-block;
  padding: 15px 30px;
  margin: 0 10px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.btn-primary {
  background: linear-gradient(45deg, #ff6b6b, #ee5a52);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(255, 255, 255, 0.2);
}

.feature-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
  animation: fadeInUp 1s ease-out 0.6s both;
}

.feature-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 2rem;
  text-align: center;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-10px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #fff;
}

.feature-card p {
  font-size: 1rem;
  opacity: 0.9;
  line-height: 1.6;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

/* 响应式设计 - 统一断点设置 */
/* 大屏幕 (1200px及以上) */
@media (min-width: 1200px) {
  .hero-content {
    max-width: 1400px;
  }
  
  .hero-title {
    font-size: 4rem;
  }
  
  .hero-subtitle {
    font-size: 1.8rem;
  }
  
  .feature-cards {
    grid-template-columns: repeat(3, 1fr);
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
  }
}

/* 平板横屏 (992px-1199px) */
@media (max-width: 1199px) and (min-width: 992px) {
  .hero-content {
    max-width: 1000px;
  }
  
  .hero-title {
    font-size: 3.2rem;
  }
  
  .feature-cards {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
}

/* 平板 (768px-991px) */
@media (max-width: 991px) and (min-width: 768px) {
  .hero-title {
    font-size: 2.8rem;
  }
  
  .hero-subtitle {
    font-size: 1.4rem;
  }
  
  .btn-primary, .btn-secondary {
    padding: 12px 24px;
    font-size: 1rem;
    margin: 0 8px;
  }
  
  .feature-cards {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    max-width: 600px;
    margin: 2rem auto 0;
  }
  
  .home-main {
    padding: 1.5rem;
  }
}

/* 手机横屏 (576px-767px) */
@media (max-width: 767px) and (min-width: 576px) {
  .hero-title {
    font-size: 2.2rem;
    line-height: 1.2;
  }
  
  .hero-subtitle {
    font-size: 1.1rem;
  }
  
  .btn-primary, .btn-secondary {
    display: inline-block;
    margin: 8px 5px;
    padding: 10px 20px;
    font-size: 0.95rem;
  }
  
  .feature-cards {
    grid-template-columns: 1fr;
    gap: 1.2rem;
    margin: 1.5rem auto 0;
  }
  
  .feature-card {
    padding: 1.5rem;
  }
  
  .home-main {
    padding: 1rem;
  }
}

/* 手机竖屏 (575px及以下) */
@media (max-width: 575px) {
  .hero-icon {
    font-size: 3rem;
  }
  
  .hero-title {
    font-size: 1.8rem;
    line-height: 1.3;
    margin-bottom: 0.8rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .hero-actions {
    margin-bottom: 2rem;
  }
  
  .btn-primary, .btn-secondary {
    display: block;
    margin: 10px auto;
    max-width: 220px;
    width: 100%;
    padding: 12px 20px;
    font-size: 0.95rem;
  }
  
  .feature-cards {
    grid-template-columns: 1fr;
    gap: 1rem;
    margin: 1.5rem auto 0;
    max-width: 350px;
  }
  
  .feature-card {
    padding: 1.2rem;
  }
  
  .feature-icon {
    font-size: 2.5rem;
    margin-bottom: 0.8rem;
  }
  
  .feature-card h3 {
    font-size: 1.3rem;
    margin-bottom: 0.8rem;
  }
  
  .feature-card p {
    font-size: 0.9rem;
  }
  
  .home-main {
    padding: 0.8rem;
  }
}

/* 超小屏幕优化 (400px及以下) */
@media (max-width: 400px) {
  .hero-title {
    font-size: 1.6rem;
  }
  
  .hero-subtitle {
    font-size: 0.9rem;
  }
  
  .btn-primary, .btn-secondary {
    max-width: 200px;
    padding: 10px 16px;
    font-size: 0.9rem;
  }
  
  .feature-card {
    padding: 1rem;
  }
  
  .home-main {
    padding: 0.5rem;
  }
}
</style>
