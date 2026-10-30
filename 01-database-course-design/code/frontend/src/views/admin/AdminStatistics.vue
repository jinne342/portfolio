<template>
  <div class="admin-statistics">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>数据统计</h2>
        </div>
        
        <!-- 统计卡片区域 -->
        <div class="content-card">
          <div class="statistics-cards">
            <el-card shadow="hover" class="stat-card">
              <template #header>
                <div class="card-header">
                  <span>总队伍数量</span>
                </div>
              </template>
              <div class="stat-value">
                {{ totalTeams || 0 }}
              </div>
              <div class="stat-desc">当前系统中的总队伍数量</div>
            </el-card>
          </div>
        </div>
        
        <!-- 左右布局区域 -->
        <div class="data-layout">
          <!-- 左侧：表格数据 -->
          <div class="data-left">
            <!-- 各学院队伍数量柱状图 -->
            <div class="content-card">
              <div class="chart-header">
                <h3>各学院队伍数量</h3>
              </div>
              <div class="chart-container">
                <el-empty v-if="!teamByCollege.length" description="暂无数据" />
                <div v-else>
                  <el-table :data="teamByCollege" style="width: 100%">
                    <el-table-column prop="college" label="学院" />
                    <el-table-column prop="count" label="队伍数量" />
                  </el-table>
                </div>
              </div>
            </div>

            <!-- 各题目被选择次数 -->
            <div class="content-card">
              <div class="chart-header">
                <h3>各题目被选择次数</h3>
              </div>
              <div class="chart-container">
                <el-empty v-if="!problemSelection.length" description="暂无数据" />
                <div v-else>
                  <el-table :data="problemSelection" style="width: 100%">
                    <el-table-column prop="problem" label="题目" />
                    <el-table-column prop="count" label="选择次数" />
                  </el-table>
                </div>
              </div>
            </div>
          </div>
          
          <!-- 右侧：图表展示 -->
          <div class="data-right">
            <!-- 各学院队伍数量图表 -->
            <div v-if="teamByCollege.length > 0" class="content-card">
              <div class="chart-header">
                <h3>各学院队伍数量分布</h3>
              </div>
              <div class="chart-container">
                <v-chart :option="teamByCollegeChart" autoresize />
              </div>
            </div>
            
            <!-- 各题目被选择次数图表 -->
            <div v-if="problemSelection.length > 0" class="content-card">
              <div class="chart-header">
                <h3>各题目被选择次数分布</h3>
              </div>
              <div class="chart-container">
                <v-chart :option="problemSelectionChart" autoresize />
              </div>
            </div>
            
            <!-- 学院队伍数量饼图 -->
            <div v-if="teamByCollege.length > 0" class="content-card">
              <div class="chart-header">
                <h3>学院队伍数量占比</h3>
              </div>
              <div class="chart-container">
                <v-chart :option="teamByCollegePieChart" autoresize />
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { ElLoading } from 'element-plus';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart, PieChart } from 'echarts/charts';
import { GridComponent, TooltipComponent, LegendComponent } from 'echarts/components';
import VChart from 'vue-echarts';
import { showError } from '../../utils/notification.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getTeamCount, getTeamCountByCollege, getProblemSelectionCount } from '../../api/statistics';

// 注册 ECharts 组件
use([
  CanvasRenderer,
  BarChart,
  PieChart,
  GridComponent,
  TooltipComponent,
  LegendComponent
]);

// 统计数据状态
const totalTeams = ref(0);
const teamByCollege = ref([]);
const problemSelection = ref([]);
const loading = ref(false);

