<template>
  <div class="new-home">
    <!-- 导航栏 -->
    <NewHeader />
    
    <!-- 英雄区域 -->
    <section class="hero-section">
      <div class="hero-content">
        <div class="hero-icon">🏆</div>
        <h1 class="hero-title">欢迎来到大学生数学建模竞赛管理系统</h1>
        <p class="hero-subtitle">专业的数学建模竞赛管理与评审平台</p>
        <div class="hero-actions">
          <router-link to="/login" class="btn-primary">立即登录</router-link>
          <router-link to="/register" class="btn-secondary">免费注册</router-link>
        </div>
      </div>
    </section>
    
    <!-- 竞赛倒计时 -->
    <section class="countdown-section">
      <div class="container">
        <h2 class="section-title">竞赛倒计时</h2>
        <div class="countdown-container">
          <div class="countdown-boxes">
            <div class="countdown-box">
              <div class="countdown-number">{{ days }}</div>
              <div class="countdown-label">天</div>
            </div>
            <div class="countdown-separator">:</div>
            <div class="countdown-box">
              <div class="countdown-number">{{ hours }}</div>
              <div class="countdown-label">时</div>
            </div>
            <div class="countdown-separator">:</div>
            <div class="countdown-box">
              <div class="countdown-number">{{ minutes }}</div>
              <div class="countdown-label">分</div>
            </div>
            <div class="countdown-separator">:</div>
            <div class="countdown-box">
              <div class="countdown-number">{{ seconds }}</div>
              <div class="countdown-label">秒</div>
            </div>
          </div>
          <div class="countdown-text">距离2026年美国大学生数学建模竞赛开始还有</div>
        </div>
        <div class="notice-card">
          <h3>注意事项</h3>
          <ul class="notice-list">
            <li>• 所有时间节点均为北京时间，请参赛选手注意时间问题。</li>
            <li>• 报名截止时间为2025年12月31日24:00，逾期将无法报名。</li>
            <li>• 竞赛开始前30分钟，参赛选手可登录系统下载竞赛题目。</li>
            <li>• 竞赛结束后，系统将自动关闭提交通道，请务必在最后一刻提交。</li>
            <li>• 如有特殊情况需要调整时间，将通过官方网站和QQ群通知。</li>
          </ul>
        </div>
      </div>
    </section>
    
    <!-- 系统介绍 -->
    <section id="system-intro" class="system-intro-section">
      <div class="container">
        <h2 class="section-title">系统介绍</h2>
        <div class="system-content">
          <div class="system-features">
            <h3>管理系统简介</h3>
            <p>大学生数学建模竞赛管理系统是一个集报名、评审、统计于一体的综合平台，为参赛队伍和评审专家提供便捷的服务。</p>
            <ul class="feature-list">
              <li>• 支持多角色管理（学生、教师、管理员）</li>
              <li>• 在线报名和组队管理</li>
              <li>• 专家评审和成绩统计</li>
              <li>• 证书生成和发放</li>
              <li>• 违规处理和通知</li>
            </ul>
          </div>
          <div class="system-flow">
            <h3>系统使用流程</h3>
            <div class="flow-steps">
              <div class="flow-step">
                <div class="flow-number">1</div>
                <div class="flow-text">注册登录</div>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-step">
                <div class="flow-number">2</div>
                <div class="flow-text">创建/加入队伍</div>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-step">
                <div class="flow-number">3</div>
                <div class="flow-text">提交作品</div>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-step">
                <div class="flow-number">4</div>
                <div class="flow-text">专家评审</div>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-step">
                <div class="flow-number">5</div>
                <div class="flow-text">成绩公布</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 奖项设置 -->
    <section id="award-setting" class="award-section">
      <div class="container">
        <h2 class="section-title">奖项设置</h2>
        <div class="award-cards">
          <div class="award-card">
            <div class="award-icon gold">🏅</div>
            <h3 class="award-title">一等奖</h3>
            <p class="award-desc">授予在数学建模竞赛中表现优异的团队</p>
            <p class="award-benefit">奖励金额：¥5000</p>
            <p class="award-benefit">颁发证书：一等奖证书</p>
          </div>
          <div class="award-card">
            <div class="award-icon silver">🥈</div>
            <h3 class="award-title">二等奖</h3>
            <p class="award-desc">授予在数学建模竞赛中表现良好的团队</p>
            <p class="award-benefit">奖励金额：¥3000</p>
            <p class="award-benefit">颁发证书：二等奖证书</p>
          </div>
          <div class="award-card">
            <div class="award-icon bronze">🥉</div>
            <h3 class="award-title">三等奖</h3>
            <p class="award-desc">授予在数学建模竞赛中表现合格的团队</p>
            <p class="award-benefit">奖励金额：¥1000</p>
            <p class="award-benefit">颁发证书：三等奖证书</p>
          </div>
          <div class="award-card">
            <div class="award-icon participation">🎖️</div>
            <h3 class="award-title">成功参赛奖</h3>
            <p class="award-desc">授予所有成功提交作品的团队</p>
            <p class="award-benefit">奖励金额：¥200</p>
            <p class="award-benefit">颁发证书：参赛证书</p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 使用说明 -->
    <section id="usage-instruction" class="usage-section">
      <div class="container">
        <h2 class="section-title">使用说明</h2>
        <div class="usage-content">
          <div class="usage-rules">
            <h3>使用规则</h3>
            <div class="rule-card">
              <h4>参赛规则</h4>
              <p>参赛队伍由3名学生组成，需在规定时间内完成数学建模论文并提交。</p>
              <p>参赛作品必须为原创，不得抄袭或剽窃他人成果。</p>
            </div>
            <div class="rule-card">
              <h4>评审规则</h4>
              <p>评审采用匿名评审方式，由专家团队根据评分标准进行评分。</p>
              <p>评审结果将在竞赛结束后15个工作日内公布。</p>
            </div>
          </div>
          <div class="competition-notes">
            <h3>参赛须知</h3>
            <ul class="notes-list">
              <li>• 参赛费用：免费</li>
              <li>• 参赛资格：在校大学生</li>
              <li>• 报名时间：每年3月1日 - 4月30日</li>
              <li>• 竞赛时间：每年5月1日 - 5月4日</li>
              <li>• 提交截止时间：5月4日20:00</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 联系我们和常见问题 -->
    <section class="contact-section">
      <div class="container">
        <h2 class="section-title">联系我们</h2>
        <div class="contact-content">
          <div class="contact-info">
            <div class="contact-item">
              <div class="contact-label">联系电话：</div>
              <div class="contact-value">18845898263</div>
            </div>
            <div class="contact-item">
              <div class="contact-label">联系邮箱：</div>
              <div class="contact-value">juxiaoqi@outlook.com</div>
            </div>
            <div class="contact-item">
              <div class="contact-label">官方QQ：</div>
              <div class="contact-value">123456789</div>
            </div>
            <div class="contact-item">
              <div class="contact-label">联系地址：</div>
              <div class="contact-value">哈尔滨理工大学理学院</div>
            </div>
          </div>
        </div>
        
        <h2 class="section-title">常见问题</h2>
        <div class="faq-content">
          <div class="faq-item">
            <div class="faq-question">
              <span>如何查询获奖信息？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>获奖名单将在官方网站公示，您可以通过团队编号或参赛题目在官网查询获奖信息。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>获奖证书什么时候发放？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>获奖证书将在颁奖典礼现场发放，或在颁奖典礼后通过邮寄方式发送给获奖团队。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>奖金如何发放？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>奖金将通过银行转账方式发放到获奖团队队长的银行账户，具体发放时间将在颁奖典礼后另行通知。</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 页脚 -->
    <footer class="footer-section">
      <div class="container">
        <div class="footer-content">
          <div class="footer-left">
            <h3>哈尔滨地区数学建模竞赛</h3>
            <p>致力于推动哈尔滨地区高校数学建模教育事业的发展</p>
            <div class="footer-contact">
              <p>电话：18845898263</p>
              <p>邮箱：juxiaoqi@outlook.com</p>
              <p>地址：哈尔滨理工大学理学院</p>
            </div>
          </div>
          <div class="footer-center">
            <h4>快速链接</h4>
            <div class="footer-links">
              <router-link to="/">首页</router-link>
              <router-link to="/competition-detail">竞赛详情</router-link>
              <router-link to="/competition-news">竞赛新闻</router-link>
              <router-link to="/award-query">竞赛奖项</router-link>
              <router-link to="/competition-time">参赛指南</router-link>
              <router-link to="/past-reviews">建模资源</router-link>
              <router-link to="/past-reviews">往届试题</router-link>
            </div>
          </div>
          <div class="footer-right">
            <div class="footer-actions">
              <router-link to="#" class="btn-download">下载题目</router-link>
              <router-link to="/register" class="btn-register-footer">报名参赛</router-link>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2025 大学生数学建模竞赛管理平台. 保留所有权利.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import NewHeader from '../components/NewHeader.vue';

