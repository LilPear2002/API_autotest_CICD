import os
import pytest
import allure
from common.request_util import RequestUtil
from utils.yaml_util import YamlUtil


@allure.epic("Flask商城接口测试")
@allure.feature("文件管理模块")
class TestUpload:
    data_list = YamlUtil.read_test_data("upload_data.yaml")
    # 获取项目根目录，方便拼接文件路径
    root_path = YamlUtil.ROOT_PATH

    @allure.story("文件上传接口")
    @pytest.mark.parametrize("case_info", data_list)
    def test_upload(self, case_info):
        url = case_info['request']['url']
        method = case_info['request']['method']
        file_name = case_info['request']['file_name']
        file_type = case_info['request']['file_type']

        # --- 1. 拼接文件的绝对路径 ---
        # 假设文件放在 resources 目录下
        file_path = os.path.join(self.root_path, "resources", file_name)

        # --- 2. 核心：构建 files 参数 ---
        # 语法: files = {'参数名': ('文件名', open(文件路径, 'rb'), 'Content-Type')}
        # 'rb' 是以二进制只读模式打开，这非常重要！
        if os.path.exists(file_path):
            file_data = open(file_path, 'rb')
            files = {
                "file": (file_name, file_data, file_type)
            }
        else:
            raise FileNotFoundError(f"测试文件不存在: {file_path}")

        try:
            # --- 3. 发送请求 ---
            # 注意：上传文件用 files 参数，不用 json 参数
            # RequestUtil 的 send_request 需要能接收 **kwargs
            req = RequestUtil()
            res = req.send_request(method=method, url=url, files=files)
            result = res.json()

            # --- 4. 断言 ---
            assert res.status_code == case_info['validate']['status_code']
            assert result['message'] == case_info['validate']['message']

        finally:
            # --- 5. 必须关闭文件流 ---
            # 否则文件会被 Python 占用，导致无法删除或移动
            file_data.close()