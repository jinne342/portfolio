<template>
  <div class="page-container">
    <div class="container">
      <h1 class="page-title">竞赛新闻</h1>
      <p class="page-subtitle">了解全国大学生数学建模竞赛的最新动态</p>
      <div class="news-list">
        <div class="news-item">
          <div class="news-meta">
            <span class="news-date">2025-04-10</span>
            <span class="news-tag">会议动态</span>
          </div>
          <h2 class="news-title">全国大学生数学建模竞赛培训工作研讨会在京召开</h2>
          <p class="news-excerpt">为进一步提高全国大学生数学建模竞赛的培训质量，推动数学建模教育改革，全国大学生数学建模竞赛培训工作研讨会于4月10日在北京召开。</p>
          <a href="#" class="news-link">阅读全文</a>
        </div>
        <div class="news-item">
          <div class="news-meta">
            <span class="news-date">2025-03-05</span>
            <span class="news-tag">赛事通知</span>
          </div>
          <h2 class="news-title">2025年全国大学生数学建模竞赛命题工作启动</h2>
          <p class="news-excerpt">2025年全国大学生数学建模竞赛命题工作正式启动，命题专家委员会已开始征集和筛选竞赛题目。</p>
          <a href="#" class="news-link">阅读全文</a>
        </div>
        <div class="news-item">
          <div class="news-meta">
            <span class="news-date">2025-02-28</span>
            <span class="news-tag">出版动态</span>
          </div>
          <h2 class="news-title">全国大学生数学建模竞赛优秀论文集出版发行</h2>
          <p class="news-excerpt">《2024年全国大学生数学建模竞赛优秀论文集》已由高等教育出版社出版发行，收录了2024年竞赛中的优秀论文100篇。</p>
          <a href="#" class="news-link">阅读全文</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 竞赛新闻页面壳子，后续将补充具体内容
</script>

<style scoped>
.page-container {
  min-height: 70vh;
  padding: 40px 0;
  background: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.page-title {
  text-align: center;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 12px;
  color: #1e293b;
}

.page-subtitle {
  text-align: center;
  font-size: 16px;
  color: #64748b;
  margin-bottom: 40px;
}

.news-list {
  display: grid;
  gap: 24px;
}

.news-item {
  background: #f8fafc;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}

.news-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.news-meta {
  display: flex;
  gap: 16px;
  margin-bottom: 12px;
  font-size: 14px;
  color: #64748b;
}

.news-date {
  font-weight: 500;
}

.news-tag {
  background: #3b82f6;
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
}

.news-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1e293b;
}

.news-excerpt {
  color: #475569;
  line-height: 1.6;
  margin-bottom: 16px;
}

.news-link {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.news-link:hover {
  color: #2563eb;
  text-decoration: underline;
}
</style>