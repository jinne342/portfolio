import { ElMessage, ElMessageBox } from 'element-plus';

/**
 * 统一的错误提示函数
 * @param {string} message - 错误消息内容
 * @param {Object} options - 额外配置选项
 */
export function showError(message, options = {}) {
  ElMessage.error({
    message,
    duration: options.duration || 3000,
    ...options
  });
}

/**
 * 统一的成功提示函数
 * @param {string} message - 成功消息内容
 * @param {Object} options - 额外配置选项
 */
export function showSuccess(message, options = {}) {
  ElMessage.success({
    message,
    duration: options.duration || 2000,
    ...options
  });
}

/**
 * 统一的警告提示函数
 * @param {string} message - 警告消息内容
 * @param {Object} options - 额外配置选项
 */
export function showWarning(message, options = {}) {
  ElMessage.warning({
    message,
    duration: options.duration || 2500,
    ...options
  });
}

/**
 * 统一的信息提示函数
 * @param {string} message - 信息内容
 * @param {Object} options - 额外配置选项
 */
export function showInfo(message, options = {}) {
  ElMessage.info({
    message,
    duration: options.duration || 2000,
    ...options
  });
}

/**
 * 统一的确认对话框
 * @param {string} title - 对话框标题
 * @param {string} message - 对话框内容
 * @param {Object} options - 额外配置选项
 * @returns {Promise} - 返回Promise对象
 */
export function showConfirm(title, message, options = {}) {
  return ElMessageBox.confirm(message, title, {
    confirmButtonText: options.confirmButtonText || '确定',
    cancelButtonText: options.cancelButtonText || '取消',
    type: options.type || 'warning',
    ...options
  });
}

/**
 * 统一的提示对话框
 * @param {string} title - 对话框标题
 * @param {string} message - 对话框内容
 * @param {Object} options - 额外配置选项
 * @returns {Promise} - 返回Promise对象
 */
export function showAlert(title, message, options = {}) {
  return ElMessageBox.alert(message, title, {
    confirmButtonText: options.confirmButtonText || '确定',
    type: options.type || 'info',
    ...options
  });
}

/**
 * 统一的输入对话框
 * @param {string} title - 对话框标题
 * @param {string} message - 对话框内容
 * @param {Object} options - 额外配置选项
 * @returns {Promise} - 返回Promise对象
 */
export function showPrompt(title, message, options = {}) {
  return ElMessageBox.prompt(message, title, {
    confirmButtonText: options.confirmButtonText || '确定',
    cancelButtonText: options.cancelButtonText || '取消',
    inputPattern: options.inputPattern,
    inputErrorMessage: options.inputErrorMessage,
    ...options
  });
}
