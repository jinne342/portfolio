<template>
  <div class="award-query-page">
    <!-- 导航栏 -->
    <NewHeader />
    
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title">获奖查询</h1>
        <p class="page-subtitle">查询大学生数学建模竞赛获奖信息</p>
      </div>
    </section>
    
    <!-- 查询功能区域 -->
    <section class="query-section">
      <div class="container">
        <div class="query-card">
          <h2 class="section-title">获奖信息查询</h2>
          <div class="query-form">
            <div class="form-row">
              <div class="form-group">
                <label for="competitionYear">竞赛年份</label>
                <select id="competitionYear" class="form-select">
                  <option value="">请选择竞赛年份</option>
                  <option value="2025">2025年</option>
                  <option value="2024">2024年</option>
                  <option value="2023">2023年</option>
                  <option value="2022">2022年</option>
                </select>
              </div>
              <div class="form-group">
                <label for="teamNumber">参赛编号</label>
                <input type="text" id="teamNumber" class="form-input" placeholder="请输入参赛编号">
              </div>
              <div class="form-group">
                <label for="memberName">队员姓名</label>
                <input type="text" id="memberName" class="form-input" placeholder="请输入队员姓名">
              </div>
            </div>
            <div class="form-row" style="margin-top: 20px;">
              <div class="form-group">
                <label for="schoolName">学校名称</label>
                <input type="text" id="schoolName" class="form-input" placeholder="请输入学校名称">
              </div>
              <div class="form-group">
                <label for="advisor">指导教师</label>
                <input type="text" id="advisor" class="form-input" placeholder="请输入指导教师姓名">
              </div>
              <div class="form-group btn-group" style="display: flex; gap: 12px; align-items: flex-end;">
                <button class="btn-primary" style="margin-top: 0;">查询</button>
                <button class="btn-secondary">重置</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 获奖统计 -->
    <section class="stats-section">
      <div class="container">
        <h2 class="section-title">获奖统计</h2>
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">🏆</div>
            <div class="stat-content">
              <div class="stat-number">128</div>
              <div class="stat-label">获奖团队总数</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">🥇</div>
            <div class="stat-content">
              <div class="stat-number">15</div>
              <div class="stat-label">一等奖团队</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">🥈</div>
            <div class="stat-content">
              <div class="stat-number">32</div>
              <div class="stat-label">二等奖团队</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">🥉</div>
            <div class="stat-content">
              <div class="stat-number">81</div>
              <div class="stat-label">三等奖团队</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">🎓</div>
            <div class="stat-content">
              <div class="stat-number">15,000+</div>
              <div class="stat-label">历年参赛队伍</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">🏫</div>
            <div class="stat-content">
              <div class="stat-number">500+</div>
              <div class="stat-label">获奖高校</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📊</div>
            <div class="stat-content">
              <div class="stat-number">5%</div>
              <div class="stat-label">一等奖比例</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📈</div>
            <div class="stat-content">
              <div class="stat-number">20%</div>
              <div class="stat-label">二等奖比例</div>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📉</div>
            <div class="stat-content">
              <div class="stat-number">30%</div>
              <div class="stat-label">三等奖比例</div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 获奖证书样本 -->
    <section class="certificate-section">
      <div class="container">
        <h2 class="section-title">获奖证书样本</h2>
        <div class="certificate-content">
          <div class="certificate-sample">
            <div class="certificate-border">
              <h3 class="certificate-title">全国大学生数学建模竞赛获奖证书</h3>
              <p class="certificate-text">兹证明</p>
              <p class="certificate-team">[队伍名称]</p>
              <p class="certificate-text">在[年份]年全国大学生数学建模竞赛中，荣获</p>
              <p class="certificate-grade">[获奖等级]</p>
              <p class="certificate-organization">中国工业与应用数学学会</p>
              <p class="certificate-date">[颁发日期]</p>
            </div>
          </div>
          <div class="certificate-info">
            <h3>证书说明</h3>
            <ul class="certificate-notes">
              <li>获奖证书由中国工业与应用数学学会统一颁发</li>
              <li>证书编号与参赛编号一一对应，可通过本系统查询验证</li>
              <li>证书包含队伍名称、队员姓名、获奖等级、指导教师等信息</li>
              <li>获奖证书是学生科技创新能力的重要证明，可用于评优评先、升学就业等</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 获奖名单展示 -->
    <section class="award-list-section">
      <div class="container">
        <h2 class="section-title">2025年获奖名单</h2>
        <div class="award-list-tabs">
          <button class="tab-btn active">一等奖</button>
          <button class="tab-btn">二等奖</button>
          <button class="tab-btn">三等奖</button>
          <button class="tab-btn">成功参赛奖</button>
        </div>
        <div class="award-list-table">
          <table>
            <thead>
              <tr>
                <th>团队编号</th>
                <th>团队名称</th>
                <th>学校名称</th>
                <th>参赛题目</th>
                <th>获奖等级</th>
                <th>指导教师</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>2025001</td>
                <td>数学建模精英队</td>
                <td>哈尔滨工业大学</td>
                <td>城市交通拥堵问题</td>
                <td>一等奖</td>
                <td>李教授</td>
              </tr>
              <tr>
                <td>2025002</td>
                <td>数模之星</td>
                <td>哈尔滨工程大学</td>
                <td>环境污染物扩散模型</td>
                <td>一等奖</td>
                <td>王教授</td>
              </tr>
              <tr>
                <td>2025003</td>
                <td>智慧建模团队</td>
                <td>哈尔滨理工大学</td>
                <td>互联网+时代的商业模式</td>
                <td>一等奖</td>
                <td>张教授</td>
              </tr>
              <tr>
                <td>2025004</td>
                <td>建模先锋</td>
                <td>黑龙江大学</td>
                <td>大数据分析与预测</td>
                <td>一等奖</td>
                <td>刘教授</td>
              </tr>
              <tr>
                <td>2025005</td>
                <td>数学创新团队</td>
                <td>东北林业大学</td>
                <td>生态系统可持续发展</td>
                <td>一等奖</td>
                <td>陈教授</td>
              </tr>
            </tbody>
          </table>
          <div class="pagination">
            <button class="page-btn">上一页</button>
            <button class="page-btn active">1</button>
            <button class="page-btn">2</button>
            <button class="page-btn">3</button>
            <button class="page-btn">4</button>
            <button class="page-btn">5</button>
            <button class="page-btn">下一页</button>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 常见问题 -->
    <section class="faq-section">
      <div class="container">
        <h2 class="section-title">常见问题</h2>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-question">
              <span>如何查询获奖信息？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>您可以通过团队编号、团队名称、学校名称或参赛题目进行查询。请在上方查询框中选择查询方式并输入相关信息，点击查询按钮即可获取结果。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>获奖证书什么时候发放？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>获奖证书将在颁奖典礼现场发放，或在颁奖典礼后通过邮寄方式发送给获奖团队。具体时间将在官网通知。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>查询结果有误怎么办？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>如果您发现查询结果有误，请联系竞赛组委会，提供相关证明材料，我们将尽快核实并处理。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>可以查询往届获奖信息吗？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>是的，您可以在查询框中选择竞赛年份，查询往届获奖信息。目前支持查询2022年及以后的获奖数据。</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 页脚 -->
    <footer class="footer-section">
      <div class="container">
        <div class="footer-bottom">
          <p>© 2025 大学生数学建模竞赛管理平台. 保留所有权利.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
