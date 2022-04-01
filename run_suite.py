"""生成测试报告"""
import logging

from common.logging_use import init_log_config
from config import BASE_DIR
from scripts.test_emp_add_params import TestEmpAddParams
from scripts.test_ihrm_login_params import TestIhrmLoginParams
from htmltestreport import HTMLTestReport

"""这个文件是整个项目的入口文件"""
"""初始化日志的配置信息"""
init_log_config(BASE_DIR+"/log/ihrm.log")


"""
1.创建测试套件实例
2.添加测试类, 组装测试用例
3.创建THMLTestReport 实例, runner
4. 调用 run(), 传入 suite
"""
import unittest

suite = unittest.TestSuite()
logging.info("测试创建套件实例, 创建成功!")
suite.addTest(unittest.makeSuite(TestEmpAddParams))
suite.addTest(unittest.makeSuite(TestIhrmLoginParams))

runner = HTMLTestReport("./report/ihrm.html", description="人力资源管理系统, 接口自动化测试 登录,添加员工模块", title="接口自动化测试")
runner.run(suite)
logging.info("测试报告生成成功!")