// 竞赛倒计时功能
const days = ref('00');
const hours = ref('00');
const minutes = ref('00');
const seconds = ref('00');

let countdownInterval = null;

const updateCountdown = () => {
  // 设定竞赛开始时间（2026年美国大学生数学建模竞赛）
  const competitionDate = new Date('2026-01-30T08:00:00');
  const now = new Date();
  const diff = competitionDate - now;
  
  if (diff <= 0) {
    days.value = '00';
    hours.value = '00';
    minutes.value = '00';
    seconds.value = '00';
    return;
  }
  
  days.value = Math.floor(diff / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');
  hours.value = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');
  minutes.value = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');
  seconds.value = Math.floor((diff % (1000 * 60)) / 1000).toString().padStart(2, '0');
};

onMounted(() => {
  updateCountdown();
  countdownInterval = setInterval(updateCountdown, 1000);
});

onUnmounted(() => {
  if (countdownInterval) {
    clearInterval(countdownInterval);
  }
});
</script>

<style scoped>
.new-home {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* 英雄区域 */
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 80px 0;
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.hero-title {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
}

.hero-subtitle {
  font-size: 18px;
  margin-bottom: 32px;
  opacity: 0.9;
}

.hero-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn-primary {
  display: inline-block;
  padding: 12px 32px;
  background: linear-gradient(45deg, #ff6b6b, #ee5a52);
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(255, 107, 107, 0.4);
}

.btn-secondary {
  display: inline-block;
  padding: 12px 32px;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

/* 竞赛倒计时 */
.countdown-section {
  padding: 60px 0;
  background: white;
}

.countdown-container {
  text-align: center;
  margin-bottom: 40px;
}

.countdown-boxes {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  margin-bottom: 16px;
}

.countdown-box {
  background: #3b82f6;
  color: white;
  padding: 20px;
  border-radius: 8px;
  min-width: 80px;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

.countdown-number {
  font-size: 36px;
  font-weight: 700;
  line-height: 1;
}

.countdown-label {
  font-size: 14px;
  margin-top: 8px;
  opacity: 0.9;
}

.countdown-separator {
  font-size: 36px;
  font-weight: 700;
  color: #3b82f6;
  line-height: 1;
}

.countdown-text {
  font-size: 16px;
  color: #475569;
  margin-top: 16px;
}

.notice-card {
  background: #fef3c7;
  border: 1px solid #fde68a;
  border-radius: 8px;
  padding: 24px;
  margin-top: 40px;
}

.notice-card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #92400e;
}

.notice-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.notice-list li {
  color: #92400e;
  line-height: 1.8;
  margin-bottom: 8px;
}

/* 通用容器样式 */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 系统介绍 */
.system-intro-section {
  padding: 60px 0;
  background: #f8fafc;
}

.section-title {
  text-align: center;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 40px;
  color: #1e293b;
}

.system-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.system-features h3,
.system-flow h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #334155;
}

.feature-list {
  margin-top: 20px;
  line-height: 1.8;
  color: #475569;
}

.flow-steps {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-top: 20px;
}

.flow-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.flow-number {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}

.flow-text {
  color: #475569;
  font-size: 14px;
}

.flow-arrow {
  color: #667eea;
  font-size: 20px;
  font-weight: bold;
}

/* 奖项设置 */
.award-section {
  padding: 60px 0;
  background: white;
}

.award-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.award-card {
  background: #f8fafc;
  padding: 24px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.award-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.award-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.award-icon.gold {
  color: #fbbf24;
}

.award-icon.silver {
  color: #9ca3af;
}

.award-icon.bronze {
  color: #d97706;
}

.award-icon.participation {
  color: #6b7280;
}

.award-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1e293b;
}

.award-desc {
  margin-bottom: 16px;
  color: #475569;
  line-height: 1.6;
}

.award-benefit {
  font-size: 14px;
  color: #64748b;
  margin-bottom: 8px;
}

/* 使用说明 */
.usage-section {
  padding: 60px 0;
  background: #f8fafc;
}

.usage-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.usage-rules h3,
.competition-notes h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 20px;
  color: #334155;
}

.rule-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  margin-bottom: 16px;
}

.rule-card h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1e293b;
}

