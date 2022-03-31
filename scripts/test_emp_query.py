import logging
import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.db_util import DBUtil
from common.get_header import get_header
from common.logging_use import init_log_config
from config import BASE_DIR, EMP_ID


class TestEmpQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()
        init_log_config(BASE_DIR + "/log/ihrm_qery.log")

    def setUp(self) -> None:
        # 测试查询接口前, 插入一个员工id
        DBUtil.uid_db(f"insert into bs_user(id,mobile,username) values({EMP_ID},'13771860987','test1');")

    def tearDown(self) -> None:
        DBUtil.uid_db(f"delete from bs_user where id = {EMP_ID};")


    # 测试 查询员工
    def test01_query_emp(self):
        resp = IhrmEmpCURD.query_emp(self.header, EMP_ID)
        # logging.info(f"查询员工成功: {resp.json()}")
        # print 调试方便, 发布上线换成 logging
        print(resp.json())
