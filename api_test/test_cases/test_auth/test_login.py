import pytest
import allure
from common.request_util import RequestUtil
from utils.yaml_util import YamlUtil
from utils.extract_util import ExtractUtil

@allure.epic("Flask商城接口测试")
@allure.feature("用户认证模块")
class TestLogin:

    # 读取测试数据
    data_list = YamlUtil.read_test_data('login_data.yaml')

    @allure.story("用户登录接口")
    @pytest.mark.parametrize("case_info", data_list)
    def test_login(self, case_info):
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

        # 提取token 接口依赖
        if result['code'] == 200:
            token = result['data']['token']

            ExtractUtil().write_extract_yaml({'access_token': token})
            print(f"提取的token已保存: {token[:10]}...")