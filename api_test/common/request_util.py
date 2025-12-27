import allure
import requests
from common.logger_util import logger
from utils.extract_util import ExtractUtil
from utils.yaml_util import YamlUtil

class RequestUtil:

    sess = requests.Session()

    def send_request(self, method, url, **kwargs):
        """
        统一请求方法
        :param method: 请求方式 (get, post, put, delete)
        :param url: 接口路径 (不需要写 base_url，只需要写 /auth/login 这种)
        :param kwargs: 其他参数 (json, params, data, headers...)
        :return: 响应内容的文本或JSON
        """

        # 1.处理URL： 从配置文件读取Base URL 进行拼接
        # 读取config.yaml
        config = YamlUtil.read_config()
        base_url = config['env']['base_url']
        full_url = base_url + url

        # 添加token
        if "/auth/login" not in url and "/auth/register" not in url:
            token = ExtractUtil().read_extract_yaml("access_token")
            # 构造headers请求头
            headers = kwargs.get("headers", {}) # 获取传入的headers，若无则为空字典
            if token:
                headers.update({"Authorization": f"Bearer {token}"})
            kwargs["headers"] = headers # 赋值回去

        # 2.统一日志记录 请求前
        method = method.lower()
        logger.info("----------------------------------")
        logger.info(f"接口请求开始 >>>")
        logger.info(f"请求地址: {full_url}")
        logger.info(f"请求方式: {method}")

        allure.attach(
            f"URL: {full_url}\nMethod: {method}\nHeaders: {kwargs.get('headers')}\nBody: {kwargs.get('json')}",
            name="请求信息",
            attachment_type=allure.attachment_type.TEXT)

        if "headers" in kwargs:
            logger.info(f"请求头: {kwargs['headers']}")
        if "json" in kwargs:
            logger.info(f"请求体: {kwargs['json']}")
        if "params" in kwargs:
            logger.info(f"请求参数: {kwargs['params']}")
        if "files" in kwargs:
            # 打印文件字典的 keys (即参数名)
            logger.info(f"上传文件参数: {kwargs['files'].keys()}")

        res = None
        try:
            res = RequestUtil.sess.request(method=method, url=full_url, **kwargs)
            allure.attach(f"Status: {res.status_code}\nResponse: {res.text}",
                          name="响应信息",
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error(f"请求异常: {e}")
            return None

        # 统一日志记录 响应后
        logger.info(f"响应状态码: {res.status_code}")
        try:
            # 尝试解析 JSON，如果不是 JSON 可能会报错
            logger.info(f"响应内容: {res.json()}")
        except:
            logger.info(f"响应内容(Text): {res.text}")

        logger.info(f"接口请求结束 <<<")

        return res