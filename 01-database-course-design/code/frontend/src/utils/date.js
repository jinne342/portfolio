/**
 * 格式化日期时间（专门针对API返回的日期格式）
 * @param {string|number|Date} dateTime - 日期时间对象、字符串或时间戳
 * @param {Object} options - 格式化选项
 * @returns {string} - 格式化后的日期时间字符串
 */
export function formatDateTime(dateTime, options = {}) {
  if (!dateTime) return '';
  try {
    let date;
    
    if (typeof dateTime === 'string') {
      // 移除微秒部分（API返回的格式如：2025-12-29T00:46:11.747000）
      const cleanedDate = dateTime.replace(/\.\d+$/, '');
      
      // 手动解析日期组件，避免浏览器兼容性问题
      const parts = cleanedDate.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})$/);
      if (parts) {
        const year = parseInt(parts[1], 10);
        const month = parseInt(parts[2], 10) - 1; // JavaScript月份从0开始
        const day = parseInt(parts[3], 10);
        const hours = parseInt(parts[4], 10);
        const minutes = parseInt(parts[5], 10);
        const seconds = parseInt(parts[6], 10);
        
        date = new Date(year, month, day, hours, minutes, seconds);
      } else {
        // 如果解析失败，尝试直接创建Date对象
        date = new Date(cleanedDate);
      }
    } else if (typeof dateTime === 'number') {
      // 处理时间戳（支持秒级和毫秒级）
      if (dateTime.toString().length === 10) {
        dateTime *= 1000; // 转换为毫秒级
      }
      date = new Date(dateTime);
    } else {
      // 处理Date对象
      date = new Date(dateTime);
    }
    
    if (isNaN(date.getTime())) {
      return '无效时间';
    }
    
    // 默认格式化选项
    const defaultOptions = {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    };
    
    return date.toLocaleString('zh-CN', { ...defaultOptions, ...options });
  } catch (error) {
    console.error('日期格式化错误:', error, '原始数据:', dateTime);
    return '无效时间';
  }
}

/**
 * 格式化日期（仅日期部分）
 * @param {string|number|Date} dateTime - 日期时间对象、字符串或时间戳
 * @returns {string} - 格式化后的日期字符串
 */
export function formatDate(dateTime) {
  return formatDateTime(dateTime, {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
}

/**
 * 格式化时间（仅时间部分）
 * @param {string|number|Date} dateTime - 日期时间对象、字符串或时间戳
 * @returns {string} - 格式化后的时间字符串
 */
export function formatTime(dateTime) {
  return formatDateTime(dateTime, {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  });
}
