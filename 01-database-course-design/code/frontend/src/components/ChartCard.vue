<template>
  <div class="chart-card">
    <h3 class="chart-title">{{ title }}</h3>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import * as echarts from 'echarts';

const props = defineProps({
  title: { type: String, required: true },
  chartData: { type: Object, required: true } // { type: 'bar'|'pie', data: [{name, value}] }
});

const chartRef = ref(null);
let chartInstance = null;

const renderChart = () => {
  if (!chartRef.value) return;
  chartInstance = echarts.init(chartRef.value);
  const { type, data } = props.chartData || { type: 'bar', data: [] };

  let option = {};
  if (type === 'bar') {
    option = {
      xAxis: { type: 'category', data: data.map(d => d.name) },
      yAxis: { type: 'value' },
      series: [{ data: data.map(d => d.value), type: 'bar', itemStyle: { color: '#4f91ff' } }],
      tooltip: { trigger: 'axis' }
    };
  } else if (type === 'pie') {
    option = {
      series: [{
        type: 'pie',
        radius: '60%',
        data: data,
        emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0,0,0,0.5)' } } 
      }],
      tooltip: { trigger: 'item' },
      legend: { bottom: '0%', left: 'center' }
    };
  }

  chartInstance.setOption(option);
};

onMounted(() => renderChart());

watch(() => props.chartData, () => {
  if (chartInstance) chartInstance.dispose();
  renderChart();
});
</script>

<style scoped>
.chart-card {
  flex: 1;
  min-width: 300px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.chart-title {
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
}

.chart-container {
  width: 100%;
  height: 300px;
}
</style>