// 获取总队伍数量
const fetchTeamCount = async () => {
  try {
    const response = await getTeamCount();
    totalTeams.value = response.total_teams || 0;
  } catch (error) {
    showError('获取总队伍数量失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 获取各学院队伍数量
const fetchTeamByCollege = async () => {
  try {
    const response = await getTeamCountByCollege();
    teamByCollege.value = response || [];
  } catch (error) {
    showError('获取各学院队伍数量失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 获取各题目被选择次数
const fetchProblemSelection = async () => {
  try {
    const response = await getProblemSelectionCount();
    problemSelection.value = response || [];
  } catch (error) {
    showError('获取各题目被选择次数失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 初始化数据
const initData = async () => {
  loading.value = true;
  try {
    // 并行请求所有统计数据
    await Promise.all([
      fetchTeamCount(),
      fetchTeamByCollege(),
      fetchProblemSelection()
    ]);
  } finally {
    loading.value = false;
  }
};

// 页面挂载时获取数据
onMounted(() => {
  initData();
});

// 各学院队伍数量柱状图配置
const teamByCollegeChart = computed(() => {
  const colleges = teamByCollege.value.map(item => item.college);
  const counts = teamByCollege.value.map(item => item.count);
  
  return {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      },
      formatter: '{b}: {c} 支队伍'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: colleges
    },
    yAxis: {
      type: 'value',
      name: '队伍数量'
    },
    series: [
      {
        name: '队伍数量',
        type: 'bar',
        data: counts,
        itemStyle: {
          color: {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
              { offset: 0, color: '#667eea' },
              { offset: 1, color: '#764ba2' }
            ]
          }
        },
        emphasis: {
          itemStyle: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [
                { offset: 0, color: '#5a67d8' },
                { offset: 1, color: '#6b46c1' }
              ]
            }
          }
        }
      }
    ]
  };
});

// 各题目被选择次数柱状图配置
const problemSelectionChart = computed(() => {
  const problems = problemSelection.value.map(item => item.problem);
  const counts = problemSelection.value.map(item => item.count);
  
  return {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      },
      formatter: '{b}: {c} 次选择'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: problems
    },
    yAxis: {
      type: 'value',
      name: '选择次数'
    },
    series: [
      {
        name: '选择次数',
        type: 'bar',
        data: counts,
        itemStyle: {
          color: {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
              { offset: 0, color: '#48bb78' },
              { offset: 1, color: '#38a169' }
            ]
          }
        },
        emphasis: {
          itemStyle: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [
                { offset: 0, color: '#38a169' },
                { offset: 1, color: '#2f855a' }
              ]
            }
          }
        }
      }
    ]
  };
});

// 各学院队伍数量饼图配置
const teamByCollegePieChart = computed(() => {
  const pieData = teamByCollege.value.map(item => ({
    name: item.college,
    value: item.count
  }));
  
  return {
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} 支队伍 ({d}%)'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        name: '学院队伍分布',
        type: 'pie',
        radius: '50%',
        data: pieData,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  };
});
</script>

<style scoped>
.admin-statistics {
  min-height: 100vh;
  background: #f5f7fa;
}

.main-layout {
  display: flex;
}

.main-content {
  flex: 1;
  padding: 30px;
}

.page-header h2 {
  font-size: 28px;
  color: #2d3748;
  margin-bottom: 20px;
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  margin-bottom: 20px;
}

/* 统计卡片样式 */
.statistics-cards {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.stat-card {
  min-width: 200px;
  flex: 1;
}

.card-header {
  font-size: 16px;
  font-weight: 500;
  color: #4a5568;
}

.stat-value {
  font-size: 32px;
  font-weight: 600;
  color: #2d3748;
  margin: 10px 0;
}

.stat-desc {
  font-size: 14px;
  color: #718096;
}

/* 图表区域样式 */
.chart-header {
  margin-bottom: 20px;
}

.chart-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #2d3748;
  margin: 0;
}

.chart-container {
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 左右布局样式 */
.data-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

/* 左侧表格区域 */
.data-left {
  display: flex;
  flex-direction: column;
}

/* 右侧图表区域 */
.data-right {
  display: flex;
  flex-direction: column;
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .data-layout {
    grid-template-columns: 1fr;
  }
}
</style>

