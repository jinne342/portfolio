<template>
  <div class="admin-user">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>用户管理</h2>
        </div>
        
        <!-- 搜索和操作区域 -->
        <div class="content-card">
          <div class="search-operations">
            <el-input
              v-model="searchQuery"
              placeholder="搜索用户名或邮箱"
              clearable
              style="width: 300px; margin-right: 10px;"
            />
            <el-button type="primary" @click="handleSearch">搜索</el-button>
            <el-button type="default" @click="handleReset">重置</el-button>
          </div>
        </div>
        
        <!-- 用户列表 -->
        <div class="content-card">
          <el-table
            :data="users"
            style="width: 100%"
            stripe
            v-loading="loading"
          >
            <el-table-column prop="user_id" label="用户ID" width="80" />
            <el-table-column prop="user_name" label="用户名" width="150" />
            <el-table-column prop="email" label="邮箱" width="250" />
            <el-table-column prop="phone" label="手机号" width="150" />
            <el-table-column prop="school_id" label="学校ID" width="100" />
            <el-table-column prop="college_id" label="学院ID" width="100" />
            <el-table-column prop="major_id" label="专业ID" width="100" />
            <el-table-column prop="user_type" label="用户类型" width="120">
              <template #default="scope">
                {{ getUserTypeText(scope.row.user_type) }}
              </template>
            </el-table-column>
            <el-table-column prop="status" label="状态" width="100">
              <template #default="scope">
                <el-tag :type="scope.row.status === 1 ? 'success' : 'warning'">
                  {{ scope.row.status === 1 ? '已激活' : '待审核' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column label="操作" width="280" fixed="right">
              <template #default="scope">
                <el-button size="small" type="primary" @click="handleEdit(scope.row)">编辑</el-button>
                <el-button size="small" type="success" v-if="scope.row.status === 0" @click="handleAudit(scope.row, 1)">审核通过</el-button>
                <el-button size="small" type="danger" v-if="scope.row.status === 0" @click="handleAudit(scope.row, 0)">审核不通过</el-button>
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
          title="编辑用户"
          width="500px"
        >
          <el-form :model="editForm" label-width="80px">
            <el-form-item label="用户名">
              <el-input v-model="editForm.user_name" />
            </el-form-item>
            <el-form-item label="邮箱">
              <el-input v-model="editForm.email" />
            </el-form-item>
            <el-form-item label="手机号">
              <el-input v-model="editForm.phone" />
            </el-form-item>
            <el-form-item label="年级">
              <el-input v-model="editForm.grade" placeholder="如：2023" />
            </el-form-item>
            <el-form-item label="用户类型">
              <el-select v-model="editForm.user_type" placeholder="请选择用户类型">
                <el-option label="超级管理员" value="0" />
                <el-option label="学生" value="1" />
                <el-option label="竞赛管理员" value="2" />
                <el-option label="教师" value="3" />
              </el-select>
            </el-form-item>
            <el-form-item label="状态">
              <el-select v-model="editForm.status" placeholder="请选择状态">
                <el-option label="待审核" value="0" />
                <el-option label="已激活" value="1" />
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
import { getUsers, updateUser, deleteUser } from '../../api/user';

// 状态管理
const users = ref([]);
const loading = ref(false);
const searchQuery = ref('');
const currentPage = ref(1);
const pageSize = ref(10);
const total = ref(0);
const editDialogVisible = ref(false);
const editForm = ref({
  user_id: '',
  user_name: '',
  email: '',
  phone: '',
  grade: '',
  user_type: 1,
  status: 1
});

// 获取用户列表
const fetchUsers = async () => {
  loading.value = true;
  try {
    const response = await getUsers();
    // 过滤搜索结果
    let filteredUsers = response;
    if (searchQuery.value) {
      const query = searchQuery.value.toLowerCase();
      filteredUsers = filteredUsers.filter(user => 
        (user.user_name && user.user_name.toLowerCase().includes(query)) ||
        (user.email && user.email.toLowerCase().includes(query))
      );
    }
    users.value = filteredUsers;
    total.value = filteredUsers.length;
  } catch (error) {
    showError('获取用户列表失败：' + (error.response?.data?.message || error.message || error));
  } finally {
    loading.value = false;
  }
};

// 搜索
const handleSearch = () => {
  fetchUsers();
};

// 重置搜索
const handleReset = () => {
  searchQuery.value = '';
  fetchUsers();
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

// 获取用户类型文本
const getUserTypeText = (userType) => {
  const typeMap = {
    0: '超级管理员',
    1: '学生',
    2: '竞赛管理员',
    3: '教师'
  };
  return typeMap[userType] || '未知类型';
};

// 处理审核
const handleAudit = async (row, status) => {
  try {
    await updateUser(row.user_id, { status });
    showSuccess(status === 1 ? '审核通过成功' : '审核不通过成功');
    fetchUsers(); // 重新获取数据
  } catch (error) {
    showError((status === 1 ? '审核通过' : '审核不通过') + '失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 编辑用户
const handleEdit = (row) => {
  editForm.value = {
    user_id: row.user_id,
    user_name: row.user_name,
    email: row.email,
    phone: row.phone,
    grade: row.grade,
    user_type: row.user_type,
    status: row.status
  };
  editDialogVisible.value = true;
};

// 保存编辑
const handleSaveEdit = async () => {
  try {
    await updateUser(editForm.value.user_id, editForm.value);
    showSuccess('更新用户成功');
    editDialogVisible.value = false;
    fetchUsers(); // 重新获取数据
  } catch (error) {
    showError('更新用户失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 删除用户
const handleDelete = async (row) => {
  try {
    await showConfirm('删除确认', '确定要删除这个用户吗？', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    });
    
    await deleteUser(row.user_id);
    showSuccess('删除用户成功');
    fetchUsers(); // 重新获取数据
  } catch (error) {
    if (error === 'cancel') {
      return; // 用户取消删除
    }
    showError('删除用户失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 初始化数据
onMounted(() => {
  fetchUsers();
});
</script>

<style scoped>
.admin-user {
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

