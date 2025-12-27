from common.request_util import RequestUtil


def test_demo():
    # 实例化请求工具
    req = RequestUtil()

    # 发送请求
    # 注意：这里不用写 http://localhost:5000/api，因为封装里已经拼接了
    res = req.send_request(method="get", url="/categories")

    # 简单的断言
    print("测试脚本打印结果:", res.json())


if __name__ == '__main__':
    test_demo()