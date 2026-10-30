<template>
  <div class="past-reviews-page">
    <!-- 导航栏 -->
    <NewHeader />
    
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title">往届回顾</h1>
        <p class="page-subtitle">大学生数学建模竞赛往届回顾</p>
      </div>
    </section>
    
    <!-- 年份选择 -->
    <section class="year-select-section">
      <div class="container">
        <div class="year-selector">
          <h2 class="section-title">选择年份</h2>
          <div class="year-buttons">
            <button class="year-btn active">2024</button>
            <button class="year-btn">2023</button>
            <button class="year-btn">2022</button>
            <button class="year-btn">2021</button>
            <button class="year-btn">2020</button>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 竞赛概览 -->
    <section class="overview-section">
      <div class="container">
        <div class="overview-card">
          <h2 class="section-title">2024年竞赛概览</h2>
          <div class="overview-content">
            <div class="overview-text">
              <p>2024年大学生数学建模竞赛于5月1日至5月4日成功举办，共有来自全国28个省市自治区的156所高校，1256支队伍参加了本次竞赛。竞赛共设置了A、B、C、D四个题目，涵盖了交通、环境、经济、医疗等多个领域的实际问题。</p>
              <p>经过专家评审，共评选出一等奖18项，二等奖36项，三等奖72项，成功参赛奖200项。本次竞赛的参赛队伍数量和质量均创历史新高，充分展示了大学生的创新能力和团队协作精神。</p>
            </div>
            <div class="overview-stats">
              <div class="stat-item">
                <div class="stat-number">156</div>
                <div class="stat-label">参赛高校</div>
              </div>
              <div class="stat-item">
                <div class="stat-number">1256</div>
                <div class="stat-label">参赛队伍</div>
              </div>
              <div class="stat-item">
                <div class="stat-number">3768</div>
                <div class="stat-label">参赛学生</div>
              </div>
              <div class="stat-item">
                <div class="stat-number">4</div>
                <div class="stat-label">竞赛题目</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 获奖情况 -->
    <section class="awards-section">
      <div class="container">
        <h2 class="section-title">获奖情况</h2>
        <div class="awards-content">
          <div class="awards-stats">
            <div class="award-stat-card">
              <div class="award-icon">🥇</div>
              <div class="award-info">
                <div class="award-number">18</div>
                <div class="award-title">一等奖</div>
                <div class="award-rate">1.43%</div>
              </div>
            </div>
            <div class="award-stat-card">
              <div class="award-icon">🥈</div>
              <div class="award-info">
                <div class="award-number">36</div>
                <div class="award-title">二等奖</div>
                <div class="award-rate">2.87%</div>
              </div>
            </div>
            <div class="award-stat-card">
              <div class="award-icon">🥉</div>
              <div class="award-info">
                <div class="award-number">72</div>
                <div class="award-title">三等奖</div>
                <div class="award-rate">5.73%</div>
              </div>
            </div>
            <div class="award-stat-card">
              <div class="award-icon">🎖️</div>
              <div class="award-info">
                <div class="award-number">200</div>
                <div class="award-title">成功参赛奖</div>
                <div class="award-rate">15.92%</div>
              </div>
            </div>
          </div>
          
          <div class="awards-ranking">
            <h3>高校获奖排名</h3>
            <div class="ranking-table">
              <table>
                <thead>
                  <tr>
                    <th>排名</th>
                    <th>学校名称</th>
                    <th>一等奖</th>
                    <th>二等奖</th>
                    <th>三等奖</th>
                    <th>总计</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>哈尔滨工业大学</td>
                    <td>3</td>
                    <td>5</td>
                    <td>8</td>
                    <td>16</td>
                  </tr>
                  <tr>
                    <td>2</td>
                    <td>哈尔滨工程大学</td>
                    <td>2</td>
                    <td>4</td>
                    <td>7</td>
                    <td>13</td>
                  </tr>
                  <tr>
                    <td>3</td>
                    <td>哈尔滨理工大学</td>
                    <td>2</td>
                    <td>3</td>
                    <td>6</td>
                    <td>11</td>
                  </tr>
                  <tr>
                    <td>4</td>
                    <td>黑龙江大学</td>
                    <td>1</td>
                    <td>3</td>
                    <td>5</td>
                    <td>9</td>
                  </tr>
                  <tr>
                    <td>5</td>
                    <td>东北林业大学</td>
                    <td>1</td>
                    <td>2</td>
                    <td>4</td>
                    <td>7</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 竞赛题目 -->
    <section class="problems-section">
      <div class="container">
        <h2 class="section-title">竞赛题目</h2>
        <div class="problems-grid">
          <div class="problem-card">
            <div class="problem-header">
              <span class="problem-type">A题</span>
              <span class="problem-difficulty">中等难度</span>
            </div>
            <h3 class="problem-title">城市交通拥堵问题建模与优化</h3>
            <p class="problem-description">针对某城市的交通拥堵问题，建立数学模型，分析拥堵原因，并提出优化方案。</p>
            <div class="problem-keywords">
              <span class="keyword">交通流</span>
              <span class="keyword">优化算法</span>
              <span class="keyword">大数据分析</span>
            </div>
          </div>
          <div class="problem-card">
            <div class="problem-header">
              <span class="problem-type">B题</span>
              <span class="problem-difficulty">较难</span>
            </div>
            <h3 class="problem-title">环境污染物扩散模型</h3>
            <p class="problem-description">研究某地区环境污染物的扩散规律，建立数学模型，预测污染物浓度分布，并提出控制策略。</p>
            <div class="problem-keywords">
              <span class="keyword">扩散方程</span>
              <span class="keyword">数值模拟</span>
              <span class="keyword">环保</span>
            </div>
          </div>
          <div class="problem-card">
            <div class="problem-header">
              <span class="problem-type">C题</span>
              <span class="problem-difficulty">中等难度</span>
            </div>
            <h3 class="problem-title">互联网+时代的商业模式创新</h3>
            <p class="problem-description">分析互联网+时代的商业模式特点，建立数学模型，评估不同商业模式的竞争力。</p>
            <div class="problem-keywords">
              <span class="keyword">商业模式</span>
              <span class="keyword">博弈论</span>
              <span class="keyword">经济模型</span>
            </div>
          </div>
          <div class="problem-card">
            <div class="problem-header">
              <span class="problem-type">D题</span>
              <span class="problem-difficulty">较易</span>
            </div>
            <h3 class="problem-title">医疗资源优化配置</h3>
            <p class="problem-description">针对某地区的医疗资源分布情况，建立数学模型，优化医疗资源配置，提高医疗服务效率。</p>
            <div class="problem-keywords">
              <span class="keyword">资源优化</span>
              <span class="keyword">排队论</span>
              <span class="keyword">医疗</span>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 精彩瞬间 -->
    <section class="gallery-section">
      <div class="container">
        <h2 class="section-title">精彩瞬间</h2>
        <div class="gallery-grid">
          <div class="gallery-item">
            <div class="gallery-placeholder">📸</div>
            <div class="gallery-caption">开幕式现场</div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">📝</div>
            <div class="gallery-caption">参赛选手认真答题</div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">💻</div>
            <div class="gallery-caption">选手们在讨论解决方案</div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">🏆</div>
            <div class="gallery-caption">颁奖典礼</div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">🤝</div>
            <div class="gallery-caption">获奖团队合影</div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">📊</div>
            <div class="gallery-caption">专家评审现场</div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- 竞赛成果 -->
    <section class="achievements-section">
      <div class="container">
        <div class="achievements-card">
          <h2 class="section-title">竞赛成果</h2>
          <div class="achievements-content">
            <div class="achievement-item">
              <div class="achievement-icon">📈</div>
              <div class="achievement-text">
                <h3>参赛规模持续增长</h3>
                <p>自2020年以来，参赛队伍数量年均增长率达15%，覆盖高校数量从87所增加到156所</p>
              </div>
            </div>
            <div class="achievement-item">
              <div class="achievement-icon">🎓</div>
              <div class="achievement-text">
                <h3>人才培养效果显著</h3>
                <p>累计培养了超过10000名具有创新能力和团队协作精神的优秀学生</p>
              </div>
            </div>
            <div class="achievement-item">
              <div class="achievement-icon">🔬</div>
              <div class="achievement-text">
                <h3>科研成果丰硕</h3>
                <p>基于竞赛题目，累计发表学术论文120余篇，申请专利30余项</p>
              </div>
            </div>
            <div class="achievement-item">
              <div class="achievement-icon">🤝</div>
              <div class="achievement-text">
                <h3>社会影响广泛</h3>
                <p>与30余家企业建立了合作关系，推动了产学研深度融合</p>
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
.past-reviews-page {
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

/* 年份选择 */
.year-select-section {
  padding: 40px 0;
  background: white;
}

.year-selector {
  text-align: center;
}

.section-title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #1e293b;
  text-align: center;
}

