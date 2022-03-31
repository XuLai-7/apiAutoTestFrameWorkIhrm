import logging
import unittest
from time import sleep

import requests
from parameterized import parameterized

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_header
from common.logging_use import init_log_config
from common.read_json_util import read_json_data
from config import TEL, BASE_DIR


# class TestEmpAdd(unittest.TestCase):
class TestEmpAddParams(unittest.TestCase):

    # 类属性
    header = None
    @classmethod
    def setUpClass(cls) -> None:
        # 使用 日志记录接口测试脚本运行情况
        # 初始化日志
        # init_log_config("../report/test1.log")
        #
        # resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
        #                      json={"mobile": "13800000002", "password": "123456"}
        #                      )
        # token = 'Bearer ' + resp.json().get('data')
        # print(token)
        # # 使用日志记录
        # logging.info(f"获取到的token: {token}")
        cls.header = get_header()

    def setUp(self) -> None:
        # 接口测试之前,先删一下指定的手机号
        # 格式化方式传参
        delete_sql = f"delete from bs_user where `mobile` ='{TEL}'"
        # print(delete_sql)
        # 使用日志记录
        logging.info(f"delete sql 语句: {delete_sql}")
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        # 一个接口测试方法执行之后, 再删一下指定的手机号
        # 格式化方式传参
        # 这里会依据手机号删除掉整条数据记录
        delete_sql = f"delete from bs_user where `mobile` ='{TEL}'"
        # print(delete_sql)
        # 使用日志记录
        logging.info(f"delete sql 语句: {delete_sql}")
        DBUtil.uid_db(delete_sql)

        """
            接口自动化测试框架实现
            1.普通方式实现
            2.接口对象层
            3.测试用例层
            4.参数化(非必须)
            
            参数化
            写数据到json文件 [{},{},{},...]
            读取json文件数据 [(),(),(),...]
            使用 parameterized 实现参数化
        """

    # 手机号定义为全局变量放到 config.py 文件中,变量名大写
    # 必选参数
    # 通用测试方法
    # 实现参数化,数据驱动
    @parameterized.expand(read_json_data(BASE_DIR+"/data/ihrm_add_emp.json"))
    def test_add_emp(self, desc, json_data, status_code, code, msg, success):
        # 准备数据
        # 调用封装的接口
        json_data = json_data
        # 使用的地方, 直接从类属性获取
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        # print(desc, ":", resp.json())
        # 使用日志记录
        # 这条测试数据的描述, 经过测试脚本的测试, 得到了怎样的响应结果
        logging.info(f"{desc} : {resp.json()}")
        # 断言
        assert_util(self, resp, status_code, code, msg, success)

    """
    # 组合参数
    def test02_add_emp(self):
        # 准备数据
        # 调用封装的接口
        json_data={"username": "cyj2", "mobile": TEL, "workNumber": "9004",
                                                 "formOfEmployment": "2"}
        resp = IhrmEmpCURD.add_emp(self.header,json_data )
        print("添加-组合", resp.json())
        # 断言
        assert_util(self, resp, 200, 10000, '操作', True)

    # 全部参数
    def test03_add_emp(self):
        # 准备数据
        # 调用封装的接口
        json_data = {"username": "wilson", "mobile": TEL, "timeOfEntry": "2022-03-28",
                                    "formOfEmployment": 1, "workNumber": "9763", "departmentName": "开发部",
                                    "departmentId": "1504873500798656512",
                                    "correctionTime": "2022-03-30T16:00:00.000Z"}
        resp = IhrmEmpCURD.add_emp(self.header,json_data
                                   )
        print("添加-全部", resp.json())
        # 断言
        assert_util(self, resp, 200, 10000, '操作', True)

        
             解决反复修改手机号
             解决思路:
                 接口测试前 (setup), 指定一个要使用过的手机号, 做删除 delete sql 实现(删的数据不存在, 不会报错,存在就删了)
                 测试添加员工接口, 使用这个手机号
                 测试添加员工接口后(teardown), 再次 删除 这个 手机号  delete sql  (避免垃圾数据)

         """
