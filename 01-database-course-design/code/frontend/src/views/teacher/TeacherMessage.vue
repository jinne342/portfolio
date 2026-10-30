<template>
  <div class="teacher-message">
    <Header />
    <div class="main-layout">
      <Sidebar />
      <main class="main-content">
        <div class="page-header">
          <h2>消息中心</h2>
        </div>
        <div class="content-card">
          <div class="message-actions">
            <el-button type="primary" @click="refreshMessages">刷新消息</el-button>
            <el-button @click="markAllAsRead">全部已读</el-button>
            <el-button type="success" @click="openSendDialog">发送消息</el-button>
          </div>
          
          <el-table
            :data="messages"
            style="width: 100%"
            stripe
            @row-click="handleRowClick"
          >
            <el-table-column
              prop="message_id"
              label="消息ID"
              width="100"
            />
            <el-table-column
              prop="sender_id"
              label="发送者ID"
              width="120"
            />
            <el-table-column
              prop="content"
              label="消息内容"
              :show-overflow-tooltip="true"
            >
              <template #default="scope">
                <span :class="{ 'unread-message': scope.row.status === 'unread' }">
                  {{ scope.row.content }}
                </span>
              </template>
            </el-table-column>
            <el-table-column
              prop="status"
              label="状态"
              width="100"
            >
              <template #default="scope">
                <el-tag :type="scope.row.status === 'read' ? 'success' : 'info'">
                  {{ scope.row.status === 'read' ? '已读' : '未读' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column
              prop="send_time"
              label="发送时间"
              width="180"
              :formatter="formatDateTime"
            />
            <el-table-column
              label="操作"
              width="150"
              fixed="right"
            >
              <template #default="scope">
                <el-button type="primary" size="small" @click="viewMessage(scope.row)">
                  查看
                </el-button>
                <el-button type="danger" size="small" @click="deleteMessage(scope.row.message_id)">
                  删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          
          <!-- 消息详情对话框 -->
          <el-dialog
            v-model="dialogVisible"
            title="消息详情"
            width="50%"
          >
            <div v-if="currentMessage" class="message-detail">
              <el-descriptions :column="1">
                <el-descriptions-item label="消息ID">{{ currentMessage.message_id }}</el-descriptions-item>
                <el-descriptions-item label="发送者ID">{{ currentMessage.sender_id }}</el-descriptions-item>
                <el-descriptions-item label="接收者ID">{{ currentMessage.receiver_id }}</el-descriptions-item>
                <el-descriptions-item label="消息内容">{{ currentMessage.content }}</el-descriptions-item>
                <el-descriptions-item label="状态">{{ currentMessage.status === 'read' ? '已读' : '未读' }}</el-descriptions-item>
                <el-descriptions-item label="发送时间">{{ formatDateTime(currentMessage.send_time) }}</el-descriptions-item>
              </el-descriptions>
            </div>
            <template #footer>
              <div class="dialog-footer">
                <el-button @click="dialogVisible = false">关闭</el-button>
                <el-button type="primary" @click="markAsRead">标记为已读</el-button>
              </div>
            </template>
          </el-dialog>
          
          <!-- 发送消息对话框 -->
          <el-dialog
            v-model="sendDialogVisible"
            title="发送消息"
            width="50%"
            @close="closeSendDialog"
          >
            <el-form :model="{ receiverId, messageContent }" label-width="80px">
              <el-form-item label="接收者ID" required>
                <el-input v-model="receiverId" placeholder="请输入接收者的用户ID" />
              </el-form-item>
              
              <el-form-item label="消息内容" required>
                <el-input
                  v-model="messageContent"
                  type="textarea"
                  :rows="4"
                  placeholder="请输入消息内容（最多200字）"
                  maxlength="200"
                  show-word-limit
                  @input="updateContentLength"
                />
                <div class="content-length" v-if="contentLength > 0">
                  {{ contentLength }} / {{ maxContentLength }} 字
                </div>
              </el-form-item>
            </el-form>
            
            <template #footer>
              <div class="dialog-footer">
                <el-button @click="closeSendDialog">取消</el-button>
                <el-button type="primary" @click="submitSendMessage">发送</el-button>
              </div>
            </template>
          </el-dialog>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Header from '../../components/Header.vue';
import Sidebar from '../../components/Sidebar.vue';
import { getUserMessages, updateMessageStatus, deleteMessage as deleteMessageAPI, sendMessage } from '../../api/message.js';
import { showError, showSuccess, showInfo } from '../../utils/notification.js';
import { formatDateTime } from '../../utils/date.js';

// 数据
const messages = ref([]);
const dialogVisible = ref(false);
const currentMessage = ref(null);

// 发送消息相关
const sendDialogVisible = ref(false);
const receiverId = ref('');
const messageContent = ref('');
const contentLength = ref(0);
const maxContentLength = 200;

// 初始化
onMounted(() => {
  fetchMessages();
});

// 获取消息列表
const fetchMessages = async () => {
  try {
    const data = await getUserMessages();
    // 直接使用API返回的数据（已在getUserMessages中确保是数组）
    if (Array.isArray(data)) {
      messages.value = data;
    } else {
      messages.value = [];
    }
  } catch (error) {
    showError('获取消息失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 刷新消息
const refreshMessages = () => {
  fetchMessages();
  showSuccess('消息已刷新');
};



// 查看消息详情
const viewMessage = (message) => {
  currentMessage.value = message;
  dialogVisible.value = true;
  
  // 自动标记为已读
  if (message.status === 'unread') {
    markAsRead();
  }
};

// 标记为已读
const markAsRead = async () => {
  if (!currentMessage.value) return;
  
  try {
    await updateMessageStatus(currentMessage.value.message_id, {
      status: 'read'
    });
    
    // 更新本地数据
    currentMessage.value.status = 'read';
    const index = messages.value.findIndex(msg => msg.message_id === currentMessage.value.message_id);
    if (index !== -1) {
      messages.value[index].status = 'read';
    }
    
    showSuccess('消息已标记为已读');
  } catch (error) {
    showError('标记已读失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 全部已读
const markAllAsRead = async () => {
  const unreadMessages = messages.value.filter(msg => msg.status === 'unread');
  if (unreadMessages.length === 0) {
    showInfo('没有未读消息');
    return;
  }
  
  try {
    // 批量标记为已读
    for (const msg of unreadMessages) {
      await updateMessageStatus(msg.message_id, {
        status: 'read'
      });
      // 更新本地数据
      msg.status = 'read';
    }
    
    showSuccess('全部消息已标记为已读');
  } catch (error) {
    showError('批量标记已读失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 删除消息
const deleteMessage = async (id) => {
  try {
    await deleteMessageAPI(id);
    // 更新本地数据
    messages.value = messages.value.filter(msg => msg.message_id !== id);
    showSuccess('消息已删除');
  } catch (error) {
    showError('删除消息失败：' + (error.response?.data?.message || error.message || error));
  }
};

// 行点击事件
const handleRowClick = (row) => {
  viewMessage(row);
};

// 打开发送消息对话框
const openSendDialog = () => {
  sendDialogVisible.value = true;
};

// 关闭发送消息对话框
const closeSendDialog = () => {
  sendDialogVisible.value = false;
  resetForm();
};

// 重置表单
const resetForm = () => {
  receiverId.value = '';
  messageContent.value = '';
  contentLength.value = 0;
};

// 更新内容长度
const updateContentLength = () => {
  contentLength.value = messageContent.value.length;
};

// 提交发送消息
const submitSendMessage = async () => {
  // 表单验证
  if (!receiverId.value.trim()) {
    showError('请输入接收者ID');
    return;
  }
  
  if (!messageContent.value.trim()) {
    showError('请输入消息内容');
    return;
  }
  
  if (messageContent.value.length > maxContentLength) {
    showError(`消息内容不能超过${maxContentLength}个字符`);
    return;
  }
  
  try {
    // 从本地存储获取当前用户ID
    const userInfo = localStorage.getItem('userInfo');
    if (!userInfo) {
      showError('用户未登录');
      return;
    }
    
    const userId = JSON.parse(userInfo).user_id;
    
    // 发送消息
    await sendMessage({
      sender_id: userId,
      receiver_id: receiverId.value,
      content: messageContent.value
    });
    
    showSuccess('消息发送成功');
    closeSendDialog();
    
    // 刷新消息列表
    fetchMessages();
  } catch (error) {
    showError('发送消息失败：' + (error.response?.data?.message || error.message || error));
  }
};
</script>

<style scoped>
.teacher-message {
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
}

.message-actions {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}

.unread-message {
  font-weight: bold;
  color: #409eff;
}

.message-detail {
  padding: 10px 0;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>