.year-buttons {
  display: flex;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
}

.year-btn {
  padding: 12px 24px;
  border: 1px solid #e2e8f0;
  background: white;
  color: #475569;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 16px;
  font-weight: 500;
}

.year-btn:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.year-btn.active {
  background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: #667eea;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* 竞赛概览 */
.overview-section {
  padding: 60px 0;
  background: #f8fafc;
}

.overview-card {
  background: white;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.overview-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 32px;
  align-items: start;
}

.overview-text {
  line-height: 1.8;
  color: #475569;
}

.overview-text p {
  margin-bottom: 16px;
}

.overview-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.stat-item {
  background: #f8fafc;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.stat-number {
  font-size: 28px;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 14px;
  color: #475569;
  font-weight: 500;
}

/* 获奖情况 */
.awards-section {
  padding: 60px 0;
  background: white;
}

.awards-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.awards-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.award-stat-card {
  background: #f8fafc;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  display: flex;
  align-items: center;
  gap: 16px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.award-stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.award-icon {
  font-size: 40px;
  flex-shrink: 0;
}

.award-info {
  flex: 1;
}

.award-number {
  font-size: 24px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 4px;
}

.award-title {
  font-size: 16px;
  font-weight: 600;
  color: #334155;
  margin-bottom: 4px;
}

.award-rate {
  font-size: 14px;
  color: #64748b;
}

/* 高校排名 */
.awards-ranking {
  background: #f8fafc;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.awards-ranking h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #1e293b;
  text-align: center;
}

.ranking-table {
  overflow-x: auto;
}

.ranking-table table {
  width: 100%;
  border-collapse: collapse;
  min-width: 500px;
}

.ranking-table th,
.ranking-table td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

.ranking-table th {
  background: #e2e8f0;
  font-weight: 600;
  color: #334155;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.ranking-table td {
  color: #475569;
  font-size: 14px;
}

.ranking-table tbody tr:hover {
  background: #ffffff;
}

/* 竞赛题目 */
.problems-section {
  padding: 60px 0;
  background: #f8fafc;
}

.problems-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.problem-card {
  background: white;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.problem-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.problem-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.problem-type {
  background: #667eea;
  color: white;
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 14px;
  font-weight: 600;
}

.problem-difficulty {
  background: #fef3c7;
  color: #92400e;
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 14px;
  font-weight: 500;
}

.problem-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1e293b;
}

.problem-description {
  line-height: 1.6;
  color: #475569;
  margin-bottom: 16px;
}

.problem-keywords {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.keyword {
  background: #e0f2fe;
  color: #0369a1;
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
}

/* 精彩瞬间 */
.gallery-section {
  padding: 60px 0;
  background: white;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.gallery-item {
  background: #f8fafc;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
}

.gallery-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.gallery-placeholder {
  height: 200px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 48px;
  color: white;
}

.gallery-caption {
  padding: 16px;
  text-align: center;
  font-weight: 600;
  color: #334155;
  background: white;
}

/* 竞赛成果 */
.achievements-section {
  padding: 60px 0;
  background: #f8fafc;
}

.achievements-card {
  background: white;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.achievements-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.achievement-item {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 24px;
  background: #f8fafc;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.achievement-item:hover {
  transform: translateX(8px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.achievement-icon {
  font-size: 40px;
  flex-shrink: 0;
}

.achievement-text h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #1e293b;
}

.achievement-text p {
  line-height: 1.6;
  color: #475569;
  font-size: 14px;
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
  .overview-content {
    grid-template-columns: 1fr;
  }
  
  .overview-stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .awards-content {
    grid-template-columns: 1fr;
  }
  
  .awards-stats {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .page-title {
    font-size: 24px;
  }
  
  .overview-stats {
    grid-template-columns: 1fr;
  }
  
  .awards-stats {
    grid-template-columns: 1fr;
  }
  
  .problems-grid {
    grid-template-columns: 1fr;
  }
  
  .gallery-grid {
    grid-template-columns: 1fr;
  }
  
  .achievement-item {
    flex-direction: column;
    text-align: center;
  }
}
</style>