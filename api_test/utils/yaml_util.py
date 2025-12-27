import os
import yaml
from utils.debug_talk import DebugTalk


class YamlUtil:
    # 获取项目根目录
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def read_config():
        config_path = os.path.join(YamlUtil.ROOT_PATH, 'config', 'config.yaml')
        try:
            with open(config_path, encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"读取配置文件失败: {e}")
            return None

    @staticmethod
    def read_test_data(yaml_name):
        data_path = os.path.join(YamlUtil.ROOT_PATH, 'data', yaml_name)
        if not os.path.exists(data_path):
            print(f"文件不存在: {data_path}")
            return []

        try:
            with open(data_path, encoding='utf-8') as f:
                value = yaml.safe_load(f)
                # 热加载替换逻辑
                str_data = str(value)
                # 遍历DebugTalk中的所有方法
                obj = DebugTalk()
                # 获取所有非魔术方法
                for method in dir(obj):
                    if not method.startswith("__"):
                        # 构造占位符 例如${get_random_number()}
                        placeholder = "${" + method + "()}"
                        if placeholder in str_data:
                            func = getattr(obj, method)
                            real_value = func()
                            # 替换字符串
                            str_data = str_data.replace(placeholder, str(real_value))
                # eval有安全风险 不过在测试框架中可以内部使用
                return eval(str_data)
        except Exception as e:
            print(f"读取测试数据文件失败: {e}")
            return None

# # 简单的测试代码，运行该文件看看能不能打印出配置
if __name__ == '__main__':
    print(YamlUtil.read_config())
    # print(YamlUtil.read_test_data('login.yaml'))
