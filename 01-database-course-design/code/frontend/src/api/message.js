import request from './index';

// 获取消息列表
export function getMessages(params) {
  return request.get('/messages/', { params });
}

// 发送消息
export function sendMessage(data) {
  return request.post('/messages/', data);
}

// 获取消息详情
export function getMessageDetail(id) {
  return request.get(`/messages/${id}/`);
}

// 获取当前用户的消息列表
export function getUserMessages() {
  // 从本地存储获取当前用户ID
  const userInfo = localStorage.getItem('userInfo');
  if (!userInfo) return Promise.reject(new Error('用户未登录'));
  
  const userId = JSON.parse(userInfo).user_id;
  
  // 调用API并确保返回的是消息数组
  return request.get(`/messages/user/${userId}/`).then(response => {
    console.log('API返回原始数据:', response);
    
    // 处理不同的响应格式
    let messages = response;
    
    // 如果响应包含value字段（OData格式）
    if (messages && typeof messages === 'object' && 'value' in messages) {
      messages = messages.value;
    }
    
    // 确保返回的是数组
    if (Array.isArray(messages)) {
      console.log('返回消息数组，长度:', messages.length);
      return messages;
    } else {
      console.error('返回的数据不是数组:', messages);
      return [];
    }
  });
}

// 更新消息状态（标记为已读）
export function updateMessageStatus(id, data) {
  return request.put(`/messages/${id}/`, data);
}

// 删除消息
export function deleteMessage(id) {
  return request.delete(`/messages/${id}/`);
}
