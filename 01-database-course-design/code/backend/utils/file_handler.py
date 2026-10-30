import os
import shutil
from typing import Optional

# 默认本地存储路径
DEFAULT_STORAGE_PATH = 'D:\数学建模管理系统'

class FileHandler:
    def __init__(self, base_path: str = DEFAULT_STORAGE_PATH):
        self.base_path = base_path
        # 确保基础路径存在
        self._ensure_path_exists(self.base_path)
        
        # 创建子目录结构
        self.submission_path = os.path.join(self.base_path, 'submissions')
        self.problem_path = os.path.join(self.base_path, 'problems')
        self.certificate_path = os.path.join(self.base_path, 'certificates')
        self.file_resource_path = os.path.join(self.base_path, 'file_resources')
        
        # 确保所有子目录存在
        self._ensure_path_exists(self.submission_path)
        self._ensure_path_exists(self.problem_path)
        self._ensure_path_exists(self.certificate_path)
        self._ensure_path_exists(self.file_resource_path)
    
    def _ensure_path_exists(self, path: str):
        """确保路径存在，如果不存在则创建"""
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
    
    def save_file(self, file, file_type: str, file_name: Optional[str] = None) -> str:
        """
        保存文件到本地存储
        
        Args:
            file: 文件对象
            file_type: 文件类型 ('submission', 'problem', 'certificate', 'file_resource')
            file_name: 可选的文件名，如果不提供则使用原始文件名
            
        Returns:
            文件存储路径（相对于存储根目录）
        """
        # 确定存储目录
        if file_type == 'submission':
            storage_dir = self.submission_path
        elif file_type == 'problem':
            storage_dir = self.problem_path
        elif file_type == 'certificate':
            storage_dir = self.certificate_path
        elif file_type == 'file_resource':
            storage_dir = self.file_resource_path
        else:
            raise ValueError(f"不支持的文件类型: {file_type}")
        
        # 获取文件名
        if file_name:
            # 如果提供了文件名，使用它
            filename = file_name
        else:
            # 否则使用原始文件名
            filename = getattr(file, 'filename', None) or f'file_{os.getpid()}_{os.urandom(8).hex()}'
        
        # 确保文件名唯一
        unique_filename = filename
        counter = 1
        while os.path.exists(os.path.join(storage_dir, unique_filename)):
            name, ext = os.path.splitext(filename)
            unique_filename = f"{name}_{counter}{ext}"
            counter += 1
        
        # 保存文件
        file_path = os.path.join(storage_dir, unique_filename)
        
        if hasattr(file, 'save'):
            # Flask/Werkzeug文件对象
            file.save(file_path)
        elif hasattr(file, 'read'):
            # 通用文件对象
            with open(file_path, 'wb') as f:
                f.write(file.read())
        else:
            raise ValueError("不支持的文件对象类型")
        
        # 返回相对路径
        relative_path = os.path.relpath(file_path, self.base_path)
        return relative_path
    
    def get_file_path(self, relative_path: str) -> str:
        """
        获取文件的完整本地路径
        
        Args:
            relative_path: 相对于存储根目录的路径
            
        Returns:
            文件的完整本地路径
        """
        return os.path.join(self.base_path, relative_path)
    
    def delete_file(self, relative_path: str) -> bool:
        """
        删除文件
        
        Args:
            relative_path: 相对于存储根目录的路径
            
        Returns:
            如果文件删除成功返回True，否则返回False
        """
        file_path = self.get_file_path(relative_path)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                return True
            except Exception:
                return False
        return False
    
    def copy_file(self, source_path: str, target_path: str) -> bool:
        """
        复制文件
        
        Args:
            source_path: 源文件路径
            target_path: 目标文件路径
            
        Returns:
            如果文件复制成功返回True，否则返回False
        """
        try:
            shutil.copy2(source_path, target_path)
            return True
        except Exception:
            return False

# 创建全局文件处理器实例
file_handler = FileHandler()
