<template>
  <div class="apply-cooperation-page">
    <!-- 导航栏 -->
    <NewHeader />
    
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title">申请协办</h1>
        <p class="page-subtitle">大学生数学建模竞赛协办申请</p>
      </div>
    </section>
    
    <!-- 协办介绍 -->
    <section class="intro-section">
      <div class="container">
        <div class="intro-card">
          <h2 class="section-title">关于协办</h2>
          <div class="intro-content">
            <p>大学生数学建模竞赛是一项具有广泛影响力的学科竞赛活动，旨在培养大学生的创新能力、团队协作精神和解决实际问题的能力。我们诚邀各高校、企业和科研机构参与协办，共同推动数学建模教育事业的发展。</p>
            <p>作为协办单位，您将获得展示品牌形象、接触优秀人才、提升社会影响力的机会，同时也为推动中国数学建模事业发展做出贡献。</p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 申请表单 -->
    <section class="form-section">
      <div class="container">
        <div class="form-card">
          <h2 class="section-title">协办申请表</h2>
          <form class="cooperation-form">
            <div class="form-grid">
              <div class="form-group">
                <label for="unitName">单位名称</label>
                <input type="text" id="unitName" class="form-input" placeholder="请输入单位名称">
              </div>
              <div class="form-group">
                <label for="unitType">单位类型</label>
                <select id="unitType" class="form-select">
                  <option value="university">高等院校</option>
                  <option value="enterprise">企业</option>
                  <option value="institute">科研机构</option>
                  <option value="other">其他</option>
                </select>
              </div>
              <div class="form-group">
                <label for="contactPerson">联系人</label>
                <input type="text" id="contactPerson" class="form-input" placeholder="请输入联系人姓名">
              </div>
              <div class="form-group">
                <label for="contactPhone">联系电话</label>
                <input type="tel" id="contactPhone" class="form-input" placeholder="请输入联系电话">
              </div>
              <div class="form-group">
                <label for="contactEmail">联系邮箱</label>
                <input type="email" id="contactEmail" class="form-input" placeholder="请输入联系邮箱">
              </div>
              <div class="form-group">
                <label for="cooperationType">协办类型</label>
                <select id="cooperationType" class="form-select">
                  <option value="academic">学术支持</option>
                  <option value="financial">资金支持</option>
                  <option value="venue">场地支持</option>
                  <option value="technical">技术支持</option>
                  <option value="media">媒体支持</option>
                  <option value="other">其他</option>
                </select>
              </div>
            </div>
            
            <div class="form-group full-width">
              <label for="unitIntroduction">单位简介</label>
              <textarea id="unitIntroduction" class="form-textarea" rows="4" placeholder="请简要介绍贵单位的基本情况、发展历程和主要业务"></textarea>
            </div>
            
            <div class="form-group full-width">
              <label for="cooperationPlan">协办计划</label>
              <textarea id="cooperationPlan" class="form-textarea" rows="6" placeholder="请详细描述贵单位的协办意向、可提供的资源和支持方式"></textarea>
            </div>
            
            <div class="form-actions">
              <button type="submit" class="btn-primary">提交申请</button>
              <button type="reset" class="btn-secondary">重置表单</button>
            </div>
          </form>
        </div>
      </div>
    </section>
    
    <!-- 协办优势 -->
    <section class="benefits-section">
      <div class="container">
        <h2 class="section-title">协办优势</h2>
        <div class="benefits-grid">
          <div class="benefit-card">
            <div class="benefit-icon">🏢</div>
            <h3 class="benefit-title">品牌推广</h3>
            <p>通过竞赛平台展示单位形象，提升品牌知名度和社会影响力</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">👥</div>
            <h3 class="benefit-title">人才对接</h3>
            <p>接触优秀学生和专业人才，为单位人才招聘和储备提供机会</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🔬</div>
            <h3 class="benefit-title">学术合作</h3>
            <p>与高校和科研机构建立合作关系，推动产学研深度融合</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">📊</div>
            <h3 class="benefit-title">行业影响力</h3>
            <p>参与学科竞赛，提升在相关领域的专业影响力和话语权</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🤝</div>
            <h3 class="benefit-title">资源共享</h3>
            <p>共享竞赛资源和平台，拓展单位的合作网络和发展空间</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🏆</div>
            <h3 class="benefit-title">社会贡献</h3>
            <p>支持教育事业发展，履行社会责任，树立良好社会形象</p>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 协办要求与流程 -->
    <section class="requirements-section">
      <div class="container">
        <div class="requirements-content">
          <div class="requirements-card">
            <h2 class="section-title">协办要求</h2>
            <ul class="requirements-list">
              <li>• 具有合法资质和良好的社会信誉</li>
              <li>• 认同数学建模竞赛的理念和宗旨</li>
              <li>• 具备一定的资源和能力，能够为竞赛提供支持</li>
              <li>• 能够遵守竞赛组委会的相关规定和安排</li>
              <li>• 愿意与组委会保持良好的沟通和合作关系</li>
            </ul>
          </div>
          
          <div class="process-card">
            <h2 class="section-title">申请流程</h2>
            <div class="process-steps">
              <div class="process-step">
                <div class="process-number">1</div>
                <div class="process-content">
                  <h4>提交申请</h4>
                  <p>填写并提交协办申请表</p>
                </div>
              </div>
              <div class="process-arrow">→</div>
              <div class="process-step">
                <div class="process-number">2</div>
                <div class="process-content">
                  <h4>资格审核</h4>
                  <p>组委会审核申请材料</p>
                </div>
              </div>
              <div class="process-arrow">→</div>
              <div class="process-step">
                <div class="process-number">3</div>
                <div class="process-content">
                  <h4>沟通洽谈</h4>
                  <p>双方就合作细节进行沟通</p>
                </div>
              </div>
              <div class="process-arrow">→</div>
              <div class="process-step">
                <div class="process-number">4</div>
                <div class="process-content">
                  <h4>签订协议</h4>
                  <p>签订协办协议</p>
                </div>
              </div>
              <div class="process-arrow">→</div>
              <div class="process-step">
                <div class="process-number">5</div>
                <div class="process-content">
                  <h4>正式合作</h4>
                  <p>开始执行协办工作</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 联系信息 -->
    <section class="contact-section">
      <div class="container">
        <div class="contact-card">
          <h2 class="section-title">联系我们</h2>
          <div class="contact-content">
            <p>如果您对协办事宜有任何疑问，欢迎随时联系我们：</p>
            <div class="contact-info">
              <div class="contact-item">
                <div class="contact-label">联系人：</div>
                <div class="contact-value">李老师</div>
              </div>
              <div class="contact-item">
                <div class="contact-label">联系电话：</div>
                <div class="contact-value">18845898263</div>
              </div>
              <div class="contact-item">
                <div class="contact-label">联系邮箱：</div>
                <div class="contact-value">juxiaoqi@outlook.com</div>
              </div>
              <div class="contact-item">
                <div class="contact-label">联系地址：</div>
                <div class="contact-value">哈尔滨理工大学理学院</div>
              </div>
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
import NewHeader from '../components/NewHeader.vue';
</script>

