import os
import yaml

class ExtractUtil:
    # 获取项目根目录
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 定义临时文件 extract.yaml的路径
    EXTRACT_YAML_PATH = os.path.join(ROOT_PATH, 'temp', 'extract.yaml')

    def write_extract_yaml(self, data):
        """
        写入中间变量到 extract.yaml (追加模式 'a')
        :param data: 字典数据，例如 {"access_token": "eyJ..."}
        """
        with open(self.EXTRACT_YAML_PATH, mode='a', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True)

    def read_extract_yaml(self, key):
        """
        读取 extract.yaml 中的指定 key 的值
        :param key: 要读取的键
        :return: 对应的值，如果不存在则返回 None
        """
        try:
            with open(self.EXTRACT_YAML_PATH, mode='r', encoding='utf-8') as f:
                value = yaml.safe_load(f)
                return value.get(key)
        except Exception:
            return None

    def clear_extract_yaml(self):
        """
        清空 extract.yaml 文件内容
        """
        with open(self.EXTRACT_YAML_PATH, mode='w', encoding='utf-8') as f:
            f.truncate()