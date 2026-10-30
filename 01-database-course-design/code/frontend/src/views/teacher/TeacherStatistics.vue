<template>
  <div class="teacher-statistics">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>数据统计</h2>
        </div>
        <div class="stats-grid">
          <div class="content-card">
            <h3>指导队伍统计</h3>
            <div class="stat-cards">
              <div class="stat-card">
                <div class="stat-value">{{ stats.teamCount }}</div>
                <div class="stat-label">总指导队伍</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">{{ stats.confirmedTeams }}</div>
                <div class="stat-label">已确认指导</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">{{ stats.pendingTeams }}</div>
                <div class="stat-label">待确认指导</div>
              </div>
            </div>
          </div>

          <div class="content-card">
            <h3>评审统计</h3>
            <div class="stat-cards">
              <div class="stat-card">
                <div class="stat-value">{{ stats.totalReviews }}</div>
                <div class="stat-label">总评审作品</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">{{ stats.completedReviews }}</div>
                <div class="stat-label">已完成评审</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">{{ stats.pendingReviews }}</div>
                <div class="stat-label">待评审作品</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">{{ stats.averageScore.toFixed(1) }}</div>
                <div class="stat-label">平均得分</div>
              </div>
            </div>
          </div>
        </div>

        <div class="charts-grid">
          <div class="content-card">
            <h3>得分分布</h3>
            <div class="chart-container">
              <v-chart :option="scoreDistributionOption" autoresize />
            </div>
          </div>

          <div class="content-card">
            <h3>评审进度</h3>
            <div class="chart-container">
              <v-chart :option="reviewProgressOption" autoresize />
            </div>
          </div>
        </div>

        <!-- 第二组统计数据 -->
        <div class="stats-grid">
          <div class="content-card">
            <h3>竞赛综合指标分析</h3>
            <div class="stat-cards">
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">参与高校数</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">参赛队伍数</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">获奖率</div>
              </div>
            </div>
          </div>

          <div class="content-card">
            <h3>历年参赛人数趋势</h3>
            <div class="stat-cards">
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">2021年</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">2022年</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">2023年</div>
              </div>
              <div class="stat-card">
                <div class="stat-value">0</div>
                <div class="stat-label">2024年</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 第二组图表 -->
        <div class="charts-grid">
          <div class="content-card">
            <h3>竞赛综合指标对比</h3>
            <div class="chart-container">
              <v-chart autoresize />
            </div>
          </div>

          <div class="content-card">
            <h3>历年参赛人数趋势</h3>
            <div class="chart-container">
              <v-chart autoresize />
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart, PieChart } from 'echarts/charts';
import { GridComponent, TooltipComponent, LegendComponent } from 'echarts/components';
import VChart from 'vue-echarts';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { request } from '../../api';
import { showError } from '../../utils/notification.js';

// 注册 ECharts 组件
use([
  CanvasRenderer,
  BarChart,
  PieChart,
  GridComponent,
  TooltipComponent,
  LegendComponent
]);

const stats = ref({
  teamCount: 0,
  confirmedTeams: 0,
  pendingTeams: 0,
  totalReviews: 0,
  completedReviews: 0,
  pendingReviews: 0,
  averageScore: 0,
  scoreDistribution: [0, 0, 0, 0, 0]
});

const fetchStatistics = async () => {
  try {
    const response = await request.get('/statistics/teacher');
    stats.value = response || {
      teamCount: 0,
      confirmedTeams: 0,
      pendingTeams: 0,
      totalReviews: 0,
      completedReviews: 0,
      pendingReviews: 0,
      averageScore: 0
    };
  } catch (error) {
    showError('获取统计数据失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 得分分布图表配置
const scoreDistributionOption = computed(() => {
  return {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      },
      formatter: '{b}: {c} 件作品'
    },
    legend: {
      bottom: '0%',
      left: 'center'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: ['0-19', '20-39', '40-59', '60-79', '80-100'],
      axisLabel: {
        color: '#4a5568',
        fontSize: 12
      },
      axisLine: {
        lineStyle: {
          color: '#e2e8f0'
        }
      },
      axisTick: {
        show: true,
        lineStyle: {
          color: '#e2e8f0'
        }
      },
      splitLine: {
        show: true,
        lineStyle: {
          color: '#f7fafc',
          type: 'dashed'
        }
      }
    },
    yAxis: {
      type: 'value',
      axisLabel: {
        color: '#4a5568',
        fontSize: 12
      },
      axisLine: {
        lineStyle: {
          color: '#e2e8f0'
        }
      },
      axisTick: {
        show: true,
        lineStyle: {
          color: '#e2e8f0'
        }
      },
      splitLine: {
        show: true,
        lineStyle: {
          color: '#f7fafc',
          type: 'dashed'
        }
      }
    },
    series: [
      {
        name: '作品数量',
        type: 'bar',
        data: stats.value.scoreDistribution,
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
        },
        barWidth: '60%'
      }
    ]
  };
});

// 评审进度图表配置
const reviewProgressOption = computed(() => {
  return {
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c} 件 ({d}%)'
    },
    legend: {
      bottom: '0%',
      left: 'center',
      orient: 'horizontal',
      textStyle: {
        color: '#4a5568',
        fontSize: 12
      }
    },
    series: [
      {
        name: '评审进度',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '20',
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [
          {
            value: stats.value.completedReviews,
            name: '已完成评审',
            itemStyle: {
              color: '#667eea'
            }
          },
          {
            value: stats.value.pendingReviews,
            name: '待评审',
            itemStyle: {
              color: '#48bb78'
            }
          }
        ],
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        },
        center: ['50%', '45%'],
        backgroundColor: '#fff'
      },
      {
        type: 'pie',
        radius: ['0%', '30%'],
        center: ['50%', '45%'],
        label: {
          show: true,
          formatter: '{b}\n{c}',
          fontSize: 16,
          fontWeight: 'bold',
          color: '#4a5568'
        },
        data: [{
          value: 1,
          name: '总评审',
          itemStyle: {
            color: 'transparent'
          },
          labelLine: {
            show: false
          }
        }]
      }
    ]
  };
});

onMounted(() => {
  fetchStatistics();
});
</script>

<style scoped>
.teacher-statistics {
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

.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 20px;
}

.charts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.content-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.content-card h3 {
  font-size: 18px;
  color: #2d3748;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid #e2e8f0;
}

.stat-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.stat-card {
  flex: 1;
  min-width: 120px;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  color: white;
  text-align: center;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 14px;
  opacity: 0.9;
}

.chart-container {
  height: 300px;
  width: 100%;
}
</style>

