import pytest
import allure
from common.request_util import RequestUtil
from utils.yaml_util import YamlUtil


@allure.epic("Flask商城交易系统")
@allure.feature("订单全链路测试")
class TestOrderFlow:
    # 读取数据
    data_list = YamlUtil.read_test_data("shop_flow_data.yaml")

    @allure.story("购物下单流程")
    @pytest.mark.parametrize("case_info", data_list)
    def test_shop_process(self, case_info):

        url = case_info['request']['url']
        method = case_info['request']['method']
        json_data = case_info['request'].get('json')

        # 发送请求 (RequestUtil 会自动带上 conftest 里登录好的 Token)
        req = RequestUtil()
        res = req.send_request(method=method, url=url, json=json_data)

        # 断言
        assert res.status_code == case_info['validate']['status_code']