import unittest

import jsonschema

from api.ihrm_login_api import IhrmLoginApi


class TestIhrmLoginParams(unittest.TestCase):
    # 测试登录成功
    def test_login(self):
        req_data = {"mobile": "13800000002", "password": "123456"}
        # 如果读取 json 文件,没有截取 desc,那么这里可以打印出描述信息.
        # 数据
        resp = IhrmLoginApi.testIhrmLogin(req_data)
        print(resp.json())
        # 校验规则
        # 根据接口的返回值,编写全量字段校验规则
        # 使用全量字段校验响应的接口数据, 替换掉之前的断言
        schema = {
            "type": "object",
            "properties": {
                "success": {
                    "const": True
                },
                "code": {
                    "const": 10000
                },
                "message": {
                    "pattern": "操作成功" # 包含操作成功即可
                },
                "data": {
                    "type": "string"
                }
            },
            "required": ["success", "code", "message", "data"]
        }
        # 调用 jsonschema.validate校验函数
        jsonschema.validate(instance=resp.json(), schema=schema)
        # 如果没有报错,就校验通过了
        # print(res)
        # 校验响应状态码 使用 断言
        self.assertEqual(200,resp.status_code)