<style scoped>
.apply-cooperation-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
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

/* 通用容器 */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 介绍区域 */
.intro-section {
  padding: 60px 0;
  background: white;
}

.intro-card {
  background: #f8fafc;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.section-title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #1e293b;
  text-align: center;
}

.intro-content {
  line-height: 1.8;
  color: #475569;
  max-width: 800px;
  margin: 0 auto;
}

.intro-content p {
  margin-bottom: 16px;
}

/* 表单区域 */
.form-section {
  padding: 60px 0;
  background: #f8fafc;
}

.form-card {
  background: white;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.cooperation-form {
  max-width: 900px;
  margin: 0 auto;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-group label {
  font-weight: 600;
  color: #334155;
  font-size: 14px;
}

.form-input,
.form-select,
.form-textarea {
  padding: 12px 16px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.3s;
  font-family: inherit;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 120px;
}

.form-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-top: 32px;
}

.btn-primary {
  display: inline-block;
  padding: 12px 32px;
  background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  display: inline-block;
  padding: 12px 32px;
  background: white;
  color: #667eea;
  border: 1px solid #667eea;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.15);
}

.btn-secondary:hover {
  background: #f8fafc;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
}

/* 协办优势 */
.benefits-section {
  padding: 60px 0;
  background: white;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-top: 40px;
}

.benefit-card {
  background: #f8fafc;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.benefit-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.benefit-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.benefit-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1e293b;
}

.benefit-card p {
  color: #475569;
  line-height: 1.6;
}

/* 要求与流程 */
.requirements-section {
  padding: 60px 0;
  background: #f8fafc;
}

.requirements-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  max-width: 1000px;
  margin: 0 auto;
}

.requirements-card,
.process-card {
  background: white;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.requirements-list {
  list-style: none;
  padding: 0;
  margin: 0;
  line-height: 2;
  color: #475569;
}

.requirements-list li {
  position: relative;
  padding-left: 24px;
}

.requirements-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #667eea;
  font-weight: bold;
}

/* 流程步骤 */
.process-steps {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.process-step {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.process-number {
  width: 32px;
  height: 32px;
  background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
  margin-top: 4px;
}

.process-content h4 {
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 8px;
}

.process-content p {
  color: #475569;
  font-size: 14px;
}

.process-arrow {
  color: #667eea;
  font-size: 20px;
  text-align: center;
  margin: 8px 0;
}

/* 联系信息 */
.contact-section {
  padding: 60px 0;
  background: white;
}

.contact-card {
  background: #f8fafc;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  text-align: center;
}

.contact-content {
  max-width: 600px;
  margin: 0 auto;
}

.contact-content p {
  margin-bottom: 24px;
  color: #475569;
  line-height: 1.6;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
}

.contact-item {
  display: flex;
  gap: 12px;
  align-items: center;
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

/* 页脚 */
.footer-section {
  background: #020617;
  color: white;
  padding: 40px 0 20px;
  margin-top: auto;
}

.footer-bottom {
  text-align: center;
  font-size: 14px;
  opacity: 0.6;
}

/* 响应式设计 */
@media (max-width: 991px) {
  .form-grid {
    grid-template-columns: 1fr;
  }
  
  .requirements-content {
    grid-template-columns: 1fr;
  }
  
  .benefits-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .page-title {
    font-size: 24px;
  }
  
  .benefits-grid {
    grid-template-columns: 1fr;
  }
  
  .form-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .btn-primary,
  .btn-secondary {
    width: 200px;
    text-align: center;
  }
  
  .intro-card,
  .form-card,
  .requirements-card,
  .process-card,
  .contact-card {
    padding: 24px;
  }
}
</style>