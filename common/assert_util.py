"""定义通用断言方法"""


def assert_util(self, resp, status_code, code, msg, success):
    # 断言
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(code, resp.json().get("code"))
    self.assertIn(msg, resp.json().get("message"))
    self.assertEqual(success, resp.json().get("success"))
