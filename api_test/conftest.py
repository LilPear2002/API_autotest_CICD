import pytest
from common.request_util import RequestUtil
from utils.yaml_util import YamlUtil
from utils.extract_util import ExtractUtil

@pytest.fixture(scope="session", autouse=True)
def excute_database_clear():
    ExtractUtil().clear_extract_yaml()
    print("测试前：清空 extract.yaml 文件内容")

@pytest.fixture(scope="session", autouse=True)
def login_finture():
    """
    全局登录 Fixture
    scope="session": 在整个测试会话只执行一次
    autouse=True: 自动使用该 Fixture，无需在测试用例中显式引用
    """
    print("\n--- 全局前置：开始执行登录 ---")
    # 直接读取登录数据
    data = {"username": "testuser", "password": "test123"}

    # 发送请求
    req = RequestUtil()
    res = req.send_request(method="post", url="/auth/login", json=data)
    result = res.json()

    # 提取token
    if res.status_code == 200 and "data" in result:
        token = result['data']['token']
        ExtractUtil().write_extract_yaml({"access_token": token})
        print(f"--- 全局登录成功，Token 已保存 ---")
    else:
        print(f"--- 全局登录失败: {result} ---")
