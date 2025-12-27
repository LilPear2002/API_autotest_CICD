import sqlite3
import os
from utils.yaml_util import YamlUtil


class DBUtil:

    def __init__(self):
        config = YamlUtil.read_config()
        relative_path = config['env']['db_path'] # 读取出来的现在是 "flask_app/instance/app.db"
        
        # --- 核心修改：动态计算绝对路径 ---
        
        # 1. 找到 api_test 的根目录 (YamlUtil.ROOT_PATH 指向的是 api_test 文件夹)
        test_root = YamlUtil.ROOT_PATH
        
        # 2. 找到整个仓库的项目根目录 (即 api_test 的上一级)
        # 你的 flask_app 和 api_test 是平级的，所以要往上走一层
        project_root = os.path.dirname(test_root)
        
        # 3. 拼接出数据库的真实绝对路径 (兼容 Windows 和 Linux)
        self.db_path = os.path.join(project_root, relative_path)
        
        # -------------------------------
        
        print(f"正在尝试连接数据库，路径: {self.db_path}") # 方便调试看路径对不对

        if not os.path.exists(self.db_path):
            # 如果还找不到，打印一下当前目录结构，帮我们找原因
            print(f"当前项目根目录下的文件: {os.listdir(project_root)}")
            raise FileNotFoundError(f"数据库文件未找到: {self.db_path}")

    def query_one(self, sql):
        """
        查询单条记录
        :return: 字典格式 {'id': 1, 'username': 'test'}
        """
        conn = sqlite3.connect(self.db_path)

        # 关键点：设置 row_factory，让查询结果返回字典而不是元组 (Tuple)
        # 这样我们在断言时可以用 res['username']，可读性更强
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            row = cursor.fetchone()  # 获取一条

            # 将 sqlite3.Row 对象转为普通字典
            return dict(row) if row else None
        except Exception as e:
            print(f"SQL执行报错: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    def query_all(self, sql):
        """查询多条记录"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            # 转为列表套字典
            return [dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"SQL执行报错: {e}")
            return []
        finally:
            cursor.close()
            conn.close()


# 调试代码
if __name__ == '__main__':
    # 你可以先在 Flask 里注册一个用户 'testuser'，然后运行这个文件试试
    db = DBUtil()
    user = db.query_one("SELECT * FROM user WHERE username='testuser'")
    print(user)