.rule-card p {
  margin-bottom: 8px;
  color: #475569;
  line-height: 1.6;
}

.notes-list {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  line-height: 1.8;
  color: #475569;
}

/* 联系我们 */
.contact-section {
  padding: 60px 0;
  background: white;
}

.contact-content {
  margin-bottom: 60px;
}

.contact-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  justify-items: center;
  text-align: center;
}

.contact-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.contact-label {
  font-weight: 600;
  color: #334155;
  font-size: 14px;
}

.contact-value {
  color: #475569;
  font-size: 16px;
}

/* 常见问题 */
.faq-content {
  max-width: 800px;
  margin: 0 auto;
}

.faq-item {
  margin-bottom: 16px;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 16px;
}

.faq-question {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  padding: 8px 0;
}

.faq-toggle {
  color: #64748b;
  font-size: 20px;
  font-weight: 300;
  transition: transform 0.3s;
}

.faq-answer {
  padding: 16px 0;
  color: #475569;
  line-height: 1.6;
}

/* 页脚 */
.footer-section {
  background: #020617;
  color: white;
  padding: 60px 0 20px;
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 40px;
  margin-bottom: 40px;
}

.footer-left h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
}

.footer-left p {
  margin-bottom: 16px;
  opacity: 0.8;
  line-height: 1.6;
}

