<template>
  <div class="feedback-page">
    <!-- 导航栏 -->
    <NewHeader />
    
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title">意见留言</h1>
        <p class="page-subtitle">大学生数学建模竞赛意见反馈</p>
      </div>
    </section>
    
    <!-- 留言表单 -->
    <section class="feedback-form-section">
      <div class="container">
        <div class="form-card">
          <h2 class="section-title">提交反馈</h2>
          <form class="feedback-form">
            <div class="form-grid">
              <div class="form-group">
                <label for="name">姓名</label>
                <input type="text" id="name" class="form-input" placeholder="请输入您的姓名">
              </div>
              <div class="form-group">
                <label for="email">邮箱</label>
                <input type="email" id="email" class="form-input" placeholder="请输入您的邮箱">
              </div>
              <div class="form-group">
                <label for="subject">主题</label>
                <select id="subject" class="form-select">
                  <option value="suggestion">建议</option>
                  <option value="question">问题咨询</option>
                  <option value="complaint">投诉</option>
                  <option value="praise">表扬</option>
                  <option value="other">其他</option>
                </select>
              </div>
              <div class="form-group">
                <label for="contact">联系方式</label>
                <input type="text" id="contact" class="form-input" placeholder="请输入您的联系方式（可选）">
              </div>
            </div>
            <div class="form-group full-width">
              <label for="content">反馈内容</label>
              <textarea id="content" class="form-textarea" rows="6" placeholder="请详细描述您的反馈内容"></textarea>
            </div>
            <div class="form-group full-width">
              <label for="verifyCode">验证码</label>
              <div class="verify-code-container">
                <input type="text" id="verifyCode" class="form-input verify-input" placeholder="请输入验证码">
                <div class="verify-code-image">
                  <span>验证码：1234</span>
                </div>
              </div>
            </div>
            <div class="form-actions">
              <button type="submit" class="btn-primary">提交反馈</button>
              <button type="reset" class="btn-secondary">重置表单</button>
            </div>
          </form>
        </div>
      </div>
    </section>
    
    <!-- 留言列表 -->
    <section class="feedback-list-section">
      <div class="container">
        <h2 class="section-title">最新反馈</h2>
        <div class="feedback-list">
          <div class="feedback-item">
            <div class="feedback-header">
              <div class="feedback-info">
                <div class="feedback-name">张三</div>
                <div class="feedback-meta">
                  <span class="feedback-subject">建议</span>
                  <span class="feedback-date">2024-12-28</span>
                </div>
              </div>
              <div class="feedback-status resolved">已处理</div>
            </div>
            <div class="feedback-content">
              <p>建议增加竞赛历史数据查询功能，方便学生了解往届竞赛情况。</p>
            </div>
            <div class="feedback-reply">
              <div class="reply-header">
                <span class="reply-author">管理员</span>
                <span class="reply-date">2024-12-29</span>
              </div>
              <div class="reply-content">
                <p>感谢您的建议，我们已经在规划中，预计下个版本会增加该功能。</p>
              </div>
            </div>
          </div>
          <div class="feedback-item">
            <div class="feedback-header">
              <div class="feedback-info">
                <div class="feedback-name">李四</div>
                <div class="feedback-meta">
                  <span class="feedback-subject">问题咨询</span>
                  <span class="feedback-date">2024-12-27</span>
                </div>
              </div>
              <div class="feedback-status resolved">已处理</div>
            </div>
            <div class="feedback-content">
              <p>请问如何修改团队信息？我需要更新团队成员。</p>
            </div>
            <div class="feedback-reply">
              <div class="reply-header">
                <span class="reply-author">管理员</span>
                <span class="reply-date">2024-12-27</span>
              </div>
              <div class="reply-content">
                <p>您好，请登录系统后，在团队管理页面找到您的团队，点击编辑按钮即可修改团队信息。</p>
              </div>
            </div>
          </div>
          <div class="feedback-item">
            <div class="feedback-header">
              <div class="feedback-info">
                <div class="feedback-name">王五</div>
                <div class="feedback-meta">
                  <span class="feedback-subject">表扬</span>
                  <span class="feedback-date">2024-12-26</span>
                </div>
              </div>
              <div class="feedback-status resolved">已处理</div>
            </div>
            <div class="feedback-content">
              <p>系统界面设计简洁美观，使用起来非常方便，感谢开发团队的努力！</p>
            </div>
            <div class="feedback-reply">
              <div class="reply-header">
                <span class="reply-author">管理员</span>
                <span class="reply-date">2024-12-26</span>
              </div>
              <div class="reply-content">
                <p>感谢您的肯定，我们会继续努力，为大家提供更好的服务！</p>
              </div>
            </div>
          </div>
        </div>
        <div class="pagination">
          <button class="page-btn">上一页</button>
          <button class="page-btn active">1</button>
          <button class="page-btn">2</button>
          <button class="page-btn">3</button>
          <button class="page-btn">下一页</button>
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
              <span>如何修改个人信息？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>登录系统后，在个人中心页面可以修改个人信息，包括姓名、邮箱、联系方式等。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>忘记密码怎么办？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>在登录页面点击"忘记密码"，按照提示操作即可重置密码。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>如何加入团队？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>登录系统后，在团队管理页面可以创建新团队或申请加入现有团队。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>竞赛题目什么时候公布？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>竞赛题目将于竞赛开始前30分钟在系统中公布，请及时关注系统通知。</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question">
              <span>如何提交作品？</span>
              <span class="faq-toggle">+</span>
            </div>
            <div class="faq-answer">
              <p>竞赛开始后，在系统中进入相应的竞赛页面，按照提示上传作品即可。</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 联系我们 -->
    <section class="contact-section">
      <div class="container">
        <div class="contact-card">
          <h2 class="section-title">联系我们</h2>
          <div class="contact-content">
            <p>如果您有紧急问题需要解决，可以通过以下方式联系我们：</p>
            <div class="contact-info">
              <div class="contact-item">
                <div class="contact-icon">📞</div>
                <div class="contact-details">
                  <div class="contact-label">联系电话</div>
                  <div class="contact-value">18845898263</div>
                </div>
              </div>
              <div class="contact-item">
                <div class="contact-icon">📧</div>
                <div class="contact-details">
                  <div class="contact-label">联系邮箱</div>
                  <div class="contact-value">juxiaoqi@outlook.com</div>
                </div>
              </div>
              <div class="contact-item">
                <div class="contact-icon">📍</div>
                <div class="contact-details">
                  <div class="contact-label">联系地址</div>
                  <div class="contact-value">哈尔滨理工大学理学院</div>
                </div>
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
.feedback-page {
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

/* 表单区域 */
.feedback-form-section {
  padding: 60px 0;
  background: #f8fafc;
}

.form-card {
  background: white;
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

/* 表单样式 */
.feedback-form {
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
  min-height: 150px;
}

/* 验证码 */
.verify-code-container {
  display: flex;
  gap: 16px;
  align-items: center;
}

.verify-input {
  flex: 1;
}

.verify-code-image {
  background: #f1f5f9;
  padding: 12px 20px;
  border-radius: 8px;
  font-weight: 600;
  color: #334155;
  font-size: 16px;
  min-width: 120px;
  text-align: center;
  border: 1px solid #e2e8f0;
}

/* 表单按钮 */
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

/* 留言列表 */
.feedback-list-section {
  padding: 60px 0;
  background: white;
}

.feedback-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 32px;
}

.feedback-item {
  background: #f8fafc;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.feedback-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.feedback-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.feedback-info {
  flex: 1;
}

.feedback-name {
  font-weight: 600;
  color: #1e293b;
  font-size: 16px;
  margin-bottom: 4px;
}

.feedback-meta {
  display: flex;
  gap: 12px;
  font-size: 14px;
}

.feedback-subject {
  background: #e0f2fe;
  color: #0369a1;
  padding: 2px 8px;
  border-radius: 12px;
  font-weight: 500;
}

.feedback-date {
  color: #64748b;
}

.feedback-status {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
}

.feedback-status.resolved {
  background: #d1fae5;
  color: #065f46;
}

.feedback-status.pending {
  background: #fef3c7;
  color: #92400e;
}

.feedback-content {
  margin-bottom: 20px;
  line-height: 1.6;
  color: #475569;
}

/* 回复样式 */
.feedback-reply {
  background: white;
  padding: 16px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.reply-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  font-size: 14px;
}

.reply-author {
  font-weight: 600;
  color: #334155;
}

.reply-date {
  color: #64748b;
}

.reply-content {
  line-height: 1.6;
  color: #475569;
  font-size: 14px;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
}

.page-btn {
  padding: 8px 16px;
  border: 1px solid #e2e8f0;
  background: white;
  color: #475569;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
}

.page-btn:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.page-btn.active {
  background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: #667eea;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

/* 常见问题 */
.faq-section {
  padding: 60px 0;
  background: #f8fafc;
}

.faq-list {
  max-width: 800px;
  margin: 0 auto;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.faq-item {
  border-bottom: 1px solid #e2e8f0;
}

.faq-item:last-child {
  border-bottom: none;
}

.faq-question {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  transition: all 0.3s;
  background: white;
}

.faq-question:hover {
  background: #f8fafc;
}

.faq-toggle {
  font-size: 20px;
  color: #64748b;
  transition: transform 0.3s;
}

.faq-answer {
  padding: 0 24px 20px;
  color: #475569;
  line-height: 1.6;
}

/* 联系我们 */
.contact-section {
  padding: 60px 0;
  background: white;
}

.contact-card {
  background: #f8fafc;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.contact-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.contact-content p {
  margin-bottom: 32px;
  color: #475569;
  line-height: 1.6;
}

.contact-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 16px;
  justify-content: center;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.contact-icon {
  font-size: 32px;
  flex-shrink: 0;
}

.contact-details {
  text-align: left;
}

.contact-label {
  font-weight: 600;
  color: #334155;
  font-size: 14px;
  margin-bottom: 4px;
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
  
  .verify-code-container {
    flex-direction: column;
    align-items: stretch;
  }
  
  .verify-code-image {
    text-align: left;
  }
  
  .contact-info {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .page-title {
    font-size: 24px;
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
  
  .feedback-header {
    flex-direction: column;
    gap: 12px;
  }
  
  .contact-info {
    grid-template-columns: 1fr;
  }
  
  .contact-item {
    flex-direction: column;
    text-align: center;
  }
  
  .contact-details {
    text-align: center;
  }
}
</style>