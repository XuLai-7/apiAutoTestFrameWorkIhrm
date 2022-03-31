import unittest

import requests
from parameterized import parameterized

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util
from common.read_json_util import read_json_data
from config import BASE_DIR


class TestIhrmLoginParams(unittest.TestCase):
    # 通用测试方法 (实现参数化)
    # 测试登录成功
    # 方法只接受 [(),(),(), ...] 的数据
    @parameterized.expand(read_json_data(BASE_DIR+"/data/ihrm_login.json"))
    def test_login(self, desc, req_data, status_code, code, msg, success):
        # 组织请求数据
        # 调用自己封装的接口
        # 断言
        # 如果读取 json 文件,没有截取 desc,那么这里可以打印出描述信息.
        # print(desc)
        resp = IhrmLoginApi.testIhrmLogin(req_data)
        print(desc, ":", resp.json())
        # 调用通用断言方法, 传入预期结果, 根据实际结果进行 断言
        assert_util(self, resp, status_code, code, msg, success)