.footer-contact p {
  font-size: 14px;
  margin-bottom: 8px;
  opacity: 0.8;
}

.footer-center h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 16px;
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.footer-links a {
  color: white;
  text-decoration: none;
  font-size: 14px;
  opacity: 0.8;
  transition: opacity 0.3s;
}

.footer-links a:hover {
  opacity: 1;
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.footer-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.btn-download {
  display: inline-block;
  padding: 12px 24px;
  background: #ef4444;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
}

.btn-download:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
}

.btn-register-footer {
  display: inline-block;
  padding: 12px 24px;
  background: #3b82f6;
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
}

.btn-register-footer:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
}

.footer-bottom {
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 14px;
  opacity: 0.6;
}

/* 响应式设计 */
@media (max-width: 991px) {
  .system-content,
  .usage-content,
  .footer-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .award-cards {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .flow-steps {
    gap: 16px;
    justify-content: center;
  }
  
  .contact-info {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  
  .footer-right {
    align-items: flex-start;
  }
}

@media (max-width: 767px) {
  .hero-title {
    font-size: 28px;
  }
  
  .hero-subtitle {
    font-size: 16px;
  }
  
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .btn-primary,
  .btn-secondary {
    width: 200px;
    text-align: center;
  }
  
  .section-title {
    font-size: 24px;
  }
  
  .award-cards {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .award-card {
    padding: 20px;
  }
  
  .countdown-boxes {
    gap: 8px;
  }
  
  .countdown-box {
    padding: 12px;
    min-width: 60px;
  }
  
  .countdown-number {
    font-size: 24px;
  }
  
  .countdown-separator {
    font-size: 24px;
  }
  
  .footer-links {
    grid-template-columns: 1fr;
  }
}
</style>