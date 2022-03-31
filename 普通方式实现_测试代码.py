import unittest
import requests


# python 中处理JSON 数据, 根据 key 获取对应值, 使用 json对象.get(key) 获取对应值
# assertEqual, assertIn
class TestIHRMLogin(unittest.TestCase):
    # 添加测试方法
    # 登录成功
    def test01_login_ok(self):
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "13800000002", "password": "123456"}
                             )
        print(resp.json())
        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(10000, resp.json().get("code"))
        self.assertIn("操作", resp.json().get("message"))
        self.assertEqual(True, resp.json().get("success"))


    # 手机号为空
    def test02_login_phone_empty(self):
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "", "password": "123456"}
                             )
        print(resp.json())

        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(20001, resp.json().get("code"))
        self.assertEqual("用户名或密码错误", resp.json().get("message"))
        self.assertEqual(False, resp.json().get("success"))

    # 密码错误
    def test03_login_password_error(self):
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "13800000002", "password": "123456789"}
                             )
        print(resp.json())

        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(20001, resp.json().get("code"))
        self.assertEqual("用户名或密码错误", resp.json().get("message"))
        self.assertEqual(False, resp.json().get("success"))
