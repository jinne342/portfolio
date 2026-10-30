<template>
  <div class="table-export">
    <button class="export-btn" @click="exportExcel">导出 Excel</button>
    <table>
      <thead>
        <tr>
          <th v-for="col in columns" :key="col.key">{{ col.label }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in rows" :key="index">
          <td v-for="col in columns" :key="col.key">{{ row[col.key] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import * as XLSX from 'xlsx';

const props = defineProps({
  columns: { type: Array, required: true },  // [{key, label}]
  rows: { type: Array, required: true },     // 数据
  exportFileName: { type: String, default: '导出数据.xlsx' },
  apiUrl: { type: String, default: '' }      // 可选：从 API 拉取数据
});

const exportExcel = () => {
  const ws = XLSX.utils.json_to_sheet(props.rows);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
  XLSX.writeFile(wb, props.exportFileName);
};
</script>

<style scoped>
.table-export {
  background: rgba(255,255,255,0.95);
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin-top: 16px;
}

.export-btn {
  padding: 6px 12px;
  background: #4f91ff;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 12px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
}
</style>
