import sqlite3
import os
from utils.yaml_util import YamlUtil


class DBUtil:

    def __init__(self):
        # 1. 从配置文件读取数据库路径
        config = YamlUtil.read_config()
        self.db_path = config['env']['db_path']

        # 检查文件是否存在，防止报错一脸懵
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"数据库文件未找到，请检查路径: {self.db_path}")

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