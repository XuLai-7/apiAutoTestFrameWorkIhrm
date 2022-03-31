"""存放全局变量"""
# 全局手机号
import os.path

TEL = "13900087897"
EMP_ID="1231827498132"
# 全局项目目录名
# __file__ 获取本文件的绝对路径
# os.path.dirname(__file__) 可以提取除文件所在的目录
BASE_DIR = os.path.dirname(__file__)

if __name__ == '__main__':
    print(BASE_DIR)
    # C: / Users / 闲客 / Desktop / testE / apiAutoTestFrameWorkIhrm
