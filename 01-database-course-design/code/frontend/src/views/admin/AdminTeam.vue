<template>
  <div class="admin-team">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>队伍管理</h2>
        </div>
        
        <!-- 搜索和操作区域 -->
        <div class="content-card">
          <div class="search-operations">
            <el-input
              v-model="searchQuery"
              placeholder="搜索队伍名称"
              clearable
              style="width: 300px; margin-right: 10px;"
            />
            <el-button type="primary" @click="handleSearch">搜索</el-button>
            <el-button type="default" @click="handleReset">重置</el-button>
          </div>
        </div>
        
        <!-- 队伍列表 -->
        <div class="content-card">
          <el-table
            :data="teams"
            style="width: 100%"
            stripe
            v-loading="loading"
          >
            <el-table-column prop="team_id" label="队伍ID" width="80" />
            <el-table-column prop="team_name" label="队伍名称" width="180" />
            <el-table-column prop="competition_id" label="竞赛ID" width="100" />
            <el-table-column prop="school_id" label="学校ID" width="100" />
            <el-table-column prop="captain_id" label="队长ID" width="100" />
            <el-table-column prop="status" label="状态" width="120">
              <template #default="scope">
                <el-tag :type="scope.row.status === 'active' ? 'success' : 'warning'">
                  {{ scope.row.status === 'active' ? '活跃' : '停用' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="create_time" label="创建时间" width="200" />
            <el-table-column label="操作" width="200" fixed="right">
              <template #default="scope">
                <el-button size="small" type="primary" @click="handleEdit(scope.row)">编辑</el-button>
                <el-button size="small" type="danger" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          
          <!-- 分页 -->
          <div class="pagination">
            <el-pagination
              v-model:current-page="currentPage"
              v-model:page-size="pageSize"
              :page-sizes="[10, 20, 50, 100]"
              layout="total, sizes, prev, pager, next, jumper"
              :total="total"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
            />
          </div>
        </div>
        
        <!-- 编辑对话框 -->
        <el-dialog
          v-model="editDialogVisible"
          title="编辑队伍"
          width="500px"
        >
          <el-form :model="editForm" label-width="80px">
            <el-form-item label="队伍名称">
              <el-input v-model="editForm.team_name" />
            </el-form-item>
            <el-form-item label="状态">
              <el-select v-model="editForm.status">
                <el-option label="活跃" value="active" />
                <el-option label="停用" value="inactive" />
              </el-select>
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="editDialogVisible = false">取消</el-button>
              <el-button type="primary" @click="handleSaveEdit">保存</el-button>
            </span>
          </template>
        </el-dialog>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { showError, showSuccess, showConfirm } from '../../utils/notification.js';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getTeams, updateTeam, deleteTeam } from '../../api/team';

// 状态管理
const teams = ref([]);
const loading = ref(false);
const searchQuery = ref('');
const currentPage = ref(1);
const pageSize = ref(10);
const total = ref(0);
const editDialogVisible = ref(false);
const editForm = ref({
  team_id: '',
  team_name: '',
  status: 'active'
});

// 获取队伍列表
const fetchTeams = async () => {
  loading.value = true;
  try {
    const response = await getTeams();
    // 状态码映射：0→'inactive'，1→'active'
    const mappedTeams = response.map(team => ({
      ...team,
      status: team.status === 1 ? 'active' : 'inactive'
    }));
    // 过滤搜索结果
    let filteredTeams = mappedTeams;
    if (searchQuery.value) {
      filteredTeams = filteredTeams.filter(team => 
        team.team_name && team.team_name.includes(searchQuery.value)
      );
    }
    teams.value = filteredTeams;
    total.value = filteredTeams.length;
  } catch (error) {
    showError('获取队伍列表失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    loading.value = false;
  }
};

// 搜索
const handleSearch = () => {
  fetchTeams();
};

// 重置搜索
const handleReset = () => {
  searchQuery.value = '';
  fetchTeams();
};

// 分页大小变化
const handleSizeChange = (size) => {
  pageSize.value = size;
  currentPage.value = 1;
};

// 当前页变化
const handleCurrentChange = (current) => {
  currentPage.value = current;
};

// 编辑队伍
const handleEdit = (row) => {
  editForm.value = {
    team_id: row.team_id,
    team_name: row.team_name,
    status: row.status
  };
  editDialogVisible.value = true;
};

// 保存编辑
const handleSaveEdit = async () => {
  try {
    await updateTeam(editForm.value.team_id, editForm.value);
    showSuccess('更新队伍成功');
    editDialogVisible.value = false;
    fetchTeams(); // 重新获取数据
  } catch (error) {
    showError('更新队伍失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 删除队伍
const handleDelete = async (row) => {
  try {
    await showConfirm('删除确认', '确定要删除这个队伍吗？', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    });
    
    await deleteTeam(row.team_id);
    showSuccess('删除队伍成功');
    fetchTeams(); // 重新获取数据
  } catch (error) {
    if (error === 'cancel') {
      return; // 用户取消删除
    }
    showError('删除队伍失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 初始化数据
onMounted(() => {
  fetchTeams();
});
</script>

<style scoped>
.admin-team {
  min-height: 100vh;
  background: #f1f5f9;
}

.main-layout {
  display: flex;
}

.main-content {
  flex: 1;
  padding: 30px;
  min-height: calc(100vh - 70px);
}

.page-header {
  margin-bottom: 20px;
}

.page-header h2 {
  font-size: 24px;
  color: #1e293b;
  margin-bottom: 8px;
  font-weight: 600;
}

.content-card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin-bottom: 20px;
}

.search-operations {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>