// 获奖查询页面壳子，后续将补充具体内容
</script>

<style scoped>
.award-query-page {
  min-height: 100vh;
  background: #f8fafc;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 页面标题 */
.page-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 60px 0;
  text-align: center;
}

.page-title {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 12px;
}

.page-subtitle {
  font-size: 16px;
  opacity: 0.9;
}

/* 通用样式 */
.section-title {
  font-size: 24px;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 32px;
  text-align: center;
}

/* 查询区域 */
.query-section {
  padding: 40px 0;
  background: white;
}

.query-card {
  background: white;
  border-radius: 12px;
  padding: 32px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.query-form {
  max-width: 800px;
  margin: 0 auto;
}

.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: #334155;
  font-size: 14px;
}

.form-input,
.form-select {
  padding: 12px 16px;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.3s;
  background: white;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.btn-primary {
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: white;
  color: #64748b;
  border: 1px solid #e2e8f0;
  padding: 12px 24px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-secondary:hover {
  background: #f1f5f9;
  transform: translateY(-2px);
}

/* 统计区域 */
.stats-section {
  padding: 40px 0;
  background: #f8fafc;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin-top: 32px;
}

.stat-card {
  background: white;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  display: flex;
  align-items: center;
  gap: 16px;
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.stat-icon {
  font-size: 40px;
}

.stat-content {
  flex: 1;
}

.stat-number {
  font-size: 28px;
  font-weight: 700;
  color: #1e293b;
  line-height: 1;
}

.stat-label {
  font-size: 14px;
  color: #64748b;
  margin-top: 4px;
}

/* 证书样本区域 */
.certificate-section {
  padding: 40px 0;
  background: white;
}

.certificate-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
  margin-top: 32px;
}

.certificate-sample {
  display: flex;
  justify-content: center;
  align-items: center;
}

.certificate-border {
  background: white;
  border: 2px solid #3b82f6;
  border-radius: 8px;
  padding: 40px;
  max-width: 400px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(59, 130, 246, 0.15);
}

.certificate-title {
  font-size: 20px;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 24px;
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 16px;
}

.certificate-text {
  font-size: 16px;
  color: #475569;
  margin: 12px 0;
}

.certificate-team {
  font-size: 18px;
  font-weight: 600;
  color: #1e293b;
  margin: 16px 0;
}

.certificate-grade {
  font-size: 24px;
  font-weight: 700;
  color: #f59e0b;
  margin: 20px 0;
}

.certificate-organization {
  font-size: 16px;
  color: #1e293b;
  margin: 24px 0 12px;
  font-weight: 600;
}

.certificate-date {
  font-size: 14px;
  color: #64748b;
  margin-top: 8px;
}

.certificate-info {
  padding: 24px;
}

.certificate-info h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 16px;
}

.certificate-notes {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.certificate-notes li {
  color: #475569;
  line-height: 1.6;
  position: relative;
  padding-left: 20px;
}

.certificate-notes li:before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #10b981;
  font-weight: bold;
}

/* 获奖名单区域 */
.award-list-section {
  padding: 40px 0;
  background: #f8fafc;
}

.award-list-tabs {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 10px 20px;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  color: #64748b;
}

.tab-btn:hover {
  background: #f1f5f9;
  color: #334155;
}

.tab-btn.active {
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  border-color: #667eea;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.award-list-table {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.award-list-table table {
  width: 100%;
  border-collapse: collapse;
}

.award-list-table th,
.award-list-table td {
  padding: 16px;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

.award-list-table th {
  background: #f8fafc;
  font-weight: 600;
  color: #334155;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.award-list-table td {
  color: #475569;
  font-size: 14px;
}

.award-list-table tr:hover {
  background: #f8fafc;
}

.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 20px;
  background: white;
}

.page-btn {
  padding: 8px 16px;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
  color: #64748b;
  font-size: 14px;
}

.page-btn:hover {
  background: #f1f5f9;
  color: #334155;
}

.page-btn.active {
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  border-color: #667eea;
}

/* 常见问题区域 */
.faq-section {
  padding: 40px 0;
  background: white;
}

.faq-list {
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
  transition: all 0.3s;
}

.faq-question:hover {
  color: #667eea;
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

/* 页脚区域 */
.footer-section {
  background: #020617;
  color: white;
  padding: 60px 0 20px;
}

.footer-bottom {
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 14px;
  opacity: 0.6;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .certificate-content {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
  
  .stat-card {
    padding: 20px;
  }
  
  .query-card {
    padding: 24px;
  }
  
  .award-list-table th,
  .award-list-table td {
    padding: 12px;
    font-size: 13px;
  }
}

@media (max-width: 480px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .page-title {
    font-size: 24px;
  }
  
  .section-title {
    font-size: 20px;
  }
  
  .certificate-border {
    padding: 24px;
  }
}
</style>