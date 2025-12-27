import pytest
import allure
from common.request_util import RequestUtil
from utils.yaml_util import YamlUtil
from common.db_util import DBUtil

@allure.epic("Flask商城接口测试")
@allure.feature("用户注册模块")
class TestRegister:

    data_list = YamlUtil.read_test_data('register_data.yaml')

    @allure.story("用户注册接口")
    @pytest.mark.parametrize("case_info", data_list)
    def test_register(self, case_info):
        url = case_info['request']['url']
        method = case_info['request']['method']
        json_data = case_info['request']['json']

        # 发送请求
        req = RequestUtil()
        res = req.send_request(method=method, url=url, json=json_data)
        result = res.json()

        # 断言验证结果
        assert res.status_code == case_info['validate']['status_code']
        assert case_info['validate']['message'] in result['message']

        # 数据库断言
        # 获取刚才请求中的用户名（注意：如果是热加载生成的，这里需要技巧）
        # 简化处理：我们在 register_data.yaml 里使用了热加载。
        # 在这里，json_data 已经是被 YamlUtil 替换过实际值的字典了，可以直接取！
        target_username = json_data['username']
        target_email = json_data['email']

        print(f"正在数据库中查询用户: {target_username}")
        sql = f"SELECT * FROM user WHERE username = '{target_username}'"

        db_res = DBUtil().query_one(sql)
        print(f"数据库查询结果: {db_res}")
        allure.attach(str(db_res), name="数据库查询结果", attachment_type=allure.attachment_type.TEXT)

        # 核心断言
        # A. 断言数据存在
        assert db_res is not None, "数据库断言失败：未查询到用户信息"
        # B. 断言关键字段一致 (API 入参与 DB 落库一致)
        assert db_res['username'] == target_username
        assert db_res['email'] == target_email
        assert db_res['is_active'] == 1