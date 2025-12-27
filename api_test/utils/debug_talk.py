import random
from faker import Faker

# 初始化 Faker (设置为中文)
f = Faker(locale='zh_CN')


class DebugTalk:

    def get_random_number(self, min_val=1000, max_val=9999):
        """生成随机数"""
        return str(random.randint(int(min_val), int(max_val)))

    def get_random_email(self):
        """生成随机邮箱"""
        return f.email()

    def get_random_name(self):
        """生成随机姓名"""
        return f.name()