import requests


class IhrmLoginApi(object):
    # 登录方法
    @classmethod
    def testIhrmLogin(cls, json_data):
        return requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json=json_data
                             )


if __name__ == '__main__':
    print(IhrmLoginApi.testIhrmLogin({"mobile": "13800000002", "password": "123456"}).json())
