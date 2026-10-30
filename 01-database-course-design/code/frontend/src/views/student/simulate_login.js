// 模拟登录脚本
// 在浏览器控制台运行此脚本以模拟登录状态

function simulateLogin(userId, username, role) {
    // 创建模拟用户信息
    const userInfo = {
        user_id: userId,
        username: username,
        role: role,
        // 可以添加更多模拟字段
        token: 'mock-token-' + Date.now()
    };
    
    // 保存到localStorage
    localStorage.setItem('userInfo', JSON.stringify(userInfo));
    localStorage.setItem('token', userInfo.token);
    
    console.log('=== 模拟登录成功 ===');
    console.log('用户ID:', userId);
    console.log('用户名:', username);
    console.log('角色:', role);
    console.log('保存到localStorage的用户信息:', userInfo);
    
    return userInfo;
}

function testMessageAPI(userId) {
    console.log('=== 测试消息API ===');
    console.log('用户ID:', userId);
    
    // 直接调用API
    fetch(`http://localhost:8000/api/messages/user/${userId}/`)
        .then(response => {
            console.log('API响应状态:', response.status);
            return response.json();
        })
        .then(data => {
            console.log('API响应数据:', data);
            console.log('消息数量:', data.value?.length || 0);
            
            if (data.value && data.value.length > 0) {
                console.log('第一条消息:', data.value[0]);
                console.log('发送时间:', data.value[0].send_time);
            }
        })
        .catch(error => {
            console.error('API调用失败:', error);
        });
}

function clearLocalStorage() {
    localStorage.removeItem('userInfo');
    localStorage.removeItem('token');
    console.log('=== 已清除localStorage ===');
}

// 导出函数以便在控制台使用
window.simulateLogin = simulateLogin;
window.testMessageAPI = testMessageAPI;
window.clearLocalStorage = clearLocalStorage;

console.log('=== 模拟登录脚本加载完成 ===');
console.log('可用函数:');
console.log('1. simulateLogin(userId, username, role) - 模拟登录');
console.log('2. testMessageAPI(userId) - 测试消息API');
console.log('3. clearLocalStorage() - 清除localStorage');
console.log('\n示例用法:');
console.log('simulateLogin("20250000001", "学生张三", "student")');
console.log('testMessageAPI("20250000001")');